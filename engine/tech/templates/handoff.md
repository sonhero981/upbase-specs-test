---
bolt: <tên change Bolt>
intent: <slug>
store_commit: <hash ngắn của store lúc ghi>
store_dirty: <true | false>
written_at: <YYYY-MM-DD HH:mm>
---
# Bàn giao · <Bnn> <tên Bolt>

File này do `/bolt` ghi và cập nhật. Mỗi phiên Claude mở trong repo `flow: comet` đọc mục của repo mình trước khi `/comet-open`, để ba repo dùng chung một bản quyết định thay vì dán lại từ terminal. Người chỉ sửa tay mục "Quyết định chung".

`store_dirty: true` nghĩa là cây làm việc của store có sửa chưa commit ở intent hoặc change Bolt, nên `store_commit` chưa phản ánh hết tài liệu đã đọc. Khi đó ghi rõ tệp nào chưa commit ở mục "Quyết định chung".

## Chung cho cả Bolt

| | |
|---|---|
| Intent | `intents/<slug>/` |
| PRD / contract | version <x.y> / <x.y> |
| Jira | <ticket Bolt> |
| Phụ thuộc | <Bolt khác phải xong trước, hoặc "không có"> |
| Thứ tự repo | <repo 1> → <repo 2> → … |

## Quyết định chung

Điều mọi repo phải theo, mỗi dòng kèm ngày và người chốt. Chưa có thì ghi "Chưa có".

- <…>

## Tiến độ theo repo

| Repo | flow | Change ở repo | Branch | Owner | Trạng thái | Cập nhật |
|---|---|---|---|---|---|---|
| <id> | comet | <tên change Bolt> | <branch> | <tên> | Chưa bàn giao · Đã bàn giao · Đã archive · PR đã merge | <YYYY-MM-DD> |
| <id> | opsx, `change_style: feature` | <change do người tạo, hoặc "chưa có"> | <branch> | <tên> | Chưa có change · Đang làm · Đã xong | <YYYY-MM-DD> |

Cột "Change ở repo": repo `comet` và repo `opsx` kiểu `bolt` dùng đúng tên change Bolt; repo `opsx` kiểu `feature` ghi change theo feature mà người chọn (`/bolt` không tự đặt tên).

## Repo <id> (flow: comet)

Tên change ở repo: `<tên change Bolt>`. Đặt đúng tên này khi chạy `/comet-open`.

Đọc trước khi code, đường dẫn tính từ gốc store:

- `intents/<slug>/construction/<unit>/code-generation/code-generation-plan.md` mục `## <repo>`: plan file của repo này
- `intents/<slug>/inception/contract-design/contract-summary.md`: contract cần dùng
- `intents/<slug>/construction/<unit>/ui-map/ui-map.md` (repo FE): UI map cho `/ui-gate`
- `intents/<slug>/inception/test-cases/test-cases.md` TC-<a>..TC-<b>
- `openspec/changes/<tên>/specs/`: Scenario của Bolt, nguồn của `specs/` ở repo

Nhóm task thô của repo, từ `tasks.md` của change Bolt:

- <nhóm 1>

Dữ liệu test: <…>

Phụ thuộc repo khác: <PR hoặc version phải có trước, hoặc "không có">
