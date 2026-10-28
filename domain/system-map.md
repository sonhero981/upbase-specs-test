# System Map — UpLnD

Phần riêng của sản phẩm đang cài. Danh sách repo, đường dẫn, remote, owner, convention, gate và `build_order`
nằm ở [`workspace.yaml`](../workspace.yaml) — không chép lại ở đây. Vùng và quyền ghi dùng chung:
`engine/tech/knowledge/system-map.md`.

## Nối store

Hiện trạng kiểm ngày 26/10/2026 bằng `openspec doctor` chạy trong từng repo. Bước 3.5 Code Generation mở change
`--schema run` ở repo, nên repo chưa nối thì chưa code theo Bolt được.

| Repo | `openspec/` | schema `run` | `references: upbase-specs` | Chạy được 3.5 |
|---|---|---|---|---|
| lms-package | có | có | có | **Được** |
| lms-be | có (`be-feature`, `be-bugfix`) | chưa | chưa | Chưa |
| ops-fe | chưa có thư mục | — | — | Chưa |
| lms-fe | chưa có thư mục | — | — | Chưa |

Mẫu để dựng: `lms-package/openspec/config.yaml` (`schema: run` + khối `references:`). Dựng xong kiểm lại bằng
`openspec doctor` trong repo đó và cập nhật bảng này.

## Phụ thuộc giữa các repo

```
lms-package ──(npm @upbase-tech/*)──> lms-fe, ops-fe
lms-be ──(REST + socket)──> lms-fe, ops-fe
```

Thứ tự implement một change chạm nhiều repo: **lms-package → lms-be → ops-fe / lms-fe** (`build_order`).
FE mock theo contract tới khi BE lên staging; FE chỉ nâng `@upbase-tech/<pkg>` sau khi PR lms-package merge `main` và đã publish.

## Package `@upbase-tech/*`

| Package | Dùng ở |
|---|---|
| `auth-package` | lms-fe, ops-fe (Keycloak) |
| `upbase-common-package` | lms-fe (editor, type lịch) |
| `upbase-notification` | lms-fe (notification drawer) |
| `quiz-result-package` | lms-fe |
| `explanation-package` | lms-fe |

## Câu hỏi treo cho BE lead

| # | Câu hỏi | Nguồn | Trạng thái |
|---|---|---|---|
| BE-1 | `lms-be/openspec/conventions/backend.md` § 2 bắt `tags: []` (BA điền sau) → endpoint mới mở cho mọi staff tới khi điền. Feature cần quyền ngay thì làm sao? | Diễn tập 261005-group 2.8 | Mở |
| BE-2 | Rule 02 nói final contract ở `_API_CONTRACT_TEMPLATE.md` của lms-be. Luồng mới dùng `inception/contract-design/contract-summary.md` ở store (Draft → Agreed → Final). Có bỏ template của repo cho feature đi qua store không? | Diễn tập 261005-group 2.8 | Mở |

## Owner theo phạm vi

| Phạm vi | Owner |
|---|---|
| API contract (mục trong `design.md`), lms-be | BE lead — Đoàn Quang Cường |
| FE (lms-fe, ops-fe) | FE lead — Nguyễn Hùng Sơn |
| lms-package | FE lead — Nguyễn Hùng Sơn |
