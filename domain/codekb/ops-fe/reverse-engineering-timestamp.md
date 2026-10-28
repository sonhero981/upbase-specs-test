# Reverse Engineering Timestamp

## Run Record

- Date: 2026-10-11 · làm mới 2026-10-13: CURRENT (không có commit mới), quét thêm màn role
- Commit: 1e01033bf (`origin/staging`, 2026-10-08 "Fix/uplms sprint 1/grading issues fix conflict (#61)")
- Repo: ops-fe (`E:\UP_BASE\ops-fe`), đọc bằng `git show|grep|ls-tree origin/staging`, không checkout
- Breadth: focused scan (kind: partial) — vùng settings / permission theo trang / menu / HTTP + auth / tenant / form controls cho intent `260923-gamification` lát US14, US8, US5
- Depth: Minimal
- Pipeline: lead-only (developer lead quét + tổng hợp 9 artifact)
- Store trước đó: không có codekb chuẩn 9 file cho ops-fe (NO_STORE). Điểm xuất phát là codekb vùng cũ `knowledge/tech/codekb/ops-fe/areas/settings-screens.md` (verified 1e01033bf), đã kiểm lại từng `file:line`; điểm lệch ở `code-quality-assessment.md`. File vùng cũ đã chuyển vào `areas/` (11/10/2026).
- Fingerprint: Upbase không cài engine `codekb-scope-diff`; freshness = `commit` + `analyzed.paths` (CURRENT khi `git -C ops-fe log --oneline 1e01033bf..origin/staging -- <analyzed.paths>` rỗng).
- Left out: `node_modules/`, `apps/ops-fe/build/`, `.claude/` (harness).

## WIP branches

| Nhánh | Commit | Ngày | Chạm vùng | Ghi chú |
|---|---|---|---|---|
| `origin/feature/uplms-sprint-1/gamification-feature` | `b5378f278` | 2026-10-07 | Có | Chưa merge vào staging; 124 file, +4744/−77. Có `features/gamification` (Settings 5 khối + Learners, **mock** `mocks/mockRequest.ts`), `libs/ui/src/common/permission-route/{PermissionRoute,PageAccessDenied}.tsx` (`PermissionRoute` trả `null` khi chưa có `profileMe`). Lưu theo **nút Save chung** (`hooks/useSaveSettings.ts:19-23`, `utils/saveOrder.ts`) — trái `BR-14.10/14.13`. Không coi là code đã có |
| `origin/feature/ops-keycloak-sso` | `763f31d41` | 2026-10-05 | Không | Diff so với staging không chạm file trong vùng |
| `origin/fix/uplms-sprint-1/grading-issues` | `0ddd42088` | 2026-10-07 | Không | Như trên |

## Scope of Analysis

```yaml
scope_version: 1
kind: partial
intent: 260923-gamification
fingerprint: unknown
commit: 1e01033bf
analyzed:
  paths:
    - apps/ops-fe/src/index.tsx
    - apps/ops-fe/src/bootstrap.ts
    - apps/ops-fe/src/module-registry.ts
    - apps/ops-fe/src/routes/
    - apps/ops-fe/src/components/access-denied/index.tsx
    - apps/ops-fe/src/pages/setting/index.tsx
    - apps/ops-fe/src/services/auth.ts
    - apps/ops-fe/src/apis/user/index.ts
    - apps/ops-fe/src/apis/roles/index.ts
    - features/role/src/components/roles/add-role/AddRole.tsx
    - features/role/src/components/roles/detail/PermissionDetail.tsx
    - scripts/generate-customer.js
    - libs/service/src/request.ts
    - libs/state/src/context/UserProvider.tsx
    - libs/state/src/context/SidebarContext.tsx
    - libs/HOC/src/
    - libs/hooks/src/permission/useHasPermission.tsx
    - libs/hooks/src/permission/usePermissions.ts
    - libs/hooks/src/permission/useMenuData.tsx
    - libs/hooks/src/use-app-mutation.tsx
    - libs/hooks/src/use-confirm.tsx
    - libs/ui/src/base/switch/
    - libs/ui/src/base/numberfield/
    - libs/ui/src/common/PopupConfirm.tsx
    - libs/utils/src/tenant-theme.ts
    - libs/core/src/types/tenant-theme.ts
    - libs/core/src/types/common.ts
    - libs/core/src/constants/permission.ts
    - libs/core/src/constants/queryKeyFactory/index.ts
    - libs/core/src/constants/queryKeyFactory/departmentKeys.ts
    - features/notification/src/index.ts
    - features/notification/src/routes.tsx
    - features/department/src/components/title/StaffTitleTable.tsx
    - features/class-and-course/src/components/courses/course-detail/create-tabs/TabNavItem.tsx
  components:
    - module-registry
    - generate-customer
    - AppRouter
    - OpsAccessGate
    - withAuthComponents
    - SettingPage
    - UserProvider
    - SidebarProvider
    - auth
    - request
    - tenant-theme
    - useHasPermission
    - usePermissions
    - useMenuData
    - permission-constants
    - HookFormSwitch
    - HookFormNumberField
    - NumberField
    - useAppMutation
    - useConfirm
    - PopupConfirm
    - queryKeyFactory
    - StaffTitleTable
    - TabNavItem
shallow:
  paths:
    - package.json
    - pnpm-workspace.yaml
    - apps/ops-fe/package.json
    - apps/ops-fe/vite.config.ts
    - apps/ops-fe/tsconfig.checker.json
    - apps/ops-fe/eslint.config.mjs
    - apps/ops-fe/.env.example
    - apps/ops-fe/src/App.tsx
    - apps/ops-fe/src/setupTests.ts
    - apps/ops-fe/src/constants/
    - .github/workflows/
    - libs/ui/package.json
    - libs/utils/src/common.ts
    - libs/core/src/types/form.ts
    - features/class-and-course/src/components/question-bank/grading-ai/FilesTable.tsx
    - configs/
    - libs/core/src/enums/upload.ts
```
