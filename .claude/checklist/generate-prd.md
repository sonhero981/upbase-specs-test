# Checklist: Generate PRD

## Tiền điều kiện
- [ ] **[BLOCK]** Đủ ba artifact đã duyệt: BRD (G1) · Impact Matrix (G2) · Solution (G3). Thiếu một → **dừng, không viết**
- [ ] Đã confirm danh sách US ở 9A trước khi viết chi tiết
- [ ] Đã hoàn tất Field Intake ở 9B trước khi viết Acceptance criteria

## Cấu trúc
- [ ] Có bảng **metadata** đầu: Target release · Epic/Story link Jira · Document owner · Designer · Tech lead · QA · Reviewer · Document status
- [ ] Có **Document version**
- [ ] **[BLOCK]** `Metrics success` — hoặc là chỉ số **thật của chính tính năng này**, hoặc **đã xoá hẳn mục**. Còn bảng ví dụ template (NPS, App Store, Transaction Input Time) = **lỗi nặng**
- [ ] `Preferences` có đủ link Dev/QA cần: Figma · tài liệu liên quan · API tham chiếu · tài khoản staging
- [ ] `Solution` tách `TDD` / `Database` / `API` khi có nội dung
- [ ] Cuối PRD có `Vấn đề tồn đọng`
- [ ] **[BLOCK]** Mục không áp dụng đã **xoá hẳn**, không để lại nội dung mẫu

## Specific Requirement
- [ ] US đánh số `US1`, `US2`… liên tục
- [ ] US chưa làm → ghi rõ trong tiêu đề (`US3: … — chưa làm`)
- [ ] Mỗi US đủ: User story · Pre-Condition · Scenario · Acceptance criteria · Out of scope
- [ ] `User story` viết **câu tiếng Việt tự nhiên**, không ép khuôn As a/I want/So that
- [ ] **[BLOCK]** `Conner case` **để trống** — việc của QA
- [ ] `Out of scope` có nội dung thật, không bỏ trống

## Acceptance criteria
- [ ] Bảng UI dùng đúng dạng: **A** `Màn hình│Giao diện│Field│Yêu cầu` (mới) hoặc **B** `Thay đổi│Section│Field│Validate` (sửa)
- [ ] Cột `Yêu cầu` đủ: định dạng · placeholder · options · mặc định · disable · tooltip · validate · hành vi
- [ ] Business rule gắn mã `BR-<số US>.<số thứ tự>`, **không trùng** trong PRD
- [ ] Rule chạm tính năng có sẵn → **dẫn mã rule KB** (`BR-EDIT-07`, `KB-CLASS-03`)
- [ ] `Data Field` — US không đụng dữ liệu thì bỏ mục, không để bảng rỗng

## Kỹ thuật
- [ ] **[BLOCK]** Field **hiện có** được nhận diện là hiện có — viết thành "mới" khiến Dev tạo trùng
- [ ] Bảng mới trong `Database` khai báo rõ có `tenant_id` hay không
- [ ] Endpoint mới đã **đối chiếu Swagger**, không trùng 708 operation đã có
- [ ] Mọi **hằng số cứng** ghi rõ: hardcode hay cấu hình được
- [ ] Mail event bị chạm đã đối chiếu KB `13`

## Chất lượng
- [ ] **[BLOCK]** Không bịa field. Không tra được và người dùng chưa trả lời → `Open Question`
- [ ] Ô `❓BA` chưa quyết → đã chuyển thành `Open Question`
- [ ] Phần chờ xác nhận → đánh dấu `Draft - Pending Confirmation`

## Delivery
- [ ] **[BLOCK]** Người dùng **đã xem bản trước chưa?** Rồi → **tạo file version mới**, giữ nguyên bản cũ, thêm mục **Lịch sử thay đổi**. Chưa → sửa tại chỗ được.
      > Mốc tăng version là **mỗi lần qua Gate** hoặc mỗi đợt người dùng trả lời một loạt câu hỏi. Làm liên tục trong một phiên thì rất dễ quên — xem `CLAUDE.md` mục *Cách làm việc*.
- [ ] **[BLOCK]** **Không có mục `Database` và `API`** — không khai bảng, không khai endpoint. Chỉ ghi *thông tin nào phải lưu* và *hệ thống phải cho phép làm gì*
- [ ] **[BLOCK]** Không có sequence diagram · cấu trúc bảng · thuật toán · lựa chọn thư viện · ước lượng hiệu năng
- [ ] Đúng thư mục `docs/prd/`, đúng version
- [ ] Đã chuẩn bị nội dung trình Gate 4, **nêu rõ mục nào đã xoá và vì sao**
