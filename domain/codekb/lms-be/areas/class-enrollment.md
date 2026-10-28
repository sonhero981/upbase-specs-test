---
repo: lms-be
area: class-enrollment
branch: feature/ai_workflow (HEAD trùng origin/staging)
verified_commit: 2fbffd3
verified_date: 2026-10-10
paths: [libs/database/src/lib/entities/class/class-user-instances.entity.ts, libs/database/src/lib/entities/class/class-mentor-instances.entity.ts, libs/modules/src/lib/class/class.service.ts, libs/modules/src/lib/class/class-add-student-strategies, apps/ops/src/class/class.controller.ts, libs/constants/src/lib/class/class.constants.ts, libs/constants/src/lib/mail/mail.ts, apps/background-job-service/src/app]
---
# lms-be · class-enrollment

## Vị trí code
- Ops: `apps/ops/src/class/class.controller.ts` (`@Controller('classes')`) → `apps/ops/src/class/class.service.ts` → `libs/modules/src/lib/class/class.service.ts` (`ClassCommonService`, ~18k dòng).
- Strategy theo loại lớp: `libs/modules/src/lib/class/class-add-student-strategies/add-student-strategy.factory.ts` (FOUNDATION, LESSON, default); Foundation tự thêm ở `lesson-add-student.strategy.ts`.
- Import: `POST /classes/:id/import-student` → BullMQ (`libs/modules/src/lib/queues/processors/import.processor.ts`) → `libs/modules/src/lib/import/import-student-class.service.ts` (L304 gọi `addStudent`, source `IMPORT`).
- Mail: `MAIL_LIST` (`libs/constants/src/lib/mail/mail.ts:94`, `defineMailList`), template MJML `apps/notification-service/src/assets/templates/*`, gửi qua `MailCommonService.sendMail` (`libs/modules/src/lib/mail/mail.service.ts:113`) → Kafka `process_send_mail` → `apps/notification-service/src/app/app.controller.ts:27`.
- Cron: `apps/background-job-service/src/app/app.controller.ts` (`@Cron`, `Asia/Ho_Chi_Minh`) → `app.service.ts` bọc `tenantContext.runForEachTenant`.

## Data
- `class_user_instances` (`libs/database/src/lib/entities/class/class-user-instances.entity.ts`): `status`, `type`, `source_type` (text, **một giá trị**), `learning_progress` (json `total_course_sections`, `total_course_sections_completed`), `started_at`, `finished_at`, `foundation_status`, `is_bonus_class`, `extend_count`, `deleted_at`. Chỉ `@Index(['user_id','class_id'])`, **không unique**.
- Enum (`libs/constants/src/lib/class/class.constants.ts`): `CLASS_USER_STATUS` READY_TO_LEARN · IN_PROGRESS · COMPLETED · CANCELED; `CLASS_USER_TYPES` (NORMAL, RESERVED, … TRANSFERED_TO, BE_TRANSFERRED, CANCELED) + `INVALID_CLASS_USER_TYPES`, `CLASS_USER_TYPE_CAN_DELETE`; `CLASS_USER_SOURCE_TYPE` (L87) SYNC_DEAL_WON · SYNC_TICKET_ENROLLMENT · SELF_ACTIVATED · PUBLIC_ENROLL · FORM_REGISTED · MANUAL · IMPORT — chưa có giá trị cho nhóm.
- Bảng con treo vào lượt ghi danh: `user_course_section_progress` (`.../class/user-course-section-progress.entity.ts`, có `started_at`, `finished_at` từng section), quiz_attempts, class_user_scores, storyline progress, notes, class_schedule_user_instances.
- `class_user_change_history_instances` (`.../class/class-user-change-history-instances.entity.ts`): lịch sử CLASS_MOVED/TRANSFERRED/RESERVED/REVERTED, actor STAFF/USER/SYSTEM, reason. Không lưu tiến độ.
- `class_mentor_instances` (`.../class/class-mentor-instances.entity.ts`): `class_id`, `mentor_id` → staffs, `is_main_mentor`, `mentor_type` STAFF|USER. Không có chiều "mentor phụ trách tập học viên nào".
- Lesson ↔ Foundation: `classes_foundation_classes` (`.../class/class-foundation-class.entity.ts`: normal_class_id, foundation_class_id, level_code); `classes.hybrid_class_id` (`class.entity.ts:151`).

## API / event
| Method | Path (ops) | Ghi chú |
|---|---|---|
| POST | `/classes/students` | `addStudent`, tags `gr_create_class`, `gr_edit_class`, `gr_create_student_in_class` (L961) |
| POST | `/classes/:id/import-student` | nhập tệp, chạy queue (L1027) |
| DELETE | `/classes/student` | `removeStudent` (L900) |
| PUT | `/classes/:id/students/transfer`, `/classes/:id/students/:student_id/revert-transfer` | L547, L578; chỉ lớp LESSON |
| PUT / GET | `/classes/:id/mentors`, `/classes/:id/main-mentor`, `/classes/mentors` | `updateClassMentors` (`class.service.ts:17808`) |

Event Kafka sau khi thêm: `RESCHEDULE_FOR_STUDENT` cho từng class_user (`persistAddStudentResult`, L7684). Consumer: `apps/event-processor-service/src/app/app.controller.ts`.

## Luồng chính
1. `addStudent(studentAndIdClass, sourceType?, isSystem?, classUserType?, query_runner?)` (`class.service.ts:7767`): mặc định `MANUAL`, nhận `query_runner` ngoài.
2. Nạp `getStudentsByLevel`, `loadFoundationCourseData`, `loadFoundationClassesForLesson` (L7535).
3. Chống trùng (~L7842-7898): đã ở lớp này → invalid; đang học cùng khoá ở lớp khác → invalid trừ khi lượt kia hết hạn / type INVALID / CANCELED, hoặc lớp REVISION/FOUNDATION, supporter, Trial, lớp hiện tại ENDED. Trả `InvalidStudents[]`, không throw.
4. Lớp ENDED không bị chặn: lượt mới đánh CANCELED, không gửi mail.
5. `persistAddStudentResult` (L7684, transaction): lưu class_user, gán class quiz, cấp quyền tài nguyên; lớp chưa ENDED → `sendMailWhenAddStudent` (L13424) + `sendMailWhenAddStudentQuiz`; rồi Kafka `RESCHEDULE_FOR_STUDENT`.
6. Mail chào mừng `WELCOME_TO_CLASS` (`mail.ts:433`): gửi **ngay** khi thêm nếu lớp FLEXIBLE/NO_EXPIRED hoặc khai giảng < 5 ngày; còn lại cron 9h `sendMailWelcomeClassJobOnline` (L7958) / `sendMailWelcomeClassJob` (L8043). **Bỏ qua khi `isSystem`**, `fillback_record=1`, hoặc type INVALID.
7. `removeStudent` (L8471): `ensureClassUsersCanDelete` → `softDeleteClassUserData` (L8520) gắn `deleted_at` cho lượt ghi danh + mọi bảng con, thu hồi quyền tài nguyên, xoá cứng `user_click_events`; gỡ Lesson gỡ luôn Foundation.

## Ràng buộc ẩn
- C2 (một lượt ghi danh) do code `addStudent` giữ, không có constraint DB.
- `source_type` một giá trị → không biểu diễn "vừa thêm tay vừa qua nhóm A, B" (Q10).
- `isSystem=true` tắt mail chào mừng → luật đứng gọi với cờ này sẽ **không** gửi mail #11, trái quyết định PO "gửi bình thường" (impact-matrix vùng 9) [suy ra].
- Gỡ học viên là soft delete; dữ liệu còn trong DB nhưng mọi truy vấn TypeORM lọc đi.
- Foundation mail (#23–#26) gửi từ luồng chấm điểm (`libs/modules/src/lib/grade/grade.service.ts:578,587,1250…`), không từ ghi danh.

## Hidden / dead
- `transfer` / `revert-transfer`: PO coi là endpoint chết (impact-matrix BI-6) nhưng ops-fe có UI gọi (`features/class-and-course/src/components/classes/transfer-class/ModalTransfer.tsx`).

## Liên quan
- lms-be `openspec/conventions/backend.md` § 4, § 6.
- codekb: `lms-be/group-department.md` (support group tự ghi danh supporter), `lms-be/reporting-audit.md`.

## Bug / câu hỏi cho 2.6
- Nguồn ghi danh qua nhóm: thêm `GROUP` vào `source_type` hay bảng nối `class_user_sources(class_user_id, source, group_id)`? Q10 cần bảng nối [TEST tự chọn].
- Luật đứng gọi `addStudent` theo lô từ job nền: chọn `isSystem` sao cho vẫn gửi #11; đo hiệu năng (nạp Foundation mỗi lần).
- Mentor phụ trách đúng nhóm: `class_mentor_instances` cần cột `group_id` hoặc bảng mới.
- "Đánh dấu kết thúc" khi nghỉ việc (Q5C): `status=CANCELED` đã mang nghĩa riêng ở luồng chống trùng (lượt CANCELED cho phép thêm lại) → cần trạng thái/cờ mới.
