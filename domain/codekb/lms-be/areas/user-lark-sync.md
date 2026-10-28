---
repo: lms-be
area: user-lark-sync
branch: feature/ai_workflow (HEAD trùng origin/staging)
verified_commit: 2fbffd3
verified_date: 2026-10-10
paths: [apps/ops/src/lark, libs/modules/src/lib/user/user-lark-sync.service.ts, libs/services/src/lib/lark/lark.service.ts, apps/event-processor-service/src/commanders/sync-lark-users.command.ts, libs/database/src/lib/entities/user/user.entity.ts]
---
# lms-be · user-lark-sync

## Vị trí code
- Webhook realtime: `apps/ops/src/lark/lark-webhook.controller.ts` (`POST /lark/webhook`) → `apps/ops/src/lark/lark-webhook.service.ts`.
- Nghiệp vụ: `libs/modules/src/lib/user/user-lark-sync.service.ts` (`syncUserFromLark` L131, `updateUserFromLark` L192, `blockUserFromLark` L378, `mapLarkStatus` L459).
- Gọi API Lark: `libs/services/src/lib/lark/lark.service.ts` (`listAllDepartmentIds` L77, `listUsersByDepartment` L107, `listAllUsers` L133).
- Đồng bộ lô: lệnh CLI tay `sync-lark-users` (`apps/event-processor-service/src/commanders/sync-lark-users.command.ts`, option `-d department_id`, dry-run).

## Data
- `users.lark_union_id`, `users.status` (BLOCKED | ACTIVE | INACTIVE | DELETED | MERGED), `users.source_type` (LARK cho user tạo từ Lark) — `libs/database/src/lib/entities/user/user.entity.ts`, `libs/constants/src/lib/user/user.ts`.
- Field đồng bộ: `full_name`, `sex`, `phone`, `employee_code`, `email`, `status` (`user-lark-sync.service.ts` ~L182).
- **Không lưu phòng ban Lark** của người: `users` không có `department_id`; bảng `departments` không đồng bộ từ Lark (xem `lms-be/group-department.md`).

## API / event
| Event Lark | Xử lý |
|---|---|
| `contact.user.created_v3` | upsert user; đã có thì mở BLOCKED + relink union_id |
| `contact.user.updated_v3` | cập nhật field; `status` chỉ áp khi Lark gửi |
| `contact.user.deleted_v3` | BLOCK user + disable Keycloak + xoá session |

Chưa xử lý event `contact.department.*`; event khác ghi log "Chưa có handler" (`lark-webhook.service.ts` ~L117).

## Luồng chính
1. Middleware verify + giải mã → `handleEvent` route theo `event_type`, khử trùng theo `header.event_id` (L55, L104).
2. `mapLarkStatus`: `is_frozen || is_resigned || is_exited` → BLOCKED; không có object status → giữ nguyên.
3. `blockUserFromLark`: BLOCKED, disable Keycloak, xoá session (L378-395).
4. CLI duyệt cây phòng ban Lark chỉ để gom user, không ghi phòng ban.

## Ràng buộc ẩn
- Dấu hiệu nghỉ việc trong code = `users.status` chuyển BLOCKED (khớp Q5A đề xuất).
- Lark có thể mở lại user (ACTIVE) → "quay lại làm việc" là luồng có thật, nhóm phải xử lý vào lại.
- Không có cron đồng bộ; Q16 đề xuất "mỗi ngày một lần ban đêm" → cron mới trong `apps/background-job-service/src/app/app.controller.ts` hoặc thêm webhook department.

## Hidden / dead
- None.

## Liên quan
- lms-be `openspec/conventions/backend.md` § 5, § 4.
- codekb: `lms-be/group-department.md`.

## Bug / câu hỏi cho 2.6
- US5 cần cây phòng ban + phòng ban sâu nhất của từng người: phải thêm gọi API department Lark (scope app) và lưu `open_department_id` ↔ nhóm. Kiểm scope app Lark hiện có.
- Chọn webhook `contact.department.*` + `contact.user.updated_v3` (đổi `department_ids`) hay cron đối soát đêm; NFR US5 đòi tự hoà giải → nên cả hai [TEST tự chọn].
- BLOCKED phát sinh từ đây phải bắn sự kiện nội bộ (Kafka) để luật nghỉ việc chạy (US19); hiện `blockUserFromLark` không phát event nào.
