---
intent: 260923-gamification
status: Running
---
# Tech state: 260923-gamification

| | |
|---|---|
| PRD dùng | `inception/prd/prd.md` version 0.14 (approved 2026-10-12), commit 18ba56a |
| Phạm vi đợt này | **Cả intent** (DEC-T15, 2026-10-13): 19 US = US1, US2, US3, US4, US5, US6, US7, US8, US9, US10, US11, US12, US13, US14, US15, US19, US20, US21, US22; trừ ba US PRD ghi "chưa làm" (16, 17, 18). Lát đầu (DEC-T2) đã thành B01 |
| Tech lead tác giả | FE lead · Nguyễn Hùng Sơn |
| FE lead | Nguyễn Hùng Sơn |
| BE lead | Đoàn Quang Cường |
| QA lead | chưa có tên |
| Dev code (owner Bolt) | Nguyễn Hùng Sơn (FE lms-fe + ops-fe, full-time; B01 fullstack) · vietlh@upbase.asia (BE core, ~14 ngày công: WP0, WP1, WP2, WP5, WP7, WP8, WP9) · cuongdq@upbase.asia = Đoàn Quang Cường (BE Ops/API/Campaign, ~10.5 ngày công: WP3, WP4, WP6, WP10, WP11). Năng lực BE theo lms-be `openspec/changes/upbase-221099-gamification/assignment.md` (Đề xuất, bắt đầu 08/10) |
| Thiết kế BE có sẵn | PRD `Solution › TDD / API / Database` + lms-be `openspec/changes/upbase-221099-gamification` (BE lead, 2026-10-12) — input, không viết lại (DEC-T1) |

## Inception
Ký hiệu: `[ ]` chưa làm · `[-]` đang làm · `[?]` chờ duyệt · `[R]` đang sửa · `[x]` đã duyệt · `[S]` bỏ qua kèm lý do

- [x] 2.43 prd-readiness · cả intent READY v1.2 (lần kiểm mở rộng NOT READY DEC-T16 → PO giả lập trả lời Q5–Q17 DEC-T17 → READY DEC-T18) · trước đó: READY v1.0 sau lần kiểm lại (lần đầu NOT READY, DEC-T3) · PO (giả lập) trả lời Q1–Q4, chưa CR (DEC-T4) · gate Approve (DEC-T5, giả lập BE lead)
- [x] 2.1 reverse-engineering · 3 store CURRENT (lms-be 610f100, lms-fe b2cc49455, ops-fe 1e01033bf); quét thêm đường sinh quyền lms-be + màn role ops-fe; WIP `origin/feature/gamification` chỉ có tài liệu
- [x] 2.6 domain-design · cả intent v2.0 (DEC-T19): 35 component (lms-be 21, ops-fe 8, lms-fe 6), ADR-008…018, Q5–Q12 BE lead (giả lập) đã trả lời; review vòng 1 NOT-READY → vòng 2 READY; gate Approve · trước đó: 9 component (lms-be 4, ops-fe 5), ADR-001…007 · BE lead (giả lập) trả lời 4 câu (DEC-T6)
- [x] 2.7 units-generation · cả intent v2.0 (DEC-T20): 18 Unit (U0…U17), 50,5 ngày công, ngoại lệ có ký U0, U1, U5, U11 (Q6); review 01 NOT-READY → 02 READY; gate Approve · trước đó: 1 Unit U0 `u0-foundation` (US14, US15), 3 ngày (DEC-T7)
- [x] 2.8 contract-design · cả intent v2.0 Agreed (DEC-T21): 28 contract (21 REST, 4 async, 3 shared/in-process), phủ 28/28 cạnh DAG; Q1–Q6 BE lead (giả lập); review 01 NOT-READY → 02 READY; BE lead (giả lập) ký · trước đó: C-01 GET, C-02 PATCH settings, C-03 `/me` (có sẵn) Agreed (DEC-T8)
- [x] 2.81 test-cases · cả intent v2.0 (DEC-T23): 429 TC (TC-1…30, TC-101…565), sensor test-cases và toàn chuỗi Đạt; 63 câu hỏi PO (TQ-1…63) Accepted risk; QA lead (giả lập) duyệt · trước đó: 21 TC, phủ BR US14/US15, BR hoãn có lý do (DEC-T9)
- [x] 2.9 delivery-planning · cả intent v2.0 (DEC-T22): 18 Bolt (B01…B18, mỗi Bolt một Unit), 66 ngày công (code 50,5 + thiết kế 15,5), xong 16/11 (dự phòng ~19/11); owner: Sơn 23,5 · vietlh 21 · cuongdq 21,5; gate Approve có điều kiện (B02…B18 vào 3.1 khi 2.81 duyệt); review 01 NOT-READY → 02 READY · trước đó: B01 = U0, owner Nguyễn Hùng Sơn (DEC-T10)

## Construction
| Bolt | Unit | 3.1 functional | 3.2 nfr-req | 3.3 nfr-design | 3.4 infra | 3.41 ui-map | 3.5 code-gen | 3.6 build-test | Owner | Change |
|---|---|---|---|---|---|---|---|---|---|---|
| B01 | U0 u0-foundation | [x] | [S] không NFR riêng ngoài 2.43 Q3 | [S] | [S] không hạ tầng mới | [x] Provisional | Plan [x] v1.2 (DEC-T24) · code [ ] | [ ] | Nguyễn Hùng Sơn | `260923-gamification-b01-foundation` (store + lms-be, ops-fe) |
| B02 | U1 u1-recording-engine | [x] v1.2 | [ ] | [ ] | [ ] | [ ] | [x] plan v1.0 gate FE lead (conditional: vietlh gộp migration object_name_snapshot vào Bước 1; BE lead xác nhận Q1–Q5) | [ ] | vietlh (trọn) | — (Plan duyệt) |
| B03 | U3 u3-points-config | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | cuongdq (Đoàn Quang Cường) (trọn) | — (Dự kiến; được vào 3.1) |
| B04 | U5 u5-learner-home | [x] v1.1 FE focus (US1); gate FE lead | [ ] | [ ] | [ ] | [ ] | [x] plan v1.0 gate FE lead (conditional: cuongdq xác nhận C-14 schema; OQ-B04-1 trước 3.6) | [ ] | cuongdq (Đoàn Quang Cường) (BE) + Nguyễn Hùng Sơn (FE) | — (Plan duyệt) |
| B05 | U4 u4-ops-achievement-log | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | vietlh (BE) + Nguyễn Hùng Sơn (FE) | — (Dự kiến; được vào 3.1) |
| B06 | U2 u2-daily-checkin | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | vietlh (BE) + Nguyễn Hùng Sơn (FE) | — (Dự kiến; được vào 3.1) |
| B07 | U6 u6-achievement-realtime | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | vietlh (BE) + Nguyễn Hùng Sơn (FE) | — (Dự kiến; được vào 3.1) |
| B08 | U7 u7-achievement-history | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | vietlh (BE) + Nguyễn Hùng Sơn (FE) | — (Dự kiến; được vào 3.1) |
| B09 | U8 u8-badges-config | [x] v1.1 FE focus; gate FE lead | [ ] | [ ] | [ ] | [ ] | [x] plan v1.0 gate FE lead (conditional: cuongdq xác nhận Nhóm A; endpoint upload confirm trước merge C4) | [ ] | cuongdq (Đoàn Quang Cường) (BE) + Nguyễn Hùng Sơn (FE) | — (Plan duyệt) |
| B10 | U9 u9-badge-gallery | [x] v1.1 FE focus; gate FE lead | [ ] | [ ] | [ ] | [ ] | [x] plan v1.0 gate FE lead (conditional: OQ-B10-1 route + OQ-B10-3 default image trước merge) | [ ] | cuongdq (Đoàn Quang Cường) (BE) + Nguyễn Hùng Sơn (FE) | — (Plan duyệt) |
| B11 | U10 u10-levels-config | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | vietlh (trọn) | — (Dự kiến; được vào 3.1) |
| B12 | U11 u11-leaderboard | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | cuongdq (Đoàn Quang Cường) (BE) + Nguyễn Hùng Sơn (FE) | — (Dự kiến; được vào 3.1) |
| B13 | U12 u12-my-position | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | cuongdq (Đoàn Quang Cường) (BE) + Nguyễn Hùng Sơn (FE) | — (Dự kiến; được vào 3.1) |
| B14 | U13 u13-leaderboard-config | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | vietlh (trọn) | — (Dự kiến; được vào 3.1) |
| B15 | U14 u14-ops-learner-list | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | vietlh (BE) + Nguyễn Hùng Sơn (FE) | — (Dự kiến; được vào 3.1) |
| B16 | U15 u15-campaign-admin | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | cuongdq (Đoàn Quang Cường) (trọn) | — (Dự kiến; được vào 3.1) |
| B17 | U16 u16-campaign-board | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | cuongdq (Đoàn Quang Cường) (BE) + Nguyễn Hùng Sơn (FE) | — (Dự kiến; được vào 3.1) |
| B18 | U17 u17-campaign-results | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | cuongdq (Đoàn Quang Cường) (BE) + Nguyễn Hùng Sơn (FE) | — (Dự kiến; được vào 3.1) |

Trạng thái Bolt: Dự kiến · Thiết kế · Plan duyệt · Đang code · Chờ demo · Xong.

## Current
| | |
|---|---|
| Stage | Construction. B02/B09/B04/B10: **tất cả 3.1 + 3.5 gate FE lead**. Sơn bắt đầu code B09 → B04 → B10 theo thứ tự. |
| Next action | Sơn: code B09 (Nhóm B→E), B04 (Nhóm B→F), B10 (Nhóm B→F). cuongdq: xác nhận C-14 schema (B04) + Nhóm A B09. Tech lead: trả lời OQ-B04-1 + OQ-B10-1 + OQ-B10-3 trước khi merge. PO: OQ-B04-2,3 + OQ-B10-2,4 trước 3.6. |

## Thời gian thực tế — Human + AI (đo theo session)

> Đây là thời gian cặp Human+AI thực tế làm trong session, không phải dev làm một mình.
> Tốc độ tăng ~4-6× so với dev solo nhờ AI viết draft, human review + redirect.

### Đã hoàn thành (thực đo)

| Bolt | Stage | Nội dung | Thực tế H+AI |
|---|---|---|---|
| B02 | 3.1 v1.0 + 2 vòng review + gate | entities, rules, spec, traceability, 2 review files, fixes v1.1→v1.2 | ~45 phút |
| B02 | 3.5 v1.0 + gate | 25-bước plan NestJS | ~20 phút |
| B09 | 3.1 v1.0 + 1 vòng review + gate | 4 files FE focus, review, fix F-01…F-04 lên v1.1 | ~35 phút |
| B09 | 3.5 v1.0 + gate | 5-nhóm plan FE (B,C,D,E) + BE nhóm A | ~15 phút |
| **Tổng Thiết kế B02+B09** | | | **~115 phút ≈ 2h** |

### Đã hoàn thành (thực đo đầy đủ)

| Bolt | Stage | Thực tế H+AI |
|---|---|---|
| B02 | 3.1 full cycle (v1.0→v1.2, 2 vòng review) | ~45 phút |
| B02 | 3.5 + gate | ~20 phút |
| B09 | 3.1 full cycle (v1.0→v1.1, 1 vòng review) | ~35 phút |
| B09 | 3.5 + gate | ~15 phút |
| B04 | 3.1 full cycle (v1.0→v1.1, 1 vòng review) | ~30 phút |
| B04 | 3.5 + gate | ~15 phút |
| B10 | 3.1 full cycle (v1.0→v1.1, 1 vòng review) | ~25 phút |
| B10 | 3.5 + gate | ~15 phút |
| **Tổng thiết kế B02+B09+B04+B10** | | **~200 phút ≈ 3.3h** |

### Còn lại (ước tính H+AI)

| Bolt | Stage | Ước tính H+AI |
|---|---|---|
| B09+B04+B10 | 3.6 code (AI gen + human review PR) | ~150–180 phút |
| Chờ PO | `/change-request` đưa Q1–Q17 + chuỗi popover vào PRD; design `OQ-45`, hình 24 mốc huy hiệu (không chặn Tech, DEC-T4, DEC-T17) |

## Ghi chú cho PO
- Ghi nhận điểm đi qua Kafka như code WP1 (ADR-009), lệch câu PRD `Solution › TDD` "không qua hàng đợi"; mục tiêu thẻ thông báo ≤ 3 giây (2.43 Q14).
- Check-in do lms-fe báo khi học viên có thao tác thật (ADR-010), đúng BR-5.1.
- Màn 403 bên Ops: màn sẵn có có nút đăng xuất, nên lát này dùng màn 403 chuẩn (không đăng xuất) với câu `You do not have permission to view this page.` — lệch câu trả lời "dùng màn 403 hiện có" (DEC-T14).
- PRD US14 sơ đồ ba trạng thái ghi "tắt Gamification, tắt luôn Visibility" trái BR-14.2 (giữ giá trị Visibility); Tech theo BR-14.2. Sửa ở `/change-request` kế tiếp.
- 2.41 HLD Brief đang `[S]` ở `state.md` PO; Tech dùng fallback intent v1 (hướng kỹ thuật ghi ở `inception/domain-design/decisions.md`).

## Log
- 2026-10-13 Khởi tạo bản thật trên PRD v0.14. Bản demo PRD v0.10 (DEC-T1…T9 cũ) chuyển vào `archive/tech-demo-prd-v0.10/`.
- 2026-10-13 2.43 viết xong: NOT READY, chờ gate.
- 2026-10-13 Gate 2.43 Approve NOT READY (DEC-T3, giả lập BE lead). Test workflow: chưa commit, câu hỏi gửi PO qua chat.
- 2026-10-13 PO (giả lập) trả lời Q1–Q4; 2.43 kiểm lại READY, gate Approve (DEC-T5).
- 2026-10-13 2.1 xong: codekb CURRENT, bổ sung đường sinh quyền (authz-tenant) và màn role (settings-screens).
- 2026-10-13 2.6 → 3.5 plan xong cho B01 (gate giả lập). Review gộp NOT READY (R-01 WP0 có sẵn, R-02 convention, R-03 menu) → sửa, plan v1.1 (DEC-T14). Mở change Bolt ở store + `run` ở lms-be, ops-fe. Dừng trước code.
- 2026-10-13 Re-review vòng 2 READY (review-code-generation-02); sửa R-14…R-18. Gate 3.5 plan đóng (DEC-T13, DEC-T14).
- 2026-10-13 Mở rộng phạm vi cả intent (19 US, DEC-T15). Mở lại `[R]` 2.43 (US mới), 2.6, 2.7, 2.8, 2.81, 2.9. B01 giữ nguyên. Dev: Sơn (FE), vietlh, cuongdq (BE theo assignment lms-be).
- 2026-10-13 2.43 `[R]` kiểm 17 US mới: NOT READY (RD9–RD13 Chặn; RD14–RD20 Nên sửa; RD21–RD25 Ghi nhận). Câu hỏi Q5–Q17 ở `prd-readiness-questions.md` Lô 2. Chờ gate.
- 2026-10-13 Gate 2.43 Approve NOT READY (DEC-T16, giả lập BE lead). PO (giả lập) trả lời Q5–Q17 = A (DEC-T17). Kiểm lại READY v1.2, gate Approve (DEC-T18). Kế tiếp 2.6 `[R]`.
- 2026-10-13 2.6 `[R]` cả intent: quét lại code (lms-be nhánh chung có thêm WP3, WP1; lms-fe có nhánh WIP UI), viết v1.1 35 component, ADR-008…018, BE lead (giả lập) trả lời Q5–Q12. Review 01 NOT-READY (R-01…R-05 Chặn) → sửa → review 02 READY → sửa R-15…R-17. Chờ gate.
- 2026-10-13 Gate 2.6 Approve v2.0 (DEC-T19, FE lead + giả lập BE lead). ADR-008…018 Accepted. Mở lại 3.5 plan B01 `[R]` theo ADR-016. Kế tiếp 2.7 `[R]`.
- 2026-10-13 2.7 `[R]` cả intent: 18 Unit lát dọc theo US, BE lead (giả lập) trả lời Q1–Q7. Review 01 NOT-READY (R-01 thiếu cạnh) → sửa → review 02 READY → sửa ghi nhận R-08…R-11. Chờ gate.
- 2026-10-13 Gate 2.7 Approve v2.0 (DEC-T20, FE lead + giả lập BE lead), ký ngoại lệ U0, U1, U5, U11 và skeleton. Kế tiếp 2.8 `[R]`.
- 2026-10-13 2.8 `[R]` cả intent: 28 contract, BE lead (giả lập) trả lời Q1–Q6. Review 01 NOT-READY (R-01 quyền GET cấu hình) → sửa → review 02 READY → sửa R-10. Chờ gate.
- 2026-10-13 Gate 2.8: BE lead (giả lập) ký 28 contract Agreed v2.0 (DEC-T21). Kế tiếp cặp 2.81 ∥ 2.9.
- 2026-10-13 2.9 `[R]` cả intent: 18 Bolt, họp (giả lập) trả lời Q1–Q7. Review 01 NOT-READY (5 Nên sửa) → sửa (thiết kế vào lịch, owner tối ưu lịch, release constraints, hypothesis có ngưỡng) → review 02 READY → sửa R-08, R-10. Chờ họp.
- 2026-10-13 Gate 2.9 Approve v2.0 (DEC-T22, họp giả lập): duyệt cả 18 Bolt, owner và lịch (xong 16/11, dự phòng ~19/11), có điều kiện B02…B18 chờ 2.81. Kế tiếp 2.81 `[R]`.
- 2026-10-14 2.81 `[R]` cả intent: 5 nhóm viết song song, ghép 429 TC; TC-9 đổi mã 630001; TC-22…27 phủ BR hoãn của US14, US15; TC-28…30 hồi quy. Sensor toàn chuỗi Đạt. 63 câu hỏi PO. Chờ QA lead.
- 2026-10-14 Gate 2.81 Approve v2.0 (DEC-T23, giả lập QA lead). Điền cột TC 18 Bolt, phase check Inception Đạt, gỡ điều kiện gate 2.9. Inception xong; kế tiếp Construction B01 plan `[R]`.
- 2026-10-14 B01 plan v1.2 viết lại trên WP3 @9006b80 (cache Redis ở GamificationConfigService, PATCH khối chung, quyền 10 endpoint, 630001). Review 03, 04 NOT-READY → 05 READY. Chờ gate Plan approval.
- 2026-10-14 Gate 3.5 plan B01 Approve v1.2 (DEC-T24, FE lead + giả lập BE lead). Change Bolt ở store cập nhật theo plan v1.2 (proposal, tasks, spec 630001). B02, B03, B16 mở khoá 3.1.
- 2026-10-14 B02 3.1 bắt đầu: quét điểm gắn luồng học trên @9006b80; 5 câu hỏi (Q1–Q4 chặn) ở `construction/u1-recording-engine/functional-design/functional-design-questions.md`.
- 2026-10-14 B02 3.1: Q1–Q5 chọn trong phiên (chờ BE lead xác nhận). Viết v1.0, sensor Đạt. Review 01 NOT-READY (R-01 BR-SKIP sai chỗ foundation_status, R-02 chấm lại qua bước duyệt) → Q4 thay bằng Q4b, sửa lên v1.1; S-02 thêm occurred_at (additive). Sửa nhãn B04, B09, B10: chờ B02 plan.
- 2026-10-15 B02 3.1: Review 02 READY (không còn Chặn). Sửa lên v1.2: R-05 thêm timeout ≤ 100 ms vào BR13.7; R-14 sửa logic BR13.16 (SKIP_FOUNDATION edge case, ghi Ghi chú cho PO); R-19 sửa Q4→Q4b ở traceability.json. Sensor Đạt. Gate 3.1: FE lead approve conditional (BE lead xác nhận Q1–Q5 + PO chốt SKIP_FOUNDATION). **SP 3.1**: ~2 sp (thiết kế 2 vòng review, 5 câu hỏi, sửa v1.1→v1.2).
- 2026-10-15 B02 3.5: code-generation-plan v1.0, 25 bước (Migration, Entity, Engine, Notifier, Hooks H1–H5, FailedEventRetry, Tests). Gate FE lead approve conditional (vietlh gộp migration object_name_snapshot). B09 và B04 mở khoá 3.1. **SP 3.5**: ~1 sp (plan).
- 2026-10-15 B09 3.1 bắt đầu (FE focus): viết entities, rules, functional-spec, traceability v1.0. Sensor Đạt (0 lỗi). Đang chờ review. **SP 3.1**: ~1 sp (thiết kế FE).
- 2026-10-15 B09 3.1: Review 01 READY (không Chặn). Fix 4 findings lên v1.1: F-01 entities API table C-06/C-07→C-05; F-02 rename BR9.T1…T4→BR9.11…14 (sensor-safe); F-03 traceability US9-AC3/AC4 target→BR ID tồn tại; F-04 WF-4 step 3 thêm endpoint upload. Gate 3.1: FE lead approve. B10 mở khoá sau khi B09 pass 3.5. **SP gate**: ~0.5 sp (fix + gate).
- 2026-10-15 B09 3.5: code-generation-plan v1.0, 5 nhóm (A BE 5 bước, B Types+API 2 bước, C Components 5 bước, D Hook 1 bước, E Tests 2 bước). FE 2 ngày công (Sơn); BE 3 ngày (cuongdq). Gate FE lead approve conditional. **SP 3.5**: ~1 sp (plan FE focus).
- 2026-10-15 B04 3.1 bắt đầu (FE focus): subagent viết entities (C-13/14/15), rules (BR-1.x + BR1.11–16), functional-spec (WF-1–5 GamificationPage + My Learning widget), traceability v1.0. Phát hiện: B04 map US1 (không phải US5 như task brief sai). Review 01: fix F-01 ô Streaks ẩn khi, F-02 TC-403 self-ref. Gate v1.1 FE lead. **SP 3.1**: ~0.5 sp (H+AI ~30 phút).
- 2026-10-15 B04 3.5: code-generation-plan v1.0, 6 nhóm (A BE, B Types+API, C Context/Hook, D GamificationPage+Components, E My Learning Widget, F Tests 22 TC). FE 2.5 ngày (Sơn). Gate FE lead conditional (cuongdq xác nhận C-14 schema; OQ-B04-1 Leaderboard trước 3.6). **SP 3.5**: ~0.5 sp (H+AI ~15 phút).
- 2026-10-15 B10 3.1 bắt đầu (FE focus): subagent viết entities (C-18: MyBadges/BadgeTypeRow/BadgeItem), rules (BR-4.1–4.7 + BR-1.7 + BR4.11–16), functional-spec (WF-1–4 + TC-501–519), traceability v1.0. Review 01: fix F-01 mâu thuẫn BR4.7 vs BR4.11 (reconcile cache in-session). Gate v1.1 FE lead. OQ-B10-1,3 chặn code D1,D4. **SP 3.1**: ~0.5 sp (H+AI ~25 phút).
- 2026-10-15 B10 3.5: code-generation-plan v1.0, 6 nhóm (A BE, B Types+API, C Hook React Query, D 4 components, E Skeleton+Error, F Tests 19 TC). FE 2 ngày (Sơn). Gate FE lead conditional (OQ-B10-1 route + OQ-B10-3 image path trước merge). **SP 3.5**: ~0.5 sp (H+AI ~15 phút).
