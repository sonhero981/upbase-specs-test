# [BRD] <Tên tính năng>

> **Bản nháp nội bộ để chốt hướng trước khi viết PRD.** Không phải tài liệu bàn giao.
>
> Nội dung ở đây sẽ được **viết lại nguyên vào PRD** sau khi được duyệt — nên viết đúng ngay từ đầu, đừng viết tắt.
>
> Phần *in nghiêng* là hướng dẫn, xoá khi viết thật.

| | |
| --- | --- |
| **Tính năng** | |
| **Người viết** | |
| **Ngày** | |
| **Trạng thái** | `Draft` / `Pending Confirmation` / `Approved` |

---

# 1. Problem

*Vấn đề người dùng đang gặp: ai gặp · gặp khi nào · hậu quả gì.*

*Viết theo góc nhìn người dùng. Không mô tả giải pháp ở mục này.*

---

# 2. Analytics

*Dữ liệu chứng minh vấn đề là thật và đáng giải quyết.*

*Chưa có số liệu → ghi `Chưa có dữ liệu định lượng` kèm căn cứ định tính (phản hồi, quan sát, ticket). Không bỏ trống.*

---

# 3. Objective

*Kết quả muốn đạt được, không phải danh sách việc làm.*

---

# 4. Stakeholder

| Stakeholder | Action |
| --- | --- |
| | |

---

# 5. Scope

## In scope

*Những gì tính năng này làm.*

## Out of scope

*Những gì **không** làm, dù người đọc có thể tưởng là có.*

## Potential scope

*Có thể làm ở đợt sau — ghi lại để không mất, nhưng không cam kết.*

---

# 6. Solution (khung)

*Hướng giải quyết ở mức tổng thể. Chưa cần chi tiết màn hình hay field — phần đó thuộc PRD.*

*Có nhiều hướng → nêu từng hướng kèm đánh đổi, và ghi rõ hướng đề xuất dưới nhãn `Recommendation`. Không tự chốt thay người quyết.*

---

# 7. Danh sách User Story dự kiến

*Rút ra từ Scope. Đây là xương sống của phần `Specific Requirement` trong PRD.*

| ID | User Story | Nguồn | Ghi chú |
| --- | --- | --- | --- |
| US1 | *Là <vai trò>, tôi cần <mục tiêu> để <giá trị>* | *Yêu cầu nào sinh ra US này* | |
| US2 | | | |

---

# 8. Tác động tới hệ thống hiện tại

*Tóm tắt từ Impact Analysis. Chi tiết để ở `working/impact-analysis/`.*

| Vùng ảnh hưởng | Mức | Ghi chú |
| --- | --- | --- |

*Chưa chạy Impact Analysis → ghi rõ `Chưa phân tích`, không đoán.*

---

# 9. Assumptions

*Điều đang giả định là đúng nhưng chưa được xác nhận. Mỗi dòng phải kiểm chứng được.*

---

# 10. Open Questions

| # | Câu hỏi | Vì sao quan trọng | Người trả lời | Chặn bước sau? |
| --- | --- | --- | --- | --- |

*`Chặn bước sau = Yes` khi thiếu câu trả lời thì không viết được PRD chính xác.*

---

# 11. References

*Tài liệu nền, KB đã đọc, PRD liên quan, link Jira.*
