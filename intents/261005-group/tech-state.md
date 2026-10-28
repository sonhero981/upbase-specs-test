---
intent: 261005-group
status: Running
---
# Tech state: 261005-group

| | |
|---|---|
| PRD dùng | `inception/prd/prd.md` version 0.7, approved, 21 US |
| Tech Design 1 | `inception/tech-design/fe-technical-design.md` v2.2 (based-on prd v0.6) · `be-technical-design.md` 23/10/2026 · Decision Brief v0.1 chưa ký |
| Phạm vi đợt này | **Lane FE**, toàn bộ US có phần FE: US1–US18 và US21. US19, US20 không có FE |
| Tech lead tác giả | FE lead · Nguyễn Hùng Sơn |
| FE lead | Nguyễn Hùng Sơn |
| BE lead | Đoàn Quang Cường |
| QA lead | chưa có |
| Dev code (owner Bolt) | **Nguyễn Hùng Sơn** — FE hiện chỉ có một người, toàn bộ lane FE do một mình làm |

## Inception
Ký hiệu: `[ ]` chưa làm · `[-]` đang làm · `[?]` chờ duyệt · `[R]` đang sửa · `[x]` đã duyệt · `[S]` bỏ qua kèm lý do

- [x] 2.1 reverse-engineering · codekb `domain/codekb/ops-fe/`, `lms-fe/` đã có
- [S] 2.6 domain-design · đường ngắn (DEC-T1): dùng `be-technical-design.md` của BE lead thay Domain Design
- [S] 2.7 units-generation · đường ngắn (DEC-T1): Unit U1–U7 lấy từ `fe-technical-design.md` mục 7
- [S] 2.8 contract-design · đường ngắn (DEC-T1): contract chưa có, là phụ thuộc chặn số 1 ở mục 13 của thiết kế FE
- [ ] 2.81 test-cases
- [S] 2.9 delivery-planning · đường ngắn (DEC-T1): thay bằng `construction/fe-task-plan.md`

## Construction
| Bolt | Unit | 3.1 functional | 3.41 ui-map | 3.5 code-gen | 3.6 build-test | Owner | Change |
|---|---|---|---|---|---|---|---|
| F1 | U7 nền tảng + U1 khung nhóm | S (thiết kế FE đủ) | S | `construction/fe-task-plan.md` | | Nguyễn Hùng Sơn | chưa mở |
| F2 | U1 còn lại + U2 | S | S | nt | | Nguyễn Hùng Sơn | chưa mở |
| F3 | U4 quan hệ người | S | S | nt | | Nguyễn Hùng Sơn | chưa mở |
| F4 | U3 giao nội dung | S | S | nt | | Nguyễn Hùng Sơn | chưa mở |
| F5 | U7 báo cáo + nhật ký | S | S | nt | | Nguyễn Hùng Sơn | chưa mở |
| F6 | U5 phạm vi + US21 | S | S | nt | | Nguyễn Hùng Sơn | chưa mở |

Trạng thái Bolt: Dự kiến · Thiết kế · Plan duyệt · Đang code · Chờ demo · Xong. Hiện mọi Bolt ở **Dự kiến**.

## Quyết định
Ghi vào `decisions.md` ở gốc intent, mã `DEC-T<n>`.

## Current
| | |
|---|---|
| Stage | 3.5 code-generation, Part 1 (plan) cho lane FE |
| Next action | Làm F1 theo thứ tự ở `construction/fe-task-plan.md` mục 4.0. Không chờ BE: dựng trên mock, nối API thật khi BE giao contract |
| Chờ PO | Câu hỏi mở #19 (mã màn cho ba thay đổi của US21), #15 (chức năng gửi thông báo đã bật chưa) |

## Ghi chú cho PO
- `fe-technical-design.md` v2.2 dựa trên PRD v0.6, **chưa phủ US21** (CR7 thêm). Phần US21 trong `fe-task-plan.md` dựng từ PRD v0.7, cần Tech PIC cập nhật thiết kế lên v2.3.
- `ux-design.md` chưa có mã màn cho ba thay đổi của US21 (câu hỏi mở #19 của PRD).

## Log
- 2026-10-26 DEC-T4 thay DEC-T2: port UI demo ở nhánh `feature/manager-group` thay vì dựng lại. 13 task FE trên Jira (UPLND-423 đến 435), gán Nguyễn Hùng Sơn, tổng 9 điểm (DEC-T5).
- 2026-10-26 Khởi tạo phần Tech theo DEC122 (PO chốt PRD final qua CR7, không viết Decision Brief lúc này). Đồng bộ intent từ `po/main`: PRD v0.5 → v0.7, thêm `be-technical-design.md`, `decision-brief.md`. Lập `construction/fe-task-plan.md` cho lane FE theo đường ngắn.
