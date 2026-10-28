# Tasks

Task thô. Task chi tiết ở `openspec/changes/261005-group-b01-group-tree-skeleton/tasks.md` của repo lms-be và ops-fe (schema run). Tick ở đây khi PR repo tương ứng đã merge.

## 1. lms-be

- [ ] 1.1 Hằng, mã lỗi `630xxx`, `LearnerGroupUserFilter` (TD `## 3` dòng `chung`) — verify: build lms-be pass, mã lỗi khớp bảng TD `## 0`
- [ ] 1.2 Entity + repository + migration M1 + `tenant.group_max_depth` (TD `## 2`, Migration `M1`) — verify: M1 up/down pass local, RLS chặn chéo tenant (TC-40)
- [ ] 1.3 Mốc skeleton: API-2 + API-1 `view=TABLE` chưa lọc, deploy staging — verify: curl TD `### API-1`, `### API-2` pass; TC-1, TC-3 phần API
- [ ] 1.4 API-1 đủ (TREE, search, lọc, sắp, `member_count` cả nhánh) + API-3, API-4, API-5, API-17 — verify: curl từng khối TD `## 1`; API-1 p95 < 500 ms với 60 nhóm/400 người
- [ ] 1.5 PR lms-be merge `staging` (mốc skeleton có thể là PR riêng merge sớm cho B05)

## 2. ops-fe

- [ ] 2.1 Phần dùng chung: `LearnerGroupAPI` (method API-1..5, API-17), type, quyền `_GR`, `LearnerGroupSelect`, ẩn menu Recipients List (TD `## 5` dòng `chung`) — verify: typecheck ops-fe, TC-106
- [ ] 2.2 Mốc skeleton: feature `learner-group` + route `/learner-groups` + sidebar, bảng tối giản + `GroupFormModal` tạo nhóm gốc gọi API staging — verify: TC-1, TC-3
- [ ] 2.3 `group-list` đủ (Cây/Bảng, tải dần, tìm kiếm, lọc, kéo thả + `MoveGroupConfirmModal`, `MaxDepthSettingModal`) (TD `#### 5.1.1`) — verify: `/ui-gate review` state/interaction; TC-35..TC-39
- [ ] 2.4 `group-form` tạo + sửa + đổi cha, `group-detail` phần U1 (TD `#### 5.1.2`, `#### 5.1.3`) — verify: `/ui-gate review`; TC-1..TC-11
- [ ] 2.5 PR ops-fe merge `staging`

## 3. Demo

- [ ] 3.1 Demo theo DoD trên staging cho FE lead + PO (tạo gốc/con, đổi cha có xác nhận, cây tải dần + tìm kiếm, đổi số cấp) — verify: biên bản demo
- [ ] 3.2 TC-1..TC-11, TC-35..TC-40, TC-105 (phần FE), TC-106 pass; TC-12 chuyển B04 (proposal mục Test case) — verify: kết quả ghi ở verify report

## Workflow follow-up

- Cập nhật bảng Bolts trong `tech/state.md` và mục Traceability của `tech/bolt-plan.md`.
- Archive change khi PR mọi repo đã merge và demo theo DoD xong.
