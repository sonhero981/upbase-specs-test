# Corner Checklist cho UpLnD

> Viết lại từ `corner-checklist.md` của AWS AI-DLC Workflows v2.10 (`core/knowledge/aidlc-product-agent/`, giấy phép MIT-0) theo nghiệp vụ LMS của UpLnD. Giữ cách dùng của AWS, thay danh sách điều kiện bằng góc hay sót trong hệ này. Stage đọc: 2.3 Requirements Analysis khi quét lỗ hổng, 2.42 PRD Generation khi viết acceptance criteria và business rule.

Phần lớn lỗi lọt qua một lượt phân tích kỹ không phải là thiếu tính năng. Chúng là **góc**: một thành phần gặp một điều kiện ít ai nghĩ tới, như danh sách rỗng, học viên bị Block giữa chừng, lớp đã kết thúc, hai mentor chấm cùng một bài. Hỏi thêm câu hỏi không tìm ra chúng. Quét từng thành phần qua một danh sách cố định thì tìm ra.

## Cách dùng
1. **Chốt hình dạng trước.** Portal nào: UpLMS, Ops, hay cả hai. Vai nào chạm. Một tenant hay mọi tenant. Tính năng mới hoàn toàn hay sửa thứ đang chạy có dữ liệu cũ.
2. **Liệt kê thành phần** từ chính yêu cầu: màn, luồng, job, mail, báo cáo, tích hợp. Không bịa thêm.
3. **Giao mỗi thành phần với các bề mặt bên dưới.** Thành phần không gửi mail thì bỏ bề mặt mail.
4. **Mỗi điều kiện áp dụng kết thúc bằng một trong ba cách:** viết thành FR hoặc acceptance criterion; ghi vào Assumptions kèm lý do không cần rule; ghi vào Out of scope.
5. **Chỉ hỏi PO điều AI không tự biết:** thực tế vận hành, quy ước của UpBase, cam kết với khách. Góc mà một mặc định hợp lý giải quyết được thì viết thành FR hoặc assumption để PO sửa, không biến thành câu hỏi.

Chuẩn: mọi điều kiện áp dụng đều có FR, assumption có lý do, hoặc loại trừ rõ. Góc để im là góc sẽ hỏng khi chạy.

## Điều kiện theo bề mặt
Mỗi dòng: điều kiện, rồi điều phải đúng.

### Người học và tài khoản
- **Bị Block hoặc vô hiệu giữa chừng**: tiến độ, điểm, bài nộp được giữ; không nhận mail; quay lại thì thấy đúng trạng thái cũ.
- **Thuộc nhiều lớp, nhiều nhóm, nhiều khoá cùng lúc**: dữ liệu không đếm trùng; quy tắc nào thắng khi hai nơi đặt khác nhau được ghi rõ.
- **Đổi vai giữa chừng** (học viên thành mentor, mentor chính thành mentor thường): quyền cũ thu hồi trong thời gian nêu rõ; bản ghi cũ vẫn truy được.
- **Tài khoản trùng hoặc gộp** (SSO, SIS đồng bộ trễ, hai email): một quy tắc nhận diện; lịch sử không mất.
- **Người dùng chưa đăng nhập lần nào, hoặc chưa có hồ sơ**: màn không vỡ; nêu việc cần làm.

### Lớp, khoá, danh mục
- **Lớp đã kết thúc**: còn xem được gì, còn làm được gì, mail nào ngừng. Ghi rõ từng việc.
- **Lớp chưa bắt đầu**: thao tác nào bị chặn, thông báo nói gì.
- **Lớp không có học viên, khoá không có bài**: hiển thị rỗng có nghĩa, không lỗi; báo cáo vẫn chạy.
- **Khoá, bài, đề bị ẩn (Hidden) hoặc gỡ khi vẫn còn người đang học**: tiến độ, điểm, chứng chỉ đã cấp giữ nguyên; không có liên kết chết.
- **Xoá khi còn tham chiếu**: `course_categories` là khoá ngoại của sáu bảng; định nghĩa chặn xoá, xoá mềm, hay chuyển sang danh mục khác.
- **Chuyển học viên giữa lớp, đổi lịch, đổi mentor**: dữ liệu đã có đi theo người hay theo lớp, ghi rõ.

### Bài học, bài kiểm tra, chấm điểm
- **Nộp sau hạn, nộp nhiều lần, nộp rồi rút**: lần nào được tính; có lưu các lần trước không.
- **Chấm lại sau khi đã công bố**: điểm cũ còn truy được; học viên có được báo; chứng chỉ đã cấp xử lý ra sao.
- **Điểm 0, chưa chấm, miễn, không áp dụng**: bốn trạng thái khác nhau từ đầu đến báo cáo; không gộp thành 0.
- **Sửa câu hỏi đang được dùng trong đề**: Question Bank có bốn nơi tiêu thụ; đề đã phát giữ bản cũ hay nhận bản mới, ghi rõ.
- **Đề 0 câu, đề toàn câu bị ẩn, điểm tối đa 0**: không chia cho 0; thông báo rõ.
- **Làm bài bị ngắt** (mất mạng, hết phiên, đóng tab): bài đang làm không mất; tiếp tục hay nộp tự động theo một quy tắc.
- **Hai mentor chấm cùng một bài, hoặc một mentor chấm ở hai tab**: không ghi đè lặng; kết quả như làm lần lượt.

### Dữ liệu cũ và thời điểm bật tính năng
- **Bản ghi tạo trước ngày bật tính năng**: hiển thị gì, tính gì, có backfill không. Mặc định phải nêu, không để Dev đoán.
- **Enum, trạng thái cũ không còn trong danh sách mới**: ánh xạ một chiều hoặc giữ nguyên, có bảng đối chiếu.
- **Bật rồi tắt, hoặc rollback**: dữ liệu sinh ra trong lúc bật vẫn đọc được.
- **Chạy song song bản cũ và mới trong lúc golive**: không ghi hai nơi lệch nhau.

### Danh sách, bộ lọc, báo cáo
- **Rỗng**: nói rõ vì sao (chưa có, bị lọc hết, không có quyền) và việc kế tiếp.
- **Đúng một dòng**: biểu đồ, trung bình vẫn có nghĩa; số ít số nhiều đúng.
- **Rất nhiều dòng**: phân trang hoặc giới hạn, và giới hạn được nói ra; export có trần hay không.
- **Tổng con không khớp tổng**: dòng thuộc nhiều nhóm hoặc không nhóm nào theo một quy tắc được nêu.
- **Sắp xếp hoà**: thứ tự ổn định, có tiêu chí phụ.
- **Lọc kết hợp mâu thuẫn**: kết quả rỗng có giải thích, không lỗi.
- **Múi giờ và kỳ học**: ngày bắt đầu, kết thúc tính theo múi giờ nào; biên ngày, cuối tháng, giao kỳ xử lý rõ.

### Thông báo và mail
- **Mail event đã tồn tại nhưng đang tắt** (KB 13): yêu cầu "thêm thông báo" có trùng mail số nào không, bật lại hay làm mới.
- **Gửi hàng loạt**: giới hạn, thứ tự, điều gì xảy ra khi một người lỗi; không gửi lặp khi job chạy lại.
- **Người nhận bị Block, rời lớp, đổi email giữa lúc gửi**: quy tắc bỏ qua.
- **Dữ liệu đổi sau khi lên lịch gửi**: mail lấy dữ liệu lúc gửi hay lúc tạo.
- **Ngôn ngữ, tên có dấu, nội dung dài**: hiển thị đúng; tiêu đề không cắt mất ý.

### Quyền và vai
- **Kiểm quyền theo từng đối tượng**, kể cả danh sách, tìm kiếm, export, không chỉ màn chi tiết.
- **Mentor chính và mentor thường, admin tenant và admin lớp**: ai thấy gì, ai sửa gì, viết thành bảng.
- **Quyền bị thu hồi khi đang đăng nhập**: có hiệu lực trong khoảng thời gian nêu rõ.
- **Casbin**: rule mới có đụng rule có sẵn không, tra KB 06 trước khi thêm vai.
- **Ops và LMS cùng chạm một dữ liệu**: nơi nào là nguồn, nơi nào chỉ đọc.

### Tenant và hằng số
- **Logic riêng UpBase chui vào code**: chỉ qua cấu hình; ghi rõ cứng hay cấu hình theo KB 15 §6.
- **Bảng mới có `tenant_id`**, truy vấn, cache, job, export không xuyên tenant.
- **Enum mới**: hệ thống hay tenant định nghĩa; tenant khác có thêm giá trị được không.
- **Giới hạn** (số học viên, dung lượng, số đề): tenant nào cũng vậy hay cấu hình riêng.

### Thời gian
- **Hạn đúng giây 0, trước hạn một giây, sau hạn một giây**: hành vi xác định ở cả ba điểm.
- **Lịch dạy chồng, phòng trùng**: chặn, cảnh báo, hay cho phép, ghi rõ.
- **Thời điểm không hợp lý** (thiếu, quá khứ xa, tương lai xa): bị đánh dấu nghi ngờ, không hiển thị như sự kiện thật.
- **Khoảng thời gian** dùng biên đóng hay mở, nêu rõ.

### Đồng thời và trùng lặp
- **Hai người sửa cùng bản ghi**: phát hiện xung đột, không mất thay đổi lặng lẽ.
- **Bấm hai lần, gửi hai lần**: không tạo bản ghi trùng.
- **Job chạy trùng chính nó** (scheduler, import, mail): chạy hai lần bằng chạy một lần.
- **Phản hồi cũ về sau phản hồi mới**: chỉ áp kết quả của lần gọi mới nhất.

### Màn hình và nhập liệu
- **Đang tải, rỗng, lỗi** là ba trạng thái khác nhau, mỗi cái nói chuyện gì xảy ra và làm gì tiếp.
- **Dữ liệu cũ trên màn**: biết lần cập nhật cuối; làm mới thất bại thì báo.
- **Cùng một số ở hai chỗ**: cùng giá trị, cùng đơn vị, cùng cách làm tròn.
- **Thao tác phá huỷ** (xoá lớp, huỷ đề, xoá điểm): xác nhận nêu rõ cái bị ảnh hưởng, hoặc có hoàn tác.
- **Nhập sai**: chỉ đúng ô và cách sửa; giữ lại mọi thứ đã gõ.
- **Rời trang khi chưa lưu, hết phiên**: không mất lặng lẽ.
- **Validate phía giao diện** cũng được kiểm ở phía máy chủ.
- **Tên tiếng Việt có dấu, so sánh và tìm kiếm**: một quy tắc cho hoa thường, dấu, khoảng trắng.

### Tích hợp và nguồn ngoài
- **SIS, Lark, GitBook, SSO chậm hoặc không phản hồi**: tính năng phụ thuộc giảm cấp, phần còn lại vẫn dùng được.
- **Có endpoint không có nghĩa là có tính năng**: tính năng Hidden hoặc đã gỡ khỏi giao diện vẫn có API; xác nhận với PO trước khi tin.
- **Dữ liệu đồng bộ hai chiều**: nguồn sự thật là một bên, ghi rõ; lệch thì phát hiện và sửa.
- **Thử lại**: không lặp tác dụng phụ (tạo tài khoản, gửi mail hai lần).

## Mở rộng danh sách
Lỗi lọt tới test hoặc production mà không có dòng nào ở đây mô tả: thêm điều kiện vào file này qua vòng học tại gate, hoặc vào `.claude/memory/team.md` nếu là bài học cách làm. Danh sách lớn lên từ lỗi thật, không từ câu hỏi thêm.
