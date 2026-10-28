---
intent: 260923-gamification
artifact: external-dependency-map
stage: 2.9 delivery-planning
version: 2.0
status: approved
approved_at: 2026-10-13 ([GIẢ LẬP] họp FE, BE, PO, QA, owner Bolt, DEC-T22)
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
scope: cả intent, 19 US (DEC-T15)
consumes: inception/units-generation/ v2.0 (DEC-T20) · inception/contract-design/contract-summary.md v2.0 (DEC-T21) · inception/test-cases/test-cases.md v1.0 (US14, US15; 2.81 cả intent làm song song) · tech-state.md · lms-be openspec/changes/upbase-221099-gamification/assignment.md
supersedes: v1.0 (B01 = U0, DEC-T10)
---

# External Dependency Map: Gamification, cả intent

Việc ngoài team Bolt phải có, ai lo, chặn Bolt nào, trễ thì làm gì.

| # | Phụ thuộc | Ai cung cấp | Chặn Bolt | Trễ thì | Trạng thái |
|---|---|---|---|---|---|
| ED-01 | Tài khoản staging SA, V, E, N và role tương ứng | BE lead / quản trị Ops | B01, mọi Bolt Ops | Test quyền trễ, không chặn code | Chưa |
| ED-02 | Ngoại lệ `tags` trong `backend.md` § 2 | BE lead | Review MR B01 | MR bị từ chối | Chưa |
| ED-03 | Cập nhật design gốc `upbase-221099` theo ADR-009…018 và contract v2.0 | BE lead | B02 trở đi | Dev BE làm theo bản cũ | Chưa |
| ED-04 | Lịch đưa `feature/gamification` lên `staging` | BE lead | Demo mọi Bolt | Demo ở môi trường dev | Chưa |
| ED-05 | Jira ticket từng Bolt | Owner Bolt `/jira-tasks` | Nhánh, MR | — | Chưa |
| ED-06 | Message lỗi mới (630001, 630012…630016) trong `en.exceptions.json` ops-fe, lms-fe | Owner Bolt | Hiển thị lỗi | Hiện mã thô | Trong Bolt |
| ED-07 | Cập nhật `assignment.md` theo bolt-plan (WP → Bolt, B01 sửa WP3) | BE lead | Tránh trùng việc | Hai người sửa cùng file | Chưa |
| ED-08 | Route websocket `/lms/socket.io` qua gateway staging/production | DevOps | B07 | Thẻ thông báo không tới | Chưa |
| ED-09 | Design còn thiếu (OQ-45): campaign học viên, nhật ký Ops, My Learning, sửa màn Gamification | PO / Designer | B04, B05, B17 (ui-map Provisional) | Làm theo component chuẩn, sửa sau | Chưa |
| ED-10 | PO chạy `/change-request` đưa 2.43 Q1–Q17 vào PRD | PO | Không chặn (DEC-T4, DEC-T17) | CR đổi khác thì mở lại stage | Chưa |
| ED-11 | Hình mặc định 24 mốc huy hiệu | Designer | B09 | Dùng hình mặc định của loại | Chưa |
| ED-12 | Thêm dev FE (nếu PO, CTO chọn) | CTO | Ngày xong | Lịch như bolt-plan | Chờ họp |
| ED-13 | QA lead có tên, chạy TC | PO / QA | 3.6 mọi Bolt | Owner tự chạy P0 | Chưa |
| ED-14 | Dữ liệu kiểm tải trên staging: 10.000 học viên, 5 triệu dòng ledger (script seed) | BE lead / DevOps | Hypothesis B05, B09, B12, B15 | Đo trên dữ liệu nhỏ, ghi rủi ro còn lại | Chưa |
| ED-15 | Tạo topic Kafka mới `process_gamification_badge_backfill` (và kiểm `process_gamification_checkin`) trên staging, production | DevOps | B06, B09 | Trao bù, check-in không chạy | Chưa |
| ED-16 | Socket.io nhiều instance ở production: sticky session hoặc chỉ websocket transport qua gateway, Redis adapter | DevOps | B07 (production) | Thẻ thông báo mất ngẫu nhiên | Chưa |
| ED-17 | 2.81 test-cases cả intent duyệt (QA lead) | Tech lead / QA | 3.1 của B02…B18 (gate 2.9 có điều kiện) | Bolt chưa vào Construction | Đang `[R]` |
