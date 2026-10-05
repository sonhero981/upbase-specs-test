# Open Questions — Group

**Ngày:** 05/10/2026 · **Cập nhật:** 05/10/2026 sau khi PO trả lời
**Nguồn:** `working/ai-drafts/clarified-requirements-20261005.md`

`Blocks = Yes` nghĩa là thiếu câu trả lời thì không viết BRD được.

---

## Nhóm A — đã trả lời

| # | Câu hỏi | Đáp án |
|---|---|---|
| ~~`OQ-01`~~ | `Group Management` và `Department Management` có chạy thật không | ✅ **`Group Management` đang chạy**, phục vụ việc tạo nhóm để gửi thông báo từ Ops. Dự án này mở rộng nó.<br>**`Department Management` không chạy**, trước đây chỉ dành cho `staffs` |
| ~~`OQ-02`~~ | Nhóm khác Lớp ở điểm nào | ✅ **Nhóm gắn người, Lớp gắn nội dung.** Bảng chín tiêu chí ở `clarified-requirements` §4.1 |
| ~~`OQ-03`~~ | Một người ở cả Lớp và Nhóm, cùng được gán một khoá | ✅ **Một lượt ghi danh** |
| ~~`OQ-04`~~ | `ORG.ROL.04` là gì | ✅ Mã chức năng: mỗi vai trò gắn một phạm vi — toàn tổ chức, một hoặc nhiều nhánh nhóm chỉ định, hay chỉ những người mình quản lý |
| ~~`OQ-05`~~ | Cơ chế đồng bộ HRM | ✅ **Chưa có.** HRM là Lark, đã đồng bộ được học viên, Lark cũng đã có sẵn cây tổ chức |

---

## `OQ-06` — Số cấp tối đa của cây. PO giao phân tích

### Giới hạn số cấp giải vấn đề gì

Ba vấn đề hay bị gộp làm một, nhưng mỗi cái cần một cơ chế khác nhau:

| Vấn đề | Giới hạn số cấp có giải được không |
|---|---|
| Cây lỗi tạo vòng lặp: A là cha B, B lại là cha A | ❌ Giải bằng **kiểm chu trình khi di chuyển nhánh**, không phải bằng giới hạn độ sâu |
| Truy vấn *cha bao trùm con* (`RC-07`) chậm khi cây sâu | ❌ Giải bằng **cách lưu trữ**. Bảng `departments` cũ đã có cột `tree_id`, cho thấy hệ từng đi hướng này |
| Giao diện cây sâu quá thì không dùng được | ⚠️ Giải bằng **giới hạn hiển thị**, không phải giới hạn dữ liệu |

Nên giới hạn số cấp **không giải tốt vấn đề nào trong ba cái trên**. Giá trị thật của nó là **van an toàn chống nhập sai**: chặn người dùng vô tình tạo cây 30 cấp bằng thao tác kéo thả.

### Con số đề xuất

**Mặc định `5` cấp, cấu hình được theo từng tổ chức, trần cứng `10`.**

| Giá trị | Lý do |
|---|---|
| Mặc định `5` | Cây tổ chức doanh nghiệp phổ biến có dạng Công ty → Khối → Phòng → Nhóm → Tổ. UpBase hiện ở quy mô 132 người được gán khoá, cây thực tế nhiều khả năng chỉ 3 tới 4 cấp |
| Cấu hình được | Nhất quán với mọi cấu hình khác: gắn `tenant_id`, không đóng cứng trong mã |
| Trần cứng `10` | Quá mức này thì giao diện cây không còn đọc được, và gần như chắc chắn là nhập sai chứ không phải cơ cấu thật |

Giới hạn áp cho **từng cây gốc**, không phải tổng. `RC-02` cho phép nhiều cây song song để thể hiện cơ cấu ma trận, mỗi cây đếm độ sâu riêng.

### Cách lấy con số đúng thay vì đoán

Con số `5` ở trên là đề xuất dựa trên dạng cây phổ biến, không phải dựa trên dữ liệu thật của UpBase. Cách kiểm chứng rẻ:

**Xuất cây tổ chức hiện có trên Lark, đếm độ sâu lớn nhất, lấy số đó cộng `2`.** Cộng dư hai cấp để tổ chức còn chỗ mở rộng mà không phải đổi cấu hình ngay.

Việc này hỏi Dev được vì cây Lark đã có sẵn và đã có cơ chế đồng bộ user.

→ Thành `OQ-17`.

---

## Nhóm B — cần trả lời trước Impact Analysis

| # | Câu hỏi | Vì sao quan trọng | Hỏi ai | Blocks |
|---|---|---|---|---|
| `OQ-07` | **Xoá một nhóm thì thành viên và nội dung đã gán qua nhóm đó xử lý thế nào?** Gỡ ghi danh, giữ nguyên, hay chuyển sang nhóm cha | Yêu cầu chỉ nói *"xử lý"*. Ba cách cho ba kết quả khác hẳn nhau với học viên đang học dở | PO | No |
| `OQ-08` | **Báo cáo hồi tố cần lùi về quá khứ bao xa?** | Quyết định giữa lưu toàn bộ lịch sử thành viên hay chỉ một cửa sổ | PO | No |
| `OQ-09` | **Người có hai quản lý trở lên do thuộc nhiều nhánh thì phạm vi dữ liệu tính thế nào?** | `RC-02` cho thuộc nhiều nhánh, `RC-16` cho quản lý đọc dữ liệu nhánh mình. Hai cái gặp nhau sinh ra trường hợp này | PO | No |
| `OQ-10` | **Gán nội dung chảy xuống nhánh con: người ở nhánh con gia nhập sau khi đã gán thì có nhận không?** | `RC-08` và `RC-09` chồng lên nhau ở đúng chỗ này | PO | No |
| `OQ-11` | **Trang người học hiện quản lý trực tiếp: lấy quản lý nào khi học viên thuộc nhiều nhánh?** | `RC-17` nói *"quản lý trực tiếp"* số ít, nhưng `RC-02` cho phép nhiều | PO | No |
| `OQ-12` | **Loại quan hệ ngoài quản lý, ví dụ mentor, làm ngay đợt này hay chỉ cần thiết kế mở rộng được?** | `RC-19` quyết định làm thật hay chỉ chừa chỗ | PO | No |
| `OQ-16` | 🆕 **`Group Management` hiện làm được gì?** Nhóm phẳng hay đã có cây · một người ở được nhiều nhóm không · đang có bao nhiêu nhóm và bao nhiêu bản ghi thật · ai đang dùng | **Phần chênh giữa cái đang có và yêu cầu chính là phạm vi thật của dự án.** Không biết cái đang có thì ước lượng công sức sẽ sai | Dev | No |
| `OQ-18` | 🆕 **`ORG.ROL.04` và `ORG.GRP.09` thuộc dự án này hay dự án khác?** | Hai mã chức năng xuất hiện trong yêu cầu. `ORG.ROL.04` là phạm vi dữ liệu theo vai trò, `ORG.GRP.09` là quy tắc người gia nhập sau tự nhận nội dung. Nếu chúng thuộc dự án khác thì `RC-09` và `RC-16` phải hoãn | PO | No |
| `OQ-19` | 🆕 **Bộ nguyên tắc chứa "nguyên tắc 6" nằm ở đâu?** | PO dẫn nguyên tắc 6 để giải thích vì sao nhóm không được chứa nội dung. Bộ nguyên tắc đó nhiều khả năng còn chi phối chỗ khác trong dự án này | PO | No |

---

## Nhóm C — hỏi Dev, trước Gate 2

| # | Câu hỏi | Vì sao quan trọng | Hỏi ai | Blocks |
|---|---|---|---|---|
| `OQ-13` | **Casbin hiện cấu hình thế nào?** Đã hỗ trợ phân quyền theo phạm vi dữ liệu động chưa | `RC-16` cần quyền đọc đổi theo cây chứ không đổi theo vai trò | Dev | No |
| `OQ-14` | **Bảng `departments` hiện có bao nhiêu bản ghi?** | `Department Management` không chạy, nhưng dữ liệu cũ có thể vẫn còn và gây nhầm khi làm migration | Dev | No |
| `OQ-15` | **Truy vấn phạm vi cha bao trùm con chịu được cây sâu mấy cấp và bao nhiêu người?** | `RC-07` là rule nền của mọi báo cáo | Dev | No |
| `OQ-17` | 🆕 **Cây tổ chức trên Lark hiện sâu mấy cấp?** Xuất ra đếm độ sâu lớn nhất | Cho con số thật thay cho đề xuất `5` ở `OQ-06` | Dev | No |
| `OQ-20` | 🆕 **Cơ chế đồng bộ học viên từ Lark hiện chạy thế nào?** Theo lịch hay theo sự kiện, khoá đối chiếu là gì, xử lý xung đột ra sao | `RC-03` mở rộng chính cơ chế này sang đồng bộ cây. Biết cái đang chạy thì mở rộng rẻ hơn dựng mới | Dev | No |

---

## Trạng thái

Năm câu chặn đã đóng. `OQ-06` có đề xuất kèm cách kiểm chứng, không còn chặn.

**Viết BRD được.** Chín câu còn lại thuộc nhóm B và C, trả lời trước Gate 2 là kịp.
