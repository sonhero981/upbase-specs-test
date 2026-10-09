# 02 — Question Bank & Case Study

| | |
|---|---|
| Hệ | UpLMS Ops |
| Đường dẫn | Academic Management → Course & Materials → Question Bank / Case Study |
| Trạng thái | Active |
| Nguồn UG | `academic-management/question-bank.md`, `academic-management/case-study.md` |

---

## 1. Question Bank

### 1.1 Phạm vi

| | |
|---|---|
| Module chính | Question Bank |
| Chức năng chính | Question / Câu hỏi |
| Module liên quan | Case Study, Storyline, Test/Quiz |
| Điều kiện | Tài khoản có quyền truy cập nhóm chức năng **Question Bank** |

**Question Bank là kho dùng chung.** Câu hỏi tạo một lần, được tiêu thụ bởi Test, Quiz, Case Study và Storyline. Đây là điểm giao lớn nhất của hệ thống — thay đổi ở đây lan ra 4 module.

### 1.2 Tám loại câu hỏi

| # | Loại | Ràng buộc đáp án |
|---|---|---|
| 1 | Đúng/Sai | ≥1 đáp án đúng **và** ≥1 đáp án sai. Không được cùng đúng hoặc cùng sai |
| 2 | Một lựa chọn | ≥1 đúng **và** ≥1 sai. Không được cùng đúng hoặc cùng sai |
| 3 | Nhiều lựa chọn | ≥1 đúng; **có thể tất cả đều đúng**. Không yêu cầu số đáp án sai tối thiểu |
| 4 | Ghép đáp án | ≥2 bộ đáp án (cột trái ↔ cột phải). **Bộ trống 1 hoặc cả 2 cột → hệ thống bỏ qua** |
| 5 | Chọn từ | Mỗi `[ ]` = một chỗ trống, mỗi chỗ trống là một nhóm đáp án, có thể nhiều đáp án đúng. Học viên chọn trúng 1 trong các đáp án đúng là tính đúng |
| 6 | Điền từ | Như Chọn từ, nhưng học viên **điền** thay vì chọn |
| 7 | Kéo thả | Mỗi `[ ]` = một chỗ trống; hệ thống tự thêm Input tương ứng. **Số Input ≥ số chỗ trống**; Input dư dùng làm đáp án gây nhiễu |
| 8 | Tự luận | Có thêm Response Option và Requirements (xem §1.3) |

### 1.3 Field

**Trường chung mọi loại:**

| Field | Bắt buộc | Ghi chú |
|---|---|---|
| Question Layout | **Có** | Cách hiển thị câu hỏi phía học viên, chọn từ giá trị cho trước |
| Self Reflection | Không | Câu hỏi tự phản chiếu, **không dùng để tính điểm** |
| Câu hỏi tự do | Không | Nếu bật → **ẩn trường Belong to** |
| Belong to | **Có** | Ẩn khi "Câu hỏi tự do". Xác định câu hỏi thuộc cấu phần nào: Course → Section → Activity → Test/Quiz, điền lần lượt trái sang phải |
| Nội dung câu hỏi | **Có** | Đề bài. *Ngoại lệ:* câu tự luận có Requirements thì để trống trường này |
| Danh sách đáp án | **Có** | Tuỳ loại câu hỏi |
| Explanation | **Có** | Lời giải chi tiết |

**Riêng loại Tự luận:**

| Field | Bắt buộc | Giá trị |
|---|---|---|
| Response Option | **Có** | `Word` \| `Excel` |
| Requirements | **Có** | Các ý nhỏ của câu tự luận |

### 1.4 Ma trận chỉnh sửa khi đã có học viên làm

Câu hỏi **chưa có học viên làm** → sửa được toàn bộ. Đã có người làm thì theo bảng (Y = sửa được):

| Trường | Đúng/Sai | Một LC | Nhiều LC | Ghép | Chọn từ | Điền từ | Kéo thả | Tự luận |
|---|---|---|---|---|---|---|---|---|
| Self Reflection | N | N | N | N | N | N | N | N |
| Question Layout | Y | Y | Y | Y | Y | Y | Y | Y |
| Câu hỏi tự do | N | N | N | N | N | N | N | N |
| Belong To | Y | Y | Y | Y | Y | Y | Y | Y |
| Nội dung câu hỏi | Y | Y | Y | Y | **N** | **N** | **N** | Y |
| Danh sách đáp án | N | N | N | N | N | N | N | N |
| Explanation | Y | Y | Y | Y | Y | Y | Y | Y |

> Ba loại **Chọn từ / Điền từ / Kéo thả** không sửa được nội dung câu hỏi vì nội dung chứa dấu `[ ]` định nghĩa chỗ trống — sửa sẽ phá vỡ ánh xạ đáp án. `[suy ra]`

### 1.5 Business Rule

| ID | Rule | Nguồn |
|---|---|---|
| KB-QB-01 | **Không xoá được câu hỏi đã thêm vào Test/Quiz/Case Study/Storyline.** | question-bank mục II |
| KB-QB-02 | Câu hỏi "Self Reflection" không dùng để tính điểm. | question-bank mục II |
| KB-QB-03 | Bật "Câu hỏi tự do" → trường Belong to bị ẩn, câu hỏi không gắn cấu phần học nào. | question-bank mục II + IV |
| KB-QB-04 | Với câu Ghép đáp án, bộ đáp án trống ở 1 hoặc cả 2 cột **bị hệ thống bỏ qua** (không báo lỗi). | question-bank mục II |
| KB-QB-05 | Câu tự luận có Requirements → điền nội dung vào Requirement, **để trống trường Nội dung câu hỏi**. | question-bank mục II |

> ⚠️ **KB-QB-04 là rule im lặng** — dữ liệu bị bỏ qua mà không cảnh báo. Loại rule này rất dễ gây bug khi có thay đổi liên quan.

---

## 2. Case Study

| | |
|---|---|
| Module chính | Case Study |
| Module liên quan | Question List |
| Điều kiện | Quyền truy cập **cả Question Bank và Case Study** |

### 2.1 Đặc tính

| Thuộc tính | Giá trị |
|---|---|
| Tính điểm | **Không** — Case Study không phải hoạt động tính điểm |
| Số lượt làm (học viên) | **1 lượt duy nhất** |
| Nguồn câu hỏi | Chọn từ Question Bank |
| Chỉnh sửa khi đã có người làm | **Được** — vì không tính điểm |

> Đây là ngoại lệ đáng chú ý: mọi thứ khác bị khoá khi "đã có học viên làm", riêng Case Study vẫn sửa được. Lý do UG nêu: không tính điểm.

### 2.2 Reorder câu hỏi

| Ràng buộc |
|---|
| Chỉ điền **số nguyên dương** |
| Thứ tự lớn nhất ≤ tổng số Question trong Case Study |
| **Không được trùng thứ tự** |

### 2.3 Business Rule

| ID | Rule | Nguồn |
|---|---|---|
| KB-CS-01 | Case Study **không tính điểm** nên được chỉnh sửa thông tin và nội dung ngay cả khi đã có học viên làm. | case-study mục II |
| KB-CS-02 | Case Study chỉ cho **1 lượt làm duy nhất**, không nộp lại được. | UG học viên `lam-case-study.md` |
| KB-CS-03 | Khu vực danh sách câu hỏi chỉ hiện **sau khi đã Save** thông tin Case Study. | case-study mục IV |

---

## 3. Phụ thuộc

| Module | Quan hệ | Chiều |
|---|---|---|
| **Test / Quiz** | Lấy câu hỏi từ Question Bank; danh sách hiển thị lọc theo Type of Test | QB → Test |
| **Case Study** | Lấy câu hỏi từ Question Bank | QB → CS |
| **Storyline** (ẩn) | Lấy câu hỏi từ Question Bank | QB → Storyline |
| **Course** | Belong to trỏ tới Course/Section/Activity | Course → QB |
| **Grading** | Câu tự luận là đối tượng chấm thủ công | QB → Grading |

---

## 4. Điểm cần BA xác nhận

| # | Câu hỏi |
|---|---|
| Q1 | "Question Layout" có những giá trị nào? UG chỉ nói "chọn 1 trong các giá trị cho trước". |
| Q2 | KB-QB-04: bộ đáp án trống bị bỏ qua **im lặng** — đúng là không có cảnh báo nào cho người tạo? |
| Q3 | Câu hỏi "tự do" (không Belong to) được dùng ở đâu, ai tiêu thụ nó? |
| Q4 | Xoá một Case Study đã có học viên làm được không? UG nói sửa được nhưng không nói về xoá. |
| Q5 | Question Bank có phân quyền theo Course/Category không, hay mọi Operator thấy toàn bộ kho? |
