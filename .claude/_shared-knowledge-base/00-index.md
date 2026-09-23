# Knowledge Base — Sản phẩm UpBase LMS

KB này là **bản chắt lọc** từ nhiều nguồn, dùng làm đầu vào cho Impact Analysis và FS. Đọc KB để biết *có gì, ràng buộc gì, chạm vào đâu*; mở nguồn gốc khi cần chi tiết.

| | |
|---|---|
| Cập nhật lần cuối | **23/09/2026** |

## Nguồn

| Nguồn | Phạm vi | Loại | Đối chiếu lần cuối |
|---|---|---|---|
| GitBook `uplms` + `uplms-ops` | 57 page User Guide | 🔄 nguồn sống | 22/09/2026 |
| [Lark → Data Architecture](https://upbasevn.sg.larksuite.com/wiki/MaFpweI68iKNMvkTioLlJ1uJgQd) | 85 bảng, 173 quan hệ (chỉ PK/FK) | 🔄 nguồn sống | 23/09/2026 |
| Swagger LMS + Ops (staging) | 555 + 153 operation, 267 DTO | 🔄 nguồn sống | 23/09/2026 |
| BA cung cấp + xác nhận trực tiếp | 30 mail event · SIS · trạng thái mail | 📌 bản chốt | 23/09/2026 |

> **🔄 nguồn sống** = có bản gốc ở ngoài, đọc lại được khi nghi ngờ. **Định kỳ mỗi tháng kiểm một lượt**; quá hạn mà yêu cầu chạm tới vùng đó thì đọc lại trước.
>
> **📌 bản chốt** = không còn file gốc, KB chính là nguồn. Nghi ngờ → **hỏi người dùng**, không tự suy.

---

## Hai hệ thống

| Hệ | URL | Đối tượng |
|---|---|---|
| **UpLMS** | https://uplms.upbase.asia · API `lms-be.staging.upbase.asia` | Học viên |
| **UpLMS Ops** | https://uplms-ops.upbase.asia · API `ops-be.staging.upbase.asia` | Operator, L&D, Mentor, SX |

Quan hệ cốt lõi: **Course chứa nội dung — Class quyết định ai học nội dung đó.** Lớp không tự chứa nội dung; mỗi lớp gắn một Course đã Publish.

---

## ⚠️ Đọc trước khi dùng KB

**KB dựng từ User Guide chỉ bao phủ khoảng một nửa hệ thống.** So với API: Ops có **25 nhóm chức năng** và LMS có **8 nhóm** không hề xuất hiện trong UG — lịch dạy, giáo viên, phòng học, lễ tân, thi cử (Examination/Entrance Test/Event Test), phòng ban, phân quyền, khảo sát.

Ngoài ra, DB cho thấy hệ thống là **multi-tenant** và có hạ tầng **marketplace** — UG không nhắc một chữ.

👉 Khi chạy Impact Analysis, **đọc [14-api-surface.md](14-api-surface.md) trước** để biết KB đang thiếu vùng nào.

---

## Danh mục KB

### Nghiệp vụ (từ User Guide)

| File | Module | Trạng thái |
|---|---|---|
| [01-course.md](01-course.md) | Course, Section, Activity, Learning Outcome, Resource, Category | Active |
| [02-question-bank.md](02-question-bank.md) | Question Bank, Case Study | Active |
| [03-assessment.md](03-assessment.md) | Test, Quiz — cấu hình (Ops) và làm bài (Student) | Một phần ẩn |
| [04-class.md](04-class.md) | Class, học viên trong lớp, mentor, tài liệu lớp | Active |
| [05-grading.md](05-grading.md) | Chấm điểm thủ công, phân công, regrading | Active — ⚠️ **mail đang tắt** |
| [06-user-account.md](06-user-account.md) | Student, Staff, Profile, SSO Lark, Security | Active |
| [07-learning-experience.md](07-learning-experience.md) | My Learning, hoạt động học, video, ghi chú, thảo luận | Active |
| [08-certificate.md](08-certificate.md) | Certificate template, gán chứng chỉ, học viên nhận | Active |
| [09-notification-email.md](09-notification-email.md) | Notification & Email thủ công, Recipients, Mail Logs, Comment Replier | **Gửi thủ công ẩn** |
| [10-storyline.md](10-storyline.md) | Articulate Storyline | **Ẩn** |
| [11-dashboard-sis.md](11-dashboard-sis.md) | SIS Operational Dashboard (3 loại đang dùng) | Active |

### Nền tảng kỹ thuật

| File | Nội dung |
|---|---|
| [12-data-model.md](12-data-model.md) | 85 bảng, quan hệ lõi, multi-tenant, marketplace, Casbin/Keycloak |
| [13-mail-events.md](13-mail-events.md) | 30 mail tự động theo event, trạng thái bật/tắt |
| [14-api-surface.md](14-api-surface.md) | Bản đồ API hai hệ, **vùng KB chưa phủ** |

### Định hướng

| File | Nội dung |
|---|---|
| [15-product-direction.md](15-product-direction.md) | **Đọc trước khi viết BRD/FS.** UpLnD: đơn tenant → SaaS đa tenant, LMS → hệ phát triển năng lực. Kèm danh sách **chỗ đóng cứng UpBase** phải gỡ |

> File 01–14 mô tả hệ thống **đang có**. File 15 mô tả nơi sản phẩm **đang đi tới**. Mọi BRD phải nói rõ yêu cầu thuộc tầng nào, và phục vụ UpBase-only hay mọi tenant.

---

## Quy ước

### Trạng thái tính năng

| Nhãn | Nghĩa |
|---|---|
| **Active** | Đang dùng |
| **Hidden** | Page UG đặt `hidden: true` — **đã có code nhưng tạm ẩn**, chưa dùng hoặc chưa tối ưu |

> ⚠️ Hidden **không phải** "không tồn tại". Khi phân tích impact, tính năng ẩn vẫn phải xét — đây là nhóm dễ bỏ sót nhất.

5 page đang ẩn: Storyline · Quản lý bài kiểm tra trong lớp · Notification & Email List · Recipients List · Mail Logs & Blocked Email.

### Mã Business Rule

| Dạng mã | Nguồn |
|---|---|
| `BR-COURSE-01`, `BR-EDIT-07`, `BR-MENTOR-02`… | **Có sẵn trong UG** — giữ nguyên nguyên văn |
| `KB-<MOD>-01` | **Claude trích**, chưa được BA duyệt |

### Ký hiệu

| Ký hiệu | Nghĩa |
|---|---|
| `❓BA` | Chưa rõ, cần BA xác nhận — **không dùng làm fact** |
| `[suy ra]` | Claude suy từ nội dung nguồn, không phải câu chữ trực tiếp |
| ✅ Đã đính chính | Kết luận cũ sai, đã sửa — ghi rõ ngày |

---

## Khoảng trống còn lại

1. **Chưa có KB cho mảng lịch dạy / giáo viên / phòng học / lễ tân / thi cử** — 33 nhóm API, ước tính cần thêm 4–6 file.
2. **Schema DB chỉ có PK/FK**, không có cột đầy đủ và kiểu dữ liệu. Nguồn tốt nhất hiện tại cho field-level là `components.schemas` trong Swagger (267 DTO).
3. **Permission matrix** nằm trong dữ liệu `casbin_rule`, không đọc được từ schema. Cần export policy hoặc tài liệu role.
4. **Chưa có NFR** — không có số liệu hiệu năng, tải, SLA.
5. **13 page UG thiếu khai báo `Module chính`** — quan hệ chéo do Claude suy ra, đã đánh dấu `[suy ra]`.
6. **Chưa có FS của bất kỳ tính năng nào.** KB sẽ giàu dần: mỗi FS viết xong thì cập nhật ngược lại KB.
