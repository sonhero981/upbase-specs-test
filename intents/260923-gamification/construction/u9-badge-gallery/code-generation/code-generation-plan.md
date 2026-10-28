---
intent: 260923-gamification
unit: u9-badge-gallery
artifact: code-generation-plan
stage: 3.5 code-generation-plan
bolt: B10
version: 1.0
status: draft
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
consumes: functional-design v1.1 (entities, rules, functional-spec, traceability)
---
# Code-Generation Plan: U9 `u9-badge-gallery`

**FE focus.** Owner code FE: Nguyễn Hùng Sơn (lms-fe). Owner code BE: cuongdq (C-18 endpoint — ghi nhận Nhóm A). Monorepo NX; TypeScript; lms-fe. Nhánh WIP có skeleton tab Badges (ADR-015).

Tổng ước tính FE: **1.5 ngày công** (Sơn).

> ⚠️ **Chặn trước khi bắt đầu code**:
> - OQ-B10-1: xác nhận route navigate từ GamificationPage sang My Profile tab Badges
> - OQ-B10-3: xác nhận path `DEFAULT_BADGE_IMAGE` trong lms-fe

---

## Nhóm A — BE: C-18 endpoint (cuongdq, ghi nhận)

### Bước A1 — GET /lms/api/v1/gamification/me/badges (C-18)
- Trả `MyBadgesDto`: mảng `badge_types` (chỉ loại đang bật — server-side filter BR-9.5)
- Mỗi `BadgeTypeRow`: `type`, `earned_count`, `total`, mảng `badges` (8 mốc)
- Mỗi `BadgeItem`: `id`, `milestone`, `name`, `description | null`, `image_url | null`, `is_earned`
- 404|630012 khi Badges tắt hoặc Test Account (BR-4.4, BR-4.5)
- Badges sorted by milestone tăng dần (server-side)

---

## Nhóm B — FE: Types + API Client (Sơn, ~0.25 ngày)

### Bước B1 — Types
**File**: `libs/api/gamification/src/lib/types/badges-learner.types.ts` (tạo mới)

```typescript
export type BadgeTypeKind = 'CHECKIN' | 'ACTIVITY' | 'TEST' | 'COURSE';

export interface BadgeItemDto {
  id: string;
  milestone: number;
  name: string;
  description: string | null;
  image_url: string | null;
  is_earned: boolean;
}

export interface BadgeTypeRowDto {
  type: BadgeTypeKind;
  earned_count: number;
  total: number;
  badges: BadgeItemDto[];
}

export interface MyBadgesDto {
  badge_types: BadgeTypeRowDto[];
}
```

### Bước B2 — API client
**File**: `libs/api/gamification/src/lib/lms-gamification.api.ts` (sửa — thêm vào file B04)

```typescript
async getMyBadges(): Promise<MyBadgesDto> {
  const res = await this.http.get('/lms/api/v1/gamification/me/badges');
  return res.data;
}
```

---

## Nhóm C — FE: State Management (Sơn, ~0.25 ngày)

### Bước C1 — useBadgeGallery hook
**File**: `libs/lms-gamification/src/lib/hooks/useBadgeGallery.ts` (tạo mới)

```typescript
export function useBadgeGallery() {
  // Dùng React Query hoặc in-memory cache (BR4.11 + BR4.7):
  // - staleTime: Infinity trong session → không re-fetch khi chuyển tab
  // - gcTime/cacheTime: 0 khi unmount component (hết phiên) → re-fetch khi reload
  const { data, isLoading, error, refetch } = useQuery({
    queryKey: ['gamification', 'my-badges'],
    queryFn: () => api.getMyBadges(),
    staleTime: Infinity,   // cache suốt phiên (BR4.11)
    retry: 1,
  });

  return {
    badgeTypes: data?.badge_types ?? [],
    loading: isLoading,
    error: !!error,
    retry: refetch,
  };
}
```

---

## Nhóm D — FE: BadgeGallery + Components (Sơn, ~0.75 ngày)

### Bước D1 — BadgeGallery (tab Badges trong My Profile)
**File**: `apps/lms/src/features/profile/tabs/BadgesTab.tsx` (sửa skeleton WIP)

> ⚠️ Cần OQ-B10-1 (route param) trước khi code phần activate tab.

```
BadgesTab
  ├── WF-1: Check features.badges từ LmsGamificationVisibility (context B04)
  │     └─ false → return null (ẩn tab — BR-4.4)
  ├── useBadgeGallery() → loading / error / data
  │     ├─ loading → <SkeletonGallery /> (BR4.12)
  │     └─ error → <InlineError onRetry={retry} /> (BR4.12, TC-518, TC-519)
  └─ data → <BadgeGallery badgeTypes={badgeTypes} />
```

### Bước D2 — BadgeGallery component
**File**: `libs/lms-gamification/src/lib/components/BadgeGallery.tsx` (tạo mới)

```typescript
const TYPE_LABELS: Record<BadgeTypeKind, string> = {
  CHECKIN: 'Check-in',
  ACTIVITY: 'Activity',
  TEST: 'Test',
  COURSE: 'Course',
};

// Render:
// badge_types.map(row => (
//   <BadgeSection key={row.type} row={row} />
// ))
```

### Bước D3 — BadgeSection component
**File**: `libs/lms-gamification/src/lib/components/BadgeSection.tsx` (tạo mới)

```typescript
interface BadgeSectionProps { row: BadgeTypeRowDto }

// Header: `{TYPE_LABELS[row.type]} Badges ({row.earned_count}/{row.total})` (BR4.13, TC-503)
// Grid: CSS grid 5 cột desktop, responsive collapse (BR4.13, OQ-B10-4)
// row.badges.map(badge => <BadgeCard key={badge.id} badge={badge} />)
```

### Bước D4 — BadgeCard component
**File**: `libs/lms-gamification/src/lib/components/BadgeCard.tsx` (tạo mới)

```typescript
interface BadgeCardProps { badge: BadgeItemDto }

const MILESTONE_UNITS: Record<BadgeTypeKind, string> = {
  CHECKIN: 'check-in days',
  ACTIVITY: 'activities',
  TEST: 'passed tests',
  COURSE: 'completed courses',
};
```

State:
- `is_earned = true`: ảnh màu, opacity 100% (BR-4.2, TC-504)
- `is_earned = false`: CSS `filter: grayscale(100%) opacity(0.4)` (BR-4.2, TC-505)
- Tên badge: luôn hiện dưới ảnh (BR4.15, TC-506)
- Hover tooltip (BR4.14, TC-507, TC-508):
  - `{badge.milestone} {MILESTONE_UNITS[type]}`
  - Nếu `badge.description != null`: thêm dòng mô tả (TC-509)

**Fallback ảnh (BR-1.7, OQ-B10-3)**:
```typescript
// Cần OQ-B10-3 để điền path
const DEFAULT_BADGE_IMAGE = '/assets/badges/default.png'; // ← xác nhận với tech lead
<img
  src={badge.image_url ?? DEFAULT_BADGE_IMAGE}
  onError={(e) => { e.currentTarget.src = DEFAULT_BADGE_IMAGE; }}
  alt={badge.name}
/>
```

---

## Nhóm E — FE: Skeleton + Error Components (Sơn, ~0.25 ngày)

### Bước E1 — SkeletonGallery (inline trong file BadgeGallery hoặc riêng)

```
4 skeleton sections:
  mỗi section: 1 placeholder header + 8 placeholder card (BR4.12)
```

### Bước E2 — InlineError component (dùng lại nếu lms-fe đã có)

```typescript
<div>
  <p>Failed to load badges.</p>
  <button onClick={onRetry}>Retry</button>
</div>
```

---

## Nhóm F — Tests (Sơn, ~0.5 ngày)

### Bước F1 — Unit tests BadgesTab + components
**File**: `libs/lms-gamification/src/lib/components/__tests__/BadgeGallery.test.tsx`

| Test | TC |
|---|---|
| Navigate từ GamificationPage → tab active | TC-501 |
| Load thành công: 4 section, 8 badge mỗi loại | TC-502 |
| Header section format đúng | TC-503 |
| is_earned true → màu | TC-504 |
| is_earned false → grayscale | TC-505 |
| Tên badge hiện cả earned + locked | TC-506 |
| Hover earned → tooltip milestone | TC-507 |
| Hover locked → tooltip milestone (không bị chặn) | TC-508 |
| description != null → tooltip 2 dòng | TC-509 |
| Thứ tự badge: milestone tăng | TC-510 |
| Loại 0 earned → 8 card grayscale, header (0/8) | TC-511 |
| Ảnh 404 → fallback DEFAULT_BADGE_IMAGE | TC-512 |
| Loại tắt → section ẩn (server không trả) | TC-513 |
| Badges tắt → tab ẩn | TC-514 |
| Test Account → tab ẩn | TC-515 |
| Không có write action trên tab | TC-516 |
| Loading: skeleton hiện | TC-517 |
| Network error → inline error + Retry | TC-518 |
| Retry → re-fetch thành công | TC-519 |

---

## Kiểm tra cắt ngang

| Rule | Bước |
|---|---|
| BR-4.1 hiện mọi badge | D2 map + F1 TC-502 |
| BR-4.2 earned/locked visual | D4 CSS + F1 TC-504,505 |
| BR-4.4 tab ẩn khi Badges tắt | D1 check features + F1 TC-514 |
| BR-4.7 + BR4.11 cache in-session | C1 React Query staleTime=Infinity + F1 (spy gọi API 1 lần) |
| BR4.12 skeleton + error | E1 + E2 + F1 TC-517,518,519 |
| BR4.13 grid 5 cột, header format | D3 CSS + label + F1 TC-503 |
| BR4.14 tooltip hover | D4 hover handler + F1 TC-507,508,509 |
| BR4.15 tên badge luôn hiện | D4 name + F1 TC-506 |
| BR4.16 navigation entry | D1 tab param + F1 TC-501 |
| BR-1.7 ảnh fallback | D4 onError + F1 TC-512 |

---

## Tóm tắt tiến độ FE

| Nhóm | Nội dung | Ước SP |
|---|---|---|
| B | Types + API client | 0.25 ngày |
| C | useBadgeGallery hook | 0.25 ngày |
| D | 4 components (BadgesTab, Gallery, Section, Card) | 0.75 ngày |
| E | Skeleton + Error | 0.25 ngày |
| F | Tests 19 TC | 0.5 ngày |
| **Tổng FE** | | **2 ngày** |

BE (cuongdq): C-18 endpoint ~1 ngày (theo assignment).

**Ghi chú**: Sơn có thể bắt đầu B, C, D2-D3 ngay. D1 (tab activate) và D4 (DEFAULT_BADGE_IMAGE) chờ OQ-B10-1 và OQ-B10-3 có câu trả lời.
