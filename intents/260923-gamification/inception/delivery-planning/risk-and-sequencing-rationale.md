---
intent: 260923-gamification
artifact: risk-and-sequencing-rationale
stage: 2.9 delivery-planning
version: 2.0
status: approved
approved_at: 2026-10-13 ([GIẢ LẬP] họp FE, BE, PO, QA, owner Bolt, DEC-T22)
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
scope: cả intent, 19 US (DEC-T15)
consumes: inception/units-generation/ v2.0 (DEC-T20) · inception/contract-design/contract-summary.md v2.0 (DEC-T21) · inception/test-cases/test-cases.md v1.0 (US14, US15; 2.81 cả intent làm song song) · tech-state.md · lms-be openspec/changes/upbase-221099-gamification/assignment.md
supersedes: v1.0 (B01 = U0, DEC-T10)
---

# Risk and Sequencing Rationale: Gamification, cả intent

## Cách xếp
Không chấm WSJF (Weighted Shortest Job First: giá trị và độ gấp chia cho độ lớn) bằng điểm số: 18 Bolt gần cùng cỡ, phụ thuộc DAG đã quyết phần lớn thứ tự. Dùng ba nguyên tắc theo thứ tự ưu tiên (Q1 họp):
1. **Skeleton trước** (Cockburn): B01 (nhánh Ops), rồi Bolt mở từng điểm tích hợp mới sớm nhất có thể: B02 (hook → Kafka → ledger), B04 (lms-fe → lms-be), B06 (check-in), B07 (socket), B12 (cron), B18 (job đóng băng).
2. **Rủi ro trước** (Cohn): engine (B02) vì mọi thứ đọc dữ liệu của nó; realtime (B07) vì hạ tầng mới. Rủi ro tải của bảng xếp hạng đo sớm qua B05 (đọc ledger lớn) trước B12; B12 giữ vị trí theo giá trị vì phụ thuộc chỉ B02, B04 nên có thể kéo lên nếu B05 đo không đạt.
3. **Giá trị trước**: theo thứ tự đề xuất của PRD (Nền tảng → Điểm → Hiển thị → Huy hiệu → Hạng → Bảng xếp hạng → Campaign). B05 nhật ký Ops đi sớm vì là công cụ duy nhất kiểm giai đoạn chạy ngầm (PRD US22).

## Đối chiếu DAG 2.7
Thứ tự B01…B18 là một thứ tự topo hợp lệ của DAG (script kiểm khi sinh lịch). Lệch so với thứ tự PRD: B04 (Hiển thị) trước B06 (check-in, thuộc nhóm Điểm) vì check-in cần API client và múi giờ của U5 (cạnh U2 → U5).

## Rủi ro
| # | Rủi ro | Khả năng | Ảnh hưởng | Giảm thiểu |
|---|---|---|---|---|
| R1 | Sơn là đường găng (~23,5 ngày gồm thiết kế) | Chắc chắn | Cao | cuongdq nhận FE ops-fe đơn giản; đề xuất ở `team-allocation.md`; FE mock theo contract Agreed |
| R2 | Đưa nhánh WIP lms-fe (238 file, lệch staging) vào lâu hơn 0,5 ngày | Trung bình | Trung bình | B04 làm sớm; 3.1 U5 xem lại; phần UI của Bolt sau giữ sau cờ |
| R3 | Route websocket qua gateway staging chưa có | Trung bình | Cao cho B07 | DevOps (ED-08) trước B07; fallback: thẻ chỉ hiện khi mở màn Gamification |
| R4 | Ledger lớn làm US12, US22, cron All time chậm | Trung bình | Trung bình | Đo ở B05, B12, B15 (2.43 Q14); đường lui bảng tổng hợp (ADR-014) |
| R5 | Sửa WP3 tại chỗ đụng code cuongdq đang làm | Trung bình | Trung bình | B01 trước mọi Bolt cấu hình; cuongdq review MR B01 |
| R6 | Chữ ký giả lập (PO, BE lead) cần người thật xác nhận | Chắc chắn | Cao | Họp thật trước khi code; DEC-T15…T21 đánh dấu [GIẢ LẬP] |
| R7 | Design thiếu (campaign học viên, nhật ký Ops, My Learning) | Chắc chắn | Trung bình | ui-map Provisional; B05, B17 làm theo component chuẩn |

## Release constraints
- Mọi Bolt lên production an toàn vì công tắc tắt mặc định (BR-14.6, 2.43 Q4). Bật chạy ngầm (Gamification bật, Visibility tắt) trên production cần tối thiểu B02 (ghi nhận), B03 (bật Points và hành động, không thì chỉ có dòng 0 điểm), B05 (công cụ kiểm), B06 (ngày có mặt và chuỗi, BR-5.12, BR-5.13).
- Bật Visibility cho học viên cần thêm B04, B07, B08 (màn, thông báo, lịch sử) trên nền chạy ngầm; Badges sau B09 + B10; Levels sau B11; Leaderboard sau B12 + B13 + B14; Campaign sau B16 + B17 + B18.
- Migration (cột `visibility_first_enabled_at`, `object_name_snapshot`, `kind`, bảng `gamification_campaign_participants`) đi cùng Bolt sở hữu, mỗi cái có down.
- lms-be: MR vào `feature/gamification` rồi lên nhánh sprint / `staging` theo `openspec/conventions/git.md` và lịch BE lead.
