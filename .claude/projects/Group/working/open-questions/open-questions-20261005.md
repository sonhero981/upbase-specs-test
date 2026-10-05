# Open Questions — Group

**Ngày:** 05/10/2026
**Nguồn:** `working/ai-drafts/clarified-requirements-20261005.md`

`Blocks = Yes` nghĩa là thiếu câu trả lời thì không viết BRD được.

---

## Nhóm A — chặn, phải trả lời trước khi viết BRD

| # | Câu hỏi | Vì sao quan trọng | Hỏi ai | Blocks |
|---|---|---|---|---|
| `OQ-01` | **`Group Management` (9 operation) và `Department Management` (9 operation) ở Ops hiện có chạy thật không?** Nếu có thì ai đang dùng, dùng để làm gì, và chúng phủ học viên hay chỉ phủ `staffs`? | Quyết định dự án này là **làm mới** hay **mở rộng cái đã có**. Hai hướng khác nhau hoàn toàn về phạm vi, công sức và rủi ro dữ liệu cũ. Không suy ra từ việc endpoint tồn tại được: hệ này đã có ba nhóm endpoint chết | PO + Dev | **Yes** |
| `OQ-02` | **Nhóm khác Lớp ở điểm nào về mặt nghiệp vụ?** Cả hai đều gom người học và đều là đường gán nội dung | Hai khái niệm từng bị lẫn ở `CR-001` của Gamification. Lẫn ở bước này thì sửa ở bước 9 rất đắt | PO | **Yes** |
| `OQ-03` | **Một người vừa trong Lớp vừa trong Nhóm, cả hai được gán cùng một khoá, thì thành một hay hai lượt ghi danh?** | Chạm thẳng vào ràng buộc hiện có: một học viên chỉ ở một khoá trong một lớp tại một thời điểm. Nếu thành hai lượt thì mọi thống kê đếm trùng | PO | **Yes** |
| `OQ-04` | **`ORG.ROL.04` là gì?** Yêu cầu nói phạm vi dữ liệu là một giá trị chọn được ở đó | Tham chiếu ngoài không tra được, giống `TNT.CFG.02` ở Gamification. Nếu module đó chưa làm thì `RC-16` phải hoãn hoặc tự dựng | PO | **Yes** |
| `OQ-05` | **Cơ chế đồng bộ HRM hiện có chưa?** Một chiều hay hai chiều, chạy theo lịch hay theo sự kiện, khoá đối chiếu là gì | `RC-03` dựa hoàn toàn vào nó. Chưa có thì phần nhóm đồng bộ phải hoãn, chỉ làm nhóm tự tạo | PO + Dev | **Yes** |
| `OQ-06` | **Số cấp tối đa của cây là bao nhiêu?** Yêu cầu nói cấu hình được nhưng không nêu trần | Cây không giới hạn độ sâu làm truy vấn phạm vi cha bao trùm con (`RC-07`) khó dự đoán hiệu năng | PO | **Yes** |

---

## Nhóm B — cần trả lời trước Impact Analysis

| # | Câu hỏi | Vì sao quan trọng | Hỏi ai | Blocks |
|---|---|---|---|---|
| `OQ-07` | **Xoá một nhóm thì thành viên và nội dung đã gán qua nhóm đó xử lý thế nào?** Gỡ ghi danh, giữ nguyên, hay chuyển sang nhóm cha | Yêu cầu chỉ nói *"xử lý"*, không nói xử lý ra sao. Ba cách cho ba kết quả khác hẳn nhau với học viên đang học dở | PO | No |
| `OQ-08` | **Báo cáo hồi tố cần lùi về quá khứ bao xa?** Không giới hạn, hay một khoảng cụ thể | Quyết định giữa lưu toàn bộ lịch sử thành viên hay chỉ lưu một cửa sổ. Ảnh hưởng khối lượng dữ liệu | PO | No |
| `OQ-09` | **Người có hai quản lý trở lên do thuộc nhiều nhánh thì phạm vi dữ liệu tính thế nào?** Cả hai cùng đọc được, hay có thứ tự ưu tiên | `RC-02` cho phép thuộc nhiều nhánh, `RC-16` cho quản lý đọc dữ liệu nhánh mình. Hai cái gặp nhau sinh ra trường hợp này | PO | No |
| `OQ-10` | **Gán nội dung chảy xuống nhánh con: người ở nhánh con gia nhập sau khi đã gán thì có nhận không?** | `RC-08` và `RC-09` chồng lên nhau ở đúng chỗ này, yêu cầu không nói rõ cái nào thắng | PO | No |
| `OQ-11` | **Trang người học hiện quản lý trực tiếp: lấy quản lý nào khi học viên thuộc nhiều nhánh?** | `RC-17` nói *"quản lý trực tiếp"* số ít, nhưng `RC-02` cho phép nhiều | PO | No |
| `OQ-12` | **Loại quan hệ ngoài quản lý, ví dụ mentor, cần làm ngay đợt này hay chỉ cần thiết kế mở rộng được?** | `RC-19` quyết định làm thật hay chỉ chừa chỗ. Khác nhau đáng kể về công sức | PO | No |

---

## Nhóm C — hỏi Dev, trước Gate 2

| # | Câu hỏi | Vì sao quan trọng | Hỏi ai | Blocks |
|---|---|---|---|---|
| `OQ-13` | **Casbin hiện cấu hình thế nào?** Nó đã hỗ trợ phân quyền theo phạm vi dữ liệu động chưa, hay chỉ theo vai trò tĩnh | `RC-16` cần quyền đọc đổi theo cây chứ không đổi theo role. KB chưa phủ vùng phân quyền | Dev | No |
| `OQ-14` | **Bảng `departments` hiện có bao nhiêu bản ghi và ai đang ghi vào đó?** | Nếu đang có dữ liệu thật thì hướng mở rộng rủi ro hơn hướng dựng bảng mới | Dev | No |
| `OQ-15` | **Truy vấn phạm vi cha bao trùm con chịu được cây sâu mấy cấp và bao nhiêu người?** | `RC-07` là rule nền của mọi báo cáo. Chạm vào mọi màn đọc dữ liệu nhóm | Dev | No |

---

## Ghi chú

`OQ-01` là câu quan trọng nhất. Trả lời xong nó, phần lớn `Potential scope` chuyển dứt khoát sang `In scope` hoặc `Out of scope`, và cỡ dự án có thể đổi.

Năm câu còn lại ở nhóm A đều chạm vào phạm vi hoặc business rule cốt lõi, nên không viết BRD trước khi có đáp án.
