# Code Quality Assessment

> Chỉ vùng lát. Thang good/fair/poor theo `code-analysis-guide.md`.

## Test Coverage

- **Không có test**: 0 file `*.test|spec.ts(x)` trên `origin/staging`; có devDeps `@testing-library/*` và `apps/ops-fe/src/setupTests.ts:1-5` nhưng không có script `test` (`apps/ops-fe/package.json` scripts). `tsconfig.checker.json:10` loại `*.spec.ts`/`*.test.ts`.
- Verify thực tế: test tay + typecheck (ops-fe `.claude/rules/07-testing-patterns.md`).

## Linting & Typecheck

- ESLint 9 flat (`apps/ops-fe/eslint.config.mjs`), lint-staged hai tầng: root `eslint --fix` (`package.json` mục `lint-staged`), app `prettier` + `eslint --max-warnings=0` (`apps/ops-fe/package.json` mục `lint-staged`).
- `request.ts:1` tắt `no-explicit-any` toàn file; `UserProvider.tsx:19` tắt cục bộ.

## CI/CD

- GitHub Actions `deploy-staging.yml` (push `staging`, L3-7) và `deploy-production.yml`: install → `vite build` (L68) → đóng gói → deploy. **CI không chạy lint, typecheck, test** (build gọi thẳng `vite build`, bỏ qua `pnpm lint` của script `build`).
- `.gitlab-ci.yml` (root và `apps/ops-fe/`) còn sót.

## Documentation

- README có ở root và `apps/ops-fe`. Comment tiếng Việt giải thích quyết định ở các file auth/tenant khá tốt (`index.tsx:11-17`, `tenant-theme.ts:43-73`, `access-denied/index.tsx:37-43`).

## Quick Assessment (vùng lát)

| Tiêu chí | Mức | Bằng chứng |
|---|---|---|
| Naming clarity | fair | `isSupperAdmin` sai chính tả (`UserProvider.tsx:40`); nút "Previous Page" gọi `logOut` (`access-denied/index.tsx:27-31`) |
| Function size | poor | `useMenuData.tsx` 1720 dòng, switch lồng theo id (L898-978) |
| Error handling | fair | Toast tập trung (`request.ts:197-270`) nhưng 422 im lặng (L216) → form phải tự hiện lỗi 422 |
| Test presence | poor | không test |
| Duplication | fair | Mẫu confirm + revert viết tay mỗi chỗ (`StaffTitleTable.tsx:62-76`) |
| Dead code | fair | `pages/setting` placeholder; `ID_SIDE_BAR.SETTING` không dùng; route đổi mật khẩu comment (`AppRouter.tsx:6-10,55-58`) |

## Technical Debt (liên quan lát)

1. `HookFormSwitch` bỏ qua `disabled` (`libs/ui/src/base/switch/HookFormSwitch.tsx:6`) — US8/BR-14.7 cần khoá switch.
2. `NumberField` biến ô rỗng thành `minNumber` (`NumberField.tsx:82-85`) và `HookFormNumberField` lưu `0` khi `undefined` (`HookFormNumberField.tsx:59`) — trái `BR-14.11` (rỗng phải báo lỗi, không lưu). Không lộ `onBlur`/`onKeyDown` ra ngoài (`HookFormNumberField.tsx:11-38`).
3. Không guard quyền theo trang (`AppRouter.tsx:28-43`).
4. `useAppMutation` không có chống race (`use-app-mutation.tsx:41-62`) — PRD §7 yêu cầu.
5. `use-confirm.tsx:2` import tương đối chéo package.
6. `generate-customer.js` thiếu `feature-marketing` trong hai map (L18-52) trong khi registry có (`module-registry.ts:8,33`); L194 lặp `config.features` thay vì `finalFeatures` (L81-83) nên feature bắt buộc không vào registry bản copy nếu config không liệt kê [suy ra].

## Lệch so với settings-screens.md cũ (verified 1e01033bf)

- "Mẫu lưu ngay khi **toggle** có xác nhận" (`StaffTitleTable`): thực ra là **select** trạng thái (`StaffTitleTable.tsx:118-126`), revert đoán bằng đảo ACTIVE/INACTIVE. Chưa có mẫu switch → API nào; `HookFormSwitch` có `onSubmit` chỉ cập nhật form local (`FilesTable.tsx:238-245`).
- "xoá ô lưu `0`": đúng một nửa — xoá ô phát `minNumber` (mặc định 0) (`NumberField.tsx:84`); đặt `minNumber=1` thì xoá ô thành `1`, không bao giờ rỗng.
- "không có prop `onBlur`/`onKeyDown` tuỳ biến": `NumberFieldInput` có `onKeyDown` (`NumberField.tsx:28,104-108`), chỉ `HookFormNumberField` không truyền.
- `filterMenuEngagement` `default` ở L971 (cũ ghi L970). Các `file:line` còn lại khớp.

## Lệch PRD

- PRD §7 (`SettingsFooter`, `saveOrder.ts`, Save chung) trái `BR-14.10/14.13` — PRD tự cảnh báo; nhánh WIP làm theo Save chung.
- PRD §3.2 yêu cầu `PermissionRoute` + `AccessDenied` theo trang: staging chưa có (chỉ ở nhánh WIP).
- PRD endpoint `/api/v1/gamification/*`: base URL thực của Ops là `…/ops/api/v1/` (`apps/ops-fe/.env.example:1`).
