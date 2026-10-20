# Project memory

Bài học chỉ đúng cho sản phẩm đang cài trong `domain/`. Dựng domain mới thì đưa file này về bản trống, theo `DOMAIN-SETUP.md`. Bài học dùng chung cho mọi sản phẩm nằm ở `memory/team.md`.

AI đọc file này ở bước Load của mọi stage. Bài học có hiệu lực từ stage kế tiếp, không áp ngược cho stage đã duyệt. Vòng học tại gate ghi vào đây trước, sau đó hỏi PO bài học có đúng cho mọi sản phẩm không; có thì chuyển sang `team.md`.

Dạng một dòng: `- <nội dung> (learned YYYY-MM-DD · <intent> <mã stage> · <tên người duyệt>)`. Các dòng đầu tiên chuyển từ `team.md` ngày 19/10/2026, chỉ có ngày sự việc.

## KB
- KB chỉ phủ khoảng một nửa hệ thống. Vùng chưa phủ ghi ❓PO, không kết luận "không ảnh hưởng" (learned 2026-09-23)
- Có endpoint không có nghĩa là có tính năng. Sáu lần endpoint chết trong hệ này (learned 2026-10-06)
- Tính năng Hidden vẫn phải xét khi phân tích ảnh hưởng (learned 2026-09-23)
- Bốn rule trong KB từng sai so với hệ thống thật. Chạm vùng nào thì đọc lại nguồn vùng đó (learned 2026-09-23)

