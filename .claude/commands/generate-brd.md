# Generate BRD – Chốt hướng trước khi viết PRD

Dùng khi yêu cầu đã được làm rõ và scope đủ chắc để trình duyệt.

**Tương đương Bước 4 + Gate 1 trong `/po-workflow`.**

BRD là **bản nháp nội bộ để chốt hướng**, không phải tài liệu bàn giao. Nội dung sẽ được viết lại nguyên vào PRD sau khi duyệt — nên viết đúng ngay, đừng viết tắt.

---

## Đầu vào

`$ARGUMENTS` — tên project hoặc input cụ thể.

> **Xác định project:** ưu tiên `$ARGUMENTS`; không có → suy từ file đang mở; >1 khả dĩ → liệt kê cho chọn. **Echo + confirm trước khi chạy.**

Đọc theo thứ tự:

1. `working/ai-drafts/clarified-requirements-*.md` — bản mới nhất
2. `working/open-questions/open-questions-*.md` — kiểm xem còn blocking question không
3. `project-context.md` · `project-decisions.md`
4. `working/raw-inputs/`
5. `.claude/_shared-knowledge-base/` — tra tính năng liên quan
6. `.claude/_templates/brd/Template.md` — cấu trúc bắt buộc

**Còn blocking question chưa trả lời → dừng, quay lại `/clarify-requirements`.** Không viết BRD trên nền chưa rõ.

---

## Ranh giới nội dung — quan trọng

| BRD **CÓ** | BRD **KHÔNG** |
|---|---|
| Vấn đề người dùng đang gặp | Chi tiết màn hình, layout |
| Dữ liệu chứng minh vấn đề | Danh sách field, validate |
| Mục tiêu muốn đạt | Expected behavior từng thao tác |
| Phạm vi In / Out / Potential | Cơ chế hệ thống, state machine |
| Business rule **mức nghiệp vụ** | API flow, cấu trúc bảng |
| Hướng giải quyết ở mức khung | Giải pháp kỹ thuật chi tiết |
| Danh sách US dự kiến | Nội dung chi tiết từng US |

> Nguyên tắc: BRD nêu **cái gì phải đúng**, không nêu **làm thế nào**. Những thứ "làm thế nào" thuộc PRD `Specific Requirement`.
>
> Thông tin chưa rõ → **Open Question**, không viết vào BRD dù là placeholder.

---

## Cách viết từng mục

### 1. Problem

Ai gặp · gặp khi nào · hậu quả gì. Viết theo góc nhìn người dùng.

Không mô tả giải pháp ở mục này — kể cả khi người dùng đã nói sẵn giải pháp trong input. Giải pháp người dùng đưa ra là `Recommendation`, không phải `Problem`.

### 2. Analytics

**Mô tả người dùng đang xoay xở thế nào với vấn đề hiện nay.** Đủ chi tiết để người đọc hiểu ngay vì sao cần thay đổi.

Hỏi người dùng theo bốn hướng này:

| Hướng | Câu hỏi |
|---|---|
| **Cách làm hiện tại** | Không có tính năng này thì họ làm gì thay thế? Theo thứ tự nào? |
| **Tiêu chí quyết định** | Họ dựa vào gì để quyết? Con số nào, quy tắc nào trong đầu? |
| **Chi phí** | Mất bao lâu? Bao nhiêu lần một ngày/tuần? Ai làm? |
| **Chỗ sai** | Hay sai ở đâu? Hậu quả khi sai? |

Có số liệu (hệ thống, ticket, thống kê) → thêm vào, càng tốt. **Không có số vẫn viết được** — mô tả hiện trạng đủ rõ là đạt.

> Ví dụ từ PRD thật — không một con số nào mà vẫn thuyết phục:
> *"Ngày D-1 thường tăng bid hàng loạt cho từ khóa để tăng cạnh tranh cho ngày camp. ROAS chiến dịch thấp → check từ khóa tiêu nhiều nhưng doanh số thấp → giảm bid 20-30%, xem có giữ được thứ hạng không."*

**Không bỏ trống.** 2/4 PRD đang lưu hành để trống mục này — và đó chính là những PRD khó đánh giá có đáng làm hay không.

### 3. Objective

Kết quả muốn đạt, không phải danh sách việc làm.

*Sai: "Xây màn cấu hình mapping kho". Đúng: "Đơn hàng được phân bổ tự động về kho phù hợp, giảm thao tác thủ công của vận hành".*

### 4. Stakeholder

Bảng `Stakeholder │ Action` — ai liên quan và họ làm gì với tính năng này.

### 5. Scope

- **In scope** — làm gì
- **Out of scope** — **không** làm gì, dù người đọc có thể tưởng là có
- **Potential scope** — có thể làm đợt sau, ghi để không mất nhưng không cam kết

Mục `Out of scope` quan trọng ngang `In scope`. Đây là chỗ chặn tranh chấp phạm vi về sau.

### 6. Solution (khung)

Hướng giải quyết ở mức tổng thể. Chưa cần màn hình hay field.

Có nhiều hướng → nêu từng hướng kèm đánh đổi, ghi hướng đề xuất dưới nhãn `Recommendation`. **Không tự chốt thay người quyết** — việc chốt thuộc Gate 3.

### 7. Danh sách User Story dự kiến

| ID | User Story | Nguồn | Ghi chú |
|---|---|---|---|
| US1 | *Là <vai trò>, tôi cần <mục tiêu> để <giá trị>* | Yêu cầu nào sinh ra US này | |

Đây là xương sống của `Specific Requirement` trong PRD. Đánh số `US1`, `US2`… liên tục.

**Nguyên tắc chia US:** một US = **một mục tiêu hoàn chỉnh của người dùng**, không chia theo màn hình, không chia theo business rule. Một US thường bị chi phối bởi nhiều rule, và một rule có thể áp cho nhiều US.

> **Define hết US, kể cả cái chưa làm ngay.** Không tự giới hạn theo sức của một đợt — việc chọn làm cái nào, khi nào, thuộc về PO và làm ở bước sau.
>
> US chưa làm trong đợt này → vẫn viết đủ, ghi rõ trong tiêu đề: `US5: Sao chép cấu hình — chưa làm`.
>
> Lý do: bức tranh đầy đủ giúp Impact Analysis quét đúng và tránh thiết kế dữ liệu chỉ vừa cho phần làm trước, rồi phải sửa khi làm tiếp.

### 8. Tác động tới hệ thống hiện tại

Chưa chạy Impact Analysis ở thời điểm viết BRD → ghi `Chưa phân tích`, **không đoán**.

Đã có sơ bộ từ KB → ghi vùng ảnh hưởng mức cao, chi tiết để Gate 2.

### 9. Assumptions

Điều đang giả định đúng nhưng chưa xác nhận. Mỗi dòng phải kiểm chứng được.

### 10. Open Questions

| # | Câu hỏi | Vì sao quan trọng | Người trả lời | Chặn bước sau? |
|---|---|---|---|---|

`Chặn bước sau = Yes` khi thiếu câu trả lời thì không viết được PRD chính xác.

### 11. References

Tài liệu nền, KB đã đọc (ghi rõ file nào), PRD liên quan, link Jira.

---

## Output

`docs/brd/brd-v0.1-YYYYMMDD.md`

Còn assumption lớn → đánh dấu trạng thái `Draft - Pending Confirmation`.

Tự review theo `.claude/checklist/generate-brd.md` trước khi trình bày.

---

## Trình bày tại Gate 1

- Problem · Analytics · Objective
- Scope: In / Out / Potential
- Hướng giải quyết + đánh đổi
- **Danh sách US dự kiến**
- Assumption đáng chú ý
- Open question còn lại

Ba lựa chọn:

> **`Approved`** – tiếp tục Giai đoạn 3 (Impact Analysis)
> **`Approved with Notes`** – ghi notes vào `project-decisions.md` rồi tiếp tục
> **`Need Revision`** – quay lại Bước 3 với hướng dẫn cụ thể

**Trả lời không rõ → hỏi lại, không suy đoán là duyệt.**
