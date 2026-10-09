# Memory: 260923-gamification
Nhật ký quan sát trong lúc làm. AI ghi, PO đọc tại gate. Mỗi dòng: thời gian, stage, một câu, hai câu ngữ cảnh. Dòng được giữ tại gate sẽ chuyển sang `.claude/memory/team.md`.

## Interpretations
- 2026-10-09T14:00 [migration] Bốn gate v1 đang chờ duyệt lại được giữ nguyên là `[?]` ở 1.1, 1.4, 1.7, 2.31, 2.32, 2.4, 2.42. Đây là intent duy nhất có CR mở lúc chuyển, nên gate kế tiếp của v2 chính là duyệt lại BRD v0.7.
- 2026-10-09T14:00 [migration] BRD, Impact Matrix, Solution đều có khối "mục không còn hiệu lực" ở đầu file từ v1. Giữ nguyên; khi PO duyệt lại nên cân nhắc dọn các mục đó thay vì giữ ghi chú chồng ghi chú.

## Deviations
- 2026-10-09T14:00 [migration] Giữ họ mã v1 và tên Unit, vì PRD v0.8 đã publish và Report-Phase-1 tham chiếu `US1`, `US7`.

## Tradeoffs
- 2026-10-09T14:00 [migration] Bản PRD v0.2 duyệt Gate 4 không còn trên đĩa, chỉ còn trên Lark. Archive của 2.42 vì thế trống tới lần duyệt kế tiếp.

## Open questions
- 2026-10-09T14:00 [migration] `requirements.md` (clarified v0.1) đã lệch xa sau 13 CR. Khi duyệt lại BRD, có nên tạo lại requirements theo mẫu v2 với mã FR không, hay chấp nhận BRD là nguồn yêu cầu của intent này.
