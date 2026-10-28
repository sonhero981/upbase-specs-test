# Reverse Engineering Timestamp

## Run Record

- Date: 2026-10-11 · làm mới 2026-10-13: CURRENT (a7a5734d3..b2cc49455 chỉ sửa `.github/workflows/deploy-production.yml`)
- Commit: a7a5734d3 (`origin/staging`, 2026-10-07 "Fix/uplms sprint 1/grading issues fix conflict (#67)")
- Repo: lms-fe
- Intent: 260923-gamification — lát US14, US8, US5
- Breadth: focused scan (`kind: partial`), depth Minimal. Lead-only: developer lead làm cả scan lẫn synthesis (Step 3 lead-only path)
- Cách đọc: `git show|grep|ls-tree origin/staging:…`; không checkout, không đọc working tree (đang ở `feature/ai_workflow`)
- Prior store: không có store 9 file chuẩn AWS. Điểm xuất phát là codekb vùng cũ `upbase-specs/.claude/knowledge/tech/codekb/lms-fe/areas/learner-shell.md` (verified a7a5734d3, 2026-10-10, không có Scope of Analysis → coi như UNKNOWN_SCOPE). Đã kiểm lại từng khẳng định bằng code; file đó **đã chuyển vào `areas/` (11/10/2026)**
- Fingerprint: Upbase không cài engine AI-DLC (`codekb-scope-diff` không có); freshness = `commit` + `analyzed.paths`: CURRENT khi `git -C lms-fe log --oneline a7a5734d3..origin/staging -- <analyzed.paths>` rỗng
- Ghi chú phạm vi: `apps/lms-pro/src/app/[page]/page.tsx` đọc sâu L60-215 + grep phần còn lại; `libs/utils/firebase.ts` đọc L25-56; `libs/state/redux/types/User/urser.ts` đọc L1-90

### Đối chiếu learner-shell.md cũ
- Khớp: providers `providers.tsx:340-389`, `client-layout.tsx:17-52`, `RouteGuard.tsx:22-82`, `menu-items.ts`, `[page]/layout.tsx`, `client.ts:42-53,114-123,212-223`, `FeatureContext.tsx:34-105`, My Profile `[page]/page.tsx:82,157-210`.
- Bổ sung: `getMe` đi qua `ReduxUserApi.getMe` (`libs/api/redux/User/user.ts:13-17`) rồi mới tới `AuthAPI.me()`; retry sau refresh bỏ qua interceptor (`libs/api/client.ts:191`); có lớp branding tenant `@upbase-tech/design-tokens` + `useTenantBranding` (`libs/hooks/useTenantTheme.ts:23-24`) mà file cũ chỉ ghi `PREVIEW_BRANDING = null`; format ngày theo giờ thiết bị, không plugin timezone (`libs/utils/common.ts:30-38`).
- Không thấy lệch sai.

## WIP branches

| Branch | Commit | Ngày | Chạm vùng | Ghi chú |
|---|---|---|---|---|
| `origin/feature/uplms-sprint-2/gamification-feature` | 61f5dd914 | 2026-10-09 | `features/gamification/*` (mock), `apps/lms-pro/src/app/gamification/page.tsx`, `libs/hooks/useGamificationVisibility.ts`, `libs/ui/layout/Sidebar/index.tsx`, `apps/lms-pro/src/constants/menu-items.ts`, `apps/lms-pro/src/app/courses/page.tsx`, `apps/lms-pro/src/app/[page]/page.tsx`, `apps/lms-pro/src/app/client-layout.tsx`, `apps/lms-pro/src/app/module-registry.ts`, `apps/lms-test/src/app/providers.tsx`, root `package.json` (lint-staged) | 4 commit chưa merge; thiếu 2 commit của staging (fb3b68733, a7a5734d3). **Không coi là code đã có** |
| `origin/feature/ai_workflow` | 69efa37e7 | 2026-10-08 | Không (tài liệu `.claude/`) | — |

## Scope of Analysis

```yaml
scope_version: 1
kind: partial
intent: 260923-gamification
fingerprint: unknown (Upbase không cài engine; freshness = commit + analyzed.paths)
commit: b2cc49455
analyzed:
  paths:
    - apps/lms-pro/src/app/layout.tsx
    - apps/lms-pro/src/app/providers.tsx
    - apps/lms-pro/src/app/client-layout.tsx
    - apps/lms-pro/src/app/tenant-branding.ts
    - apps/lms-pro/src/app/module-registry.ts
    - "apps/lms-pro/src/app/[page]/"
    - apps/lms-pro/src/app/courses/page.tsx
    - apps/lms-pro/src/constants/menu-items.ts
    - apps/lms-pro/src/services/request.ts
    - apps/lms-pro/src/utils/helpers/keycloak.ts
    - apps/lms-pro/src/redux/services/User/
    - features/auth/src/components/RouteGuard.tsx
    - features/courses/src/components/mycourses/MyLearningHeader.tsx
    - libs/api/client.ts
    - libs/api/constants.ts
    - libs/api/index.ts
    - libs/api/api/profile/
    - libs/api/redux/User/
    - libs/HOC/src/
    - libs/state/redux/slice/User/
    - libs/state/redux/types/User/
    - libs/state/contexts/FeatureContext.tsx
    - libs/ui/layout/Sidebar/
    - libs/ui/layout/MenuItemsList/index.tsx
    - libs/utils/firebase.ts
    - libs/hooks/useTenantTheme.ts
  components:
    - RootLayout
    - ProvidersWrapper
    - ClientLayout
    - FeatureContext
    - AuthManager
    - RouteGuard
    - withAuthorization
    - HttpClient
    - AuthAPI
    - CoursesAPI
    - userSlice
    - MENU_ITEMS
    - Sidebar
    - MenuItemsList
    - DynamicPageLayout
    - MyCourse
    - MyLearningHeader
    - ProfilePage
    - useTenantBranding
shallow:
  paths:
    - package.json
    - pnpm-workspace.yaml
    - turbo.json
    - .github/workflows/
    - tools/eslint-config/
    - apps/lms-pro/package.json
    - apps/lms-pro/next.config.js
    - apps/lms-pro/.eslintrc.js
    - apps/lms-pro/src/constants/routers.ts
    - apps/lms-pro/src/api/courses/
    - libs/api/api/courses/
    - libs/api/api/user/
    - libs/api/api/notification/
    - libs/state/redux/slice/Login/Login.tsx
    - libs/ui/layout/MenuItem/
    - libs/ui/layout/Notification/
    - libs/hooks/useNotification.tsx
    - libs/utils/helpers/index.ts
    - libs/utils/common.ts
    - libs/utils/tenant-theme.ts
    - libs/core/constants/User.ts
```
