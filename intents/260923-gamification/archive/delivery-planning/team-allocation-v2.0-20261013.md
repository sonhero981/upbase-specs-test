---
intent: 260923-gamification
artifact: team-allocation
stage: 2.9 delivery-planning
version: 2.0
status: approved
approved_at: 2026-10-13 ([GIẢ LẬP] họp FE, BE, PO, QA, owner Bolt, DEC-T22)
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
scope: cả intent, 19 US (DEC-T15)
consumes: inception/units-generation/ v2.0 (DEC-T20) · inception/contract-design/contract-summary.md v2.0 (DEC-T21) · inception/test-cases/test-cases.md v1.0 (US14, US15; 2.81 cả intent làm song song) · tech-state.md · lms-be openspec/changes/upbase-221099-gamification/assignment.md
supersedes: v1.0 (B01 = U0, DEC-T10)
---

# Team Allocation: Gamification, cả intent

Mob ở đây là dev code thật nhận Bolt (owner), không phải agent. Năng lực theo `assignment.md` lms-be (Đề xuất, BE lead) và tech-state (DEC-T15).

| Người | Vai trò | Năng lực đợt này | Tải được gán (code + thiết kế) | Bolt |
|---|---|---|---|---|
| Nguyễn Hùng Sơn | FE lead, tech lead tác giả | FE lms-fe + ops-fe, full-time (1 người × 5 ngày/tuần, ~10 ngày tới 28/10); kiêm tech lead tác giả (thiết kế Construction) | 23,5 ngày | B01 FE, B04 FE, B05 FE, B06 FE, B07 FE, B08 FE, B09 FE, B10 FE, B12 FE, B13 FE, B15 FE, B17 FE, B18 FE |
| vietlh | Dev BE | BE core, ~14 ngày (assignment WP0, WP1, WP2, WP5, WP7, WP8, WP9) | 21 ngày | B02 BE, B05 BE, B06 BE, B07 BE, B08 BE, B10 BE, B11 BE+FE, B14 BE+FE, B15 BE |
| cuongdq (Đoàn Quang Cường) | BE lead, dev BE | BE Ops/API/Campaign, ~10,5 ngày (WP3, WP4, WP6, WP10, WP11); kiêm BE lead review | 21,5 ngày | B01 BE, B03 BE+FE, B04 BE, B09 BE, B12 BE, B13 BE, B16 BE+FE, B17 BE, B18 BE |
| QA lead (chưa có tên) | QA | — | — | Chạy TC sau deploy mỗi Bolt (3.6) |
| PO (Bùi Đức Huy) | PO | — | — | `/change-request` Q1–Q17; design còn thiếu (OQ-45); duyệt chuỗi nháp |

## So với năng lực
- Code 50,5 ngày công (BE 28,5, FE 22), cộng thiết kế Construction 0,5 ngày mỗi người mỗi Bolt.
- vietlh 21 ngày, cuongdq 21,5 ngày — `assignment.md` có 14 và 10,5: cuongdq vượt vì nhận thêm FE ops-fe và BE của B01.
- Sơn 23,5 ngày — đường găng, kéo ngày xong tới 16/11 sáng. Chưa tính 3.6 (QA lead) và review MR.

## Cách gán
- Owner BE (chịu DoD cuối, mở change `run`, Jira) chọn để xong sớm nhất và cân tải (Q7), không theo đúng mảng của `assignment.md`: vietlh nhận engine, nhật ký Ops, check-in, realtime, lịch sử, tab Badges, hạng, cấu hình bảng, danh sách học viên; cuongdq nhận B01 (sửa WP3 của mình), cấu hình điểm, màn học viên phía API, cấu hình huy hiệu, bảng xếp hạng, vị trí của tôi, campaign. Giữ mảng core cho vietlh thì xong muộn hơn 3 ngày làm việc.
- FE: dev BE làm trọn bốn Bolt ops-fe (B03, B16 cuongdq; B11, B14 vietlh — Bolt fullstack đúng protocol); Sơn làm FE lms-fe và FE ops-fe còn lại (B05, B09, B15). Bolt hai người lệch "một owner làm trọn" (Q3 họp).
- Thiết kế Construction: owner BE viết phần BE của 3.1, 3.5; Sơn (tech lead tác giả) viết 3.41 và rà plan cho Bolt có FE của Sơn; Bolt ops-fe do dev BE làm trọn (B03, B11, B14, B16) thì dev đó viết 3.41, Sơn duyệt ở gate FE lead (không tính ngày); B01 Sơn viết lại plan `[R]`. Thiết kế B13 có thể bắt đầu trước khi plan B12 duyệt — chấp nhận, rà lại khi B12 duyệt.
- Bolt không phụ thuộc nhau chạy song song khác owner BE; FE xếp theo thứ tự Bolt.

## Đề xuất giảm nút thắt (PO, CTO chốt ở họp, Q5)
1. Đã áp: dev BE làm trọn bốn Bolt ops-fe (B03, B11, B14, B16).
2. Thêm một dev FE lms-fe, hoặc giao 3.1 của Bolt BE-nặng (B02, B06, B07, B12, B18) cho BE lead viết: rút đường găng của Sơn.
3. Cắt đợt release: đợt 1 tới B15, campaign (B16–B18) đợt 2.
