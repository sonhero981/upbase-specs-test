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

## Bước 3 — PO trả lời đợt hai (05/10/2026)

| Ngày | Quyết định | Lý do | Người quyết | Gate |
| --- | --- | --- | --- | --- |
| 05/10/2026 | **`OQ-10` ✅ Có công tắc tự ghi danh khi tạo nhóm.** Chuỗi tiếng Anh: `New group members will be automatically enrolled to this group's existing course`. Chọn bật hay tắt lúc tạo nhóm | | PO | Bước 3 |
| 05/10/2026 | **`OQ-11` ✅ Trang người học hiện NHIỀU quản lý**, không phải một | Người thuộc nhiều nhánh thì có nhiều quản lý, hiện đủ | PO | Bước 3 |
| 05/10/2026 | **`OQ-12` ✅ Loại quan hệ `mentor` làm luôn đợt này**, không hoãn | | PO | Bước 3 |
| 05/10/2026 | **`OQ-16` ✅ Bỏ qua phần `Group Management` đang có, coi như chưa có gì.** Thiết kế như làm mới | Tránh bị ràng buộc bởi cái cũ khi cái cũ phục vụ mục đích khác | PO | Bước 3 |
| 05/10/2026 | **`OQ-18` ✅ Phạm vi dữ liệu đơn giản hoá: quản lý chỉ xem được nhóm mình quản lý, không xem được nhóm khác.** Không cần cơ chế phạm vi nhiều mức của `ORG.ROL.04` ở đợt này | Giảm phạm vi, bỏ phụ thuộc vào một module chưa làm | PO | Bước 3 |
| 05/10/2026 | **`OQ-19` ✅ Nguyên tắc 6 chưa có trong KB, phải bổ sung.** Đã tạo `16-domain-principles.md` | PO chỉ ra: dự án mới thì nguyên tắc mới, không thể có sẵn trước | PO | Bước 3 |
| 05/10/2026 | **Bỏ toàn bộ câu hỏi kỹ thuật cho Dev (nhóm C).** Không làm Technical Design chi tiết | Dev phân tích lại bằng công cụ của họ. Thiết kế sai từ PO **neo suy nghĩ người đọc**, tốn công gỡ hơn là không có gì. Đã ghi thành quy tắc trong `CLAUDE.md` | PO | Bước 3 |
| 05/10/2026 | **`OQ-06` ✅ Cây tổ chức thật trên Lark sâu 4 cấp** dưới gốc. Số cấp tối đa chốt **6**, cấu hình được theo tổ chức | Đo từ file HRM thật: 384 nhân sự, 53 phòng ban, 5 khối cấp 1. Chỉ 2 phòng ban chạm cấp 4 | PO + dữ liệu | Bước 3 |

