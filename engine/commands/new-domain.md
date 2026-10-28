---
description: Dựng khung domain pack cho một sản phẩm mới trong một repo mới: manifest domain.md, khung KB, corner checklist, reset team memory. Theo DOMAIN-SETUP.md
argument-hint: <tên sản phẩm> [tên công ty]
---
# /new-domain

Dựng phần khung của một domain pack. Phần cần người, như duyệt KB, viết corner checklist, chọn template công ty, vẫn là người làm; lệnh này chỉ tạo khung, hỏi đúng câu, và ghi đúng chỗ. Đọc `DOMAIN-SETUP.md` trước khi chạy.

## 0. Kiểm an toàn
- `intents/` còn intent nào thì dừng: domain mới dựng ở repo mới, không đè lên repo đang có việc. Nói PO clone sang thư mục mới rồi chạy lại.
- `domain/domain.md` đang có thì hỏi PO: giữ `templates/` làm điểm xuất phát hay bỏ. Mọi thứ khác trong thư mục domain sẽ bị xoá; xác nhận rồi mới xoá.

## 1. Hỏi PO, một lượt
Hộp chọn hoặc chat, ghi nguyên văn:
1. Tên sản phẩm, tên công ty, portal hoặc ứng dụng con
2. Một tenant hay đa tenant; hằng số nào phải cấu hình theo tenant
3. Vai người dùng chính
4. Nguồn: tài liệu người dùng ở đâu, schema DB ở đâu, API spec ở đâu; nguồn nào còn cập nhật, nguồn nào là bản chốt
5. Thư mục ngoài repo được phép đọc để cập nhật KB
6. Sản phẩm so sánh mặc định cho Market Research, tối đa ba
7. Đích publish tài liệu: Lark, Confluence, Notion, khác; space và node cha nếu có
8. Đích User Guide: GitBook hay khác, repo nào, cho đối tượng nào
9. Template PRD của công ty: có sẵn thì đường dẫn hoặc dán nội dung; chưa có thì dùng bản hiện tại trong `templates/` làm nền
10. Tên mục của template mà công ty cấm đổi

## 2. Dựng khung
- Xoá `domain/` trừ `templates/` nếu PO giữ; tạo lại thư mục
- Viết `domain.md` theo sáu mục của `DOMAIN-SETUP.md` mục 5, điền từ câu trả lời; điểm chưa biết ghi `❓PO`, không tự điền. Mục 3 bản đồ KB liệt kê các file sẽ viết với tên và câu hỏi mỗi file trả lời, chưa có nội dung
- Viết `00-index.md` khung: bảng nguồn từ câu 4 với cột đối chiếu lần cuối để trống, danh sách file KB dự kiến, mục Trạng thái tính năng trống, mục câu hỏi để sau trống
- Tạo từng file KB trong bản đồ với frontmatter `status: chưa viết`, một dòng mô tả câu hỏi file sẽ trả lời
- Chép `engine/knowledge/corner-checklist-aws.md` thành `corner-checklist.md`, thêm đầu file dòng "Chưa viết lại cho <sản phẩm>, xem DOMAIN-SETUP.md mục 6"
- `templates/prd.md`: từ câu 9 và 10; ghi danh sách tên mục bắt buộc giữ vào `domain.md` mục 4 phần 2.42
- `memory/team.md` về bản trống: giữ đoạn mở đầu và các heading, xoá mọi dòng bài học, thêm dòng ghi ngày khởi tạo domain
- `intents/` chỉ còn `.gitkeep`

## 3. Dựng KB cùng PO
Không tự làm cả KB trong một lượt. Theo `DOMAIN-SETUP.md` mục 4: hỏi PO bắt đầu từ nguồn nào, chắt lọc thành một file, trình PO duyệt, ghi ngày đối chiếu vào `00-index.md`, rồi sang file sau. Mã rule `BR-<MODULE>-NN` cho rule có trong tài liệu chính thức, `KB-<MODULE>-NN` cho rule AI trích. Vùng nguồn không phủ ghi vào `api-surface` mục vùng chưa phủ.

## 4. Kết thúc
Trình PO: thư mục đã tạo, file nào còn `chưa viết`, câu nào trong `domain.md` còn `❓PO`, và ba việc kế tiếp: duyệt KB từng file, viết lại corner checklist, chạy thử một intent profile S. Chạy `python3 engine/scripts/po-tools.py status` để chắc engine đọc được cây mới. Tự kiểm theo checklist cuối `DOMAIN-SETUP.md`.
