# Component Inventory — lms-fe (focused: learner shell)

Chỉ component trong vùng quét. Inventory đầy đủ `@lms/*`: `lms-fe/.claude/inventory/01..05`. Tên heading dùng verbatim trong `analyzed.components`.

## Bootstrap & providers

### RootLayout
- **Responsibility:** server shell, font, CSS token tenant (khi có branding), `Suspense` toàn cục cho static export.
- **Location:** `apps/lms-pro/src/app/layout.tsx:111-147`
- **Depends on:** `ProvidersWrapper`, `ClientLayout`, `@upbase-tech/design-tokens.renderTokenCss` (L3,117-119).

### ProvidersWrapper
- **Responsibility:** Redux `Provider` + chuỗi provider (AntConfig → PinnedNotify → Feature → Course → CourseNote → QueryClient → AuthProvider → RouteGuard → PreviousSectionRoute → AntdApp) + popup toàn cục.
- **Location:** `apps/lms-pro/src/app/providers.tsx:138-399`
- **Depends on:** `QueryClient` (L109-116), `auth` (L58), `MENU_ITEMS` (L47-51,192), `modules` (L61,205).

### ClientLayout
- **Responsibility:** sau tương tác đầu (`pointerdown|keydown|touchstart|scroll`, `once`) lấy count-unread và lắng FCM foreground.
- **Location:** `apps/lms-pro/src/app/client-layout.tsx:9-55`
- **Depends on:** `getCountUnRead`, `showNotification` (`@lms/contexts`), `onMessageListener` (`libs/utils/firebase.ts:47-56`).

### FeatureContext
- **Responsibility:** DI container: API class, `authManager`, `menuItems`, `router`, `pathname`, `dispatch`, `appModules`. Không chứa feature flag.
- **Location:** `libs/state/contexts/FeatureContext.tsx:34-105`; giá trị `apps/lms-pro/src/app/providers.tsx:167-210`

## Auth & phân quyền

### AuthManager
- **Responsibility:** `initAuth` Keycloak (url/realm/clientId từ env), public route chứng chỉ, xoá cookie cũ, đăng ký FCM token sau login, logout BE + xoá localStorage.
- **Location:** `apps/lms-pro/src/utils/helpers/keycloak.ts:32-64`
- **Depends on:** `@upbase-tech/auth-package` 1.0.1, `UserApi.logout`.

### RouteGuard
- **Responsibility:** chặn render tới khi có user; store trống thì `getMe`. Lỗi `/me` → giữ loading (`authorized=false`).
- **Location:** `features/auth/src/components/RouteGuard.tsx:11-91`
- **Depends on:** `useFeature().userContextApi`, `getMe`, `userReducer`.

### withAuthorization
- **Responsibility:** HOC theo `user.type`; chờ cứng 100ms; `/` → điều hướng theo vai trò; sai vai trò → `router.replace(COURSES)` và render `null`.
- **Location:** `libs/HOC/src/withAuthorization.tsx:6-53`

## Data / HTTP

### HttpClient
- **Responsibility:** axios instance dùng chung: gắn Bearer, refresh 401 qua hàng đợi, toast lỗi, redirect 403.
- **Location:** `libs/api/client.ts:89-252`; cấu hình lms-pro `apps/lms-pro/src/services/request.ts:9-27`
- **Contract:** xem `api-documentation.md` § Error contract.

### AuthAPI
- **Responsibility:** `me`, hồ sơ, devices, activities, pinned notifications, đổi mật khẩu.
- **Location:** `libs/api/api/profile/index.ts:53-169`

### CoursesAPI
- **Responsibility:** danh sách khoá, `getMyLearnings`, catalog.
- **Location:** `libs/api/api/courses/index.ts:67-95` (phần đọc)

### userSlice
- **Responsibility:** state `user`, `loginHistory`; `getMe.fulfilled` merge nguyên payload.
- **Location:** `libs/state/redux/slice/User/User.tsx:13-93,95-109,220-320`; type `libs/state/redux/types/User/urser.ts:16-49`

## Navigation

### MENU_ITEMS
- **Responsibility:** cấu hình menu học viên (`MENU_OPTIONS` → `makeMenuLevel`), `MENU_BOTTOM` cho mobile. `showMenu` tính lúc import.
- **Location:** `apps/lms-pro/src/constants/menu-items.ts:7-175`

### Sidebar
- **Responsibility:** render logo, `menuItems`, `menuBottom` (mobile), overlay guide.
- **Location:** `libs/ui/layout/Sidebar/index.tsx:21-140`
- **Depends on:** `useFeature()` (L30-31), `MenuItemsList` (L104-111,123-128).

### MenuItemsList
- **Responsibility:** map option → `MenuItem` (có `url`) hoặc `NotificationMenuItem` (không `url`). Không lọc.
- **Location:** `libs/ui/layout/MenuItemsList/index.tsx:13-44`; ẩn ở `libs/ui/layout/MenuItem/index.tsx:379`

### DynamicPageLayout
- **Responsibility:** route `[page]`: whitelist slug profile, slug khác `notFound()`; `generateStaticParams` chỉ `overview`.
- **Location:** `apps/lms-pro/src/app/[page]/layout.tsx:1-27`

## Màn học viên

### MyCourse
- **Responsibility:** trang My Learning `/courses`: infinite list khoá + query `['myLearnings']` → `IMyLearning`.
- **Location:** `apps/lms-pro/src/app/courses/page.tsx:46-343` (`withAuthorization([STUDENT])` L343)

### MyLearningHeader
- **Responsibility:** tiêu đề, `Last login` (`fromNow`, giờ thiết bị), 2 `StatItem` Courses/Tests. Chưa có slot điểm/hạng. Hex hardcode.
- **Location:** `features/courses/src/components/mycourses/MyLearningHeader.tsx:13-17,112-166`

### ProfilePage
- **Responsibility:** My Profile: tab `my-profile`, `sercurity` (login history); `setting` bị comment; `activeTab` state cục bộ.
- **Location:** `apps/lms-pro/src/app/[page]/page.tsx:60-457`

## Tenant

### useTenantBranding
- **Responsibility:** đọc branding từ store của `@upbase-tech/design-tokens`, fallback `UPBASE_BRANDING`. Chưa có nguồn branding từ BE.
- **Location:** `libs/hooks/useTenantTheme.ts:20-44`; nguồn tĩnh `apps/lms-pro/src/app/tenant-branding.ts:3`
