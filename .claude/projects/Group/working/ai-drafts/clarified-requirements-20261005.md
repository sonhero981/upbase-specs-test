# Làm rõ yêu cầu — Group

**Ngày:** 05/10/2026 · **Phiên bản:** v0.1
**Input:** `working/raw-inputs/yeu-cau-goc-20261005.md` — 19 hạng mục, hai nhóm `Group` và `User Group Relationship`
**Mục đích PO nêu:** tổ chức các nhóm học tập, để gán, theo dõi và đánh giá theo từng nhóm

---

## 1. Phát hiện lớn nhất — hệ thống đã có hai thứ tên gần giống

Tra `14-api-surface.md` mục 2.3 *Tổ chức và phân quyền*:

| Nhóm API | Số operation | Nội dung KB ghi |
|---|---|---|
| **`Group Management`** | 9 | CRUD group, gán user |
| **`Department Management`** | 9 | `list-unit`, `parent-list` → **cây phòng ban** |

Và trong data model, bảng **`departments`** có cột `unit` và `tree_id`, KB ghi thẳng là *"cây phòng ban"*. Nó gắn với `staffs`, không gắn với `users`.

Hai nhóm API này cộng lại bao gần hết phần khung của yêu cầu: cây nhiều cấp, CRUD nhóm, gán người vào nhóm.

**Nhưng không được kết luận là đã có tính năng.** KB `14` ghi ngay phía trên bảng đó:

> *"Ba lần trong một buổi phân tích. Tỷ lệ endpoint 'chết' trong hệ này đủ cao để không bao giờ suy ra tính năng từ sự tồn tại của endpoint."*

Ba trường hợp đã xác nhận chết: `Examination` (8 op), `Entrance Test` (3 op), `trial/upgrade-now`.

Thêm một dữ kiện ngược chiều: ở dự án Gamification, PO đã chốt **xếp hạng theo phòng ban không làm được vì "`departments` chỉ gắn `staffs`, học viên không có phòng ban"**. Tức là dù cây phòng ban có tồn tại, nó **không phủ học viên**.

→ Câu trả lời cho `OQ-01` quyết định toàn bộ phạm vi dự án này. Xem mục 5.

---

## 2. Chuẩn hoá input

| Nhóm | Nội dung |
|---|---|
| **Stakeholder request** | PO yêu cầu dựng chức năng nhóm với 19 hạng mục |
| **Problem** | *(chưa nêu rõ)* Hiện không gom được học viên thành nhóm để gán nội dung và theo dõi. `US16` của Gamification phải hoãn vì thiếu cái này, và quản lý trực tiếp không có công cụ xem người mình phụ trách |
| **Expected outcome** | Gán nội dung theo nhóm · theo dõi tiến độ theo nhóm · đánh giá theo nhóm · quản lý xem được người thuộc nhánh mình |
| **Users / roles** | Nhân sự vận hành (dựng cây, quản thành viên) · **người quản lý** (vai trò mới, là người dùng chứ không phải role) · học viên (xem quản lý của mình) |
| **Systems / modules** | UpLMS Ops: quản lý nhóm, gán nội dung, phân quyền · UpLMS: trang người học · tích hợp HRM |
| **Constraints** | Đồng bộ từ HRM quyết định ai sửa được gì · phạm vi dữ liệu gắn với `ORG.ROL.04` · phạm vi nhóm cha bao trùm nhánh con là quy tắc nền của mọi báo cáo |
| **Proposed solution** | Toàn bộ 19 hạng mục là mô tả giải pháp, không phải mô tả vấn đề. Chúng là `Recommendation`, chưa phải yêu cầu đã chốt |

> ⚠️ Input mô tả **giải pháp đã nghĩ sẵn** khá chi tiết, nhưng không nêu vấn đề gốc. Ví dụ hạng mục 15 *"Chỉ định quản lý trực tiếp trên hồ sơ, dùng cho báo cáo chéo nhánh và giai đoạn bàn giao"* là một giải pháp cho tình huống nào đó chưa được mô tả. Biết tình huống thật có thể dẫn tới cách làm khác đơn giản hơn.

---

## 3. Requirement candidates

| ID | Requirement | Type | Source | Confidence | Ghi chú |
|---|---|---|---|---|---|
| `RC-01` | Cây nhóm nhiều cấp, số cấp tối đa cấu hình được. Mỗi nhóm có mã, tên, mô tả, nhóm cha | Data · Functional | Mục 1 | High | Trùng khung với `Department Management` nếu nhóm đó còn sống |
| `RC-02` | Quan hệ người và nhóm là nhiều-nhiều. Nhiều cây gốc song song để thể hiện cơ cấu ma trận | Data | Mục 2 | High | **Đây là chỗ khác `departments` rõ nhất** — `staffs.department_id` là một-nhiều |
| `RC-03` | Phân loại nhóm theo nguồn: đồng bộ HRM và tự tạo. Nguồn quyết định quyền sửa | Business Rule | Mục 3 | Medium | Cơ chế đồng bộ HRM chưa có mô tả nào |
| `RC-04` | Tạo, sửa, di chuyển nhóm. Di chuyển nhánh thì nhánh con đi theo và quan hệ quản lý tính lại | Functional | Mục 4 | High | |
| `RC-05` | Thêm gỡ thành viên thủ công, một hoặc nhiều người, có tìm kiếm | Functional | Mục 5 | High | |
| `RC-06` | Thêm gỡ thành viên theo lô: tệp mẫu, tải lên, đối soát từng dòng, báo lỗi theo dòng | Functional | Mục 6 | High | |
| `RC-07` | Phạm vi nhóm cha bao trùm toàn bộ nhánh con ở mọi màn đọc dữ liệu | Business Rule | Mục 7 | High | **Rule nền**, chi phối mọi báo cáo. Ảnh hưởng hiệu năng truy vấn |
| `RC-08` | Gán nội dung cho nhóm, có tuỳ chọn chảy xuống nhánh con, mặc định tắt | Functional | Mục 8 | High | **Đường gán thứ hai song song với Lớp** — xem `OQ-04` |
| `RC-09` | Cấu hình từng nhóm: người vào sau có tự nhận nội dung đã gán không, toàn bộ hay chỉ còn hiệu lực | Business Rule | Mục 9 | Medium | Chạm logic ghi danh hiện có |
| `RC-10` | Danh sách nhóm dạng cây hoặc bảng, lọc theo nguồn, cấp, trạng thái, người quản lý | Screen | Mục 10 | High | |
| `RC-11` | Nhật ký thay đổi thành viên, đủ để dựng lại ai thuộc nhóm nào tại một thời điểm quá khứ | Data · NFR | Mục 11 | High | Yêu cầu lưu lịch sử có dấu thời gian, giống ràng buộc `C3` ở Gamification |
| `RC-12` | Lưu trữ nhóm: ngừng nhận nội dung mới, giữ lịch sử. Xoá nhóm: xử lý thành viên và nội dung đã gán | Business Rule | Mục 12 | Medium | *"Xử lý"* chưa định nghĩa — xem `OQ-07` |
| `RC-13` | Một nhóm có một hoặc nhiều người quản lý, là người dùng chứ không phải vai trò | Data | Mục 13 | High | |
| `RC-14` | Quản lý suy ra theo cây: không chỉ định đích danh thì lấy quản lý của nhóm cha gần nhất. Tính động | Business Rule | Mục 14 | High | Quan hệ tính lúc đọc, không lưu cứng |
| `RC-15` | Chỉ định quản lý đích danh trên hồ sơ, ghi đè kết quả suy ra từ cây | Functional | Mục 15 | Medium | Tình huống dùng chưa rõ — xem mục 2 |
| `RC-16` | Người quản lý đọc được dữ liệu của nhánh mình, không đọc nhánh khác cùng cấp. Chọn được ở `ORG.ROL.04` | Role-Permission | Mục 16 | Low | **Vùng KB chưa phủ.** Hệ thống dùng Casbin |
| `RC-17` | Trang người học hiện quản lý trực tiếp và đường liên hệ | Screen | Mục 17 | High | Phần duy nhất chạm UpLMS phía học viên |
| `RC-18` | Quản lý bị khoá hoặc rời nhóm thì cảnh báo nhóm trống quản lý, cho chuyển quan hệ sang người khác | Functional | Mục 18 | Medium | |
| `RC-19` | Khai thêm loại quan hệ ngoài quản lý, ví dụ mentor, dùng chung cơ chế gán và phạm vi dữ liệu | Data · Functional | Mục 19 | Medium | Yêu cầu thiết kế mở rộng được từ đầu |

---

## 4. Ba chỗ nhóm mới đụng thứ đang chạy

### 4.1 Nhóm và Lớp

`classes` đã có và cũng gom người học lại. Ở dự án Gamification, hai khái niệm này từng bị lẫn, `CR-001` phải làm rõ: *"phòng ban chính là chức năng nhóm, đồng bộ từ HRM, khác với Lớp"*.

Khác biệt nhìn thấy được:

| | Lớp | Nhóm theo yêu cầu này |
|---|---|---|
| Gắn với | Một khoá học cụ thể | Không gắn khoá |
| Vòng đời | Theo đợt học | Lâu dài, theo cơ cấu tổ chức |
| Người thuộc | Ghi danh vào lớp | Thành viên theo cây |
| Cấu trúc | Phẳng | Cây nhiều cấp |

Nhưng cả hai đều là đường để **gán nội dung học**. Có hai đường gán song song thì phải trả lời: một người vừa trong lớp vừa trong nhóm được gán cùng khoá thì tính một hay hai lượt ghi danh.

### 4.2 Nhóm và phạm vi dữ liệu

`RC-16` là yêu cầu phân quyền thật sự, không phải hiển thị. Hệ thống dùng **Casbin** (`casbin_rule` với `ptype`, `v0`–`v6`), và KB **chưa phủ vùng phân quyền**.

Phạm vi dữ liệu theo nhánh cây là loại phân quyền động: quyền đọc của một người đổi khi cây đổi, không phải khi role đổi. Casbin làm được nhưng cần thiết kế riêng.

### 4.3 Nhóm và báo cáo hồi tố

`RC-11` nói báo cáo phải dựng lại được *"tại một thời điểm trong quá khứ ai thuộc nhóm nào"*. Đây là yêu cầu **lưu lịch sử quan hệ theo thời gian**, nặng hơn nhiều so với lưu trạng thái hiện tại.

Nó chi phối cả `RC-07` (phạm vi cha bao trùm con): báo cáo của tháng trước phải dùng cây của tháng trước, không dùng cây hôm nay.

---

## 5. Phạm vi sơ bộ

### In scope

Khung nhóm và cây · thành viên thủ công và theo lô · quan hệ quản lý · gán nội dung cho nhóm · nhật ký thay đổi · màn danh sách và tìm kiếm.

### Out of scope

| | Vì sao |
|---|---|
| Đồng bộ HRM hai chiều | Yêu cầu chỉ nói đồng bộ *từ* HRM |
| Nhóm cho nhân sự vận hành | `Department Management` đã phục vụ staff. Dự án này nhắm học viên |

### Potential scope — chờ `OQ-01`

Toàn bộ phần khung nhóm (`RC-01`, `RC-04`, `RC-05`, `RC-10`) có thể chuyển từ *làm mới* sang *mở rộng cái đã có*, tuỳ `Group Management` và `Department Management` còn sống hay không.

---

## 6. Phân cỡ đề xuất

**Cỡ `L`.** Đủ cả bốn dấu hiệu, chỉ cần một là đã `L`:

| Dấu hiệu | Ở đây |
|---|---|
| Chạm từ 3 module trở lên | User · Class · Course assignment · Phân quyền · Report · tích hợp HRM |
| Đổi data model | Quan hệ nhiều-nhiều người với nhóm, bảng lịch sử thành viên, bảng quan hệ quản lý |
| Có conflict | Hai đường gán nội dung song song (Lớp và Nhóm) |
| Nhiều hướng giải quyết | Mở rộng `departments` hay dựng bảng mới, là hai hướng khác hẳn nhau |

→ Chạy đủ 9 bước, đủ 4 Gate.

Chi tiết câu hỏi mở: `working/open-questions/open-questions-20261005.md`
