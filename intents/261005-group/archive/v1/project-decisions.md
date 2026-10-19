# Project Decisions

**Project:** Group

Nơi ghi mọi quyết định đã chốt. AI tra file này để **không hỏi lại câu đã có đáp án**.

> ⚠️ **Đây là bộ nhớ của dự án — đừng xoá trong quá trình làm việc.**

---

## Bước 2 — PO trả lời câu hỏi chặn (05/10/2026)

| Ngày | Quyết định | Lý do | Người quyết | Gate |
| --- | --- | --- | --- | --- |
| 05/10/2026 | ~~**`OQ-01` `Group Management` có thật và đang chạy**, dự án này mở rộng nó~~<br>⚠️ **Quyết định này đã bị thay thế bởi `BA-01` cùng ngày ở Bước 5: bỏ hẳn, coi như chưa có gì.** Lý do đổi: rà Swagger thấy nhóm hiện tại là nhóm **phẳng**, không có gì để kế thừa | — | PO | Bước 2 → Bước 5 |
| 05/10/2026 | **Khi mở lại chức năng gửi thông báo từ Ops, chọn người nhận từ chính chức năng nhóm này** | Một nguồn nhóm duy nhất cho mọi mục đích | PO | Bước 2 |
| 05/10/2026 | **`Department Management` hiện KHÔNG chạy.** Trước đây chỉ dành cho staff | Không phải nền để mở rộng | PO | Bước 2 |
| 05/10/2026 | **`OQ-02` ✅ Nhóm gắn NGƯỜI, Lớp gắn NỘI DUNG.** Bảng so sánh chín tiêu chí do PO cung cấp, xem `clarified-requirements` §2 | Hai khái niệm từng bị lẫn ở `CR-001` của Gamification | PO | Bước 2 |
| 05/10/2026 | **Gán nội dung cho nhóm là một LUẬT ĐỨNG, không phải sao chép một lần.** Ai thuộc nhóm thì vào lớp. Người gia nhập sau vẫn tự nhận, đó là `ORG.GRP.09` | Sao chép một lần thì không khác gì nhập file | PO | Bước 2 |
| 05/10/2026 | **Nhóm không được chứa gì ngoài người.** Quan hệ nội dung với nội dung chỉ sống trong Lộ trình, quan hệ người với nội dung chỉ sống trong Lớp và Automation | Nguyên tắc 6 *(cần tra bộ nguyên tắc gốc)* | PO | Bước 2 |
| 05/10/2026 | **`OQ-03` ✅ Một lượt ghi danh.** Người vừa ở Lớp vừa ở Nhóm, cùng được gán một khoá, vẫn chỉ sinh một lượt | Giữ nguyên ràng buộc hiện có: tiến độ treo vào lượt ghi danh | PO | Bước 2 |
| 05/10/2026 | **`OQ-04` ✅ `ORG.ROL.04` là mã chức năng:** mỗi vai trò gắn một phạm vi — toàn tổ chức, một hoặc nhiều nhánh nhóm chỉ định, hay chỉ những người mình quản lý. Cùng một quyền nhưng khác phạm vi thì thấy khác nhau | | PO | Bước 2 |
| 05/10/2026 | **`OQ-05` ✅ Chưa có đồng bộ cây tổ chức.** HRM là **Lark**. Đã đồng bộ được **học viên** từ Lark sang. Dev xác nhận **Lark đã có sẵn cây tổ chức** | Nền đồng bộ user đã có, mở rộng sang cây là việc tiếp theo | PO + Dev | Bước 2 |

## Bước 3 — PO trả lời đợt hai (05/10/2026)

| Ngày | Quyết định | Lý do | Người quyết | Gate |
| --- | --- | --- | --- | --- |
| 05/10/2026 | **`OQ-10` ✅ Có công tắc tự ghi danh khi tạo nhóm.** Chuỗi tiếng Anh: `New group members will be automatically enrolled to this group's existing course`. Chọn bật hay tắt lúc tạo nhóm | | PO | Bước 3 |
| 05/10/2026 | **`OQ-11` ✅ Trang người học hiện NHIỀU quản lý**, không phải một | Người thuộc nhiều nhánh thì có nhiều quản lý, hiện đủ | PO | Bước 3 |
| 05/10/2026 | **`OQ-12` ✅ Loại quan hệ `mentor` làm luôn đợt này**, không hoãn | | PO | Bước 3 |
| 05/10/2026 | **`OQ-16` ✅ Bỏ qua phần `Group Management` đang có, coi như chưa có gì.** Thiết kế như làm mới | Tránh bị ràng buộc bởi cái cũ khi cái cũ phục vụ mục đích khác | PO | Bước 3 |
| 05/10/2026 | **`OQ-18` ✅ Phạm vi dữ liệu đơn giản hoá: quản lý chỉ xem được nhóm mình quản lý, không xem được nhóm khác.** Không cần cơ chế phạm vi nhiều mức của `ORG.ROL.04` ở đợt này | Giảm phạm vi, bỏ phụ thuộc vào một module chưa làm | PO | Bước 3 |
| 05/10/2026 | **`OQ-19` ✅ Nguyên tắc 6 chưa có trong KB, phải bổ sung.** Đã tạo `16-domain-principles.md` | PO chỉ ra: dự án mới thì nguyên tắc mới, không thể có sẵn trước | PO | Bước 3 |
| 05/10/2026 | **Bỏ toàn bộ câu hỏi kỹ thuật cho Dev (nhóm C).** Không làm Technical Design chi tiết | Dev phân tích lại bằng công cụ của họ. Thiết kế sai từ PO **neo suy nghĩ người đọc**, tốn công gỡ hơn là không có gì. Đã ghi thành quy tắc trong `CLAUDE.md` | PO | Bước 3 |
| 05/10/2026 | **`OQ-06` ✅ Cây tổ chức thật trên Lark sâu 4 cấp** dưới gốc. Số cấp tối đa chốt **6**, cấu hình được theo tổ chức | Đo từ file HRM thật: 384 nhân sự, 53 phòng ban, 5 khối cấp 1. Chỉ 2 phòng ban chạm cấp 4 | PO + dữ liệu | Bước 3 |

## Gate 1 — PO duyệt ba câu đã giao phân tích (05/10/2026)

| Ngày | Quyết định | Lý do | Người quyết | Gate |
| --- | --- | --- | --- | --- |
| 05/10/2026 | **`OQ-07` ✅ Xoá nhóm có điều kiện.** Nhóm **chưa từng** có thành viên và **chưa từng** gán nội dung thì xoá được. Nhóm đã từng có một trong hai thì **chỉ lưu trữ**, nút xoá ẩn đi kèm giải thích | Xoá nhóm đã có lịch sử là phá chính yêu cầu `RC-11` *(dựng lại ai thuộc nhóm nào tại một thời điểm quá khứ)*. Lưu trữ đã là thứ người dùng thật sự cần | PO | Gate 1 |
| 05/10/2026 | **`OQ-08` ✅ Giữ toàn bộ lịch sử thành viên, không giới hạn thời gian, không dọn** | Khối lượng quá nhỏ để phải lo: 384 nhân sự, vài trăm dòng mỗi năm. Đặt hạn lưu trữ tạo lỗi khó chịu — báo cáo năm ngoái chạy được, năm kia thì không. Nhất quán với `BR-3.9` của Gamification | PO | Gate 1 |
| 05/10/2026 | **`OQ-09` ✅ Quản lý xem được một người thì xem TOÀN BỘ dữ liệu học của người đó**, kể cả nội dung người đó nhận qua nhánh khác | Tiến độ treo vào lượt ghi danh của Lớp, không treo vào nhóm. Một khoá có một tiến độ, không chia được theo nhánh. Cách chia phần sẽ khiến hai quản lý thấy hai con số khác nhau cho cùng một người | PO | Gate 1 |
| 05/10/2026 | **Hệ quả chấp nhận của `OQ-09`:** người thuộc hai nhánh thì cả hai quản lý cùng thấy toàn bộ dữ liệu học của họ | Hệ quả của cơ cấu ma trận mà `RC-02` cố ý cho phép, không phải lỗi phân quyền. Không muốn vậy thì đừng xếp người đó vào hai nhánh | PO | Gate 1 |

## Bước 5 — PO chốt phạm vi liên quan (05/10/2026)

| Ngày | Quyết định | Lý do | Người quyết | Gate |
| --- | --- | --- | --- | --- |
| 05/10/2026 | **`BA-01` ✅ Bỏ hẳn `Group Management` và `Recipients List` đang có. Coi như chưa có gì.** Sau này mở lại chức năng gửi thông báo từ Ops thì chọn người nhận thẳng từ chức năng Nhóm mới | Nhóm hiện tại là nhóm **phẳng**, chỉ CRUD và gán user — không có cha con, không có nguồn, không có quản lý. Không có gì để kế thừa | PO | Bước 5 |
| 05/10/2026 | **`BA-02` ✅ `Test Account` bị loại khỏi MỌI báo cáo và MỌI logic** của chức năng Nhóm | Giữ đúng `KB-USER-TA-01`. Không lọc thì số liệu nhóm gồm cả tài khoản kiểm thử của L&D và QA | PO | Bước 5 |
| 05/10/2026 | **`BA-03` ✅ Luật đứng theo luật của Lớp.** Lớp không cho thêm người thì nhóm cũng không thêm được — không có ngoại lệ riêng cho đường đi qua nhóm | Lớp là nơi giữ nghĩa vụ học. Mở ngoại lệ sẽ tạo hai bộ luật cho cùng một việc | PO | Bước 5 |
| 05/10/2026 | **`BA-04` ✅ Gán vào đúng lớp đã gắn với nhóm**, không phải tự đi tìm lớp theo khoá | Người gán chọn lớp cụ thể, hệ thống không đoán. Khác cách Comment Replier làm *(tự tìm theo Category, mỗi khoá một lớp)* | PO | Bước 5 |
| 05/10/2026 | **`BA-07` ✅ Vượt `Số học viên tối đa` chỉ CẢNH BÁO, vẫn thêm được bình thường** | Đây là hành vi hiện có của chức năng lớp, không phải luật mới. Nhóm theo luôn | PO | Bước 5 |
| 05/10/2026 | **Swagger đổi tên miền:** `https://uplms-api.staging.upbase.asia/{lms\|ops}/api/v1/docs`. Hai host cũ `lms-be` và `ops-be` bỏ | PO cung cấp. Host cũ có chứng chỉ TLS không khớp tên miền, không đọc được | PO | Bước 5 |
| 05/10/2026 | **`BA-05a` ✅ Báo cáo theo nhóm PHẢI xem lại được theo mốc quá khứ.** Mở số liệu quý trước thì vẫn ra đúng con số đã chốt lúc đó | Không có thì báo cáo quý 3 sẽ tính theo danh sách thành viên hôm nay, ra số sai | PO | Bước 5 |
| 05/10/2026 | **`BA-05b` ✅ Nhật ký thành viên KHÔNG dùng thường xuyên** — chỉ tra khi có vấn đề | `US15` là màn tra cứu nhẹ, không phải công cụ vận hành hằng ngày | PO | Bước 5 |
| 05/10/2026 | **Hệ quả của `BA-05`: dữ liệu thành viên theo thời gian là NỀN của báo cáo, không phải một màn hình.** Mọi báo cáo theo nhóm phải đọc qua lớp này, kể cả báo cáo hiện tại | Nếu chỉ coi nó là nhật ký để tra tay thì báo cáo quá khứ không chạy được | PO + phân tích | Bước 5 |
| 05/10/2026 | **`BA-06` ✅ Người nghỉ việc GIỮ NGUYÊN trong nhóm, không gỡ.** Luật đứng bỏ qua người `Block`; danh sách thành viên mặc định ẩn họ, có bộ lọc hiện lại; báo cáo hiện tại loại họ; báo cáo theo mốc quá khứ tính theo trạng thái tại mốc đó | Gỡ không hoàn tác được, đánh dấu thì có. Gỡ khỏi nhóm sẽ kích hoạt luật `OQ-22` → gỡ khỏi lớp → **số liệu quý đã chốt bị đổi**. Nhất quán với cách hệ xử lý tài khoản: nghỉ việc chuyển `Block`, không xoá | PO | Bước 5 |
| 05/10/2026 | **Luật đồng bộ kèm theo `BA-06`: người biến mất khỏi nguồn HRM thì ghi là "rời nhóm" kèm thời điểm, KHÔNG xoá dòng quan hệ** | Người nghỉ việc biến mất khỏi cây Lark. Nếu nhóm đồng bộ là bản sao đúng của Lark thì lần đồng bộ kế tiếp sẽ tự gỡ họ — đúng thứ `BA-06` muốn tránh | PO + phân tích | Bước 5 |

## Gate 2 — PO duyệt Impact Matrix (06/10/2026)

| Ngày | Quyết định | Lý do | Người quyết | Gate |
| --- | --- | --- | --- | --- |
| 06/10/2026 | **`CF-1` ✅ Bộ lọc báo cáo làm ĐỘNG, lọc theo gì cũng được.** Không ràng buộc cứng `Course` + `Class code`. Đặt đúng chỗ trong dashboard hiện có, không dựng màn riêng | `KB-SIS-01` là ràng buộc của bản cũ, không phải luật bất biến. Nới ra thì báo cáo theo nhóm vào được dashboard sẵn có, người dùng không phải nhớ hai nơi | PO | Gate 2 |
| 06/10/2026 | **`CF-2` ✅ Tách tài khoản theo vai trò.** Một người trong tổ chức có thể đồng thời là **học viên thật**, **tài khoản kiểm thử**, và **nhân sự trả lời bình luận** — mỗi vai một tài khoản riêng, không gộp | Gộp vào một tài khoản thì mọi logic phải đi kèm điều kiện loại trừ. Tách ra thì `BA-02` *(loại `Test Account`)* tự giải quyết xung đột hai luật đứng | PO | Gate 2 |
| 06/10/2026 | **`CF-3` ✅ Nhóm đồng bộ từ HRM KHÔNG cho sửa.** Thêm gỡ thành viên thủ công chỉ áp cho nhóm tự tạo | Nhất quán với `KB-USER-01` `KB-USER-02`: dữ liệu từ hệ nhân sự là chỉ đọc trên Ops | PO | Gate 2 |
| 06/10/2026 | **`CF-6` ✅ Mentor của nhóm CHÍNH LÀ mentor của lớp.** Không phải hai khái niệm. Khi thêm nhóm vào lớp thì mentor của nhóm được gán luôn làm mentor trong lớp, **phụ trách đúng nhóm đó** | Lớp chỉ là nơi chứa. Mentor đi theo nhóm, không đi theo lớp | PO | Gate 2 |
| 06/10/2026 | **`BI-1` ✅ Gán nhóm vào lớp có Foundation là hành vi BÌNH THƯỜNG**, giống thêm hàng loạt học viên vào lớp có Foundation. Không cần cảnh báo riêng | Không phải việc mới, chỉ là đường vào khác | PO | Gate 2 |
| 06/10/2026 | **`BI-2` ✅ Mail gửi hàng loạt là BÌNH THƯỜNG.** Không cần gộp, hoãn hay tắt mail cho đường gán qua nhóm | Giống hệt thêm hàng loạt học viên vào lớp. `OQ-26` và `OQ-27` tự đóng | PO | Gate 2 |
| 06/10/2026 | **`CF-5` ✅ Phạm vi dữ liệu TÁCH THEO MÀN.** Mỗi màn khai rõ nó đọc theo phạm vi nào — màn quản lý nhóm đọc theo quan hệ quản lý, màn giao bài đọc theo Role | Cộng hai phạm vi thì vai quản lý thành vô nghĩa; giao nhau thì Role bị vô hiệu. Tách theo màn giữ được cả hai | PO | Gate 2 |
| 06/10/2026 | **`CF-4` ✅ Người nghỉ việc MẤT lượt ghi danh.** Chỉ giữ lại những gì thuộc báo cáo quá khứ | PO quyết. ⚠️ **Đảo quyết định `BA-06` ngày 05/10** *(giữ nguyên trong nhóm, chỉ đánh dấu)* | PO | Gate 2 |
| 06/10/2026 | **`CF-6` ✅ Mentor đầu tiên được thêm vào lớp là `Main Responsible`**, đổi lại được sau | Không cần luật phức tạp khi lớp có nhiều nhóm nhiều mentor. `OQ-35` đóng | PO | Gate 2 |
| 06/10/2026 | **`OQ-28` ✅ Cảnh báo vượt sức chứa hiện MỘT DÒNG ở màn danh sách học viên trong lớp.** Không realtime, **không chặn** thao tác | Luật đứng chạy nền, không có ai ngồi trước màn hình. Cảnh báo để người vận hành thấy khi họ vào xem, không phải để ngăn | PO | Gate 2 |
| 06/10/2026 | **`OQ-29` ✅ Hệ thống CHƯA CÓ chức năng chuyển lớp.** Muốn chuyển thì **xoá khỏi lớp cũ, thêm vào lớp mới, học lại từ đầu**. Tạm chấp nhận | ⚠️ Swagger có `PUT /classes/{id}/students/transfer` và `revert-transfer` nhưng **tính năng không chạy** — lần thứ 6 endpoint chết trong hệ này. Đã ghi vào KB `14` | PO | Gate 2 |
| 06/10/2026 | **`OQ-36` ✅ Người nghỉ việc: ĐÁNH DẤU lượt ghi danh đã kết thúc, KHÔNG xoá dữ liệu** | `class_user_instances` đã có cột `status`. Xoá thì báo cáo quá khứ tính lại ra số khác, và 6 bảng treo vào sẽ mồ côi. Nhất quán với `KB-USER-03`: nghỉ việc chuyển `Block`, không xoá tài khoản | PO | Gate 2 |
| 06/10/2026 | **Phân biệt hai luồng rời lớp:**<br>• **Xoá khỏi lớp thủ công** *(ví dụ để chuyển lớp)* → **mất tiến độ thật**, học lại từ đầu<br>• **Nghỉ việc** → **đánh dấu kết thúc**, giữ nguyên dữ liệu | Hai việc khác nhau, đừng áp chung một luật | PO + phân tích | Gate 2 |

## Gate 4 — PRD được duyệt (06/10/2026)

| Ngày | Quyết định | Lý do | Người quyết | Gate |
| --- | --- | --- | --- | --- |
| 06/10/2026 | **✅ `Approved` — PRD `v0.1` được duyệt không kèm ghi chú.** 20 user story · 122 business rule · 4 sơ đồ · 14.015 từ | | PO | Gate 4 |
| 06/10/2026 | **Lớp đã kết thúc thì KHÔNG thêm người**, kể cả qua đường nhóm. Xác nhận lại `BR-7.5` | Lớp kết thúc là ràng buộc của chính chức năng Lớp, nhóm không mở ngoại lệ | PO | Gate 4 |

## Bước 9 — PO chốt khi viết PRD (06/10/2026)

| Ngày | Quyết định | Lý do | Người quyết | Gate |
| --- | --- | --- | --- | --- |
| 06/10/2026 | **Hai cửa của luật đứng tách bạch:**<br>• **Lớp đã kết thúc → KHÔNG thêm người.** Luật đứng dừng im lặng, ghi nhật ký *(`BR-7.5`)*<br>• **Vượt sức chứa → VẪN thêm.** Chỉ hiện một dòng ở màn danh sách học viên trong lớp *(`BR-7.6`)* | Lớp kết thúc là ràng buộc của chính chức năng Lớp, nhóm không mở ngoại lệ. Sức chứa chỉ là cảnh báo vận hành | PO | Bước 9 |
| 06/10/2026 | **`BR-20.4` ✅ Người rời nhóm mà không có quản lý nào → gửi quản trị viên hệ thống** | Không để một trường hợp trôi đi mà không ai nhận | PO | Bước 9 |
| 06/10/2026 | **`F-01` ✅ Nhóm không có `cấp bậc` và `đơn vị kinh doanh`.** Giữ đúng bốn thứ: tên · mã · mô tả · nhóm cha | PO: *"nó là nhóm, và chỉ là nhóm"* | PO | Bước 9 |
| 06/10/2026 | **`F-02` ✅ Mã nhóm bắt buộc và duy nhất** | | PO | Bước 9 |
| 06/10/2026 | **`F-03` `F-04` `F-05` ✅ Màn danh sách nhóm hành xử như Drive:** số thành viên đếm cả nhánh con · tìm thấy nhóm con thì hiện đường dẫn từ gốc · dạng cây tải dần theo nhánh | Người dùng đã quen mô hình thư mục, không phải học lại | PO | Bước 9 |
| 06/10/2026 | **`F-06` ✅ Đã có người học thì không gỡ lớp khỏi nhóm được.** Cùng logic gỡ học viên khỏi lớp | | PO | Bước 9 |
| 06/10/2026 | **`F-07` ✅ Một người có nhiều quản lý. Quản lý gắn với hồ sơ là quản lý chính** — cao nhất.<br>Thứ bậc **không đổi phạm vi dữ liệu**, chỉ đổi thứ tự hiển thị và người nhận email | | PO | Bước 9 |
| 06/10/2026 | **`F-08` ✅ Học viên thấy tên, ảnh, email của quản lý.** Không hiện số điện thoại | | PO | Bước 9 |
| 06/10/2026 | **`F-11` ✅ Tên nhóm tối đa 255 ký tự, mô tả 1000** | | PO | Bước 9 |
| 06/10/2026 | **`F-12` ✅ Hai công tắc *chảy xuống nhánh con* và *tự ghi danh* mặc định TẮT** | Bật mặc định thì một thao tác gán có thể kéo cả khối vào lớp mà người gán không lường | PO | Bước 9 |
| 06/10/2026 | **Rule workflow mới: PRD không có mục `Database` và `API`.** Thay bằng `Dữ liệu phải lưu` — ghi thông tin nghiệp vụ nào phải lưu và vì sao | PO: *"chỉ viết scope của BA/PO, không viết scope của Dev"*. Đã ghi vào `generate-prd.md`, `Template.md`, checklist | PO | Bước 9 |
| 06/10/2026 | **Rule workflow mới: ba thứ không hỏi người viết nữa** — bảng metadata để trống · link Figma và tài khoản staging để trống · Metrics success **luôn tự đề xuất** | Người viết điền sau, đỡ phải hỏi lại ở mọi dự án | PO | Bước 9 |

## Bước 7 — PO chốt nhóm D (06/10/2026)

| Ngày | Quyết định | Lý do | Người quyết | Gate |
| --- | --- | --- | --- | --- |
| 06/10/2026 | **`OQ-21` ✅ Khi đồng bộ, người chỉ thuộc nhóm SÂU NHẤT** trên nhánh của họ, không thuộc các nhóm cha trên đường đi | Một người một quan hệ thành viên, không nhân bản theo độ sâu. Nhóm cha vẫn bao trùm nhánh con ở mức **đọc** *(báo cáo, phạm vi quản lý)* — `RC-07` không đổi | PO | Bước 7 |
| 06/10/2026 | **`OQ-22` ✅ Rời nhóm thì xét theo tình trạng học của từng khoá:**<br>• **Chưa học** → chuyển được<br>• **Đang học dở** hoặc **đã học xong** → **thông báo cho quản lý và L&D vào xử lý thủ công**, hệ thống **không tự quyết** | Hệ thống không được tự xoá dữ liệu học của ai. Khi có dữ liệu thì để người quyết | PO | Bước 7 |
| 06/10/2026 | **`OQ-23` ✅ Điều chuyển phòng ban dùng CÙNG LUẬT với `OQ-22`** | Cùng bản chất: rời một nhóm, sang nhóm khác | PO | Bước 7 |
| 06/10/2026 | **`OQ-24` ✅ KHÔNG làm nhóm động theo điều kiện.** Đúng **hai** cách vào nhóm: đồng bộ từ HRM theo cây tổ chức, và tự tạo thủ công | Giữ phạm vi gọn. `US19` chính thức bỏ khỏi danh sách | PO | Bước 7 |
| 06/10/2026 | **Hệ quả: ba trường hợp rời nhóm có ba luật khác nhau**<br>• **Nghỉ việc** → đánh dấu lượt ghi danh kết thúc, giữ dữ liệu *(`OQ-36`)*<br>• **Điều chuyển / gỡ khỏi nhóm, chưa học khoá nào** → chuyển được<br>• **Điều chuyển / gỡ khỏi nhóm, đang hoặc đã học** → báo người quyết | Ba tình huống khác nhau. Áp một luật cho cả ba sẽ hoặc mất dữ liệu, hoặc chặn việc hợp lệ | PO + phân tích | Bước 7 |
| 06/10/2026 | **`OQ-37` ✅ Người có khoá mà CHƯA HỌC: hệ thống TỰ xoá khỏi các khoá đó rồi thêm vào nhóm mới**, không hỏi ai | Chưa học thì không mất gì. Bắt người vận hành bấm tay cho từng trường hợp là việc thừa | PO | Bước 7 |
| 06/10/2026 | **`OQ-38` ✅ Thông báo cho QUẢN LÝ qua email hệ thống.** Tạm thời chỉ quản lý, chưa gửi L&D | Dùng hạ tầng mail sẵn có | PO | Bước 7 |
| 06/10/2026 | **Bổ sung một mail event mới cho `US20`.** 30 mail tự động hiện có không có cái nào cho việc này, nên làm mới. Mã tham chiếu trong tài liệu: `MAIL-GRP-01` | PO: *"chưa có thì bổ sung thôi"*. Không chọn cách ghép vào mail sẵn có — nội dung và người nhận khác hẳn | PO | Bước 7 |

