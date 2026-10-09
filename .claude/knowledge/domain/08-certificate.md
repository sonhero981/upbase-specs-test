# 08 — Certificate (Chứng chỉ)

| | |
|---|---|
| Hệ | UpLMS Ops (tạo & gán) · UpLMS (học viên nhận) |
| Đường dẫn | Academic Management → Course & Materials → Certificates · LMS → Certificate |
| Trạng thái | Active |
| Nguồn UG | `academic-management/certificate-management.md`, `gan-chung-chi-cho-khoa-hoc-certificate.md`, `uplms/danh-sach-chung-chi.md` |

---

## 1. Hai bước tách rời

```
Bước A — Certificate Management        Bước B — Gán vào khoá học
(tạo Certificate Template)      →      (Course → bước 4 → Choose Template)
```

Người tạo khoá học **không tạo template**, chỉ **chọn từ kho template đã có**.

---

## 2. Ràng buộc then chốt

| Ràng buộc | Chi tiết |
|---|---|
| **Lọc theo Category** | Khi chọn template cho khoá, hệ thống **chỉ hiển thị chứng chỉ cùng Category với khoá học** |
| **Bắt buộc để Publish** | Khoá chỉ Publish được khi **đã tạo nội dung VÀ đã gán chứng chỉ** (BR-CONTENT-09) |
| **Điều kiện nhận** | Học viên nhận chứng chỉ sau khi **hoàn thành khoá học** — tức đạt **Pass Point** (BR-COURSE-INFO-06) |
| Thứ tự | Certificate là **bước cuối cùng** trong quy trình tạo khoá học |

> ⚠️ **Category là khoá liên kết ẩn.** Đổi Category của khoá học có thể làm template đang gán trở nên không hợp lệ. Danh sách template trống thường là do chưa có template cùng Category, chứ không phải chưa có template nào.

---

## 3. Phía học viên

`LMS → Certificate` — danh sách chứng chỉ đã đạt.

| Thao tác | Ghi chú |
|---|---|
| Xem chi tiết | Click tên chứng chỉ hoặc icon xem |
| **Share with LinkedIn** | Chia sẻ lên mạng xã hội |
| Copy link | Sao chép đường link chứng chỉ |
| Download | Tải về — **định dạng ảnh** |

---

## 4. Business Rule

| ID | Rule | Nguồn |
|---|---|---|
| KB-CERT-01 | Hệ thống **chỉ hiển thị chứng chỉ cùng Category** với Category của khoá học. | gan-chung-chi mục II |
| KB-CERT-02 | Certificate là **bước cuối** trong quy trình tạo khoá học. | gan-chung-chi mục III |
| KB-CERT-03 | Khoá chỉ Publish được khi đã tạo nội dung **và** gán chứng chỉ. | BR-CONTENT-09 |
| KB-CERT-04 | Học viên nhận chứng chỉ **sau khi hoàn thành khoá học**. | gan-chung-chi mục II |
| KB-CERT-05 | ⚠️ **Thay đổi chứng chỉ của khoá học có thể ảnh hưởng đến chứng chỉ học viên đã nhận.** | gan-chung-chi mục III |
| KB-CERT-06 | Chứng chỉ tải về dưới **định dạng ảnh**. | danh-sach-chung-chi mục III |
| KB-CERT-07 | Chứng chỉ có **đường link chia sẻ được** (copy link, share LinkedIn). | danh-sach-chung-chi mục II |

> **KB-CERT-05 là rule rủi ro nhất module này** — UG chỉ nói "có thể ảnh hưởng", không nói ảnh hưởng thế nào. Đây là lỗ hổng cần làm rõ trước khi có dự án nào chạm vào chứng chỉ.

---

## 5. Phụ thuộc

| Module | Quan hệ |
|---|---|
| **Course** | Bắt buộc gán trước khi Publish; là bước 4 của luồng tạo khoá |
| **Course Category** ⚠️ | **Lọc danh sách template** — quan hệ ẩn, dễ sót |
| **Resource** | UG khai báo Certificate liên quan Resources |
| **Pass Point** | Điều kiện cấp chứng chỉ |
| **UpLMS (học viên)** | Màn danh sách chứng chỉ, chia sẻ, tải |
| **Mạng ngoài (LinkedIn)** | Chia sẻ chứng chỉ — link công khai |

---

## 6. Điểm cần BA xác nhận

| # | Câu hỏi |
|---|---|
| Q1 | **KB-CERT-05: đổi template của khoá thì chứng chỉ học viên đã nhận bị ảnh hưởng ra sao?** Cấp lại, giữ nguyên bản cũ, hay link cũ hỏng? |
| Q2 | Link chứng chỉ chia sẻ được — là link công khai không cần đăng nhập? Có hết hạn không? |
| Q3 | Certificate Template gồm những field nào (tên học viên, ngày cấp, mã chứng chỉ, chữ ký...)? UG không mô tả. |
| Q4 | Một khoá gán được nhiều chứng chỉ hay chỉ một? |
| Q5 | Khoá học không cấp chứng chỉ thì Publish kiểu gì, khi BR-CONTENT-09 bắt buộc phải gán? |
| Q6 | Chứng chỉ có mã định danh / cơ chế xác thực (verify) không? |
| Q7 | Đổi Category của khoá đã Publish → template đang gán xử lý thế nào? |
