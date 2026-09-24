# 14 — API Surface

| | |
|---|---|
| UpLMS (học viên) | https://lms-be.staging.upbase.asia/api/v1/docs · JSON: `/docs-json` |
| UpLMS Ops | https://ops-be.staging.upbase.asia/api/v1/docs · JSON: `/docs-json` |
| Truy cập | **Công khai, không cần auth** để đọc spec (staging) |
| Ngày trích | 23/09/2026 |

| | LMS | Ops |
|---|---|---|
| Endpoint path | 142 | **413** |
| Operation | 153 | **555** |
| DTO schema | 51 | **216** |
| Nhóm tag | 26 | **58** |

---

## 1. 🚨 Kết luận quan trọng nhất

**KB dựng từ User Guide chỉ bao phủ khoảng một nửa hệ thống.**

| | LMS | Ops |
|---|---|---|
| Nhóm chức năng KB đã có | 18 | 33 |
| **Nhóm chức năng KB CHƯA có** | **8** | **25** |

Toàn bộ mảng **lịch dạy – giáo viên – phòng học – thi cử – tổ chức – phân quyền** không có trong UG, nên không có trong KB. Đây không phải chi tiết nhỏ: riêng nhóm `Schedules` + `request-schedules` ở Ops đã là **45 operation**, nhiều hơn cả module Course (20).

> Khi chạy Impact Analysis, **đừng coi KB là đủ**. Bất cứ thay đổi nào chạm tới Class, User, Quiz đều có thể lan sang các mảng dưới đây mà KB không cảnh báo được.

---

## 2. Mảng lớn chưa có trong KB

### 2.1 Lịch & vận hành giảng dạy — mảng lớn nhất

| Nhóm API | Ops | LMS | Nội dung lộ ra từ endpoint |
|---|---|---|---|
| `Schedules` | 21 | 4 | `teacher-schedules`, `weekly-norms`, `busy-schedule`, `available-receptionists`, `on-call-people`, `facilities` |
| `request-schedules` | 24 | 14 | `teaching`, `time-off`, `teaching-mode`, `busy-schedules`, `receptionists` |
| `Class Schedule` | 9 | — | `{class_id}/rooms`, `{class_id}/schedule-calendar`, `{class_id}/teacher` |
| `Room Schedule Management` | 9 | — | `available-rooms`, `inactive/{room_id}` |
| `Room Management` | 4 | — | CRUD phòng học |
| `Holiday Schedule Management` | 1 | — | `import` lịch nghỉ lễ |
| `Class Teaching Progress Management` | 7 | 6 | `get-lesson/{id}`, `{classId}/get-course-section/{classScheduleId}` |
| `Calendar Student` | — | 2 | Lịch phía học viên |
| `Class Facility Management` | 4 | — | CRUD cơ sở (**giải thích filter `Facility`** ở SIS dashboard) |

Hàm ý: hệ thống quản lý **buổi học thực tế** (lecture/session), **giáo viên và định mức giờ dạy**, **phòng học**, **lễ tân và ca trực**, **đơn xin nghỉ / đổi chế độ dạy**. Bảng DB tương ứng: `class_lecture_instances`.

> Đây cũng là nguồn dữ liệu cho dashboard **Tỉ lệ chuyên cần** (buổi học, điểm danh) mà [11-dashboard-sis.md](11-dashboard-sis.md) không giải thích được.

### 2.2 Thi cử — ngoài Test/Quiz trong khoá

| Nhóm API | Ops | LMS | Endpoint đáng chú ý |
|---|---|---|---|
| `Examination` | 8 | — | `{id}/students` |
| `Event Test Management` | 10 | — | `participants`, `attempts/answers/{id}` |
| `Entrance Test` | — | 3 | `chart-data/{quizAttemptId}`, `quiz-attempts/{attemptId}/answers` |
| `Event Management` | 1 | — | — |

Ba loại bài kiểm tra **nằm ngoài khoá học**: kỳ thi (Examination), bài test theo sự kiện (Event Test), bài kiểm tra đầu vào (Entrance Test). KB [03-assessment.md](03-assessment.md) chỉ mô tả Test/Quiz **bên trong** khoá.

> ❌ **PO xác nhận 23/09/2026: `Examination` và `Entrance Test` — hệ thống tạm thời KHÔNG CÓ hai chức năng này.**
>
> Endpoint vẫn tồn tại trong Swagger nhưng **chức năng không được dùng**. Đây là bằng chứng cho thấy **bề mặt API không đồng nghĩa với tính năng đang chạy** — có endpoint không có nghĩa là có tính năng.
>
> ⚠️ **Áp dụng khi phân tích:** thấy một nhóm API lạ thì **hỏi PO trước khi kết luận tính năng đó tồn tại**. `Event Test Management` và `Event Management` chưa được xác nhận — vẫn `❓BA`.

### 🔁 Danh sách endpoint có nhưng tính năng KHÔNG có

Cập nhật dần. Mỗi dòng là một lần suýt kết luận sai.

| Endpoint / nhóm API | Trạng thái thật | Xác nhận |
|---|---|---|
| `Examination` (Ops, 8 op) | ❌ Không có tính năng | PO 23/09/2026 |
| `Entrance Test` (LMS, 3 op) | ❌ Không có tính năng | PO 23/09/2026 |
| `POST /api/v1/courses/{id}/trial/upgrade-now` (LMS) | ❌ **Không có khoá Trial** | PO 23/09/2026 |
| `Event Test Management` (Ops, 10 op) · `Event Management` (Ops, 1 op) | `❓BA` — chưa xác nhận | — |

> **Ba lần trong một buổi phân tích.** Tỷ lệ endpoint "chết" trong hệ này đủ cao để **không bao giờ suy ra tính năng từ sự tồn tại của endpoint**.

### 2.3 Tổ chức & phân quyền

| Nhóm API | Ops | Nội dung |
|---|---|---|
| `Roles Management` | 8 | CRUD role, gán/gỡ staff khỏi role |
| `Permissions management` | 2 | `permissions`, `state-permission-initial` |
| `Group Management` | 9 | CRUD group, gán user |
| `Department Management` | 9 | `list-unit`, `parent-list` → **cây phòng ban** |
| `Staff Position` / `Staff Level` / `Staff Facility` | 6/2/5 | Chức danh, cấp bậc, cơ sở của nhân sự |

> **Đây là nguồn cho permission matrix** mà KB còn thiếu. Kết hợp với `casbin_rule` trong DB ([12-data-model.md](12-data-model.md)).

### 2.4 Danh mục học thuật

| Nhóm API | Ops | LMS | Ghi chú |
|---|---|---|---|
| `Subject Management` | 5 | 2 | LMS có `subjects/program-name` → **liên quan `Program` ACCA/CFA/CMA** |
| `Course Level Management` | 5 | — | **Giải thích "course 4 level"** ở SIS dashboard |
| `Course Timeline Management` | 8 | — | Timeline khoá học |
| `Course Tag Management` | 5 | — | Tag |
| `majors` | 1 | — | Ngành học |
| `universities` | 1 | — | Trường đại học (khớp `users.university_program_id`) |
| `Question Categories` / `Question Tag` | 2/2 | — | Phân loại câu hỏi |

### 2.5 Thương mại & tenant

| Nhóm API | Ops | Ghi chú |
|---|---|---|
| `Lessee Contacts Management` | 5 | *Lessee* = bên thuê |
| `Lessee Tag Management` | 5 | |

Khớp với `tenant.billing_model`, `tenant.can_publish_marketplace`, `course_listing` trong DB. `❓BA`

### 2.6 Khác

| Nhóm API | Ops | Ghi chú |
|---|---|---|
| `Caching Manager` | 11 | Khớp bảng `caching_settings` |
| `Address Management` | 6 | Khớp `provinces`/`districts`/`wards` |
| `Surveys Management` | 4 | **Khảo sát** — UG không có |
| `Story` | 6 | Khác `Storyline Management` (17) — **hai khái niệm riêng** |
| `Mail Log Management` | 4 | Khớp [13-mail-events.md](13-mail-events.md) |
| `Import logs` | 2 | Khớp `import_logs` |
| `Feature Section Management` | 2 | `❓BA` — feature flag? |

---

## 3. Nhóm API khớp với KB hiện có

| KB | Nhóm API tương ứng (Ops/LMS) |
|---|---|
| [01-course.md](01-course.md) | `Course Management`(20) · `Course Full Management`(31/11) · `Course LMS`(19) · `Course Category Management` · `Course Learning Outcome`/`Outcome Management` · `Resource Management`(30) |
| [02-question-bank.md](02-question-bank.md) | `Question Bank`(8) · `Question Topic` · `Question Categories` · `Question Tag` |
| [03-assessment.md](03-assessment.md) | `Quiz`(25/3) · `Quiz Attempt`(7/8) · `Class Quiz Management`(9) |
| [04-class.md](04-class.md) | `Class Management`(51/13) · `Class Resource Management`(30/4) |
| [05-grading.md](05-grading.md) | `Quiz Attempt Grading`(14) |
| [06-user-account.md](06-user-account.md) | `User Management`(24/14) · `Staff Management`(15) · `Auth`(3/3) |
| [07-learning-experience.md](07-learning-experience.md) | `Course Discussion Manage`(7) · `Course Section Note Manage`(5) · `Resource LMS`(5) |
| [08-certificate.md](08-certificate.md) | `Certificate`(6) · `User Certificate`(2) |
| [09-notification-email.md](09-notification-email.md) | `Notifications Management`(5/7) · `Mail Log Management`(4) · `Support Group Management`(9) |
| [10-storyline.md](10-storyline.md) | `Storyline Management`(17) |
| [11-dashboard-sis.md](11-dashboard-sis.md) | `Sis Dashboard`(12) ✅ xác nhận SIS nằm trong Ops |

> **`Class Management` ở Ops có 51 operation** — gấp hơn 2 lần bất kỳ nhóm nào khác. KB [04-class.md](04-class.md) dựng từ 6 page UG gần như chắc chắn chưa phủ hết.

---

## 4. Cách dùng nguồn này

| Việc | Cách làm |
|---|---|
| Lấy danh sách endpoint của một module | `curl -s <host>/api/v1/docs-json \| jq '.paths \| keys'` |
| Lấy **field + kiểu dữ liệu** của một entity | Đọc `components.schemas` — **216 DTO ở Ops**, đây là nguồn tốt nhất hiện có cho field-level spec |
| Kiểm chứng một business rule | So endpoint + DTO với rule `KB-*` trong KB |
| Viết FS cần API contract | Trích thẳng từ `docs-json`, không suy đoán |

> `components.schemas` là thứ KB đang thiếu nhất: **kiểu dữ liệu, required, enum ở cấp field**. UG chỉ mô tả UI. Khi viết FS, lấy từ đây.

---

## 5. Điểm cần BA xác nhận

| # | Câu hỏi |
|---|---|
| Q1 | 🚨 **Mảng lịch dạy / giáo viên / phòng học / lễ tân — có thuộc phạm vi BA không?** Nếu có, cần bổ sung KB (ước tính thêm 4–6 file). |
| Q2 | **Examination / Event Test / Entrance Test** khác Test/Quiz trong khoá thế nào? |
| Q3 | `Subject` vs `Course Category` vs `Program` vs `Course Level` — **4 khái niệm phân loại**, quan hệ ra sao? |
| Q4 | `Story` (6 endpoint) khác `Storyline` (17) thế nào? |
| Q5 | `Surveys Management` — tính năng khảo sát đang dùng? |
| Q6 | `Feature Section Management` — cơ chế bật/tắt tính năng? Nếu đúng thì **đây là nơi quản lý các page `hidden`**. |
| Q7 | Staging có phản ánh đúng production không? Có môi trường prod docs không? |
| Q8 | API docs công khai không cần auth — có chủ đích không? (chỉ ghi nhận, không phải việc của BA) |
