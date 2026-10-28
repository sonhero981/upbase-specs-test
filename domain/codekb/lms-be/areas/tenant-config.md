---
repo: lms-be
area: tenant-config
branch: origin/staging
verified_commit: 1051114
verified_date: 2026-10-10
paths: [libs/database/src/lib/entities/tenant, libs/database/src/lib/entities/cache-manager, libs/database/src/lib/extends, libs/database/migrations, libs/constants/src/lib/tenant, libs/constants/src/lib/timezone, libs/modules/src/lib/tenant, libs/services/src/lib/redis, libs/utils/src/lib/common, apps/lms/src/app, apps/ops/src/app, apps/ops/src/caching-settings, apps/background-job-service/src/app]
---
# lms-be · tenant-config

## Vị trí code
- Entity `tenant`: `libs/database/src/lib/entities/tenant/tenant.entity.ts:4-27`. Service đọc: `TenantCommonService.getTenantSetting` `libs/modules/src/lib/tenant/tenant.service.ts:18-23`.
- Endpoint đọc cấu hình tenant: LMS `GET /setting` `apps/lms/src/app/app.controller.ts:41-51`; Ops `GET /setting` `apps/ops/src/app/app.controller.ts:58-68`. Chỉ GET, trả nguyên row `tenant`.
- Cache: `libs/services/src/lib/redis/` (`redis-cache.module.ts`, `cache.service.ts`, `cache.decorator.ts`); quản lý ở Ops `apps/ops/src/caching-settings/caching-settings.controller.ts:45-73`.
- Cron: `apps/background-job-service/src/app/app.controller.ts` (`@nestjs/schedule`, `app.module.ts:14`).

## Data
- `tenant`: `type`, `billing_model`, `can_publish_marketplace`, `contract_type`, `name`, `subdomain` (unique) + id/timestamps (`tenant.entity.ts:4-27`). **Không có cột múi giờ.** Mọi cột kiểu `text`, kể cả `can_publish_marketplace` (`libs/database/migrations/1789910000000-create-tenant-table.ts:8`). ALTER duy nhất: unique `subdomain` (`1789995000000-unique-tenant-subdomain-and-rename-default-tenant.ts:20`).
- `DEFAULT_TENANT_SUBDOMAIN = 'upbase'` (`libs/constants/src/lib/tenant/tenant.constants.ts:17`).
- **Không có bảng setting / key-value / feature flag theo tenant.** `feature_sections` (`libs/database/src/lib/entities/feature-section/feature-section.entity.ts:6`) là section môn học, không phải flag.
- `caching_settings` (`libs/database/src/lib/entities/cache-manager/cache-manager.entity.ts:4-30`): có `tenant_id`, `prefix`, `ttl`, `status` — bật/tắt cache theo prefix.

## API / event
- `GET /setting` (LMS, Ops) như trên. Không có PUT cấu hình tenant nào.
- CRUD `caching-managers` ở Ops (`caching-settings.controller.ts:45-73`).

## Luồng chính
1. Request vào → `RequestQueryRunnerMiddleware` (forRoutes `*`, `libs/database/src/lib/database.module.ts:57`) đọc `x-tenant-id` (`libs/database/src/lib/extends/request-query-runner.middleware.ts:51-53`).
2. `RequestQueryRunnerInterceptor` (APP_INTERCEPTOR, `database.module.ts:34`) set GUC `app.tenant_id` (`request-query-runner.interceptor.ts:41`); tenant trong CLS key `request_tenant_id` (`tenant.constants.ts:10`), đọc bằng `getRequestTenantId` (`libs/database/src/lib/extends/request-tenant.ts:21`).
3. Cache: `@Cache({key,id})` (`cache.decorator.ts:15-80`) chỉ cache khi `caching_settings` có row `prefix = key` và `status=ENABLED` (L41-67); key `tenant:{id}:key` (`cache.service.ts:17-20`).
4. Job: `TenantContextService.runForEachTenant` (`libs/database/src/lib/extends/tenant-context.service.ts:168-184`) chạy tuần tự từng tenant, lỗi tenant nào log rồi bỏ qua; dùng ở `apps/background-job-service/src/app/app.service.ts:47`.

## Ràng buộc ẩn
- **Múi giờ hardcode VN toàn hệ thống**: `ServerTimezone = { UTC_OFFSET: 7, DATABASE: 'Asia/Ho_Chi_Minh' }` (`libs/constants/src/lib/timezone/timezone.constants.ts:1-4`); `utcOffset(7)` literal `apps/ops/src/schedules/schedule.service.ts:173-176`; `Intl` `timeZone: 'Asia/Ho_Chi_Minh'` `libs/utils/src/lib/common/date.common.ts:46`; mọi `@Cron` đặt `timeZone: 'Asia/Ho_Chi_Minh'` (`apps/background-job-service/src/app/app.controller.ts:19`). Không dùng moment-timezone / dayjs tz.
- `RedisCacheModule` đăng ký `isGlobal: true` (`redis-cache.module.ts:16`) nhưng chỉ được import ở Ops (`apps/ops/src/app/app.module.ts:114`) và `libs/modules/src/lib/quiz-attempt/quiz-attempt.module.ts:10`; apps/lms dùng được nhờ QuizAttemptModule [suy ra, chưa kiểm wiring].
- Cache bật hay không do **dữ liệu** (`caching_settings`) chứ không do code: cùng một hàm có `@Cache` có thể cache ở tenant này, không ở tenant khác.

## Giới hạn hạ tầng
- Tenant: multi-tenant theo cột `tenant_id` + Postgres RLS (chi tiết `lms-be/authz-tenant.md`). Bảng mới có `tenant_id` phải thêm policy `tenant_isolation_<table>`.
- Cache: Redis, key theo tenant; không có in-memory cache cấu hình.
- Job: `@nestjs/schedule`, không Bull/BullMQ; `runForEachTenant` tuần tự.
- Đường ghi vào `tenant`: chỉ migration (không có API ghi).

## Hidden / dead
- `GET /setting` trả nguyên row `tenant` nhưng chưa có trường cấu hình nào ngoài thông tin hợp đồng [suy ra: lms-fe không gọi endpoint này, xem `lms-fe/learner-shell.md` mục Data].

## Liên quan
- lms-be `openspec/conventions/database.md`, `backend.md` § 2.
- codekb: `lms-be/authz-tenant.md` (RLS, tenant context), `lms-be/learner-presence.md`.
- Nhánh **`origin/draft/gamification`** (chưa merge, 71534e1, 2026-10-07): `libs/database/migrations/1790000000000-create-gamification-tables.ts` thêm `tenant.timezone varchar(64) NOT NULL DEFAULT 'Asia/Ho_Chi_Minh'` (L27), 10 bảng `gamification_*` có RLS (L314-317). Chỉ có migration + dbml + seed, chưa có service.

## Bug / câu hỏi cho 2.6
- HLD chốt: nhận `tenant.timezone` theo draft hay cách khác (PRD BR-14.9 để BE quyết). Mọi chỗ hardcode +7 ở trên không tự đổi theo cột mới.
- Cấu hình gamification (2 công tắc + point rules) là bảng mới; cache theo `@Cache` cần row `caching_settings` cho từng tenant, nếu không là đọc DB mỗi lần (PRD NFR US8/US14 yêu cầu giữ sẵn).
- Job theo ngày (đứt streak, leaderboard) không được dùng `@Cron` cố định giờ VN nếu tenant khác múi giờ: chạy theo giờ và lọc tenant theo `timezone`, hoặc tính lúc ghi [suy ra].
