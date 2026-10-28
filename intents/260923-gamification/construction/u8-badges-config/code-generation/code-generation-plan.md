---
intent: 260923-gamification
unit: u8-badges-config
artifact: code-generation-plan
stage: 3.5 code-generation-plan
bolt: B09
version: 1.0
status: draft
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
consumes: functional-design v1.1 (entities, rules, functional-spec, traceability)
---
# Code-Generation Plan: U8 `u8-badges-config`

**FE focus.** Owner code FE: Nguyễn Hùng Sơn (ops-fe). Owner code BE: cuongdq (lms-be — các bước BE ghi nhận, không do plan này điều phối). Monorepo NX; TypeScript.

Tổng ước tính FE: **2 ngày công** (Sơn).

---

## Nhóm A — BE: Entities + Migration (cuongdq)

> Các bước này do cuongdq thực hiện ở `lms-be`. Ghi nhận ở đây để FE biết schema API sẽ có.

### Bước A1 — Migration: tạo bảng `gamification_badge_types` và `gamification_badges`
- File: `lms-be/src/migrations/<ts>_create_gamification_badges.ts`
- `gamification_badge_types`: `id`, `tenant_id`, `type VARCHAR(20)` (CHECKIN/ACTIVITY/TEST/COURSE), `is_enabled BOOLEAN DEFAULT false`, `created_at`, `updated_at`
- `gamification_badges`: `id`, `tenant_id`, `badge_type_id FK`, `milestone INTEGER`, `default_name VARCHAR(255)`, `name VARCHAR(255)`, `description TEXT NULL`, `image_resource_id UUID NULL FK resources`, `created_at`, `updated_at`
- Index: `(tenant_id, badge_type_id)` trên `gamification_badges`
- Seed riêng: 4 × 8 = 32 bản ghi mỗi tenant với tên/hình mặc định

### Bước A2 — Entity TypeORM: GamificationBadgeType + GamificationBadge
- `libs/database/src/lib/entities/gamification/gamification-badge-type.entity.ts`
- `libs/database/src/lib/entities/gamification/gamification-badge.entity.ts`
- Relation: BadgeType `@OneToMany` Badge, Badge `@ManyToOne` BadgeType

### Bước A3 — GamificationSetting: thêm field `badges_enabled`
- File hiện có: `libs/database/src/lib/entities/gamification/gamification-setting.entity.ts`
- Thêm `@Column({ default: false }) badgesEnabled: boolean`
- Migration additive: `ALTER TABLE gamification_settings ADD COLUMN badges_enabled BOOLEAN DEFAULT false`

### Bước A4 — GamificationSettingsOpsService: implement GET/PATCH /badges
- File: `apps/lms-be/src/modules/gamification/ops/gamification-settings-ops.service.ts`
- `getBadgesConfig(tenantId)`: trả `badges_enabled` + 4 badge_types + 8 mốc mỗi loại
- `updateBadgesConfig(tenantId, dto)`: PATCH `badges_enabled` hoặc `badge_type.is_enabled`
- `updateBadge(tenantId, badgeId, dto)`: PATCH `name`, `description`, `image_resource_id`
- Validate: PATCH milestone → throw `BusinessException(630004)`; name rỗng → trả `default_name`

### Bước A5 — BadgeBackfill job (A-04, BR-9.9)
- Khi bật `badges_enabled` hoặc bật badge_type: enqueue BackfillBadgesJob
- Trao huy hiệu cho học viên đủ điều kiện chưa được trao

---

## Nhóm B — FE: API Client + Types (Sơn, ~0.5 ngày)

### Bước B1 — Types: BadgeType, Badge, BadgesConfigResponse
**File**: `libs/api/gamification/src/lib/types/badges.types.ts` (tạo mới)

```typescript
export type BadgeTypeKind = 'CHECKIN' | 'ACTIVITY' | 'TEST' | 'COURSE';

export interface BadgeDto {
  id: string;
  milestone: number;
  defaultName: string;
  name: string;
  description: string | null;
  imageUrl: string | null;
}

export interface BadgeTypeDto {
  type: BadgeTypeKind;
  isEnabled: boolean;
  badges: BadgeDto[];
}

export interface BadgesConfigResponse {
  badgesEnabled: boolean;
  badgeTypes: BadgeTypeDto[];
}

export interface UpdateBadgesDto {
  badgesEnabled?: boolean;
  badgeType?: { type: BadgeTypeKind; isEnabled: boolean };
}

export interface UpdateBadgeDto {
  name?: string;
  description?: string | null;
  imageResourceId?: string;
}
```

### Bước B2 — API client: GamificationSettingsOpsApi (badges endpoints)
**File**: `libs/api/gamification/src/lib/gamification-settings-ops.api.ts` (sửa — thêm vào file hiện có của B01/B03)

```typescript
// thêm 3 method vào GamificationSettingsOpsApi class

async getBadgesConfig(): Promise<BadgesConfigResponse> {
  const res = await this.http.get('/ops/api/v1/gamification/badges');
  return res.data;
}

async updateBadgesConfig(dto: UpdateBadgesDto): Promise<BadgesConfigResponse> {
  const res = await this.http.patch('/ops/api/v1/gamification/badges', dto);
  return res.data;
}

async updateBadge(id: string, dto: UpdateBadgeDto): Promise<BadgeDto> {
  const res = await this.http.patch(`/ops/api/v1/gamification/badges/${id}`, dto);
  return res.data;
}
```

---

## Nhóm C — FE: GamificationSettingsPage khối Badges (Sơn, ~1 ngày)

### Bước C1 — BadgesBlock component (tạo mới)
**File**: `features/gamification/src/components/badges/BadgesBlock.tsx`

Trách nhiệm: render toàn bộ khối Badges (toggle Badges + 4 loại + 8 mốc mỗi loại).

```
BadgesBlock
  ├── toggle `badges_enabled` (BR-9.6, BR9.12)
  ├── cảnh báo cố định OQ-50 (luôn hiện)
  └── BadgeTypeSection × 4 (CHECKIN, ACTIVITY, TEST, COURSE)
        ├── toggle `is_enabled` (BR-9.5, BR9.12)
        ├── dòng "Awarded at ..." (BR9.14)
        └── BadgeRow × 8
              ├── milestone (chỉ đọc, BR-9.2)
              ├── BadgeImagePicker (BR9.13, WF-4)
              ├── ô tên (blur → PATCH, BR-9.3, BR9.12)
              └── ô mô tả (blur → PATCH, BR-9.3, BR9.12)
```

Props:
```typescript
interface BadgesBlockProps {
  tenantId: string;
}
```

State nội bộ:
```typescript
const [config, setConfig] = useState<BadgesConfigResponse | null>(null);
const [loading, setLoading] = useState(true);
const [error, setError] = useState<string | null>(null);
```

WF-1: `useEffect` → `getBadgesConfig()` → `setConfig`; lỗi mạng → skeleton + retry message.

### Bước C2 — BadgeTypeSection component (tạo mới)
**File**: `features/gamification/src/components/badges/BadgeTypeSection.tsx`

Props:
```typescript
interface BadgeTypeSectionProps {
  badgeType: BadgeTypeDto;
  globalEnabled: boolean; // badges_enabled toàn org
  onToggle: (type: BadgeTypeKind, isEnabled: boolean) => Promise<void>;
  onBadgeChange: (id: string, dto: UpdateBadgeDto) => Promise<void>;
}
```

- Toggle `is_enabled`: gọi `onToggle` → optimistic update → rollback nếu lỗi (BR9.12, TC-318)
- Dòng "Awarded at": `MILESTONE_LABELS[type]` map (BR9.14)
- 8 `BadgeRow` với `disabled={!badgeType.isEnabled}` (BR9.11)

```typescript
const MILESTONE_LABELS: Record<BadgeTypeKind, string> = {
  CHECKIN: 'Awarded at 4, 8, 16, 32, 64, 128, 256, 512 check-in days.',
  ACTIVITY: 'Awarded at 10, 25, 50, 100, 200, 400, 800, 1600 activities.',
  TEST: 'Awarded at 2, 4, 8, 16, 32, 64, 128, 256 passed tests.',
  COURSE: 'Awarded at 1, 2, 4, 8, 16, 32, 64, 128 completed courses.',
};
```

### Bước C3 — BadgeRow component (tạo mới)
**File**: `features/gamification/src/components/badges/BadgeRow.tsx`

Props:
```typescript
interface BadgeRowProps {
  badge: BadgeDto;
  disabled: boolean; // true khi loại đang tắt (BR9.11)
  onSave: (dto: UpdateBadgeDto) => Promise<void>;
}
```

- Milestone: `<span>{badge.milestone}</span>` — không có ô nhập (BR-9.2)
- Ô tên: `defaultValue={badge.name}`, `placeholder={badge.defaultName}`, `onBlur` → gọi `onSave({name: value || ''})` (BE trả defaultName nếu rỗng — BR-9.8, TC-309)
- Ô mô tả: `onBlur` → `onSave({description: value || null})` (TC-314)
- `disabled` prop áp vào tất cả input và button trong row (BR9.11, TC-315)

### Bước C4 — BadgeImagePicker component (tạo mới)
**File**: `features/gamification/src/components/badges/BadgeImagePicker.tsx`

Dùng lại `ModalUploadFile` (`libs/ui/src/base/upload-file/ModalUploadFile/ModalUploadFile.tsx:48`).

```typescript
interface BadgeImagePickerProps {
  currentImageUrl: string | null;
  badgeId: string;
  disabled: boolean;
  onSave: (dto: UpdateBadgeDto) => Promise<void>;
}
```

WF-4:
1. Hiện thumbnail `currentImageUrl` (fallback = ảnh mặc định nếu 404 — BR-1.7, TC-313)
2. Bấm "Chọn ảnh" → mở `ModalUploadFile`
3. Client validate định dạng + kích thước ≤ 1MB (BR9.13); lỗi → hiện thông báo, không gọi API
4. Upload `POST /lms/api/v1/resources/upload` qua `ModalUploadFile.tsx:48` → nhận `resource_id`
5. Gọi `onSave({imageResourceId: resource_id})` → `PATCH /badges/{id}`
6. Cập nhật thumbnail từ response

Validate client (BR9.13):
```typescript
const ALLOWED_TYPES = ['image/png', 'image/jpeg', 'image/webp', 'image/svg+xml'];
const MAX_SIZE_BYTES = 1 * 1024 * 1024; // 1MB

function validateImage(file: File): string | null {
  if (!ALLOWED_TYPES.includes(file.type)) return 'Định dạng không hợp lệ (.png/.jpg/.jpeg/.webp/.svg)';
  if (file.size > MAX_SIZE_BYTES) return 'Ảnh không được vượt quá 1MB';
  return null;
}
```

### Bước C5 — Kết nối vào GamificationSettingsPage
**File**: `features/gamification/src/pages/GamificationSettingsPage.tsx` (sửa — file hiện có B01)

- Import và render `<BadgesBlock tenantId={tenantId} />` bên dưới khối Points (B01/B03)
- Không shared state giữa Points và Badges — mỗi khối tự quản lý

---

## Nhóm D — FE: Auto-save handler + Error handling (Sơn, ~0.25 ngày)

### Bước D1 — useBadgesConfig hook (tạo mới)
**File**: `features/gamification/src/hooks/useBadgesConfig.ts`

Đóng gói toàn bộ state management và auto-save logic:

```typescript
export function useBadgesConfig(tenantId: string) {
  const [config, setConfig] = useState<BadgesConfigResponse | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const loadConfig = useCallback(async () => { /* WF-1 */ }, [tenantId]);

  const toggleBadges = useCallback(async (enabled: boolean) => {
    // Optimistic update → PATCH → rollback on error (BR9.12, TC-318)
  }, [config]);

  const toggleBadgeType = useCallback(async (type: BadgeTypeKind, enabled: boolean) => {
    // Optimistic update → PATCH → rollback (BR9.12)
  }, [config]);

  const saveBadge = useCallback(async (id: string, dto: UpdateBadgeDto) => {
    // PATCH /badges/{id} → update state from response (BR9.12, BR-9.8)
  }, []);

  return { config, loading, error, toggleBadges, toggleBadgeType, saveBadge, reload: loadConfig };
}
```

Rollback pattern (TC-318):
```typescript
const prevConfig = config;
setConfig(optimisticUpdate(config, ...));
try {
  const updated = await api.updateBadgesConfig(dto);
  setConfig(updated);
  showToast('Saved');
} catch {
  setConfig(prevConfig); // rollback
  showToast('Lỗi lưu, thử lại', 'error');
}
```

---

## Nhóm E — Tests (Sơn, ~0.25 ngày)

### Bước E1 — Unit tests BadgesBlock + hooks
**File**: `features/gamification/src/components/badges/__tests__/BadgesBlock.test.tsx`

| Test | TC |
|---|---|
| Tải xong: render 4 loại, 32 mốc | TC-301 |
| Tắt Badges: PATCH badges_enabled:false | TC-302 |
| Dòng "Awarded at" đúng format, không "every" | TC-305, TC-306 |
| Milestone không có ô nhập | TC-307 |
| Xoá trắng tên → ô về defaultName | TC-309 |
| Tên 256 ký tự → hiện lỗi 422|000405 | TC-310 |
| Validate ảnh sai định dạng/quá 1MB → không upload | TC-311, TC-312 |
| Image 404 → fallback mặc định | TC-313 |
| Xoá mô tả → PATCH description:null | TC-314 |
| Loại tắt → row disabled | TC-315 |
| Không có nút tạo/xoá | TC-316 |
| PATCH 500 → toggle rollback, toast lỗi | TC-318 |

### Bước E2 — Integration test: auto-save flow
**File**: `features/gamification/src/components/badges/__tests__/AutoSave.integration.test.tsx`

- Blur ô tên → PATCH gọi 1 lần (không gọi khi đang gõ) — TC-317
- Upload ảnh thành công → PATCH image_resource_id → thumbnail update — TC-311

---

## Kiểm tra cắt ngang

| Rule | Bước kiểm |
|---|---|
| BR9.11 Loại tắt → disabled | C2 props + C3 disabled + E1 TC-315 |
| BR9.12 Auto-save blur/toggle | D1 hook + E2 TC-317 |
| BR9.13 Định dạng/kích thước | C4 validateImage + E1 TC-311, TC-312 |
| BR9.14 Format "Awarded at" | C2 MILESTONE_LABELS + E1 TC-305, TC-306 |
| BR-9.2 Milestone chỉ đọc | C3 span-only + E1 TC-307 |
| BR-9.8 Xoá trắng tên | C3 onBlur + D1 saveBadge + E1 TC-309 |
| BR-1.7 Ảnh 404 fallback | C4 onError + E1 TC-313 |
| BR-14.11 Toggle rollback | D1 rollback pattern + E1 TC-318 |

---

## Tóm tắt tiến độ FE

| Nhóm | Nội dung | Ước SP |
|---|---|---|
| B | Types + API client | 0.5 ngày |
| C | 5 components + kết nối page | 1 ngày |
| D | useBadgesConfig hook | 0.25 ngày |
| E | Tests | 0.25 ngày |
| **Tổng FE** | | **2 ngày** |

BE (cuongdq): Migration + Entities + OpsService + BackfillJob ~3 ngày (theo assignment lms-be).
