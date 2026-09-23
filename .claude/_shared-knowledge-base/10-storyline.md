# 10 — Storyline

| | |
|---|---|
| Hệ | UpLMS Ops (dựng) · UpLMS (học viên học) |
| Đường dẫn | Academic Management → Course & Materials → Storyline |
| Trạng thái | 🔴 **hidden** — tính năng đã có nhưng đang ẩn |
| Vai trò | SX |
| Nguồn UG | `uplms-ops/academic-management/storyline.md` (367 dòng) |

---

## 1. Phạm vi

| | |
|---|---|
| Module chính | Academic Management / Course & Materials |
| Chức năng chính | Storyline |
| Module liên quan | Course, Question Bank / Question List, Resources, UpLMS học viên |

Storyline là dạng nội dung học tương tác, thêm vào Section của khoá học (Section → Action → Add Story Line).

> 🔴 **Page đang `hidden: true`.** Tính năng đã phát triển (UG chi tiết 367 dòng, có validate cụ thể) nhưng chưa bật hoặc chưa tối ưu cho sản phẩm hiện tại. Vẫn phải xét khi phân tích impact vào Course Content hoặc Question Bank.

---

## 2. Cấu trúc

```
Storyline
└── Storyline Item (có Order)
    └── Document: Text | Question | Video | Interaction
```

---

## 3. Field

### 3.1 Storyline Info

| Field | Bắt buộc | Ghi chú |
|---|---|---|
| Story Line Name | **Có** | |
| Duration – Hour | Không | Thời gian dự kiến, **hiển thị trên màn UpLMS học viên** |
| Duration – Minutes | Không | |
| Description | **Có** | |

### 3.2 Storyline Item

| Cột | Ghi chú |
|---|---|
| Order | Thứ tự hiển thị |
| Storyline Item Name | |
| Documents | Số lượng Document trong Item |
| Action | Edit / Delete |

### 3.3 Document — 4 loại

| Loại | Field |
|---|---|
| **Text** | Text Name, Description (nội dung) |
| **Question** | Text Name, Description *(UG ghi giống hệt Text — `❓BA` có phải lỗi tài liệu?)* |
| **Video** | Video Name, Upload (từ thiết bị hoặc kho hệ thống) |
| **Interaction** | Xem §3.4 |

> **Tên Document chỉ hiển thị trên UpLMS Ops, KHÔNG hiển thị trên giao diện học của học viên.** Lặp lại ở cả 4 loại.

### 3.4 Interaction — Labeled Graphic

| Field | Bắt buộc | Ràng buộc |
|---|---|---|
| Document Name | **Có** | |
| Interaction Type | **Có** | **Giai đoạn này mặc định `Labeled Graphic`** — hàm ý sẽ có loại khác |
| Background Image | **Có** | JPG, JPEG, PNG, GIF, WEBP |
| Marker List | **Có** | **Tối thiểu 1, tối đa 10 marker** |

**Mỗi Marker:**

| Field | Bắt buộc | Ghi chú |
|---|---|---|
| Marker Title | **Có** | Tiêu đề popup khi học viên click |
| Marker Content | **Có** | Nội dung popup, hỗ trợ text + ảnh, scroll được |
| Marker Style | Không | Icon marker (`+`, `?`, …). Mặc định `+` |

**Tạo marker:** upload ảnh nền → click vị trí bất kỳ trên ảnh → form nhập thông tin ở panel trái.
**Thao tác:** kéo thả để di chuyển (cập nhật ngay) · Edit qua icon bút chì hoặc click marker · Delete có xác nhận, **sau khi xoá số thứ tự marker còn lại được đánh lại liên tiếp**.

**Validate khi Save Document:** Document Name không trống · Background Image phải upload trước · ít nhất 1 Marker · mỗi Marker đủ Title và Content. Vi phạm → **báo lỗi ngay dưới field, không cho Save**.

---

## 4. Business Rule

| ID | Rule | Nguồn |
|---|---|---|
| KB-SL-01 | **Chỉ xoá/chỉnh sửa được khi Storyline chưa được học.** Đã có người học → hệ thống **chặn Update**. | storyline mục II |
| KB-SL-02 | Xoá Storyline Item sẽ **xoá tất cả Document** trong Item đó. | storyline mục II |
| KB-SL-03 | Tên Document **chỉ hiển thị trên UpLMS Ops**, không hiển thị cho học viên. | storyline mục II (×4 loại) |
| KB-SL-04 | Interaction: Marker **tối thiểu 1, tối đa 10**. | storyline mục II |
| KB-SL-05 | Xoá Marker → **số thứ tự các marker còn lại được đánh lại liên tiếp**. | storyline mục II |
| KB-SL-06 | `Interaction Type` **giai đoạn này mặc định là `Labeled Graphic`** — chỉ có một loại. | storyline mục II |
| KB-SL-07 | Danh sách Storyline mặc định sắp xếp **thời gian tạo giảm dần**. | storyline mục II |

---

## 5. Phân quyền — chi tiết hơn các module khác

UG module này khai báo quyền theo từng thao tác, rõ hơn hẳn phần còn lại:

| Thao tác | Quyền cần |
|---|---|
| Xem danh sách | Quyền xem danh sách Storyline |
| Tạo mới | Quyền tạo Storyline |
| Chỉnh sửa / xoá | Quyền chỉnh sửa Storyline |
| **Gán Storyline vào Course** | **Quyền tạo hoặc chỉnh sửa Course** (không phải quyền Storyline) |

> Đây là mẫu khai báo quyền tốt nhất trong toàn bộ UG — nên dùng làm chuẩn cho các module khác khi bổ sung permission matrix.

---

## 6. Phụ thuộc

| Module | Quan hệ |
|---|---|
| **Course** | Storyline thêm vào Section; gán cần quyền Course |
| **Question Bank** | Document loại Question lấy từ Question List |
| **Resources** | Video upload từ kho tài nguyên hệ thống |
| **UpLMS (học viên)** | Giao diện học Storyline; Duration hiển thị cho học viên |

---

## 7. Điểm cần BA xác nhận

| # | Câu hỏi |
|---|---|
| Q1 | **Storyline đang ẩn — có kế hoạch bật lại không? Đã có khoá học nào dùng Storyline chưa?** |
| Q2 | Document loại **Question** trong UG mô tả field giống hệt Text (Text Name + Description) — có phải lỗi tài liệu? Thực tế Question lấy từ Question Bank thế nào? |
| Q3 | `Interaction Type` "giai đoạn này mặc định Labeled Graphic" — có roadmap thêm loại khác không? |
| Q4 | Storyline có tính vào tiến độ / điểm hoàn thành khoá học không? |
| Q5 | KB-SL-01 chặn mọi update khi đã có người học — chặt hơn Course (BR-EDIT-03 vẫn cho sửa một phần). Đúng là chủ ý? |
