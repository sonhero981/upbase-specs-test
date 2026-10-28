---
intent: 260923-gamification
artifact: bolt-plan
stage: 2.9 delivery-planning
version: 2.0
status: approved
approved_at: 2026-10-13 ([GIẢ LẬP] họp FE, BE, PO, QA, owner Bolt, DEC-T22)
updated: 2026-10-14 điền cột TC + phase check sau 2.81 v2.0 (DEC-T23), không đổi Bolt
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
scope: cả intent, 19 US (DEC-T15)
consumes: inception/units-generation/ v2.0 (DEC-T20) · inception/contract-design/contract-summary.md v2.0 (DEC-T21) · inception/test-cases/test-cases.md v1.0 (US14, US15; 2.81 cả intent làm song song) · tech-state.md · lms-be openspec/changes/upbase-221099-gamification/assignment.md
supersedes: v1.0 (B01 = U0, DEC-T10)
---

# Bolt Plan: Gamification, cả intent (19 US)

Một **Bolt** là một lượt xây trọn một phần việc, kết thúc bằng thứ chạy được trên staging, có Definition of Done, confidence hypothesis (điều Bolt chứng minh khi xong) và owner. 18 Bolt, mỗi Bolt đúng một Unit của 2.7; B01 giữ số và giữ là walking skeleton (lát mỏng nhất đi qua các điểm tích hợp thật, ngoại lệ có ký ở 2.7 Q3). Code 50,5 ngày công, cộng thiết kế Construction (3.1, 3.41, 3.5) 0,5 ngày mỗi người mỗi Bolt và viết lại plan B01: tổng 66 ngày công. Xong dự kiến **16/11 sáng** theo lịch kín, chưa có dự phòng (xem Nút thắt). Owner: người ghi đầu tiên chịu DoD cuối; Bolt có hai người thì người FE làm phần FE trong cùng change (lệch "một owner fullstack", Q3 họp). Chưa tính 3.6 (QA) và review MR.

## Bolts

| Bolt | Units | Owner | Repo | Ngày công | Phụ thuộc |
|---|---|---|---|---|---|
| B01 | U0 | cuongdq (Đoàn Quang Cường) (BE) + Nguyễn Hùng Sơn (FE) | lms-be, ops-fe | 3 | — |
| B02 | U1 | vietlh (trọn) | lms-be | 3,5 | B01 |
| B03 | U3 | cuongdq (Đoàn Quang Cường) (trọn) | lms-be, ops-fe | 2,5 | B01 |
| B04 | U5 | cuongdq (Đoàn Quang Cường) (BE) + Nguyễn Hùng Sơn (FE) | lms-be, lms-fe | 3 | B02 |
| B05 | U4 | vietlh (BE) + Nguyễn Hùng Sơn (FE) | lms-be, ops-fe | 3 | B02 |
| B06 | U2 | vietlh (BE) + Nguyễn Hùng Sơn (FE) | lms-be, lms-fe | 3 | B02, B04 |
| B07 | U6 | vietlh (BE) + Nguyễn Hùng Sơn (FE) | lms-be, lms-fe | 3 | B04 |
| B08 | U7 | vietlh (BE) + Nguyễn Hùng Sơn (FE) | lms-be, lms-fe | 2 | B04 |
| B09 | U8 | cuongdq (Đoàn Quang Cường) (BE) + Nguyễn Hùng Sơn (FE) | lms-be, ops-fe | 3 | B01, B02 |
| B10 | U9 | vietlh (BE) + Nguyễn Hùng Sơn (FE) | lms-be, lms-fe | 1,5 | B04, B09 |
| B11 | U10 | vietlh (trọn) | lms-be, ops-fe | 2,5 | B03, B09 |
| B12 | U11 | cuongdq (Đoàn Quang Cường) (BE) + Nguyễn Hùng Sơn (FE) | lms-be, lms-fe | 4,5 | B02, B04 |
| B13 | U12 | cuongdq (Đoàn Quang Cường) (BE) + Nguyễn Hùng Sơn (FE) | lms-be, lms-fe | 2 | B12 |
| B14 | U13 | vietlh (trọn) | lms-be, ops-fe | 2 | B03, B05, B12 |
| B15 | U14 | vietlh (BE) + Nguyễn Hùng Sơn (FE) | lms-be, ops-fe | 3 | B05, B12 |
| B16 | U15 | cuongdq (Đoàn Quang Cường) (trọn) | lms-be, ops-fe | 3 | B01 |
| B17 | U16 | cuongdq (Đoàn Quang Cường) (BE) + Nguyễn Hùng Sơn (FE) | lms-be, lms-fe | 3 | B12, B13, B16 |
| B18 | U17 | cuongdq (Đoàn Quang Cường) (BE) + Nguyễn Hùng Sơn (FE) | lms-be, ops-fe, lms-fe | 3 | B05, B17 |

Phụ thuộc Bolt = cạnh DAG 2.7 (mỗi Bolt một Unit). Thứ tự số Bolt là thứ tự làm đề xuất; Bolt không phụ thuộc nhau chạy song song khác owner (Lịch).

## Lịch dự kiến theo người

Ngày làm việc từ thứ Tư 14/10/2026, bỏ thứ Bảy, Chủ nhật. Phần FE mock theo contract Agreed khi BE chưa lên staging, nên FE của một Bolt chỉ chờ FE của Bolt nó phụ thuộc; phần BE chờ BE của Bolt phụ thuộc.

| Người | Bolt (phần) | Bắt đầu | Kết thúc |
|---|---|---|---|
| Nguyễn Hùng Sơn | B01 (viết lại plan (ADR-016)) | 14/10 sáng | 14/10 sáng |
| Nguyễn Hùng Sơn | B01 (FE) | 14/10 chiều | 15/10 chiều |
| Nguyễn Hùng Sơn | B02 (thiết kế + rà plan) | 16/10 sáng | 16/10 sáng |
| Nguyễn Hùng Sơn | B04 (thiết kế + rà plan) | 16/10 chiều | 16/10 chiều |
| Nguyễn Hùng Sơn | B04 (FE) | 19/10 sáng | 20/10 chiều |
| Nguyễn Hùng Sơn | B05 (thiết kế + rà plan) | 21/10 sáng | 21/10 sáng |
| Nguyễn Hùng Sơn | B05 (FE) | 21/10 chiều | 22/10 chiều |
| Nguyễn Hùng Sơn | B06 (thiết kế + rà plan) | 23/10 sáng | 23/10 sáng |
| Nguyễn Hùng Sơn | B06 (FE) | 23/10 chiều | 26/10 sáng |
| Nguyễn Hùng Sơn | B07 (thiết kế + rà plan) | 26/10 chiều | 26/10 chiều |
| Nguyễn Hùng Sơn | B07 (FE) | 27/10 sáng | 27/10 chiều |
| Nguyễn Hùng Sơn | B08 (thiết kế + rà plan) | 28/10 sáng | 28/10 sáng |
| Nguyễn Hùng Sơn | B08 (FE) | 28/10 chiều | 29/10 sáng |
| Nguyễn Hùng Sơn | B09 (thiết kế + rà plan) | 29/10 chiều | 29/10 chiều |
| Nguyễn Hùng Sơn | B09 (FE) | 30/10 sáng | 02/11 sáng |
| Nguyễn Hùng Sơn | B10 (thiết kế + rà plan) | 02/11 chiều | 02/11 chiều |
| Nguyễn Hùng Sơn | B10 (FE) | 03/11 sáng | 03/11 chiều |
| Nguyễn Hùng Sơn | B12 (thiết kế + rà plan) | 04/11 sáng | 04/11 sáng |
| Nguyễn Hùng Sơn | B12 (FE) | 04/11 chiều | 05/11 sáng |
| Nguyễn Hùng Sơn | B13 (thiết kế + rà plan) | 05/11 chiều | 05/11 chiều |
| Nguyễn Hùng Sơn | B13 (FE) | 06/11 sáng | 06/11 chiều |
| Nguyễn Hùng Sơn | B15 (thiết kế + rà plan) | 09/11 sáng | 09/11 sáng |
| Nguyễn Hùng Sơn | B15 (FE) | 09/11 chiều | 10/11 chiều |
| Nguyễn Hùng Sơn | B17 (thiết kế + rà plan) | 11/11 sáng | 11/11 sáng |
| Nguyễn Hùng Sơn | B17 (FE) | 11/11 chiều | 12/11 chiều |
| Nguyễn Hùng Sơn | B18 (thiết kế + rà plan) | 13/11 sáng | 13/11 sáng |
| Nguyễn Hùng Sơn | B18 (FE) | 13/11 chiều | 16/11 sáng |
| vietlh | B02 (thiết kế BE) | 16/10 sáng | 16/10 sáng |
| vietlh | B02 (BE) | 16/10 chiều | 21/10 chiều |
| vietlh | B05 (thiết kế BE) | 22/10 sáng | 22/10 sáng |
| vietlh | B05 (BE) | 22/10 chiều | 23/10 chiều |
| vietlh | B06 (thiết kế BE) | 26/10 sáng | 26/10 sáng |
| vietlh | B06 (BE) | 26/10 chiều | 28/10 sáng |
| vietlh | B07 (thiết kế BE) | 28/10 chiều | 28/10 chiều |
| vietlh | B07 (BE) | 29/10 sáng | 30/10 chiều |
| vietlh | B08 (thiết kế BE) | 02/11 sáng | 02/11 sáng |
| vietlh | B08 (BE) | 02/11 chiều | 03/11 sáng |
| vietlh | B10 (thiết kế BE) | 03/11 chiều | 03/11 chiều |
| vietlh | B10 (BE) | 04/11 sáng | 04/11 sáng |
| vietlh | B11 (thiết kế BE) | 04/11 chiều | 04/11 chiều |
| vietlh | B11 (BE) | 05/11 sáng | 05/11 chiều |
| vietlh | B11 (FE) | 06/11 sáng | 09/11 sáng |
| vietlh | B14 (thiết kế BE) | 09/11 chiều | 09/11 chiều |
| vietlh | B14 (BE) | 10/11 sáng | 10/11 chiều |
| vietlh | B14 (FE) | 11/11 sáng | 11/11 chiều |
| vietlh | B15 (thiết kế BE) | 12/11 sáng | 12/11 sáng |
| vietlh | B15 (BE) | 12/11 chiều | 13/11 chiều |
| cuongdq (Đoàn Quang Cường) | B01 (BE) | 14/10 chiều | 15/10 chiều |
| cuongdq (Đoàn Quang Cường) | B03 (thiết kế BE) | 16/10 sáng | 16/10 sáng |
| cuongdq (Đoàn Quang Cường) | B03 (BE) | 16/10 chiều | 19/10 sáng |
| cuongdq (Đoàn Quang Cường) | B03 (FE) | 19/10 chiều | 20/10 chiều |
| cuongdq (Đoàn Quang Cường) | B04 (thiết kế BE) | 22/10 sáng | 22/10 sáng |
| cuongdq (Đoàn Quang Cường) | B04 (BE) | 22/10 chiều | 23/10 sáng |
| cuongdq (Đoàn Quang Cường) | B09 (thiết kế BE) | 23/10 chiều | 23/10 chiều |
| cuongdq (Đoàn Quang Cường) | B09 (BE) | 26/10 sáng | 27/10 sáng |
| cuongdq (Đoàn Quang Cường) | B12 (thiết kế BE) | 27/10 chiều | 27/10 chiều |
| cuongdq (Đoàn Quang Cường) | B12 (BE) | 28/10 sáng | 02/11 sáng |
| cuongdq (Đoàn Quang Cường) | B13 (thiết kế BE) | 02/11 chiều | 02/11 chiều |
| cuongdq (Đoàn Quang Cường) | B13 (BE) | 03/11 sáng | 03/11 chiều |
| cuongdq (Đoàn Quang Cường) | B16 (thiết kế BE) | 04/11 sáng | 04/11 sáng |
| cuongdq (Đoàn Quang Cường) | B16 (BE) | 04/11 chiều | 05/11 chiều |
| cuongdq (Đoàn Quang Cường) | B16 (FE) | 06/11 sáng | 09/11 sáng |
| cuongdq (Đoàn Quang Cường) | B17 (thiết kế BE) | 09/11 chiều | 09/11 chiều |
| cuongdq (Đoàn Quang Cường) | B17 (BE) | 10/11 sáng | 11/11 sáng |
| cuongdq (Đoàn Quang Cường) | B18 (thiết kế BE) | 11/11 chiều | 11/11 chiều |
| cuongdq (Đoàn Quang Cường) | B18 (BE) | 12/11 sáng | 13/11 chiều |

| Người | Tải (ngày công) | Xong phần của mình |
|---|---|---|
| Nguyễn Hùng Sơn | 23,5 | 16/11 sáng |
| vietlh | 21 | 13/11 chiều |
| cuongdq (Đoàn Quang Cường) | 21,5 | 13/11 chiều |

**Nút thắt: Sơn** (FE lms-fe mọi Bolt học viên + thiết kế Construction của tech lead tác giả): 23,5 ngày. Dev BE nhận trọn bốn Bolt ops-fe (B03, B16: cuongdq; B11, B14: vietlh) và cuongdq nhận BE của B01 (code WP3 của mình). Owner chọn bằng thử nhiều cách gán để xong sớm nhất và cân tải (Q7); hai dev BE vượt năng lực trong `assignment.md` (14 và 10,5). Lịch đã kín gần 100% cả ba người: chưa có chỗ cho review MR, ký gate của BE lead, hỗ trợ 3.6, sửa khi hypothesis không đạt. Cộng dự phòng ~15% (khoảng 3,5 ngày làm việc) thì mốc xong thực tế khoảng **19/11 chiều**; PO, CTO chốt ở họp nhận mức tải này hay thêm người (Q5).

## B01 — Nền tảng (U0 `u0-foundation`)

| Mục | Nội dung |
|---|---|
| Units | U0 (US14, US15) |
| Walking skeleton | **Walking skeleton (ngoại lệ có ký, 2.7 Q3)**: ops-fe → lms-be qua guard + Casbin thật, RLS, Redis. Plan 3.5 đang `[R]` (ADR-016). |
| Contract | C-01, C-02, C-03 |
| Definition of Done | (1) MR lms-be vào `feature/gamification` rồi lên `staging` theo lịch BE lead; PR FE vào `staging`; deploy staging. (2) Demo dưới đây chạy trên staging. (3) TC P0 của Bolt pass (3.6; TC của Bolt có sau 2.81). (4) `x-curl` của C-01, C-02, C-03 chạy PASS, chuyển Final. (5) Ngưỡng của confidence hypothesis đạt hoặc có quyết định của lead. (6) Công tắc vẫn tắt trên production |
| Confidence hypothesis | Tên quyền + tags chặn được route thật, công tắc có hiệu lực ngay sau khi lưu (ADR-002, ADR-003); sửa trên WP3 không phá các khối khác |
| Demo | SA bật Gamification, bật Visibility (popover lần đầu), tắt; staff chỉ quyền xem thấy công tắc nhưng không bấm được; staff không quyền mở link ra 403; màn role có ba quyền gamification |
| Real project check | lms-be: curl theo `openspec/conventions/verification.md`, migration up/down, test của change `run`; FE: `/ui-gate review`, typecheck, lint |
| TC | US14: TC-1…TC-14, TC-22…TC-25; US15: TC-15…TC-20, TC-26…TC-27; REG: TC-21, TC-28…TC-30 |
| Ngày công | 3 (BE 1,5 · FE 1,5) |
| Owner | cuongdq (Đoàn Quang Cường) (BE) + Nguyễn Hùng Sơn (FE); chịu DoD cuối: cuongdq (Đoàn Quang Cường) |

## B02 — Engine ghi nhận (U1 `u1-recording-engine`)

| Mục | Nội dung |
|---|---|
| Units | U1 (US13) |
| Walking skeleton | Điểm tích hợp skeleton: hook → Kafka → event-processor → ledger; cron background-job. |
| Contract | A-01, S-02, S-03 |
| Definition of Done | (1) MR lms-be vào `feature/gamification` rồi lên `staging` theo lịch BE lead; PR FE vào `staging`; deploy staging. (2) Demo dưới đây chạy trên staging. (3) TC P0 của Bolt pass (3.6; TC của Bolt có sau 2.81). (4) `x-curl` của A-01, S-02, S-03 chạy PASS, chuyển Final. (5) Ngưỡng của confidence hypothesis đạt hoặc có quyết định của lead. (6) Công tắc vẫn tắt trên production |
| Confidence hypothesis | Hook thêm ≤ 200 ms vào thao tác hoàn thành (p95, đo trước/sau trên staging) và 0 dòng trùng khi gửi lại cùng payload ở mọi đường hoàn thành (2.43 Q14, NFR-GAM-01) |
| Demo | Trên staging: hoàn thành hoạt động, khoá, bài Test (tự chấm và chấm tay) → dòng ledger đúng, mở lại không cộng thêm, Test Account không có dòng, tắt Points → dòng 0 điểm; làm hỏng Kafka → FailedEvent → cron chạy lại |
| Real project check | lms-be: curl theo `openspec/conventions/verification.md`, migration up/down, test của change `run`; FE: `/ui-gate review`, typecheck, lint |
| TC | US13: TC-101…TC-125 |
| Ngày công | 3,5 (BE 3,5 · FE 0) |
| Owner | vietlh (trọn); chịu DoD cuối: vietlh |

## B03 — Cấu hình điểm (U3 `u3-points-config`)

| Mục | Nội dung |
|---|---|
| Units | U3 (US8) |
| Walking skeleton | Không |
| Contract | C-04 |
| Definition of Done | (1) MR lms-be vào `feature/gamification` rồi lên `staging` theo lịch BE lead; PR FE vào `staging`; deploy staging. (2) Demo dưới đây chạy trên staging. (3) TC P0 của Bolt pass (3.6; TC của Bolt có sau 2.81). (4) `x-curl` của C-04 chạy PASS, chuyển Final. (5) Ngưỡng của confidence hypothesis đạt hoặc có quyết định của lead. (6) Công tắc vẫn tắt trên production |
| Confidence hypothesis | PATCH từng trường không đè nhau khi lưu dồn dập (ADR-004) |
| Demo | Vận hành bật Points, khai điểm, điểm nền; tự lưu từng ô; giá trị mặc định 10/10/150/25 |
| Real project check | lms-be: curl theo `openspec/conventions/verification.md`, migration up/down, test của change `run`; FE: `/ui-gate review`, typecheck, lint |
| TC | US8: TC-147…TC-167 |
| Ngày công | 2,5 (BE 1 · FE 1,5) |
| Owner | cuongdq (Đoàn Quang Cường) (trọn); chịu DoD cuối: cuongdq (Đoàn Quang Cường) |

## B04 — Màn Gamification học viên (U5 `u5-learner-home`)

| Mục | Nội dung |
|---|---|
| Units | U5 (US1) |
| Walking skeleton | Điểm tích hợp skeleton: lms-fe → lms-be đọc dữ liệu engine thật. Nhận việc đưa nhánh WIP lms-fe vào (ADR-015). |
| Contract | C-13, C-14, C-15 |
| Definition of Done | (1) MR lms-be vào `feature/gamification` rồi lên `staging` theo lịch BE lead; PR FE vào `staging`; deploy staging. (2) Demo dưới đây chạy trên staging. (3) TC P0 của Bolt pass (3.6; TC của Bolt có sau 2.81). (4) `x-curl` của C-13, C-14, C-15 chạy PASS, chuyển Final. (5) Ngưỡng của confidence hypothesis đạt hoặc có quyết định của lead. (6) Công tắc vẫn tắt trên production |
| Confidence hypothesis | Nhánh WIP lms-fe đưa vào được mà không vỡ staging, và cờ ẩn hiện theo BR-1.8 đủ cho mọi thành phần |
| Demo | Học viên mở menu Gamification thấy điểm, chuỗi, huy hiệu, hạng thật do B02 ghi; hai panel How to; khối My Learning; tắt Visibility thì mất menu và link trả not found |
| Real project check | lms-be: curl theo `openspec/conventions/verification.md`, migration up/down, test của change `run`; FE: `/ui-gate review`, typecheck, lint |
| TC | US1: TC-201…TC-230 |
| Ngày công | 3 (BE 1 · FE 2) |
| Owner | cuongdq (Đoàn Quang Cường) (BE) + Nguyễn Hùng Sơn (FE); chịu DoD cuối: cuongdq (Đoàn Quang Cường) |

## B05 — Nhật ký ghi nhận Ops (U4 `u4-ops-achievement-log`)

| Mục | Nội dung |
|---|---|
| Units | U4 (US22) |
| Walking skeleton | Không. Mở công cụ kiểm giai đoạn chạy ngầm cho vận hành. |
| Contract | C-09 |
| Definition of Done | (1) MR lms-be vào `feature/gamification` rồi lên `staging` theo lịch BE lead; PR FE vào `staging`; deploy staging. (2) Demo dưới đây chạy trên staging. (3) TC P0 của Bolt pass (3.6; TC của Bolt có sau 2.81). (4) `x-curl` của C-09 chạy PASS, chuyển Final. (5) Ngưỡng của confidence hypothesis đạt hoặc có quyết định của lead. (6) Công tắc vẫn tắt trên production |
| Confidence hypothesis | Lọc nhật ký trả trang ≤ 2 giây trên dữ liệu 5 triệu dòng ledger (ED-14, 2.43 Q14) |
| Demo | Vận hành lọc nhật ký theo học viên, loại sự kiện, khoảng ngày; thấy dòng 0 điểm; chạy ngầm vẫn thấy |
| Real project check | lms-be: curl theo `openspec/conventions/verification.md`, migration up/down, test của change `run`; FE: `/ui-gate review`, typecheck, lint |
| TC | US22: TC-168…TC-187 |
| Ngày công | 3 (BE 1,5 · FE 1,5) |
| Owner | vietlh (BE) + Nguyễn Hùng Sơn (FE); chịu DoD cuối: vietlh |

## B06 — Check-in hằng ngày (U2 `u2-daily-checkin`)

| Mục | Nội dung |
|---|---|
| Units | U2 (US5) |
| Walking skeleton | Điểm tích hợp skeleton: lms-fe → check-in → Kafka. |
| Contract | C-16, A-02 |
| Definition of Done | (1) MR lms-be vào `feature/gamification` rồi lên `staging` theo lịch BE lead; PR FE vào `staging`; deploy staging. (2) Demo dưới đây chạy trên staging. (3) TC P0 của Bolt pass (3.6; TC của Bolt có sau 2.81). (4) `x-curl` của C-16, A-02 chạy PASS, chuyển Final. (5) Ngưỡng của confidence hypothesis đạt hoặc có quyết định của lead. (6) Công tắc vẫn tắt trên production |
| Confidence hypothesis | Tín hiệu thao tác thật từ lms-fe (ADR-010) đủ để phân biệt request nền |
| Demo | Mở UpLMS và bấm một mục → có ngày có mặt, chuỗi tăng; tab treo qua đêm không tính; hai thiết bị một bản ghi |
| Real project check | lms-be: curl theo `openspec/conventions/verification.md`, migration up/down, test của change `run`; FE: `/ui-gate review`, typecheck, lint |
| TC | US5: TC-126…TC-146 |
| Ngày công | 3 (BE 2 · FE 1) |
| Owner | vietlh (BE) + Nguyễn Hùng Sơn (FE); chịu DoD cuối: vietlh |

## B07 — Thông báo realtime (U6 `u6-achievement-realtime`)

| Mục | Nội dung |
|---|---|
| Units | U6 (US2) |
| Walking skeleton | Không. Hạ tầng mới; cần DevOps mở route websocket (ED). |
| Contract | A-03, S-03 |
| Definition of Done | (1) MR lms-be vào `feature/gamification` rồi lên `staging` theo lịch BE lead; PR FE vào `staging`; deploy staging. (2) Demo dưới đây chạy trên staging. (3) TC P0 của Bolt pass (3.6; TC của Bolt có sau 2.81). (4) `x-curl` của A-03, S-03 chạy PASS, chuyển Final. (5) Ngưỡng của confidence hypothesis đạt hoặc có quyết định của lead. (6) Công tắc vẫn tắt trên production |
| Confidence hypothesis | Gateway socket.io + redis-emitter chạy được qua gateway staging nhiều instance |
| Demo | Hoàn thành hoạt động → thẻ +điểm hiện góc dưới phải trong ≤ 3 giây; nhiều thẻ không gộp; offline không nhận |
| Real project check | lms-be: curl theo `openspec/conventions/verification.md`, migration up/down, test của change `run`; FE: `/ui-gate review`, typecheck, lint |
| TC | US2: TC-231…TC-250 |
| Ngày công | 3 (BE 2 · FE 1) |
| Owner | vietlh (BE) + Nguyễn Hùng Sơn (FE); chịu DoD cuối: vietlh |

## B08 — Lịch sử ghi nhận (U7 `u7-achievement-history`)

| Mục | Nội dung |
|---|---|
| Units | U7 (US3) |
| Walking skeleton | Không |
| Contract | C-17 |
| Definition of Done | (1) MR lms-be vào `feature/gamification` rồi lên `staging` theo lịch BE lead; PR FE vào `staging`; deploy staging. (2) Demo dưới đây chạy trên staging. (3) TC P0 của Bolt pass (3.6; TC của Bolt có sau 2.81). (4) `x-curl` của C-17 chạy PASS, chuyển Final. (5) Ngưỡng của confidence hypothesis đạt hoặc có quyết định của lead. (6) Công tắc vẫn tắt trên production |
| Confidence hypothesis | Trang lịch sử 20 mục trả ≤ 1 giây với học viên có 10.000 dòng ledger |
| Demo | Mở Achievement history từ panel, tải 20 mục, dòng 0 điểm không hiện |
| Real project check | lms-be: curl theo `openspec/conventions/verification.md`, migration up/down, test của change `run`; FE: `/ui-gate review`, typecheck, lint |
| TC | US3: TC-251…TC-268 |
| Ngày công | 2 (BE 1 · FE 1) |
| Owner | vietlh (BE) + Nguyễn Hùng Sơn (FE); chịu DoD cuối: vietlh |

## B09 — Cấu hình huy hiệu + trao bù (U8 `u8-badges-config`)

| Mục | Nội dung |
|---|---|
| Units | U8 (US9) |
| Walking skeleton | Không |
| Contract | C-05, A-04, S-03 |
| Definition of Done | (1) MR lms-be vào `feature/gamification` rồi lên `staging` theo lịch BE lead; PR FE vào `staging`; deploy staging. (2) Demo dưới đây chạy trên staging. (3) TC P0 của Bolt pass (3.6; TC của Bolt có sau 2.81). (4) `x-curl` của C-05, A-04, S-03 chạy PASS, chuyển Final. (5) Ngưỡng của confidence hypothesis đạt hoặc có quyết định của lead. (6) Công tắc vẫn tắt trên production |
| Confidence hypothesis | Trao bù theo lô xong ≤ 5 phút với 10.000 học viên trên dữ liệu ED-14 (BR-9.9) |
| Demo | Bật Badges sau ba tuần chạy ngầm → học viên nhận đủ mốc đã vượt, không thông báo; đổi tên, ảnh mốc |
| Real project check | lms-be: curl theo `openspec/conventions/verification.md`, migration up/down, test của change `run`; FE: `/ui-gate review`, typecheck, lint |
| TC | US9: TC-301…TC-337 |
| Ngày công | 3 (BE 1,5 · FE 1,5) |
| Owner | cuongdq (Đoàn Quang Cường) (BE) + Nguyễn Hùng Sơn (FE); chịu DoD cuối: cuongdq (Đoàn Quang Cường) |

## B10 — Tab Badges (U9 `u9-badge-gallery`)

| Mục | Nội dung |
|---|---|
| Units | U9 (US4) |
| Walking skeleton | Không |
| Contract | C-18 |
| Definition of Done | (1) MR lms-be vào `feature/gamification` rồi lên `staging` theo lịch BE lead; PR FE vào `staging`; deploy staging. (2) Demo dưới đây chạy trên staging. (3) TC P0 của Bolt pass (3.6; TC của Bolt có sau 2.81). (4) `x-curl` của C-18 chạy PASS, chuyển Final. (5) Ngưỡng của confidence hypothesis đạt hoặc có quyết định của lead. (6) Công tắc vẫn tắt trên production |
| Confidence hypothesis | Số đếm (đã đạt/tổng) trên tab khớp ô Badges của B04 với cùng học viên, sau khi tắt bật một loại |
| Demo | My Profile → Badges: đã đạt màu, chưa đạt xám, trỏ vào thấy mốc |
| Real project check | lms-be: curl theo `openspec/conventions/verification.md`, migration up/down, test của change `run`; FE: `/ui-gate review`, typecheck, lint |
| TC | US4: TC-338…TC-353 |
| Ngày công | 1,5 (BE 0,5 · FE 1) |
| Owner | vietlh (BE) + Nguyễn Hùng Sơn (FE); chịu DoD cuối: vietlh |

## B11 — Cấu hình hạng (U10 `u10-levels-config`)

| Mục | Nội dung |
|---|---|
| Units | U10 (US10) |
| Walking skeleton | Không |
| Contract | C-06 |
| Definition of Done | (1) MR lms-be vào `feature/gamification` rồi lên `staging` theo lịch BE lead; PR FE vào `staging`; deploy staging. (2) Demo dưới đây chạy trên staging. (3) TC P0 của Bolt pass (3.6; TC của Bolt có sau 2.81). (4) `x-curl` của C-06 chạy PASS, chuyển Final. (5) Ngưỡng của confidence hypothesis đạt hoặc có quyết định của lead. (6) Công tắc vẫn tắt trên production |
| Confidence hypothesis | Luật lên hạng BR-10.4a đúng khi đổi cấu hình giữa chừng |
| Demo | Đặt bội số, trần; tắt Points khoá tiêu chí, khối Levels cảnh báo; hạng chỉ tính mốc mới vượt |
| Real project check | lms-be: curl theo `openspec/conventions/verification.md`, migration up/down, test của change `run`; FE: `/ui-gate review`, typecheck, lint |
| TC | US10: TC-354…TC-388 |
| Ngày công | 2,5 (BE 1 · FE 1,5) |
| Owner | vietlh (trọn); chịu DoD cuối: vietlh |

## B12 — Bảng xếp hạng (U11 `u11-leaderboard`)

| Mục | Nội dung |
|---|---|
| Units | U11 (US6) |
| Walking skeleton | Điểm tích hợp skeleton: cron → snapshot. |
| Contract | C-19, S-03 |
| Definition of Done | (1) MR lms-be vào `feature/gamification` rồi lên `staging` theo lịch BE lead; PR FE vào `staging`; deploy staging. (2) Demo dưới đây chạy trên staging. (3) TC P0 của Bolt pass (3.6; TC của Bolt có sau 2.81). (4) `x-curl` của C-19, S-03 chạy PASS, chuyển Final. (5) Ngưỡng của confidence hypothesis đạt hoặc có quyết định của lead. (6) Công tắc vẫn tắt trên production |
| Confidence hypothesis | Một lượt cron 16 bảng cho 10.000 học viên, 5 triệu dòng xong ≤ 15 phút (ED-14); API bảng ≤ 1 giây |
| Demo | Năm bảng theo năm khung, cron 8 tiếng, Last updated; đổi khung LEVEL/BADGES biến mất |
| Real project check | lms-be: curl theo `openspec/conventions/verification.md`, migration up/down, test của change `run`; FE: `/ui-gate review`, typecheck, lint |
| TC | US6: TC-401…TC-435 |
| Ngày công | 4,5 (BE 3,5 · FE 1) |
| Owner | cuongdq (Đoàn Quang Cường) (BE) + Nguyễn Hùng Sơn (FE); chịu DoD cuối: cuongdq (Đoàn Quang Cường) |

## B13 — Vị trí của tôi (U12 `u12-my-position`)

| Mục | Nội dung |
|---|---|
| Units | U12 (US7) |
| Walking skeleton | Không |
| Contract | C-20 |
| Definition of Done | (1) MR lms-be vào `feature/gamification` rồi lên `staging` theo lịch BE lead; PR FE vào `staging`; deploy staging. (2) Demo dưới đây chạy trên staging. (3) TC P0 của Bolt pass (3.6; TC của Bolt có sau 2.81). (4) `x-curl` của C-20 chạy PASS, chuyển Final. (5) Ngưỡng của confidence hypothesis đạt hoặc có quyết định của lead. (6) Công tắc vẫn tắt trên production |
| Confidence hypothesis | Vị trí trả ≤ 1 giây và khớp thứ hạng của chính học viên trong bảng đầy đủ (so 20 học viên ngẫu nhiên) |
| Demo | Học viên ngoài top 5 thấy dòng mình, một người dưới, khoảng cách người trên |
| Real project check | lms-be: curl theo `openspec/conventions/verification.md`, migration up/down, test của change `run`; FE: `/ui-gate review`, typecheck, lint |
| TC | US7: TC-436…TC-446 |
| Ngày công | 2 (BE 1 · FE 1) |
| Owner | cuongdq (Đoàn Quang Cường) (BE) + Nguyễn Hùng Sơn (FE); chịu DoD cuối: cuongdq (Đoàn Quang Cường) |

## B14 — Cấu hình bảng xếp hạng + xem trước (U13 `u13-leaderboard-config`)

| Mục | Nội dung |
|---|---|
| Units | U13 (US11) |
| Walking skeleton | Không |
| Contract | C-07, C-08 |
| Definition of Done | (1) MR lms-be vào `feature/gamification` rồi lên `staging` theo lịch BE lead; PR FE vào `staging`; deploy staging. (2) Demo dưới đây chạy trên staging. (3) TC P0 của Bolt pass (3.6; TC của Bolt có sau 2.81). (4) `x-curl` của C-07, C-08 chạy PASS, chuyển Final. (5) Ngưỡng của confidence hypothesis đạt hoặc có quyết định của lead. (6) Công tắc vẫn tắt trên production |
| Confidence hypothesis | Đổi công tắc hiện ở lms-fe ngay lần mở trang sau (BR-11.7), không chờ cron |
| Demo | Tắt bảng, bảng khoá theo chức năng, không tắt được bảng cuối; xem trước All time |
| Real project check | lms-be: curl theo `openspec/conventions/verification.md`, migration up/down, test của change `run`; FE: `/ui-gate review`, typecheck, lint |
| TC | US11: TC-447…TC-467 |
| Ngày công | 2 (BE 1 · FE 1) |
| Owner | vietlh (trọn); chịu DoD cuối: vietlh |

## B15 — Danh sách học viên Ops (U14 `u14-ops-learner-list`)

| Mục | Nội dung |
|---|---|
| Units | U14 (US12) |
| Walking skeleton | Không |
| Contract | C-10 |
| Definition of Done | (1) MR lms-be vào `feature/gamification` rồi lên `staging` theo lịch BE lead; PR FE vào `staging`; deploy staging. (2) Demo dưới đây chạy trên staging. (3) TC P0 của Bolt pass (3.6; TC của Bolt có sau 2.81). (4) `x-curl` của C-10 chạy PASS, chuyển Final. (5) Ngưỡng của confidence hypothesis đạt hoặc có quyết định của lead. (6) Công tắc vẫn tắt trên production |
| Confidence hypothesis | Danh sách khoảng tự do ≤ 2 giây/trang và export 50.000 dòng ≤ 30 giây trên dữ liệu ED-14 (2.43 Q14) |
| Demo | Lọc khoảng tự do, sắp xếp, xuất Excel; bấm tên mở nhật ký đã lọc |
| Real project check | lms-be: curl theo `openspec/conventions/verification.md`, migration up/down, test của change `run`; FE: `/ui-gate review`, typecheck, lint |
| TC | US12: TC-468…TC-491 |
| Ngày công | 3 (BE 1,5 · FE 1,5) |
| Owner | vietlh (BE) + Nguyễn Hùng Sơn (FE); chịu DoD cuối: vietlh |

## B16 — Quản lý campaign (U15 `u15-campaign-admin`)

| Mục | Nội dung |
|---|---|
| Units | U15 (US20) |
| Walking skeleton | Không |
| Contract | C-11, C-01 |
| Definition of Done | (1) MR lms-be vào `feature/gamification` rồi lên `staging` theo lịch BE lead; PR FE vào `staging`; deploy staging. (2) Demo dưới đây chạy trên staging. (3) TC P0 của Bolt pass (3.6; TC của Bolt có sau 2.81). (4) `x-curl` của C-11, C-01 chạy PASS, chuyển Final. (5) Ngưỡng của confidence hypothesis đạt hoặc có quyết định của lead. (6) Công tắc vẫn tắt trên production |
| Confidence hypothesis | Lưu lúc vắt qua 00:00 giờ tổ chức áp đúng luật trạng thái tại lúc lưu (BR-20.10): chỉ tên được lưu |
| Demo | Tạo, sửa, xoá theo trạng thái; quyền học viên chỉ xem; popover tắt Gamification nêu số campaign |
| Real project check | lms-be: curl theo `openspec/conventions/verification.md`, migration up/down, test của change `run`; FE: `/ui-gate review`, typecheck, lint |
| TC | US20: TC-501…TC-530 |
| Ngày công | 3 (BE 1,5 · FE 1,5) |
| Owner | cuongdq (Đoàn Quang Cường) (trọn); chịu DoD cuối: cuongdq (Đoàn Quang Cường) |

## B17 — Campaign phía học viên (U16 `u16-campaign-board`)

| Mục | Nội dung |
|---|---|
| Units | U16 (US19) |
| Walking skeleton | Không. Chưa có design (OQ-45): ui-map Provisional. |
| Contract | C-21, S-03 |
| Definition of Done | (1) MR lms-be vào `feature/gamification` rồi lên `staging` theo lịch BE lead; PR FE vào `staging`; deploy staging. (2) Demo dưới đây chạy trên staging. (3) TC P0 của Bolt pass (3.6; TC của Bolt có sau 2.81). (4) `x-curl` của C-21, S-03 chạy PASS, chuyển Final. (5) Ngưỡng của confidence hypothesis đạt hoặc có quyết định của lead. (6) Công tắc vẫn tắt trên production |
| Confidence hypothesis | Bảng Points của campaign bằng tổng điểm ledger lọc theo khoảng và loại hành động (so tay 5 học viên), cập nhật cùng lượt cron với bảng chung |
| Demo | Học viên chọn campaign đang chạy, xem bảng tạm tính và vị trí |
| Real project check | lms-be: curl theo `openspec/conventions/verification.md`, migration up/down, test của change `run`; FE: `/ui-gate review`, typecheck, lint |
| TC | US19: TC-531…TC-550 |
| Ngày công | 3 (BE 1,5 · FE 1,5) |
| Owner | cuongdq (Đoàn Quang Cường) (BE) + Nguyễn Hùng Sơn (FE); chịu DoD cuối: cuongdq (Đoàn Quang Cường) |

## B18 — Đóng băng + kết quả campaign (U17 `u17-campaign-results`)

| Mục | Nội dung |
|---|---|
| Units | U17 (US21) |
| Walking skeleton | Điểm tích hợp skeleton: job đóng băng. |
| Contract | C-12, C-21, S-03 |
| Definition of Done | (1) MR lms-be vào `feature/gamification` rồi lên `staging` theo lịch BE lead; PR FE vào `staging`; deploy staging. (2) Demo dưới đây chạy trên staging. (3) TC P0 của Bolt pass (3.6; TC của Bolt có sau 2.81). (4) `x-curl` của C-12, C-21, S-03 chạy PASS, chuyển Final. (5) Ngưỡng của confidence hypothesis đạt hoặc có quyết định của lead. (6) Công tắc vẫn tắt trên production |
| Confidence hypothesis | Đóng băng đúng biên dù có ghi lại trễ (C11) và người bị Block sau biên vẫn có mặt (C12) |
| Demo | Campaign kết thúc: chốt người tham gia, đóng băng sau 24 giờ; Ops xem ba tab, xuất Excel; học viên xem kết quả chính thức |
| Real project check | lms-be: curl theo `openspec/conventions/verification.md`, migration up/down, test của change `run`; FE: `/ui-gate review`, typecheck, lint |
| TC | US21: TC-551…TC-565 |
| Ngày công | 3 (BE 2 · FE 1) |
| Owner | cuongdq (Đoàn Quang Cường) (BE) + Nguyễn Hùng Sơn (FE); chịu DoD cuối: cuongdq (Đoàn Quang Cường) |

## Phase boundary verification
Kiểm `traceability.json` của các stage Inception đã chạy (không có `user-stories/` vì intent v1):

| Stage | File | Kết quả |
|---|---|---|
| 2.6 domain-design | `inception/domain-design/traceability.json` | 19 US + 14 dòng AC US14/US15: OK, không GAP |
| 2.7 units-generation | `inception/units-generation/traceability.json` | 19/19 US → Unit, không GAP |
| 2.9 | Bảng Bolts | 18/18 Unit → Bolt |
| 2.81 test-cases | `inception/test-cases/test-cases.md` v2.0 | 429 TC, 19/19 US, mọi BR có TC; 63 câu PO là Accepted risk |

**Đạt** (2026-10-14): 2.81 v2.0 duyệt (DEC-T23), sensor toàn chuỗi US → Unit → Bolt → TC Đạt (429 TC, 0 lỗi); cột TC của mọi Bolt đã điền. Điều kiện của gate 2.9 (DEC-T22) đã gỡ. Bản tổng hợp `verification/phase-check-inception.md` thuộc PO, không ghi ở đây.

## Traceability
<!-- trace:start -->
| Bolt | Unit | Change ở store |
|---|---|---|
| B01 | U0 | 260923-gamification-b01-foundation |
| B02 | U1 | chưa mở |
| B03 | U3 | chưa mở |
| B04 | U5 | chưa mở |
| B05 | U4 | chưa mở |
| B06 | U2 | chưa mở |
| B07 | U6 | chưa mở |
| B08 | U7 | chưa mở |
| B09 | U8 | chưa mở |
| B10 | U9 | chưa mở |
| B11 | U10 | chưa mở |
| B12 | U11 | chưa mở |
| B13 | U12 | chưa mở |
| B14 | U13 | chưa mở |
| B15 | U14 | chưa mở |
| B16 | U15 | chưa mở |
| B17 | U16 | chưa mở |
| B18 | U17 | chưa mở |

Đạt. US đợt này: 19 · Unit: 18 · Bolt: 18 · TC: 429 · lỗi: 0.
<!-- trace:end -->
