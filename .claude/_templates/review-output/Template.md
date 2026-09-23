# Review: <Tên tài liệu> <version>

| | |
| --- | --- |
| **Loại** | BRD / Impact Matrix / Solution Comparison / PRD / User Guide |
| **Chế độ** | Thường / **Shadow** *(tài liệu người khác viết)* |
| **Người review** | |
| **Ngày** | |

---

## 1. Input Readiness

*Tài liệu có đủ nền để tồn tại không.*

| Yêu cầu nền | Có? | Ghi chú |
| --- | --- | --- |
| | ✅ / ❌ | |

**Thiếu nền → dừng, không review tiếp.** Review một PRD viết trên Impact Matrix chưa duyệt là review trên cát.

---

## 2. Tóm tắt tài liệu

*Bắt buộc với chế độ **Shadow**. Trình bày hiểu biết của AI về tài liệu để người dùng xác nhận không hiểu sai trước khi đọc findings.*

---

## 3. Findings

| # | Mức | Vị trí | Vấn đề | Đề xuất sửa |
| --- | --- | --- | --- | --- |
| 1 | `BLOCK` | `US2 → BR-2.3` | | |
| 2 | `Cao` | `bảng UI → field Trạng thái` | | |
| 3 | `Trung bình` | | | |
| 4 | `Thấp` | | | |

### Mức độ

| Mức | Nghĩa |
| --- | --- |
| **`BLOCK`** | Không duyệt được cho đến khi sửa. Sai về nội dung, hoặc vi phạm ranh giới tài liệu |
| **Cao** | Gây hiểu sai hoặc làm sai khi triển khai |
| **Trung bình** | Thiếu thông tin, người đọc phải đi hỏi thêm |
| **Thấp** | Trình bày, nhất quán, cách diễn đạt |

> Findings phải trỏ **vị trí cụ thể** — `US2 → BR-2.3`, không phải "phần business rule". Để sửa nhắm đích.

### Phân nhóm *(chế độ Shadow)*

| Nhóm | Số lượng |
| --- | --- |
| **Sai** — khác với hệ thống thật | |
| **Thiếu** — chưa đề cập | |
| **Mơ hồ** — hiểu được nhiều cách | |

---

## 4. Open Questions còn lại

| # | Câu hỏi | Người trả lời | Chặn việc gì |
| --- | --- | --- | --- |

---

## 5. Phụ lục A — Nguồn AI đã đọc

*Bắt buộc với chế độ **Shadow**. Để người dùng biết review dựa trên gì và **thiếu gì**.*

| Nguồn | Cụ thể |
| --- | --- |
| KB | |
| DB | |
| Swagger | |
| Mail event | |
| **Chưa tra được** | *vùng nào không có nguồn để tra* |

---

## 6. Phụ lục B — Câu hỏi AI tự trả lời được

*Bắt buộc với chế độ **Shadow**. Những chỗ tài liệu không nói nhưng AI suy được từ KB — ghi rõ nguồn để người dùng kiểm lại.*

| # | Chỗ tài liệu bỏ ngỏ | AI suy ra | Nguồn | Độ chắc |
| --- | --- | --- | --- | --- |
| | | | | Chắc / Suy đoán |

---

## 7. Decision

> `Approved` / `Approved with Notes` / `Need Revision`

**Lý do:**

**Nếu `Need Revision`** — danh sách mã cần sửa, theo thứ tự ưu tiên:

1. `US2 → BR-2.3`
2. …
