# 12 — Data Model

| | |
|---|---|
| Nguồn | **Lark wiki → `Data Architecture`** — https://upbasevn.sg.larksuite.com/wiki/MaFpweI68iKNMvkTioLlJ1uJgQd |
| File | `UpLnd DB Full.html` (node con của trang trên) |
| Đối chiếu lần cuối | **05/10/2026** — tải lại file gốc, đọc được 85 bảng · 173 quan hệ, khớp bản KB này. `obj_edit_time` của file = 23/09/2026 11:41, **nguồn chưa đổi** |
| Quy mô | **85 bảng · 173 quan hệ khoá ngoại · 320 cột được khai** |
| Giới hạn | ⚠️ Không có kiểu dữ liệu, không có index, không có ràng buộc.<br>✅ **Đính chính 05/10/2026:** bản KB cũ ghi diagram *"chỉ chứa PK và FK"* — **sai**. Diagram có cả **cột thường**: `groups.name`, `departments.left/right/code/short_name`, `class_user_instances.source_type/status/learning_progress`, `users.type/status/is_operator`. Vẫn **không bảo đảm đủ cột**, nhưng nhiều hơn chỉ khoá |

> ## 🔄 Nguồn sống — phải đọc lại, không tin bản chép
>
> Schema nằm trên Lark và **thay đổi theo hệ thống**. KB này chỉ là bản chụp tại ngày đối chiếu ở trên.
>
> **Đọc lại khi:**
> - Yêu cầu chạm tới bảng / quan hệ dữ liệu — **bắt buộc**, trước khi kết luận trong Impact Analysis
> - Người dùng báo DB có thay đổi
> - **Định kỳ mỗi tháng** — quá 1 tháng kể từ "Đối chiếu lần cuối" thì đọc lại trước khi dùng
>
> Đọc lại xong mà **khác** bản này → cập nhật KB và sửa ngày, **đừng chỉ dùng tạm rồi bỏ qua**.

<details>
<summary><b>Cách lấy file từ Lark</b> (node con là <code>file</code>, không phải docx — không mở bằng tool đọc doc thường)</summary>

1. `wiki/v2/spaces/get_node?token=MaFpweI68iKNMvkTioLlJ1uJgQd` → lấy `space_id`
2. `wiki/v2/spaces/{space_id}/nodes?parent_node_token=MaFpweI68iKNMvkTioLlJ1uJgQd` → node con, lấy `obj_token`
3. `drive/v1/files/{obj_token}/download` → file HTML
4. Dữ liệu nằm trong biến JS `RAW` trong HTML: `{tables, edges, layout}`

Cần `user_access_token` (scope `wiki:wiki` + `drive:drive`) — `tenant_access_token` **không đọc được wiki**.

</details>

> Đây là nguồn đầu tiên cho tầng dữ liệu. KB trước đó dựng hoàn toàn từ UG nên không có gì về data model.

---

## 1. 🚨 Ba phát hiện ngoài phạm vi UG

### 1.1 Hệ thống là **multi-tenant**

Bảng `tenant` là gốc, `tenant_id` xuất hiện trên hầu hết bảng nghiệp vụ (`courses`, `classes`, `users`, `staffs`, `quizzes`, `resources`, `notifications`, `roles`, `groups`, `storyline`, `mail_logs`…).

```
tenant
├── id (PK)
├── type
├── billing_model
├── can_publish_marketplace
├── contract_type
├── name
└── subdomain
```

**UG không nhắc một chữ nào về tenant.** Toàn bộ UG viết như thể hệ thống phục vụ một tổ chức duy nhất (UpBase). `❓BA`

### 1.2 Có hạ tầng **marketplace / thương mại**

```
course_listing
├── id (PK)
├── tenant_id  → tenant
├── visibility
├── pricing_model
└── commission_rule_id
```

Cộng với `tenant.billing_model`, `tenant.can_publish_marketplace`, `tenant.contract_type`, và các nhóm API `Lessee Contacts Management` / `Lessee Tag Management` (*lessee* = bên thuê).

Mail template có biến `IS_PUBLIC_ENROLL` — khớp với khả năng học viên tự đăng ký khoá công khai.

`❓BA` — đây là tính năng đã có, đang tắt, hay chuẩn bị cho roadmap?

### 1.3 Xác thực & phân quyền dùng hạ tầng chuyên biệt

| Bằng chứng | Nghĩa |
|---|---|
| `users.keycloak_user_id` | Xác thực qua **Keycloak** (identity provider) |
| `users.lark_union_id` | Liên kết tài khoản **Lark** (khớp SSO trong UG) |
| `casbin_rule` (ptype, v0–v6) | Phân quyền dùng **Casbin** — engine RBAC/ABAC |
| `roles`, `role_staff_instances`, `groups`, `group_user_instances` | Mô hình role & group |

> **Đây là câu trả lời một phần cho câu hỏi "permission matrix ở đâu".** Quyền không nằm trong bảng tĩnh mà trong policy Casbin (`v0`–`v6` là các trường policy: subject, object, action…). Muốn có ma trận quyền thật thì phải đọc dữ liệu `casbin_rule`, không đọc được từ schema. API có `Roles Management` (8) và `Permissions management` (2).

---

## 2. Quan hệ lõi

```
tenant ─┬─► courses ──► classes ──► class_user_instances ──► quiz_attempts
        │      │            │
        │      │            └─► class_mentor_instances
        │      │            └─► class_lecture_instances
        │      │            └─► class_quiz_settings ──► class_user_quiz_settings
        │      │
        │      ├─► course_sections ─┬─► course_tab_documents
        │      │                    ├─► quizzes  [1-1]
        │      │                    └─► storyline
        │      ├─► course_categories
        │      └─► certificates
        │
        ├─► users ──► user_details [1-1]
        └─► staffs ─┬─► staff_details [1-1]
                    └─► departments
```

### Khoá ngoại của các bảng lõi

| Bảng | FK | Trỏ tới |
|---|---|---|
| `courses` | `tenant_id`, `course_category_id`, `certificate_id` | tenant, course_categories, certificates |
| `classes` | `tenant_id`, `course_id`, **`hybrid_class_id`** | tenant, courses, **classes (tự tham chiếu)** |
| `users` | `tenant_id`, `detail_id` [1-1], `university_program_id`, `english_level_id`, `keycloak_user_id`, `category_primary_id`, `lark_union_id` | — |
| `staffs` | `tenant_id`, `detail_id` [1-1], `department_id`, `course_category_id` | — |
| `quizzes` | `tenant_id`, `case_study_story_id`, `course_category_id` | — |
| `quiz_attempts` | `quiz_id`, `user_id`, `class_user_id` | quizzes, users, class_user_instances |
| `course_sections` | `tenant_id`, `quiz_id` [1-1], `storyline_id` | — |
| `resources` | `tenant_id`, `parent_id`, `origin_resource_id`, `created_by_staff_id`, `created_by_user_id` | — |
| `certificates` | `tenant_id`, `courseCategoryId` | — |

---

## 3. Những gì DB xác nhận / bổ sung cho KB

| Phát hiện | Ý nghĩa |
|---|---|
| **`classes.hybrid_class_id` → `classes`** | Lớp **tự tham chiếu** — đây chính là cơ chế liên kết **Lesson ↔ Foundation** mô tả ở [04-class.md](04-class.md). Tên cột là `hybrid`, không phải `foundation`. |
| **`course_categories` là FK của 6 bảng** | `courses`, `users.category_primary_id`, `staffs`, `quizzes`, `certificates`, `support-groups`. **Rộng hơn cả những gì KB đã ghi** — KB nói Category chi phối 3 luồng, thực tế là 6. |
| **`course_sections.quiz_id` là 1-1** | Section Test gắn 1-1 với Section. |
| **`resources.parent_id` + `resource_closure`** | Cấu trúc **cây thư mục** cho tài liệu (closure table). |
| **`resources.origin_resource_id`** | Theo dõi **nguồn gốc** khi tài liệu được tái sử dụng — khớp với "chọn từ kho tài nguyên hệ thống". |
| **`course_discussions_closure`** | Thảo luận cũng dùng closure table → **hỗ trợ reply lồng nhiều tầng**, không chỉ 1 tầng như UG mô tả. |
| **4 bảng grading** | `quiz_attempt_gradings`, `quiz_attempt_question_gradings`, `quiz_attempt_answer_gradings`, `topic_attempts` — chấm điểm ở 3 cấp: lần chấm → câu hỏi → từng đoạn câu trả lời. Khớp với cơ chế bôi đoạn để chấm. |
| **`class_user_quiz_settings`** | Cấu hình bài kiểm tra **theo từng học viên**, không chỉ theo lớp. |
| **`otps`** | Bảng OTP riêng — khớp mail #9. |
| **`mail_logs`, `notifications`, `notification_user_instances`, `notification_group_instances`** | Hạ tầng thông báo đầy đủ, khớp [09-notification-email.md](09-notification-email.md). |
| **`import_logs`, `import_log_detail_instances`** | Log import theo dòng — khớp View Log trong UG. |
| **`field_change_logs`** | **Audit trail** cấp field. UG không nhắc.<br>⚠️ **Đọc 05/10/2026: chỉ có 5 cột** — `tenant_id · id · object_type · object_id · created_by_staff_id`. **Không có tên trường, giá trị cũ, giá trị mới, thời điểm.** Đừng giả định nó ghi được nội dung thay đổi |
| **`class_user_instances.source_type`** | 🟢 **Lượt ghi danh đã có cột ghi nguồn gốc.** Cột đầy đủ: `id · user_id · class_id · status · started_at · finished_at · type · source_type · learning_progress`. Quan trọng cho mọi tính năng thêm một đường ghi danh mới *(đọc 05/10/2026)* |
| **`groups` chỉ có 3 cột** | `tenant_id · id · name`. Khớp `CreateGroupDto` trong Swagger — nhóm hiện tại **chỉ là tên cộng danh sách người**, không cấu trúc *(đọc 05/10/2026)* |
| **`batch_job_progress_logs`** | Theo dõi tiến độ job nền. |
| **`provinces`, `districts`, `wards`** | Địa giới hành chính VN → API `Address Management`. |
| **`users.university_program_id`, `english_level_id`** | Thuộc tính học viên UG không có. `english_level_id` **nhiều khả năng là "level đầu vào"** của SIS dashboard. |
| **`question_filters` [1-1], `question_topics`, `question_reports`** | Câu hỏi có filter riêng và chủ đề — khớp "chủ đề kiến thức" trong SIS dashboard. |
| **`caching_settings`** | Khớp API `Caching Manager` (11 endpoint). |

---

## 4. Bảng chưa ánh xạ được sang KB

| Bảng | Ghi chú |
|---|---|
| `course_listing` | Marketplace — §1.2 |
| `course_copy_content_logs` | Log copy nội dung khoá (BR-COPY-01/02) |
| `course_section_links` | Liên kết giữa section? |
| `course_outcomes` vs `course_learning_outcomes` vs `course_section_outcome_instances` | **Ba bảng outcome** — UG chỉ mô tả Learning Outcome ở cấp Section |
| `class_lecture_instances` | **Lecture** — khái niệm UG không có, liên quan `Schedules` |
| `class_user_scores` | Điểm tổng hợp theo học viên |
| `class_user_storyline_progress` | Tiến độ Storyline riêng |
| `departments` | **Cây phòng ban dựng bằng Nested Set** — `tree_id` · `left` · `right` · `code` · `short_name` · `type` · `description`. Chỉ `staffs.department_id` trỏ vào, **không phục vụ `users`** *(đọc 05/10/2026)* |
| `support-groups` | Comment Replier — **không có `tenant_id`** (khác mọi bảng khác) |
| `report_logs`, `quiz_reports` | Báo cáo |
| `attachment-files` | File đính kèm chung |
| `districts` / `provinces` / `wards` dùng `code` làm PK | Không theo chuẩn `id` như bảng khác |

---

## 5. Điểm cần BA xác nhận

| # | Câu hỏi |
|---|---|
| Q1 | 🚨 **Multi-tenant: hệ thống đang phục vụ bao nhiêu tenant? UpBase là một tenant hay là toàn bộ hệ?** |
| Q2 | 🚨 **Marketplace (`course_listing`, `billing_model`, `commission_rule_id`, Lessee) đã dùng chưa hay là roadmap?** |
| Q3 | **Keycloak** đóng vai trò gì bên cạnh SSO Lark — là IdP chính? |
| Q4 | Ma trận quyền nằm trong dữ liệu `casbin_rule` — xin **bản export policy** hoặc tài liệu mô tả role. |
| Q5 | `classes.hybrid_class_id` — đúng là link Lesson ↔ Foundation? Tên "hybrid" có nghĩa khác không? |
| Q6 | `class_lecture_instances` / **Lecture** là gì? Liên quan buổi học trong SIS dashboard? |
| Q7 | Ba bảng outcome khác nhau thế nào? |
| Q8 | `users.english_level_id` có phải "level đầu vào" IA/IIA/IB/IIB không? |
| Q9 | Tại sao `support-groups` không có `tenant_id`? Có chủ đích hay thiếu sót? |
| Q10 | Xin **schema đầy đủ** (có cột + kiểu dữ liệu), diagram này chỉ có khoá. |
