# Memory: 261005-group
Nhật ký quan sát trong lúc làm. AI ghi, PO đọc tại gate. Mỗi dòng: thời gian, stage, một câu, hai câu ngữ cảnh. Dòng được giữ tại gate sẽ chuyển sang `.claude/memory/team.md`.

## Interpretations
- 2026-10-09T11:30 [CR1] Lời PO "tiếp tục" sau gate có khuyến nghị Request Changes được hiểu là chọn đúng khuyến nghị đó. PO đã hai lần trả lời bằng cách chấp nhận khuyến nghị; nếu muốn khác, lời trả lời sẽ nói rõ.
- 2026-10-09T10:00 [migration] BRD v1 được xem là artifact của cả ba stage 1.1, 1.4, 1.7; không tách thành intent-statement, scope-document, initiative-brief. Tách sẽ phải viết lại nội dung đã duyệt. Người đọc cần bản một trang thì chạy bổ sung 2.41 HLD Brief, nó phục vụ đúng việc đó.
- 2026-10-09T10:00 [migration] competitive-analysis v0.2 đánh dấu `[?]` dù là stage Ideation, vì §9.2 đang chờ PO đọc và có thể sinh CR cho PRD. Trạng thái chờ duyệt mô tả đúng việc đang treo.

## Deviations
- 2026-10-09T11:00 [CR1] Lời PO "theo đề xuất, tiếp tục" được hiểu là duyệt 1.2 kèm chỉ thị và xác nhận luôn bảng ảnh hưởng đã trình ở gate, nên không trình lại impact preview trước khi sửa. Bảng ảnh hưởng đã nằm trong thông điệp gate, hỏi lại là hỏi hai lần.
- 2026-10-09T10:00 [migration] Giữ họ mã v1 (RC, OQ, BA, F, U, BR-x.y) thay vì đổi sang FR, PU, BR1.1 theo GLOSSARY. Đổi mã trên PRD đã publish sẽ làm lệch bản Lark và mọi tham chiếu trong Gamification, Report-Phase-1.

## Tradeoffs
- 2026-10-09T10:00 [migration] Chụp archive cho bản đã duyệt từ nội dung hiện tại, không có bản chụp đúng thời điểm duyệt. BRD v0.1 lúc Gate 1 đã mất từ v1; archive chỉ bảo vệ từ hôm nay trở đi.

## Open questions
- 2026-10-09T10:00 [migration] Mục tên cũ trong PRD (Preferences, TDD, Dữ liệu phải lưu, Unit, Vấn đề tồn đọng) có đổi theo template v2 khi có CR kế tiếp không, hay giữ nguyên tới khi chủ template duyệt D8.
