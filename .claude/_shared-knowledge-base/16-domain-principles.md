# 16 — Nguyên tắc mô hình hoá

**Đối chiếu lần cuối:** 05/10/2026
**Nguồn:** PO nêu trong lúc làm dự án Group
**Loại:** 📌 Bản chốt — không có tài liệu gốc, nghi ngờ thì hỏi PO

Bộ nguyên tắc quyết định **cái gì được chứa cái gì** trong UpLnD. Chúng chi phối mọi tính năng mới, nên trước khi thiết kế một thực thể mới phải đối chiếu ở đây.

> ⚠️ **File này chưa đầy đủ.** PO dẫn *"nguyên tắc 6"* nhưng chưa có tài liệu gốc liệt kê đủ bộ. Các nguyên tắc khác ghi `❓BA` cho tới khi tra được.

---

## Bảng nguyên tắc

| # | Nội dung | Nguồn |
|---|---|---|
| 1–5 | `❓BA` — chưa tra được | — |
| **6** | **Quan hệ nội dung với nội dung chỉ sống trong Lộ trình.**<br>**Quan hệ người với nội dung chỉ sống trong Lớp và Automation.** | PO, 05/10/2026, dự án Group |
| 7+ | `❓BA` — chưa biết bộ này có bao nhiêu nguyên tắc | — |

---

## Nguyên tắc 6 — chi tiết

Nguyên tắc này trả lời câu hỏi *"thực thể X có được chứa thực thể Y không"*.

| Loại quan hệ | Chỉ được sống ở |
|---|---|
| Nội dung ↔ nội dung | **Lộ trình** |
| Người ↔ nội dung | **Lớp** và **Automation** |

Hệ quả cho các thực thể khác:

| Thực thể | Được chứa gì | Không được chứa gì |
|---|---|---|
| **Nhóm** | Người | **Bất cứ thứ gì khác.** Không chứa khoá học, không chứa lộ trình |
| **Lớp** | Người ↔ một đối tượng nội dung | Nhiều đối tượng nội dung cùng lúc |
| **Lộ trình** | Nội dung ↔ nội dung | |

### Hai cách dùng sai mà nguyên tắc 6 chặn

| Cách dùng sai | Vỡ ở đâu |
|---|---|
| **Dùng Lớp làm Nhóm** — tạo *"lớp phòng Marketing"* rồi nhét mọi khoá vào | Lớp gắn đúng một nội dung và có thời hạn, phòng ban thì không. Đổi cơ cấu là phải sửa hàng chục lớp |
| **Nhét nội dung vào Nhóm** — để nhóm *"chứa"* khoá học | Quan hệ người với nội dung không được sống trong Nhóm. Nhóm chỉ là địa chỉ để gán, không phải nơi giữ nghĩa vụ học |

---

## Nhóm, Lớp, Lộ trình — ranh giới

Bảng do PO cung cấp ngày 05/10/2026, dự án Group. Khác nhau ở **đối tượng gắn vào**: Nhóm gắn **người**, Lớp gắn **nội dung**.

| | Nhóm | Lớp |
|---|---|---|
| Trả lời câu hỏi | **Ai** thuộc về đâu | Ai học **cái gì**, trong **khoảng nào** |
| Gắn với | Người. Không có nội dung | Đúng một đối tượng nội dung: một khoá hoặc một lộ trình |
| Thời gian | Không có | Có. Thời hạn, ngày kích hoạt riêng từng người |
| Sinh ra gì | **Không sinh nghĩa vụ học.** Chỉ là địa chỉ để gán | **Sinh nghĩa vụ học.** Vào lớp là có việc phải làm |
| Tiến độ học nằm ở đâu | Không có | Treo vào lượt ghi danh của lớp, không treo vào người |
| Quan hệ với người | Nhiều-nhiều, lồng nhau | Một người vào một lớp là một lượt ghi danh |
| Nguồn gốc | Có thể đến từ HRM, chỉ đọc | Luôn do L&D tạo |
| Vòng đời | Lâu dài, theo cơ cấu tổ chức | Theo khoá, mở rồi đóng |
| Dùng cho | Giao hàng loạt, cộng dồn báo cáo, suy ra quản lý, phạm vi dữ liệu | Theo dõi tiến độ, chốt kết quả, cấp chứng chỉ |

**Dòng chảy:**

```
Nhóm  ──gán nội dung──►  Lớp  ──ghi danh──►  Người học có nghĩa vụ
 (ai)                     (ai + học gì + khi nào)
```

Gán nội dung cho nhóm là một **luật đứng**, không phải sao chép thành viên một lần: ai thuộc nhóm này thì vào lớp này, kể cả người gia nhập sau. Sao chép một lần thì không khác gì nhập file.

---

## Vùng KB còn trống liên quan

| Khái niệm | Trạng thái |
|---|---|
| **Lộ trình** | ❓ Chưa có file KB nào. Nguyên tắc 6 dựa vào nó |
| **Automation** | ❓ Chưa có file KB nào. Nguyên tắc 6 dựa vào nó |
| Nguyên tắc 1–5 và 7+ | ❓ Chưa tra được tài liệu gốc |
