# Impact Matrix — Gamification

| | |
| --- | --- |
| **Project** | Gamification |
| **Version** | v0.1 |
| **Ngày** | 23/09/2026 |
| **Nguồn input** | `brd-v0.6-20260923.md` (Gate 1 `Approved with Notes`) · `related-map-v0.2` · KB `01`–`15` · schema Lark `Data Architecture` (đọc lại 23/09) · Swagger LMS + Ops |
| **Trạng thái** | `Pending Confirmation` — **6 conflict cần PO quyết** |

> Bản phân tích **nội bộ**. Kết quả chảy vào PRD ở: `Solution` · `Database` · `API` · `Acceptance criteria → Data Field` · `Out of scope`.

---

## 1. Summary

Gamification là module mới, **chỉ đọc dữ liệu học tập**, nên phần lớn tác động là *thêm mới* chứ không *đổi hành vi*. Nhưng ba chỗ đổi thật: **bảng `tenant` phải thêm tham số múi giờ**, **màn My Learning phải hiện điểm và hạng**, và **quy trình chấm bài phải chấm hết tồn trước khi chốt kỳ**.

Chỗ nguy hiểm nhất **không nằm ở nơi ai cũng nhìn**. Ba thứ đáng lo nhất:

1. **Tài khoản `Test Account` của nhóm Comment Replier sẽ xuất hiện trên bảng xếp hạng công khai** — đây là tài khoản học viên thật theo định nghĩa hệ thống, nhưng là người của công ty.
2. **Ngày bật tính năng, mọi học viên cũ mở lại nội dung đã học sẽ được cộng điểm** nếu không nạp sẵn dấu khử trùng.
3. **Học lại cùng nội dung ở lớp khác: hệ thống bảo "chưa học", gamification không cộng điểm** — hai hệ thống nói hai điều khác nhau với cùng một học viên.

| | Số lượng |
| --- | --- |
| Vùng bị ảnh hưởng (High / Medium / Low) | **5 / 5 / 2** |
| Conflict cần escalate | **6** |
| FR/NFR bổ sung phát hiện được | **9** |
| Coverage gap | **14** |
| Chỗ đóng cứng tenant tăng thêm | **1** *(Foundation)* |

---

## 2. Current Situation — Dependency Map *(STEP 1)*

| Loại | Mục | Nguồn | Ghi chú |
| --- | --- | --- | --- |
| **Module** | Learning Experience | KB `07` | **Nguồn sự kiện chính.** Chỉ đọc |
| **Module** | Assessment (chỉ Test) | KB `03` | Quiz · Case Study · Storyline **bị loại** |
| **Module** | Grading | KB `05` | Nơi chốt đạt/trượt bài chấm tay |
| **Module** | Course · Certificate | KB `01` · `08` | Mốc "hoàn thành khoá" |
| **Module** | Class | KB `04` | Không sửa — nhưng là gốc của `C5` |
| **Module** | User Account | KB `06` | `Block` · SSO Lark |
| **Data** | `user_course_section_progress` | KB `12` · Lark schema | FK → `class_user_instances`, **không FK tới `users`** |
| **Data** | `class_user_instances` | KB `12` | Cầu nối duy nhất `users` ↔ nội dung học |
| **Data** | `quiz_attempts` · `quiz_attempt_gradings` | KB `12` | Nguồn sự kiện bài Test |
| **Data** | `quizzes` | KB `03` | `Graded Assignment` · `Pass Point` |
| **Data** | `courses_users_certificates` | KB `12` | **Bảng duy nhất nối thẳng `users`** |
| **Data** | `tenant` | KB `12` | 7 cột, **không có múi giờ** → `S21` |
| **Data** | `resources` | KB `12` | FK của 4 bảng — dùng cho ảnh huy hiệu/hạng |
| **Data** | `casbin_rule` | KB `12` | ptype + v0–v6 |
| **Rule** | `KB-LX-03a` `KB-LX-03b` | KB `07` | Điều kiện hoàn thành Activity |
| **Rule** | `KB-LX-08` | KB `07` 🆕 | Đã học ≥1 hoạt động → không huỷ ghi danh |
| **Rule** | `KB-TEST-01` `01a` `01b` | KB `03` 🆕 | `Pass Point` phụ thuộc `Graded Assignment` |
| **Rule** | `BR-EDIT-07` | KB `01` | Test đã có người làm → khoá cấu hình |
| **Rule** | `BR-COURSE-INFO-06` | KB `01` | `Pass Point` = điều kiện chứng chỉ |
| **Rule** | `KB-CR-01` `KB-CR-03` | KB `09` | ⚠️ Comment Replier — xem `CF-1` |
| **Process** | Enroll → Activate/Begin → học → hoàn thành khoá → chứng chỉ | KB `07` · `08` | |
| **Process** | Nộp bài → mentor chấm → `finish` → đạt/trượt | KB `05` | Độ trễ nhiều ngày |
| **Permission** | Casbin | KB `06` · `casbin_rule` | Thêm resource, không đổi cơ chế |
| **Integration** | Keycloak / SSO Lark | KB `06` · `15` §6 | 🟢 `S3` **không còn phụ thuộc** |
| **Integration** | Hệ Email ngoài | KB `09` | 🟢 **Không dùng** |
| **Mail event** | #10 · #29 — hoàn thành khoá | KB `13` | 🟢 Đang bật. Cùng thời điểm với sự kiện cộng điểm |
| **Mail event** | 8 mail luồng chấm điểm | KB `13` `KB-MAIL-03` | 🔴 **Đang tắt** — PO chốt không bật lại |
| **Tính năng ẩn** | Storyline | KB `00-index` | 🟢 Đã loại (`BA-04`) — hai lý do cùng loại trừ |
| **Tính năng ẩn** | **Quản lý bài kiểm tra trong lớp** | KB `00-index` · `13` §74 | ⚠️ Bài Test có **Thời gian mở/đóng**. Xem `CG-6` |
| **Tính năng ẩn** | Notice List · Recipients List · Mail Logs | KB `09` §1 | 🟢 Không dùng |

---

## 3. Desired Situation *(STEP 2)*

Từ BRD v0.6 — module mới gồm 5 lớp:

```
Lớp 1  Bắt sự kiện học tập      3 hành động học + "vào hệ thống hằng ngày"
Lớp 2  Quy đổi ra điểm          bảng cấu hình + khử trùng + trần điểm/ngày
Lớp 3  Tích luỹ và xét ngưỡng   điểm · 4 loại huy hiệu · hạng
Lớp 4  Xếp hạng theo kỳ         kỳ lịch (tự động) + chiến dịch (vận hành khai)
Lớp 5  Phản hồi cho học viên    đẩy khi online · trang thành tích · bảng xếp hạng
```

**23 hạng mục In scope · 17 US làm đợt này · 9 ràng buộc `C1`–`C9`.**

FR/NFR đã có trong BRD: `C1`–`C9` · `BR-TEST` · `BR-REGRADE` · `BR-SKIP` · `S22` (tiêu chí phụ khi đồng hạng).

---

## 4. Impact Matrix — 12 vùng *(STEP 3.0)*

| # | Vùng | Bị ảnh hưởng? | Mô tả | Severity | Nguồn |
| --- | --- | --- | --- | --- | --- |
| 1 | **Business process** | ✅ Có | **Quy trình chấm bài phải chấm hết tồn trước khi chốt kỳ** — ràng buộc mới lên team chấm, không phải yêu cầu chức năng. Thêm quy trình vận hành: cấu hình gamification · tạo chiến dịch · công bố kết quả và trao thưởng ngoài hệ thống | **Medium** | `BA-02` · `TR-5` |
| 2 | **Module / function** | ✅ Có | Module mới. Các module hiện hữu thành **nguồn sự kiện chỉ đọc**. My Learning **bị sửa** | **High** | `BA-08` · BRD §8 |
| 3 | **Screen / report** | ✅ Có | 9 màn mới (4 LMS + 5 Ops) · **1 màn existing bị sửa: My Learning** | **Medium** | `BA-08` |
| 4 | **Data** | ✅ Có | 10 thực thể mới. **`tenant` phải thêm tham số múi giờ** — đây là thay đổi bảng hiện hữu duy nhất | **High** | `S21` `C6` · bảng `tenant` |
| 5 | **API** | ✅ Có | Toàn bộ API gamification là mới. **`GET /api/v1/courses/my-learnings` phải trả thêm điểm và hạng** — thêm field, không phá contract cũ | **Medium** | `BA-08` |
| 6 | **Role / permission** | ✅ Có | Thêm resource Casbin cho cấu hình gamification. L&D/Mentor/Giáo viên xử lý bằng phân quyền thường (`BA-11`) | **Low** | `casbin_rule` · `BA-11` |
| 7 | **Business rule** | ✅ Có | 3 rule mới (`BR-TEST` `BR-REGRADE` `BR-SKIP`). **2 rule hiện hữu vừa được đính chính** trong đợt này (`KB-LX-04` bị gỡ, `KB-TEST-01a` thêm mới) | **High** | KB `03` · `07` |
| 8 | **NFR** | ✅ Có | Bảng xếp hạng tính từ sổ giao dịch theo khoảng ngày, toàn tổ chức, nhiều kỳ lồng nhau, ba chỉ số. Sổ giao dịch tăng tuyến tính theo hoạt động học | **High** | `OQ-B9` · `C3` `C7` |
| 9 | **Notification / Email** | ⚠️ Rất ít | Gamification **không dùng** cơ chế thông báo hiện có, **không gửi mail** (`S10` `N5`). Chạm duy nhất: mail #10/#29 (hoàn thành khoá) bắn cùng thời điểm với sự kiện cộng điểm — hai kênh khác nhau nên không trùng lặp thật | **Low** | KB `13` · `S10` |
| 10 | **Reporting** | ❌ Không | **SIS độc lập** (`BA-07`). Gamification không đẩy dữ liệu vào dashboard nào. ⚠️ Nhưng L&D là stakeholder và **chưa có báo cáo nào phục vụ họ** — xem `CG-14` | **Low** | `BA-07` |
| 11 | **Test** | ✅ Có | Vùng phải kiểm lại: luồng hoàn thành Activity · luồng hoàn thành khoá · luồng chấm bài (`finish`) · màn My Learning · quy trình bật/tắt hai công tắc | **Medium** | — |
| 12 | **Release** | ✅ Có | Thứ tự: cấu hình → dữ liệu → job nền → màn Ops → màn LMS. **Hai công tắc cho phép ra mắt an toàn** — bật `Gamification` chạy ngầm trước, `Visibility` sau | **Medium** | `S12` · `TR-7` |

**Tổng: High 5 · Medium 5 · Low 2.**

> Vùng thuộc phần **KB chưa phủ** (KB `14` §1–2): đã kiểm. `Examination` và `Entrance Test` — PO xác nhận **chức năng không tồn tại** (`BA-06`). Lịch dạy · phòng học · phòng ban — không giao với gamification. Phân quyền — đã xét ở vùng 6.

---

## 5. Conflict Analysis *(STEP 3a)*

> **Sáu conflict, escalate cho PO quyết. Tôi không tự chốt.**

| # | Chiều | Conflict | Hiện tại | Mới | Ai quyết |
| --- | --- | --- | --- | --- | --- |
| **CF-1** | **Process + Permission** | 🔴 **Tài khoản của người công ty sẽ lên bảng xếp hạng công khai.** `KB-CR-01`: thành viên nhóm Comment Replier **phải là tài khoản học viên có `Test Account = Yes`**. `KB-CR-03`: họ được **tự động thêm vào các lớp**. Về mặt dữ liệu họ là học viên thật, có tiến độ học thật | Test Account là học viên bình thường trong mọi truy vấn | `A15` — bảng xếp hạng công khai danh tính học viên | **PO** |
| **CF-2** | **Business rule** | 🔴 **Học lại nội dung ở lớp khác: hệ thống bảo "chưa học", gamification không cộng điểm.** Tiến độ gắn theo lượt ghi danh (`class_user_id`), nên vào lớp mới là tiến độ về 0 và học viên **phải học lại**. Nhưng `C5` khử trùng theo người nên **không cộng điểm** | Học viên học lại, thanh tiến độ chạy bình thường | `C5` — mỗi nội dung trả điểm một lần trong đời | **PO** |
| **CF-3** | **Business rule** | 🟠 **Đổi ngưỡng hạng thì người cũ giữ hạng, người mới phải đạt cao hơn.** `A3` nói hạng chỉ lên không tụt; `C4` nói đổi cấu hình áp dụng từ lúc đổi. Ghép lại: hai học viên **cùng số điểm nhưng khác hạng** | — | `A3` + `C4` | **PO** |
| **CF-4** | **Business rule** | 🟠 **Tương tự với huy hiệu.** `A5` nói huy hiệu đạt rồi giữ vĩnh viễn. Nâng ngưỡng huy hiệu → người đạt trước giữ, người sau phải làm nhiều hơn cho cùng một huy hiệu | — | `A5` + `C4` | **PO** |
| **CF-5** | **Data** | 🟠 **Xoá tài nguyên đang dùng làm ảnh huy hiệu.** `resources` là FK của 4 bảng và có cơ chế quản lý riêng. Vận hành xoá một ảnh đang gắn với huy hiệu thì huy hiệu mất hình — kể cả huy hiệu học viên đã đạt | Quản lý tài nguyên không biết gamification đang dùng | `S4` — huy hiệu có hình | **PO + Dev** |
| **CF-6** | **Process** | 🟡 **Tắt `Gamification` giữa lúc chiến dịch đang chạy.** Chiến dịch đang chạy không sửa được (`S17`), nhưng công tắc tổ chức lại tắt được bất cứ lúc nào. Chiến dịch dở dang xử lý sao — huỷ, giữ nguyên, hay chốt sớm? | — | `S12` + `S17` | **PO** |

---

## 6. Bidirectional Impact — FR/NFR còn thiếu *(STEP 3b)*

### New → Old

| # | Chiều | Phát hiện | FR/NFR bổ sung | Feed ngược BRD? |
| --- | --- | --- | --- | --- |
| BI-1 | New→Old | `tenant` phải thêm tham số múi giờ — **bảng hiện hữu duy nhất bị sửa** | `FR-1`: tham số múi giờ cấp tổ chức, thiết kế để module Tenant sau tiếp quản | ✅ Có (`S21` đã có, nhưng chưa nêu là sửa bảng hiện hữu) |
| BI-2 | New→Old | `GET /courses/my-learnings` phải trả thêm điểm và hạng | `FR-2`: thêm field, giữ tương thích ngược | ✅ Có |
| BI-3 | New→Old | Team chấm bài chịu ràng buộc thời gian mới | `TR-5` — quy trình, không phải chức năng | ✅ Có |

### Old → New — *chiều hay bị bỏ*

| # | Phát hiện | Ràng buộc lên tính năng mới | FR bổ sung |
| --- | --- | --- | --- |
| **BI-4** | 🟢 `BR-EDIT-07` khoá `Graded Assignment` sau khi có người làm bài | Quy tắc đếm bài Test **ổn định**, không có kịch bản tính lại ngược | — *(thuận lợi)* |
| **BI-5** | 🟢 `KB-LX-08` chặn huỷ ghi danh sau khi đã học | Đường cày điểm ghi danh–huỷ–ghi danh lại **đã bị chặn sẵn** | — *(thuận lợi)* |
| **BI-6** | 🔴 **Học viên đã học xong hết khoá của mình thì gần như không còn cách kiếm điểm** — chỉ còn "vào hệ thống hằng ngày" | Nhóm học viên chăm nhất lại là nhóm bị kẹt ở đáy bảng xếp hạng | **`FR-3`**: cân nhắc cách ghi nhận cho nhóm này, hoặc chấp nhận có chủ đích |
| **BI-7** | 🔴 **Ngày bật tính năng, học viên cũ mở lại nội dung đã học sẽ được cộng điểm** nếu không nạp sẵn dấu khử trùng | Ngày đầu tiên thành ngày cày điểm tập thể | **`FR-4`**: nạp dấu khử trùng từ tiến độ hiện có tại thời điểm bật → xem `TR-2` |
| **BI-8** | 🟠 Khoá **Flexible** chỉ bắt đầu khi học viên bấm **Activate** | Học viên giữ khoá chưa Activate thì không sinh sự kiện nào — bình thường, nhưng cần rõ là không tính | `FR-5`: nêu rõ trong `Out of scope` của US |
| **BI-9** | 🟠 **Khoá Trial** tồn tại (`POST /courses/{id}/trial/upgrade-now`) | Hoạt động trong khoá dùng thử có tính điểm không? | **`FR-6`** — `OQ-C3` |
| **BI-10** | 🟠 Mô hình **Foundation → Normal Course** là đặc thù UpBase (KB `15` §6) | `BR-SKIP` nhúng khái niệm Foundation vào gamification → **chỗ đóng cứng mới** | **`FR-7`**: viết tổng quát *"khoá được đánh dấu bỏ qua thì không tính hoàn thành"* thay vì gọi tên Foundation |
| **BI-11** | 🟠 Bài Test có **Thời gian mở / đóng** (tính năng đang ẩn — KB `13` §74) | Học viên không làm được bài ngoài cửa sổ thời gian → ảnh hưởng khả năng kiếm điểm, không phải lỗi | `FR-8`: ghi nhận, không xử lý |
| **BI-12** | 🟡 `support-groups` **không có `tenant_id`** (KB `15` §6, 🔴) | Nếu loại trừ Test Account qua nhóm Comment Replier thì chạm bảng không có tenant | **`FR-9`**: loại trừ theo cờ `Test Account` trên tài khoản, **không** theo nhóm |

---

## 7. Coverage Gaps *(STEP 3c)*

### Boundary

| # | Case chưa định nghĩa | FR bổ sung |
| --- | --- | --- |
| CG-1 | Học viên **0 điểm** — hiện ở đâu trên bảng xếp hạng? Đồng hạng cuối với toàn bộ người 0 điểm? | Quy tắc hiển thị nhóm 0 điểm |
| CG-2 | **Kỳ chưa có ai được điểm** — bảng rỗng hiện gì | Trạng thái rỗng |
| CG-3 | Điểm **bằng đúng ngưỡng** hạng — lên hạng hay chưa? (`>=` hay `>`) | Quy ước so sánh ngưỡng, áp chung cho hạng và huy hiệu |
| CG-4 | **Chạm trần điểm/ngày giữa chừng** — hoàn thành hoạt động thứ N khi trần đã đầy: không cộng, cộng một phần, hay dời sang hôm sau? | Quy tắc khi chạm trần |
| CG-5 | **Chiến dịch bắt đầu và kết thúc cùng một ngày** | Cho phép hay chặn |
| CG-6 | **Biên ngày và biên kỳ** — học viên hoàn thành hoạt động lúc 23:59:59 theo múi giờ tổ chức | `C9` đã có nguyên tắc, cần rõ quy ước đóng/mở khoảng |

### Exception

| # | Case chưa định nghĩa | FR bổ sung |
| --- | --- | --- |
| CG-7 | **Hai thiết bị cùng hoàn thành một hoạt động gần như đồng thời** — cộng điểm hai lần? | Chống trùng ở tầng ghi nhận, không chỉ dựa khử trùng nội dung |
| CG-8 | **Job chốt kỳ chạy lỗi hoặc chạy muộn** | Cơ chế chạy lại, bảo đảm chốt đúng biên kỳ dù job trễ |
| CG-9 | **Học viên bị `Block` giữa kỳ** — `A14` nói biến khỏi bảng đang chạy. Bị Block rồi mở lại thì sao? | Quy tắc vào/ra bảng xếp hạng |
| CG-10 | **Mentor chấm bài sau khi kỳ đã chốt** — snapshot đã đóng băng (`O5`) | Điểm vào kỳ hiện tại, không sửa snapshot cũ |
| CG-11 | **Vận hành đổi cấu hình điểm giữa lúc chiến dịch đang chạy** — `S17` khoá chiến dịch nhưng **không khoá bảng điểm** | Có khoá bảng điểm khi có chiến dịch đang chạy không |

### Shared entity

| # | Entity | Rủi ro |
| --- | --- | --- |
| CG-12 | **`resources`** — FK của 4 bảng, dùng cho ảnh huy hiệu và ảnh hạng | Xoá tài nguyên đang dùng → `CF-5` |
| CG-13 | **`course_categories`** — FK của **6 bảng** (`courses`, `users`, `staffs`, `quizzes`, `certificates`, `support-groups`) | Gamification **không chạm ở đợt này**. Nhưng nếu sau này huy hiệu hay chiến dịch phân theo danh mục thì chạm 6 bảng — ghi để nhớ |
| — | **Question Bank** | Không chạm — gamification không đi tới tầng câu hỏi |

### Side effect

| # | Hệ quả ngoài ý muốn |
| --- | --- |
| CG-14 | **L&D là stakeholder nhưng không có báo cáo nào phục vụ họ.** SIS độc lập, gamification không đẩy dữ liệu đi đâu. Họ chỉ xem được bảng xếp hạng như học viên |
| — | `CF-1` (Test Account) và `CF-2` (học lại không được điểm) đã nêu ở §5 |

---

## 8. Transition Requirements *(STEP 4)*

### Data

| # | Yêu cầu | Mức |
| --- | --- | --- |
| **TR-1** | **Không backfill điểm.** Kỳ lịch bắt đầu từ thời điểm bật (`A16`), không dựng lại bảng cho kỳ trước | Đã chốt |
| **TR-2** | 🔴 **Nạp sẵn dấu khử trùng từ tiến độ hiện có tại thời điểm bật.** Không làm thì ngày đầu tiên mọi học viên cũ mở lại nội dung đã học đều được cộng điểm | **Bắt buộc** — `BI-7` |
| **TR-3** | Thêm cột múi giờ vào `tenant`, đặt giá trị mặc định cho tổ chức hiện tại | Bắt buộc |
| **TR-4** | Quyết định trạng thái khởi tạo: mọi học viên bắt đầu ở **0 điểm và hạng thấp nhất** | Cần PO xác nhận |

### Compatibility

| # | Yêu cầu |
| --- | --- |
| **TR-5** | **Quy trình chấm bài:** chấm hết bài tồn trước khi chốt kỳ. Ràng buộc vận hành, không phải chức năng — theo hướng PO đã chọn ở `BA-02` |
| **TR-6** | API hiện có **không đổi contract** — My Learning chỉ **thêm** field. Bản cũ của ứng dụng vẫn chạy được |

### Cutover

| # | Yêu cầu |
| --- | --- |
| **TR-7** | **Ra mắt hai nhịp:** bật `Gamification` (chạy ngầm) → 2–4 tuần xem phân bố thật → chỉnh cấu hình → bật `Visibility in UpLMS` |
| **TR-8** | **Rollback:** tắt `Visibility` trước (học viên không thấy nữa nhưng dữ liệu còn), chỉ tắt `Gamification` khi thật sự phải dừng |
| **TR-9** | Khi bật `Visibility`: **không bắn thông báo hồi tố** (đã có trong BRD §6.4) |

---

## 9. Kiểm tra chiều tenant *(STEP 5)*

| Câu hỏi | Trả lời | Xử lý |
| --- | --- | --- |
| **Có nhúng thêm logic riêng UpBase vào code không?** | ⚠️ **Có một chỗ.** `BR-SKIP` nhắc đích danh **Foundation** — mô hình Foundation → Normal Course là đặc thù UpBase (KB `15` §6) | **`FR-7`**: viết tổng quát *"khoá được đánh dấu bỏ qua thì không tính là hoàn thành"*, không gọi tên Foundation |
| **Có hằng số cứng mới không?** | Trần điểm/ngày · ngưỡng hạng · ngưỡng huy hiệu · số điểm mỗi hành động · múi giờ · **số người liền kề hiển thị ở "Vị trí của tôi"** | 5 cái đầu **phải cấu hình được theo tổ chức**. Số người liền kề chấp nhận hardcode — ghi rõ trong PRD |
| **Bảng mới có `tenant_id` không?** | **Bắt buộc có ở cả 10 thực thể mới** | Đặc biệt chú ý bảng **sổ giao dịch điểm** và **snapshot kỳ** — đây là nơi rò rỉ gây hậu quả nặng nhất |
| **Enum/danh mục mới: hệ thống hay tenant định nghĩa?** | **Hệ thống định nghĩa:** 4 loại huy hiệu · danh mục chỉ số đo lường · loại kỳ lịch.<br>**Tenant định nghĩa:** huy hiệu cụ thể · hạng · chiến dịch · bảng điểm | Khớp `C2` — mở rộng bằng cấu hình |

> ⚠️ **Không dùng `support-groups` để loại trừ Test Account** — bảng này **không có `tenant_id`** (KB `15` §6, mức 🔴). Loại trừ theo cờ trên tài khoản. → `FR-9`

**Chỗ đóng cứng tenant tăng thêm: 1** *(Foundation trong `BR-SKIP`)* — có cách gỡ, chi phí gần bằng 0 nếu làm ngay.

---

## 10. Risk Summary

| # | Risk | Mức | Giảm nhẹ |
| --- | --- | --- | --- |
| R1 | **Hiệu năng bảng xếp hạng** — chưa ước lượng được tải | 🔴 Cao | `OQ-B9`. Giai đoạn chạy ngầm (`TR-7`) là cơ hội đo tải thật trước khi học viên vào |
| R2 | **Ngày đầu bật tính năng thành ngày cày điểm tập thể** | 🔴 Cao | `TR-2` — nạp sẵn dấu khử trùng |
| R3 | **Tài khoản công ty trên bảng xếp hạng công khai** | 🔴 Cao | `CF-1` — PO quyết |
| R4 | **Nhóm học viên chăm nhất bị kẹt ở đáy bảng** vì đã học hết nội dung | 🟠 Vừa | `BI-6` — PO quyết chấp nhận hay xử lý |
| R5 | **Hai hệ thống nói hai điều khác nhau** khi học viên học lại ở lớp khác | 🟠 Vừa | `CF-2` — PO quyết |
| R6 | **Đổi cấu hình tạo ra hai chuẩn** cho cùng một hạng/huy hiệu | 🟠 Vừa | `CF-3` `CF-4` — PO quyết |
| R7 | **Sổ giao dịch điểm tăng tuyến tính** theo hoạt động học, không có cơ chế dọn | 🟠 Vừa | Cần chính sách lưu trữ — `OQ-C5` |
| R8 | Xoá tài nguyên làm hỏng ảnh huy hiệu đã trao | 🟡 Thấp | `CF-5` |

---

## 11. Open Questions

| # | Câu hỏi | Vì sao quan trọng | Người trả lời | Chặn Gate 3? |
| --- | --- | --- | --- | --- |
| **OQ-C1** | **`CF-1` — loại trừ tài khoản `Test Account = Yes` khỏi bảng xếp hạng?** | Người của công ty đứng trên bảng xếp hạng học viên | PO | **Yes** |
| **OQ-C2** | **`CF-2` — học lại nội dung ở lớp khác thì nói gì với học viên?** Hệ thống bảo chưa học, gamification không cộng điểm | Học viên sẽ khiếu nại và không ai giải thích được | PO | **Yes** |
| **OQ-C3** | **Hoạt động trong khoá Trial có tính điểm không?** | `BI-9` — có thể là đường kiếm điểm không mong muốn | PO | **Yes** |
| **OQ-C4** | **`BI-6` — học viên đã học hết nội dung thì kiếm điểm bằng gì?** | Nhóm chăm nhất lại xếp thấp nhất — ngược mục tiêu `O1` | PO | **Yes** |
| **OQ-C5** | **Chính sách lưu trữ sổ giao dịch điểm** — giữ bao lâu, có dọn không | `R7`. Ảnh hưởng thiết kế dữ liệu và `OQ-B9` | PO + Dev | No — Gate 3 |
| **OQ-C6** | **`CF-6` — tắt gamification giữa lúc chiến dịch đang chạy thì chiến dịch xử lý sao?** | Huỷ / giữ nguyên / chốt sớm | PO | No |
| **OQ-C7** | **`CG-11` — có khoá bảng điểm khi đang có chiến dịch chạy không?** | `S17` khoá chiến dịch nhưng không khoá bảng điểm — đổi giữa chừng là đổi luật giữa cuộc chơi | PO | No |
| `OQ-B2` | Dữ liệu tiến độ học có dấu thời gian không | Cần cho `C5`, `C7`, trần điểm/ngày, `TR-2` | Dev | **Yes** |
| `OQ-B9` | Bảng xếp hạng chịu tải được không | `R1` | Dev | **Yes** |
| `OQ-B12` | Thời điểm đạt huy hiệu / hoàn thành khoá / bài Test có lưu được không | `C8`, `S22` | Dev | **Yes** |
| `OQ-B11` | Múi giờ tổ chức khai ở đâu | `C6` `C9` `TR-3` | PO + Dev | No |
| `A24` `A25` | Hai giả định từ Bước 5 chưa được xác nhận | Xem `related-map-v0.2` §10 | PO | No |

---

## 12. Phụ lục — Nguồn đã đọc

| Nguồn | Cụ thể |
| --- | --- |
| **KB nghiệp vụ** | `01-course.md` (`BR-EDIT-07`, `BR-COURSE-INFO-06`) · `03-assessment.md` §1–2, §Rule (`KB-TEST-01`, `01a`, `01b`) · `04-class.md` · `05-grading.md` §9 · `06-user-account.md` · `07-learning-experience.md` §1–3, §10 (`KB-LX-03a/b`, `KB-LX-08`) · `08-certificate.md` · `09-notification-email.md` §1, §7–8 (`KB-CR-01`, `KB-CR-03`) · `11-dashboard-sis.md` |
| **KB kỹ thuật** | `12-data-model.md` · `13-mail-events.md` (mail #10, #29, `KB-MAIL-03`) · `14-api-surface.md` §1–2, §2.2 · `15-product-direction.md` §6 |
| **DB — đọc lại nguồn gốc** | ✅ **Tải trực tiếp từ Lark `Data Architecture` ngày 23/09/2026** (`UpLnd DB Full.html`). 85 bảng · 173 quan hệ · 320 cột — **khớp KB 12**. Quan hệ đã lần: `class_user_instances` (8 FK) · `user_course_section_progress` (4 FK) · `courses_users_certificates` (4 FK) · `course_categories` (FK của 6 bảng) · `resources` (FK của 4 bảng) · `departments` → `staffs` · `tenant` (7 cột, không có múi giờ) |
| **Swagger** | LMS 144 op / 25 nhóm · Ops 548 op / 57 nhóm. Đã soi: toàn bộ endpoint ghi của LMS · nhóm `Quiz Attempt`, `Quiz Attempt Grading`, `Notifications Management`, `User Management`, `Course LMS`, `Certificate`, `Permissions management`, `Roles Management` |
| **Mail** | KB `13` — mail #10, #29 (đang bật) · 8 mail luồng chấm điểm (đang tắt) |
| **Quyết định** | `project-decisions.md` — toàn bộ 40+ dòng · `change-requests.md` CR-001…006 |
| **⚠️ Chưa tra được** | • **Ước lượng tải thật** — không có số liệu về số học viên, số hoạt động hoàn thành mỗi ngày. `R1` và `OQ-B9` chưa định lượng được<br>• **Ba con số ở `Analytics`** (`OQ-B4`) — chưa lấy, nên chưa biết quy mô bài toán<br>• **Cơ chế nộp bài kiểm tra** — không thấy trong Swagger, PO xác nhận có (`BA-01`), nhưng **tôi chưa biết nó phát sinh sự kiện thế nào**<br>• **`Event Test Management` và `Event Management`** — hai nhóm API chưa được PO xác nhận là có tính năng hay không (`❓BA`)<br>• **Nguồn ghi nhận "ngày có mặt"** — PO xác nhận làm được (`BA-03`) nhưng chưa biết bằng cơ chế nào |
