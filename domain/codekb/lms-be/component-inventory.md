# Component Inventory — lms-be

> Focused scan: chỉ component chạm lát US14/US8/US5, `origin/staging` @ `1051114`. Không phải danh sách đầy đủ repo (52 domain `libs/modules`, xem `code-structure.md`). Tên heading dùng verbatim trong `analyzed.components`.

## Tenant context & data access

### TenantContextService
- **Trách nhiệm**: mở scope tenant (CLS + connection riêng + GUC `app.tenant_id`), bypass RLS, gắn tenant theo actor, chạy job cho từng tenant.
- **Vị trí**: `libs/database/src/lib/extends/tenant-context.service.ts:19-185` (`run` L34-51, `withoutRls` L59-76, `bindTenant` L83-101, `resetTenantContext` L132-149, `runForEachTenant` L168-184).
- **Phụ thuộc**: `DataSource`, `ClsService`, entity `Tenant`.
- **Dùng bởi**: `RequestQueryRunnerMiddleware`, interceptor RPC, `LmsGuard`, `OpsAuthService`, cron, permission scan.

### RequestQueryRunnerMiddleware
- **Trách nhiệm**: với HTTP, đọc `x-tenant-id` và bọc cả request trong `TenantContextService.run` tới khi response `finish/close`.
- **Vị trí**: `libs/database/src/lib/extends/request-query-runner.middleware.ts:14-55`; đăng ký `forRoutes('*')` ở `libs/database/src/lib/database.module.ts:57`.
- **Lưu ý**: interceptor cùng tên (`request-query-runner.interceptor.ts:29`) chỉ xử lý `rpc`.

### RequestDataSource
- **Trách nhiệm**: proxy `DataSource` để repository/manager/`createQueryRunner` dùng connection của scope; ngoài scope thì log cảnh báo và dùng connection mặc định.
- **Vị trí**: `libs/database/src/lib/extends/request-data-source.ts:12-78`; provider `database.module.ts:39-43`.

### TenantIdSubscriber
- **Trách nhiệm**: tự gán `tenant_id` từ CLS trước insert cho entity có cột này.
- **Vị trí**: `libs/database/src/lib/extends/tenant-id.subscriber.ts:14-37`.
- **Lưu ý**: chỉ `beforeInsert`; không áp cho `query()` SQL thô hay `insert()` query builder không qua entity [suy ra từ TypeORM subscriber, chưa kiểm].

## Tenant config

### Tenant
- **Trách nhiệm**: entity tổ chức; hiện chỉ thông tin hợp đồng.
- **Vị trí**: `libs/database/src/lib/entities/tenant/tenant.entity.ts:4-27`; repository rỗng `libs/database/src/lib/repositories/tenant/tenant.repository.ts:6`.
- **Lưu ý**: không có cột timezone/setting; bảng không bật RLS.

### TenantCommonService
- **Trách nhiệm**: đọc row tenant hiện tại.
- **Vị trí**: `libs/modules/src/lib/tenant/tenant.service.ts:6-24`; dùng ở `apps/lms/src/app/app.controller.ts:47-48`, `apps/ops/src/app/app.controller.ts:64-65`.

### ServerTimezone
- **Trách nhiệm**: hằng múi giờ máy chủ `UTC_OFFSET: 7`, `DATABASE: 'Asia/Ho_Chi_Minh'`.
- **Vị trí**: `libs/constants/src/lib/timezone/timezone.constants.ts:1-4`. Bản sao literal: `libs/utils/src/lib/common/date.common.ts:46`, `apps/ops/src/schedules/schedule.service.ts:173-176`, các `@Cron` ở `apps/background-job-service/src/app/app.controller.ts:19-209`.

## Authentication & authorization

### LmsGuard
- **Trách nhiệm**: xác thực học viên/giảng viên, gắn tenant, set `request.user`.
- **Vị trí**: `apps/lms/src/auth/guard/lms.guard.ts:12-99` (logic L38-80).
- **Phụ thuộc**: `KeycloakJwtService`, `KeycloakService`, `UserService.getUserByUserKeycloakId` (`user.service.ts:3181-3199`), `TenantContextService`.
- **Lưu ý**: gắn theo route; chạy ở **mọi** request có guard, kể cả request nền của FE.

### StaffGuard
- **Trách nhiệm**: xác thực staff Ops, ủy quyền cho `OpsAuthService`.
- **Vị trí**: `apps/ops/src/auth/guard/staff.guard.ts:16-93`.

### OpsAuthService
- **Trách nhiệm**: kiểm `azp`, tìm staff (kể cả khớp email rồi ghi `keycloak_user_id`), kiểm trạng thái, `bindTenant`, whitelist, gọi kiểm quyền.
- **Vị trí**: `apps/ops/src/auth/ops-auth.service.ts:20-181` (`authorize` L143-179).

### PermissionCommonService
- **Trách nhiệm**: quét và đồng bộ quyền từ controller vào `casbin_rule` theo tenant; kiểm role → group → (path, method).
- **Vị trí**: `libs/modules/src/lib/permission/permission.service.ts` (`scanAndSyncPermissions` L57-80, `checkCanAcceptRoles` L88-138).
- **Lưu ý**: route không có rule `p` → `true` (L103-105).

## Learner presence

### UserService.getDetailLms
- **Trách nhiệm**: dữ liệu bootstrap của `GET /me`: user, ảnh, đếm khoá/chứng chỉ, row tenant, theme placeholder.
- **Vị trí**: `libs/modules/src/lib/user/user.service.ts:3118-3158`.
- **Lưu ý**: bọc `@Cache` (L3118-3121) → khi cache bật thân hàm không chạy.

### CourseService.getMyLearnings
- **Trách nhiệm**: tổng hợp My Learning: `last_login` (Keycloak), số khoá, số bài test.
- **Vị trí**: `apps/lms/src/courses/courses.service.ts:190-273`; route `apps/lms/src/courses/courses.controller.ts:132-139`.
- **Lưu ý**: `Promise.all` không try/catch (L205-256): Keycloak lỗi là cả endpoint lỗi.

### KeycloakService.getListActivity
- **Trách nhiệm**: gọi custom endpoint activity của Keycloak.
- **Vị trí**: `libs/services/src/lib/keycloak/keycloak.service.ts:435-457`.

## Caching

### Cache decorator
- **Trách nhiệm**: `@Cache` đọc/ghi Redis theo key tiền tố tenant khi `caching_settings` của prefix đang `ENABLED`; `@ClearCache` xoá key sau khi chạy hàm.
- **Vị trí**: `libs/services/src/lib/redis/cache.decorator.ts:15-124`; key builder `cache.service.ts:17-20`; TTL mặc định 1 giờ `libs/constants/src/lib/cache/cache.constants.ts:24-26`.
- **Wiring**: `RedisCacheModule` (`redis-cache.module.ts:12-68`) global qua `ThirdPartyModule` (`libs/services/src/lib/third-party.service.ts:10-30`) trong `ShareModule` (`libs/modules/src/lib/share.module.ts:70`).

### CachingSettingService
- **Trách nhiệm**: CRUD `caching_settings` và xoá key Redis từ Ops.
- **Vị trí**: `apps/ops/src/caching-settings/caching-settings.service.ts` (`changeCachingSettingStatus` L187-204, `create` L212-230, `update` L238-257); controller `caching-settings.controller.ts:45-297`; entity `libs/database/src/lib/entities/cache-manager/cache-manager.entity.ts:4-30`.
- **Phụ thuộc**: `RedisCacheService` (key không tiền tố tenant, `redis-cache.service.ts:81-113`).

## Background jobs

### BackgroundJobCron
- **Trách nhiệm**: lịch `@Cron` (`@nestjs/schedule`) gọi `AppService` → `runForEachTenant`.
- **Vị trí**: `apps/background-job-service/src/app/app.controller.ts:19-209` (skim), `app.service.ts:46-48`.
- **Lưu ý**: một giờ chạy cho mọi tenant theo `Asia/Ho_Chi_Minh`.
