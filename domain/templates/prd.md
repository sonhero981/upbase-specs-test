---
intent: <slug>
artifact: prd
feature: <SP-FNNN, lấy từ intent.md>
version: 0.1
status: draft
inputs: <stories@version, requirements@version>
services: <service hoặc repo code bị chạm theo Impact Matrix; lệch với tech-design.md thì sửa qua change request>
---
# [PRD] <Tên tính năng>

> Template chuẩn UpLnD, hợp nhất từ template gốc Lark wiki `Arz6w5xvpihQcRkBLe0ljJghgsl` và bốn PRD đang dùng. Tên mục do chủ template công ty quyết giữ nguyên: Metrics success, Specific Requirement, Pre - Condition, Conner case. Tên mục do repo quyết đã đổi: References, Technical Direction, Data to Retain, Units, Traceability, Open Issues.
> Phần *in nghiêng* là hướng dẫn, xoá khi viết thật. Mục không áp dụng thì xoá hẳn, không để nội dung mẫu.

| | |
| --- | --- |
| **Mã tính năng** | *<SP>-F<NNN>, ví dụ LMS-F012. Mã ngắn trong tài liệu này đổi sang mã đầy đủ theo quy ước: US1 là US-LMS-F012-01, AC1.1 là AC-LMS-F012-01.1* |
| **Target release** | *Sprint, quý* |
| **Epic** | *Link Jira* |
| **Story** | *Link Jira* |
| **Related** | *Tài liệu liên quan lúc viết PRD. Link ba file thiết kế và Decision Brief ghi ở `intent.md` mục References, không sửa PRD đã duyệt để thêm link* |
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

*Lấy từ intent-statement. Ai gặp, gặp khi nào, hậu quả. Không mô tả giải pháp.*

---

# Analytics

*Lấy từ intent-statement, mục Current workaround. Mô tả người dùng đang xoay xở thế nào, đủ chi tiết để hiểu vì sao cần thay đổi. Có số thì thêm, không có vẫn viết được.*

---

# Objective

*Lấy từ intent-statement. Ghi kết quả mong muốn, không ghi danh sách việc làm.*

---

# Out of scope

*Lấy từ scope-document. Cấp tính năng, kèm lý do một câu. Gồm cả thứ từng nằm trong phạm vi nhưng bị loại theo CR nào.*

| Không làm | Vì sao |
| --- | --- |

---

# Stakeholder

| Stakeholder | Action |
| --- | --- |

---

# References

*Mọi thứ Dev và QA cần để bắt đầu. Thiếu link ở đây thì họ phải đi hỏi.*

- **UX:** *link Figma*
- **Tài liệu kỹ thuật bên thứ ba:** *spec, docs đối tác*
- **API tham chiếu:** *endpoint hệ ngoài đang tích hợp*
- **Tài khoản tích hợp staging:** *người viết điền, không đưa lên Lark nếu nhạy cảm*
- **Tài liệu nền khác:** *KB, PRD liên quan*

---

# Metrics success

*Lấy từ intent-statement. Mỗi objective ít nhất một cách đo, chỉ giữ factor đo được. Tuyệt đối không giữ bảng ví dụ của template.*

| Factor (HEART) | Goal | Signal | Metrics |
| --- | --- | --- | --- |

---

# Solution

*Lấy từ solution-options nếu có. Giải pháp tổng thể ở mức nghiệp vụ, đủ để hình dung trước khi vào từng US.*

## Technical Direction

*Ràng buộc nghiệp vụ mà cách làm nào cũng phải thoả. Ghi điều phải đúng, để Dev quyết làm thế nào; hướng kỹ thuật do Tech PIC viết ở tech-design.md tại 2.43. Không sequence diagram, không cấu trúc bảng, không thuật toán, không thư viện.*

## Vòng đời trạng thái

*Tuỳ chọn. Chỉ viết khi tính năng có đối tượng đổi trạng thái mà người dùng thấy, như lớp, đơn, chứng chỉ. Mức nghiệp vụ, không thiết kế bảng. Không áp dụng thì xoá mục.*

| Trạng thái | Sự kiện chuyển | Ai kích hoạt | Điều kiện | Trạng thái sau |
| --- | --- | --- | --- | --- |

## Data to Retain

*Thông tin nghiệp vụ nào bắt buộc phải lưu và vì sao. Không khai bảng, cột, kiểu dữ liệu.*

| Thông tin | Vì sao phải lưu | Ràng buộc |
| --- | --- | --- |

---

# Units

*Lấy từ stories.md. Nhóm US làm độc lập được, để Dev biết bắt đầu từ đâu. Dev chốt Unit thật.*

| Unit | Gồm US | Phụ thuộc | Release độc lập được? |
| --- | --- | --- | --- |

**Thứ tự đề xuất:** *U1, sau đó U2*. Chỉ đề xuất, Dev chốt.

*Profile S bỏ mục này.*

---

# Specific Requirement

> **Quy ước đánh số:** User story `US1`, `US2` liên tục. Business rule `BR<US>.<n>`, ví dụ `BR1.1`, `BR2.3`, unique toàn PRD. US chưa làm trong phạm vi này ghi rõ trong tiêu đề: `US3: Sao chép quy tắc, chưa làm`.

## US1: <Tên user story>

### 1/ User story

*Một câu tự nhiên theo vai. Ví dụ: "Là vận hành, tôi cần mapping kho vật lý với kho kênh bán để xử lý đơn và trừ tồn đúng kho."*

**Ưu tiên:** *Must, Should hoặc Could, lấy từ stories.md. Story List đổi sang cột Priority trên Jira.*

### 2/ Pre - Condition

*Trạng thái dữ liệu, quyền, cấu hình. US khác phải xong trước thì ghi mã, ví dụ `US2`: story này chỉ đủ điều kiện giao Dev khi US đó đạt.*

### 3/ Scenario

*Người dùng đi từ đâu, làm gì, theo thứ tự nào.*

### 4/ Acceptance criteria

**Tiêu chí chấp nhận**

*Mỗi dòng một tiêu chí kiểm được, có đạt hoặc không đạt, viết theo hành vi người dùng thấy. Luồng chính và mỗi nhánh đáng kể có ít nhất một AC. Mỗi US có ít nhất một AC cho nhánh lỗi hoặc bị từ chối; mỗi ngưỡng số có AC ở giá trị biên. Mỗi BR bên dưới có ít nhất một AC trỏ tới. Validate của cùng một màn gom thành một AC trỏ về bảng UI, không mỗi dòng bảng một AC. Mã ổn định, không đánh lại.*

- `AC1.1` *Khi <điều kiện hoặc hành động>, <kết quả quan sát được>. Theo `BR1.1`*
- `AC1.2` *Khi bỏ trống field bắt buộc ở màn <tên màn>, hệ thống báo lỗi và không cho lưu, theo cột Yêu cầu của bảng UI*

**UI / UX / Rule UX / Rule UI**

*Cột Màn hình ghi tên màn. Mã màn `SCR` do Design PIC đặt ở ux-design.md tại 2.43; Story List lấy mã từ đó.*

*Dạng A, tính năng mới:*

| Màn hình | Giao diện | Field | Yêu cầu |
| --- | --- | --- | --- |
| | | | *định dạng · placeholder · options · mặc định · điều kiện disable · tooltip · validate · hành vi khi thao tác* |

*Dạng B, sửa tính năng đã có:*

| Thay đổi | Section | Field | Validate |
| --- | --- | --- | --- |

**Business requirement — Business rule**

- `BR1.1` *Rule nghiệp vụ, khẳng định kiểm chứng được. Rule chạm tính năng có sẵn thì dẫn mã KB, ví dụ `BR-EDIT-07`, `KB-CLASS-03`. Rule có điều kiện thì ghi thêm: khi nào áp · nếu vi phạm thì hệ thống làm gì*
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

*Để trống. QA viết corner case ở test-design.md; corner case làm đổi yêu cầu thì đưa vào PRD qua change request.*

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
