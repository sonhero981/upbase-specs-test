---
repo: ops-fe
area: group-related-screens
branch: feature/ai_workflow (HEAD trùng origin/staging)
verified_commit: 1e01033bf
verified_date: 2026-10-10
paths: [features/notification/src/pages/recipients, features/department/src, features/class-and-course/src/components/classes, features/user/src/pages/student-profile, features/dashboard/src, libs/hooks/src/permission, apps/ops-fe/src/apis]
---
# ops-fe · group-related-screens

Kèm phần lms-fe (hồ sơ học viên, US17) ở cuối vì chỉ một điểm chạm.

## Vị trí code
- Module: mỗi feature là `AppModule` ở `features/<x>/src/index.ts`, đăng ký ở `apps/ops-fe/src/module-registry.ts` (viết tay; `pnpm gen` chỉ ghi đè registry ở bản copy theo khách, xem `ops-fe/settings-screens.md`). API class `apps/ops-fe/src/apis/<domain>/index.ts` dùng `fetcher` của `@ops/service`.
- Recipients List (nhóm phẳng): `features/notification/src/pages/recipients/{ListGroupReceiver,CreateAndUpdateGroup}.tsx`, components `features/notification/src/components/recipients/*`; route `/list-group`, `/create-group`, `/update-group/:id` (`features/notification/src/constant/index.ts`, `routes.tsx`).
- Phòng ban: `features/department/src/components/departments/DepartmentList/DepartmentList.tsx` (antd Table chế độ cây `expandable={{ childrenColumnName: 'child' }}` ~L357), `DepartmentForm/DepartmentForm.tsx` (chọn cha qua `hooks/useDepartmentParent.tsx`).
- Lớp: thêm học viên `features/class-and-course/src/components/classes/add-user/AddUserToClass.tsx`, `profile/user/ModalAddStudentsInClass.tsx`; nhập tệp `ModalImportClassStudent.tsx`; mentor `add-mentor/*`, `profile/user/ListMentorClass.tsx`; chuyển lớp `transfer-class/ModalTransfer.tsx`.
- Hồ sơ học viên Ops: `features/user/src/pages/student-profile/index.tsx` (tab Overview, Class & Course, Security).
- SIS dashboard: `features/dashboard/src/pages/index.tsx`, filter `features/dashboard/src/components/chart-filter/index.tsx`.

## Data
- Type `Group` ở `libs/core/src/types/groups.ts`; cây phòng ban `IDepartmentTree`, `IDepartmentTreeTable` ở `@ops/core`.

## API / event
- `NotificationAPI` (`apps/ops-fe/src/apis/notifications/index.ts`): `groups` CRUD, `groups/users`, `notifications/:id/select-groups`.
- `ClassesAPI` (`apps/ops-fe/src/apis/classes/index.ts`): `addStudentInClass` (POST `classes/students`), `deleteStudentInClass`, `transferStudentInclass` (L149), `cancelTransferStudentInClass` (L163), `getClassMentor`.
- Department API: `apps/ops-fe/src/apis/department/index.ts`. Dashboard: `apps/ops-fe/src/apis/dashboard/index.ts` (`sis-dashboard/*`).

## Luồng chính
1. Menu: `libs/hooks/src/permission/useMenuData.tsx`; mục hiện khi `visibleSidebarList` (`libs/state/src/context/SidebarContext.tsx`) chứa id **và** qua lọc quyền `allowRender.*` (`apps/ops-fe/src/constants/sidebar.ts`, `permissionsToCheck`).
2. Quyền: mã ở `libs/core/src/constants/permission.ts` (vd `VIEW_GROUP: "gr_get_groups"` L124); kiểm bằng `useHasPermission` (`libs/hooks/src/permission/useHasPermission.tsx`, đọc `profileMe.roles[].permissions`, SUPER_ADMIN luôn qua).
3. Không có guard quyền theo route (`apps/ops-fe/src/routes/AppRouter.tsx`); gate ở menu và từng nút/trang.
4. Nhập tệp dùng chung `ModalImport` (`libs/ui/src/base/upload-file/ModalImport.tsx`: `uploadUrl`, `templateFile`, `type`, poll `import-logs`).

## Ràng buộc ẩn
- Filter SIS bắt buộc `course_id` + `class_code[]` (zod ~L66-95 trong chart-filter) — báo cáo theo nhóm cần filter riêng.
- Feature flag là hằng trong code (vd `features/class-and-course/src/constants/feature-flags.ts`, `SHOW_CLASS_MENTOR_LIST=false`); không có flag theo env.
- Không có `TreeSelect` nào; cây dùng Table-tree (phòng ban) hoặc `TreeComponent` (`libs/ui/src/common/treeComponent/`).

## Hidden / dead
- Danh sách mentor ở màn tạo/sửa lớp ẩn bởi `SHOW_CLASS_MENTOR_LIST=false`.

## Liên quan
- ops-fe `.claude/rules/*`, `.claude/inventory/*`.
- lms-fe (US17): hồ sơ học viên `apps/lms-pro/src/app/[page]/page.tsx` (tab `my-profile`), component `features/user/src/components/profile/MyProfile.tsx` (`@lms/feature-user`); dữ liệu `GET me` (`libs/api/api/profile/index.ts` ~L59) → `IUser` (`libs/state/redux/types/User/urser.ts` L16) chưa có trường nhóm/quản lý; lms-fe không có tham chiếu nhóm, phòng ban, mentor nào. Convention ở lms-fe `.claude/rules`, `.claude/inventory`.
- codekb: `lms-be/group-department.md`, `lms-be/authz-tenant.md`, `lms-be/class-enrollment.md`.

## Bug / câu hỏi cho 2.6
- Màn cây nhóm: tái dùng mẫu Table-tree của `DepartmentList.tsx` (dựng lại component, không import chéo feature) [suy ra].
- Ẩn Recipients List (Q17): bỏ id khỏi `SidebarContext`/`sidebarIds` hay đổi quyền; nhóm thông báo vẫn dùng ở màn tạo thông báo (`components/notification/createNotiComponent/AddGroupToNoti.tsx`) → ẩn menu không đủ.
- US17 ở lms-fe cần API mới trả quản lý/mentor của học viên (LMS guard), không có sẵn.
