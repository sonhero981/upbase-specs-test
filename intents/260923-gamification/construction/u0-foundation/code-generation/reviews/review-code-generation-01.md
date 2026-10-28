# Review code-generation 01 (toàn lát 2.6 → 3.5)

Reviewer: subagent general-purpose theo `engine/tech/agents/tech-reviewer.md` (fallback tech-protocol), 2026-10-13. Spot-check ~45 `file:line` trên `origin/staging` (lms-be 610f100, ops-fe 1e01033bf): gần như đúng hết. Sensor mọi stage Đạt.

**Kết luận: NOT READY** → đã sửa, xem cột Xử lý.

| Mã | Mức | Vấn đề | Xử lý |
|---|---|---|---|
| R-01 | Chặn | `origin/feature/gamification` có WP0 `65d3aad` (VietLH, 12/10): migration, entity, seed, module Ops; plan làm lại từ `staging`, trùng timestamp, trùng WP3 của cuongdq | ADR-001 viết lại: B01 dựng trên WP0, plan BE-1…BE-10 thành delta; ED-07 cập nhật `assignment.md`; DEC-T14 |
| R-02 | Chặn | `openspec/conventions/*` không có trên `origin/staging` | Plan ghi base `65d3aad`, `file:line` lms-be kiểm ở đó; change `run` commit lên branch cá nhân bước 0.1 |
| R-03 | Chặn | Filter menu `adminPermission && item` (`useMenuData.tsx:1434-1437`) ẩn mục với role thường; thiếu `sidebarIds` | OPS-5 thêm `sidebarIds`; OPS-6 sửa filter theo từng item; ui-map UI-5 |
| R-04 | Nên sửa | Thứ tự rule C-02 mơ hồ khi `is_enabled=false, is_visible=true` | C-02 + BE-5 chốt thứ tự: có `is_visible` khi tắt → 400 trước; TC-9 bốn case; unit test thứ 10 |
| R-05 | Nên sửa | Cột bảng mơ hồ (dbml tự mâu thuẫn) | Hết: bảng do WP0 tạo (`1789997000000-create-gamification-tables.ts:151-176`), B01 chỉ thêm một cột |
| R-06 | Nên sửa | PO nói "dùng màn 403 hiện có", thiết kế dùng antd `Result` vì nút AccessDenied đăng xuất | Ghi chú cho PO + DEC-T14 |
| R-07 | Nên sửa | Thiếu message lỗi BE + chuỗi ops-fe | BE-3 thêm `EXCEPTION_MESSAGES`; OPS-9 ghi chuỗi tiếng Anh |
| R-08 | Nên sửa | `form.ts:85` sai | Sửa `form.ts:66` |
| R-09 | Nên sửa | `tech-decisions.md` thiếu DEC-T6…T13 | Đã ghi DEC-T6…T14 |
| R-10 | Ghi nhận | BR-14.4, BR-15.4 ở TC nhưng không ở rules/trace | rules.md mục "Ngoài lát", traceability `reverse`; TC-4 bỏ BR-14.4, thêm dòng BR hoãn |
| R-11 | Ghi nhận | Race cache GET miss / PATCH | ADR-003 Consequences ghi accepted risk |
| R-12 | Ghi nhận | Gợi ý `Popconfirm` + `RedisCacheModule` | OPS-8, BE-5 |
| R-13 | Ghi nhận | Sơ đồ US14 PRD (tắt luôn Visibility) trái BR-14.2 | Ghi chú cho PO |
