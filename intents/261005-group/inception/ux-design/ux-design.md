---
intent: 261005-group
artifact: ux-design
feature: LMS-F002
owner: Design PIC
version: 0.2
status: draft
inputs: prd@0.8
---
# UX Design: Nhóm học viên (Group)

## 1. Danh sách màn
Portal UpLMS Ops trừ khi ghi khác. Ops thiết kế ở desktop 1920; SCR24 và SCR25 thêm bản 375. UpLMS thiết kế ở 1920 và 375. Chữ giao diện tiếng Anh; bản tiếng Anh của chuỗi trong PRD do Design dịch, giữ nguyên ý.

| SCR | Tên màn | Mới hoặc sửa | US | Figma |
|---|---|---|---|---|
| SCR1 | Danh sách nhóm, dạng Cây và Bảng (page, Organization › Learner Groups) | Mới | US6 xem danh sách nhóm · US2 di chuyển nhánh · US5 nhãn nhóm đồng bộ · US13 nhãn chưa có quản lý · US14 ẩn nhóm lưu trữ |  |
| SCR2 | Tạo nhóm, sửa nhóm (drawer bên phải) | Mới | US1 tạo và sửa nhóm · US2 đổi nhóm cha |  |
| SCR3 | Xác nhận di chuyển nhánh (hộp xác nhận) | Mới | US2 di chuyển nhánh |  |
| SCR4 | Chi tiết nhóm: đầu trang, khối thông tin, thao tác nhóm (page, Learner Groups › tên nhóm, có bốn tab) | Mới | US1 sửa nhóm · US5 nhóm đồng bộ · US14 lưu trữ, khôi phục, xoá |  |
| SCR5 | Xác nhận lưu trữ nhóm, xác nhận xoá nhóm (hộp xác nhận, hai biến thể) | Mới | US14 lưu trữ nhóm |  |
| SCR6 | Chi tiết nhóm, tab Members (tab của SCR4) | Mới | US3 thêm gỡ thủ công · US4 nhập tệp · US5 nhóm đồng bộ khoá thành viên |  |
| SCR7 | Thêm thành viên (modal lớn, cùng mẫu màn Add Student của lớp) | Mới | US3 thêm thành viên |  |
| SCR8 | Xác nhận gỡ thành viên (hộp xác nhận, hai biến thể) | Mới | US3 gỡ thành viên · US20 báo quản lý |  |
| SCR9 | Nhập tệp thành viên và kết quả (modal và hộp kết quả, cùng mẫu Import Student của lớp) | Mới | US4 thêm gỡ theo lô |  |
| SCR10 | Log nhập tệp (page, cùng mẫu View Log của lớp) | Mới | US4 xem log lỗi |  |
| SCR11 | Chi tiết nhóm, tab Assigned Classes (tab của SCR4) | Mới | US7 giao nội dung · US8 công tắc tự ghi danh |  |
| SCR12 | Giao nội dung cho nhóm (modal rộng, có khối xem trước) | Mới | US7 giao nội dung |  |
| SCR13 | Xác nhận bật, tắt tự ghi danh; xác nhận bật Cascade to sub-groups (hộp xác nhận, ba biến thể) | Mới | US8 bật tắt tự ghi danh · US7 chảy xuống nhánh con sau khi giao |  |
| SCR14 | Chi tiết nhóm, tab People in Charge (tab của SCR4) | Mới | US9 gán quản lý · US10 kế thừa quản lý · US12 gán mentor · US13 cảnh báo trống quản lý |  |
| SCR15 | Gán quản lý, gán mentor (modal chọn nhiều người, hai chế độ) | Mới | US9 gán quản lý · US12 gán mentor |  |
| SCR16 | Chi tiết nhóm, tab Report (tab của SCR4) | Mới | US18 báo cáo theo nhóm ở thời điểm hiện tại |  |
| SCR17 | Nhật ký thay đổi thành viên (page, mở từ SCR4 hoặc SCR18 với bộ lọc chọn sẵn) | Mới | US15 tra nhật ký · US19 dấu vết tự gỡ |  |
| SCR18 | Student Profile, tab Overview (page có sẵn, User Management › Students › Student Profile) | Sửa | US10 ba loại quản lý · US11 quản lý chính · US13 chuyển phụ trách · US15 lối vào nhật ký |  |
| SCR19 | Chỉ định, thay quản lý chính (modal chọn một người) | Mới | US11 quản lý chính |  |
| SCR20 | Chuyển toàn bộ phụ trách (modal rộng: chọn người nhận, xem trước, xác nhận) | Mới | US13 chuyển phụ trách |  |
| SCR21 | Class Detail, tab Students (tab có sẵn của Class Detail) | Sửa | US7 dòng vượt sức chứa |  |
| SCR22 | Class Detail, tab Mentors (tab có sẵn của Class Detail) | Sửa | US12 mentor phụ trách nhóm, người chịu trách nhiệm chính |  |
| SCR23 | Khung UpLMS Ops cho tài khoản học viên (khung app: sidebar và header theo vai) | Sửa | US16 quản lý chỉ thấy màn theo dõi · US12 mentor chỉ thấy màn chấm bài |  |
| SCR24 | My Team, theo dõi nhánh (page, màn duy nhất của quản lý trên Ops; 1920 và 375) | Mới | US16 quản lý theo dõi nhánh |  |
| SCR25 | Hồ sơ học viên mở từ My Team (page, chỉ xem; 1920 và 375) | Mới, bản chỉ xem của SCR18 | US16 xem toàn bộ dữ liệu học của một người |  |
| SCR26 | Sidebar UpLMS Ops, mục Organization (khung app của nhân sự vận hành) | Sửa | US6 lối vào danh sách nhóm |  |
| SCR27 | UpLMS, hồ sơ học viên, khối My Managers (khối trên trang hồ sơ có sẵn của UpLMS; 1920 và 375) | Sửa | US17 học viên xem quản lý |  |
| SCR28 | Email MAIL-GRP-02, được gán phụ trách (email) | Mới | US9 · US11 · US13 email cho người được gán |  |
| SCR29 | Email MAIL-GRP-01, người rời nhóm còn khoá đang học (email, hai biến thể: gửi quản lý; gửi quản trị viên hệ thống) | Mới | US20 báo quản lý |  |
| SCR30 | Tạo, sửa thông báo: ô Recipient groups (page có sẵn của Engagement & Support) | Sửa | US21 thông báo gửi theo nhóm |  |
| SCR31 | Chi tiết thông báo: khối Selected groups (page có sẵn) | Sửa | US21 thông báo gửi theo nhóm |  |
| SCR32 | Danh sách thông báo: bộ lọc Group (page có sẵn) | Sửa | US21 thông báo gửi theo nhóm |  |
| SCR33 | Form nhân sự vận hành: bỏ Department và Business unit (form có sẵn của Staff) | Sửa | Phạm vi: bỏ phòng ban của nhân sự (PRD mục 8) |  |
| SCR34 | Form support group: bỏ trường phòng ban (form có sẵn của Engagement & Support) | Sửa | Phạm vi: bỏ phòng ban của nhân sự (PRD mục 8) |  |

US19 tự gỡ khoá chưa học không có màn riêng; dấu vết hiện ở SCR17 với lý do Transferred. US22 báo cáo tại một mốc quá khứ để đợt sau, chưa thiết kế ở đợt này.

## 2. Luồng và tương tác
### Nhân sự vận hành
```mermaid
flowchart LR
  NAV[SCR26 Sidebar · Organization] -->|Learner Groups| L[SCR1 Danh sách nhóm]
  L -->|Create group| C[SCR2 Tạo nhóm]
  C -->|Save| D[SCR4 Chi tiết nhóm]
  C -->|mã trùng, tên trống| C
  L -->|kéo thả nhánh| MV[SCR3 Xác nhận di chuyển]
  MV -->|Move| L
  L -->|thả vào chính nó hoặc nhánh con| L
  L -->|bấm tên nhóm| D
  D -->|Edit, nhóm tự tạo| C
  D -->|Archive, Delete| AR[SCR5 Xác nhận lưu trữ, xoá]
  AR -->|Archive| D
  AR -->|Delete| L
  D --> M[SCR6 tab Members]
  M -->|Add members| AM[SCR7 Thêm thành viên]
  M -->|Remove| RM[SCR8 Xác nhận gỡ]
  M -->|Import| IM[SCR9 Nhập tệp]
  IM -->|View log| LOG[SCR10 Log nhập tệp]
  D --> A[SCR11 tab Assigned Classes]
  A -->|Assign classes| AS[SCR12 Giao nội dung]
  A -->|bật, tắt công tắc| TG[SCR13 Xác nhận tự ghi danh]
  D --> P[SCR14 tab People in Charge]
  P -->|Assign manager, Assign mentor| PK[SCR15 Chọn người]
  D --> R[SCR16 tab Report]
  D -->|Membership log| H[SCR17 Nhật ký]
  SP[SCR18 Student Profile] -->|Set primary manager| PM[SCR19 Chọn quản lý chính]
  SP -->|Transfer all responsibilities| TR[SCR20 Chuyển phụ trách]
  SP -->|Membership log| H
  SP -->|bấm nhóm trong khối Groups| D
```

### Quản lý, mentor, học viên và email
```mermaid
flowchart LR
  E2[SCR28 Email được gán phụ trách] -->|Open My Team| T[SCR24 My Team]
  LOGIN[Đăng nhập Ops bằng tài khoản học viên] --> SH[SCR23 Khung theo vai]
  SH -->|vai quản lý| T
  SH -->|vai mentor| G[Màn chấm bài có sẵn]
  T -->|bấm một người| PV[SCR25 Hồ sơ chỉ xem]
  E1[SCR29 Email người rời nhóm còn khoá, bản gửi quản trị viên] -->|View profile| SP[SCR18 Student Profile]
  E1M[SCR29 bản gửi quản lý, không có đường dẫn] -.->|quản lý báo vận hành| SP
  SP -->|vận hành gỡ khỏi lớp| CD[Class Detail có sẵn]
  NL[SCR32 Danh sách thông báo] -->|Create| NC[SCR30 Tạo thông báo, chọn nhóm]
  NL -->|bấm một thông báo| ND[SCR31 Chi tiết thông báo]
  U[UpLMS · Hồ sơ] --> MM[SCR27 My Managers]
```

### Điều hướng và hành vi theo user story
- US1, US2: tạo nhóm từ SCR1 mở drawer SCR2; lưu xong mở SCR4 của nhóm vừa tạo. Sửa từ SCR4 mở SCR2 với mã nhóm khoá. Đổi nhóm cha trong SCR2 chạy cùng bộ kiểm tra như kéo thả và đi qua SCR3. Nhóm đồng bộ không có nút Edit, không kéo được trên cây.
- US2 kéo thả trên SCR1: chỉ ở dạng Cây. Rê qua một nhóm hợp lệ thì dòng đó có viền màu thành công; rê qua chính nó, nhánh con của nó hoặc nhóm khác nguồn thì viền màu lỗi kèm một dòng lý do cạnh con trỏ. Thả hợp lệ mở SCR3, thả không hợp lệ không làm gì.
- US3, US4: SCR6 có hai nút Add members và Import; chọn dòng thì hiện thanh thao tác Remove. Gỡ luôn đi qua SCR8; có người đang học nội dung giao qua nhóm thì SCR8 ở biến thể cảnh báo, nêu số người và việc quản lý sẽ nhận email.
- US7, US8: SCR11 liệt kê lớp đã giao, mỗi dòng có hai công tắc Cascade to sub-groups và Auto-enroll. Đổi Auto-enroll mở SCR13. Bật Cascade mở SCR13 biến thể Cascade nêu số người ở nhánh con sẽ vào lớp; tắt Cascade lưu ngay, thông báo không ai bị gỡ. Xác nhận thì lưu ngay, không cần nút Save. Khi cờ giao nội dung của tổ chức còn tắt, Assign classes khoá kèm dòng giải thích. Assign classes mở SCR12; khối xem trước cập nhật mỗi khi chọn lớp hoặc đổi công tắc Cascade to sub-groups.
- US9, US10, US12, US13: SCR14 có ba khối: Managers, Mentors, và khối kế thừa khi nhóm chưa gán quản lý. Nhóm trống quản lý có Alert cảnh báo ở đầu tab và nhãn No manager ở SCR1.
- US11, US13: trên SCR18, khối Managers có nút Set primary manager (thành Change primary manager khi đã có) và Remove primary manager; khối Responsibilities chỉ hiện khi người đó đang quản lý hoặc làm mentor của ít nhất một nhóm, có nút Transfer all responsibilities mở SCR20.
- US14: SCR4 hiện Delete khi nhóm chưa từng có thành viên, chưa từng được giao nội dung và không có nhóm con; còn lại hiện Archive và một dòng giải thích lý do không xoá được. Nhóm đồng bộ không có Archive. Nhóm đang lưu trữ chỉ còn Restore, mọi nút sửa khác ẩn; Restore ở nhóm cha khôi phục cả nhánh đã lưu trữ cùng lần; nhóm con mà nhóm cha còn lưu trữ thì không có Restore.
- US15: SCR17 mở từ SCR4 với bộ lọc Group chọn sẵn, từ SCR18 với bộ lọc Person chọn sẵn; mới nhất lên đầu.
- US16: quản lý đăng nhập Ops thấy khung rút gọn SCR23, vào thẳng SCR24. Bản 375 chuyển bảng thành danh sách thẻ, mỗi thẻ một người, số khoá quá hạn nổi bật.
- US17: SCR27 là khối mới trên trang hồ sơ UpLMS, chỉ đọc.
- US18: SCR16 tính ở thời điểm hiện tại, chưa có ô chọn mốc; Segmented chọn View by: Members, Sub-groups, Courses, mặc định Members.
- US20: email SCR29 gửi quản lý liệt kê đủ khoá và tình trạng, không có đường dẫn hồ sơ; bản gửi quản trị viên hệ thống có nút View profile mở SCR18. Quản lý quyết xong thì báo nhân sự vận hành; vận hành gỡ khỏi lớp ở Class Detail như hiện nay.
- US21: SCR30 thêm ô chọn nhiều Recipient groups, mỗi dòng có tên, đường dẫn từ gốc, số người nhận tính cả nhánh con; SCR31 có khối Selected groups với trạng thái từng nhóm; SCR32 thêm bộ lọc Group.
- Tài khoản đã khoá: vẫn hiện trong danh sách quản lý, mentor của SCR14 với Tag Locked và dòng phụ "Not counted while locked"; không tính khi xét nhóm trống quản lý và kế thừa.
- Bỏ phòng ban của nhân sự: SCR33, SCR34 bỏ trường phòng ban và đơn vị kinh doanh khỏi form và khỏi bảng liên quan.

### State của từng màn
| SCR | Default | Empty | Loading | Success | Error | Disabled | Permission |
|---|---|---|---|---|---|---|---|
| SCR1 | Có, cây gấp ở cấp gốc; bảng 20 dòng | Có ba trường hợp: chưa có nhóm nào (nút Create group); tìm không ra; lọc không ra | Có: tải danh sách; tải nhánh khi mở mũi tên (spinner tại dòng) | Có: thông báo sau khi di chuyển nhánh, sau khi xoá nhóm | Có: lỗi tải danh sách; lỗi tải một nhánh (thử lại tại dòng) | Có: nhóm đồng bộ không kéo được; nhóm lưu trữ chữ xám khi bật hiện | Có: chỉ có quyền xem thì ẩn Create group và tắt kéo thả |
| SCR2 | Có | Không: form luôn có trường | Có: đang lưu | Có: đóng drawer, mở SCR4, thông báo đã tạo hoặc đã lưu | Có: tên trống, tên quá 255 ký tự, mô tả quá 1000 ký tự, mã trùng, lỗi lưu | Có: nút Save mờ khi thiếu trường bắt buộc; ô mã khoá khi sửa | Không: chỉ mở được khi có quyền quản lý nhóm |
| SCR3 | Có: tên nhánh, số nhóm con, số người bị ảnh hưởng, cha cũ và mới | Không: luôn có nội dung | Có: đang di chuyển | Có: đóng hộp, cây cập nhật | Có: lỗi khi di chuyển, giữ nguyên vị trí cũ | Không: chỉ mở khi thả hợp lệ | Không: chỉ mở khi có quyền |
| SCR4 | Có: nhóm tự tạo đang dùng | Không: tab bên dưới tự xử lý rỗng | Có | Có: sau lưu trữ, khôi phục | Có: lỗi tải; nhóm không tồn tại hoặc đã xoá | Có: nhóm đồng bộ ẩn Edit, Move, Archive, Delete kèm dòng giải thích; nhóm lưu trữ chỉ còn Restore, nhóm con có nhóm cha lưu trữ không có Restore; nhóm có lịch sử hoặc có nhóm con không có Delete | Có: chỉ xem thì ẩn mọi nút thao tác |
| SCR5 | Có: Archive nêu số thành viên, số lớp đang giao, số nhóm con bị lưu trữ theo, hệ quả; Delete nêu không khôi phục được | Không | Có | Có | Có: lỗi khi lưu trữ, xoá | Không | Không |
| SCR6 | Có: bảng thành viên, ẩn người đã nghỉ | Có: nhóm chưa có thành viên (nút Add members, Import); lọc không ra | Có | Có: sau thêm, gỡ | Có: lỗi tải; lỗi khi gỡ | Có: nhóm đồng bộ ẩn Add, Import, Remove, thay bằng dòng giải thích; nhóm lưu trữ ẩn thao tác | Có: chỉ xem thì ẩn thao tác |
| SCR7 | Có: bảng người, ô tìm theo tên, mã nhân viên, email | Có: tìm không ra | Có | Có: đóng modal, SCR6 cập nhật, thông báo đã thêm N người | Có: lỗi tải, lỗi khi thêm | Có: người đã trong nhóm hiện mờ, nhãn Already in group, không chọn được; nút Add mờ khi chưa chọn ai | Không: chỉ mở khi có quyền |
| SCR8 | Có, hai biến thể: không ai đang học; có người đang học (cảnh báo, quản lý nhận email) | Không | Có | Có | Có | Không | Không |
| SCR9 | Có: chọn hành động, tải mẫu, vùng kéo thả tệp | Không | Có: đang tải lên, đang xử lý | Có: hộp kết quả Processed N rows | Có: sai định dạng, nhiều tệp, tệp rỗng, lỗi tải lên | Có: vùng tải lên khoá khi chưa chọn hành động | Không |
| SCR10 | Có: bảng dòng lỗi, trường lỗi bôi đỏ, cột Error reason | Có: không có dòng lỗi | Có | Không: chỉ đọc | Có: lỗi tải | Không: chỉ đọc | Không |
| SCR11 | Có: bảng lớp đã giao, công tắc trên dòng | Có: nhóm chưa được giao lớp nào (nút Assign classes) | Có | Có: sau giao lớp, sau gỡ lớp, sau đổi công tắc | Có: lỗi tải; lỗi khi đổi công tắc thì công tắc quay về trạng thái cũ | Có: lớp đã có học viên từ nhóm thì không có Remove, thay bằng dòng giải thích; nhóm lưu trữ khoá công tắc và nút; cờ giao nội dung của tổ chức tắt thì Assign classes khoá kèm dòng giải thích | Có: chỉ xem thì công tắc chỉ đọc |
| SCR12 | Có: chọn lớp, hai công tắc, khối xem trước | Có: không có lớp nào đang nhận học viên; tìm không ra | Có: tải lớp; tính lại khối xem trước | Có: đóng modal, SCR11 cập nhật | Có: lỗi tải, lỗi khi giao | Có: nút Assign mờ khi chưa chọn lớp | Không |
| SCR13 | Có, ba biến thể: bật Auto-enroll khi có N người chưa vào lớp; tắt Auto-enroll; bật Cascade nêu số người nhánh con sẽ vào lớp | Không | Có | Có | Có: lỗi lưu, công tắc quay về | Không | Không |
| SCR14 | Có: quản lý gán trực tiếp, mentor; người bị khoá có Tag Locked, không tính | Có ba trường hợp: chưa gán, đang kế thừa (khối kế thừa); trống quản lý (cảnh báo); chưa có mentor | Có | Có | Có | Có: nhóm lưu trữ ẩn nút gán | Có: chỉ xem thì ẩn nút gán, gỡ |
| SCR15 | Có: tìm theo tên, email, chọn nhiều | Có: tìm không ra | Có | Có | Có | Có: người đã là quản lý, mentor của nhóm hiện mờ; nút Assign mờ khi chưa chọn | Không |
| SCR16 | Có: thời điểm hiện tại, View by Members | Có: nhóm chưa có thành viên hoặc chưa được giao; View by Sub-groups với nhóm không có nhóm con | Có: đang tính báo cáo, không chặn màn | Không: chỉ đọc | Có: lỗi tính báo cáo | Không: chưa có ô chọn mốc ở đợt này | Có: chỉ xem vẫn xem được |
| SCR17 | Có | Có: lọc không ra | Có | Không: chỉ đọc | Có | Không: chỉ đọc, không sửa xoá dòng | Có: cần quyền xem nhật ký nhóm |
| SCR18 | Có: thêm ba khối Groups, Managers, Responsibilities | Có: Not in any group; chưa có quản lý; khối Responsibilities ẩn khi không phụ trách gì | Có | Có: sau chỉ định, gỡ quản lý chính, sau chuyển phụ trách | Có | Không: dữ liệu đồng bộ vẫn chỉ định được quản lý chính | Có: chỉ xem thì ẩn nút |
| SCR19 | Có | Có: tìm không ra | Có | Có | Có | Có: không chọn được chính học viên đó (giả định, PRD câu hỏi mở #12) | Không |
| SCR20 | Có: chọn người nhận, danh sách sẽ chuyển, số nhóm, số người, người nhận | Không: chỉ mở khi có phụ trách | Có | Có: thông báo đã chuyển | Có | Có: nút Transfer mờ khi chưa chọn người nhận; không chọn được chính người đang chuyển | Không |
| SCR21 | Có: thêm dòng vượt sức chứa ở đầu danh sách | Không: không đổi màn có sẵn | Không: không đổi | Không: không đổi | Không: không đổi | Không: dòng chỉ thông báo, không khoá thao tác nào | Không: không đổi |
| SCR22 | Có: thêm cột Group in charge, nhãn Main responsible | Không: không đổi | Không: không đổi | Có: sau đổi người chịu trách nhiệm chính | Không: không đổi | Không: không đổi | Không: không đổi |
| SCR23 | Có ba biến thể: chỉ quản lý; chỉ mentor; vừa quản lý vừa mentor | Không | Không: theo khung có sẵn | Không | Có: tài khoản học viên không có vai nào trên Ops thì hiện trang không có quyền | Không | Có: đây chính là màn phân quyền theo vai |
| SCR24 | Có, 1920 và 375 | Có: chưa có ai trong nhánh; lọc không ra | Có | Không: chỉ đọc | Có | Không | Có: bị thu hồi quyền quản lý khi đang xem (chờ Dev đề xuất, PRD câu hỏi mở #7) |
| SCR25 | Có, 1920 và 375 | Có: người chưa có khoá nào | Có | Không: chỉ đọc | Có: người không còn trong nhánh | Không | Có: ẩn Edit Profile, tab Setting, Security; chỉ xem dữ liệu học |
| SCR26 | Có | Không | Không | Không | Không | Không | Có: mục chỉ hiện với người có quyền xem nhóm |
| SCR27 | Có, 1920 và 375 | Có: No manager information yet | Có | Không: chỉ đọc | Có | Không | Không: học viên nào cũng xem được khối của mình |
| SCR28 | Có: một nhóm; một hồ sơ; gộp nhiều nhóm khi nhận chuyển phụ trách | Không | Không: email | Không | Không | Không | Không |
| SCR29 | Có: một khoá; nhiều khoá; bản gửi quản lý không có nút, bản gửi quản trị viên có View profile | Không | Không: email | Không | Không | Không | Không |
| SCR30 | Có: ô Recipient groups có tìm | Có: tìm không ra; chưa có nhóm nào | Có: tải nhóm | Có: lưu thông báo như hiện có | Có: lỗi tải nhóm | Có: nhóm lưu trữ không có trong ô chọn | Không: theo quyền thông báo hiện có |
| SCR31 | Có: khối Selected groups | Có: thông báo không chọn nhóm | Không: theo màn có sẵn | Không: chỉ đọc | Không: theo màn có sẵn | Có: nhóm đã lưu trữ hiện Tag Archived | Không: theo quyền hiện có |
| SCR32 | Có: thêm bộ lọc Group | Có: lọc không ra | Không: theo màn có sẵn | Không | Không: theo màn có sẵn | Không | Không: theo quyền hiện có |
| SCR33 | Có: form không còn Department, Business unit | Không | Không: theo form có sẵn | Không: theo form có sẵn | Không: theo form có sẵn | Không | Không |
| SCR34 | Có: form không còn trường phòng ban | Không | Không: theo form có sẵn | Không: theo form có sẵn | Không: theo form có sẵn | Không | Không |

### Trường hợp biên bắt buộc
| EC | Màn | Tình huống | Cách giao diện xử lý |
|---|---|---|---|
| EC-01 | SCR1 | Kéo một nhóm vào chính nó hoặc nhánh con của nó | Viền màu lỗi, dòng lý do "Can't move a group into its own sub-group", thả không có tác dụng |
| EC-02 | SCR1 | Kéo nhóm tự tạo vào nhóm đồng bộ, hoặc nhóm đồng bộ đi đâu | Nhóm đồng bộ không có tay kéo; thả vào nhóm khác nguồn hiện viền lỗi kèm lý do khác nguồn |
| EC-03 | SCR1 | Kết quả tìm là nhóm con sâu | Kết quả hiện đường dẫn từ gốc, cắt giữa khi quá dài, đầy đủ trong tooltip |
| EC-04 | SCR1 | Cây hàng chục nhóm, tên dài | Tải theo nhánh, tên cắt một dòng kèm tooltip, số thành viên căn phải |
| EC-05 | SCR2 | Chọn nhóm cha là nhóm lưu trữ hoặc nhóm đồng bộ | Không xuất hiện trong ô chọn |
| EC-06 | SCR4 | Mở đường dẫn tới một nhóm đã bị xoá | Trang Not found kèm nút về danh sách nhóm |
| EC-07 | SCR5 | Lưu trữ nhóm cha có nhánh con | Hộp xác nhận nêu số nhóm con bị lưu trữ theo và người đang học vẫn học tiếp |
| EC-08 | SCR5 | Xoá nhóm | Chỉ hiện khi chưa có lịch sử và không có nhóm con; hộp xác nhận nói rõ không khôi phục được, focus vào Cancel |
| EC-09 | SCR6, SCR8 | Gỡ nhiều người, có người đang học, có người đã nghỉ việc | Một hộp xác nhận nêu tổng số người gỡ và số người đang học; người đã nghỉ gỡ được, không đổi lượt ghi danh |
| EC-10 | SCR6 | Người thuộc nhóm con (vào gián tiếp) | Bộ lọc Direct or sub-group; người thuộc nhóm con không chọn để gỡ ở nhóm cha, vì thành viên chỉ ở nhóm sâu nhất |
| EC-11 | SCR7 | Thêm người đã ở trong nhóm | Hiện mờ, nhãn Already in group, không chọn được |
| EC-12 | SCR9 | Tệp có dòng hợp lệ và dòng lỗi ba loại | Dòng hợp lệ vẫn xử lý; hộp kết quả nêu thành công và lỗi; log ghi ba lý do riêng |
| EC-13 | SCR9 | Gỡ qua tệp người đang học | Như gỡ tay: vẫn gỡ, quản lý nhận email; hộp kết quả nêu số người đang học đã báo quản lý |
| EC-14 | SCR11 | Gỡ lớp đã có người trong nhóm học | Không có nút Remove, dòng "This class already has learners from this group and can't be removed" |
| EC-15 | SCR11 | Lớp đã giao nay đã kết thúc | Dòng lớp có nhãn Ended; công tắc Auto-enroll vẫn hiện nhưng người vào sau không được thêm (luật đứng dừng im lặng); tooltip giải thích |
| EC-16 | SCR12 | Nhóm cha không có thành viên trực tiếp, nhánh con có người, công tắc Cascade tắt | Khối xem trước ghi 0 người sẽ vào lớp và gợi ý bật Cascade to sub-groups |
| EC-17 | SCR12 | Giao cho nhóm lớn, lớp có Foundation | Khối xem trước nêu số người; giao chạy nền, modal đóng ngay, thông báo khi xong |
| EC-18 | SCR13 | Bật công tắc khi có N người chưa vào lớp | Hai lựa chọn Enroll now và Only apply to new members; N bằng 0 thì bật thẳng, không hỏi |
| EC-19 | SCR14 | Nhóm đang kế thừa, vận hành gán riêng một người | Khối kế thừa biến mất, danh sách chỉ còn người gán riêng |
| EC-20 | SCR14 | Gán quản lý cho người đang là thành viên của chính nhóm | Gán được, người đó giữ tư cách thành viên |
| EC-21 | SCR16 | Báo cáo tại mốc quá khứ | Chuyển sang US22, đợt sau; đợt này không có ô chọn mốc |
| EC-22 | SCR18 | Học viên có thông tin đồng bộ, không sửa được trên Ops | Nút chỉ định quản lý chính vẫn hiện, vẫn làm được |
| EC-23 | SCR20 | Người nhận đã quản lý sẵn một số nhóm | Danh sách xem trước đánh dấu nhóm người nhận đã quản lý; email chỉ liệt nhóm mới |
| EC-24 | SCR23 | Một tài khoản vừa là quản lý vừa là mentor | Sidebar có hai mục My Team và Grading; vào mặc định My Team |
| EC-25 | SCR24 | Quản lý hàng trăm người, người thuộc hai nhánh | Phân trang; một người một dòng, cột Group liệt kê các nhóm trong phạm vi của quản lý |
| EC-26 | SCR27 | Học viên vừa là thành viên vừa là quản lý nhóm mình | Không hiện chính họ, hiện quản lý cấp gần nhất (theo đề xuất ở PRD câu hỏi mở #12) |
| EC-27 | Mọi màn có danh sách người | Tài khoản kiểm thử | Không xuất hiện ở bảng, ô tìm, con số, báo cáo |
| EC-28 | SCR4 | Nhóm chưa có lịch sử nhưng có nhóm con | Không có Delete; dòng "Delete or move its sub-groups first" |
| EC-29 | SCR4 | Mở nhóm con trong khi nhóm cha đang lưu trữ | Không có Restore; dòng "Restore the parent group to restore this one" |
| EC-30 | SCR14, SCR1 | Quản lý duy nhất của nhóm và mọi nhóm cha bị khoá | Người đó hiện Tag Locked; nhóm mang nhãn No manager và cảnh báo trống quản lý |
| EC-31 | SCR11, SCR12 | Cờ giao nội dung của tổ chức còn tắt | Assign classes khoá, dòng "Assigning classes to groups isn't turned on for your organization yet" |
| EC-32 | SCR30 | Một người thuộc nhiều nhóm được chọn | Số người nhận đếm không trùng; người đó nhận một thông báo |
| EC-33 | SCR30 | Nhóm 0 người nhận; nhóm bị lưu trữ trước khi gửi | Chờ PO có luật (mục 7) |

Flow prototype khung xám: `flow-prototype.html` cùng thư mục, mở bằng trình duyệt, ba luồng: Danh sách nhóm và kéo thả, Giao nội dung và công tắc tự ghi danh, Chuyển toàn bộ phụ trách.

## 3. Thành phần giao diện
Tên component theo UpBase Design System, thư viện gốc mà kit UpLMS Ops dựng lên; đối chiếu lại với kit Ops khi dựng UI.

| Vùng | Component của UI kit | Ghi chú |
|---|---|---|
| Khung app Ops | App Shell: sidebar thu gọn, Breadcrumb, Page Header | Như màn Ops hiện có |
| Cây nhóm (SCR1) | Tree, Tree Item có Holder Icon để kéo | Dòng cây cần thêm số thành viên, Tag nguồn, Tag No manager |
| Bảng nhóm, thành viên, lớp đã giao, nhật ký, báo cáo, My Team | Table, Pagination | 20 dòng mỗi trang |
| Đổi dạng xem Cây, Bảng; View by của báo cáo | Segmented | |
| Ô tìm, bộ lọc | Input / Search, Select, DatePicker (khoảng ngày cho nhật ký) | |
| Ô chọn nhóm người nhận (SCR30) | Select chọn nhiều có tìm, dòng gồm tên, đường dẫn từ gốc, số người nhận | |
| Nhãn nguồn, trạng thái, Already in group, No manager, Archived, Ended, Primary | Tag / Basic, Tag / Status | Tag Success và Warning thiếu tương phản ở UpBase (đã ghi nhận ở kit UpLMS); dùng Default hoặc kèm chữ |
| Tab của chi tiết nhóm, Student Profile | Tabs / Basic | |
| Form tạo, sửa nhóm | Drawer, Form / Form Item / Vertical, Input, Textarea, Select có tìm | Drawer như bản FE đã dựng |
| Modal và hộp xác nhận | Modal / Basic, Modal / Confirmation | |
| Công tắc Auto-enroll, Cascade, Show archived, Show former employees | Switch / Basic | |
| Nhập tệp | Upload / Drag and Drop, Radio Group cho hành động | Theo mẫu Import Student |
| Cảnh báo trống quản lý, dòng vượt sức chứa, dòng giải thích nhóm đồng bộ | Alert | |
| Danh sách người trong khối, quản lý, mentor | Avatar, Listy / List Item | |
| Khối xem trước (SCR12, SCR20) | Statistic, Alert, Table | Ghép, chưa có mẫu trong app |
| Trạng thái rỗng | Empty, Result 403 cho trang không có quyền | |
| Thẻ người trên 375 (SCR24) | Card | Mẫu mới trên Ops |

Component kit chưa có:
| Mã | Cần gì | Màn | Xử lý tạm | Đề xuất bổ sung kit |
|---|---|---|---|---|
| K1 | Trạng thái vị trí thả hợp lệ và không hợp lệ của dòng cây, kèm dòng lý do | SCR1 | Viền màu thành công hoặc lỗi trên Tree Item, dòng lý do bằng Tooltip | Thêm state Drop target valid, invalid cho Tree Item |
| K2 | Dòng cây có cột phụ: số thành viên, nhãn | SCR1 | Ghép Tree Item với Tag và chữ số căn phải | Thêm vùng Extra bên phải Tree Item |
| K3 | Khối xem trước số người trước khi xác nhận | SCR12, SCR20 | Ghép Statistic, Alert, Table | Đề xuất component Preview Summary nếu dùng lại ở nơi khác |
| K4 | Thẻ người cho danh sách trên điện thoại ở Ops | SCR24 | Card với Avatar và Statistic nhỏ | Đề xuất khi có bản mobile thứ hai trên Ops |

Bốn đề xuất này gửi người phụ trách kit UpLMS Ops; trong lúc chờ, màn dùng cách xử lý tạm.

## 4. Accessibility
Mức WCAG 2.2 AA (mặc định khi sản phẩm chưa chốt). Điểm cần lưu ý:
- SCR1: kéo thả có cách làm bằng bàn phím thay thế: đổi nhóm cha trong SCR2. Cây điều hướng được bằng phím mũi tên, Enter mở nhánh. Vị trí thả không chỉ dựa vào màu, luôn có dòng lý do.
- Mọi công tắc có nhãn chữ đi cùng; trạng thái bật tắt đọc được bằng trình đọc màn hình.
- Tag trạng thái có chữ, không chỉ màu. Tránh Tag Success, Warning cho chữ nhỏ cho tới khi UpBase sửa tương phản.
- Hộp xác nhận: focus vào nút an toàn (Cancel) khi mở với thao tác xoá, lưu trữ; Esc đóng hộp.
- Bảng: tiêu đề cột sắp xếp được có trạng thái sắp xếp đọc được; ô có nút chỉ icon có nhãn ẩn.
- Bản 375 (SCR24, SCR25, SCR27): vùng chạm tối thiểu 24 x 24 px theo AA, khuyến nghị 44 x 44 px cho nút chính; tên tiếng Việt có dấu đủ chiều cao dòng.
- Thông báo kết quả (đã thêm, đã chuyển) đọc được bằng trình đọc màn hình.

## 5. Ý kiến về PRD
Đồng ý với PRD bản 0.8. Các đề xuất trước của Design đã vào PRD. Đề xuất mới cho câu hỏi mở #20:

| Mã | Lập trường | Nội dung | Lý do |
|---|---|---|---|
| US1 · câu hỏi mở #20 | Đề xuất sửa | Mã nhóm tối đa 50 ký tự; chỉ chữ không dấu, số, gạch nối, gạch dưới; không dấu cách; không phân biệt hoa thường khi kiểm trùng | Mã hiện ở đường dẫn, tệp nhập, báo cáo; mã nhóm đồng bộ lấy từ mã phòng ban |
| US4 · câu hỏi mở #20 | Đề xuất sửa | Tệp nhập thành viên tối đa 1.000 dòng mỗi lần; quá thì báo lỗi trước khi xử lý, không xử lý dòng nào. Tech PIC xác nhận con số theo khả năng xử lý | Nhóm đông nhất hiện là 55 người; User Guide của Import Student chưa ghi giới hạn |
| US3 · US6 · US9 · câu hỏi mở #20 | Đề xuất sửa | Tìm theo tên không phân biệt dấu tiếng Việt và hoa thường: "lan" tìm ra "Lân", "Lan" | Tên người và nhóm tiếng Việt có dấu, người dùng hay gõ không dấu |
| US6 · US16 · US18 · câu hỏi mở #20 | Đề xuất sửa | Phân trang: 20 dòng mỗi trang; có đúng 20 dòng thì một trang; đổi bộ lọc thì về trang 1 | Thống nhất với các danh sách Ops |

## 6. Rủi ro và câu hỏi cần chốt
Các câu 1 đến 9 của bản trước đã có quyết định của PO.

| # | Nội dung | Cần ai trả lời | Chặn |
|---|---|---|---|
| 1 | Nhóm 0 người nhận có chọn được trong ô Recipient groups không, và khi gửi thì báo gì | PO | Không |
| 2 | Nhóm đã chọn bị lưu trữ trước khi thông báo được gửi thì xử lý thế nào | PO | Không |
| 3 | Chức năng gửi thông báo trên UpLMS Ops đang bật hay chưa (ảnh hưởng thứ tự làm SCR30 đến SCR32) | Tech PIC | Không |
| 4 | Bị thu hồi quyền quản lý khi đang xem My Team thì màn xử lý thế nào | Dev | Không |
| 5 | Bốn giá trị đề xuất cho câu hỏi mở #20 ở mục 6 | PO | Không |
| 6 | File Figma và kit của UpLMS Ops; cần trước khi dựng UI | Design | Không, chặn bước dựng UI |
