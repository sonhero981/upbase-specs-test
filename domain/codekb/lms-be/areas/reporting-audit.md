---
repo: lms-be
area: reporting-audit
branch: feature/ai_workflow (HEAD trùng origin/staging)
verified_commit: 2fbffd3
verified_date: 2026-10-10
paths: [apps/ops/src/sis-dashboard, apps/lms/src/report, libs/modules/src/lib/report, libs/database/src/lib/entities/class/user-course-section-progress.entity.ts, libs/database/src/lib/entities/field_change_logs, libs/database/src/lib/entities/mail-log, libs/database/migrations-stored-procedure]
---
# lms-be · reporting-audit

## Vị trí code
- SIS Dashboard (Ops): `apps/ops/src/sis-dashboard/sis-dashboard.controller.ts` (`@Controller('sis-dashboard')`, nhóm quyền `dashboard_sis`) → `sis-dashboard.service.ts`.
- Report LMS (học viên): `apps/lms/src/report/report.controller.ts` (`@Controller('report')`, `LmsGuard`) → `apps/lms/src/report/report.service.ts` → `libs/modules/src/lib/report/report.service.ts`.
- Stored procedure: `libs/database/migrations-stored-procedure/*`, khoá ở `libs/database/src/lib/stored-procedure/stored-procedure.key.ts`.
- Audit: `field_change_logs`, `mail_logs`, `class_user_change_history_instances`, `import_logs`.

## Data
- `user_course_section_progress` (`libs/database/src/lib/entities/class/user-course-section-progress.entity.ts`): `class_user_id`, `course_section_id`, `started_at`, `finished_at` từng section. Nguồn tiến độ mọi báo cáo đang tính trực tiếp.
- Không có bảng snapshot / thống kê theo ngày. `report_logs` (`libs/database/src/lib/entities/action-logs/report/report-log.entity.ts`) chỉ log lượt chạy job thống kê quiz.
- `field_change_logs` (`libs/database/src/lib/entities/field_change_logs/field_change_logs.entity.ts`): `field_key`, `old_value`, `new_value`, `reason`, `object_type`, `object_id`, `metadata` (json), `created_by_staff_id`, `created_at`. Một nơi ghi: `libs/modules/src/lib/user/user.service.ts` `persistUserUpdate` ~L2261 (đổi `teacher_status`).
- `mail_logs` (`libs/database/src/lib/entities/mail-log/mail-log.entity.ts`): type, action, email, status NEW/SENT/FAIL, retry, object_id; Ops `apps/ops/src/mail-log/*` (`/mail-logs`).

## API / event
| Method | Path | Khoá |
|---|---|---|
| GET | `/report/:class_id/{overall,topic,weekly,learning-result,exam-prediction,mock-test-result}` (LMS) | class_id + user hiện tại |
| GET | `/sis-dashboard/{student-background-distribution, distribution-of-student-by-class-per-test, list-student-in-test, list-quiz-by-course-id, list-user-in-class, get-list-section-belong-to-of-quiz, scoring-ratio-per-class-for-with-quiz, list-progress-of-student-in-class, list-test-by-course-id, list-student-in-course-content-per-class}` (Ops) | course_id / class_code |

## Luồng chính
1. SIS service trộn QueryBuilder và raw `dataSource.query(...)` (`sis-dashboard.service.ts` ~L1201, L1220, L1361, L1916, L2094, L2166) trên `class_user_instances` + `user_course_section_progress`.
2. Loại `is_operator`, `is_super_student`, `is_supporter` khỏi số liệu.
3. Report LMS: `checkPermissionUser` rồi tính trực tiếp trên progress, quiz_attempts, gradings.

## Ràng buộc ẩn
- Mọi báo cáo khoá theo lớp/khoá (KB-SIS-01); không có chiều người hay nhóm.
- `user_course_section_progress.finished_at` cho phép dựng tiến độ tại mốc quá khứ mà không cần snapshot [suy ra; cần kiểm section sửa sau mốc và soft delete].
- Gỡ học viên soft delete cả progress (xem `lms-be/class-enrollment.md`) → báo cáo quá khứ mất người đó nếu lọc `deleted_at IS NULL`.

## Hidden / dead
- `field_change_logs` đủ cột nhưng gần như không dùng (một writer, repository rỗng `libs/database/src/lib/repositories/field_change_logs/field_change_logs.repository.ts`).

## Liên quan
- lms-be `openspec/conventions/backend.md` § 6.
- codekb: `lms-be/class-enrollment.md`, `lms-be/group-department.md`. Intent `261006-report-phase-1` cùng sửa SIS dashboard.

## Bug / câu hỏi cho 2.6
- Báo cáo theo nhóm (US18) là endpoint mới, không nới SIS cũ (CF-1). Truy vấn: thành viên tại mốc × cây tại mốc × progress từ `finished_at`.
- Q1 "lưu thêm lịch sử tiến độ" có thể không cần nếu chấp nhận suy từ `finished_at`; HLD chốt.
- Nhật ký nhóm (US15): bảng lịch sử thành viên riêng thay vì `field_change_logs` (vốn theo cột của một row) [TEST tự chọn].
