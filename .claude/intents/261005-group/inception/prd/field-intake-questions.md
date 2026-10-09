# Field Intake — Nhóm học viên

**Ngày:** 06/10/2026 · **Giai đoạn 9B** — tra trước khi hỏi
**Nguồn tra:** Swagger `components.schemas` *(đọc 05/10)* · schema Lark *(đọc 05/10)* · KB `04` `06` `09` `11` `12`

> Mục đích: phân biệt field **đã tồn tại** với field **thực sự mới**, để không mô tả lại cái đã có thành mới. Dev sẽ tạo trùng nếu nhầm.

**Quy ước:**

| Ký hiệu | Nghĩa |
|---|---|
| `[đề xuất]` | Tôi tự điền từ KB hoặc Swagger — **cần người viết xem lại** |
| `❓BA` | Không suy được, cần người viết cung cấp |
| **A** | Màn mới hoàn toàn |
| **B** | Sửa màn có sẵn |
| **C** | Chỉ đọc, hiển thị |

---

## 0. Một bộ field đã được nghĩ ra sẵn

`CreateDepartmentDto` trong Swagger — thuộc chức năng cây phòng ban **không chạy**, nhưng bộ field thì đã thiết kế một lần rồi:

| Field | Bắt buộc | Mô tả trong Swagger |
|---|---|---|
| `name` | ✅ | Tên phòng ban |
| `short_name` | | Tên rút gọn |
| `type` | ✅ | **Cấp bậc phòng ban** |
| `unit` | ✅ | **Đơn vị kinh doanh** |
| `description` | | Mô tả |
| `parent_id` | | **Id phòng ban cha** — đây là cây |

✅ **Người viết chốt 06/10: bỏ `type` và `unit`.** *"Không cần, nó là nhóm, và chỉ là nhóm."*

Nhóm giữ đúng bốn thứ: **tên · mã · mô tả · nhóm cha**. Hai field kia là khái niệm của cây phòng ban hành chính, không thuộc về một tập hợp người.

> Nhắc lại cho rõ: đây là **tham khảo bộ field**, không phải đề xuất dùng lại bảng. Thiết kế dữ liệu là việc của Dev.

---

## 1. Phân loại màn

### Màn mới hoàn toàn — **A**

Vì đã chốt bỏ hẳn chức năng nhóm cũ, mọi màn nhóm đều là mới:

| Màn | US | Unit |
|---|---|---|
| Danh sách nhóm *(cây + bảng)* | `US6` | U1 |
| Tạo và sửa nhóm | `US1` · `US2` | U1 |
| Chi tiết nhóm — tab Thành viên | `US3` · `US4` | U1 |
| Chi tiết nhóm — tab Nội dung được giao | `US7` · `US8` | U3 |
| Chi tiết nhóm — tab Người phụ trách | `US9` · `US12` · `US13` | U4 |
| Cấu hình đồng bộ cơ cấu | `US5` | U2 |
| Nhật ký thay đổi thành viên | `US15` | U7 |
| Báo cáo cộng dồn theo nhóm | `US18` | U7 |
| Màn quản lý theo dõi nhánh mình *(LMS)* | `US16` | U5 |

### Sửa màn có sẵn — **B**

| Màn | Sửa gì | US |
|---|---|---|
| **Hồ sơ học viên** *(Ops)* | Thêm khối *Nhóm đang thuộc* và *Quản lý chỉ định đích danh* | `US11` |
| **Hồ sơ học viên** *(LMS)* | Thêm khối *Quản lý của tôi* | `US17` |
| **Dashboard SIS** | Thêm bộ lọc theo nhóm. Bộ lọc làm **động**, không ràng buộc cứng khoá và lớp | `US18` |
| **Chi tiết lớp — tab Học viên** | Hiện **nguồn ghi danh** *(qua nhóm hay thêm tay)*. Thêm dòng cảnh báo vượt sức chứa | `US7` |
| **Chi tiết lớp — tab Mentor** | Mentor đi theo nhóm, hiện mentor này phụ trách nhóm nào | `US12` |

> Màn hồ sơ học viên hiện có **3 tab**: Overview · Class and Course · Security. Thông tin học viên **không sửa được** trên Ops, trừ Username.

---

## 2. Bảng field — U1 Khung nhóm

### Màn tạo và sửa nhóm — **A**

| Field | Hiện có | Kiểu | Bắt buộc | Giá trị hợp lệ | Validate | Rule chi phối | Ghi chú |
|---|---|---|---|---|---|---|---|
| Tên nhóm | Mới | Text | ✅ | | Không rỗng. Tối đa **255 ký tự** `[đề xuất]` | | |
| Mã nhóm | Mới | Text | ✅ | | **Duy nhất** trong tổ chức | `BR-1.x` | |
| Mô tả | Mới | Text dài | | | Tối đa **1000 ký tự** `[đề xuất]` | | |
| Nhóm cha | Mới | Chọn một | | Nhóm cùng nguồn, không phải chính nó, không phải con cháu nó | Chặn chu trình. Chặn vượt 6 cấp | `BR-1.x` | Để trống nghĩa là nhóm gốc |
| Nguồn | Mới | Hệ thống tự gán | ✅ | `Đồng bộ` · `Tự tạo` | Người dùng **không chọn được** | `BR-5.x` | Quyết định ai sửa được gì |
| Trạng thái | Mới | Hệ thống tự gán | ✅ | `Đang dùng` · `Lưu trữ` | | `BR-14.x` | |


### Màn danh sách nhóm — **A**

| Hạng mục | Nội dung |
|---|---|
| **Hai cách xem** | Dạng **cây** *(gấp mở từng nhánh)* và dạng **bảng phẳng*. Mặc định `[đề xuất]` dạng cây |
| **Cột hiển thị** | Tên nhóm · Mã · Nguồn · **Số thành viên** · Người quản lý · Trạng thái · Cập nhật lần cuối |
| **Số thành viên đếm thế nào** | **Giống Drive đếm thư mục** — gồm cả người ở nhánh con, không chỉ người gán trực tiếp |
| **Bộ lọc** | Nguồn · Cấp · Trạng thái · Người quản lý |
| **Tìm kiếm** | Theo tên và mã. Tìm thấy nhóm con thì **hiện cả đường dẫn từ gốc**, giống Drive |
| **Sắp xếp** | `[đề xuất]` theo tên, theo số thành viên, theo ngày cập nhật |
| **Phân trang** | Dạng bảng thì phân trang. Dạng cây **tải dần** — mở nhánh nào tải nhánh đó |

### Màn chi tiết nhóm — tab Thành viên — **A**

| Hạng mục | Nội dung |
|---|---|
| **Cột** | Họ tên · Mã nhân viên · Email · Phòng ban *(theo nguồn nhân sự)* · Ngày vào nhóm · Trạng thái tài khoản |
| **Bộ lọc** | Trạng thái tài khoản · Vào nhóm trực tiếp hay thuộc nhánh con |
| **Hai cách thêm** | Chọn tay nhiều người · Nhập tệp |
| **Nhập tệp** | `.csv` hoặc `.xlsx`, **mỗi lần 1 tệp**. Bản ghi lỗi không thêm, ghi vào log. Giống cách import học viên hiện có |
| **Khoá khi là nhóm đồng bộ** | Nhóm đồng bộ **không cho thêm gỡ thủ công**. Nút ẩn kèm giải thích |
| **Người nghỉ việc** | Mặc định **ẩn**, có bộ lọc hiện lại |

> `Test Account` **không bao giờ xuất hiện** ở màn này, kể cả khi bật mọi bộ lọc.

---

## 3. Bảng field — U3 Giao nội dung

### Chi tiết nhóm — tab Nội dung được giao — **A**

| Field | Hiện có | Kiểu | Bắt buộc | Giá trị hợp lệ | Validate | Ghi chú |
|---|---|---|---|---|---|---|
| Lớp được gán | Mới | Chọn nhiều | ✅ | Lớp đang nhận thêm người | Lớp đã kết thúc **không chọn được** | Chọn **lớp**, không chọn khoá |
| Chảy xuống nhánh con | Mới | Bật tắt | | | | **Mặc định tắt** |
| Tự ghi danh người vào sau | Mới | Bật tắt | | | | **Mặc định tắt**. Chuỗi tiếng Anh đã chốt: `New group members will be automatically enrolled to this group's existing course` |

| Hạng mục | Nội dung |
|---|---|
| **Cột danh sách** | Tên lớp · Khoá học · Thời hạn lớp · Số người đã vào qua nhóm này · Ngày gán |
| **Khi gán** | Hiện trước số người sẽ vào lớp. `[đề xuất]` kèm cảnh báo nếu vượt sức chứa lớp — **không chặn** |
| **Gỡ một lớp khỏi nhóm** | 🔴 **Đã có người trong nhóm học lớp đó thì KHÔNG gỡ được.** Cùng logic với gỡ học viên khỏi lớp. Nút ẩn kèm giải thích |

> Lớp có lớp Foundation gắn kèm thì người vào lớp chính **cũng vào Foundation**. Đây là hành vi sẵn có, không cảnh báo riêng.

---

## 4. Bảng field — U4 Người phụ trách

### Chi tiết nhóm — tab Người phụ trách — **A**

| Field | Hiện có | Kiểu | Bắt buộc | Giá trị hợp lệ | Ghi chú |
|---|---|---|---|---|---|
| Người quản lý | Mới | Chọn nhiều | | Tài khoản nhân sự vận hành | Một nhóm nhiều quản lý |
| Mentor | Mới | Chọn nhiều | | Tài khoản nhân sự vận hành | Đi theo nhóm vào lớp |
| Kế thừa từ nhóm cha | Mới | Hiển thị | — | — | Nhóm con chưa gán thì hiện quản lý kế thừa, ghi rõ *kế thừa từ nhóm nào* |

### Hồ sơ học viên *(Ops)* — **B**

| Thay đổi | Section | Field | Ghi chú |
|---|---|---|---|
| **Thêm** | Overview | Khối **Nhóm đang thuộc** | Danh sách nhóm kèm đường dẫn đầy đủ từ gốc |
| **Thêm** | Overview | Khối **Quản lý** | Phân biệt rõ: *kế thừa theo nhóm* và *chỉ định đích danh* |
| **Thêm** | Overview | Nút **chỉ định quản lý đích danh** | Cho trường hợp báo cáo chéo nhánh |

> Thông tin học viên **không sửa được** trên Ops trừ Username. Quan hệ quản lý chỉ định là thứ mới, không nằm trong ràng buộc đó — cần xác nhận → `F-07`.

---

## 5. Bảng field — U7 Nền tảng

### Nhật ký thay đổi thành viên — **A**

| Cột | Nội dung |
|---|---|
| Thời điểm | |
| Người bị thay đổi | |
| Nhóm | |
| Hành động | `Vào nhóm` · `Rời nhóm` |
| Lý do | `Thêm tay` · `Nhập tệp` · `Đồng bộ` · `Nghỉ việc` · `Điều chuyển` |
| Người thao tác | Để trống nếu do đồng bộ tự làm |

Bộ lọc: khoảng thời gian · nhóm · người · lý do.

> Màn này **tra khi có vấn đề**, không dùng hằng ngày. Không cần tối ưu cho việc xem liên tục.

### Báo cáo cộng dồn theo nhóm — **A** và **B**

| Hạng mục | Nội dung |
|---|---|
| **Chọn nhóm** | Một nhóm, tuỳ chọn gồm cả nhánh con |
| **Chọn mốc thời gian** | Hiện tại, hoặc một ngày trong quá khứ |
| **Đặt ở đâu** | Trong dashboard hiện có, **bộ lọc làm động**, không dựng màn riêng |

#### Chỉ số — `[đề xuất]`, xếp theo câu người dùng thật sự hỏi

| Người dùng hỏi gì | Chỉ số |
|---|---|
| *"Phòng này có bao nhiêu người phải học?"* | **Số người có nghĩa vụ** — người trong nhóm được giao ít nhất một nội dung |
| *"Bao nhiêu người đã xong?"* | **Số hoàn thành** và **tỉ lệ hoàn thành** |
| *"Ai đang chậm?"* | **Số người quá hạn** và **số người chưa bắt đầu** — hai nhóm này cần hành động khác nhau |
| *"Tiến độ chung thế nào?"* | **Tiến độ trung bình** của người đang học |
| *"So với phòng khác ra sao?"* | **Bảng so sánh các nhóm cùng cấp**, cùng nhóm cha |

Năm dòng đầu là số của một nhóm. Dòng cuối là thứ `O4` thật sự hứa — *cộng dồn từ một phòng ban lên tới cả khối* chỉ có nghĩa khi so được các nhánh với nhau.

> Tách **chưa bắt đầu** khỏi **quá hạn** vì hai thứ này đòi hai cách xử lý: chưa bắt đầu thì nhắc, quá hạn thì phải quyết gia hạn hay cho trượt.

> Mọi số liệu **loại `Test Account`**. Người nghỉ việc: báo cáo hiện tại loại ra, báo cáo theo mốc quá khứ tính theo trạng thái tại mốc đó.

---

## 6. Bảng field — U5 Phía học viên và quản lý

### Hồ sơ học viên *(LMS)* — **B**

| Thay đổi | Field | Ghi chú |
|---|---|---|
| **Thêm** | Khối **Quản lý của tôi** | Hiện **nhiều** quản lý. **Quản lý chính lên đầu**, có nhãn phân biệt với quản lý theo nhóm |
| **Thêm** | Cách liên hệ | Hiện **tên, ảnh và email**. Không hiện số điện thoại |

### Màn quản lý theo dõi nhánh mình — **A**

| Hạng mục | Nội dung |
|---|---|
| **Phạm vi** | Chỉ người trong nhánh mình phụ trách. Màn này đọc theo **quan hệ quản lý**, không đọc theo vai trò hệ thống |
| **Dữ liệu thấy được** | **Toàn bộ** dữ liệu học của người đó, kể cả khoá họ nhận qua nhánh khác |
| **Cột** `[đề xuất]` | Họ tên · Nhóm · **Số khoá quá hạn** · Số khoá đang học · Số khoá hoàn thành · Lần học gần nhất |
| **Sắp xếp mặc định** | Theo **số khoá quá hạn** giảm dần — người cần chú ý nhất lên đầu |
| **Không đưa vào** | Tiến độ phần trăm của từng khoá. Quản lý nhìn danh sách để biết *ai cần nhắc*, không để đọc chi tiết. Chi tiết nằm ở màn hồ sơ từng người |

---

## 7. Câu cần người viết trả lời

## 7. Trạng thái — người viết trả lời 06/10/2026

| # | Câu | Đáp án |
|---|---|---|
| ~~`F-01`~~ ✅ | Nhóm có cần `cấp bậc` và `đơn vị kinh doanh` không | **Không.** *"Nó là nhóm, và chỉ là nhóm"* |
| ~~`F-02`~~ ✅ | Mã nhóm bắt buộc và duy nhất không | **Có cả hai** |
| ~~`F-03`~~ ✅ | Số thành viên đếm cả nhánh con không | **Có**, giống Drive đếm thư mục |
| ~~`F-04`~~ ✅ | Tìm thấy nhóm con có hiện đường dẫn từ gốc không | **Có**, như Drive |
| ~~`F-05`~~ ✅ | Dạng cây tải hết hay tải dần | **Tải dần** — mở nhánh nào tải nhánh đó |
| ~~`F-06`~~ ✅ | Gỡ lớp khỏi nhóm thì xử lý thế nào | **Đã có người học thì không gỡ được.** Cùng logic gỡ học viên khỏi lớp |
| ~~`F-07`~~ ✅ | Quản lý chỉ định đích danh là gì | **Một người có nhiều quản lý. Quản lý gắn với hồ sơ là quản lý chính** — cao nhất |
| ~~`F-08`~~ ✅ | Học viên thấy gì về quản lý | **Tên, ảnh, email** |
| ~~`F-09`~~ ✅ | Báo cáo theo nhóm gồm chỉ số nào | **Đồng ý đề xuất** ở §5 |
| ~~`F-10`~~ ✅ | Màn quản lý theo dõi hiện cột nào | **Đồng ý đề xuất** ở §6 |
| ~~`F-11`~~ ✅ | Độ dài tối đa tên nhóm và mô tả | **255 và 1000 ký tự** |
| ~~`F-12`~~ ✅ | Hai công tắc mặc định bật hay tắt | **Mặc định tắt** cả hai |
| **`F-13`** | `MAIL-GRP-01` gửi cho quản lý nào | 🟡 **Phát sinh từ `F-07`.** Đề xuất: quản lý chính ở `To`, quản lý khác ở `CC`. Xem dưới |

---

## `F-07` — "chỉ định đích danh" là gì

Hệ thống có **ba cách** biết ai quản lý ai. Hai cách đầu đi qua nhóm, cách thứ ba không:

| # | Cách | Gắn vào | Ví dụ |
|---|---|---|---|
| 1 | **Gán quản lý cho nhóm** — `US9` | Nhóm | Chị Lan quản lý nhóm `Fulfillment HCM` → quản lý cả 55 người trong đó |
| 2 | **Suy ra theo cây** — `US10` | Nhóm cha | Nhóm `Fulfillment HCM / Ca sáng` chưa gán ai → lấy quản lý của nhóm cha, vẫn là chị Lan |
| 3 | **Chỉ định đích danh** — `US11` | **Một người cụ thể** | Anh Minh thuộc nhóm `Fulfillment HCM`, nhưng báo cáo cho anh Hùng ở `Tech`. Gắn thẳng anh Hùng vào hồ sơ anh Minh |

Cách 3 giải quyết **báo cáo chéo nhánh** — người làm ở phòng A nhưng báo cáo cho trưởng phòng B. Không có nó thì phải xếp anh Minh vào nhóm `Tech`, mà anh Minh không thuộc phòng đó.

✅ **Người viết chốt 06/10:** *"Một người có nhiều quản lý. Quản lý gắn với profile là quản lý to nhất."*

### Thứ bậc giữa các quản lý

| Loại | Nguồn | Vị trí |
|---|---|---|
| **Quản lý chính** | Gắn đích danh trên hồ sơ — `US11` | **Cao nhất.** Chịu trách nhiệm chính về người đó |
| Quản lý theo nhóm | Gán cho nhóm — `US9` | Thường |
| Quản lý kế thừa | Suy từ nhóm cha — `US10` | Thường |

Thứ bậc này **không đổi phạm vi dữ liệu** — `OQ-09` đã chốt: xem được một người thì xem toàn bộ dữ liệu học của người đó, bất kể là loại quản lý nào.

Nó đổi **hai thứ khác**:

| Chỗ | Ảnh hưởng |
|---|---|
| **Hiển thị** | Hồ sơ học viên xếp quản lý chính lên đầu, có nhãn phân biệt |
| **`MAIL-GRP-01`** | 🔴 **Gửi cho ai?** Xem dưới |

### Hệ quả cho `MAIL-GRP-01` — `F-13`

Mail báo *"người này rời nhóm mà còn nghĩa vụ học"* cần **một người chịu trách nhiệm**, không phải một danh sách.

| Cách | Hệ quả |
|---|---|
| Gửi **mọi** quản lý | Ba người nhận ba mail, mỗi người tưởng người kia xử lý. Không ai làm gì |
| **Gửi quản lý chính** ⭐ | Rõ ai phải quyết. Đây chính là lý do thứ bậc có ích |
| Gửi quản lý chính, các quản lý khác nhận bản sao | Rõ trách nhiệm mà vẫn không ai bị bỏ sót thông tin |

**Đề xuất: cách thứ ba.** Người chịu trách nhiệm ở dòng `To`, còn lại ở `CC`.

> Nếu người đó **không có quản lý chính** *(chưa ai gắn đích danh)* thì gửi cho quản lý theo nhóm — và nếu nhiều người thì tất cả cùng ở dòng `To`. Đây là lúc vấn đề *"không ai nhận trách nhiệm"* quay lại, nên `US13` cảnh báo nhóm trống quản lý có giá trị thật.

---

## 8. Nguồn đã tra

| Nguồn | Cụ thể |
|---|---|
| Swagger | `CreateGroupDto` *(2 field)* · `EditGroupDto` *(1)* · `AddUserToGroupDto` · **`CreateDepartmentDto`** *(6 field, có `parent_id`)* · `UpdateDepartmentDto` |
| Schema Lark | `groups` *(3 cột)* · `group_user_instances` · `departments` *(10 cột)* · `users` *(11 cột)* · `class_user_instances` *(9 cột, có `source_type`)* |
| KB | `04-class` *(import lớp, sức chứa, Foundation)* · `06-user-account` *(3 tab hồ sơ, ràng buộc không sửa, `Test Account`)* · `09-notification` · `11-dashboard-sis` *(bộ lọc)* · `12-data-model` |
| **Chưa tra được** | Màn hồ sơ học viên phía LMS — KB `06` §6 chỉ mô tả tab Security, không mô tả bố cục chung |
