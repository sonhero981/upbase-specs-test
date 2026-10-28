# Business Overview — lms-fe (focused: learner shell)

> Focused scan cho intent `260923-gamification`, lát US14 (công tắc theo tenant), US8 (cấu hình điểm), US5 (điểm vào hệ thống hằng ngày). Đọc theo `origin/staging` @ `a7a5734d3`. Mọi `file:line` theo commit đó.

## Business Context

lms-fe là monorepo FE của UpLMS (pnpm + Turborepo). Ba app Next.js 14: `lms-pro` (app học viên/giáo viên), `lms-test` (app làm bài thi), `lms-zoom` (không có trong CI). Convention repo ở `lms-fe/.claude/rules/*` và `.claude/inventory/*` — không chép lại.

Vùng quét này là **khung app học viên lms-pro** (learner shell): nơi mọi màn học viên đi qua, và là nơi gamification sẽ được bật/ẩn theo công tắc của tổ chức.

## Business Transactions (trong vùng quét)

| Transaction | Mô tả | Điểm vào code |
|---|---|---|
| Mở app / bootstrap phiên | Keycloak init → lấy hồ sơ `GET /me` → mở khoá render | `apps/lms-pro/src/app/providers.tsx:363-369`, `features/auth/src/components/RouteGuard.tsx:22-82` |
| Điều hướng bằng Sidebar | Menu tĩnh theo `MENU_OPTIONS` | `apps/lms-pro/src/constants/menu-items.ts:7-175`, `libs/ui/layout/Sidebar/index.tsx:104-111` |
| Xem My Learning | Header số khoá/bài test/last login + danh sách khoá | `apps/lms-pro/src/app/courses/page.tsx:169-193`, `features/courses/src/components/mycourses/MyLearningHeader.tsx:112-166` |
| Xem My Profile | Tab hồ sơ + bảo mật (login history) ở route động `/overview` | `apps/lms-pro/src/app/[page]/page.tsx:157-210` |
| Phân quyền theo vai trò | STUDENT/TEACHER, sai vai trò → về `/courses` | `libs/HOC/src/withAuthorization.tsx:21-44` |
| Đăng xuất | Keycloak logout + `POST auth/logout` + xoá localStorage | `apps/lms-pro/src/utils/helpers/keycloak.ts:57-63`, `libs/state/redux/slice/Login/Login.tsx:21-31` |
| Nhận thông báo | Đếm chưa đọc + FCM foreground sau tương tác đầu | `apps/lms-pro/src/app/client-layout.tsx:17-52` |

## Business Dictionary

| Thuật ngữ | Nghĩa trong code | Nguồn |
|---|---|---|
| User type | `STUDENT` / `TEACHER` | `libs/state/redux/types/User/urser.ts:78-81` |
| My Learning | Route `/courses` (`PageLink.COURSES`) | `apps/lms-pro/src/constants/routers.ts:3` |
| My Profile | Route `/overview` (`PageLink.MYPROFILE`) qua dynamic route `[page]` | `apps/lms-pro/src/constants/routers.ts:25`, `libs/core/constants/User.ts:60-61` |
| App module | Module bật theo bản build khách hàng (schedule, test, certificate…) | `apps/lms-pro/src/app/module-registry.ts:10-16` |
| Branding / tenant theme | Màu theo tổ chức qua `@upbase-tech/design-tokens`; hiện `PREVIEW_BRANDING = null` | `apps/lms-pro/src/app/tenant-branding.ts:3`, `libs/hooks/useTenantTheme.ts:23-24` |

## Liên hệ với lát gamification

- **US14 (công tắc):** FE hiện **không có** khái niệm feature flag hay cấu hình theo tenant đọc từ BE. Ẩn/hiện chỉ có `showMenu` tĩnh lúc import (`menu-items.ts:34`). Chi tiết ở `architecture.md` § Infrastructure Constraints.
- **US8 (cấu hình điểm):** màn cấu hình nằm ở ops-fe, **không** thuộc lms-fe. lms-fe chỉ tiêu thụ kết quả (điểm/hạng trên My Learning, PRD §4.1).
- **US5 (điểm vào hệ thống):** FE không có tín hiệu "học viên chủ động mở/quay lại". `GET /me` chỉ chạy khi store trống (`RouteGuard.tsx:35-44,57-58`). Xem `architecture.md` § Interaction Diagrams.
- Code chưa có gamification trên `origin/staging`. Nhánh dở dang ghi ở `reverse-engineering-timestamp.md` § WIP branches.

## Ngoài phạm vi quét

Course/activity player, test, certificate, teacher, lms-test, lms-zoom. Xem `reverse-engineering-timestamp.md` § Scope of Analysis.
