# Technology Stack — lms-fe

Stack đầy đủ và quy ước dùng: `lms-fe/.claude/rules/04-imports-and-dependencies.md` (Key Dependencies), `05-ui-and-styling.md`. Bảng dưới chỉ ghi version kiểm được ở `origin/staging` @ `a7a5734d3` cho phần chạm learner shell.

## Runtime & build

| Thành phần | Version | Bằng chứng |
|---|---|---|
| Node | `20.x` | `package.json:55-57` |
| pnpm | `10.22.0` | `package.json:58` |
| Turborepo | `^2.10.2` | `package.json:52`; tasks `turbo.json:4-27` |
| TypeScript | `^5.9.3` (catalog) | `pnpm-workspace.yaml` catalog |
| Next.js | `^14.2.35` (App Router) | `apps/lms-pro/package.json:78` |
| React | `18.2.0` root / `^18.2.0` lms-pro | `package.json:126`; `apps/lms-pro/package.json:83` |

## Libraries (vùng learner shell)

| Library | Version | Dùng cho | Bằng chứng |
|---|---|---|---|
| `react-query` | `3.39.3` (v3 API) | server state | `package.json:129`; `apps/lms-pro/src/app/providers.tsx:33,109-116` |
| `@reduxjs/toolkit` / `react-redux` | `^1.9.7` / `^8.1.3` | client state (`userSlice`) | `apps/lms-pro/package.json:51,92` |
| `axios` | `^1.6.2` | HTTP client | `apps/lms-pro/package.json:63`; `libs/api/client.ts:2-7` |
| `@upbase-tech/auth-package` | `1.0.1` | Keycloak `initAuth`, `AuthProvider` | `apps/lms-pro/package.json:53`; `keycloak.ts:5,32` |
| `keycloak-js` | `^25.0.1` | adapter (qua auth-package) | `apps/lms-pro/package.json:75` |
| `@upbase-tech/design-tokens` | `1.0.0` | branding/token CSS theo tenant | `apps/lms-pro/package.json:54`; `layout.tsx:3`; `providers.tsx:56` |
| `@upbase-tech/upbase-notification` | `^1.0.6` | UI drawer thông báo | `apps/lms-pro/package.json:58` |
| `firebase` | `^10.7.1` | FCM push | `apps/lms-pro/package.json:72`; `libs/utils/firebase.ts:31-56` |
| `antd` | `^5.25.0` | UI primitives | `apps/lms-pro/package.json:61` |
| `dayjs` | `^1.11.12` (plugin `utc`, `weekday`, `relativeTime`; **không** `timezone`) | format ngày | `apps/lms-pro/package.json:67`; `providers.tsx:22-24,98-99`; `MyLearningHeader.tsx:2-6` |
| `react-hot-toast` | — | toast lỗi HTTP + app | `libs/api/client.ts:8`; `providers.tsx:32,354-360` |
| `zod` | `^3.22.4` | schema form | `apps/lms-pro/package.json:103` |
| `@sentry/nextjs` | `^10.35.0` | error monitoring | `apps/lms-pro/package.json:52`; `apps/lms-pro/next.config.js:2` |
| `tailwindcss` + `tailwind-merge` | catalog / `^3.3.1` | styling | `apps/lms-pro/package.json:100,128` |

## Không có (đã grep trên staging)

- `socket.io-client`, WebSocket, EventSource, `refetchInterval`: không có trong `apps/lms-pro`, `libs`, `features` (grep `socket.io|EventSource|WebSocket|refetchInterval`).
- dayjs `timezone` plugin hoặc `.tz(`: không có.
- Test runner (Jest/Vitest/Playwright): không có file `*.test.*`/`*.spec.*` hay config. Xem `code-quality-assessment.md`.

## Deploy

Docker multi-stage + GitHub Actions, chỉ lms-pro và lms-test (`.github/workflows/deploy-staging.yml:28-35`). Chi tiết: `lms-fe/.claude/rules/06-commands-and-workflow.md` § CI/CD.
