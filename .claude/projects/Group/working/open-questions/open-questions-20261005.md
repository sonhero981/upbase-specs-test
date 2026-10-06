# Open Questions — Group

**Ngày:** 05/10/2026 · **Cập nhật:** 05/10/2026 sau khi PO trả lời
**Nguồn:** `working/ai-drafts/clarified-requirements-20261005.md`

`Blocks = Yes` nghĩa là thiếu câu trả lời thì không viết BRD được.

---

## Nhóm A — đã trả lời

| # | Câu hỏi | Đáp án |
|---|---|---|
| ~~`OQ-01`~~ | `Group Management` và `Department Management` có chạy thật không | ⚠️ **Đáp án đã thay đổi — xem `BA-01`.**<br>Ban đầu ghi *"`Group Management` đang chạy, dự án này mở rộng nó"*. Ngày 05/10 PO chốt **bỏ hẳn cả `Group Management` lẫn Recipients List, coi như chưa có gì** — nhóm hiện tại là nhóm phẳng, không có gì để kế thừa.<br>**`Department Management` không chạy**, trước đây chỉ dành cho `staffs` |
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

> ✅ **Cả ba đã chốt ngày 05/10/2026 tại Gate 1. PO đồng ý toàn bộ đề xuất bên dưới.** Phần phân tích giữ nguyên để tra lại lý do. Xem `project-decisions.md`.

### ~~`OQ-07`~~ ✅ — Xoá nhóm thì thành viên và nội dung đã gán xử lý thế nào

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

### ~~`OQ-08`~~ ✅ — Báo cáo hồi tố lùi về quá khứ bao xa

**Đề xuất: giữ toàn bộ, không dọn.**

Lý do là khối lượng dữ liệu quá nhỏ để phải lo. Đo từ file HRM thật:

| | Số |
|---|---|
| Nhân sự trong cây | 384 |
| Phòng ban | 53 |

Mỗi lần một người vào hoặc ra một nhóm là một dòng. Với tỉ lệ biến động nhân sự thông thường, con số này ở mức vài trăm dòng mỗi năm. Mười năm vẫn chưa tới mức cần nghĩ tới chuyện dọn.

Đổi lại, đặt một hạn lưu trữ sẽ tạo ra một loại lỗi khó chịu: báo cáo của năm ngoái chạy được, năm kia thì không, và không ai nhớ vì sao.

Quyết định này cũng nhất quán với Gamification, nơi `BR-3.9` chốt *"sổ giao dịch điểm giữ toàn bộ, không giới hạn thời gian, không dọn"* với lý do tương tự.

### ~~`OQ-09`~~ ✅ — Người có nhiều quản lý thì phạm vi dữ liệu tính thế nào

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

> ✅ **Cả bốn đã chốt ngày 06/10/2026 ở Bước 7.** Xem `project-decisions.md`.

| # | Câu hỏi | Đáp án |
|---|---|---|
| ~~`OQ-21`~~ | Khi đồng bộ, người ở nhánh sâu thuộc một nhóm sâu nhất hay cả đường đi | ✅ **Nhóm sâu nhất.** Một người một quan hệ thành viên, không nhân bản theo độ sâu. Nhóm cha vẫn bao trùm nhánh con ở mức **đọc** |
| ~~`OQ-22`~~ | Một người rời nhóm thì nghĩa vụ học đã nhận xử lý thế nào | ✅ **Xét theo tình trạng học của từng khoá.** Chưa học → chuyển được. Đang học dở hoặc đã xong → **thông báo cho quản lý và L&D vào xử lý thủ công**, hệ thống không tự quyết |
| ~~`OQ-23`~~ | Học viên bị điều chuyển phòng ban thì xử lý thế nào | ✅ **Cùng luật với `OQ-22`** |
| ~~`OQ-24`~~ | Có cần nhóm động theo điều kiện không | ✅ **Không.** Đúng hai cách vào nhóm: đồng bộ từ HRM theo cây tổ chức, và tự tạo thủ công. `US19` bỏ |

### Ba trường hợp rời nhóm, ba luật khác nhau

| Trường hợp | Luật | Chốt ở |
|---|---|---|
| **Nghỉ việc** | Gỡ khỏi nhóm. Lượt ghi danh **đánh dấu kết thúc**, giữ nguyên dữ liệu | `CF-4` · `OQ-36` |
| **Rời nhóm, chưa học khoá nào** | Chuyển được, không vướng gì | `OQ-22` |
| **Rời nhóm, đang học dở hoặc đã học xong** | **Báo quản lý và L&D**, người quyết chứ không phải hệ thống | `OQ-22` |

Áp một luật cho cả ba sẽ hoặc mất dữ liệu học, hoặc chặn việc hợp lệ.

### Hai chỗ `OQ-22` còn cần làm rõ trước khi viết PRD

| # | Câu | Vì sao |
|---|---|---|
| `OQ-37` | **"Chuyển được" nghĩa là gì?** `OQ-29` đã chốt **chưa có chức năng chuyển lớp** — muốn chuyển thì xoá khỏi lớp cũ rồi thêm vào lớp mới. Với người chưa học thì không mất gì, nhưng cần nói rõ hệ thống làm **tự động** hay chỉ **gợi ý** | Quyết định `US20` có bao nhiêu phần tự động |
| `OQ-38` | **Thông báo cho quản lý và L&D là loại gì — email hay thông báo trong hệ thống?** Và **L&D là ai** trong mô hình phân quyền hiện có | 30 mail event hiện có **không có cái nào cho việc này**. Màn gửi thông báo thủ công đang `hidden` |

---

## Nhóm E — phát sinh ở Bước 5, rà phạm vi liên quan (05/10)

Năm câu `BA-01` `BA-02` `BA-03` `BA-04` `BA-07` đã chốt, xem `project-decisions.md`. Hai câu còn lại:

### ~~`BA-05`~~ ✅ — `US15` cần nhật ký kiểu nào

> ✅ **PO chốt 05/10/2026:** *(a)* báo cáo theo nhóm **phải** xem lại được theo mốc quá khứ · *(b)* nhật ký **không dùng thường xuyên**, chỉ tra khi có vấn đề.
> **Hệ quả:** dữ liệu thành viên theo thời gian là **nền của báo cáo**, không phải một màn hình. `US15` là màn tra cứu nhẹ. Thêm `US18` cho báo cáo cộng dồn.

> ⚠️ **Câu hỏi ban đầu đặt sai.** Tôi hỏi *"cần nhật ký riêng hay `field_change_logs` đã đủ"* — đó là hỏi PO về một bảng trong cơ sở dữ liệu, tức là câu kỹ thuật. Câu đúng phải là: **`US15` cần trả lời được những câu hỏi gì.**

#### Hai loại nhật ký trả lời hai câu khác nhau

| | Nhật ký **thay đổi** | Nhật ký **thành viên theo thời gian** |
|---|---|---|
| Ghi cái gì | Mỗi lần có người sửa dữ liệu | Mỗi lần một người vào hoặc ra một nhóm |
| Trả lời câu | *"Ai đã sửa gì, lúc nào"* | *"Lúc đó, ai ở trong nhóm nào"* |
| Dùng để | Truy trách nhiệm khi có sai sót | Dựng lại báo cáo của một mốc quá khứ |
| Hệ đã có chưa | ✅ Có — `field_change_logs` | ❌ Chưa |

#### Vì sao loại thứ nhất không thay được loại thứ hai

Ví dụ thật:

> Quý 3 chốt báo cáo: *"Fulfillment HCM — 48/55 người hoàn thành khoá An toàn lao động"*.
> Tháng 10 phòng này nhận thêm 6 người. Hôm nay mở lại báo cáo quý 3.

| Có nhật ký thành viên | Không có |
|---|---|
| Vẫn ra **48/55** — tính theo 55 người có mặt ngày 30/09 | Ra **48/61** — tính theo danh sách hôm nay |

Nhật ký thay đổi *về lý thuyết* suy ra được con số 55, nhưng phải có trạng thái gốc rồi phát lại toàn bộ lịch sử từ ngày đầu tới 30/09. Mỗi lần xem một báo cáo cũ là một lần phát lại.

#### Câu đúng cần PO trả lời

| # | Câu | Vì sao cần |
|---|---|---|
| **a** | **Báo cáo theo nhóm có cần xem lại theo mốc quá khứ không?** Ví dụ mở lại số liệu quý 3 và vẫn ra đúng con số đã chốt lúc đó | Cần → phải có nhật ký thành viên. Không cần → `O5` chỉ còn để truy trách nhiệm, nhẹ hơn nhiều |
| **b** | **Ai sẽ tra nhật ký này, và để làm gì?** Vận hành tự tra, hay chỉ dùng khi có khiếu nại | Quyết định `US15` là một màn hình thật hay chỉ là dữ liệu nằm sẵn |

### ~~`BA-06`~~ ✅ — người nghỉ việc còn trong nhóm không

> ✅ **PO chốt 05/10/2026: đồng ý toàn bộ đề xuất bên dưới**, kèm luật đồng bộ *(người biến mất khỏi nguồn HRM thì ghi là rời nhóm kèm thời điểm, không xoá dòng)*.

#### Hiện trạng

`KB-USER-03`: nhân sự bị xoá ở hệ thống tổ chức *(nghỉ việc)* → tài khoản UpLMS **tự chuyển `Block`**. Người `Block` không đăng nhập được, bị đăng xuất khỏi mọi thiết bị.

Cơ chế này **đã chạy**. Thứ chưa có là: sau khi `Block` thì quan hệ với nhóm xử lý thế nào.

#### Câu này không gộp được — phải tách bốn

| # | Câu con | Nhận xét |
|---|---|---|
| 1 | Có **gỡ khỏi nhóm** không | Câu gốc, ba câu còn lại phụ thuộc vào nó |
| 2 | Có hiện trong **danh sách thành viên** không | Giữ hết thì danh sách đầy người đã nghỉ |
| 3 | Có tính vào **báo cáo** không | Báo cáo hiện tại và báo cáo quá khứ phải khác nhau |
| 4 | Có **nhận nội dung mới** qua luật đứng không | Rõ ràng là không. Họ không đăng nhập được |

#### 🔴 Chỗ nguy hiểm: `BA-06` và `OQ-22` tương tác với nhau

Nếu chọn **gỡ khỏi nhóm**, mà `OQ-22` lại theo tiền lệ Comment Replier *(rời nhóm thì gỡ khỏi lớp)*, thì dây chuyền là:

```
Nghỉ việc → Block → gỡ khỏi nhóm → gỡ khỏi lớp → mất lượt ghi danh
                                                  → mất dữ liệu học
                                                  → báo cáo quý trước đổi số
```

Một người nghỉ việc làm **số liệu của quý đã chốt thay đổi**. Đây là lý do mạnh nhất để không gỡ.

#### Đề xuất: giữ trong nhóm, đánh dấu trạng thái, lọc ở nơi dùng

| Chỗ | Xử lý |
|---|---|
| **Quan hệ với nhóm** | **Giữ nguyên.** Không gỡ, không xoá dòng |
| **Luật đứng** | **Bỏ qua người `Block`.** Không ghi danh thêm vào lớp nào |
| **Danh sách thành viên nhóm** | Mặc định **ẩn**, có bộ lọc để hiện lại |
| **Báo cáo hiện tại** *(nhóm này đang học thế nào)* | **Loại** người `Block` |
| **Báo cáo theo mốc quá khứ** | Tính theo trạng thái **tại mốc đó**, không theo hôm nay |

Ba lý do:

| | Lý do |
|---|---|
| 1 | **Gỡ không hoàn tác được, đánh dấu thì có.** Người nghỉ rồi quay lại làm là chuyện thường. Đã gỡ thì phải dựng lại thủ công; đánh dấu thì bật lại là xong |
| 2 | **Chặn dây chuyền ở trên.** Không gỡ khỏi nhóm thì không kích hoạt luật `OQ-22`, dữ liệu học quá khứ còn nguyên |
| 3 | **Nhất quán với cách hệ này đã xử lý tài khoản.** Nghỉ việc không xoá tài khoản mà chuyển `Block`. Nhóm nên theo cùng nguyên tắc |

#### ⚠️ Một chỗ cơ chế đồng bộ sẽ đánh nhau với đề xuất này

Người nghỉ việc **biến mất khỏi cây tổ chức trên Lark**. Nếu nhóm đồng bộ là bản sao đúng của Lark thì lần đồng bộ kế tiếp sẽ tự gỡ họ ra — đúng thứ đề xuất này muốn tránh.

Nên luật đồng bộ phải nói rõ: **người biến mất khỏi nguồn HRM thì ghi là "rời nhóm" kèm thời điểm, không xoá dòng quan hệ.**

Đây là chỗ nhóm **đồng bộ** và nhóm **tự tạo** hành xử khác nhau, cần ghi thành luật ở PRD.

---

## Trạng thái

| Nhóm | Trạng thái |
|---|---|
| A · B · C | ✅ Đóng |
| `OQ-06` `OQ-07` `OQ-08` `OQ-09` | ✅ Đóng tại Gate 1, 05/10/2026 |
| `BA-01` `BA-02` `BA-03` `BA-04` `BA-07` | ✅ Đóng ở Bước 5, 05/10/2026 |
| `BA-05` `BA-06` | ✅ Đóng ở Bước 5, 05/10/2026 |
| **D — `OQ-21`…`OQ-24`** | 🔴 Còn mở. `OQ-21` và `OQ-22` **chặn PRD**. Quyết ở Bước 7 |
