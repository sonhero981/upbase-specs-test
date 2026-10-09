---
intent: 260923-gamification
artifact: related-features-map
version: 0.2
status: approved
approved: 2026-09-23
migrated-from: .claude/projects/Gamification/working/impact-analysis/related-map-v0.2-20260923.md
---
# Related Features & Docs Map — Gamification

> # ⚠️ CR-007 đã thay đổi phạm vi sau khi tài liệu này được duyệt
>
> Ngày 23/09/2026, PO chốt **bỏ hẳn chiến dịch, kỳ lịch và cơ chế chốt kỳ**, thay bằng **bộ chọn khoảng ngày tự do** trên bảng xếp hạng. Đồng thời **khoá mốc huy hiệu sau khi tạo**, nên huy hiệu đã nhận không bao giờ bị lấy lại.
>
> **Những mục sau trong tài liệu này KHÔNG còn hiệu lực:**
> - Mọi nội dung về **chiến dịch**: thực thể, vòng đời, chỉ số xếp hạng do vận hành cố định, luật cấm sửa khi đang chạy
> - Mọi nội dung về **kỳ lịch như một thực thể riêng**, **chốt kỳ**, **snapshot**, **đóng băng kết quả**
> - Mục tiêu **`O5`** (kết quả không đổi về sau) — đã bỏ, PO chấp nhận số liệu sống
> - Quyết định **gỡ huy hiệu khi nâng ngưỡng** — không còn, vì mốc nay khoá
>
> Trạng thái đúng nằm ở `working/raw-inputs/change-requests.md` mục **CR-007** và ở PRD.

---


| | |
|---|---|
| Project | Gamification · **Bước 5** |
| Version | **v0.2** — 23/09/2026 |
| Input | `docs/brd/brd-v0.6-20260923.md` (Gate 1 `Approved with Notes`) |
| Nguồn quét | KB `01`–`15` · schema DB 85 bảng · Swagger LMS + Ops |
| Trạng thái | 🟢 **12/12 `❓BA` đã được PO chốt** — chờ soát lần cuối |

## Change log

| Version | Nội dung |
|---|---|
| v0.1 | Bản quét đầu — 12 `❓BA` |
| **v0.2** | **PO trả lời toàn bộ 12 câu.** Gỡ `F1`. Đóng `F2` bằng quy trình ngoài. **Loại Storyline khỏi nguồn sự kiện.** Bỏ `Graded Activity`. Thêm màn My Learning vào phạm vi. Ba đính chính KB |

---

# 1. ✅ PO chốt — 12 câu `❓BA`

| # | Câu hỏi | Chốt của PO | Hệ quả |
|---|---|---|---|
| **BA-01** | Học viên nộp bài kiểm tra qua đâu? | **Hành động nộp bài ghi nhận được.** Swagger có thể cũ | ✅ `F1` gỡ bỏ. Không đào sâu API nữa |
| **BA-02** | Bài chấm tay: mốc ghi nhận là lúc nào? | **Ai nộp trước được chấm trước** — quản lý bằng **quy trình ngoài hệ thống** | ✅ `F2` khép lại. Xem §2 về rủi ro còn lại |
| **BA-03** | Nguồn "ngày học viên có mặt" | ✅ **Làm được** | `S3` và huy hiệu Tích cực có nguồn |
| **BA-04** | Storyline có phải nguồn sự kiện không? | ❌ **Không tính** — giống Quiz và Case Study | Gỡ `class_user_storyline_progress` khỏi nguồn sự kiện |
| **BA-05** | Chấm lại thì điểm đã cộng xử lý sao? | **Chỉ có từ không-pass → pass.** Không có trường hợp pass → không-pass | ✅ **Không cần cơ chế thu hồi.** `A5` giữ nguyên. Xem `A24` |
| **BA-06** | Examination / Entrance Test có tính không? | ❌ **Hệ thống tạm thời KHÔNG CÓ hai chức năng này** | Loại khỏi phạm vi. **KB `14` đã sửa** |
| **BA-07** | SIS có chồng lấn không? | **SIS độc lập** | Không liên quan |
| **BA-08** | Có hiện điểm/hạng ở My Learning không? | ✅ **Có hiện** | 🆕 My Learning từ "không sửa" thành **màn bị sửa** |
| **BA-09** | Huỷ ghi danh thì điểm xử lý sao? | **Đã học ít nhất 1 hoạt động thì KHÔNG huỷ ghi danh được** | ✅ Đường cày điểm này **đã bị chặn sẵn**. **KB `07` đã bổ sung `KB-LX-08`** |
| **BA-10** | `skip-foundation` có tính hoàn thành không? | ❌ **Không tính hoàn thành** | Rule cho "số khoá hoàn thành" |
| **BA-11** | L&D / Mentor / Giáo viên xem được gì? | **Chỉ là role trong Ops, tuỳ phân quyền** | Không cần xử lý riêng — Casbin lo |
| **BA-12** | Có phân biệt `Graded Activity` không? | ❌ **Hệ thống không còn khái niệm này** | **KB `07` đã sửa** — `KB-LX-04` bị gỡ |

## Ba đính chính KB phát sinh từ vòng này

| KB | Thay đổi |
|---|---|
| `07-learning-experience.md` | ❌ Gỡ `KB-LX-04` — **không còn `Graded Activity`**. 🆕 Thêm `KB-LX-08` — đã học ≥1 hoạt động thì không huỷ ghi danh được |
| `14-api-surface.md` | ❌ `Examination` và `Entrance Test` — **chức năng không có**, dù endpoint vẫn tồn tại. Kèm cảnh báo: **có endpoint không có nghĩa là có tính năng** |
| `CLAUDE.md` | Thêm nguyên tắc: **dừng ở mức phân tích, cần biết cơ chế kỹ thuật thì hỏi PO, không tự đào Swagger/DB để kết luận** |

---

# 2. ⚠️ Rủi ro còn lại sau khi chốt `BA-02`

PO chốt: bài chấm tay đi theo thứ tự nộp, mentor chấm trước bài nộp trước, quản lý bằng quy trình ngoài.

Điều này xử lý được **thứ tự xếp hạng** (`S22`). Nhưng một hệ quả vẫn còn, ghi lại để theo dõi chứ không đề nghị đổi:

> **Điểm có thể rơi vào kỳ khác với kỳ học viên làm bài.** Nộp ngày 30/9, mentor chấm xong ngày 3/10 → điểm thuộc tháng 10 dù nỗ lực thuộc tháng 9. Với `C7` (một điểm thuộc nhiều kỳ) thì lệch này lan sang mọi bảng xếp hạng chứa ngày đó.

Chỉ thành vấn đề thật khi có chiến dịch kết thúc đúng lúc còn bài chưa chấm. Cách giảm nhẹ rẻ nhất là **quy trình: chấm hết bài tồn trước khi chốt kỳ** — cùng loại giải pháp ngoài hệ thống mà PO đã chọn.

→ Nêu lại ở Gate 2 dưới dạng *Transition Requirement*, không phải yêu cầu chức năng.

---

# 3. Module / tính năng nghiệp vụ

| Hệ | Module | New / Existing | Ghi chú |
|---|---|---|---|
| LMS + Ops | **Gamification** | 🆕 New | Toàn bộ là mới |
| LMS | **Learning Experience** | Existing | **Nguồn sự kiện chính** — hoàn thành hoạt động. Chỉ đọc |
| LMS + Ops | **Assessment** | Existing | Nguồn sự kiện theo `BR-TEST`. **Chỉ Test** — loại Quiz, Case Study |
| Ops | **Grading** | Existing | Nơi chốt đạt/trượt bài chấm tay |
| LMS + Ops | **Course** | Existing | Hoàn thành khoá · `Graded Assignment` · `Pass Point` |
| LMS + Ops | **Certificate** | Existing | Mốc "hoàn thành khoá" |
| LMS + Ops | **Class** | Existing | Không sửa — là lý do sinh ra `C5` |
| LMS + Ops | **User Account** | Existing | `Block` ảnh hưởng `A14` |
| LMS | **Notification** | Existing | 🟢 Chỉ dùng phía hiển thị, không dùng cơ chế gửi hiện có |
| Ops | **Phân quyền (Casbin)** | Existing | Thêm resource mới. `BA-11` — L&D/Mentor/Giáo viên xử lý qua phân quyền thường |
| Ops | **Tenant / Hồ sơ tổ chức** | ⚠️ Chưa có | Đợt này chỉ khai tham số múi giờ (`S21`) |
| ~~LMS~~ | ~~**Storyline**~~ | ❌ **Loại** | `BA-04` — không tính, giống Quiz và Case Study |
| ~~Ops~~ | ~~**Dashboard / SIS**~~ | ❌ **Loại** | `BA-07` — độc lập |
| ~~—~~ | ~~**Examination / Entrance Test**~~ | ❌ **Loại** | `BA-06` — hệ thống không có |
| Ops | **Group / Department** | Hoãn | `N1` — chờ đồng bộ HRM |

---

# 4. Màn hình

| Hệ | Màn hình | New / Existing |
|---|---|---|
| LMS | **Thành tích của tôi** | 🆕 New |
| LMS | **Lịch sử điểm** | 🆕 New |
| LMS | **Bảng xếp hạng** | 🆕 New |
| LMS | Thông báo đẩy khi đang online | 🆕 New |
| **LMS** | **My Learning** | 🔧 **Existing — BỊ SỬA.** `BA-08`: có hiện điểm và hạng |
| Ops | **Cấu hình bảng điểm** | 🆕 New |
| Ops | **Quản lý huy hiệu** | 🆕 New |
| Ops | **Quản lý hạng** | 🆕 New |
| Ops | **Quản lý chiến dịch** | 🆕 New |
| Ops | **Bật/tắt gamification** | 🆕 New |
| Ops | Màn phân quyền | Existing — thêm resource, không đổi màn |
| LMS | Course Detail · Activity | Existing — **không sửa**, chỉ là nơi phát sinh sự kiện |

---

# 5. Data model / Entity

## 5.1 Bảng hiện có — chỉ đọc, không sửa

| Bảng | Vai trò |
|---|---|
| `users` | Chủ thể nhận điểm |
| `class_user_instances` | Cầu nối `users` ↔ `classes`. **Mọi bảng tiến độ treo vào đây** → lý do của `C5` |
| `user_course_section_progress` | **Nguồn sự kiện "hoàn thành hoạt động"** |
| `quiz_attempts` · `quiz_attempt_gradings` | Nguồn sự kiện bài Test |
| `quizzes` | `Graded Assignment`, `Pass Point` → `BR-TEST` |
| `courses_users_certificates` | **Nguồn sự kiện "hoàn thành khoá"**. Bảng duy nhất nối thẳng `users` |
| `courses` · `course_sections` | Đơn vị nội dung để chống cộng trùng (`C5`) |
| `tenant` | Nơi gắn cấu hình. **Không có trường múi giờ** → `S21` |
| `casbin_rule` | Phân quyền |
| `resources` · `attachment-files` | Ảnh huy hiệu, ảnh hạng |
| ~~`class_user_storyline_progress`~~ | ❌ **Loại** — `BA-04` |
| ~~`notifications`~~ · ~~`notification_user_instances`~~ | ❌ **Không dùng** — `S10` không đi qua cơ chế này |
| ~~`groups`~~ · ~~`departments`~~ | Hoãn — `N1` |

## 5.2 Thực thể mới — thiết kế chi tiết ở Gate 2

| Thực thể | Ràng buộc chi phối |
|---|---|
| **Cấu hình gamification** — hai công tắc · múi giờ · trần điểm/ngày | `C1`, `C6`, `C9`, `S12`, `S21` |
| **Quy tắc cộng điểm** — hành động → số điểm, bật/tắt | `C2`, `C4` |
| **Sổ giao dịch điểm** — từng lần cộng, kèm nguồn và thời điểm | `C3`, `C8` — **nền của gần như mọi thứ** |
| **Dấu nội dung đã tính điểm** — chống cộng trùng theo người học | `C5` |
| **Ngày có mặt của học viên** | `C9`, `BA-03` |
| **Danh mục chỉ số đo lường** — dùng chung ba chỗ | `S23`, `C2` |
| **Huy hiệu** + **huy hiệu đã đạt** | `S5`, `C8` |
| **Hạng** + **hạng hiện tại** | `S6`, `A3` |
| **Chiến dịch** — khoảng · phạm vi · chỉ số · trạng thái | `S15`–`S17`, `N3` |
| **Snapshot kết quả kỳ** — kèm chỉ số đã dùng | `S19`, `C7`, `O5` |

---

# 6. Job / tác vụ nền

| Job | New/Existing | Ghi chú |
|---|---|---|
| **Chốt kỳ lịch và lưu snapshot** | 🆕 New | Chạy tại biên kỳ theo **múi giờ tổ chức** (`C6`) |
| **Chốt chiến dịch khi hết hạn** | 🆕 New | |
| **Tính sẵn bảng xếp hạng** | 🆕 New *(nếu chọn hướng này)* | Phụ thuộc `OQ-B9` |

---

# 7. Role / Permission

| Vai trò | Quyền cần |
|---|---|
| **Học viên** | Xem thành tích, lịch sử điểm, bảng xếp hạng của mình và của người khác (`A15` — công khai) |
| **Nhân sự vận hành** | Cấu hình điểm · huy hiệu · hạng · chiến dịch · bật/tắt |
| **Quản trị** | Gán quyền cấu hình gamification |
| **L&D · Mentor · Giáo viên** | `BA-11` — **chỉ là role trong Ops, tuỳ phân quyền.** Không cần xử lý riêng |
| **Quản lý trực tiếp** | ⚠️ **Chưa có công cụ nào ở đợt này** — cần `US18` (hoãn) |

---

# 8. Business rule hiện có bị chạm

| Mã rule | Nội dung | Chạm thế nào |
|---|---|---|
| `KB-LX-03a` | Activity chứa Video hoàn thành khi **xem ≥80%** | Điều kiện phát sinh sự kiện |
| `KB-LX-03b` | Activity chứa Text/Ảnh hoàn thành khi **mở hiển thị** | Rủi ro đã chấp nhận (`N2`) |
| **`KB-LX-08`** 🆕 | **Đã học ≥1 hoạt động → không huỷ ghi danh được** | 🟢 **Chặn sẵn** đường cày điểm bằng ghi danh–huỷ–ghi danh lại |
| ~~`KB-LX-04`~~ | ~~`Graded Activity`~~ | ❌ **Đã bỏ** — `BA-12` |
| `KB-TEST-01` | `Manual Grading = Yes` → ép `Graded Assignment = Yes` | Bài chấm tay luôn có ngưỡng đạt |
| `KB-TEST-01a` | **`Pass Point` chỉ tồn tại khi `Graded Assignment = Yes`** | Nền của `BR-TEST` |
| `KB-TEST-01b` | **Quiz và Case Study không có ngưỡng đạt** | Nền của `BR-TEST` · `N6` |
| `BR-EDIT-07` | Test đã có người làm → **không sửa** `Graded Assignment`, `Pass Point` | 🟢 Quy tắc đếm **ổn định**, không tính lại ngược |
| `BR-COURSE-INFO-06` | `Pass Point` là điểm tối thiểu để nhận chứng chỉ | Định nghĩa "hoàn thành khoá" |
| `KB-CR-03` / `KB-CR-04` | Comment Replier **tự động thêm/xoá học viên khỏi lớp** | ⚠️ Sinh lượt ghi danh ngoài ý muốn → củng cố `C5` |
| `KB-MAIL-03` | 8 mail luồng chấm điểm **đang tắt** | Học viên không được báo khi chấm xong |

## Rule mới cho gamification

| Mã | Nội dung | Nguồn |
|---|---|---|
| `BR-TEST` | Test `Graded Assignment = Yes` → tính khi **đạt**. `= No` → tính khi **hoàn thành**. Quiz, Case Study, **Storyline** → **không tính** | `A22` + `BA-04` |
| `BR-REGRADE` 🆕 | **Chấm lại chỉ đi một chiều: không-pass → pass.** Không có trường hợp pass → không-pass. Nên **không cần cơ chế thu hồi điểm hay huy hiệu** | `BA-05` |
| `BR-SKIP` 🆕 | **`skip-foundation` không tính là hoàn thành khoá** | `BA-10` |

---

# 9. NFR

| Khía cạnh | Trạng thái |
|---|---|
| **Hiệu năng — bảng xếp hạng** | 🔴 `OQ-B9` — chặn Gate 2 |
| **Hiệu năng — ghi sự kiện** | Chưa ước lượng |
| **Dung lượng** | Sổ giao dịch tăng tuyến tính theo hoạt động học |
| **Tính đúng đắn** | Snapshot kỳ đã chốt **không được đổi** (`O5`, `A14`) |
| **Múi giờ** | Biên kỳ và biên ngày phải nhất quán (`C6`, `C9`) |
| **Riêng tư** | ✅ Đã chốt — công khai danh tính (`A15`) |

---

# 10. Assumption mới phát sinh

| # | Giả định | Vì sao cần xác nhận |
|---|---|---|
| **A24** | **Chấm lại từ không-pass thành pass thì học viên ĐƯỢC cộng điểm** cho bài đó | PO nói *"chấm lại không tính"* — tôi hiểu là **không cần lo chuyện thu hồi**, chứ không phải bài chấm lại thì mất điểm. Nếu hiểu sai thì học viên bị thiệt khi mentor chấm sai lần đầu |
| **A25** | **Điểm hiện ở My Learning là điểm tích luỹ và hạng hiện tại**, không phải điểm theo kỳ | `BA-08` nói "có hiện" nhưng chưa rõ hiện con số nào |

---

# 11. Còn lại trước Gate 2

| # | Câu | Owner |
|---|---|---|
| `OQ-B2` | Dữ liệu tiến độ học có dấu thời gian không | Dev |
| `OQ-B9` | Bảng xếp hạng chịu tải được không | Dev |
| `OQ-B12` | Thời điểm đạt huy hiệu / hoàn thành khoá / hoàn thành bài Test có lưu được không | Dev |
| `OQ-B11` | Múi giờ tổ chức khai ở đâu trong đợt này | PO + Dev |
| `A24` · `A25` | Hai giả định ở §10 | PO |

**Chốt xong là chạy `/compact` rồi dựng Impact Matrix (Bước 6).**
