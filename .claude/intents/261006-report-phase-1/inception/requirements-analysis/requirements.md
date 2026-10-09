---
intent: 261006-report-phase-1
artifact: requirements
version: 0.1
status: draft
note: Bản làm rõ v1 ngày 2026-10-06, 24 requirement ứng viên, chờ PO trả lời 12 câu chặn
migrated-from: .claude/projects/Report-Phase-1/working/ai-drafts/clarified-requirements-20261006.md
---
# Làm rõ yêu cầu — Report Phase 1

**Ngày:** 06/10/2026 · **Phiên bản:** v0.1
**Input:** `working/raw-inputs/yeu-cau-goc-20261006.md` — 4 chiều, 16 chỉ số, 2 yêu cầu bấm sang danh sách
**Mục đích PO nêu:** *"xây dựng báo cáo và dashboard theo các chiều sau"*
**Đã đối chiếu:** KB `01` · `03` · `04` · `05` · `06` · `07` · `08` · `09` · `11` · `12` · `13` · `14` · `15` · `16` — cùng PRD Group v0.1 và PRD Gamification v0.8

---

## 1. Bốn phát hiện cần PO quyết trước khi đi tiếp

| # | Phát hiện | Vì sao chặn |
|---|---|---|
| 1 | **Chiều nhóm/quản lý trùng phần lớn với dự án Group.** `US16` của Group *(quản lý xem danh sách người mình phụ trách, sắp theo số khoá quá hạn)* và `US18` *(báo cáo cộng dồn theo nhóm, có số quá hạn và số chưa bắt đầu)* vừa được duyệt ngày 06/10 | Hai PRD đặc tả cùng một màn thì Dev không biết theo bản nào. Thêm nữa, Group dùng hai chữ *"quá hạn"* và *"chưa bắt đầu"* mà **chưa định nghĩa ở đâu** — xem §4.1 |
| 2 | **Hệ thống chưa có khái niệm năng lực.** *"Kỹ năng vừa đạt và còn thiếu"* và *"nhóm thiếu năng lực nào nhiều nhất"* cần một khung năng lực mà KB `15` ghi là *thiếu hoàn toàn* | Không có khung thì không tính được *"thiếu"* so với cái gì — xem §4.2 |
| 3 | **"Điểm và hạng" nhiều khả năng thuộc Gamification**, dự án đang chờ PO review PRD v0.8 | Nếu đúng thì đây là dùng lại, không phải làm mới, và chịu hai công tắc bật tắt của Gamification — xem §4.3 |
| 4 | **Hai chỉ số nằm ở vùng KB chưa phủ hoặc chưa rõ nghĩa.** *"Buổi chưa xếp lịch"* thuộc mảng lịch dạy, *"hàng chờ duyệt"* chưa rõ là luồng duyệt nào | KB không kết luận được, phải hỏi — xem §4.5 |

---

## 2. Chuẩn hoá input

| Nhóm | Nội dung | Nhãn |
|---|---|---|
| **Stakeholder request** | PO yêu cầu dựng báo cáo và dashboard theo 4 chiều: người học · nhóm/quản lý · khoá học · lớp học, tổng 16 chỉ số | `Fact` |
| **Problem** | *(chưa nêu)* Bốn vấn đề AI suy ra ở §3, chờ PO xác nhận | `Open Question` |
| **Expected outcome** | Mỗi người mở dashboard ra là biết **việc cần làm** hoặc **người, lớp cần xử lý**, và bấm từ con số sang thẳng danh sách để hành động | `[suy ra]` từ câu *"bấm được sang danh sách người để xử lý"* |
| **Users / roles** | Học viên · quản lý trực tiếp *(một người dùng, không phải vai trò — theo Group)* · người phụ trách khoá học · người phụ trách lớp. Hai vai sau **chưa rõ là ai** | `Fact` · `Open Question` |
| **Systems / modules** | UpLMS: trang người học, màn quản lý *(theo Group)* · UpLMS Ops: khoá, lớp, chấm điểm, Dashboard SIS · Thảo luận · Lịch dạy *(KB chưa phủ)* · Group · Gamification | `[suy ra]` |
| **Constraints** | Dữ liệu và hạ tầng cho đa tenant, nên mọi ngưỡng phải cấu hình được · `Test Account` không tính vào số liệu · phụ thuộc hai dự án chưa xây | `Fact` — `CLAUDE.md`, KB `15` §7, KB `06` §8b |
| **Proposed solution** | **Toàn bộ bảng là danh sách chỉ số, tức là giải pháp.** Chưa nói chỉ số phục vụ quyết định nào | `Recommendation` |

> ⚠️ Input mô tả **thứ cần hiện**, không nói **vì sao cần**. Không biết vấn đề thì không phân biệt được chỉ số nào cốt lõi và chỉ số nào có cũng được, mà đó chính là việc phải làm khi cắt *"Phase 1"*.
>
> Có một ý thiết kế rõ và nên giữ: **mỗi con số phải bấm được sang danh sách để xử lý.** Đây là dashboard để hành động, không phải báo cáo để đọc. Group đi cùng hướng này ở `US16`: *"quản lý nhìn danh sách để biết ai cần nhắc, không để đọc chi tiết"*.

---

## 3. Vấn đề gốc — AI suy ra, chờ PO xác nhận

| Chiều | Vấn đề suy ra | Dấu hiệu đang có | Nhãn |
|---|---|---|---|
| **Người học** | Vào hệ thống không biết việc gì cần làm trước, nên không bắt đầu hoặc bỏ dở | Số liệu General Launch 8/9–21/9/2026, trích từ Gamification: **45%** người đăng nhập không bắt đầu học *(53 vào, 29 bắt đầu)*, hoàn thành **64.1%** so với tiêu chí 80% | Số liệu là `Fact`. Quan hệ nhân quả là `Assumption` |
| **Nhóm / quản lý** | Quản lý không biết người mình phụ trách đang học thế nào | Problem đã duyệt của Group: *"Không có cách nào xem tiến độ học của riêng những người mình phụ trách"* | `Fact` — PRD Group |
| **Khoá học** | Việc tồn đọng không ai thấy cho tới khi có người phàn nàn | **8 mail chấm điểm đang tắt** *(`KB-MAIL-03`)*. Mentor không biết có bài mới cho tới khi tự mở màn Mark hoặc Grading List | `Assumption` |
| **Lớp học** | Không quét được toàn bộ lớp để biết lớp nào cần can thiệp | Dashboard SIS **bắt buộc chọn khoá và lớp, tối đa 4 lớp** *(`KB-SIS-01` · `KB-SIS-02`)*. Muốn tìm lớp có vấn đề phải mở lần lượt từng nhóm 4 lớp | `Assumption` |

→ `OQ-12`

---

## 4. Đối chiếu với thứ đã có và đang làm

### 4.1 Chiều nhóm/quản lý trùng với dự án Group

PRD Group v0.1 được PO duyệt và publish lên Lark ngày 06/10/2026. Hai US chạm thẳng vào chiều này:

| Chỉ số của Report | Group đã có | Chênh lệch |
|---|---|---|
| Ai quá hạn | `US16` cột *Số khoá quá hạn*, sắp xếp mặc định theo cột này · `US18` chỉ số *số quá hạn* | **Trùng** |
| Ai chưa bắt đầu | `US18` chỉ số *số chưa bắt đầu*, ở cấp nhóm bên Ops | Màn quản lý `US16` **chưa có** |
| Ai chậm | `US16` kịch bản viết *"sắp xếp sẵn theo ai đang chậm nhất"* nhưng thực tế sắp theo số khoá quá hạn. **Không có định nghĩa "chậm"** | **Mới** |
| Nhóm thiếu năng lực nào | Không có | **Mới**, phụ thuộc `OQ-03` |
| Bấm chỉ số sang danh sách người | `US16` **chính là danh sách người**, lọc được theo nhóm và theo có hay không khoá quá hạn | Thiếu bộ lọc ứng với từng chỉ số |

> ⚠️ **Group dùng *"quá hạn"* và *"chưa bắt đầu"* nhưng không định nghĩa ở đâu cả.** Đã rà toàn bộ PRD và `project-decisions.md` của Group. Report cần đúng hai định nghĩa này, cộng thêm *"chậm"*, nên **định nghĩa một lần ở Report, Group dùng lại** — xem `OQ-06`.

Group đã chốt sẵn những luật mà chiều này **phải dùng nguyên văn, không định nghĩa lại**:

| Mã | Nội dung |
|---|---|
| `BR-16.1` | Quản lý xem được người trong **toàn bộ nhánh** mình phụ trách, gồm cả nhóm con |
| `BR-16.2` | Xem được một người thì xem **toàn bộ** dữ liệu học của họ, kể cả khoá nhận qua nhánh khác |
| `BR-16.4` | Màn quản lý đọc theo **quan hệ quản lý**, không theo vai trò hệ thống |
| `BR-16.5` · `BR-18.4` | **Không tính tài khoản kiểm thử** |
| `BR-16.6` · `BR-18.5` | Chế độ xem hiện tại **loại người đã nghỉ việc** |
| `BR-18.1` · `BR-18.2` | Xem theo mốc quá khứ thì tính theo thành viên **tại mốc đó** |

**Ba cách xử lý** → `OQ-02`

| | Cách | Được | Mất |
|---|---|---|---|
| **a** | Report nhận lại màn của `US16` và toàn bộ `US18`. Group chỉ giữ dữ liệu nhóm, quan hệ quản lý và luật | Một màn một chủ. Mọi chỉ số định nghĩa ở một chỗ | **Mở lại PRD vừa duyệt** bằng change request. Phần việc của Group đang chờ Dev phải đợi Report |
| **b** ⭐ | Report **mở rộng trên nền** màn của Group: thêm *chậm*, *chưa bắt đầu*, khối chỉ số ở trên cùng, bộ lọc ứng với từng chỉ số. Dùng nguyên văn luật của Group | Không đụng PRD đã duyệt. Group làm trước, Report làm tiếp | PRD Report có những dòng *"Sửa"* trỏ vào màn định nghĩa ở PRD Group, người đọc phải mở cả hai |
| c | Bỏ chiều này khỏi Report, để Group lo | Gọn nhất | Phần mới — *chậm*, năng lực, khối chỉ số — không ai làm |

`Recommendation` — **cách b.** Chiều nhóm của Report vốn không chạy được trước khi Group xây xong nhóm và quan hệ quản lý *(Unit `U1` khung nhóm · `U4` quan hệ quản lý và mentor của Group)*, nên làm sau Group là thứ tự tự nhiên chứ không phải nhượng bộ. Cách a sạch hơn về lâu dài, nhưng phải đổi bằng việc mở lại một PRD vừa duyệt trong ngày.

### 4.2 Năng lực — hệ thống chưa có

KB `15` §5 đặt hệ thống hiện tại cạnh vòng tròn phát triển năng lực:

| Mắt xích | Hiện có |
|---|---|
| Vị trí yêu cầu năng lực gì | ❌ **Thiếu hoàn toàn.** Không có thực thể nào cho vị trí hay khung năng lực |
| Người này đang thiếu gì | ⚠️ Chỉ có mầm mống, chưa phải năng lực |
| Học cái gì thì lấp được | ⚠️ Ba bảng outcome, là hạ tầng sơ khai gần nhất |

Hai chỉ số của Report cần đủ ba thứ: năng lực là gì, thế nào là đạt, và **thiếu so với cái gì**. Thứ ba cần mắt xích đầu tiên, đúng mắt xích đang thiếu hoàn toàn.

Gamification cũng đã ghi *"Lộ trình học · Khung năng lực — tính năng riêng, làm sau"* vào Out of scope. KB `15` §8 xếp các câu hỏi về năng lực vào nhóm *"không giải quyết ở giai đoạn này"*.

Những thứ gần nhất đang có:

| Nguồn | Đang có gì | Trả lời được "đạt" không | Trả lời được "thiếu" không |
|---|---|---|---|
| **Learning Outcome** cấp Section *(KB `01` §3.3)* | Mỗi Section có một hoặc nhiều outcome, gắn được với Activity trong Section đó *(`BR-CONTENT-03` · `BR-CONTENT-04`)* | Có thể, ví dụ hoàn thành hết Activity gắn với outcome | Chỉ so với khoá đã được giao. Lúc đó *"còn thiếu"* gần như trùng với *"tiến độ đang dở"* |
| **Chủ đề câu hỏi** trong bài Test *(KB `03` §5)* | Kết quả bài thi đã chia theo chủ đề. Dashboard SIS thứ ba đang tính tỉ lệ ghi điểm theo chủ đề | Có, khi tỉ lệ đúng theo chủ đề vượt ngưỡng | Chỉ với chủ đề đã làm bài. Không biết người này **cần** chủ đề nào |
| **Khung năng lực dựng mới** | Không có | Có | Có — nhưng đây là một dự án riêng cỡ L |

→ `OQ-03`

`Recommendation` — **để sang phase sau**, trừ khi PO đã có sẵn nguồn năng lực. Nếu muốn có tín hiệu ngay ở Phase 1 thì dùng **kết quả theo chủ đề câu hỏi** và gọi đúng tên của nó, đừng gọi là *"năng lực"*.

Lý do: KB `15` §8 câu Q3 còn bỏ ngỏ *"ba bảng outcome có phải nền của lớp năng lực, hay sẽ dựng thực thể mới"*. Dùng outcome làm "năng lực" trong một dự án báo cáo là **chốt ngầm câu hỏi chiến lược đó** mà không ai quyết.

### 4.3 "Điểm và hạng" thuộc Gamification

PRD Gamification v0.8 *(05/10/2026, đang chờ PO review)* đã có:

| Mã | Nội dung |
|---|---|
| `US1` Trang Thành tích của tôi | Điểm tích luỹ · hạng hiện tại kèm tiến độ tới hạng kế tiếp · huy hiệu. **Có sẵn một khối điểm và hạng trên My Learning**, bấm vào sang trang này |
| `US7` Vị trí của tôi | Vị trí trên bảng xếp hạng, kèm vài người liền kề |
| `BR-1.1` | Trang chỉ tồn tại khi công tắc `Gamification` **và** `Visibility in UpLMS` đều bật |

Nếu *"điểm và hạng"* là của Gamification thì Report **dùng lại khối đó**, không định nghĩa lại điểm hay hạng, và khối phải ẩn theo hai công tắc trên.

Nếu là **điểm học tập** *(điểm khoá, điểm bài Test)* và **thứ hạng trong lớp** thì đó là khái niệm mới. Hệ thống chưa xếp hạng học viên trong lớp ở đâu cả, và cho học viên thấy thứ hạng của người khác là một quyết định riêng.

→ `OQ-04`

### 4.4 Dashboard SIS đang có

| | |
|---|---|
| Đang dùng | 3 dashboard: tiến độ học · phân phối điểm bài kiểm tra · tỉ lệ ghi điểm theo câu hỏi và chủ đề *(KB `11` §1)* |
| Ràng buộc | Bắt buộc chọn **khoá và lớp** *(`KB-SIS-01`)* · **tối đa 4 lớp**, mỗi lớp một biểu đồ *(`KB-SIS-02`)* · chỉ lấy khoá 4 level *(`KB-SIS-03`)* |
| Sắp bị sửa | Group `US18` sẽ **bỏ ràng buộc bắt buộc chọn khoá và lớp**, thêm bộ lọc nhóm và mốc thời gian |

Chiều khoá học và lớp học của Report đặt vào Dashboard SIS hay dựng màn mới là **việc của Bước 7**. Ghi lại ở đây vì nếu chọn mở rộng SIS thì **hai dự án cùng sửa một màn**.

### 4.5 Vùng KB chưa phủ — không kết luận

| Chỉ số | Vì sao chưa kết luận được |
|---|---|
| **Buổi chưa xếp lịch** | Thuộc mảng lịch dạy: nhóm API `Schedules` · `Class Schedule` · bảng `class_lecture_instances`. **KB chưa phủ** *(KB `14` §2.1)*. Câu *"mảng lịch dạy có thuộc phạm vi BA không"* vẫn còn treo *(KB `14` §5 Q1)* |
| **Hàng chờ duyệt** | KB có hai luồng chờ người duyệt, đều trong chấm điểm: **kết quả chấm chờ mentor chính review** trước khi gửi học viên, và **yêu cầu chấm lại từ học viên** *(KB `05` §5)*. Mảng lịch dạy có đơn xin dạy, xin nghỉ, đổi chế độ dạy *(`request-schedules`)* nhưng KB chưa phủ. **Khoá học không có bước duyệt nội dung**: `Draft` sang `Publish` không qua ai *(KB `01` §4)* |
| **Phân quyền** | Ai xem được chiều khoá học và lớp học. Quyền nằm trong policy Casbin, KB chưa phủ |

### 4.6 Thông báo chấm điểm đang tắt

8 mail của luồng chấm điểm đang **tắt có chủ đích** *(`KB-MAIL-03`)*, trong đó có mail #32 *"nhắc mentor danh sách đang chờ chấm"* và mail #35 *"báo mentor chính có yêu cầu review bài chấm"*.

Nên chỉ số *"bài chưa chấm"*, và *"hàng chờ duyệt"* nếu hiểu là hàng chờ review, **đang bù cho chỗ thiếu thông báo**. Không phải xung đột. Nhưng nếu sau này bật lại 8 mail đó thì vai trò của hai chỉ số này đổi theo.

---

## 5. Requirement candidates

### Chiều người học

| ID | Requirement | Type | Source | Confidence | Ghi chú — đối chiếu KB |
|---|---|---|---|---|---|
| `RC-01` | Danh sách việc cần làm hôm nay | Screen-Report · Business Rule | Chiều người học, mục 1 | **Low** — *"việc"* chưa định nghĩa | Hệ thống **không có hạn theo từng Activity**. Hạn chỉ có ở: thời hạn lượt ghi danh *(cố định hoặc linh động — KB `04` §3)* · cửa sổ mở và đóng bài kiểm tra *(`KB-MAIL-07`)* · buổi học theo lịch *(KB chưa phủ)*. Chỉ lấy thứ đến hạn hôm nay thì phần lớn ngày danh sách sẽ trống. → `OQ-05` |
| `RC-02` | Danh sách nội dung sắp hết hạn | Screen-Report | Chiều người học, mục 2 | Medium — thiếu ngưỡng *"sắp"* | **Đã có từng phần:** My Learning hiện *thời hạn còn lại* từng khoá *(KB `07` §1)* · mail #16 nhắc bài kiểm tra **đóng trong 1 ngày** · mail #12 báo khoá **đã** hết hạn. Mới: gom về một chỗ. Khoá linh động chưa Activate thì chưa có hạn *(`KB-CLASS-03`)*. → `OQ-14` |
| `RC-03` | Danh sách khoá đang học dở, kèm tiến độ | Screen-Report | Chiều người học, mục 3 | **High** | Dữ liệu có sẵn: tiến độ = số Activity hoàn thành / tổng Activity *(`KB-LX-01`)*. Trạng thái `Resume` phía học viên có thể tương ứng, nhưng cách ánh xạ trạng thái hai phía còn `❓BA` *(KB `07` §12 Q1)* |
| `RC-04` | Kỹ năng vừa đạt và kỹ năng còn thiếu | Data · Business Rule | Chiều người học, mục 4 | **Low** | ❌ Chưa có khung năng lực — §4.2. → `OQ-03` |
| `RC-05` | Điểm và hạng | Screen-Report | Chiều người học, mục 5 | Medium | Nhiều khả năng dùng lại khối của Gamification `US1` — §4.3. → `OQ-04` |

### Chiều nhóm / quản lý

| ID | Requirement | Type | Source | Confidence | Ghi chú — đối chiếu KB |
|---|---|---|---|---|---|
| `RC-06` | Người trong nhóm đang **chậm** | Business Rule | Chiều nhóm, mục 1 | **Low** — *"chậm"* chưa định nghĩa | → `OQ-06` |
| `RC-07` | Người trong nhóm đang **quá hạn** | Screen-Report | Chiều nhóm, mục 2 | Medium — có ở Group nhưng chưa định nghĩa | **Trùng** Group `US16` · `US18` — §4.1. → `OQ-06` |
| `RC-08` | Người trong nhóm **chưa bắt đầu** | Screen-Report | Chiều nhóm, mục 3 | Medium — có ở Group nhưng chưa định nghĩa | Group `US18` có ở cấp nhóm bên Ops. Màn quản lý `US16` chưa có. → `OQ-06` |
| `RC-09` | Nhóm thiếu năng lực nào nhiều nhất | Data · Business Rule | Chiều nhóm, mục 4 | **Low** | Như `RC-04`, cộng dồn theo nhóm. → `OQ-03` |
| `RC-10` | Mỗi chỉ số bấm được sang danh sách người để xử lý | Functional | Chiều nhóm, câu cuối | **High** — nói rõ | *"Xử lý"* là làm gì thì chưa rõ. Group `US16` đã loại: giao bài, sửa thời hạn, xuất tệp. → `OQ-11` |
| `RC-11` | Phạm vi dữ liệu của quản lý | Role-Permission | Group `BR-16.1` → `BR-16.6` | **High** | Dùng nguyên văn luật Group — §4.1 |

### Chiều khoá học

| ID | Requirement | Type | Source | Confidence | Ghi chú — đối chiếu KB |
|---|---|---|---|---|---|
| `RC-12` | Nội dung đang chạy | Screen-Report | Chiều khoá học, mục 1 | Medium | `[suy ra]` Khoá có ít nhất một lớp đang diễn ra. Danh sách trạng thái lớp chính thức còn `❓BA` *(KB `04` §11 Q1)*. → `OQ-15` |
| `RC-13` | Tỷ lệ hoàn thành theo nội dung | Screen-Report | Chiều khoá học, mục 2 | Medium — thiếu độ chi tiết | Dashboard SIS thứ nhất đang tính theo **lớp**, tối đa 4 lớp. Mới: theo **khoá**, gộp mọi lớp. → `OQ-16` |
| `RC-14` | Hàng chờ duyệt | Process | Chiều khoá học, mục 3 | **Low** | Chưa rõ luồng duyệt nào — §4.5. → `OQ-09` |
| `RC-15` | Câu hỏi chưa trả lời | Screen-Report | Chiều khoá học, mục 4 | Medium | `[suy ra]` Bình luận của học viên trong Thảo luận chưa ai phản hồi *(KB `07` §7)*. Bình luận **gắn theo khoá**, hiện ở mọi lớp dùng khoá đó *(`KB-LX-12`)* — khớp với chiều khoá học. Nhóm Comment Replier trả lời theo Course Category *(KB `09` §7)*. Mail #21 · #22 báo **học viên** khi có người trả lời. Chiều ngược lại — báo **người trả lời** khi có câu hỏi mới — **không có mail nào**. → `OQ-13` |
| `RC-16` | Bài chưa chấm | Screen-Report | Chiều khoá học, mục 5 | **High** | **Dữ liệu đã có:** Grading List xem bài của mọi lớp người dùng phụ trách, lọc theo trạng thái `Awaiting Grading` · `Regrading` *(KB `05` §3–4)*. Mới: con số tổng và lối bấm sang. Đang bù cho 8 mail chấm điểm bị tắt — §4.6 |
| `RC-17` | Buổi chưa xếp lịch | Screen-Report | Chiều khoá học, mục 6 | **Low** | Vùng KB chưa phủ — §4.5. → `OQ-10` |

### Chiều lớp học

| ID | Requirement | Type | Source | Confidence | Ghi chú — đối chiếu KB |
|---|---|---|---|---|---|
| `RC-18` | Danh sách lớp đang có vấn đề | Business Rule · Screen-Report | Chiều lớp học, mục 1 | **Low** — *"vấn đề"* chưa định nghĩa | Dữ liệu cho nhiều dấu hiệu đã có: tiến độ, quá hạn, chưa bắt đầu, bài chưa chấm, mentor của lớp *(KB `04` §7)*. Riêng chuyên cần thì ngưỡng **70% đang đóng cứng** *(`KB-SIS-05`)* và dashboard chuyên cần chưa rõ còn dùng không *(KB `11` §1)*. → `OQ-07` |
| `RC-19` | Mỗi khối bấm được sang đúng lớp hoặc đúng danh sách | Functional | Chiều lớp học, câu cuối | **High** — nói rõ | Đích đến đã có: Class Detail · màn Mark của lớp · Grading List lọc theo lớp. ⚠️ **Tab Test/Quiz trong Class Detail đang `hidden`** *(KB `03` §6)* — muốn bấm sang danh sách theo bài kiểm tra thì phải hỏi tab này có bật lại không |

### Xuyên suốt

| ID | Requirement | Type | Source | Confidence | Ghi chú |
|---|---|---|---|---|---|
| `RC-20` | Ai xem chiều khoá học và lớp học, phạm vi tới đâu | Role-Permission | `[suy ra]` | **Low** | KB chưa phủ phân quyền. Trong chấm điểm, mentor chỉ xem bài được giao còn mentor chính xem toàn lớp *(`KB-GRAD-03`)*. → `OQ-08` |
| `RC-21` | `Test Account` không tính vào bất kỳ chỉ số nào | Business Rule | KB `06` §8b | **High** | `KB-USER-TA-01`: *"`Test Account` được bỏ qua ở mọi logic nghiệp vụ"*. Group `BR-16.5` · `BR-18.4` và Gamification `C10` đều đã áp |
| `RC-22` | Người nghỉ việc không hiện ở chế độ xem hiện tại | Business Rule | Group `BR-16.6` · `BR-18.5` | **High** | Tài khoản tự chuyển `Block` khi nghỉ việc *(`KB-USER-03`)* |
| `RC-23` | Mọi ngưỡng — *sắp hết hạn*, *chậm*, *lớp có vấn đề* — cấu hình theo tổ chức | NFR · Business Rule | `CLAUDE.md` · KB `15` §7 | **High** | Không lặp lại chuyện ngưỡng chuyên cần 70% bị đóng cứng *(KB `15` §6)* |
| `RC-24` | *"Báo cáo"* gồm gì ngoài dashboard: xuất tệp, xem lại quá khứ, gửi định kỳ | Screen-Report | Câu yêu cầu: *"báo cáo **và** dashboard"* | **Low** | Group `US18` có xem theo mốc quá khứ nhưng **loại** xuất tệp và gửi định kỳ. → `OQ-01` |

---

## 6. Phạm vi sơ bộ

### In scope — tạm, chờ câu hỏi chặn

Bốn chiều với những chỉ số **định nghĩa được**, lối bấm từ chỉ số sang danh sách, hai luật loại trừ `RC-21` *(không tính `Test Account`)* · `RC-22` *(không hiện người nghỉ việc)*, ngưỡng cấu hình theo tổ chức.

### Out of scope — đề xuất

| | Vì sao |
|---|---|
| **Dựng khung năng lực** | Hệ thống chưa có, Gamification cũng đã để ngoài. Đó là một dự án riêng cỡ L — chờ `OQ-03` |
| **Đổi cách tính tiến độ hoặc điều kiện hoàn thành Activity** | Dashboard **đọc** logic hiện có *(`KB-LX-01` · `KB-LX-03`)*. PO đã xác nhận giữ nguyên điều kiện hoàn thành Text/Ảnh *(`KB-LX-03b`)* |
| **Định nghĩa lại điểm, hạng, huy hiệu** | Thuộc Gamification |
| **Đổi quan hệ quản lý hoặc phạm vi dữ liệu theo nhóm** | Thuộc Group, đã chốt ở `BR-16.1` → `BR-16.6` |
| **Bật lại 8 mail chấm điểm** | Quyết định riêng, không nằm trong yêu cầu |
| **Báo cáo cho UpAcademy, Admin, Super Admin** | Ngoài phạm vi UpLnD *(`CLAUDE.md`)* |

### Potential scope — chờ trả lời

| | Chờ |
|---|---|
| Xuất tệp · xem lại theo mốc quá khứ · xu hướng theo thời gian · gửi định kỳ qua email | `OQ-01` |
| Hành động ngay trên danh sách, ví dụ nhắc học viên | `OQ-11` |
| Lộ trình học, khi đã có | `A-06` |

---

## 7. Phân cỡ đề xuất

**Cỡ `L`.** Có cả bốn dấu hiệu, trong khi chỉ cần một là đã `L`:

| Dấu hiệu | Ở đây |
|---|---|
| Chạm từ 3 module trở lên | Learning Experience · Class · Course · Grading · Assessment · Thảo luận · Lịch dạy · Dashboard SIS · Group · Gamification |
| Đổi data model | Có thể: cấu hình ngưỡng theo tổ chức; nếu chọn làm năng lực thì có thực thể mới |
| Có conflict | Trùng màn với Group `US16` · `US18`. Có thể cùng sửa Dashboard SIS với Group `US18` |
| Nhiều hướng giải quyết | Mở rộng Dashboard SIS hay dựng màn mới · trang tổng quan người học đặt ở đâu · năng lực lấy từ nguồn nào |

→ Đủ 9 bước, đủ 4 Gate.

---

## 8. `Recommendation` — cắt Phase 1 theo phụ thuộc

Chưa phải quyết định. Ghi lại để PO cân nhắc khi trả lời `OQ-01`.

| Chiều | Phụ thuộc | Làm được khi nào |
|---|---|---|
| **Khoá học** | Dữ liệu đã có, trừ *buổi chưa xếp lịch* *(vùng KB chưa phủ)* và *hàng chờ duyệt* *(chưa định nghĩa)* | Ngay |
| **Lớp học** | Dữ liệu đã có, chỉ cần định nghĩa *"có vấn đề"* | Ngay |
| **Người học** | Phần lớn đã có. *Điểm và hạng* chờ Gamification. *Kỹ năng* chờ `OQ-03` | Ngay, trừ hai chỉ số |
| **Nhóm / quản lý** | Chờ Group xây xong nhóm và quan hệ quản lý | Sau Group |

Phase 1 có thể gồm **khoá học, lớp học và người học** *(trừ kỹ năng)*. Chiều nhóm/quản lý đi cùng hoặc ngay sau Group.

Chi tiết câu hỏi mở: `working/open-questions/open-questions-20261006.md`
