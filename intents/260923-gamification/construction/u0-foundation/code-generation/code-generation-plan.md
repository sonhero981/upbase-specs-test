---
intent: 260923-gamification
unit: u0-foundation
bolt: B01
artifact: code-generation-plan
stage: 3.5 code-generation (Part 1 — Planning)
version: 1.2
status: approved
approved_at: 2026-10-14 (FE lead + [GIẢ LẬP] BE lead, DEC-T24)
review: review-code-generation-03 NOT-READY → sửa R-19…R-22; review-code-generation-04 NOT-READY → sửa R-24…R-26; review-code-generation-05 READY → sửa R-27
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả) · phần lms-be soi chéo với owner BE
owner_bolt: cuongdq (BE, chịu DoD cuối) + Nguyễn Hùng Sơn (FE) — bolt-plan v2.0 (DEC-T22)
supersedes: v1.1 (DEC-T13, DEC-T14; viết trên WP0 @65d3aad, archive/code-generation/code-generation-plan-v1.1-20261014.md)
consumes: ../functional-design/ v1.0 (DEC-T11) · ../ui-map/ui-map.md v1.0 Provisional (DEC-T12) · inception/contract-design/contract-summary.md v2.0 Agreed (C-01, C-02, C-03, S-01; DEC-T21) · inception/domain-design/decisions.md v2.0 (ADR-002, ADR-003, ADR-004, ADR-005, ADR-016) · inception/test-cases/test-cases.md v2.0 (TC-1…TC-30) · inception/delivery-planning/bolt-plan.md v2.0 B01 · codekb lms-be `origin/feature/gamification` @9006b80 (WP0 + WP3 c235167 + WP1), ops-fe @1e01033bf + working tree B01
---
# Code Generation Plan: U0 `u0-foundation` (Bolt B01) — v1.2

## Vì sao viết lại (ADR-016)
v1.1 viết trên WP0 khi phần cấu hình chung "chưa có". Nhánh `feature/gamification` nay có WP3 (`c235167`, cuongdq): `GamificationSettingController` 10 endpoint `GET`/`PUT` năm khối, `tags: []`, `security` chỉ có group (`apps/ops/src/gamification-setting/gamification-setting.controller.ts:18,35-200`); `GamificationGeneralSettingService` ghi `PUT` cả hai công tắc (`services/gamification-general-setting.service.ts:35-64`), không có `visibility_first_enabled_at`, không kiểm BR-14.2; `GamificationConfigService` đọc DB mỗi lần, **không cache** (`libs/modules/src/lib/gamification/config/gamification-config.service.ts:55-77`). B01 sửa tại chỗ code WP3 thay vì viết service mới.

| Đổi so với v1.1 | Lý do |
|---|---|
| Không tạo service/controller/DTO mới; sửa `GamificationGeneralSettingService`, controller, DTO của WP3 | Code đã có (ADR-016) |
| `PUT /gamification/settings` → `PATCH` một trường | ADR-004, C-02 |
| Mọi endpoint của controller WP3 khai tên quyền + `tags` ngay trong B01 | ADR-002, ADR-016: không để API cấu hình mở cho mọi staff |
| Mã lỗi `400\|700001` → `400\|630001` | C-02 v2.0 (2.8 Q1) |
| Thêm cache Redis cho cấu hình gốc ngay trong B01 (WP3 chưa cache) | ADR-003, C-01, U0-IC3, TC-12, TC-13 (review-code-generation-03 R-19) |
| Response thêm `has_been_visible`, `running_campaign_count` (= 0 tới B16) | C-01 v2.0 |
| Owner BE: cuongdq (code WP3 của cuongdq) | bolt-plan v2.0 |
| ops-fe đã code phần lớn (working tree, `progress.md`): plan ghi phần còn lại | Phiên trước (DEC-T14) |

## Câu hỏi cho plan (BE lead duyệt ở gate)
| # | Câu | Đề xuất |
|---|---|---|
| Q2 | Bốn khối còn lại giữ `PUT` tới Bolt của chúng? | Có (ADR-016). B01 chỉ đổi khối chung + quyền của cả 10 endpoint |
| Q3 | Cache ở `GamificationConfigService` dùng chung với engine ở event-processor (chưa dùng Redis)? | `GamificationConfigModule` tự import `RedisCacheModule`, cache bắt buộc ở mọi app dùng module (ADR-003 áp nguyên); event-processor cần biến `LIB_SERVICES_REDIS_*` (BE-5c, ED-18). Không dùng `@Optional` để cache không tắt im lặng (review 04 R-24) |

## Test strategy
- **Minimal** (DEC-T13, accepted risk chuẩn): lms-be curl bắt buộc (`openspec/conventions/verification.md`) + unit test service khối chung; ops-fe không có test runner → `/ui-gate review` (Provisional) + typecheck + TC chạy tay ở 3.6. Không áp ngưỡng 80% coverage.
- Hướng dẫn chạy test: `unit-test-instructions.md` cùng thư mục.

## lms-be

**Base: `origin/feature/gamification` @ `9006b80`.** Branch cá nhân của cuongdq tách từ `feature/gamification` (`openspec/conventions/git.md`). Change `run` `260923-gamification-b01-foundation` mở sau khi PR store merge (`code-generation.md` Part 1 bước 4). Mọi `file:line` kiểm ở `9006b80`.

Rule repo: `openspec/conventions/backend.md` § 1, § 2 (ngoại lệ `tags`, ADR-002), § 3; `database.md` § 1, § 3; `verification.md`; `git.md`.

### Checklist
| # | Lớp | Việc | File | Rule / contract | Verify |
|---|---|---|---|---|---|
| - [ ] BE-1 | Migration | `<ts>-add-visibility-first-enabled-at`: `ALTER TABLE "gamification_settings" ADD "visibility_first_enabled_at" TIMESTAMP WITH TIME ZONE NULL`; `down()` drop cột. Bảng đã có RLS từ WP0. Timestamp phải lớn hơn migration cuối của nhánh `1791874289448-add-points-by-source-to-user-stats.ts` (WP1); sinh bằng lệnh tạo migration của repo lúc code | **Tạo** `libs/database/migrations/<ts > 1791874289448>-add-visibility-first-enabled-at.ts` | ADR-005; BR-14.13 | run migration local; up/down ghi `progress.md` (`database.md` § 1) |
| - [ ] BE-2 | Entity | Thêm `visibility_first_enabled_at: Date \| null` (`timestamptz`, nullable, comment "Mốc lần đầu bật hiển thị cho học viên") sau `last_enabled_at` | **Sửa** `libs/database/src/lib/entities/gamification/gamification-setting.entity.ts:53-54` | ADR-005 | build |
| - [ ] BE-3 | Exception code | `GAMIFICATION_DISABLED: '400\|630001'` vào `EXCEPTION_CODES` (chỗ trống trước `630002`); message key `GAMIFICATION_DISABLED: 'exceptions.gamification_disabled'` vào `EXCEPTION_MESSAGES`; thêm `'GAMIFICATION_DISABLED'` vào union `GamificationSettingErrorKey` | **Sửa** `libs/constants/src/lib/exceptions/exceptions.code.ts:635-636`; `exceptions.message.ts:681-682`; `libs/exceptions/src/lib/gamification/gamification-setting.exceptions.ts:5-15` | C-02 400, S-01 | build |
| - [ ] BE-4 | DTO | `UpdateGamificationSettingDto`: hai field thành `@IsOptional() @IsBoolean()` + validator lớp "đúng một trường" (rỗng hoặc hai trường → 422 `422\|000405`); thêm `GamificationGeneralSettingResponse` có `has_been_visible`, `running_campaign_count` vào `libs/interface` (đang khai trong service WP3 `:8-13`) | **Sửa** `libs/interface/src/lib/gamification/setting/gamification-setting.dto.ts:20-28`. **Chuyển** interface response từ `apps/ops/src/gamification-setting/services/gamification-general-setting.service.ts:8-13` sang `libs/interface/src/lib/gamification/setting/` (§ 1: DTO/interface ở `libs/interface`) | BR-14.10, BR-14.11; C-01, C-02 | build; 422 ở BE-9 |
| - [ ] BE-5 | Business logic | Viết lại `GamificationGeneralSettingService.validate/project/apply/toResponse` theo C-02: (1) dto có `is_visible` (bất kỳ giá trị) mà `current.setting.is_enabled = false` → `GamificationSettingException('GAMIFICATION_DISABLED')`; (2) giá trị bằng hiện tại → không ghi, trả bản ghi; (3) `is_enabled` false→true: `last_enabled_at = now`, `first_enabled_at ??= now` (giữ logic WP3 `:40-43`); `is_enabled` true→false: **giữ** `is_visible` (BR-14.2; WP3 hiện ghi đè `is_visible` từ dto `:45`); (4) `is_visible` false→true: `visibility_first_enabled_at ??= now`; (5) `apply` ghi đúng cột đổi; (6) `toResponse` thêm `has_been_visible = visibility_first_enabled_at != null`, `running_campaign_count = 0` (B16 thay bằng đếm campaign In Progress). Cache và xoá cache ở BE-5b. `validateCross` của base giữ nguyên (`base-gamification-setting.service.ts:92-120`) | **Sửa** `apps/ops/src/gamification-setting/services/gamification-general-setting.service.ts:28-72` | BR-14.1, 14.2, 14.5, 14.6, 14.10, 14.13; ADR-005 | BE-8 |
| - [ ] BE-5b | Cache (ADR-003) | Trong `GamificationConfigService`: (1) `getSetting()` đọc `CacheService.getCache` khoá `${GAMIFICATION_REDIS_KEYS.CONFIG}:settings` (CacheService tự thêm tiền tố tenant), miss thì đọc DB (giữ `createDefaults` của WP3) rồi `setCache` TTL 3600; không cache in-memory; (2) giá trị lấy từ Redis là JSON → **dựng lại** `first_enabled_at`, `last_enabled_at`, `visibility_first_enabled_at`, `created_at`, `updated_at` thành `Date` trước khi trả (engine B02 so sánh `Date`); (3) hàm mới `invalidateSetting()` gọi `deleteCache` khoá trên. `GamificationConfigModule` **import `RedisCacheModule`** (module không global, `CacheService` là export của nó; `CACHE_MANAGER` mới global) và inject `CacheService` bắt buộc (không `@Optional`). `BaseGamificationSettingService.update()` gọi `this.configService.invalidateSetting()` sau `commitTransaction` (base đã có `configService`, không sửa constructor năm service con) | **Sửa** `libs/modules/src/lib/gamification/config/gamification-config.service.ts:40-48,71-77` (+ hàm `invalidateSetting`, hydrate); `libs/modules/src/lib/gamification/config/gamification-config.module.ts:1-8` (imports); `apps/ops/src/gamification-setting/services/base-gamification-setting.service.ts:54-67`. Dùng `libs/services/src/lib/redis/cache.service.ts:34,44,56`, `redis-cache.module.ts:12-68`; khoá `libs/constants/src/lib/gamification/gamification.constants.ts:82-87` | ADR-003; C-01; U0-IC3 | BE-8b; TC-12, TC-13 |
| - [ ] BE-5c | Cấu hình app | Mọi app import `GamificationConfigModule` (ops; event-processor qua engine WP1) giờ cần kết nối Redis: kiểm đủ biến `LIB_SERVICES_REDIS_*` gồm host, port, password, ping interval, TLS (`.env.example:100-107`) có ở môi trường deploy của event-processor (staging, production); thiếu thì báo DevOps trước khi merge (ED-18) | — | ADR-003 | event-processor khởi động được với module mới |
| - [ ] BE-6 | API + quyền | Controller WP3: `@Put('settings')` → `@Patch('settings')` (`:52-64`); thay `GAMIFICATION_SECURITY` (`:18`) bằng khối quyền theo `x-permission` của contract cho **cả 10 endpoint**: GET settings `security name = gr_view_gamification_settings`, `tags` = ba mã (C-01); PATCH settings `name = gr_update_gamification_settings`, `tags` = mã update (C-02); bốn GET khối còn lại `tags` = view + update (C-04…C-07, BR-15.7); bốn PUT khối còn lại `tags` = update (giữ `PUT` tới Bolt của khối, Q2). Bỏ chữ "múi giờ" trong comment `:33`, `:50`. Giữ `@Controller('gamification')` một đoạn (scan bỏ `/` trong path controller) | **Sửa** `apps/ops/src/gamification-setting/gamification-setting.controller.ts:1,18,35-200` | ADR-002, ADR-016; BR-15.1, 15.2, 15.3, 15.7; C-01, C-02, C-04…C-07 | BE-9; TC-15…TC-19 trên staging |
| - [ ] BE-7 | Convention | Ghi ngoại lệ `tags` cho nhóm `gamification_management` (ED-02) | **Sửa** `openspec/conventions/backend.md:29-37` | ADR-002 | BE lead duyệt trong MR |
| - [ ] BE-8 | Unit test | `gamification-general-setting.service.spec.ts` (mock `GamificationConfigService`, `RequestDataSource`/query runner): bật lần đầu ghi hai mốc; bật lại chỉ đổi `last_enabled_at`; tắt giữ `is_visible`; `is_visible` khi tắt → `630001` (cả khi giá trị bằng hiện tại); bật Visibility lần đầu ghi mốc, lần sau không đổi; giá trị bằng hiện tại không ghi; `has_been_visible` đúng; `running_campaign_count = 0`; `update` gọi `configService.invalidateSetting()` sau commit (mock kiểm được). Trước khi viết: chạy runner với spec rỗng tạm để chắc jest nhận file (`passWithNoTests`) | **Tạo** `apps/ops/src/gamification-setting/services/gamification-general-setting.service.spec.ts` | BR-14.1, 14.2, 14.5, 14.13 | `npx nx test ops --testPathPattern=gamification-general-setting` xanh, 9 test |
| - [ ] BE-8b | Unit test cache | `gamification-config.service.spec.ts` (mock `CacheService`, repository): cache hit không gọi DB; miss đọc DB rồi `setCache` TTL 3600; giá trị từ cache có các trường thời điểm là `Date`; `invalidateSetting` gọi `deleteCache` đúng khoá | **Tạo** `libs/modules/src/lib/gamification/config/gamification-config.service.spec.ts` | ADR-003 | `npx nx test modules --testPathPattern=gamification-config` xanh, 4 test |
| - [ ] BE-9 | Curl verify | `x-curl` C-01 GET; C-02 PATCH `{is_enabled:true}`; PATCH `{is_visible:true}` khi tắt → `400\|630001`; PATCH `{}` → 422; staging: `PUT /gamification/point-rules` bằng role V → 403, mọi endpoint bằng role N → 403; ghi PASS/FAIL/BLOCKED vào `progress.md` | — | C-01, C-02, C-04 | 4 PASS local + 2 staging |
| - [ ] BE-10 | MR | MR branch cá nhân → `feature/gamification`, cuongdq tự review chéo với vietlh (đụng code WP3); lên nhánh sprint / `staging` theo lịch BE lead (ED-04); deploy, chạy migration; tạo role V, E, N (ED-01) | — | — | TC-12…TC-19 trên staging |

Không làm ở B01: đổi `PUT` → `PATCH` của bốn khối còn lại (B03, B09, B11, B14); bỏ `630011` và việc tự tắt tiêu chí khi tắt Badges (B09, B11 theo C-05, C-06); đếm campaign thật (B16).

## ops-fe

Rule repo: `.claude/rules/01-code-placement.md`, inventory `.claude/inventory/*`, UI theo `../ui-map/ui-map.md` qua `/ui-gate`. Code B01 đang ở **working tree** (`feature/ai_workflow`, untracked) — `openspec/changes/260923-gamification-b01-foundation/progress.md` của ops-fe ghi chi tiết. Bước đầu: chuyển sang branch ticket từ `staging` (`/jira-tasks`), commit phần đã có.

### Checklist
| # | Lớp | Việc | File | Trạng thái | Verify |
|---|---|---|---|---|---|
| - [x] OPS-1 | Types | `IGamificationSettings`, `IUpdateGamificationSetting`, `IGamificationAPI` | `libs/core/src/types/gamification.ts`; `api-service.interface.ts` (cuối) | Đã làm (progress 1.1). **Sửa**: bỏ `updated_at` (`libs/core/src/types/gamification.ts:7`, ngoài C-01 v2.0), thêm `running_campaign_count: number` | typecheck |
| - [x] OPS-2 | Constant | `gamificationKeys`, `TITLE_GAMIFICATION_GR` (3 mã), `ID_SIDE_BAR.GAMIFICATION` | `libs/core/src/constants/...` (WT: `permission.ts:149`, `:249`) | Đã làm (1.2) | typecheck |
| - [ ] OPS-3 | API | Đã gọi thật (`USE_MOCK = false`, `PATCH`; `apps/ops-fe/src/apis/gamification/index.ts:5,41-49` WT). **Còn**: xoá hẳn mock chết (`mockResponse`, `mockUpdate`, literal `400\|700001` ở `:24`) | `apps/ops-fe/src/apis/gamification/index.ts` (WT) | Gần xong | typecheck; TC-1, TC-2 trên staging |
| - [x] OPS-4 | DI | Inject `GamificationAPI` vào FeatureContext | `libs/state/src/context/FeatureContext.tsx`, `apps/ops-fe/src/index.tsx` | Đã làm (1.3) | typecheck |
| - [ ] OPS-5 | Module | `@ops/feature-gamification`, registry, package, `generate-customer.js` | `features/gamification/*` (WT) | Đã làm (2.1); **còn** chạy `pnpm gen` với một config có và không có feature | `pnpm gen` |
| - [x] OPS-6 | Menu | Mục Gamification, filter từng item theo ba quyền | `libs/hooks/src/permission/useMenuData.tsx:1437-1466` (WT) | Đã làm (2.2); verify SA/V/N ở 3.6 | TC-18 |
| - [ ] OPS-7 | UI lib | `HookFormSwitch` nhận `disabled` (đã làm, 3.2) **và** `aria-label` (ui-gate R7 flag) | `libs/ui/src/base/switch/HookFormSwitch.tsx` | Còn `aria-label` | chỗ dùng cũ không đổi |
| - [ ] OPS-8 | UI | `GamificationSettingsPage`, `GeneralSettingsCard`, `SwitchWithConfirm` (đã làm, 3.3). **Bổ sung**: nhánh quyền chỉ `gr_view_gamification_learners` → trang không có khối chung (khối Campaign đến ở B16, 2.43 Q1) — code sẵn, kiểm ở B05 khi quyền này xuất hiện; popover tắt đọc `running_campaign_count` (= 0 tới B16); chuỗi trạng thái lỗi `Could not load gamification settings.` / `Reload` (ngoài ui-map) → ghi vào ui-map Provisional | `features/gamification/src/pages/GamificationSettingsPage.tsx`, `src/components/*` (WT); file ngoài plan v1.1 đã thêm: `src/constants/settings.ts`, 3 `.module.scss` | Phần lớn đã làm | `/ui-gate review` lại; TC-1…TC-11, TC-16…TC-18 |
| - [ ] OPS-9 | Message | Đổi `400\|700001` → `400\|630001`, message `Turn on Gamification before changing Visibility in UpLMS.` | `libs/service/src/en.exceptions.json` (WT, progress 1.4) | Cần sửa mã | TC-9 trên staging |
| - [ ] OPS-9b | Review FE | Chạy lại `/fe:review`, sửa 6 mục "Nên sửa" của lần 2026-10-13 (`progress.md` chỉ ghi số lượng, không ghi nội dung) và ghi chi tiết vào `progress.md` | `features/gamification/*` | Chưa | `/fe:review` 0 Nên sửa |
| - [ ] OPS-9c | Dọn change | Change `openspec/changes/260923-gamification-b01-walking-skeleton-aws/` ở ops-fe là bản demo PRD v0.10 (bolt-plan v1.0 ghi `[DEMO cũ]`): giữ có banner, không dùng; xoá khi archive intent | — | Giữ, ghi lý do | — |
| - [ ] OPS-10 | Kết thúc | `pnpm typecheck:ops-fe` (lọc theo file đổi, nợ cũ 1117 lỗi), lint, `/opsx:verify`, PR vào `staging` | — | — | PR merge |

## TC của B01
- Chạy ở B01: TC-1…TC-21 (TC-24 chỉ phần khối chung).
- Hoãn: TC-22, TC-23 (cần ghi nhận và màn học viên: B02, B04), TC-24 phần bốn khối (B03, B09, B11, B14 khi đổi `PATCH`), TC-25, TC-26 (campaign: B16), TC-27 (quyền xem học viên: B05), TC-28…TC-30 (hồi quy luồng học: B02, B04).

## Kiểm tích hợp (staging, sau MR lms-be + PR ops-fe)
| Điểm | Cách kiểm | TC |
|---|---|---|
| U0-IC1 | SA bật/tắt trên ops-fe, `GET` thấy ngay | TC-2, TC-7, TC-13 |
| U0-IC2 | DB một dòng mỗi tenant, RLS bật | TC-12, TC-14 |
| U0-IC3 | Key Redis `tenant:{id}:gamification:config:settings` có sau GET, bị xoá sau PATCH; `GET` ngay sau `PATCH` thấy giá trị mới | TC-12, TC-13 |
| U0-IC4 | Màn role có hai quyền gamification (quyền thứ ba hiện ở B05, ADR-002); V/E/N đúng quyền trên cả 10 endpoint; N mở link ra 403 | TC-15…TC-19 |
| Hồi quy | Màn role, cache settings, trang Ops có quyền sẵn; 4 khối WP3 còn `PUT` vẫn chạy với quyền mới | TC-21 |

## Chặn trước khi code
- ED-07: BE lead cập nhật `assignment.md` (B01 sửa WP3; owner BE cuongdq).
- ED-18: biến Redis cho event-processor (BE-5c).
- ED-01 role V, E, N trên staging (role L ở B05); ED-05 Jira; ED-02 convention `tags`.
- Q2, Q3 ở trên (gate).

## Vấn đề khi áp chuẩn AWS (accepted risk, DEC-T13)
| # | Chuẩn AWS | Thực tế Upbase | Xử lý ở B01 |
|---|---|---|---|
| 1 | Scope `feature`: 80% coverage + CI test trước merge | lms-be chỉ bắt curl; ops-fe không test runner; CI chỉ build + deploy | Minimal: 13 unit test (9 + 4 cache) + curl + `/ui-gate review` + TC chạy tay |
| 2 | Testing Contract do engine sinh | Không có engine `aidlc` | Mục Test strategy + `unit-test-instructions.md` |
| 3 | Plan theo Unit, code cùng repo | Unit xuyên 2 repo, hai owner | Một section mỗi repo = `tasks.md` của change `run` từng repo |
