# Tasks

Task thô. Task chi tiết ở `openspec/changes/260923-gamification-b01-walking-skeleton-aws/tasks.md` của repo lms-be, ops-fe, lms-fe (schema run) = checklist section repo trong `intents/260923-gamification/construction/u0-walking-skeleton/code-generation/code-generation-plan.md`. Tick ở đây khi PR repo tương ứng đã merge.

## 1. lms-be

- [ ] 1.1 Migration `tenant.timezone` + `gamification_settings` + `presence_days` có RLS kèm bypass, entity, repository (plan BE-1…BE-4) — verify: migration up/down sạch local, TC-51
- [ ] 1.2 Constant, DTO, `GamificationSettingsService`, `LearnerPresenceService` + 12 unit test (plan BE-5…BE-8, BE-11) — verify: `nx test modules` đúng 12 test xanh
- [ ] 1.3 C-01 `GET`/`PATCH /gamification/settings` (Ops, chờ OQ-C1) và C-03 `POST /gamification/presence` (LMS) (plan BE-9, BE-10, BE-12) — verify: 3 curl PASS
- [ ] 1.4 PR lms-be merge `staging`, migration chạy trên staging (plan BE-13) — verify: TC-46

## 2. ops-fe

- [ ] 2.1 Types, constant, `GamificationAPI`, DI, feature module, menu, white-label map (plan OPS-1…OPS-6) — verify: `pnpm typecheck:ops-fe`, `pnpm gen` có / không có feature
- [ ] 2.2 Màn `gamification-settings` (plan OPS-7, ui-map ops-fe) — verify: `/ui-gate review` Provisional, TC-1, TC-2 (phần bật), TC-14
- [ ] 2.3 PR ops-fe merge `staging` (plan OPS-8)

## 3. lms-fe

- [ ] 3.1 Type, `GamificationAPI.recordPresence` silent, `PresenceSignal` mount ở `ClientLayout` lms-pro (plan LMS-1…LMS-4) — verify: DevTools 1 request 200 không toast, TC-48
- [ ] 3.2 PR lms-fe merge `staging` (plan LMS-5)

## 4. Demo

- [ ] 4.1 Kiểm tích hợp `U0-IC1…IC4` trên staging (plan mục "Kiểm tích hợp") — verify: biên bản demo FE lead + BE lead
- [ ] 4.2 TC-1, TC-2 (phần bật), TC-13, TC-14, TC-32 (curl), TC-40, TC-46, TC-48, TC-49, TC-51 pass — verify: biên bản 3.6 `construction/build-and-test/b01/`

## Workflow follow-up

- Cập nhật bảng Construction trong `tech-state.md` và Traceability của `bolt-plan.md`.
- Archive change khi PR mọi repo đã merge và demo theo DoD xong.
