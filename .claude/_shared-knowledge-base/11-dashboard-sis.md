# 11 — SIS Operational Dashboard

| | |
|---|---|
| Hệ | **UpLMS Ops** — SIS là *nhóm dashboard bên trong Ops*, không phải hệ thống riêng |
| Đường dẫn | Dashboard → SIS Operational Dashboard |
| Trạng thái | Active |
| Vai trò | Admin / UpLMS Operator, Giảng viên (Teacher), Quản lý chương trình |
| Nguồn | UG `dashboard/sis-operational-dashboard.md` · BA xác nhận 23/09/2026 · API tag `Sis Dashboard` (12 endpoint, Ops) |

> ✅ **Đã đính chính (23/09/2026).** Bản KB đầu tiên suy đoán SIS là hệ thống thứ ba tách rời — **sai**. BA xác nhận SIS là nhóm dashboard trong Ops. API Ops có tag `Sis Dashboard` với 12 endpoint, xác nhận lại điều này.

---

## 1. Dashboard hiện có — 3 loại

BA xác nhận **hiện tại chỉ có 3 dashboard đang dùng**:

| # | Dashboard | Trạng thái |
|---|---|---|
| 1 | **Tiến độ học trên UpLMS** | 🟢 Đang dùng |
| 2 | **Phân phối điểm các bài kiểm tra** | 🟢 Đang dùng |
| 3 | **Tỷ lệ ghi điểm trên từng câu hỏi / chủ đề kiến thức** | 🟢 Đang dùng |
| — | Tỉ lệ chuyên cần | ⚪ UG có mô tả, **BA không liệt kê trong 3 loại hiện tại** |
| — | Tỉ lệ đầu vào | ⚪ UG có mô tả, **BA không liệt kê trong 3 loại hiện tại** |

> `❓BA` — Hai dashboard *Tỉ lệ chuyên cần* và *Tỉ lệ đầu vào* được mô tả rất chi tiết trong UG (có filter, tooltip, popup danh sách học viên) nhưng không nằm trong 3 loại BA nêu. Chúng đã gỡ, đang ẩn, hay chỉ là UG viết trước? Nội dung của chúng vẫn giữ ở §4 để không mất thông tin.

---

## 2. Bộ filter chuẩn

| Filter | Bắt buộc | Chọn nhiều | Phụ thuộc | Ghi chú |
|---|---|---|---|---|
| Facility | Không | Có | — | Danh sách cơ sở — API có `Class Facility Management`, `Staff Facility Management` |
| Program | Không | Không | — | `ACCA`, `CFA`, `CMA` |
| **Course** | **Có** | Không | Program | **Chỉ lấy course 4 level** — API có `Course Level Management` |
| From – To | Không | — | — | Chỉ lấy lớp có **Start date** trong khoảng lọc |
| Status | Không | Có | — | `DRAFT`, `PUBLIC`, `ENDED` |
| **Class code** | **Có** | Có | Course + From-To + Status | **Tối đa 4 lớp**, mỗi lớp 1 biểu đồ |
| Section | Không | Không | Course + Class | Chỉ dashboard Chuyên cần |

> Hai khái niệm trước đây không giải thích được, nay đã có nguồn: **Facility** ứng với API `Class Facility Management` / `Staff Facility Management`; **"course 4 level"** ứng với API `Course Level Management`. Cả hai đều là module có thật trong Ops, chỉ là UG chưa viết.

---

## 3. Business Rule

| ID | Rule | Nguồn |
|---|---|---|
| KB-SIS-01 | Filter **Course** và **Class code** bắt buộc ở mọi dashboard. | UG mục III |
| KB-SIS-02 | **Chọn tối đa 4 lớp**, mỗi lớp render 1 biểu đồ riêng. | UG mục III |
| KB-SIS-03 | Filter Course **chỉ lấy course 4 level**. | UG mục III |
| KB-SIS-04 | Lọc theo thời gian → **chỉ lấy lớp có Start date trong khoảng lọc**. | UG mục III |
| KB-SIS-05 | Ngưỡng mục tiêu chuyên cần **70%** *(thuộc dashboard chưa rõ còn dùng)*. | UG mục III |
| KB-SIS-06 | Class code phụ thuộc Course + From-To + Status; Section phụ thuộc Course + Class. | UG mục III |
| KB-SIS-07 | Dashboard yêu cầu dữ liệu lớp / bài kiểm tra / tiến độ **đã được khởi tạo hoặc đồng bộ**. | UG mục I |

---

## 4. Hai dashboard trong UG nhưng không nằm trong 3 loại hiện tại

*Giữ lại để tra cứu — cần BA xác nhận trạng thái.*

### 4.1 Tỉ lệ chuyên cần

Biểu đồ cột *Attendance rate by sessions*, mỗi cột = 1 buổi học, **ngưỡng mục tiêu 70%** (đường xanh lá).
Hover → tên buổi (VD *Buổi 1 - Offline - 22/08/2025*), tỷ lệ %, sĩ số.
Click cột → popup: `ID`, `Student Name`, `Email/Phone`, `Checkin`, `Status` (**PRESENT** / **ABSENT**).

> Dữ liệu buổi học và điểm danh đến từ nhóm API **`Schedules` (21) / `Class Schedule` (9) / `Room Schedule Management` (9)** — mảng chức năng UG chưa viết, xem [14-api-surface.md](14-api-surface.md).

### 4.2 Tỉ lệ đầu vào

Biểu đồ tròn *Student background distribution*, level `IA` / `IIA` / `IB` / `IIB` / `Other`.
Click → popup: `ID`, `Student Name`, `Email/Phone`, `Duration`, `Progress` (%).

> "Level đầu vào" nhiều khả năng ứng với cột **`users.english_level_id`** trong DB — xem [12-data-model.md](12-data-model.md). `❓BA`

---

## 5. Phụ thuộc

| Module | Quan hệ |
|---|---|
| **Class Management** | Dữ liệu lớp (code, status, start date) |
| **Quiz / Quiz Attempt** | Dữ liệu bài kiểm tra và điểm |
| **UpLMS** | Dữ liệu tiến độ học tập |
| **Schedules / Class Schedule** | Buổi học, điểm danh *(nhóm API chưa có trong UG)* |
| **Course Level / Facility** | Filter *(nhóm API chưa có trong UG)* |

---

## 6. Điểm cần BA xác nhận

| # | Câu hỏi |
|---|---|
| Q1 | Hai dashboard *Tỉ lệ chuyên cần* và *Tỉ lệ đầu vào* — đã gỡ, đang ẩn, hay UG viết trước khi làm? |
| Q2 | **Level đầu vào** (IA/IIA/IB/IIB/Other) có phải là `users.english_level_id` không? Gán ở đâu? |
| Q3 | **Program** (ACCA/CFA/CMA) khác gì **Course Category**? DB chỉ có `course_categories`, không có bảng program riêng. |
| Q4 | **"Course 4 level"** — `Course Level Management` trong API quản lý cái này? 4 level là gì? |
| Q5 | Dữ liệu điểm danh nhập ở đâu — qua nhóm API `Schedules` hay nhập tay? |
| Q6 | Vai trò **Teacher** khác **Mentor** thế nào? |
| Q7 | Ba dashboard đang dùng chưa được trích chi tiết (UG mô tả kỹ 2 cái không dùng, 3 cái đang dùng thì chưa). Cần bổ sung. |
