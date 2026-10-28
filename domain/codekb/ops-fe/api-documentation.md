# API Documentation

## External APIs (lms-be app `ops`) mà ops-fe gọi trong vùng

Base URL: `process.env.VITE_API_PUBLIC` (`libs/service/src/request.ts:45-55`), staging `https://uplms-api.staging.upbase.asia/ops/api/v1/` (`apps/ops-fe/.env.example:1`). Prefix do BE đặt (`lms-be apps/ops/src/main.ts:53-54`).

| Method | Path | Gọi ở | BE | Auth | Ghi chú |
|---|---|---|---|---|---|
| GET | `/me` | `apps/ops-fe/src/apis/user/index.ts:59-61` ← `UserProvider.tsx:166` | `lms-be apps/ops/src/app/app.controller.ts:34-43` (`StaffGuard`, `getStaffDetail(sub)`) | Bearer Keycloak | Trả staff + `roles[].permissions` + `tenant`/`theme`. 403 / `FORBIDDEN_DOMAIN_ACCESS` → `accessDenied` (`UserProvider.tsx:178-184`) |

Endpoint BE có nhưng **ops-fe không gọi**:

| Method | Path | BE | Ghi chú |
|---|---|---|---|
| GET | `/setting` | `lms-be apps/ops/src/app/app.controller.ts:58-68` | Trả bản ghi `Tenant` theo tenant trong CLS (`lms-be libs/modules/src/lib/tenant/tenant.service.ts:18-23`). FE không dùng; `PageLink.SETTING` bị comment (`apps/ops-fe/src/constants/pageLink.ts:71`) |
| GET | `/my-role` | `app.controller.ts:45-56` | Quyền lấy qua `/me` thay thế |

Endpoint PRD cho lát (chưa tồn tại ở cả FE lẫn BE staging — `git grep -i gamif` rỗng):

| Method | Path (PRD) | US | Ghi chú |
|---|---|---|---|
| GET, PUT | `/api/v1/gamification/settings` | US14 | Thực tế sẽ là `…/ops/api/v1/gamification/settings` theo base URL |
| GET, PUT | `/api/v1/gamification/point-rules` | US8 (+ điểm nền US5) | PUT "full block" theo PRD §7.4 cũ — cần xem lại khi tự lưu từng ô |

## Contract chung của response / lỗi

- `apiRequest` trả `res.data`, lỗi axios ném `error.response.data` (`request.ts:66-88`); `fetcher` trả `res.data` (`request.ts:57-64`).
- Lỗi: interceptor toast theo `en.exceptions.json` + `replacements` (`request.ts:197-234`); **không toast** với 422, 413, `/me` 403 và mã trong `toastExceptions` (`request.ts:170-187`, `215-220`). `error.others[].errors[]` được toast từng dòng (`request.ts:235-266`).
- Header: `Content-Type: application/json` (`request.ts:90-99`), `Authorization` (`request.ts:101-112`). **Không có header tenant.**
- 401: refresh một lần, hàng đợi subscriber (`request.ts:114-168`).

## Internal APIs (surface nội bộ dùng cho lát)

| Surface | Chữ ký | Vị trí |
|---|---|---|
| `useHasPermission` | `(perm: string) => boolean` · `(perms: T[]) => Record<T, boolean>`; `superadmin` luôn `true` | `libs/hooks/src/permission/useHasPermission.tsx:9-43` |
| `usePermissions` | `(roles?) => { allowRender, adminPermission, allowRenderOptimized }` theo `permissionsToCheck` | `libs/hooks/src/permission/usePermissions.ts:6-37` |
| `useUserContext` | `{ profileMe, isSupperAdmin, accessDenied, profileLoading, tenantContext, … }` | `libs/state/src/context/UserProvider.tsx:16-50`, `233-241` |
| `useAppMutation` | `{ mutationFn, queryKey?, queryKeyPrefix?, successMessage?, onSuccess?, onError? }` → `useMutation` | `libs/hooks/src/use-app-mutation.tsx:4-63` |
| `useConfirm` | `confirm(IConfirm)` + `contextHolder` (modal `PopupConfirm`) | `libs/hooks/src/use-confirm.tsx:4-53` |
| `AppModule` | `{ name, routes: RouteObject[], pageLink, sidebarIds? }` | `libs/core/src/types/common.ts:42-47` |
| `setRequestConfig` | `{ PageLink, getAuthHeader, refreshAuth }` | `libs/service/src/request.ts:18-31` |
| `applyTenantFromMe` | `(me) => TenantContext \| null`, hydrate `getTenantManager()` + cache `up.tenant.v2` | `libs/utils/src/tenant-theme.ts:50-64` |
| `FeatureProvider` value | inject `XxxAPI` (`UsersAPI`, `StaffAPI`…) | `apps/ops-fe/src/index.tsx:128-188` |

Chưa có: `GamificationAPI`, `gamificationKeys`, permission `gr_*_gamification_*`, `ID_SIDE_BAR.GAMIFICATION*`.
