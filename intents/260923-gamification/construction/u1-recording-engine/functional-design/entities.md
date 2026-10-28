---
intent: 260923-gamification
unit: u1-recording-engine
artifact: entities
stage: 3.1 functional-design
bolt: B02
version: 1.1
status: draft
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
consumes: unit-of-work.md v2.0 (U1), components.md v2.0, contract-summary.md v2.0 (A-01, S-02, S-03), PRD v0.14 US13 + Solution › TDD, functional-design-questions.md Q1–Q5
---
# Entities: U1 `u1-recording-engine`

Technology-agnostic. Bảng, cột, migration cụ thể ở `../code-generation/code-generation-plan.md` (3.5). Bằng chứng "có sẵn" theo lms-be `origin/feature/gamification` @9006b80 (nhánh dựng của intent, ADR-008).

```yaml
entities:
  - name: CompletionFact
    kind: value-object
    status: existing (WP1), thêm trường tuỳ chọn
    description: "Dữ kiện một lần hoàn thành do điểm gắn luồng học phát ra, cũng là message A-01 và payload của lần chạy lại."
    source: "libs/interface/src/lib/gamification/engine/gamification-record.dto.ts:18-61"
    attributes:
      - {name: action, type: enum, required: true, allowed: [ACTIVITY_COMPLETED, COURSE_COMPLETED, TEST_PASSED, CHECKIN], note: "CHECKIN do U2 phát; U1 chỉ phát ba loại còn lại"}
      - {name: learner, type: reference, required: true, references: User}
      - {name: tenant, type: reference, required: true, note: "gắn khi phát"}
      - {name: occurredAt, type: timestamp, required: true, note: "thời điểm gốc của lần hoàn thành (BR13.8, C11); không đổi khi chạy lại"}
      - {name: enrollment, type: reference, required: "true trừ CHECKIN", references: ClassUser}
      - {name: objectType, type: enum, required: "true trừ CHECKIN", allowed: [COURSE_SECTION, QUIZ, COURSE]}
      - {name: object, type: reference, required: "true trừ CHECKIN", note: "Learning Activity, bài Test hoặc khoá"}
      - {name: objectName, type: text, required: false, note: "MỚI (A-01 additive): tên nội dung lúc hoàn thành (BR13.23)"}
      - {name: courseName, type: text, required: false, note: "MỚI (A-01 additive)"}
    constraints:
      - "ACTIVITY_COMPLETED ⇒ objectType COURSE_SECTION; TEST_PASSED ⇒ QUIZ; COURSE_COMPLETED ⇒ COURSE"
      - "Thiếu trường bắt buộc hoặc sai loại ⇒ dữ kiện hỏng (BR13.25)"

  - name: AchievementHistory
    kind: entity
    status: existing (WP0), sửa
    description: "Sổ giao dịch: mỗi dòng là một lần ghi nhận điểm (POINT), một huy hiệu (BADGE) hoặc một hạng (LEVEL). Chỉ thêm, không sửa, không xoá."
    source: "libs/database/src/lib/entities/gamification/gamification-achievement-history.entity.ts:5-41"
    attributes:
      - {name: tenant, type: reference, required: true}
      - {name: learner, type: reference, required: true, references: User}
      - {name: entryType, type: enum, required: true, allowed: [POINT, BADGE, LEVEL]}
      - {name: pointSource, type: enum, required: "POINT", allowed: [ACTIVITY_COMPLETED, COURSE_COMPLETED, TEST_PASSED, CHECKIN]}
      - {name: enrollment, type: reference, required: "POINT trừ CHECKIN", references: ClassUser}
      - {name: objectType, type: enum, required: "POINT trừ CHECKIN"}
      - {name: object, type: reference, required: "POINT trừ CHECKIN"}
      - {name: objectNameSnapshot, type: text, required: false, note: "MỚI: tên nội dung tại lúc ghi (BR13.23, BR-3.11)"}
      - {name: points, type: integer, required: true, default: 0, min: 0, note: "0 khi Points hoặc hành động tắt (BR13.13)"}
      - {name: badge, type: reference, required: "BADGE"}
      - {name: level, type: integer, required: "LEVEL"}
      - {name: occurredAt, type: timestamp, required: true, note: "= CompletionFact.occurredAt"}
    constraints:
      - "Duy nhất (enrollment, pointSource, object) với dòng POINT có enrollment — chống cộng trùng C5 (BR13.1, BR13.5). Có sẵn: migration 1789997000000:276"
      - "Duy nhất (learner, badge) với dòng BADGE; (learner, level) với dòng LEVEL. Có sẵn: :279, :282"
      - "Không sửa, không xoá (BR-3.5)"

  - name: UserStats
    kind: entity
    status: existing (WP0), dùng nguyên
    description: "Thành tích hiện tại của một học viên, cập nhật cùng lúc với dòng sổ giao dịch, khoá dòng trong lần ghi."
    source: "libs/database/src/lib/entities/gamification/gamification-user-stats.entity.ts:5-63"
    attributes:
      - {name: learner, type: reference, required: true, unique: true, references: User}
      - {name: totalPoints, type: integer, default: 0}
      - {name: pointsBySource, type: map, default: "{}"}
      - {name: totalActivitiesCompleted, type: integer, default: 0}
      - {name: totalTestsPassed, type: integer, default: 0}
      - {name: totalCoursesCompleted, type: integer, default: 0, note: "đếm lượt hoàn thành, không đếm chứng chỉ (BR13.12)"}
      - {name: totalBadgesAcquired, type: integer, default: 0, note: "chỉ tăng (ADR-011)"}
      - {name: level, type: integer, default: 1}
      - {name: lastPointsAt, type: timestamp}
      - {name: lastActivityAt, type: timestamp}
      - {name: lastCourseAt, type: timestamp}
      - {name: lastBadgeAt, type: timestamp}
    constraints:
      - "Một dòng mỗi học viên; tạo khi ghi lần đầu"
      - "Mọi thay đổi đi cùng dòng sổ giao dịch trong một lần ghi không tách rời (BR13.5)"

  - name: FailedEvent
    kind: entity
    status: existing (WP0), sửa
    description: "Một lần ghi nhận lỗi (phát lỗi hoặc engine lỗi) chờ chạy lại."
    source: "libs/database/src/lib/entities/gamification/gamification-failed-event.entity.ts:5-20"
    attributes:
      - {name: tenant, type: reference, required: true}
      - {name: kind, type: enum, required: true, default: RECORD, allowed: [RECORD, CHECKIN, BADGE_BACKFILL, BADGE_BACKFILL_JOB], note: "MỚI (S-03). U1 tạo RECORD; ba loại còn lại do U2, U8 ghi"}
      - {name: payload, type: document, required: true, note: "dữ kiện gốc, giữ occurredAt gốc"}
      - {name: occurredAt, type: timestamp, required: false, note: "MỚI (additive, bổ sung vào S-02): chép từ payload để U17 lọc được 'còn lỗi chờ trước biên campaign' (ADR-013)"}
      - {name: errorMessage, type: text, required: false}
      - {name: status, type: enum, required: true, default: PENDING, allowed: [PENDING, RESOLVED, GAVE_UP]}
      - {name: retryCount, type: integer, required: true, default: 0, min: 0, max: 5}
    constraints:
      - "Chỉ RECORD và CHECKIN tính cho điều kiện đóng băng campaign (S-02)"

  - name: GamificationSetting
    kind: entity
    status: existing (U0), chỉ đọc
    description: "Cấu hình chung của tổ chức; U1 đọc công tắc và mốc bật."
    source: "libs/database/src/lib/entities/gamification/gamification-setting.entity.ts:12 is_enabled, :18 points_enabled, :54 last_enabled_at"
    attributes:
      - {name: isEnabled, type: boolean}
      - {name: lastEnabledAt, type: timestamp, note: "cửa thời điểm (BR13.18)"}
      - {name: pointsEnabled, type: boolean}
      - {name: badgesEnabled, type: boolean}
      - {name: levelsEnabled, type: boolean}

  - name: PointRule
    kind: entity
    status: existing (U0/U3), chỉ đọc
    description: "Điểm và công tắc của từng hành động."
    source: "libs/database/src/lib/entities/gamification/gamification-point-setting.entity.ts:12 source, :15 is_enabled, :18 points"
    attributes:
      - {name: action, type: enum}
      - {name: isEnabled, type: boolean}
      - {name: points, type: integer, min: 0}

  - name: User
    kind: entity
    status: existing, chỉ đọc (LearnerDirectory)
    source: "libs/database/src/lib/entities/user/user.entity.ts:189 is_operator"
    attributes:
      - {name: isTestAccount, type: boolean, note: "users.is_operator (C10)"}

  - name: ClassUser
    kind: entity
    status: existing, chỉ đọc (LearnerDirectory)
    description: "Lượt ghi danh; mọi tiến độ treo vào đây (C5)."
    source: "libs/database/src/lib/entities/class/class-user-instances.entity.ts:20 tenant_id, :30-31 status"
    attributes:
      - {name: status, type: enum, allowed: [READY_TO_LEARN, IN_PROGRESS, COMPLETED, CANCELED], note: "libs/constants/src/lib/class/class.constants.ts:80-85"}

  - name: LearningContent
    kind: entity
    status: existing, chỉ đọc
    description: "Section, bài làm, khoá mà điểm gắn đọc để phân loại."
    source: "libs/database/src/lib/entities/course/course-section.entity.ts:43 name, :74 course_section_type; libs/database/src/lib/entities/quiz/quiz.entity.ts:47 name, :94 is_graded, :117-118 required_percent_score; libs/database/src/lib/entities/quiz/quiz-attempts.entity.ts:131 score_percentage; libs/database/src/lib/entities/course/course.entity.ts:40 name"
    attributes:
      - {name: sectionType, type: enum, note: "ACTIVITY = Learning Activity (BR13.17); course.constants.ts:35-48"}
      - {name: quizType, type: enum, note: "quiz.constants.ts:33-43; năm loại là bài Test (BR13.14)"}
      - {name: isGraded, type: boolean, note: "Graded Assignment"}
      - {name: passPercent, type: number, required: false, note: "ngưỡng đạt phần trăm của bài Test (BR13.14)"}
      - {name: attemptPercent, type: number, note: "phần trăm điểm tổng của lượt làm, hệ thống đã quy đổi sẵn (BR13.14)"}
      - {name: name, type: text}

relationships:
  - {from: AchievementHistory, to: User, cardinality: "N:1"}
  - {from: AchievementHistory, to: ClassUser, cardinality: "N:0..1", note: "dòng POINT trừ CHECKIN"}
  - {from: UserStats, to: User, cardinality: "1:1"}
  - {from: ClassUser, to: User, cardinality: "N:1"}
  - {from: CompletionFact, to: AchievementHistory, cardinality: "1:0..1 dòng POINT (+ 0..n BADGE, LEVEL)"}
  - {from: FailedEvent, to: CompletionFact, cardinality: "1:1 (payload)"}
```

## Tóm tắt
- **Mới / sửa của U1**: `AchievementHistory.objectNameSnapshot`; `FailedEvent.kind`, `FailedEvent.occurredAt` (additive, cập nhật S-02 qua PR store); `CompletionFact.objectName`, `courseName` (tuỳ chọn, additive A-01). Không entity mới.
- **Dùng nguyên**: `UserStats` và ba ràng buộc duy nhất của sổ giao dịch (WP0, migration 1789997000000:276-282) đã đủ cho chống cộng trùng và song song.
- **Chỉ đọc**: cấu hình (U0, U3), `User`, `ClassUser`, `LearningContent`.
- Tiến độ học không phải entity của U1: điểm gắn chỉ đọc trạng thái trước/sau, không sửa (Nguyên tắc nền PRD).
