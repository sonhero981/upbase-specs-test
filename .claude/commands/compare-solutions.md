# Compare Solutions – So sánh phương án và đề xuất

Dùng khi có nhiều hướng giải quyết, hoặc cần một bản đánh giá trước khi chốt hướng làm PRD.

**Tương đương Bước 7–8 + Gate 3 trong `/po-workflow`.**

---

## Đầu vào

`$ARGUMENTS` — tên project.

> **Xác định project:** ưu tiên `$ARGUMENTS`; không có → suy từ file đang mở; >1 khả dĩ → liệt kê cho chọn. **Echo + confirm trước khi chạy.**

Đọc theo thứ tự:

1. `docs/brd/brd-v*.md` — đã qua Gate 1
2. `working/impact-analysis/impact-matrix-v*.md` — đã qua Gate 2
3. `project-decisions.md` — quyết định đã chốt trước đó
4. `.claude/_shared-knowledge-base/` — cách hệ thống đang làm việc tương tự
5. `.claude/_templates/solution-comparison/Template.md`

**Chưa có Impact Matrix được duyệt → dừng.** So sánh phương án mà không biết ảnh hưởng thì so sánh trên giả định.

---

## Bước 7 – Xác định tình huống

**Hỏi trước:** *"Anh/chị đã có định hướng giải pháp cho yêu cầu này chưa? Nếu có, mô tả ngắn định hướng đó."*

### TH1 — Đã có định hướng

1. Nhận xét **alignment với Objective trong BRD** — định hướng này giải quyết đúng vấn đề không
2. Chỉ ra **điểm mạnh** và **gap** cụ thể, đối chiếu Impact Matrix
3. Gợi ý thêm **1–2 option thay thế** nếu thấy có hướng đáng cân nhắc
4. Sang Bước 8 với tất cả options

> Định hướng người dùng đưa ra **không mặc nhiên là phương án được chọn**. Vẫn phải đưa vào bảng so sánh như các option khác — để quyết định dựa trên đánh đổi, không dựa trên thứ tự đề xuất.

### TH2 — Chưa có định hướng

1. Gợi ý **2–3 option** dựa trên BRD, Impact Matrix, và cách hệ thống đang giải quyết bài toán tương tự (tra KB)
2. Lưu vào `working/raw-inputs/solution-options-draft-YYYYMMDD.md`
3. Sang Bước 8 — **không chờ confirm từng option**, Gate 3 là điểm review

**Trả lời không rõ có/chưa → hỏi lại, không tự suy đoán.**

---

## Bước 8 – So sánh

### Tiêu chí

| Tiêu chí | Đánh giá gì |
|---|---|
| **Business fit** | Giải quyết đúng vấn đề trong BRD không |
| **Tác động người dùng & quy trình** | Người dùng phải đổi thói quen bao nhiêu |
| **Tác động hệ thống / data / API** | Lấy từ Impact Matrix — vùng nào bị chạm, severity |
| **Effort** | Ước lượng tương đối giữa các option, không phải số tuyệt đối |
| **Risk** | Rủi ro kỹ thuật và nghiệp vụ |
| **Dependency** | Phụ thuộc vào đội khác, hệ ngoài, tính năng chưa có |
| **Nợ đóng cứng tenant** | Option này có nhúng thêm logic riêng UpBase không — đối chiếu KB `15` §6 |
| Pros / Cons | Tóm gọn |

### Cách viết

- Mỗi option một cột hoặc một khối, so **cùng bộ tiêu chí**
- Khác biệt thật phải nổi lên — nếu hai option giống nhau ở mọi tiêu chí thì chúng không phải hai option khác nhau
- **Effort và Risk ghi tương đối** (Cao / Trung bình / Thấp) kèm lý do, không bịa số giờ

### Recommendation

Ghi rõ:

1. **Option đề xuất**
2. **Điều kiện** — đề xuất này đúng khi nào (*"nếu chấp nhận không hỗ trợ dữ liệu cũ trước tháng 6"*)
3. **Risk phải chấp nhận** nếu chọn option này
4. **Cái gì sẽ đổi kết luận** — dữ kiện nào nếu khác đi thì đề xuất đổi

> **Ghi là `Recommendation`, không ghi là quyết định.** Việc chốt thuộc Gate 3 và thuộc người dùng.

---

## Output

`working/solution-options/solution-comparison-v0.1-YYYYMMDD.md`

Tự kiểm theo `.claude/checklist/compare-solutions.md` trước khi trình bày.

---

## Trình bày tại Gate 3

- (Nếu người dùng đã có định hướng) nhận xét ngắn về định hướng đó
- Danh sách options và **nguồn gốc** (người dùng đề xuất / AI gợi ý / cách hệ thống đang làm)
- Bảng so sánh tóm tắt
- **Recommendation** kèm điều kiện và risk phải chấp nhận
- Open question cần trả lời trước khi approve

Ba lựa chọn: `Approved` / `Approved with Notes` / `Need Revision` (quay lại Bước 7).

Duyệt xong → **ghi vào `project-decisions.md`**: option được chọn · lý do · trade-off chấp nhận · ngày · Gate 3.
