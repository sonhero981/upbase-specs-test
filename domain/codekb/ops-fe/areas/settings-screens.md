---
repo: ops-fe
area: settings-screens
branch: origin/staging
verified_commit: 1e01033bf
verified_date: 2026-10-10
paths: [apps/ops-fe/src/module-registry.ts, apps/ops-fe/src/bootstrap.ts, apps/ops-fe/src/routes, apps/ops-fe/src/constants, apps/ops-fe/src/components/access-denied, apps/ops-fe/src/pages/setting, scripts/generate-customer.js, configs, features/department/src/components/title, features/class-and-course/src/components/courses/course-detail/create-tabs, libs/core/src/constants/permission.ts, libs/core/src/constants/queryKeyFactory, libs/core/src/types, libs/core/src/enums/upload.ts, libs/hooks/src/permission, libs/hooks/src/use-app-mutation.tsx, libs/hooks/src/use-confirm.tsx, libs/ui/src/base/switch, libs/ui/src/base/numberfield, libs/ui/src/base/upload-file/ModalUploadFile, libs/ui/src/common, libs/state/src/context/UserProvider.tsx, libs/service/src/request.ts, libs/utils/src/tenant-theme.ts]
---
# ops-fe · settings-screens

Mẫu dựng màn cấu hình Ops (switch, ô số, lưu ngay, xác nhận, quyền theo trang). Permission/menu cơ bản đã ở `ops-fe/group-related-screens.md`; convention ở ops-fe `.claude/rules` + `.claude/inventory`.

## Vị trí code
- **Không có màn cấu hình hệ thống/tenant nào.** `apps/ops-fe/src/pages/setting/index.tsx:5-25` là placeholder, không route trỏ tới; `ID_SIDE_BAR.SETTING` (`libs/core/src/constants/permission.ts:231`) chưa dùng.
- Module: `apps/ops-fe/src/module-registry.ts:1-34` (viết tay), type `AppModule {name, routes, pageLink, sidebarIds?}` `libs/core/src/types/common.ts:42-47`; tiêu thụ ở `AppRouter.tsx:64`, `bootstrap.ts:5-27`, `index.tsx:20,190`. Mẫu module: `features/notification/src/index.ts:5-15`.
- Generator `scripts/generate-customer.js`: feature mới phải có ở **cả** `FEATURE_MODULE_MAP` và `FEATURE_FOLDER_MAP` (L18-52), thiếu thì `process.exit(1)` (L85-94); ghi đè registry của **bản copy** `../ops-fe-<name>` (L188-216).
- Menu: `ID_SIDE_BAR` (`permission.ts:166-287`); `menuEngagement` `libs/hooks/src/permission/useMenuData.tsx:794-896` (mẫu cha có con `ID_CX` L795-832, `checkShowParentMenu` L126-128); `filterMenuEngagement` L898-978.

## Data
- Quyền: `GET /me` (`apps/ops-fe/src/apis/user/index.ts:59-61`) gọi ở `libs/state/src/context/UserProvider.tsx:160-187`; `useHasPermission` đọc `profileMe.roles[].permissions`, SUPER_ADMIN (`role.code === 'superadmin'`, `permission.ts:149-151`) luôn qua.
- Tenant: lấy từ `/me` qua `applyTenantFromMe` (`libs/utils/src/tenant-theme.ts:50-64`); `ITenantInfo` (`libs/core/src/types/tenant-theme.ts:26-36`) **không có timezone**. FE không gửi `x-tenant-id` (`libs/service/src/request.ts:90-112`).
- Query key factory: `libs/core/src/constants/queryKeyFactory/` (barrel `index.ts:1-24`, mẫu `departmentKeys.ts:1-6`). Chưa có `gamificationKeys`.

## API / event
- Không có API settings tenant nào phía Ops FE. Mutation chuẩn: `useAppMutation` (`libs/hooks/src/use-app-mutation.tsx:30-63`, `successMessage` → `toast.success`, invalidate qua `queryKey`/`queryKeyPrefix`).

## Luồng chính
1. Mẫu **lưu ngay khi toggle có xác nhận**: `features/department/src/components/title/StaffTitleTable.tsx:38-78` — `useConfirm().confirm` (modal) → `mutate` → toast; huỷ/lỗi thì revert `setValue` (L62-76).
2. Mẫu **lưu khi blur/Enter**: `features/class-and-course/src/components/courses/course-detail/create-tabs/TabNavItem.tsx:83-94` (`onBlur → onConfirm`, Enter → `blur()`, Esc → huỷ; nút xoá `onMouseDown preventDefault` L59).
3. Switch: `HookFormSwitch` (`libs/ui/src/base/switch/HookFormSwitch.tsx:6-33`) — checkbox Bootstrap `form-switch`, gọi `onChange` rồi `onSubmit(checked)` (L19-22).
4. Ô số: `HookFormNumberField` (`libs/ui/src/base/numberfield/HookFormNumberField.tsx:11-131`, react-number-format) — có `onSubmit` thì bọc `<form onSubmit>` (L112-121) nên Enter submit.

## Ràng buộc ẩn
- `HookFormSwitch` **bỏ qua `disabled`** dù type có (`libs/core/src/types/form.ts:66`): không destructure, không gắn vào `<input>`.
- `HookFormSwitch.onSubmit` chạy **sau** khi giá trị form đã đổi → popover xác nhận phải tự revert khi huỷ/lỗi.
- `NumberField`: giá trị `0` hiển thị rỗng, xoá ô lưu `0` (`HookFormNumberField.tsx:56,59`); `isAllowed` bỏ qua `maxNumber` khi rỗng/0 (`NumberField.tsx:89`); không có prop `onBlur`/`onKeyDown` tuỳ biến; `<form>` lồng khi trang đã bọc form.
- Không có wrapper Popconfirm; cả repo không dùng antd `Popconfirm`. Có `useConfirm` (modal, `libs/hooks/src/use-confirm.tsx:18`), `PopupConfirm` (`libs/ui/src/common/PopupConfirm.tsx:24`), `BaseActionPopover` (menu hành động).
- `filterMenuEngagement` `default: return null` (`useMenuData.tsx:970`): item mới thiếu `case` thì ẩn với non-admin.
- **Không có guard quyền theo trang**: `AppRouter.tsx:41` chỉ fallback "No access"; `OpsAccessGate` (`apps/ops-fe/src/components/access-denied/index.tsx:7-59`) là gate toàn app khi `/me` 403, nút "Previous Page" thực ra `logOut` (L27-31).
- `RESOURCE_LOCATION` (`libs/core/src/enums/upload.ts:1-21`) chưa có `GAMIFICATION` (không ảnh hưởng US8/US14).

## Giới hạn hạ tầng
- Tenant: FE không biết timezone tổ chức, không gửi tenant; mọi cấu hình theo tenant do BE suy từ token.
- Dedupe/thứ tự lưu: không có cơ chế sẵn chống lần lưu trước ghi đè lần sau (PRD §7 yêu cầu) — phải tự làm (vd tuần tự hoá mutation theo khối) [suy ra].
- Không có toast helper riêng; `toast.success` của react-hot-toast trực tiếp hoặc qua `useAppMutation`.

## Hidden / dead
- `pages/setting` placeholder; `ID_SIDE_BAR.SETTING` không dùng.
- `apps/ops-fe/src/pages/{cache,shop/...}` import `src/components/base/upload-file/ModalUploadFile/UploadFileInterface` không tồn tại [suy ra có thể làm `check-types` lỗi].

## Liên quan
- codekb: `ops-fe/group-related-screens.md` (sửa nhỏ: `module-registry.ts` viết tay, `pnpm gen` chỉ ghi bản copy theo khách), `lms-be/authz-tenant.md`, `lms-be/tenant-config.md`.
- Nhánh **`origin/feature/uplms-sprint-1/gamification-feature`** (chưa merge, b5378f278, 2026-10-07; 124 file): `features/gamification` (Settings 5 khối + Learners, mock), `PermissionRoute` + `PageAccessDenied` (`libs/ui/src/common/permission-route/`), `TITLE_GAMIFICATION_GR` (`gr_view_gamification_config`, `gr_update_gamification_config`, `gr_view_gamification_learners`), `ID_SIDE_BAR.GAMIFICATION*`, `gamificationKeys`, `HookFormSwitch` nhận `disabled`, map generator. **Lưu theo nút Save chung + Discard** (`hooks/useSaveSettings.ts:19-77`, `components/settings/SettingsToolbar.tsx:12-37`) và **modal** confirm (`useSettingsConfirms.tsx:6-48`).

## Bug / câu hỏi cho 2.6
- Nhánh gamification ngược BR-14.10/14.13 (tự lưu, popover): tái dùng phần permission/menu/keys/switch, viết lại tầng lưu.
- Ô điểm US8 (≥1, không trần, lưu khi blur/Enter): `NumberField` hiện coi rỗng = 0 và không có onBlur — cần mở rộng component hoặc component riêng.
- Phân quyền: US15 ngoài lát; trang tạm cho SUPER_ADMIN [giả định điều phối]. Cần `PermissionRoute` (có ở nhánh) — lưu ý nó trả `null` khi chưa có `profileMe`, `/me` lỗi không phải 403 thì trắng trang.
- Bug sẵn có: generator thiếu `feature-marketing` trong cả hai map (registry có `marketingModule`, `module-registry.ts:8,33`); L194 lặp `config.features` thay vì danh sách đã gộp feature bắt buộc [suy ra].

## Màn role hiện nhóm quyền (kiểm 2026-10-13, `origin/staging` 1e01033bf)
- `features/role/src/components/roles/add-role/AddRole.tsx:38` lấy `RolesAPI.permissionsDetail()` (`apps/ops-fe/src/apis/roles/index.ts:35-37`, `GET /permissions`) rồi render mọi nhóm bằng `Object.entries`; tên nhóm hiển thị = key bỏ `_management` và `_` (`AddRole.tsx:224`, `detail/PermissionDetail.tsx:89`).
- Nhóm mới `gamification_management` tự hiện thành "gamification" — US15 không cần sửa màn role (BR-15.1).
