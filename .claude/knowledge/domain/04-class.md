# 04 — Class (Lớp học)

| | |
|---|---|
| Hệ | UpLMS Ops |
| Đường dẫn | Academic Management → Class → Class List |
| Trạng thái | Active |
| Nguồn UG | `uplms-ops/class-management/` (6 page) |

---

## 1. Vị trí trong hệ thống

> *"Nếu Academic Management là nơi xây dựng nội dung cần dạy, thì Class Management là nơi quyết định ai học, học nội dung nào và trong thời gian nào."*

**Lớp không tự chứa nội dung.** Mỗi lớp gắn với một Course đã Publish. Thuộc về lớp là: danh sách học viên, trợ giảng, tài liệu riêng của lớp, thời hạn truy cập, kết quả bài kiểm tra.

Vòng đời: **Tạo lớp → Thêm học viên & trợ giảng → Vận hành (tài liệu, điều chỉnh thời hạn/cấu phần, chấm bài)**

---

## 2. Loại lớp — cơ chế Foundation tự sinh

| Type | Ai tạo |
|---|---|
| **Lesson** | Người dùng tạo thủ công |
| **Foundation** | **Hệ thống tự tạo** khi Course Normal gắn với lớp Lesson có cấu hình Foundation Course |

### Đồng bộ một chiều — rule dễ sót nhất của module này

```
Lớp Lesson  ──(thêm/xoá học viên, trợ giảng)──►  Lớp Foundation   ✅ đồng bộ
Lớp Lesson  ◄──(thêm/xoá học viên, trợ giảng)──  Lớp Foundation   ❌ KHÔNG đồng bộ
```

> ⚠️ Thao tác tại Foundation **không tác động ngược** lên Lesson. Mọi thay đổi chạm tới học viên/mentor trong lớp phải xét chiều này.

---

## 3. Duration — hai cách tính thời hạn

| Duration | Cách tính |
|---|---|
| **Fixed** | Lớp diễn ra trong khoảng Start Date – End Date đã đặt |
| **Flexible** | Lớp diễn ra trong **N ngày, tính từ ngày học viên bấm Activate** khoá học |

Thời hạn mặc định của lớp **Foundation là 60 ngày** (BR-STATUS-01).

Thời hạn riêng của từng học viên **có thể dài hoặc ngắn hơn** thời hạn mặc định của lớp.

> Với `Duration = Flexible`, **nếu học viên chưa Activate thì không cập nhật được thời hạn riêng** cho học viên đó.

---

## 4. Field — Create Class

| Field | Bắt buộc | Kiểu | Mặc định | Ghi chú |
|---|---|---|---|---|
| Name | **Có** | Text | — | |
| Code | Không | Text | — | `❓BA` có unique không? |
| Construction Mode | **Có** | Enum | `Online` | Hình thức lớp |
| Type | **Có** | Enum | `Lesson` | **Chỉ tạo được Lesson** |
| Số học viên tối đa | `❓BA` | Number | — | |
| Duration | `❓BA` | Enum | — | `Fixed` \| `Flexible` |
| Course | — | Chọn | — | Add Course → **chỉ hiện Normal Course** (BR-TYPE-001) |

### Import lớp hàng loạt

| Ràng buộc | Giá trị |
|---|---|
| Định dạng | `.csv` hoặc `.xlsx` |
| Số file / lần | **1** |
| Xử lý lỗi | Bản ghi hợp lệ → tạo thành công; bản ghi lỗi → không tạo, ghi vào log |
| Xem lỗi | **View Log** — trường lỗi bôi đỏ, lý do ở cột `Errors` |

---

## 5. Trạng thái lớp & quy tắc chỉnh sửa

Trạng thái xuất hiện trong UG: `DRAFT`, `PUBLIC`, `ENDED` (theo filter của SIS Dashboard). Lớp **Ended không chỉnh sửa được**.

### Lớp Foundation

| Tình trạng | Được sửa |
|---|---|
| Đã có học viên học | **Chỉ** Name, Code, Số học viên tối đa |
| Chưa có học viên học | Tất cả, **trừ** Type và Course |

### Lớp Lesson

| Tình trạng | Được sửa |
|---|---|
| Chưa có học viên học | Tất cả |
| Đã có học viên nhưng lớp chưa bắt đầu / học viên chưa học | Không sửa: Status, Construction Mode, Type, Course |
| Đã có học viên đang học hoặc lớp đã bắt đầu | Không sửa: Status, Construction Mode, Type, Course |

> Hai dòng cuối của bảng Lesson có ràng buộc **giống hệt nhau**. `❓BA` — có phải thiếu một mức ràng buộc chặt hơn cho trường hợp lớp đã bắt đầu không?

---

## 6. Học viên trong lớp

### Điều chỉnh cấu phần học theo từng học viên

`Class Detail → Student → Action → Edit Course Content`

| Thao tác | Quy tắc |
|---|---|
| Chọn/Bỏ chọn **All** | Tất cả checkbox cấu phần được tick/bỏ tick |
| Chọn **Section** | Tất cả Activity, Test, Quiz thuộc Section được chọn |
| Chọn **Activity** | Section chứa Activity đó được chọn (chọn ngược lên) |
| **Bỏ chọn** cấu phần | Cấu phần không xuất hiện trong chương trình học của học viên |
| Xoá cấu phần **đã học** | **Không được phép** |
| Xoá cấu phần **chưa học** | Được phép |

Điều chỉnh này **chỉ áp dụng cho học viên được chọn**, không ảnh hưởng toàn lớp.

### Allow Pass Foundation

`Lớp Lesson có gắn Foundation → Student → Action → Allow Pass Foundation`

Sau khi áp dụng, học viên **không bắt buộc hoàn thành khoá Foundation** và học thẳng khoá chính.

---

## 7. Trợ giảng (Mentor)

| Thuộc tính | Giá trị |
|---|---|
| Nguồn danh sách | **Staff List** trên hệ thống |
| Main Responsible | Trợ giảng chịu trách nhiệm chính về chấm điểm; **người review cuối cùng** trước khi gửi kết quả cho học viên |

---

## 8. Tài liệu lớp học (Class Resource)

### Cột hiển thị

`File name` · `Size` · `Date` · `Owner` (người upload) · `Location` (mặc định Root) · `Access` (Student / Teacher)

### Giới hạn upload — khác Course Resource

| Loại | Dung lượng tối đa | Số lượng / lần |
|---|---|---|
| **Media** (video, audio) | **20GB** | **1** |
| Tài liệu khác | **500MB** | **10** |

### Quyền chia sẻ

| Trường | Giá trị |
|---|---|
| Student | Mặc định `Apply to All`; chọn `Custom` để giới hạn học viên cụ thể |
| Permission | `View` (chỉ xem trên UpLMS) \| `Download` (xem + tải) |

> **Media chỉ có quyền `View`, không chuyển sang `Download` được.** Tài liệu không phải Media mặc định `Download`.

Danh sách mặc định sắp xếp theo **thời gian tạo giảm dần**. Move to Folder chỉ chọn được **một** thư mục đích.

---

## 9. Business Rule

### Nguyên văn từ UG

| ID | Rule |
|---|---|
| BR-TYPE-001 | Khi chọn Course cho lớp **Lesson**, hệ thống chỉ hiển thị **Normal Course**. |
| BR-MENTOR-01 | **Main Responsible** là trợ giảng chịu trách nhiệm chính về chấm điểm, người review cuối trước khi gửi kết quả cho học viên. |
| BR-MENTOR-02 | Lớp Lesson có gắn Foundation → thêm trợ giảng vào Lesson thì **cũng thêm vào Foundation**. |
| BR-MENTOR-03 | Lớp Lesson có gắn Foundation → xoá trợ giảng khỏi Lesson thì **cũng xoá khỏi Foundation**. |
| BR-STATUS-01 | Thời hạn mặc định của lớp **Foundation là 60 ngày**. |

### Rule Claude trích thêm

| ID | Rule | Nguồn |
|---|---|---|
| KB-CLASS-01 | Thêm/xoá **học viên** ở lớp Lesson cũng áp dụng cho lớp Foundation gắn kèm. | quan-ly-hoc-vien-trong-lop mục III |
| KB-CLASS-02 | Thao tác tại lớp Foundation **không tác động ngược** lên lớp Lesson. | tong-quan-lop-hoc + quan-ly-tro-giang |
| KB-CLASS-03 | `Duration = Flexible` + học viên chưa Activate → **không cập nhật được thời hạn** của học viên đó. | quan-ly-hoc-vien-trong-lop mục III |
| KB-CLASS-04 | **Không xoá được cấu phần học viên đã học** khỏi chương trình của họ. | quan-ly-hoc-vien-trong-lop mục III |
| KB-CLASS-05 | Lớp trạng thái **Ended không được chỉnh sửa**. | tao-lop-hoc mục II |
| KB-CLASS-06 | Media trong Class Resource **chỉ có quyền View**, không chuyển sang Download. | quan-ly-tai-lieu-lop-hoc mục II |
| KB-CLASS-07 | Import lớp: mỗi lần **1 file**, `.csv`/`.xlsx`; bản ghi lỗi không tạo lớp và được ghi log. | tao-lop-hoc mục III |

---

## 10. Phụ thuộc

| Module | Quan hệ | Chiều |
|---|---|---|
| **Course** | Lớp gắn Course đã Publish; lớp Lesson chỉ nhận Normal Course | Course → Class |
| **Student** | Danh sách học viên trong lớp | Student → Class |
| **Staff** | Nguồn danh sách Mentor | Staff → Class |
| **Grading** | Tab Grading trong Class Detail; Main Responsible quyết định luồng duyệt | hai chiều |
| **Test/Quiz** | Tab Test/Quiz (**đang ẩn**); kết quả học viên | hai chiều |
| **Resources** | Class Resource dùng chung kho tài nguyên hệ thống | hai chiều |
| **Foundation Class** | Lớp tự sinh, đồng bộ một chiều | Lesson → Foundation |
| **SIS Dashboard** | Dữ liệu chuyên cần, đầu vào, tiến độ theo lớp | Class → Dashboard |

---

## 11. Điểm cần BA xác nhận

| # | Câu hỏi |
|---|---|
| Q1 | Danh sách trạng thái lớp chính thức? UG rải rác `DRAFT`/`PUBLIC`/`ENDED` (từ filter Dashboard) và "lớp đã bắt đầu / chưa bắt đầu" — hai hệ khái niệm khác nhau. |
| Q2 | Bảng quy tắc sửa lớp Lesson có 2 dòng ràng buộc giống hệt nhau — đúng hay thiếu? |
| Q3 | Class Code có bắt buộc unique không? |
| Q4 | Khi xoá học viên khỏi lớp, dữ liệu học tập (tiến độ, bài đã làm, điểm) xử lý ra sao? |
| Q5 | Một lớp gắn được nhiều Course hay chỉ một? UG nói "mỗi lớp gắn với một khoá học" nhưng thao tác là "Add Course". |
| Q6 | Lớp Foundation bị xoá khi nào — khi gỡ Foundation Course khỏi Normal Course? |
| Q7 | "Construction Mode" có giá trị nào ngoài Online? |
