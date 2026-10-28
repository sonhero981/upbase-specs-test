# Component Inventory

> Chỉ component trong vùng quét sâu. Tên heading dùng verbatim trong `analyzed.components`.

## App shell

### module-registry
Danh sách `AppModule` viết tay (`apps/ops-fe/src/module-registry.ts:18-34`); `bootstrap.ts:5-27` gộp `pageLink`/`sidebarIds`. Phụ thuộc: mọi `@ops/feature-*`.

### generate-customer
Script build bản theo khách (`scripts/generate-customer.js`): map `FEATURE_MODULE_MAP`/`FEATURE_FOLDER_MAP` (L18-52), validate (L81-94), ghi đè `module-registry.ts` của bản copy (L188-216). Không có `feature-marketing` trong hai map dù registry có `marketingModule` (`module-registry.ts:8,33`).

### AppRouter
`apps/ops-fe/src/routes/AppRouter.tsx:25-71`: `/` → profile, route của module (L64), `*` → 404. Không guard quyền theo trang; route thiếu `element` hiện `No access` (L41).

### OpsAccessGate
Gate toàn app (`apps/ops-fe/src/components/access-denied/index.tsx:44-57`): loading khi chờ `/me`, `accessDenied` → `AccessDeniedScreen` (L7-35). Nút "Previous Page" thực chất `logOut` (L27-31).

### withAuthComponents
HOC chỉ kiểm `isAuthenticated`, chưa đăng nhập thì `manager.login()` (`libs/HOC/src/with-auth-components.tsx:4-19`). Không kiểm quyền.

### SettingPage
`apps/ops-fe/src/pages/setting/index.tsx:6-25`: placeholder in chữ "Setting", không route nào dùng; `ID_SIDE_BAR.SETTING` (`permission.ts:231`) không được tham chiếu.

## State / auth / HTTP

### UserProvider
`libs/state/src/context/UserProvider.tsx:88-231`: gọi `GET /me` một lần (L160-187), cấp `profileMe`, `isSupperAdmin` (L189-190), `accessDenied`, `profileLoading`, `tenantContext`.

### SidebarProvider
`libs/state/src/context/SidebarContext.tsx:25-46`: `visibleSidebarList` = danh sách cứng (L29-42) + `sidebarIds` của module (L43).

### auth
`apps/ops-fe/src/services/auth.ts:16-27`: `initAuth` Keycloak (`VITE_KEYCLOAK_*`), logout xoá `localStorage`.

### request
`libs/service/src/request.ts`: axios instance (L53-55), gắn Bearer (L101-112), refresh 401 (L114-168), toast lỗi toàn cục (L197-270). Không header tenant.

### tenant-theme
`libs/utils/src/tenant-theme.ts:50-84`: `applyTenantFromMe` (hydrate tenant manager + theme + cache), `restoreCachedTenantTheme`. Type `ITenantInfo` không có timezone (`libs/core/src/types/tenant-theme.ts:26-36`).

## Permission / menu

### useHasPermission
`libs/hooks/src/permission/useHasPermission.tsx:13-43`: check `roles[].permissions.includes(perm)`, `superadmin` luôn qua. Dùng ở 12 chỗ trong `features/` (git grep).

### usePermissions
`libs/hooks/src/permission/usePermissions.ts:6-37`: map `permissionsToCheck` (`apps/ops-fe/src/constants/sidebar.ts`) → `allowRender*`, `adminPermission`.

### useMenuData
`libs/hooks/src/permission/useMenuData.tsx` (1720 dòng): khai menu theo nhóm; mẫu cha có con `ID_CX` (L795-832), `checkShowParentMenu` (L126-128), lọc non-admin `filterMenuEngagement` (L898-978, `default: return null` L971-972).

### permission-constants
`libs/core/src/constants/permission.ts`: `TITLE_*_GR` permission codes, `CODE_ADMIN.SUPER_ADMIN = "superadmin"` (L149-151), `ID_SIDE_BAR` (L166-287). Chưa có gamification.

## Form controls / feedback

### HookFormSwitch
`libs/ui/src/base/switch/HookFormSwitch.tsx:6-33`: checkbox Bootstrap `form-switch`; `onChange(checked)` rồi `onSubmit(checked)` (L19-22) → giá trị form đổi **trước** khi lưu. Không destructure `disabled` (L6) dù `IBaseInputProps.disabled` có (`libs/core/src/types/form.ts:66`). Chỗ dùng có lưu: chỉ cập nhật form local (`features/class-and-course/src/components/question-bank/grading-ai/FilesTable.tsx:238-245`), chưa có mẫu switch → API.

### HookFormNumberField
`libs/ui/src/base/numberfield/HookFormNumberField.tsx:11-132`: `0` hiển thị rỗng (L56); `undefined` lưu `0` (L59); có `onSubmit` thì bọc `<form>` (L112-121) → Enter submit, dễ thành form lồng. Không nhận prop `onBlur`/`onKeyDown` (props L11-38).

### NumberField
`libs/ui/src/base/numberfield/NumberField.tsx`: `NumericFormat`; khi người dùng xoá ô, giá trị phát ra là `floatValue || minNumber` (L82-85, `minNumber` mặc định `0` L46) → ô rỗng không bao giờ là "rỗng" ở form state. `isAllowed` bỏ qua `maxNumber`/`maxLength` khi `value` falsy (L89). `NumberFieldInput` hỗ trợ `onKeyDown` (L28, L104-108) nhưng không destructure `onBlur` (L33-60) [suy ra: RHF `onBlur` không tới input].

### useAppMutation
`libs/hooks/src/use-app-mutation.tsx:30-63`: bọc `useMutation`, toast success, invalidate. Không serialize, không cancel request cũ.

### useConfirm
`libs/hooks/src/use-confirm.tsx:18-53`: confirm **modal** (antd `Modal` qua `PopupConfirm`); import tương đối chéo lib `../../ui/src/common/PopupConfirm` (L2).

### PopupConfirm
`libs/ui/src/common/PopupConfirm.tsx:24-…`: antd `Modal`. Repo không có Popconfirm; chỉ có antd `Popover` dùng trực tiếp (`features/class-and-course/src/components/courses/course-detail/course-tree-item/CourseTreeItem.tsx:7,126`).

### queryKeyFactory
`libs/core/src/constants/queryKeyFactory/`: barrel `index.ts:1-24`, mẫu `departmentKeys.ts:1-6`. Chưa có `gamificationKeys`.

## Mẫu tham chiếu

### StaffTitleTable
`features/department/src/components/title/StaffTitleTable.tsx:33-81`: đổi trạng thái bằng select (L118-126) → modal confirm → `useAppMutation` → lỗi/huỷ thì `setValue` revert (L62-76). Revert đoán giá trị cũ bằng đảo ACTIVE/INACTIVE, không lấy từ baseline.

### TabNavItem
`features/class-and-course/src/components/courses/course-detail/create-tabs/TabNavItem.tsx:70-99`: input `onBlur → onConfirm` (L83), Enter → `blur()` (L85-88), Esc → `onCancel` (L90-93), nút xoá chặn blur (L59). Mẫu đúng nhất cho "lưu khi rời ô / Enter" của `BR-14.10`.
