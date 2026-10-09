# Team memory

Bài học đã được PO giữ lại tại gate, áp cho mọi intent từ lần chạy sau. AI đọc file này ở bước Load của mọi stage. Thêm dòng qua vòng học, không sửa tay giữa chừng một intent. Mâu thuẫn với `CLAUDE.md` thì `CLAUDE.md` thắng, và phải hỏi PO.

Dòng đầu tiên chuyển từ các sự cố và quyết định đã ghi trong `CLAUDE.md`, command cũ và `project-decisions.md` của Group, Gamification. Ngày là ngày sự việc xảy ra.

## Versioning
- Mốc tăng version là mỗi lần PO duyệt hoặc trả lời một đợt câu hỏi, không phải mỗi lần sửa một dòng. Bản đã duyệt phải được chụp lại trước khi sửa tiếp; một lần đã ghi đè bản duyệt ở Gate 1 mười lăm lần liên tiếp (learned 2026-10-06)

## Questions
- Không dựng danh sách câu hỏi kỹ thuật cho Dev. Chỉ hỏi câu mà đáp án làm đổi phạm vi hoặc business rule (learned 2026-10-05)
- Cần biết một cơ chế kỹ thuật có tồn tại không thì hỏi PO, không tự đào Swagger rồi kết luận (learned 2026-10-05)

## PRD
- PRD không có mục Database và API. Thay bằng Data to Retain: thông tin nào phải lưu và vì sao (learned 2026-10-06)
- Không hỏi người viết ba thứ: bảng metadata, link Figma và tài khoản staging, Success Metrics. Để trống hoặc tự đề xuất, người viết điền sau (learned 2026-10-06)
- Không giữ bảng ví dụ của template. Hai PRD cũ mang nguyên chỉ số NPS của một app khác (learned 2026-09-23)
- Technical Direction chỉ nêu cái gì phải đúng, không vẽ sequence, không thiết kế bảng, không chọn thuật toán (learned 2026-10-05)
- Define hết user story kể cả cái chưa làm, ghi "chưa làm" trong tiêu đề. Bức tranh đầy đủ giúp phân tích ảnh hưởng đúng (learned 2026-09-23)

## KB
- KB chỉ phủ khoảng một nửa hệ thống. Vùng chưa phủ ghi ❓BA, không kết luận "không ảnh hưởng" (learned 2026-09-23)
- Có endpoint không có nghĩa là có tính năng. Sáu lần endpoint chết trong hệ này (learned 2026-10-06)
- Tính năng Hidden vẫn phải xét khi phân tích ảnh hưởng (learned 2026-09-23)
- Bốn rule trong KB từng sai so với hệ thống thật. Chạm vùng nào thì đọc lại nguồn vùng đó (learned 2026-09-23)

## Lark
- Node intent phải có trước. Tài liệu nằm trong node intent, không nằm thẳng dưới node cha chung (learned 2026-10-06)
- Tên tài liệu trên Lark có thể khác tên file. Lần publish sau giữ tên trên Lark, định danh là token (learned 2026-10-06)
- API trả 200 không có nghĩa nội dung vào đúng chỗ. Đếm lại heading, bảng, sơ đồ, ảnh sau mỗi lần publish (learned 2026-09-23)
- Mermaid trên Lark: stateDiagram-v2 mất dòng mô tả, dùng flowchart. Xuống dòng trong nhãn mũi tên thành node rác (learned 2026-10-06)
- Cảnh báo trước khi publish nếu tài liệu chứa tài khoản staging; người đọc trên Lark rộng hơn thư mục local (learned 2026-09-23)

## Writing
- Không viết tắt trong tài liệu bàn giao. "Giải O2" phải là "Giải quyết mục tiêu O2" (learned 2026-10-01)
- Mã đứng liền nhau phải có dấu phân cách, Lark dính `US1US6` thành một chữ (learned 2026-10-01)
- Trích mã thì kèm nội dung. Một dự án L sinh hàng trăm mã, không ai nhớ hết (learned 2026-10-01)
- Dọn dấu vết quy trình trước khi bàn giao. Dev và QA không tra được "9A" hay "Gate 3" là gì (learned 2026-09-23)
- Sơ đồ viết sẵn trong file dưới dạng Mermaid, không vẽ thêm sau khi publish. File nguồn là bản duy nhất (learned 2026-10-06)
