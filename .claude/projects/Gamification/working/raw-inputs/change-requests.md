# Change Requests — Gamification

| CR ID | Ngày | Nội dung thay đổi | Lý do / Nguồn | Trạng thái |
| --- | --- | --- | --- | --- |
| **CR-001** | 2026-09-23 | **Đưa Bảng xếp hạng (leaderboard) vào phạm vi đợt này.** Kèm 6 yêu cầu chi tiết. Bỏ xếp hạng theo phòng ban | PO chỉ định trực tiếp (ảnh chụp bảng + chỉ thị) | ✅ **Đã áp dụng** — BRD v0.2, re-entry từ Bước 4 do PO confirm |
| **CR-002** | 2026-09-23 | **Chỉ số xếp hạng của chiến dịch chọn được** — theo điểm, theo huy hiệu, hoặc theo số khoá hoàn thành. Kèm **luật chỉnh sửa chiến dịch** (đang chạy thì không sửa được) | PO trả lời tại Gate 1 (OQ-A4) | ✅ **Đã áp dụng** — BRD v0.3 |
| **CR-004** | 2026-09-23 | **Gate 1 `Need Revision`.** Đổi cơ chế điểm đăng nhập · định nghĩa lại loại huy hiệu · ngưỡng lên hạng theo nhiều chỉ số · thu hẹp thông báo · tách stakeholder | PO phản hồi tại Gate 1 | ✅ **Đã áp dụng** — BRD v0.4 |
| **CR-007** | 2026-09-23 | **Bỏ hẳn chiến dịch, kỳ lịch và cơ chế chốt kỳ.** Thay bằng **bộ chọn khoảng ngày tự do** trên bảng xếp hạng. Chấp nhận kết quả sống.<br>**Khoá mốc huy hiệu sau khi tạo**, nên huy hiệu đã nhận không bao giờ mất | PO nêu tại 9C, khi viết `US8` | 🔄 **Đang áp dụng** |
| **CR-009** | 2026-10-01 | **Điểm check-in đổi từ mức cố định sang tăng dần theo chuỗi ngày đăng nhập liên tiếp.** Thêm khối chuỗi trên trang Thành tích. Chuỗi tính theo ngày đăng nhập, đếm mọi ngày dương lịch | PO yêu cầu, sau khi nghe phân tích rủi ro | 🔄 **Đang áp dụng** |

---

# CR-007 — Bỏ chiến dịch và kỳ lịch, thay bằng khoảng ngày tự do

## Nguyên văn PO

> *"nếu theo kỳ lịch mà cũng chỉ hiển thứ hạng cho những người có hoạt động cố gắng thì có khác gì chọn theo khoảng trượt đâu nhỉ, chỉ khác là chọn nhanh hơn thôi chứ, còn nếu muốn xem lại lịch sử thì phải chọn 1 ngày chính xác trong quá khứ để xem chứ, nên là tính năng chiến dịch tôi thấy cũng chả cần thiết nữa, muốn xem thì chọn khoảng ngày mà xem là đc thôi"*
>
> *"chuyển logic point sẽ set được logic mỗi event sẽ được bao nhiêu điểm; các mốc để nhận được huy hiệu sẽ không thay đổi được cố định các mốc, về level thì sẽ tính được dựa trên bao nhiêu points sẽ lên level, bao nhiêu huy hiệu sẽ được lên level, bao nhiều khóa hoàn thành sẽ được lên level"*
>
> *"đổi sang như này thì có thay đổi thì cũng chỉ áp dụng sau khi có thay đổi, còn huy hiệu đã nhận được thì có thay đổi cũng không mất huy hiệu được"*

## Nhận định

Lập luận của PO đúng ở chỗ cốt lõi: **một bộ chọn khoảng ngày tự do bao trùm cả kỳ lịch lẫn chiến dịch.** Nút *"tháng này"* chỉ là lối tắt điền sẵn hai cái ngày. Muốn xem tháng 9 năm ngoái thì đằng nào cũng phải chọn ngày cụ thể.

## Cái mất: `O5`

`O5` là *"kết quả mỗi kỳ công bố được và không thay đổi về sau, đủ tin cậy làm căn cứ trao thưởng"*.

Với truy vấn theo khoảng ngày, **kết quả của cùng một khoảng có thể khác nhau tuỳ lúc hỏi**:

| Nguyên nhân | Hệ quả |
|---|---|
| Bài chấm tay nộp 30/9, mentor chấm 3/10 | Điểm rơi vào tháng nào tuỳ cách ghi ngày |
| Học viên bị `Block` hoặc rời tổ chức (`BR-6.8`) | Biến mất khỏi bảng, kể cả bảng của khoảng đã qua |

**PO chọn chấp nhận.** Việc trao thưởng vốn đã làm ngoài hệ thống, đội truyền thông ghi lại số liệu tại đúng lúc công bố.

→ `O5` viết lại thành mục tiêu nhẹ hơn, hoặc bỏ.

## Cái được

| Bỏ được | |
|---|---|
| Thực thể chiến dịch, vòng đời và trạng thái của nó | `US12`, `US13` |
| Cơ chế chốt kỳ, đóng băng, snapshot | `US14`, `S19` |
| Màn xem lại kỳ đã kết thúc | `US8`, `S20` |
| Hai US "chưa làm" về chiến dịch | `US19`, `US21` |
| `CF-6` Gate 2 — không tắt được gamification khi chiến dịch đang chạy | Không còn tình huống này |
| `OQ-04` cơ chế dừng chiến dịch · `OQ-05` khoá bảng điểm khi chiến dịch chạy | Không còn cần |

**Danh sách US: 17 xuống 13.**

## Thay đổi thứ hai: ba tầng cấu hình khác nhau

| Thứ | Sửa được không | Áp dụng thế nào |
|---|---|---|
| **Điểm mỗi hành động** | ✅ Sửa được | Từ thời điểm sửa trở đi (`C4`) |
| **Mốc huy hiệu** | ❌ **Khoá sau khi tạo** | Không đổi được nên không có tình huống phải xét lại |
| **Ngưỡng lên hạng** | ✅ Sửa được, theo ba chỉ số: điểm · số huy hiệu · số khoá hoàn thành | Từ thời điểm sửa trở đi. Hạng **không tụt** |

## 🔄 Trả lại một quyết định đã đảo trước đó

Vì mốc huy hiệu nay **khoá sau khi tạo**, tình huống nâng ngưỡng rồi gỡ huy hiệu **không còn tồn tại**.

| Đã quyết trước | Nay |
|---|---|
| `BR-4.6` `BR-4.7` — hạ ngưỡng thì cấp bù, nâng ngưỡng thì gỡ | ❌ **Bỏ.** Mốc không sửa được |
| `BR-1.4` sửa 23/09 — huy hiệu bám cấu hình, gỡ được | 🔄 **Trả lại bản gốc: huy hiệu đã nhận giữ vĩnh viễn** |
| `A5` bị bác bỏ | ✅ **Có hiệu lực trở lại** |
| `C4` chỉ áp cho điểm | ✅ **Áp lại cho mọi thứ** |
| Sự kiện `Badge removed` trong lịch sử | ❌ **Bỏ** |
| `OQ-22` không báo khi gỡ huy hiệu | Không còn cần |

Kết quả là **ba cơ chế nay cùng một luật**: mọi thay đổi cấu hình chỉ áp từ thời điểm đổi trở đi, và không có gì bị lấy lại khỏi học viên. Nhất quán hơn hẳn bản trước.

---

# CR-004 — Phản hồi Gate 1 (Need Revision)

| # | Yêu cầu của PO | Thay đổi trong BRD |
|---|---|---|
| 1 | Tách **L&D** và **Quản lý trực tiếp** (quản lý trực tiếp của học viên trong tổ chức) | Stakeholder từ 1 dòng thành 2. ⚠️ Quản lý trực tiếp **chưa có công cụ nào** trong đợt này — `US18` là công cụ duy nhất phục vụ họ, mà đã hoãn |
| 2 | **Điểm đăng nhập: mỗi lần login được điểm**, chống spam bằng khoảng cách thời gian (ví dụ dưới 2 tiếng thì không tính). **Không dùng chuỗi ngày liên tiếp** | `S3` viết lại. Xem §6.7 |
| 3 | **Bốn loại huy hiệu đo bằng chỉ số đếm**: Tích cực (số lần login) · Học tập (số hoạt động hoàn thành) · Test (số bài test hoàn thành) · Course (số khoá hoàn thành) | `S5` viết lại. Ba loại điều kiện cũ bị gỡ → `N4` |
| 4 | **US hiệu quả chiến dịch bỏ** — hệ thống chỉ cung cấp **kết quả**, đội truyền thông tự đo hiệu quả bên ngoài | Gỡ US. `O4` viết lại. Thêm `N11` |
| 5 | **US tính bù điểm bỏ** — chạy ngầm thì bật lên đã có sẵn; tắt hẳn thì không ghi gì nên không bù | Gỡ US và gỡ mục Out of scope tương ứng |
| 6 | **B8: `Point` = điểm, `Level` = hạng học viên.** Ngưỡng lên hạng có thể dùng **nhiều logic**: điểm, huy hiệu, số khoá hoàn thành | `S6` mở rộng. **Đây là yêu cầu mới, không chỉ là chốt từ vựng** |

## 🆕 Phát hiện: ba chỗ dùng chung một khái niệm

Sau thay đổi 3 và 6, cùng một khái niệm **"chỉ số đo lường"** xuất hiện ở ba nơi:

| Nơi dùng | Chỉ số |
|---|---|
| Điều kiện huy hiệu | Số lần đăng nhập · số hoạt động · số bài test · số khoá |
| Ngưỡng lên hạng | Điểm · số huy hiệu · số khoá |
| Chỉ số xếp hạng chiến dịch | Điểm · số huy hiệu · số khoá |

→ Đề xuất `S23`: **một danh mục chỉ số duy nhất dùng lại ở cả ba chỗ**, thay vì ba cơ chế riêng. Lý do quan trọng nhất không phải gọn code, mà là *"số khoá hoàn thành"* phải được tính giống hệt nhau ở cả ba chỗ — tách riêng là mở đường cho ba định nghĩa lệch nhau, loại lỗi rất khó phát hiện và phá thẳng `O6`.

## 🟢 Hệ quả tốt: phụ thuộc Notification gần như biến mất

`OQ-B5` + `OQ-B6` được trả lời: **chỉ đẩy trong hệ thống khi học viên đang online, không gửi mail.**

| | Trước (v0.3) | Sau (v0.4) |
|---|---|---|
| Mức tác động tới Notification | 🟠 Vừa | 🟢 **Rất thấp** |
| Phụ thuộc module Notification đang ẩn | Có | **Không** |
| Ràng buộc job nửa tiếng (`KB-NOTI-05`) | Có | **Không** |
| Nguy cơ trùng mail #10/#29 | Có | **Không** |

Đây là một trong những thay đổi làm giảm rủi ro nhiều nhất của vòng này.

## 🔺 Hệ quả ngược: phụ thuộc Keycloak nặng lên

| | Trước | Sau |
|---|---|---|
| Mức tác động tới User/Auth | 🟠 Vừa | 🔴 **Cao** |
| Vai trò | Một hành động tính điểm phụ | **Nguồn dữ liệu cho cả `S3` lẫn huy hiệu loại Tích cực** |

Nếu `OQ-B1` trả lời là Keycloak không ghi sự kiện đăng nhập thì **mất hai hạng mục**, không phải một.

Kèm theo một câu hỏi mới `OQ-B14`: **"đăng nhập" là gì?** Học viên dùng SSO Lark có thể rất hiếm khi nhập lại thông tin đăng nhập — nếu chỉ tính lần đăng nhập thật thì cả `S3` lẫn huy hiệu Tích cực gần như không phát sinh.

---

# CR-002 — Chỉ số xếp hạng chọn được cho chiến dịch

## Nguyên văn PO

> *"chiến dịch có giới hạn nội dung là sao nhỉ, ý bạn có phải là các thành phần tính thành tích đúng ko, cái đó thì sẽ dựa vào lúc setup thôi, muốn chiến dịch đó tính theo point, theo huy hiệu theo số course hoàn thành được thì là động, chỉ cần làm logic chỉnh sửa chiến dịch thôi, ví dụ đang chạy rồi thì không sửa được"*

## Tôi đã hỏi sai hướng

| | |
|---|---|
| **Tôi định hỏi** | Chiến dịch có giới hạn **nội dung nào được tính điểm** không? (ví dụ: chỉ hoạt động của khoá An toàn thông tin mới sinh điểm chiến dịch) |
| **PO mô tả** | Chiến dịch chọn được **xếp hạng theo chỉ số nào**: điểm · huy hiệu · số khoá hoàn thành |

Hai chuyện khác nhau. Câu hỏi của tôi về **đầu vào** (nội dung nào sinh điểm), điều PO nói về **đầu ra** (sắp xếp bảng theo con số nào).

**Kết luận:**
- **Giới hạn nội dung** → PO không yêu cầu → giữ ở `Out of scope` (US18)
- **Chỉ số xếp hạng chọn được** → yêu cầu mới → vào `In scope`
- **Luật chỉnh sửa chiến dịch** → yêu cầu mới → vào `In scope`

## 🚨 Hệ quả: bài toán đồng hạng quay lại, nặng hơn

Ba chỉ số không giống nhau về độ phân tán:

| Chỉ số | Khoảng giá trị thực tế | Nguy cơ đồng hạng |
|---|---|---|
| **Điểm** | Hàng trăm đến hàng nghìn | Thấp — phân tán tự nhiên |
| **Số huy hiệu** | 0–10 | **Cao** |
| **Số khoá hoàn thành** | 0–5 trong một kỳ | **Rất cao** |

Xếp hạng theo "số khoá hoàn thành" trong một chiến dịch một tháng thì phần lớn học viên sẽ cùng ở mức 1 hoặc 2 khoá — **hàng chục người đồng hạng nhất**.

→ Tiêu chí phụ **"ai đạt mức đó sớm hơn xếp trên"** (§6.6) từ chỗ *nên có* thành **bắt buộc**. Không có nó thì hai trong ba chỉ số không dùng được.

`C3` đã bắt lưu từng lần cộng điểm kèm thời điểm nên dữ liệu có sẵn — nhưng với chỉ số "số huy hiệu" và "số khoá" thì cần thời điểm đạt **huy hiệu** và thời điểm **hoàn thành khoá**, không phải thời điểm cộng điểm. `❓BA` — cần xác nhận cả ba loại mốc đều lưu được thời điểm.

## Hệ quả thứ hai: snapshot phải lưu cả chỉ số

Kết quả cuối kỳ (S18) phải ghi kèm **chỉ số đã dùng để xếp**. Một chiến dịch xếp theo huy hiệu và một chiến dịch xếp theo điểm cho ra hai bảng không so sánh được với nhau.

---

# CR-003 — Bỏ phạm vi xếp hạng theo lớp

## Nguyên văn PO

> *"không phải giữ phạm vi xếp hạng theo lớp mà có thể filter xem theo lớp, như thế chắc dễ hình dung hơn, xem theo lớp chứ không phải làm trong 1 lớp để xem, để biết các học viên trong lớp đó học như nào, và chức năng này tạm bỏ vì sau này chính là filter theo nhóm đấy, bây giờ làm cho lớp thì lại bị trùng mục đích, sau lại phải làm lại"*

## Tôi hiểu sai mục đích

Tôi đề xuất "phạm vi xếp hạng theo lớp" như một **bảng xếp hạng riêng trong lớp** để học viên thi đua với bạn cùng lớp — lập luận là bảng toàn tổ chức quá lớn nên không ai với tới được.

PO mô tả khác: đó là **bộ lọc xem theo lớp** trên cùng một bảng xếp hạng, và mục đích là **để biết học viên trong lớp đó học thế nào** — tức góc nhìn quản lý, không phải góc nhìn thi đua của học viên.

## Quyết định: bỏ khỏi đợt này

Lý do của PO: bộ lọc theo lớp **sau này chính là bộ lọc theo nhóm**. Làm riêng cho lớp bây giờ thì trùng mục đích, sau phải làm lại.

→ Gộp thành một hạng mục hoãn duy nhất: **bộ lọc bảng xếp hạng theo nhóm** (bao gồm cả lớp và phòng ban), chờ chức năng nhóm đồng bộ từ HRM.

## ⚠️ Rủi ro còn lại — ghi nhận, không tranh luận lại

Đợt này chỉ có **một bảng xếp hạng toàn tổ chức**. Với hàng nghìn học viên, phần lớn sẽ không bao giờ ở gần nhóm đầu, và chu kỳ ngắn không đổi được điều đó vì người chăm nhất vẫn đứng đầu mọi chu kỳ.

Cơ chế giảm nhẹ duy nhất là **"Vị trí của tôi"** (S17) — luôn hiện thứ hạng người đang xem kèm vài người liền kề.

Ghi lại để theo dõi sau khi ra mắt, không phải để đề nghị đổi quyết định.

---

# CR-001 — Bảng xếp hạng

## Nội dung gốc (chép nguyên văn từ ảnh PO cung cấp)

| Hạng mục | Nội dung |
|---|---|
| Phạm vi xếp hạng | Toàn tổ chức, trong phòng ban của tôi, hoặc trong lớp. Người học chọn được phạm vi muốn xem |
| Chu kỳ xếp hạng | Kỳ là một khoảng có ngày bắt đầu và ngày kết thúc. Tuần, tháng, quý, năm là nút bấm nhanh sinh ra khoảng đó. Kỳ cố định theo lịch, không dùng cửa sổ trượt. Biên kỳ cắt theo múi giờ của tổ chức khai ở TNT.CFG.02, không theo giờ máy chủ. Chu kỳ ngắn cho người mới cơ hội đứng đầu. |
| Kỳ tự khai cho chiến dịch | Khai hai ngày bất kỳ, không cần trùng biên lịch, kèm tên chiến dịch, phạm vi người tham gia và nội dung được tính |
| Vị trí của tôi | Luôn hiện thứ hạng của người đang xem kèm vài người liền kề, kể cả khi họ không nằm trong nhóm đầu |
| Chốt kỳ và lưu kết quả | Hết kỳ thì đóng băng bảng, lưu kết quả cuối để công bố và trao thưởng, rồi mở kỳ mới về 0 |
| Lịch sử các kỳ trước | Xem lại bảng xếp hạng của tháng trước, quý trước, chiến dịch đã kết thúc |

## Chỉ thị kèm theo (nguyên văn)

> *"thôi làm nốt leaderboard trong giai đoạn này luôn, đây là yêu cầu"*
>
> *"xếp hạng theo nhóm chưa làm trong giai đoạn này, vì chức năng nhóm chưa làm, cứ xếp hạng theo cả tổ chức"*

---

## Đối chiếu hệ thống — ba phát hiện

### 1. 🚨 Học viên **không có phòng ban**

`Fact` — quan hệ khoá ngoại trong schema:

```
departments.id ──► staffs.department_id        ← phòng ban gắn với NHÂN SỰ
users                                           ← học viên KHÔNG có department_id
```

Bảng `departments` (có `unit`, `tree_id` — là cây phòng ban) chỉ nối tới `staffs`, tức nhân sự vận hành. Bảng `users` (học viên) **không có cột phòng ban nào**.

Nên "xếp hạng trong phòng ban của tôi" hiện **không khả thi về mặt dữ liệu** với học viên — không chỉ là "chức năng nhóm chưa làm", mà là học viên chưa được gắn vào phòng ban nào cả.

→ Khớp với chỉ thị của PO: bỏ khỏi đợt này.

### 2. ⚠️ "Nhóm" và "Lớp" là hai chuyện khác nhau

| Khái niệm | Trạng thái dữ liệu | Có xếp hạng được không? |
|---|---|---|
| **Phòng ban** (`departments`) | Chỉ gắn với nhân sự, không gắn học viên | ❌ Không |
| **Nhóm người dùng** (`groups` + `group_user_instances`) | **Có** trong DB, **có** 9 endpoint `Group Management`. Nhưng giao diện quản lý trên Ops (`Recipients List`) **đang ẩn** — KB `09` §1 | ⚠️ Dữ liệu có, giao diện chưa dùng được |
| **Lớp** (`classes` + `class_user_instances`) | **Có đầy đủ và đang chạy.** Mọi học viên đều thuộc ít nhất một lớp | ✅ **Có** |

PO nói *"cứ xếp hạng theo cả tổ chức"*. Cần làm rõ câu này có bao gồm bỏ luôn **phạm vi lớp** không — vì lớp khác hẳn hai cái kia, dữ liệu đã sẵn sàng. `❓BA`

### 3. 🚨 `TNT.CFG.02` — tham chiếu ngoài, không tra được

Yêu cầu ghi: *"Biên kỳ cắt theo múi giờ của tổ chức khai ở TNT.CFG.02"*.

- **Không có** mã `TNT.CFG.02` ở bất kỳ đâu trong repo hay KB
- Bảng `tenant` hiện có `id`, `type`, `billing_model`, `can_publish_marketplace`, `contract_type`, `name`, `subdomain` — **không có trường múi giờ**
- Không có khái niệm múi giờ ở bất kỳ chỗ nào trong KB

→ Đây là phụ thuộc vào một hạng mục cấu hình **chưa tồn tại**. `❓BA`

---

## Tác động tới các quyết định đã chốt

### A8 bị bác bỏ

BRD v0.1 giả định: *"Các chiến dịch không chồng lấn thời gian — tại một thời điểm chỉ có tối đa một kỳ đang chạy."*

CR-001 cho thấy **ngược lại**: dòng "Lịch sử các kỳ trước" nói xem lại được *"bảng xếp hạng của tháng trước, quý trước, chiến dịch đã kết thúc"* — tức tháng, quý và chiến dịch **cùng tồn tại song song**.

**Hệ quả thiết kế:** một lần cộng điểm phải quy được vào **nhiều kỳ cùng lúc**. 10 điểm nhận ngày 15/10 đồng thời tính vào bảng tuần, bảng tháng, bảng quý, bảng năm, và mọi chiến dịch đang chạy hôm đó.

Nghĩa là **"điểm theo kỳ" không phải một con số được cộng dồn, mà là kết quả tính từ sổ giao dịch điểm theo khoảng ngày.** Ràng buộc `C3` (lưu từng lần cộng điểm) đã bao được điều này — nhưng cách hiểu về "điểm theo kỳ" ở BRD v0.1 cần viết lại.

Riêng phần *"chốt kỳ, đóng băng bảng, lưu kết quả cuối"* thì ngược lại — kết quả cuối kỳ **phải được vật chất hoá và lưu lại**, không tính lại mỗi lần xem.

### N6 cần xem lại

BRD v0.1 ghi `N6 — Phần thưởng vật chất: không làm`. CR-001 xuất hiện cụm *"lưu kết quả cuối để công bố và **trao thưởng**"*.

Cách hiểu của tôi: hệ thống chỉ cần **giữ lại bảng xếp hạng cuối kỳ** để con người dựa vào đó trao thưởng ngoài hệ thống — không cần quản lý phần thưởng trong sản phẩm. Cần PO xác nhận. `❓BA`

### US9 phình ra

BRD v0.1, US9 chỉ là *"tạo và quản lý chiến dịch"*. CR-001 thêm hai thứ:

| Thêm | Vấn đề |
|---|---|
| **"phạm vi người tham gia"** | Chiến dịch giới hạn được ai tham gia. Nhưng cơ chế nhóm học viên chưa dùng được (phát hiện 2) — vậy khoanh phạm vi bằng gì? Theo lớp? Theo khoá? `❓BA` |
| **"nội dung được tính"** | Chiến dịch giới hạn được nội dung nào tính điểm (ví dụ chỉ tính khoá An toàn thông tin). Đây là chức năng lọc điểm theo phạm vi nội dung — chưa có trong BRD v0.1 |

### N1 bị đảo

`N1 — Bảng xếp hạng: không làm` → **chuyển vào In scope**. `US13` từ *"chưa làm"* → **làm trong đợt này**.

---

## Điểm re-entry đề xuất

**BRD (Bước 4)** — chờ PO confirm.

| Lý do | |
|---|---|
| Loại thay đổi | Phạm vi + business rule mức nghiệp vụ → bảng trong `/change-request` CR-2 chỉ về **BRD** |
| Tầng bị sai lệch kết luận | Scope (N1 đảo chiều) · Assumption (A8 bị bác) · US list (US13 đổi trạng thái, US9 phình) · Objective (O5 "làm nền cho leaderboard sau" nay không còn đúng) |
| BRD đã được duyệt chưa? | **Chưa** — đang trình Gate 1, chưa có quyết định. Nên không phải "sửa tài liệu đã chốt", chỉ là cập nhật bản nháp trước khi duyệt |

**Tài liệu sẽ cập nhật:**

| File | Từ → Đến |
|---|---|
| `working/ai-drafts/clarified-requirements-20260923.md` | v0.2 → v0.3 |
| `working/open-questions/open-questions-20260923.md` | cập nhật |
| `docs/brd/brd-v0.1-20260923.md` | **v0.1 → v0.2** |
| `project-context.md` · `project-decisions.md` | cập nhật |

**Gate phải duyệt lại:** Gate 1 (chưa duyệt lần nào — sẽ trình lại bản v0.2). Các Gate sau chưa chạy nên không bị ảnh hưởng.

✅ **PO confirm điểm re-entry = BRD (Bước 4)** — 23/09/2026.

---

## PO trả lời — 23/09/2026

| # | Câu hỏi | Đáp án |
|---|---|---|
| 1 | Phòng ban là gì? | **Phòng ban chính là chức năng nhóm** — được **đồng bộ từ HRM của tổ chức** sang thành cây thư mục kiểu sơ đồ tổ chức. **Hiện chưa làm → bỏ qua** |
| 2 | `TNT.CFG.02` là gì? | **Cấu hình tenant trong module Tenant.** Hiện chưa có multi-tenant → **cứ làm cho tổ chức hiện tại**.<br>Nội dung TNT.CFG.02 (PO cung cấp): *"Hồ sơ tổ chức và tham số — Tên, mã định danh, **múi giờ**, ngôn ngữ hiển thị, định dạng ngày và số. Các tham số này chi phối cách hiển thị và cách tính mốc thời hạn học trong toàn hệ thống"* |
| 3 | Tháng trước / quý trước / chiến dịch đã kết thúc | **Không phải chiến dịch.** Tháng, quý là **mốc snapshot hệ thống tự tính**. **Chiến dịch** là khoảng **do vận hành setup** |
| 4 | Trao thưởng | **Hành động ngoài hệ thống.** Hệ thống chỉ giữ lại bảng xếp hạng cuối kỳ |
| 5 | Phạm vi người tham gia chiến dịch | *"hiện tại chắc chỉ dùng cho phạm vi lớp và khóa, nhưng như thế cũng hơi khó nhỉ, nếu như thế thì sẽ có mức trần về điểm, ai hoàn thành thì cũng sẽ có điểm giống nhau, lúc đấy lại phải thêm yếu tố thời gian hoàn thành trước nữa, như thế thì hơi phức tạp"* → xem phân tích dưới |

### Ba điều làm rõ quan trọng

**a) Hai loại kỳ khác bản chất — không được gộp**

| Loại | Ai tạo | Ví dụ |
|---|---|---|
| **Kỳ lịch** | **Hệ thống tự tính**, không cần cấu hình | Tuần này · Tháng 9 · Quý III · Năm 2026 |
| **Chiến dịch** | **Vận hành khai tay** — hai ngày bất kỳ, không cần trùng biên lịch | *"Tháng an toàn thông tin 10/9–15/10"* |

Bản CR-001 ban đầu tôi hiểu nhầm hai cái này là một. `US12` (quản lý chiến dịch) chỉ áp cho loại thứ hai; loại thứ nhất **không cần màn quản lý nào**.

**b) `A8` chính thức bị bác bỏ**

Kỳ lịch lồng nhau theo bản chất (tuần nằm trong tháng, tháng trong quý, quý trong năm), cộng thêm chiến dịch chạy song song. **Một lần cộng điểm quy vào nhiều kỳ cùng lúc.** → ràng buộc `C7` mới.

**c) Múi giờ là tham số của tổ chức, không phải hằng số**

Bảng `tenant` hiện **không có trường múi giờ**. Module Tenant chứa `TNT.CFG.02` chưa được làm. Nhưng biên kỳ (`23:59:59` ngày cuối tháng là lúc nào?) phụ thuộc vào nó.

→ Đợt này phải khai **một tham số múi giờ ở cấp tổ chức**, thiết kế để module Tenant sau này tiếp quản. → ràng buộc `C6` mới.

> ⚠️ Ngoài phạm vi nhưng đáng ghi: TNT.CFG.02 nói các tham số này *"chi phối cách tính **mốc thời hạn học** trong toàn hệ thống"*. Nghĩa là hạn khoá học hiện cũng đang tính theo giờ máy chủ chứ không theo múi giờ tổ chức. Đây là vấn đề của module Course/Class, không phải của gamification — nêu để PO biết.

---

## 🔍 Phân tích câu hỏi 5 — bài toán đồng hạng trong chiến dịch giới hạn nội dung

PO nêu đúng vấn đề: **nếu chiến dịch chỉ tính một khoá, điểm có trần. Ai hoàn thành cũng bằng điểm nhau → bảng xếp hạng vô nghĩa.**

Thêm tiêu chí thời gian hoàn thành thì giải được, nhưng PO thấy phức tạp.

### Nhận định

Vấn đề này **chỉ xảy ra khi nội dung bị giới hạn**. Kỳ lịch (tuần/tháng/quý) tính mọi hoạt động nên điểm phân tán tự nhiên, không bị đồng hạng hàng loạt.

### Ba hướng

| Hướng | Nội dung | Đánh đổi |
|---|---|---|
| **A** | Thêm tiêu chí phụ **"ai đạt mức điểm đó sớm hơn xếp trên"** cho mọi bảng | Không phức tạp như tưởng — xem dưới. Nhưng vẫn không cứu được trường hợp mọi người cùng hoàn thành 100% |
| **B** ⭐ | **Hoãn "giới hạn nội dung được tính" sang đợt sau.** Chiến dịch đợt này = khoảng thời gian + phạm vi người tham gia, **mọi nội dung đều tính**. Nhu cầu *"cùng học khoá X trước ngày Y"* dùng **huy hiệu** thay vì bảng xếp hạng | Bỏ một tính năng khỏi đợt này. Nhưng đúng công cụ hơn |
| **C** | Chiến dịch giới hạn nội dung xếp hạng **theo thời điểm hoàn thành** thay vì theo điểm | Là một cơ chế thứ hai phải xây và giải thích cho học viên |

### `Recommendation` — **B, kèm A như một rule chung**

**Vì sao B:** nhu cầu *"tháng này cả công ty cùng học khoá An toàn thông tin"* **vốn không phải bài toán xếp hạng** — nó là bài toán *đạt hay chưa đạt trước hạn*. Công cụ đúng cho nó là **huy hiệu có điều kiện thời gian**, mà hệ thống đã có sẵn trong phạm vi: `S5` đã gồm điều kiện **"hoàn thành một nội dung cụ thể"** và **"theo mốc thời gian"**. Ghép hai cái là ra đúng *"hoàn thành khoá X trước 15/10 thì được huy hiệu Y"*.

Dùng bảng xếp hạng cho việc này là dùng sai công cụ — và chính vì sai công cụ nên mới sinh ra bài toán đồng hạng mà PO vừa phát hiện.

**Vì sao vẫn nên có A:** tiêu chí phụ theo thời điểm rẻ hơn PO nghĩ. Ràng buộc `C3` đã bắt lưu từng lần cộng điểm kèm thời điểm, nên *"ai đạt mức điểm này sớm hơn"* chỉ là sắp xếp theo `(điểm giảm dần, thời điểm đạt tăng dần)` — không cần dữ liệu mới, không cần cơ chế mới.

Và nó phục vụ đúng `Problem`: học viên học sớm xếp trên học viên học dồn sát hạn, dù cùng điểm.

---

# CR-009 — Điểm check-in tăng dần theo chuỗi

## Nguyên văn PO

> *"phần điểm checkin bạn đã làm đúng theo rule là daily check in, đăng nhập liên tục mới có điểm chưa nhỉ, đã theo logic đó chưa, hay đăng nhập cách ngày vẫn nhận đc điểm, t muốn làm theo dạng streak ấy"*
>
> *"hãy làm điểm tăng dần theo chuỗi và hiện chuỗi trên giao diện"*

Hai lựa chọn PO chốt sau khi đọc phân tích rủi ro:

| Câu hỏi | PO chọn |
|---|---|
| Chuỗi tăng khi nào | **Ngày có đăng nhập** — không cần học gì |
| Ngày nghỉ xử lý sao | **Đếm mọi ngày dương lịch** — thứ 7, chủ nhật, ngày lễ không vào là đứt |

## Trạng thái trước CR

`US5` đang là check-in rời rạc: mỗi ngày vào hệ thống được một mức điểm **cố định**, ngày nào vào thì ngày đó có điểm, vào cách ngày vẫn được điểm bình thường. Scope ghi rõ *"Không có chuỗi ngày liên tiếp"*.

Rule này đến từ chính `CR-004`, khi PO bác bỏ cơ chế chuỗi: *"sẽ có cơ chế chống spam chứ không phải nhiều ngày liên tiếp mới có điểm"*, rồi chốt lại ở `A21`: *"đổi thành đăng nhập hằng ngày, kiểu mỗi ngày vào thì sẽ được điểm"*.

`CR-009` đảo lại quyết định đó.

## Rule mới

### Công thức điểm

Điểm nhận được ở ngày thứ `n` của chuỗi:

```
điểm = min( điểm_nền + (n - 1) × bước_tăng , trần_điểm_chuỗi )
```

Ví dụ với `điểm_nền = 25`, `bước_tăng = 5`, `trần = 50`:

| Ngày của chuỗi | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8+ |
|---|---|---|---|---|---|---|---|---|
| Điểm | 25 | 30 | 35 | 40 | 45 | 50 | 50 | 50 |

Ba tham số đều do vận hành cấu hình, đặt cùng chỗ với bảng điểm hiện có.

### Chuỗi tăng và đứt

| # | Rule |
|---|---|
| 1 | Chuỗi **tăng 1** khi học viên đăng nhập, tính **một lần duy nhất trong ngày**. Đăng nhập nhiều lần trong ngày không tăng thêm |
| 2 | **Không đăng nhập trọn một ngày dương lịch → chuỗi về `0`.** Lần đăng nhập kế tiếp bắt đầu chuỗi mới từ `1`, điểm về mức nền |
| 3 | Biên ngày cắt theo **múi giờ tổ chức**, theo `C9` *("Ngày" trong check-in và trần điểm/ngày cắt theo múi giờ tổ chức)* |
| 4 | **Điểm đã nhận không bị thu hồi khi đứt chuỗi.** Giữ nguyên tắc xuyên suốt: không lấy lại gì của học viên |
| 5 | Hệ thống lưu **chuỗi dài nhất từng đạt**, không reset khi đứt |
| 6 | Điểm chuỗi **vẫn chịu trần điểm mỗi ngày**. Chạm trần thì ghi vào lịch sử với `0` điểm kèm lý do, giống mọi nguồn điểm khác |
| 7 | `Test Account` bị loại khỏi toàn bộ cơ chế chuỗi, theo `C10` *(`Test Account` bị loại khỏi toàn bộ logic gamification)* |
| 8 | Đổi ba tham số cấu hình **chỉ áp dụng từ thời điểm đổi**, theo `C4`. Chuỗi đang chạy **không bị reset** khi đổi cấu hình |

### Hiển thị

Trang Thành tích của tôi thêm một khối:

| Thành phần | Nội dung |
|---|---|
| Chuỗi hiện tại | Số ngày liên tiếp đang giữ |
| Chuỗi dài nhất | Kỷ lục của chính học viên đó |
| Điểm ngày mai | Mức điểm sẽ nhận nếu ngày mai vào, hoặc dòng báo đã chạm trần |
| Nhắc giữ chuỗi | Một dòng nói rõ **không vào ngày mai là chuỗi về `0`** |

Lịch sử ghi nhận hiện điểm check-in kèm **ngày thứ mấy của chuỗi**, để học viên đối chiếu được con số.

## Tác động

| Hạng mục | Thay đổi |
|---|---|
| `US5` *(Điểm khi vào hệ thống hằng ngày)* | **Viết lại phần tính điểm.** Mức cố định → công thức tăng dần, cộng 8 rule trên |
| `US1` *(Trang Thành tích của tôi)* | Thêm khối chuỗi |
| `US3` *(Lịch sử ghi nhận)* | Dòng điểm check-in thêm thông tin ngày thứ mấy của chuỗi |
| `US8` *(Cấu hình điểm)* | Thêm ba tham số: điểm nền, bước tăng, trần điểm chuỗi |
| Bảng `Thành tích của học viên` | Thêm `chuỗi hiện tại`, `chuỗi dài nhất`, `ngày có mặt gần nhất` |
| Bảng `Ngày có mặt của học viên` | **Không đổi.** Đã đủ để dựng lại chuỗi khi cần đối chiếu |
| Scope | Bỏ dòng *"Không có chuỗi ngày liên tiếp"* |

Không phát sinh bảng mới.

## Rủi ro PO chấp nhận

Bốn điểm đã nêu trước khi PO quyết, ghi lại để sau này không phải tranh luận lại:

| # | Rủi ro | Vì sao |
|---|---|---|
| 1 | **Thưởng hành vi mở ứng dụng, không thưởng việc học.** Số liệu General Launch cho thấy 53 người đăng nhập nhưng chỉ 29 người bắt đầu học — 45% vào mà không học. Chuỗi tính theo đăng nhập trả điểm cho đúng nhóm đó | Ăn vào `O5` *(điểm số đáng tin, không bị thổi lên bằng thao tác đối phó)* |
| 2 | **Nghỉ cuối tuần là đứt chuỗi.** Học viên là nhân viên, không mở UpLMS thứ 7 chủ nhật. Chuỗi thực tế hiếm khi vượt 5 ngày, và người chăm nhất cũng đứt chuỗi mỗi tuần | Phần thưởng chuỗi dài gần như không ai với tới |
| 3 | **Nghỉ phép, công tác, ốm đều bị phạt** như nhau | Phản tác dụng về quản trị nhân sự |
| 4 | **Bảng xếp hạng khó giải thích.** Hai người cùng học 20 ngày, một người liền mạch một người ngắt quãng, điểm chênh đáng kể dù khối lượng học như nhau | Câu hỏi *"sao tôi học nhiều hơn mà điểm thấp hơn"* không có câu trả lời gọn |

## Một mâu thuẫn phải xử lý khi viết `US5`

Lựa chọn hiển thị của PO có nhắc **cảnh báo sắp đứt chuỗi**. Cảnh báo này chỉ hữu ích khi học viên **không** ở trong hệ thống — nhưng `BR-2.1` chốt *thông báo chỉ đẩy khi học viên đang mở UpLMS, không gửi mail, không xếp hàng gửi sau*. Người sắp đứt chuỗi theo định nghĩa là người không vào, nên họ sẽ không bao giờ thấy cảnh báo.

Hai cách:

| | Cách | Đánh đổi |
|---|---|---|
| **a** ⭐ | **Bỏ cảnh báo đẩy.** Thay bằng dòng nhắc tĩnh ngay trên trang Thành tích: *"Vào mỗi ngày để giữ chuỗi. Không vào ngày mai là chuỗi về 0."* Học viên đọc lúc đang xem thành tích | Không chặn được người đã nghỉ vài ngày |
| **b** | **Mở lại kênh mail** riêng cho việc nhắc chuỗi | Đảo quyết định `CR-004` *(thu hẹp thông báo, không gửi mail)*, và là loại mail dễ gây khó chịu nhất |

Đề xuất **a**, đã viết vào bảng hiển thị ở trên. PO phản đối thì nói, tôi đổi sang **b**.
