# Code Structure — lms-fe (focused: learner shell)

Layout monorepo, alias `@lms/*`, quy tắc đặt code: xem `lms-fe/.claude/rules/01-code-placement.md` và `04-imports-and-dependencies.md`. Workspace khai ở `pnpm-workspace.yaml:1-7` (`apps/lms-pro|lms-zoom|lms-test`, `features/*`, `libs/*`, `tools/*`).

## Packages chạm trong vùng quét

| Package | Path | Vai trò trong learner shell |
|---|---|---|
| `lms-pro` | `apps/lms-pro/` | App: layout, providers, routes, menu, cấu hình HTTP/Keycloak |
| `@lms/feature-auth` | `features/auth/` | `RouteGuard` |
| `@lms/feature-courses` | `features/courses/` | `MyLearningHeader` (+ list khoá, popup) |
| `@lms/api` | `libs/api/` | HttpClient, API class, `ReduxUserApi` |
| `@lms/contexts` | `libs/state/` | Redux slices (`User`, `Login`…), `FeatureContext` |
| `@lms/hoc` | `libs/HOC/` | `withAuthorization` |
| `@lms/ui` | `libs/ui/` | `Layout`, `Sidebar`, `MenuItemsList`, `MenuItem` |
| `@lms/utils`, `@lms/hooks`, `@lms/core` | `libs/utils/`, `libs/hooks/`, `libs/core/` | `makeMenuLevel`, FCM, `formatDate`, `useTenantBranding`, constants |

## File Classification (vùng quét)

| Loại | File |
|---|---|
| Configuration / bootstrap | `apps/lms-pro/src/app/layout.tsx`, `apps/lms-pro/src/app/providers.tsx`, `apps/lms-pro/src/app/module-registry.ts`, `apps/lms-pro/src/app/tenant-branding.ts`, `apps/lms-pro/src/constants/menu-items.ts` |
| Middleware (auth/HTTP) | `libs/api/client.ts`, `apps/lms-pro/src/services/request.ts`, `apps/lms-pro/src/utils/helpers/keycloak.ts`, `features/auth/src/components/RouteGuard.tsx`, `libs/HOC/src/withAuthorization.tsx` |
| Controller (route/page) | `apps/lms-pro/src/app/courses/page.tsx`, `apps/lms-pro/src/app/[page]/layout.tsx`, `apps/lms-pro/src/app/[page]/page.tsx`, `apps/lms-pro/src/app/client-layout.tsx` |
| Repository (API access) | `libs/api/api/profile/index.ts`, `libs/api/api/courses/index.ts`, `libs/api/redux/User/user.ts`, `apps/lms-pro/src/redux/services/User/user.ts` (re-export) |
| Model / state | `libs/state/redux/slice/User/User.tsx`, `libs/state/redux/slice/Login/Login.tsx`, `libs/state/redux/types/User/urser.ts`, `libs/state/contexts/FeatureContext.tsx` |
| UI component | `libs/ui/layout/Sidebar/index.tsx`, `libs/ui/layout/MenuItemsList/index.tsx`, `features/courses/src/components/mycourses/MyLearningHeader.tsx` |
| Utility | `libs/utils/firebase.ts`, `libs/utils/helpers/index.ts` (`makeMenuLevel` L119-129), `libs/utils/common.ts` (`formatDate` L33-38), `libs/hooks/useTenantTheme.ts` |

## Code Patterns

- **Re-export lớp app**: app không tự viết API mà re-export từ `@lms/api` (`apps/lms-pro/src/api/courses/index.ts:1`, `apps/lms-pro/src/redux/services/User/user.ts:1`). Default export đi qua tên riêng ở barrel (`libs/api/index.ts:20-26`).
- **Static API class**: `class AuthAPI { static me() }` (`libs/api/api/profile/index.ts:53-60`); object literal cho bản cũ (`MyProfileAPI`, L10-51).
- **Thunk nhận API qua tham số** để `libs/state` không phụ thuộc app: `getMe(api: IUserContextAPI)` (`libs/state/redux/slice/User/User.tsx:95-109`).
- **Query inline ở page** (không có hook/query-key tập trung): `useQuery({ queryKey: ['myLearnings'] … })` (`apps/lms-pro/src/app/courses/page.tsx:169-175`).
- **Lazy component cho popup/third-party** qua `next/dynamic` (`apps/lms-pro/src/app/providers.tsx:74-96`).
- **Route động một cấp có whitelist**: `[page]` chỉ nhận slug trong `MYPROFILE_TREE`/`SECURITY_TREE`, còn lại `notFound()` (`apps/lms-pro/src/app/[page]/layout.tsx:6,22-24`; `libs/core/constants/User.ts:60-61`).
- **Tab state cục bộ**: My Profile giữ `activeTab` bằng `useState`, không đọc URL (`apps/lms-pro/src/app/[page]/page.tsx:82,134-143`).
- **Lệch rules**: `withAuthorization` import UI bằng đường dẫn tương đối `'../../ui'` thay vì `@lms/ui` (`libs/HOC/src/withAuthorization.tsx:4`).

## Điểm nối sẵn cho lát gamification

| Nhu cầu | Điểm nối | Bằng chứng |
|---|---|---|
| Menu item mới | `MENU_OPTIONS` | `menu-items.ts:7-132` |
| Ẩn menu | `showMenu` (tĩnh) | `menu-items.ts:34`; `MenuItem/index.tsx:379` |
| Widget My Learning | `MyLearningHeader` + `IMyLearning` | `MyLearningHeader.tsx:13-17,151-163`; `courses/page.tsx:177-193` |
| Tab My Profile | `items`, `getTabContent`, `mobileOverviewItems` | `[page]/page.tsx:157-210,274` |
| Bootstrap sau mount | `ClientLayout` (tương tác đầu) | `client-layout.tsx:17-52` |
| Module theo khách hàng | `modules` registry | `module-registry.ts:10-16` |
