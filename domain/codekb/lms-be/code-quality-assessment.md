# Code Quality Assessment — lms-be

> `origin/staging` @ `1051114`. Chỉ số toàn repo là skim; đánh giá chi tiết chỉ cho vùng lát (xem `reverse-engineering-timestamp.md`).

## Test Coverage
- **Hiện trạng: gần như không có test.** 4 file `*.spec.ts` trên 1222 file `.ts` trong `apps/` + `libs/`, đều là spec mặc định do generator sinh: `apps/lms/src/app/app.controller.spec.ts`, `app.service.spec.ts`, `apps/ops/src/app/app.controller.spec.ts`, `app.service.spec.ts` (vd kiểm `{ message: 'Hello API' }`, `apps/lms/src/app/app.controller.spec.ts:16-20`).
- Có hạ tầng Jest (`jest.config.ts`, `jest.preset.js`, script `"test": "nx test"` `package.json:26`) nhưng không có coverage config.
- Vùng lát (tenant context, guard, cache, permission): **0 test**.

## Code Quality Indicators
- **Linting**: ESLint + `@nx` + `jsdoc` (`.eslintrc.json:4`); script `package.json:14-15`. `eslint-disable jsdoc/require-jsdoc` rải ở constructor (vd `tenant-context.service.ts:22`, `ops-auth.service.ts:23`).
- **Formatting**: Prettier (`package.json:13`).
- **Pre-commit**: `.husky/pre-commit` chạy `npx lint-staged`; lint-staged chạy `git add .`, `npm run format` (Prettier toàn repo) và `npm run lint` (ESLint `--fix` toàn repo) (`package.json:168-175`) → commit nào cũng format/lint cả repo và `git add .` có thể kéo file ngoài ý muốn.
- **CI/CD**: `.github/workflows/deploy-staging.yml` chỉ build image + deploy EC2 (L23-157); **không có bước lint/test/typecheck**.
- **Documentation**: `README.md`, `AGENTS.md`, `CLAUDE.md`, `openspec/README.md` + `openspec/conventions/*` (thay `.agents/` từ commit c279942, 12/10). JSDoc tiếng Việt tốt ở vùng tenant (`tenant-context.service.ts:28-33,53-58`).

## Quick Assessment (vùng lát)

| Tiêu chí | Mức | Ghi chú |
|---|---|---|
| Naming clarity | good | Vùng tenant/guard đặt tên rõ (`bindTenant`, `withoutRls`) |
| Function size | poor | `user.service.ts` 4111 dòng, `class.service.ts` 18332 dòng (god file) |
| Error handling | fair | Guard chuyển lỗi về `SAPPException` (`staff.guard.ts:58-71`); `my-learnings` không bao lỗi Keycloak (`courses.service.ts:205`) |
| Test presence | poor | Xem trên |
| Duplication | fair | Giờ VN lặp ở nhiều nơi (xem TD-3); `getTenantSetting` lặp logic trong `user.service.ts:3141-3142` và `staffs.service.ts:477` |
| Dead code | fair | socket.io không dùng; `theme` placeholder (`user.service.ts:3148-3156`) |

## Technical Debt (vùng lát)

| ID | Mô tả | Bằng chứng | Ảnh hưởng tới gamification |
|---|---|---|---|
| TD-1 | **Invalidation cache lệch tenant**: `@Cache` đọc key `tenant:{id}:ops:caching_manager:{prefix}` và `tenant:{id}:{prefix}…`, nhưng Ops admin set/xoá key thô `ops:caching_manager:{prefix}` và `KEYS {prefix}*` | `cache.decorator.ts:39-41`; `cache.service.ts:17-20`; `redis-cache.service.ts:21,81-113`; `caching-settings.service.ts:201,250-255` | Tắt cache hoặc đổi TTL từ Ops không có hiệu lực tới khi key hết hạn (1 giờ, `cache.constants.ts:25`). Cấu hình gamification nếu cache theo cơ chế này sẽ chậm cập nhật sau PUT |
| TD-2 | **Route Ops chưa khai quyền thì cho qua**; `caching-managers` khai `tags: []`, `/setting` không khai | `permission.service.ts:94-105`; `caching-settings.controller.ts:249,270,291`; `apps/ops/src/app/app.controller.ts:58-63` | Endpoint PUT gamification quên `tags` là mở cho mọi staff (PRD `US15`) |
| TD-3 | **Múi giờ hardcode** +7 / `Asia/Ho_Chi_Minh` (58 chỗ grep) | `timezone.constants.ts:1-4`; `date.common.ts:46`; `schedule.service.ts:173-176`; `background-job-service/src/app/app.controller.ts:19-209` | Trái `C6`, `C9`, `BR-14.9` |
| TD-4 | **GET làm thay đổi trạng thái** | `caching-settings.controller.ts:215` → `caching-settings.service.ts:187-203` | Không lặp lại mẫu này cho công tắc gamification |
| TD-5 | `GET /me` không bọc `SAPPResponse` trong khi `/setting` có | `apps/lms/src/app/app.controller.ts:27,50` | Contract không đồng nhất khi thêm field |
| TD-6 | `RedisCacheService` dùng `KEYS` (chặn Redis) | `redis-cache.service.ts:21` | Tránh khi xoá cache theo prefix gamification |
| TD-7 | `@Cache` không try/catch quanh Redis | `cache.decorator.ts:42,60,69,78` | Redis lỗi làm hỏng request đọc cấu hình → trái `NFR-GAM-01` nếu đọc config trong luồng học |
| TD-8 | Không có test cho tenant context/RLS | — | Bảng `gamification_*` mới không có lưới an toàn khi quên policy |

## Handoff Summary
- **Intent-relevant finding**: Cấu hình theo tenant chưa có chỗ chứa (`tenant.entity.ts:7-26`), cache cấu hình sẵn có bị TD-1, và guard quyền Ops mở mặc định (TD-2) — ba điểm 2.6 phải thiết kế lại thay vì tái dùng nguyên trạng.
- **Risks / follow-up**: hook check-in đặt sau `@Cache` sẽ không chạy (`user.service.ts:3118`); lỗi ghi trong transaction đang mở của request sẽ làm hỏng thao tác chính (connection dùng chung, `request-data-source.ts:71`).
