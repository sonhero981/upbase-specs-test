# Bolt B01 · Walking skeleton: khung cây nhóm

| | |
|---|---|
| Intent | `intents/261005-group/` |
| PRD / TD | PRD version 0.2 (commit 03b49a8) / TD version 1.0 (DEC-T2) · Bolt plan 1.0 (DEC-T3) |
| Owner · Lane | Dev A · A |
| Unit | U1 (`tech/hld.md` mục 6) |
| US / BR | US1 · BR-1.1–1.6 · US2 · BR-2.1–2.6 · US6 · BR-6.1–6.5 |
| Repo | lms-be, ops-fe (không chạm lms-fe, lms-package) |
| Phụ thuộc | — (Bolt đầu tiên; B02, B05 chờ mốc skeleton của Bolt này) |
| Ước lượng | 4 ngày công (BE 2, FE 2), vượt trần ~3 ngày/Unit (bolt-plan mục 6 #2) |

## Đọc trước (owner chưa đọc tài liệu nào)
Đường dẫn tính từ `intents/261005-group/`. **Lưu ý [TEST]:** bản diễn tập dùng `tech/technical-design.md` là MỘT FILE ĐƠN (template cũ); quy ước mới là thư mục `tech/technical-design/`. Mọi anchor dưới đây trỏ vào file đơn, anchor là tiêu đề `##`/`###`/`####` trong file.

1. `tech/bolt-plan.md` mục `### B01 · Walking skeleton: khung cây nhóm` — giả thuyết, mốc skeleton, DoD, demo; DoD chung ở đầu mục `## 3. Chi tiết từng Bolt`.
2. `tech/technical-design.md` `## 0. Quy ước chung` — envelope, phân trang, mã lỗi `630xxx`, quyền, tài khoản kiểm thử, đa tenant/RLS.
3. `tech/technical-design.md` `## 1. API contract`: kiểu `LearnerGroupItem`, `### API-1`, `### API-2`, `### API-3`, `### API-4`, `### API-5`, `### API-17`.
4. `tech/technical-design.md` `## 2. Data model` (bảng `learner_groups`, `learner_group_parent_histories`, `learner_group_user_instances`, `tenant.group_max_depth`) + bảng Migration dòng `M1`.
5. lms-be: `tech/technical-design.md` `## 3. LLD lms-be` các dòng Unit `chung` + `U1`.
6. ops-fe: `tech/technical-design.md` `## 5. LLD ops-fe` các dòng Unit `chung` + `U1`; `### 5.1 UI map ops-fe` (UI-1, UI-2, UI-8, UI-9) + `#### 5.1.1 group-list`, `#### 5.1.2 group-form`, `#### 5.1.3 group-detail` (phần U1).
7. `tech/technical-design.md` `## 7. Test kỹ thuật` + `## Assumptions & Open Questions` (#1, #2, #3, #9 liên quan Bolt này).
8. Hành vi: `specs/` của change này; test case: `qa/test-cases.md` (danh sách ở mục Test case).

## Why
Chứng minh khung cây nhóm dạng `path` materialized + RLS theo tenant, module mới `apps/ops/src/learner-groups` (lms-be) và feature `@ops/feature-learner-group` (ops-fe) lắp được vào hệ thống hiện có mà không đụng `/groups` cũ, và đếm thành viên cả nhánh đạt p95 < 500 ms (R-05). Mọi Bolt sau (B02–B11) dựng trên bảng và màn của Bolt này.

## What Changes
- **lms-be**
  - Hằng, mã lỗi, `LearnerGroupUserFilter` — TD `## 3` dòng `chung`; mã lỗi ở TD `## 0` bảng mã lỗi.
  - Entity + repository + migration M1 — TD `## 2` + Migration `M1`; `## 3` dòng `U1`.
  - DTO, `LearnerGroupTreeService`, controller `learner-groups` + `learner-group-settings` — TD `## 3` dòng `U1`.
  - API-1, API-2, API-3, API-4, API-5, API-17 — TD `## 1` các khối cùng mã. API-6 (archive/restore/delete) thuộc B10, không làm ở đây dù TD đặt route ở controller U1.
- **ops-fe**
  - `LearnerGroupAPI` (chỉ method của API-1..5, API-17), type, quyền `_GR`, `LearnerGroupSelect`, ẩn menu Recipients List — TD `## 5` dòng `chung`.
  - Feature `features/learner-group` + route + sidebar; màn `group-list`, `group-form`, `group-detail` (phần U1) — TD `## 5` dòng `U1`, `#### 5.1.1`–`#### 5.1.3`.
- Không có thay đổi **BREAKING**: endpoint và bảng đều mới; `GET /setting` cũ chỉ thêm field (TD `### API-17` dòng Tương thích ngược).

## Capabilities

### New Capabilities
- `learner-group-hierarchy`: tạo, sửa, di chuyển nhóm học viên nhiều cấp trong một tenant; luật mã, nguồn, số cấp tối đa (US1, US2).
- `learner-group-browsing`: xem danh sách nhóm dạng cây/bảng, đếm thành viên cả nhánh, tìm kiếm có đường dẫn, ẩn nhóm lưu trữ (US6).

### Modified Capabilities
- Không có (store chưa có spec nào).

## Impact
- lms-be: `libs/constants`, `libs/exceptions`, `libs/database` (entity, migration M1), `libs/interface`, `libs/modules/src/lib/learner-group`, `apps/ops/src/learner-groups`. Không sửa `apps/ops/src/groups/*`, `libs/modules/src/lib/group/*`.
- ops-fe: `apps/ops-fe/src/apis/learner-group`, `libs/core` (type, `permission.ts`), `libs/ui` (`LearnerGroupSelect`), `features/learner-group` (mới), sidebar, `features/notification` (ẩn menu).
- Bảo mật: `tags: []` → endpoint mở cho mọi staff tới khi BA điền `tags` (TD Assumptions #3); chặn release, không chặn code.

## Definition of Done
- DoD chung (bolt-plan `## 3`): curl đại diện API-1..5, API-17 pass local · M1 up/down pass · màn ops-fe pass `/ui-gate review` (chưa có Figma: chỉ state/interaction/reuse) · TC liệt kê pass · PR lms-be, ops-fe merge `staging` · typecheck một lần cuối.
- Riêng B01: quyền `gr_manage_learner_group`/`gr_view_learner_group` khai ở ops-fe `permission.ts` (BE `tags: []`) · đo API-1 p95 với 60 nhóm/400 người, ghi kết quả.
- Mốc skeleton (~ngày 1.5, merge sớm cho B05): M1 + entity + API-2 + API-1 `view=TABLE` chưa lọc → `/learner-groups` bảng tối giản + `GroupFormModal` tạo nhóm gốc trên staging; TC-1, TC-3.

## Test case
`qa/test-cases.md`: US1 TC-1..TC-7 · US2 TC-8..TC-12 · US6 TC-35..TC-40, TC-105, TC-106 (20 TC).

Giới hạn khi chạy ở B01 [TEST tự chọn] (bolt-plan gán TC theo US nên vài TC cần phần của Bolt sau):
- Nhóm `SYNC` (TC-7, TC-11, TC-35) chỉ sinh từ B03 → seed bằng SQL `source='SYNC'` trên local/staging.
- Thành viên (TC-8, TC-37) do B02 làm → seed `learner_group_user_instances` bằng SQL.
- TC-8 "mở nhật ký di chuyển": không có màn (TD Assumptions #14) → kiểm bảng `learner_group_parent_histories`.
- TC-12 cần giao lớp (B04) → hoãn sang B04, không tính vào DoD B01.
- TC-36 lọc "Người quản lý" cần dữ liệu quản lý (B05) → B01 chỉ kiểm tham số gửi đúng, kết quả rỗng hợp lệ.
- TC-39 ô chọn nhóm ở dashboard (B11), Theo dõi nhánh (B08) → B01 kiểm ô Nhóm cha + danh sách.
- TC-105 "API từ chối vai trò không có quyền" mâu thuẫn `tags: []` (TD Assumptions #3) → B01 chỉ kiểm phần menu ẩn theo quyền FE; phần API chờ BA điền `tags`.

## Demo
FE lead + PO xem trên staging: tạo nhóm gốc, nhóm con; đổi nhóm cha có hộp xác nhận ảnh hưởng; cây tải dần + tìm kiếm có đường dẫn; đổi số cấp tối đa.
