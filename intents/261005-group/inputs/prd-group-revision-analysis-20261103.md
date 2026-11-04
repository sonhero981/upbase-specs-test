---
intent: 261005-group
artifact: change-impact-preview
status: draft
date: 2026-11-03
baseline: prd@0.8, approved 2026-10-26
---
# Rà soát đề nghị sửa PRD Group

Đây là bản phân tích và đề xuất để PO chốt trước khi mở sửa bản đã duyệt. Các Recommendation dưới đây chưa phải business rule có hiệu lực. PRD v0.8 và các file thiết kế của các team chưa thay đổi.

## 1. Phạm vi và nguồn

Yêu cầu của PO ngày 03/11/2026 gồm: xem xét Show archived; kiểm tra chuyển nhóm và thông báo khi có người học; làm rõ Already in class và khối xem trước; kiểm tra gỡ lớp khi có người học; làm rõ Enrolled via this group và Reason; xem lại thứ tự cột Member list.

Nguồn đã đối chiếu:

- `inception/prd/prd.md`: bản 0.8 đã duyệt, đặc biệt US2 di chuyển nhánh · US3 thêm gỡ thành viên · US6 xem danh sách nhóm · US7 giao lớp · US14 lưu trữ · US15 nhật ký · US19 xử lý lớp chưa học khi rời nhóm · US20 xử lý lớp đã có dữ liệu học khi rời nhóm.
- `inception/ux-design/ux-design.md`: luồng và trạng thái màn.
- `inception/ux-design/flow-prototype.html`: nhãn Enrolled via this group, cách tính khối xem trước và điều kiện hiện Remove.
- `inception/tech-design/be-technical-design.md`: thông tin đối chiếu thiết kế, không dùng để tự kết luận hành vi đã triển khai.
- `decisions.md`: các quyết định đã chốt; không có quyết định mới nào được suy từ yêu cầu rà soát này.
- Ảnh PO gửi: màn Assign classes có ba số Will be enrolled, Already in class, Skipped; chưa chọn lớp và cả ba bằng 0. Ảnh không có bảng Members hoặc cột Reason.

Fact trong tài liệu này là nội dung của đặc tả, không phải kết quả kiểm tra hệ thống đang chạy. Chưa dùng nguồn sống bên ngoài để khẳng định cơ chế hiện có của chức năng Lớp; nếu thay đổi đụng hành vi gỡ học viên của chức năng Lớp thì phải đối chiếu lại nguồn vùng đó.

## 2. Show archived

Fact: US6 xem danh sách nhóm quy định ẩn nhóm lưu trữ mặc định và có Show archived ở cả cây lẫn bảng. US14 lưu trữ nhóm cho phép mở nhóm lưu trữ để xem và Restore. Báo cáo theo mốc quá khứ đã được tách để sau nên chưa thể dùng làm lối tìm nhóm lưu trữ thay thế.

PO đã làm rõ bộ lọc hiện có chọn được Archived và xác nhận nguyên văn: “dạng cây sẽ áp dụng bộ lọc như dạng bảng”.

Hướng cập nhật: bỏ công tắc Show archived trùng chức năng; dạng cây và dạng bảng dùng chung bộ lọc Status. Recommendation về giá trị: Active · Archived · All, mặc định Active. Nhóm lưu trữ vẫn mở được để xem và khôi phục theo quyền; bộ lọc danh sách không làm nhóm lưu trữ xuất hiện trong ô chọn nhóm để giao lớp hoặc thêm quan hệ mới.

## 3. Chuyển nhóm: cần phân biệt hai thao tác

### 3.1. Di chuyển cả nhánh sang nhóm cha khác

Fact: US2 di chuyển nhánh cho phép di chuyển nhóm tự tạo đang dùng tới nhóm cha hợp lệ cùng nguồn. Không có điều kiện chặn vì đã có người học. Thành viên và nội dung đã giao giữ nguyên. Người hiện có trong nhánh không tự nhận lớp của nhóm cha mới. Người vào sau nhận lớp theo hai công tắc Cascade to sub-groups và Auto-enroll. Di chuyển được ghi vào nhật ký hệ thống, không tạo bản ghi vào hoặc rời nhóm.

PO xác nhận vẫn cho di chuyển nhánh khi đã có người học, giữ lượt ghi danh, tiến độ và kết quả; người hiện tại không tự nhận lớp của nhóm cha mới; quản lý kế thừa và phạm vi xem dữ liệu thay đổi theo vị trí mới.

Hộp xác nhận tiếng Anh:

> Move this branch from {A} to {B}? Existing enrollments, learning progress, and results will be preserved. Current members will not be automatically enrolled in classes assigned by the new parent group. Inherited managers and data access permissions will change based on the branch’s new location.

Recommendation: hộp xác nhận hiện thêm số nhóm con và số thành viên không trùng bị ảnh hưởng.

Thông báo thành công: `Group moved successfully.` Khi lỗi: `Couldn't move this group. No changes were saved.` Cây chỉ thể hiện vị trí mới khi thao tác thành công.

Open Question: người hiện có đang nhận lớp từ nhóm cha cũ còn được giữ nguồn giao đó không? Đề xuất giữ lượt ghi danh và tiến độ, dừng phát sinh ghi danh mới từ nhánh cha cũ sau di chuyển. Đồng thời cần chốt nguồn giao được hiển thị thế nào để không làm sai bước xử lý khi người đó rời nhóm sau này.

PO đã chốt quản lý kế thừa và phạm vi xem dữ liệu thay đổi theo vị trí mới. Open Question còn lại: tác động tới mentor phụ trách. Recommendation: giữ quản lý gán trực tiếp; chưa tự bổ sung email mới cho thao tác di chuyển nhánh.

### 3.2. Chuyển một người từ nhóm A sang nhóm B

Fact: một người được thuộc nhiều nhóm. Thêm họ vào B không mặc nhiên có nghĩa là rời A. PRD hiện mô tả thêm và gỡ thành viên, chưa quy định một thao tác Move member độc lập.

Fact: khi thực sự rời A, luật được xét riêng cho từng lớp: lớp thêm tay giữ nguyên; lớp còn nhóm khác giao giữ nguyên và không gửi email xử lý; lớp chỉ nhận qua A và chưa học được tự gỡ; lớp đang học hoặc đã hoàn thành giữ nguyên và gửi email cho người phụ trách. Vào B thì áp luật giao lớp của B. Nghỉ việc là trường hợp riêng, không áp cùng cách xử lý với điều chuyển.

Recommendation: không chặn đổi nhóm chỉ vì người đó đã có dữ liệu học. Hộp xác nhận phải phân biệt số lớp sẽ bị gỡ và số lớp được giữ; không dùng câu chung rằng mọi lớp đều giữ nguyên hoặc mọi lớp đều bị gỡ. Email xử lý theo US20 chỉ gửi khi rời nhóm làm mất nguồn giao cuối cùng và còn lớp đã có dữ liệu học. Không tự tạo thao tác chuyển thành viên mới trong đợt sửa này.

Assumption cần PO xác nhận: yêu cầu “chuyển nhóm” bao gồm việc rà soát cả di chuyển nhánh và điều chuyển thành viên; chưa mặc định PO yêu cầu thêm nút chuyển thành viên.

## 4. Khối xem trước ở Assign classes

Fact: PRD cho chọn nhiều lớp nhưng gọi các tổng là số người. Một người có thể chưa vào lớp A và đã ở lớp B; vì vậy không thể cộng các tổng theo lớp rồi gọi kết quả là số người duy nhất.

Recommendation: hiển thị kết quả riêng cho từng lớp được chọn. Trong một lớp, mỗi người chỉ được đếm một lần dù xuất hiện qua nhiều nhóm trong nhánh.

| Nhãn đề xuất | Ý nghĩa |
|---|---|
| New enrollments | Thành viên trong phạm vi giao chưa có lượt ghi danh ở lớp và đủ điều kiện để được thêm khi xác nhận. |
| Already in class | Thành viên trong phạm vi giao đã có lượt ghi danh ở đúng lớp này, dù do thêm tay hoặc qua nhóm khác; không tạo lượt ghi danh thứ hai và không đặt lại tiến độ. |
| Skipped | Thành viên trong phạm vi giao không được thêm vì một điều kiện nghiệp vụ đã được định nghĩa. Chỉ hiện khi có trường hợp thực tế, kèm lý do và số lượng từng lý do. |

Không gọi người đã học khoá trong một lớp khác là Already in class của lớp đang chọn. Auto-enroll chỉ điều khiển người vào nhóm sau này, không thay đổi kết quả giao cho thành viên hiện tại.

Ví dụ: nhóm có An và Bình; chọn lớp A và B. An đã ở A, chưa ở B; Bình chưa ở cả hai. Lớp A hiện 1 New enrollment và 1 Already in class; lớp B hiện 2 New enrollments và 0 Already in class. Nếu cần tổng chung thì gọi là 3 lượt ghi danh mới, không gọi 3 người.

Fact: tài khoản kiểm thử bị loại khỏi mọi logic nhóm; lớp đã kết thúc không nằm trong danh sách chọn; vượt sức chứa không chặn ghi danh. Prototype lại dùng tài khoản kiểm thử làm lý do Skipped. Đây là điểm cần thống nhất, không đủ cơ sở dựng thêm các lý do như hết chỗ hoặc đã học khoá.

PO đề xuất nguyên văn: “Nhãn đề xuất: New enrollments/ already in class / skipped”. Phương án rà soát dùng New enrollments · Already in class · Skipped; lý do hợp lệ để tính Skipped vẫn cần làm rõ, không tự bổ sung điều kiện loại trừ. Recommendation: Khi chưa chọn lớp, hiện `Select at least one class to preview enrollments.` thay cho ba số 0.

Khi nhóm không có thành viên trực tiếp, nhánh con có thành viên và Cascade to sub-groups tắt, hiện `This group has no direct members. Turn on Cascade to sub-groups to include members of its sub-groups.` Thành viên ngoài phạm vi do công tắc tắt không phải người bị bỏ qua vì lỗi.

Open Question: lượt ghi danh đã kết thúc do nghỉ việc có được tính là Already in class khi tài khoản hoạt động trở lại không? Chưa có đủ quy tắc để tự chọn giữa giữ kết thúc và ghi danh lại. Lượt được thêm sau thời điểm xem trước cũng cần được kiểm tra lại khi xác nhận để không tạo trùng.

## 5. Gỡ lớp khi nhóm đã có người học

Fact: BR-7.10 điều kiện gỡ lớp viết “đã có người trong nhóm học lớp đó”, nhưng AC7.6 và chuỗi tiếng Anh có thể được hiểu là chỉ cần đã ghi danh. Prototype dùng số Enrolled via this group lớn hơn 0 để ẩn Remove, không kiểm tra đã bắt đầu học. Điều này có thể khiến lớp vừa giao thành công đã không gỡ được dù chưa ai học.

Quyết định của PO, nguyên văn: “chặn khi phát sinh hoạt động học”. Quyết định này thay thế đề xuất Unassign cho phép gỡ dù đã có người đang học.

Nội dung thay thế cho BR-7.10 điều kiện gỡ lớp:

> Không cho gỡ một lớp khỏi nhóm khi có ít nhất một người học thuộc phạm vi xét đã phát sinh hoạt động học trong lớp đó, kể cả người đã hoàn thành. Việc chỉ có lượt ghi danh nhưng chưa phát sinh hoạt động học không phải điều kiện chặn gỡ lớp.

Giữ nhãn Remove. Khi thoả điều kiện chặn, nút bị ẩn và thay bằng thông báo:

> This class can't be removed because learners from this group have already started learning.

Các tình huống cần cập nhật cùng AC7.6 hành vi nút Remove và EC-14 gỡ lớp đã có người học:

| Tình huống | Kết quả cần kiểm |
|---|---|
| Đã có lượt ghi danh nhưng chưa ai phát sinh hoạt động học | Không bị chặn bởi điều kiện hoạt động học; các điều kiện quyền thao tác và trạng thái nhóm vẫn áp dụng. |
| Có ít nhất một người phát sinh hoạt động học | Chặn gỡ; ẩn Remove và hiện thông báo trên. |
| Có người đã hoàn thành | Vẫn chặn vì đã phát sinh hoạt động học. |
| Hoạt động học phát sinh sau khi mở màn hoặc hộp xác nhận | Kiểm tra lại trước khi hoàn tất; từ chối gỡ nếu đã phát sinh hoạt động học và hiện cùng thông báo. |

Already in class chỉ có nghĩa đã ghi danh. Không dùng số này hoặc Enrolled via this group lớn hơn 0 để chặn Remove. Bỏ câu “Cùng logic với việc gỡ học viên khỏi lớp” để điều kiện có thể được đọc và kiểm độc lập.

Open Question còn lại: định nghĩa cụ thể của hoạt động học; phạm vi người được xét khi có nhánh con hoặc nhiều nguồn ghi danh; hệ quả đối với các lượt ghi danh chưa học và mentor khi gỡ lớp. Câu trả lời của PO chỉ chốt thời điểm chặn, không tự chốt các nội dung này.

## 6. Assigned Classes: Enrolled via this group và Reason

Fact: Enrolled via this group là số lượng trên một dòng lớp, không phải số người đã bắt đầu học. PRD chưa định nghĩa đầy đủ cách đếm nguồn trùng, nhánh con và người đã rời nhóm.

Recommendation: dùng nhãn `Learners covered by this assignment`, nghĩa là số người hiện thuộc phạm vi quan hệ giao lớp và có lượt ghi danh được quan hệ đó bao phủ. Một người một lần trong mỗi lớp; gồm người ở nhánh con nếu quan hệ giao đang áp cho nhánh con; có thể đồng thời được nhiều nguồn khác bao phủ. Chỉ số này không thể hiện việc người đó đã học và không dùng làm điều kiện chặn Remove.

Ví dụ: người đã ở lớp do thêm tay, sau đó được nhóm giao cùng lớp, thì vẫn có một lượt ghi danh và có thể được tính trong phạm vi giao của nhóm. Không gọi họ là người được nhóm tạo mới lượt ghi danh. Cần thống nhất với cách ghi nguồn trong AC7.3 chống trùng ghi danh và các nguồn của lượt ghi danh.

Open Question: có cần thay chỉ số hiện tại bằng số người được quan hệ giao lớp bao phủ như đề xuất, hay PO muốn đếm luỹ kế những người từng được nhóm tạo mới lượt ghi danh? Hai số có nghĩa khác nhau, không được dùng chung nhãn. Trường hợp tắt Cascade nhưng giữ lượt ghi danh đã có cũng phải theo đúng định nghĩa được PO chọn.

Fact: không có cột Reason trong bảng Assigned Classes của PRD và prototype đã đọc. Reason có căn cứ trong nhật ký thay đổi thành viên; Error reason có trong bảng lỗi nhập tệp. Ảnh PO gửi không có cột Reason nên chưa xác định được cột đang được nhắc tới thuộc màn nào.

Recommendation theo từng ngữ cảnh:

| Ngữ cảnh | Nhãn và giá trị |
|---|---|
| Kết quả giao lớp | Dùng bộ nhãn New enrollments · Already in class · Skipped theo đề xuất PO. Đây là kết quả xem trước, không gọi chung là Reason. Lý do bỏ qua là thông tin bổ sung của Skipped và còn cần làm rõ. |
| Lớp đã kết thúc hoặc không gỡ được theo phương án giữ chặn | Dùng nhãn trạng thái hoặc câu giải thích cạnh thao tác, không thêm cột Reason chung. |
| Nhật ký thành viên | Dùng Change reason. Các giá trị đã có trong PRD: Thêm tay · Nhập tệp · Đồng bộ · Nghỉ việc · Điều chuyển. Chuỗi tiếng Anh cần Design thống nhất. |
| Lỗi nhập tệp | Giữ Error reason, mô tả lỗi của từng dòng. |

Không tạo một danh sách giá trị Reason mới cho Assigned Classes khi chưa biết cột đó cần trả lời câu hỏi nghiệp vụ nào.

## 7. Member list: thứ tự cột

Fact: PRD hiện ghi Họ tên · Mã nhân viên · Email · Phòng ban · Ngày vào nhóm · Trạng thái tài khoản. Người thuộc nhánh con có thể xuất hiện khi bật bộ lọc nhưng không gỡ được ở nhóm cha. Dữ liệu phòng ban của nhân sự vận hành bị bỏ theo quyết định trước đó; chưa đủ cơ sở suy rằng trường Phòng ban trong danh sách học viên cũng đã bị bỏ.

Recommendation về thứ tự:

`Checkbox → Full name → Employee ID → Email → Member group → Joined on → Account status`

Member group chỉ rõ nhóm trực tiếp để biết dòng nào thuộc nhóm đang mở và dòng nào tới từ nhánh con; tên nhóm con kèm đường dẫn khi cần phân biệt trùng tên. Dòng thuộc nhánh con không có checkbox có thể chọn, kèm giải thích phải mở nhóm trực tiếp để gỡ. Full name là liên kết mở hồ sơ theo quyền. Joined on là ngày vào nhóm trực tiếp hiển thị trên dòng, không phải ngày người đó được nhìn thấy từ nhóm cha.

Open Question: PO có cần giữ thêm Department riêng với Member group không? Đề xuất thay Department bằng Member group nếu mục đích là nhận biết quan hệ trong cây nhóm. Không tự coi nhóm tự tạo là phòng ban nhân sự. Khi một người thuộc nhiều nhóm con, đề xuất một dòng mỗi người và liệt kê các nhóm trực tiếp tương ứng; trường Joined on cần hiện theo từng quan hệ, không gộp thành một ngày không rõ nghĩa.

## 8. Impact preview và bước xin xác nhận

Recommendation: mở một change request, sửa phần bị chạm thay vì viết lại toàn bộ PRD. Chưa cấp mã change request và chưa mở lại stage trước khi PO xác nhận phạm vi.

| Stage | Xử lý đề xuất | Lý do và đầu ra |
|---|---|---|
| 2.3 Requirements Analysis | Sửa phần bị chạm | Đối chiếu chuyển nhóm và cách tính nguồn; làm rõ điều kiện chặn gỡ khi phát sinh hoạt động học theo quyết định PO. Chưa tự chốt hệ quả gỡ lớp đối với lượt ghi danh chưa học. |
| 2.31 Impact Analysis | Sửa phần bị chạm | Xét lượt ghi danh nhiều nguồn, nhánh cũ và mới, quản lý kế thừa, mentor, tiến độ, thông báo, lưu trữ và số liệu trong impact-matrix.md. |
| 2.4 User Stories | Giữ danh sách, đối chiếu phần bị chạm | Chưa đề xuất user story mới. Nếu PO yêu cầu thao tác chuyển thành viên độc lập thì đánh giá lại phạm vi. |
| 2.42 PRD Generation | Sửa phần bị chạm | Cập nhật US2 di chuyển nhánh · US3 thành viên · US6 danh sách nhóm · US7 giao lớp · US8 tự ghi danh · US14 lưu trữ và các tham chiếu bị tác động; thêm định nghĩa, thông báo, tiêu chí chấp nhận, lịch sử phiên bản và truy vết. |
| 2.43 Design Alignment | Tiếp tục với bản PRD mới sau duyệt | Decision Brief phải phản ánh phần đổi. Các PIC tự cập nhật file thiết kế và xác nhận phần bị chạm; AI của PO không sửa file của PIC. |

Trước khi sửa artifact đã duyệt, dùng lệnh archive của engine để chụp bản trước change request. Các stage thay đổi phải được trình duyệt lại. Sau duyệt mới cập nhật bản bàn giao và Story List, rà soát nội dung Jira tương ứng và publish lại PRD theo đích đã cấu hình.

PO đã xác nhận hướng di chuyển nhánh và thời điểm chặn gỡ lớp. Những điểm còn mở gồm định nghĩa hoạt động học, phạm vi người được xét khi gỡ, tác động mentor, định nghĩa số người trên Assigned Classes và vị trí, ý nghĩa cột Reason. Các đề xuất còn lại có thể xác nhận theo từng phần hoặc chỉnh trực tiếp trong phản hồi.

## 9. Danh sách nhóm: dạng bảng và dạng cây

Yêu cầu PO: thêm Parent group trong bảng; xem lại thứ tự cột; xem xét chuyển Source thành badge cạnh tên và gom theo nhóm cha; bỏ bộ lọc Level vì người dùng không biết nhóm thuộc cấp nào.

Recommendation về thứ tự cột:

`Group name → Code → Parent group → Members → Status → Last updated`

Source chuyển thành badge Manual hoặc HR sync cạnh tên; bộ lọc Source vẫn giữ. Bỏ bộ lọc Level ở cả hai dạng. Parent group hiển thị nhóm cha trực tiếp, nhóm gốc hiện No parent; tooltip hiển thị đường dẫn đầy đủ để phân biệt tên trùng. Members vẫn đếm người không trùng trong toàn nhánh.

Recommendation: mặc định bảng phẳng, có thể thêm Group by: None / Parent group nếu PO chọn làm khả năng gom. Chưa coi việc gom hoặc bỏ cột Manager là quyết định đã chốt; bộ lọc Manager có thể giữ.

Dạng cây: tên nhóm → badge nguồn Manual/HR sync → badge Archived nếu có → số thành viên. Tên dài rút gọn bằng dấu ba chấm; hover hoặc focus hiện đầy đủ. Không cắt các badge theo tên. Giữ chỉ báo No manager khi phù hợp.

Đối với yêu cầu “Thêm option xoá khi chuyển group” ở Edit group, PO trả lời nguyên văn: “bỏ qua cái này đi, chưa chắc, làm sau”. Mục này nằm ngoài phạm vi sửa hiện tại, không bổ sung thao tác và không giữ làm câu hỏi chặn.

## 10. Đã áp dụng vào PRD theo yêu cầu PO

PO yêu cầu nguyên văn: “bây giờ sửa vào prd, chỉ sửa những phần đã review, tuyệt đối không sửa những phần không liên quan”. Đã cập nhật PRD v0.9 draft, CR9, riêng US2 di chuyển nhánh · US6 danh sách nhóm · US7 giao và gỡ lớp · US14 hiển thị nhóm lưu trữ, kèm câu hỏi mở #21 về các định nghĩa chưa chốt. Bản trước sửa nằm ở archive/prd-generation/prd-pre-CR9-20261103.md.

Nguồn thành badge cạnh tên, thêm Parent group và bỏ Level. Giữ cột Manager, chưa bổ sung gom nhóm theo Parent group. Không áp dụng thay Member list, đổi định nghĩa Enrolled via this group hoặc Reason; không bổ sung thao tác xoá trong Edit group. Chưa sửa file thiết kế, Story List hoặc bản publish. PRD sửa chưa được duyệt; đầu tài liệu này mô tả mốc trước khi áp dụng, mục này ghi trạng thái mới nhất.

## 11. Add Member theo màn Add Student

PO yêu cầu bỏ Staff code và Department, sau đó xác nhận nguyên văn: “làm giống màn add student”, kèm ảnh tham chiếu. Nội dung này thay đề xuất bảng chỉ có Member và Email trước đó. Phạm vi là SCR7 thêm thành viên; không thay bảng SCR6 danh sách thành viên của nhóm.

Bố cục áp dụng theo ảnh:

- Tiêu đề Add Member; nút Add và Cancel ở phía trên bên phải.
- Các điều khiển Search · Sort by · From date · To date; nút Reset và Search.
- Bảng theo thứ tự Checkbox · ID · Member · Email · Phone · Date. Chỉ đổi nhãn Student name thành Member.
- Date có hai dòng Created và Updated của hồ sơ học viên, không phải ngày vào nhóm. ID dùng cùng dữ liệu với màn Add Student, không tự đồng nhất với Staff code.
- Không có cột Staff code hoặc Department. Các lựa chọn sắp xếp, phạm vi tìm kiếm và trường ngày lọc dùng cùng hành vi hiện có của Add Student; ảnh không cho biết các lựa chọn này nên không tự khai thêm.

Giữ các quy tắc hiện tại về người đã ở nhóm có nhãn Already in group và không chọn lại được, loại tài khoản kiểm thử, chọn nhiều, phân trang 20 dòng và quyền thao tác.

Đã cập nhật riêng phần Add Member trong US3 thêm thành viên của PRD v0.9 draft, cùng lịch sử phiên bản. Bản ngay trước cập nhật lưu ở archive/prd-generation/prd-pre-CR9-add-member-20261103.md. Không sửa file thiết kế hoặc bảng Members.

## 12. Đối chiếu giao diện ngày 04/11/2026

Nguồn: bốn ảnh PO gửi ngày 04/11/2026. Phạm vi chỉ gồm Members, Add members, Assigned Classes và Assign classes. Đây là đối chiếu ảnh và đặc tả, không phải xác minh hành vi hệ thống đang chạy. Nội dung dưới đây thay phần đề xuất Member list ở mục 7 và mẫu Add Student tại mục 11 đối với các màn này.

### 12.1. Members: vị trí đặc tả và thay đổi

Mô tả nằm ở US3 thêm và gỡ thành viên thủ công, bảng Giao diện và validate, các dòng SCR6 tab Members. PRD trước sửa có Họ tên, Mã nhân viên, Email, Phòng ban, Ngày vào nhóm, Trạng thái tài khoản. Ảnh 1 đã bỏ mã nhân viên khỏi bảng và đổi Department thành Subgroup nhưng placeholder vẫn còn staff code.

Đã cập nhật PRD theo thứ tự Checkbox · # · Full name · Email · Subgroup · Joined date · Account status · thao tác theo quyền. Đây là thứ tự hợp lý để nhận diện người, xác định quan hệ trong nhánh, rồi xem thời điểm và trạng thái. Email giúp phân biệt các hàng trùng họ tên trong ảnh.

Subgroup chỉ hiển thị nhóm con thuộc nhánh đang xem mà người đó trực tiếp là thành viên, không phải phòng ban nhân sự và không phải mọi nhóm khác của người đó. Người trực tiếp thuộc nhóm đang mở hiển thị dấu gạch với tooltip Direct member. Người thuộc nhánh con vẫn không được gỡ ở nhóm cha, theo quy tắc hiện có. Các nhóm tên dài cần hover hoặc focus hiện đủ, tốt hơn nếu kèm đường dẫn để phân biệt tên trùng.

Đã chuẩn hoá placeholder thành Search by name or email trong PRD cho cả Members và Add members. Đề nghị giao diện bỏ staff code khỏi placeholder ảnh 1. Không cần thêm Staff code trở lại bảng.

Open Question: một người thuộc nhiều nhóm con thì Joined date ở một dòng là ngày của quan hệ nào? Đề xuất hiển thị ngày cùng từng nhóm trong thông tin chi tiết, chưa tự chọn ngày sớm nhất hoặc muộn nhất. Ảnh không chứng minh được ngày đang lấy theo quan hệ nào.

Ảnh không đủ để xác nhận checkbox của thành viên nhánh con đã khoá hay chưa, hoặc hành vi ẩn người nghỉ việc đã đáp ứng PRD. Các quy tắc này giữ nguyên, cần đối chiếu khi kiểm thử.

### 12.2. Add members: ảnh mới thay mẫu Add Student hôm trước

Ảnh 2 có Checkbox · # · Full name · Email · Current group; Search, Sort by, Reset, Search, Add, Cancel. Không có Phone, Date, ID, From date hoặc To date như mẫu Add Student trước đó. PRD đã được sửa theo ảnh mới: Checkbox · # · Full name · Email · Current groups. Giữ Full name giống Members; dùng Current groups ở số nhiều vì một người được thuộc nhiều nhóm.

Current groups thể hiện các nhóm người đó đang trực tiếp là thành viên; không lặp các nhóm cha chỉ vì người đó thuộc nhóm sâu nhất. Nhóm dài rút gọn, hover hoặc focus hiện đủ; không có nhóm hiển thị dấu gạch. Không có Staff code hoặc Department. Placeholder đề nghị dùng Search by name or email cho rõ phạm vi tìm.

Giữ quy tắc người đã ở chính nhóm đang thêm hiện mờ, có nhãn Already in group, không chọn lại; người thuộc nhóm khác vẫn thêm được. Ảnh hiện nhiều hàng màu nhạt nhưng không cho biết điều kiện khoá thực tế; không kết luận tất cả người trong ảnh đã thuộc nhóm đích. Ảnh cũng chưa thấy rõ nhãn Already in group, nên cần kiểm tra hiển thị nhãn này.

### 12.3. Assigned Classes và Assign classes

| Nội dung | Đối chiếu | Xử lý |
|---|---|---|
| Các cột Assigned Classes | Ảnh 3 có #, Class name, Course, Class duration, Enrolled by group, Assigned date, Cascade to sub-groups, Auto-enroll, menu thao tác; cơ bản khớp các trường PRD | Đã ghi rõ nhãn và thứ tự cột trong PRD, bổ sung ô tìm kiếm theo tên lớp hoặc khoá, Reset và Search. |
| Enrolled by group | Tương ứng cột Số người đã vào qua nhóm này trong PRD. PRD chưa đủ định nghĩa công thức; ảnh chỉ hiển thị 0 | Giữ câu hỏi mở #22 về công thức, không suy cách tính từ ảnh hoặc từ tên trường. |
| Course đang trống | Ảnh 3 chưa có tên khoá ở hàng lớp | Đề nghị bổ sung tên khoá theo cột PRD, chưa có căn cứ bỏ cột Course. |
| Menu ba chấm | Ảnh 3 chưa mở menu nên chưa xác minh Remove | Giữ luật chặn khi phát sinh hoạt động học; không dùng Enrolled by group lớn hơn 0 để chặn. |
| Nhãn Preview | Ảnh 4 dùng Will be enrolled và Already enrolled in this class, khác New enrollments và Already in class đã được PO chọn | Đề nghị sửa giao diện về New enrollments · Already in class · Skipped; giữ PRD theo bộ nhãn đã chốt. |
| Chọn nhiều lớp | Ảnh 4 dùng một khối tổng | Cần thể hiện kết quả theo lớp hoặc dùng đơn vị lượt ghi danh cho tổng; không gọi tổng của nhiều lớp là số người không trùng. |
| Chưa chọn lớp | Ảnh 4 hiện ba số 0 | Recommendation: hiện Select at least one class to preview enrollments để phân biệt chưa chọn với đã tính ra 0; chưa áp thêm quy tắc này vào PRD. |
| Bảng chọn lớp | Ảnh 4 có #, Class name, Course, Class duration, Capacity | Đã bổ sung cấu trúc cột này vào PRD, giữ quy tắc sức chứa không chặn giao lớp. |
| Capacity là dấu gạch | Ảnh 4 có lớp tên gợi ý giới hạn 1 nhưng giá trị cột là dấu gạch | Cần kiểm dữ liệu sức chứa của lớp; tên lớp không đủ chứng minh giá trị thật. Nếu giới hạn thực tế là 1 thì phải hiển thị 1. Không tự coi dấu gạch là hết chỗ hoặc vô hạn. |

Recommendation về Enrolled by group: giữ ý nghĩa nguồn ghi danh, dùng nhãn rõ hơn Enrolled via this group và tooltip sau khi PO chốt cách đếm. Đếm mỗi người một lần trong một lớp khi lượt ghi danh có nguồn của nhóm đang xem; đây không phải tổng thành viên và không đo đã bắt đầu học. Không đếm người chỉ có nguồn thủ công hoặc nguồn nhóm khác mà không có nguồn nhóm này. Quy tắc nhận nguồn của người đã vào lớp từ trước và cách giữ nguồn khi đổi Cascade vẫn cần PO chốt.

Ví dụ theo phương án đề xuất: nhóm có 20 người; 8 người có lượt ghi danh chỉ mang nguồn thủ công và 12 người có lượt ghi danh mang nguồn nhóm này. Enrolled by group là 12, còn số thành viên nhóm đã ở lớp là 20. Nếu toàn bộ 20 người chỉ được thêm tay thì cột có thể là 0 theo cách đếm nguồn, nhưng ảnh 3 không đủ căn cứ kết luận đó là nguyên nhân số 0 hiện tại. Auto-enroll tắt chỉ dừng ghi danh cho người vào nhóm sau, không giải thích việc thành viên hiện tại chưa được ghi danh khi giao lớp lần đầu.

PO đã trả lời nguyên văn: “Đếm lượt ghi danh có nguồn nhóm này”. Đã cập nhật định nghĩa, tooltip, dữ liệu nguồn và ví dụ kiểm tra trong US7 giao lớp của PRD v0.11 draft; không tiếp tục để lựa chọn giữa đếm theo nguồn và đếm mọi thành viên ở trạng thái mở. Giữ nhãn Enrolled by group. Các câu hỏi về phạm vi nhánh con và vòng đời nguồn khi rời nhóm hoặc đổi Cascade vẫn giữ nguyên.

Đã cập nhật PRD v0.10 draft trong phạm vi US3 danh sách/thêm thành viên và US7 giao lớp, kèm câu hỏi mở #22. Bản trước sửa: archive/prd-generation/prd-pre-CR9-ui-review-20261104.md. Các phần khác, file thiết kế và bản publish giữ nguyên.

### 12.4. Quyết định về Enrolled by group

Nguyên văn PO: “Đếm lượt ghi danh có nguồn nhóm này”. Cột đếm lượt ghi danh trong lớp mà nhóm đang xem là một nguồn; mỗi lượt tính một lần ở nhóm đó. Lượt chỉ có nguồn thêm tay hoặc nguồn nhóm khác không tính. Một lượt có nhiều nguồn được tính ở mỗi nhóm có trong danh sách nguồn, không tạo thêm lượt ghi danh. Đây không phải số lượt ghi danh mới trong một thao tác hoặc số người đã bắt đầu học. Chưa tự chốt số liệu luỹ kế hay các trường hợp rời nhóm, tắt Cascade ngoài quyết định trên.

## 13. Rà soát toàn bộ nhận xét UAT

Đã đối chiếu danh sách tổng hợp UAT ngày 04/11/2026 tại inputs/uat-coverage-20261104.md, gồm từng nhận xét, mức độ PRD đã bao phủ, phần chỉ thuộc giao diện, điểm trái đặc tả và ảnh hưởng tới các artifact. PO xác nhận Graph chỉ là đổi tên Tree. Mục option xoá trong Edit group tiếp tục để sau theo quyết định trước. Bản audit này chưa sửa thêm PRD; các khoảng trống mới như tự sinh mã và nhật ký thành tab cần đưa vào phạm vi sửa tiếp của CR9, không tự đánh dấu đã được xử lý.

## 14. Đồng bộ UAT Coverage sau khi PO rút gọn

Theo DEC154, đã sửa mục 5.1 của UAT Coverage về đúng các giá trị Reason trong PRD và đồng bộ các nội dung giữ lại: mã nhóm tự tạo tự sinh, Graph/Table, nhật ký giới hạn theo nhóm đang chọn. Các bản sửa là requirements v0.7 draft, impact-matrix v0.8 draft và PRD v0.11 draft; các nhận định “PRD chưa sửa” trong các mục trước là trạng thái lịch sử. UAT Coverage được cập nhật theo trạng thái mới. Không khôi phục nội dung PO xoá, không quyết thay mục để sau; Account status vẫn cần đối chiếu và chốt.

## 15. Gộp mốc phiên bản nháp theo yêu cầu PO

Lịch sử bàn giao được gộp thành v0.9 ngày 03/11, v0.10 ngày 04/11 cho Members và giao lớp, v0.11 ngày 04/11 cho mã tự sinh, Graph/Table và nhật ký. PRD hiện tại là v0.11 draft. Các mốc v0.10 đến v0.13 trong ghi chép cũ là số bản nháp trước khi gộp, không phải các bản đã được duyệt; đối chiếu theo DEC155. Nội dung nghiệp vụ không đổi do việc gộp số phiên bản.
