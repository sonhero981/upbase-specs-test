---
intent: <slug>
unit: <unit-name>
artifact: ui-map
version: 0.1
status: draft
ui_map_status: Provisional | Final
---
# UI Map: <unit-name>

Input bắt buộc của `/ui-gate build`. Trạng thái **Provisional** (chưa có Figma node: `/ui-gate review` bỏ so pixel, chỉ audit) → **Final** (đủ node).
Nguồn hành vi: `../functional-design/frontend-components.md`. Bỏ section của repo Unit không chạm.

## <repo FE thứ nhất>
Theo `.claude/commands/ui-gate.md` của repo đó; reuse `.claude/inventory/*` trước khi tạo mới. (section một repo FE)

### UI-1 Screen catalog
| screen-slug | App | Route | Figma desktop / tablet / mobile | Class |
|---|---|---|---|---|

### UI-2 Shared components
| Component | Used in | Reuse / New | Path |
|---|---|---|---|

### UI-3 New components
| Tên | Props API | Variants | Vì sao wrapper có sẵn không đủ |
|---|---|---|---|

### UI-4 State coverage
| Screen | default | loading | empty | error | disabled |
|---|---|---|---|---|---|

### UI-5 Interactions
| Screen | Trigger | Event | Action |
|---|---|---|---|

### UI-6 Forms
| Screen | Field | Validation (zod) | Submit → contract |
|---|---|---|---|

### UI-7 Animation
| Element | Duration | Easing |
|---|---|---|

### UI-8 Token deviations
| Figma variable | Extend config / align token | Đã duyệt |
|---|---|---|

### UI-9 Assets
| Asset | Có sẵn trong `@lms/assets` / cần export |
|---|---|

## <repo FE thứ hai>
Theo `.claude/commands/ui-gate.md` của repo đó; API qua `XxxAPI` + `useFeature()`; file < 300 dòng; nêu ảnh hưởng white-label.
Đủ UI-1 → UI-9 như trên; UI-6 validation zod + `HookForm*`; UI-8 SCSS var / antd token; UI-9 `@ops/assets`.
