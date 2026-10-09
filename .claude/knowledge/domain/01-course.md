# 01 — Course (Khoá học & nội dung)

| | |
|---|---|
| Hệ | UpLMS Ops (dựng) · UpLMS (học viên tiêu thụ) |
| Đường dẫn | Academic Management → Course & Materials → Courses |
| Trạng thái | Active |
| Vai trò | UpLMS Operator, L&D |
| Nguồn UG | `uplms-ops/academic-management/quan-ly-khoa-hoc-courses/` (6 page) |

---

## 1. Vị trí trong hệ thống

Course là **đơn vị nội dung gốc**: chứa bài học, bài kiểm tra, quiz, tài liệu và chứng chỉ. Class không tự chứa nội dung — lớp phải gắn vào một Course đã Publish. **Course phải hoàn chỉnh trước khi mở lớp.**

Luồng dựng khoá học — 4 bước tuần tự:

```
1. Course Info  →  2. Course Content  →  3. Resource  →  4. Certificate
   (thông tin)      (Section/Activity)    (tài liệu)     (mẫu chứng chỉ)
```

---

## 2. Cấu trúc nội dung

```
Course
└── Section                    ← Learning Outcome tạo ở cấp này
    ├── Activity
    │   └── Tab (≥1)
    │       └── Document: Text | Video | Quiz
    ├── Section Test
    ├── Case Study
    └── Storyline
Course-level: Midterm Test, Final Test
```

> UG ghi "cấu trúc gồm 2 cấp: Section → Activity" (BR-COURSE-02), nhưng phần hướng dẫn mô tả thêm tầng Tab → Document bên trong Activity. `❓BA` — chốt lại số tầng chính thức.

---

## 3. Field

### 3.1 Course Info

| Field | Bắt buộc | Kiểu | Giá trị / Ràng buộc |
|---|---|---|---|
| Course Name | **Có** | Text | — |
| Describe | Không | Text | Mô tả nội dung/mục tiêu |
| Code | Không | Text | **Unique toàn hệ thống** — trùng thì báo lỗi |
| Tag | Không | Multi-select | Chọn tag có sẵn hoặc tạo mới |
| Course Category | **Có** | Dropdown | Chọn từ danh mục có sẵn (BR-COURSE-INFO-01) |
| Type | **Có** | Enum | `Normal Course` \| `Foundation Course` — chỉ chọn 1 tại thời điểm tạo |
| Foundation Course | Không | Dropdown | Chỉ hiện khi Type = Normal. **Chỉ liệt kê Foundation cùng Category** |
| Pass Point | **Có** | Number | Điểm tối thiểu để nhận chứng chỉ |
| Điểm thành phần | **Có** | Number ×4 | Tiến độ học / Section Test / Mid Test / Final Test — **tổng phải = 100** |

### 3.2 Section

| Field | Bắt buộc | Ghi chú |
|---|---|---|
| Section Name | **Có** | — |
| Section Short Name | Không | Dùng khi biểu đồ hạn chế độ dài |
| Describe | Không | — |
| Section Code | — | **Hệ thống tự sinh** theo rule của khoá (BR-CONTENT-05) |

### 3.3 Learning Outcome (cấp Section)

| Field | Bắt buộc | Ghi chú |
|---|---|---|
| Name | **Có** | Tên hiển thị |
| Mô tả | Không | — |
| Add more learning outcome | Không | Các tiêu chí con, gắn được với từng Activity trong Section |

### 3.4 Activity

| Field | Bắt buộc | Kiểu | Giá trị / Ràng buộc |
|---|---|---|---|
| Activity Name | `❓BA` | Text | UG không đánh dấu (*) |
| Duration | Không | Number | Thời lượng ước lượng |
| Type of Activity | `❓BA` | Enum | `Text` \| `Video` \| `Quiz` — **chỉ dùng để hiển thị icon** phía học viên (BR-CONTENT-06) |
| Choose Learning Outcome | Không | Multi-select | Chỉ chọn được LO thuộc Section chứa Activity |
| Upload File | Không | File | Từ kho hệ thống hoặc thiết bị, **≤500MB**, nhiều file |
| Activity Code | — | — | **Hệ thống tự sinh** (BR-CONTENT-05) |

### 3.5 Resource (bước 3)

| Ràng buộc | Giá trị |
|---|---|
| Định dạng | .jpg .jpeg .png .gif .webp .mp4 .pdf .docx .doc .xls .xlsx .csv .txt .ppt .pptx .zip .mp3 |
| Dung lượng / file | **500MB** |
| Số file / lần upload | **10** |

> Xoá tài liệu ở đây **chỉ gỡ khỏi khoá học, không xoá khỏi kho tài nguyên hệ thống**.

---

## 4. Trạng thái Course

| Trạng thái | Ý nghĩa | Hệ quả |
|---|---|---|
| **Draft** | Đang tạo dở, chưa publish | **Không thêm được vào lớp** |
| **Publish** | Hoàn chỉnh, sẵn sàng | Thêm được vào lớp |
| **Lock** | Đã có ≥1 học viên bắt đầu học | Ràng buộc chỉnh sửa (xem §6) |
| **Block** | Bị chặn | **Không thêm được vào lớp** |

Điều kiện Publish: **đã tạo nội dung VÀ đã gán chứng chỉ** (BR-CONTENT-09).

---

## 5. Business Rule — nguyên văn từ UG

### Chung

| ID | Rule |
|---|---|
| BR-COURSE-01 | Khoá học sau khi tạo mặc định ở trạng thái **Draft**. |
| BR-COURSE-02 | Cấu trúc nội dung khoá học gồm 2 cấp: **Section → Activity**. |

### Course Info

| ID | Rule |
|---|---|
| BR-COURSE-INFO-01 | **Course Category** bắt buộc chọn từ danh sách có sẵn. |
| BR-COURSE-INFO-02 | Một khoá học chỉ được chọn một **Type** tại thời điểm tạo. |
| BR-COURSE-INFO-03 | Hệ thống hỗ trợ 2 Type: **Normal Course** và **Foundation Course**. |
| BR-COURSE-INFO-04 | Nếu Type = Normal, Admin có thể gắn kèm một Foundation Course; khi đó học viên **phải hoàn thành Foundation trước** khi học khoá chính. |
| BR-COURSE-INFO-05 | Với Normal Course, Admin có thể chọn hoặc không chọn Foundation Course. |
| BR-COURSE-INFO-06 | **Pass Point** là điểm yêu cầu học viên phải đạt để nhận chứng chỉ. |
| BR-COURSE-INFO-07 | Tổng điểm các thành phần phải bằng **100**. |
| BR-COURSE-INFO-08 | Thành phần điểm gồm: **Tiến độ học, Section Test, Mid Test, Final Test**. |

### Loại khoá học

| ID | Rule |
|---|---|
| BR-COURSE-TYPE-01 | **Foundation Course** là khoá nền tảng, cần hoàn thành trước khoá chính. |
| BR-COURSE-TYPE-02 | **Normal Course** có thể yêu cầu hoàn thành một số Foundation Course trước. |
| BR-COURSE-TYPE-03 | Khi Block một Foundation Course đã gắn Normal Course → hệ thống **cảnh báo Foundation sẽ bị unlink** khỏi các Normal liên quan. |
| BR-COURSE-TYPE-04 | Khi Block Normal Course → hệ thống **cảnh báo khoá sẽ bị remove khỏi các lớp chưa bắt đầu**. |

### Course Content

| ID | Rule |
|---|---|
| BR-CONTENT-01 | Tạo **Section** trước khi tạo **Activity**. |
| BR-CONTENT-02 | **Learning Outcome** được tạo ở cấp **Section**. |
| BR-CONTENT-03 | Một Section có thể có một hoặc nhiều Learning Outcome. |
| BR-CONTENT-04 | Một Activity có thể gắn một hoặc nhiều LO **đã tạo trong Section chứa Activity đó**. |
| BR-CONTENT-05 | **Section Code** và **Activity Code** được hệ thống tạo tự động theo rule của khoá học. |
| BR-CONTENT-06 | **Type of Activity** dùng để hiển thị icon trên giao diện học viên UpLMS. |
| BR-CONTENT-07 | Type of Activity gồm: **Text, Video, Quiz**. |
| BR-CONTENT-08 | Activity có thể đính kèm một hoặc nhiều Resource. |
| BR-CONTENT-09 | Khoá học chỉ được Publish khi **đã tạo nội dung và gán chứng chỉ**. |

### Activity & Document

| ID | Rule |
|---|---|
| BR-ACTIVITY-01 | Activity phải thuộc một Section đã tồn tại. |
| BR-ACTIVITY-02 | Một Activity có thể có một hoặc nhiều Tab. |
| BR-ACTIVITY-03 | Mỗi Tab có thể có một hoặc nhiều Document. |
| BR-ACTIVITY-04 | Document trong Activity gồm 3 loại: **Text, Video, Quiz**. |
| BR-ACTIVITY-05 | Với Document dạng Text, nội dung có thể chứa cả định dạng ảnh. |
| BR-ACTIVITY-06 | Timeline được sắp xếp theo thứ tự thời gian của video. |
| BR-ACTIVITY-07 | Câu hỏi trong Video được sắp xếp theo thứ tự thời gian của video. |

### Chỉnh sửa khoá học — **nhóm rule rủi ro cao nhất**

| ID | Rule |
|---|---|
| BR-EDIT-01 | Lớp chưa có học viên, hoặc có nhưng chưa học → **sửa được tất cả** thông tin khoá học. |
| BR-EDIT-02 | Đã có học viên học nhưng chưa ai học xong → Course Info vẫn sửa được tất cả. |
| BR-EDIT-03 | Đã có học viên học, chưa học xong → sửa/xoá được Section, Activity, Tab dạng Text/Video **nếu không chứa Test/Quiz/Case Study đã có người làm**. |
| BR-EDIT-04 | Đã có học viên học, chưa học xong → được phép kéo thả cấu phần học. |
| BR-EDIT-05 | Đã có học viên học, chưa học xong → được thêm cấu phần học và bài Test. |
| BR-EDIT-06 | Test/Quiz/Case Study **đã có người làm** → không được xoá bài đó và **không được xoá cấu phần chứa nó**. |
| BR-EDIT-07 | Test/Quiz đã có người làm → **không sửa** được Type of Test, Test Mode, Graded Assignment, Grading Preference, Pass Point, Attempt.<br>⚠️ **Ngoại lệ (PO xác nhận 23/09/2026): không áp cho lượt làm bài của `Test Account`** — khoá vẫn sửa tiếp được. Xem [06-user-account.md](06-user-account.md) §8b `KB-USER-TA-02`. |
| BR-EDIT-08 | Test/Quiz đã có người làm → danh sách câu hỏi **chỉ xem**, không thêm/xoá/sửa tại Add Question. |
| BR-EDIT-09 | Test/Quiz chưa có người làm → sửa được toàn bộ Setting, thêm/xoá câu hỏi, xoá bài test. |
| BR-EDIT-10 | Đã có học viên **học xong** → được thêm cấu phần học nhưng **không được thêm Test/Quiz/Case Study**. |

### Cập nhật nội dung cho học viên đang học

| ID | Rule |
|---|---|
| BR-STUDENT-CONTENT-01 | Khi khoá đã có học viên học, cấu phần mới thêm **không tự động hiển thị ngay** cho học viên. |
| BR-STUDENT-CONTENT-02 | Để học viên thấy cấu phần mới, cần **cập nhật Course Content cho lớp hoặc cho từng học viên**. |

### Copy Course Content

| ID | Rule |
|---|---|
| BR-COPY-01 | Nếu Activity đã gắn LO, liên kết được giữ nguyên **nếu Copy đồng thời cả LO và Section chứa Activity đó**. |
| BR-COPY-02 | Khoá đã có học viên hoàn thành 100% → **chỉ Copy được bài kiểm tra không tính điểm**. |

### Xoá dữ liệu

| ID | Rule |
|---|---|
| BR-DELETE-01 | Không được xoá Test/Quiz/Case Study đã có học viên làm. |
| BR-DELETE-02 | Không được xoá cấu phần cha nếu bên trong chứa Test/Quiz/Case Study đã có học viên làm. |
| BR-DELETE-03 | **Không thể xoá Course Category đã được gán với khoá học.** |

### Rule Claude trích thêm (chưa có mã trong UG)

| ID | Rule | Nguồn |
|---|---|---|
| KB-COURSE-01 | Xoá Section sẽ **xoá toàn bộ nội dung bên trong** Section đó. | Tạo hoạt động học, mục II |
| KB-COURSE-02 | Danh sách Foundation Course khi tạo Normal Course **chỉ hiện khoá cùng Category**. | Tạo khoá học, mục IV |
| KB-COURSE-03 | Đổi thứ tự được Section và Test; đổi thứ tự Activity **chỉ trong cùng một Section**; Learning Outcome không đổi thứ tự. | Tạo hoạt động học, mục II |
| KB-COURSE-04 | Copy Section sẽ copy **toàn bộ nội dung bên trong, gồm cả Section Test**. | Tạo hoạt động học, mục II |
| KB-COURSE-05 | Thứ tự Document trong Tab là thứ tự hiển thị nội dung cho học viên. | Tạo hoạt động học, mục II |

---

## 6. Course Category

| Thuộc tính | Giá trị |
|---|---|
| Module chính | Course Category |
| Module liên quan | Course, Certificate |
| Ràng buộc xoá | Không xoá được Category đã gán khoá học (BR-DELETE-03) |
| Vai trò ẩn | **Category là khoá liên kết 3 chiều**: lọc Foundation Course, lọc Certificate Template, và phân nhóm Comment Replier |

> ⚠️ Category trông như một bảng danh mục đơn giản nhưng thực chất chi phối 3 luồng khác. Mọi thay đổi ở Category phải xét cả 3.

---

## 7. Phụ thuộc

| Module liên quan | Quan hệ | Chiều |
|---|---|---|
| **Class** | Lớp phải gắn Course đã Publish | Course → Class |
| **Question Bank** | Câu hỏi trong Test/Quiz lấy từ Question Bank | QB → Course |
| **Case Study** | Thêm vào Section | Case Study → Course |
| **Storyline** (ẩn) | Thêm vào Section | Storyline → Course |
| **Certificate** | Bắt buộc gán trước khi Publish | Certificate → Course |
| **Course Category** | Bắt buộc; chi phối lọc Foundation + Certificate | Category → Course |
| **Resource** | Tài liệu khoá, dùng chung kho hệ thống | hai chiều |
| **UpLMS (học viên)** | Nội dung hiển thị phía học viên | Course → UpLMS |

---

## 8. Điểm cần BA xác nhận

| # | Câu hỏi |
|---|---|
| Q1 | BR-COURSE-02 nói cấu trúc 2 cấp (Section → Activity), nhưng hướng dẫn mô tả Tab và Document bên trong Activity. Cấu trúc chính thức mấy tầng? |
| Q2 | Activity Name và Type of Activity có bắt buộc không? UG không đánh dấu (*). |
| Q3 | "Rule của khoá học" khi tự sinh Section Code / Activity Code là rule gì? |
| Q4 | Trạng thái **Lock** chuyển sang **Block** được không, và ngược lại? UG không mô tả chuyển đổi trạng thái. |
| Q5 | Điểm thành phần có 4 loại cố định hay cấu hình được? |
| Q6 | Khi Block Normal Course, khoá bị remove khỏi "lớp chưa bắt đầu" — lớp đã bắt đầu thì xử lý ra sao? |
