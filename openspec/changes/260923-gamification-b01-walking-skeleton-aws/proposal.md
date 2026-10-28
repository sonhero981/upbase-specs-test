# Bolt B01 · Walking skeleton (chuẩn AWS)

> **[DEMO cũ]** Dựng trên PRD v0.10 (DEC-T1…T8). Thiết kế gốc từ 13/10: PRD v0.14 + lms-be `openspec/changes/upbase-221099-gamification` (DEC-T1 ở `intents/260923-gamification/decisions.md (mã DEC-T)`; artifact demo ở `archive/tech-demo-prd-v0.10/`). Không dùng change này để code.

| | |
|---|---|
| Intent | `intents/260923-gamification/` |
| PRD / contract | PRD 0.10 ([DEMO] coi như đã duyệt) / `contract-summary.md` 1.0 Agreed (DEC-T4) · functional-design 1.0 (DEC-T6) · ui-map 1.0 Provisional (DEC-T7) · plan 1.0 (DEC-T8) |
| Owner · Lane | Dev A · A |
| Unit | U0 `u0-walking-skeleton` (walking skeleton) |
| US / BR | Không US. BR14.1, 14.5–14.9, 14.14–14.16 · BR5.1–5.3, 5.11–5.13, 5.15–5.18 (`construction/u0-walking-skeleton/functional-design/rules.md`) |
| Repo | lms-be, ops-fe, lms-fe (không chạm lms-package) |
| Phụ thuộc | — (Bolt đầu); B02–B04 dựng trên bảng, module, API của Bolt này |
| Ước lượng | 2,1 ngày công (bolt-plan B01) |

Change này thay bản mẫu cũ `260923-gamification-b01-walking-skeleton` (layout `tech/`) cho luồng chuẩn AWS; bản cũ giữ để so sánh.

## Why
Chứng minh một công tắc lưu trên Ops đổi được hành vi ghi nhận ở lms-be cho học viên của đúng tổ chức, cắt ngày theo múi giờ tổ chức, và lỗi ghi nhận không chặn học viên vào lms-pro (confidence hypothesis B01, `inception/delivery-planning/bolt-plan.md`).

## What Changes
- **lms-be**: migration `tenant.timezone` + `gamification_settings` + `presence_days` có RLS kèm bypass; C-01 `GET`/`PATCH /gamification/settings` (Ops, khai quyền ADR-007); C-03 `POST /gamification/presence` (LMS, shape cuối) — `construction/u0-walking-skeleton/code-generation/code-generation-plan.md` mục `## lms-be`; `inception/contract-design/contract-summary.md` C-01, C-03, C-04, C-05.
- **ops-fe**: feature `@ops/feature-gamification`, route, menu, quyền, trang một công tắc — plan mục `## ops-fe`; `construction/u0-walking-skeleton/ui-map/ui-map.md` mục `## ops-fe`; contract C-01, C-07.
- **lms-fe**: `PresenceSignal` ở lms-pro gửi C-03 silent một lần khi có user — plan mục `## lms-fe`; contract C-03.
- Không **BREAKING**: endpoint, bảng mới; `tenant` thêm cột có default (C-04).

## Capabilities

### New Capabilities
- `gamification-settings`: cấu hình gamification theo tổ chức, đọc / bật tắt trên Ops, chặn theo quyền.
- `learner-presence`: ghi nhận ngày có mặt của học viên theo múi giờ tổ chức, tín hiệu từ app học viên.

### Modified Capabilities
- Không có.

## Đọc trước
Đường dẫn tính từ `intents/260923-gamification/`.
1. `inception/delivery-planning/bolt-plan.md` mục `## B01` — giả thuyết, DoD, demo, release chỉ staging.
2. `construction/u0-walking-skeleton/functional-design/` — `rules.md` (BR), `functional-spec.md` (WF-1…WF-4, state machine), `frontend-components.md`.
3. `inception/contract-design/contract-summary.md` — quy ước chung, mục Quyền endpoint Ops, C-01, C-03, C-04, C-05, C-07.
4. `construction/u0-walking-skeleton/code-generation/code-generation-plan.md` — section repo mình làm; mục "Chặn trước khi code".
5. `construction/u0-walking-skeleton/ui-map/ui-map.md` — ops-fe (Provisional).
6. `inception/test-cases/test-cases.md` — TC ở mục Test case dưới.

## Test case
| Chạy ở Bolt này | Hoãn sang Bolt | Lý do hoãn |
|---|---|---|
| TC-1 (phần API + trang chỉ một công tắc), TC-2 (phần bật, mốc), TC-13, TC-14, TC-40 (phần `DISABLED`), TC-46, TC-48, TC-49, TC-51 | TC-2 phần `Saved`/Visibility, TC-3…TC-11 → B02 | Visibility, popover, `Saved` là U1 |
| TC-32 (phần curl `ALREADY_RECORDED`) | TC-31, TC-33…TC-45 → B04 | chuỗi, điểm, thao tác chủ động là U3 |

## Dữ liệu để chạy / demo
- Staging, tenant hiện có (`timezone` = `Asia/Ho_Chi_Minh` sau migration).
- Ops: một superadmin, một staff không có mã `gr_*_gamification_settings`.
- LMS: một học viên sạch.
- Không seed; migration không tạo bản ghi settings (tạo khi đọc lần đầu, BR14.6).

## Impact
- lms-be: `libs/database` (migration, entity, repository, `tenant.entity.ts`), `libs/constants`, `libs/interface`, `libs/modules/src/lib/gamification`, `apps/ops|lms/src/gamification`, hai `app.module.ts`. Dữ liệu cũ: `tenant` thêm cột default.
- ops-fe: `features/gamification` (mới), `apps/ops-fe/src/apis/gamification`, `libs/core`, `libs/state` (FeatureContext), `libs/hooks` (menu), `module-registry.ts`, `scripts/generate-customer.js`.
- lms-fe: `apps/lms-pro` (`api/gamification`, `components/gamification`, `client-layout.tsx`), `libs/core/types`.

## Definition of Done
- 3 curl PASS (C-01 GET, C-01 PATCH, C-03); 12 unit test lms-be xanh; migration up/down sạch local.
- Màn `gamification-settings` pass `/ui-gate review` (Provisional, chỉ audit).
- 4 điểm kiểm tích hợp `U0-IC1…IC4` đạt trên staging; TC ở mục trên pass.
- PR lms-be, ops-fe, lms-fe merge `staging`; typecheck một lần cuối mỗi repo FE.

## Demo
FE lead + BE lead trên staging: superadmin bật Gamification trên ops-fe → học viên mở lms-pro → DB có đúng một ngày có mặt; mở lại không thêm; tắt rồi mở ngày khác không ghi; staff thường thấy trang không có quyền và API trả 403.
