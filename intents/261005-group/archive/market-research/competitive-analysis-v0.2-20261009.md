---
intent: 261005-group
artifact: competitive-analysis
version: 0.2
status: approved
approved: 2026-10-09
note: v0.2 ngày 2026-10-07, §9.2 có ba điểm chờ PO xem
migrated-from: .claude/projects/Group/working/ai-drafts/nghien-cuu-lms-khac-v0.2-20261007.md
---
# Các LMS khác làm chức năng Nhóm thế nào

**Ngày:** 05/10/2026 · **Cập nhật:** 07/10/2026 *(v0.2)*
**Mục đích:** đối chiếu yêu cầu của UpLnD với cách làm phổ biến, để biết chỗ nào đang theo mẫu chung và chỗ nào đang thiếu

> ⚠️ **Đây là tài liệu tham khảo, không phải đề xuất giải pháp.** Không dòng nào ở đây là quyết định. Mọi chỗ gợi ý đều ghi nhãn `Recommendation` và chờ PO.

## Lịch sử thay đổi

| Version | Ngày | Nội dung |
|---|---|---|
| `v0.1` | 05/10/2026 | Bản đầu: TalentLMS · Docebo · Moodle · mô hình tích hợp HRIS. Viết ở Bước 3, **trước khi có PRD**. File gốc: `nghien-cuu-lms-khac-20261005.md` |
| **`v0.2`** | 07/10/2026 | Thêm **§8** *(bốn bài TalentLMS do PO đưa)* và **§9** *(đối chiếu với PRD `v0.1` đã duyệt 06/10)*. **§1–§7 giữ nguyên chữ**, kể cả ba "khoảng trống" ở §7 mà PRD đã đóng — xem §9.4 |

---

## 1. Mẫu chung: hầu hết đều tách hai loại nhóm

Ba nền tảng lớn đều có **hai khái niệm riêng biệt**, không gộp làm một:

| Nền tảng | Loại theo cơ cấu | Loại tuỳ ý |
|---|---|---|
| **TalentLMS** | `Branch` — sub-portal độc lập, có quản trị riêng, thương hiệu riêng, bộ quy tắc riêng | `Group` — gom learner cần cùng một bộ training, kèm báo cáo nhóm |
| **Docebo** | `Branch` — mô phỏng cơ cấu công ty, người trong cùng nhánh thấy nhau | `Group` — gom kiểu không chính thức, **có thể cắt ngang nhiều nhánh** |
| **Moodle** | `Cohort` — phạm vi toàn site hoặc toàn danh mục khoá | `Group` — nằm trong **một khoá** cụ thể |

Điểm chung: **cơ cấu tổ chức là một loại nhóm, không phải toàn bộ khái niệm nhóm.** Docebo nói thẳng rằng group dùng để gom những tập hợp *"có thể là tập con bên trong cơ cấu, hoặc cắt ngang nhiều phần của cơ cấu"*.

Điều này khớp với cách PO đóng khung bài toán ngày 05/10: cây tổ chức đồng bộ từ HRM chỉ là **một nguồn** tạo nhóm, không phải bản chất của chức năng.

---

## 2. Cohort của Moodle hoạt động đúng như "luật đứng"

Tài liệu Moodle mô tả: *thêm hoặc bớt người khỏi một cohort thì họ tự động được ghi danh hoặc gỡ ghi danh khỏi những khoá gắn với cohort đó.*

Đây chính là cơ chế PO mô tả: gán nội dung cho nhóm là **một luật đứng**, không phải sao chép thành viên một lần. Cách hiểu của UpLnD trùng với một hệ đã chạy nhiều năm.

Khác biệt đáng chú ý: Moodle **gỡ ghi danh** khi người rời cohort. Yêu cầu của UpLnD chưa nói rõ chuyện này — `OQ-07` mới chỉ bàn trường hợp xoá cả nhóm, chưa bàn trường hợp một người rời nhóm.

---

## 3. Khái niệm yêu cầu hiện chưa có: nhóm động

Moodle có `Dynamic Cohorts`, cho phép thành viên vào ra **tự động theo điều kiện** thay vì gán tay:

- Nhiều điều kiện trong một luật, ghép bằng `AND` hoặc `OR`
- Điều kiện dựa trên: trường hồ sơ chuẩn, trường hồ sơ tuỳ chỉnh, trạng thái ghi danh, lần đăng nhập cuối, vai trò trong một ngữ cảnh

Yêu cầu 19 hạng mục của UpLnD hiện có **hai cách vào nhóm**: đồng bộ từ HRM, và gán tay. Không có cách thứ ba là *theo điều kiện*.

Ví dụ thứ mà nhóm động làm được còn hai cách kia thì không: *"mọi người có chức danh chứa chữ Trưởng nhóm, ở bất kỳ phòng ban nào"*. Cây tổ chức không gom được nhóm này vì họ nằm rải rác, mà gán tay thì phải cập nhật mỗi lần có người lên chức.

**Không đề xuất làm.** Chỉ nêu để PO biết có khoảng trống đó, và quyết ở Bước 7 xem có đưa vào phạm vi không.

---

## 4. Đồng bộ HRIS: ba tầng dữ liệu

Tài liệu về tích hợp HRIS với LMS mô tả ba tầng, và hệ nào cũng phải quyết riêng từng tầng:

| Tầng | Dữ liệu | UpLnD hiện ở đâu |
|---|---|---|
| 1 | Người dùng: tên, email, mã nhân viên, trạng thái | ✅ Đã đồng bộ được từ Lark |
| 2 | **Cơ cấu: phòng ban, quản lý, địa điểm, chức danh** | ❌ Chưa. Đây là phần dự án này làm |
| 3 | Sự kiện vòng đời: tuyển mới, điều chuyển, nghỉ việc | ❓ Chưa rõ |

Nguyên tắc chung: **HRIS luôn là hệ gốc**, LMS đọc từ đó và ghi ngược lại kết quả học.

Tầng 3 đáng chú ý vì yêu cầu hiện tại chưa nhắc tới. `RC-18` có nói trường hợp quản lý rời vị trí, nhưng chưa nói trường hợp **một học viên bị điều chuyển sang phòng ban khác** — khi đó nghĩa vụ học đã gán qua nhóm cũ xử lý ra sao.

---

## 5. Lỗi hay gặp nhất khi đồng bộ cơ cấu

Một tài liệu về thất bại khi tích hợp HRIS ghi: *phần lớn các lần đồng bộ HRIS sang LMS hỏng vì nhóm lồng nhau. Nếu HRIS không làm phẳng cơ cấu trước khi đẩy qua API, LMS nhiều khả năng sẽ tạo ra hồ sơ người dùng trùng.*

Đúng tình huống UpLnD sắp gặp: cây Lark có 4 cấp, 53 phòng ban, và yêu cầu `RC-07` nói **nhóm cha bao trùm toàn bộ nhánh con**.

Câu hỏi nảy ra từ đây: khi đồng bộ, một người ở `ECOM / Trung tâm vận hành 1 / Growth 1 / Sub-Growth 1` được ghi là thành viên của **một nhóm sâu nhất**, hay của **cả bốn nhóm trên đường đi**? Hai cách cho hai kết quả khác hẳn nhau ở báo cáo và ở phạm vi quản lý.

→ Thành `OQ-21`.

---

## 6. Nhịp đồng bộ

Tài liệu tích hợp phân biệt hai nhịp theo loại sự kiện:

| Loại | Nhịp phù hợp |
|---|---|
| Ghi danh, nghỉ việc | Gần thời gian thực, qua webhook |
| Thay đổi cơ cấu tổ chức | Theo lô, mỗi ngày hoặc mỗi tuần là đủ |

Cơ cấu tổ chức đổi vài lần một năm, nên đồng bộ theo lô là đủ. Nhưng **nghỉ việc thì khác** — người đã rời công ty mà vẫn còn trong nhóm và vẫn nhận nội dung mới là một vấn đề thật.

---

## 7. Tóm tắt: ba chỗ yêu cầu đang thiếu so với mẫu chung

| | Khoảng trống | Hệ nào có |
|---|---|---|
| 1 | **Nhóm động theo điều kiện** — ngoài đồng bộ và gán tay | Moodle `Dynamic Cohorts` |
| 2 | **Người rời nhóm thì nghĩa vụ học xử lý thế nào** — yêu cầu mới bàn trường hợp xoá cả nhóm | Moodle gỡ ghi danh |
| 3 | **Sự kiện vòng đời nhân sự** — điều chuyển, nghỉ việc | Tầng 3 của mô hình tích hợp HRIS |

Và một chỗ yêu cầu **chặt hơn** mẫu chung: `RC-11` đòi dựng lại được ai thuộc nhóm nào tại một thời điểm quá khứ. Không nguồn nào trong ba nền tảng trên nhắc tới việc này như một tính năng sẵn có.

> 🔄 **07/10:** cả ba khoảng trống đã được PRD `v0.1` đóng. Xem §9.4. Giữ nguyên bảng này để còn dấu vết.

---

## 8. Bổ sung 07/10 — bốn bài TalentLMS do PO đưa

Nguyên văn bốn bài: `working/raw-inputs/talentlms-help-articles-20261007.md`. Dưới đây chỉ rút phần **luật**, bỏ phần thao tác bấm nút.

### 8.1 Nhóm trong Branch và "nhóm mặc định"

**Fact — TalentLMS làm thế này:**

- Group gắn được vào một Branch. Gắn rồi thì **quản trị viên của Branch** quản lý được group đó *(thêm người, khoá, lộ trình)*. Không gắn thì họ không có quyền này
- Mỗi Branch có **đúng một** *default group*. Một group làm default cho **nhiều** Branch được
- Người mới tạo trong Branch **tự vào default group và tự ghi danh** các khoá của group — với điều kiện khoá đó **đã gán cho Branch trước**
- Group có **Group key**: người dùng tự đăng ký vào group bằng mã, khỏi phải thêm tay
- **Thêm tay bởi Admin hoặc Instructor thì KHÔNG tự ghi danh**, kể cả khi group đã có khoá. Muốn tự ghi danh thì bật *Auto-enroll users to training* **lúc tạo group**. Muốn ghi danh người đang có thì dùng *Mass actions*, hoặc bấm từng người *Add all remaining group courses to user*
- Gỡ một người khỏi Learning Path của group thì gỡ khỏi mọi khoá trong đó, nhưng **tiến độ và lịch sử hoàn thành giữ nguyên**. Ghi danh lại thì **học tiếp từ chỗ dừng**

**Đọc ra gì cho UpLnD:**

- *Default group* của Branch chính là cách TalentLMS làm **luật đứng theo cơ cấu**. UpLnD làm tương đương bằng hai luật đã có: đồng bộ đưa người vào nhóm sâu nhất *(`BR-5.2`)*, rồi công tắc tự ghi danh chạy mỗi lần có người vào qua đồng bộ *(`BR-8.4`)*. **Khớp.**
- Mặc định của TalentLMS cũng là **không tự ghi danh** người thêm tay. Trùng quyết định `F-12` *(hai công tắc mặc định tắt)*. **Khớp.**
- Công tắc tự ghi danh ở TalentLMS đặt ở **cấp group**. PRD đặt ở **cấp từng cặp nhóm với lớp** *(`BR-8.1`)*, linh hoạt hơn. Có một chỗ lệch câu chữ: chuỗi tiếng Anh PRD mượn — `New group members will be automatically enrolled to this group's existing course` — là chuỗi cấp group của TalentLMS, đọc hơi lạ khi nằm trên **từng dòng lớp**. Chỉ là câu chữ, không phải luật. Ghi ở §9.3
- **Tiến độ giữ khi gỡ** là chỗ khác hẳn UpLnD. Ghi ở §9.2 mục c

### 8.2 Chia sẻ tệp cho cả nhóm

**Fact:** Group và Branch có tab **Files**. Admin tải tệp lên, bật *Shared*, mọi thành viên thấy tệp ở *My Files*. Người giám sát nhóm không có quyền Admin thì **chỉ thấy tệp đã bật Shared**.

**Đọc ra gì:** nhóm của TalentLMS **chứa cả tệp**. PRD đã đưa *Nhóm chứa nội dung* vào Out of scope theo **nguyên tắc 6** — nhóm chỉ chứa người, *"không chứa bất cứ thứ gì khác"* *(KB `16-domain-principles.md`)*. Tệp không phải nội dung học, nhưng vẫn là "thứ khác". **Không đề xuất thêm:** Lark Drive đã chia sẻ tệp theo phòng ban rồi, làm nữa là trùng công cụ.

### 8.3 Group Supervisor — vai giám sát nhóm

**Fact — TalentLMS làm thế này:**

- Là **vai chức năng**, tách khỏi ba vai hệ thống *(Administrator · Instructor · Learner)*. **Ghép** với vai gốc của người đó. **Quyền sửa phụ thuộc vai gốc**, vai giám sát chỉ thêm quyền **xem** trong phạm vi nhóm
- Thấy được: thành viên, khoá, tệp, thông tin nhóm, và một tab **Reports** riêng *(tổng quan · người · khoá · dòng thời gian)*, có lọc và **xuất tệp**
- **Nhắn tin** cho thành viên là quyền riêng, **mặc định tắt**
- Phạm vi **chỉ trong nhóm được gán**. **Nhiều** supervisor cho một nhóm. **Một** supervisor cho nhiều nhóm, phạm vi tính riêng từng nhóm
- Điều kiện gán: người đó **phải đang là thành viên của nhóm**, và vai gốc có quyền *Groups > Supervision > Supervise*. Learner cũng làm supervisor được nếu tạo user type tuỳ chỉnh
- Supervisor **không được loại khỏi** ghi danh mà nhóm nhận. Nhóm nhận khoá nào thì supervisor cũng học khoá đó
- Vào nhóm mình giám sát qua **giao diện Admin hay Instructor**, tuỳ quyền *Supervise* bật ở nhánh nào của user type
- Có **sự kiện thông báo hệ thống** *Group Supervisor assignment*: người được gán nhận thông báo kèm nội dung họ được xem gì
- Gỡ vai → **mất ngay** quyền xem nhóm, vai gốc không đổi
- Chỉ có ở bản Pro *(tối đa 10 nhóm)* và Enterprise, giao diện mới

**Đọc ra gì:** đây là bài sát với `US9` · `US16` nhất. Đối chiếu từng dòng ở §9.1 và §9.2.

### 8.4 Xoá group hoặc branch

**Fact:**

- Admin xoá được. **Vĩnh viễn, không hoàn tác.** Hành động ghi vào Timeline
- Xoá **không** đụng người dùng, khoá, **lượt ghi danh**, tiến độ. Lượt ghi danh sinh ra qua nhóm **vẫn còn hiệu lực** sau khi nhóm biến mất
- Khoá tạo bên trong nhóm vẫn còn, vẫn hiện ở *My training* của người đã ghi danh
- Branch có thêm lựa chọn **deactivate** *(tạm ngưng)*. **Group thì không có.**

**Đọc ra gì:**

- TalentLMS cho xoá thoải mái vì họ **không có nhu cầu `O5`** *(dựng lại ai thuộc nhóm nào tại một thời điểm quá khứ)*. PRD chặt hơn **có chủ đích**: chỉ xoá nhóm chưa từng có thành viên và chưa từng giao nội dung *(`BR-14.1`)*, còn lại chỉ lưu trữ *(`BR-14.2`)*
- Giống nhau ở chỗ quan trọng: xoá hay lưu trữ đều **không đụng lượt ghi danh đã sinh** *(`BR-14.4`)*. **Khớp**
- *Lưu trữ* của UpLnD tương đương *deactivate* của TalentLMS — mà TalentLMS chỉ có cho Branch, không có cho Group. UpLnD làm **đủ hơn** ở chỗ này

---

## 9. Đối chiếu với PRD `v0.1` *(đã duyệt 06/10/2026)*

> PRD đã duyệt nên **không sửa gì ở đây**. Mục 9.2 là ba chỗ đáng để PO xem lại; muốn đưa vào thì đi qua `/change-request`, điểm re-entry **PRD**, chỉ chạm US nêu tên.

### 9.1 PRD đang khớp với TalentLMS — không cần làm gì

| TalentLMS | PRD `v0.1` | Ghi chú |
|---|---|---|
| Nhiều supervisor một nhóm · một supervisor nhiều nhóm | `BR-9.1` *(một nhóm nhiều quản lý)* · `BR-9.2` *(một người quản lý nhiều nhóm)* | Khớp |
| Vai giám sát **ghép** vai gốc, quyền sửa theo vai gốc, phạm vi theo nhóm | `CF-5` *(phạm vi dữ liệu tách theo màn)* · `BR-16.4` *(màn theo dõi đọc theo quan hệ quản lý, không theo vai hệ thống)* | Khớp hướng. TalentLMS đã chạy đúng kiểu "hai phạm vi, không cộng, không giao" này |
| Người thêm tay **không** tự ghi danh, trừ khi bật công tắc | `F-12` *(hai công tắc mặc định tắt)* · `BR-8.3` *(bật công tắc thì chọn ghi danh luôn người đang thiếu hay chỉ từ giờ)* | Khớp. *Mass actions* của TalentLMS tương đương lựa chọn ở `BR-8.3` |
| Default group: người mới vào Branch tự vào nhóm và tự ghi danh | `BR-5.2` *(vào nhóm sâu nhất)* · `BR-8.4` *(luật đứng chạy cả với người vào qua đồng bộ)* | Khớp |
| Xoá nhóm không đụng lượt ghi danh và tiến độ | `BR-14.4` *(lưu trữ không đụng lượt ghi danh đã sinh)* | Khớp |
| Supervisor **không được loại** khỏi ghi danh của nhóm | PRD không có luật loại trừ quản lý khỏi luật đứng. Cộng với `CF-2` *(tài khoản tách theo vai)*: quan hệ quản lý gắn vào **tài khoản nhân sự vận hành** *(`US9` pre-condition)*, còn **tài khoản học viên** của cùng người đó vẫn vào lớp theo luật đứng như mọi thành viên | Khớp về kết quả. **Ghi rõ để sau không ai đề xuất "loại quản lý khỏi luật đứng"** — TalentLMS cũng không làm vậy |
| Supervisor phải **là thành viên** nhóm | UpLnD **ngược lại**: quản lý là tài khoản Ops, **không phải** thành viên *(nhóm chỉ chứa học viên)* | Khác cấu trúc nhưng **có chủ đích** theo `CF-2`. Không phải lỗ hổng |

### 9.2 Ba chỗ PRD đang để trống hoặc chưa nói rõ — chờ PO xem

**a. `US16` *(quản lý theo dõi nhánh)* nằm ở portal nào, dùng tài khoản nào?**

- *Fact TalentLMS:* supervisor vào nhóm mình giám sát qua giao diện **Admin hoặc Instructor**, tuỳ quyền bật ở đâu. Họ phải nói rõ vì vai chức năng không tự có "cửa vào"
- *Fact PRD:* `US9` bắt người được gán **có tài khoản nhân sự vận hành**. `BR-16.4` nhắc tới người *"vừa là quản lý nhóm vừa có vai trò xem toàn công ty"* — tức là vai Ops. Nhưng **`US16` không ghi portal nào**, và `project-context.md` bảng *Phạm vi sản phẩm* lại xếp `US16`–`US17` vào **UpLMS** *(portal học viên)*
- *Open Question:* màn theo dõi nhánh ở **UpLMS Ops** hay **UpLMS**? Nếu Ops thì trưởng phòng phải có tài khoản Ops, và `project-context.md` đang ghi sai. Nếu UpLMS thì `US9` đang sai vì tài khoản học viên không phải tài khoản Ops
- *Recommendation:* **Ops**, vì hai luật `US9` và `BR-16.4` đều đã giả định như vậy; chỉ cần thêm một dòng vào `US16` và sửa bảng phạm vi trong `project-context.md`. Chọn UpLMS thì phải đụng `US9` và `CF-2`, nặng hơn nhiều

**b. Người được gán làm quản lý không được báo**

- *Fact TalentLMS:* có sự kiện thông báo riêng *Group Supervisor assignment*
- *Fact PRD:* `US9` *(gán quản lý)* và `US13` *(chuyển toàn bộ phụ trách)* **không gửi gì** cho người nhận vai. Mail duy nhất của dự án là `MAIL-GRP-01` ở `US20`. Hệ quả: trưởng phòng **không biết** mình đã được gán, không vào màn `US16`; lần đầu họ biết là khi nhận mail `US20` báo có người rời nhóm
- *Recommendation:* thêm **một mail event** cho hai thời điểm *gán quản lý* và *nhận chuyển phụ trách* — tạm gọi `MAIL-GRP-02` — dùng cùng hạ tầng với `MAIL-GRP-01`. Việc nhỏ. Hoặc ghi rõ vào Out of scope của `US9` để khỏi ai hỏi lại

**c. Gỡ khỏi lớp làm mất tiến độ — quản lý ở `US20` cần được báo trước**

- *Fact TalentLMS:* gỡ ghi danh **giữ tiến độ**, ghi danh lại học tiếp
- *Fact UpLnD:* xoá khỏi lớp thủ công **mất tiến độ thật**, học lại từ đầu *(quyết định Gate 2, 06/10; `OQ-29` chuyển lớp tạm chấp nhận)*. Đây là ràng buộc của chức năng **Lớp**, ngoài phạm vi dự án này — **không đề xuất sửa**
- *Chỗ chạm dự án:* `US20` kịch bản ghi quản lý nhận mail rồi *"giữ nguyên lớp, hoặc gỡ họ khỏi lớp"*. Ở TalentLMS hai lựa chọn này **đảo ngược được**; ở UpLnD thì **gỡ là mất**. Quản lý không biết điều đó sẽ gỡ nhầm
- *Recommendation:* thêm **một câu cảnh báo** vào nội dung `MAIL-GRP-01` *("Gỡ khỏi lớp sẽ xoá tiến độ đã học, không khôi phục được")*. Chỉ câu chữ, không đổi luật. Hộp xác nhận gỡ khỏi lớp bên chức năng Lớp có cảnh báo chưa thì `❓BA`

### 9.3 Chỗ TalentLMS có mà PRD **cố ý** không làm — giữ nguyên

| TalentLMS có | PRD quyết | Vì sao giữ |
|---|---|---|
| **Group key** — tự đăng ký vào nhóm | `OQ-24`: đúng **hai** cách vào nhóm, đồng bộ và tự tạo | HRM là hệ gốc. Người tự đăng ký vào phòng ban là đi ngược nguyên tắc `BR-5.1` |
| **Tệp** trong nhóm | Out of scope *Nhóm chứa nội dung* — nguyên tắc 6 | Lark Drive đã làm việc này |
| **Nhắn tin** cho thành viên | `US17` Out of scope *(nhắn tin cho quản lý)* | Chưa cần |
| **Xuất báo cáo** của supervisor | `US16` · `US18` Out of scope *(xuất ra tệp)* | Để đợt sau |
| Công tắc tự ghi danh **cấp nhóm** | `BR-8.1`: cấp **từng cặp nhóm với lớp** | PRD linh hoạt hơn. Chỉ nên **xem lại chuỗi hiển thị** mượn từ TalentLMS cho khớp ngữ cảnh từng dòng lớp — việc của người viết, không cần PO |
| Branch **deactivate**, group **không** | `US14` lưu trữ cho mọi nhóm | UpLnD đủ hơn |

### 9.4 Cập nhật cho §7 — ba khoảng trống đã đóng thế nào

| Khoảng trống ở §7 | PRD `v0.1` xử lý |
|---|---|
| 1. Nhóm động theo điều kiện | **Out of scope** — `OQ-24`, đúng hai cách vào nhóm |
| 2. Người rời nhóm thì nghĩa vụ học ra sao | `BR-3.4` *(xét theo tình trạng học từng khoá)* · `US19` *(chưa học thì tự gỡ)* · `US20` *(đang học hoặc đã xong thì báo quản lý)* |
| 3. Sự kiện vòng đời nhân sự | Nghỉ việc: `BR-5.7` *(ghi rời nhóm kèm thời điểm, không xoá)* · `OQ-36` *(đánh dấu lượt ghi danh kết thúc)*. Điều chuyển: `OQ-23` dùng cùng luật với rời nhóm |

Chỗ "chặt hơn thị trường" *(`RC-11`, dựng lại quá khứ)* được bài xoá nhóm **xác nhận lại**: TalentLMS xoá vĩnh viễn, ghi một dòng Timeline, không dựng lại được. UpLnD đi xa hơn thị trường ở điểm này, và cái giá là `BR-14.2` *(nhóm có lịch sử chỉ lưu trữ, không xoá)*.

---

## Nguồn

**v0.1 — 05/10/2026**

- [What is the difference between groups and branches in TalentLMS](https://help.talentlms.com/hc/en-us/articles/9651522351260-What-is-the-difference-between-groups-and-branches-in-TalentLMS)
- [Best Practices for Setting up Branches and Groups — Docebo Community](https://community.docebo.com/product-q-a-7/best-practices-for-setting-up-branches-and-groups-505)
- [Groups and cohorts — MoodleDocs](https://docs.moodle.org/502/en/Groups_and_cohorts)
- [Dynamic cohorts — Moodle Marketplace](https://marketplace.moodle.com/plugins/tool_dynamic_cohorts)
- [HRIS Integration in LMS: Failures, Sync Issues & Models](https://lmspedia.org/hris-integration-in-lms-why-it-breaks-where-it-works-and-how-different-approaches-compare/)
- [TalentLMS Features For Organizational Mapping — eLearning Industry](https://elearningindustry.com/talentlms-features-organizational-mapping)

**v0.2 — 07/10/2026, PO đưa.** Nguyên văn lưu ở `working/raw-inputs/talentlms-help-articles-20261007.md`

- [How to use groups in branches in TalentLMS](https://help.talentlms.com/hc/en-us/articles/10730406045980-How-to-use-groups-in-branches-in-TalentLMS) — bài cập nhật 21/09/2026
- [How to share a file with all the users of a branch or group in TalentLMS](https://help.talentlms.com/hc/en-us/articles/9651458780444-How-to-share-a-file-with-all-the-users-of-a-branch-or-group-in-TalentLMS) — 05/03/2026
- [What is the Group Supervisor role in TalentLMS, and how it works](https://help.talentlms.com/hc/en-us/articles/27464091325340-What-is-the-Group-Supervisor-role-in-TalentLMS-and-how-it-works) — 21/07/2026
- [What happens if you delete a group or branch in TalentLMS?](https://help.talentlms.com/hc/en-us/articles/24882793526684-What-happens-if-you-delete-a-group-or-branch-in-TalentLMS) — 01/09/2026
