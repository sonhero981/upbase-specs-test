# Reverse Engineering Timestamp

## Run Record

- Date: 2026-10-11 · làm mới 2026-10-13 (lát Nền tảng US14, US15: CURRENT, quét thêm đường sinh quyền)
- Commit: 1051114 (`origin/staging`, commit 2026-10-09 "feat: gen staff password ưhen create new")
- Mode: focused scan, lead-only (developer lead quét + tự tổng hợp 9 artifact, không có link architect)
- Breadth: lát US14 (công tắc gamification theo tenant), US8 (cấu hình điểm), US5 (điểm vào hệ thống hằng ngày) của intent `260923-gamification` — cấu hình tenant, múi giờ, xác thực / `GET /me` / last login, my-learnings, phân quyền Ops + tenant/RLS, cache Redis theo tenant, cron, socket. Skim cấp thư mục cho stack, CI, test.
- Đọc code: `git show` / `git grep` trên `origin/staging`, không checkout.
- Điểm xuất phát: codekb vùng cũ `codekb/lms-be/areas/tenant-config.md`, `learner-presence.md`, `authz-tenant.md` (verified 1051114 / 2fbffd3) — đã kiểm lại bằng code; đã chuyển vào `areas/` (11/10/2026).
- Engine AWS (`codekb-snapshot`, `codekb-scope-diff --mint`, `codekb-publish`) không cài ở Upbase → `fingerprint: unknown`; freshness = `commit` + `analyzed.paths` (`git log 1051114..origin/staging -- <paths>` rỗng là CURRENT).
- Left out: `node_modules/`, `dist/`, `storages/`, `.yarn/`, `.claude/`, `openspec/` (chỉ trỏ tới, không quét).

### Đính chính so với codekb vùng cũ
- GUC `app.tenant_id` cho HTTP được set trong `TenantContextService.run` (`libs/database/src/lib/extends/tenant-context.service.ts:41`) qua middleware; `RequestQueryRunnerInterceptor` chỉ xử lý `rpc` (`request-query-runner.interceptor.ts:29`). Bản cũ ghi interceptor set GUC.
- `RedisCacheModule` có sẵn ở mọi app qua `ThirdPartyModule` global (`libs/services/src/lib/third-party.service.ts:10-30`) trong `ShareModule` (`libs/modules/src/lib/share.module.ts:70`). Bản cũ để "[suy ra, chưa kiểm wiring]".
- Repo **có** Bull (`libs/modules/src/lib/queues/queue.module.ts:9`, vài module Ops); cron vẫn là `@nestjs/schedule`. Bản cũ ghi "không Bull/BullMQ".
- `GET /me` đã trả kèm row `tenant` (`libs/modules/src/lib/user/user.service.ts:3141-3142`) — chưa ghi ở bản cũ.
- Mới phát hiện: invalidation cache Ops lệch tiền tố tenant (`code-quality-assessment.md` TD-1).

## WIP branches

| Nhánh | Commit / ngày | Chạm vùng | Nội dung |
|---|---|---|---|
| `origin/draft/gamification` | `71534e1` / 2026-10-07 | Có | 3 file: `gamification.dbml`, migration `1790000000000-create-gamification-tables.ts` (thêm `tenant.timezone varchar(64) NOT NULL DEFAULT 'Asia/Ho_Chi_Minh'` L27; `gamification_settings` 1 row/tenant với `is_enabled`, `is_visible`, 4 công tắc chức năng, `first_enabled_at`, `last_enabled_at` L57-83; `gamification_point_rules` unique `(tenant_id, action_code)`, `points >= 1`, `params jsonb` L86-102; `gamification_checkins` unique `(user_id, checkin_date)` L218-229; `learner_stats.last_checkin_date` L243; RLS có bypass L310-319), seed `1790001000000-seed-gamification-defaults.ts`. Không có service/controller |
| `origin/feature/gamification` | `c279942` / 2026-10-12 | Tài liệu | Luồng AI OpenSpec của BE (`openspec/`, `.claude/commands/{opsx,be}`) + change `upbase-221099-gamification` (design gốc, DEC-T1). `git diff origin/staging...c279942 -- apps libs` rỗng: không có code chạy |
| `origin/ai-workflow` | `54a4e1b` / 2026-10-12 | Tài liệu | OpenSpec change `upbase-221099-gamification` (proposal, design, tasks, specs `configuration`, `point-awarding`…), `PRD-gamification.md`; không có code chạy |
| `origin/feat/multi_tenant_database` | `400eb66` / 2026-10-02 | Đã merge vào staging | — |

Không coi các nhánh trên là code đã có.

## Scope of Analysis

```yaml
scope_version: 1
kind: partial
intent: 260923-gamification
fingerprint: unknown (Upbase không cài engine; freshness = commit + analyzed.paths)
commit: 610f100
analyzed:
  paths:
    - apps/lms/src/app/
    - apps/lms/src/auth/
    - apps/lms/src/main.ts
    - apps/lms/src/courses/courses.controller.ts
    - apps/lms/src/courses/courses.service.ts
    - apps/ops/src/auth/
    - apps/ops/src/app/app.controller.ts
    - apps/ops/src/caching-settings/
    - libs/database/src/lib/database.module.ts
    - libs/database/src/lib/extends/tenant-context.service.ts
    - libs/database/src/lib/extends/request-query-runner.middleware.ts
    - libs/database/src/lib/extends/request-query-runner.interceptor.ts
    - libs/database/src/lib/extends/request-data-source.ts
    - libs/database/src/lib/extends/request-tenant.ts
    - libs/database/src/lib/extends/tenant-id.subscriber.ts
    - libs/database/src/lib/entities/tenant/
    - libs/database/src/lib/entities/cache-manager/
    - libs/database/migrations/1789910000000-create-tenant-table.ts
    - libs/database/migrations/1789930000000-enable-rls-on-tenant-tables.ts
    - libs/database/migrations/1789994000000-add-rls-bypass-to-tenant-policies.ts
    - libs/modules/src/lib/tenant/
    - libs/modules/src/lib/permission/permission.service.ts
    - libs/modules/src/lib/scan-operation/scan-operation.service.ts
    - apps/ops/src/permissions/
    - libs/services/src/lib/redis/
    - libs/services/src/lib/third-party.service.ts
    - libs/constants/src/lib/tenant/
    - libs/constants/src/lib/timezone/
    - libs/constants/src/lib/cache/
    - libs/constants/src/lib/role/role.ts
  components:
    - TenantContextService
    - RequestQueryRunnerMiddleware
    - RequestDataSource
    - TenantIdSubscriber
    - Tenant
    - TenantCommonService
    - ServerTimezone
    - LmsGuard
    - StaffGuard
    - OpsAuthService
    - PermissionCommonService
    - UserService.getDetailLms
    - CourseService.getMyLearnings
    - KeycloakService.getListActivity
    - Cache decorator
    - CachingSettingService
    - BackgroundJobCron
shallow:
  paths:
    - package.json
    - tsconfig.base.json
    - docker.runtime-base.Dockerfile
    - .eslintrc.json
    - .husky/
    - .github/workflows/
    - .env.example
    - apps/
    - libs/modules/src/lib/user/user.service.ts
    - libs/modules/src/lib/share.module.ts
    - libs/modules/src/lib/queues/
    - libs/services/src/lib/keycloak/keycloak.service.ts
    - libs/database/src/lib/entities/user/user.entity.ts
    - libs/database/src/lib/entities/abstract/
    - libs/database/migrations/
    - libs/utils/src/lib/common/date.common.ts
    - libs/constants/src/lib/user/user.ts
    - apps/background-job-service/src/app/
    - apps/ops/src/schedules/schedule.service.ts
    - apps/ops/src/groups/group.controller.ts
    - apps/ops/src/staffs/staffs.service.ts
    - apps/lms/src/users/users.controller.ts
```
