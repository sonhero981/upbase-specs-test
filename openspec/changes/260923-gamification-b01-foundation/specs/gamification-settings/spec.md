# Spec Delta

## Purpose

Cho vận hành đọc và bật tắt hai công tắc chung của gamification theo tổ chức trên UpLMS Ops; mặc định tắt hẳn, có hiệu lực ngay khi lưu.

## ADDED Requirements

### Requirement: Cấu hình mặc định tắt hẳn
Hệ thống SHALL trả cấu hình của tổ chức hiện tại; tổ chức chưa có cấu hình MUST nhận bản mặc định mọi công tắc tắt, kể cả khi hai yêu cầu đầu tiên đến cùng lúc. Nguồn: BR14.6, BR14.8. TC-1, TC-14.

#### Scenario: Tổ chức chưa có cấu hình
- **WHEN** superadmin mở trang Gamification lần đầu
- **THEN** trang chỉ có công tắc `Gamification` tắt; cấu hình trả `is_enabled=false`, `is_visible=false`, `has_been_visible=false`

#### Scenario: Hai yêu cầu đầu tiên cùng lúc
- **WHEN** hai yêu cầu đọc đến cùng lúc ở tổ chức chưa có cấu hình
- **THEN** chỉ một bản ghi được tạo, cả hai nhận cùng bản mặc định

### Requirement: Bật tắt Gamification ghi mốc bật
Vận hành SHALL bật tắt `Gamification` bằng một lần bấm; chuyển sang bật MUST ghi `last_enabled_at`, lần đầu ghi thêm `first_enabled_at`; tắt MUST giữ nguyên giá trị Visibility. Tắt phải xác nhận qua popover. Nguồn: BR14.1, BR14.2, BR14.5, BR14.13. TC-2, TC-6, TC-7, TC-8.

#### Scenario: Bật lần đầu
- **WHEN** vận hành có quyền sửa bấm bật `Gamification`
- **THEN** lưu ngay, `first_enabled_at` = `last_enabled_at` = lúc bật, hiện `Saved`, công tắc `Visibility in UpLMS` xuất hiện

#### Scenario: Huỷ tắt
- **WHEN** vận hành bấm tắt `Gamification` rồi chọn `Cancel` trên popover
- **THEN** công tắc về bật và không có yêu cầu lưu nào

#### Scenario: Tắt rồi bật lại
- **WHEN** vận hành xác nhận tắt rồi bật lại `Gamification`
- **THEN** `last_enabled_at` đổi, `first_enabled_at` giữ nguyên, `Visibility in UpLMS` hiện lại với giá trị cũ

### Requirement: Visibility chỉ khi Gamification bật
`Visibility in UpLMS` SHALL chỉ hiện và chỉ đổi được khi `Gamification` đang bật. Lần bật đầu tiên trong đời tổ chức MUST hỏi lại bằng popover và ghi mốc; các lần sau không hỏi. Nguồn: BR14.2, BR14.13. TC-4, TC-5, TC-9.

#### Scenario: Bật Visibility lần đầu
- **WHEN** vận hành bật `Visibility in UpLMS` khi `has_been_visible=false` và chọn `Show`
- **THEN** lưu `is_visible=true`, `has_been_visible` thành true

#### Scenario: Bật Visibility lần sau
- **WHEN** vận hành bật `Visibility in UpLMS` khi `has_been_visible=true`
- **THEN** lưu ngay, không popover

#### Scenario: Bật Visibility khi Gamification tắt
- **WHEN** yêu cầu lưu `is_visible=true` gửi khi `is_enabled=false`
- **THEN** hệ thống trả `400|630001` và không đổi cấu hình

#### Scenario: Tắt Visibility khi Gamification tắt
- **WHEN** yêu cầu lưu `is_visible=false` gửi khi `is_enabled=false`, kể cả khi `is_visible` đang là false
- **THEN** hệ thống trả `400|630001` và không đổi cấu hình

### Requirement: Lưu một công tắc, có hiệu lực ngay
Mỗi yêu cầu lưu SHALL đổi đúng một công tắc; yêu cầu không hợp lệ MUST bị từ chối. Lần đọc ngay sau khi lưu MUST thấy giá trị mới. Lưu lỗi thì màn về giá trị đã lưu. Nguồn: BR14.10, BR14.11, BR14.12. TC-10, TC-11, TC-13.

#### Scenario: Body không hợp lệ
- **WHEN** yêu cầu lưu có body rỗng, hai công tắc, hoặc giá trị không phải boolean
- **THEN** hệ thống trả `422|000405`, cấu hình không đổi

#### Scenario: Đọc ngay sau khi lưu
- **WHEN** vận hành tắt `Gamification` rồi cấu hình được đọc ngay
- **THEN** kết quả đọc là `is_enabled=false`

#### Scenario: Lưu lỗi
- **WHEN** yêu cầu lưu thất bại
- **THEN** công tắc về giá trị đã lưu, báo lỗi, không hiện `Saved`

### Requirement: Cô lập theo tổ chức
Cấu hình SHALL gắn với một tổ chức; người của tổ chức này MUST NOT đọc hay ghi cấu hình tổ chức khác. Múi giờ là thuộc tính tổ chức, mặc định `Asia/Ho_Chi_Minh`, không ghi qua API cấu hình. Nguồn: BR14.8, BR14.9. TC-12.

#### Scenario: Đọc cấu hình tổ chức khác
- **WHEN** nhân sự tổ chức A gọi API cấu hình
- **THEN** chỉ nhận cấu hình tổ chức A
