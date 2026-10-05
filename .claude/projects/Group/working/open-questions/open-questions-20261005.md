# Open Questions — Group

**Ngày:** 05/10/2026 · **Cập nhật:** 05/10/2026 sau khi PO trả lời
**Nguồn:** `working/ai-drafts/clarified-requirements-20261005.md`

`Blocks = Yes` nghĩa là thiếu câu trả lời thì không viết BRD được.

---

## Nhóm A — đã trả lời

| # | Câu hỏi | Đáp án |
|---|---|---|
| ~~`OQ-01`~~ | `Group Management` và `Department Management` có chạy thật không | ✅ **`Group Management` đang chạy**, phục vụ việc tạo nhóm để gửi thông báo từ Ops. Dự án này mở rộng nó.<br>**`Department Management` không chạy**, trước đây chỉ dành cho `staffs` |
| ~~`OQ-02`~~ | Nhóm khác Lớp ở điểm nào | ✅ **Nhóm gắn người, Lớp gắn nội dung.** Bảng chín tiêu chí ở `clarified-requirements` §4.1 |
| ~~`OQ-03`~~ | Một người ở cả Lớp và Nhóm, cùng được gán một khoá | ✅ **Một lượt ghi danh** |
| ~~`OQ-04`~~ | `ORG.ROL.04` là gì | ✅ Mã chức năng: mỗi vai trò gắn một phạm vi — toàn tổ chức, một hoặc nhiều nhánh nhóm chỉ định, hay chỉ những người mình quản lý |
| ~~`OQ-05`~~ | Cơ chế đồng bộ HRM | ✅ **Chưa có.** HRM là Lark, đã đồng bộ được học viên, Lark cũng đã có sẵn cây tổ chức |

---

## `OQ-06` — Số cấp tối đa của cây. Đã đo từ dữ liệu thật

### Cây tổ chức hiện tại trên Lark

Đo từ `working/raw-inputs/lark-users-by-department.csv`, file xuất từ HRM:

| | Số |
|---|---|
| Nhân sự trong cây | 384 |
| Phòng ban riêng biệt | 53 |
| Khối ở cấp 1 | 5 — `ECOM` · `VẬN HÀNH` · `Tech` · `CHUYỂN ĐỔI SỐ` · `BOD` |
| **Độ sâu lớn nhất** | **4 cấp** dưới gốc |

Phân bố phòng ban theo độ sâu:

| Cấp | Số phòng ban | Số người |
|---|---|---|
| 1 | 2 | 6 |
| 2 | 22 | 203 |
| 3 | 27 | 166 |
| 4 | 2 | 9 |

Hai nhánh duy nhất chạm cấp 4:

```
ECOM / Trung tâm vận hành 1 / Growth 1 / Sub-Growth 1
ECOM / Marketing B2C HN / Booking / Sub-Booking
```

Cây thật nông hơn dự đoán. Hơn một nửa nhân sự nằm ở cấp 2, và chỉ 9 người trong 384 ở cấp sâu nhất.

### Đề xuất: mặc định 6 cấp, cấu hình được

| | |
|---|---|
| Giá trị mặc định | **`6`** — thực tế dùng 4, dư 2 cấp để tổ chức mở rộng mà không phải đổi cấu hình |
| Cách đếm | Từ **nhóm gốc là cấp 1**. Gốc ảo `(root)` của Lark không tính |
| Phạm vi áp dụng | **Từng cây gốc**, không phải tổng. `RC-02` cho phép nhiều cây song song |
| Cấu hình | Gắn tổ chức, không đóng cứng trong mã |

### Giới hạn số cấp giải vấn đề gì

Ba vấn đề hay bị gộp làm một, nhưng chỉ một trong ba thật sự cần tới nó:

| Vấn đề | Giới hạn số cấp giải được không |
|---|---|
| Cây lỗi tạo vòng lặp: A là cha B, B lại là cha A | ❌ Phải kiểm chu trình khi di chuyển nhánh |
| Truy vấn *cha bao trùm con* (`RC-07`) chậm khi cây sâu | ❌ Thuộc về cách lưu trữ, là việc của Dev |
| Người dùng vô tình tạo cây quá sâu bằng kéo thả | ✅ **Đây là việc của nó** |

Nên giá trị thật của giới hạn là **van an toàn chống nhập sai**, không phải để bảo vệ hiệu năng.
---

## `OQ-07` · `OQ-08` · `OQ-09` — PO giao phân tích

### `OQ-07` — Xoá nhóm thì thành viên và nội dung đã gán xử lý thế nào

**Câu hỏi này có thể không cần trả lời, vì nên bỏ luôn chức năng xoá.**

Lý do nằm ở hai chỗ đã chốt:

| Đã chốt | Hệ quả |
|---|---|
| Nhóm **không sinh nghĩa vụ học**, nghĩa vụ nằm ở Lớp *(nguyên tắc 6)* | Lượt ghi danh đã sinh ra **sống độc lập trong Lớp**. Xoá nhóm không đụng tới chúng |
| `RC-11` đòi dựng lại *"tại một thời điểm quá khứ ai thuộc nhóm nào"* | Xoá nhóm là **phá chính yêu cầu này**. Báo cáo của quý trước sẽ trỏ vào một nhóm không còn tồn tại |
| `RC-12` đã có cơ chế **lưu trữ**: ngừng nhận nội dung mới, giữ nguyên lịch sử | Đây đúng là thứ người dùng cần khi họ nghĩ mình cần "xoá" |

**Đề xuất:**

| Nhóm thế nào | Cho làm gì |
|---|---|
| Chưa từng có thành viên và chưa từng gán nội dung | **Xoá được.** Đây là nhóm tạo nhầm, không có lịch sử để mất |
| Đã từng có thành viên hoặc đã từng gán nội dung | **Chỉ lưu trữ được, không xoá.** Nút xoá ẩn đi kèm giải thích |

Nếu vẫn muốn giữ chức năng xoá cho mọi nhóm, thì quy tắc là: **lượt ghi danh giữ nguyên**, vì chúng sống ở Lớp. Người đang học dở vẫn học tiếp. Chỉ luật đứng *"ai vào nhóm này thì vào lớp kia"* mất đi, nên từ đó không có ai mới được thêm vào lớp qua đường này nữa.

### `OQ-08` — Báo cáo hồi tố lùi về quá khứ bao xa

**Đề xuất: giữ toàn bộ, không dọn.**

Lý do là khối lượng dữ liệu quá nhỏ để phải lo. Đo từ file HRM thật:

| | Số |
|---|---|
| Nhân sự trong cây | 384 |
| Phòng ban | 53 |

Mỗi lần một người vào hoặc ra một nhóm là một dòng. Với tỉ lệ biến động nhân sự thông thường, con số này ở mức vài trăm dòng mỗi năm. Mười năm vẫn chưa tới mức cần nghĩ tới chuyện dọn.

Đổi lại, đặt một hạn lưu trữ sẽ tạo ra một loại lỗi khó chịu: báo cáo của năm ngoái chạy được, năm kia thì không, và không ai nhớ vì sao.

Quyết định này cũng nhất quán với Gamification, nơi `BR-3.9` chốt *"sổ giao dịch điểm giữ toàn bộ, không giới hạn thời gian, không dọn"* với lý do tương tự.

### `OQ-09` — Người có nhiều quản lý thì phạm vi dữ liệu tính thế nào

`OQ-18` đã chốt hướng: **quản lý chỉ xem được nhóm mình quản lý**. Phần còn lại cần làm rõ là khi một người thuộc hai nhánh có hai quản lý khác nhau.

Hai cách:

| | Cách | Hệ quả |
|---|---|---|
| **a** ⭐ | Xem được người thì **xem toàn bộ dữ liệu học** của người đó | Quản lý nhánh A thấy cả tiến độ khoá mà X học qua nhánh B |
| b | Chỉ xem dữ liệu phát sinh từ nội dung gán qua nhánh mình | Mỗi quản lý thấy một phần |

**Đề xuất a**, vì cách b không khớp với cách dữ liệu đang lưu: tiến độ học treo vào **lượt ghi danh của Lớp**, không treo vào nhóm. Một khoá có một tiến độ, không chia được theo nhánh mà người đó thuộc về.

Cách b cũng tạo ra một tình huống khó giải thích: hai quản lý cùng mở hồ sơ một người, thấy hai con số khác nhau, và không ai biết con số nào đúng.

**Hệ quả phải chấp nhận:** người thuộc hai nhánh thì hai quản lý cùng thấy toàn bộ dữ liệu học của họ. Đây là hệ quả của cơ cấu ma trận mà `RC-02` cố ý cho phép, không phải lỗi phân quyền. Nếu tổ chức không muốn vậy thì phải không xếp người đó vào hai nhánh.

---

## Nhóm B — còn lại

| # | Câu hỏi | Vì sao quan trọng | Blocks |
|---|---|---|---|
| ~~`OQ-10`~~ | Người gia nhập sau có tự nhận nội dung đã gán không | ✅ **Có công tắc chọn lúc tạo nhóm.** Chuỗi: `New group members will be automatically enrolled to this group's existing course` |
| ~~`OQ-11`~~ | Trang người học hiện quản lý nào | ✅ **Hiện nhiều quản lý** |
| ~~`OQ-12`~~ | Quan hệ `mentor` làm ngay hay hoãn | ✅ **Làm luôn đợt này** |
| ~~`OQ-16`~~ | `Group Management` hiện làm được gì | ✅ **Bỏ qua, coi như chưa có gì** |
| ~~`OQ-18`~~ | `ORG.ROL.04` và `ORG.GRP.09` thuộc dự án nào | ✅ **Đơn giản hoá:** quản lý chỉ xem được nhóm mình quản lý. Không dùng cơ chế phạm vi nhiều mức ở đợt này |
| ~~`OQ-19`~~ | Bộ nguyên tắc chứa nguyên tắc 6 ở đâu | ✅ **Chưa có trong KB, đã bổ sung** `16-domain-principles.md` |

---

## Nhóm C — đã bỏ

Toàn bộ câu hỏi kỹ thuật cho Dev (`OQ-13`, `OQ-14`, `OQ-15`, `OQ-17`, `OQ-20`) **bỏ khỏi dự án này**.

PO chốt ngày 05/10: Dev sẽ phân tích lại bằng công cụ của họ. Một thiết kế hoặc một giả định kỹ thuật sai từ phía PO **neo suy nghĩ người đọc**, tốn công gỡ hơn là không có gì.

Quy tắc này đã ghi vào `CLAUDE.md` và `clarify-requirements.md` để áp cho mọi dự án sau.

Riêng `OQ-17` *(cây Lark sâu mấy cấp)* không cần hỏi Dev nữa — đã đo được từ file HRM, xem `OQ-06`.

---

## Nhóm D — phát sinh từ nghiên cứu LMS khác (05/10)

Bốn câu này không chặn viết BRD, nhưng nên có đáp án trước Bước 7 vì chúng ảnh hưởng phạm vi.

| # | Câu hỏi | Vì sao |
|---|---|---|
| `OQ-21` | **Khi đồng bộ, người ở nhánh sâu được ghi là thành viên của một nhóm sâu nhất, hay của cả bốn nhóm trên đường đi?** | Tài liệu tích hợp HRIS ghi rằng phần lớn lần đồng bộ hỏng vì nhóm lồng nhau, do không làm phẳng cơ cấu trước khi đẩy. Hai cách cho hai kết quả khác hẳn ở báo cáo và phạm vi quản lý |
| `OQ-22` | **Một người rời nhóm thì nghĩa vụ học đã nhận qua nhóm đó xử lý thế nào?** | Yêu cầu mới bàn trường hợp xoá cả nhóm (`OQ-07`), chưa bàn trường hợp một người rời. Moodle gỡ ghi danh trong tình huống tương tự |
| `OQ-23` | **Học viên bị điều chuyển phòng ban thì nghĩa vụ học theo nhóm cũ xử lý thế nào?** | Tầng 3 của mô hình tích hợp HRIS là sự kiện vòng đời nhân sự. Yêu cầu hiện chỉ nhắc trường hợp quản lý rời vị trí |
| `OQ-24` | **Có cần nhóm động theo điều kiện không?** Ví dụ *"mọi người có chức danh chứa chữ Trưởng nhóm, ở bất kỳ phòng ban nào"* | Hiện chỉ có hai cách vào nhóm: đồng bộ và gán tay. Nhóm cắt ngang cơ cấu không làm được bằng cả hai cách đó. Moodle có `Dynamic Cohorts` |

---

## Trạng thái

Không còn câu nào chặn. **Viết BRD được.**

Bốn câu nhóm D để Bước 7 quyết, không cần trả lời ngay.
