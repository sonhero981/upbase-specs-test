---
intent: 260923-gamification
unit: u0-foundation
artifact: entities
stage: 3.1 functional-design
version: 1.0
status: approved
approved_at: 2026-10-13 ([GIẢ LẬP] BE lead, DEC-T11)
---
# Entities: U0 `u0-foundation`

Technology-agnostic. Kiểu dữ liệu, bảng, cache cụ thể ở `../code-generation/code-generation-plan.md`.

## GamificationSetting
Cấu hình gamification của một tổ chức. Mỗi tổ chức đúng một bản (BR14.8).

| Thuộc tính | Ý nghĩa | Bắt buộc | Mặc định | Ai đổi |
|---|---|---|---|---|
| tenant | Tổ chức sở hữu | Có | — | Tạo lúc đầu, không đổi |
| isEnabled | Công tắc `Gamification` | Có | false (BR14.6) | Vận hành có quyền sửa |
| isVisible | Công tắc `Visibility in UpLMS` | Có | false | Vận hành có quyền sửa; giữ giá trị khi isEnabled false (BR14.2) |
| firstEnabledAt | Lần đầu bật `Gamification` | Không | rỗng | Hệ thống, chỉ ghi một lần |
| lastEnabledAt | Lần bật `Gamification` gần nhất | Không | rỗng | Hệ thống, mỗi lần bật (BR14.5) |
| visibilityFirstEnabledAt | Lần đầu bật `Visibility in UpLMS` | Không | rỗng | Hệ thống, chỉ ghi một lần (BR14.13) |
| updatedAt | Lần ghi gần nhất | Có | lúc tạo | Hệ thống |

Thuộc tính của US8–US11 (bốn công tắc chức năng, bảng xếp hạng, trần hạng) có trên cùng bản ghi theo design gốc nhưng thuộc Unit sau, U0 không đọc ghi.

Trạng thái suy ra:
| isEnabled | isVisible | Trạng thái (BR14.1) |
|---|---|---|
| false | bất kỳ | Tắt hẳn |
| true | false | Chạy ngầm |
| true | true | Bật đầy đủ |

## TenantProfile (sửa)
| Thuộc tính | Ý nghĩa | Mặc định |
|---|---|---|
| timezone | Múi giờ IANA của tổ chức (BR14.9) | `Asia/Ho_Chi_Minh` cho tổ chức có sẵn và mới |

## Quyền Gamification (dữ liệu của hệ phân quyền sẵn có)
| Quyền | Được làm (BR15.7, lát này) |
|---|---|
| Xem cấu hình | Mở trang, xem công tắc |
| Sửa cấu hình | Mở trang, xem và đổi công tắc |
| Xem danh sách học viên và hạng | Mở trang (để thấy khối Campaign ở Unit sau); lát này không thấy khối chung |

Không có entity quyền mới (US15 Data Field); chỉ thêm bản ghi quyền.
