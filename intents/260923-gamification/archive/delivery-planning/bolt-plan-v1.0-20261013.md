---
intent: 260923-gamification
artifact: bolt-plan
stage: 2.9 delivery-planning
version: 1.0
status: approved
approved_at: 2026-10-13 ([GIẢ LẬP] họp FE, BE, PO, QA, owner Bolt, DEC-T10)
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
scope: US14, US15
consumes: inception/units-generation/ v1.0 (DEC-T7) · inception/contract-design/contract-summary.md v1.0 (DEC-T8) · inception/test-cases/test-cases.md v1.0 (DEC-T9) · tech-state.md
---
# Bolt Plan: Gamification, lát Nền tảng (US14 · US15)

Một Bolt cho một Unit. Bolt kết thúc bằng thứ chạy được trên staging, có Definition of Done, confidence hypothesis và một owner làm cả FE + BE.

## Bolts

| Bolt | Units | Owner | Repo | Ngày công | Phụ thuộc |
|---|---|---|---|---|---|
| B01 | U0 | Nguyễn Hùng Sơn | lms-be, ops-fe | 3 | — |

Change OpenSpec: `260923-gamification-b01-foundation` ở `openspec/changes/` của store và change `run` cùng tên ở lms-be, ops-fe. (Change `260923-gamification-b01-walking-skeleton-aws` cùng tiền tố là bản demo PRD v0.10, có banner `[DEMO cũ]`, không dùng.)

## B01 — Nền tảng (U0 `u0-foundation`)

| Mục | Nội dung |
|---|---|
| Units | U0 (US14, US15) |
| Walking skeleton | **Có.** Lát đi qua mọi điểm tích hợp thật của lát: ops-fe → lms-be qua guard và Casbin thật (C-01…C-03), bảng mới dưới RLS kèm bypass, cache Redis theo tenant (U0-IC1…IC4) |
| Definition of Done | (1) MR lms-be merge vào `feature/gamification` (WP0) rồi lên `staging` theo lịch BE lead, PR ops-fe merge `staging`, deploy staging; (2) U0-IC1…IC4 đạt trên staging; (3) TC P0 (TC-1, 2, 4, 6, 7, 8, 13, 15, 16, 17, 18) pass; (4) 3 `x-curl` của C-01, C-02 chạy PASS, contract chuyển Final |
| Confidence hypothesis | Khai quyền bằng `tags` (ADR-002) chặn được route thật với role không có quyền mà superadmin vẫn qua, và công tắc có hiệu lực ngay sau khi lưu (ADR-003). Sai thì lộ ở TC-16, TC-18 (403) hoặc TC-13 (cache) |
| Demo | Staging: SA bật Gamification, bật Visibility (popover lần đầu), tắt (popover); staff chỉ có quyền xem thấy công tắc nhưng không bấm được; staff không quyền không thấy menu, mở link ra 403; màn role có nhóm gamification |
| Real project check | lms-be: curl theo `openspec/conventions/verification.md`, migration up/down; ops-fe: `/ui-gate review`, `pnpm typecheck:ops-fe`, lint |
| TC | TC-1…TC-21 (US14, US15, REG) |
| Ngày công | 3 (lms-be 1,5 · ops-fe 1,5) |
| Release | Lên staging và production đều an toàn: Gamification mặc định tắt (BR-14.6), route chỉ superadmin tới khi gán quyền |

## Trace
<!-- trace:start -->
| Bolt | Unit | Change ở store |
|---|---|---|
| B01 | U0 | 260923-gamification-b01-foundation |

Đạt. US đợt này: 2 · Unit: 1 · Bolt: 1 · TC: 21 · lỗi: 0.
<!-- trace:end -->
