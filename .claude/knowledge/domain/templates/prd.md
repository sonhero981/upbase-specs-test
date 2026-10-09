---
intent: <slug>
artifact: prd
version: 0.1
status: draft
---
# [PRD] <Tên tính năng>

> Template chuẩn UpLnD, hợp nhất từ template gốc Lark wiki `Arz6w5xvpihQcRkBLe0ljJghgsl` và bốn PRD đang dùng. Tên mục do chủ template công ty quyết giữ nguyên: Metrics success, Specific Requirement, Pre - Condition, Conner case. Tên mục do repo quyết đã đổi: References, Technical Direction, Data to Retain, Proto-Units, Traceability, Open Issues.
> Phần *in nghiêng* là hướng dẫn, xoá khi viết thật. Mục không áp dụng thì xoá hẳn, không để nội dung mẫu.

| | |
| --- | --- |
| **Target release** | *Sprint, quý* |
| **Epic** | *Link Jira* |
| **Story** | *Link Jira* |
| **Related** | *HLD Brief, tài liệu liên quan* |
| **Document status** | `DRAFT`, `IN REVIEW`, `PUBLISHED` |
| **Document owner** | |
| **Designer** | |
| **Tech lead** | |
| **QA** | |
| **Reviewer** | |

---

# Document version

| Version | Người cập nhật | Nội dung | Impact | Ngày cập nhật |
| --- | --- | --- | --- | --- |
| v0.1 | | *Bản đầu* | | |

---

# Problem

*Chép từ HLD Brief mục 2. Ai gặp, gặp khi nào, hậu quả. Không mô tả giải pháp.*

---

# Analytics

*Chép từ HLD Brief mục 2 và intent-statement mục Current workaround. Mô tả người dùng đang xoay xở thế nào, đủ chi tiết để hiểu vì sao cần thay đổi. Có số thì thêm, không có vẫn viết được.*

---

# Objective

*Chép từ HLD Brief mục 2. Kết quả, không phải danh sách việc làm.*

---

# Out of scope

*Chép từ HLD Brief mục 3. Cấp tính năng, kèm lý do một câu. Gồm cả thứ từng nằm trong phạm vi rồi bị loại theo CR nào.*

| Không làm | Vì sao |
| --- | --- |

---

# Stakeholder

| Stakeholder | Action |
| --- | --- |

---

# References

*Mọi thứ Dev và QA cần để bắt đầu. Thiếu link ở đây thì họ phải đi hỏi.*

- **HLD Brief:** *link Lark*
- **UX:** *link Figma*
- **Tài liệu kỹ thuật bên thứ ba:** *spec, docs đối tác*
- **API tham chiếu:** *endpoint hệ ngoài đang tích hợp*
- **Tài khoản tích hợp staging:** *người viết điền, không đưa lên Lark nếu nhạy cảm*
- **Tài liệu nền khác:** *KB, PRD liên quan*

---

# Metrics success

*Chép từ HLD Brief mục 2. Mỗi objective ít nhất một cách đo, chỉ giữ factor đo được. Tuyệt đối không giữ bảng ví dụ của template.*

| Factor (HEART) | Goal | Signal | Metrics |
| --- | --- | --- | --- |

---

# Solution

*Chép từ HLD Brief mục 4. Giải pháp tổng thể, đủ để hình dung cách làm trước khi vào từng US.*

## Technical Direction

*Chép từ HLD Brief mục 9 do Tech lead viết, cộng ràng buộc nghiệp vụ mà cách làm nào cũng phải thoả. Ghi cái gì phải đúng, để Dev quyết làm thế nào. Không sequence diagram, không cấu trúc bảng, không thuật toán, không thư viện.*

## Data to Retain

*Thông tin nghiệp vụ nào bắt buộc phải lưu và vì sao. Không khai bảng, cột, kiểu dữ liệu.*

| Thông tin | Vì sao phải lưu | Ràng buộc |
| --- | --- | --- |

---

# Proto-Units

*Chép từ HLD Brief mục 5 và stories.md. Nhóm US làm độc lập được, để Dev biết bắt đầu từ đâu. Dev chốt Unit thật.*

| Proto-Unit | Gồm US | Phụ thuộc | Release độc lập được? |
| --- | --- | --- | --- |

**Thứ tự đề xuất:** *PU1 rồi PU2*. Chỉ đề xuất, Dev chốt.

*Profile S bỏ mục này.*

---

# Specific Requirement

> **Quy ước đánh số:** User story `US1`, `US2` liên tục. Business rule `BR<US>.<n>`, ví dụ `BR1.1`, `BR2.3`, unique toàn PRD. US chưa làm trong phạm vi này ghi rõ trong tiêu đề: `US3: Sao chép quy tắc, chưa làm`.

## US1: <Tên user story>

### 1/ User story

*Một câu tự nhiên theo vai. Ví dụ: "Là vận hành, tôi cần mapping kho vật lý với kho kênh bán để xử lý đơn và trừ tồn đúng kho."*

### 2/ Pre - Condition

*Trạng thái dữ liệu, quyền, cấu hình, US khác đã xong.*

### 3/ Scenario

*Người dùng đi từ đâu, làm gì, theo thứ tự nào.*

### 4/ Acceptance criteria

**UI / UX / Rule UX / Rule UI**

*Dạng A, tính năng mới:*

| Màn hình | Giao diện | Field | Yêu cầu |
| --- | --- | --- | --- |
| | | | *định dạng · placeholder · options · mặc định · điều kiện disable · tooltip · validate · hành vi khi thao tác* |

*Dạng B, sửa tính năng đã có:*

| Thay đổi | Section | Field | Validate |
| --- | --- | --- | --- |

**Business requirement — Business rule**

- `BR1.1` *Rule nghiệp vụ, khẳng định kiểm chứng được. Rule chạm tính năng có sẵn thì dẫn mã KB, ví dụ `BR-EDIT-07`, `KB-CLASS-03`*
- `BR1.2` *…*

**Data Field**

*Field mới hoặc bị đổi. Field hiện có phải ghi là hiện có. US không đụng dữ liệu thì bỏ mục.*

| Field | Kiểu | Bắt buộc | Giá trị hợp lệ | Hiện có? | Ghi chú |
| --- | --- | --- | --- | --- | --- |

**NFR**

*Không có thì xoá.*

### 5/ Out of scope

*Những gì US này không làm, dù người đọc có thể tưởng là có.*

### 6/ Conner case

*Để trống. QA điền.*

---

## US2: <Tên user story>

*(Lặp đủ sáu mục.)*

---

# Traceability

| FR | US | BR |
| --- | --- | --- |

*Mọi FR có US hoặc ghi Deferred, N/A kèm lý do. Mọi BR thuộc một US. Chi tiết ở `traceability.md`.*

---

# Open Issues

| # | Nội dung | Người trả lời | Chặn việc gì |
| --- | --- | --- | --- |

---

# Comments

*Trao đổi trong quá trình review.*
