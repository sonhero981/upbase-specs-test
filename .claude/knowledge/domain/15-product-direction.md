# 15 — Định hướng sản phẩm UpLnD Platform

| | |
|---|---|
| Nguồn | BA cung cấp 23/09/2026 |
| Trạng thái | **Định hướng** — chưa phải hệ thống hiện tại |

> ⚠️ **Mọi file KB khác (01–14) mô tả hệ thống ĐANG CÓ.** File này mô tả nơi sản phẩm đang đi tới. Khi viết BRD/FS, phải biết mình đang viết cho tầng nào.

---

## 0. Kiến trúc sản phẩm — 4 portal

**UpLnD Platform** là sản phẩm lớn, gồm:

| Portal | Đối tượng | Vai trò | Phạm vi KB |
|---|---|---|---|
| **UpLMS** | Người học | Học, làm bài, xem kết quả | ✅ KB 01–14 |
| **UpLMS Ops** | Người vận hành | Dựng nội dung, mở lớp, chấm điểm | ✅ KB 01–14 |
| **UpAcademy** | Tổ chức (B2B) · khách lẻ (B2C) | **Marketplace** mua khoá học | ⚪ Chưa có KB |
| **Admin** | Bên B2B | Tenant **tự quản trị** UpLnD của mình | ⚪ Chưa có KB |
| **Super Admin** | UpBase | Quản lý **các tenant** | ⚪ Chưa có KB |

> **UpLnD = UpLMS + UpLMS Ops** — cụm phục vụ *người học* và *người vận hành*. Đây là phạm vi đang làm.
>
> Dấu vết marketplace trong DB (`course_listing`, `tenant.can_publish_marketplace`, `billing_model`, `commission_rule_id`) và API (`Lessee Contacts/Tag Management`) thuộc về **UpAcademy** và **Super Admin** — giải thích tại sao chúng có trong schema mà UG không nhắc.

## 0.1 Thứ tự ưu tiên — đã chốt

```
[1] UpLnD đủ tính năng cho người học + người vận hành
        ↓  ready for go-to-market
[2] Multi-tenant → bán SaaS
        ↓
[3] UpAcademy · Admin · Super Admin
```

> ⚠️ **Nhưng database và hạ tầng phải chuẩn hoá NGAY TỪ ĐẦU**, không đợi tới bước [2].
>
> Đây là ràng buộc quan trọng nhất với công việc BA hiện tại: **tính năng làm cho UpBase, nhưng dữ liệu và hạ tầng thiết kế cho đa tenant.** Xem §6 — danh sách chỗ đóng cứng — và §7 — tác động lên quy trình.

---

## 1. Đang ở đâu

UpLMS chạy thật, **một tenant, cấu hình cứng cho UpBase**. Là một LMS đủ dùng: khoá, lớp, ghi danh, chứng chỉ, thông báo. Quản lý được việc học, nhưng chỉ trả lời được câu **"ai đã học gì"**.

## 2. Đi về đâu — hai chuyển dịch khác nhau về bản chất

| | **Hạ tầng** | **Sản phẩm** |
|---|---|---|
| Từ → đến | Đơn tenant → **SaaS đa tenant** | LMS → **hệ phát triển năng lực** |
| Nội dung | Cô lập dữ liệu, ngữ cảnh tenant xuyên suốt, xác thực và phân quyền tập trung | Đổi đơn vị đo: **khoá học hoàn thành → năng lực đạt được**. Khoá học tụt xuống thành phương tiện |
| Bản chất | Việc kỹ thuật — tốn công, **không rủi ro về mặt sản phẩm** | **Chuyển dịch thật** |

## 3. Bài toán lớn: không phải multi-tenant, mà là **khác biệt**

Thị trường LMS đã đỏ và rẻ. Lên SaaS bằng một LMS bình thường nghĩa là đi bán thứ mà TalentLMS, Moodle và chục cái khác đã bán, với giá thấp hơn.

> **Hạ tầng đa tenant không tạo ra khách hàng — nó chỉ cho phép phục vụ khách hàng nếu đã có lý do để họ mua.**

## 4. Vòng tròn khép kín — lý do để mua

```
Vị trí yêu cầu năng lực gì
   → người này đang thiếu gì
   → học cái gì thì lấp được
   → học xong sinh bằng chứng
   → cập nhật lại năng lực
```

---

## 5. Hệ thống hiện tại đứng ở đâu so với vòng tròn

| Mắt xích | Hạ tầng đã có | Đánh giá |
|---|---|---|
| Vị trí yêu cầu năng lực gì | ❌ Không có entity nào cho **vị trí / khung năng lực** | Thiếu hoàn toàn |
| Người này đang thiếu gì | ⚠️ `users.english_level_id`, `university_program_id`, `category_primary_id` | Mầm mống, chưa phải năng lực |
| Học cái gì thì lấp được | ⚠️ `course_outcomes`, `course_learning_outcomes`, `course_section_outcome_instances` | **3 bảng outcome** — hạ tầng sơ khai gần nhất với competency |
| Học xong sinh bằng chứng | ⚠️ `quiz_attempts`, `courses_users_certificates` | **Chỉ có điểm bài test và chứng chỉ hoàn thành** |
| Cập nhật lại năng lực | ❌ Không có | Thiếu hoàn toàn |

> **Ba bảng outcome là tài sản đáng chú ý nhất.** KB [12-data-model.md](12-data-model.md) từng đánh dấu chúng là "chưa ánh xạ được sang KB" vì UG chỉ mô tả Learning Outcome ở cấp Section. Xét theo định hướng, đây có thể là nền của lớp năng lực. `❓BA`

---

## 6. 🚨 Các chỗ đóng cứng UpBase — nợ kỹ thuật của chuyển dịch SaaS

Trích từ KB, đây là những chỗ logic UpBase bị nhúng vào sản phẩm. Mỗi chỗ là một điểm phải gỡ khi lên đa tenant:

| Chỗ đóng cứng | Nguồn | Mức |
|---|---|---|
| **`support-groups` không có `tenant_id`** — khác mọi bảng khác | [12-data-model.md](12-data-model.md) | 🔴 Cao — rò rỉ dữ liệu giữa tenant |
| **Mail #23 fix cứng nội dung** cho case lớp chính khai giảng sau Foundation | [13-mail-events.md](13-mail-events.md) | 🟠 |
| **Comment Replier tự động thêm/xoá học viên vào lớp**, gia hạn mỗi năm 1 lần | [09-notification-email.md](09-notification-email.md) | 🟠 Quy trình vận hành UpBase nhúng vào code |
| **Thời hạn Foundation mặc định 60 ngày** (BR-STATUS-01) | [04-class.md](04-class.md) | 🟡 Cấu hình được? |
| **Ngưỡng chuyên cần 70%** | [11-dashboard-sis.md](11-dashboard-sis.md) | 🟡 Cấu hình được? |
| **Program = ACCA / CFA / CMA** cố định | [11-dashboard-sis.md](11-dashboard-sis.md) | 🟠 Đặc thù UpBase |
| **Điểm thành phần 4 loại cố định** (Tiến độ / Section / Mid / Final) | [01-course.md](01-course.md) | 🟠 Mô hình chấm của UpBase |
| **Tổng điểm thành phần phải = 100** (BR-COURSE-INFO-07) | [01-course.md](01-course.md) | 🟡 |
| **SSO Lark** là đường đăng nhập học viên | [06-user-account.md](06-user-account.md) | 🟠 Tenant khác dùng IdP khác — `keycloak_user_id` có thể là lối ra |
| **Đồng bộ tài khoản từ HRIS UpBase** một chiều | [06-user-account.md](06-user-account.md) | 🔴 Cao — mỗi tenant một HRIS |
| **Foundation → Normal Course** là mô hình học của UpBase | [01-course.md](01-course.md) | 🟠 |

---

## 7. Tác động lên quy trình BA

### Mọi BRD phải trả lời trước

| Câu hỏi | Vì sao |
|---|---|
| Yêu cầu này phục vụ **UpBase-only hay mọi tenant**? | Quyết định nó là cấu hình hay là code |
| Nó thuộc tầng **LMS (đang có)** hay tầng **năng lực (định hướng)**? | Quyết định KB nào là nguồn |

### Mọi FS phải có mục tenant-awareness

| Hạng mục | Nội dung |
|---|---|
| Field global vs per-tenant | Field nào dùng chung, field nào mỗi tenant một giá trị |
| Hằng số | Mọi con số cứng (60 ngày, 70%, 100 điểm) phải khai báo rõ: hardcode hay cấu hình |
| Cô lập dữ liệu | Truy vấn có lọc `tenant_id` không |
| Danh mục | Enum cố định hay tenant tự định nghĩa (Program, Category, Level) |

### Impact Analysis thêm một chiều quét

Ngoài 12 vùng hiện có, thêm: **"thay đổi này có làm tăng hay giảm nợ đóng cứng UpBase ở §6 không?"**

> Nếu không thêm chiều này, mỗi FS mới sẽ **đóng cứng thêm một giả định đơn tenant** — và chuyển dịch SaaS càng xa.

---

## 8. Câu hỏi để sau — KHÔNG giải quyết ở giai đoạn này

Ghi lại để không mất, nhưng **đây không phải việc của giai đoạn xây UpLnD**. Sẽ xử lý khi bước sang tầng năng lực.

| # | Câu hỏi |
|---|---|
| Q1 | **"Bằng chứng năng lực" là gì?** Hiện chỉ có điểm quiz và chứng chỉ hoàn thành. |
| Q2 | **Ai sở hữu khung năng lực?** Khách hàng tự dựng, mua kèm bộ dựng sẵn theo ngành, hay import từ HRIS? |
| Q3 | **3 bảng outcome** có phải nền của lớp năng lực, hay sẽ dựng entity mới? |
| Q4 | **Nội dung chuyên ngành ACCA/CFA/CMA** có nằm trong định hướng khác biệt không? |
| Q5 | Tenant đầu tiên ngoài UpBase là ai, khi nào? |
