# 05 — Grading (Chấm điểm thủ công)

| | |
|---|---|
| Hệ | UpLMS Ops |
| Đường dẫn | Operations → Class → Test/Quiz → Grade work · Class Detail → Mark · Class → Grading List |
| Trạng thái | Active |
| Vai trò | **Mentor**, **Mentor chính (Main Responsible)** |
| Nguồn UG | `uplms-ops/cham-diem-grading/cham-diem-thu-cong/` (5 page) |

> ⚠️ **Cả 5 page của cụm này đều thiếu khai báo `Module chính`.** Quan hệ chéo dưới đây do Claude suy ra từ nội dung — cần BA xác nhận.

---

## 1. Phạm vi

Chấm tay **các câu tự luận**. Kích hoạt khi bài Test có `Manual Grading = Yes` (chỉ khả dụng với Type of Test = Constructed hoặc Mixed).

4 chức năng: chấm điểm bài làm · phân công người chấm · chấm lại (regrading) · lịch sử chấm.

---

## 2. Phân vai — Mentor vs Mentor chính

| Quyền | Mentor | Mentor chính |
|---|---|---|
| Xem bài được giao | ✅ | ✅ |
| Xem **toàn bộ** bài test/quiz của lớp | ❌ | ✅ |
| **Assign Grader** (giao người chấm) | ❌ | ✅ |
| Filter theo Mentor ở màn Mark | ❌ | ✅ |
| Review & duyệt kết quả trước khi gửi học viên | ❌ | ✅ |
| Yêu cầu chấm lại, giao lại người chấm | ❌ | ✅ |

Mentor chính = **Main Responsible** của lớp, đặt ở `Class Detail → Tab Mentors` (BR-MENTOR-01).

---

## 3. Hai màn quản lý bài chấm

| | **Mark** | **Grading List** |
|---|---|---|
| Vị trí | Class Detail → Mark | Class (sub-menu) → Grading List |
| Phạm vi | **Một lớp** | **Tất cả các lớp** của người dùng |
| Cột riêng | Có cột `Grader` (chỉ Mentor chính thấy) | Không có cột Grader |
| Filter | Status, Test/Quiz, **Mentor** (chỉ Mentor chính) | Status, **Class**, Test/Quiz |

Cột chung: `Student name` · `Test/quiz` · `Status` · `Submission time` · `Grading attempts` · `Final score` · `Comment`. Search theo `Student name`.

---

## 4. Trạng thái bài chấm

| Trạng thái | Nghĩa | Áp dụng |
|---|---|---|
| `Unsubmitted` | Học viên chưa nộp | cả 2 loại |
| `Submitted` | Đã hoàn thành | chấm **tự động** |
| `Awaiting Grading` | Đã nộp, chờ chấm | chấm **thủ công** |
| `Finish Grading` | Đã chấm xong, kết quả đã gửi học viên | chấm **thủ công** |
| `Regrading` | Mentor chính yêu cầu chấm lại | chấm **thủ công** |

*(BR-TEST-STATUS-01, BR-TEST-STATUS-02 — xem [03-assessment.md](03-assessment.md))*

---

## 5. Luồng chấm & duyệt

```
Học viên nộp bài
      ↓
[Awaiting Grading]
      ↓  Mentor chính: Assign Grader → email cho mentor được giao
Mentor chấm
      ↓  Submit to review → email cho Mentor chính
Mentor chính review
      ├─ Finish    → [Finish Grading] → gửi kết quả cho học viên qua Email
      └─ Regrading → [Regrading] → nhập Reason + chọn Mentor (có thể đổi người chấm)
                                    → email cho mentor được phân chấm lại
```

**Học viên cũng khởi tạo được regrading:** tại màn kết quả bài test → `Request Regrading` → nhập lý do (**bắt buộc**) → Save → hệ thống thông báo cho Mentor chính.

---

## 6. Cách chấm

### 6.1 Truy cập màn chấm — 4 đường vào

1. Từ **email** (link chấm bài gửi cho người được giao)
2. Test/Quiz trong lớp → `Grade work` tại Action của học viên
3. `Grading List` → `Grade`
4. Test/Quiz Detail trong Class Detail → `Grade`

### 6.2 Mã màu câu hỏi

| Màu | Nghĩa |
|---|---|
| 🔴 Đỏ | Câu trắc nghiệm trả lời **sai** |
| 🟢 Xanh | Trắc nghiệm **đúng**, hoặc tự luận **đã chấm** |
| ⚪ Xám | Câu tự luận **chưa chấm** |

### 6.3 Chấm câu trả lời bằng File

Tải file bài làm về → chấm/ghi chú trên file → `Upload graded file` → điền điểm → `Save`.

> ⚠️ **`Cancel` sau khi upload sẽ xoá luôn file chấm điểm.** Xoá file cũng **xoá điểm đã chấm gắn với file đó**.

### 6.4 Chấm bài Word/Excel trực tiếp trên hệ thống

Bôi đoạn cần chấm → hiện 2 lựa chọn:

| Lựa chọn | Bắt buộc | Tuỳ chọn |
|---|---|---|
| **Comment** | Để lại bình luận | Có thể thêm điểm |
| **Grading** | Chấm điểm | Có thể thêm bình luận |

### 6.5 Hoàn tất

`Comment & Recommendations` (bình luận + gợi ý cải thiện) → `Finish` để gửi kết quả cho học viên.

---

## 7. Business Rule

| ID | Rule | Nguồn |
|---|---|---|
| KB-GRAD-01 | Chỉ chấm câu học viên **đã trả lời (Submitted)**; câu `Unsubmitted` hệ thống **tự động chấm 0 điểm**. | README + cham-diem-bai-lam mục III |
| KB-GRAD-02 | **Tổng điểm một câu hỏi không được vượt quá số điểm đã cài đặt** cho câu đó, nếu không hệ thống báo lỗi. | cham-diem-bai-lam mục III |
| KB-GRAD-03 | Mentor thường chỉ xem/chấm bài được giao; **Mentor chính xem được toàn bộ** bài test/quiz. | README mục IV |
| KB-GRAD-04 | Việc chấm điểm **được lưu tạm đến thời điểm thoát**, có thể tiếp tục sau (đóng trình duyệt hoặc Exit đều được). | README + cham-diem-bai-lam |
| KB-GRAD-05 | **Chỉ Mentor chính** có quyền Assign Grader và có filter Mentor tại màn Mark. | quan-ly-and-phan-cong mục III |
| KB-GRAD-06 | Ngay sau khi Assign, hệ thống **gửi thông báo cho mentor được giao chấm**. | quan-ly-and-phan-cong mục II |
| KB-GRAD-07 | Danh sách người chấm khi Assign Grader = **danh sách Mentor của lớp đó**. | quan-ly-and-phan-cong mục II |
| KB-GRAD-08 | **Chỉ chấm lại được bài đã được chấm điểm.** | cham-lai-regrading mục III |
| KB-GRAD-09 | `Finish` → trạng thái `Finish Grading` + gửi kết quả cho học viên qua Email. `Regrading` → trạng thái `Regrading`. | cham-lai-regrading mục III |
| KB-GRAD-10 | Mentor chính **có thể giao bài chấm lại cho người chấm mới**. | cham-lai-regrading mục III |
| KB-GRAD-11 | Học viên gửi Request Regrading **bắt buộc nhập lý do**. | cham-lai-regrading mục IV |
| KB-GRAD-12 | `Cancel` sau khi upload file chấm → **file chấm bị xoá**. Xoá file → **điểm gắn với file cũng bị xoá**. | cham-diem-bai-lam mục II + IV |
| KB-GRAD-13 | Grading History lưu: số thứ tự lần chấm, thời gian hoàn thành, người chấm, điểm. | lich-su-cham-bai mục II |

---

## 8. Phụ thuộc — điểm nóng của hệ thống

| Module | Quan hệ | Ghi chú |
|---|---|---|
| **Test/Quiz** | `Manual Grading = Yes` mới sinh bài cần chấm | Cấu hình ở Ops quyết định có luồng chấm hay không |
| **Question Bank** | Chỉ câu **tự luận** mới chấm tay | Loại câu hỏi quyết định |
| **Class** | Bài chấm gắn theo lớp; Main Responsible lấy từ tab Mentors | |
| **Staff** | Mentor lấy từ Staff List | |
| **Email / Notification** ⚠️ | **4 điểm gửi email**: assign grader · submit to review · regrading assign · gửi kết quả cho học viên | **Module Email đang `hidden`** — xem §9 |
| **Student (UpLMS)** | Học viên xem kết quả, gửi Request Regrading | |
| **BR-TEST-01** | Bài chấm tay chưa xong → điểm trong file export **rỗng** | Rule nằm ở màn đang ẩn |

---

## 9. 🚨 Rủi ro đã được BA xác nhận — 8 mail chấm điểm đang tắt

Bản KB đầu tiên suy đoán nguyên nhân là "module Email đang ẩn" — **sai**. BA xác nhận (23/09/2026): hệ thống gửi mail tự động vẫn chạy, nhưng **8 mail thuộc luồng chấm điểm đang tạm ngưng kích hoạt**.

| STT mail | Nội dung | Mắt xích |
|---|---|---|
| 17 | Báo mentor có học viên vừa nộp bài | Bài về hàng chờ |
| 18 | Gửi mentor mới thêm vào lớp danh sách bài đã hoàn thành | Onboard mentor |
| 19 | Báo học viên bài đã chấm xong + link kết quả | **Trả kết quả** |
| 20 | Báo học viên hoàn tất chấm ở lần thứ N + link | **Trả kết quả** |
| 32 | Nhắc mentor danh sách đang chờ chấm | Nhắc việc |
| 33 | Báo mentor có yêu cầu chấm lại + lý do + link | **Regrading** |
| 34 | Báo main mentor có yêu cầu chấm lại từ học viên | **Regrading** |
| 35 | Báo main mentor có yêu cầu review bài chấm | **Review** |

**Hệ quả thực tế:** toàn bộ luồng chấm điểm hiện **không có thông báo đẩy**. Mentor không biết có bài mới cho đến khi tự vào màn Mark/Grading List; học viên không biết bài đã chấm xong cho đến khi tự mở kết quả. Cách 1 trong 4 đường vào màn chấm (*"từ email — click link chấm bài"*, §6.1) **hiện không dùng được**.

`❓BA` — có cơ chế thông báo thay thế không, hay chấp nhận vận hành thủ công? Chi tiết 30 mail: [13-mail-events.md](13-mail-events.md).

---

## 10. Điểm cần BA xác nhận

| # | Câu hỏi |
|---|---|
| Q1 | **Module Email đang ẩn — 4 email trong luồng chấm có thực sự gửi được không?** (rủi ro cao nhất) |
| Q2 | Cả 5 page của cụm Grading thiếu khai báo Module chính — quan hệ chéo Claude suy ra ở §8 có đúng không? |
| Q3 | Bài Mixed: phần trắc nghiệm chấm tự động, phần tự luận chấm tay — điểm tổng hợp lại ở bước nào? |
| Q4 | Regrading có giới hạn số lần không? `Grading attempts` tăng không giới hạn? |
| Q5 | Mentor chính tự chấm bài của mình rồi tự Finish được không, hay bắt buộc qua bước review? |
| Q6 | Học viên Request Regrading có giới hạn số lần / thời hạn không? |
| Q7 | Nếu Mentor bị xoá khỏi lớp khi đang giữ bài chưa chấm xong thì bài đó về đâu? |
