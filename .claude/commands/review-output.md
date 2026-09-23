# Review Output – Kiểm tra và duyệt tài liệu

Review mọi loại tài liệu trong workflow: BRD · Impact Matrix · Solution Comparison · PRD · User Guide.

Dùng được cho **tài liệu AI viết** lẫn **tài liệu người khác viết** (chế độ Shadow — xem §5).

---

## Đầu vào

`$ARGUMENTS` — đường dẫn file, hoặc tên project + loại tài liệu.

> **Xác định project:** ưu tiên `$ARGUMENTS`; không có → suy từ file đang mở; >1 khả dĩ → liệt kê cho chọn. **Echo + confirm trước khi chạy.**

---

## Bước 1 – Nhận diện loại tài liệu

| Dấu hiệu | Loại | Bộ tiêu chí |
|---|---|---|
| Có `Scope` + `Danh sách US dự kiến`, không có chi tiết field | BRD | §4.1 |
| Có `Dependency Map` + `Impact Matrix` 12 vùng | Impact Matrix | §4.2 |
| Có bảng so sánh option + `Recommendation` | Solution Comparison | §4.3 |
| Có `Specific Requirement` + `Acceptance criteria` | **PRD** | §4.4 |
| Có hướng dẫn thao tác + ảnh màn hình | User Guide | §4.5 |

Không nhận diện được → hỏi người dùng, **không đoán**.

---

## Bước 2 – Input Readiness Gate

Trước khi review nội dung, kiểm tài liệu có đủ nền để tồn tại không:

| Loại | Yêu cầu nền |
|---|---|
| BRD | Clarified requirements đã có · không còn blocking question |
| Impact Matrix | BRD đã qua Gate 1 · phạm vi liên quan đã chốt |
| Solution Comparison | Impact Matrix đã qua Gate 2 |
| PRD | BRD (G1) + Impact (G2) + Solution (G3) đều đã duyệt |
| User Guide | PRD đã duyệt · tính năng đã dev xong |

**Thiếu nền → báo ngay, không review tiếp.** Review một PRD viết trên Impact Matrix chưa duyệt là review trên cát.

---

## Bước 3 – Tiêu chí chung (mọi loại)

| # | Tiêu chí |
|---|---|
| 1 | Tách rõ `Fact` / `Assumption` / `Open Question` / `Recommendation` |
| 2 | Không có nội dung bịa — mọi khẳng định truy được về nguồn |
| 3 | Ghi rõ nguồn input đã dùng |
| 4 | Version và ngày đúng quy ước, không ghi đè bản cũ |
| 5 | **Không còn nội dung mẫu của template** — mục không dùng phải xoá hẳn |
| 6 | Open question có owner và cờ blocking |
| 7 | Không tự chốt quyết định thay người dùng |

---

## Bước 4 – Tiêu chí riêng theo loại

### 4.1 BRD

- [ ] **[BLOCK]** Không chứa chi tiết màn hình, field, validate, cơ chế hệ thống — những thứ đó thuộc PRD
- [ ] **[BLOCK]** Thông tin chưa rõ → Open Question, **không** viết placeholder vào nội dung
- [ ] `Problem` viết theo góc nhìn người dùng, không mô tả giải pháp
- [ ] `Analytics` có dữ liệu, hoặc ghi rõ `Chưa có dữ liệu định lượng` + căn cứ định tính
- [ ] `Objective` là kết quả, không phải danh sách việc làm
- [ ] Scope tách đủ In / Out / Potential
- [ ] Giải pháp stakeholder đề xuất được đặt dưới nhãn `Recommendation`, không thành yêu cầu đã chốt
- [ ] Danh sách US: mỗi US là **một mục tiêu hoàn chỉnh của người dùng**, không chia theo màn hình

### 4.2 Impact Matrix

- [ ] **[BLOCK]** Đủ 4 STEP theo thứ tự
- [ ] **[BLOCK]** Quét đủ 12 vùng, vùng không ảnh hưởng ghi rõ lý do
- [ ] Conflict được **escalate**, không tự resolve
- [ ] Bidirectional có **cả chiều Old→New** — chiều này hay bị bỏ
- [ ] Coverage check đủ 4 loại: boundary · exception · shared entity · side effect
- [ ] Transition Requirements đủ Data / Compatibility / Cutover
- [ ] **Tính năng `hidden` được xét** — không bỏ qua vì "đang ẩn"
- [ ] **Vùng KB chưa phủ** được đánh `❓BA`, không kết luận "không ảnh hưởng"
- [ ] Có mục kiểm tra **chiều tenant**
- [ ] **Phụ lục nguồn đã đọc** — KB nào, bảng nào, endpoint nào

### 4.3 Solution Comparison

- [ ] Các option so **cùng bộ tiêu chí**
- [ ] Khác biệt giữa các option là thật, không phải cùng một phương án viết hai cách
- [ ] Effort / Risk ghi tương đối kèm lý do, **không bịa số giờ**
- [ ] `Recommendation` có **điều kiện** và **risk phải chấp nhận**
- [ ] Ghi rõ **cái gì sẽ đổi kết luận**
- [ ] Không ghi là quyết định cuối

### 4.4 PRD

**Cấu trúc**
- [ ] **[BLOCK]** Có đủ mục bắt buộc theo template: metadata · Document version · Problem · Objective · Solution · Specific Requirement
- [ ] **[BLOCK]** `Metrics success` — hoặc là chỉ số thật của tính năng này, hoặc **đã xoá hẳn**. Còn bảng ví dụ của template (NPS, App Store, Transaction Input Time) là **lỗi nặng**
- [ ] `Preferences` có đủ link Dev/QA cần: Figma · tài liệu liên quan · API tham chiếu · tài khoản staging
- [ ] `Conner case` để trống — **đúng**, đây là việc QA

**Specific Requirement**
- [ ] US đánh số liên tục `US1`, `US2`… US chưa làm ghi rõ trong tiêu đề
- [ ] Mỗi US đủ: User story · Pre-Condition · Scenario · Acceptance criteria · Out of scope
- [ ] Business rule gắn mã `BR-<số US>.<số thứ tự>`, không trùng
- [ ] Rule chạm tính năng có sẵn → **dẫn mã rule trong KB** (`BR-EDIT-07`, `KB-CLASS-03`)
- [ ] Bảng UI ghi đủ: định dạng · placeholder · options · mặc định · disable · tooltip · validate · hành vi
- [ ] **Field hiện có được nhận diện là hiện có**, không viết lại thành mới
- [ ] `Out of scope` có nội dung thật, không bỏ trống

**Kỹ thuật**
- [ ] Bảng mới trong `Database` khai báo rõ có `tenant_id` hay không
- [ ] Endpoint mới đã **đối chiếu Swagger**, không trùng endpoint đã có
- [ ] Mọi **hằng số cứng** ghi rõ: hardcode hay cấu hình được
- [ ] Mail event bị chạm đã đối chiếu KB `13-mail-events.md`

### 4.5 User Guide

- [ ] Viết cho người dùng cuối, không dùng thuật ngữ nội bộ
- [ ] Có đủ mục: phạm vi & module liên quan · điều kiện tiên quyết · hướng dẫn chi tiết · lưu ý & quy tắc nghiệp vụ · lỗi thường gặp
- [ ] **Khai báo `Module chính` / `Module liên quan`** — 13 page UG hiện tại thiếu mục này
- [ ] Ảnh màn hình khớp với tính năng đã dev, không phải ảnh placeholder
- [ ] Business rule trong guide khớp với PRD

---

## Bước 5 – Chế độ Shadow: tài liệu người khác viết

Khi review tài liệu **không do workflow này sinh ra** (PRD của PO khác, tài liệu kế thừa):

1. **Đọc và tóm tắt trước** — trình bày hiểu biết của mình về tài liệu để người dùng xác nhận không hiểu sai
2. **Chạy Impact Analysis ngầm** — quét KB/DB/API xem tài liệu có bỏ sót vùng nào
3. **Phụ lục A — nguồn đã đọc:** liệt kê KB, bảng, endpoint đã tra
4. **Phụ lục B — câu hỏi AI tự trả lời được:** những chỗ tài liệu không nói nhưng AI suy được từ KB, ghi rõ nguồn để người dùng kiểm
5. Findings chia ba nhóm: **sai** · **thiếu** · **mơ hồ**

> Mục đích của chế độ này: tìm chỗ tài liệu **sai so với hệ thống thật**, không phải chấm điểm cách viết.

---

## Output

```markdown
# Review: <Tên tài liệu> <version> — Loại: <BRD / Impact / Solution / PRD / User Guide>

## Input Readiness
<Đủ nền chưa. Thiếu gì.>

## Tóm tắt tài liệu
<Bắt buộc với chế độ Shadow. Để người dùng xác nhận AI hiểu đúng.>

## Findings

| # | Mức | Vị trí | Vấn đề | Đề xuất sửa |
|---|---|---|---|---|
| 1 | `BLOCK` / `Cao` / `Trung bình` / `Thấp` | US2 → BR-2.3 | | |

## Open Questions còn lại

## Phụ lục A – Nguồn AI đã đọc
<Bắt buộc với chế độ Shadow>

## Phụ lục B – Câu hỏi AI tự trả lời được
<Bắt buộc với chế độ Shadow>

## Decision
`Approved` / `Approved with Notes` / `Need Revision`
```

Findings phải trỏ **vị trí cụ thể** (`US2 → BR-2.3`, `bảng UI → field Trạng thái`) để sửa nhắm đích.

Tự kiểm theo `.claude/checklist/review-output.md` trước khi trả kết quả.
