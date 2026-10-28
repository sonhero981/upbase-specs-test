---
intent: 260923-gamification
unit: u0-foundation
bolt: B01
artifact: code-generation-plan
stage: 3.5 code-generation (Part 1 — Planning)
version: 1.1
status: approved
approved_at: 2026-10-13 (FE lead + [GIẢ LẬP] BE lead, DEC-T13; sửa theo review-code-generation-01, DEC-T14)
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả) · BE lead Đoàn Quang Cường (soi chéo lms-be, giả lập)
owner_bolt: Nguyễn Hùng Sơn
consumes: ../functional-design/ v1.0 (DEC-T11) · ../ui-map/ui-map.md v1.0 Provisional (DEC-T12) · inception/contract-design/contract-summary.md v1.0 Agreed (DEC-T8) · inception/test-cases/test-cases.md v1.0 (DEC-T9) · inception/delivery-planning/bolt-plan.md B01 · codekb lms-be @610f100 + WP0 `origin/feature/gamification` @65d3aad (DEC-T14), ops-fe @1e01033bf
---
# Code Generation Plan: U0 `u0-foundation` (Bolt B01)

## Summary
- Builds (delta trên WP0 lms-be): cột `visibility_first_enabled_at`, service đọc/ghi + cache Redis, C-01 GET / C-02 PATCH có khai quyền (`tags`); ops-fe feature `@ops/feature-gamification`, menu theo 3 quyền, trang khối chung hai công tắc + popover + `Saved`.
- Touches: lms-be `libs/database` (1 migration, entity), `libs/constants`, `libs/exceptions`, `libs/interface`, `libs/modules/src/lib/gamification/settings/`, `apps/ops/src/gamification-setting/`, `openspec/conventions/backend.md`; ops-fe `features/gamification/`, `apps/ops-fe/src/apis/gamification/`, `libs/core`, `libs/state`, `libs/hooks`, `libs/ui` (HookFormSwitch), `libs/service/src/en.exceptions.json`.
- Tests: unit test service lms-be; 3 curl; ops-fe `/ui-gate review` + typecheck + Playwright MCP theo TC.

## Cách đọc
- Plan là bản gốc; `tasks.md` của change `run` ở lms-be, ops-fe = checklist section repo đó. Lệch plan: dừng, sửa plan ở store (FE + BE lead duyệt), ghi `progress.md`.
- Thứ tự: lms-be → ops-fe. ops-fe mock theo C-01, C-02 (`// TODO(api)`) tới khi lms-be lên staging.
- File "sửa" kèm `file:line`: lms-be ở `65d3aad` (WP0, base của B01), ops-fe ở `origin/staging` 1e01033bf. File "tạo" theo rule đặt code của repo.
- Cột Rule trỏ `../functional-design/rules.md`.

## Test strategy
- **Minimal** (AWS stage-protocol §8, mặc định Upbase): lms-be `openspec/conventions/verification.md` bắt curl, unit test khi plan yêu cầu (BE-8); ops-fe không có test runner (`ops-fe .claude/rules/07-testing-patterns.md:3`). Không áp ngưỡng 80% (accepted risk, mục cuối).
- Test-after theo lớp. Không có Testing Contract của engine `aidlc` (Upbase không cài engine).

## lms-be

**Base: `origin/feature/gamification` @ `65d3aad`** ("feat: gamification WP0 foundation", VietLH 12/10) — đã có `tenant.timezone` (`libs/database/migrations/1789996500000-add-timezone-to-tenant.ts`), bảng `gamification_settings` (`1789997000000-create-gamification-tables.ts:151-176`) có RLS + bypass (`TENANT_TABLES` `:4-5`, vòng lặp `:426-428`, `enableRls` `:471-485`), seed bản mặc định cho tenant có sẵn (`1789998000000-seed-gamification-defaults.ts:53-55`), entity `GamificationSetting` (`libs/database/src/lib/entities/gamification/gamification-setting.entity.ts:7-58`), repository, constants (`libs/constants/src/lib/gamification/gamification.constants.ts:82-87` Redis keys), module rỗng `apps/ops/src/gamification-setting/gamification-setting.module.ts` (đã đăng ký `apps/ops/src/app/app.module.ts:65,72`). B01 chỉ làm **delta** trên WP0 (DEC-T14). Mọi `file:line` dưới đây kiểm ở `65d3aad` trừ khi ghi khác.

Branch: branch cá nhân tách từ feature branch `feature/gamification` theo `openspec/conventions/git.md` (mục Branch, "Thứ tự với feature nhiều dev"). Change `run` `260923-gamification-b01-foundation` đang untracked ở `feature/ai_workflow` local → commit lên branch này ở bước đầu.

Rule repo: `openspec/conventions/backend.md` § 1, § 2 (ngoại lệ `tags`, ADR-002), § 3; `database.md` § 1, § 3; `verification.md`; `git.md` — các file này có ở `65d3aad`, **không có** trên `origin/staging`.

### Checklist
| # | Lớp | Việc | File | Rule / contract | Verify |
|---|---|---|---|---|---|
| - [ ] BE-1 | Migration | `1789999000000-add-visibility-first-enabled-at`: `ALTER TABLE "gamification_settings" ADD "visibility_first_enabled_at" TIMESTAMP WITH TIME ZONE` (null); `down()` drop cột. RLS đã có từ WP0 | **Tạo** `libs/database/migrations/1789999000000-add-visibility-first-enabled-at.ts` (sau `1789998000000-seed-gamification-defaults.ts`) | ADR-005; BR14.13 | `npm run typeorm:run-migrations` local; revert chỉ khi dev đồng ý; ghi up/down vào progress.md (`database.md` § 1) |
| - [ ] BE-2 | Entity | Thêm `visibility_first_enabled_at: Date \| null` (`timestamptz`, nullable, comment) sau `last_enabled_at`. Giữ `extends AbstractEntity` của WP0 (DEC-T14) | **Sửa** `libs/database/src/lib/entities/gamification/gamification-setting.entity.ts:53-54` | ADR-005 | build |
| - [ ] BE-3 | Constant + exception | Thêm vào file WP0: `GAMIFICATION_PERMISSION` (3 mã, group `gamification_management`), `GAMIFICATION_SETTINGS_CACHE_KEY = \`${GAMIFICATION_REDIS_KEYS.CONFIG}:settings\``, TTL 3600. Mã `GAMIFICATION_DISABLED: '400\|700001'` vào `EXCEPTION_CODES` + message key `GAMIFICATION_DISABLED: 'exceptions.gamification_disabled'` vào `EXCEPTION_MESSAGES` (`libs/constants/src/lib/exceptions/exceptions.message.ts`, giá trị là i18n key như `'exceptions.forbidden'`; chuỗi tiếng Anh nằm ở ops-fe OPS-9); `GamificationDisabledException` (mẫu `libs/exceptions/src/lib/common/common.exception.ts:69-83`) | **Sửa** `libs/constants/src/lib/gamification/gamification.constants.ts:87` (thêm sau), `exceptions.code.ts`, `exceptions.message.ts`. **Tạo** `libs/exceptions/src/lib/gamification/gamification.exception.ts` + export của `libs/exceptions` | BR14.2; C-02 400 | build |
| - [ ] BE-4 | DTO | `UpdateGamificationSettingDto` (`@IsOptional() @IsBoolean()` `is_enabled`, `is_visible` + validator lớp "đúng một trường" → 422), interface `GamificationSettingsResponse` (6 field C-01) | **Tạo** `libs/interface/src/lib/dto/gamification/gamification-setting.dto.ts`. **Sửa** `libs/interface/src/index.ts` (export) | BR14.10, BR14.11; C-01, C-02 | build |
| - [ ] BE-5 | Business logic | `GamificationSettingsService` trong `libs/modules/src/lib/gamification/settings/`: `getSettings()` (CacheService `getCache` → miss thì `getOrCreate()` → `setCache` TTL 3600; `libs/services/src/lib/redis/cache.service.ts:34,44` ở `origin/staging`); `getOrCreate()` (`INSERT … ON CONFLICT (tenant_id) DO NOTHING` với `tenant_id` gán tường minh từ `getRequestTenantId` `libs/database/src/lib/extends/request-tenant.ts:21`, tenant rỗng thì ném lỗi; seed WP0 đã tạo cho tenant có sẵn, hàm này cho tenant mới — ADR-007); `updateSetting(dto)` **theo thứ tự**: (1) có `is_visible` (bất kỳ giá trị) mà `is_enabled=false` → `GamificationDisabledException`; (2) bằng giá trị cũ → trả bản ghi, không ghi; (3) `is_enabled` false→true: `last_enabled_at = now()`, `first_enabled_at = COALESCE(…, now())`; (4) `is_visible` false→true: `visibility_first_enabled_at = COALESCE(…, now())`; ghi xong `deleteCache` (`cache.service.ts:56`) trong cùng request; map `has_been_visible`. Không cache in-memory (ADR-003). Module import `RedisCacheModule` (mẫu `apps/ops/src/caching-settings/caching-settings.module.ts:8`) | **Tạo** `libs/modules/src/lib/gamification/settings/{gamification-settings.service.ts, gamification-settings.module.ts, index.ts}`. **Sửa** `libs/modules/src/lib/gamification/index.ts:1-2` (thêm `export * from './settings'`) | BR14.1, 14.2, 14.5, 14.6, 14.10 | BE-8 |
| - [ ] BE-6 | API (Ops) | Controller trong module WP0: `@Controller('gamification')` một đoạn (contract: scan bỏ `/` trong path controller); `@Get('settings')`, `@Patch('settings')`; `@UseGuards(StaffGuard)`; `@ApiOperation` đúng khối `x-permission` C-01, C-02 (`security` + `tags` có mã, ADR-002); `SAPPResponse.Success` (mẫu `apps/ops/src/groups/group.controller.ts:60-90` ở `origin/staging`) | **Tạo** `apps/ops/src/gamification-setting/gamification-setting.controller.ts`. **Sửa** `apps/ops/src/gamification-setting/gamification-setting.module.ts:1-4` (controllers, import module service) | BR15.1, 15.2, 15.3, 15.7; C-01, C-02 | curl BE-9; TC-15…TC-19 trên staging |
| - [ ] BE-7 | Convention | Ghi ngoại lệ `tags` cho nhóm `gamification_management` | **Sửa** `openspec/conventions/backend.md:29-37` | ADR-002 | BE lead duyệt trong MR |
| - [ ] BE-8 | Unit test | (0) Kiểm runner: jest `passWithNoTests` → chạy với 1 spec rỗng tạm phải thấy "Tests: 1", xoá sau. `gamification-settings.service.spec.ts` (repository, CacheService mock): tạo mặc định khi chưa có; cache hit không gọi DB; bật lần đầu ghi 2 mốc; bật lại chỉ đổi `last_enabled_at`; tắt giữ `is_visible`; `is_visible:true` khi tắt → exception; `is_visible:true` khi tắt **và** đang `is_visible=true` → vẫn exception (thứ tự kiểm); bật Visibility lần đầu ghi mốc, lần sau không đổi; ghi bằng giá trị cũ không update; mọi lần ghi gọi `deleteCache` | **Tạo** cạnh service (jest `libs/modules/jest.config.ts`) | BR14.1, 14.2, 14.5, 14.6, 14.10 | `npx nx test modules --testPathPattern=libs/modules/src/lib/gamification/settings` xanh, đúng **10 test** |
| - [ ] BE-9 | Curl verify | `x-curl` C-01 GET; C-02 PATCH `{is_enabled:true}`; C-02 PATCH `{is_visible:true}` khi tắt → 400 (local, service do dev chạy, `verification.md`); ghi PASS/FAIL/BLOCKED vào progress.md | — | C-01, C-02 | 3 PASS |
| - [ ] BE-10 | MR | MR branch cá nhân → `feature/gamification` (`git.md`); feature branch lên nhánh sprint rồi `staging` theo lịch WP của BE lead; deploy, chạy migration; tạo role V, E, N (ED-01) | — | — | TC-12…TC-19 trên staging |

Không làm ở U0: các cột US8–US11 (WP0 đã tạo, không đọc ghi); endpoint learners (WP4); luồng ghi nhận (WP1, WP5); `RedisCacheModule` cho app `lms`, event-processor (Unit sau).

## ops-fe

Rule repo: `.claude/rules/01-code-placement.md` (feature `features/{name}/src/`, API class `apps/ops-fe/src/apis/{domain}/`, file < 300 dòng), inventory `.claude/inventory/*`, UI theo `../ui-map/ui-map.md` section ops-fe qua `/ui-gate`.

### Checklist
| # | Lớp | Việc | File | Rule / contract | Verify |
|---|---|---|---|---|---|
| - [ ] OPS-1 | Types | `IGamificationSettings` (6 field C-01), `IUpdateGamificationSetting` (`{ is_enabled?: boolean; is_visible?: boolean }`), `IGamificationAPI` | **Tạo** `libs/core/src/types/gamification.ts`. **Sửa** `libs/core/src/types/index.ts:69`; `libs/core/src/types/api-service.interface.ts:3429` (thêm cuối file, mẫu `ICacheAPI` `:399`) | C-01, C-02 | typecheck |
| - [ ] OPS-2 | Constant | `gamificationKeys`; `TITLE_GAMIFICATION_GR = { VIEW: 'gr_view_gamification_settings', UPDATE: 'gr_update_gamification_settings', VIEW_LEARNERS: 'gr_view_gamification_learners' }`; `ID_SIDE_BAR.GAMIFICATION` | **Tạo** `libs/core/src/constants/queryKeyFactory/gamificationKeys.ts`. **Sửa** `libs/core/src/constants/queryKeyFactory/index.ts:24-25`; `libs/core/src/constants/permission.ts:147` + `:242-243` | ADR-002; BR15.3 | typecheck |
| - [ ] OPS-3 | API | `GamificationAPI.getSettings()` → `GET /gamification/settings`; `updateSetting(body)` → `PATCH` (`fetcher` `libs/service/src/request.ts:57`, mẫu `apps/ops-fe/src/apis/cache/index.ts:1-30`) | **Tạo** `apps/ops-fe/src/apis/gamification/index.ts` | C-01, C-02 | typecheck; mock `// TODO(api)` tới khi BE-10 xong |
| - [ ] OPS-4 | DI | Inject `GamificationAPI` vào FeatureProvider | **Sửa** `libs/state/src/context/FeatureContext.tsx:1` + `:51`; `apps/ops-fe/src/index.tsx:39` + `:132` | — | typecheck |
| - [ ] OPS-5 | Module | `@ops/feature-gamification`: `index.ts` (`AppModule` như `features/cache/src/index.ts:5-10`, có `sidebarIds: [ID_SIDE_BAR.GAMIFICATION]` để `visibleSidebarList` chứa id — `libs/state/src/context/SidebarContext.tsx:28-44`, `apps/ops-fe/src/bootstrap.ts:21`), `routes.tsx`, `constants/routes.ts` (`GAMIFICATION: '/gamification'`), `package.json` (mẫu `features/cache/package.json`) | **Tạo** `features/gamification/{package.json, src/index.ts, src/routes.tsx, src/constants/routes.ts}`. **Sửa** `apps/ops-fe/src/module-registry.ts:16` + `:33`; `apps/ops-fe/package.json:13-27`; `scripts/generate-customer.js:33` + `:51`; `pnpm install` | ui-map White-label | `pnpm install`; typecheck; `pnpm gen` một config có và không có `feature-gamification` |
| - [ ] OPS-6 | Menu | Mục "Gamification" trong `menuSystemAdministration` (`showMenu: visibleSidebarList.includes(ID_SIDE_BAR.GAMIFICATION)`). Filter hiện tại `menuSystemAdministration.filter((item) => adminPermission && item)` (`:1434-1437`, `adminPermission` = superadmin, `libs/hooks/src/permission/usePermissions.ts:22-25`) sẽ ẩn mục với role thường → **sửa filter theo từng item**: `item.id === ID_SIDE_BAR.GAMIFICATION ? hasAnyGamification : adminPermission`, `hasAnyGamification` từ `useHasPermission` với 3 mã, thêm vào deps `useMemo` | **Sửa** `libs/hooks/src/permission/useMenuData.tsx:1431` (thêm item) + `:1434-1437` (filter) | BR15.3; ui-map UI-5 | SA thấy; N không thấy; V thấy |
| - [ ] OPS-7 | UI lib | `HookFormSwitch` nhận `disabled` (đã có trong `IBaseInputProps`, `libs/core/src/types/form.ts:66`) truyền vào `<input disabled>` | **Sửa** `libs/ui/src/base/switch/HookFormSwitch.tsx:6,15-24` | BR15.7 | Mọi chỗ dùng cũ không đổi (prop tuỳ chọn) |
| - [ ] OPS-8 | UI | Screen `gamification-settings`: `GamificationSettingsPage` (`PageLayouts`, `withAuthComponents`; không có quyền nào → `Result 403`; quyền xem/sửa → `GeneralSettingsCard`; chỉ quyền học viên → trống; `useQuery(gamificationKeys.settings)`), `GeneralSettingsCard`, `SwitchWithConfirm` (`Popconfirm` antd, hoàn tác khi Huỷ; `HookFormSwitch` đổi giá trị trước `onSubmit` `HookFormSwitch.tsx:19-22` nên phải `setValue` lại khi Huỷ/lỗi), `useMutation` một trường, bỏ qua khi đang lưu trường đó, `toast.success('Saved')`. Chuỗi đúng ui-map. Gợi ý: `Popconfirm` cần child nhận ref/onClick, `HookFormSwitch` là FC thường → dùng `open` có kiểm soát và bọc `<span>`. `data-testid` như ui-map | **Tạo** `features/gamification/src/pages/GamificationSettingsPage.tsx`, `src/components/{GeneralSettingsCard,SwitchWithConfirm}.tsx` (+ `.module.scss` nếu cần) | BR14.1, 14.2, 14.10, 14.12, 14.13, 15.3, 15.7; ui-map UI-1…UI-9; FE-O1…O6 | `/ui-gate build` trước, `/ui-gate review` (Provisional) trước khi tick; TC-1…TC-11, TC-16…TC-18 |
| - [ ] OPS-9 | Message | Thêm `{ "code": "400\|700001", "message": "Turn on Gamification before changing Visibility in UpLMS." }` (file là mảng `{code, message}`, đọc ở `libs/service/src/request.ts:189-195`) | **Sửa** `libs/service/src/en.exceptions.json` | C-02 400 | TC-9 hiện đúng message |
| - [ ] OPS-10 | Kết thúc | `pnpm typecheck:ops-fe` một lần cuối (rules/08), lint, `/opsx:verify`, push + PR vào `staging` | — | — | PR merge |

## Kiểm tích hợp (staging, sau MR lms-be + PR ops-fe)
| Điểm | Cách kiểm | TC |
|---|---|---|
| U0-IC1 | SA bật/tắt trên ops-fe, `GET` thấy ngay | TC-2, TC-7, TC-13 |
| U0-IC2 | DB một dòng mỗi tenant, RLS bật | TC-12, TC-14 |
| U0-IC3 | Key Redis `tenant:{id}:gamification:config:settings` bị xoá sau PATCH | TC-12, TC-13 |
| U0-IC4 | Màn role có nhóm gamification; V/E/N đúng quyền; N mở link ra 403 | TC-15…TC-19 |
| Hồi quy | Màn role, cache settings, trang Ops có quyền sẵn | TC-21 |

## Chặn trước khi code
- ED-07: BE lead cập nhật `assignment.md` của `upbase-221099-gamification` — phần "cấu hình chung + quyền" của WP3 chuyển sang B01 (owner Nguyễn Hùng Sơn) (DEC-T14).
- ED-01 (role V, E, N trên staging) cho TC quyền; ED-05 Jira.
- Không còn câu hỏi thiết kế mở (domain-design Q1–Q4 đã trả lời).

## Vấn đề khi áp chuẩn AWS (accepted risk, DEC-T13)
| # | Chuẩn AWS | Thực tế Upbase | Xử lý ở B01 |
|---|---|---|---|
| 1 | Scope `feature`: 80% coverage + CI test trước merge | lms-be chỉ bắt curl; ops-fe không test runner; CI chỉ build + deploy | Minimal: 10 unit test + 3 curl + `/ui-gate review` + Playwright MCP theo TC |
| 2 | Testing Contract do engine sinh | Không có engine `aidlc` | Mục Test strategy thay thế |
| 3 | Plan theo Unit, code cùng repo | Unit xuyên 2 repo | Một section mỗi repo = `tasks.md` của change `run` từng repo |
