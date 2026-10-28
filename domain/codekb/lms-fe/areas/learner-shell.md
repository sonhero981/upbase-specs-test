---
repo: lms-fe
area: learner-shell
branch: origin/staging
verified_commit: a7a5734d3
verified_date: 2026-10-10
paths: [apps/lms-pro/src/app, apps/lms-pro/src/constants, apps/lms-pro/src/api/courses, features/auth/src/components, features/courses/src/components/mycourses, libs/api/client.ts, libs/api/api/courses, libs/api/api/profile, libs/api/redux/User, libs/state/contexts/FeatureContext.tsx, libs/state/redux/slice/User, libs/state/redux/types/User, libs/ui/layout/Sidebar, libs/ui/layout/MenuItem, libs/ui/layout/Notification, libs/utils/firebase.ts, libs/hooks/useNotification.tsx, libs/core/constants/User.ts]
---
# lms-fe · learner-shell

Khung app học viên lms-pro. Convention (stack, alias, placement) ở lms-fe `.claude/rules/*` + `.claude/inventory/*`, không chép lại.

## Vị trí code
- Providers: `apps/lms-pro/src/app/providers.tsx:340-389`; layout `layout.tsx:135-143`; `client-layout.tsx:17-52`.
- Guard: `features/auth/src/components/RouteGuard.tsx:22-82`.
- My Learning: route `/courses` `apps/lms-pro/src/app/courses/page.tsx` (`withAuthorization([STUDENT])` L343), header `features/courses/src/components/mycourses/MyLearningHeader.tsx`.
- Menu: `apps/lms-pro/src/constants/menu-items.ts:7-175`; Sidebar `libs/ui/layout/Sidebar/index.tsx:30,104-107`; render `libs/ui/layout/MenuItem/index.tsx:379`.
- Dynamic route: `apps/lms-pro/src/app/[page]/layout.tsx:6-24`; My Profile `apps/lms-pro/src/app/[page]/page.tsx`.
- HTTP client: `libs/api/client.ts`.

## Data
- My Learning: `CoursesAPI.getMyLearnings()` → `fetcher('courses/my-learnings')`, trả `any` (`libs/api/api/courses/index.ts:77-78`). Query inline `['myLearnings']`, `retry:false, staleTime:0, refetchOnMount:'always'` (`courses/page.tsx:169-175`); map `course_count`/`test_count`/`last_login` → `IMyLearning {courses, assessments, lastLogin?}` (`page.tsx:177-193`; type `MyLearningHeader.tsx:13-17`). Header render 2 `StatItem` + Last login (`MyLearningHeader.tsx:112-163`), chưa có slot điểm/hạng.
- User: `IUser` `libs/state/redux/types/User/urser.ts:16-49` (`type` STUDENT/TEACHER L78-81). **Không có** `is_operator`/`is_super_student`/cờ test. `getMe.fulfilled` merge toàn bộ payload vào store (`libs/state/redux/slice/User/User.tsx:228-233`).
- **Không có** feature flag / tenant config đọc từ BE. `FeatureContext` (`libs/state/contexts/FeatureContext.tsx:34-105`) là DI container (API class, `menuItems`, router…), không chứa flag. Branding tĩnh `PREVIEW_BRANDING = null` (`apps/lms-pro/src/app/tenant-branding.ts:3`).

## API / event
- `GET me`: `RouteGuard.tsx:58` → thunk `getMe` (`User.tsx:95-109`) → `AuthAPI.me()` `fetcher('me')` (`libs/api/api/profile/index.ts:58-60`).
- Notification: `getCountUnRead` + FCM `onMessageListener` sau tương tác đầu tiên (`client-layout.tsx:17-52`); FCM ở `libs/utils/firebase.ts:31-56`, SW `apps/lms-pro/public/firebase-messaging-sw.js`. `@upbase-tech/upbase-notification` chỉ là UI drawer (`libs/ui/layout/Notification/NotificationDrawer.tsx:8-11`). Không polling, không `refetchInterval`.
- **Không có** `socket.io-client` / WebSocket / EventSource trong package.json các app hay code.

## Luồng chính
1. `layout.tsx` → `ProvidersWrapper` → QueryClient (defaults `staleTime: 3000000`, `refetchOnWindowFocus: false`, `providers.tsx:109-116`) → `AuthProvider` (L363-368) → `RouteGuard` (L369).
2. `RouteGuard` effect theo `pathname`; store có `user.id` thì return (L35-44), chưa có thì `getMe` → thực tế `GET /me` chạy **một lần mỗi lần tải trang** [suy ra].
3. Tương tác đầu tiên (`pointerdown|keydown|touchstart|scroll`, `once`) → bootstrap notification (`client-layout.tsx:38-45`).
4. Menu: `MENU_OPTIONS` → `makeMenuLevel` (`libs/utils/helpers/index.ts:119`) → `FeatureContext.menuItems` (`providers.tsx:167-210`) → Sidebar → `MenuItem` ẩn khi `showMenu === false`.
5. HTTP lỗi: toast khi `!silent && !toastExceptions.includes(code) && !isSilentError` (`client.ts:212-218`).

## Ràng buộc ẩn
- `showMenu` là hằng tính lúc import (`menu-items.ts:34,140`, dựa `module-registry.ts:10-16` tĩnh) → không ẩn/hiện menu runtime theo tenant được nếu không đổi `menuItems` thành động.
- **Mọi mã `403*` redirect `window.location.href = '/'`, kể cả request `silent`** (`client.ts:219-223`). 404 không xử lý riêng → toast `statusText` nếu không `silent`. `toastExceptions` ở `client.ts:42-53`.
- **Không có listener `visibilitychange`/`focus`** trong apps/features/libs; chỉ `pagehide` để chặn toast (`client.ts:67-71`). `refetchOnWindowFocus: true` chỉ bật lẻ (vd `courses/my-course/[courseId]/results/page.tsx:75`).
- `[page]` chỉ nhận slug `overview|devices|login_history|change_password` (`libs/core/constants/User.ts:60-61`), slug khác `notFound()` (`[page]/layout.tsx:22-24`), `generateStaticParams` chỉ `overview` (L8-11) → route mới phải là folder riêng.
- My Profile: `activeTab` state không đọc URL (`[page]/page.tsx:82`); tab ở `items` (L193-210), `getTabContent` (L157-191), `mobileOverviewItems` (L274-318); key `sercurity` sai chính tả đang dùng thật.
- `MyLearningHeader` hardcode hex (`#3370FE`, `#10B367`…), trái rules/05.

## Giới hạn hạ tầng
- Tenant: FE không gửi header tenant (request interceptor chỉ gắn `Authorization`, `client.ts:114-123`); tenant do BE suy từ user.
- Dedupe: không có cơ chế chống gọi trùng giữa nhiều tab.
- Realtime: chỉ FCM; `onMessageListener` trả Promise nên chỉ resolve **một lần** (`libs/utils/firebase.ts:47-56`, `client-layout.tsx:30-32`).
- Cache: React Query v3, stale 50 phút mặc định.

## Hidden / dead
- Tab `setting` trong My Profile bị comment (`[page]/page.tsx:193-210`).

## Liên quan
- lms-fe `.claude/rules/01-code-placement.md` (không đặt business logic trong `libs/`), `03-architecture-patterns.md`, `.claude/inventory/*`.
- codekb: `lms-be/learner-presence.md`, `lms-be/tenant-config.md`, `ops-fe/group-related-screens.md` (hồ sơ học viên).
- Nhánh **`origin/feature/uplms-sprint-2/gamification-feature`** (chưa merge, 61f5dd914, 2026-10-09): `features/gamification/*` chạy mock, `apps/lms-pro/src/app/gamification/page.tsx`, `libs/hooks/useGamificationVisibility.ts` (đọc cache `['gamification','me']`), Sidebar lọc runtime; sửa `menu-items.ts`, `courses/page.tsx`, `[page]/page.tsx`, `client-layout.tsx`, lms-test providers. Staging đi trước nhánh 2 commit.

## Bug / câu hỏi cho 2.6
- Visibility (US14): PRD §8 định 404 khi ẩn; **không được dùng 403** vì client redirect về `/` (`client.ts:219-223`). Mọi call gamification phải `silent: true`.
- Check-in (US5) "chủ động mở/quay lại": FE chưa có điểm bám; phải thêm `visibilitychange`/tương tác đầu (mẫu `client-layout.tsx:38-45`). `GET /me` không chạy lại khi quay lại tab nên không dùng làm tín hiệu được.
- Toast realtime: FCM chỉ bắt tin foreground đầu → hoặc sửa `onMessageListener` thành subscribe, hoặc socket mới (PRD §5 chọn socket.io, BE chưa có gateway).
- Nhánh gamification đặt `useGamificationVisibility` ở `libs/hooks` (PRD §2.1 cũng vậy) — trái rules/01; HLD chốt có chấp nhận ngoại lệ không.
