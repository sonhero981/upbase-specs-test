# Tasks

Task thô. Task chi tiết ở `openspec/changes/260923-gamification-b01-foundation/tasks.md` của lms-be, ops-fe (schema run) = checklist section repo trong `intents/260923-gamification/construction/u0-foundation/code-generation/code-generation-plan.md`. Tick ở đây khi MR/PR repo tương ứng đã merge.

## 1. lms-be

- [ ] 1.1 Migration `visibility_first_enabled_at` (timestamp > 1791874289448) + entity (plan BE-1, BE-2) — verify: migration up/down sạch local
- [ ] 1.2 Mã `630001`, DTO PATCH một trường, sửa `GamificationGeneralSettingService` WP3, cache Redis + `invalidateSetting` trong `GamificationConfigService`, biến Redis cho event-processor (plan BE-3…BE-5, BE-5b, BE-5c, BE-8, BE-8b) — verify: `nx test ops` 9 test + `nx test modules` 4 test xanh
- [ ] 1.3 C-01 `GET`, C-02 `PATCH`, tên quyền + `tags` cho cả 10 endpoint WP3, ngoại lệ `backend.md` (plan BE-6, BE-7, BE-9) — verify: 4 curl local + 2 staging PASS
- [ ] 1.4 MR lms-be merge vào `feature/gamification`, lên `staging`, migration chạy (plan BE-10) — verify: TC-12

## 2. ops-fe

- [ ] 2.1 Phần còn lại sau code phiên trước: types (`running_campaign_count`, bỏ `updated_at`), xoá mock chết, `aria-label`, mã `630001`, `pnpm gen`, `/fe:review` 6 Nên sửa (plan OPS-1, OPS-3, OPS-5, OPS-7, OPS-9, OPS-9b) — verify: `pnpm typecheck:ops-fe` 0 lỗi mới, `pnpm gen` có / không có feature
- [ ] 2.2 Màn `gamification-settings` (plan OPS-8, ui-map ops-fe) — verify: `/ui-gate review` Provisional, TC-1…TC-11
- [ ] 2.3 PR ops-fe merge `staging` (plan OPS-10)

## 3. Demo

- [ ] 3.1 Kiểm tích hợp U0-IC1…IC4 trên staging — verify: TC-1…TC-21 (role V, E, N)
- [ ] 3.2 Biên bản 3.6 `construction/build-and-test/b01/`, contract C-01, C-02 chuyển Final

## Workflow follow-up

- Cập nhật bảng Construction trong `tech-state.md` và Trace của `bolt-plan.md`.
- Archive change khi MR/PR mọi repo đã merge và demo theo DoD xong.
