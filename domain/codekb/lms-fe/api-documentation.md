# API Documentation — lms-fe (focused: learner shell)

lms-fe không expose HTTP API. Hai bề mặt: **API consumed** (lms-be REST + Keycloak) và **internal surface** (export của `@lms/*` mà vùng quét dùng). Base URL `NEXT_PUBLIC_BASE_API_URL` (`libs/api/client.ts:93-95`, `libs/api/constants.ts:1`). Response shape BE: đọc trực tiếp lms-be (codekb `lms-be`), không đoán ở đây.

## API consumed (lms-be, trong vùng)

Mọi call qua `fetcher` → Bearer token Keycloak (`apps/lms-pro/src/services/request.ts:11-24`), timeout 30s (`libs/api/client.ts:98`), 304 hợp lệ (L101).

| Method | Path | Gọi từ | Khi nào | FE đọc field | Bằng chứng |
|---|---|---|---|---|---|
| GET | `/me` | `AuthAPI.me()` ← `ReduxUserApi.getMe` ← `getMe` thunk | `RouteGuard` khi store chưa có `user.id` | toàn bộ `IUser` (merge) | `libs/api/api/profile/index.ts:58-60`; `libs/api/redux/User/user.ts:13-17`; `features/auth/src/components/RouteGuard.tsx:57-58` |
| GET | `/courses/my-learnings` | `CoursesAPI.getMyLearnings()` | Mount My Learning, `staleTime: 0` | `course_count`, `test_count` (số hoặc `"c/t"`), `last_login` | `libs/api/api/courses/index.ts:77-78`; `apps/lms-pro/src/app/courses/page.tsx:169-193` |
| GET | `/courses?page_index&page_size` | `CoursesAPI.get` | Danh sách khoá My Learning (infinite) | — | `libs/api/api/courses/index.ts:67-75`; `courses/page.tsx:150-167` |
| GET | `/users/activities` | `AuthAPI.getListHistory` | My Profile mount (`type: 'login'`) | `meta`, `userActivities` | `libs/api/api/profile/index.ts:131-135`; `apps/lms-pro/src/app/[page]/page.tsx:145-155` |
| GET | `/users/devices` | `AuthAPI.getListDevices` | My Profile mount (UI `DeviceList` đang ẩn) | — | `profile/index.ts:117-119`; `[page]/page.tsx:129-132,154,180-182` |
| GET | `/notifications/count-unread` | `NotificationAPI.getCountUnRead` | Sau tương tác đầu tiên | — | `libs/api/api/notification/index.ts:4-5`; `apps/lms-pro/src/app/client-layout.tsx:29` |
| GET | `/notifications/pinned` | `AuthAPI.getPinnedNotifications` | `PinnedNotifyProvider` | — | `profile/index.ts:166-168`; `apps/lms-pro/src/app/providers.tsx:342-347` |
| POST | `/auth/logout` | `UserApi.logout(session_id, keycloak_user_id)` | `onBeforeLogout` của Keycloak | — | `libs/api/api/user/index.ts:43-53`; `apps/lms-pro/src/utils/helpers/keycloak.ts:57-58` |
| POST | `{KEYCLOAK_URL}realms/{realm}/user-session-provider/sessions/device` | `setDeviceFirebaseToSession` | Sau login, `silent: true` | — | `keycloak.ts:68-79` |

**Chưa có trên staging:** mọi endpoint `/api/v1/gamification/*` (PRD §API). Chưa có field điểm/hạng trong `courses/my-learnings` mà FE đọc (`courses/page.tsx:188-192`).

## Error contract FE áp lên mọi call

| Điều kiện | Hành vi | Bằng chứng |
|---|---|---|
| Lỗi có `error.code` dạng `<status>` + `<code>` nối bằng dấu gạch đứng (vd `400`·`100016`) | Toast message từ `ExceptionErrorCode`, fallback `statusText` | `libs/api/client.ts:148,205-218` |
| `config.silent === true` | Không toast | `client.ts:12-13,213` |
| Mã trong `toastExceptions` | Không toast | `client.ts:42-53,214` |
| 401 không mã hoặc mã chung `000000`, cancel, đang `pagehide` | Không toast | `client.ts:78-86` |
| 401 | Refresh 1 lần qua Keycloak rồi retry | `client.ts:155-196` |
| Mã bắt đầu `403` | `window.location.href = '/'`, **không xét `silent`** | `client.ts:219-223` |
| 404 | Không xử lý riêng → toast nếu không `silent` | `client.ts:205-218` |

## Internal surface (`@lms/*` dùng trong vùng)

| Export | Package | Chữ ký / nội dung | Bằng chứng |
|---|---|---|---|
| `configureHttpClient(config)` | `@lms/api` | `{ apiURL, getAuthHeader, refreshAuth? }` → `{ request, fetcher, fetchFormData }` | `libs/api/client.ts:17-40,262-265` |
| `fetcher(url, cfg?)` | `@lms/api` | trả `res.data`; `cfg.silent?: boolean` | `client.ts:107-112,276-277` |
| `getRequest()` | `@lms/api` | AxiosInstance đang active | `client.ts:291` |
| `AuthAPI`, `MyProfileAPI`, `CoursesAPI`, `UserApi`, `NotificationAPI`, `ReduxUserApi` | `@lms/api` | static class / object | `libs/api/index.ts:1-26` |
| `getMe`, `userReducer`, `getLogoutUser` | `@lms/contexts` | thunk Redux | `libs/state/redux/slice/User/User.tsx:95-109`; `libs/state/redux/slice/Login/Login.tsx:21-31` |
| `useFeature()`, `FeatureProvider` | `@lms/contexts` | DI context, xem `component-inventory.md` | `libs/state/contexts/FeatureContext.tsx:99-105` |
| `withAuthorization(roles)(Component)` | `@lms/hoc` | HOC theo `user.type` | `libs/HOC/src/withAuthorization.tsx:6-53` |
| `RouteGuard` | `@lms/feature-auth` | bọc children, gate theo `/me` | `features/auth/src/components/RouteGuard.tsx:11-91` |
| `makeMenuLevel(options)` | `@lms/utils` | gán `id`, `depth` cho `MenuOption[]` | `libs/utils/helpers/index.ts:119-129` |
| `onMessageListener()` | `@lms/utils/firebase` | Promise resolve tin FCM đầu tiên | `libs/utils/firebase.ts:47-56` |
| `useTenantBranding()` | `@lms/hooks` | branding hiện hành, fallback Upbase | `libs/hooks/useTenantTheme.ts:23-24` |
| `IUser`, `UserType` | `@lms/contexts` | type user, không có cờ Test Account | `libs/state/redux/types/User/urser.ts:16-49,78-81` |
