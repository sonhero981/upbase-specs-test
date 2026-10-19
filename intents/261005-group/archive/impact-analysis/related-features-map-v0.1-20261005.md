---
intent: 261005-group
artifact: related-features-map
version: 0.1
status: approved
approved: 2026-10-05
migrated-from: .claude/projects/Group/working/impact-analysis/related-features-map-20261005.md
---
# Related Features & Docs Map — Group

**Ngày:** 05/10/2026 · **Bước 5** — chốt phạm vi liên quan trước khi dựng Impact Matrix
**Input:** `docs/brd/brd-v0.1-20261005.md` · `project-context.md` · KB `04` `06` `09` `11` `12` `14` `15` `16`

> Bảng này để PO soát: **đủ chưa · có sót · dòng nào không liên quan.** Mọi `❓BA` phải chốt trước khi sang Bước 6, không để giả định trôi vào Impact Matrix.

---

## ✅ Hai nguồn đã đối chiếu lại — 05/10/2026

| Nguồn | Kết quả |
|---|---|
| **Swagger** `uplms-api.staging.upbase.asia/{lms\|ops}` | ✅ **Đã đọc lại.** Tên miền mới PO cung cấp. Ops **514 operation** · LMS **136**. KB `14` đã cập nhật |
| **DB schema** trên Lark *(`UpLnd DB Full.html`)* | ✅ **Không cần tải lại.** `obj_edit_time` của file = **23/09/2026 11:41**, đúng ngày KB `12` đối chiếu. File nguồn chưa đổi kể từ đó |

> ⚠️ Lưu ý về nguồn schema: file HTML trên Lark do người dựng thủ công. **File chưa đổi không bảo đảm DB thật chưa đổi** — chỉ bảo đảm KB `12` khớp với nguồn hiện có.

### Ba nhóm chức năng chết đã bị gỡ khỏi API

So với bản trích 23/09/2026, Ops giảm 41 operation và LMS giảm 17. Nguyên nhân chính:

| Nhóm | Cũ | Nay |
|---|---|---|
| `Examination` · `Event Test Management` · `Event Management` (Ops) | 19 | **0** |
| `Entrance Test` · `Auth` (LMS) | 6 | **0** |

PO đã xác nhận `Examination` và `Entrance Test` không có tính năng từ 23/09. Nay cả `Event Test Management` — nhóm treo `❓BA` suốt từ đó — **cũng biến mất**, nên câu hỏi tự đóng.

### 🆕 Một nhóm mới ảnh hưởng thẳng tới `O4`

`Report LMS` — 6 endpoint phía học viên, KB chưa từng ghi:

```
GET /report/{class_id}/overall · weekly · topic
GET /report/{class_id}/learning-result · mock-test-result · exam-prediction
```

> 🔴 **Mọi báo cáo đều lấy `class_id` làm khoá.** Không có chiều nào theo người, theo nhóm hay theo phòng ban. `O4` *(cộng dồn số liệu theo cơ cấu)* **không tận dụng được gì** ở đây — phải thêm một chiều mới.

---

## 1. Module và tính năng

| Hệ | Tính năng / Module | New / Existing | Nguồn | Ghi chú |
|---|---|---|---|---|
| Ops | ~~**Group Management**~~ | ❌ **Bỏ hẳn** | PO 05/10 · `BA-01` | Nhóm **phẳng**, chỉ CRUD và gán user. Không cha con, không nguồn, không quản lý. **Coi như chưa có gì** |
| Ops | ~~**Recipients List**~~ *(Nhóm người nhận Email)* | ❌ **Bỏ hẳn** | PO 05/10 · `BA-01` | Khi mở lại chức năng gửi thông báo từ Ops sẽ chọn người nhận thẳng từ chức năng Nhóm mới |
| Ops | **Department Management** | Existing · ❌ không chạy | KB `14` §2.3 · PO 05/10 | Cây phòng ban cho `staffs`. Không phải nền để mở rộng |
| Ops | **Class Management** | Existing | KB `04` · **45** operation | Đường gán nội dung hiện tại. Nhóm nối vào đây |
| Ops | **Foundation Class** *(lớp tự sinh)* | Existing | KB `04` §2 | 🔴 Gán qua nhóm vào lớp Lesson sẽ **lan sang Foundation**. Xem `BR-04` |
| Ops | **User Management — Student** | Existing | KB `06` §2 · 24 operation | Nguồn người cho nhóm |
| Ops | **Staff Management** | Existing | KB `06` §3 · 15 operation | Nguồn người **quản lý** và **mentor** |
| Ops | **Comment Replier** *(`support-groups`)* | Existing · 🟢 active | KB `09` §7 | 🔴 **Tiền lệ của luật đứng trong chính hệ này.** Xem §4 |
| Ops | **Roles & Permissions** *(Casbin)* | Existing | KB `12` §1.3 · 8 + 2 operation | Nơi phạm vi dữ liệu theo nhánh sẽ sống |
| Ops | **SIS Dashboard** | Existing | KB `11` · 12 operation | Báo cáo cộng dồn theo nhóm sẽ phải vào đây hoặc chỗ tương đương |
| Ops | **Notifications Management** | Existing · 🔴 `hidden` | KB `09` | Dùng nhóm làm nguồn người nhận khi mở lại |
| Ops | **Staff Position / Level / Facility** | Existing | KB `14` §2.3 — 6/2/5 operation | Thuộc tính nhân sự. Có thể là nguồn cho nhóm động, nếu làm |
| Ops | **Import logs** | Existing | KB `12` · 2 operation | Nền cho `US4` thêm thành viên theo lô |
| LMS | **Trang hồ sơ học viên** | Existing | KB `06` §6 | Chỗ hiện quản lý của mình — `US17` |
| LMS | **Gamification — `US16`** | New *(dự án khác)* | `.claude/projects/Gamification/` | Bộ lọc bảng xếp hạng theo nhóm, đang chờ chức năng này |
| Ngoài | **Lark — SSO + đồng bộ nhân sự** | Existing | KB `06` §8 | Nguồn cơ cấu tổ chức. 🔴 Phụ thuộc ngoài lớn nhất |

---

## 2. Dữ liệu và thực thể

> Bản chụp KB `12` ngày 23/09/2026. **Chỉ có khoá chính và khoá ngoại**, không có danh sách cột đầy đủ.

### Đã có

| Thực thể | Nguồn | Ghi chú |
|---|---|---|
| `groups` | KB `12` §1.3 | Có `tenant_id`. Đây là nhóm hiện tại, phẳng |
| `group_user_instances` | KB `12` §1.3 | Quan hệ người với nhóm |
| `notification_group_instances` | KB `12` §3 | Nhóm làm người nhận thông báo |
| `departments` *(`unit`, `tree_id`)* | KB `12` §4 | **Cây phòng ban đã tồn tại**, nhưng gắn `staffs`, không gắn `users` |
| `staffs.department_id` | KB `12` §2 | Nhân sự vận hành có phòng ban |
| **`users`** | KB `12` §2 | 🔴 **Không có `department_id`.** Học viên hiện chưa gắn cơ cấu — đây là khoảng trống chính |
| `users.lark_union_id` | KB `12` §1.3 | Mối nối sang Lark, nền cho đồng bộ cây |
| `users.keycloak_user_id` | KB `12` §1.3 | Danh tính |
| `classes` · `class_user_instances` | KB `12` §2 | Lượt ghi danh. Tiến độ treo ở đây, không treo vào nhóm |
| `classes.hybrid_class_id` | KB `12` §3 | Lesson ↔ Foundation |
| `casbin_rule` *(`v0`–`v6`)* | KB `12` §1.3 | Phân quyền. Ma trận quyền **không đọc được từ schema** |
| `field_change_logs` | KB `12` §3 | Audit trail cấp field. ❓`BA-05` — dùng được cho `US15` không |
| `import_logs` · `import_log_detail_instances` | KB `12` §3 | Log import theo dòng |
| `tenant` · `tenant_id` | KB `12` §1.1 | Hệ đa tenant. `groups` đã có `tenant_id` |

### Phải thêm

| Thực thể | Phục vụ |
|---|---|
| Quan hệ **cha con giữa nhóm** | `US1` · `US2` — cây nhiều cấp |
| **Nguồn của nhóm** *(đồng bộ HRM / tự tạo)* | `US5` |
| Quan hệ **người ↔ nhóm** nhiều-nhiều, có cấp | `US3` · `US4` — `group_user_instances` hiện có thể đã đủ hoặc chưa |
| Quan hệ **quản lý** và **mentor** với nhóm | `US9` · `US12` |
| Quan hệ **quản lý chỉ định đích danh** với người | `US11` |
| **Nhật ký thành viên theo thời điểm** | `US15` · `O5` |
| **Gán nội dung cho nhóm** *(luật đứng)* + công tắc tự ghi danh | `US7` · `US8` |
| **Trạng thái lưu trữ** của nhóm | `US14` |

---

## 3. API và tích hợp

| Nhóm API | Hệ | Số op | New / Existing | Ghi chú |
|---|---|---|---|---|
| `Group Management` | Ops | 9 | Existing | Mở rộng. PO chốt `OQ-16`: thiết kế như làm mới |
| `Department Management` | Ops | 9 | Existing · chết | Không dùng lại |
| `User Management` | Ops | 24 | Existing | Nguồn người |
| `Class Management` | Ops | 51 | Existing | Nơi luật đứng đổ vào |
| `Roles Management` · `Permissions management` | Ops | 8 · 2 | Existing | Phạm vi dữ liệu |
| `Notifications Management` | Ops | 5 | Existing | Người nhận theo nhóm |
| `Sis Dashboard` | Ops | 12 | Existing | Báo cáo theo nhóm |
| `Import logs` | Ops | 2 | Existing | `US4` |
| **Đồng bộ cơ cấu từ Lark** | — | — | **New** | Tầng 2 của mô hình HRIS. Tầng 1 *(người)* đã chạy |

---

## 4. 🔴 Comment Replier — tiền lệ của luật đứng, đã chạy trong hệ này

KB `09` §7 ghi hai quy tắc của Comment Replier:

> Thêm thành viên vào nhóm → **tự động thêm vào các lớp** có Danh mục gắn với nhóm *(mỗi khoá chỉ thêm vào **1 lớp duy nhất**)*; thời hạn học **gia hạn liên tục mỗi năm một lần**
>
> Xoá thành viên khỏi nhóm / xoá nhóm → thành viên **bị xoá khỏi các lớp** có khoá thuộc Category đã thêm

Đây đúng là cơ chế `US7` và `US8` sắp làm, chỉ khác nguồn gắn kết *(Category thay vì nội dung chọn tay)*. Ba thứ rút ra:

| Rút ra | Ảnh hưởng |
|---|---|
| **Một khoá có nhiều lớp thì chọn lớp nào** — Comment Replier chốt *"mỗi khoá chỉ thêm vào 1 lớp duy nhất"* | `US7` sẽ gặp đúng tình huống này. Chưa có câu trả lời nào trong BRD |
| **Rời nhóm thì bị gỡ khỏi lớp** — hệ này đã chọn hướng đó một lần rồi | Là dữ liệu đầu vào trực tiếp cho `OQ-22`, cùng hướng với Moodle |
| **Thời hạn học phải xử lý** — Comment Replier gia hạn mỗi năm một lần | `US7` chưa nói gì về thời hạn khi vào lớp qua nhóm |

> KB `15` §6 xếp cơ chế này là **chỗ đóng cứng UpBase mức 🟠**: *"quy trình vận hành UpBase nhúng vào code"*. Làm `US7`·`US8` theo cùng kiểu sẽ **thêm một chỗ đóng cứng nữa**.

---

## 5. Business rule hiện có bị chạm

| ID | Rule | Chạm thế nào |
|---|---|---|
| `KB-USER-01` | Tài khoản học viên **đồng bộ tự động** từ hệ nhân sự, không tạo thủ công | Nhóm đồng bộ phải theo cùng nguyên tắc: hệ gốc là Lark |
| `KB-USER-03` | Nhân sự bị xoá ở hệ tổ chức → tài khoản **tự chuyển `Block`** | 🟢 **Một phần của `OQ-23` đã có sẵn cơ chế.** Còn lại: người `Block` có bị gỡ khỏi nhóm không, có còn trong báo cáo không |
| `KB-USER-TA-01` | **`Test Account` bị bỏ qua ở mọi logic nghiệp vụ** | ✅ `BA-02` — PO chốt 05/10: **loại khỏi mọi báo cáo và mọi logic** của chức năng Nhóm |
| `KB-CLASS-01` | Thêm học viên vào lớp Lesson → **cũng thêm vào lớp Foundation** gắn kèm | 🔴 Gán một nhóm 55 người vào lớp Lesson sẽ kéo cả 55 vào Foundation |
| `KB-CLASS-02` | Thao tác ở Foundation **không tác động ngược** lên Lesson | Chiều ngược của luật đứng phải tính |
| `KB-CLASS-03` | `Duration = Flexible` + chưa Activate → không cập nhật được thời hạn | Người vào nhóm sau 6 tháng vẫn nhận đủ N ngày. Đúng hay không là câu nghiệp vụ |
| `KB-CLASS-05` | **Lớp `Ended` không chỉnh sửa được** | 🔴 Luật đứng gặp lớp đã `Ended` thì xử lý thế nào — chưa ai trả lời |
| — | **Lớp có `Số học viên tối đa`** | KB `04` §4. Nhóm đông hơn sức chứa lớp thì xử lý thế nào |
| `KB-SIS-01` | Filter **Course** và **Class code** bắt buộc ở mọi dashboard | Báo cáo theo nhóm sẽ phải thêm một chiều lọc mới |
| `KB-USER-07` | Một Staff gán được **nhiều Role cùng lúc** | Người quản lý có thể mang nhiều vai, phạm vi dữ liệu phải hợp lại |

---

## 6. NFR và chiều tenant

Đối chiếu KB `15` §6 — *"thay đổi này có làm tăng chỗ đóng cứng cho UpBase không"*:

| Chỗ đóng cứng | Mức sẵn có | Dự án này làm gì |
|---|---|---|
| **Đồng bộ tài khoản từ HRIS UpBase một chiều** | 🔴 Cao — *"mỗi tenant một HRIS"* | ⚠️ **Tăng thêm.** Giờ đồng bộ cả cơ cấu, không chỉ người. Tenant khác dùng HRIS khác thì phải làm lại tầng này |
| **SSO Lark là đường đăng nhập học viên** | 🟠 | Không đổi |
| **Comment Replier tự thêm xoá học viên vào lớp** | 🟠 | ⚠️ **Thêm một chỗ cùng kiểu**, nếu `US7`·`US8` làm theo cùng cách |
| `support-groups` không có `tenant_id` | 🔴 | Không chạm. Nhưng `groups` **có** `tenant_id`, nên nhóm mới không lặp lại lỗi này |

Hai NFR cần trả lời ở Impact Matrix:

| | Câu |
|---|---|
| Khối lượng | Cây 53 phòng ban, 384 người, truy vấn *cha bao trùm toàn nhánh* chạy ở mọi màn đọc dữ liệu |
| Nhịp đồng bộ | Cơ cấu đổi vài lần một năm. Nghỉ việc thì khác — người đã rời mà vẫn nhận nội dung mới là vấn đề thật |

---

## 7. ✅ PO đã chốt — 05/10/2026

| # | Câu | Quyết định |
|---|---|---|
| ~~`BA-01`~~ | `Group Management` và `Recipients List` đang chạy hay đang ẩn | **Bỏ hẳn cả hai, coi như chưa có gì.** Sau này mở lại chức năng gửi thông báo từ Ops thì chọn người nhận thẳng từ chức năng Nhóm mới |
| ~~`BA-02`~~ | `Test Account` có vào nhóm không | **Loại khỏi mọi báo cáo và mọi logic.** Giữ đúng `KB-USER-TA-01` |
| ~~`BA-03`~~ | Luật đứng gặp lớp `Ended` thì làm gì | **Theo luật của Lớp.** Lớp không cho thêm thì nhóm cũng không thêm được. Không có ngoại lệ riêng cho đường đi qua nhóm |
| ~~`BA-04`~~ | Một khoá nhiều lớp thì gán vào lớp nào | **Vào đúng lớp đã gắn với nhóm.** Hệ thống không tự đi tìm lớp theo khoá — khác cách Comment Replier làm |
| ~~`BA-07`~~ | Nhóm đông hơn sức chứa lớp | **Chỉ cảnh báo, vẫn thêm được bình thường.** Đây là hành vi hiện có của lớp, nhóm theo luôn |

### Còn hai câu chưa chốt

| # | Câu | Vì sao cần |
|---|---|---|
| **`BA-05`** | **`US15` cần một nhật ký riêng, hay `field_change_logs` đã đủ?** | Quyết định `US15` là việc mới hay là việc đọc lại dữ liệu đã có. Không chặn Impact Matrix, nhưng chặn PRD |
| **`BA-06`** | **Người `Block` do nghỉ việc còn trong nhóm không, còn trong báo cáo không?** `KB-USER-03` đã tự Block, nhưng không nói gì về nhóm | Một phần của `OQ-23`. Chạm `US16` và mọi báo cáo theo nhóm |

### Hệ quả của `BA-03` và `BA-04` — gọn hơn tưởng

Hai quyết định này **cắt bỏ phần lớn độ phức tạp** mà §4 cảnh báo:

| Điều từng lo | Nay |
|---|---|
| Luật đứng phải tự chọn lớp trong số nhiều lớp của một khoá | ❌ Không còn. Người gán chọn lớp cụ thể |
| Luật đứng phải có bộ luật riêng khi gặp lớp `Ended`, lớp đầy, lớp chưa mở | ❌ Không còn. Dùng chung luật của Lớp |
| Comment Replier là khuôn mẫu phải theo | ❌ Không theo. Chỉ còn là tiền lệ tham khảo cho `OQ-22` *(rời nhóm thì gỡ khỏi lớp)* |

> Vẫn còn nguyên: **`KB-CLASS-01`** — gán nhóm vào lớp Lesson sẽ kéo cả nhóm vào lớp Foundation gắn kèm. Quyết định *"theo luật của Lớp"* không gỡ được chuyện này, vì đó đúng là luật của Lớp.

---

## 8. Dòng cố ý KHÔNG đưa vào phạm vi

| Không xét | Vì sao |
|---|---|
| `Schedules` · `Class Schedule` · `Room Management` *(45+ operation)* | Mảng lịch dạy. Nhóm không chạm buổi học hay phòng học |
| `Examination` · `Entrance Test` | KB `14` §2.2 — PO xác nhận **không có tính năng** |
| `Course Listing` · `Lessee` *(marketplace)* | KB `12` §1.2 — `❓BA` từ 23/09, chưa ai xác nhận đang dùng |
| `Storyline` · `Question Bank` · `Grading` | Không chạm. Nhóm dừng ở mức *ai vào lớp nào* |
| Cấu trúc bảng, chỉ mục, cách lưu cây | PO chốt 05/10: **không làm technical design**. Dev tự phân tích |
