# Open Questions — Report Phase 1

**Ngày:** 06/10/2026
**Nguồn:** `working/ai-drafts/clarified-requirements-20261006.md`

`Blocks = Yes` nghĩa là thiếu câu trả lời thì không viết BRD được.

Mỗi câu có sẵn lựa chọn và đề xuất. Đồng ý với đề xuất thì chỉ cần trả lời *"theo đề xuất"*.

---

## Nhóm A — chặn BRD

| # | Câu hỏi | Vì sao quan trọng | Owner | Blocks |
|---|---|---|---|---|
| `OQ-01` | Phase 1 gồm những gì, *"báo cáo"* có gồm xuất tệp, xem quá khứ, gửi định kỳ không | Quyết định số US và có phải lưu số liệu theo thời gian không | PO | Yes |
| `OQ-02` | Chiều nhóm/quản lý xử lý thế nào với Group `US16` · `US18` | Hai PRD đặc tả cùng một màn | PO | Yes |
| `OQ-03` | Kỹ năng và năng lực lấy từ đâu | Hệ thống chưa có khung năng lực | PO | Yes |
| `OQ-04` | *"Điểm và hạng"* là của Gamification hay điểm học tập | Dùng lại hay làm mới | PO | Yes |
| `OQ-05` | *"Việc cần làm hôm nay"* lấy từ đâu | Không có hạn theo Activity, danh sách dễ trống | PO | Yes |
| `OQ-06` | Định nghĩa *chưa bắt đầu*, *chậm*, *quá hạn* | Business rule cốt lõi, Group cũng đang thiếu | PO | Yes |
| `OQ-07` | *"Lớp có vấn đề"* gồm dấu hiệu nào | Business rule cốt lõi của chiều lớp học | PO | Yes |
| `OQ-08` | Ai xem chiều khoá học và lớp học, phạm vi tới đâu | Phân quyền, KB chưa phủ | PO | Yes |
| `OQ-09` | *"Hàng chờ duyệt"* là hàng nào | Chỉ số hay chức năng mới | PO | Yes |
| `OQ-10` | *"Buổi chưa xếp lịch"* và mảng lịch dạy có thuộc phạm vi không | Vùng KB chưa phủ | PO | Yes |
| `OQ-11` | Quản lý *"xử lý"* gì từ danh sách người | Gửi nhắc là chức năng mới | PO | Yes |
| `OQ-12` | Vấn đề gốc là gì | Phần Problem của BRD, căn cứ để cắt Phase 1 | PO | Yes |

Chi tiết từng câu, kèm lựa chọn và đề xuất:

### `OQ-01` — Phase 1 gồm những gì, và "báo cáo" khác "dashboard" ở đâu

**Câu hỏi.**
1. Bảng bốn chiều là **toàn bộ** Phase 1, hay là bức tranh chung để từ đó cắt ra Phase 1?
2. Ngoài dashboard xem trên màn hình, *"báo cáo"* có gồm thứ nào dưới đây không?

| | Thứ | Đang có ở đâu |
|---|---|---|
| a | Xuất ra tệp | Group `US16` · `US18` đều loại. Gamification `US12` *(danh sách học viên và hạng bên Ops)* có xuất Excel |
| b | Xem lại số liệu tại một mốc quá khứ | Group `US18` có, cho số liệu theo nhóm |
| c | Xu hướng theo thời gian, ví dụ tháng này so với tháng trước | Dashboard khoá học phía học viên chỉ so tuần này với tuần liền trước *(KB `07` §5)* |
| d | Gửi định kỳ qua email | Group `US18` loại |

**Vì sao quan trọng.** Mỗi thứ là một nhóm US riêng. Thứ b và c còn đòi lưu số liệu theo thời gian, nặng hơn hẳn việc chỉ đọc trạng thái hiện tại.

**Đề xuất.** Phase 1 làm dashboard **trạng thái hiện tại** kèm lối bấm sang danh sách. Cắt theo phụ thuộc như `clarified-requirements` §8: khoá học, lớp học, người học trước; chiều nhóm/quản lý đi cùng hoặc ngay sau Group. Bốn thứ a b c d để phase sau, trừ khi đang có người cần ngay — nếu có thì cho biết ai cần cái nào.

**Blocks:** Yes

---

### `OQ-02` — Chiều nhóm/quản lý xử lý thế nào với dự án Group

**Câu hỏi.** Group `US16` *(quản lý xem danh sách người mình phụ trách)* và `US18` *(báo cáo cộng dồn theo nhóm)* đã duyệt ngày 06/10. Chọn một:

| | Cách |
|---|---|
| a | Report nhận lại màn của `US16` và toàn bộ `US18`. Group chỉ giữ dữ liệu nhóm, quan hệ quản lý và luật. **Cần change request bên Group** |
| **b** ⭐ | Report **mở rộng trên nền** màn của Group: thêm *chậm*, *chưa bắt đầu*, khối chỉ số, bộ lọc ứng với từng chỉ số. Dùng nguyên văn luật của Group |
| c | Bỏ chiều này khỏi Report, để Group lo |

**Vì sao quan trọng.** Hai PRD cùng đặc tả một màn thì Dev không biết theo bản nào.

**Đề xuất: b.** Chiều nhóm của Report vốn phải chờ Group xây xong nhóm và quan hệ quản lý mới chạy được, nên làm sau Group là tự nhiên. Không phải mở lại một PRD vừa duyệt. Bảng so sánh đầy đủ: `clarified-requirements` §4.1.

**Blocks:** Yes

---

### `OQ-03` — Kỹ năng và năng lực lấy từ đâu

**Câu hỏi.** *"Kỹ năng vừa đạt và còn thiếu"* và *"nhóm thiếu năng lực nào nhiều nhất"* cần biết ba thứ: năng lực là gì, thế nào là đạt, **thiếu so với cái gì**. Hệ thống chưa có khung năng lực. Chọn một:

| | Nguồn | Trả lời được "thiếu" theo nghĩa nào |
|---|---|---|
| a | **Learning Outcome** cấp Section — đạt khi hoàn thành các Activity gắn với outcome đó | Chỉ thiếu so với khoá đã được giao. Gần như trùng với *"tiến độ đang dở"* |
| b | **Chủ đề câu hỏi** trong bài Test — đạt khi tỉ lệ đúng theo chủ đề vượt ngưỡng | Chỉ với chủ đề đã làm bài. Không biết người này cần chủ đề nào |
| c | **Dựng khung năng lực mới** | Đầy đủ — nhưng là một dự án riêng cỡ L |
| **d** ⭐ | **Để sang phase sau** | — |

**Vì sao quan trọng.** KB `15` §8 câu Q3 còn bỏ ngỏ *"ba bảng outcome có phải nền của lớp năng lực không"*. Chọn a là chốt ngầm câu hỏi chiến lược đó trong một dự án báo cáo.

**Đề xuất: d.** Nếu muốn có tín hiệu ngay ở Phase 1 thì chọn b, nhưng trên giao diện gọi là *"kết quả theo chủ đề"*, không gọi là *"năng lực"*.

**Blocks:** Yes

---

### `OQ-04` — "Điểm và hạng" là của Gamification hay là điểm học tập

**Câu hỏi.** Chọn một:

| | Nghĩa | Hệ quả |
|---|---|---|
| a | **Điểm và hạng của Gamification** | Dùng lại khối điểm và hạng mà Gamification `US1` *(Trang Thành tích của tôi)* đã đặt trên My Learning. Khối ẩn khi tắt công tắc `Gamification` hoặc `Visibility in UpLMS` *(Gamification `BR-1.1`)* |
| b | **Điểm học tập** *(điểm khoá, điểm bài Test)* và **thứ hạng trong lớp** | Khái niệm mới. Thêm một quyết định: học viên có thấy thứ hạng của người khác không |

**Blocks:** Yes

---

### `OQ-05` — "Việc cần làm hôm nay" lấy từ đâu

**Câu hỏi.** Hệ thống **không có hạn theo từng Activity**. Hạn chỉ có ở cấp khoá *(thời hạn lượt ghi danh)* và ở bài kiểm tra có cửa sổ mở/đóng *(`KB-MAIL-07`)*. Nên nếu *"việc hôm nay"* chỉ gồm thứ đến hạn hôm nay, **phần lớn ngày danh sách sẽ trống**. Chọn một:

| | Cách | Gồm |
|---|---|---|
| a | **Chỉ thứ có mốc rơi vào hôm nay** | Bài kiểm tra mở hoặc đóng hôm nay · khoá hết hạn hôm nay · buổi học hôm nay *(chỉ khi mảng lịch dạy thuộc phạm vi — `OQ-10`)* |
| **b** ⭐ | **a, cộng phần theo nhịp** | Với mỗi khoá có hạn: phần còn lại chia cho số ngày còn lại, ra lượng nên học hôm nay để kịp hạn |

Và một câu phụ: **khoá linh động chưa Activate** có hiện thành việc *"Bắt đầu khoá X"* không? Bấm Activate là bắt đầu đếm ngược N ngày *(`KB-LX-02`)*. Nhắc bắt đầu mọi khoá linh động cùng lúc có thể khiến học viên kích hoạt hàng loạt rồi để hết hạn.

**Vì sao quan trọng.** Đây là khối chính của chiều người học, và nhắm thẳng vào con số *45% đăng nhập mà không bắt đầu*.

**Đề xuất: b.** Cách a trống phần lớn ngày. Cách b dùng chung phép tính nhịp với định nghĩa *"chậm"* ở `OQ-06`, nên định nghĩa một lần, dùng hai chỗ. Câu phụ thì PO quyết.

**Blocks:** Yes

---

### `OQ-06` — Trạng thái học của một lượt ghi danh

**Câu hỏi.** Báo cáo cần ba chữ *chưa bắt đầu*, *chậm*, *quá hạn*. Group cũng dùng *quá hạn* và *chưa bắt đầu* ở `US16` · `US18`, nhưng **không định nghĩa ở đâu**. Đề xuất định nghĩa một lần ở đây, Group dùng lại:

| Trạng thái | Định nghĩa đề xuất |
|---|---|
| **Chưa bắt đầu** | Chưa học hoạt động nào. Cùng mốc với `KB-LX-08` *(đã học ít nhất một hoạt động thì không huỷ ghi danh được nữa)*. Khoá linh động chưa Activate cũng thuộc trạng thái này |
| **Đúng nhịp** | Đã bắt đầu, chưa hết hạn, không chậm |
| **Chậm** | Đã bắt đầu, chưa hết hạn, và **tiến độ thấp hơn phần thời hạn đã trôi qua** quá một khoảng. Ví dụ đã qua 60% thời hạn mà mới xong 30%. Khoảng chênh mặc định `[đề xuất]` **20 điểm phần trăm**, cấu hình theo tổ chức |
| **Quá hạn** | Đã hết hạn mà chưa hoàn thành. Tính theo **thời hạn riêng của học viên** nếu có *(KB `04` §3: thời hạn riêng có thể dài hoặc ngắn hơn thời hạn lớp)* |
| **Hoàn thành** | Theo cách hệ thống đang tính, không đổi |

Hai luật đi kèm:

1. **Mỗi lượt ghi danh thuộc đúng một trạng thái**, để các con số cộng lại bằng tổng. Một người có nhiều lượt ghi danh thì có thể xuất hiện ở nhiều ô.
2. **Hết hạn mà chưa học gì thì tính *quá hạn*, không tính *chưa bắt đầu*.** Lúc đó việc phải làm là quyết gia hạn hay cho trượt, không còn là nhắc — đúng lập luận Group đã dùng khi tách hai chỉ số ở `US18`.

Và một câu phụ: hệ thống có trường hợp **học xong mà chưa đạt** *(mail #27 báo kết quả khoá học chưa đạt)*. **Tỉ lệ hoàn thành có tính người chưa đạt không?**

Còn một cách định nghĩa *chậm* khác: **không học hoạt động nào trong N ngày**. Không đề xuất, vì cách này đo sự vắng mặt chứ không đo chậm — người dồn học cuối tuần mà vẫn kịp hạn thì không nên bị gọi là chậm.

**Vì sao quan trọng.** Đây là business rule cốt lõi của chiều nhóm và chiều lớp. Định nghĩa lệch giữa hai dự án thì quản lý thấy một số ở màn Group, một số khác ở màn Report.

**Đề xuất:** bảng trên. Chốt xong nên ghi vào KB để mọi dự án sau dùng chung — việc này cần PO đồng ý.

**Blocks:** Yes

---

### `OQ-07` — "Lớp có vấn đề" gồm dấu hiệu nào

**Câu hỏi.** Chọn các dấu hiệu:

| # | Dấu hiệu | Dữ liệu |
|---|---|---|
| 1 | Tỉ lệ học viên **quá hạn** vượt ngưỡng | Đã có — theo `OQ-06` |
| 2 | Tỉ lệ học viên **chưa bắt đầu** vượt ngưỡng sau N ngày kể từ khi lớp bắt đầu | Đã có |
| 3 | Tỉ lệ học viên **chậm** vượt ngưỡng | Đã có — theo `OQ-06` |
| 4 | **Bài chờ chấm tồn quá N ngày** | Đã có — Grading List có thời điểm nộp bài *(KB `05` §3)* |
| 5 | **Lớp đang có học viên mà chưa có mentor nào** | Đã có *(KB `04` §7)* |
| 6 | **Chuyên cần** dưới ngưỡng | Ngưỡng 70% đang đóng cứng *(`KB-SIS-05`)*. Dashboard chuyên cần chưa rõ còn dùng *(KB `11` §1)*. Dữ liệu điểm danh thuộc mảng lịch dạy |
| 7 | **Còn buổi chưa xếp lịch** | Mảng lịch dạy, KB chưa phủ — `OQ-10` |

**Đề xuất:** dấu hiệu **1 đến 5** cho Phase 1 — dữ liệu đã có và mỗi dấu hiệu chỉ rõ ai phải xử lý. Dấu hiệu 6 và 7 chờ `OQ-10`. Mỗi lớp trong danh sách hiện **dấu hiệu nào đã bật**, không chỉ một nhãn *"có vấn đề"*. Ngưỡng mặc định đề xuất ở bước Field Intake, cấu hình theo tổ chức.

**Blocks:** Yes

---

### `OQ-08` — Ai xem chiều khoá học và chiều lớp học, phạm vi tới đâu

**Câu hỏi.** Hai chiều này nằm bên Ops. Chọn một:

| | Cách |
|---|---|
| a | Người có vai trò vận hành thấy **toàn bộ** khoá và lớp của tổ chức |
| b | **Theo phụ trách:** mentor thấy lớp mình, người phụ trách khoá thấy khoá mình |
| c | **Cả hai:** vai trò vận hành thấy toàn bộ, mentor thấy phần mình |

Và một câu phụ: **khoá học có "người phụ trách" không?** KB không ghi khái niệm này. Nếu không có thì cách b chỉ áp được cho lớp.

**Vì sao quan trọng.** Đây là phân quyền. KB chưa phủ vùng phân quyền, và Group đã đặt nguyên tắc *mỗi màn khai rõ nó đọc theo phạm vi nào* *(`BR-16.4`)*.

**Đề xuất: c.** Hiện chấm điểm đã chạy theo kiểu này: mentor chỉ xem bài được giao, mentor chính xem toàn lớp *(`KB-GRAD-03`)*.

**Blocks:** Yes

---

### `OQ-09` — "Hàng chờ duyệt" là hàng nào

**Câu hỏi.** Trong hệ thống có những luồng chờ người duyệt sau. *"Hàng chờ duyệt"* là cái nào?

| | Luồng | Ghi chú |
|---|---|---|
| a | Kết quả chấm **chờ mentor chính review** trước khi gửi học viên | KB `05` §5 |
| b | **Yêu cầu chấm lại** từ học viên | KB `05` §5 · `KB-GRAD-11` *(bắt buộc nhập lý do)* |
| c | Đơn trong mảng lịch dạy: xin dạy, xin nghỉ, đổi chế độ dạy | KB chưa phủ |
| d | Một luồng duyệt **chưa có trong hệ thống**, ví dụ duyệt nội dung khoá trước khi Publish | Nếu là d thì đây là một chức năng mới, không còn là một chỉ số |

**Blocks:** Yes

---

### `OQ-10` — "Buổi chưa xếp lịch" và mảng lịch dạy

**Câu hỏi.**
1. Mảng lịch dạy *(buổi học, giáo viên, phòng học)* có thuộc phạm vi dự án này không?
2. Nếu có, *"buổi chưa xếp lịch"* nghĩa là gì: lớp có số buổi dự kiến mà chưa đặt ngày giờ, chưa có phòng, hay chưa có giáo viên?

**Vì sao quan trọng.** KB chưa phủ mảng này *(KB `14` §2.1)*. Nếu thuộc phạm vi thì phải đọc lại nguồn và bổ sung KB trước Bước 5.

**Đề xuất.** Chỉ đưa vào khi mảng này **đang được dùng thật**. Hệ thống này đã sáu lần có endpoint mà không có tính năng *(KB `14` §2.2)*, nên đừng dựng chỉ số trên một vùng chưa biết còn sống hay không.

**Blocks:** Yes

---

### `OQ-11` — Quản lý "xử lý" gì từ danh sách người

**Câu hỏi.** Bấm chỉ số sang danh sách rồi, quản lý làm được gì ngay trên đó?

| | Cách |
|---|---|
| a | **Chỉ xem**, tự liên hệ ngoài hệ thống, ví dụ nhắn qua Lark |
| b | **Gửi nhắc** trong hệ thống cho một hoặc nhiều người |
| c | Khác |

Group `US16` đã loại: giao bài, sửa thời hạn học, xuất tệp.

**Vì sao quan trọng.** Cách b là một chức năng mới: 30 mail tự động hiện có không có mail nào cho việc này, và màn gửi thông báo thủ công đang ẩn *(KB `09` §1)*.

**Đề xuất: a** cho Phase 1. Cách b nên làm ở phase sau, vì nó khép được vòng *thấy → nhắc → theo dõi*, nhưng cần thêm một loại thông báo mới và luật chống nhắc dồn dập.

**Blocks:** Yes

---

### `OQ-12` — Vấn đề gốc

**Câu hỏi.** Yêu cầu nêu chỉ số, chưa nêu vấn đề. `clarified-requirements` §3 có bốn vấn đề AI suy ra, mỗi chiều một vấn đề. Đúng không, thiếu gì? Có số liệu minh hoạ thêm không — ví dụ bao nhiêu bài chờ chấm quá một tuần, bao nhiêu lớp kết thúc với tỉ lệ hoàn thành thấp?

**Vì sao quan trọng.** Đây là phần `Problem` và `Analytics` của BRD, và là căn cứ để chọn chỉ số nào cốt lõi khi cắt Phase 1.

**Blocks:** Yes

---

## Nhóm B — không chặn BRD, cần trước Bước 5 hoặc trước Field Intake

| # | Câu hỏi | Vì sao quan trọng | Đề xuất | Owner | Blocks |
|---|---|---|---|---|---|
| `OQ-13` | *"Câu hỏi chưa trả lời"* có phải là **bình luận gốc của học viên trong Thảo luận chưa được nhân sự hoặc nhóm Comment Replier phản hồi**? Học viên trả lời nhau có tính là đã trả lời không? | Quyết định con số đếm cái gì | Đúng như câu hỏi. Học viên trả lời nhau **không** tính là đã trả lời | PO | No |
| `OQ-14` | *"Sắp hết hạn"* là trong bao nhiêu ngày? | Ngưỡng mặc định khi tạo tổ chức | Mặc định **7 ngày**, cấu hình theo tổ chức. Áp cho cả thời hạn khoá và cửa sổ bài kiểm tra | PO | No |
| `OQ-15` | *"Nội dung đang chạy"* có phải là khoá có ít nhất một lớp đang diễn ra? Cần thêm danh sách trạng thái lớp chính thức: KB đang có hai hệ khái niệm — `DRAFT` · `PUBLIC` · `ENDED` và *đã bắt đầu / chưa bắt đầu* *(KB `04` §11 Q1)* | Không có trạng thái lớp chính thức thì không xác định được lớp nào đang diễn ra | Đúng như câu hỏi | PO | No |
| `OQ-16` | *"Tỷ lệ hoàn thành theo nội dung"* tính ở cấp khoá, hay xuống tới Section và Activity để thấy học viên bỏ dở ở đâu? | Độ chi tiết quyết định số màn | Cấp khoá, bấm vào thì xuống Section | PO | No |

---

## Giả định đang dùng — sai thì sửa

| # | Giả định | Căn cứ |
|---|---|---|
| `A-01` | `Test Account` không tính vào bất kỳ chỉ số nào | `KB-USER-TA-01` *(bỏ qua `Test Account` ở mọi logic nghiệp vụ)* · Group `BR-16.5` · `BR-18.4` · Gamification `C10` |
| `A-02` | Người nghỉ việc không hiện ở chế độ xem hiện tại | Group `BR-16.6` · `BR-18.5` |
| `A-03` | Mọi ngưỡng cấu hình theo tổ chức, không đóng cứng | `CLAUDE.md` · KB `15` §7 |
| `A-04` | *"Hôm nay"* cắt theo **múi giờ tổ chức**. Tham số này do Gamification thêm vào cấu hình tổ chức *(Gamification `C6` · `C9`: biên ngày cắt theo múi giờ tổ chức)*. Report làm trước Gamification thì Report phải tự thêm tham số này | Gamification `project-context.md` |
| `A-05` | Chiều người học và chiều nhóm/quản lý nằm ở **UpLMS**. Chiều khoá học và lớp học nằm ở **Ops** | Group: quản lý là một người dùng, màn `US16` nằm ở UpLMS |
| `A-06` | *"Nội dung"* hiện là khoá học. Lớp có thể gắn một lộ trình *(KB `16`)* nhưng lộ trình chưa có KB, nên các chỉ số phải mở rộng được sang lộ trình | KB `16` |
| `A-07` | Dashboard chỉ **đọc** dữ liệu đang có, không đổi cách tính tiến độ và điều kiện hoàn thành | `KB-LX-01` *(tiến độ = số Activity hoàn thành / tổng Activity)* · `KB-LX-03` *(điều kiện hoàn thành theo thứ tự Quiz → Video → Text/Ảnh)* |

---

## Trạng thái

| Nhóm | Trạng thái |
|---|---|
| A — `OQ-01` → `OQ-12` | 🔴 Mở. Chặn BRD |
| B — `OQ-13` → `OQ-16` | 🟡 Mở. Không chặn BRD |
| Giả định `A-01` → `A-07` | Chờ PO xác nhận cùng đợt |
