# Code Quality Assessment — lms-fe (focused: learner shell)

Quy trình lint/typecheck/test chuẩn của repo: `lms-fe/.claude/rules/02`, `06`, `07`, `08`. File này chỉ ghi hiện trạng kiểm được ở `origin/staging` @ `a7a5734d3`.

## Test Coverage
- **Không có test tự động**: không file `*.test.*`/`*.spec.*`, không config Jest/Vitest/Playwright (grep `git ls-tree` trên staging). Verify hiện là test tay (rules/07).
- Hệ quả cho lát: logic visibility/check-in mới không có lưới an toàn; cần dựng unit test cho hàm thuần (mapper, selector visibility) khi làm.

## Linting & Type checking
- ESLint: lms-pro `eslint:recommended` + `@typescript-eslint/recommended` + `next/core-web-vitals`, tắt `no-explicit-any` (`apps/lms-pro/.eslintrc.js:1-20`). Config chung `tools/eslint-config/`.
- `lint-staged` thiếu `apps/lms-test`, `libs/api`, `libs/HOC`, nhiều `features/*`, còn trỏ `libs/contexts` không tồn tại (`package.json:59-114`) → `libs/api/client.ts`, `libs/HOC` không bị lint khi commit.
- Typecheck: `check-types: tsc --noEmit` (`apps/lms-pro/package.json:12`); turbo task `turbo.json:20-23`.

## CI/CD
- Chỉ build + deploy Docker cho lms-pro, lms-test khi push `staging` (`.github/workflows/deploy-staging.yml:4-6,28-35`). **Không có job lint/check-types/test riêng**; kiểm type chỉ gián tiếp qua `next build` (không thấy `ignoreBuildErrors`/`ignoreDuringBuilds` trong `apps/lms-pro/next.config.js`).

## Quick ratings (vùng quét)

| Tiêu chí | Mức | Ghi chú + bằng chứng |
|---|---|---|
| Naming clarity | fair | `urser.ts` sai chính tả file (`libs/state/redux/types/User/urser.ts`); key tab `sercurity` đang dùng thật (`apps/lms-pro/src/app/[page]/page.tsx:173,205`) |
| Function size | fair | `Providers` gom DI + HubSpot DOM hack + localStorage route (`providers.tsx:138-391`); `ProfilePage` ~400 dòng (`[page]/page.tsx:60-457`) |
| Error handling | fair | Tập trung ở interceptor tốt (`libs/api/client.ts:202-226`); nhưng 403 redirect bỏ qua `silent` (L219-223); retry sau refresh không qua instance (L191); `loadMoreLoginHistory` nuốt lỗi vì thiếu `return` trước `rejectWithValue` (`libs/state/redux/slice/User/User.tsx:215-217`) |
| Typing | poor | `getMyLearnings(): Promise<any>` (`libs/api/api/courses/index.ts:77`); parse shape ở page (`courses/page.tsx:177-193`) |
| Duplication | fair | Hai lớp API cho user (`ReduxUserApi` gọi lại `AuthAPI`, `libs/api/redux/User/user.ts:13-26`) |
| Dead code | fair | Menu item bị comment (`menu-items.ts:36-43,72-78,100-131`); tab `setting` comment (`[page]/page.tsx:200-203`); `MKTInApp` comment (`providers.tsx:375`); `getListDevices` gọi trong khi `DeviceList` ẩn (`[page]/page.tsx:154,180-182`) |

## Technical Debt Signals (vùng quét)

| Signal | Vị trí | Liên quan lát |
|---|---|---|
| Menu tĩnh, không ẩn runtime được | `apps/lms-pro/src/constants/menu-items.ts:34,171`; `providers.tsx:192` | US14 trực tiếp |
| 403 luôn redirect `/` | `libs/api/client.ts:219-223` | US14 (mã lỗi khi ẩn) |
| Không có tín hiệu focus/visibility | chỉ `pagehide` `libs/api/client.ts:67-71` | US5 |
| FCM listener chỉ resolve một lần | `libs/utils/firebase.ts:47-56` | US5 toast |
| Hex hardcode trái rules/05 | `features/courses/src/components/mycourses/MyLearningHeader.tsx:54,108,140,154,160` | widget điểm sẽ đặt cạnh |
| `AuthAPI.getCertificate` đảo `page_size`/`page_index` | `libs/api/api/profile/index.ts:137-139` | ngoài lát (ghi để không mất) |
| `withAuthorization` chờ cứng 100ms, import UI tương đối | `libs/HOC/src/withAuthorization.tsx:4,14-19` | route `/gamification` sẽ dùng HOC này |
| Logout không xoá cache React Query (chỉ `localStorage.clear`) | `apps/lms-pro/src/utils/helpers/keycloak.ts:60-63` | PRD §4.1 `removeQueries(['gamification'])`; [suy ra] Keycloak logout điều hướng rời trang nên cache RAM mất theo |
| TODO "Next14" | `apps/lms-pro/src/app/layout.tsx:6`; `providers.tsx:232` | không |

## Documentation
- Comment tiếng Việt giải thích lý do khá đầy đủ ở client/auth (`libs/api/client.ts:61-87,131-135,254-291`; `services/request.ts:6-8`).
- `.claude/rules/04` lệch code về `design-tokens` (xem `dependencies.md` § Lệch tài liệu).
