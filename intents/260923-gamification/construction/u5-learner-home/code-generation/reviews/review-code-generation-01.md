---
intent: 260923-gamification
unit: u5-learner-home
artifact: review-code-generation-plan
stage: 3.5 code-generation-plan
bolt: B04
version: review-01
reviewer: FE lead Nguyễn Hùng Sơn
date: 2026-10-15
verdict: READY
---
# Review 3.5 Code-Generation Plan: B04 `u5-learner-home`

## Verdict: READY

Không có Chặn. Plan đủ để Sơn bắt đầu code lms-fe.

## Checklist

| Hạng mục | Kết quả |
|---|---|
| Phủ WF-1…WF-5 | Đạt — D1 (tổng), D2 (WF-2), D3 (WF-3), D4 (WF-4), E1-E2 (WF-5) |
| BR1.11 GET /me một lần | Đạt — C1 context singleton |
| BR1.12 lazy rules | Đạt — C2 fetchedRef cache |
| BR-1.8 ẩn theo features.* | Đạt — D2 + E1 |
| 22 TC phủ F1 | Đạt |
| Leaderboard scope chưa chốt | Ghi nhận — D1 placeholder, chờ OQ-B04-1 |
| Tách BE (Nhóm A) rõ | Đạt |

## Findings

### F-01 — Ghi nhận
`level_criteria` trong GamificationRulesDto là `{ label: string }[]` — plan giả định BE trả chuỗi "Every …" đã format sẵn. Nếu BE trả `{ threshold, type }` dạng raw thì FE cần tự ghép. Cần cuongdq xác nhận schema C-14 trước khi code D4.

## Gate

**[x] FE lead approve** — Nguyễn Hùng Sơn (2026-10-15): plan v1.0 đủ để bắt đầu code. B04 3.5 PASS. **B10 mở khoá** (B04 + B09 đều pass 3.5).
