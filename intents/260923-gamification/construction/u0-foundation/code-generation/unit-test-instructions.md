---
intent: 260923-gamification
unit: u0-foundation
bolt: B01
artifact: unit-test-instructions
stage: 3.5 code-generation (Part 1)
version: 1.0
status: approved
---
# Unit Test Instructions: U0 (Bolt B01)

Viết ở Part 1 theo thứ tự AWS; owner cập nhật nếu Part 2 lệch plan.

## lms-be
| Bước | Lệnh / việc | Kỳ vọng |
|---|---|---|
| 1 | Kiểm runner nhận spec: tạo tạm `apps/ops/src/gamification-setting/services/tmp.spec.ts` có một `it` rỗng, chạy `npx nx test ops --testPathPattern=gamification-setting` | "Tests: 1 passed"; xoá file tạm |
| 2 | `npx nx test ops --testPathPattern=gamification-general-setting` | 9 test xanh (plan BE-8) |
| 2b | `npx nx test modules --testPathPattern=gamification-config` | 4 test cache xanh (plan BE-8b) |
| 3 | Migration: chạy migration local, kiểm cột `visibility_first_enabled_at`; revert một bước rồi chạy lại (chỉ khi dev đồng ý) | up/down chạy được, ghi `progress.md` |
| 4 | Curl theo `x-curl` C-01, C-02 (`contract-summary.md` v2.0) + PATCH `{}` + PATCH `{is_visible:true}` khi tắt | 200, 200, 422 `422\|000405`, 400 `400\|630001` |
| 5 | Staging: `PUT /gamification/point-rules` bằng role V; mọi endpoint bằng role N | 403 `403\|000000` |
| 6 | Redis: sau GET có khoá `tenant:{id}:gamification:config:settings`; sau PATCH khoá bị xoá | TC-12, TC-13 |

## ops-fe
Không có test runner (`.claude/rules/07-testing-patterns.md`).
| Bước | Lệnh / việc | Kỳ vọng |
|---|---|---|
| 1 | `pnpm typecheck:ops-fe`, lọc theo file đổi | 0 lỗi mới |
| 2 | ESLint `features/gamification/src`, file lib đổi | sạch |
| 3 | `/ui-gate review` (Provisional) | không flag mới; R7 `aria-label` đã sửa |
| 4 | TC chạy tay ở 3.6: TC-1…TC-11, TC-16…TC-18 | theo `test-cases.md` v2.0 |
