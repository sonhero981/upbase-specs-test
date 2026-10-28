# Code Structure

> Chỉ vùng liên quan lát US14/US8/US5. Quy tắc đặt file: ops-fe `.claude/rules/01-code-placement.md`; inventory: ops-fe `.claude/inventory/01-ui.md` … `06-upbase-packages.md` (không chép lại).

## Package Organization

| Workspace | Package | Vai trò trong lát |
|---|---|---|
| `apps/ops-fe` | `ops-fe` (`apps/ops-fe/package.json:2`) | App shell: bootstrap, router, registry, API class |
| `features/*` | `@ops/feature-*` | Mỗi nghiệp vụ một module; gamification sẽ là `features/gamification` (chưa có trên staging) |
| `libs/core` | `@ops/core` | Types, permission codes, query key factory |
| `libs/hooks` | `@ops/hooks` | `useHasPermission`, `useMenuData`, `useAppMutation`, `useConfirm` |
| `libs/ui` | `@ops/ui` | `HookFormSwitch`, `HookFormNumberField`, `PopupConfirm` |
| `libs/state` | `@ops/state` | `UserProvider`, `SidebarProvider`, `FeatureProvider` |
| `libs/service` | `@ops/service` | axios `request`, `fetcher`, `setRequestConfig` |
| `libs/utils` | `@ops/utils` | `applyTenantFromMe`, date helpers |
| `libs/HOC` | `@ops/hoc` | `withAuthComponents` |

Alias resolve ở Vite (`apps/ops-fe/vite.config.ts:17-31`) và workspace deps (`apps/ops-fe/package.json:10-31`).

## File Classification (vùng quét sâu)

| Loại | File |
|---|---|
| Configuration | `apps/ops-fe/src/index.tsx`, `apps/ops-fe/src/bootstrap.ts`, `apps/ops-fe/src/module-registry.ts`, `apps/ops-fe/src/services/auth.ts`, `scripts/generate-customer.js` |
| Controller/Handler (route) | `apps/ops-fe/src/routes/AppRouter.tsx`, `features/notification/src/routes.tsx` (mẫu) |
| Middleware (HTTP) | `libs/service/src/request.ts` |
| Middleware (UI gate) | `apps/ops-fe/src/components/access-denied/index.tsx`, `libs/HOC/src/with-auth-components.tsx` |
| Service/State | `libs/state/src/context/UserProvider.tsx`, `libs/state/src/context/SidebarContext.tsx`, `libs/hooks/src/use-app-mutation.tsx` |
| Utility | `libs/hooks/src/permission/useHasPermission.tsx`, `usePermissions.ts`, `useMenuData.tsx`, `libs/utils/src/tenant-theme.ts` |
| Model/Entity | `libs/core/src/types/common.ts` (`AppModule` L42-47), `libs/core/src/types/tenant-theme.ts`, `libs/core/src/constants/permission.ts`, `libs/core/src/constants/queryKeyFactory/` |
| UI component | `libs/ui/src/base/switch/HookFormSwitch.tsx`, `libs/ui/src/base/numberfield/{HookFormNumberField,NumberField}.tsx`, `libs/ui/src/common/PopupConfirm.tsx`, `libs/hooks/src/use-confirm.tsx` |
| Page | `apps/ops-fe/src/pages/setting/index.tsx` (placeholder) |
| Mẫu tham chiếu | `features/department/src/components/title/StaffTitleTable.tsx`, `features/class-and-course/src/components/courses/course-detail/create-tabs/TabNavItem.tsx` |

## Code Patterns

- **Đăng ký module**: feature export `xxxModule: AppModule` (mẫu `features/notification/src/index.ts:5-15`), thêm vào `apps/ops-fe/src/module-registry.ts:18-34` và `apps/ops-fe/package.json` deps; muốn build theo khách thì thêm cả `FEATURE_MODULE_MAP` + `FEATURE_FOLDER_MAP` (`scripts/generate-customer.js:18-52`), thiếu thì `process.exit(1)` (L85-94).
- **Route**: mảng `{ path, element }` (`features/notification/src/routes.tsx:10-40`), path lấy từ hằng `XXX_ROUTES` cũng là `pageLink` của module.
- **Menu**: id ở `ID_SIDE_BAR` (`libs/core/src/constants/permission.ts:166-287`); item + children trong `useMenuData` (mẫu cha-con `ID_CX` `useMenuData.tsx:795-832`); lọc non-admin bằng `switch(item.id)` (`useMenuData.tsx:898-978`), item không có `case` → `default: return null` (L971-972) tức bị ẩn.
- **Query key factory**: object hàm trả tuple `as const` (`libs/core/src/constants/queryKeyFactory/departmentKeys.ts:1-6`), export qua barrel (`index.ts:1-24`).
- **Mutation**: `useAppMutation({ mutationFn, queryKey|queryKeyPrefix, successMessage })` (`libs/hooks/src/use-app-mutation.tsx:30-63`).
- **Lưu khi blur/Enter, Esc huỷ**: `TabNavItem.tsx:83-94`; chặn blur khi bấm nút phụ bằng `onMouseDown preventDefault` (L59).
- **Rollback tay sau confirm/lỗi**: `StaffTitleTable.tsx:45-78` (select trạng thái, không phải switch).

## Ngày giờ

Có `dayjs` + plugin `utc` (`libs/utils/src/common.ts:12-16`), không có plugin `timezone`; helper `formatDateTimeWithTimeZone` (`common.ts:108-123`) chỉ ghép giờ UTC. Lát US5 không cần FE tính ngày.
