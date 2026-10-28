# Technology Stack

> Version theo `package.json` trên `origin/staging`. Danh sách đầy đủ: ops-fe `.claude/rules/04-imports-and-dependencies.md` (không chép lại).

## Languages & Runtime

| Thành phần | Version | Nguồn |
|---|---|---|
| TypeScript | `^5.8.3` | `apps/ops-fe/package.json:122` |
| Node (CI) | 20 | `.github/workflows/deploy-staging.yml:41` |
| pnpm | `9.0.0` | `package.json:3`, `deploy-staging.yml:35` |

## Frameworks

| Thành phần | Version | Dùng trong lát | Nguồn |
|---|---|---|---|
| React | `18.2.0` | toàn bộ | `apps/ops-fe/package.json:65` |
| Vite | `^6.2.5` | build/dev, proxy `/api` | `apps/ops-fe/package.json:124`, `apps/ops-fe/vite.config.ts:45-51` |
| react-router-dom | `^6.11.2` | `AppRouter` | `apps/ops-fe/package.json:71` |

## Libraries chạm tới lát

| Library | Version | Vai trò | Nguồn |
|---|---|---|---|
| react-query | `3.38.0` (v3 API) | server state, `useAppMutation` | `apps/ops-fe/package.json:70` |
| react-hook-form | `^7.55.0` | form, `Controller` trong `HookForm*` | `apps/ops-fe/package.json:68` |
| zod | `^3.24.2` | schema validate | `apps/ops-fe/package.json:78` |
| axios | `0.26.1` | `libs/service/src/request.ts` | `apps/ops-fe/package.json:53` |
| antd | `^5.24.3` | `Modal` (`PopupConfirm`), `Popover`, `Skeleton` | `apps/ops-fe/package.json:52`, `libs/ui/package.json:13` |
| bootstrap | `^5.3.3` | class `form-switch` của `HookFormSwitch` | `libs/ui/package.json:15` |
| react-number-format | `^5.4.4` | `NumberField` | `libs/ui/package.json:56` |
| react-hot-toast | `^2.6.0` | toast success/lỗi (`Toaster` portal `index.tsx:115`) | `apps/ops-fe/package.json:69` |
| dayjs (+ `utc`) | `^1.11.7` | format ngày; không dùng plugin `timezone` | `apps/ops-fe/package.json:56`, `libs/utils/src/common.ts:12-16` |
| `@upbase-tech/auth-package` | `1.0.1` | Keycloak `initAuth`, `AuthProvider` | `apps/ops-fe/package.json:48` |
| `@upbase-tech/tenant-context` | `1.0.0` | `initTenant`, `tenantContextFromMe`, `getTenantManager` | `apps/ops-fe/package.json:50` |
| `@upbase-tech/design-tokens` | `1.0.0` | `applyTokens` theme theo tenant | `apps/ops-fe/package.json:49` |

## UI kit

Metronic (`libs/_metronic`, `@ops/_metronic`) + Bootstrap class + antd 5 + wrapper `@ops/ui`. Không có Popconfirm wrapper (xem `component-inventory.md` › PopupConfirm).

## Build & Tooling

- Build: `vite build` → `apps/ops-fe/build` (`vite.config.ts:53-56`); script `build` chạy `pnpm lint` trước (`apps/ops-fe/package.json:132`), CI gọi thẳng `vite build` (`deploy-staging.yml:68`).
- Typecheck: `tsc -p tsconfig.checker.json --noEmit` (`apps/ops-fe/package.json` script `typecheck:base`; `apps/ops-fe/tsconfig.checker.json:1-11`).
- Lint: ESLint 9 flat config `apps/ops-fe/eslint.config.mjs` + `.eslintrc.js` cũ ở root.
- Test: devDeps `@testing-library/*` (`apps/ops-fe/package.json` devDependencies) + `src/setupTests.ts`, **không có test runner script, 0 file `*.test|spec.ts(x)`**.
