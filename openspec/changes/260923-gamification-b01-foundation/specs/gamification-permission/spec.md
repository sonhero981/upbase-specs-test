# Spec Delta

## Purpose

Đưa quyền Gamification vào hệ phân quyền Ops hiện có: tách xem và sửa, chặn menu, trang và API với người không có quyền.

## ADDED Requirements

### Requirement: Nhóm quyền Gamification trên màn role
Hệ thống SHALL hiện nhóm quyền `gamification` trên màn role hiện có sau khi bản mới lên môi trường, gồm quyền xem và quyền sửa cấu hình; không có màn phân quyền riêng. Nguồn: BR15.1, BR15.5. TC-15.

#### Scenario: Quản trị mở màn role
- **WHEN** superadmin mở màn tạo hoặc sửa role
- **THEN** thấy nhóm `gamification` với `View gamification settings`, `Update gamification settings`

### Requirement: Tách quyền xem và sửa
Người chỉ có quyền xem SHALL thấy công tắc nhưng MUST NOT đổi được; người có quyền sửa đổi được. API lưu MUST trả 403 với người không có quyền sửa. Nguồn: BR15.2, BR15.7. TC-16, TC-17.

#### Scenario: Chỉ quyền xem
- **WHEN** nhân sự chỉ có quyền xem mở trang và gọi API lưu
- **THEN** công tắc không bấm được, API lưu trả `403|000000`

#### Scenario: Có quyền sửa
- **WHEN** nhân sự có quyền sửa bật `Gamification`
- **THEN** lưu thành công

### Requirement: Không quyền thì không vào
Nhân sự không có quyền nào trong nhóm Gamification SHALL không thấy mục menu; mở thẳng đường dẫn MUST ra màn 403; API đọc MUST trả 403. Đổi quyền có hiệu lực theo cơ chế hiện có. Nguồn: BR15.3, BR15.6. TC-18, TC-19.

#### Scenario: Không có quyền
- **WHEN** nhân sự không có quyền gamification xem menu và mở `/gamification`
- **THEN** không có mục Gamification, trang hiện 403, API đọc trả `403|000000`

#### Scenario: Được gán quyền sau
- **WHEN** quản trị gán quyền xem cho role của nhân sự và nhân sự tải lại thông tin
- **THEN** mục Gamification hiện và trang mở được
