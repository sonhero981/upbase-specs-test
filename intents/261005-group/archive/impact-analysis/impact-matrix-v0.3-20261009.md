---
intent: 261005-group
artifact: impact-matrix
version: 0.3
status: approved
approved: 2026-10-09 (v0.3); 2026-10-06 (v0.2)
cr: CR1 ngày 2026-10-09, vùng 9 và BI-6
gate: v1 Gate 2
migrated-from: .claude/projects/Group/working/impact-analysis/impact-matrix-v0.2-20261006.md
---
# Impact Matrix — Group

| | |
| --- | --- |
| **Project** | Group |
| **Version** | **v0.3** — 09/10/2026, CR1. v0.2 ngày 06/10/2026 |
| **Ngày** | Dựng 05/10/2026 · duyệt Gate 2 ngày 06/10/2026 |
| **Nguồn input** | `brd-v0.1-20261005.md` · `related-features-map-20261005.md` · KB `04` `05` `06` `09` `11` `12` `13` `14` `15` `16` · **Swagger đọc 05/10/2026** · **schema Lark tải và đọc 05/10/2026** |
| **Trạng thái** | ✅ **Approved — Gate 2, 06/10/2026.** 6/6 conflict đã quyết |
| **Cập nhật** | 09/10/2026 — CR1: thêm `MAIL-GRP-02` vào vùng 9 và `BI-6`. Trước đó 06/10/2026 ghi quyết định Gate 2 |

> Bản phân tích **nội bộ**, không phải mục trong PRD. Kết quả chảy vào PRD ở `Solution` · `Out of scope` · `Acceptance criteria`.

---

## 1. Summary

Chức năng Nhóm không tự nó phức tạp — nó **chỉ chứa người**. Độ khó nằm ở chỗ nó nối vào Lớp bằng một luật đứng, và Lớp là module đông đặc nhất hệ *(45 operation ở Ops)* với một cơ chế tự sinh lớp Foundation.

> ✅ **Gate 2 đã duyệt 06/10/2026.** Cả **6 conflict** đã có quyết định, **4 FR bổ sung** đóng vì PO xác nhận là hành vi bình thường, **7 Open Question** đóng. Ba chỗ từng đánh giá là nguy hiểm nhất đều được giải — không phải bằng cách làm thêm, mà bằng cách xác nhận hệ thống đã xử lý chúng theo cách chấp nhận được.

Ba chỗ từng đánh giá nguy hiểm nhất:

| | Chỗ | Vì sao |
|---|---|---|
| 1 | ~~Mail #11 đang bật~~ | ✅ **Đã giải 06/10** — PO chốt gửi bình thường, giống thêm hàng loạt học viên vào lớp |
| 2 | ~~Lớp Foundation tự sinh~~ | ✅ **Đã giải 06/10** — PO chốt là hành vi bình thường, không cần cảnh báo riêng |
| 3 | ~~`KB-SIS-01` chặn báo cáo theo nhóm~~ | ✅ **Đã giải 06/10** — PO chốt bộ lọc làm **động**, lọc theo gì cũng được, đặt trong dashboard hiện có |

| | Số lượng |
| --- | --- |
| Vùng bị ảnh hưởng (High / Medium / Low) | **7 / 5 / 0** |
| Conflict cần escalate | **6** |
| FR/NFR bổ sung phát hiện được | **11** |
| Coverage gap | **15** |
| Chỗ đóng cứng tenant tăng thêm | **2** |

### Bốn thứ schema thật nói mà bản chép không nói

Đọc lại `UpLnd DB Full.html` từ Lark ngày 05/10 *(85 bảng · 173 quan hệ, khớp KB `12` về số)*:

| Phát hiện | Nghĩa |
|---|---|
| 🟢 `class_user_instances` **đã có cột `source_type`** | Hệ thống sẵn phân biệt được lượt ghi danh đến từ đâu. `C2` không phải dựng từ con số không |
| 🟢 `departments` **đã dựng cây bằng Nested Set** — có `tree_id`, `left`, `right`, `code`, `short_name` | Hệ này đã làm cây một lần rồi. Chỉ là cây đó gắn `staffs`, không gắn `users` |
| 🔴 `field_change_logs` **chỉ có 5 cột**: `tenant_id · id · object_type · object_id · created_by_staff_id` | **Không có tên trường, giá trị cũ, giá trị mới, thời điểm.** Xác nhận `BA-05` bằng dữ liệu: không dùng được cho nhật ký thành viên |
| 🔴 `class_user_instances` **có 6 bảng treo vào** | `OQ-22` *(rời nhóm thì lượt ghi danh xử lý sao)* chạm 6 bảng dữ liệu học, không chỉ một dòng |

---

## 2. Current Situation — Dependency Map *(STEP 1)*

| Loại | Mục | Nguồn | Ghi chú |
| --- | --- | --- | --- |
| Module | **Class Management** | KB `04` · 45 op | Đường gán nội dung duy nhất hiện có |
| Module | **Foundation Class** — lớp tự sinh | KB `04` §2 | Đồng bộ **một chiều** Lesson → Foundation |
| Module | **User Management — Student** | KB `06` §2 · 22 op | Nguồn người cho nhóm |
| Module | **Staff Management** | KB `06` §3 · 10 op | Nguồn người quản lý và mentor |
| Module | **Comment Replier** | KB `09` §7 · 9 op | 🔴 Đã có một luật đứng đang chạy |
| Module | **SIS Dashboard** | KB `11` · 10 op | Báo cáo vận hành |
| Module | ~~Group Management~~ | PO 05/10 | ❌ Bỏ hẳn. `CreateGroupDto` chỉ có `name` + `users` |
| Module | ~~Recipients List~~ | PO 05/10 | ❌ Bỏ hẳn |
| Data | `class_user_instances` | **Schema Lark, đọc 05/10** | `id · user_id · class_id · status · started_at · finished_at · type · **source_type** · learning_progress`.<br>🟢 **Đã có cột `source_type`** — hệ thống sẵn phân biệt được lượt ghi danh đến từ đâu.<br>🔴 **6 bảng khác treo vào đây**: `class_user_scores` · `quiz_attempts` · `user_course_section_progress` · `class_user_storyline_progress` · `class_user_quiz_settings` · `course_section_notes` |
| Data | `classes.hybrid_class_id` | KB `12` §3 | Lesson ↔ Foundation. 7 bảng trỏ về `classes` |
| Data | `users` | **Schema Lark** | `tenant_id · id · detail_id · username · password · keycloak_user_id · category_primary_id · lark_union_id · type · status · is_operator`.<br>🔴 **Không có `department_id`** — học viên chưa gắn cơ cấu nào.<br>🔴 **15 bảng giữ khoá ngoại trỏ về `users`** — shared entity lớn nhất hệ |
| Data | `departments` | **Schema Lark** | `tenant_id · id · description · tree_id · **left** · **right** · name · short_name · code · type`.<br>🟢 **Cây đã dựng sẵn bằng Nested Set** *(`left`/`right`)*, có cả `code` và `short_name`.<br>⚠️ Nhưng **chỉ `staffs.department_id` trỏ vào** — không phục vụ học viên |
| Data | `groups` · `group_user_instances` | **Schema Lark** | `groups`: **đúng 3 cột** — `tenant_id · id · name`.<br>`group_user_instances`: `id · group_id · user_id`.<br>Khớp `CreateGroupDto`. Xác nhận bằng dữ liệu: **không có gì để kế thừa** |
| Data | `casbin_rule` | **Schema Lark** | `tenant_id · id · ptype · v0…v6`. Ma trận quyền nằm trong **dữ liệu**, không đọc được từ cấu trúc |
| Data | `field_change_logs` | **Schema Lark** | `tenant_id · id · object_type · object_id · created_by_staff_id`.<br>🔴 **Không có tên trường, giá trị cũ, giá trị mới, thời điểm.** Xác nhận `BA-05`: **không dùng được** cho nhật ký thành viên |
| Data | `roles.is_group` | **Schema Lark** | Có khái niệm role dạng nhóm. `❓BA` — liên quan gì tới chức năng Nhóm không |
| Data | `support_groups_user_instances` | **Schema Lark** | Comment Replier có bảng nối riêng, không dùng chung `group_user_instances` |
| Business Rule | `KB-CLASS-01` | KB `04` §9 | Thêm học viên vào Lesson → **cũng thêm vào Foundation** |
| Business Rule | `KB-CLASS-05` | KB `04` §9 | Lớp `Ended` không chỉnh sửa được |
| Business Rule | `KB-CLASS-03` | KB `04` §9 | `Flexible` + chưa Activate → không set thời hạn |
| Business Rule | `KB-USER-01` · `KB-USER-02` | KB `06` §7 | Học viên đồng bộ tự động, không sửa được trừ Username |
| Business Rule | `KB-USER-03` | KB `06` §7 | Nghỉ việc → **tự chuyển `Block`** |
| Business Rule | `KB-USER-TA-01` | KB `06` §8b | **`Test Account` bị bỏ qua ở mọi logic nghiệp vụ** |
| Business Rule | `KB-SIS-01` | KB `11` §3 | 🔴 Filter **Course** và **Class code** *bắt buộc* ở mọi dashboard |
| Business Rule | `KB-USER-07` | KB `06` §7 | Một Staff mang **nhiều Role** cùng lúc |
| Process | ~~Chuyển học viên giữa lớp~~ | Swagger `PUT /classes/{id}/students/transfer` · `revert-transfer` | ❌ **PO chốt 06/10: endpoint có, tính năng KHÔNG có.** Chuyển lớp hiện là xoá khỏi lớp cũ, thêm lớp mới, **học lại từ đầu** |
| Process | **Xoá học viên khỏi lớp** | KB `04` Q4 · PO 06/10 | 🔴 **Mất tiến độ thật.** Đây là cách vận hành đang dùng để chuyển lớp |
| Permission | Casbin RBAC/ABAC | KB `12` §1.3 · KB `06` Q1 | Ma trận quyền là **khoảng trống lớn nhất của KB** |
| Integration | **Lark — SSO + đồng bộ nhân sự** | KB `06` §8 | 🔴 Phụ thuộc ngoài lớn nhất |
| **Mail event** | **#11 Chào mừng vào khoá học** | KB `13` — Cronjob + OPS | 🟢 **Đang bật** |
| **Mail event** | #12 Khoá học đã hết hạn | KB `13` | 🟢 Đang bật |
| **Mail event** | #23 #24 #25 #26 — Foundation | KB `13` | 🟢 Đang bật |
| **Mail event** | #17–#20, #32–#35 — chấm điểm | KB `13` | 🔴 **Đang tắt có chủ đích** |
| **Tính năng ẩn** | Notification & Email List · Recipients List · Mail Logs | KB `00-index` · KB `09` | `hidden` — vẫn có code |
| **Tính năng ẩn** | Storyline · Quản lý bài kiểm tra trong lớp | KB `00-index` | Không chạm |

---

## 3. Desired Situation *(STEP 2)*

Từ BRD `v0.1`: **20 User Story**, 5 mục tiêu, 3 ràng buộc bất biến.

| Thành phần mới | Nội dung |
|---|---|
| **Nhóm nhiều cấp** | Tối đa 6 cấp, nhiều cây gốc song song, phân loại theo nguồn *(đồng bộ HRM / tự tạo)* |
| **Luật đứng** | Gán nội dung cho nhóm → người trong nhóm vào lớp. Người gia nhập sau vẫn tự nhận nếu công tắc bật |
| **Quan hệ quản lý và mentor** | Gán cho nhóm · suy ra theo cây · chỉ định đích danh trên hồ sơ |
| **Phạm vi dữ liệu theo nhánh** | Quản lý chỉ xem được người trong nhánh mình phụ trách |
| **Thành viên theo thời gian** | Nền của báo cáo, không chỉ để tra tay |
| **Báo cáo cộng dồn theo nhóm** | Xem được ở hiện tại hoặc tại một mốc quá khứ |

Ba ràng buộc bất biến: `C1` nhóm chỉ chứa người · `C2` một lượt ghi danh · `C3` thành viên lưu kèm thời điểm.

---

## 4. Impact Matrix — 12 vùng *(STEP 3.0)*

| # | Vùng | Ảnh hưởng | Mô tả | Severity | Nguồn |
| --- | --- | --- | --- | --- | --- |
| 1 | **Business process** | ✅ | Thêm một **đường giao bài thứ hai** song song với đường hiện tại *(chọn tay từng người vào lớp)*. Hai đường phải không sinh ghi danh trùng | 🔴 **High** | BRD `C2` |
| 2 | **Module / function** | ✅ | Class · User · Permission · Reporting đều phải nhận thêm khái niệm Nhóm. Class chịu nhiều nhất | 🔴 **High** | KB `04` `06` |
| 3 | **Screen / report** | ✅ | Màn nhóm *(cây + bảng)*, màn thành viên, màn gán nội dung, màn quản lý, màn báo cáo theo nhóm, màn tra nhật ký. Phía LMS: khối quản lý trên hồ sơ học viên | 🔴 **High** | BRD §7 |
| 4 | **Data** | ✅ | `users` **chưa có bất kỳ quan hệ cơ cấu nào**. Phải thêm: quan hệ cha con giữa nhóm · nguồn nhóm · quan hệ quản lý và mentor · **thành viên kèm thời điểm** · trạng thái lưu trữ | 🔴 **High** | KB `12` §2 |
| 5 | **API** | ✅ | `Group Management` hiện có **9 endpoint nhưng `CreateGroupDto` chỉ gồm `name` + `users`**. Không kế thừa được gì. Thêm nhóm endpoint gán nội dung và báo cáo | 🟡 Medium | Swagger 05/10 |
| 6 | **Role / permission** | ✅ | Phạm vi dữ liệu theo nhánh là **chiều mới** trong Casbin. Chưa ai đọc được ma trận quyền hiện tại — KB `06` Q1 treo từ 23/09 | 🔴 **High** | KB `12` §1.3 |
| 7 | **Business rule** | ✅ | 8 rule hiện có bị chạm. Nặng nhất: `KB-CLASS-01` *(Foundation)*, `KB-SIS-01` *(filter bắt buộc)*, `KB-USER-TA-01` *(`Test Account`)* | 🔴 **High** | §5 · §6 |
| 8 | **NFR** | ✅ | Truy vấn *cha bao trùm toàn nhánh* chạy ở **mọi màn đọc dữ liệu**, không chỉ màn nhóm. Thêm lớp thành viên theo thời gian vào đường đọc của mọi báo cáo | 🟡 Medium | BRD `C3` |
| 9 | **Notification / Email** | ✅ | 🔴 **Mail #11 đang bật.** Gán nhóm vào lớp → mỗi người một mail *"Chào mừng vào khoá học"*. Lớp Lesson có Foundation thì thêm mail #23–#26 về sau. Mail #12 *(hết hạn)* cũng nhân theo số người.<br>**CR1 09/10/2026:** dự án thêm **hai** mail event mới, không phải một: `MAIL-GRP-01` *(người rời nhóm còn nghĩa vụ học, `US20`)* và `MAIL-GRP-02` *(được gán quản lý hoặc nhận chuyển phụ trách, `US9` `US13`)*. Cả hai gửi cho nhân sự vận hành, số lượng nhỏ, không phải mail hàng loạt | 🔴 **High** | KB `13` · CR1 |
| 10 | **Reporting** | ✅ | `Report LMS` *(6 endpoint)* và `Sis Dashboard` *(10)* **đều lấy `class_id` làm khoá**. Không có chiều nào theo người hay theo nhóm. `US18` không tận dụng được gì | 🔴 **High** | Swagger · KB `11` |
| 11 | **Test** | ✅ | Vùng phải test lại: thêm gỡ học viên khỏi lớp · lớp Foundation · mail #11 #12 #23–26 · mọi dashboard · phân quyền · đồng bộ Lark · Comment Replier | 🟡 Medium | — |
| 12 | **Release** | ✅ | Đồng bộ lần đầu chạm **384 người × 53 phòng ban** cùng lúc. Phải tách khỏi lần bật luật đứng, nếu không là một đợt mail hàng loạt | 🟡 Medium | §8 |

### Vùng xét mà **không** bị ảnh hưởng

| Vùng | Lý do |
|---|---|
| Course · Section · Learning Outcome | Nhóm không chạm nội dung. Nguyên tắc 6 — `C1` |
| Question Bank · Quiz · Test | Nhóm dừng ở mức *ai vào lớp nào*, không chạm bài kiểm tra |
| Grading | Mentor của lớp lấy từ Staff, không lấy từ nhóm. Quan hệ mentor của nhóm là **khái niệm khác** |
| Certificate | Cấp theo lượt ghi danh, không theo nhóm |
| Storyline | `hidden`, không liên quan |
| `Schedules` · `Room` · `Class Schedule` | ⚠️ `❓BA` — nằm trong **vùng KB chưa phủ** *(KB `14` §2.1, 45+ operation)*. Không kết luận "không ảnh hưởng", chỉ ghi là **chưa tra được** |

---

## 5. Conflict Analysis *(STEP 3a)*

> Escalate, **không tự giải**.

| # | Chiều | Conflict | Trạng thái |
| --- | --- | --- | --- |
| ~~`CF-1`~~ | Business rule | Dashboard bắt buộc lọc theo `Course` + `Class code`, `US18` không có hai thứ đó | ✅ **PO chốt 06/10: bộ lọc làm ĐỘNG**, lọc theo gì cũng được, đặt trong dashboard hiện có |
| ~~`CF-2`~~ | Process | Hai luật đứng cùng tác động một lớp — Comment Replier và Nhóm | ✅ **PO chốt 06/10: tách tài khoản theo vai trò.** Xem phân tích dưới |
| ~~`CF-3`~~ | Data | Nhóm đồng bộ có cho sửa tay không | ✅ **PO chốt 06/10: KHÔNG cho sửa.** Thêm gỡ thủ công chỉ áp cho nhóm tự tạo |
| ~~`CF-4`~~ | Data | **Người nghỉ việc: gỡ khỏi nhóm hay giữ lại** | ✅ **PO chốt 06/10: gỡ khỏi nhóm, lượt ghi danh ĐÁNH DẤU kết thúc chứ không xoá** *(`OQ-36`)*. Thay thế `BA-06` ngày 05/10 |
| ~~`CF-5`~~ | Permission | Một người mang nhiều Role thì phạm vi dữ liệu hợp lại thế nào | ✅ **PO chốt 06/10: TÁCH THEO MÀN.** Mỗi màn khai rõ đọc theo phạm vi nào |
| ~~`CF-6`~~ | Business rule | Từ "Mentor" trùng tên khác nghĩa | ✅ **PO chốt 06/10: không phải hai khái niệm.** Mentor của nhóm chính là mentor của lớp. Sinh ra một FR mới — xem dưới |

### `CF-2` — tách tài khoản theo vai trò

PO chốt 06/10: một người trong tổ chức có thể đồng thời đóng ba vai, và **mỗi vai một tài khoản riêng**:

| Vai | Tài khoản |
|---|---|
| Học viên thật | Tài khoản đồng bộ từ HRM |
| Kiểm thử nội dung | Tài khoản `Test Account` riêng |
| Trả lời bình luận | Tài khoản Comment Replier riêng |

Xung đột tự giải: `KB-CR-01` bắt Comment Replier **phải là `Test Account = Yes`**, mà `BA-02` đã chốt **loại `Test Account` khỏi mọi logic nhóm**. Nên tài khoản Comment Replier không bao giờ vào nhóm, và hai luật đứng không gặp nhau.

> ⚠️ **Một câu nảy ra:** tài khoản `Test Account` và Comment Replier **không phải nhân sự**, nên không có trong cây tổ chức Lark. `KB-USER-01` lại nói học viên **không tạo thủ công được**. Hai tài khoản này tạo bằng cách nào → `OQ-34`.

### `CF-4` — PO đảo quyết định hai lần, còn một chỗ chưa khép

| | `BA-06` *(05/10)* | `CF-4` *(06/10)* |
|---|---|---|
| Quan hệ với nhóm | **Giữ**, đánh dấu, lọc ở nơi dùng | **Gỡ** theo đồng bộ |
| Lượt ghi danh | Giữ nguyên | **Mất** |
| Báo cáo quá khứ | Tính theo trạng thái tại mốc | *"Chỉ ghi nhận những thứ thuộc báo cáo trong quá khứ"* |

Bản 06/10 thay thế bản 05/10.

#### 🔴 Chỗ chưa khép: "mất lượt ghi danh" và "báo cáo quá khứ vẫn đúng" không tự đi với nhau

Báo cáo trong hệ này **được tính ra từ dữ liệu**, không được lưu sẵn ở đâu. Xoá lượt ghi danh là xoá chính thứ mà báo cáo đọc.

> Quý 3 chốt: *"Fulfillment HCM — 48/55 hoàn thành khoá An toàn lao động"*.
> Tháng 10, bảy người nghỉ việc, lượt ghi danh của họ mất.
> Mở lại báo cáo quý 3 → hệ thống tính lại từ dữ liệu còn lại → ra **41/48**, không phải 48/55.

Muốn giữ đúng con số cũ thì phải có **một trong hai** thứ, và hiện chưa có thứ nào:

| | Cách | Phải thêm gì |
|---|---|---|
| **a** | **Chốt số liệu định kỳ** — mỗi kỳ lưu lại một bản báo cáo đông cứng | Cơ chế snapshot báo cáo. **Một tính năng riêng, BRD chưa có** |
| **b** ✅ | **Không xoá, chỉ đánh dấu lượt ghi danh là đã kết thúc do nghỉ việc.** Báo cáo hiện tại loại ra, báo cáo quá khứ vẫn tính | Một giá trị trạng thái. `class_user_instances` **đã có cột `status`** |

> ✅ **PO chốt 06/10: cách b.**

**Lý do chọn b.** Ba lý do:

| | |
|---|---|
| 1 | **Rẻ hơn hẳn.** `class_user_instances.status` đã tồn tại. Cách a là dựng một tính năng mới |
| 2 | **Nhất quán với cách hệ này đối xử với tài khoản.** Nghỉ việc không xoá tài khoản mà chuyển `Block` *(`KB-USER-03`)* |
| 3 | **Không mồ côi dữ liệu.** 6 bảng treo vào `class_user_instances`: điểm · lượt làm bài · tiến độ section · tiến độ storyline · cấu hình quiz · ghi chú. Xoá dòng cha thì chúng xử lý ra sao là câu chưa ai trả lời |

> Cách b vẫn đạt đúng điều PO muốn: **người đã nghỉ không còn xuất hiện ở bất kỳ báo cáo hiện tại nào**, không còn nhận nội dung mới, không còn trong danh sách nhóm. Khác biệt duy nhất là dữ liệu không bị xoá khỏi đĩa.

→ `OQ-36`.

#### Còn một dây chuyền phải chặn

`OQ-22` hỏi *"một người rời nhóm thì nghĩa vụ học đã nhận xử lý thế nào"*. Nếu `OQ-22` chọn **gỡ khỏi lớp**, thì **mọi** người rời nhóm — kể cả chuyển phòng ban, kể cả bị gỡ nhầm — đều mất lượt ghi danh, không riêng người nghỉ việc.

`OQ-22` phải phân biệt được **lý do rời nhóm**, không áp một luật cho mọi trường hợp. Chốt ở Bước 7.

### `CF-6` — PO giải bằng cách khác, nhưng sinh ra một FR mới

PO chốt 06/10: **không phải hai khái niệm.** Mentor của nhóm chính là mentor sẽ gán vào lớp. Thêm nhóm vào lớp thì mentor của nhóm thành mentor trong lớp, **phụ trách đúng nhóm đó**.

Cách này gọn hơn đổi tên. Nhưng hệ thống hiện chưa làm được:

| | Hiện tại | Cần |
|---|---|---|
| `class_mentor_instances` | `id · class_id · mentor_id · **is_main_mentor** · **mentor_type**` | Thêm chiều: mentor này phụ trách **nhóm nào** trong lớp |
| Phạm vi chấm bài | Mentor gắn với **cả lớp** | Mentor chỉ chấm bài của **nhóm mình** |
| `BR-MENTOR-01` | Một `Main Responsible` cho cả lớp, review cuối | ✅ **PO chốt 06/10: mentor đầu tiên được thêm vào lớp là `Main Responsible`**, đổi lại được sau |

🟢 Hệ đã có sẵn `mentor_type` và `is_main_mentor` — không phải dựng từ con số không.

### `CF-1` — chi tiết, vì đây là chỗ không viết lại yêu cầu mà gỡ được

`KB-SIS-01` không phải gợi ý giao diện mà là **ràng buộc dữ liệu**: mọi dashboard hiện có đều truy vấn từ một lớp cụ thể. `Report LMS` xác nhận lại điều này — cả 6 endpoint đều có dạng `/report/{class_id}/...`.

`US18` hỏi một câu khác hẳn: *"phòng Fulfillment HCM học hành thế nào"* — câu này cắt ngang nhiều lớp, nhiều khoá.

| Hướng | Đánh đổi |
|---|---|
| Báo cáo theo nhóm là **một màn riêng**, không đụng dashboard hiện có | Hai nơi xem số liệu, người dùng phải biết vào đâu |
| **Nới `KB-SIS-01`** để dashboard hiện có nhận thêm chiều nhóm | Đụng vào 10 endpoint đang chạy |

Không tự chọn. Để Bước 7 so sánh.

---

## 6. Bidirectional Impact — FR/NFR còn thiếu *(STEP 3b)*

### New → Old

| # | Phát hiện | FR/NFR bổ sung | Feed ngược BRD? |
| --- | --- | --- | --- |
| ~~`BI-1`~~ | Gán nhóm vào lớp Lesson kéo cả nhóm vào Foundation. Nhóm 55 người thành 110 lượt ghi danh | ✅ **PO chốt 06/10: bình thường**, giống thêm hàng loạt học viên vào lớp có Foundation. Không cần cảnh báo riêng | ❌ Không |
| ~~`BI-2`~~ | Mail #11 bắn hàng loạt khi gán nhóm | ✅ **PO chốt 06/10: bình thường.** Không gộp, không hoãn, không tắt | ❌ Không |
| ~~`BI-3`~~ | Mail #12 *(hết hạn khoá)* nhân theo số người | ✅ Cùng `BI-2` | ❌ Không |
| ~~`BI-4`~~ | Mọi dashboard phải thêm chiều lọc theo nhóm | ✅ **`CF-1` chốt: bộ lọc động**, đặt trong dashboard hiện có | ❌ Không |
| `BI-5` | `Test Account` là **học viên thật về mặt dữ liệu**. Mọi truy vấn nhóm không lọc sẽ tính cả tài khoản kiểm thử | `BA-02` đã chốt loại. Cần ghi thành rule áp cho **từng** màn, không chỉ nói chung | ✅ Có |
| `BI-6` | Người được gán làm quản lý **không được báo**, nên không biết để mở màn theo dõi nhánh. Phát hiện từ nghiên cứu LMS v0.2 §9.2b, sau khi PRD đã duyệt | ✅ **CR1 09/10/2026:** thêm `RC-20` và mail event `MAIL-GRP-02`, ghi ở PRD `US9` `BR-9.6` `BR-9.7`, `US11` `BR-11.7` và `US13` `BR-13.6` `BR-13.7` | ✅ Có |

### Old → New — *chiều hay bị bỏ*

| # | Phát hiện | FR/NFR bổ sung | Feed ngược BRD? |
| --- | --- | --- | --- |
| ~~`BI-6`~~ | Tưởng hệ thống đã có cơ chế chuyển học viên giữa lớp — `PUT /classes/{id}/students/transfer` | ✅ **PO chốt 06/10: endpoint có, tính năng KHÔNG có.** Chuyển lớp hiện là xoá khỏi lớp cũ, thêm vào lớp mới, **học lại từ đầu**.<br>Luật đứng không phải xử lý trường hợp này | ❌ Không |
| `BI-6b` | 🟠 **Xoá khỏi lớp làm mất tiến độ thật.** Đây là hành vi hiện có, và là cái người vận hành đang dùng để chuyển lớp | Luật đứng phải phân biệt **hai luồng rời lớp**: xoá thủ công *(mất tiến độ)* và nghỉ việc *(đánh dấu, giữ dữ liệu — `OQ-36`)* | ✅ **Có** |
| `BI-7` | `KB-CLASS-03`: lớp `Flexible` mà học viên chưa Activate thì **không set được thời hạn riêng**. Người vào nhóm sau 6 tháng vẫn nhận đủ N ngày | Đúng hay sai là câu nghiệp vụ, phải chốt | ✅ Có |
| `BI-8` | Lớp `Ended` không sửa được *(`KB-CLASS-05`)*. `BA-03` chốt theo luật Lớp — nghĩa là luật đứng **im lặng dừng lại** | Cần quy tắc: dừng im lặng hay báo cho người gán biết | ✅ Có |
| `BI-9` | Lớp có `Số học viên tối đa`. `BA-07` chốt chỉ cảnh báo — nhưng cảnh báo cho **ai**, khi người mới vào nhóm 3 tháng sau và không có ai đang ngồi trước màn hình | Luật đứng chạy nền thì cảnh báo đi đâu | ✅ **Có** |
| `BI-10` | `KB-USER-02`: thông tin học viên không sửa được trên Ops, **trừ Username** | Nhóm đồng bộ phải theo cùng nguyên tắc. Xem `CF-3` | ✅ Có |
| `BI-11` | Ma trận quyền nằm trong `casbin_rule`, **không đọc được từ schema**. KB `06` Q1 treo từ 23/09 | Không thiết kế phạm vi dữ liệu trên một nền chưa ai nhìn thấy. Cần bản export policy | ✅ Có |

---

## 7. Coverage Gaps *(STEP 3c)*

### Boundary

| # | Case chưa định nghĩa | FR bổ sung |
| --- | --- | --- |
| `CG-1` | **Nhóm rỗng** được gán nội dung. Sau đó có người vào | Luật đứng phải chạy tại thời điểm người vào, không phải lúc gán |
| `CG-2` | **Nhóm cha rỗng nhưng nhánh con có người.** Gán cho cha, chảy xuống con | Quy tắc *cha bao trùm con* áp cho gán nội dung hay chỉ cho báo cáo |
| `CG-3` | Một người thuộc **nhiều nhóm cùng được gán một khoá** | `C2` nói một lượt ghi danh. Nhưng gỡ khỏi một nhóm thì lượt đó còn không |
| `CG-4` | Cây chạm **đúng 6 cấp**, rồi di chuyển một nhánh xuống sâu hơn | Chặn ở đâu, báo gì |
| `CG-5` | Di chuyển nhánh tạo **vòng lặp** — A là cha B, B lại là cha A | `OQ-06` đã ghi: giới hạn số cấp **không** giải được việc này |

### Exception

| # | Case chưa định nghĩa | FR bổ sung |
| --- | --- | --- |
| `CG-6` | **Đồng bộ đang chạy mà có người sửa tay** cùng lúc | Ai thắng |
| `CG-7` | **Đồng bộ nửa chừng thì lỗi.** Một nửa cây đã cập nhật | Toàn bộ hoặc không gì cả, hay chấp nhận dở dang |
| `CG-8` | Cây Lark đổi lớn giữa hai lần đồng bộ — một khối bị giải thể | Có cảnh báo trước khi áp không |
| `CG-9` | Quyền quản lý **bị thu hồi giữa lúc họ đang xem báo cáo** | — |

### Shared entity

| # | Entity | Rủi ro |
| --- | --- | --- |
| `CG-10` | **`users`** — **15 bảng** giữ khoá ngoại trỏ về *(đo từ schema 05/10)* | Shared entity lớn nhất hệ. Thêm quan hệ cơ cấu vào `users` chạm mọi nơi đọc học viên |
| `CG-11` | **`class_user_instances`** — **6 bảng** treo vào: điểm, lượt làm bài, tiến độ section, tiến độ storyline, cấu hình quiz, ghi chú | 🔴 `OQ-22` *(rời nhóm thì lượt ghi danh xử lý sao)* **chạm 6 bảng dữ liệu học**, không chỉ một dòng |
| `CG-12` | **`course_categories`** — **6 bảng** trỏ về: `courses` · `quizzes` · `certificates` · `staffs` · `support-groups` · **`users.category_primary_id`** | ✅ Đã kiểm. Nhóm **không** chạm Category trực tiếp. Nhưng Comment Replier gắn Category, nên `CF-2` đi vòng qua đây |
| `CG-13` | **Question Bank** — tiêu thụ bởi Test, Quiz, Case Study, Storyline | ✅ Đã kiểm. Nhóm **không** chạm. Nhóm dừng ở mức *ai vào lớp nào* |
| `CG-14` | `support-groups` dùng chung từ *"nhóm"* nhưng là **thực thể khác hẳn**, có bảng nối riêng `support_groups_user_instances`, lại **không có `tenant_id`** | Đặt tên và giao diện phải tách bạch, nếu không Ops sẽ nhầm hai thứ. Cùng loại vấn đề với `CF-6` |

### Side effect

| # | Hệ quả ngoài ý muốn |
| --- | --- |
| `CG-15` | **Người nghỉ việc làm số liệu quý đã chốt thay đổi** — dây chuyền `Block` → gỡ nhóm → gỡ lớp → mất ghi danh → mất dữ liệu ở 6 bảng treo vào. `BA-06` đã chặn, nhưng phải ghi thành luật rõ, không để suy ra |

---

## 8. Transition Requirements *(STEP 4)*

| Loại | Nội dung |
| --- | --- |
| **Data** | `groups` và `group_user_instances` **đang có dữ liệu thật hay rỗng?** PO chốt bỏ chức năng cũ, nhưng chưa ai nói dữ liệu cũ xử lý ra sao → `OQ-25`.<br>Đồng bộ lần đầu dựng **53 nhóm, 384 quan hệ thành viên**.<br>`C3` yêu cầu thành viên kèm thời điểm — mốc thời gian của lần đồng bộ đầu là ngày bật, không phải ngày người đó vào công ty. Báo cáo lùi xa hơn mốc đó **sẽ không có dữ liệu** |
| **Compatibility** | Đường gán cũ *(chọn tay vào lớp)* và đường mới *(qua nhóm)* **phải chạy song song lâu dài**, không phải giai đoạn chuyển tiếp. `C2` là thứ giữ cho hai đường không đụng nhau |
| **Cutover** | 🔴 **Tách làm hai lần bật.** Lần một: đồng bộ cây và thành viên, **chưa gán nội dung nào**. Lần hai: mở chức năng gán. Bật cùng lúc thì lần đồng bộ đầu tiên có thể kích hoạt luật đứng và bắn mail hàng loạt.<br>Rollback: tắt luật đứng được, nhưng **lượt ghi danh đã sinh thì không thu hồi tự động** — chúng sống ở Lớp |

---

## 9. Kiểm tra chiều tenant *(STEP 5)*

| Câu hỏi | Trả lời | Xử lý |
| --- | --- | --- |
| Có nhúng thêm logic riêng UpBase vào code không? | ⚠️ **Có, hai chỗ** | Xem bảng dưới |
| Có hằng số cứng mới không? | **Số cấp tối đa = 6** | ✅ Đã chốt **cấu hình được theo tổ chức**, không đóng cứng |
| Bảng mới có `tenant_id` không? | Phải có | `groups` hiện **đã có** `tenant_id`. Mọi bảng mới phải theo |
| Enum mới: hệ thống hay tenant định nghĩa? | **Nguồn nhóm** *(đồng bộ HRM / tự tạo)* và **loại quan hệ** *(quản lý / mentor)* | Nguồn nhóm là **hệ thống định nghĩa**. Loại quan hệ nên để **tenant tự thêm** — tổ chức khác có thể cần `coach`, `buddy` |

### Hai chỗ đóng cứng tăng thêm

| Chỗ | Mức sẵn có | Dự án này làm gì |
|---|---|---|
| **Đồng bộ từ HRIS UpBase một chiều** | 🔴 Cao — *"mỗi tenant một HRIS"* | ⚠️ **Tăng.** Trước chỉ đồng bộ người, nay đồng bộ cả cơ cấu. Tenant khác dùng HRIS khác phải làm lại tầng này.<br>**Cách tách:** định nghĩa một *hình dạng dữ liệu cơ cấu* chuẩn, Lark chỉ là một bộ chuyển đổi đổ vào đó |
| **Luật đứng tự thêm người vào lớp** | 🟠 — Comment Replier đã là một chỗ như vậy | ⚠️ **Thêm một chỗ cùng kiểu.** Khác biệt: lần này luật đứng **do người dùng cấu hình** *(chọn nhóm, chọn lớp, bật tắt công tắc)*, không đóng cứng theo Category như Comment Replier. Nhẹ hơn, nhưng vẫn là quy trình vận hành nhúng vào sản phẩm |

---

## 10. Risk Summary

| # | Risk | Mức | Giảm nhẹ |
| --- | --- | --- | --- |
| `R-1` | **Bắn mail hàng loạt khi bật** | 🔴 Cao | Tách cutover làm hai lần. Chốt quy tắc mail cho đường gán qua nhóm trước khi làm |
| `R-2` | **Ghi danh nhân đôi vì Foundation** mà người gán không biết | 🔴 Cao | Báo trước khi gán: *"lớp này có Foundation, N người sẽ vào 2 lớp"* |
| `R-3` | **Báo cáo theo nhóm không làm được** vì `KB-SIS-01` | 🔴 Cao | `CF-1` phải quyết ở Bước 7 trước khi viết PRD |
| `R-4` | **Thiết kế phạm vi dữ liệu trên nền chưa ai nhìn thấy** — ma trận quyền Casbin | 🟠 | Xin bản export policy. KB `06` Q1 treo từ 23/09, đã hai tuần |
| `R-5` | **Lịch sử thành viên chỉ có từ ngày bật.** Báo cáo lùi xa hơn không có dữ liệu | 🟠 | Nói rõ với người dùng, không để họ tưởng có dữ liệu cũ |
| `R-6` | **Hai luật đứng đụng nhau** — Comment Replier và Nhóm | 🟠 | `CF-2` phải quyết |
| `R-7` | **Từ "Mentor" trùng tên, khác nghĩa** — Ops chọn nhầm người, Dev dựng nhầm quan hệ | 🟠 | `CF-6` — đổi tên khái niệm mới trước khi viết PRD |
| `R-8` | Vùng `Schedules` · `Room` chưa tra được, KB không phủ | 🟡 | Ghi `❓BA`, không kết luận không ảnh hưởng |

---

## 11. Open Questions

| # | Câu hỏi | Vì sao quan trọng | Người trả lời | Chặn Gate 3? |
| --- | --- | --- | --- | --- |
| `OQ-25` | **`groups` và `group_user_instances` đang có dữ liệu thật hay rỗng?** PO chốt bỏ chức năng cũ, nhưng chưa nói dữ liệu cũ xử lý ra sao | Quyết định Transition có phần migration hay không | PO · Dev | ❌ Không |
| ~~`OQ-26`~~ | Gán nội dung qua nhóm có gửi mail #11 không | ✅ **Đóng 06/10 — gửi bình thường** | PO | — |
| ~~`OQ-27`~~ | Gán nhóm cho lớp có Foundation thì báo gì | ✅ **Đóng 06/10 — không cần báo gì riêng** | PO | — |
| `OQ-34` | **Tài khoản `Test Account` và Comment Replier tạo bằng cách nào?** Chúng không phải nhân sự nên không có trong cây Lark, mà `KB-USER-01` nói học viên không tạo thủ công được | `CF-2` dựa vào việc tách tài khoản. Nếu không tạo được thì cách tách không chạy | PO · Dev | ❌ Không |
| ~~`OQ-35`~~ | Lớp chứa nhiều nhóm, mỗi nhóm một mentor — ai là `Main Responsible` | ✅ **Đóng 06/10 — mentor đầu tiên vào lớp, đổi lại được** | PO | — |
| ~~`OQ-36`~~ | "Mất lượt ghi danh" là xoá dữ liệu hay đánh dấu đã kết thúc | ✅ **Đóng 06/10 — ĐÁNH DẤU, KHÔNG XOÁ.** Dùng `class_user_instances.status` | PO | — |
| ~~`OQ-28`~~ | Cảnh báo vượt sức chứa lớp đi đâu | ✅ **Đóng 06/10 — một dòng ở màn danh sách học viên trong lớp, không realtime, không chặn** | PO | — |
| ~~`OQ-29`~~ | Người bị chuyển lớp thì luật đứng xử lý sao | ✅ **Đóng 06/10 — chưa có chức năng chuyển lớp.** Endpoint `transfer` là endpoint chết. Chuyển lớp = xoá khỏi lớp cũ, thêm lớp mới, học lại từ đầu | PO | — |
| `OQ-30` | **Loại quan hệ** *(quản lý / mentor)* do hệ thống định nghĩa cố định, hay tenant tự thêm được | Chiều tenant. Tổ chức khác có thể cần `coach`, `buddy` | PO | ❌ Không |
| `OQ-31` | **Xin bản export `casbin_rule`** hoặc tài liệu mô tả role | Không thiết kế phạm vi dữ liệu trên nền chưa nhìn thấy | Dev | ❌ Không — nhưng chặn PRD |
| ~~`OQ-32`~~ | Đổi tên khái niệm `mentor` mới thành gì | ✅ **Đóng 06/10 — không cần đổi.** `CF-6` chốt: chỉ có **một** khái niệm mentor, nó đi theo nhóm vào lớp | PO | — |
| `OQ-33` | **`roles.is_group` là gì?** Cột này có trong schema, có liên quan tới chức năng Nhóm không | Nếu hệ đã có khái niệm role dạng nhóm thì phải biết trước khi dựng cái mới | PO · Dev | ❌ Không |

Cộng với **4 câu nhóm D còn mở**: `OQ-21` · `OQ-22` · `OQ-23` · `OQ-24`. Trong đó `OQ-21` và `OQ-22` chặn PRD.

---

## 12. Phụ lục — Nguồn đã đọc

| Nguồn | Cụ thể |
| --- | --- |
| **KB** | `00-index` *(trạng thái ẩn)* · `01-course §226` · `04-class §2 §4 §5 §9 §10` · `05-grading §1 §2` · `06-user-account §2 §7 §8b` · `09-notification-email §5 §7` · `11-dashboard-sis §2 §3` · `12-data-model §1 §2 §3 §4` · `13-mail-events §2` · `14-api-surface` *(toàn bộ)* · `15-product-direction §6` · `16-domain-principles` |
| **DB** | ✅ **Đã tải và đọc lại file gốc** `UpLnd DB Full.html` từ Lark ngày 05/10/2026 — không dùng bản chép trong KB.<br>`obj_edit_time` của file = **23/09/2026 11:41**, đúng ngày KB `12` đối chiếu. Đọc được **85 bảng · 173 quan hệ**, khớp số trong KB.<br>Bảng đã đọc cột: `users` · `classes` · `class_user_instances` · `groups` · `group_user_instances` · `departments` · `staffs` · `casbin_rule` · `field_change_logs` · `roles` · `support-groups` · `support_groups_user_instances` · `notification_group_instances`.<br>Đã đếm khoá ngoại trỏ về: `users` (15) · `staffs` (12) · `classes` (7) · `class_user_instances` (6) · `course_categories` (6) · `groups` (2) · `departments` (1) |
| **Swagger** | Đọc lại **05/10/2026** từ tên miền mới. Ops 514 operation · LMS 136.<br>Schema: `CreateGroupDto` · `EditGroupDto` · `AddUserToGroupDto`.<br>Endpoint: `Group Management` (9) · `Department Management` (9) · `Support Group Management` (9) · `Report LMS` (6) · nhóm `classes/*/students/*` |
| **Mail** | KB `13` — #11 #12 #23 #24 #25 #26 *(đang bật)* · #17–#20 #32–#35 *(đang tắt)* |
| **Quyết định** | `project-decisions.md` — Bước 2 · Bước 3 · Gate 1 · Bước 5 |
| **⚠️ Chưa tra được** | • **Ma trận quyền Casbin** — `casbin_rule` không đọc được từ schema, chưa có bản export. KB `06` Q1 treo từ 23/09<br>• **Vùng `Schedules` · `Room Management` · `Class Schedule`** — 45+ operation, KB chưa phủ. Không kết luận có ảnh hưởng hay không<br>• **Cơ chế `transfer` học viên giữa lớp** — chỉ thấy qua endpoint, không có tài liệu nào mô tả<br>• **Dữ liệu thật trong `groups`** — chưa biết rỗng hay có |
