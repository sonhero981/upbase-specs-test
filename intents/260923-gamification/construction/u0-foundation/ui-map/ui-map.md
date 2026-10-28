---
intent: 260923-gamification
unit: u0-foundation
artifact: ui-map
stage: 3.41 ui-map
version: 1.0
status: approved
ui_map_status: Provisional
approved_at: 2026-10-13 (FE lead, DEC-T12)
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
consumes: ../functional-design/frontend-components.md v1.0 · design/Gamification - Disable.png · design/Gamification - Enable - Setting.png (khối Gamification đầu trang) · ops-fe .claude/commands/ui-gate.md + .claude/inventory/* @1e01033bf
---
# UI Map: u0-foundation

Input của `/ui-gate build`. **Provisional**: chưa có link Figma (OQ-11), chỉ có ảnh `design/`; `/ui-gate review` bỏ so pixel, chỉ audit token, state, a11y. Popover, `Saved`, 403 dùng chuẩn (PO 2.43: không cần design riêng). Path "có sẵn" kiểm ở `origin/staging` 1e01033bf.

## lms-fe
Không có màn (ADR-006). Không chạy `/ui-gate`.

## ops-fe
Theo `E:\UP_BASE\ops-fe\.claude\commands\ui-gate.md`; API qua `GamificationAPI` + `useFeature()`; file < 300 dòng; antd token + SCSS module, không Tailwind.

**White-label**: `@ops/feature-gamification` vào `FEATURE_MODULE_MAP`, `FEATURE_FOLDER_MAP` (`scripts/generate-customer.js:33,51`); customer không khai thì module, route, menu biến mất.

### UI-1 Screen catalog
| screen-slug | App | Route | Figma desktop / tablet / mobile | Class |
|---|---|---|---|---|
| `gamification-settings` | ops-fe | `/gamification` | chưa có node · ảnh `design/Gamification - Disable.png` (tắt), khối đầu `design/Gamification - Enable - Setting.png` (bật) / — / — | MEDIUM (default, loading, error, no-access, view-only) |

### UI-2 Shared components
| Component | Used in | Reuse / New | Path |
|---|---|---|---|
| `PageLayouts` | gamification-settings | Reuse | `libs/ui/src/layout/page-layout/PageLayouts.tsx:169`, mẫu `features/cache/src/pages/index.tsx:9-40` |
| `HookFormSwitch` | gamification-settings | **Sửa**: thêm prop `disabled?: boolean` truyền vào `<input disabled>` | `libs/ui/src/base/switch/HookFormSwitch.tsx:6-33` |
| `Popconfirm` (antd) | gamification-settings | Reuse raw antd (wrapper `PopupConfirm` là Modal, `libs/ui/src/common/PopupConfirm.tsx:1`) | antd |
| `Result` (antd, `status='403'`) | no-access | Reuse raw antd; không dùng `AccessDeniedScreen` (nút gọi `logOut()`, `apps/ops-fe/src/components/access-denied/index.tsx:30`) | antd |
| `withAuthComponents` | gamification-settings | Reuse | `libs/HOC/src/with-auth-components.tsx:21` |
| `useHasPermission` | page, menu | Reuse | `libs/hooks/src/permission/useHasPermission.tsx:13-43` (superadmin qua, L29) |
| `toast` (`react-hot-toast`) | `Saved` | Reuse | mẫu `features/cache/src/components/table/CacheButton.tsx:8,35` |
| `Spin` (antd) / `ErrorMessage` | loading, error | Reuse | `libs/ui/src/common/index.ts:16` |

### UI-3 New components
| Tên | Props API | Variants | Vì sao wrapper có sẵn không đủ |
|---|---|---|---|
| `GamificationSettingsPage` | — (route element) | — | Trang mới của feature |
| `GeneralSettingsCard` | `settings: IGamificationSettings`, `canEdit: boolean`, `savingField: 'is_enabled' \| 'is_visible' \| null`, `onChange(field, next)` | view-only khi `canEdit=false` | Bố cục "tiêu đề + mô tả trái, công tắc phải" chưa có wrapper; đặt trong feature |
| `SwitchWithConfirm` | `checked`, `disabled`, `confirm?: { title, description, okText, cancelText }`, `onConfirm(next)` | có / không confirm | Gói `HookFormSwitch` + `Popconfirm`, hoàn tác giá trị khi Huỷ (FE-O3); đặt trong feature |

### UI-4 State coverage
| Screen | default | loading | empty | error | disabled |
|---|---|---|---|---|---|
| gamification-settings | `GeneralSettingsCard` theo bản ghi đã lưu | `Spin` thay thẻ khi C-01 lần đầu | Chỉ có quyền học viên: chỉ tiêu đề trang (FE-O1) | Thông báo lỗi + tải lại | Không quyền sửa: công tắc `disabled`; đang lưu: bỏ qua bấm công tắc đó; không quyền nào: `Result 403`, không gọi C-01 |

### UI-5 Interactions
| Screen | Trigger | Event | Action |
|---|---|---|---|
| gamification-settings | Mở route | mount | Không có quyền nào trong 3 → `Result 403`; có → `getSettings()` (C-01) |
| gamification-settings | Bật `Gamification` | switch on | `updateSetting({ is_enabled: true })` (C-02) |
| gamification-settings | Tắt `Gamification` | switch off | `Popconfirm` (chuỗi BR14.13) → `Turn off` gọi C-02 `{ is_enabled:false }`; `Cancel` → về bật, không gọi |
| gamification-settings | Bật `Visibility` khi `has_been_visible=false` | switch on | `Popconfirm` → `Show` gọi C-02 `{ is_visible:true }`; `Cancel` → về tắt |
| gamification-settings | Bật `Visibility` khi `has_been_visible=true` / tắt `Visibility` | switch | Gọi C-02 ngay |
| gamification-settings | C-02 200 | success | Giá trị đã lưu = `data` trả về; `toast.success('Saved')`; xoá `savingField` |
| gamification-settings | C-02 lỗi | error | `setValue` về giá trị đã lưu; toast lỗi do `@ops/service` (`libs/service/src/request.ts:215-220`); xoá `savingField` |
| Menu | Có ≥1 quyền | render sidebar | Mục "Gamification" (`libs/hooks/src/permission/useMenuData.tsx:1347-1432`); filter `:1434-1437` sửa theo từng item: Gamification theo 3 quyền, mục khác giữ `adminPermission` (plan OPS-6) |

### UI-6 Forms
| Screen | Field | Validation (zod) | Submit → contract |
|---|---|---|---|
| gamification-settings | `is_enabled`, `is_visible` (`HookFormSwitch`) | `z.object({ is_enabled: z.boolean(), is_visible: z.boolean() })` | Bấm là gửi một trường: `PATCH /gamification/settings` (C-02) |

### UI-7 Animation
| Element | Duration | Easing |
|---|---|---|
| Công tắc, Popconfirm, toast | Mặc định | Mặc định |

### UI-8 Token deviations
| Figma variable | Extend config / align token | Đã duyệt |
|---|---|---|
| Không có (Provisional) | Align class sẵn có: tiêu đề `fw-bold text-gray-900`, mô tả `text-gray-500`, nền `card` (như `access-denied/index.tsx:19-22`) | Không thêm token |

### UI-9 Assets
| Asset | Có sẵn / cần export |
|---|---|
| Icon menu Gamification | Chưa có; SVG inline như các mục khác (`useMenuData.tsx:1393-1405`) tới khi design chốt |

### Chuỗi UI
| Vị trí | Chuỗi |
|---|---|
| Breadcrumb / tiêu đề trang | `UpLMS Ops` / `Gamification` · `Gamification` |
| Thẻ, công tắc 1 | `Gamification` · `Enable gamification to boost your users' engagement and motivation throughout their training.` |
| Công tắc 2 | `Visibility in UpLMS` · `Show points, badges and ranks to your users. While this is off, they still accrue but stay hidden.` |
| Popover tắt | `Turn off gamification?` · `Points, badges and levels stop being recorded and all four features are locked. Existing data is kept. Turning it back on starts recording from that moment, nothing is backfilled.` · `Turn off` / `Cancel` |
| Popover hiển thị | `Show gamification to your users?` · `They will immediately see all points, badges and levels earned so far. No notifications are sent for past achievements.` · `Show` / `Cancel` |
| Lưu xong | `Saved` |
| No-access | `You do not have permission to view this page.` (chuẩn tạm, chờ design) |

`data-testid`: `gamification-settings-page`, `gamification-switch`, `visibility-switch`, `gamification-no-access`.
