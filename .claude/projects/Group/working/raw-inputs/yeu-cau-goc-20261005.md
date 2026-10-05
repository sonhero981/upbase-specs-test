# Yêu cầu gốc — Group

**Ngày nhận:** 05/10/2026
**Nguồn:** PO cung cấp, dạng bảng chụp màn hình
**Ghi nguyên văn, không diễn giải.**

---

## Mục đích PO nêu

> *"mục đích là tổ chức các nhóm học tập, để gán theo dõi đánh giá theo từng nhóm"*

---

## Nhóm `Group`

| # | Hạng mục | Mô tả |
|---|---|---|
| 1 | Cây nhóm nhiều cấp | Nhóm tổ chức theo cây, số cấp tối đa do tổ chức cấu hình. Mỗi nhóm có mã, tên, mô tả và nhóm cha |
| 2 | Một người thuộc nhiều nhóm ở nhiều nhánh | Quan hệ người và nhóm là nhiều-nhiều. Cơ cấu ma trận thể hiện bằng nhiều cây gốc chạy song song, ví dụ một cây theo phòng ban và một cây theo tuyến sản phẩm |
| 3 | Phân loại nhóm theo nguồn | Nhóm tổ chức đồng bộ từ HRM và nhóm tự do do người dùng khởi tạo. Nguồn quyết định ai được sửa cấu trúc và ai được sửa thành viên |
| 4 | Khởi tạo và chỉnh sửa nhóm | Tạo, đổi tên, đổi mô tả, di chuyển sang nhóm cha khác. Di chuyển một nhánh thì toàn bộ nhánh con đi theo và quan hệ quản lý suy ra được tính lại |
| 5 | Quản lý thành viên thủ công | Thêm và gỡ từng người hoặc nhiều người cùng lúc, có tìm kiếm trong danh sách người dùng |
| 6 | Quản lý thành viên theo lô | Tệp mẫu, tải lên, đối soát từng dòng, kết quả kèm lý do lỗi |
| 7 | Phạm vi nhóm cha bao trùm nhánh con | Mọi màn đọc dữ liệu nhóm cha đều gồm người ở toàn bộ nhánh bên dưới. Quy tắc mặc định, và là nền của mọi báo cáo theo nhóm |
| 8 | Gán nội dung cho nhóm | Chọn một nhóm làm đối tượng nhận nội dung, có tùy chọn gán chảy xuống các nhánh con. Tùy chọn quyết định theo từng lần gán, mặc định tắt |
| 9 | Quy tắc với người gia nhập nhóm sau khi đã gán | Cấu hình cho từng nhóm: người mới vào có tự nhận nội dung đã gán cho nhóm hay không, và nhận toàn bộ hay chỉ nội dung còn hiệu lực |
| 10 | Danh sách nhóm, tìm kiếm và lọc | Xem dạng cây hoặc dạng bảng, lọc theo nguồn, cấp, trạng thái, người quản lý |
| 11 | Nhật ký thay đổi thành viên | Ghi ai vào nhóm nào, ai ra, lúc nào, do người thao tác hay do đồng bộ. Báo cáo hồi tố dựa vào đây để biết tại một thời điểm trong quá khứ ai thuộc nhóm nào |
| 12 | Lưu trữ và xóa nhóm | Nhóm lưu trữ thì không nhận nội dung mới nhưng dữ liệu lịch sử giữ nguyên. Xóa thì xử lý thành viên và các nội dung đã gán qua nhóm đó |

## Nhóm `User Group Relationship`

| # | Hạng mục | Mô tả |
|---|---|---|
| 13 | Gán người quản lý cho nhóm | Một nhóm có một hoặc nhiều người quản lý. Người quản lý là một người dùng trong hệ thống, không phải một vai trò riêng |
| 14 | Suy ra quản lý theo cây nhóm | Người không được chỉ định đích danh thì quản lý là người quản lý của nhóm cha gần nhất có gán. Quan hệ tính động, cây đổi thì quan hệ đổi theo |
| 15 | Chỉ định quản lý trực tiếp trên hồ sơ | Gán đích danh trên hồ sơ một người, ghi đè kết quả suy ra từ cây. Dùng cho báo cáo chéo nhánh và giai đoạn bàn giao |
| 16 | Phạm vi dữ liệu theo quan hệ quản lý | Người quản lý đọc được dữ liệu của mọi người trong nhánh mình phụ trách, không đọc được nhánh khác cùng cấp. Phạm vi này là một giá trị chọn được ở `ORG.ROL.04` |
| 17 | Người học xem người quản lý của mình | Trên trang người học, hiện ai là quản lý trực tiếp và đường liên hệ |
| 18 | Xử lý khi người quản lý rời vị trí | Tài khoản người quản lý bị khóa hoặc rời nhóm thì hệ thống cảnh báo các nhóm đang trống quản lý và cho chuyển toàn bộ quan hệ sang người khác |
| 19 | Các loại quan hệ khác ngoài quản lý | Khai thêm loại quan hệ như mentor, dùng chung cơ chế gán và cơ chế phạm vi dữ liệu |

---

## Tham chiếu ngoài xuất hiện trong yêu cầu

| Mã | Ngữ cảnh | Trạng thái |
|---|---|---|
| `ORG.ROL.04` | Phạm vi dữ liệu theo quan hệ quản lý là một giá trị chọn được ở đây | ❓ Chưa tra được, giống trường hợp `TNT.CFG.02` ở dự án Gamification |
