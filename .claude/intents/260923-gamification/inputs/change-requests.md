# Change Requests — Gamification

| CR ID | Ngày | Nội dung thay đổi | Lý do / Nguồn | Trạng thái |
| --- | --- | --- | --- | --- |
| **CR-001** | 2026-09-23 | **Đưa Bảng xếp hạng (leaderboard) vào phạm vi đợt này.** Kèm 6 yêu cầu chi tiết. Bỏ xếp hạng theo phòng ban | PO chỉ định trực tiếp (ảnh chụp bảng + chỉ thị) | ✅ **Đã áp dụng** — BRD v0.2, re-entry từ Bước 4 do PO confirm |
| **CR-002** | 2026-09-23 | **Chỉ số xếp hạng của chiến dịch chọn được** — theo điểm, theo huy hiệu, hoặc theo số khoá hoàn thành. Kèm **luật chỉnh sửa chiến dịch** (đang chạy thì không sửa được) | PO trả lời tại Gate 1 (OQ-A4) | ✅ **Đã áp dụng** — BRD v0.3 |
| **CR-004** | 2026-09-23 | **Gate 1 `Need Revision`.** Đổi cơ chế điểm đăng nhập · định nghĩa lại loại huy hiệu · ngưỡng lên hạng theo nhiều chỉ số · thu hẹp thông báo · tách stakeholder | PO phản hồi tại Gate 1 | ✅ **Đã áp dụng** — BRD v0.4 |
| **CR-007** | 2026-09-23 | **Bỏ hẳn chiến dịch, kỳ lịch và cơ chế chốt kỳ.** Thay bằng **bộ chọn khoảng ngày tự do** trên bảng xếp hạng. Chấp nhận kết quả sống.<br>**Khoá mốc huy hiệu sau khi tạo**, nên huy hiệu đã nhận không bao giờ mất | PO nêu tại 9C, khi viết `US8` | 🔄 **Đang áp dụng** |
| **CR-009** | 2026-10-01 | **Điểm check-in đổi từ mức cố định sang tăng dần theo chuỗi ngày đăng nhập liên tiếp.** Thêm khối chuỗi trên trang Thành tích. Chuỗi tính theo ngày đăng nhập, đếm mọi ngày dương lịch | PO yêu cầu, sau khi nghe phân tích rủi ro | 🔄 **Đang áp dụng** |
| **CR-010** | 2026-10-01 | **Bỏ trần điểm mỗi ngày.** Kéo theo bỏ sự kiện `No points` trong lịch sử. Làm rõ logic lên hạng: mỗi mốc chạm được đều cho một hạng, không phải lấy tiêu chí cao nhất | PO review design và đính chính | 🔄 **Đang áp dụng** |
| **CR-011** | 2026-10-06 | **Trang cấu hình Ops tự lưu, bỏ nút lưu.** Chỉ giữ hai xác nhận dạng popover. Tắt `Points` hoặc `Badges` thì tiêu chí lên hạng tương ứng khoá theo. Bỏ giới hạn trên của số điểm. Bỏ ô chọn múi giờ và nhãn trạng thái | PO làm design màn `Enable - Setting`, thấy lệch với PRD và TD-FE | ✅ **Đã áp dụng** — PRD v0.9, re-entry từ PRD do PO confirm |
| **CR-012** | 2026-10-08 | **Bảng xếp hạng: `Badges` chỉ còn ở `All time` như `Level`, thêm bảng `Activities`.** Kèm câu chữ check-in thay cho "login", và mấy chỗ vá đi cùng | PO review design màn cấu hình huy hiệu và chuỗi check-in | ✅ **Đã áp dụng** — gộp với `CR-013`, re-entry từ BRD do PO confirm |
| **CR-013** | 2026-10-08 | **Đưa chiến dịch (campaign) trở lại phạm vi**, đảo một phần `CR-007`. Học viên bỏ bộ chọn khoảng ngày tự do, chỉ còn khung cố định. Campaign chọn khoảng thời gian và loại hành động tính điểm, **số điểm theo cấu hình chung** | PO chỉ định: khoảng ngày tự do phía học viên là lỗ hổng để spam tính toán | ✅ **Đã áp dụng** — BRD v0.7 · Impact v0.3 · Solution v0.2 · PRD v0.10, re-entry từ BRD do PO confirm |

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
| `BR-4.6` · `BR-4.7` — hạ ngưỡng thì cấp bù, nâng ngưỡng thì gỡ | ❌ **Bỏ.** Mốc không sửa được |
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

---

# CR-010 — Bỏ trần điểm ngày, làm rõ logic lên hạng

## Nguyên văn PO

> *"không có trần điểm ngày"*
>
> *"Every 3,000 points đúng là cứ 3000 điểm lên hạng 1 lần mà, có phải cộng dồn đâu, tiêu chí nào đến trước thì lên hạng trước"*

## 1. Bỏ trần điểm mỗi ngày

`BR-8.6` và `BR-13.3` bị bỏ. Kéo theo:

| Chỗ | Thay đổi |
|---|---|
| `US8` | Bỏ ô nhập trần, bỏ `BR-8.6` và `BR-8.7`, bỏ trường dữ liệu |
| `US3` | Bỏ sự kiện `No points` — chạm trần là lý do duy nhất sinh ra nó. Còn **ba** loại sự kiện |
| `US5` | `BR-5.10` viết lại: **trần điểm chuỗi** chỉ chặn mức điểm của riêng một ngày check-in, không phải trần cho tổng điểm trong ngày |
| `US13` | Từ bốn cửa kiểm còn **ba**. US này nay không có tham số cấu hình nào |
| `C9` | Chỉ còn áp cho biên ngày của check-in |

> ⚠️ **Đừng nhầm hai cái tên gần giống nhau.** *Trần điểm mỗi ngày* (bỏ) chặn tổng điểm một học viên nhận trong ngày. *Trần điểm chuỗi* (giữ, `BR-8.5c`) chặn mức điểm cao nhất của một lần check-in khi chuỗi dài ra.

### Rủi ro phải nêu

`OQ-A2` ngày 23/09 chốt **không làm chống cày riêng cho hoạt động chỉ có Text/Ảnh**, với lý do *"chống cộng trùng (`C5`) và trần điểm/ngày (`S8`) vẫn áp cho mọi loại"*. Bỏ trần ngày thì **một trong hai lớp phòng vệ đó mất**.

Hoạt động chỉ có Text hoặc Ảnh hoàn thành ngay khi mở hiển thị (`KB-LX-03b`). Học viên bấm qua 50 hoạt động như vậy trong mười phút thì nhận đủ 50 lần điểm, và chống cộng trùng **không chặn được** vì mỗi hoạt động là một nội dung khác nhau.

Lớp còn lại: hoạt động chứa Video phải xem đủ **80% thời lượng** (`KB-LX-03a`) nên không bấm qua được. Rủi ro chỉ nằm ở hoạt động thuần Text/Ảnh.

PO chấp nhận.

## 2. Làm rõ logic lên hạng

`BR-10.2` giữ nguyên cơ chế nhưng **đổi cách diễn đạt**. Chữ *"các tiêu chí cộng dồn với nhau"* gây hiểu nhầm thành phải gộp ba chỉ số lại rồi mới tính.

Cách viết mới: **mỗi lần bất kỳ tiêu chí nào chạm thêm một mốc, học viên lên một hạng ngay lúc đó.** Tiêu chí nào chạm trước thì lên trước.

PO xác nhận phương án **A** sau khi so hai cách tính trên cùng một ví dụ:

| | Cách A *(chọn)* | Cách B *(loại)* |
|---|---|---|
| Quy tắc | Đếm mọi mốc đã chạm của cả ba tiêu chí | Chỉ lấy tiêu chí có nhiều mốc nhất |
| `9.000` điểm · `10` khoá · `5` huy hiệu | `1 + 3 + 2 + 1` = **hạng 7** | `1 + 3` = hạng 4 |

Lý do loại B: học viên chạm mốc ở tiêu chí không dẫn đầu thì hạng đứng im, nên hai trong ba tiêu chí gần như không có tác dụng, và các công tắc bật tắt từng tiêu chí ở `US10` mất ý nghĩa.

`BR-10.2` nay có **ví dụ theo dòng thời gian** sáu tháng thay cho phép tính gộp, để người đọc thấy hạng lên dần theo từng mốc chạm được.

---

# CR-011 — Trang cấu hình Ops tự lưu

## Nguyên văn PO

> *"Design thì tôi đang làm như này `Gamification - Enable - Setting.png`, muốn nhập xong là tự lưu chứ không có popup hay modal gì nên không có nút save, đổi lại giải pháp theo hướng này được không"*
>
> *"không giới hạn điểm nhập, ko giới hạn 100"*
>
> *"nếu tắt cấu hình badge hay point thì các phần cấu hình lên hạng do 2 phần này cũng tắt theo"*
>
> *"trong design ko cần chọn múi giờ, cái này cấu hình theo tenant rồi"*
>
> *"múi giờ theo tenant, BE sẽ thiết kế vào technical design sau, còn lại ok"*

## Trạng thái trước CR

PRD viết từ lúc bốn khối còn là bốn màn riêng: mỗi khối một nút lưu, sau khi lưu thì nhắc *"chỉ áp dụng từ bây giờ"*. TD-FE §7.4 thì đã chuyển sang **một nút Save chung** cho cả trang, kèm ba confirm modal khi gạt công tắc và cảnh báo khi rời trang chưa lưu. Hai tài liệu lệch nhau, và cả hai đều lệch với design.

## Hai điều chỉnh so với nguyên văn — PO đã đồng ý

| PO muốn | Điều chỉnh | Lý do |
|---|---|---|
| *"Nhập xong là tự lưu"* | **Lưu khi rời ô hoặc bấm Enter**, không lưu trong lúc gõ | Cấu hình có hiệu lực ngay và không tính lại quá khứ (`C4`). Đổi bội số lên hạng `3000` → `5000`, lưu lúc ô đang là `5` thì học viên được cộng điểm đúng lúc đó nhảy lên trần hạng, mà hạng không tụt (`BR-10.3`). Debounce cũng không cứu được vì người dùng hay dừng tay giữa chừng |
| *"Không có popup hay modal gì"* | **Giữ hai xác nhận**, dạng popover nhỏ cạnh công tắc: tắt `Gamification` · bật `Visibility in UpLMS` lần đầu | Tự lưu thì bấm nhầm có hiệu lực ngay. Tắt `Gamification` để lại khoảng trống dữ liệu không tính bù (`BR-14.5`). Bật `Visibility` lần đầu là thời điểm ra mắt cho toàn bộ học viên (`BR-14.4`). Cả hai gần như chỉ xảy ra một lần nên hỏi lại không gây phiền |

## Rule mới

| # | Rule | Mã |
|---|---|---|
| 1 | Trang tự lưu, không có nút lưu. Ô nhập lưu khi rời ô hoặc Enter, công tắc lưu khi bấm, hình lưu khi tải lên xong | `BR-14.10` |
| 2 | Giá trị không hợp lệ thì không lưu, báo lỗi tại ô. Rời trang khi ô đang lỗi thì ô về giá trị đã lưu | `BR-14.11` |
| 3 | Lưu xong báo nhỏ `Saved`. Lưu lỗi thì ô về giá trị cũ. Không có cảnh báo rời trang | `BR-14.12` |
| 4 | Chỉ hai xác nhận, dạng popover | `BR-14.13` |
| 5 | Nhắc *"chỉ áp dụng từ bây giờ"* thành **dòng cố định đầu khối**, không bật lên sau mỗi lần lưu | `US8` · `US10` |
| 6 | **Tắt `Points` hoặc `Badges` thì tiêu chí lên hạng tương ứng khoá theo.** Khoá giữ nguyên giá trị, bật lại thì chạy lại như cũ. Không hỏi lại, nêu hệ quả bằng dòng giải thích dưới công tắc | `BR-10.7` |
| 7 | "Chặn lưu" đổi thành **không tắt được tiêu chí hoặc bảng đang chạy cuối cùng**. Tắt chức năng nguồn mà không còn gì chạy thì vẫn cho tắt, khối hiện cảnh báo cố định | `BR-10.8` · `BR-11.5` |
| 8 | Số điểm **không giới hạn trên** | `BR-8.5` |
| 9 | **Múi giờ lấy theo tenant**, không có ô chọn trên màn Gamification. Cách lưu do BE quyết trong technical design | `BR-14.9` |
| 10 | Bỏ nhãn trạng thái tổng. Hai công tắc cùng dòng giải thích của `Visibility in UpLMS` đã đủ | `US14` |

## Lỗ hổng phát hiện khi phân tích — đã vá trong CR này

Trước CR, tắt `Badges` thì tiêu chí lên hạng theo huy hiệu bị khoá, nhưng khoá **không đổi giá trị** (TD-FE §7.3). Nếu đó là tiêu chí duy nhất đang bật thì `BR-10.8` vẫn coi là hợp lệ, trong khi thực tế không ai lên hạng được. `Leaderboard` có lỗ tương tự. Rule 7 vá bằng khái niệm **"đang chạy"** = bật và không bị khoá.

## Tác động

| Hạng mục | Thay đổi |
|---|---|
| `US1` | Panel `How to level up?` chỉ hiện tiêu chí **đang chạy**, không hiện tiêu chí bị khoá |
| `US5` · `US6` | Sửa tham chiếu tiền điều kiện: múi giờ lấy theo tenant, không còn *"khai ở `US14`"* |
| `US8` | Bỏ nút lưu và nhắc sau lưu. Bỏ giới hạn trên. Thêm dòng giải thích dưới công tắc `Points` |
| `US9` | Bỏ nút lưu. Thêm dòng giải thích dưới công tắc `Badges` |
| `US10` | Viết lại `BR-10.7` và `BR-10.8`. Tiêu chí `Points` khoá khi chức năng điểm tắt |
| `US11` | Viết lại `BR-11.5` |
| `US14` | Thêm `BR-14.10` đến `BR-14.13`. Bỏ ô chọn múi giờ, bỏ nhãn trạng thái. Hai cảnh báo thành popover |
| Database · API | Bảng `tenant` từ **Sửa** thành **Đọc**. Endpoint `settings` bỏ múi giờ |
| TD-FE | Sửa §7.1 · §7.2 · §7.3. **Cơ chế lưu ở §2.2 · §4.2 · §7.4 · §7.5 để Dev tự cập nhật**, PRD chỉ ghi hai điều phải đúng — theo ranh giới PO với Dev |
| `OQ-08` · `OQ-36` | Cập nhật theo quyết định mới |

## Rủi ro PO chấp nhận

| # | Rủi ro | Vì sao |
|---|---|---|
| 1 | Không giới hạn trên mà lại tự lưu: gõ nhầm `1500` thay vì `150` cũng có hiệu lực ngay | Điểm đã cộng theo số nhầm không tính lại, theo `C4` |
| 2 | Không có nút lưu nên không có bước *"xem lại trước khi lưu"* | Mỗi ô có hiệu lực ngay khi rời ô |

---

# CR-012 — Bảng xếp hạng theo huy hiệu chỉ còn ở All time, thêm bảng Activities

## Nguyên văn PO

> *"viết lại câu này, để vận hành và học viên hiểu là checkin mỗi ngày chứ không phải login, vì ngày thứ 2 nếu chưa bị logout mà vào lại hệ thống thì vẫn được tính là checkin chứ không phải logout ra login lại mới tính"*
>
> *"huy hiệu cũng là tích lũy nên chắc không đưa vào leaderboard được, vì nếu trong cùng 1 khoảng thời gian thì huy hiệu newbie dễ đạt hơn lên granmaster, tôi nghĩ nên bỏ huy hiệu trong leaderboard mà thay bằng activity"*
>
> *"giữ badges cho all time, khi filter khoảng ngày thì level và huy hiệu ko có"*
>
> *"bổ sung activties trong leaderboard"*

## Phân tích

**Đếm huy hiệu trong một khoảng ngày đo độ mới, không đo độ chăm.** Mốc tăng gấp đôi nên người mới qua mốc liên tục, người cũ cả tháng không qua mốc nào. Ví dụ với `Activity badges` trong một tháng: người mới làm 30 hoạt động nhận 2 huy hiệu (mốc 10, 25), người cũ đang ở 420 làm 300 hoạt động nhận 0 (mốc kế là 800).

**Bảng `Activities` có giá trị riêng, không trùng `Points`.** Với cấu hình mặc định, bảng `Points` nghiêng về check-in: vào đủ 30 ngày không học gì được `1.095` điểm, cao hơn người chỉ vào ngày thường mà hoàn thành 60 hoạt động (khoảng `1.025`). `Activities` là bảng duy nhất đo thuần việc học theo khoảng ngày với độ phân giải đủ dùng.

## Đề xuất — chờ PO confirm

| # | Nội dung |
|---|---|
| 1 | Năm bảng. Theo khoảng ngày: `Points` · `Activities` · `Courses`. Chỉ ở `All time`: `Level` · `Badges`. Thêm công tắc `Show activities` ở `US11` |
| 2 | `US12`: chọn khoảng ngày thì ẩn cột `Level` và `Badges`, thêm cột `Activities` |
| 3 | Xoá `BR-6.14` — rule cũ còn sót, mâu thuẫn với `BR-6.2b` và `OQ-29` |
| 4 | Đếm số khoá hoàn thành từ dữ liệu học, không từ sổ giao dịch điểm. Hiện `BR-11.4` nói bảng `Courses` không phụ thuộc chức năng nào, nhưng định nghĩa chỉ số lại đếm từ sổ điểm — tắt `Points` thì bảng đứng im |
| 5 | Câu chữ check-in: học viên `for visiting UpLMS each day, +5 for each day in a row, up to 40` · Ops `Award points once a day when users first visit, even if they're still signed in from before. Each day in a row adds 5 more, up to 40 on day 7.` · mốc huy hiệu `Awarded at ... check-in days`. Ba dòng mốc còn lại đổi `every` thành `at` |
| 6 | `BR-5.1`: chỉ tính khi học viên **chủ động mở hoặc quay lại** UpLMS. Request nền tự chạy không tính, để người treo tab qua đêm không tự giữ chuỗi |

## Rủi ro cần PO chấp nhận

| # | Rủi ro | Vì sao |
|---|---|---|
| 1 | Bảng `Activities` biến việc bấm lướt hoạt động chỉ có chữ hoặc ảnh thành cách nhanh nhất để lên top | Rủi ro đã chấp nhận ở `CR-010`, nay có thêm động cơ trực tiếp. Hoạt động chứa video không bị vì phải xem đủ 80% |
| 2 | Hoạt động to nhỏ khác nhau đều tính là 1 | Học viên được giao khoá chia nhiều hoạt động nhỏ có lợi |

## Điểm re-entry đề xuất

**PRD.** Đổi chi tiết chức năng, không đổi phạm vi. PO chọn gộp với `CR-013` và chạy từ BRD.

## ⚠️ Chỉnh điểm 4 khi áp vào PRD — PO cần xác nhận lại

Đề xuất gốc *"đếm số khoá từ dữ liệu học"* có lỗ: dữ liệu học ghi cả những lần hoàn thành **trong lúc `Gamification` tắt**, đếm từ đó là trái `BR-14.5` (tắt hẳn thì không ghi gì, bật lại không tính bù).

PRD v0.10 viết thành **yêu cầu**, không chỉ nguồn dữ liệu: mọi chỉ số đếm (số ngày có mặt · số hoạt động · số bài Test · số khoá) **đếm mọi lần xảy ra trong lúc `Gamification` bật, không phụ thuộc công tắc `Points` hay từng hành động**. Cách lấy dữ liệu do Dev quyết.

Mở rộng sang số hoạt động và số bài Test vì cùng một lỗi: trước đây `US4` đếm cả hai từ sổ giao dịch điểm, nên tắt `Points` thì tiến độ huy hiệu và bảng `Activities` cũng đứng im.

---

# CR-013 — Campaign trở lại, học viên bỏ khoảng ngày tự do

## Nguyên văn PO

> *"leaderboard ngoài LMS chỉ có filter các khung cố định như this week, this month, this quater, this year, không cho chọn khoảng, để tránh user spam hệ thống tính toán nhiều, đây là lỗ hổng bảo mật"*
>
> *"để giải quyết bài toán này thì sẽ bổ sung thêm chức năng campaign, khi tạo campaign sẽ chọn được diễn ra trong khoảng nào, cấu phần tạo nên camp đó bào gồm point và activities, với point thì setting tương tự như gamification, nhưng chỉnh số được số point cho mỗi loại hành động tùy thuộc vào camp đó"*
>
> *"theo quy trình change request đi, chỉ có thay đổi một chút là phần point trong camp sẽ chỉ được chọn loại hành động nào thôi chứ không được sửa số point, số point theo cấu hình chung cả gamification"*

## Trạng thái trước CR

`CR-007` bỏ chiến dịch, kỳ lịch và cơ chế chốt kỳ, thay bằng **bộ chọn khoảng ngày tự do** trên bảng xếp hạng. Lý do lúc đó: khoảng ngày tự do bao trùm cả kỳ lịch lẫn chiến dịch.

CR này bỏ bộ chọn tự do phía học viên, nên tiền đề của `CR-007` không còn. Campaign quay lại để lấp đúng chỗ đó: **những khoảng thời gian có chủ đích** mà khung cố định không diễn tả được.

## Rule mới đã rõ

| # | Rule |
|---|---|
| 1 | Bảng xếp hạng phía học viên chỉ có `All time` · `This week` · `This month` · `This quarter` · `This year`. Không có bộ chọn khoảng tự do. Mọi khung đều tính sẵn, nên học viên gọi bao nhiêu lần cũng chỉ là đọc |
| 2 | Tạo campaign: chọn **khoảng thời gian** diễn ra |
| 3 | Campaign gồm hai cấu phần: **điểm** và **số hoạt động** |
| 4 | Phần điểm: vận hành **chỉ chọn loại hành động nào được tính**. **Số điểm theo cấu hình chung**, không sửa riêng cho campaign |

## Hệ quả của rule 4 — campaign đơn giản đi nhiều

Điểm campaign **không phải một loại điểm mới**. Nó là điểm chung, lọc theo hai điều kiện: thời điểm nằm trong khoảng campaign, và loại hành động được chọn. Sổ giao dịch điểm đã lưu từng lần cộng kèm nguồn và thời điểm (`C3`), nên **không cần ghi thêm gì** khi học viên hành động.

Kéo theo:
- **Hai campaign chồng thời gian không xung đột**, vì chỉ là hai cách lọc khác nhau trên cùng một sổ
- **Campaign phụ thuộc cấu hình chung.** Tắt `Points`, hoặc tắt một hành động, thì phần đó ngừng đóng góp cho mọi campaign đang chạy
- **Đổi số điểm chung giữa chừng thì campaign mang hai mức điểm**, theo `C4`. Học viên hành động trước và sau thời điểm đổi nhận số điểm khác nhau trong cùng một campaign

## Câu hỏi còn mở — chặn BRD

| # | Câu hỏi | Đề xuất |
|---|---|---|
| 1 | Campaign xếp hạng thế nào: **hai bảng** (điểm và hoạt động) hay vận hành **chọn một** chỉ số? | Hai bảng, giống cấu trúc bảng xếp hạng chung |
| 2 | Ai tham gia? | Toàn tổ chức ở đợt này. Chọn theo nhóm chờ chức năng nhóm từ HRM |
| 3 | Kết thúc thì **đóng băng** kết quả không? Bài nộp trong campaign mà chấm sau khi kết thúc có tính không? | Đóng băng. Campaign làm ra để trao thưởng, số liệu sống (`BR-6.10`) sẽ làm thứ hạng đổi sau khi đã công bố |
| 4 | Campaign đang chạy sửa được gì? | Theo `CR-002`: không sửa khoảng thời gian và loại hành động, chỉ sửa tên và mô tả |
| 5 | Màn danh sách học viên bên Ops (`US12`) có giữ bộ chọn khoảng ngày tự do không? | Giữ. Mục tiêu `O4` đang dựa vào nó, người dùng Ops ít và có phân quyền |

## Điểm re-entry đề xuất

**BRD.** Campaign đưa một thực thể bị loại ở `CR-007` trở lại phạm vi, đổi mục `Out of scope` và cách đạt mục tiêu `O4`.

## PO trả lời — 08/10/2026

> *"5 câu chặn đều theo đề xuất"*

Kèm bốn lựa chọn qua câu hỏi chốt:

| Câu hỏi | PO chọn |
|---|---|
| Re-entry | **Gộp `CR-012` với `CR-013`, chạy từ BRD.** Cả bốn Gate duyệt lại |
| Bài nộp trong campaign mà chấm sau khi kết thúc | **Tính theo lúc chấm đạt.** Chỉ tính nếu được chấm đạt trong thời gian campaign. Kết quả đóng băng ngay khi kết thúc |
| Đổi số điểm chung khi campaign đang chạy | **Chấp nhận hai mức điểm** trong cùng một campaign, theo `C4` |
| `CR-012` | **Đồng ý cả sáu điểm**, chấp nhận hai rủi ro của bảng `Activities` |

### Chốt cuối

| # | Rule |
|---|---|
| 1 | Campaign có **hai bảng**: điểm (chỉ các loại hành động được chọn) và số hoạt động |
| 2 | Người tham gia: **toàn tổ chức** |
| 3 | Kết thúc thì **đóng băng**. Một lần cộng điểm thuộc campaign khi **thời điểm cộng** nằm trong khoảng campaign. Bài chấm sau khi kết thúc không tính |
| 4 | Đang chạy: **chỉ sửa tên và mô tả**. Không sửa khoảng thời gian và loại hành động |
| 5 | `US12` bên Ops **giữ bộ chọn khoảng ngày tự do** |
| 6 | Hai campaign được chồng thời gian |
| 7 | Học viên **xem lại được campaign đã kết thúc**, thấy kết quả đã đóng băng |
| 8 | Ops có **màn xem và xuất Excel kết quả từng campaign**. Không dùng `US12` thay được vì `US12` không lọc theo loại hành động và là số liệu sống |
| 9 | **Chỉ xoá được khi chưa bắt đầu.** Đang chạy thì không dừng, không xoá |
| 10 | Campaign nằm **trong trang bảng xếp hạng**. Tắt công tắc `Leaderboard` thì campaign ẩn theo, dữ liệu giữ nguyên |

### Mặc định Claude đặt, chưa hỏi PO — duyệt ở Gate

| # | Mặc định | Lý do |
|---|---|---|
| a | Khoảng campaign tính **theo ngày trọn**, biên ngày cắt theo múi giờ tổ chức | Cùng quy tắc với khung cố định (`C6`) |
| b | **Ngày bắt đầu không được ở quá khứ** | Campaign tính hồi tố thì học viên không biết mình đang thi đua |
| c | Phải chọn **ít nhất một loại hành động** | Không chọn gì thì bảng điểm rỗng |
| d | **Không thông báo** khi campaign bắt đầu hay kết thúc | Thông báo hiện chỉ dành cho thành tích (`S10`) |
| e | Học viên bị `Block` hoặc rời tổ chức **vẫn nằm trong kết quả đã đóng băng** | Theo `A14` đã chốt cho snapshot |

