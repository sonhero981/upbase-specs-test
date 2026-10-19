# 2.41 HLD Brief & Alignment, câu hỏi
Intent: 261005-group · Stage: 2.41 · Cách trả lời: Chat · Đã trả lời: 4/4

## Q1. PIC Design, Tech PIC và QA PIC của intent Group là ai?
Vì sao hỏi: ba người này ghi mục 8, 9, 10 của HLD Brief trực tiếp trong repo và ký mục 12; tên điền vào `intent.md` (đang trống) và bảng đầu brief.
A. Chưa xác định, để trống rồi điền sau
X. Khác, xin nói rõ: <Design: …> <Tech: …> <QA: …>
Chặn: có
[Answer]: X, "sao phải biết là ai nhỉ, chỉ cần biết có từng đó role là được mà"
Hiểu là: brief ghi theo vai Design, Tech, QA; cột Tên ở mục 12 và bảng đầu để trống, PIC tự điền tên khi ký. `intent.md` không cần tên.

## Q2. PIC ghi định hướng theo cách nào và tới hạn nào?
Vì sao hỏi: quyết định cách chờ sign-off; `state.md` ghi hạn để nhắc.
A. PIC tự ghi vào repo (sửa mục của mình, commit `hld(261005-group): <design|tech|qa> direction`), hạn trong 5 ngày làm việc  [đề xuất, theo cách HLD Brief được thiết kế: file trong repo là nguồn sự thật, Lark chỉ nhận bản cuối]
B. Họp liên team một buổi, PO ghi lại theo tin nhắn xác nhận của PIC
C. Cả hai: gửi file trước, họp để chốt mục 7
X. Khác, xin nói rõ
Chặn: có
[Answer]: A, "PIC sẽ ghi luôn vào repo, tôi sẽ merge request, chưa cần hạn"
Hiểu là: PIC sửa mục của mình trên nhánh riêng và mở merge request, PO merge; không đặt hạn trong `state.md`, chỉ ghi "chờ MR của PIC".

## Q3. Quyết định nào cần chốt trong họp hoặc trong lượt ghi của PIC? (chọn nhiều)
Vì sao hỏi: mục 7 của brief chỉ nên có câu hỏi thật, có người quyết và hạn. Dưới đây là đề xuất rút từ Open Question còn mở và Vấn đề tồn đọng của PRD; PO bớt hoặc thêm.
A. Bảng `groups` và `group_user_instances` của chức năng nhóm cũ đang có dữ liệu thật hay rỗng; bỏ, giữ, hay chuyển đổi (`OQ-25`, ai quyết: Dev cùng PO)  [đề xuất]
B. Bản export ma trận quyền `casbin_rule` để Dev nối phạm vi theo quan hệ quản lý với vai trò hệ thống ở màn theo dõi nhánh (`OQ-31`, tồn đọng #2, ai quyết: Dev)  [đề xuất]
C. Loại quan hệ quản lý và mentor do hệ thống định nghĩa cố định hay tổ chức tự thêm được (`OQ-30`, tồn đọng #3, ai quyết: PO)  [đề xuất]
D. Tài khoản kiểm thử và tài khoản trả lời bình luận tạo bằng cách nào khi không nằm trong cây Lark (`OQ-34`, tồn đọng #4, ai quyết: PO cùng Dev)  [đề xuất]
E. Ba góc chưa có luật: đồng bộ lỗi nửa chừng, thu quyền khi đang xem báo cáo, tên Nhóm trùng support group (tồn đọng #7, ai quyết: Dev và Design)  [đề xuất]
X. Khác, xin nói rõ (ví dụ `roles.is_group` là gì, `OQ-33`; hộp xác nhận gỡ học viên khỏi lớp đã cảnh báo chưa, tồn đọng #6; số liệu vận hành thật cho mục Analytics, tồn đọng #1)
Chặn: không
[Answer]: "a dev sẽ quyết b dev sẽ quyết c cố định d chọn trong ops e ko ảnh hưởng x dev quyết"
Hiểu là:
- A `OQ-25` dữ liệu nhóm cũ: vào mục 7, người quyết Dev
- B `OQ-31` ma trận quyền: vào mục 7, người quyết Dev
- C `OQ-30` loại quan hệ: PO chốt ngay, **cố định** do hệ thống định nghĩa (quản lý, mentor), tổ chức không tự thêm. Đóng tồn đọng #3, không vào mục 7
- D `OQ-34` tài khoản kiểm thử và trả lời bình luận: PO chốt ngay, **tạo hoặc chọn thẳng trong UpLMS Ops**, không qua cây Lark. Đóng tồn đọng #4, không vào mục 7
- E tồn đọng #7 ba góc: PO đánh giá không ảnh hưởng, không vào mục 7, giữ ở PRD cho Dev
- X `OQ-33` `roles.is_group` và tồn đọng #6 hộp xác nhận gỡ khỏi lớp: vào mục 7, người quyết Dev. Tồn đọng #1 số liệu Analytics là việc của người viết, không đưa vào mục 7

## Q4. Điều PO muốn nhấn mạnh với ba PIC, hoặc chưa muốn đưa vào brief?
Vì sao hỏi: mục 1 "thứ cần quyết hôm nay" và mục 11 release lấy từ đây; Figma và Jira trong `intent.md` đang trống.
A. Nhấn mạnh dữ liệu thành viên theo thời gian là nền của báo cáo, phải có trước khi dữ liệu tích luỹ (Unit U7 trước U2, U4)  [đề xuất, theo thứ tự Unit trong PRD]
B. Nhấn mạnh hai luật đứng đụng nhau: Comment Replier và Nhóm, tách tài khoản theo vai
C. Không có gì thêm
X. Khác, xin nói rõ
Chặn: không
[Answer]: "lưu ý tất cả các phần lưu ý cho dev"
Hiểu là: mục 9 Technical Direction phải mang đủ mọi điểm lưu ý cho Dev đã có trong PRD (mục *TDD — ràng buộc nghiệp vụ cho thiết kế kỹ thuật*, *Dữ liệu phải lưu*, *Vấn đề tồn đọng*) và Impact Matrix (shared entity, luồng tự sinh, mail hàng loạt, tenant). Template giới hạn năm dòng in nghiêng đầu mục 9; cách làm: năm dòng là năm cụm, mỗi cụm trỏ sang bảng đầy đủ ở mục 6, không bỏ ý nào.

## Consolidated Summary
- Brief ghi theo vai Design, Tech, QA; không cần tên, PIC tự điền khi ký
- PIC ghi mục 8, 9, 10 trên repo qua merge request, PO merge; không đặt hạn
- Mục 7 có bốn câu, đều do Dev quyết: dữ liệu nhóm cũ (`OQ-25`) · ma trận quyền (`OQ-31`) · `roles.is_group` (`OQ-33`) · hộp xác nhận gỡ khỏi lớp (tồn đọng #6)
- PO chốt hai việc ngay, sẽ ghi DEC: loại quan hệ **cố định** (đóng `OQ-30`, tồn đọng #3) · tài khoản kiểm thử và trả lời bình luận **tạo hoặc chọn trong Ops** (đóng `OQ-34`, tồn đọng #4)
- Ba góc tồn đọng #7 không vào mục 7, giữ ở PRD cho Dev
- Mục 9 mang đủ mọi điểm lưu ý cho Dev từ PRD và Impact Matrix, năm dòng đầu là năm cụm trỏ sang mục 6
[Answer]: "Looks correct"
