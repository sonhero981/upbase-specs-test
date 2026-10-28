# Bolt B01 · Nền tảng (US14, US15)

| | |
|---|---|
| Intent | `intents/260923-gamification/` |
| PRD / contract | PRD 0.14 + 2.43 Q1–Q17 (DEC-T4, DEC-T17) / `contract-summary.md` 2.0 Agreed (DEC-T21) · functional-design 1.0 (DEC-T11) · ui-map 1.0 Provisional (DEC-T12) · plan 1.2 (DEC-T24, viết lại theo ADR-016) · test-cases 2.0 (DEC-T23) |
| Owner | cuongdq (BE, chịu DoD cuối) + Nguyễn Hùng Sơn (FE) — bolt-plan v2.0 (DEC-T22) |
| Unit | U0 `u0-foundation` (walking skeleton, mang US14, US15) |
| US / BR | US14 · US15 — BR14.1, 14.2, 14.5, 14.6, 14.8–14.13 · BR15.1–15.3, 15.5–15.7 (`construction/u0-foundation/functional-design/rules.md`) |
| Repo | lms-be, ops-fe (không chạm lms-fe, lms-package — ADR-006) |
| Phụ thuộc | — |
| Ước lượng | 3 ngày công (bolt-plan B01) |

## Why
Mở đường cho mọi Unit gamification: cấu hình theo tổ chức có hiệu lực ngay, và phân quyền Ops chặn được route thật. Confidence hypothesis ở `inception/delivery-planning/bolt-plan.md` mục B01.

## What Changes
- **lms-be** (sửa tại chỗ code WP3 trên `origin/feature/gamification` @9006b80, ADR-016): cột `visibility_first_enabled_at`; `GamificationGeneralSettingService` theo C-02 (PATCH một trường, `400|630001`, giữ `is_visible` khi tắt, `has_been_visible`, `running_campaign_count`); cache Redis cấu hình gốc trong `GamificationConfigService` (ADR-003); tên quyền + `tags` cho cả 10 endpoint của controller WP3; ngoại lệ `tags` trong `backend.md` — plan mục `## lms-be` (BE-1…BE-10, BE-5b, BE-5c, BE-8b).
- **ops-fe** (đã code phần lớn ở working tree, `progress.md`): feature `@ops/feature-gamification`, menu theo 3 quyền, `HookFormSwitch` nhận `disabled`, trang khối chung hai công tắc + popover + `Saved` — plan mục `## ops-fe` (OPS-1…OPS-10), ui-map `## ops-fe`.
- **BREAKING trong nhánh `feature/gamification`** (chưa lên staging, chưa có consumer): `PUT /gamification/settings` → `PATCH`; 10 endpoint WP3 bắt đầu chặn theo quyền. Ngoài nhánh: không breaking; prop `disabled` tuỳ chọn.

## Capabilities

### New Capabilities
- `gamification-settings`: đọc và bật tắt hai công tắc chung theo tổ chức, có hiệu lực ngay.
- `gamification-permission`: ba quyền Gamification trong hệ phân quyền Ops, chặn trang, menu và API.

### Modified Capabilities
- Không có.

## Đọc trước
Đường dẫn tính từ `intents/260923-gamification/`.
1. `inception/delivery-planning/bolt-plan.md` mục B01 — DoD, demo.
2. `inception/domain-design/decisions.md` — ADR-002 (tags), ADR-003 (cache), ADR-004 (PATCH), ADR-005 (mốc Visibility), ADR-016 (sửa WP3).
3. `construction/u0-foundation/functional-design/` — `rules.md`, `functional-spec.md`, `frontend-components.md`.
4. `inception/contract-design/contract-summary.md` v2.0 — S-01, C-01, C-02, C-03, C-04…C-07 (quyền GET/PUT bốn khối), mục Quyền endpoint.
5. `construction/u0-foundation/code-generation/code-generation-plan.md` — section repo mình làm.
6. `construction/u0-foundation/ui-map/ui-map.md` — ops-fe.
7. `inception/test-cases/test-cases.md` v2.0 — TC-1…TC-21 (TC hoãn: plan mục "TC của B01").

## Test case
| Chạy ở Bolt này | Hoãn sang Bolt | Lý do hoãn |
|---|---|---|
| TC-1…TC-21 | BR14.3, BR14.7, BR15.8, US15-AC4 | Không có luồng ghi nhận, khối chức năng, campaign, endpoint learners trong lát |

## Dữ liệu để chạy / demo
- Staging, tenant hiện có (`timezone = Asia/Ho_Chi_Minh` sau migration), chưa có bản ghi `gamification_settings`.
- Ops: SA; role V (chỉ `gr_view_gamification_settings`), E (`gr_update_gamification_settings`), N (không quyền gamification) tạo sau deploy (ED-01).

## Impact
- lms-be: `libs/database` (1 migration, entity WP0), `libs/constants`, `libs/exceptions`, `libs/interface`, `libs/modules/src/lib/gamification/settings`, `apps/ops/src/gamification-setting`, `openspec/conventions/backend.md`.
- ops-fe: `features/gamification` (mới), `apps/ops-fe/src/apis/gamification`, `libs/core`, `libs/state` (FeatureContext), `libs/hooks` (menu), `libs/ui` (HookFormSwitch), `libs/service/src/en.exceptions.json`, `module-registry.ts`, `scripts/generate-customer.js`.

## Definition of Done
- 3 curl PASS; 10 unit test lms-be xanh; migration up/down sạch local.
- Màn `gamification-settings` pass `/ui-gate review` (Provisional).
- U0-IC1…IC4 đạt trên staging; TC P0 pass.
- MR lms-be merge vào `feature/gamification` rồi lên `staging` theo lịch BE lead, PR ops-fe merge `staging`; typecheck ops-fe một lần cuối.

## Demo
FE lead + BE lead trên staging: SA bật Gamification, bật Visibility (popover lần đầu), tắt Gamification (popover); V thấy công tắc không bấm được; N không thấy menu, mở link ra 403, API 403; màn role có nhóm gamification.
