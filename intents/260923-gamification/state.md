---
intent: 260923-gamification
profile: L
depth: Standard
status: Running
---
# State: 260923-gamification

| | |
|---|---|
| Profile | L, lý do: v1 phân cỡ L ngày 23/09/2026, đủ 9 bước và 4 gate |
| Depth | Standard |
| Answer mode | Chat, theo cách v1 đã làm |
| Switches | summary confirmation: on · reviewer: on · learnings: on |
| Created | 2026-09-23, chuyển sang v2 ngày 2026-10-09 |

## Stages
Ký hiệu: `[ ]` chưa làm · `[-]` đang làm · `[?]` chờ duyệt · `[R]` đang sửa · `[x]` đã duyệt · `[S]` bỏ qua kèm lý do. Ghi chú `v1:` trỏ tới artifact kế thừa từ luồng v1.

### IDEATION
- [x] 1.1 intent-capture · v1: ideation/brd.md v0.8 §1 đến §4. Duyệt 2026-10-12 (DEC145), 11 finding là rủi ro chấp nhận. v0.6 Gate 1 Approved with Notes 2026-09-23
- [S] 1.2 market-research · v1 không làm
- [x] 1.4 scope-definition · v1: ideation/brd.md v0.8 §5 đến §7. Duyệt 2026-10-12 (DEC145)
- [x] 1.7 approval-handoff · v1: ideation/brd.md v0.8, không có bản một trang. Duyệt 2026-10-12 (DEC145), archive/approval-handoff/brd-v0.8-20261012.md
### INCEPTION
- [x] 2.3 requirements-analysis · v1: inception/requirements-analysis/requirements.md v0.1 ngày 2026-09-23, không cập nhật sau CR; nội dung CR ở brd.md, prd.md và inputs/change-requests.md
- [x] 2.31 impact-analysis · v1: inception/impact-analysis/impact-matrix.md v0.4. Duyệt 2026-10-12 (DEC146). v0.2 Gate 2 duyệt 2026-09-23
- [x] 2.32 solution-options · v1: inception/solution-options/solution-options.md v0.2. Duyệt 2026-10-12, chốt option K (DEC147). v0.1 duyệt 2026-09-23
- [x] 2.4 user-stories · v1: inception/prd/prd.md §Danh sách user story. Duyệt 2026-10-12 cùng 2.42 (DEC157)
- [x] 2.42 prd-generation · v1: inception/prd/prd.md v0.15. Duyệt lại 2026-10-14 sau CR-014 (DEC162); v0.14 duyệt 2026-10-12 kèm ba quyết định (DEC157), sau một lần Request Changes. Archive prd-generation/prd-v0.14-20261012.md; (CR-009 đến CR-013, design, US22, technical design backend). v0.2 Gate 4 duyệt 2026-09-23. Lark đang v0.8
- [S] 2.43 design-alignment · intent đã có Epic trên Jira và đã giao Dev trước khi có stage này

## Current
| | |
|---|---|
| Stage | Mọi stage của profile đã duyệt. CR-012, CR-013, CR-014 đã đóng |
| Next action | PO trả lời OQ-42, OQ-49, OQ-52 trước Unit Campaign. Dev cập nhật technical design theo PRD v0.15 |
| Blocking questions open | 0 chặn gate; 15 câu hỏi mở trong PRD |
| Open CR | CR-015 parked, làm sau bản ra mắt (DEC166). Chưa mở lại stage nào, PRD v0.15 giữ nguyên cho bản đầu |
| Parked | no |

## Versions
| Artifact | Version | Status | Approved | Lark |
|---|---|---|---|---|
| brd | v0.8 | approved | v0.6: 2026-09-23 | — |
| requirements | v0.1 | approved | 2026-09-23 | — |
| related-features-map | v0.2 | approved | 2026-09-23 | — |
| impact-matrix | v0.4 | approved | v0.2: 2026-09-23 | — |
| solution-options | v0.2 | approved | v0.1: 2026-09-23 | — |
| initiative-brief | — | không có, v1 dùng BRD | — | — |
| prd | v0.15 | approved | v0.15: 2026-10-14 · v0.14: 2026-10-12 · v0.2: 2026-09-23 | v0.15 · Hjuxd3my6oG0UuxBGNOllABAgye, publish 2026-10-14 |

## Log
- 2026-09-23 created ở luồng v1, cỡ L. Gate 1, 2, 3, 4 trong ngày; CR-001 đến CR-008
- 2026-10-01 CR-009, CR-010, chốt design; PRD v0.3 đến v0.7
- 2026-10-05 PRD v0.8 publish Lark (Unit, Out of scope cấp tính năng)
- 2026-10-06 CR-011, PRD v0.9
- 2026-10-08 CR-012 và CR-013 gộp, chạy lại từ BRD: BRD v0.7, Impact v0.3, Solution v0.2, PRD v0.10 chờ duyệt lại
- 2026-10-09 chuyển sang luồng v2, giữ nội dung và họ mã v1; bản cũ của BRD, Impact, Solution vào archive
- 2026-10-09 PO thêm nhật ký ghi nhận bên Ops (S25 · US22), stage đang chờ duyệt nên sửa thẳng: BRD v0.8, Impact v0.4, PRD v0.11. Thêm OQ-46
- 2026-10-12 Dev thêm technical design backend (PR #3) và thay mất phần nghiệp vụ của giải pháp; PO yêu cầu dựng lại. PRD v0.12, thêm OQ-47, OQ-48. Technical design viết theo phạm vi trước CR-012, CR-013, US22, đã ghi lưu ý cho Dev
- 2026-10-12 PO đóng OQ-47 (dòng 0 điểm ẩn với học viên, hiện cho vận hành) và OQ-48 (Test Account = users.is_operator, ghi vào KB 06). PRD v0.13
- 2026-10-12 Review Product Lead lần 01: BRD NOT-READY 11 finding, PRD NOT-READY 15 finding. PO Approve BRD v0.8 (1.1 · 1.4 · 1.7), Impact v0.4 (2.31), Solution v0.2 (2.32, option K); Request Changes PRD v0.13 (2.4 · 2.42). Progress: 6/8 | INCEPTION 3/5 · Next: sửa PRD rồi trình lại 2.4 · 2.42
- 2026-10-12 Sửa PRD theo review lần 01 và tám quyết định của PO (DEC149 đến DEC156), PRD v0.14. Review lần 02: NOT-READY, 0 Critical, 3 Major mới. PO Approve kèm ba quyết định (DEC157 đến DEC160). Đóng CR-012, CR-013. Progress: 8/8 | INCEPTION 5/5 · Next: publish Lark, rồi 2.41 HLD Brief
- 2026-10-12 Publish PRD v0.14 lên Lark: doc v0.8 cũ đã bị xoá, ghi đè doc `[PRD] Gamification` hiện có trong node (Hjuxd3my6oG0UuxBGNOllABAgye, đang v0.7); chép Target release, Epic điền tay vào PRD trước khi ghi đè. Đối chiếu: heading 15/32/141/23 khớp, 11 bảng trắng, 0 sơ đồ dạng code, 10 ảnh trong mục Design
- 2026-10-14 CR-014: phần xem trước bảng xếp hạng bên Ops giữ khoảng ngày tự do. Re-entry 2.42, chỉ US11. PO duyệt PRD v0.15
- 2026-10-14 Publish PRD v0.15 lên Lark, ghi đè doc Hjuxd3my6oG0UuxBGNOllABAgye. Bảng thông tin trên Lark đã bị sửa sau 12/10 (Target release xoá trắng, bỏ ❓ ở Designer, Tech lead, QA, Reviewer), đã chép theo Lark trước khi ghi đè. Đối chiếu: heading 15/32/141/23, 11 bảng trắng, 10 ảnh
- 2026-10-19 15:04 migrate lên engine 2.1.0 bởi buidhui, DEC163
- 2026-10-19 15:11 migrate lên engine 2.1.0 bởi buidhui, DEC164
- 2026-10-20 09:26 migrate lên engine 2.1.0 bởi buidhui, DEC165
- 2026-10-25 CR-015 ghi nhận: lên hạng bằng EXP. Parked tới sau bản ra mắt, chưa archive, chưa sửa artifact. Phân tích ở inputs/change-requests.md, DEC166
- 2026-10-25 CR-015 thêm trần ngưỡng cho EXP mỗi hạng, mặc định 5.000 (DEC167). Vẫn parked
- 2026-10-26 Tạo Improvement UPLND-401 trên Jira cho CR-015, gắn epic UPLNDEP-8, backlog
- 2026-10-26 PRD v0.15 thêm ghi chú CR-015 ở US10 (callout và một dòng Out of scope), không đổi rule bản ra mắt, giữ version
- 2026-10-26 CR-015: ô EXP chuyển vào khối Levels theo design, thêm giải thích nền, bước, trần ngưỡng và câu chữ khối Levels (DEC168). Cập nhật Jira UPLND-401
- 2026-10-27 CR-015 gộp EXP vào điểm: hạng lên theo điểm tích luỹ, thêm hành động điểm cho huy hiệu, giữ bảng Level (DEC169). Sửa ghi chú trong PRD
- 2026-10-27 CR-015 ghi lý do giữ cả bảng Level và Points (DEC170), cập nhật Jira UPLND-401
