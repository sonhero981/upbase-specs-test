# 14 — API Surface

| | |
|---|---|
| UpLMS (học viên) | https://uplms-api.staging.upbase.asia/lms/api/v1/docs · JSON: `/docs-json` |
| UpLMS Ops | https://uplms-api.staging.upbase.asia/ops/api/v1/docs · JSON: `/docs-json` |
| Truy cập | **Công khai, không cần auth** để đọc spec (staging) |
| Ngày trích | **05/10/2026** |

> 🔄 **Tên miền đã đổi (PO cung cấp 05/10/2026).** Hai host cũ `lms-be.staging.upbase.asia` và `ops-be.staging.upbase.asia` **không dùng được nữa** — chứng chỉ TLS không khớp tên miền. Host mới gộp làm một, tách bằng tiền tố đường dẫn `/lms` và `/ops`.

| | LMS | Ops | | LMS cũ | Ops cũ |
|---|---|---|---|---|---|
| Endpoint path | 126 | **381** | | 142 | 413 |
| Operation | 136 | **514** | | 153 | 555 |
| DTO schema | 46 | **200** | | 51 | 216 |
| Nhóm tag | 23 | **52** | | 26 | 58 |

> **Bề mặt API co lại, không phình ra.** Giảm 41 operation ở Ops và 17 ở LMS so với bản 23/09/2026. Nguyên nhân chính là ba nhóm chức năng chết đã bị gỡ — xem §2.2.

### Đổi so với bản 23/09/2026

| Nhóm | Cũ | Mới | |
|---|---|---|---|
| `Examination` (Ops) | 8 | **0** | ✅ Đã gỡ — khớp PO xác nhận *"không có tính năng"* |
| `Event Test Management` (Ops) | 10 | **0** | ✅ Đã gỡ — **trả lời được `❓BA` treo từ 23/09** |
| `Event Management` (Ops) | 1 | **0** | ✅ Đã gỡ — cùng lý do |
| `Entrance Test` (LMS) | 3 | **0** | ✅ Đã gỡ — khớp PO xác nhận |
| `Auth` (LMS) | 3 | **0** | Chuyển đi đâu chưa rõ. `❓BA` |
| `majors` · `universities` (Ops) | 1 · 1 | **0** | Đã gỡ |
| `Staff Facility` → `Staff Facility Management` | 5 | 5 | Chỉ đổi tên nhóm |
| `Course Learning Outcome` / `Outcome Management` | gộp | 5 + 4 | Giờ tách rõ hai nhóm |
| **`Report LMS`** (LMS) | — | **6** | 🆕 **Nhóm mới, KB chưa có.** Xem §2.7 |
| `Class Management` (Ops) | 51 | 45 | −6 |
| `Staff Management` (Ops) | 15 | 10 | −5 |
| `Quiz` (Ops) | 25 | 22 | −3 |
| `Class Management` (LMS) | 13 | 10 | −3 |
| `User Management` (LMS) | 14 | 11 | −3 |
| `User Management` (Ops) | 24 | 22 | −2 |
| `Sis Dashboard` (Ops) | 12 | 10 | −2 |

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
| ~~`Examination`~~ | **0** | — | ✅ Đã gỡ khỏi API (05/10/2026) |
| ~~`Event Test Management`~~ | **0** | — | ✅ Đã gỡ khỏi API (05/10/2026) |
| ~~`Entrance Test`~~ | — | **0** | ✅ Đã gỡ khỏi API (05/10/2026) |
| ~~`Event Management`~~ | **0** | — | ✅ Đã gỡ khỏi API (05/10/2026) |

Ba loại bài kiểm tra **nằm ngoài khoá học** từng lộ ra qua API: kỳ thi (Examination), bài test theo sự kiện (Event Test), bài kiểm tra đầu vào (Entrance Test). KB [03-assessment.md](03-assessment.md) chỉ mô tả Test/Quiz **bên trong** khoá.

> ❌ **PO xác nhận 23/09/2026: `Examination` và `Entrance Test` — hệ thống KHÔNG CÓ hai chức năng này.**
>
> ✅ **Đối chiếu lại 05/10/2026: cả bốn nhóm đã bị gỡ khỏi Swagger.** Thực tế khớp lời PO, và `Event Test Management` + `Event Management` — hai nhóm treo `❓BA` từ 23/09 — **cũng đã biến mất**, nên không cần hỏi nữa.
>
> ⚠️ **Bài học vẫn giữ nguyên:** lần trước endpoint tồn tại mà tính năng không có. **Bề mặt API không đồng nghĩa với tính năng đang chạy** theo cả hai chiều. Thấy một nhóm API lạ thì **hỏi PO trước khi kết luận**.

### 🔁 Danh sách endpoint có nhưng tính năng KHÔNG có

Cập nhật dần. Mỗi dòng là một lần suýt kết luận sai.

| Endpoint / nhóm API | Trạng thái thật | Xác nhận |
|---|---|---|
| ~~`Examination`~~ (Ops) | ❌ Không có tính năng → **đã gỡ khỏi API 05/10** | PO 23/09/2026 |
| ~~`Entrance Test`~~ (LMS) | ❌ Không có tính năng → **đã gỡ khỏi API 05/10** | PO 23/09/2026 |
| ~~`Event Test Management`~~ · ~~`Event Management`~~ (Ops) | ❌ **Đã gỡ khỏi API 05/10** — không cần hỏi nữa | Đối chiếu 05/10/2026 |
| `POST /api/v1/courses/{id}/trial/upgrade-now` (LMS) | ❌ **Không có khoá Trial** | PO 23/09/2026 |
| `Department Management` (Ops, 9 op) | ❌ **Không chạy.** Trước đây chỉ dành cho `staffs` | PO 05/10/2026 |
| **`Group Management`** (Ops, 9 op) | ❌ **Coi như không có.** Nhóm phẳng, chỉ CRUD + gán user. PO chốt bỏ hẳn, làm lại từ đầu ở dự án Group | PO 05/10/2026 |
| **Recipients List** *(màn nhóm người nhận Email)* | ❌ **Coi như không có.** Khi mở lại chức năng gửi thông báo từ Ops sẽ chọn người nhận từ chức năng Nhóm mới | PO 05/10/2026 |
| **`PUT /api/v1/classes/{id}/students/transfer`**<br>**`PUT /api/v1/classes/{id}/students/{student_id}/revert-transfer`** | ❌ **Không có chức năng chuyển lớp.** Muốn chuyển thì xoá khỏi lớp cũ, thêm vào lớp mới, **học lại từ đầu** | PO 06/10/2026 |
| `Auth` (LMS, 3 op) | `❓BA` — biến mất khỏi Swagger 05/10, chưa rõ chuyển đi đâu | — |

> **Sáu lần trong hai buổi phân tích.** Tỷ lệ endpoint "chết" trong hệ này đủ cao để **không bao giờ suy ra tính năng từ sự tồn tại của endpoint** — và chiều ngược lại cũng đúng: nhóm chức năng chết **có thể bị gỡ bất cứ lúc nào**, nên số liệu trong file này phải đối chiếu lại trước mỗi đợt phân tích.
>
> Lần thứ sáu đáng chú ý vì khác bốn lần trước: `transfer` **không phải cả một nhóm API** mà là **hai endpoint lẻ nằm giữa một nhóm đang chạy** *(`Class Management`)*. Nhóm API sống không bảo đảm mọi endpoint trong đó đều sống.

### 2.3 Tổ chức & phân quyền

| Nhóm API | Ops | Nội dung |
|---|---|---|
| `Roles Management` | 8 | CRUD role, gán/gỡ staff khỏi role |
| `Permissions management` | 2 | `permissions`, `state-permission-initial` |
| `Group Management` | 9 | ❌ **Coi như không có** — PO chốt 05/10/2026, xem bảng endpoint chết.<br>Hiện là **nhóm phẳng**: `GET POST /groups` · `GET PUT DELETE /groups/{id}` · `POST DELETE /groups/users` · `GET /groups/{id}/users` · `GET /groups/{id}/select-users`. **Không có cha con, không có nguồn, không có quản lý** |
| `Department Management` | 9 | ❌ Không chạy. `list-unit`, `parent-list` → **cây phòng ban**, `{id}/assign-position` → gắn chức danh. Dành cho `staffs`, không dành cho `users` |
| `Support Group Management` | 9 | Comment Replier. `{id}/supporters` thêm gỡ thành viên, `{id}/avatar` |
| `Staff Position` / `Staff Level` / `Staff Facility Management` | 6/2/5 | Chức danh, cấp bậc, cơ sở của nhân sự |

### 2.3b 🆕 `Report LMS` — nhóm mới phát hiện 05/10/2026

Sáu endpoint ở phía **học viên**, KB chưa có file nào mô tả:

| Endpoint | Nội dung |
|---|---|
| `GET /report/{class_id}/overall` | Hoạt động tổng quan |
| `GET /report/{class_id}/weekly` | Hoạt động theo tuần |
| `GET /report/{class_id}/topic` | Hoạt động theo chủ đề |
| `GET /report/{class_id}/learning-result` | Kết quả học |
| `GET /report/{class_id}/mock-test-result` | Kết quả thi thử |
| `GET /report/{class_id}/exam-prediction` | **Dự đoán kết quả thi** |

> ⚠️ **Mọi báo cáo đều lấy `class_id` làm khoá.** Không có chiều nào theo người, theo nhóm hay theo phòng ban. Bất kỳ yêu cầu nào về *"cộng dồn số liệu theo cơ cấu tổ chức"* đều phải thêm một chiều mới vào đây, không tận dụng được.
>
> `❓BA` — `exam-prediction` là tính năng đang chạy hay endpoint chết như `Examination` trước đây?

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
| [06-user-account.md](06-user-account.md) | `User Management`(22/11) · `Staff Management`(10). ⚠️ `Auth` **đã biến mất** khỏi cả hai Swagger (05/10) |
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
| Lấy danh sách endpoint của một module | `curl -s https://uplms-api.staging.upbase.asia/{ops\|lms}/api/v1/docs-json \| jq '.paths \| keys'` |
| Lấy **field + kiểu dữ liệu** của một entity | Đọc `components.schemas` — **200 DTO ở Ops**, đây là nguồn tốt nhất hiện có cho field-level spec |
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
