---
bolt: 260923-gamification-b01-foundation
intent: 260923-gamification
store_commit: 95d8fe6
store_dirty: false
written_at: 2026-11-11 16:51
---
# Bàn giao · B01 Nền tảng

File này do `/bolt` ghi và cập nhật. Mỗi phiên Claude mở trong repo `flow: comet` đọc mục của repo mình trước khi `/comet-open`, để ba repo dùng chung một bản quyết định thay vì dán lại từ terminal. Người chỉ sửa tay mục "Quyết định chung".

`store_dirty: true` nghĩa là cây làm việc của store có sửa chưa commit ở intent hoặc change Bolt, nên `store_commit` chưa phản ánh hết tài liệu đã đọc. Khi đó ghi rõ tệp nào chưa commit ở mục "Quyết định chung".

## Chung cho cả Bolt

| | |
|---|---|
| Intent | `intents/260923-gamification/` |
| PRD / contract | PRD 0.15 (proposal Bolt còn ghi 0.14, xem "Quyết định chung") / `contract-summary.md` 2.0 Agreed |
| Jira | Chưa có subtask |
| Phụ thuộc | Không có |
| Thứ tự repo | lms-be (flow `opsx`) → ops-fe (flow `comet`) |

## Quyết định chung

Điều mọi repo phải theo, mỗi dòng kèm ngày và người chốt. Chưa có quyết định nào.

Cảnh báo của `/bolt` ngày 2026-11-11, chờ người xác nhận:

- [chờ xác nhận] Proposal Bolt ghi PRD 0.14, nhưng `prd.md` hiện hành là 0.15 (CR-014, duyệt 2026-10-14). Tech lead xác nhận 0.15 không đổi phạm vi US14, US15 và BR đã liệt kê trong proposal, rồi cập nhật proposal Bolt, trước khi mở change ở repo.

## Tiến độ theo repo

| Repo | flow | Change ở repo | Branch | Owner | Trạng thái | Cập nhật |
|---|---|---|---|---|---|---|
| lms-be | opsx, `change_style: feature` | chưa có (xem ghi chú dưới bảng) | chưa tạo | cuongdq (Đoàn Quang Cường) | Chưa có change | 2026-11-11 |
| ops-fe | comet | `260923-gamification-b01-foundation` | chưa tạo | Nguyễn Hùng Sơn | Chưa bàn giao | 2026-11-11 |

Cột "Change ở repo": repo `comet` và repo `opsx` kiểu `bolt` dùng đúng tên change Bolt; repo `opsx` kiểu `feature` ghi change theo feature mà người chọn (`/bolt` không tự đặt tên).

Ghi chú lms-be: change gần nhất của intent này ở lms-be là `upbase-221099-gamification` (be-feature, 63/63 task xong, PRD v0.14 từ bản đọc cục bộ). Change đó không chứa việc BE của Bolt này (migration `visibility_first_enabled_at`, PATCH một trường, mã `630001`, theo nhóm 1 của change Bolt). Owner lms-be quyết: bổ sung vào change đó bằng `/opsx:update`, hoặc mở change mới theo ticket, rồi ghi tên change vào cột trên.

## Repo ops-fe (flow: comet)

Tên change ở repo: `260923-gamification-b01-foundation`. Đặt đúng tên này khi chạy `/comet-open`.

Đọc trước khi code, đường dẫn tính từ gốc store:

- `intents/260923-gamification/construction/u0-foundation/code-generation/code-generation-plan.md` mục `## ops-fe`: plan file của repo này
- `intents/260923-gamification/inception/contract-design/contract-summary.md`: contract C-01, C-02
- `intents/260923-gamification/construction/u0-foundation/ui-map/ui-map.md`: UI map cho `/ui-gate`
- `intents/260923-gamification/inception/test-cases/test-cases.md` TC-1..TC-11 (kiểm tích hợp TC-1..TC-21)
- `openspec/changes/260923-gamification-b01-foundation/specs/`: Scenario của Bolt, nguồn của `specs/` ở repo

Nhóm task thô của repo, từ `tasks.md` của change Bolt:

- 2.1 Phần còn lại sau code phiên trước: types, xoá mock chết, `aria-label`, mã `630001`, `pnpm gen`, `/fe:review` (plan OPS-1, OPS-3, OPS-5, OPS-7, OPS-9, OPS-9b)
- 2.2 Màn `gamification-settings` (plan OPS-8, ui-map ops-fe), verify bằng `/ui-gate review`
- 2.3 PR ops-fe merge `staging` (plan OPS-10)

Dữ liệu test: theo mục "Dữ liệu để chạy / demo" của proposal Bolt.

Phụ thuộc repo khác: phần lớn code ops-fe đã có ở working tree theo `progress.md` của lần trước; bỏ mock cần lms-be lên staging (nhóm 1 của change Bolt, MR lms-be merge và migration chạy).
