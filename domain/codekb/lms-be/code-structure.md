# Code Structure — lms-be

> `origin/staging` @ `1051114`. Quy ước đặt code đầy đủ ở `openspec/conventions/backend.md` § 1 (không chép lại). File này chỉ ghi cấu trúc chạm lát US14/US8/US5.

## Build System
- Nx 16 (`package.json:123`), yarn (`.yarn/`), TypeScript path alias `@sapp/*` (`tsconfig.base.json:19-29`).
- Migration TypeORM CLI: `package.json:6-11`, thư mục `libs/database/migrations/` (38 file).
- Chi tiết version: `technology-stack.md`.

## Module Organization

| Tầng | Đường dẫn | Vai trò | Vùng lát chạm |
|---|---|---|---|
| App LMS | `apps/lms/src/<feature>/` (29 mục) | Controller + service mỏng cho học viên | `app/` (`/me`, `/setting`), `auth/guard/`, `courses/` (`my-learnings`) |
| App Ops | `apps/ops/src/<feature>/` (59 mục) | Controller cho vận hành | `auth/`, `app/` (`/setting`), `caching-settings/` |
| App nền | `apps/background-job-service/src/app/` | `@Cron` + `runForEachTenant` | job theo ngày (chỉ skim) |
| Business chung | `libs/modules/src/lib/<domain>/` (52 domain) | `*CommonService`, `UserService`… | `tenant/`, `user/`, `permission/` |
| Data | `libs/database/src/lib/entities/` (48 nhóm), `extends/`, `migrations/` | Entity, tenant context, RLS | `entities/tenant/`, `entities/cache-manager/`, `entities/user/`, `extends/` |
| Hạ tầng | `libs/services/src/lib/` | Redis, Keycloak, Casbin, FCM, S3… | `redis/`, `keycloak/` |
| Hằng số | `libs/constants/src/lib/` | Enum, key cache, tenant, timezone | `tenant/`, `timezone/`, `cache/`, `role/` |

## Key Files (lát)

| File | Loại | Ghi chú |
|---|---|---|
| `libs/database/src/lib/database.module.ts` | Configuration | `@Global`, mount CLS (L24), `APP_INTERCEPTOR` (L34), middleware `forRoutes('*')` (L57) |
| `libs/database/src/lib/extends/tenant-context.service.ts` | Middleware/Utility | `run`, `withoutRls`, `bindTenant`, `runForEachTenant` (L34-184) |
| `libs/database/src/lib/extends/request-query-runner.middleware.ts` | Middleware | HTTP: đọc `x-tenant-id` (L51-53) |
| `libs/database/src/lib/extends/request-query-runner.interceptor.ts` | Middleware | **Chỉ RPC/Kafka** (L29) |
| `libs/database/src/lib/extends/request-data-source.ts` | Repository | Proxy DataSource về connection của request (L44-78) |
| `libs/database/src/lib/extends/tenant-id.subscriber.ts` | Middleware | Tự điền `tenant_id` khi insert (L27-36) |
| `libs/database/src/lib/entities/tenant/tenant.entity.ts` | Model | 6 cột text (L7-26) |
| `libs/modules/src/lib/tenant/tenant.service.ts` | Service | `getTenantSetting` (L18-23) — service duy nhất của module tenant |
| `apps/lms/src/app/app.controller.ts` | Controller | `/me` (L20-28), `/guide-active` (L30-39), `/setting` (L41-51) |
| `apps/lms/src/auth/guard/lms.guard.ts` | Middleware | Guard LMS (L38-80) |
| `libs/modules/src/lib/user/user.service.ts` | Service | 4111 dòng; đọc L3112-3199 (`getDetailLms`, `getUserByUserKeycloakId`) |
| `apps/lms/src/courses/courses.service.ts` | Service | `getMyLearnings` (L190-273) |
| `apps/ops/src/auth/ops-auth.service.ts` | Service | `authorize` (L143-179) |
| `libs/modules/src/lib/permission/permission.service.ts` | Service | `checkCanAcceptRoles` (L88-138) |
| `libs/services/src/lib/redis/cache.decorator.ts` | Utility | `@Cache` (L15-92), `@ClearCache` (L94-124) |
| `libs/services/src/lib/redis/redis-cache.service.ts` | Utility | Thao tác Redis thô, không tiền tố tenant (L20-113) |
| `apps/ops/src/caching-settings/*` | Controller/Service | CRUD `caching_settings` |
| `libs/constants/src/lib/timezone/timezone.constants.ts` | Configuration | `ServerTimezone` (L1-4) |

## Code Patterns

- **Controller → CommonService**: controller trả `SAPPResponse.Success(data)` (`apps/lms/src/app/app.controller.ts:50`, `apps/lms/src/courses/courses.controller.ts:138`); quy ước contract ở `openspec/conventions/backend.md` § 2.
- **Guard theo route**: `@UseGuards(LmsGuard)` / `@UseGuards(StaffGuard)` trên từng handler (`app.controller.ts:22`, `caching-settings.controller.ts:58`).
- **Khai quyền Ops bằng `@ApiOperation({ security, tags })`**: mẫu đầy đủ `apps/ops/src/groups/group.controller.ts:66-86`; quy ước comment `caching-settings.controller.ts:33-43`.
- **Truy cập DB qua `RequestDataSource`** (`tenant.service.ts:10,20`) hoặc `@InjectRepository` (`ops-auth.service.ts:25`); cả hai đều đi qua connection đã set tenant khi trong scope.
- **Cache khai báo**: `@Cache({ key: CACHE_KEY.X, id })` (`user.service.ts:3118-3121`); key ở `libs/constants/src/lib/cache/cache.constants.ts:1-22`.
- **Transaction thủ công**: `queryRunner.startTransaction()` (vd `apps/lms/src/request-schedules/request-busy-schedules.service.ts:47`); không có decorator transaction.
- **Job đa tenant**: `this.tenantContext.runForEachTenant(() => ...)` (`apps/background-job-service/src/app/app.service.ts:46-48`).

## File Classification (vùng lát)
- Model: `entities/tenant/`, `entities/cache-manager/`, `entities/user/user.entity.ts`
- Controller: `apps/lms/src/app/`, `apps/lms/src/courses/courses.controller.ts`, `apps/ops/src/app/app.controller.ts`, `apps/ops/src/caching-settings/caching-settings.controller.ts`
- Service: `libs/modules/src/lib/tenant/`, `user/user.service.ts`, `permission/permission.service.ts`, `apps/lms/src/courses/courses.service.ts`, `apps/ops/src/auth/ops-auth.service.ts`
- Middleware: `libs/database/src/lib/extends/`, `apps/lms/src/auth/guard/`, `apps/ops/src/auth/guard/`
- Configuration: `libs/database/src/lib/database.module.ts`, `libs/services/src/lib/redis/redis-cache.module.ts`, `libs/services/src/lib/third-party.service.ts`
- Migration: `libs/database/migrations/1789910000000-*`, `1789930000000-*`, `1789994000000-*`
- Test: chỉ 4 spec mặc định (xem `code-quality-assessment.md`)
