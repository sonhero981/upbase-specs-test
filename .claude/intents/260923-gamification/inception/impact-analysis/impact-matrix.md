---
intent: 260923-gamification
artifact: impact-matrix
version: 0.3
status: review
approved: 2026-09-23 (v0.2, Gate 2)
note: v0.3 mang CR-013 §14, chờ duyệt lại
migrated-from: .claude/projects/Gamification/working/impact-analysis/impact-matrix-v0.3-20261008.md
---
# Impact Matrix — Gamification

> # ⚠️ Hai lớp thay đổi sau khi tài liệu này được duyệt lần đầu
>
> **`CR-007` — 23/09/2026.** Bỏ chiến dịch, kỳ lịch và cơ chế chốt kỳ, thay bằng **bộ chọn khoảng ngày tự do**. Khoá mốc huy hiệu sau khi tạo.
>
> **`CR-013` — 08/10/2026.** Phía học viên **bỏ bộ chọn khoảng ngày tự do**, chỉ còn khung cố định. **Campaign quay lại ở dạng mới** (BRD v0.7 §6.9). Bản v0.3 chỉ cập nhật những phần campaign chạm tới — xem §14.
>
> **Những mục sau KHÔNG còn hiệu lực:**
> - **Mô hình chiến dịch cũ**: chỉ số xếp hạng do vận hành chọn, mỗi lần một chiến dịch. Thay bằng §14
> - **Kỳ lịch như một thực thể riêng**, chốt kỳ lịch, snapshot kỳ lịch. **Chỉ campaign mới đóng băng**
> - Quyết định **gỡ huy hiệu khi nâng ngưỡng** — không còn, vì mốc nay khoá
>
> Các thay đổi từ `CR-008` đến `CR-012` chỉ nằm ở PRD. Trạng thái đúng nằm ở `working/raw-inputs/change-requests.md` và ở PRD.

---


| | |
| --- | --- |
| **Project** | Gamification |
| **Version** | **v0.3** |
| **Ngày** | 23/09/2026 · cập nhật 08/10/2026 |
| **Nguồn input** | `brd-v0.7-20261008.md` · `related-map-v0.2` · KB `01`–`15` · schema Lark `Data Architecture` (đọc lại 23/09) · Swagger LMS + Ops |
| **Trạng thái** | 🔄 **v0.3 chờ PO duyệt lại** — mang `CR-013`. Thêm `CF-7` cần PO xác nhận. Bản v0.2 được PO duyệt ngày 23/09/2026 |

## Change log

| Version | Nội dung |
|---|---|
| v0.1 | Bản đầu — 6 conflict, 14 coverage gap, 9 FR bổ sung |
| **v0.2** | **PO quyết toàn bộ 6 conflict.** `CF-2` biến mất · `C5` phải sửa · thêm `C10` loại trừ `Test Account` · gỡ `R2` · `R4` · gỡ khoá Trial khỏi phạm vi · chốt `A24` · `A25` |
| **v0.2.1** | **Ba câu Dev đã có đáp án.** `OQ-B2` ✅ có dấu thời gian · `OQ-B9` ✅ chịu được — **`R1` hạ từ 🔴 xuống 🟡**, xem §11.1 · `OQ-B12` ✅ lưu hết. `A27` PO xác nhận. **Không còn câu hỏi chặn Gate 3** |
| **v0.3** | **`CR-013` — campaign quay lại ở dạng mới.** Thêm §14 phân tích campaign. Thêm `CF-7` thay `CF-6`. Đóng `CG-10`, `CG-11`, `OQ-C7`, `OQ-C8`. Viết lại `TR-5`, `TR-8`. Thêm `R10`, `R11`. §11.1 tính lại số bảng phải tính |

---

## 1. Summary

Gamification là module mới, **chỉ đọc dữ liệu học tập**. Ba chỗ đổi thật: **`tenant` thêm tham số múi giờ**, **My Learning hiện điểm tích luỹ và hạng**, **quy trình chấm bài phải chấm hết tồn trước khi chốt kỳ**.

Sau vòng quyết của PO, **bức tranh rủi ro nhẹ đi đáng kể**:

| | v0.1 | **v0.2** |
|---|---|---|
| Conflict chưa quyết | 6 | **0** |
| Risk 🔴 Cao | 3 | **1** *(chỉ còn hiệu năng)* |
| Coverage gap | 14 | **11** |
| Chỗ đóng cứng tenant mới | 1 | **1** *(Foundation)* |

Ba quyết định của PO gỡ được nhiều nhất:

1. **`Test Account` bị loại khỏi toàn bộ logic** → gỡ `R3`, và thành ràng buộc `C10` áp cho mọi tầng
2. **Một khoá chỉ ở một lớp tại một thời điểm** → `CF-2` biến mất, `C5` đơn giản đi hẳn, `R2` gỡ bỏ
3. **Học viên tự ghi danh khoá mới từ catalog** → `R4` gỡ bỏ

| | Số lượng |
| --- | --- |
| Vùng bị ảnh hưởng (High / Medium / Low) | **5 / 5 / 2** |
| Conflict còn treo | **0** |
| FR/NFR bổ sung | **7** |
| Coverage gap | **11** |
| Chỗ đóng cứng tenant tăng thêm | **1** |

---

## 2. Current Situation — Dependency Map *(STEP 1)*

| Loại | Mục | Nguồn | Ghi chú |
| --- | --- | --- | --- |
| **Module** | Learning Experience | KB `07` | **Nguồn sự kiện chính.** Chỉ đọc |
| **Module** | Assessment (chỉ Test) | KB `03` | Quiz · Case Study · Storyline **bị loại** |
| **Module** | Grading | KB `05` | Chốt đạt/trượt bài chấm tay |
| **Module** | Course · Certificate | KB `01` · `08` | Mốc "hoàn thành khoá" |
| **Module** | Class | KB `04` | Một khoá **chỉ ở một lớp tại một thời điểm** |
| **Module** | User Account | KB `06` | `Block` · SSO Lark · **`Test Account` §8b** |
| **Data** | `user_course_section_progress` | Lark schema | FK → `class_user_instances` |
| **Data** | `class_user_instances` | Lark schema | Cầu nối duy nhất `users` ↔ nội dung học |
| **Data** | `quiz_attempts` · `quiz_attempt_gradings` | Lark schema | Nguồn sự kiện bài Test |
| **Data** | `quizzes` | KB `03` | `Graded Assignment` · `Pass Point` |
| **Data** | `courses_users_certificates` | Lark schema | **Bảng duy nhất nối thẳng `users`** |
| **Data** | `tenant` | Lark schema | 7 cột, **không có múi giờ** → `S21` |
| **Data** | `resources` | Lark schema | FK của 4 bảng — ảnh huy hiệu/hạng |
| **Data** | `casbin_rule` | Lark schema | ptype + v0–v6 |
| **Rule** | `KB-USER-TA-01`…`03` | KB `06` §8b 🆕 | **`Test Account` bỏ qua mọi logic** |
| **Rule** | `KB-LX-03a` `03b` `08` | KB `07` | Điều kiện hoàn thành · chặn huỷ ghi danh |
| **Rule** | `KB-TEST-01` `01a` `01b` | KB `03` | `Pass Point` phụ thuộc `Graded Assignment` |
| **Rule** | `BR-EDIT-07` | KB `01` | Khoá cấu hình Test — **trừ lượt của `Test Account`** |
| **Rule** | `BR-COURSE-INFO-06` | KB `01` | `Pass Point` = điều kiện chứng chỉ |
| **Process** | Enroll → Activate/Begin → học → hoàn thành khoá → chứng chỉ | KB `07` · `08` | Có **catalog tự ghi danh** |
| **Process** | Nộp bài → mentor chấm → `finish` → đạt/trượt | KB `05` | Nộp trước chấm trước (quy trình ngoài) |
| **Permission** | Casbin | Lark schema | Thêm resource, không đổi cơ chế |
| **Integration** | Keycloak / SSO Lark | KB `06` | 🟢 `S3` **không còn phụ thuộc** |
| **Mail event** | #10 · #29 hoàn thành khoá | KB `13` | 🟢 Đang bật, kênh khác gamification |
| **Mail event** | 8 mail luồng chấm điểm | `KB-MAIL-03` | 🔴 Đang tắt — PO chốt không bật lại |
| **Tính năng ẩn** | Storyline · Notice List · Recipients List · Mail Logs | KB `00-index` | 🟢 Không dùng |
| **Tính năng ẩn** | **Quản lý bài kiểm tra trong lớp** | KB `13` §74 | ⚠️ Bài Test có Thời gian mở/đóng → `CG-6` |
| **Không tồn tại** | Examination · Entrance Test · **Khoá Trial** | KB `14` §2.2 🆕 | Có endpoint, **không có tính năng** |

---

## 3. Desired Situation *(STEP 2)*

Module mới, 5 lớp. **23 hạng mục In scope · 17 US · 10 ràng buộc `C1`–`C10`.**

Rule mới: `BR-TEST` · `BR-REGRADE-01/02` · `BR-SKIP` · `S22` (tiêu chí phụ khi đồng hạng).

---

## 4. Impact Matrix — 12 vùng *(STEP 3.0)*

| # | Vùng | Bị ảnh hưởng? | Mô tả | Severity |
| --- | --- | --- | --- | --- |
| 1 | **Business process** | ✅ | 🔧 Quy trình chấm bài phải **chấm hết bài tồn trước khi campaign kết thúc**, vì bài chấm sau đó không tính (`TR-5`). Thêm quy trình: cấu hình gamification · tạo campaign · công bố kết quả ngoài hệ thống | **Medium** |
| 2 | **Module / function** | ✅ | Module mới. Module hiện hữu thành **nguồn sự kiện chỉ đọc**. My Learning **bị sửa** | **High** |
| 3 | **Screen / report** | ✅ | 9 màn mới · **1 màn existing bị sửa: My Learning** (hiện điểm tích luỹ + hạng). 🔧 `CR-013` thêm: Ops danh sách và tạo campaign · Ops kết quả campaign kèm xuất Excel · học viên xem campaign trong trang bảng xếp hạng | **Medium** |
| 4 | **Data** | ✅ | 10 thực thể mới. **`tenant` thêm tham số múi giờ** — bảng hiện hữu duy nhất bị sửa. 🔧 `CR-013` thêm **campaign** và **kết quả campaign đã đóng băng**. Điểm campaign **không ghi thêm** — đọc từ sổ giao dịch điểm đã có | **High** |
| 5 | **API** | ✅ | API gamification mới. `GET /courses/my-learnings` **thêm field**, không phá contract | **Medium** |
| 6 | **Role / permission** | ✅ | Thêm resource Casbin. L&D/Mentor/Giáo viên xử lý bằng phân quyền thường | **Low** |
| 7 | **Business rule** | ✅ | 4 rule mới. **3 rule hiện hữu được đính chính trong đợt này** (`KB-LX-04` gỡ · `KB-TEST-01a` thêm · `BR-EDIT-07` thêm ngoại lệ `Test Account`) | **High** |
| 8 | **NFR** | ✅ | Bảng xếp hạng tính từ sổ giao dịch theo khoảng ngày, toàn tổ chức, nhiều kỳ lồng nhau. 🔧 `CR-013`: học viên chỉ chọn khung cố định nên **mọi bảng phía học viên tính sẵn được**, không còn phép tính tuỳ ý. Mỗi campaign đang chạy thêm hai bảng. Xem §11.1 | **High** |
| 9 | **Notification / Email** | ⚠️ Rất ít | **Không dùng** cơ chế thông báo hiện có, **không gửi mail**. Chạm duy nhất: mail #10/#29 bắn cùng lúc với sự kiện cộng điểm — khác kênh nên không trùng | **Low** |
| 10 | **Reporting** | ❌ | SIS độc lập. ⚠️ L&D là stakeholder nhưng **chưa có báo cáo nào phục vụ họ** → `CG-11` | **Low** |
| 11 | **Test** | ✅ | Kiểm lại: hoàn thành Activity · hoàn thành khoá · chấm bài (`finish`) · My Learning · hai công tắc · **loại trừ `Test Account`** | **Medium** |
| 12 | **Release** | ✅ | Thứ tự: cấu hình → dữ liệu → job nền → màn Ops → màn LMS. Hai công tắc cho phép ra mắt hai nhịp | **Medium** |

**High 5 · Medium 5 · Low 2.**

> Vùng thuộc phần KB chưa phủ (KB `14` §1–2): đã kiểm. `Examination`, `Entrance Test` — **không có tính năng**. Lịch dạy · phòng học · phòng ban — không giao. Phân quyền — đã xét ở vùng 6.

---

## 5. Conflict Analysis *(STEP 3a)* — ✅ 6/6 đã quyết

| # | Conflict | ✅ Quyết của PO | Hệ quả |
| --- | --- | --- | --- |
| **CF-1** | Tài khoản `Test Account` lên bảng xếp hạng công khai | **`Test Account` bỏ qua HẾT mọi logic gamification** — không điểm, huy hiệu, hạng, xếp hạng | → **ràng buộc `C10`**. Đã ghi KB `06` §8b. Gỡ `R3` |
| **CF-2** | Học lại ở lớp khác không được điểm | **Không tồn tại.** Một khoá chỉ ở **một lớp tại một thời điểm**. Xoá ra thêm lại → học lại → **tính như khoá mới, được điểm** | → **`C5` phải sửa**, xem §6. Gỡ `R5` |
| **CF-3** | Đổi ngưỡng hạng → cùng điểm khác hạng | **Chấp nhận** — người cũ giữ hạng (`A3`), người mới theo ngưỡng mới (`C4`) | Ghi rõ trong PRD để vận hành biết trước |
| **CF-4** | Tương tự với huy hiệu | **Áp dụng cùng nguyên tắc `CF-3`** *(suy ra — PO xác nhận lại ở Gate 2)* | |
| **CF-5** | Xoá tài nguyên làm hỏng ảnh huy hiệu | **Có huy hiệu mặc định** — mất ảnh thì rơi về ảnh mặc định | Đơn giản, không cần khoá tài nguyên |
| ~~CF-6~~ | ~~Tắt gamification giữa lúc chiến dịch chạy~~ | ~~Đang có chiến dịch thì không tắt được — phải dừng chiến dịch trước~~ | 🔄 **Thay bằng `CF-7`** ở v0.3 |
| **CF-7** 🆕 | **Tắt `Gamification` khi có campaign đang chạy.** `CF-6` bắt phải dừng campaign trước, nhưng `CR-013` chốt **campaign đang chạy không dừng được** và **nhiều campaign được chồng thời gian**. Giữ `CF-6` thì vận hành gần như không bao giờ tắt được gamification | `Recommendation` — **vẫn cho tắt.** Campaign không nhận thêm gì trong thời gian tắt, giống rule *"campaign phụ thuộc cấu hình chung"*. Popover xác nhận khi tắt nêu thêm số campaign đang chạy. **Chờ PO xác nhận ở Gate 2** | Gỡ `CG-10`. Viết lại `TR-8` |

---

## 6. 🔧 `C5` phải sửa — feed ngược vào BRD

| | |
|---|---|
| **Cũ (v0.1–v0.6)** | Chống cộng trùng "đã học" tính theo **người học, cắt ngang lớp** |
| **Mới (v0.6.1)** | Chống cộng trùng trong phạm vi **một lượt ghi danh**. Được thêm lại → **lượt học mới tính điểm mới** |

**Lý do:** PO xác nhận một khoá chỉ ở một lớp tại một thời điểm, nên kịch bản học song song hai lớp — thứ sinh ra `C5` ban đầu — **không xảy ra được**.

**Kèm một câu rule thay cho cả job nạp dữ liệu:**

> **Chỉ cộng điểm khi bản ghi tiến độ CHUYỂN TRẠNG THÁI sang hoàn thành, tính từ thời điểm bật tính năng.**

Nội dung đã hoàn thành từ trước không chuyển trạng thái nữa nên không phát sinh điểm. → **`TR-2` của v0.1 (nạp sẵn dấu chống cộng trùng) không còn cần**, thay bằng một rule. Gỡ `R2`.

✅ **Đã áp vào BRD v0.6.1.**

---

## 7. Bidirectional Impact *(STEP 3b)*

### New → Old

| # | Phát hiện | FR bổ sung |
| --- | --- | --- |
| BI-1 | `tenant` thêm tham số múi giờ — bảng hiện hữu duy nhất bị sửa | `FR-1` |
| BI-2 | `GET /courses/my-learnings` trả thêm **điểm tích luỹ + hạng** (`A25`) | `FR-2` — thêm field, giữ tương thích ngược |
| BI-3 | Team chấm bài chịu ràng buộc thời gian mới | `TR-5` — quy trình |
| **BI-13** 🆕 | **Mọi truy vấn của gamification phải lọc `Test Account`** — ở tầng ghi nhận sự kiện, không chỉ ở tầng hiển thị | **`FR-10`** — lọc từ lớp 1, tránh ghi rồi lọc sau |

### Old → New — *chiều hay bị bỏ*

| # | Phát hiện | Ràng buộc lên tính năng mới |
| --- | --- | --- |
| **BI-4** | 🟢 `BR-EDIT-07` khoá cấu hình Test sau khi có người làm | Quy tắc đếm **ổn định**, không tính lại ngược |
| **BI-5** | 🟢 `KB-LX-08` chặn huỷ ghi danh sau khi đã học | Đường cày điểm **đã bị chặn sẵn** |
| **BI-14** 🆕 | 🟢 **Một khoá chỉ ở một lớp tại một thời điểm** | Loại bỏ toàn bộ nhóm vấn đề trùng lặp xuyên lớp |
| ~~BI-6~~ | ~~Học viên học hết nội dung thì kẹt ở đáy bảng~~ | ❌ **Sai** — có catalog tự ghi danh khoá mới |
| ~~BI-7~~ | ~~Ngày bật thành ngày cày điểm tập thể~~ | ❌ **Không xảy ra** nếu áp rule chuyển-trạng-thái ở §6 |
| **BI-8** | Khoá **Flexible** chỉ bắt đầu khi bấm **Activate** | `FR-5`: nêu rõ trong `Out of scope` — chưa Activate thì không sinh sự kiện |
| ~~BI-9~~ | ~~Khoá Trial có tính điểm không~~ | ❌ **Không có khoá Trial** (`A26`) |
| **BI-10** | Mô hình **Foundation** là đặc thù UpBase | **`FR-7`**: viết tổng quát *"khoá được đánh dấu bỏ qua thì không tính hoàn thành"* |
| **BI-11** | Bài Test có **Thời gian mở/đóng** (tính năng đang ẩn) | `FR-8`: ghi nhận, không xử lý |
| **BI-12** | `support-groups` **không có `tenant_id`** | **`FR-9`**: loại trừ `Test Account` theo **cờ trên tài khoản**, không theo nhóm |

---

## 8. Coverage Gaps *(STEP 3c)*

### Boundary

| # | Case chưa định nghĩa | FR bổ sung |
| --- | --- | --- |
| CG-1 | Học viên **0 điểm** hiện ở đâu trên bảng xếp hạng | Quy tắc hiển thị nhóm 0 điểm |
| CG-2 | **Kỳ chưa có ai được điểm** — bảng rỗng hiện gì | Trạng thái rỗng |
| CG-3 | Điểm **bằng đúng ngưỡng** hạng — lên hay chưa (`>=` hay `>`) | Quy ước so sánh, áp chung cho hạng và huy hiệu |
| CG-4 | **Chạm trần điểm/ngày giữa chừng** — không cộng, cộng một phần, hay dời sang hôm sau | Quy tắc khi chạm trần |
| CG-5 | **Chiến dịch bắt đầu và kết thúc cùng ngày** | Cho phép hay chặn |
| CG-6 | **Biên ngày và biên kỳ** — hoàn thành lúc 23:59:59 theo múi giờ tổ chức | Quy ước đóng/mở khoảng |

### Exception

| # | Case chưa định nghĩa | FR bổ sung |
| --- | --- | --- |
| CG-7 | **Hai thiết bị cùng hoàn thành một hoạt động gần như đồng thời** | Chống trùng ở tầng ghi nhận |
| CG-8 | **Job chốt kỳ chạy lỗi hoặc trễ** | Cơ chế chạy lại, chốt đúng biên kỳ |
| CG-9 | **Học viên bị `Block` giữa kỳ**, rồi mở lại | Quy tắc vào/ra bảng xếp hạng |
| ~~CG-10~~ | ~~`CF-6` kéo theo: phải có cách dừng chiến dịch đang chạy~~ | ✅ **Không còn cần** — `CF-7` cho tắt gamification mà không phải dừng campaign. PO chốt campaign đang chạy không dừng được (`N22`) |
| ~~CG-11~~ | ~~Đổi cấu hình điểm giữa lúc chiến dịch đang chạy~~ | ✅ **PO chốt 08/10: không khoá.** Campaign mang hai mức điểm, theo `C4` |

### Shared entity

| # | Entity | Rủi ro |
| --- | --- | --- |
| CG-12 | **`resources`** — ảnh huy hiệu và ảnh hạng | ✅ Đã giải bằng **huy hiệu mặc định** (`CF-5`) |
| CG-13 | **`course_categories`** — FK của **6 bảng** | Không chạm ở đợt này. Nếu sau này huy hiệu/chiến dịch phân theo danh mục thì chạm 6 bảng — ghi để nhớ |
| — | **Question Bank** | Không chạm |

### Side effect

| # | Hệ quả ngoài ý muốn |
| --- | --- |
| CG-14 | **L&D là stakeholder nhưng không có báo cáo nào phục vụ họ.** Chỉ xem được bảng xếp hạng như học viên |

---

## 9. Transition Requirements *(STEP 4)*

### Data

| # | Yêu cầu | Mức |
| --- | --- | --- |
| **TR-1** | **Không tính bù.** Không dựng lại lịch sử trước thời điểm bật `Gamification` | ✅ PO chốt |
| **TR-2** | 🔧 **Thay cho job nạp dữ liệu: một rule.** *Chỉ cộng điểm khi bản ghi tiến độ chuyển trạng thái sang hoàn thành, tính từ lúc bật* | Bắt buộc — §6 |
| **TR-3** | Thêm cột múi giờ vào `tenant`, đặt mặc định cho tổ chức hiện tại | Bắt buộc |
| **TR-4** | Mọi học viên bắt đầu ở **0 điểm và hạng thấp nhất** | Cần PO xác nhận |
| **TR-10** 🆕 | **Loại trừ `Test Account` ngay từ lần chạy đầu tiên** — không để lọt vào dữ liệu rồi lọc sau | Bắt buộc — `C10` |

### Compatibility

| # | Yêu cầu |
| --- | --- |
| **TR-5** | 🔧 **Quy trình chấm bài:** chấm hết bài tồn **trước khi campaign kết thúc**. Bài chấm đạt sau đó không tính cho campaign — học viên thiệt nếu mentor chấm chậm. Vận hành nên báo mentor ngày kết thúc của từng campaign |
| **TR-6** | API hiện có **không đổi contract** — My Learning chỉ **thêm** field |

### Cutover

| # | Yêu cầu |
| --- | --- |
| **TR-7** | **Ra mắt hai nhịp:** bật `Gamification` (chạy ngầm) → 2–4 tuần xem phân bố thật → chỉnh cấu hình → bật `Visibility in UpLMS` |
| **TR-8** | 🔧 **Rollback:** tắt `Visibility` trước, chỉ tắt `Gamification` khi thật sự phải dừng. Campaign đang chạy **không chặn việc tắt**, chỉ không nhận thêm gì trong thời gian tắt (`CF-7`) |
| **TR-9** | Khi bật `Visibility`: **không bắn thông báo hồi tố** |

---

## 10. Kiểm tra chiều tenant *(STEP 5)*

| Câu hỏi | Trả lời | Xử lý |
| --- | --- | --- |
| **Có nhúng logic riêng UpBase không?** | ⚠️ **Một chỗ** — `BR-SKIP` nhắc đích danh **Foundation**, mô hình đặc thù UpBase (KB `15` §6) | **`FR-7`**: viết tổng quát *"khoá được đánh dấu bỏ qua thì không tính hoàn thành"* |
| **Có hằng số cứng mới không?** | Trần điểm/ngày · ngưỡng hạng · ngưỡng huy hiệu · số điểm mỗi hành động · múi giờ · số người liền kề ở "Vị trí của tôi" | 5 cái đầu **phải cấu hình được theo tổ chức**. Số người liền kề chấp nhận hardcode — ghi rõ trong PRD |
| **Bảng mới có `tenant_id` không?** | **Bắt buộc ở cả 10 thực thể mới** | Chú ý nhất: **sổ giao dịch điểm** và **snapshot kỳ** |
| **Enum mới: hệ thống hay tenant định nghĩa?** | **Hệ thống:** 4 loại huy hiệu · danh mục chỉ số · loại kỳ lịch.<br>**Tenant:** huy hiệu cụ thể · hạng · chiến dịch · bảng điểm | Khớp `C2` |

> ⚠️ **Không dùng `support-groups` để loại trừ `Test Account`** — bảng này không có `tenant_id` (KB `15` §6, 🔴). Loại theo **cờ trên tài khoản** (`FR-9`).

**Chỗ đóng cứng tenant tăng thêm: 1** *(Foundation)* — gỡ được, chi phí gần bằng 0 nếu làm ngay.

---

## 11. Risk Summary

| # | Risk | Mức | Giảm nhẹ |
| --- | --- | --- | --- |
| **R1** | **Hiệu năng bảng xếp hạng** | 🟡 **Thấp** *(hạ từ 🔴)* | Xem §11.1 — **cơ chế chốt kỳ (`S19`) đã tự giới hạn bài toán**. Giai đoạn chạy ngầm vẫn là cơ hội đo tải thật |
| ~~R2~~ | ~~Ngày đầu thành ngày cày điểm tập thể~~ | ✅ Gỡ | Rule chuyển-trạng-thái ở §6 |
| ~~R3~~ | ~~Tài khoản công ty trên bảng xếp hạng~~ | ✅ Gỡ | `C10` |
| ~~R4~~ | ~~Học viên chăm nhất kẹt ở đáy bảng~~ | ✅ Gỡ | Có catalog tự ghi danh |
| ~~R5~~ | ~~Hai hệ thống nói hai điều khác nhau khi học lại~~ | ✅ Gỡ | `CF-2` không tồn tại |
| **R6** | **Đổi cấu hình tạo hai chuẩn** cho cùng một hạng/huy hiệu | 🟠 Vừa | PO chấp nhận (`CF-3`). Ghi rõ trong PRD để vận hành biết trước khi đổi |
| **R7** | **Sổ giao dịch điểm tăng tuyến tính**, chưa có chính sách dọn | 🟠 Vừa | `OQ-C5` |
| **R9** | **Học viên trượt lần đầu, chấm lại thành đạt thì không có điểm** (`BR-REGRADE-02`) | 🟡 Thấp | PO đã chốt. Rủi ro là học viên thắc mắc khi mentor chấm sai lần đầu |
| **R10** 🆕 | **Campaign phụ thuộc cấu hình chung.** Tắt một hành động hoặc đổi số điểm giữa chừng thì luật của campaign đang chạy đổi theo, dù campaign "không sửa được" | 🟠 Vừa | PO chấp nhận 08/10. Vận hành cần biết: đổi cấu hình chung là đổi luật mọi campaign đang chạy |
| **R11** 🆕 | **Bài chấm sau khi campaign kết thúc không tính** | 🟡 Thấp | PO chốt 08/10. Giảm nhẹ bằng quy trình `TR-5` |

### 11.1 🔽 Vì sao `R1` hạ từ 🔴 xuống 🟡

PO phản biện: *"bảng có thể sẽ chỉ hiển thị vài tuần vài tháng vài quý của năm gần nhất thôi chứ có hiển thị vô thời hạn đâu"* — **đúng, và lý do sâu hơn nằm ở `S19`.**

Khi tôi nêu `R1` ở v0.1, tôi đã **tính thiếu tác dụng của cơ chế chốt kỳ**:

| Loại bảng | Cách lấy dữ liệu | Chi phí |
|---|---|---|
| **Kỳ đã kết thúc** | Đọc thẳng **snapshot đã đóng băng** (`S19`) | Gần bằng 0 — chỉ là đọc bảng kết quả |
| **Kỳ đang chạy** | Tính từ sổ giao dịch theo khoảng ngày | Chỉ tính cho **kỳ đang mở** |

Số bảng phải tính trực tiếp tại bất kỳ thời điểm nào là **tối đa 5**: tuần hiện tại · tháng hiện tại · quý hiện tại · năm hiện tại · chiến dịch đang chạy (tối đa 1, theo `N3`).

> 🔧 **Tính lại ở v0.3 (`CR-013`).** Không còn giới hạn một campaign. Số bảng phải tính = khung cố định (`All time` · tuần · tháng · quý · năm, nhân số bảng của mỗi khung) **cộng hai bảng cho mỗi campaign đang chạy**. Campaign đã kết thúc đọc từ kết quả đóng băng, chi phí gần bằng 0.
>
> Hai điều giữ cho bài toán vẫn nhỏ: học viên **không còn chọn khoảng ngày tự do**, nên không ai gọi được phép tính tuỳ ý; và mỗi bảng campaign chỉ là một truy vấn gộp trên sổ giao dịch, lọc theo khoảng và loại hành động. Nếu số campaign chạy cùng lúc trở thành vấn đề thì đó là việc của Gate 3, không phải rủi ro mới.

Nặng nhất là **bảng của năm hiện tại** — gom tới 12 tháng giao dịch. Nhưng đó là một truy vấn gộp có chỉ mục theo `(tenant, ngày)` trên dữ liệu quy mô một tổ chức, không phải bài toán khó.

**Hai điểm còn cần chú ý khi thiết kế, không phải rủi ro:**

| # | Điểm |
|---|---|
| 1 | **`US7` "Vị trí của tôi" bắt buộc xếp hạng toàn bộ**, không rút gọn được — muốn biết thứ hạng của một người thì phải so với tất cả. Đây là truy vấn nặng nhất, và nó chạy mỗi lần học viên mở trang |
| 2 | **Bảng của năm hiện tại càng về cuối năm càng nặng.** Nếu cần, tính sẵn theo chu kỳ thay vì tính trực tiếp — quyết ở Gate 3 |

→ Chuyển từ **Risk** sang **ghi chú thiết kế** cho `Solution` của PRD.

---

## 12. Open Questions

> ✅ **Không còn câu hỏi nào chặn Gate 3.** 🔧 v0.3 có thêm `OQ-C10` (`CF-7`), PO xác nhận ở Gate 2.

### Đã đóng ở vòng này

| # | Kết luận |
|---|---|
| `OQ-B2` | ✅ **Dữ liệu tiến độ có dấu thời gian**, ghi nhận được thời điểm hoàn thành. `C7`, trần điểm/ngày, rule chuyển-trạng-thái đều khả thi |
| `OQ-B9` | ✅ **Chịu được.** Bảng chỉ hiển thị một số kỳ gần nhất, không vô thời hạn. Cộng với `S19` (kỳ đã chốt đọc từ snapshot) → tối đa 5 bảng tính trực tiếp. Xem §11.1 |
| `OQ-B12` | ✅ **Lưu hết** — thời điểm đạt huy hiệu, hoàn thành khoá, hoàn thành bài Test. `C8` và `S22` khả thi |
| `A27` | ✅ **PO xác nhận:** không tính bù = tính từ lúc ghi nhận. Bật `Visibility` thì học viên **thấy ngay điểm và hạng đã tích trong lúc chạy ngầm**, kèm lịch sử để tra lý do |

### Còn lại — không chặn

| # | Câu hỏi | Người trả lời | Xử lý ở |
| --- | --- | --- | --- |
| `OQ-C5` | **Chính sách lưu trữ sổ giao dịch điểm** — giữ bao lâu, có dọn không | PO + Dev | Gate 3 |
| ~~`OQ-C7`~~ | ✅ **PO chốt 08/10: không khoá bảng điểm.** Campaign mang hai mức điểm | — | — |
| ~~`OQ-C8`~~ | ✅ **Không còn cần.** Campaign đang chạy không dừng được (`N22`), và tắt gamification không cần dừng campaign (`CF-7`) | — | — |
| `OQ-C10` 🆕 | **`CF-7` — tắt `Gamification` khi có campaign đang chạy thì vẫn cho tắt, đúng không?** | PO | Gate 2 |
| `OQ-C9` | **`CF-4` — huy hiệu áp cùng nguyên tắc `CF-3` chứ?** Người đạt trước giữ, người sau theo ngưỡng mới | PO | Gate 3 |
| `OQ-B11` | **Múi giờ tổ chức khai ở đâu trong đợt này?** | PO + Dev | Gate 3 |
| `TR-4` | **Mọi học viên bắt đầu ở 0 điểm và hạng thấp nhất** — xác nhận | PO | Field Intake |
| `OQ-B4` | **Ba con số Analytics** — cần trước khi viết PRD | PO + Dev | Trước PRD |

---

## 13. Phụ lục — Nguồn đã đọc

| Nguồn | Cụ thể |
| --- | --- |
| **KB nghiệp vụ** | `01-course.md` (`BR-EDIT-07` + ngoại lệ mới, `BR-COURSE-INFO-06`) · `03-assessment.md` §1–2 + `KB-TEST-01/01a/01b` · `04-class.md` · `05-grading.md` §9 · `06-user-account.md` **§8b mới** · `07-learning-experience.md` §1–3, §10 · `08-certificate.md` · `09-notification-email.md` §1, §7–8 · `11-dashboard-sis.md` |
| **KB kỹ thuật** | `12-data-model.md` · `13-mail-events.md` · `14-api-surface.md` §1–2, **§2.2 + bảng endpoint chết mới** · `15-product-direction.md` §6 |
| **DB — đọc lại nguồn gốc** | ✅ **Tải trực tiếp từ Lark `Data Architecture` ngày 23/09/2026.** 85 bảng · 173 quan hệ · 320 cột — khớp KB 12. Quan hệ đã lần: `class_user_instances` (8 FK) · `user_course_section_progress` (4 FK) · `courses_users_certificates` (4 FK) · `course_categories` (FK của 6 bảng) · `resources` (FK của 4 bảng) · `departments` → `staffs` · `tenant` (7 cột, không có múi giờ) |
| **Swagger** | LMS 144 op / 25 nhóm · Ops 548 op / 57 nhóm. Đã soi toàn bộ endpoint ghi của LMS, và các nhóm `Quiz Attempt`, `Quiz Attempt Grading`, `Notifications Management`, `User Management`, `Course LMS`, `Certificate`, `Permissions management`, `Roles Management` |
| **Quyết định** | `project-decisions.md` · `change-requests.md` CR-001…006 · toàn bộ phản hồi Gate 1 và Gate 2 |
| **⚠️ Chưa tra được** | • **Ba con số Analytics** (`OQ-B4`) — chưa lấy, cần trước khi viết PRD<br>• **Cơ chế nộp bài phát sinh sự kiện thế nào** — PO xác nhận có, tôi chưa biết cách nó bắn sự kiện<br>• **Cơ chế ghi nhận "ngày có mặt"** — PO xác nhận làm được, chưa biết bằng đường nào<br>• **`Event Test Management` · `Event Management`** — chưa xác nhận có tính năng hay không<br><br>*(Đã gỡ khỏi danh sách: ước lượng tải — `OQ-B9` đã có đáp án và §11.1 giải thích vì sao bài toán tự giới hạn)* |

---

## 14. 🆕 Campaign — phân tích ảnh hưởng *(`CR-013`, v0.3)*

Campaign theo BRD v0.7 §6.9: vận hành chọn khoảng thời gian và loại hành động tính điểm, số điểm theo cấu hình chung, hai bảng (điểm · số hoạt động), toàn tổ chức, được chồng thời gian, đóng băng khi kết thúc.

### 14.1 Đọc gì, ghi gì

| | Campaign đọc | Campaign ghi |
|---|---|---|
| **Sổ giao dịch điểm** | Từng lần cộng kèm **nguồn** và **thời điểm** (`C3`) — lọc theo khoảng và loại hành động | ❌ Không ghi. Học viên hành động thì không có gì thêm |
| **Dữ liệu tiến độ học** | Hoạt động chuyển sang hoàn thành trong khoảng | ❌ Không ghi |
| **Cấu hình chung** | Hành động nào đang bật, số điểm bao nhiêu | ❌ Không ghi |
| **Campaign** *(mới)* | — | Tên · mô tả · khoảng · loại hành động |
| **Kết quả đã đóng băng** *(mới)* | — | Ghi **một lần** khi campaign kết thúc |

**Điểm quan trọng nhất:** campaign **không chạm luồng cộng điểm**. `NFR-GAM-01` (lỗi gamification không làm hỏng thao tác học) không bị ảnh hưởng thêm.

### 14.2 Phụ thuộc vào thứ đã có

| Phụ thuộc | Hệ quả | Xử lý |
|---|---|---|
| Sổ giao dịch phải lưu **loại hành động** của từng lần cộng | Thiếu thì không lọc được | ✅ Đã có — `C3` lưu nguồn |
| Thời điểm cộng điểm bài Test là **lúc chấm đạt** | Bài chấm sau khi kết thúc không tính | PO chốt — `R11`, `TR-5` |
| Cấu hình chung đổi giữa chừng | Luật campaign đổi theo | PO chấp nhận — `R10` |
| Công tắc `Leaderboard` | Tắt thì campaign ẩn theo | PO chốt |
| Công tắc `Gamification` | Tắt thì campaign không nhận thêm gì | `CF-7` — chờ PO |

### 14.3 Ràng buộc mới

| # | Ràng buộc |
|---|---|
| `C11` 🆕 | **Kết quả đóng băng phải tính đúng theo biên thời gian**, kể cả khi tác vụ đóng băng chạy trễ. Vì campaign là phép lọc theo thời điểm trên sổ giao dịch, tính trễ vẫn ra đúng số — miễn là lọc theo thời điểm cộng, không lọc theo thời điểm chạy. Áp cho `CG-8` |
| `C12` 🆕 | **Kết quả đã đóng băng giữ nguyên mãi.** Học viên bị `Block` hoặc rời tổ chức **sau khi campaign kết thúc** vẫn nằm trong kết quả (`A14`). Người đã bị `Block` hoặc rời tổ chức **trước lúc kết thúc** thì không có mặt, giống bảng đang chạy (`BR-6.8`) |

### 14.4 Coverage gap mới

| # | Case | Xử lý đề xuất |
|---|---|---|
| CG-15 🆕 | Campaign **bắt đầu và kết thúc cùng một ngày** — thay cho `CG-5` | `Recommendation` — cho phép. Một ngày là khoảng hợp lệ |
| CG-16 🆕 | Vận hành **tắt một hành động** đang được campaign chọn | Hành động đó ngừng đóng góp. Campaign vẫn chạy với các hành động còn lại (`R10`) |
| CG-17 🆕 | **Không học viên nào có điểm** khi campaign kết thúc | Kết quả rỗng vẫn đóng băng, hiện trạng thái rỗng |

### 14.5 Kiểm tra chiều tenant

Campaign và kết quả đóng băng **bắt buộc có `tenant_id`** (`C1`). Campaign là dữ liệu do tenant tạo, khớp dòng *"Tenant: … chiến dịch"* ở §10. Loại hành động là danh mục hệ thống, chịu `C2`.
