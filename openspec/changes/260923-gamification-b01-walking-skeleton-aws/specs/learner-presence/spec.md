# Spec Delta

## Purpose

Ghi nhận học viên có mặt trên UpLMS mỗi ngày theo múi giờ tổ chức, tự động từ app học viên và không bao giờ cản trở việc học.

## ADDED Requirements

### Requirement: Một ngày có mặt mỗi học viên mỗi ngày
Khi Gamification bật, hệ thống SHALL ghi tối đa một ngày có mặt cho mỗi học viên mỗi ngày, ngày cắt theo múi giờ tổ chức; lần sau trong ngày và yêu cầu đồng thời MUST trả `ALREADY_RECORDED`, không lỗi. Visibility tắt vẫn ghi. Nguồn: BR5.1, BR5.3, BR5.13 (`construction/u0-walking-skeleton/functional-design/rules.md`). TC-13, TC-32.

#### Scenario: Lần đầu trong ngày
- **WHEN** Gamification bật và học viên mở lms-pro lần đầu trong ngày
- **THEN** `POST /gamification/presence` trả 200 `RECORDED`, `presence_date` = hôm nay theo `Asia/Ho_Chi_Minh`, `streak` và `points_awarded` `null`; có đúng một bản ghi (U0-IC1)

#### Scenario: Gửi lại cùng ngày
- **WHEN** gọi `POST /gamification/presence` lần nữa trong ngày
- **THEN** trả `ALREADY_RECORDED`, không thêm bản ghi (TC-32 phần curl)

#### Scenario: Hai thiết bị cùng lúc
- **WHEN** hai yêu cầu ghi nhận của cùng học viên đến đồng thời
- **THEN** một `RECORDED`, một `ALREADY_RECORDED`, không lỗi hệ thống (BR5.1)

### Requirement: Không ghi khi Gamification tắt
Khi Gamification tắt hoặc tổ chức chưa có cấu hình, hệ thống SHALL không ghi gì và trả `DISABLED` với `next_check_after` = min(lúc nhận + 60 phút, 00:00 hôm sau theo múi giờ tổ chức). Nguồn: BR5.12, BR5.15. TC-40.

#### Scenario: Tắt rồi học viên vào
- **WHEN** Gamification tắt và học viên mở lms-pro
- **THEN** 200 `DISABLED`, `presence_date` `null`, không có bản ghi mới (TC-40, U0-IC3)

### Requirement: Mốc hỏi lại
Mỗi kết quả ghi nhận SHALL kèm `next_check_after`; ngoài `DISABLED` là 00:00 ngày kế tiếp theo múi giờ tổ chức, biểu diễn UTC. Nguồn: BR5.15.

#### Scenario: Biên ngày theo giờ tổ chức
- **WHEN** học viên được ghi lúc 10:00 (+07) ngày D
- **THEN** `next_check_after` = 17:00Z ngày D (BR5.3, BR5.15)

### Requirement: Ghi nhận không cản trở học viên
App học viên SHALL gửi tín hiệu tự động, một lần cho mỗi người dùng trong một phiên mở app, không chờ, không thông báo, không chuyển trang khi lỗi; hệ thống MUST không trả từ chối quyền cho học viên. Nguồn: BR5.2, BR5.11, BR5.16, BR5.17, BR5.18. TC-48.

#### Scenario: Lỗi ghi nhận
- **WHEN** ghi nhận trả lỗi hệ thống hoặc mất mạng
- **THEN** lms-pro tải và dùng bình thường, không toast, không chuyển trang (BR5.11)

#### Scenario: Hành vi 403 cũ không đổi
- **WHEN** một API cũ trả 403 và ghi nhận trả `400|010004`
- **THEN** API cũ vẫn chuyển về `/` như trước; ghi nhận lỗi không toast, không chuyển trang (TC-48)

#### Scenario: Trang công khai
- **WHEN** người chưa đăng nhập mở trang chứng chỉ công khai
- **THEN** không gửi tín hiệu (BR5.17)
