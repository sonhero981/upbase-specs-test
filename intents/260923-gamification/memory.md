# Memory: 260923-gamification
Nhật ký quan sát trong lúc làm. AI ghi, PO đọc tại gate. Mỗi dòng: thời gian, stage, một câu, hai câu ngữ cảnh. Dòng được giữ tại gate sẽ chuyển sang `memory/team.md`.

## Interpretations
- 2026-10-09T18:00 [2.42] BRD và PRD dùng hai bộ số US khác nhau từ v1 (BRD US24 = PRD US22). Giữ nguyên để không làm gãy tham chiếu cũ; BRD ghi chú số PRD tương ứng.
- 2026-10-09T14:00 [migration] Bốn gate v1 đang chờ duyệt lại được giữ nguyên là `[?]` ở 1.1, 1.4, 1.7, 2.31, 2.32, 2.4, 2.42. Đây là intent duy nhất có CR mở lúc chuyển, nên gate kế tiếp của v2 chính là duyệt lại BRD v0.7.
- 2026-10-09T14:00 [migration] BRD, Impact Matrix, Solution đều có khối "mục không còn hiệu lực" ở đầu file từ v1. Giữ nguyên; khi PO duyệt lại nên cân nhắc dọn các mục đó thay vì giữ ghi chú chồng ghi chú.

## Deviations
- 2026-10-12T09:00 [2.42] Technical design backend của Dev (PR #3) thay cả khối nghiệp vụ của mục giải pháp thay vì thêm vào cạnh; dựng lại nguyên văn bản v0.11 dưới `## TDD`, trước `## Backend`. Nên thống nhất với Dev: technical design thêm mục mới, không sửa mục PO viết.
- 2026-10-09T18:00 [2.42] Thêm US22 mà không mở CR; các stage bị chạm (1.4, 2.31, 2.4, 2.42) đều đang `[?]` nên theo change-request §1 là sửa trong stage đang mở. Ghi DEC136 đến DEC141 để giữ dấu vết vì nó đảo một dòng Out of scope cũ của US3.
- 2026-10-09T14:00 [migration] Giữ họ mã v1 và tên Unit, vì PRD v0.8 đã publish và Report-Phase-1 tham chiếu `US1`, `US7`.

## Tradeoffs
- 2026-10-09T14:00 [migration] Bản PRD v0.2 duyệt Gate 4 không còn trên đĩa, chỉ còn trên Lark. Archive của 2.42 vì thế trống tới lần duyệt kế tiếp.

## Open questions
- 2026-10-09T18:00 [2.42] BR-13.8 hứa vận hành thấy lần cộng điểm lỗi nhưng chưa có màn nào; PO không muốn đưa vào nhật ký US22. Cần chỗ khác hoặc sửa lại chính BR-13.8 (OQ-46).
- 2026-10-09T14:00 [migration] `requirements.md` (clarified v0.1) đã lệch xa sau 13 CR. Khi duyệt lại BRD, có nên tạo lại requirements theo mẫu v2 với mã FR không, hay chấp nhận BRD là nguồn yêu cầu của intent này.
