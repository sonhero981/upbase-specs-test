---
repo: lms-be
area: group-department
branch: feature/ai_workflow (HEAD trùng origin/staging)
verified_commit: 2fbffd3
verified_date: 2026-10-10
paths: [libs/database/src/lib/entities/group, libs/database/src/lib/entities/group-user-instances, libs/modules/src/lib/group, apps/ops/src/groups, libs/database/src/lib/entities/department, libs/modules/src/lib/department, apps/ops/src/department, libs/database/src/lib/entities/support-group, libs/modules/src/lib/support-group]
---
# lms-be · group-department

## Vị trí code
- Nhóm phẳng: `apps/ops/src/groups/group.controller.ts` → `apps/ops/src/groups/group.service.ts` → `libs/modules/src/lib/group/group.service.ts` (`GroupCommonService`). Repo `libs/database/src/lib/repositories/group/group.repository.ts`, `group-user.repository.ts`. DTO `libs/interface/src/lib/dto/group/group.dto.ts`.
- Phòng ban: `apps/ops/src/department/department.controller.ts` → `libs/modules/src/lib/department/department.service.ts`.
- Support group (Comment Replier): `apps/ops/src/support-group/*`, `libs/modules/src/lib/support-group/support-group.service.ts`.

## Data
- `groups` (`libs/database/src/lib/entities/group/group.entity.ts`): `tenant_id`, `name` (1000), `search_vector` (tsvector) + `id/created_at/updated_at/deleted_at` từ `AbstractEntity` (`libs/database/src/lib/entities/abstract/abstract.entity.ts`). Không có cha con, nguồn, trạng thái lưu trữ, quản lý.
- `group_user_instances` (`.../group-user-instances/group-user-instances.entity.ts`): `group_id`, `user_id`, `@Unique(['group_id','user_id'])`, FK CASCADE, không có `tenant_id`, không có thời điểm vào/ra ngoài `created_at`.
- `notification_group_instances` (`.../notification-group-instances/notification-group-instances.entity.ts`): `notification_id`, `group_id`, FK CASCADE về `groups`.
- `departments` (`.../department/department.entity.ts`): Nested Set — `tree_id` (= id gốc), `left`, `right`, index (`left`,`right`); `name`, `short_name`, `code` (unique theo tenant), `type` (cấp bậc), `unit_id` → business_units. `parent_id`/`child` chỉ để trả về.
- Chỉ `staffs.department_id` trỏ vào `departments` (`libs/database/src/lib/entities/staff/staff.entity.ts`). `users` không có quan hệ phòng ban (`libs/database/src/lib/entities/user/user.entity.ts`).
- Support group: `support_groups` (`course_category_id`, `display_name`, `avatar`) + `support_group_user_instances` (`libs/database/src/lib/entities/support-group/*`).

## API / event
| Method | Path (ops) | Quyền (`tags`) |
|---|---|---|
| GET | `/groups`, `/groups/:id`, `/groups/:id/users`, `/groups/:id/select-users` | `gr_get_groups` … |
| POST / DELETE | `/groups/users` | |
| POST / PUT / DELETE | `/groups`, `/groups/:id` | `gr_create_group`, `gr_edit_group`, `gr_remove_group` |
| GET | `/departments`, `/departments/parent-list`, `/departments/list-unit`, `/departments/:id`, `/departments/:id/positions` | phần lớn `tags: []` → không có dòng `p`, mọi staff gọi được |
| POST / PUT / DELETE | `/departments`, `/departments/:id`, `/departments` (xoá lô), `/departments/:id/assign-position` | |

Nhóm phẳng chỉ phục vụ người nhận thông báo: `libs/modules/src/lib/notification/notification.service.ts` (~L221, L481, L1249-1268, DTO `groups: string[]`). Không chỗ nào khác tham chiếu.

## Luồng chính
1. Tạo nhóm: `CreateGroupDto(name, users?)` → `GroupCommonService.createGroup`.
2. Gỡ thành viên: `GroupCommonService.removeUserFromGroup` (`libs/modules/src/lib/group/group.service.ts:323-345`) xoá cứng `.delete()` trên `group_user_instances`.
3. Xoá nhóm: `deleteGroup` (L280) `softDelete`.
4. Cây phòng ban: `createDepartment` (L344) dịch `left/right` +2; `updateDepartment` (L423) tính lại cả cây khi đổi cha/cây; `removeDepartments` (L573) chỉ xoá lá rồi tính lại; `getAvailableParentList` (L56) loại cây con bằng `left/right`; `validateDepartmentData` (L646) ép thứ bậc `type` cố định (`DEPARTMENT_TYPES`).
5. Support group: thêm supporter → `addSupporterToClass` (`libs/modules/src/lib/support-group/support-group.service.ts` L897) ghi danh supporter vào một lớp mỗi khoá cùng category, bật `users.is_supporter` (L860); cron 2h sáng `handleSupporterClassUser` (`apps/background-job-service/src/app/app.controller.ts` L146). Đây là "luật đứng" duy nhất đang chạy.

## Ràng buộc ẩn
- Unique (`group_id`,`user_id`) + `deleted_at`: không lưu được nhiều lần vào/ra của cùng người trong cùng nhóm.
- Nested Set sửa cây = cập nhật hàng loạt `left/right` cả cây; `type` phòng ban theo thứ bậc cố định, không khớp "nhóm tự tạo cắt ngang cơ cấu" [suy ra].
- Department không đồng bộ từ Lark (xem `lms-be/user-lark-sync.md`), chỉ CRUD tay trên Ops.

## Hidden / dead
- Màn "Recipients List" (ops-fe) là UI của `/groups`; PO chốt bỏ (DEC24).

## Liên quan
- lms-be `openspec/conventions/database.md`, `backend.md` § 1.
- codekb: `lms-be/class-enrollment.md`, `lms-be/authz-tenant.md`, `ops-fe/group-related-screens.md`.

## Bug / câu hỏi cho 2.6
- Bug: `removeUserFromGroup` không `await` lệnh delete và không chạy qua `query_runner` → transaction vô tác dụng (`libs/modules/src/lib/group/group.service.ts:334-345`).
- Tái dùng `groups` (thêm cột) hay entity mới? Đổi `groups` kéo theo `notification_group_instances`. Đề xuất entity mới + bảng lịch sử thành viên (`joined_at`, `left_at`, `reason`) [TEST tự chọn].
- Dùng lại Nested Set của `departments` cho cây nhóm hay adjacency list + closure/CTE đệ quy? Cây nhóm cần lịch sử cha con theo thời gian (Q2) — Nested Set không giữ lịch sử.
