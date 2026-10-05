# Project Decisions

**Project:** Group

Nơi ghi mọi quyết định đã chốt. AI tra file này để **không hỏi lại câu đã có đáp án**.

> ⚠️ **Đây là bộ nhớ của dự án — đừng xoá trong quá trình làm việc.**

---

## Bước 2 — PO trả lời câu hỏi chặn (05/10/2026)

| Ngày | Quyết định | Lý do | Người quyết | Gate |
| --- | --- | --- | --- | --- |
| 05/10/2026 | **`OQ-01` ✅ `Group Management` có thật và đang chạy**, nhưng phục vụ mục đích khác: tạo nhóm để **gửi thông báo từ Ops**. Dự án này **mở rộng nó** thành chức năng nhóm đầy đủ | Dùng lại cái đã có thay vì dựng song song | PO | Bước 2 |
| 05/10/2026 | **Khi mở lại chức năng gửi thông báo từ Ops, chọn người nhận từ chính chức năng nhóm này** | Một nguồn nhóm duy nhất cho mọi mục đích | PO | Bước 2 |
| 05/10/2026 | **`Department Management` hiện KHÔNG chạy.** Trước đây chỉ dành cho staff | Không phải nền để mở rộng | PO | Bước 2 |
| 05/10/2026 | **`OQ-02` ✅ Nhóm gắn NGƯỜI, Lớp gắn NỘI DUNG.** Bảng so sánh chín tiêu chí do PO cung cấp, xem `clarified-requirements` §2 | Hai khái niệm từng bị lẫn ở `CR-001` của Gamification | PO | Bước 2 |
| 05/10/2026 | **Gán nội dung cho nhóm là một LUẬT ĐỨNG, không phải sao chép một lần.** Ai thuộc nhóm thì vào lớp. Người gia nhập sau vẫn tự nhận, đó là `ORG.GRP.09` | Sao chép một lần thì không khác gì nhập file | PO | Bước 2 |
| 05/10/2026 | **Nhóm không được chứa gì ngoài người.** Quan hệ nội dung với nội dung chỉ sống trong Lộ trình, quan hệ người với nội dung chỉ sống trong Lớp và Automation | Nguyên tắc 6 *(cần tra bộ nguyên tắc gốc)* | PO | Bước 2 |
| 05/10/2026 | **`OQ-03` ✅ Một lượt ghi danh.** Người vừa ở Lớp vừa ở Nhóm, cùng được gán một khoá, vẫn chỉ sinh một lượt | Giữ nguyên ràng buộc hiện có: tiến độ treo vào lượt ghi danh | PO | Bước 2 |
| 05/10/2026 | **`OQ-04` ✅ `ORG.ROL.04` là mã chức năng:** mỗi vai trò gắn một phạm vi — toàn tổ chức, một hoặc nhiều nhánh nhóm chỉ định, hay chỉ những người mình quản lý. Cùng một quyền nhưng khác phạm vi thì thấy khác nhau | | PO | Bước 2 |
| 05/10/2026 | **`OQ-05` ✅ Chưa có đồng bộ cây tổ chức.** HRM là **Lark**. Đã đồng bộ được **học viên** từ Lark sang. Dev xác nhận **Lark đã có sẵn cây tổ chức** | Nền đồng bộ user đã có, mở rộng sang cây là việc tiếp theo | PO + Dev | Bước 2 |
