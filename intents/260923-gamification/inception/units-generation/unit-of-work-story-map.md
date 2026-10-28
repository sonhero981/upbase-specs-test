---
intent: 260923-gamification
artifact: unit-of-work-story-map
stage: 2.7 units-generation
version: 2.0
status: approved
approved_at: 2026-10-13 (FE lead + [GIẢ LẬP] BE lead, DEC-T20)
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
scope: cả intent, 19 US (DEC-T15)
consumes: inception/domain-design/components.md v2.0, decisions.md v2.0 (DEC-T19)
supersedes: v1.0 (U0 cho US14, US15, DEC-T7)
---

# Unit of Work Story Map: Gamification, cả intent

Khoá theo US (intent v1, không có `stories.md`). Mỗi US đúng một Unit; mỗi Unit có ít nhất một US.

## Story map

| US | Unit | Directory | Ghi chú |
|---|---|---|---|
| US1 | U5 | `u5-learner-home` |  |
| US2 | U6 | `u6-achievement-realtime` |  |
| US3 | U7 | `u7-achievement-history` |  |
| US4 | U9 | `u9-badge-gallery` |  |
| US5 | U2 | `u2-daily-checkin` |  |
| US6 | U11 | `u11-leaderboard` | Gồm cron tính sẵn và con trỏ version |
| US7 | U12 | `u12-my-position` |  |
| US8 | U3 | `u3-points-config` | BR-10.7 nghiệm thu ở Unit của US10 (cùng mục) |
| US9 | U8 | `u8-badges-config` | Gồm trao bù BR-9.9 |
| US10 | U10 | `u10-levels-config` |  |
| US11 | U13 | `u13-leaderboard-config` |  |
| US12 | U14 | `u14-ops-learner-list` |  |
| US13 | U1 | `u1-recording-engine` | US không có UI; kiểm qua ledger, màn nhật ký thuộc Unit của US22 |
| US14 | U0 | `u0-foundation` | BR-14.13 phần số campaign nghiệm thu ở Unit của US20 (xem `unit-of-work.md` mục AC nghiệm thu ở Unit khác) |
| US15 | U0 | `u0-foundation` | Quyền thứ ba nghiệm thu ở Unit của US22 (cùng mục) |
| US19 | U16 | `u16-campaign-board` | BR-19.6 nghiệm thu ở Unit của US21 (cùng mục) |
| US20 | U15 | `u15-campaign-admin` |  |
| US21 | U17 | `u17-campaign-results` | Gồm chốt người tham gia và đóng băng |
| US22 | U4 | `u4-ops-achievement-log` |  |

## Cross-cutting
| Mối quan tâm | Unit chủ | Unit dùng |
|---|---|---|
| Ẩn hiện theo công tắc phía học viên (BR-1.8) | U5 (cờ hiển thị) | U6, U7, U9, U11, U12, U16 |
| Quyền Ops (BR-15.*) | U0 (tên quyền + tags) | U3, U4, U8, U10, U13, U14, U15, U17 |
| Test Account, Block (C10, BR-6.8) | U1 (ghi nhận), U11 (bảng) | U4, U14, U16, U17 |
| Múi giờ tổ chức (C6, C9) | U0 (TenantProfile) | U2, U11, U15, U17 |

## Implementation order within each Unit
Mỗi Unit: lms-be (migration nếu có → service → endpoint/consumer/cron) → FE (API client → màn) → test tay đầu-cuối. Chi tiết ở 3.5 plan của Bolt.

## Coverage verification
19/19 US có Unit; 18/18 Unit có ít nhất một US. Ngoài phạm vi: ba US PRD ghi "chưa làm" (16, 17, 18).
