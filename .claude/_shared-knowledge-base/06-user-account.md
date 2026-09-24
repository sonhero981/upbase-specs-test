# 06 — User & Account

| | |
|---|---|
| Hệ | UpLMS Ops (quản lý) · UpLMS (học viên tự xem) |
| Trạng thái | Active |
| Nguồn UG | `uplms-ops/user-management/` (3 page) · `uplms/tai-khoan/` (3 page) |

---

## 1. Hai loại tài khoản

| | **Student (Học viên)** | **Staff (Nhân sự vận hành)** |
|---|---|---|
| Đăng nhập vào | UpLMS | UpLMS Ops |
| Nguồn dữ liệu | **Đồng bộ tự động từ hệ thống nhân sự UpBase** | Tạo trên UpLMS Ops (thủ công / import) |
| Xác thực | **SSO qua Lark** hoặc mã Credential | Username + Password |
| Quên mật khẩu | **Không có** (do dùng SSO Lark) | Có — 2 cách (xem §4) |
| Role | 1 role | **Nhiều role cùng lúc** |

---

## 2. Student

### Nguyên tắc cốt lõi

> **Tài khoản và thông tin học viên được đồng bộ từ hệ thống nhân sự của tổ chức.** Không tạo thủ công, không sửa được trên UpLMS Ops — **ngoại trừ trường Username**.

Phía học viên (UpLMS), học viên **chỉ sửa được ảnh đại diện**.

### Trạng thái

| Trạng thái | Mô tả |
|---|---|
| `Active` | Đăng nhập được vào UpLMS |
| `Block` | **Không** đăng nhập được |

**4 cách chuyển trạng thái:**

1. Student List → Action → Block
2. Student List → cột Status → chuyển trực tiếp
3. Student Profile → Setting → chọn giá trị mới
4. **Tự động:** nhân sự bị xoá trong hệ thống thông tin tổ chức (nghỉ việc) → UpLMS Ops **tự chuyển sang Block**

> ⚠️ Khi học viên bị **Block**, hệ thống **tự đăng xuất tất cả thiết bị** đang đăng nhập của học viên đó.
> Học viên **không tự kích hoạt lại** — chỉ người có quyền trên UpLMS Ops mới chuyển Block → Active.

### Màn Student Profile — 3 tab

| Tab | Nội dung |
|---|---|
| Overview | Personal Information + Account Information |
| Class and Course | Danh sách khoá học đang tham gia |
| Security | Lịch sử đăng nhập UpLMS |

### Bộ lọc Student List

`Search` (Full name, Username, Email, SĐT) · `Status` (Active/Block) · `Sort by` (Họ tên) · `From Date – To Date` (ngày cập nhật)

### Export Excel

Xuất theo **điều kiện tìm kiếm hiện tại**. Trường xuất: `ID`, `Full name`, `Username`, `Email`, `Phone`, `Type User`, `Status`.

---

## 3. Staff

### Trạng thái

Giống Student (`Active` / `Block`), nhưng **chỉ 3 cách** chuyển (không có cách tự động từ hệ thống nhân sự). Block → tự đăng xuất mọi thiết bị.

### Ràng buộc

| Rule |
|---|
| **Username** và **Phone** KHÔNG sửa được sau khi tạo tài khoản |
| Mỗi nhân viên gán được **nhiều Role cùng lúc** |
| File import: `.csv` hoặc `.xlsx`, **mỗi lần 1 file** |
| `Username`, `Email`, `SĐT` trong file import phải **duy nhất**, không trùng dữ liệu đã có |

### Bộ lọc Staff List

`Search` · `Status` · `Role` · `Gender` · `Date` — kết hợp được nhiều điều kiện.

---

## 4. Reset password (Staff)

| Cách | Áp dụng cho | Luồng |
|---|---|---|
| **1 — Qua User Management** | Người **có** quyền edit Staff | Staff List → Action → Reset password → xác nhận |
| **2 — Forgot Password** | Người **không** có quyền edit Staff | Màn đăng nhập → Forgot Password → nhập email → nhận mã code qua email → Verify → nhập mật khẩu mới → Submit |

**Edit Email:** Staff List → Action → Edit Email → nhập email mới + **OTP gửi tới email đó** → Save.

---

## 5. Đăng nhập học viên (UpLMS)

| Phương thức | Ghi chú |
|---|---|
| **SSO qua Lark** | Phương thức chính |
| Mã Credential | Phương thức phụ |

Điều kiện: **học viên phải là nhân sự của UpBase** và tài khoản đã được tạo trên UpLMS.

Lỗi thường gặp: chưa có tài khoản Lark, hoặc tài khoản Lark chưa thuộc tổ chức UpBase.

---

## 6. Security (học viên tự xem)

`LMS → Profile → Security` — lịch sử đăng nhập gồm: **Thời gian đăng nhập**, **IP**, **Địa điểm đăng nhập**.

Học viên chỉ **xem**, không có thao tác đăng xuất từ xa. Phát hiện bất thường → liên hệ đội vận hành.

---

## 7. Business Rule

| ID | Rule | Nguồn |
|---|---|---|
| KB-USER-01 | Tài khoản học viên **đồng bộ tự động** từ hệ thống nhân sự UpBase, không tạo thủ công. | quan-ly-hoc-vien-student |
| KB-USER-02 | Thông tin học viên **không sửa được** trên UpLMS Ops, **trừ Username**. | quan-ly-hoc-vien-student |
| KB-USER-03 | Nhân sự bị xoá ở hệ thống tổ chức → tài khoản học viên **tự động chuyển Block**. | quan-ly-hoc-vien-student |
| KB-USER-04 | Block (student hoặc staff) → **tự đăng xuất tất cả thiết bị** đang đăng nhập. | cả 2 page |
| KB-USER-05 | Học viên/nhân sự bị Block **không tự kích hoạt lại được**; chỉ người có quyền trên Ops mới đổi về Active. | cả 2 page, mục IV |
| KB-USER-06 | **Username và Phone của Staff không sửa được** sau khi tạo. | quan-ly-nhan-vien-staff mục III |
| KB-USER-07 | Một Staff gán được **nhiều Role cùng lúc**. | quan-ly-nhan-vien-staff mục III |
| KB-USER-08 | Import Staff: Username/Email/SĐT phải **unique** so với dữ liệu đã có. | quan-ly-nhan-vien-staff mục III |
| KB-USER-09 | Học viên đăng nhập bằng **SSO Lark** → **không có chức năng Quên mật khẩu**. | dang-nhap-dang-xuat mục III |
| KB-USER-10 | Học viên **chỉ sửa được ảnh đại diện**; thông tin khác do hệ thống/vận hành quản lý. | thong-tin-tai-khoan mục III |
| KB-USER-11 | Nhân sự đăng nhập được nhưng không thấy menu → **chưa gán Role** hoặc Role không có quyền. | quan-ly-nhan-vien-staff mục IV |

---

## 8. Phụ thuộc

| Module | Quan hệ |
|---|---|
| **Hệ thống nhân sự UpBase** ⚠️ | **Nguồn chân lý của tài khoản học viên** — hệ thống ngoài, đồng bộ một chiều vào UpLMS |
| **Lark** ⚠️ | Nhà cung cấp SSO cho học viên — hệ thống ngoài |
| **Class** | Học viên được thêm vào lớp; Staff là nguồn danh sách Mentor |
| **Grading** | Mentor / Mentor chính lấy từ Staff |
| **Comment Replier** | Thành viên nhóm phải là học viên có `Test Account = Yes` |
| **Role & Permission** | Quyết định menu/chức năng nhìn thấy được |

> ⚠️ **Hai phụ thuộc ngoài hệ thống** (HRIS UpBase và Lark) là rủi ro tích hợp lớn nhất của module này. Mọi thay đổi về tài khoản phải xét cả hai.

---

---

## 8b. 🔑 `Test Account` — tài khoản kiểm thử nội bộ

✅ **PO xác nhận 23/09/2026.**

| | |
|---|---|
| **Mục đích** | **L&D và QA dùng để vào kiểm tra khoá học sau khi soạn** — giao diện đã ổn chưa, nội dung có sai gì không |
| **Bản chất** | Là **tài khoản học viên thật**, có tiến độ học thật, xuất hiện trong mọi truy vấn học viên thông thường |

### Quy tắc — rất dễ bỏ sót khi phân tích

| ID | Rule |
|---|---|
| **KB-USER-TA-01** | **`Test Account` được bỏ qua ở mọi logic nghiệp vụ.** Đây là nguyên tắc chung, không phải ngoại lệ lẻ tẻ |
| **KB-USER-TA-02** | **`Test Account` vào học thì khoá học KHÔNG bị khoá chỉnh sửa** — vẫn sửa tiếp được nếu cần. Tức là `BR-EDIT-07` (*"Test đã có người làm → không sửa được cấu hình"*) **không áp cho lượt làm bài của `Test Account`** |
| **KB-USER-TA-03** | Thành viên nhóm **Comment Replier bắt buộc là `Test Account = Yes`** (`KB-CR-01`) — nên nhóm nhân sự trả lời bình luận **đều là tài khoản kiểm thử** |

> ⚠️ **Áp dụng khi phân tích bất kỳ tính năng nào đếm, xếp hạng, thống kê hay khoá dữ liệu theo hành vi học viên:** phải hỏi *"`Test Account` có bị loại trừ không?"* — mặc định là **có**.
>
> Vì `Test Account` là học viên thật về mặt dữ liệu, mọi truy vấn không lọc sẽ **tính cả người của công ty vào số liệu học viên**.

---

## 9. Điểm cần BA xác nhận

| # | Câu hỏi |
|---|---|
| Q1 | **Danh sách Role đầy đủ là gì?** UG chỉ nói "quyền truy cập nhóm chức năng X" — chưa có ma trận Role × Chức năng. Đây là khoảng trống lớn nhất của KB. |
| Q2 | Hệ thống nhân sự UpBase là hệ nào (tên, cơ chế đồng bộ, tần suất)? |
| Q3 | Đồng bộ HRIS là một chiều hay hai chiều? Username sửa trên UpLMS có bị ghi đè ở lần sync sau không? |
| ~~Q4~~ | ~~`Test Account` là trường của Student — nằm ở đâu, ai set?~~ ✅ **Đã trả lời phần mục đích và quy tắc — xem §8b.** Còn lại: nằm ở màn nào, ai set? |
| Q5 | `Type User` trong file export có những giá trị nào? |
| Q6 | Staff có bị ảnh hưởng bởi HRIS không, hay hoàn toàn quản lý thủ công? |
| Q7 | Trang Staff có mục "Tạo tài khoản" và "Chỉnh sửa" nhưng **nội dung để trống** trong UG — quy trình thực tế thế nào? |
