---
repo: lms-be
area: learner-presence
branch: origin/staging
verified_commit: 1051114
verified_date: 2026-10-10
paths: [apps/lms/src/app, apps/lms/src/main.ts, apps/lms/src/auth/guard, apps/lms/src/users, apps/lms/src/courses, apps/lms/src/course-section, libs/modules/src/lib/user, libs/modules/src/lib/class, libs/services/src/lib/keycloak, libs/database/src/lib/entities/user, libs/database/src/lib/database.module.ts, libs/utils/src/lib/log, libs/interface/src/lib/socket]
---
# lms-be · learner-presence

Tín hiệu "học viên có mặt" và các điểm chạm phía LMS: bootstrap, My Learning, ghi tiến độ.

## Vị trí code
- Bootstrap LMS: `GET /me` `apps/lms/src/app/app.controller.ts:20-28` → `UserService.getDetailLms` `libs/modules/src/lib/user/user.service.ts:3118-3158`. Khác: `GET /guide-active` (L30-39), `GET /setting` (L41-51), `GET /users/profile` `apps/lms/src/users/users.controller.ts:104-115`, `GET /users/activities` (L134-143).
- Guard: `LmsGuard` `apps/lms/src/auth/guard/lms.guard.ts:38-80`.
- My Learning: `GET /courses/my-learnings` `apps/lms/src/courses/courses.controller.ts:132-139` → `courses.service.ts:190-273`.
- Ghi tiến độ: `PUT /course-sections/course/:class_id/section/:section_id/progress` `apps/lms/src/course-section/course-section.controller.ts:233-253` → `course-section.service.ts:225-241` → `ClassCommonService.updateUserCourseSectionProgress` `libs/modules/src/lib/class/class.service.ts:10395-10457`.

## Data
- `users` **không có** `last_login` / `last_active` / `last_seen` (`libs/database/src/lib/entities/user/user.entity.ts:42-270`). Không có bảng login log / session cho học viên (`staff_sessions` chỉ cho staff).
- `user_click_events` (`libs/database/src/lib/entities/user/user-click-event.entity.ts:7-60`) chỉ ghi tương tác popup.
- Cờ trên `users`: `is_super_student` (L55-56), `is_operator` (L184-189), `is_supporter` (L198-203). **Không có cờ Test Account.** `LmsGuard` nạp sẵn 3 cờ vào `request.user` (`user.service.ts:3186-3193`).

## API / event
- `GET /me`: chỉ đọc, có `@Cache({ key: CACHE_KEY.USER, id: userId })` (`user.service.ts:3118`).
- `GET /courses/my-learnings`: response `SAPPResponse.Success({ last_login, course_count: "done/total", test_count: "done/total" })` (`courses.service.ts:268-272`). `last_login` lấy từ Keycloak `getListActivity(..., type:'login')` (`courses.service.ts:205-211`; `libs/services/src/lib/keycloak/keycloak.service.ts:435-457`, custom endpoint `/user-session-provider/activities`). Không `@Cache`.
- Socket: có dependency `@nestjs/websockets`, `@nestjs/platform-socket.io`, `socket.io` (`package.json:47,52,132`) và interface `libs/interface/src/lib/socket/index.ts:1-20`, nhưng **không có `@WebSocketGateway` nào**.
- PUT progress không emit Kafka/event.

## Luồng chính
1. Request LMS → middleware/interceptor tenant (`libs/database/src/lib/database.module.ts:34,57`) — chưa biết user.
2. `LmsGuard` (gắn theo route, **không global**, vd `courses.controller.ts:121`) tra user `withoutRls` rồi `bindTenant(user.tenant_id)` (`lms.guard.ts:59-70`) — điểm đầu tiên biết cả user lẫn tenant.
3. FE mở app gọi `GET /me` một lần mỗi lần tải trang (xem `lms-fe/learner-shell.md`), có thể bị cache Redis.
4. My Learning gọi Keycloak mỗi request, đếm `class_user` và quiz MID_TERM/FINAL/CHAPTER_TEST (`courses.service.ts:190-273`).
5. PUT progress: tìm progress, nếu có thì ghi đè `status` rồi `.save()` (`class.service.ts:10444-10455`).

## Ràng buộc ẩn
- Global của apps/lms chỉ có `ValidationPipe` (`apps/lms/src/main.ts:28`), `ClassSerializerInterceptor` (L46), hai cái của DatabaseModule, và `JobLogInterceptor` chỉ cho Kafka (`libs/utils/src/lib/log/logger.module.ts:41-48`). Không có `APP_GUARD`.
- PUT progress **không kiểm trạng thái cũ** (`class.service.ts:10446`): gửi FINISHED lần 2 vẫn save; `finished_at` đang bị comment (L10448). Không có row progress thì không làm gì nhưng vẫn trả UPDATE_SUCCESS (L10445).

## Giới hạn hạ tầng
- Tenant: RLS theo `app.tenant_id`; `LmsGuard` đọc user bằng bypass RLS (`lms.guard.ts:59-61`).
- Idempotency/dedupe: không có cơ chế ghi "lần đầu trong ngày" nào; mọi bootstrap endpoint chỉ đọc.
- Transaction: PUT progress **không có transaction** (`class.service.ts:10452-10454`), interceptor request cũng không mở.
- Đường ghi `user_course_section_progress`: hàm trên là đường chính trong phạm vi đọc; chưa quét hết đường ghi khác (job, Ops) [chưa kiểm].
- Realtime: chưa có gateway; FE dùng FCM (xem `lms-fe/learner-shell.md`).

## Hidden / dead
- Dependency socket.io có nhưng không dùng.
- `GET /me` trả `theme` hardcode placeholder (`user.service.ts:3148-3156`).

## Liên quan
- codekb: `lms-be/tenant-config.md`, `lms-be/authz-tenant.md` (Test Account, guard), `lms-be/class-enrollment.md`, `lms-fe/learner-shell.md`.
- Nhánh `origin/draft/gamification`: `gamification_checkins(tenant_id, user_id, checkin_date date)` unique `(user_id, checkin_date)` (`1790000000000-create-gamification-tables.ts:218-229`), `learner_stats.last_checkin_date`, `checkin_days` (L243-244).

## Bug / câu hỏi cho 2.6
- **Nguồn check-in (US5)**: không có tín hiệu sẵn; Keycloak login không dùng được (PRD US5 Out of scope cũng loại). HLD chọn: ghi trong `LmsGuard` sau L70 (mọi request, kể cả request nền → trái BR-5.1) hay endpoint check-in riêng do FE gọi khi người dùng chủ động mở/quay lại (PRD API nói "không có endpoint riêng" — lệch, cần chốt).
- Nếu đặt check-in trong `getDetailLms` thì `@Cache` (L3118) chặn khi cache USER bật.
- Unique `(user_id, checkin_date)` chặn ghi trùng hai thiết bị (PRD CG-7); cần kết hợp `last_checkin_date` để tránh ghi DB mỗi request (PRD NFR US5) [suy ra].
- PUT progress không phân biệt "vừa chuyển sang hoàn thành" và không transaction → hook cộng điểm (US13) phải tự đọc status cũ + chống trùng ở ledger (C5).
- My Learning thêm field gamification (PRD FR-2): endpoint đã phụ thuộc Keycloak, không try/catch quanh `Promise.all` (`courses.service.ts:205`) — thêm truy vấn mới phải theo NFR-GAM-01 [suy ra].
- Test Account: chưa có cờ; xem `lms-be/authz-tenant.md`.
