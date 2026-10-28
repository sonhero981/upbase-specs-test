---
repo: lms-be
area: authz-tenant
branch: feature/ai_workflow (HEAD trùng origin/staging)
verified_commit: 2fbffd3
verified_date: 2026-10-10
paths: [apps/ops/src/auth, libs/modules/src/lib/permission, libs/modules/src/lib/scan-operation, libs/services/src/lib/casbin, libs/database/src/lib/entities/casbin, libs/database/src/lib/entities/role, libs/database/src/lib/extends, apps/lms/src/auth, libs/modules/src/lib/lms-permission]
---
# lms-be · authz-tenant

## Vị trí code
- Guard Ops: `apps/ops/src/auth/guard/staff.guard.ts` → `apps/ops/src/auth/ops-auth.service.ts` (`authorize`).
- Kiểm quyền: `libs/modules/src/lib/permission/permission.service.ts` (`checkCanAcceptRoles` ~L88, `scanAndSyncPermissions` L57).
- Quét quyền: `libs/modules/src/lib/scan-operation/scan-operation.service.ts`, gọi từ `apps/ops/src/permissions/permissions.service.ts` `onModuleInit` (L30).
- Guard LMS: `apps/lms/src/auth/guard/lms.guard.ts`; kiểm tài nguyên `libs/modules/src/lib/lms-permission/lms-permission.service.ts` (L38). LMS không dùng Casbin.
- Tenant: `libs/database/src/lib/extends/` (`tenant-context.service.ts`, `request-query-runner.middleware.ts`, `tenant-id.subscriber.ts`, `tenant-ownership.service.ts`).

## Data
- `casbin_rule` (`libs/database/src/lib/entities/casbin/casbin.entity.ts`): `ptype`, `v0..v6`, `tenant_id`. `g`+`v2='g-p'` = định nghĩa quyền (v0 key, v3 tên, v4 nhóm module, v5 ACTIVE/INACTIVE); `g`+`v2='p-r'` = vai trò → quyền; `p` = quyền → (path, method). Hằng `libs/constants/src/lib/casbin/casbin.ts`.
- `roles` (`libs/database/src/lib/entities/role/role.entity.ts`): `code`, `name`, `is_group` (false chỉ cho superadmin, điều kiện hiện UI — không liên quan chức năng Nhóm).
- `role_staff_instances` (`.../role-staff-instances/role-staff-instances.entity.ts`): staff N-N role.
- `staffs` là định danh Ops, `users` là định danh LMS; `staffs` không có `user_id` (`libs/database/src/lib/entities/staff/staff.entity.ts`).
- Cờ trên `users` (`libs/database/src/lib/entities/user/user.entity.ts`): `is_operator`, `is_supporter`, `is_super_student`. Không có loại "Test Account": `USER_TYPES` chỉ STUDENT/TEACHER (`libs/constants/src/lib/user/user.ts`).

## API / event
- Khai quyền bằng metadata Swagger: `@UseGuards(StaffGuard)` + `@ApiOperation({ security: [{ group, name, display_name, description, isScan: ['true'] }], tags: [<key được gọi>] })` — mẫu `apps/ops/src/groups/group.controller.ts:60-87`, quy ước ghi ở `apps/ops/src/department/department.controller.ts` L32-43.
- Không có migration/seed quyền: Ops khởi động → quét controller → ghi `casbin_rule` từng tenant (bỏ qua khi `NODE_ENV=LOCAL`).

## Luồng chính
1. `StaffGuard.canActivate`: identity từ gateway header, không có thì verify Bearer Keycloak.
2. `OpsAuthService.authorize`: kiểm `azp`, tìm staff theo `keycloak_user_id`, `bindTenant`, nạp role, whitelist (`libs/constants/src/lib/role/role.ts`).
3. `checkCanAcceptRoles`: route **chưa có dòng `p` → cho qua**; có thì role → nhóm quyền → route.
4. Tenant: middleware đọc `x-tenant-id` → CLS + `set_config('app.tenant_id')`; RLS `tenant_isolation_<table>` (`libs/database/migrations/1789930000000-enable-rls-on-tenant-tables.ts`); `TenantIdSubscriber.beforeInsert` tự điền `tenant_id`; job dùng `runForEachTenant`.

## Ràng buộc ẩn
- Enforcer Casbin (`libs/services/src/lib/casbin/casbin.module.ts`, `assets/model.conf`) không dùng lúc request; kiểm quyền là truy vấn tay.
- **Không có data scope chung.** Chỉ có lọc ad-hoc: facility manager (`apps/ops/src/request-schedules/receptionist-request.service.ts` ~L265), grading theo staff (`apps/ops/src/quiz-attempt-grading/quiz-attempt-grading.controller.ts`, ghi chú "không phân quyền casbin").
- Bảng mới có `tenant_id` phải thêm RLS policy theo mẫu migration trên.

## Hidden / dead
- `staff_user_management` (staff ↔ giảng viên, `libs/database/src/lib/entities/staff-user-instances/staff-user-instances.entity.ts`) và `staff_business_unit_management`: không thấy dùng để lọc dữ liệu [suy ra từ grep].

## Liên quan
- lms-be `openspec/conventions/backend.md` § 2, § 3; `database.md` § 3 (RLS).
- codekb: `lms-be/group-department.md`, `ops-fe/group-related-screens.md`.

## Bug / câu hỏi cho 2.6
- Rủi ro: endpoint mới quên `tags` thì mở cho mọi staff. Phần lớn `/departments` đang như vậy.
- Phạm vi theo nhánh (US16, BR-9.3) phải tự xây ở tầng service — Casbin hiện tại không làm được.
- Quản lý/mentor là `staffs`, học viên là `users`, không có khoá nối người thật giữa hai bảng. PRD "Tài khoản tách theo vai trò" khớp với điều này nhưng US17 (hồ sơ học viên hiện quản lý) phải đọc chéo staffs.
- PRD loại "tài khoản kiểm thử" khỏi mọi logic: code không có khái niệm này; gần nhất là `is_operator` / `is_super_student` / `classes.is_test_class` → cần PO chốt cờ nào [TEST tự chọn: `is_operator`].

## Đường sinh quyền từ code (kiểm 2026-10-13, `origin/staging` 610f100)
- Ops khởi động → `PermissionCommonService.scanAndSyncPermissions` (`libs/modules/src/lib/permission/permission.service.ts:57`) → `ScanOperationService.discoverControllers` → ghi `casbin_rule` cho từng tenant (`runForEachTenant`, bỏ qua khi `NODE_ENV=LOCAL`, L58-61).
- **Định nghĩa quyền (`g`, `g-p`) lấy từ `@ApiOperation.security[0]`**: `scan-operation.service.ts:91-93` gom `security[0]`; `createDefaultGroupPermissions` (`permission.service.ts:317`) ghi `v0 = security.name[0]` (L364), `v3 = display_name[0]` (L367), `v4 = security.group[0]` (L368), `v5 = ACTIVE` (L369). Quyền này hiện trên màn role Ops qua `GET /permissions` (`apps/ops/src/permissions/permissions.controller.ts:31`, nhóm theo `v4`).
- **Gắn route vào quyền (`p`) lấy từ `@ApiOperation.tags`**: `scan-operation.service.ts:101` `group = tags ?? []`; L145-152 sinh dòng `p` với `v0 = tag`, `v1 = route`, `v2 = method`. `tags: []` → route không có dòng `p` → `checkCanAcceptRoles` cho qua mọi staff (`permission.service.ts:94-105`).
- Hệ quả cho Gamification (US15): khai `security` đủ thì ba quyền xuất hiện trên màn role ngay (BR-15.1 không cần sửa màn); nhưng nếu giữ `tags: []` theo `openspec/conventions/backend.md` § 2 thì gán quyền cho role **không chặn được route** (trái BR-15.3) cho tới khi `tags` có mã quyền.
