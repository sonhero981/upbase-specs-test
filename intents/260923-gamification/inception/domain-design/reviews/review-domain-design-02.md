Kết luận: READY

Reviewer: aidlc-architecture-reviewer-agent · Stage 2.6 domain-design v1.1 · Vòng 2 · Đã tự kiểm lại từng sửa đổi tác giả tuyên bố, không tin tóm tắt.

**Tình trạng finding vòng 1**

| Mã | Mức trước | Giờ | Ghi chú đã kiểm |
|---|---|---|---|
| R-01 | Chặn | Đã sửa | `LeaderboardComputation` là chủ duy nhất `LeaderboardSnapshot`; `LeaderboardService` và `CampaignLeaderboard` cùng `depends_on` nó, `CampaignLeaderboard` ghi version 0 "qua LeaderboardComputation". Đồ thị không vòng (script riêng + `tech-tools.py` đều 0 lỗi). Rationale khớp yaml. |
| R-02 | Chặn | Đã sửa | `FailedEventStore` (chủ `FailedEvent`, `depends_on: []`); `FailedEventRetry` → Store + Engine; Engine → Store; `GamificationRecordPublisher` → Engine + Store. Không vòng. `isRetry` không ghi lỗi có thật ở code (`gamification-engine.handlers.spec.ts:605`, `handleFailure`). |
| R-03 | Chặn | Đã sửa | ADR-015 và `LmsGamificationFeature` nay đúng hiện trạng WIP (`useLeaderboardParams.ts:14`, `types/model.ts:90`, `RangeFilter` chỉ năm khung). |
| R-04 | Chặn | Đã sửa | Năm điểm hook được liệt kê; `:10395` mô tả đúng (`:10447` chỉ gán FINISHED cho section, không đổi `class_user`, không transaction); `createTopicAttempt :3269`, `createCaseStudyAttempt :3558`, `saveUserProgressAfterSubmit :1448` (gọi từ `:262`, `:790`) đúng dòng. |
| R-05 | Chặn | Đã sửa (còn R-15) | ADR-017 + `CampaignParticipant` + Q11 cho cơ chế khả thi, sai số 15 phút ghi rõ. |
| R-06 | Nên sửa | Đã sửa (còn R-17) | ADR-018 + Q12: con trỏ đổi qua `GamificationConfig` (xoá cache), giữ version liền trước một chu kỳ. |
| R-07 | Nên sửa | Đã sửa | ADR-009 nay ghi chỉ lệch PRD (`prd.md:211`), phương án thay thế đúng. |
| R-08 | Nên sửa | Còn một phần (R-16) | `CheckinService` và `LmsCheckinTrigger` đã đổi đúng; ADR-010 chưa cập nhật. |
| R-09 | Nên sửa | Đã sửa | `LmsGamificationVisibility`, `LmsAchievementRealtime` thành `modified`; ref file WT API ops-fe; `object_name_snapshot (mới)`; bỏ `FailedEvent.occurred_at` (đọc từ payload). Ref khung WP0 có file cụ thể. |
| R-10 | Nên sửa | Đã sửa | `LearnerDirectory` (reused, `user.entity.ts:86-88,189`, `class-user-instances.entity.ts:15,30` đúng) cùng `references`; `BadgeBackfill` → Config + Engine + LearnerDirectory; `CampaignLeaderboard` không còn ghi trực tiếp. |
| R-11 | Nên sửa | Đã sửa | BR-5.15 có cơ chế (`current_streak = 0` khi tắt, so `last_enabled_at`, bật lại giữa ngày không cộng); `awardBackfill`; BR-9.9 có mục tiêu ≤ 5 phút; bảng Points của campaign ẩn khi Points tắt có ở API học viên. |
| R-12 | Nên sửa | Đã sửa | ADR-004…007 có "Alternatives Rejected", ADR-012 có Context, tên mục thống nhất, ADR-003 sửa dẫn chứng (interceptor chỉ cho Kafka). |
| R-13 | Ghi nhận | Còn | Giữ, chuyển 2.8/3.1. |
| R-14 | Ghi nhận | Đã sửa | Hai dependency socket.io redis có trong `external_dependencies` của `AchievementNotifier` và trong ADR-008. |

**Finding mới**

| Mã | Mức (Chặn/Nên sửa/Ghi nhận) | Vị trí | Vấn đề | Hành động |
|---|---|---|---|---|
| R-15 | Nên sửa | `components.md` `CampaignLeaderboard.behaviour`, `LeaderboardComputation.behaviour`; `decisions.md` ADR-017, ADR-013 | Danh sách `CampaignParticipant` chỉ được chốt ở job 15 phút đầu tiên sau biên kết thúc, còn bảng tạm tính trong 24 giờ chờ do cron 8 giờ tính qua `computeRange`, vốn loại học viên Block/rời (BR-6.8). Người bị Block sau kết thúc sẽ biến khỏi bảng tạm tính rồi (có thể) có mặt lại khi đóng băng, hoặc ngược lại. | Ghi trong behaviour: bảng tạm tính của campaign đã kết thúc dùng `CampaignParticipant` (sau khi đã chốt) thay vì lọc theo `status` hiện tại. |
| R-16 | Nên sửa | `decisions.md` ADR-010 (Decision) so với `components.md` `CheckinService`, `LmsCheckinTrigger` | ADR-010 chưa cập nhật theo R-08: vẫn ghi "`SET NX` ... Kafka `process_gamification_checkin`", "nhớ ngày đã gửi trong phiên". Component nay publish `process_gamification_record` kiểu CHECKIN trước rồi mới `SET NX`, khoá client theo (user, ngày múi giờ tổ chức). Chưa rõ topic `process_gamification_checkin` (đã có trong code constants) còn dùng hay bỏ, và ai chèn `Checkin` (entity của `CheckinService`) khi message đi qua `process_gamification_record`. | Đồng bộ ADR-010 với component; nêu số phận topic checkin và nơi chèn `Checkin`. |
| R-17 | Ghi nhận | `components.md` `LeaderboardComputation.behaviour`, header "ADR-008 đến ADR-015" | `LeaderboardComputation` nói "xoá version cũ chừa version 0" còn ADR-018 nói giữ thêm version liền trước; đoạn mở đầu `components.md` vẫn ghi ADR tới 015 dù đã có 017, 018. | Đồng bộ câu chữ. |

**Công cụ**

| Công cụ | Kết quả | Diễn giải |
|---|---|---|
| `tech-tools.py check --stage=domain-design` | Đạt, lỗi 0 | Khớp kiểm riêng: 35 component, tên duy nhất, `depends_on`/`dependents` đối xứng, mọi entity một chủ (kể cả `User`, `ClassUser`, `CampaignParticipant`, `LeaderboardSnapshot`, `FailedEvent`), `references` đúng owner, không vòng; traceability 33 id đều trỏ component có thật. |

**Tóm tắt:** Năm Chặn vòng 1 đã được xử lý và kiểm lại bằng code; đồ thị nay thật sự không vòng nhờ `LeaderboardComputation` và `FailedEventStore`. Còn hai mục Nên sửa nhỏ (R-15, R-16) và ghi nhận, không chặn; nên sửa trước khi qua cổng.
