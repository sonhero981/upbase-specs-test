---
intent: 260923-gamification
unit: u5-learner-home
artifact: code-generation-plan
stage: 3.5 code-generation-plan
bolt: B04
version: 1.0
status: draft
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
consumes: functional-design v1.1 (entities, rules, functional-spec, traceability)
---
# Code-Generation Plan: U5 `u5-learner-home`

**FE focus.** Owner code FE: Nguyễn Hùng Sơn (lms-fe). Owner code BE: cuongdq (lms-be — Nhóm A ghi nhận, không do plan này điều phối). Monorepo NX; TypeScript; lms-fe. Nhánh WIP lms-fe có skeleton GamificationPage sẵn (ADR-015).

Tổng ước tính FE: **2 ngày công** (Sơn).

---

## Nhóm A — BE: API endpoints (cuongdq, ghi nhận)

### Bước A1 — GET /lms/api/v1/gamification/me (C-13)
- LearnerGamificationController: endpoint trả GamificationMeDto
- Trả 404|630012 khi Gamification tắt, Visibility tắt, hoặc Test Account
- Field `features.*`: bật/tắt theo cấu hình tenant
- Field `points`, `streak`, `level`, `badges`: đọc từ UserStats

### Bước A2 — GET /lms/api/v1/gamification/rules (C-14)
- Trả `point_rules` (chỉ hành động đang bật) + `level_criteria` (chỉ tiêu chí đang chạy)
- Hành động tắt không có trong mảng → FE tự ẩn dòng tương ứng

### Bước A3 — GET /lms/api/v1/courses/my-learnings (C-15, additive)
- Thêm field `gamification: {points, level} | null` vào response hiện có
- `null` khi Gamification/Visibility tắt hoặc Test Account
- Backward-compatible: FE cũ bỏ qua field mới

---

## Nhóm B — FE: Types + API Client (Sơn, ~0.5 ngày)

### Bước B1 — Types: GamificationMe, GamificationRules, MyLearningGamification
**File**: `libs/api/gamification/src/lib/types/learner.types.ts` (tạo mới)

```typescript
export interface GamificationFeatures {
  points: boolean;
  checkin: boolean;
  badges: boolean;
  levels: boolean;
  leaderboard: boolean;
}

export interface GamificationMeDto {
  features: GamificationFeatures;
  points: number;
  streak: number;
  level: number;
  badges: number;
  timezone: string;
  today: string; // date string, dùng cho B06 (check-in)
  boards?: unknown[];       // US6, scope B04 render placeholder
  default_board?: unknown;  // US6
}

export interface PointRule {
  source: string; // ActionCode: CHECKIN, ACTIVITY, TEST, COURSE
  points: number;
  checkin_cap?: number; // chỉ có cho CHECKIN
}

export interface LevelCriteria {
  label: string; // "Every 3,000 points", "Every 5 completed courses"...
}

export interface GamificationRulesDto {
  point_rules: PointRule[];
  level_criteria: LevelCriteria[];
}

export interface MyLearningGamificationDto {
  points: number | null;
  level: number | null;
}
```

### Bước B2 — API client: LmsGamificationApiClient
**File**: `libs/api/gamification/src/lib/lms-gamification.api.ts` (tạo mới)

```typescript
export class LmsGamificationApiClient {
  async getMe(): Promise<GamificationMeDto> {
    const res = await this.http.get('/lms/api/v1/gamification/me');
    return res.data;
  }

  async getRules(): Promise<GamificationRulesDto> {
    const res = await this.http.get('/lms/api/v1/gamification/rules');
    return res.data;
  }
}
// MyLearnings: dùng API client hiện có của khoá học, đọc thêm field gamification
```

---

## Nhóm C — FE: State Management (Sơn, ~0.5 ngày)

### Bước C1 — LmsGamificationVisibility context/store
**File**: `libs/lms-gamification/src/lib/context/GamificationVisibilityContext.tsx` (tạo mới)

Đây là singleton context bọc toàn app shell lms-fe. Gọi `GET /me` một lần, chia sẻ kết quả:

```typescript
interface GamificationVisibilityState {
  status: 'loading' | 'available' | 'unavailable'; // unavailable: 404|630012
  features: GamificationFeatures | null;
  me: GamificationMeDto | null;
}
```

- Mount: gọi `getMe()` → set state
- 404|630012 → `status: 'unavailable'` → menu item ẩn (BR-1.1, BR-1.5)
- Không gọi lại khi chuyển route (BR1.11)
- Export hook: `useGamificationVisibility()`

### Bước C2 — useGamificationRules hook
**File**: `libs/lms-gamification/src/lib/hooks/useGamificationRules.ts` (tạo mới)

```typescript
export function useGamificationRules() {
  const [rules, setRules] = useState<GamificationRulesDto | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(false);
  const fetchedRef = useRef(false); // cache in-memory, không re-fetch (BR1.12)

  const fetchIfNeeded = useCallback(async () => {
    if (fetchedRef.current) return;
    fetchedRef.current = true;
    setLoading(true);
    try {
      const data = await api.getRules();
      setRules(data);
    } catch {
      setError(true);
    } finally {
      setLoading(false);
    }
  }, []);

  return { rules, loading, error, fetchIfNeeded };
}
```

---

## Nhóm D — FE: GamificationPage + Components (Sơn, ~0.75 ngày)

### Bước D1 — GamificationPage (sửa skeleton WIP)
**File**: `apps/lms/src/features/gamification/GamificationPage.tsx` (sửa skeleton từ nhánh WIP ADR-015)

```
GamificationPage
  ├── LmsGamificationVisibility (dùng context)
  ├── SummaryStrip (WF-2)
  │     ├── StreaksCard
  │     ├── PointsCard → mở HowToCollectPanel
  │     ├── BadgesCard → navigate My Profile Badges (B10)
  │     └── LevelCard  → mở HowToLevelUpPanel
  ├── HowToCollectPanel (lazy, WF-3)
  ├── HowToLevelUpPanel (lazy, WF-4)
  └── LeaderboardSection (placeholder OQ-B04-1 — render placeholder cho đến khi PO chốt scope)
```

Props: không có — đọc từ `useGamificationVisibility()`.

### Bước D2 — SummaryStrip + 4 Card
**File**: `libs/lms-gamification/src/lib/components/SummaryStrip.tsx`

Cards ẩn hiện theo `features.*` (BR-1.8):

```typescript
const { me, features } = useGamificationVisibility();

// Format helpers:
// Points: Intl.NumberFormat với dấu chấm nghìn (BR-1.6)
// Streaks: `{n} Streaks`  (BR1.14)
// Level:   `Level {n}`    (BR1.14)
// Badges:  `{n} Badges`   (BR1.14)
```

| Card | Hiện khi | Hover | Click |
|---|---|---|---|
| StreaksCard | `features.checkin` | Tooltip `Days in a row you've visited.` | — |
| PointsCard | `features.points` | `How to collect points?` | `setShowCollectPanel(true)` |
| BadgesCard | `features.badges` | `Go to badge gallery` | `navigate('/profile/badges')` |
| LevelCard | `features.levels` | `How to level up?` | `setShowLevelPanel(true)` |

Học viên mới (all 0): hiện đúng, Level hiện `Level 1` (TC-420).

### Bước D3 — HowToCollectPanel (lazy)
**File**: `libs/lms-gamification/src/lib/components/HowToCollectPanel.tsx`

```typescript
const { fetchIfNeeded, rules, loading, error } = useGamificationRules();
useEffect(() => { if (open) fetchIfNeeded(); }, [open]);
```

Render `point_rules` theo format BR1.15:
```typescript
function formatCheckinRow(rule: PointRule): { label: string; desc: string } {
  if (rule.points >= 40) {
    return { label: `${rule.points} pts`, desc: 'for visiting each day' };
  }
  return {
    label: `${rule.points}–${rule.checkin_cap} pts`,
    desc: `for visiting each day, +5 in a row, up to ${rule.checkin_cap}`,
  };
}
```

Nút "Achievement History":
- `features.points = true` → cuối panel này → navigate B08 (U7)
- `features.points = false AND features.levels = true` → nút chuyển vào HowToLevelUpPanel
- Cả hai false → không render nút (BR-1.8)

Skeleton khi loading. Thông báo lỗi khi fetch fail (không crash).

### Bước D4 — HowToLevelUpPanel (lazy, dùng rules cache)
**File**: `libs/lms-gamification/src/lib/components/HowToLevelUpPanel.tsx`

Render `level_criteria` — mỗi dòng bắt đầu bằng `Every` (BR1.16, BR-10.2):
```typescript
// level_criteria mảng đã chứa chuỗi chuẩn từ BE: "Every 3,000 points", etc.
// FE render trực tiếp — không tự ghép "Every"
// Mảng rỗng → hiện "No active level criteria" (edge case)
```

### Bước D5 — Menu guard + Route
**File**: `apps/lms/src/app/routes.tsx` (sửa)

```typescript
// Menu item "Gamification" chỉ hiện khi status = 'available'
const { status } = useGamificationVisibility();
// Route guard: status = 'unavailable' → redirect /not-found (BR-1.1)
```

---

## Nhóm E — FE: My Learning Widget (Sơn, ~0.25 ngày)

### Bước E1 — GamificationWidget component
**File**: `libs/lms-gamification/src/lib/components/GamificationWidget.tsx` (tạo mới)

```typescript
interface GamificationWidgetProps {
  gamification: MyLearningGamificationDto | null;
}

// gamification = null → return null (không render, BR1.13)
// Render: "{points} Points · Level {level}" với null-check per field (BR-1.8)
// Click → navigate('/gamification')
```

### Bước E2 — Kết nối vào MyLearningPage
**File**: `apps/lms/src/features/my-learning/MyLearningPage.tsx` (sửa)

- Đọc field `gamification` từ response `/courses/my-learnings` (C-15)
- Render `<GamificationWidget gamification={data.gamification} />` đầu màn, trước danh sách khoá
- Không thay đổi layout hiện có (BR US1-AC12)

---

## Nhóm F — Tests (Sơn, ~0.5 ngày)

### Bước F1 — Unit tests GamificationPage + components
**File**: `libs/lms-gamification/src/lib/components/__tests__/GamificationPage.test.tsx`

| Test | TC |
|---|---|
| Tải xong: 4 ô hiện đúng | TC-401, TC-404 |
| 404|630012: menu ẩn, route → not-found | TC-402, TC-403 |
| Hover ô Streaks → tooltip | TC-405 |
| Click Points → panel trượt | TC-406 |
| Panel check-in: format dòng + điểm | TC-407, TC-408 |
| Click Level → panel level-up | TC-409 |
| Panel level-up: "Every" mỗi dòng | TC-410 |
| Click Badges → navigate Badges | TC-411 |
| Click Streaks → không có hành động | TC-412 |
| ✕ đóng panel | TC-413 |
| My Learning widget: hiện + click | TC-414, TC-415 |
| features.points=false → ô Points ẩn | TC-416 |
| features.badges=false → ô Badges ẩn | TC-417 |
| features.levels=false → ô Level ẩn | TC-418 |
| Test Account: not-found | TC-419 |
| Học viên mới (all 0) | TC-420 |
| Gamification tắt → widget My Learning null | TC-421 |
| Points tắt → widget chỉ hiện Level | TC-422 |

---

## Kiểm tra cắt ngang

| Rule | Bước kiểm |
|---|---|
| BR-1.1 404|630012 → unavailable | C1 context status + D5 route guard + F1 TC-402,403 |
| BR-1.8 ẩn theo features.* | D2 SummaryStrip + E1 Widget + F1 TC-416–422 |
| BR1.11 GET /me một lần | C1 context singleton + F1 (mock đếm call) |
| BR1.12 GET /rules lazy + cache | C2 hook fetchedRef + F1 TC-406 (gọi 1 lần) |
| BR1.13 widget null-safe | E1 null check + F1 TC-421 |
| BR1.14 format 4 ô | D2 format helpers + F1 TC-404 |
| BR1.15 format check-in panel | D3 formatCheckinRow + F1 TC-407,408 |
| BR1.16 "Every" trong panel level | D4 render + F1 TC-410 |
| BR-1.6 dấu chấm nghìn | D2 Intl.NumberFormat + F1 TC-404 |

---

## Tóm tắt tiến độ FE

| Nhóm | Nội dung | Ước SP |
|---|---|---|
| B | Types + API client | 0.5 ngày |
| C | Context + hook state | 0.5 ngày |
| D | GamificationPage + 4 panel/component | 0.75 ngày |
| E | My Learning widget | 0.25 ngày |
| F | Tests 22 TC | 0.5 ngày |
| **Tổng FE** | | **2.5 ngày** |

BE (cuongdq): C-13, C-14, C-15 endpoints ~2 ngày (theo assignment lms-be).

**Ghi chú OQ-B04-1**: Leaderboard section. Plan hiện render placeholder. Sau khi PO chốt scope, update bước D1 trước khi merge.
