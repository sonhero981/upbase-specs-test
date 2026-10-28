# Spec Delta

## Purpose

Cho vận hành đọc và bật tắt gamification của tổ chức trên UpLMS Ops: mặc định tắt hẳn, gắn theo tổ chức, chỉ người có quyền thao tác được.

## ADDED Requirements

### Requirement: Cấu hình mặc định tắt hẳn
Hệ thống SHALL trả cấu hình gamification của tổ chức hiện tại; tổ chức chưa có cấu hình MUST nhận bản mặc định (mọi công tắc tắt, mọi mốc rỗng), kể cả khi hai yêu cầu đầu tiên đến cùng lúc. Tổ chức lấy từ phiên. Nguồn: BR14.6, BR14.8 (`construction/u0-walking-skeleton/functional-design/rules.md`). TC-1, TC-13.

#### Scenario: Tổ chức chưa có cấu hình
- **WHEN** superadmin mở trang Gamification lần đầu
- **THEN** trang chỉ có một công tắc `Gamification` ở trạng thái tắt; đọc cấu hình trả `is_enabled=false`, mọi mốc `null` (TC-1)

#### Scenario: Hai yêu cầu đầu tiên cùng lúc
- **WHEN** hai superadmin cùng mở trang lần đầu ở tổ chức chưa có cấu hình
- **THEN** chỉ một bản ghi được tạo và cả hai nhận cùng bản mặc định, không lỗi (BR14.6)

### Requirement: Bật tắt Gamification ghi mốc bật
Vận hành SHALL bật tắt công tắc `Gamification` bằng một lần bấm, không nút lưu; mỗi lần chuyển tắt sang bật MUST ghi `last_enabled_at`, lần đầu ghi thêm `first_enabled_at`; tắt MUST giữ nguyên Visibility và bốn công tắc chức năng. Nguồn: BR14.1, BR14.5, BR14.7, BR14.15. TC-2, TC-8.

#### Scenario: Bật lần đầu
- **WHEN** superadmin bấm bật `Gamification`
- **THEN** cấu hình trả `is_enabled=true`, `first_enabled_at` = `last_enabled_at` = lúc bật (BR14.5)

#### Scenario: Tắt rồi bật lại
- **WHEN** superadmin tắt rồi bật lại `Gamification`
- **THEN** `last_enabled_at` đổi, `first_enabled_at` giữ nguyên, các công tắc khác giữ giá trị (BR14.5, BR14.7)

#### Scenario: Ghi dữ liệu không hợp lệ
- **WHEN** gửi ghi cấu hình với body rỗng hoặc `is_enabled` không phải boolean
- **THEN** trả lỗi dữ liệu không hợp lệ `422|000405`, bản ghi không đổi; trường lạ bị bỏ qua (BR14.15)

#### Scenario: Ghi lỗi trên màn
- **WHEN** ghi công tắc thất bại (mạng, hệ thống)
- **THEN** công tắc về giá trị đã lưu trước đó (BR14.1)

### Requirement: Chỉ người có quyền thao tác cấu hình
Trang và các thao tác đọc ghi cấu hình gamification SHALL chỉ mở cho người có quyền xem / sửa; trong lát chưa role nào có quyền nên chỉ superadmin qua. Staff không có quyền MUST thấy trạng thái không có quyền, không bị đăng xuất. Nguồn: BR14.14 (ADR-007, chờ OQ-C1). TC-14, TC-49.

#### Scenario: Staff không có quyền
- **WHEN** staff không phải superadmin mở thẳng trang Gamification và gọi đọc / ghi cấu hình
- **THEN** không có mục menu; trang hiện trạng thái không có quyền, không đăng xuất; API trả `403|000000` (TC-14)

#### Scenario: Quyền trang cũ không đổi
- **WHEN** staff có role cũ vào các trang Ops có sẵn sau khi quét quyền route mới
- **THEN** quyền trang cũ như trước; superadmin vào được trang Gamification (TC-49)

### Requirement: Múi giờ tổ chức
Mỗi tổ chức SHALL có múi giờ, mặc định `Asia/Ho_Chi_Minh` cho tổ chức đang có và tổ chức mới; không có chỗ chọn múi giờ trên trang Gamification. Nguồn: BR14.9. TC-13, TC-46.

#### Scenario: Thêm múi giờ không đổi hành vi cũ
- **WHEN** gọi `GET /setting` và `GET /me` ở hai app sau khi triển khai
- **THEN** các field cũ giữ nguyên, có thêm `timezone = Asia/Ho_Chi_Minh` (TC-46)

### Requirement: Chỉ bật trên staging tới khi hoàn tất lát
Gamification SHALL chỉ được bật trên staging cho tới khi Bolt B04 xong; trước khi bật production MUST dọn dữ liệu ngày có mặt do Bolt này ghi. Nguồn: BR14.16 (bolt-plan R1, R2).

#### Scenario: Phát hành B01
- **WHEN** PR của Bolt này lên production
- **THEN** cấu hình Gamification ở production vẫn tắt (mặc định BR14.6)
