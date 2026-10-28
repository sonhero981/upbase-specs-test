---
intent: 260923-gamification
artifact: external-dependency-map
stage: 2.9 delivery-planning
version: 1.0
status: approved
approved_at: 2026-10-13 ([GIẢ LẬP] họp, DEC-T10)
---
# External Dependency Map: Gamification, lát Nền tảng

| # | Phụ thuộc | Ai cung cấp | Cần cho | Trạng thái |
|---|---|---|---|---|
| ED-01 | Tài khoản staging: SA, V (chỉ xem), E (sửa), N (không quyền) | BE lead / quản trị Ops | TC-15…TC-19 | Cần tạo role V, E sau deploy |
| ED-02 | Ngoại lệ `tags` trong `lms-be/openspec/conventions/backend.md` § 2 | BE lead | Review MR lms-be | Chưa |
| ED-03 | Cập nhật design gốc `upbase-221099-gamification` (PATCH, bỏ timezone, `visibility_first_enabled_at`, cache) | BE lead | Unit sau | Chưa |
| ED-04 | Lịch đưa `feature/gamification` lên nhánh sprint / `staging` | BE lead | TC trên staging | Chưa |
| ED-05 | Jira ticket B01 | Owner Bolt `/jira-tasks` | Nhánh, PR | Chưa |
| ED-06 | Message `exceptions.gamification_disabled` trong `en.exceptions.json` ops-fe | Owner Bolt | TC-9 hiển thị | Trong B01 |
| ED-07 | Cập nhật `assignment.md` của `upbase-221099-gamification`: phần cấu hình chung + quyền của WP3 chuyển sang B01 | BE lead | Tránh trùng việc với cuongdq (DEC-T14) | Chưa |
