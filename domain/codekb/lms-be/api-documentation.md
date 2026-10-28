# API Documentation — lms-be

> Chỉ các API chạm lát US14/US8/US5, `origin/staging` @ `1051114`. Prefix `api/v1` cho cả LMS và Ops (`.env.example:19-20`), hai app chạy host riêng. Quy ước request/response: `openspec/conventions/backend.md` § 2. Swagger chỉ bật khi `NODE_ENV != PRODUCTION` (`apps/lms/src/main.ts:55-60`).

## REST APIs — apps/lms (học viên)

| Method | Path | Guard | Handler → Service | Response | Ghi chú |
|---|---|---|---|---|---|
| GET | `/api/v1/me` | `LmsGuard` | `app.controller.ts:20-28` → `UserService.getDetailLms` `user.service.ts:3118-3158` | Object user **không bọc** `SAPPResponse` (L27) gồm `detail`, `courses`, `certificates`, `tenant`, `theme` | `@Cache` key `lms:user:{userId}` (L3118-3121); `theme` hardcode (L3148-3156) |
| GET | `/api/v1/guide-active` | `LmsGuard` | `app.controller.ts:30-39` | `SAPPResponse.Success` | Ngoài lát |
| GET | `/api/v1/setting` | `LmsGuard` | `app.controller.ts:41-51` → `tenant.service.ts:18-23` | `SAPPResponse.Success(tenant row)` | Không cache; chỉ GET |
| GET | `/api/v1/courses/my-learnings` | `LmsGuard` | `courses.controller.ts:132-139` → `courses.service.ts:190-273` | `{ last_login, course_count: "done/total", test_count: "done/total" }` (L268-272) | Gọi Keycloak mỗi request (L207-211); không cache |
| GET | `/api/v1/users/activities` | `LmsGuard` | `apps/lms/src/users/users.controller.ts:134-143` | Danh sách activity Keycloak | Cùng nguồn `last_login` |

## REST APIs — apps/ops (vận hành)

| Method | Path | Guard | Handler | Ghi chú |
|---|---|---|---|---|
| GET | `/api/v1/setting` | `StaffGuard` | `apps/ops/src/app/app.controller.ts:58-68` | Như LMS; không khai `@ApiOperation` → không có rule Casbin → mọi staff gọi được |
| GET | `/api/v1/me` | `StaffGuard` | `app.controller.ts:34` | Nằm trong `ROUTE_WHITE_LIST` (`libs/constants/src/lib/role/role.ts:9`) |
| GET, POST | `/api/v1/caching-managers` | `StaffGuard` | `caching-settings.controller.ts:56,235` | `security.group: caching_management`; POST `tags: []` (L249) |
| GET, PATCH, DELETE | `/api/v1/caching-managers/:id` | `StaffGuard` | `caching-settings.controller.ts:78,256,277` | PATCH `tags: []` (L270) |
| GET | `/api/v1/caching-managers/:id/change-status` | `StaffGuard` | `caching-settings.controller.ts:215` | **GET làm đổi trạng thái** (`caching-settings.service.ts:187-203`) |
| GET, DELETE | `/api/v1/caching-managers/:id/keys`, `keys/:id`, `keys` | `StaffGuard` | `caching-settings.controller.ts:101-193` | Xoá key Redis |

Đây là mẫu "cấu hình theo tenant sửa từ Ops" duy nhất trên staging; gamification settings/point-rules (PRD) chưa tồn tại.

## Authentication / Authorization
- **LMS**: identity từ header gateway, không có thì verify Bearer (`lms.guard.ts:42-48`); kiểm `azp == lmsClientId` (L51); tra user bỏ RLS, `bindTenant` (L59-70); gắn `request.user` gồm `id, is_super_student, is_operator, is_supporter, type, tenant_id` (`user.service.ts:3186-3193`). Không có kiểm quyền theo endpoint.
- **Ops**: như trên + `OpsAuthService.authorize` (`ops-auth.service.ts:143-179`): whitelist role `superadmin` và route `/api/v1/me` (`role.ts:8-9`); còn lại `checkCanAcceptRoles(path, method)` (`permission.service.ts:88-138`). **Route chưa có rule `p` thì cho qua** (L94-105). Rule `p` sinh từ `tags` khi quét controller lúc khởi động (`permission.service.ts:57-80`), bỏ qua ở `LOCAL` (L58-60).

## Internal APIs (lib dùng chung)

| Symbol | Vị trí | Hợp đồng |
|---|---|---|
| `TenantCommonService.getTenantSetting(): Promise<Tenant>` | `libs/modules/src/lib/tenant/tenant.service.ts:18` | Đọc tenant hiện tại từ CLS |
| `getRequestTenantId(cls)` | `libs/database/src/lib/extends/request-tenant.ts:21-24` | `undefined` khi ngoài scope |
| `TenantContextService.run / withoutRls / bindTenant / runForEachTenant` | `tenant-context.service.ts:34,59,83,168` | Xem `component-inventory.md` |
| `@Cache({key,id})`, `@ClearCache({key,id})` | `libs/services/src/lib/redis/cache.decorator.ts:15,94` | Key tiền tố tenant |
| `CacheService.get/set/deleteCache` | `libs/services/src/lib/redis/cache.service.ts:34-58` | Key tiền tố tenant (L30-32) |
| `RedisCacheService.setKey/removeKey/removePrefixKeys` | `libs/services/src/lib/redis/redis-cache.service.ts:81-113` | Key **thô**, dùng `KEYS prefix*` (L21) |
| `KeycloakService.getListActivity(kcId, {page,page_size,type})` | `libs/services/src/lib/keycloak/keycloak.service.ts:435-457` | Custom endpoint `/realms/{realm}/user-session-provider/activities/{id}`, có retry |

## Events / Messaging
- Không có event/Kafka nào phát ra từ `/me`, `/setting`, `my-learnings`. Kafka chỉ đi qua `RequestQueryRunnerInterceptor` cho context `rpc` (`request-query-runner.interceptor.ts:29`), tenant lấy từ payload key `tenant_id` (`tenant.constants.ts:7`).
- Không có WebSocket gateway (xem `architecture.md` Infrastructure Constraints).

## Data Models (lát)

| Entity | Bảng | Cột chính | Bằng chứng |
|---|---|---|---|
| `Tenant` | `tenant` | `type, billing_model, can_publish_marketplace, contract_type, name, subdomain` (đều text) + id/timestamps | `tenant.entity.ts:4-27`; migration `1789910000000-create-tenant-table.ts:8` |
| `CachingSetting` | `caching_settings` | `tenant_id, name, description, endpoint, status, ttl, prefix, use_for` | `cache-manager.entity.ts:4-30` |
| `User` | `users` | `tenant_id` (L48-49), unique theo tenant (L43-45), cờ `is_super_student/is_operator/is_supporter`; **không** có `last_login`, `timezone` | `libs/database/src/lib/entities/user/user.entity.ts` |
