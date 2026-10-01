# Clarified Requirements — Gamification

| | |
|---|---|
| Project | Gamification |
| Ngày | 23/09/2026 |
| Input | `working/raw-inputs/yeu-cau-goc-20260923.md` |
| Nguồn đối chiếu | KB `01`–`15` · schema DB 85 bảng (Lark `Data Architecture`, đối chiếu 23/09/2026) · Swagger LMS 153 op + Ops 555 op |
| Trạng thái | 🟢 **v0.2** — 8/9 blocking question đã có đáp án; còn **OQ-07** chờ PO chọn phương án |

## Change Log

| Version | Ngày | Nội dung |
|---|---|---|
| v0.1 | 23/09/2026 | Bản đầu — 9 blocking question |
| **v0.2** | 23/09/2026 | PO trả lời 9 câu. Thu hẹp phạm vi (bỏ lộ trình · kỹ năng · leaderboard). Đính chính logic hoàn thành Video. Bổ sung stakeholder Đội truyền thông nội bộ. Thêm §13 phân tích OQ-07 theo yêu cầu PO |

> Bản này **cập nhật tại chỗ** thay vì tạo file mới, vì v0.1 chưa qua Gate nào — vẫn đang trong vòng lặp Bước 2–3 của workflow. Nội dung cũ được giữ nguyên, phần đổi đánh dấu rõ ở §14.

---

## 1. Chuẩn hoá input

| Nhóm | Nội dung |
|---|---|
| **Stakeholder request** | PO yêu cầu xây chức năng gamification |
| **Problem** | ⚠️ **Chưa được nêu.** Input chỉ nói mục tiêu ("thúc đẩy động lực học"), không mô tả vấn đề hiện tại → xem `OQ-09` |
| **Expected outcome** | Học viên có động lực học hơn |
| **Users / roles** | Học viên (UpLMS) — nhận điểm/huy hiệu/hạng · Vai trò cấu hình phía Ops **chưa được nêu** → `OQ-08` |
| **Systems / modules** | UpLMS (hiển thị) · UpLMS Ops (cấu hình) · chạm Learning Experience, Course, Assessment, Certificate, Notification, User, Class |
| **Constraints / dependencies** | Bật/tắt ở cấp tenant · tái dùng hệ thống thông báo sẵn có · hệ thống đã có khoá học và học viên |
| **Proposed solution** | ⚠️ **Toàn bộ 11 dòng trong bảng là giải pháp đã được nghĩ sẵn**, không phải vấn đề. Xem §2 |

### ⚠️ Input là bản thiết kế, không phải bản mô tả vấn đề

Bảng 11 dòng mô tả **hệ thống sẽ trông như thế nào**, không mô tả **vì sao cần**. Theo quy ước, toàn bộ nội dung này là `Recommendation` của PO, không phải yêu cầu đã chốt.

Điều này **không làm input kém giá trị** — nó rất rõ ràng và có chủ đích (ba dòng còn tự kèm lý do: chu kỳ điểm, lịch sử điểm, chống cày điểm). Nhưng nó có hệ quả thật:

- Mục `Problem` và `Analytics` của BRD/PRD hiện **không có nguồn** — không biết học viên đang mất động lực ở đâu, đo bằng gì
- Không có cách đánh giá phương án thay thế, vì không biết tiêu chí thành công
- Khi Dev/QA hỏi "tại sao rule này chứ không phải rule kia", không có căn cứ trả lời

→ `OQ-09` xử lý việc này.

---

## 2. Requirement candidates

| ID | Requirement Candidate | Type | Source | Confidence | Notes |
|---|---|---|---|---|---|
| RC-01 | Cấu hình hành động nào được bao nhiêu điểm; bật/tắt từng hành động | Functional · Data | Bảng dòng 1 | **High** | Cần màn cấu hình phía Ops (chưa nêu) |
| RC-02 | Danh mục 6 hành động tính điểm | Business Rule | Bảng dòng 2 | **Medium** | **3/6 loại chưa có nền dữ liệu** — xem §3 |
| RC-03 | Quản lý huy hiệu: tên · hình · mô tả · điều kiện đạt | Functional · Data | Bảng dòng 3 | **High** | Cần chỗ lưu ảnh — `resources` đã có |
| RC-04 | 5 loại điều kiện huy hiệu | Business Rule | Bảng dòng 4 | **Medium** | **1/5 loại chưa có nền dữ liệu** (kỹ năng) |
| RC-05 | Hạng người học theo ngưỡng điểm: tên · hình · ngưỡng | Functional · Data | Bảng dòng 5 | **High** | ⚠️ Va tên với `Course Level` và `Staff Level` |
| RC-06 | Hai loại điểm tách nhau: tích luỹ vĩnh viễn (xét hạng) + theo kỳ (thi đua) | Data · Business Rule | Bảng dòng 6 | **High** | "Kỳ" chưa được định nghĩa — `OQ-04` |
| RC-07 | Chống cày điểm: không cộng khi học lại · trần điểm/ngày · không cộng khi bỏ qua quá nhanh | Business Rule | Bảng dòng 7 | **Medium** | ⚠️ **Xung đột với logic hoàn thành hiện tại** — xem §4 |
| RC-08 | Lịch sử điểm — học viên xem được từng lần cộng đến từ đâu | Screen-Report · Data | Bảng dòng 8 | **High** | Bắt buộc lưu log giao dịch điểm, không chỉ số dư |
| RC-09 | Thông báo khi nhận điểm / huy hiệu / lên hạng | API-Integration | Bảng dòng 9 | **Medium** | ⚠️ Giả định "dùng cái sẵn có" cần kiểm — xem §5 |
| RC-10 | Trang "Thành tích của tôi": điểm · hạng · huy hiệu đã có · huy hiệu sắp đạt kèm phần còn thiếu | Screen-Report | Bảng dòng 10 | **High** | "Sắp đạt" cần tính tiến độ từng huy hiệu |
| RC-11 | Bật/tắt gamification ở cấp tổ chức (tenant) | Functional · Data | Bảng dòng 11 | **High** | Chưa rõ tắt thì dữ liệu đã tích xử lý ra sao — `OQ-07` |
| **RC-12** | **Bảng xếp hạng (leaderboard)** | Screen-Report | `[suy ra]` từ dòng 6 + dòng 8 | **Low** | 🚨 **Chưa được khai báo thành yêu cầu** — xem §2.1 |
| RC-13 | Màn cấu hình gamification phía Ops | Screen-Report | `[suy ra]` từ RC-01/03/05 | **Low** | Không có màn này thì RC-01/03/05 không dùng được |
| RC-14 | Phân quyền: vai trò nào được cấu hình gamification | Role-Permission | `[suy ra]` | **Low** | Hệ thống dùng Casbin — `OQ-08` |

### 2.1 🚨 RC-12 — Bảng xếp hạng bị nhắc hai lần nhưng không có dòng yêu cầu

Từ "xếp hạng" xuất hiện **hai lần trong input, cả hai đều ở vị trí lý do chứ không phải yêu cầu**:

> Dòng 6: *"điểm theo kỳ để **xếp hạng thi đua**"*
> Dòng 8: *"Điểm không giải thích được thì không ai tin **bảng xếp hạng**"*

Nhưng không có dòng nào mô tả bảng xếp hạng, và dòng 10 (Trang thành tích của tôi) **chỉ hiển thị dữ liệu của chính người học** — điểm, hạng, huy hiệu của mình.

`Assumption`: bảng xếp hạng nằm trong ý định của PO nhưng bị quên khi liệt kê.

Đây là chỗ đáng chặn sớm vì:
- Nếu **có** bảng xếp hạng → toàn bộ RC-06 (điểm theo kỳ) mới có lý do tồn tại, và phát sinh loạt vấn đề riêng: phạm vi so sánh (toàn tổ chức / theo lớp / theo phòng ban), quyền riêng tư (học viên có muốn điểm mình bị người khác thấy không), xử lý đồng hạng
- Nếu **không** có → RC-06 mất mục đích, chỉ cần một loại điểm duy nhất, và **data model đơn giản đi đáng kể**

→ `OQ-01`

---

## 3. Đối chiếu KB — cái gì đã có, cái gì chưa

Đã tra: KB `01`–`15` · 85 bảng DB · 708 operation Swagger.

### 3.1 Toàn bộ gamification là greenfield

| Nguồn | Kết quả |
|---|---|
| KB `01`–`15` | Không có khái niệm điểm thưởng / huy hiệu / hạng / xếp hạng |
| DB 85 bảng | Không có bảng nào cho gamification |
| Swagger 708 op | Không có endpoint nào |

`Fact` — độ chắc chắn **cao**: DB và Swagger phủ toàn hệ thống, không chỉ phần KB phủ được, nên kết luận này không rơi vào vùng "KB chưa phủ" (KB `14` §1–2).

### 3.2 Nền dữ liệu cho từng hành động tính điểm (RC-02)

| Hành động (input) | Nền dữ liệu hiện có | Đánh giá |
|---|---|---|
| Hoàn thành hoạt động | ✅ `user_course_section_progress` · KB `07` §3 định nghĩa rõ điều kiện hoàn thành | **Có** — nhưng xem §4 |
| Hoàn thành khoá | ✅ `courses_users_certificates` · Pass Point (`BR-COURSE-INFO-06`) | **Có** |
| **Hoàn thành lộ trình** | ❌ Không có bảng, không có API, không có trong KB | 🚨 **Không có** — `OQ-02` |
| Đạt bài kiểm tra | ✅ `quiz_attempts` · `quiz_attempt_gradings` · `class_user_scores` | **Có** — "đạt" cần định nghĩa, `OQ-05` |
| Đạt điểm cao | ⚠️ Có điểm, nhưng "cao" là ngưỡng nào? | `OQ-05` |
| **Đăng nhập nhiều ngày liên tiếp** | ⚠️ Không có bảng lịch sử đăng nhập của **học viên**. `staff_sessions` chỉ cho nhân sự Ops. Có `GET /api/v1/users/activities` (tham số `ip`, `type`) — **chưa rõ có lưu lịch sử đăng nhập không** | 🚨 `❓BA` — `OQ-03` |

### 3.3 Nền dữ liệu cho điều kiện huy hiệu (RC-04)

| Điều kiện (input) | Nền dữ liệu | Đánh giá |
|---|---|---|
| Theo số lượng hoàn thành | ✅ Đếm được từ progress | Có |
| Theo chuỗi ngày liên tiếp | ⚠️ Phụ thuộc `OQ-03` | Chưa chắc |
| Theo mốc thời gian | ✅ Timestamp có sẵn | Có |
| Theo hoàn thành một nội dung cụ thể | ✅ `course_sections` · Activity | Có |
| **Theo đạt một kỹ năng cụ thể** | ⚠️ **Không có khái niệm "kỹ năng"**. Gần nhất là **Learning Outcome** — 3 bảng (`course_outcomes`, `course_learning_outcomes`, `course_section_outcome_instances`) + API `Course Learning Outcome Management` ở cả LMS và Ops | 🚨 `OQ-06` |

> KB `15` §định hướng ghi rõ 3 bảng outcome này là *"hạ tầng sơ khai gần nhất với competency"*. Nếu "kỹ năng" = Learning Outcome thì làm được; nếu là khái niệm mới thì đây là **một tính năng riêng, không thuộc gamification**.

### 3.4 Cái đã có và tái dùng được

| Thứ | Nơi có | Dùng cho |
|---|---|---|
| Hệ thống tiến độ học | `user_course_section_progress` · `class_user_storyline_progress` | Nguồn sự kiện cộng điểm |
| Kết quả bài kiểm tra | `quiz_attempts` · `class_user_scores` | Nguồn sự kiện |
| Cấp chứng chỉ | `courses_users_certificates` | Nguồn sự kiện |
| Hộp thư thông báo trong app | `GET /notifications` · `count-unread` · `mark-read` · `pinned` | Hiển thị thông báo thành tích |
| **Push notification** | `POST /api/v1/notifications/device-token` | Đẩy thông báo real-time |
| Lưu ảnh | `resources` · `attachment-files` | Ảnh huy hiệu, ảnh hạng |
| Hạ tầng đa tenant | `tenant` (`id`, `type`, `billing_model`, `contract_type`…) | Bật/tắt cấp tổ chức |
| Mẫu cấu hình theo tenant | `caching_settings` | Mẫu để làm bảng cấu hình gamification |
| Phân quyền | `casbin_rule` (ptype, v0–v6) | Quyền cấu hình |

---

## 4. 🚨 Xung đột: chống cày điểm vs logic hoàn thành hiện tại

`Fact` — KB `07` §3, nguyên văn từ User Guide:

| Nội dung trong Activity | Điều kiện được tính **Hoàn thành** |
|---|---|
| Chứa Quiz | Phải hoàn thành Quiz |
| Chứa Video | **Chỉ cần play video** |
| Chứa Text / Ảnh | **Chỉ cần mở hiển thị** |

Nghĩa là hiện tại một Activity dạng Text được tính hoàn thành **ngay khi hiển thị ra màn hình**. Video được tính hoàn thành khi **bấm play**, không cần xem hết.

**Hệ quả nếu cộng điểm theo "hoàn thành hoạt động" (RC-02):** học viên bấm lướt qua toàn bộ Activity dạng Text trong một khoá sẽ nhận đủ điểm mà không học gì. Đây chính là thứ RC-07 muốn chặn — nhưng nguyên nhân nằm ở **logic hoàn thành có sẵn**, không nằm ở gamification.

Ba lựa chọn, mỗi cái một cái giá:

| Hướng | Nội dung | Đánh đổi |
|---|---|---|
| **A** | Gamification dùng điều kiện riêng, chặt hơn (thời gian tối thiểu trên Activity, % video đã xem) | Hai định nghĩa "hoàn thành" song song trong một sản phẩm → học viên thấy Activity ✅ xanh nhưng không được điểm, dễ khiếu nại |
| **B** | Siết logic hoàn thành hiện tại cho cả hệ thống | Đổi hành vi tính năng đang chạy, ảnh hưởng tiến độ học và điều kiện cấp chứng chỉ của **học viên hiện hữu** → phải xử lý dữ liệu cũ |
| **C** | Không cộng điểm cho Activity dạng Text/Ảnh; chỉ cộng cho Quiz và mốc lớn (hoàn thành khoá, đạt bài kiểm tra) | Mất phần lớn cơ hội cộng điểm thường xuyên — mà cộng điểm nhỏ đều đặn mới là thứ tạo thói quen |

`Recommendation` — **hướng A**, nhưng chưa chốt: đây là quyết định của Gate 3 sau khi có Impact Matrix. Nêu ở đây vì nó ảnh hưởng tới phạm vi (hướng B kéo theo sửa module Learning Experience đang chạy).

→ `OQ-10`

---

## 5. ⚠️ "Dùng hệ thống thông báo sẵn có, chỉ thêm sự kiện mới" — giả định cần kiểm

`Fact` — Swagger cho thấy hệ thống thông báo chia hai phía:

| Phía | Endpoint | Tính chất |
|---|---|---|
| **UpLMS (học viên đọc)** | `GET /notifications` · `count-unread` · `mark-read` · `mark-all-read` · `pinned` · `POST device-token` | ✅ Hộp thư + push đã có, **tái dùng được** |
| **Ops (tạo thông báo)** | `POST /notifications` với `{title, type, action, send_time, send_finish_time, groups, files}` | ⚠️ Đây là **trình soạn thảo gửi thủ công theo nhóm**, không phải API sự kiện |

Ba điểm cần lưu ý:

1. **Không có đường tạo thông báo theo sự kiện cho từng người.** Cái đang có là soạn tay → chọn nhóm người nhận → hẹn giờ gửi. Gamification cần "cộng 10 điểm cho user X lúc 14:32" — cơ chế khác hẳn.
2. **`KB-NOTI-05`: thời gian gửi chỉ nhận phút = 00 hoặc 30** (job chạy theo nửa tiếng). Thông báo thành tích mà trễ tới 30 phút thì mất hoàn toàn tác dụng khích lệ.
3. **KB `09` §1: 3/4 page của module Notification phía Ops đang `hidden`** — phần gửi thủ công. Không chặn việc đọc thông báo phía học viên, nhưng cần biết khi thiết kế màn cấu hình.

`Assumption`: phần **hiển thị** tái dùng được; phần **sinh thông báo** phải làm mới. "Chỉ thêm sự kiện mới" nhẹ hơn thực tế.

### 5.1 Hai va chạm với 30 mail event đang chạy (KB `13`)

**a) Trùng thông báo khi hoàn thành khoá** — `Fact`

| Mail | Nội dung | Trạng thái |
|---|---|---|
| #10 | Hoàn thành khoá học + link certificate | 🟢 **đang chạy** |
| #29 | Hoàn thành khoá học (không kèm chứng chỉ) | 🟢 **đang chạy** |

Học viên hoàn thành khoá **đã nhận mail rồi**. Nếu gamification bắn thêm "bạn vừa nhận N điểm" cho cùng sự kiện, học viên nhận hai thông báo cho một việc. Cần chốt: gộp điểm vào mail sẵn có, hay tách riêng kênh trong app.

**b) Ngược lại — luồng chấm điểm hiện không có thông báo nào** — `Fact`

KB `13` §Chấm điểm + `KB-MAIL-03`: **8 mail thuộc luồng chấm điểm đang tạm ngưng kích hoạt**, trong đó có **mail #19 "Báo học viên bài đã chấm xong"**.

Nghĩa là hiện tại học viên **không được báo khi bài đã chấm xong**. Nếu gamification cộng điểm cho "đạt bài kiểm tra", thông báo "+N điểm" sẽ là **thông báo đầu tiên và duy nhất** học viên nhận được về bài kiểm tra đó — biết mình được điểm thưởng trước khi biết bài đã chấm.

`Recommendation`: nêu ở Gate 2. Đây có thể là lý do tốt để bật lại mail #19 trước, nhưng **đó là quyết định của luồng Grading, không phải của gamification** — không tự gộp vào phạm vi.

→ `OQ-11`

---

## 6. 🚨 Dữ liệu học tập gắn với **lớp**, không gắn với **người**

`Fact` — quan hệ khoá ngoại trong schema:

```
users ──< class_user_instances >── classes
               │
               ├──< user_course_section_progress   (tiến độ học)
               ├──< class_user_storyline_progress
               ├──< quiz_attempts
               └──1  class_user_scores
```

Mọi bảng tiến độ học đều treo vào `class_user_instances` (**một lượt ghi danh vào lớp**), không treo vào `users`. Ngoại lệ duy nhất là `courses_users_certificates` — có `user_id` trực tiếp.

**Hệ quả cho RC-07 "không cộng điểm khi học lại nội dung đã hoàn thành":**

Một học viên học **cùng một khoá qua hai lớp** sẽ có hai bản ghi tiến độ độc lập. Nếu chống cộng trùng theo `class_user_id` thì vẫn được cộng điểm hai lần cho cùng một nội dung — đúng kịch bản cày điểm mà RC-07 muốn chặn, nhưng nguyên nhân là **cấu trúc dữ liệu**, không phải hành vi gian lận.

Chống cộng trùng phải theo `(user_id, course_section_id)` hoặc `(user_id, activity_id)`, tức là **cắt ngang lớp**.

Đây không phải tình huống hiếm: `KB-CR-03` cho thấy hệ thống **tự động thêm học viên vào lớp** khi thêm vào nhóm Comment Replier, mỗi khoá một lớp. Học viên có thể bị ghi danh nhiều lớp mà không chủ động.

→ `OQ-12`

---

## 7. ⚠️ Va tên với khái niệm đang dùng

| Từ trong yêu cầu | Đã bị chiếm bởi | Rủi ro |
|---|---|---|
| **Điểm / Point** | `Pass Point` — điểm tối thiểu để nhận chứng chỉ (`BR-COURSE-INFO-06`) · `class_user_scores` — điểm bài kiểm tra | Học viên và vận hành nhầm điểm thưởng với điểm học |
| **Hạng / Level** | `Course Level Management` (độ khó khoá học) · `Staff Level` (cấp bậc nhân sự) — cả hai là nhóm API đang chạy | Ba khái niệm cùng tên "Level" trong một sản phẩm |

`Recommendation`: chốt từ vựng **trước khi viết PRD**, vì tên sẽ đi vào tên bảng, tên endpoint, nhãn UI và tài liệu Dev/QA. Gợi ý: điểm thưởng = **Reward Point** (hoặc XP), hạng = **Rank** / **Tier** (tránh Level).

Không phải blocking — nhưng sửa sau khi Dev đã code thì đắt. → `OQ-13` (non-blocking)

---

## 8. Scope sơ bộ

> ⚠️ Scope này **chưa chốt** — phụ thuộc `OQ-01`, `OQ-02`, `OQ-06`.

### In Scope

- Cấu hình quy tắc cộng điểm theo hành động, bật/tắt từng hành động (RC-01)
- Cộng điểm cho các hành động **đã có nền dữ liệu**: hoàn thành hoạt động · hoàn thành khoá · đạt bài kiểm tra · đạt điểm cao (RC-02 một phần)
- Quản lý huy hiệu và điều kiện đạt (RC-03, RC-04 — trừ điều kiện "kỹ năng")
- Hạng người học theo ngưỡng điểm (RC-05)
- Hai loại điểm: tích luỹ vĩnh viễn + theo kỳ (RC-06)
- Cơ chế chống cày điểm (RC-07)
- Lịch sử cộng điểm cho học viên (RC-08)
- Thông báo thành tích (RC-09)
- Trang "Thành tích của tôi" (RC-10)
- Bật/tắt gamification cấp tenant (RC-11)
- Màn cấu hình phía Ops + phân quyền (RC-13, RC-14)

### Out of Scope

- **Xây tính năng Lộ trình học** — nếu chưa có thì đó là tính năng riêng, không gộp vào gamification (`OQ-02`)
- **Xây hệ thống Kỹ năng / Competency** — tương tự (`OQ-06`)
- **Sửa logic hoàn thành Activity của module Learning Experience** — trừ khi chọn hướng B ở §4
- **Phần thưởng vật chất** — đổi điểm lấy quà, voucher, ưu đãi. Input không nhắc
- **Gamification cho nhân sự Ops** — chỉ học viên
- **Thi đua theo đội/nhóm** — input chỉ nói cá nhân
- Cấu hình gamification riêng cho từng lớp hoặc từng khoá — input nói cấu hình ở cấp tổ chức

### Potential Scope

- Bảng xếp hạng (RC-12) — chờ `OQ-01`
- Điều kiện huy hiệu theo kỹ năng — chờ `OQ-06`
- Cộng điểm theo chuỗi ngày đăng nhập — chờ `OQ-03`
- Thi đua theo phòng ban (`departments` đã có bảng)
- Gamification cho UpAcademy — ngoài phạm vi UpLnD hiện tại

---

## 9. Assumptions

| # | Giả định | Căn cứ | Kiểm chứng thế nào |
|---|---|---|---|
| A1 | Gamification áp dụng cho **học viên UpLMS**, không cho nhân sự Ops | Input: "động lực học của các học viên" | PO xác nhận |
| A2 | Cấu hình đặt ở **UpLMS Ops** | Mọi cấu hình hệ thống đều ở Ops | PO xác nhận |
| A3 | **Hạng chỉ lên, không tụt** | Input: điểm tích luỹ "vĩnh viễn" → không giảm → hạng không giảm | PO xác nhận |
| A4 | Điểm **không hết hạn** với loại tích luỹ | Từ "vĩnh viễn" | PO xác nhận |
| A5 | Huy hiệu **đạt rồi giữ vĩnh viễn**, không thu hồi | Thông lệ; input không nhắc thu hồi | PO xác nhận |
| A6 | Ảnh huy hiệu và ảnh hạng dùng hạ tầng `resources` sẵn có | Hệ thống đã có quản lý tài nguyên | Kiểm ở Impact Analysis |
| A7 | Điểm là **số nguyên** | Thông lệ | PO xác nhận |
| A8 | Một hành động có thể sinh **nhiều loại điểm cùng lúc** (vừa cộng tích luỹ vừa cộng theo kỳ) | Input nói "hai con số tách nhau" nhưng cùng nguồn | `OQ-04` làm rõ |

---

## 10. Phân loại cỡ yêu cầu

**Cỡ L** — chạy đủ 9 bước, đủ 4 Gate.

| Tiêu chí cỡ L | Có / Không | Căn cứ |
|---|---|---|
| Chạm ≥3 module | ✅ **7 module** | Learning Experience · Course · Assessment · Certificate · Notification · User · Class |
| Đổi data model / quan hệ | ✅ | Toàn bộ bảng gamification là mới; cần quan hệ cắt ngang lớp (§6) |
| Có conflict | ✅ | §4 — chống cày điểm vs logic hoàn thành Activity |
| Chạm tính năng `hidden` | ✅ | KB `09` §1 — 3/4 page Notification Ops đang ẩn |
| Nhiều hướng giải quyết | ✅ | §4 ba hướng · §6 hai cách chống cộng trùng · sinh điểm theo event vs theo batch |

Đạt **5/5** tiêu chí. Không có nghi ngờ về phân loại.

---

## 11. Điểm mạnh của input — giữ nguyên, đừng phân tích lại

Ba chỗ PO đã tự nêu lý do, và cả ba đều đúng với thực tế hệ thống:

| Input | Nhận xét |
|---|---|
| *"Hai con số tách nhau, vì người vào sau không bao giờ đuổi kịp điểm tích lũy"* | Đúng. Hệ thống có học viên cũ với tiến độ đã tích lũy — một bảng xếp hạng dùng điểm tích luỹ sẽ đóng băng ngay từ ngày đầu |
| *"Điểm không giải thích được thì không ai tin bảng xếp hạng"* | Đúng, và kéo theo ràng buộc kỹ thuật thật: phải lưu **log giao dịch điểm**, không được chỉ lưu số dư. Đã đưa vào RC-08 |
| *"Có tenant không muốn dùng cơ chế này"* | Khớp với định hướng đa tenant ở KB `15`. Bật/tắt phải nằm ở tầng dữ liệu tenant ngay từ đầu, không hardcode |

---

---

# 13. Phân tích OQ-07 — "Tắt gamification" nghĩa là gì

> PO yêu cầu phân tích thêm, gồm cả phương án *"chỉ tắt bật hiển thị ngoài giao diện học viên"*.

## 13.1 Đây không phải ba phương án — là hai chiều độc lập

Câu hỏi tưởng là chọn một trong ba, nhưng thực ra có **hai công tắc khác nhau về bản chất**:

| Chiều | Câu hỏi | Ảnh hưởng |
|---|---|---|
| **1. Ghi nhận** | Backend có tiếp tục tính và cộng điểm không? | Dữ liệu, tải hệ thống, khả năng hồi phục |
| **2. Hiển thị** | Học viên có thấy điểm/hạng/huy hiệu không? | Trải nghiệm người học |

Tổ hợp lại cho **ba trạng thái có ý nghĩa**:

| Trạng thái | Ghi nhận | Học viên thấy | Ops thấy | Dùng khi nào |
|---|---|---|---|---|
| **Tắt hẳn** | ❌ | ❌ | ❌ *(chỉ thấy màn cấu hình)* | Tổ chức không dùng cơ chế này |
| **Chạy ngầm** | ✅ | ❌ | ✅ | **Chạy thử trước khi mở cho học viên** |
| **Bật đầy đủ** | ✅ | ✅ | ✅ | Vận hành bình thường |

Trạng thái thứ tư (không ghi nhưng vẫn hiển thị) vô nghĩa — bỏ.

## 13.2 Chiều 1 — tắt hẳn có mất dữ liệu vĩnh viễn không?

Câu hỏi thật nằm ở đây: **bật lại thì giai đoạn tắt có thành lỗ hổng không?**

Xét 4 hành động tính điểm còn lại trong phạm vi sau khi PO chốt:

| Hành động | Dấu vết còn lại trong DB | Tính bù được sau? |
|---|---|---|
| Hoàn thành hoạt động | `user_course_section_progress` | **Có** |
| Hoàn thành khoá | `courses_users_certificates` | **Có** |
| Đạt bài kiểm tra | `quiz_attempts` · `quiz_attempt_gradings` | **Có** |
| Đạt điểm cao | `class_user_scores` | **Có** |
| *Chuỗi ngày đăng nhập* | Keycloak event | **Không** — nhưng đã chốt tính từ ngày go-live nên nhất quán |

`Assumption` — **cần Dev xác nhận:** các bảng trên có `created_at`/`updated_at`. Căn cứ: hai DTO trong Swagger (`CourseSectionDetailResponseDto`, `CourseSectionLinkDetailResponseDto`) có đủ cặp trường này, cho thấy codebase dùng mẫu base entity. Nhưng DTO của bảng tiến độ **không được khai trong Swagger**, và sơ đồ DB chỉ có PK/FK nên không kiểm được. Chưa xác nhận thì không coi là `Fact`.

**Nếu đúng:** tắt hẳn **không** gây mất mát không hồi phục. Bật lại có thể chạy job tính bù từ dữ liệu sẵn có.

### ⚠️ Nhưng đừng hứa tính bù

Job tính bù phải **tôn trọng luật chống cày điểm**, đặc biệt là *"giới hạn điểm tối đa mỗi ngày"*. Tính bù 6 tháng quá khứ nghĩa là phải **phát lại theo từng ngày** để áp trần đúng, không được cộng gộp một cục. Đây không phải việc tầm thường.

`Recommendation`: chọn tắt hẳn thì ghi rõ trong PRD **"bật lại tính từ thời điểm bật"**. Muốn tính bù thì tách thành US riêng, làm sau, không gánh vào đợt này.

## 13.3 Chiều 2 — vì sao nên tách riêng công tắc hiển thị

Đây là lý do thực dụng, không phải để đủ tính năng.

**Số điểm cho mỗi hành động gần như chắc chắn sai ở lần đặt đầu tiên.** Không có cách nào biết trước 10 điểm cho một Activity là quá dễ hay quá khó — phải nhìn dữ liệu thật mới biết.

Vấn đề: một khi học viên **đã thấy** điểm và hạng của mình, chỉnh số điểm xuống là **lấy đi thứ họ đã có**. Kể cả khi đã chốt "đổi cách tính chỉ áp dụng từ lúc đổi trở đi", học viên vẫn thấy tốc độ lên hạng chậm lại và sẽ hỏi.

Chạy ngầm 2–4 tuần trước khi mở cho phép:

- Xem phân bố điểm thật — bao nhiêu phần trăm học viên chạm hạng cao nhất, có ai bỏ xa phần còn lại không
- Kiểm luật chống cày có chặn đúng chỗ không, đặc biệt với Activity dạng Text/Ảnh (vẫn hoàn thành khi mở hiển thị — `KB-LX-03b`)
- **Đội truyền thông nội bộ có số liệu thật** để thiết kế chiến dịch đầu tiên, thay vì đoán

Chi phí: **một cờ boolean + chặn hiển thị phía UpLMS.** Rất rẻ so với giá trị.

### Cái giá phải trả khi mở sau giai đoạn chạy ngầm

Ngày mở, học viên thấy mình có sẵn vài nghìn điểm và một hạng mà chưa từng được báo. Hai ràng buộc bắt buộc:

| Ràng buộc | Vì sao |
|---|---|
| **Không bắn thông báo hồi tố** | Nếu không, mỗi học viên nhận hàng trăm thông báo dội về cùng lúc |
| Trang lịch sử điểm vẫn giải thích được từng giao dịch | Thoả RC-08 — nguồn điểm vẫn tra được dù lúc đó không được báo |

## 13.4 Về đa tenant

PO nói *"cứ làm bật tắt cho hệ thống hiện tại là được thôi"*. Đồng ý về phạm vi giao diện — **không cần màn quản lý nhiều tenant**.

Nhưng theo ràng buộc xuyên suốt của repo (`CLAUDE.md`): **cờ phải nằm trong bảng cấu hình gắn `tenant_id`, không hardcode**. Chi phí lúc này bằng 0; hardcode rồi gỡ sau thì đắt. Mẫu có sẵn trong hệ thống: `caching_settings`.

## 13.5 Recommendation

**Hai công tắc, ba trạng thái.** Mặc định khi tạo tổ chức mới: **Tắt hẳn**.

| Phải chấp nhận | Nội dung |
|---|---|
| Thêm một cờ cấu hình | `is_enabled` + `is_visible_to_learner` thay vì một cờ |
| Một business rule bắt buộc | Không bắn thông báo hồi tố khi chuyển từ chạy ngầm sang bật đầy đủ |
| Một quyết định phải ghi rõ trong PRD | Bật lại sau khi tắt hẳn → **tính từ thời điểm bật**, không tính bù |

> Đây là `Recommendation`, không phải quyết định. PO chốt ở Gate 1.

---

# 14. Những gì đã đổi ở v0.2

| Mục | Thay đổi |
|---|---|
| RC-02 | Bỏ **"hoàn thành lộ trình"** — lộ trình làm sau (OQ-02). Còn **4/6** hành động |
| RC-04 | Bỏ điều kiện **"đạt kỹ năng"** — thuộc tính năng Khung năng lực, làm sau (OQ-06). Còn **4/5** loại điều kiện |
| RC-04 | Điều kiện "chuỗi ngày liên tiếp" **giữ lại** — nguồn dữ liệu là Keycloak (OQ-03) |
| RC-06 | **Giữ nguyên** — "kỳ" = chiến dịch, hết kỳ **lưu lại**. Là nền cho leaderboard sau (OQ-04) |
| RC-07 | Logic hoàn thành Activity **giữ nguyên**, không sửa (OQ-10). Gánh nặng chống cày dồn hết vào **trần điểm/ngày** và **chống cộng trùng nội dung đã học** |
| RC-11 | Thêm chiều thứ hai: công tắc hiển thị — xem §13 |
| RC-12 | Bảng xếp hạng → **Potential scope**, làm sau (OQ-01) |
| §4 | Xung đột đã được giải: PO chọn **không sửa** logic hiện tại. Video nay là **≥80% thời lượng**, đã cập nhật KB `07` (`KB-LX-03a`, `KB-LX-03b`) |
| Stakeholder | Thêm **Đội truyền thông nội bộ** — người dùng thật của cơ chế chiến dịch |
| Problem | Đã có: **học viên không chủ động vào học** (OQ-09) |

## 14.1 Hệ quả của việc hoãn ba tính năng

Lộ trình · Kỹ năng · Leaderboard đều **"làm sau"** chứ không phải "không làm". Điều này đặt một ràng buộc thiết kế:

> **Danh mục hành động tính điểm và danh mục điều kiện huy hiệu phải mở rộng được bằng cấu hình, không được đóng cứng thành enum trong code.**

Nếu đóng cứng, mỗi lần thêm một loại hành động (hoàn thành lộ trình) hay một loại điều kiện (đạt kỹ năng) đều phải sửa schema và deploy lại. Đây là chỗ dễ làm sai nhất khi Dev thấy "hiện chỉ có 4 loại".

Sẽ đưa vào Impact Matrix (Gate 2) và mục `Solution` của PRD.

## 14.2 Một điểm cần lưu ý về chống cày điểm

PO chốt giữ nguyên logic hoàn thành Activity. Video nay đã chặt (≥80% thời lượng) nên rủi ro cày qua video **đã hết**.

Nhưng `KB-LX-03b`: **Activity dạng Text/Ảnh vẫn hoàn thành ngay khi mở hiển thị.** Nghĩa là toàn bộ khả năng chống cày cho loại nội dung này dồn vào hai cơ chế trong RC-07:

- **Trần điểm tối đa mỗi ngày** — chặn được tổng thiệt hại
- **Không cộng điểm khi học lại nội dung đã hoàn thành** — chặn lặp

Cơ chế thứ ba trong RC-07 — *"không cộng điểm cho hoạt động bỏ qua quá nhanh"* — **không áp dụng được cho Text/Ảnh** nếu không đo thời gian ở Activity, mà đo thời gian thì chính là sửa logic hoàn thành (điều PO đã chốt không làm).

`Open Question` mới → `OQ-16`: với Activity dạng Text/Ảnh, chấp nhận chỉ dựa vào trần điểm/ngày, hay gamification tự đo thời gian **riêng cho việc cộng điểm** mà không đụng tới trạng thái hoàn thành?

---

# 15. Bước tiếp theo

| Còn lại | Trạng thái |
|---|---|
| OQ-07 | Đã phân tích ở §13, chờ PO chọn |
| OQ-16 | Mới phát sinh, xem §14.2 |

Hai câu này chốt xong là chạy `/generate-brd`.

Xem `working/open-questions/open-questions-20260923.md`.
