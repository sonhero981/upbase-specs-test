# Business Overview — lms-be

> Focused scan cho intent `260923-gamification` (lát US14, US8, US5). Code theo `origin/staging` @ `1051114`. Phạm vi đọc sâu: xem `reverse-engineering-timestamp.md`.

## Business Context

lms-be là backend NestJS của sản phẩm UpLMS / UpLnD: một repo Nx chứa nhiều app chạy riêng (`apps/lms` cho học viên/giảng viên, `apps/ops` cho vận hành, cùng các service nền). Hệ thống đã chuyển sang **multi-tenant theo `tenant_id` + Postgres RLS** (`libs/database/migrations/1789930000000-enable-rls-on-tenant-tables.ts:3-32`), nhưng vẫn chỉ có một tenant mặc định `upbase` (`libs/constants/src/lib/tenant/tenant.constants.ts:17`).

Hai nhóm người dùng tách định danh: học viên/giảng viên là `users` (guard `LmsGuard`, `apps/lms/src/auth/guard/lms.guard.ts:12`), nhân sự vận hành là `staffs` (guard `StaffGuard`, `apps/ops/src/auth/guard/staff.guard.ts:16`). Cả hai xác thực qua Keycloak (xem `architecture.md` mục Interaction Diagrams).

## Business Capabilities liên quan lát

| Capability | Trạng thái trong code | Bằng chứng |
|---|---|---|
| Hồ sơ / cấu hình tổ chức (tenant) | Chỉ có thông tin hợp đồng, **chỉ đọc** | `libs/database/src/lib/entities/tenant/tenant.entity.ts:4-27`; `GET /setting` LMS `apps/lms/src/app/app.controller.ts:41-51`, Ops `apps/ops/src/app/app.controller.ts:58-68` |
| Múi giờ tổ chức | **Không có**, hardcode giờ VN toàn hệ thống | `libs/constants/src/lib/timezone/timezone.constants.ts:1-4` |
| Công tắc tính năng theo tenant | **Không có** bảng flag/setting; chỉ có bật/tắt cache theo prefix | `libs/database/src/lib/entities/cache-manager/cache-manager.entity.ts:4-30` |
| Học viên vào hệ thống (bootstrap) | `GET /me` chỉ đọc, có thể bị cache Redis | `apps/lms/src/app/app.controller.ts:20-28`, `libs/modules/src/lib/user/user.service.ts:3118-3158` |
| "Lần đăng nhập gần nhất" | Không lưu ở DB; đọc từ Keycloak mỗi lần | `apps/lms/src/courses/courses.service.ts:205-211,258-261` |
| Phân quyền vận hành | Casbin rule trong DB, kiểm thủ công theo path+method | `libs/modules/src/lib/permission/permission.service.ts:88-138` |
| Gamification (điểm, chuỗi, cấu hình) | **Chưa có trên staging**; chỉ có nhánh nháp | xem `reverse-engineering-timestamp.md` mục WIP branches |

## Business Transactions liên quan

1. **Học viên mở UpLMS** → `GET /api/v1/me` (prefix `api/v1` từ `.env.example:19`) → trả user + `tenant` + đếm khoá/chứng chỉ (`user.service.ts:3140-3147`). Không ghi gì. Chi tiết luồng: `architecture.md` Interaction Diagrams #1.
2. **Đọc cấu hình tổ chức** → `GET /setting` trả nguyên row `tenant` (`libs/modules/src/lib/tenant/tenant.service.ts:18-23`). Diagram #2.
3. **Vận hành sửa một cấu hình theo tenant** → mẫu gần nhất là `caching-managers` ở Ops (`apps/ops/src/caching-settings/caching-settings.controller.ts:45-47`), đi qua `StaffGuard` → `OpsAuthService.authorize` → `checkCanAcceptRoles`. Diagram #3.
4. **My Learning** → `GET /api/v1/courses/my-learnings` trả `last_login`, `course_count`, `test_count` (`courses.service.ts:268-272`).

## Business Rules thấy trong code (liên quan PRD)

- Ngày/giờ luôn theo `Asia/Ho_Chi_Minh` (+7): mọi `@Cron` (`apps/background-job-service/src/app/app.controller.ts:19`), format ngày (`libs/utils/src/lib/common/date.common.ts:46`), lịch (`apps/ops/src/schedules/schedule.service.ts:173-176`). Trái `C6`/`C9`/`BR-14.9` của PRD nếu tenant khác múi giờ.
- Không có khái niệm `Test Account`: `users` chỉ có `is_super_student` (`libs/database/src/lib/entities/user/user.entity.ts:56`), `is_operator` (L189), `is_supporter` (L203). PRD `C10`, `BR-5.14` cần PO chốt cờ.
- Tenant mới chỉ sinh bằng migration (`libs/database/migrations/1789920000000-add-tenant-id-to-core-tables.ts:67`), không có API tạo tenant → PRD `BR-14.6` "mặc định tắt khi khởi tạo tổ chức" phải giải bằng seed/lazy-create.

## Glossary

| Thuật ngữ | Nghĩa trong code |
|---|---|
| Tenant | Row bảng `tenant`; id lan truyền qua header `x-tenant-id` và CLS key `request_tenant_id` (`tenant.constants.ts:10`) |
| RLS | Policy `tenant_isolation_<table>` so `tenant_id` với GUC `app.tenant_id` |
| `bindTenant` | Gắn tenant của actor vào request khi header chưa có (`libs/database/src/lib/extends/tenant-context.service.ts:83-101`) |
| Caching setting | Row `caching_settings` quyết định một `@Cache` prefix có bật ở tenant đó hay không |
