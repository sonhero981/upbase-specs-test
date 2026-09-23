# 13 — Mail Events (Email tự động theo event)

| | |
|---|---|
| Hệ | UpLMS + UpLMS Ops + Cronjob |
| Trạng thái | 🟢 **Hệ thống gửi mail tự động ĐANG CHẠY** |
| Nguồn | `Danh sách mail UpLMS.xlsx` (30 mail) · BA xác nhận 23/09/2026 |

> ✅ **Đính chính quan trọng (23/09/2026).** Bản KB đầu tiên kết luận "module Email đang ẩn → luồng nghiệp vụ đứt ở mắt xích thông báo" — **sai**.
>
> Cái đang ẩn trên Ops chỉ là **phần gửi thủ công** (soạn và gửi Notification/Email theo setting trên giao diện). **Hệ thống gửi mail tự động theo event vẫn hoạt động bình thường** với 30 mail template.

---

## 1. Ba nguồn trigger

| Nguồn | Số mail | Nghĩa |
|---|---|---|
| **LMS** | 14 | Sự kiện phát sinh từ hệ thống học viên |
| **OPS** | 11 | Sự kiện phát sinh từ hệ thống vận hành |
| **Cronjob** | 3 | Chạy theo lịch |
| LMS + OPS | 1 | Cả hai |
| Cronjob + OPS | 1 | Cả hai |

---

## 2. Danh sách 30 mail event

### Tài khoản & bảo mật

| STT | Trigger | Nội dung | Trạng thái |
|---|---|---|---|
| 1 | OPS | Tài khoản UpLMS Ops **đã được mở khoá** | 🟢 |
| 2 | OPS | Tài khoản UpLMS Ops **đã bị khoá** | 🟢 |
| 4 | OPS | **Tạo tài khoản staff thành công** — gửi kèm Username + Password | 🟢 |
| 6 | LMS | Reset password LMS thành công, **kèm mật khẩu mới** | 🔴 **Ngưng** — LMS dùng SSO Lark, không còn tính năng reset password |
| 7 | OPS | Reset password staff thành công, kèm mật khẩu mới | `❓BA` |
| 8 | OPS | Đổi mật khẩu thành công (không kèm mật khẩu) | 🔴 **Ngưng** — *"giờ cũng ẩn nút đổi pass đi rồi"* |
| 9 | LMS + OPS | **Mã OTP** kèm thời gian hiệu lực `{{EFFECT_TIME}}` phút | `❓BA` — vẫn dùng cho Edit Email của Staff? |

### Khoá học & chứng chỉ

| STT | Trigger | Nội dung | Trạng thái |
|---|---|---|---|
| 10 | LMS | **Hoàn thành khoá học** + link certificate | 🟢 |
| 11 | Cronjob + OPS | **Chào mừng vào khoá học** — nội dung phân nhánh theo `IS_PUBLIC_ENROLL` / `IS_FLEXIBLE_CLASS` / lớp có ngày khai giảng | 🟢 |
| 12 | Cronjob | **Khoá học đã hết hạn** + hướng dẫn liên hệ gia hạn | 🟢 |
| 29 | LMS | Hoàn thành khoá học (**không kèm chứng chỉ**) | 🟢 |
| 27 | LMS | **Kết quả khoá học chưa đạt** + điểm toàn khoá và tiêu chí đánh giá | 🟢 |

### Foundation Course

| STT | Trigger | Nội dung | Trạng thái |
|---|---|---|---|
| 23 | LMS | **Vượt qua Foundation** — báo thông tin khoá chính sắp bắt đầu | 🟢 ⚠️ *nội dung fix cứng cho case lớp chính khai giảng sau lớp Foundation; lớp flexible vẫn học bình thường* |
| 24 | LMS | Vượt qua Foundation **kèm certificate** | 🟢 |
| 25 | LMS | **Trượt Foundation lần 1** + điểm toàn khoá, tiêu chí đánh giá | 🟢 |
| 26 | LMS | **Trượt Foundation lần cuối** + hướng dẫn liên hệ hỗ trợ | 🟢 |

### Bài kiểm tra — thời gian truy cập

| STT | Trigger | Nội dung | Trạng thái |
|---|---|---|---|
| 13 | LMS | Danh sách bài kiểm tra **có giới hạn thời gian truy cập** trong khoá (dạng bảng mở–đóng) | 🟢 |
| 14 | LMS | Thời gian mở/đóng của **một bài kiểm tra** vừa thiết lập hoặc thay đổi | 🟢 |
| 15 | Cronjob | **Nhắc trước N ngày** về bài kiểm tra sắp mở | 🟢 |
| 16 | Cronjob | Nhắc bài kiểm tra **sắp hết hạn trong 1 ngày** | 🟢 |

> ⚠️ **Bốn mail này lộ ra một cơ chế UG hoàn toàn không mô tả: bài kiểm tra có `Thời gian mở` và `Thời gian đóng`.** KB [03-assessment.md](03-assessment.md) dựng từ UG chỉ có `Test Mode` (Tutor/Timed) và `Attempt` — không có khái niệm cửa sổ thời gian truy cập. DB có bảng `class_quiz_settings` và `class_user_quiz_settings`, API có `Class Quiz Management` (9 endpoint). `❓BA`

### Chấm điểm — **nhóm BA nêu là đang tạm ngưng**

| STT | Trigger | Nội dung | Trạng thái |
|---|---|---|---|
| 17 | LMS | Báo mentor **có học viên vừa nộp bài** | 🔴 Ngưng |
| 18 | OPS | Gửi mentor vừa được thêm vào lớp **danh sách học viên đã hoàn thành bài** | 🔴 Ngưng |
| 19 | OPS | Báo học viên **bài đã chấm xong** + link xem kết quả | 🔴 Ngưng |
| 20 | OPS | Báo học viên **hoàn tất chấm ở lần chấm thứ N** + link | 🔴 Ngưng |
| 32 | OPS | **Nhắc mentor** danh sách học viên đang chờ chấm | 🔴 Ngưng |
| 33 | OPS | Báo mentor **có yêu cầu chấm lại** + lý do + link | 🔴 Ngưng |
| 34 | LMS | Báo **main mentor có yêu cầu chấm lại từ học viên** + lý do + link | 🔴 Ngưng |
| 35 | OPS | Báo **main mentor có yêu cầu review bài chấm** từ mentor + link | 🔴 Ngưng |

> 🚨 **Đây là điểm cần chú ý nhất.** BA xác nhận *"các mail liên quan đến chức năng chấm điểm"* đang tạm ngưng kích hoạt. Nghĩa là **cảnh báo ở [05-grading.md](05-grading.md) §9 vẫn đúng, chỉ khác nguyên nhân**: không phải vì module Email ẩn, mà vì 8 mail này bị tắt có chủ đích.
>
> Hệ quả: luồng chấm điểm hiện **không có thông báo tự động** ở cả 4 mắt xích (assign · submit to review · regrading · trả kết quả cho học viên). Mentor và học viên phải tự vào hệ thống kiểm tra. `❓BA` — có cơ chế thay thế không?

### Thảo luận

| STT | Trigger | Nội dung | Trạng thái |
|---|---|---|---|
| 21 | LMS | **1 người trả lời comment** + nội dung trả lời | 🟢 |
| 22 | LMS | **Nhiều người trả lời comment** + nội dung | 🟢 |

---

## 3. Biến template

Template dùng cú pháp **Handlebars**: `{{VAR}}`, `{{#if}}`, `{{else}}`, `{{/if}}`, `{{#unless}}`, `{{{TABLE_ROWS}}}` (triple-brace = raw HTML).

| Biến | Dùng ở |
|---|---|
| `{{FIRST_NAME}}`, `{{STAFF_NAME}}`, `{{USERNAME}}`, `{{PASSWORD}}` | Tài khoản |
| `{{OTP_CODE}}`, `{{EFFECT_TIME}}` | OTP |
| `{{COURSE_NAME}}`, `{{COURSE_NORMAL_NAME}}`, `{{COURSE_DESCRIPTION}}` | Khoá học |
| `{{START_DATE}}`, `{{END_DATE}}`, `{{FLEXIBLE_DAYS}}` | Thời hạn |
| `{{CERTIFICATE_LINK}}` | Chứng chỉ |
| `{{QUIZ_NAME}}`, `{{START_TIME}}`, `{{END_TIME}}`, `{{NUMBER_DURATION_QUIZ}}`, `{{{TABLE_ROWS}}}` | Bài kiểm tra |
| `{{#if IS_PUBLIC_ENROLL}}`, `{{#if IS_FLEXIBLE_CLASS}}`, `{{#unless IS_NO_EXPIRED_CLASS}}` | Điều kiện |

> ⚠️ **`IS_PUBLIC_ENROLL`** hàm ý có luồng **học viên tự đăng ký khoá công khai** — UG không mô tả. Liên quan tới bảng `course_listing` (visibility, pricing_model) trong DB. Xem [12-data-model.md](12-data-model.md). `❓BA`

---

## 4. Business Rule

| ID | Rule | Nguồn |
|---|---|---|
| KB-MAIL-01 | Hệ thống gửi **mail tự động theo event**; phần gửi thủ công trên Ops đang ẩn. | BA xác nhận 23/09/2026 |
| KB-MAIL-02 | Mail reset/đổi mật khẩu phía LMS **ngưng** — học viên đăng nhập SSO Lark, không có chức năng reset password. | Excel comment + BA |
| KB-MAIL-03 | **8 mail thuộc luồng chấm điểm đang tạm ngưng kích hoạt.** | BA xác nhận |
| KB-MAIL-04 | Mail #23 (vượt Foundation) **fix cứng nội dung** cho trường hợp lớp chính khai giảng sau lớp Foundation; lớp flexible vẫn học ngay. | Excel comment |
| KB-MAIL-05 | Mail #4 gửi **mật khẩu dạng plaintext** trong email khi tạo tài khoản staff. | Excel STT 4 |
| KB-MAIL-06 | Mail #6 và #7 gửi **mật khẩu mới dạng plaintext** sau khi reset. | Excel STT 6, 7 |
| KB-MAIL-07 | Bài kiểm tra có **cửa sổ thời gian truy cập** (Thời gian mở / Thời gian đóng); hết giờ thì không truy cập được. | Excel STT 13–16 |
| KB-MAIL-08 | Có cronjob **nhắc trước N ngày** khi bài kiểm tra sắp mở và **trước 1 ngày** khi sắp đóng. | Excel STT 15, 16 |

> **KB-MAIL-05 và KB-MAIL-06 là rủi ro bảo mật**: mật khẩu gửi plaintext qua email. Ghi lại để BA cân nhắc, không phải để Claude tự sửa.

---

## 5. Phụ thuộc

| Module | Quan hệ |
|---|---|
| **User / Staff** | Mail tài khoản, khoá/mở khoá, OTP |
| **Course / Class** | Chào mừng, hết hạn, hoàn thành, Foundation |
| **Quiz** | Cửa sổ thời gian truy cập, nhắc lịch |
| **Grading** ⚠️ | 8 mail — **đang tạm ngưng** |
| **Certificate** | Link chứng chỉ trong mail |
| **Discussion** | Thông báo trả lời comment |
| **Cronjob** | 4 mail chạy theo lịch (11, 12, 15, 16) |
| **mail_logs** (DB) | Lưu lịch sử gửi — xem [09-notification-email.md](09-notification-email.md) §6 |

---

## 6. Điểm cần BA xác nhận

| # | Câu hỏi |
|---|---|
| Q1 | Mail **#7 (reset password staff)** và **#9 (OTP)** còn chạy không? Staff vẫn dùng username/password nên có thể vẫn cần. |
| Q2 | 8 mail chấm điểm ngưng — **có cơ chế thông báo thay thế không**, hay mentor/học viên phải tự kiểm tra? |
| Q3 | STT thiếu trong file: **3, 5, 28, 30, 31** — đã xoá hay chưa điền? |
| Q4 | **Cửa sổ thời gian truy cập bài kiểm tra** (mail 13–16) — cấu hình ở đâu? UG không mô tả. |
| Q5 | **`IS_PUBLIC_ENROLL`** — có luồng học viên tự đăng ký khoá công khai? |
| Q6 | Mail gửi mật khẩu plaintext (#4, #6, #7) — có kế hoạch đổi sang link đặt mật khẩu không? |
| Q7 | Mail #23 fix cứng nội dung — có ticket sửa cho case lớp flexible chưa? |
