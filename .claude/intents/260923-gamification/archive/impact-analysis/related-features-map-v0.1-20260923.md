# Related Features & Docs Map — Gamification

| | |
|---|---|
| Project | Gamification · **Bước 5** |
| Ngày | 23/09/2026 |
| Input | `docs/brd/brd-v0.6-20260923.md` (Gate 1 `Approved with Notes`) · `project-context.md` |
| Nguồn quét | KB `01`–`15` · schema DB 85 bảng · Swagger LMS **144 op / 25 nhóm** + Ops **548 op / 57 nhóm** |
| Trạng thái | 🟡 **Chờ PO soát** — đủ chưa · có sót · dòng nào không liên quan |

> Mục đích của bước này là **nhận diện**, không phải phân tích. Dòng nào đánh `Existing` thì ở bước sau **không được coi là mới**.
> Chỗ chưa chắc ghi `❓BA` — phải chốt trước khi dựng Impact Matrix.

---

# 🚨 Hai phát hiện cần xử lý trước

## F1 — Không tìm thấy endpoint nộp bài kiểm tra ở cả hai hệ

`Fact` — quét toàn bộ endpoint ghi (`POST`/`PUT`/`PATCH`) của cả hai Swagger:

| Hệ | Nhóm `Quiz Attempt` | Có endpoint ghi không? |
|---|---|---|
| **LMS** | 8 operation | ❌ **Toàn bộ là `GET`** |
| **Ops** | 7 operation | ❌ Không có endpoint nộp bài |
| Ops `Quiz Attempt Grading` | 14 operation | ✅ Có — nhưng là **chấm bài**, không phải nộp bài |

Nghĩa là **hành động "học viên nộp bài kiểm tra" không xuất hiện trong bề mặt API đã quét** — mà đó là một trong ba hành động tính điểm (`S2`).

Ba khả năng, chưa phân biệt được:

1. Swagger tải ngày 23/09 lúc 08:07 **chưa đầy đủ hoặc đã cũ**
2. Việc nộp bài đi qua **một service khác** không nằm trong hai `docs-json` này
3. Có cơ chế khác (job, message queue) mà API không lộ ra

→ `❓BA-01`. **Phải làm rõ trước Gate 2** — không biết sự kiện phát sinh ở đâu thì không thiết kế được lớp bắt sự kiện.

## F2 — Bài Test chấm tay: "thời điểm đạt" lệch xa "thời điểm làm bài"

`Fact` — Ops có `PUT /api/v1/quiz-attempt-gradings/{id}/finish`. Với bài `Manual Grading = Yes`:

```
Học viên nộp bài  ──────(vài ngày)──────►  Mentor chấm xong  ──►  Mới biết đạt hay trượt
      ▲                                           ▲
   lúc học viên nỗ lực                   lúc hệ thống ghi nhận
```

Ba hệ quả:

| # | Hệ quả |
|---|---|
| 1 | **`S22` (ai đạt sớm hơn xếp trên) bị méo.** Hai học viên nộp cùng lúc có thể xếp khác nhau chỉ vì mentor chấm bài này trước bài kia. Thứ hạng phụ thuộc lịch làm việc của mentor, không phụ thuộc nỗ lực học viên |
| 2 | **Điểm có thể rơi vào kỳ khác với kỳ học viên làm bài.** Nộp ngày 30/9, chấm xong ngày 3/10 → điểm vào tháng 10 dù nỗ lực thuộc tháng 9. Với `C7` (một điểm thuộc nhiều kỳ) thì sai lệch này lan sang mọi bảng xếp hạng |
| 3 | **Học viên không được báo.** 8 mail luồng chấm điểm đang tắt (`KB-MAIL-03`), và `S10` chỉ đẩy khi đang online → rất có thể học viên nhận điểm mà không biết vì sao |

`Recommendation` — cân nhắc **lấy thời điểm nộp bài làm mốc ghi nhận**, dù điểm chỉ được cộng sau khi chấm xong. Nhưng đây là quyết định của Gate 3, nêu ở đây để không bị bỏ sót. → `❓BA-02`

---

# 1. Module / tính năng nghiệp vụ

| Hệ | Module | New / Existing | Nguồn | Ghi chú |
|---|---|---|---|---|
| LMS + Ops | **Gamification** | 🆕 **New** | BRD v0.6 | Toàn bộ là mới |
| LMS | **Learning Experience** | Existing | KB `07` | **Nguồn sự kiện chính** — hoàn thành hoạt động. Chỉ đọc |
| LMS + Ops | **Assessment (Test/Quiz/Case Study)** | Existing | KB `03` | Nguồn sự kiện cho `BR-TEST`. **Phải loại Quiz và Case Study ra** |
| Ops | **Grading** | Existing | KB `05` | Nơi xác định đạt/trượt của bài chấm tay → `F2` |
| LMS + Ops | **Course** | Existing | KB `01` | Nguồn sự kiện hoàn thành khoá · `Graded Assignment`, `Pass Point` |
| LMS + Ops | **Certificate** | Existing | KB `08` | Mốc "hoàn thành khoá" |
| LMS + Ops | **Class** | Existing | KB `04` | Không bị sửa, nhưng là lý do sinh ra `C5` |
| LMS + Ops | **User Account** | Existing | KB `06` | Trạng thái `Block` ảnh hưởng `A14` |
| LMS + Ops | **Notification** | Existing | KB `09` | 🟢 Chỉ dùng phía hiển thị. **Không dùng cơ chế gửi hiện có** |
| Ops | **Phân quyền (Casbin)** | Existing | KB `14` · `casbin_rule` | Thêm nhóm quyền mới cho cấu hình gamification |
| Ops | **Tenant / Hồ sơ tổ chức** | ⚠️ **Chưa có** | `TNT.CFG.02` | Module chưa làm. Đợt này chỉ khai tham số múi giờ (`S21`) |
| Ops | **Dashboard / SIS** | Existing | KB `11` | ❓ Có chồng lấn với dữ liệu gamification không → `❓BA-07` |
| Ops | **Group / Department** | Existing *(giao diện ẩn)* | KB `09` · `14` | Hoãn (`N1`). `departments` **chỉ gắn nhân sự**, không gắn học viên |
| LMS | **Storyline** | Existing | KB `10` | ❓ `class_user_storyline_progress` có phải nguồn sự kiện riêng không → `❓BA-04` |
| LMS + Ops | **Examination / Entrance Test** | Existing *(KB chưa phủ)* | KB `14` §1–2 | ❓ Có tính là "bài Test" không → `❓BA-06` |

---

# 2. Màn hình

| Hệ | Màn hình | New / Existing | Nguồn | Ghi chú |
|---|---|---|---|---|
| LMS | **Thành tích của tôi** | 🆕 New | `S11` · US1, US4 | Điểm · hạng · huy hiệu đã có · huy hiệu sắp đạt |
| LMS | **Lịch sử điểm** | 🆕 New | `S9` · US3 | Có thể là tab trong màn trên |
| LMS | **Bảng xếp hạng** | 🆕 New | `S14` · US6, US7, US8 | Chọn kỳ · vị trí của tôi · lịch sử kỳ |
| LMS | Thông báo đẩy khi đang online | 🆕 New | `S10` · US2 | **Không dùng hộp thư thông báo hiện có** |
| Ops | **Cấu hình bảng điểm** | 🆕 New | `S1` · US9 | |
| Ops | **Quản lý huy hiệu** | 🆕 New | `S4`, `S5` · US10 | |
| Ops | **Quản lý hạng** | 🆕 New | `S6` · US11 | |
| Ops | **Quản lý chiến dịch** | 🆕 New | `S15`–`S17` · US12, US13 | |
| Ops | **Bật/tắt gamification** | 🆕 New | `S12` · US16 | Hai công tắc |
| Ops | Màn phân quyền | Existing | US17 | Thêm resource mới, không đổi màn |
| LMS | Course Detail · Activity | Existing | KB `07` | **Không sửa** — chỉ là nơi phát sinh sự kiện |
| LMS | My Learning | Existing | KB `07` | ❓ Có hiện điểm/hạng ở đây không → `❓BA-08` |

---

# 3. Data model / Entity

## 3.1 Bảng hiện có — chỉ đọc, không sửa

| Bảng | Vai trò với gamification | Nguồn |
|---|---|---|
| `users` | Chủ thể nhận điểm | KB `12` |
| `class_user_instances` | Cầu nối `users` ↔ `classes`. **Mọi bảng tiến độ treo vào đây** → lý do của `C5` | KB `12` |
| `user_course_section_progress` | **Nguồn sự kiện "hoàn thành hoạt động"** | KB `12` |
| `class_user_storyline_progress` | ❓ Nguồn sự kiện riêng? → `❓BA-04` | KB `12` |
| `quiz_attempts` | Nguồn sự kiện bài Test | KB `12` |
| `quiz_attempt_gradings` | Nơi chốt đạt/trượt bài chấm tay → `F2` | KB `12` |
| `class_user_scores` | Điểm bài kiểm tra (1-1 với `class_user_instances`) | KB `12` |
| `courses_users_certificates` | **Nguồn sự kiện "hoàn thành khoá"**. Là bảng duy nhất nối thẳng `users` | KB `12` |
| `quizzes` | `Graded Assignment`, `Pass Point` → `BR-TEST` | KB `03` |
| `courses` · `course_sections` | Đơn vị nội dung để chống cộng trùng (`C5`) | KB `12` |
| `classes` | Không dùng trực tiếp ở đợt này | KB `12` |
| `tenant` | Nơi gắn cấu hình (`C1`). **Không có trường múi giờ** → `S21` | KB `12` |
| `casbin_rule` | Phân quyền cấu hình | KB `12` |
| `resources` · `attachment-files` | Ảnh huy hiệu, ảnh hạng (`A9`) | KB `12` |
| `notifications` · `notification_user_instances` | 🟢 **Không dùng** — `S10` không đi qua cơ chế này | KB `12` |
| `groups` · `group_user_instances` | Hoãn (`N1`) | KB `12` |
| `departments` | Hoãn (`N1`). **Chỉ gắn `staffs`, không gắn `users`** | KB `12` |

## 3.2 Thực thể mới — thiết kế chi tiết ở Gate 2

| Thực thể | Mục đích | Ràng buộc chi phối |
|---|---|---|
| **Cấu hình gamification** | Hai công tắc · múi giờ · trần điểm/ngày | `C1`, `C6`, `C9`, `S12`, `S21` |
| **Quy tắc cộng điểm** | Hành động → số điểm, bật/tắt | `C2`, `C4` |
| **Sổ giao dịch điểm** | Từng lần cộng, kèm nguồn và thời điểm | `C3`, `C8` — **nền của gần như mọi thứ** |
| **Dấu nội dung đã tính điểm** | Chống cộng trùng theo người học | `C5` |
| **Ngày có mặt của học viên** | Nguồn cho `S3` và huy hiệu Tích cực | `C9`, `❓BA-03` |
| **Danh mục chỉ số đo lường** | Dùng chung cho huy hiệu · hạng · xếp hạng | `S23`, `C2` |
| **Huy hiệu** + **huy hiệu đã đạt** | 4 loại, ngưỡng đếm | `S5`, `C8` |
| **Hạng** + **hạng hiện tại** | Ngưỡng theo nhiều chỉ số | `S6`, `A3` |
| **Chiến dịch** | Khoảng · phạm vi · chỉ số · trạng thái | `S15`–`S17`, `N3` |
| **Snapshot kết quả kỳ** | Kết quả đóng băng, kèm chỉ số đã dùng | `S19`, `C7`, `O5` |

---

# 4. API / Integration / Job

## 4.1 Endpoint hiện có — nguồn sự kiện

| Hệ | Endpoint | Vai trò | Ghi chú |
|---|---|---|---|
| LMS | `PUT /api/v1/course-sections/course/{class_id}/section/{section_id}/progress` | **Điểm móc chính** cho "hoàn thành hoạt động" | DTO `UpdateUserCourseSectionProgressDto` |
| LMS | `PUT /api/v1/course-sections/{class_id}/storyline/{course_section_id}/retake` | ⚠️ **Học lại storyline** — liên quan trực tiếp tới chống cộng trùng (`C5`) | `❓BA-04` |
| LMS | ❌ *(không tìm thấy)* | Nộp bài kiểm tra | **`F1`** |
| Ops | `PUT /api/v1/quiz-attempt-gradings/{id}/finish` | Chốt kết quả bài chấm tay | **`F2`** |
| Ops | `POST /api/v1/quiz-attempt-gradings/question-gradings/{id}/grade` | Chấm từng câu | |
| Ops | `POST /api/v1/quiz-attempt-gradings/request-regrading` · `request-review` | ⚠️ **Chấm lại** — điểm đã cộng có bị tính lại không → `❓BA-05` | |
| Ops | `POST /api/v1/courses/{id}/certificates` · `Certificate` (6 op) | Nguồn "hoàn thành khoá" | |
| LMS | `GET /api/v1/users/course-certificate/count` | Đã có sẵn số khoá hoàn thành | Có thể tái dùng cho chỉ số |
| LMS | `GET /api/v1/users/activities` *(tham số `ip`, `type`)* | ❓ Có phải nguồn cho "ngày có mặt" không → **`❓BA-03`** | Response chưa khai trong Swagger |
| LMS | `POST /api/v1/courses/catalog/enroll` · `un-enroll` | ⚠️ Học viên **tự huỷ ghi danh** — điểm đã nhận xử lý sao → `❓BA-09` | |
| LMS | `PUT /api/v1/courses/{class_id}/skip-foundation` | ⚠️ **Bỏ qua Foundation** — có tính là hoàn thành không → `❓BA-10` | |
| LMS | `POST /api/v1/notifications/device-token` | 🟢 Push đã có sẵn — có thể tái dùng cho `S10` | |
| Ops | `Permissions management` (2) · `Roles Management` (8) | Thêm resource phân quyền mới | |

## 4.2 Endpoint mới

Toàn bộ API của gamification là mới: cấu hình · huy hiệu · hạng · chiến dịch · bảng xếp hạng · lịch sử điểm · trang thành tích. Danh sách chi tiết ở Gate 2.

## 4.3 Job / tác vụ nền

| Job | New/Existing | Ghi chú |
|---|---|---|
| **Chốt kỳ lịch và lưu snapshot** | 🆕 New | Chạy tại biên kỳ theo **múi giờ tổ chức** (`C6`) |
| **Chốt chiến dịch khi hết hạn** | 🆕 New | |
| **Tính sẵn bảng xếp hạng** | 🆕 New *(nếu chọn hướng này)* | Phụ thuộc `OQ-B9` |
| Cronjob nhắc bài kiểm tra (`KB-MAIL-08`) | Existing | Không liên quan, ghi để loại trừ |

---

# 5. Role / Permission

| Vai trò | New/Existing | Quyền cần | Nguồn |
|---|---|---|---|
| **Học viên** | Existing | Xem thành tích, lịch sử điểm, bảng xếp hạng của **chính mình và của người khác** (`A15` — công khai) | KB `06` |
| **Nhân sự vận hành** | Existing | Cấu hình điểm · huy hiệu · hạng · chiến dịch · bật/tắt | `S13` · US17 |
| **Quản trị** | Existing | Gán quyền cấu hình gamification | US17 |
| **L&D** | Existing | ❓ Quyền xem có khác học viên không → `❓BA-11` | Stakeholder mới |
| **Quản lý trực tiếp** | Existing | ⚠️ **Chưa có công cụ nào ở đợt này** — cần `US18` (hoãn) | Stakeholder mới |
| Mentor / Giáo viên | Existing | ❓ Có thấy bảng xếp hạng không → `❓BA-11` | KB `05` |

> Hệ thống dùng **Casbin** (`casbin_rule`, ptype + v0–v6). Thêm resource mới, không đổi cơ chế.

---

# 6. Business rule hiện có bị chạm

| Mã rule | Nội dung | Chạm thế nào |
|---|---|---|
| `KB-LX-03a` | Activity chứa Video hoàn thành khi **xem ≥80% thời lượng** | Điều kiện phát sinh sự kiện cộng điểm |
| `KB-LX-03b` | Activity chứa Text/Ảnh hoàn thành khi **mở hiển thị** | Rủi ro đã chấp nhận (`N2`, §6.5) |
| `KB-LX-04` | `Graded Activity` là hoạt động **bắt buộc** để tính điểm khoá | ❓ Gamification có phân biệt không → `❓BA-12` |
| `KB-TEST-01` | `Manual Grading = Yes` → ép `Graded Assignment = Yes`, `Attempt = 1` | Bảo đảm bài chấm tay luôn có ngưỡng đạt |
| `KB-TEST-01a` | **`Pass Point` chỉ tồn tại khi `Graded Assignment = Yes`** | Nền của `BR-TEST` |
| `KB-TEST-01b` | **Quiz và Case Study không có ngưỡng đạt** | Nền của `BR-TEST` · `N6` |
| `BR-EDIT-07` | Test đã có người làm → **không sửa** `Graded Assignment`, `Pass Point` | 🟢 Bảo đảm quy tắc đếm **ổn định**, không tính lại ngược |
| `BR-COURSE-INFO-06` | `Pass Point` là điểm tối thiểu để nhận chứng chỉ | Định nghĩa "hoàn thành khoá" |
| `KB-CR-03` / `KB-CR-04` | Comment Replier **tự động thêm/xoá học viên khỏi lớp** | ⚠️ Sinh ra lượt ghi danh ngoài ý muốn → củng cố `C5` |
| `KB-MAIL-03` | 8 mail luồng chấm điểm **đang tắt** | Học viên không được báo khi chấm xong → `F2` hệ quả 3 |
| `KB-NOTI-05` | Thông báo gửi theo job nửa tiếng | 🟢 **Không còn liên quan** — `S10` không dùng cơ chế này |

---

# 7. NFR

| Khía cạnh | Vấn đề | Trạng thái |
|---|---|---|
| **Hiệu năng — bảng xếp hạng** | Tính thứ hạng từ sổ giao dịch theo khoảng ngày, toàn tổ chức, nhiều kỳ lồng nhau, ba chỉ số | 🔴 `OQ-B9` — chặn Gate 2 |
| **Hiệu năng — ghi sự kiện** | Mỗi hoạt động hoàn thành sinh một lần xử lý điểm | Chưa ước lượng |
| **Dung lượng** | Sổ giao dịch điểm tăng tuyến tính theo hoạt động học | Chưa ước lượng |
| **Tính đúng đắn** | Snapshot kỳ đã chốt **không được đổi** dù dữ liệu gốc thay đổi về sau | `O5`, `A14` |
| **Múi giờ** | Biên kỳ và biên ngày phải nhất quán | `C6`, `C9` |
| **Riêng tư** | ✅ Đã chốt — bảng xếp hạng công khai danh tính | `A15` |

---

# 8. Danh sách `❓BA` phải chốt trước Gate 2

| # | Câu hỏi | Ảnh hưởng nếu không chốt | Owner |
|---|---|---|---|
| **❓BA-01** | **Học viên nộp bài kiểm tra qua đâu?** Không tìm thấy endpoint ghi nào ở cả hai Swagger | Không thiết kế được lớp bắt sự kiện cho một trong ba hành động tính điểm | Dev |
| **❓BA-02** | **Bài chấm tay: mốc ghi nhận là lúc nộp hay lúc chấm xong?** | `S22` bị méo; điểm rơi nhầm kỳ | PO + Dev |
| **❓BA-03** | **Nguồn "ngày học viên có mặt"** — `GET /users/activities` có dùng được không? | `S3` và huy hiệu Tích cực không có nguồn | Dev |
| **❓BA-04** | **Storyline có phải nguồn sự kiện riêng không?** Có endpoint `retake` — học lại thì chống cộng trùng thế nào | Bỏ sót một loại nội dung học, hoặc cày điểm qua retake | PO + Dev |
| **❓BA-05** | **Chấm lại (`request-regrading`) thì điểm đã cộng xử lý sao?** Học viên từ đạt thành trượt hoặc ngược lại | Điểm và huy hiệu có thể phải thu hồi — mâu thuẫn `A5` | PO |
| **❓BA-06** | **Examination / Entrance Test có tính là "bài Test" không?** Nằm trong vùng KB chưa phủ | Đếm thừa hoặc thiếu ở huy hiệu loại Test | PO |
| **❓BA-07** | **Dashboard SIS có chồng lấn với dữ liệu gamification không?** | Hai chỗ cùng báo cáo mức độ tham gia, có thể lệch nhau | PO |
| **❓BA-08** | **Có hiện điểm/hạng ở màn My Learning không**, hay chỉ ở trang Thành tích? | Phạm vi màn hình | PO |
| **❓BA-09** | **Học viên tự huỷ ghi danh (`un-enroll`) thì điểm đã nhận xử lý sao?** | Có thể cày điểm bằng ghi danh–huỷ–ghi danh lại | PO |
| **❓BA-10** | **`skip-foundation` có tính là hoàn thành không?** | Đếm sai "số khoá hoàn thành" | PO |
| **❓BA-11** | **L&D, Mentor, Giáo viên có xem được bảng xếp hạng không?** | Phân quyền | PO |
| **❓BA-12** | **Gamification có phân biệt `Graded Activity` với hoạt động thường không?** | Ảnh hưởng số điểm theo loại hoạt động | PO |

---

# 9. Câu hỏi soát cho PO

1. **Đủ chưa** — còn module, màn hình, hay luồng nào bị chạm mà tôi chưa liệt kê?
2. **Có dòng nào không liên quan** — nên bỏ khỏi phạm vi quét?
3. **12 câu `❓BA`** — câu nào anh trả lời được ngay, câu nào cần hỏi Dev?
4. **Có KB hay PRD cũ nào nên đọc thêm** trước khi dựng Impact Matrix?

**Không sang Bước 6 cho tới khi phạm vi được chốt.**
