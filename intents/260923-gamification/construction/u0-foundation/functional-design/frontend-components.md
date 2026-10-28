---
intent: 260923-gamification
unit: u0-foundation
artifact: frontend-components
stage: 3.1 functional-design
version: 1.0
status: approved
approved_at: 2026-10-13 ([GIẢ LẬP] BE lead, DEC-T11)
---
# Frontend Components: U0 `u0-foundation`

Chỉ ops-fe (ADR-006). Tên component là khái niệm; file cụ thể ở code-generation-plan.

| Mã | Component | Trách nhiệm | Rule |
|---|---|---|---|
| FE-O1 | GamificationSettingsPage | Kiểm quyền vào trang (một trong ba quyền); đọc cấu hình; quyết hiện khối chung theo quyền | BR15.3, BR15.7 |
| FE-O2 | GeneralSettingsCard | Công tắc `Gamification`; `Visibility in UpLMS` + dòng giải thích khi Gamification bật; chế độ chỉ xem (công tắc không bấm được) khi không có quyền sửa | BR14.1, BR14.2, BR15.7 |
| FE-O3 | ConfirmPopover | Popover nhỏ gắn cạnh công tắc (không modal) hỏi lại hai thao tác; Huỷ thì công tắc về như cũ, không gửi lưu. Xác nhận sẵn có của Ops là modal nên không dùng | BR14.13 |
| FE-O4 | SaveFeedback | Báo `Saved` nhỏ tự ẩn; lỗi thì về giá trị đã lưu + báo lỗi | BR14.12 |
| FE-O5 | Menu item Gamification | Hiện khi có ít nhất một quyền | BR15.3 |
| FE-O6 | NoAccess | Màn 403 chuẩn (không đăng xuất người dùng); màn AccessDenied sẵn có không dùng vì nút của nó đăng xuất | BR15.3 |

## Tương tác
- Đang lưu một công tắc thì không gửi lần lưu thứ hai cho chính công tắc đó (bấm lại bị bỏ qua tới khi có kết quả).
- Công tắc của thư viện UI đổi giá trị trước khi báo sự kiện: khi Huỷ popover hoặc lưu lỗi phải đặt lại giá trị đã lưu.
- Sau khi lưu thành công dùng bản ghi server trả về làm giá trị đã lưu (không tự suy).

## Trạng thái màn
| Trạng thái | Hiển thị |
|---|---|
| Đang tải | Skeleton khối chung |
| Lỗi tải | Thông báo lỗi chuẩn Ops |
| Không quyền | NoAccess (403) |
| Chỉ quyền học viên | Trang tiêu đề Gamification, không khối nào (lát này) |
