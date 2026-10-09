# 07 — Learning Experience (Trải nghiệm học viên)

| | |
|---|---|
| Hệ | UpLMS (https://uplms.upbase.asia) |
| Trạng thái | Active |
| Vai trò | Học viên |
| Nguồn UG | `uplms/khoa-hoc/`, `uplms/thong-bao.md` (13 page) |

---

## 1. My Learning — danh sách khoá học

Chỉ hiển thị khoá học viên **đã được thêm vào**. Thông tin mỗi khoá: tên · giới thiệu · **tiến độ học** · **thời hạn còn lại** · **trạng thái (đã Activate hay chưa)**.

Tìm kiếm theo tên (đợi 3–5 giây hoặc Enter) · Lọc theo **Danh mục** và **Trạng thái**, **kết hợp được nhiều điều kiện** cùng lúc và kết hợp với tìm kiếm.

### Thời hạn còn lại — hiển thị khác nhau theo loại khoá

| Loại | Cách tính |
|---|---|
| Thời hạn **cố định** (Fixed) | Theo lịch trình chung của lớp. VD: lớp 1/1–31/12/2026, hôm nay 1/12 → còn 30 ngày |
| Thời hạn **linh động** (Flexible) | Đếm ngược từ N ngày kể từ lúc học viên bấm **Activate** |

### Tiến độ học

> **Công thức:** `Tiến độ = Số Activity đã hoàn thành / Tổng số Activity của khoá học`

---

## 2. Vào học — Begin vs Activate

| Loại khoá | Nút | Hành vi |
|---|---|---|
| Thời hạn cố định | **Begin** | Vào thẳng Course Detail |
| Thời hạn linh động | **Activate** | Hộp thoại xác nhận → **bắt đầu đếm ngược N ngày** |

> Không thấy nút Begin mà chỉ thấy Activate = khoá linh động chưa kích hoạt.

### Màn Course Detail

| Vùng | Nội dung |
|---|---|
| Trái | Tất cả chương (Section) theo thứ tự thiết kế, kèm tiến độ và thời gian học dự kiến |
| Phải | Mô tả chương, Learning Outcome, danh sách hoạt động: Learning Activity / Test Activity / Case Study Activity |

---

## 3. Logic tính hoàn thành Activity — rule quan trọng

Hoạt động học được tính **Hoàn thành** khi icon Check chuyển **xanh**.

| Nội dung trong Activity | Điều kiện hoàn thành |
|---|---|
| Chứa **Quiz** | Phải **hoàn thành Quiz** |
| Chứa **Video** | Phải **xem tối thiểu 80% thời lượng video** |
| Chứa **Text / Ảnh** | Chỉ cần **mở hiển thị** |

> ✅ **Đã đính chính (23/09/2026) — PO xác nhận.** User Guide ghi điều kiện với Video là *"phải play video"*. Hệ thống **đã cập nhật thành xem tối thiểu 80% thời lượng**. UG chưa được cập nhật theo.
>
> ⚠️ **Text / Ảnh vẫn tính hoàn thành ngay khi mở hiển thị** — PO xác nhận giữ nguyên, không sửa. Đây là ràng buộc phải tính đến khi thiết kế bất kỳ cơ chế nào cộng thưởng theo số Activity hoàn thành.

> **Mức độ ưu tiên: Quiz → Video → Text/Ảnh.**
> Activity có **nhiều Tab** → phải học hết tất cả các Tab mới tính Hoàn thành.

> ❌ **Đã bỏ (PO xác nhận 23/09/2026):** ~~Hoạt động đánh dấu `Graded Activity` là hoạt động bắt buộc hoàn thành để tính điểm hoàn thành khoá học.~~
>
> **Hệ thống không còn khái niệm `Graded Activity`.** User Guide còn mô tả — đã lạc hậu. Mọi hoạt động học nay đồng hạng về mặt tính hoàn thành khoá.

---

## 4. Video bài giảng

| Tính năng | Ghi chú |
|---|---|
| Play/Pause | Click nút hoặc click thẳng vào video |
| Âm lượng, phóng to/thu nhỏ | — |
| **Picture in Picture** | Thu nhỏ video, **vẫn chạy khi chuyển sang tab trình duyệt khác**, kéo thả vị trí được |
| **Timeline** | Danh sách mốc thời gian; click → video nhảy tới mốc đó. **Chỉ hiện với video đã được cấu hình timeline** |
| **Câu hỏi trong video** | Marker trên thanh tiến độ cho biết số câu và mốc thời gian. Trả lời → Submit → xem đáp án + giải thích. Có thể **Finish** hoặc **Skip** |

> ⚠️ **Câu hỏi trong Video KHÔNG dùng để tính điểm khoá học** — và học viên **Skip được**.

---

## 5. Dashboard khoá học

**Điều kiện hiển thị:** khoá có Status = `Resume` hoặc `Review`. Khoá `Ready to learn` **chưa có Dashboard** (click vào sẽ vào thẳng Course Content).

> ⚠️ Xuất hiện thêm bộ trạng thái khoá học phía học viên: `Ready to learn` / `Resume` / `Review` — **khác** với bộ trạng thái phía Ops (`Draft`/`Publish`/`Lock`/`Block`). `❓BA` — hai bộ này ánh xạ với nhau ra sao?

| Biểu đồ | Công thức / Logic |
|---|---|
| **Overall Progress** | `Số Activity đã hoàn thành / Tổng số Activity của khoá` — không phân biệt loại Activity |
| **This Week** | So sánh số Activity hoàn thành & thời gian học **tuần này vs tuần liền trước** (chỉ tuần liền trước) |
| **Section Progress** | `Số Activity hoàn thành trong Section / Tổng Activity của Section` |
| **Your Learning Results** | Kết quả theo Section, tính từ các bài Test đã làm |
| **Overall average score** | Trung bình các Section **đã ghi nhận điểm**; Section chưa có điểm **không tham gia tính** |

Thông điệp This Week: `>` tuần trước → *"You've outperformed last week! Aim higher!"* · `=` → *"You've matched last week's progress. Go further!"* · `<` → *"More activities/minutes to outperform last week"*

---

## 6. Ghi chú (Notes)

| Đặc tính | Giá trị |
|---|---|
| Phạm vi hiển thị | Mở ở **Course Detail** → toàn bộ ghi chú của khoá. Mở ở **Activity** → chỉ ghi chú của activity đó |
| Tìm kiếm | Theo Section → Activity (chọn Section trước) |
| **Chỉnh sửa** | ⚠️ **Chỉ sửa được tại chính hoạt động chứa ghi chú đó** |
| Xoá | Từ danh sách ghi chú |

---

## 7. Thảo luận (Discussion)

Bình luận bằng **chữ hoặc ảnh** (chọn nhiều ảnh cùng lúc). Gửi bằng Enter hoặc nút Submit. Có Reply, Edit, Delete (Delete cần xác nhận, **không hoàn tác được**).

| Rule |
|---|
| Chỉ chỉnh sửa và xoá **bình luận của chính mình** |
| ⚠️ **Bình luận gắn theo KHOÁ HỌC** — mọi bình luận thuộc khoá sẽ hiển thị ở **tất cả các lớp** có gán khoá đó |

> Rule cuối cùng là điểm dễ gây bất ngờ: học viên lớp A thấy bình luận của học viên lớp B nếu hai lớp dùng chung khoá.

---

## 8. Tài liệu — phân biệt hai loại

| | **Course Resource** | **Class Resource** |
|---|---|---|
| Gắn với | **Khoá học** | **Lớp học cố định** |
| Phạm vi | Tồn tại ở **tất cả lớp** có gắn khoá đó | Chỉ lớp đó |
| Ví dụ | Tài liệu chung của khoá | Video record bài giảng, tài liệu của giảng viên lớp |
| Hiển thị | Theo Section/Activity | Theo **cấu trúc thư mục** thiết lập ở Ops |
| Layout | Danh sách | **List** hoặc **Grid** |
| Quyền | Xem + tải | Theo phân quyền Ops (`View` / `Download`) |

Cả hai đều lọc được theo Section → Activity, mặc định sắp xếp **thời gian tạo giảm dần**.

---

## 9. Thông báo

> ⚠️ **Chỉ truy cập được thông báo TRƯỚC khi vào chi tiết một khoá học** — thiết kế có chủ đích để tránh học viên mất tập trung khi đang học.

| Chức năng | Ghi chú |
|---|---|
| Tab `All` / `Unread` | Lọc thông báo |
| `Mark as all read` | Đánh dấu đã đọc toàn bộ |
| Thông báo có điều hướng | Kết quả bài kiểm tra → màn kết quả · Có người trả lời bình luận → hoạt động học chứa bình luận đó |

---

## 10. Business Rule

| ID | Rule | Nguồn |
|---|---|---|
| KB-LX-01 | Tiến độ học = số Activity hoàn thành / tổng Activity của khoá. | danh-sach-khoa-hoc mục III |
| KB-LX-02 | Khoá Flexible hết hạn sau N ngày **kể từ khi học viên bấm Activate**. | hoat-dong-hoc mục III |
| KB-LX-03 | Logic hoàn thành Activity theo ưu tiên **Quiz → Video → Text/Ảnh**; nhiều Tab thì phải học hết mọi Tab. | hoat-dong-hoc mục II |
| **KB-LX-03a** | Activity chứa **Video** hoàn thành khi **xem tối thiểu 80% thời lượng**. ✅ PO xác nhận 23/09/2026 — UG còn ghi *"phải play video"*, đã lạc hậu. | PO xác nhận |
| **KB-LX-03b** | Activity chứa **Text / Ảnh** hoàn thành khi **mở hiển thị**, không có điều kiện thời gian. ✅ PO xác nhận 23/09/2026 — giữ nguyên, không sửa. | PO xác nhận |
| ~~KB-LX-04~~ | ~~`Graded Activity` là hoạt động **bắt buộc** hoàn thành để tính điểm khoá học.~~ ❌ **Đã bỏ — hệ thống không còn khái niệm này.** PO xác nhận 23/09/2026 | ~~hoat-dong-hoc mục III~~ |
| **KB-LX-08** | **Học viên đã học ít nhất 1 hoạt động trong khoá → KHÔNG huỷ ghi danh (`un-enroll`) được nữa.** ✅ PO xác nhận 23/09/2026 | PO xác nhận |
| KB-LX-05 | **Câu hỏi trong Video không tính điểm** khoá học và **Skip được**. | thao-tac-voi-video mục III |
| KB-LX-06 | Timeline video **chỉ hiện với video đã cấu hình mốc thời gian**. | thao-tac-voi-video mục III |
| KB-LX-07 | Dashboard khoá **chỉ hiện khi Status = Resume hoặc Review**; `Ready to learn` chưa có Dashboard. | dashboard-khoa-hoc mục I |
| KB-LX-08 | `Overall average score` chỉ tính Section **đã ghi nhận điểm**. | dashboard-khoa-hoc mục III |
| KB-LX-09 | `This Week` **chỉ so với tuần liền trước**, không so với tuần khác. | dashboard-khoa-hoc mục III |
| KB-LX-10 | **Chỉ chỉnh sửa ghi chú tại hoạt động học chứa ghi chú đó.** | tinh-nang-ghi-chu mục III |
| KB-LX-11 | Chỉ sửa/xoá được **bình luận của chính mình**. | thao-luan mục III |
| KB-LX-12 | ⚠️ **Bình luận gắn theo khoá học → hiển thị ở tất cả lớp có gán khoá đó.** | thao-luan mục III |
| KB-LX-13 | Thông báo **chỉ truy cập được trước khi vào chi tiết khoá học**. | thong-bao mục I |
| KB-LX-14 | Học viên chỉ xem/tải được tài liệu lớp mà mình **có quyền** theo phân quyền Ops. | tai-lieu-lop-hoc mục III |
| KB-LX-15 | Course Resource tồn tại ở **tất cả lớp** gắn khoá đó; Class Resource chỉ thuộc một lớp. | tai-lieu-khoa-hoc + tai-lieu-lop-hoc |

---

## 11. Phụ thuộc

| Module | Quan hệ |
|---|---|
| **Course** | Nguồn toàn bộ nội dung học |
| **Class** | Quyết định học viên thấy khoá nào, thời hạn bao lâu, cấu phần nào |
| **Test/Quiz/Case Study** | Hoạt động kiểm tra |
| **Grading** | Kết quả bài tự luận trả về học viên; Request Regrading |
| **Certificate** | Nhận chứng chỉ khi hoàn thành |
| **Notification** | Thông báo kết quả, trả lời bình luận |
| **Comment Replier** | Nhóm nhân sự trả lời bình luận với Display Name/Avatar chung |

---

## 12. Điểm cần BA xác nhận

| # | Câu hỏi |
|---|---|
| Q1 | **Bộ trạng thái khoá phía học viên (`Ready to learn`/`Resume`/`Review`) ánh xạ thế nào với trạng thái phía Ops (`Draft`/`Publish`/`Lock`/`Block`)?** |
| Q2 | KB-LX-12: bình luận hiển thị chéo giữa các lớp cùng khoá — đúng là chủ đích thiết kế chứ không phải lỗi? |
| Q3 | "Thời gian học" trong This Week được đo bằng gì (time on page? thời lượng video đã xem?) |
| Q4 | Activity chứa cả Quiz và Video thì áp rule nào — chỉ Quiz (ưu tiên cao nhất) hay cả hai? |
| Q5 | `Review` status nghĩa là gì — đã hoàn thành khoá? |
| Q6 | Khoá hết hạn thì học viên còn xem lại được nội dung/chứng chỉ không? |
