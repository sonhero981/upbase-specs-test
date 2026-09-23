# 03 — Assessment (Test & Quiz)

| | |
|---|---|
| Hệ | UpLMS Ops (cấu hình) · UpLMS (học viên làm bài) |
| Trạng thái | Active — **nhưng page "Quản lý bài kiểm tra trong lớp" đang `hidden`** |
| Nguồn UG | `tao-bai-test-quiz-cho-khoa-hoc.md`, `hoat-dong-kiem-tra/*` (student), `quan-ly-bai-kiem-tra-trong-lop-test-quiz.md` (ẩn) |

---

## 1. Phân biệt Test / Quiz / Case Study

| | **Test** | **Quiz** | **Case Study** |
|---|---|---|---|
| Vị trí | Section Test, Midterm Test, Final Test | Trong Activity, hoặc trong Video | Trong Section |
| Tính điểm khoá học | **Có** (nếu Graded Assignment = Yes) | Có thể tính điểm hoàn thành Quiz, **nhưng không tính vào hoàn thành khoá học** | **Không** |
| Loại câu hỏi | Trắc nghiệm, tự luận, hoặc cả hai | **Chỉ trắc nghiệm** | Theo Question Bank |
| Số lượt làm | Theo Attempt (Unlimited / Limited) | `❓BA` | **1 lượt duy nhất** |
| Resume khi gián đoạn | **Có** | `❓BA` | `❓BA` |

---

## 2. Cấu hình bài Test (phía Ops)

| Field | Giá trị | Mặc định | Ghi chú |
|---|---|---|---|
| Name | Text | — | |
| **Type of Test** | `Multiple Choice` \| `Constructed` \| `Mixed` | Multiple Choice | **Quyết định danh sách câu hỏi hiển thị ở Add Question** |
| **Test Mode** | `Tutor` \| `Timed` | Tutor | Tutor = không giới hạn thời gian |
| **Manual Grading** | `Yes` \| `No` | — | **Chỉ hiện khi Type = Constructed hoặc Mixed.** No → Mixed chấm tự động phần trắc nghiệm; Constructed toàn phần thì không chấm |
| **Graded Assignment** | `Yes` \| `No` | — | Có tính điểm cho toàn khoá hay không |
| **Grading Preference** | `After each question` \| `After all questions` | After all questions | Thời điểm hiện đáp án + lời giải |
| **Pass Point** | `Auto 50%` \| `Manual` | Auto 50% | Manual → Admin nhập số |
| **Attempt** | `Unlimited` \| `Limited` | Unlimited | |
| **Total Score** | Number | — | **> 0**, thập phân tối đa **2 chữ số**, có thể khác thang 100 |

### Ràng buộc liên trường — quan trọng

> **Manual Grading = Yes** → hệ thống ép **Graded Assignment = Yes** và **Attempt = 1**.

Đây là ràng buộc cascade duy nhất được ghi rõ trong UG. Mọi thay đổi chạm tới 3 trường này phải xét cùng nhau.

---

## 3. Thêm câu hỏi vào Test

### Lọc theo Type of Test

| Type of Test | Danh sách câu hỏi hiển thị |
|---|---|
| Multiple Choice | Toàn bộ câu trắc nghiệm trên hệ thống |
| Constructed | Toàn bộ câu tự luận trên hệ thống |
| Mixed | Cả trắc nghiệm và tự luận |

### Logic thứ tự câu hỏi

| Thao tác | Kết quả |
|---|---|
| Chọn đơn lẻ từng câu | Câu chọn trước đứng trước |
| Chọn toàn bộ câu trong trang | Giữ nguyên thứ tự đang hiển thị ở màn Add Question |
| Chọn → bỏ chọn → chọn lại | **Câu đó bị đẩy xuống cuối danh sách** |

Thứ tự ở **Setup Score** và **Reorder** kế thừa thứ tự chọn ở **Add Question**.

### Setup Score

Điểm mặc định chia đều: `100 / tổng số câu`. Operator chỉnh lại từng câu được.

> UG mục IV ghi lỗi *"Không chuyển được sang Reorder — Total Score sau khi điều chỉnh có tổng chưa bằng 100"*, nhưng phần cấu hình lại nói Total Score "có thể điền khác thang điểm 100". `❓BA` — hai chỗ này mâu thuẫn.

### Reorder — 3 cách

1. Kéo thả từng câu
2. Chọn câu → Action → Top / Bottom / vị trí cụ thể
3. Chọn nhiều câu → Top / Bottom — **chỉ khi các câu được chọn nằm liền kề nhau**

---

## 4. Business Rule

### Nguyên văn từ UG (mã có sẵn)

| ID | Rule |
|---|---|
| BR-QUESTION-01 | Câu hỏi thêm vào Test/Quiz được lấy từ Question Bank. |
| BR-QUESTION-02 | Danh sách câu hỏi hiển thị phụ thuộc vào Type of Test. |
| BR-QUESTION-03 | Chọn đơn lẻ từng câu → câu nào chọn trước đứng trước. |
| BR-QUESTION-04 | Chọn toàn bộ câu trong trang → giữ nguyên thứ tự đang hiển thị. |
| BR-QUESTION-05 | Chọn → bỏ chọn → chọn lại → câu đó xuống cuối danh sách. |
| BR-QUESTION-06 | Thứ tự tại Setup Score và Reorder phụ thuộc thứ tự chọn tại Add Question. |
| BR-REORDER-01 | Số thứ tự phản ánh thứ tự thực tế của câu hỏi trong bài Test/Quiz. |
| BR-TEST-01 | Bài kiểm tra chấm thủ công **chưa chấm xong** → điểm trong file export **hiển thị rỗng**. |
| BR-TEST-STATUS-01 | Bài **chấm tự động**: trạng thái gồm `Unsubmitted` (chưa nộp), `Submitted` (đã hoàn thành). |
| BR-TEST-STATUS-02 | Bài **chấm thủ công**: trạng thái gồm `Unsubmitted`, `Awaiting Grading` (đã nộp, chờ chấm), `Finish Grading` (đã chấm xong). |

*(Rule chỉnh sửa Test khi đã có người làm: xem BR-EDIT-06 → BR-EDIT-09 ở [01-course.md](01-course.md))*

### Rule Claude trích thêm

| ID | Rule | Nguồn |
|---|---|---|
| KB-TEST-01 | Manual Grading = Yes → **ép** Graded Assignment = Yes và Attempt = 1. | tao-bai-test mục II + III |
| KB-TEST-02 | Chỉ di chuyển được nhiều câu hỏi cùng lúc khi các câu **liền kề nhau**. | tao-bai-test mục III |
| KB-TEST-03 | Quiz **chỉ có dạng trắc nghiệm**. | tao-bai-test mục II |
| KB-TEST-04 | Quiz tồn tại trong hoạt động học **và trong Video** của hoạt động học. | tao-bai-test mục II |
| KB-TEST-05 | Bài Test đã có người làm → chỉ sửa được **tên bài Test** và **thứ tự câu hỏi (Reorder)**. | tao-bai-test mục II |
| KB-TEST-06 | Hết thời gian làm bài → hệ thống **tự động nộp** theo các câu đã làm, kể cả khi học viên chưa bấm Finish. | UG học viên, hoat-dong-kiem-tra |
| KB-TEST-07 | Câu hỏi xuất hiện **trong Video không dùng để tính điểm** khoá học. | UG học viên, thao-tac-voi-video |
| KB-TEST-08 | Quiz dạng "hiển thị đáp án ngay": sau khi đã xem đáp án thì **không chọn lại được**. | UG học viên, lam-bai-quiz |

---

## 5. Trải nghiệm làm bài (phía học viên)

### Bố cục

Câu hỏi hiển thị 1 cột (đề → câu hỏi → đáp án) hoặc 2 cột (đề trái, câu hỏi + đáp án phải). Do **Question Layout** ở Question Bank quyết định.

### Công cụ khi làm bài

| Công cụ | Hành vi |
|---|---|
| Danh sách câu hỏi | Chuyển nhanh giữa câu |
| Bộ lọc | `Unattempted` \| `Attempted` \| `Flag to Review` |
| Flag to Review | Gắn cờ xem lại |
| Clear Selection | Xoá đáp án câu hiện tại |
| Highlight / Unhighlight | Bôi đậm văn bản |
| **Scratch Pad** | Nháp tạm, lưu **theo câu hỏi** — **mất khi chuyển sang câu khác** |
| Calculator | Máy tính |
| Confirm Answer | Hiện đáp án + lời giải ngay (với loại hiển thị đáp án ngay) |
| Finish | Nộp bài |

> ⚠️ **Scratch Pad mất nội dung khi chuyển câu** — đây là hành vi dễ bị hiểu nhầm là bug. Ghi rõ để không bị "sửa nhầm" trong dự án sau.

### Resume bài bị gián đoạn

Áp dụng cho **Section Test, Midterm Test, Final Test**. Khi mở lại bài chưa hoàn thành:

| Tình huống | Lựa chọn |
|---|---|
| Lượt làm dở là **lượt cuối cùng** | `Continue` — giữ nguyên câu đã làm, **đồng hồ tiếp tục đếm ngược trừ đi khoảng gián đoạn** |
| **Vẫn còn lượt khác** | `Continue the previous attempt` (tiếp tục, giữ câu đã làm) hoặc `Start a new attempt` (làm lại từ đầu) |

Nếu đồng hồ trên hộp thoại chạy về `00:00:00` → học viên phải bấm `Continue` để hệ thống nộp bài và tính kết quả theo các câu đã làm.

### Kết quả bài thi

Hiển thị: tổng điểm · kết quả theo từng chủ đề · chi tiết từng câu (tên, chủ đề, loại, kết quả, % học viên làm đúng, thời gian làm) · số câu chia theo trắc nghiệm/tự luận (xanh = đúng, đỏ = sai).

---

## 6. ⚠️ Page ẩn: Quản lý bài kiểm tra trong lớp

`uplms-ops/class-management/.../quan-ly-bai-kiem-tra-trong-lop-test-quiz.md` — **325 dòng, `hidden: true`**.

Đây là màn Test/Quiz trong Class Detail: danh sách bài kiểm tra của khoá gắn với lớp, kết quả từng học viên, export điểm. Tính năng **đã có nhưng đang ẩn**.

> Liên quan trực tiếp tới BR-TEST-01 (export điểm rỗng khi chưa chấm xong) — rule này thuộc màn đang ẩn. Khi phân tích impact về điểm/export, phải hỏi BA xem màn này có được bật lại không.

`❓BA` — Claude chưa đọc chi tiết page này. Cần xác nhận có đưa vào KB không.

---

## 7. Phụ thuộc

| Module | Quan hệ |
|---|---|
| **Question Bank** | Nguồn câu hỏi; Type of Test lọc danh sách |
| **Course** | Test thuộc Section (Section Test) hoặc thuộc Course (Mid/Final) |
| **Class** | Kết quả bài kiểm tra ghi nhận theo học viên trong lớp |
| **Grading** | Manual Grading = Yes → bài chảy vào luồng chấm tay |
| **Notification & Email** (ẩn) | Kết quả bài kiểm tra gửi thông báo cho học viên |
| **Dashboard khoá học** | "Your Learning Results" tính từ kết quả Test theo Section |
| **SIS Dashboard** | Dashboard "Phân phối điểm" lấy dữ liệu bài kiểm tra |

---

## 8. Điểm cần BA xác nhận

| # | Câu hỏi |
|---|---|
| Q1 | Mâu thuẫn Total Score: cấu hình nói "có thể khác thang 100", nhưng lỗi thường gặp nói "tổng chưa bằng 100 thì không sang được Reorder". Cái nào đúng? |
| Q2 | Quiz có Attempt không? Có resume khi gián đoạn không? UG chỉ nói Test. |
| Q3 | Attempt = Limited thì nhập số ở đâu, giới hạn bao nhiêu? |
| Q4 | Bài Mixed với Manual Grading = No: phần tự luận không chấm thì điểm tổng tính thế nào? |
| Q5 | Page "Quản lý bài kiểm tra trong lớp" đang ẩn — có kế hoạch bật lại không? Có nên đưa vào KB? |
| Q6 | Grading Preference = After each question áp dụng được cho Test Mode = Timed không? |
