---
intent: 260923-gamification
unit: u1-recording-engine
artifact: code-generation-plan
stage: 3.5
bolt: B02
version: 1.0
status: draft
author: vietlh (owner)
---

# Code Generation Plan: U1 `u1-recording-engine`

## Summary

- Builds: LearningFlowHooks (5 điểm gắn), GamificationEngine sửa nhỏ, AchievementNotifier no-op, FailedEventStore sửa, FailedEventRetry cron, migration 2 cột mới
- Touches: `libs/database/migrations/`, `libs/database/src/lib/entities/gamification/`, `libs/modules/src/lib/gamification/engine/`, `libs/modules/src/lib/class/`, `apps/mock-test-service/src/`, `apps/background-job-service/src/gamification/`, `libs/interface/src/lib/gamification/`
- Tests: ~25 unit tests (jest) theo các TC-101…TC-125; test-after trên brownfield codebase

---

## Nhóm 1 — Migration DB

### Bước 1 — Migration thêm cột `kind` và `occurred_at` vào `gamification_failed_events`

- [ ] **Mục tiêu**: FailedEvent phân loại theo kind (RECORD / CHECKIN / BADGE_BACKFILL / BADGE_BACKFILL_JOB) để FailedEventRetry định tuyến chạy lại (BR13.22); `occurred_at` dùng để CampaignLeaderboard lọc "còn lỗi chờ trước biên" (ADR-013, S-02 additive)
- [ ] **File thay đổi**: `libs/database/src/lib/migrations/<timestamp>-gamification-add-failed-event-kind-occurred-at.ts` (timestamp tiếp sau `1789997000000`; dùng timestamp thực tế lúc tạo, ví dụ `1789999000000`)
- [ ] **Hành động**: add (file mới)
- [ ] **Chi tiết**:
  - `ALTER TABLE gamification_failed_events ADD COLUMN IF NOT EXISTS kind VARCHAR(30) NOT NULL DEFAULT 'RECORD'`
  - `ALTER TABLE gamification_failed_events ADD COLUMN IF NOT EXISTS occurred_at TIMESTAMPTZ NULL`
  - Đặt comment: `kind = loại sự kiện lỗi; RECORD dùng cho sự kiện ghi nhận thông thường`
  - Rollback: `ALTER TABLE gamification_failed_events DROP COLUMN IF EXISTS kind, DROP COLUMN IF EXISTS occurred_at`
  - **Tham chiếu**: `entities.md` FailedEvent.kind, FailedEvent.occurredAt; ADR-013; contract-summary S-02

---

## Nhóm 2 — Entity sửa

### Bước 2 — Thêm `kind` và `occurred_at` vào `GamificationFailedEvent` entity

- [ ] **Mục tiêu**: Entity phản ánh đúng schema sau migration (BR13.22, BR13.8, ADR-013)
- [ ] **File thay đổi**: `libs/database/src/lib/entities/gamification/gamification-failed-event.entity.ts`
- [ ] **Hành động**: edit
- [ ] **Chi tiết**:
  - Thêm `@Column({ name: 'kind', type: 'varchar', length: 30, default: 'RECORD', comment: 'RECORD | CHECKIN | BADGE_BACKFILL | BADGE_BACKFILL_JOB' }) kind: string`
  - Thêm `@Column({ name: 'occurred_at', type: 'timestamptz', nullable: true, comment: 'Thời điểm gốc của sự kiện, chép từ payload' }) occurred_at: Date | null`
  - Thêm constant enum `GamificationFailedEventKind` vào `libs/constants/src/lib/gamification/gamification.constants.ts` (hoặc file constants riêng): `RECORD = 'RECORD'`, `CHECKIN = 'CHECKIN'`, `BADGE_BACKFILL = 'BADGE_BACKFILL'`, `BADGE_BACKFILL_JOB = 'BADGE_BACKFILL_JOB'`
  - **Tham chiếu**: `entities.md` FailedEvent; contract-summary S-02; ADR-013

### Bước 3 — Thêm `object_name_snapshot` vào `GamificationAchievementHistory` entity

- [ ] **Mục tiêu**: Lưu tên nội dung tại lúc ghi để hiển thị lịch sử không bị ảnh hưởng khi đổi tên (BR13.23, BR-3.11, A-01)
- [ ] **File thay đổi**: `libs/database/src/lib/entities/gamification/gamification-achievement-history.entity.ts`
- [ ] **Hành động**: edit
- [ ] **Chi tiết**:
  - Thêm `@Column({ name: 'object_name_snapshot', type: 'text', nullable: true, comment: 'Tên nội dung tại lúc ghi (BR13.23)' }) object_name_snapshot: string | null`
  - Trường này nullable để tương thích ngược với dòng cũ chưa có giá trị
  - **Ghi chú**: Cột `object_name_snapshot` cần migration thêm cột vào bảng `gamification_achievement_history`. Tạo migration riêng cùng bước này hoặc ghép vào migration Bước 1.
  - **Tham chiếu**: `entities.md` AchievementHistory.objectNameSnapshot; BR13.23

### Bước 4 — Thêm `object_name` và `course_name` vào `GamificationRecordPayloadDto`

- [ ] **Mục tiêu**: CompletionFact mang tên nội dung để engine lưu vào `object_name_snapshot` mà không cần tra DB (BR13.23, A-01 additive)
- [ ] **File thay đổi**: `libs/interface/src/lib/gamification/engine/gamification-record.dto.ts`
- [ ] **Hành động**: edit
- [ ] **Chi tiết**:
  - Thêm `@IsOptional() @IsString() object_name?: string` — tên nội dung lúc hoàn thành
  - Thêm `@IsOptional() @IsString() course_name?: string` — tên khoá học
  - Cả hai `@IsOptional()` vì là additive, không phá vỡ A-01 đã ký
  - **Tham chiếu**: `entities.md` CompletionFact.objectName, courseName; A-01; BR13.23

---

## Nhóm 3 — GamificationEngine sửa nhỏ

### Bước 5 — EligibilityHandler thêm kiểm cửa thời điểm `occurredAt >= lastEnabledAt`

- [ ] **Mục tiêu**: Chặn ghi nhận khi sự kiện xảy ra trước lần bật gần nhất (BR13.18, Q1)
- [ ] **File thay đổi**: `libs/modules/src/lib/gamification/engine/handlers/eligibility.handler.ts`
- [ ] **Hành động**: edit
- [ ] **Chi tiết**:
  - Sau khi kiểm `setting.is_enabled`, đọc `setting.last_enabled_at`
  - Nếu `last_enabled_at != null` và `ctx.occurredAt < last_enabled_at` → gọi `this.skip(ctx)` và return
  - Log: `GAMIFICATION_SKIPPED_BEFORE_ENABLED` kèm `{ occurredAt, lastEnabledAt }` khi chạy lại (isRetry) vượt qua vòng tắt/bật
  - Điều kiện: `last_enabled_at` null (dữ liệu cũ WP0 chưa có) thì không áp vế thời điểm
  - **Tham chiếu**: BR13.18; `rules.md`; `functional-spec.md` WF-3 bước 2; `entities.md` GamificationSetting.lastEnabledAt

### Bước 6 — PointHandler ghi `object_name_snapshot` khi insert dòng POINT

- [ ] **Mục tiêu**: Dòng sổ giao dịch giữ tên nội dung tại lúc ghi (BR13.23)
- [ ] **File thay đổi**: `libs/modules/src/lib/gamification/engine/handlers/point.handler.ts`
- [ ] **Hành động**: edit
- [ ] **Chi tiết**:
  - Trong method `insertPointRow`, thêm trường `object_name_snapshot: payload.object_name ?? null` vào `.values({...})`
  - `payload.object_name` lấy từ `GamificationRecordPayloadDto.object_name` (Bước 4)
  - Thiếu `object_name` trong payload → snapshot = null (không tra DB thêm tại đây; tra DB không đáng tin nếu nội dung đã đổi tên, logic tra thêm để hook quyết định)
  - **Tham chiếu**: BR13.23; `entities.md` AchievementHistory.objectNameSnapshot; A-01

### Bước 7 — Engine bổ sung gọi AchievementNotifier sau commit (BR13.24)

- [ ] **Mục tiêu**: Sau khi lưu bền, không phải chạy lại, engine báo thành tích qua cổng thông báo (BR13.24). U1 dùng adapter no-op; U6 thay bằng bản thật
- [ ] **File thay đổi**: `libs/modules/src/lib/gamification/engine/gamification-engine.service.ts`
- [ ] **Hành động**: edit
- [ ] **Chi tiết**:
  - Thêm dependency inject `AchievementNotifier` vào constructor (interface, sau Bước 8)
  - Sau `await queryRunner.commitTransaction()`, khi `!options.isRetry` và `ctx.outcome === RECORDED`:
    - Thu thập danh sách thành tích cần gửi: dòng POINT có điểm > 0, dòng BADGE, dòng LEVEL vừa ghi trong lần này (lấy từ ctx)
    - Lọc: chỉ khi `settings.is_visible === true`
    - Gọi `await this.achievementNotifier.notify(achievements)` — bọc try/catch, nuốt lỗi, log `GAMIFICATION_NOTIFY_FAILED`
  - Cần thêm list `badgesAwarded` và `levelsAwarded` vào `RecordContext` để engine thu thập kết quả từ `BadgeHandler`, `LevelHandler`
  - **Tham chiếu**: BR13.24; `rules.md`; `components.md` GamificationEngine; contract-summary S-03

---

## Nhóm 4 — AchievementNotifier interface + no-op adapter

### Bước 8 — Định nghĩa interface `AchievementNotifier` và no-op adapter

- [ ] **Mục tiêu**: Engine inject qua DI; U1 dùng no-op; U6 thay bằng adapter socket.io thật (BR13.24, S-03)
- [ ] **File thay đổi** (mới):
  - `libs/modules/src/lib/gamification/notifier/achievement-notifier.interface.ts`
  - `libs/modules/src/lib/gamification/notifier/noop-achievement-notifier.service.ts`
- [ ] **Hành động**: add
- [ ] **Chi tiết**:
  - Interface `AchievementNotifier`:
    ```typescript
    export interface AchievementNotifier {
      notify(achievements: AchievementNotification[]): Promise<void>
    }
    export const ACHIEVEMENT_NOTIFIER = Symbol('AchievementNotifier')
    ```
  - Type `AchievementNotification`:
    ```typescript
    export type AchievementNotification = {
      type: 'POINT' | 'BADGE' | 'LEVEL'
      points?: number
      badgeId?: string
      level?: number
      occurredAt: Date
    }
    ```
  - `NoopAchievementNotifierService implements AchievementNotifier`: method `notify()` return Promise.resolve() ngay lập tức
  - Đăng ký provider trong `GamificationEngineModule` (hoặc module tương đương):
    ```typescript
    { provide: ACHIEVEMENT_NOTIFIER, useClass: NoopAchievementNotifierService }
    ```
  - **Tham chiếu**: BR13.24; `components.md` AchievementNotifier; contract-summary S-03; `unit-of-work.md` U1 ghi chú

---

## Nhóm 5 — LearningFlowHooks trong lms-be (H1, H2)

### Bước 9 — H1: Hook `createCourseSectionProgress` — phát ACTIVITY_COMPLETED + COURSE_COMPLETED

- [ ] **Mục tiêu**: Sau commit tiến độ, phát CompletionFact khi section là Learning Activity và/hoặc lượt ghi danh chuyển COMPLETED (BR13.2, BR13.17, BR13.20, BR13.7)
- [ ] **File thay đổi**: `libs/modules/src/lib/class/class.service.ts`
- [ ] **Hành động**: edit (vùng sau dòng commit ~:10277, sau `queryRunner.commitTransaction()`)
- [ ] **Chi tiết**:
  - Đọc trạng thái lượt ghi danh TRƯỚC lần lưu: capture `previousClassUserStatus = class_user_instance.status` trước khi transaction bắt đầu (dòng ~:10079)
  - Inject `GamificationRecordPublisher` vào `ClassService` (hoặc service con tương ứng)
  - Sau `await queryRunner.commitTransaction()` và trước return:
    ```
    // Lọc sớm BR13.19: skip nếu gamification tắt hoặc is_operator, đọc lỗi thì đi tiếp
    // H1-a: ACTIVITY_COMPLETED
    if (section.course_section_type === LEARNING_ACTIVITY_TYPE) {
      await publisher.publish({ action: 'ACTIVITY_COMPLETED', ... object_name: section.name, ... })
    }
    // H1-b: COURSE_COMPLETED — chỉ khi chuyển trạng thái
    if (previousClassUserStatus !== COMPLETED && class_user_instance.status === COMPLETED) {
      await publisher.publish({ action: 'COURSE_COMPLETED', ... object_name: course.name, ... })
    }
    ```
  - Bọc toàn bộ hook trong try/catch, không throw ra ngoài (BR13.7)
  - `occurred_at` = thời điểm hiện tại (ISO 8601) — thời điểm section hoàn thành
  - `class_user_id`, `object_type = COURSE_SECTION`, `object_id = section_id`, `object_name = section.name`
  - Với COURSE_COMPLETED: `object_type = COURSE`, `object_id = course.id`, `object_name = course.name`
  - **Kiểm tra loại section**: `course_section_type` đọc từ entity CourseSection; hằng số `LEARNING_ACTIVITY_TYPE` từ `libs/constants` (kiểm `course.constants.ts:35-48`)
  - **Tham chiếu**: BR13.2, BR13.7, BR13.17, BR13.19, BR13.20; `functional-spec.md` H1; `components.md` LearningFlowHooks `:10079`

### Bước 10 — H2: Hook `updateUserCourseSectionProgress` — phát ACTIVITY_COMPLETED

- [ ] **Mục tiêu**: Đánh dấu FINISHED một section (không có transaction, không đổi class_user.status) phát ACTIVITY_COMPLETED nếu section là Learning Activity (BR13.2, BR13.17, BR13.20)
- [ ] **File thay đổi**: `libs/modules/src/lib/class/class.service.ts`
- [ ] **Hành động**: edit (vùng sau dòng ~:10446-10452, sau lần gọi save cuối của updateUserCourseSectionProgress)
- [ ] **Chi tiết**:
  - Đọc `previousProgressStatus` trước khi save (trước dòng save hiện tại)
  - Sau save:
    ```
    // Không có COURSE_COMPLETED (không đổi class_user)
    if (section.course_section_type === LEARNING_ACTIVITY_TYPE
        && previousProgressStatus !== FINISHED
        && param.status === FINISHED) {
      await publisher.publish({ action: 'ACTIVITY_COMPLETED', ... })
    }
    ```
  - Bọc try/catch, không throw (BR13.7)
  - `occurred_at` = thời điểm hiện tại
  - **Tham chiếu**: BR13.17, BR13.20; `functional-spec.md` H2; `components.md` LearningFlowHooks `:10395`

---

## Nhóm 6 — LearningFlowHooks trong mock-test-service (H3, H4, H5)

### Bước 11 — H3: Hook `submitQuizAttempt` — phát TEST_PASSED (+ ACTIVITY_COMPLETED, COURSE_COMPLETED)

- [ ] **Mục tiêu**: Sau nộp bài Test trong khoá, phát TEST_PASSED khi đủ điều kiện BR13.14; phát ACTIVITY_COMPLETED nếu Quiz trong Learning Activity; phát COURSE_COMPLETED nếu lượt ghi danh chuyển COMPLETED
- [ ] **File thay đổi**: `apps/mock-test-service/src/quiz/quiz.service.ts`
- [ ] **Hành động**: edit (sau commit ở dòng ~:293, bên trong hoặc ngay sau `handlePostSubmitEvents`/`saveUserProgressAfterSubmit`)
- [ ] **Chi tiết**:
  - Capture `previousClassUserStatus` TRƯỚC khi save tiến độ (BR13.20)
  - Inject `GamificationRecordPublisher` vào `QuizService` (qua module)
  - Logic TEST_PASSED theo BR13.14:
    - Bài phải là Test (kiểm quiz_type ∈ {MIDTERM, FINAL, TRIAL, TOPIC_CHECK, CHAPTER_CHECK} — kiểm `quiz.constants.ts:33-43`)
    - Bài phải gắn lượt ghi danh (`class_user_id` không null) (BR13.14 lượt không gắn thì không phát [Q3])
    - `Graded = No` (not is_graded): phát khi nộp xong
    - `Graded = Yes` (is_graded):
      - Nếu không tạo bản chấm (chỉ trắc nghiệm, `grade.service.ts:172-178`): xét điểm lượt ngay khi nộp; phát nếu `attempt.score_percentage >= quiz.required_percent_score` (hoặc `required_percent_score` null thì phát khi hoàn thành)
      - Nếu có bản chấm tay: KHÔNG phát tại đây → chờ H5
  - ACTIVITY_COMPLETED: nếu quiz nằm trong section loại Learning Activity (tra section của quiz để kiểm)
  - COURSE_COMPLETED: nếu `previousClassUserStatus !== COMPLETED && class_user_instance.status === COMPLETED`
  - Bọc toàn bộ trong try/catch, không throw (BR13.7)
  - `occurred_at` = thời điểm nộp bài
  - **Tham chiếu**: BR13.14, BR13.17, BR13.19, BR13.20; `functional-spec.md` H3; `components.md` LearningFlowHooks `:1540-1570`

### Bước 12 — H4: Hook `createTopicAttempt` / `createCaseStudyAttempt` — phát COURSE_COMPLETED

- [ ] **Mục tiêu**: Case Study không có TEST_PASSED và không có ACTIVITY_COMPLETED, nhưng có thể làm lượt ghi danh COMPLETED → phát COURSE_COMPLETED (BR13.14, BR13.17)
- [ ] **File thay đổi**: `apps/mock-test-service/src/quiz/quiz.service.ts`
- [ ] **Hành động**: edit (sau dòng ~:3048-3051 của createTopicAttempt và ~:3344 của createCaseStudyAttempt sau commit ~:3299 và ~:3588)
- [ ] **Chi tiết**:
  - Capture `previousClassUserStatus` trước lần giao dịch
  - Sau commit, nếu `previousClassUserStatus !== COMPLETED && classUser.status === COMPLETED`:
    ```
    await publisher.publish({ action: 'COURSE_COMPLETED', object_type: 'COURSE', object_id: courseId, object_name: courseName, ... })
    ```
  - Không phát TEST_PASSED, không phát ACTIVITY_COMPLETED (không có điểm Test cho Case Study; Case Study không phải Learning Activity)
  - `occurred_at` = thời điểm tạo
  - **Tham chiếu**: BR13.14, BR13.17; `functional-spec.md` H4; `components.md` LearningFlowHooks `:3018`, `:3344`

### Bước 13 — H5: Hook `finishGrading` — phát TEST_PASSED lần chấm đầu

- [ ] **Mục tiêu**: Sau kết thúc chấm tay, kiểm lịch sử chấm của lượt làm: chỉ phát TEST_PASSED khi đây là lần đầu bản chấm của lượt đi tới trạng thái kết thúc VÀ lượt đạt (BR13.15, BR13.14)
- [ ] **File thay đổi**: `libs/modules/src/lib/quiz-attempt-grading/quiz-attempt-grading.service.ts`
- [ ] **Hành động**: edit (sau commit ~:3117)
- [ ] **Chi tiết**:
  - Trước khi lưu kết quả chấm, đọc lịch sử chấm của lượt làm (`quizAttemptId`):
    ```
    const hasFinishedGradingBefore = await gradingRepo
      .count({ where: { quiz_attempt_id: quizAttemptId, status: FINISHED } }) > 0
    ```
    (Tham chiếu `quiz-attempt-grading.service.ts:3616-3673` logic tạo bản chấm mới; `:3061-3075` kết thúc từ IN_REVIEW; `:3538-3558` gửi duyệt)
  - Sau commit kết quả chấm, nếu `!hasFinishedGradingBefore`:
    - Bài Test Graded = Yes VÀ có lượt ghi danh VÀ `attempt.score_percentage >= quiz.required_percent_score`:
      ```
      await publisher.publish({ action: 'TEST_PASSED', ... occurred_at: now, ... })
      ```
  - Nếu `hasFinishedGradingBefore`: không phát dù điểm thay đổi (BR13.15)
  - `occurred_at` = thời điểm chấm xong (hiện tại)
  - **Tham chiếu**: BR13.14, BR13.15; `functional-spec.md` H5 / WF-2; `components.md` LearningFlowHooks `:2988`

---

## Nhóm 7 — FailedEventStore sửa

### Bước 14 — FailedEventStore: cập nhật `save()` để ghi `kind` và `occurred_at`

- [ ] **Mục tiêu**: Mọi nơi lưu FailedEvent phải ghi đúng `kind` và `occurred_at` từ payload (BR13.8, BR13.22, ADR-013)
- [ ] **File thay đổi**: `libs/modules/src/lib/gamification/engine/gamification-record.publisher.ts` và `libs/modules/src/lib/gamification/engine/gamification-engine.service.ts`
- [ ] **Hành động**: edit
- [ ] **Chi tiết**:
  - Trong `GamificationRecordPublisher.saveFailedEvent()`: thêm `kind: GamificationFailedEventKind.RECORD` và `occurred_at: payload.occurred_at ? new Date(payload.occurred_at) : null`
  - Trong `GamificationEngineService.handleFailure()`: thêm `kind: GamificationFailedEventKind.RECORD` và `occurred_at: ctx.payload.occurred_at ? new Date(ctx.payload.occurred_at) : null`
  - **Tham chiếu**: BR13.8; `entities.md` FailedEvent; ADR-013; S-02

### Bước 15 — FailedEventRetry: định nghĩa registry cho loại sự kiện lỗi khác

- [ ] **Mục tiêu**: FailedEventRetry có thể định tuyến theo `kind`; loại chưa có handler thì giữ PENDING mà không tăng retryCount (BR13.22)
- [ ] **File thay đổi** (mới): `libs/modules/src/lib/gamification/retry/failed-event-retry.types.ts`
- [ ] **Hành động**: add
- [ ] **Chi tiết**:
  - Interface `FailedEventHandler`:
    ```typescript
    export interface FailedEventHandler {
      kind: string
      handle(event: GamificationFailedEvent): Promise<GamificationRecordResult>
    }
    export const FAILED_EVENT_HANDLERS = Symbol('FailedEventHandlers')
    ```
  - U2 (CheckinService) sẽ đăng ký handler cho CHECKIN, U8 cho BADGE_BACKFILL và BADGE_BACKFILL_JOB
  - **Tham chiếu**: BR13.22; S-03 FailedEventStore retry routing

---

## Nhóm 8 — FailedEventRetry (cron)

### Bước 16 — Tạo `GamificationFailedEventRetryService` với cron 15 phút

- [ ] **Mục tiêu**: Cron chạy 15 phút mỗi tenant: lấy FailedEvent PENDING (cũ trước), định tuyến theo kind, cập nhật trạng thái (BR13.21, BR13.22)
- [ ] **File thay đổi** (mới): `apps/background-job-service/src/gamification/gamification-failed-event-retry.service.ts`
- [ ] **Hành động**: add
- [ ] **Chi tiết**:
  - Class `GamificationFailedEventRetryService`:
  - `@Cron('0 */15 * * * *')` — mỗi 15 phút; dùng `timeZone: 'UTC'`
  - Method `retryFailedEvents()`:
    1. Lấy tất cả `tenant_id` có FailedEvent PENDING
    2. Với mỗi tenant: lấy danh sách PENDING sắp theo `created_at ASC` (cũ trước — BR13.21)
    3. Với mỗi event: dựa theo `event.kind`:
       - `RECORD` (hoặc null / chuỗi lạ → coi là RECORD, BR13.22): gọi `engine.record(payload, { isRetry: true })`
       - Loại khác (CHECKIN, BADGE_BACKFILL, BADGE_BACKFILL_JOB): kiểm registry `FAILED_EVENT_HANDLERS`; nếu không có handler → log và bỏ qua (không tăng retryCount, BR13.22)
    4. Kết quả:
       - `RECORDED`, `DUPLICATE`, `SKIPPED` → cập nhật status = `RESOLVED`
       - `FAILED` hoặc exception: `retry_count += 1`; nếu `retry_count >= 5` → `status = GAVE_UP`, log `GAMIFICATION_RECORD_GAVE_UP` kèm `{ eventId, tenantId }`
  - Inject: `GamificationFailedEventRepository`, `GamificationEngineService`, `FAILED_EVENT_HANDLERS` (multi-provider)
  - **Tham chiếu**: BR13.21, BR13.22; `functional-spec.md` WF-4; `components.md` FailedEventRetry

### Bước 17 — Đăng ký `GamificationFailedEventRetryService` vào `GamificationJobModule`

- [ ] **Mục tiêu**: Cron active trong background-job-service
- [ ] **File thay đổi**: `apps/background-job-service/src/gamification/gamification-job.module.ts`
- [ ] **Hành động**: edit (module hiện đang rỗng)
- [ ] **Chi tiết**:
  - Import các module cần thiết: `GamificationEngineModule` (hoặc re-export), `TypeOrmModule.forFeature([GamificationFailedEvent])`
  - Khai báo providers: `GamificationFailedEventRetryService`
  - **Tham chiếu**: BR13.21; `components.md` FailedEventRetry `apps/background-job-service:19`

---

## Nhóm 9 — GamificationRecordPublisher — kiểm timeout

### Bước 18 — GamificationRecordPublisher: kiểm và đảm bảo timeout ≤ 100ms

- [ ] **Mục tiêu**: Việc phát có hạn chờ ≤ 100 ms để toàn bộ hook không vượt 200 ms p95 (BR13.7)
- [ ] **File thay đổi**: `libs/modules/src/lib/gamification/engine/gamification-record.publisher.ts`
- [ ] **Hành động**: edit (nếu timeout chưa có)
- [ ] **Chi tiết**:
  - Kiểm trong `kafkaService.sendTopic()` đã có timeout config chưa (kiểm file KafkaService)
  - Nếu chưa: bọc `kafkaService.sendTopic()` với `Promise.race([sendPromise, timeoutPromise(100)])` — quá 100ms coi như lỗi, gọi `saveFailedEvent`
  - Nếu đã có timeout ở KafkaService cấp config: ghi comment xác nhận `// Timeout ≤ 100ms cấu hình tại KafkaService — BR13.7` và không thay đổi code
  - **Tham chiếu**: BR13.7; `rules.md`; `components.md` GamificationRecordPublisher

---

## Nhóm 10 — Unit Tests

### Bước 19 — Test: EligibilityHandler — cửa thời điểm (BR13.18)

- [ ] **Mục tiêu**: Bao phủ BR13.18; TC-118 (hoàn thành lúc tắt / xử lý sau khi bật → SKIPPED)
- [ ] **File thay đổi** (sửa file test có sẵn): `libs/modules/src/lib/gamification/engine/gamification-engine.handlers.spec.ts`
- [ ] **Hành động**: edit
- [ ] **Chi tiết**:
  - Thêm describe block `EligibilityHandler - cửa thời điểm`:
    - `it('SKIPPED khi occurredAt < lastEnabledAt')` — TC-118
    - `it('RECORDED khi lastEnabledAt null (dữ liệu cũ)')` — BR13.18 điều kiện null
    - `it('RECORDED khi occurredAt >= lastEnabledAt')` — happy path
  - **Tham chiếu**: BR13.18; TC-118; `rules.md`

### Bước 20 — Test: GamificationEngine — object_name_snapshot và dòng 0 điểm

- [ ] **Mục tiêu**: Bao phủ BR13.23 (giữ tên nội dung), BR13.13 (dòng 0 điểm khi Points tắt); TC-116, TC-117
- [ ] **File thay đổi**: `libs/modules/src/lib/gamification/engine/gamification-engine.handlers.spec.ts`
- [ ] **Hành động**: edit
- [ ] **Chi tiết**:
  - `it('ghi object_name_snapshot từ payload.object_name')` — BR13.23
  - `it('object_name_snapshot null khi payload thiếu object_name')` — BR13.23 edge case
  - `it('ghi dòng 0 điểm khi points_enabled=false, chỉ số vẫn tăng')` — TC-116
  - `it('ghi dòng 0 điểm khi hành động tắt, badges xét bình thường')` — TC-117
  - **Tham chiếu**: BR13.13, BR13.23; TC-116, TC-117

### Bước 21 — Test: LearningFlowHooks — H1 và H2

- [ ] **Mục tiêu**: Bao phủ BR13.2, BR13.17, BR13.20; TC-101 (hoàn thành học), TC-103 (đã xong trước bật)
- [ ] **File thay đổi** (mới): `libs/modules/src/lib/class/class.service.gamification-hooks.spec.ts`
- [ ] **Hành động**: add
- [ ] **Chi tiết**:
  - Mock `GamificationRecordPublisher`
  - `it('H1: phát ACTIVITY_COMPLETED khi section là Learning Activity')` — TC-101
  - `it('H1: phát COURSE_COMPLETED khi lượt ghi danh chuyển COMPLETED')` — TC-101
  - `it('H1: không phát COURSE_COMPLETED nếu lượt đã COMPLETED từ trước')` — TC-103, BR13.20
  - `it('H1: không phát nếu section không phải Learning Activity')` — BR13.17
  - `it('H2: phát ACTIVITY_COMPLETED khi section là Learning Activity và status đổi sang FINISHED')` — BR13.17
  - `it('H2: không phát COURSE_COMPLETED')` — BR13.17
  - `it('H1/H2: lỗi publisher không throw ra caller')` — BR13.7
  - **Tham chiếu**: BR13.2, BR13.7, BR13.17, BR13.20; TC-101, TC-103

### Bước 22 — Test: LearningFlowHooks — H3 (nộp bài Test)

- [ ] **Mục tiêu**: Bao phủ BR13.14 (Graded Yes/No, ngưỡng điểm); TC-119, TC-120, TC-121
- [ ] **File thay đổi** (mới): `apps/mock-test-service/src/quiz/quiz.service.gamification-hooks.spec.ts`
- [ ] **Hành động**: add
- [ ] **Chi tiết**:
  - Mock `GamificationRecordPublisher`
  - `it('H3: Graded=No phát TEST_PASSED khi nộp')` — TC-120
  - `it('H3: Graded=Yes điểm đạt phát TEST_PASSED (tự chấm)')` — TC-119
  - `it('H3: Graded=Yes điểm không đạt không phát')` — TC-119
  - `it('H3: Graded=Yes bài chấm tay có bản chấm KHÔNG phát tại đây → chờ H5')` — BR13.14
  - `it('H3: Quiz trong hoạt động phát ACTIVITY_COMPLETED')` — TC-121, BR13.17
  - `it('H3: Case Study không phát TEST_PASSED, không phát ACTIVITY_COMPLETED')` — TC-121
  - `it('H3: lượt ghi danh chuyển COMPLETED phát COURSE_COMPLETED')` — BR13.20
  - **Tham chiếu**: BR13.14, BR13.17, BR13.20; TC-119, TC-120, TC-121

### Bước 23 — Test: LearningFlowHooks — H5 (chấm tay)

- [ ] **Mục tiêu**: Bao phủ BR13.15 (chấm lại không phát); TC-122, TC-123
- [ ] **File thay đổi** (mới): `libs/modules/src/lib/quiz-attempt-grading/quiz-attempt-grading.service.gamification-hooks.spec.ts`
- [ ] **Hành động**: add
- [ ] **Chi tiết**:
  - `it('H5: lần chấm đầu đạt phát TEST_PASSED')` — BR13.15
  - `it('H5: lần chấm đầu trượt không phát')` — BR13.15
  - `it('H5: chấm lại (đã có bản chấm kết thúc) không phát dù đổi điểm')` — TC-122, TC-123
  - `it('H5: bản chấm bị trả từ duyệt trước khi kết thúc → lần kết thúc sau là lần đầu → phát')` — TC-122 edge case, BR13.15
  - **Tham chiếu**: BR13.15; TC-122, TC-123

### Bước 24 — Test: FailedEventRetry — cron và định tuyến

- [ ] **Mục tiêu**: Bao phủ BR13.21, BR13.22; TC-109 (chạy lại mang giờ gốc), TC-110 (GAVE_UP sau 5 lần)
- [ ] **File thay đổi** (mới): `apps/background-job-service/src/gamification/gamification-failed-event-retry.service.spec.ts`
- [ ] **Hành động**: add
- [ ] **Chi tiết**:
  - Mock `GamificationFailedEventRepository`, `GamificationEngineService`
  - `it('RESOLVED khi engine trả RECORDED')` — TC-109, BR13.21
  - `it('RESOLVED khi engine trả DUPLICATE')` — BR13.22 (DUPLICATE → RESOLVED)
  - `it('retry_count tăng khi engine lỗi, chưa đủ 5')` — BR13.21
  - `it('GAVE_UP và log GAMIFICATION_RECORD_GAVE_UP khi retry_count >= 5')` — TC-110, BR13.21
  - `it('loại CHECKIN chưa có handler → giữ PENDING, không tăng retry_count')` — BR13.22
  - `it('kind null / chuỗi lạ coi là RECORD')` — BR13.22
  - **Tham chiếu**: BR13.21, BR13.22; TC-109, TC-110

### Bước 25 — Test: GamificationEngine — AchievementNotifier được gọi sau commit

- [ ] **Mục tiêu**: Bao phủ BR13.24 (cổng thông báo no-op ở U1); không phát khi isRetry
- [ ] **File thay đổi**: `libs/modules/src/lib/gamification/engine/gamification-engine.handlers.spec.ts`
- [ ] **Hành động**: edit
- [ ] **Chi tiết**:
  - Mock `AchievementNotifier`
  - `it('gọi notifier sau RECORDED không phải chạy lại')` — BR13.24
  - `it('không gọi notifier khi isRetry=true')` — BR13.24
  - `it('lỗi notifier không ảnh hưởng kết quả RECORDED')` — BR13.24
  - **Tham chiếu**: BR13.24; `rules.md`; TC liên quan

---

## Thứ tự thực hiện và dependency

```
Bước 1 → Bước 2 → Bước 3    (Migration trước Entity)
Bước 4                         (DTO độc lập với migration)
Bước 8 → Bước 5 → Bước 6 → Bước 7    (Interface trước Engine)
Bước 14                       (FailedEventStore sau Entity)
Bước 15 → Bước 16 → Bước 17  (Types trước Service trước Module)
Bước 9, 10                    (H1, H2 cần Publisher)
Bước 11, 12, 13               (H3, H4, H5 cần Publisher)
Bước 18                       (Kiểm Publisher timeout)
Bước 19–25                    (Tests sau implementation)
```

---

## Traceability ngược

| Bước | BR / US | TC |
|---|---|---|
| 1, 2, 14 | BR13.8, BR13.22, ADR-013 | TC-108, TC-109 |
| 3 | BR13.23, BR-3.11 | (U4 kiểm qua C-09) |
| 4 | A-01 additive, BR13.23 | — |
| 5 | BR13.18 | TC-118 |
| 6 | BR13.23 | — |
| 7, 8, 25 | BR13.24, S-03 | — |
| 9, 21 | BR13.2, BR13.7, BR13.17, BR13.19, BR13.20 | TC-101, TC-103, TC-104, TC-111 |
| 10, 21 | BR13.17, BR13.20 | TC-101 |
| 11, 22 | BR13.14, BR13.17, BR13.20 | TC-119, TC-120, TC-121 |
| 12, 22 | BR13.14, BR13.17 | TC-121 |
| 13, 23 | BR13.14, BR13.15 | TC-122, TC-123 |
| 15, 16, 24 | BR13.21, BR13.22 | TC-109, TC-110 |
| 17 | BR13.21 | — |
| 18 | BR13.7 | TC-125 |

**Kịch bản TC còn lại** (không test được bằng unit test, cần integration hoặc staging):
- TC-102 (DUPLICATE hai tab): cần Kafka thật hoặc integration test DB
- TC-105 (Test Account): unit test mock `user.is_operator=true` — đã có trong file handler spec
- TC-106 (hai tab song song): cần concurrent test với DB thật
- TC-108 (Kafka hỏng): unit test mock kafkaService throw
- TC-112, TC-113, TC-114 (lượt ghi danh mới): unit test mock class_user khác nhau
- TC-116, TC-117 (Points tắt): unit test mock config `points_enabled=false`

---

## Ghi chú kỹ thuật

- Toàn bộ hook (H1–H5) dùng `try/catch` bên ngoài mọi logic gamification; lỗi chỉ log, không throw (BR13.7)
- `GamificationRecordPublisher` inject vào `ClassService` và `QuizService` qua module của service — kiểm xem đã export chưa; nếu chưa thì thêm vào exports của `GamificationModule`
- Lọc sớm BR13.19 (đọc config trước publish): kiểm `gamificationConfigService.getSetting().is_enabled`; nếu tắt thì không publish. Đọc lỗi thì vẫn publish (engine kiểm lại). Cân nhắc cache Redis (ADR-003) — không cần thêm logic, `getConfig()` đã cache
- Migration cần đánh timestamp theo thứ tự, kiểm migration cuối cùng hiện có (WP0 dùng `1789997000000`, WP0 seed `1789998000000`) → migration Bước 1 dùng `1789999000000` hoặc timestamp thực tế
- `GamificationRecordPayloadDto.object_name` là trường mới; các hook cũ WP1 không gắn field này → engine fallback `object_name_snapshot = null` (không sao, không làm hỏng dữ liệu cũ)
- File spec có sẵn `gamification-engine.handlers.spec.ts`: đọc trước khi edit để không trùng test name
