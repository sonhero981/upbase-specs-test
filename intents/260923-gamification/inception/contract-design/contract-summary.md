---
intent: 260923-gamification
artifact: contract-summary
stage: 2.8 contract-design
version: 2.0
status: agreed
approved_at: 2026-10-13 ([GIẢ LẬP] BE lead ký, DEC-T21)
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
scope: cả intent, 19 US (DEC-T15)
consumes: inception/units-generation/ v2.0 (DEC-T20), inception/domain-design/ v2.0 (DEC-T19), inception/prd/prd.md v0.14 + 2.43 Q1–Q17, lms-be change upbase-221099-gamification (DEC-T1), lms-be origin/feature/gamification @9006b80 · ops-fe @1e01033bf · lms-fe @b2cc49455
supersedes: v1.0 (C-01…C-03, DEC-T8)
---
# Contract Summary: Gamification, cả intent

28 contract: 21 REST (Ops, lms), 4 async (Kafka, socket.io), 3 shared-schema / in-process. Không có API public / external. Provider: lms-be (app `ops`, `lms`, `event-processor-service`); consumer: ops-fe, lms-fe, và Unit khác trong lms-be. Câu hỏi và trả lời ở `contract-design-questions.md`.

**Trạng thái**: Draft → đã ký (BE lead ký "Approved by", được code) → Final (sau curl ở 3.6). Mọi contract **Agreed** (BE lead ký 2026-10-13, DEC-T21), được code.

**Lệch so với design gốc và code WP3** (đã có ADR hoặc câu hỏi): `PUT` cả khối → `PATCH` một trường (ADR-004, ADR-016); `tags` mang mã quyền, `security` có tên quyền (ADR-002); mã lỗi gamification dùng dải `630xxx` của WP3 (Q1, đổi C-02 v1.0); bỏ trần trên của WP3 cho điểm, điểm nền, bội số, trần hạng (Q2); endpoint `users` của design gốc đổi tên `learners` để khớp mã quyền; check-in qua `POST /gamification/check-in` (ADR-010); bỏ lỗi `630011` và bỏ việc tự tắt tiêu chí BADGES khi tắt Badges của WP3 (BR-10.7, BR-10.8); `gamification_failed_events` thêm cột `kind`.

## Base URL và quy ước chung
Xem S-01. Ops: `https://uplms-api.staging.upbase.asia/ops/api/v1`; lms: `https://uplms-api.staging.upbase.asia/lms/api/v1` (lms-fe `apps/lms-pro/.env.example:4`, ops-fe `apps/ops-fe/.env.example:1`). Field `snake_case`. Tenant lấy từ người dùng đã xác thực, không header.

**Mã lỗi gamification** (dải `630xxx`, `lms-be origin/feature/gamification @9006b80: libs/constants/src/lib/exceptions/exceptions.code.ts:635-645`; exception HTTP 400 `GamificationSettingException`):

| Mã | Key | Dùng ở |
|---|---|---|
| 400\|630001 | GAMIFICATION_DISABLED (mới, chỗ trống của WP3) | C-02, C-04…C-07, C-11 ghi khi Gamification tắt |
| 400\|630002…630011 | Có sẵn WP3 (point rules, badges, milestone, ảnh, level, tiêu chí, bảng) | C-04…C-07 |
| 400\|630013 | GAMIFICATION_EXPORT_LIMIT (mới) | C-10 export |
| 400\|630014 | GAMIFICATION_CAMPAIGN_INVALID_DATES (mới) | C-11 |
| 400\|630015 | GAMIFICATION_CAMPAIGN_LOCKED (mới) | C-11 |
| 404\|630012 | GAMIFICATION_NOT_AVAILABLE (mới) | mọi API lms trừ C-15, C-16 |
| 404\|630016 | GAMIFICATION_BOARD_NOT_AVAILABLE (mới) | C-19, C-20, C-21 khi bảng tắt/khoá |

Hai mã 404 cần exception mới (exception WP3 `GamificationSettingException` cố định HTTP 400, R-09).

## Contracts

| # | Provider Unit | Consumer | Mechanism | Owner | Có sẵn / mới | Trạng thái | Unit |
|---|---|---|---|---|---|---|---|
| S-01 | lms-be (ops, lms) | ops-fe, lms-fe | shared-schema | BE lead | Có sẵn + mới | Agreed | mọi Unit |
| C-01 | U0 | ops-fe OpsSettingsPage | REST Ops | BE lead | Sửa WP3 | Agreed | U0 (+U15 thêm running_campaign_count) |
| C-02 | U0 | ops-fe OpsSettingsPage | REST Ops | BE lead | Sửa WP3 (PUT → PATCH) | Agreed | U0 |
| C-03 | lms-be ops (có sẵn) | ops-fe useHasPermission | REST Ops | BE lead | Có sẵn, không đổi | Agreed | U0 |
| C-04 | U3 | ops-fe OpsSettingsPage (khối Points) | REST Ops | BE lead | Sửa WP3 | Agreed | U3 |
| C-05 | U8 | ops-fe OpsSettingsPage (khối Badges) | REST Ops | BE lead | Sửa WP3 | Agreed | U8 |
| C-06 | U10 | ops-fe OpsSettingsPage (khối Levels) | REST Ops | BE lead | Sửa WP3 | Agreed | U10 |
| C-07 | U13 | ops-fe OpsSettingsPage (khối Leaderboard) | REST Ops | BE lead | Sửa WP3 | Agreed | U13 |
| C-08 | U13 | ops-fe OpsSettingsPage | REST Ops | BE lead | Mới | Agreed | U13 |
| C-09 | U4 | ops-fe OpsAchievementLogPage | REST Ops | BE lead | Mới | Agreed | U4 |
| C-10 | U14 | ops-fe OpsLearnerListPage | REST Ops | BE lead | Mới | Agreed | U14 |
| C-11 | U15 | ops-fe OpsCampaignPanels | REST Ops | BE lead | Mới | Agreed | U15 |
| C-12 | U17 | ops-fe OpsCampaignPanels | REST Ops | BE lead | Mới | Agreed | U17 |
| C-13 | U5 | lms-fe LmsGamificationVisibility, LmsGamificationFeature | REST lms | BE lead | Mới | Agreed | U5, U2 |
| C-14 | U5 | lms-fe LmsGamificationFeature | REST lms | BE lead | Mới | Agreed | U5 |
| C-15 | U5 | lms-fe LmsAppShellIntegration (My Learning) | REST lms | BE lead | Có sẵn, thêm field | Agreed | U5 |
| C-16 | U2 | lms-fe LmsCheckinTrigger | REST lms | BE lead | Mới | Agreed | U2 |
| C-17 | U7 | lms-fe LmsGamificationFeature | REST lms | BE lead | Mới | Agreed | U7 |
| C-18 | U9 | lms-fe LmsGamificationFeature (tab Badges) | REST lms | BE lead | Mới | Agreed | U9 |
| C-19 | U11 | lms-fe LmsGamificationFeature | REST lms | BE lead | Mới | Agreed | U11 |
| C-20 | U12 | lms-fe LmsGamificationFeature | REST lms | BE lead | Mới | Agreed | U12 |
| C-21 | U16 | lms-fe LmsGamificationFeature | REST lms | BE lead | Mới | Agreed | U16, U17 |
| A-01 | U1 | U1 engine (event-processor); producer U1 hook | Kafka | BE lead | Có sẵn WP1, thêm field tuỳ chọn | Agreed | U1, U2 |
| A-02 | U2 | U2 consumer (event-processor) | Kafka | BE lead | Topic có sẵn, payload mới | Agreed | U2 |
| A-03 | U6 | lms-fe LmsAchievementRealtime | socket.io | BE lead | Mới | Agreed | U6 |
| A-04 | U8 | U8 BadgeBackfill (event-processor) | Kafka | BE lead | Topic mới | Agreed | U8 |
| S-02 | U0, U1, U2, U11, U15, U17 | các Unit đọc | shared-schema | BE lead | WP0 + mới | Agreed | nhiều |
| S-03 | U1, U8, U11 | U2, U6, U14, U16, U17, FailedEventRetry | in-process-sync | BE lead | WP1 + mới | Agreed | U1, U2, U6, U8, U11, U14, U16, U17 |

### Phủ cạnh DAG (`unit-of-work-dependency.md`)

| Cạnh (A phụ thuộc B) | Contract | Ghi chú |
|---|---|---|
| U1 → U0 | S-02 (cấu hình), S-03 | Engine đọc công tắc qua GamificationConfig (in-process, cùng lib) |
| U2 → U1 | A-02, S-03 (engine.record) | Consumer check-in gọi engine trong cùng tiến trình |
| U2 → U5 | C-13 (today, timezone), C-16 | Dùng API client và app shell của U5 |
| U3 → U0 | C-04, S-02 | Khối mới trên trang và API của U0 |
| U4 → U1 | S-02 (ledger), C-09 |  |
| U5 → U1 | S-02 (user_stats), C-13, C-14, C-15 |  |
| U6 → U5 | A-03, C-13 (cờ hiển thị), S-03 (AchievementNotifier.notify) | U6 thay adapter no-op của U1 |
| U7 → U5 | C-17 | Panel mở từ panel của U5 |
| U8 → U0 | C-05, S-02 |  |
| U8 → U1 | A-04, S-03 (engine.awardBackfill) |  |
| U9 → U5 | C-18 | Tab mở từ ô Badges của U5 |
| U9 → U8 | S-02 (cấu hình huy hiệu) |  |
| U10 → U3 | S-02 (points_enabled → is_locked), C-06 |  |
| U10 → U8 | S-02 (badges_enabled → is_locked), C-06 |  |
| U11 → U1 | S-02 (ledger, user_stats) |  |
| U11 → U5 | C-19 trên LearnerGamificationApi của U5 |  |
| U12 → U11 | S-02 (snapshot), C-20 |  |
| U13 → U3 | S-02 (points_enabled → locked_boards), C-07 |  |
| U13 → U4 | C-08 trên GamificationOpsDataApi của U4 |  |
| U13 → U11 | S-02 (snapshot), C-08 |  |
| U14 → U4 | C-10 trên GamificationOpsDataApi của U4 |  |
| U14 → U11 | S-03 (computeRange) | Không có REST giữa hai Unit |
| U15 → U0 | C-11, C-01 (running_campaign_count) |  |
| U16 → U11 | S-02 (snapshot), S-03 (computeRange, writeSnapshot), C-21 |  |
| U16 → U12 | C-21 (/leaderboard/me trong campaign) |  |
| U16 → U15 | S-02 (campaigns) |  |
| U17 → U4 | C-12 trên GamificationOpsDataApi của U4 |  |
| U17 → U16 | S-02 (snapshot version 0, participants), S-03 (computeRange với participant_ids, writeSnapshot), C-21 |  |

## Quyền endpoint (ADR-002)

| Mã quyền | Khai `security.name` ở | `tags` của endpoint |
|---|---|---|
| `gr_view_gamification_settings` | mọi GET cấu hình, GET campaign | C-01 (vào trang) và GET campaign: cả ba mã (2.43 Q1). GET bốn khối cấu hình và xem trước (C-04…C-08): chỉ `view_settings` + `update_settings` (BR-15.7: quyền học viên không xem cấu hình) |
| `gr_update_gamification_settings` | mọi PATCH cấu hình, POST/PUT/DELETE campaign | chỉ mã này |
| `gr_view_gamification_learners` | C-09, C-10, C-12 | chỉ mã này |

- Mọi endpoint Ops: `@UseGuards(StaffGuard)`, `@ApiOperation({ operationId, security, tags })` theo cột trên; ngoại lệ có chủ đích của `backend.md` § 2 (`tags: []`), BE lead ghi vào convention (ADR-002). WP3 có `@ApiTags('Gamification Setting')` ở class (`gamification-setting.controller.ts:20`) — giữ cho Swagger, không ảnh hưởng quyền.
- API lms: `LmsGuard`, không có hệ quyền; khai `@ApiOperation({ operationId })` cho Swagger.

## S-01 Quy ước chung và schema dùng chung

Envelope, lỗi, phân trang, mã lỗi gamification, schema dùng chung. Mọi contract REST tham chiếu `S-01#/…`.

```yaml
x-contract-id: S-01
x-kind: shared-schema
x-status: Agreed
x-evidence:
  response_success: libs/utils/src/lib/common/response.common.ts:12-17 SAPPResponse.Success → {success:true, data}
  response_error: libs/exceptions/src/lib/exceptions.filter.ts:100-109
  validation: apps/ops/src/main.ts:30-44, apps/lms/src/main.ts:28-45 (whitelist, transform, stopAtFirstError; 422|000405)
  pagination_meta: libs/interface/src/lib/dto/response/response.dto.ts:12-18
  ops_paged_pattern: apps/ops/src/caching-settings/caching-settings.service.ts:32-57 trả Success({metadata, caching_setttings}) — tên khoá danh sách không thống nhất trong repo; gamification chốt khoá items
    (Q4)
  prefix: APP_OPS_PREFIX / APP_LMS_PREFIX = api/v1 (.env.example:19-20)
  gamification_exception: 'lms-be origin/feature/gamification @9006b80: libs/exceptions/src/lib/gamification/gamification-setting.exceptions.ts:17-32 (HTTP 400, dải 630xxx, exceptions.code.ts:635-645)'
components:
  schemas:
    ErrorResponse:
      type: object
      required:
      - success
      - data
      - error
      properties:
        success:
          type: boolean
          enum:
          - false
        data:
          nullable: true
        error:
          type: object
          required:
          - code
          - message
          properties:
            code:
              type: string
              example: 400|630001
            message:
              type: string
            others:
              nullable: true
            replacements:
              type: object
    PaginationMeta:
      type: object
      required:
      - total_records
      - total_pages
      - page_size
      - page_index
      properties:
        total_records:
          type: integer
        total_pages:
          type: integer
        page_size:
          type: integer
        page_index:
          type: integer
        next_page:
          type: boolean
          description: response.dto.ts:12-18
    Learner:
      type: object
      required:
      - user_id
      - full_name
      properties:
        user_id:
          type: string
          format: uuid
        full_name:
          type: string
        avatar:
          type: string
          nullable: true
    LeaderboardRow:
      type: object
      required:
      - learner
      - value
      properties:
        rank:
          type: integer
          nullable: true
          description: null khi chưa có chỉ số (BR-6.6, BR-6.16 hạng 1)
        learner:
          $ref: '#/components/schemas/Learner'
        value:
          type: integer
        achieved_at:
          type: string
          format: date-time
          nullable: true
    ActionCode:
      type: string
      enum:
      - CHECKIN
      - ACTIVITY_COMPLETED
      - COURSE_COMPLETED
      - TEST_PASSED
      description: 'lms-be origin/feature/gamification @9006b80: libs/constants/src/lib/gamification/gamification.constants.ts:2-7'
    BadgeType:
      type: string
      enum:
      - CHECKIN
      - ACTIVITY
      - TEST
      - COURSE
    LevelCriterion:
      type: string
      enum:
      - POINTS
      - COURSES
      - BADGES
    BoardCategory:
      type: string
      enum:
      - POINTS
      - ACTIVITIES
      - COURSES
      - BADGES
      - LEVEL
  responses:
    Unauthorized:
      description: 401|000000
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    Forbidden:
      description: 403|000000 — staff không có quyền nào trong tags
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    ValidationError:
      description: 422|000405 — ValidationPipe, others = chi tiết field
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    GamificationNotAvailable:
      description: 404|630012 — Gamification hoặc Visibility tắt, Test Account (BR-1.1, BR-1.5). lms-fe ẩn toàn bộ
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
```

## C-01 Đọc cấu hình chung

Đổi từ v1.0: thêm `running_campaign_count` (additive, 2.43 Q7). WP3 hiện trả `{is_enabled, is_visible, first_enabled_at, last_enabled_at}` (`lms-be origin/feature/gamification @9006b80: apps/ops/src/gamification-setting/services/gamification-general-setting.service.ts:8-13`).

```yaml
openapi: 3.0.3
info:
  title: Gamification general settings - read (Ops)
  version: 1.0.0
  x-contract-id: C-01
  x-status: Agreed
  x-provider: lms-be ops · GamificationSettingsOpsApi
  x-consumer: ops-fe OpsSettingsPage
  x-units: U0, U15
servers:
- url: https://uplms-api.staging.upbase.asia/ops/api/v1
x-existing: 'lms-be origin/feature/gamification @9006b80: gamification-setting.controller.ts:35-47 (GET settings, sửa tags + security name)'
paths:
  /gamification/settings:
    get:
      operationId: get_gamification_settings
      summary: Đọc cấu hình chung
      description: Tạo bản mặc định nếu chưa có (ADR-007). Cache Redis (ADR-003).
      x-permission:
        security:
        - group:
          - gamification_management
          name:
          - gr_view_gamification_settings
          display_name:
          - View gamification settings
          description:
          - Permission to view gamification settings
          isScan:
          - 'true'
        tags:
        - gr_view_gamification_settings
        - gr_update_gamification_settings
        - gr_view_gamification_learners
      x-curl: 'curl -s ''https://uplms-api.staging.upbase.asia/ops/api/v1/gamification/settings'' -H ''Authorization: Bearer <auth-value>'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    $ref: '#/components/schemas/GeneralSettings'
              example:
                success: true
                data:
                  is_enabled: true
                  is_visible: false
                  has_been_visible: false
                  first_enabled_at: '2026-10-13T02:00:00.000Z'
                  last_enabled_at: '2026-10-13T02:00:00.000Z'
                  running_campaign_count: 0
        '401':
          $ref: S-01#/components/responses/Unauthorized
        '403':
          $ref: S-01#/components/responses/Forbidden
components:
  schemas:
    GeneralSettings:
      type: object
      required:
      - is_enabled
      - is_visible
      - has_been_visible
      - first_enabled_at
      - last_enabled_at
      - running_campaign_count
      properties:
        is_enabled:
          type: boolean
        is_visible:
          type: boolean
          description: Giữ giá trị khi is_enabled false (BR-14.2)
        has_been_visible:
          type: boolean
          description: visibility_first_enabled_at khác null (ADR-005, 2.43 Q2)
        first_enabled_at:
          type: string
          format: date-time
          nullable: true
        last_enabled_at:
          type: string
          format: date-time
          nullable: true
        running_campaign_count:
          type: integer
          description: Số campaign In Progress cho popover tắt (2.43 Q7). Trước U15 luôn 0
```

## C-02 Ghi một công tắc chung

Đổi từ v1.0: mã lỗi `400|700001` → `400|630001` theo dải WP3 (Q1). WP3 có `PUT settings` (`lms-be origin/feature/gamification @9006b80: gamification-setting.controller.ts:52-64`) — thay bằng PATCH (ADR-004, ADR-016).

```yaml
openapi: 3.0.3
info:
  title: Gamification general settings - update (Ops)
  version: 1.0.0
  x-contract-id: C-02
  x-status: Agreed
  x-provider: lms-be ops · GamificationSettingsOpsApi
  x-consumer: ops-fe OpsSettingsPage
  x-units: U0
servers:
- url: https://uplms-api.staging.upbase.asia/ops/api/v1
paths:
  /gamification/settings:
    patch:
      operationId: update_gamification_settings
      summary: Ghi đúng một công tắc
      description: 'is_visible khi is_enabled=false → 400|630001 (BR-14.2). Bật is_enabled: last_enabled_at = now, first_enabled_at nếu null (BR-14.5). Bật is_visible lần đầu: visibility_first_enabled_at
        (ADR-005). Xoá cache trong request (2.43 Q3). Bằng giá trị đang lưu: không ghi, 200.'
      x-permission:
        security:
        - group:
          - gamification_management
          name:
          - gr_update_gamification_settings
          display_name:
          - Update gamification settings
          description:
          - Permission to update gamification settings
          isScan:
          - 'true'
        tags:
        - gr_update_gamification_settings
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              minProperties: 1
              maxProperties: 1
              description: 'Đúng một trường mỗi lần ghi (ADR-004). '
              properties:
                is_enabled:
                  type: boolean
                is_visible:
                  type: boolean
      x-curl: 'curl -s -X PATCH ''https://uplms-api.staging.upbase.asia/ops/api/v1/gamification/settings'' -H ''Authorization: Bearer <auth-value>'' -H ''Content-Type: application/json'' -d ''{"is_enabled":true}'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    $ref: C-01#/components/schemas/GeneralSettings
        '400':
          description: 'GAMIFICATION_DISABLED: đổi is_visible khi Gamification tắt'
          content:
            application/json:
              schema:
                $ref: S-01#/components/schemas/ErrorResponse
              example:
                success: false
                data: null
                error:
                  code: 400|630001
                  message: exceptions.<key>
                  others: null
                  replacements: {}
        '401':
          $ref: S-01#/components/responses/Unauthorized
        '403':
          $ref: S-01#/components/responses/Forbidden
        '422':
          $ref: S-01#/components/responses/ValidationError
```

## C-03 Ops GET /me (có sẵn)

Không đổi so với v1.0 (`apps/ops/src/app/app.controller.ts:34-43`; `roles[].permissions` ở `apps/ops/src/staffs/staffs.service.ts:453-472`).

```yaml
openapi: 3.0.3
info:
  title: Ops me (có sẵn)
  version: 1.0.0
  x-contract-id: C-03
  x-status: Agreed
  x-provider: lms-be ops
  x-consumer: ops-fe
  x-units: U0
servers:
- url: https://uplms-api.staging.upbase.asia/ops/api/v1
x-backward-compatibility: Không đổi
paths:
  /me:
    get:
      operationId: get_me
      summary: 'Field ops-fe đọc: roles[].permissions'
      description: Có sẵn.
      x-curl: 'curl -s ''https://uplms-api.staging.upbase.asia/ops/api/v1/me'' -H ''Authorization: Bearer <auth-value>'''
      responses:
        '200':
          description: OK, shape hiện tại
```

## C-04 Bảng điểm

WP3: `GET/PUT point-rules` (`lms-be origin/feature/gamification @9006b80: gamification-setting.controller.ts:69-98`), DTO `libs/interface/src/lib/gamification/setting/gamification-setting.dto.ts:30-54`, giới hạn CHECKIN 1–40 và 1–1000 (`gamification-point-rule.service.ts:11-16`) trái BR-8.5, BR-8.5a → bỏ (Q2). **Lệch WP3 thêm (R-02):** tắt Points không ghi `is_enabled = false` cho tiêu chí hạng POINTS — chỉ suy ra `is_locked` (BR-10.7 giữ giá trị).

```yaml
openapi: 3.0.3
info:
  title: Gamification point rules (Ops)
  version: 1.0.0
  x-contract-id: C-04
  x-status: Agreed
  x-provider: lms-be ops · GamificationSettingsOpsApi
  x-consumer: ops-fe OpsSettingsPage
  x-units: U3
servers:
- url: https://uplms-api.staging.upbase.asia/ops/api/v1
paths:
  /gamification/point-rules:
    get:
      operationId: get_gamification_point_rules
      summary: Đọc khối Points
      description: Bốn hành động theo thứ tự ActionCode; mặc định theo design 10/10/150/25 (2.43 Q15).
      x-permission:
        security:
        - group:
          - gamification_management
          name:
          - gr_view_gamification_settings
          display_name:
          - View gamification settings
          description:
          - Permission to view gamification settings
          isScan:
          - 'true'
        tags:
        - gr_view_gamification_settings
        - gr_update_gamification_settings
      x-curl: 'curl -s ''https://uplms-api.staging.upbase.asia/ops/api/v1/gamification/point-rules'' -H ''Authorization: Bearer <auth-value>'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    $ref: '#/components/schemas/PointRules'
        '401': &id001
          $ref: S-01#/components/responses/Unauthorized
        '403': &id002
          $ref: S-01#/components/responses/Forbidden
    patch:
      operationId: update_gamification_point_rules
      summary: Ghi một trường của khối Points
      description: 'Đúng một trong: points_enabled, hoặc {source, is_enabled}, hoặc {source, points}. Tắt Points thì khoá tiêu chí hạng POINTS và bảng POINTS mà giữ giá trị (BR-10.7, BR-11.4). Áp từ lúc
        lưu (C4).'
      x-permission:
        security:
        - group:
          - gamification_management
          name:
          - gr_update_gamification_settings
          display_name:
          - Update gamification settings
          description:
          - Permission to update gamification settings
          isScan:
          - 'true'
        tags:
        - gr_update_gamification_settings
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              minProperties: 1
              maxProperties: 1
              description: 'Đúng một trường mỗi lần ghi (ADR-004). Ô trống gửi không được: FE báo lỗi tại ô (BR-14.11).'
              properties:
                points_enabled:
                  type: boolean
                rule:
                  type: object
                  minProperties: 2
                  maxProperties: 2
                  required:
                  - source
                  properties:
                    source:
                      $ref: S-01#/components/schemas/ActionCode
                    is_enabled:
                      type: boolean
                    points:
                      type: integer
                      minimum: 1
                      maximum: 2147483647
      x-curl: 'curl -s -X PATCH ''https://uplms-api.staging.upbase.asia/ops/api/v1/gamification/point-rules'' -H ''Authorization: Bearer <auth-value>'' -H ''Content-Type: application/json'' -d ''{"rule":{"source":"CHECKIN","points":20}}'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    $ref: '#/components/schemas/PointRules'
        '400':
          description: GAMIFICATION_DISABLED (630001) khi Gamification tắt (BR-14.7); GAMIFICATION_INVALID_POINT_RULES (630002)
          content:
            application/json:
              schema:
                $ref: S-01#/components/schemas/ErrorResponse
        '401': *id001
        '403': *id002
        '422':
          $ref: S-01#/components/responses/ValidationError
components:
  schemas:
    PointRules:
      type: object
      required:
      - points_enabled
      - rules
      properties:
        points_enabled:
          type: boolean
        rules:
          type: array
          items:
            type: object
            required:
            - source
            - is_enabled
            - points
            properties:
              source:
                $ref: S-01#/components/schemas/ActionCode
              is_enabled:
                type: boolean
              points:
                type: integer
                minimum: 1
                maximum: 2147483647
                description: Không giới hạn trên nghiệp vụ (BR-8.5); trần kỹ thuật int32 (Q2). Với CHECKIN là điểm nền (BR-8.5a)
              checkin_settings:
                type: object
                nullable: true
                properties:
                  step:
                    type: integer
                    example: 5
                  cap:
                    type: integer
                    description: max(40, nền), chỉ đọc
```

## C-05 Cấu hình huy hiệu

WP3: `GET/PUT badges` (`lms-be origin/feature/gamification @9006b80: gamification-setting.controller.ts:103-132`), DTO `gamification-setting.dto.ts:56-114`, ảnh FILE .png/.jpg/.jpeg/.webp/.svg ≤ 1MB (`gamification-badge-setting.service.ts:18-19,220-241`, khớp 2.43 Q12). Tách PATCH loại và PATCH từng mốc (Q3). **Lệch WP3 thêm (R-02):** bỏ lỗi `630011 BADGES_LAST_LEVEL_CRITERION` (`base-gamification-setting.service.ts:92-120`) và bỏ việc `project()` ghi `is_enabled = false` cho tiêu chí BADGES khi tắt Badges (`gamification-badge-setting.service.ts:129-134`): PRD cho tắt, tiêu chí chỉ khoá và giữ giá trị, khối Levels hiện cảnh báo (BR-10.7, BR-10.8).

```yaml
openapi: 3.0.3
info:
  title: Gamification badges (Ops)
  version: 1.0.0
  x-contract-id: C-05
  x-status: Agreed
  x-provider: lms-be ops · GamificationSettingsOpsApi
  x-consumer: ops-fe OpsSettingsPage
  x-units: U8
servers:
- url: https://uplms-api.staging.upbase.asia/ops/api/v1
paths:
  /gamification/badges:
    get:
      operationId: get_gamification_badges
      summary: Đọc khối Badges
      description: 4 loại × 8 mốc, sắp theo mốc tăng dần.
      x-permission:
        security:
        - group:
          - gamification_management
          name:
          - gr_view_gamification_settings
          display_name:
          - View gamification settings
          description:
          - Permission to view gamification settings
          isScan:
          - 'true'
        tags:
        - gr_view_gamification_settings
        - gr_update_gamification_settings
      x-curl: 'curl -s ''https://uplms-api.staging.upbase.asia/ops/api/v1/gamification/badges'' -H ''Authorization: Bearer <auth-value>'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    $ref: '#/components/schemas/BadgeSettings'
        '401': &id001
          $ref: S-01#/components/responses/Unauthorized
        '403': &id002
          $ref: S-01#/components/responses/Forbidden
    patch:
      operationId: update_gamification_badges
      summary: Bật tắt Badges hoặc một loại
      description: 'Đúng một trong: badges_enabled, hoặc {type, is_enabled}. Chuyển sang bật thì phát việc trao bù A-04 sau khi lưu (BR-9.9). Tắt Badges khoá tiêu chí BADGES, bảng BADGES (BR-10.7, BR-11.4).'
      x-permission:
        security:
        - group:
          - gamification_management
          name:
          - gr_update_gamification_settings
          display_name:
          - Update gamification settings
          description:
          - Permission to update gamification settings
          isScan:
          - 'true'
        tags:
        - gr_update_gamification_settings
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              minProperties: 1
              maxProperties: 1
              description: 'Đúng một trường mỗi lần ghi (ADR-004). '
              properties:
                badges_enabled:
                  type: boolean
                badge_type:
                  type: object
                  required:
                  - type
                  - is_enabled
                  properties:
                    type:
                      $ref: S-01#/components/schemas/BadgeType
                    is_enabled:
                      type: boolean
      x-curl: 'curl -s -X PATCH ''https://uplms-api.staging.upbase.asia/ops/api/v1/gamification/badges'' -H ''Authorization: Bearer <auth-value>'' -H ''Content-Type: application/json'' -d ''{"badges_enabled":true}'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    $ref: '#/components/schemas/BadgeSettings'
        '400':
          description: 630001 Gamification tắt; 630003 dữ liệu sai. Không trả 630011 (R-02)
          content:
            application/json:
              schema:
                $ref: S-01#/components/schemas/ErrorResponse
        '401': *id001
        '403': *id002
        '422': &id003
          $ref: S-01#/components/responses/ValidationError
  /gamification/badges/{id}:
    patch:
      operationId: update_gamification_badge
      summary: Ghi một trường của một mốc
      description: Đúng một trong name, description, image_resource_id. name rỗng → default_name (US9). Mốc không sửa (630004). Áp ngay cho người đã đạt, không thông báo (BR-9.4).
      x-permission:
        security:
        - group:
          - gamification_management
          name:
          - gr_update_gamification_settings
          display_name:
          - Update gamification settings
          description:
          - Permission to update gamification settings
          isScan:
          - 'true'
        tags:
        - gr_update_gamification_settings
      parameters:
      - name: id
        in: path
        required: true
        schema:
          type: string
          format: uuid
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              minProperties: 1
              maxProperties: 1
              description: 'Đúng một trường mỗi lần ghi (ADR-004). '
              properties:
                name:
                  type: string
                  maxLength: 255
                  nullable: true
                description:
                  type: string
                  nullable: true
                image_resource_id:
                  type: string
                  format: uuid
                  nullable: true
      x-curl: 'curl -s -X PATCH ''https://uplms-api.staging.upbase.asia/ops/api/v1/gamification/badges/<id>'' -H ''Authorization: Bearer <auth-value>'' -H ''Content-Type: application/json'' -d ''{"name":"Legend"}'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    $ref: '#/components/schemas/Badge'
        '400':
          description: 630001; 630005 ảnh sai định dạng/kích thước
          content:
            application/json:
              schema:
                $ref: S-01#/components/schemas/ErrorResponse
        '404':
          description: Mốc không thuộc tenant
          content:
            application/json:
              schema:
                $ref: S-01#/components/schemas/ErrorResponse
        '401': *id001
        '403': *id002
        '422': *id003
components:
  schemas:
    Badge:
      type: object
      required:
      - id
      - milestone
      - name
      - default_name
      properties:
        id:
          type: string
          format: uuid
        milestone:
          type: integer
          description: Chỉ đọc (BR-9.2)
        name:
          type: string
        default_name:
          type: string
        description:
          type: string
          nullable: true
        image_resource_id:
          type: string
          format: uuid
          nullable: true
        image_url:
          type: string
          description: Ảnh mặc định khi tài nguyên bị xoá (BR-1.7)
    BadgeSettings:
      type: object
      required:
      - badges_enabled
      - badge_types
      properties:
        badges_enabled:
          type: boolean
        badge_types:
          type: array
          items:
            type: object
            required:
            - type
            - is_enabled
            - badges
            properties:
              type:
                $ref: S-01#/components/schemas/BadgeType
              is_enabled:
                type: boolean
              badges:
                type: array
                items:
                  $ref: '#/components/schemas/Badge'
```

## C-06 Cấu hình hạng

WP3: `GET/PUT levels` (`lms-be origin/feature/gamification @9006b80: gamification-setting.controller.ts:137-166`), DTO `gamification-setting.dto.ts:116-149`; trần 2..1000, bội số POINTS ≤ 1.000.000 (`gamification-level-setting.service.ts:11-17`) → bỏ trần trên theo PRD, giữ BADGES ≤ 32 vì chỉ có 32 mốc (Q2). Design có công tắc trần: `level_cap_enabled` false = không trần (2.43 RD21). Tiêu chí khoá do tắt Points/Badges không bị đổi `is_enabled`; `running_criteria_count = 0` chỉ để cảnh báo, không chặn (BR-10.8, R-02).

```yaml
openapi: 3.0.3
info:
  title: Gamification levels (Ops)
  version: 1.0.0
  x-contract-id: C-06
  x-status: Agreed
  x-provider: lms-be ops · GamificationSettingsOpsApi
  x-consumer: ops-fe OpsSettingsPage
  x-units: U10
servers:
- url: https://uplms-api.staging.upbase.asia/ops/api/v1
paths:
  /gamification/levels:
    get:
      operationId: get_gamification_levels
      summary: Đọc khối Levels
      description: Kèm is_locked, running_criteria_count.
      x-permission:
        security:
        - group:
          - gamification_management
          name:
          - gr_view_gamification_settings
          display_name:
          - View gamification settings
          description:
          - Permission to view gamification settings
          isScan:
          - 'true'
        tags:
        - gr_view_gamification_settings
        - gr_update_gamification_settings
      x-curl: 'curl -s ''https://uplms-api.staging.upbase.asia/ops/api/v1/gamification/levels'' -H ''Authorization: Bearer <auth-value>'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    $ref: '#/components/schemas/LevelSettings'
        '401': &id001
          $ref: S-01#/components/responses/Unauthorized
        '403': &id002
          $ref: S-01#/components/responses/Forbidden
    patch:
      operationId: update_gamification_levels
      summary: Ghi một trường của khối Levels
      description: 'Đúng một trong: levels_enabled, level_cap_enabled, level_cap, {category, is_enabled}, {category, multiplier}. Tắt tiêu chí đang chạy cuối cùng → 630007 (BR-10.8). Áp từ lúc lưu, chỉ
        tính mốc mới vượt (BR-10.4a).'
      x-permission:
        security:
        - group:
          - gamification_management
          name:
          - gr_update_gamification_settings
          display_name:
          - Update gamification settings
          description:
          - Permission to update gamification settings
          isScan:
          - 'true'
        tags:
        - gr_update_gamification_settings
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              minProperties: 1
              maxProperties: 1
              description: Đúng một trường mỗi lần ghi (ADR-004). BADGES multiplier ≤ 32.
              properties:
                levels_enabled:
                  type: boolean
                level_cap_enabled:
                  type: boolean
                level_cap:
                  type: integer
                  minimum: 2
                  maximum: 2147483647
                criterion:
                  type: object
                  minProperties: 2
                  maxProperties: 2
                  required:
                  - category
                  properties:
                    category:
                      $ref: S-01#/components/schemas/LevelCriterion
                    is_enabled:
                      type: boolean
                    multiplier:
                      type: integer
                      minimum: 1
      x-curl: 'curl -s -X PATCH ''https://uplms-api.staging.upbase.asia/ops/api/v1/gamification/levels'' -H ''Authorization: Bearer <auth-value>'' -H ''Content-Type: application/json'' -d ''{"criterion":{"category":"POINTS","multiplier":3000}}'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    $ref: '#/components/schemas/LevelSettings'
        '400':
          description: 630001; 630006 giá trị sai; 630007 tiêu chí cuối; 630008 tiêu chí đang khoá
          content:
            application/json:
              schema:
                $ref: S-01#/components/schemas/ErrorResponse
        '401': *id001
        '403': *id002
        '422':
          $ref: S-01#/components/responses/ValidationError
components:
  schemas:
    LevelSettings:
      type: object
      required:
      - levels_enabled
      - level_cap_enabled
      - criteria
      - running_criteria_count
      properties:
        levels_enabled:
          type: boolean
        level_cap_enabled:
          type: boolean
        level_cap:
          type: integer
          nullable: true
          minimum: 2
        criteria:
          type: array
          items:
            type: object
            required:
            - category
            - is_enabled
            - multiplier
            - is_locked
            properties:
              category:
                $ref: S-01#/components/schemas/LevelCriterion
              is_enabled:
                type: boolean
              multiplier:
                type: integer
                minimum: 1
              is_locked:
                type: boolean
                description: Khoá theo Points/Badges tắt (BR-10.7)
        running_criteria_count:
          type: integer
          description: 0 → ops-fe hiện cảnh báo cố định (BR-10.8)
```

## C-07 Cấu hình bảng xếp hạng

WP3: `GET/PUT leaderboard-settings` (`lms-be origin/feature/gamification @9006b80: gamification-setting.controller.ts:171-200`), DTO `gamification-setting.dto.ts:151-175`, `locked_boards` (`gamification-leaderboard-setting.service.ts:14-17`).

```yaml
openapi: 3.0.3
info:
  title: Gamification leaderboard settings (Ops)
  version: 1.0.0
  x-contract-id: C-07
  x-status: Agreed
  x-provider: lms-be ops · GamificationSettingsOpsApi
  x-consumer: ops-fe OpsSettingsPage
  x-units: U13
servers:
- url: https://uplms-api.staging.upbase.asia/ops/api/v1
paths:
  /gamification/leaderboard-settings:
    get:
      operationId: get_gamification_leaderboard_settings
      summary: Đọc khối Leaderboard
      description: ''
      x-permission:
        security:
        - group:
          - gamification_management
          name:
          - gr_view_gamification_settings
          display_name:
          - View gamification settings
          description:
          - Permission to view gamification settings
          isScan:
          - 'true'
        tags:
        - gr_view_gamification_settings
        - gr_update_gamification_settings
      x-curl: 'curl -s ''https://uplms-api.staging.upbase.asia/ops/api/v1/gamification/leaderboard-settings'' -H ''Authorization: Bearer <auth-value>'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    $ref: '#/components/schemas/LeaderboardSettings'
        '401': &id001
          $ref: S-01#/components/responses/Unauthorized
        '403': &id002
          $ref: S-01#/components/responses/Forbidden
    patch:
      operationId: update_gamification_leaderboard_settings
      summary: Ghi một công tắc
      description: Đúng một trong sáu boolean. Bảng đang khoá → 630009; tắt bảng đang chạy cuối cùng → 630010. Hiệu lực ở lần mở trang kế tiếp (BR-11.7).
      x-permission:
        security:
        - group:
          - gamification_management
          name:
          - gr_update_gamification_settings
          display_name:
          - Update gamification settings
          description:
          - Permission to update gamification settings
          isScan:
          - 'true'
        tags:
        - gr_update_gamification_settings
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              minProperties: 1
              maxProperties: 1
              description: 'Đúng một trường mỗi lần ghi (ADR-004). '
              properties:
                leaderboard_enabled:
                  type: boolean
                lb_show_points:
                  type: boolean
                lb_show_activities:
                  type: boolean
                lb_show_courses:
                  type: boolean
                lb_show_badges:
                  type: boolean
                lb_show_levels:
                  type: boolean
      x-curl: 'curl -s -X PATCH ''https://uplms-api.staging.upbase.asia/ops/api/v1/gamification/leaderboard-settings'' -H ''Authorization: Bearer <auth-value>'' -H ''Content-Type: application/json'' -d
        ''{"lb_show_badges":false}'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    $ref: '#/components/schemas/LeaderboardSettings'
        '400':
          description: 630001; 630009; 630010
          content:
            application/json:
              schema:
                $ref: S-01#/components/schemas/ErrorResponse
        '401': *id001
        '403': *id002
        '422':
          $ref: S-01#/components/responses/ValidationError
components:
  schemas:
    LeaderboardSettings:
      type: object
      required:
      - leaderboard_enabled
      - lb_show_points
      - lb_show_activities
      - lb_show_courses
      - lb_show_badges
      - lb_show_levels
      - locked_boards
      - running_board_count
      properties:
        leaderboard_enabled:
          type: boolean
        lb_show_points:
          type: boolean
        lb_show_activities:
          type: boolean
        lb_show_courses:
          type: boolean
        lb_show_badges:
          type: boolean
        lb_show_levels:
          type: boolean
        locked_boards:
          type: array
          items:
            $ref: S-01#/components/schemas/BoardCategory
          description: BR-11.4
        running_board_count:
          type: integer
          description: 0 → cảnh báo cố định (BR-11.5)
```

## C-08 Bảng xem trước trên trang cấu hình

2.43 Q16: All time, theo công tắc Show, không dòng You, không chọn khung.

```yaml
openapi: 3.0.3
info:
  title: Gamification leaderboard preview (Ops)
  version: 1.0.0
  x-contract-id: C-08
  x-status: Agreed
  x-provider: lms-be ops · GamificationOpsDataApi
  x-consumer: ops-fe OpsSettingsPage
  x-units: U13
servers:
- url: https://uplms-api.staging.upbase.asia/ops/api/v1
paths:
  /gamification/leaderboard-preview:
    get:
      operationId: get_gamification_leaderboard_preview
      summary: Top 5 All time của một bảng
      description: Đọc snapshot theo con trỏ (ADR-018). Bảng đang tắt hoặc khoá → rows rỗng.
      x-permission:
        security:
        - group:
          - gamification_management
          name:
          - gr_view_gamification_settings
          display_name:
          - View gamification settings
          description:
          - Permission to view gamification settings
          isScan:
          - 'true'
        tags:
        - gr_view_gamification_settings
        - gr_update_gamification_settings
      parameters:
      - name: category
        in: query
        required: true
        schema:
          type: string
          enum:
          - POINTS
          - ACTIVITIES
          - COURSES
          - BADGES
          - LEVEL
      x-curl: 'curl -s ''https://uplms-api.staging.upbase.asia/ops/api/v1/gamification/leaderboard-preview?category=POINTS'' -H ''Authorization: Bearer <auth-value>'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    $ref: '#/components/schemas/LeaderboardPreview'
        '401':
          $ref: S-01#/components/responses/Unauthorized
        '403':
          $ref: S-01#/components/responses/Forbidden
        '422':
          $ref: S-01#/components/responses/ValidationError
components:
  schemas:
    LeaderboardPreview:
      type: object
      required:
      - category
      - rows
      - last_updated_at
      properties:
        category:
          $ref: S-01#/components/schemas/BoardCategory
        rows:
          type: array
          maxItems: 5
          items:
            $ref: S-01#/components/schemas/LeaderboardRow
        last_updated_at:
          type: string
          format: date-time
          nullable: true
```

## C-09 Nhật ký ghi nhận toàn tổ chức

US22. Quyền xem học viên (BR-22.7); Gamification tắt vẫn đọc (BR-15.8). Không export (US22). Mẫu list: `apps/ops/src/caching-settings/caching-settings.service.ts:32-57`.

```yaml
openapi: 3.0.3
info:
  title: Gamification achievement history (Ops)
  version: 1.0.0
  x-contract-id: C-09
  x-status: Agreed
  x-provider: lms-be ops · GamificationOpsDataApi
  x-consumer: ops-fe OpsAchievementLogPage
  x-units: U4
servers:
- url: https://uplms-api.staging.upbase.asia/ops/api/v1
paths:
  /gamification/achievement-history:
    get:
      operationId: get_gamification_achievement_history
      summary: Danh sách ghi nhận, mới nhất trước
      description: Gồm dòng 0 điểm, giữ dòng của người đã Block (BR-22.5), loại Test Account (BR-22.4). Lần lỗi không hiện (BR-22.8).
      x-permission:
        security:
        - group:
          - gamification_management
          name:
          - gr_view_gamification_learners
          display_name:
          - View gamification learners
          description:
          - Permission to view gamification learners, achievement history and campaign results
          isScan:
          - 'true'
        tags:
        - gr_view_gamification_learners
      parameters:
      - name: page_index
        in: query
        required: true
        schema:
          type: integer
          minimum: 1
      - name: page_size
        in: query
        required: true
        schema:
          type: integer
          minimum: 1
          maximum: 100
      - name: user_id
        in: query
        required: false
        schema:
          type: string
          format: uuid
      - name: event_types
        in: query
        required: false
        schema:
          type: array
          items:
            type: string
            enum:
            - POINT
            - BADGE
            - LEVEL
      - name: point_sources
        in: query
        required: false
        schema:
          type: array
          items:
            $ref: S-01#/components/schemas/ActionCode
      - name: from
        in: query
        required: false
        schema:
          type: string
          format: date
        description: Ngày theo múi giờ tenant
      - name: to
        in: query
        required: false
        schema:
          type: string
          format: date
      x-curl: 'curl -s ''https://uplms-api.staging.upbase.asia/ops/api/v1/gamification/achievement-history?page_index=1&page_size=20'' -H ''Authorization: Bearer <auth-value>'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    type: object
                    required:
                    - items
                    - metadata
                    properties:
                      items:
                        type: array
                        items:
                          $ref: '#/components/schemas/AchievementLogItem'
                      metadata:
                        $ref: S-01#/components/schemas/PaginationMeta
        '401':
          $ref: S-01#/components/responses/Unauthorized
        '403':
          $ref: S-01#/components/responses/Forbidden
        '422':
          $ref: S-01#/components/responses/ValidationError
components:
  schemas:
    AchievementLogItem:
      type: object
      required:
      - id
      - occurred_at
      - learner
      - event_type
      - details
      properties:
        id:
          type: string
          format: uuid
        occurred_at:
          type: string
          format: date-time
        learner:
          $ref: S-01#/components/schemas/Learner
        event_type:
          type: string
          enum:
          - POINT
          - BADGE
          - LEVEL
        point_source:
          $ref: S-01#/components/schemas/ActionCode
        points:
          type: integer
          nullable: true
          description: 0 vẫn trả (BR-22.1a); null với BADGE, LEVEL
        details:
          type: object
          description: Dữ liệu để FE dựng chuỗi Details (US22)
          properties:
            object_name:
              type: string
              nullable: true
              description: Tên lúc ghi (BR-3.11)
            course_name:
              type: string
              nullable: true
            streak_day:
              type: integer
              nullable: true
            badge_name:
              type: string
              nullable: true
            milestone:
              type: integer
              nullable: true
            badge_type:
              $ref: S-01#/components/schemas/BadgeType
            level:
              type: integer
              nullable: true
```

## C-10 Danh sách học viên và hạng + export

US12. Export trả JSON, ops-fe dựng xlsx (ADR-014; mẫu `apps/ops/src/users/users.controller.ts:496`), tối đa 50.000 dòng (2.43 Q14).

```yaml
openapi: 3.0.3
info:
  title: Gamification learners (Ops)
  version: 1.0.0
  x-contract-id: C-10
  x-status: Agreed
  x-provider: lms-be ops · GamificationOpsDataApi
  x-consumer: ops-fe OpsLearnerListPage
  x-units: U14
servers:
- url: https://uplms-api.staging.upbase.asia/ops/api/v1
paths:
  /gamification/learners:
    get:
      operationId: get_gamification_learners
      summary: Danh sách học viên
      description: All time đọc UserStats; khoảng khác computeRange (cập nhật tức thì, BR-12.5). Loại Test Account, Block, rời (BR-12.3, BR-12.7). Mặc định sắp LEVEL DESC, Levels tắt thì POINTS DESC.
      x-permission:
        security:
        - group:
          - gamification_management
          name:
          - gr_view_gamification_learners
          display_name:
          - View gamification learners
          description:
          - Permission to view gamification learners, achievement history and campaign results
          isScan:
          - 'true'
        tags:
        - gr_view_gamification_learners
      parameters:
      - name: page_index
        in: query
        required: true
        schema:
          type: integer
          minimum: 1
      - name: page_size
        in: query
        required: true
        schema:
          type: integer
          minimum: 1
          maximum: 100
      - &id001
        name: search
        in: query
        required: false
        schema:
          type: string
        description: Tên học viên
      - &id002
        name: sort_by
        in: query
        required: false
        schema:
          type: string
          enum:
          - LEVEL
          - POINTS
          - BADGES
          - ACTIVITIES
          - COURSES
          - LAST_VISIT
          - NAME
      - &id003
        name: sort_type
        in: query
        required: false
        schema:
          type: string
          enum:
          - ASC
          - DESC
      - &id004
        name: range_code
        in: query
        required: false
        schema:
          type: string
          enum:
          - ALL_TIME
          - THIS_WEEK
          - THIS_MONTH
          - THIS_QUARTER
          - THIS_YEAR
          - CUSTOM
      - &id005
        name: from
        in: query
        required: false
        schema:
          type: string
          format: date
        description: Bắt buộc khi CUSTOM
      - &id006
        name: to
        in: query
        required: false
        schema:
          type: string
          format: date
      x-curl: 'curl -s ''https://uplms-api.staging.upbase.asia/ops/api/v1/gamification/learners?page_index=1&page_size=10&range_code=ALL_TIME'' -H ''Authorization: Bearer <auth-value>'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    type: object
                    required:
                    - items
                    - metadata
                    properties:
                      items:
                        type: array
                        items:
                          $ref: '#/components/schemas/LearnerRow'
                      metadata:
                        $ref: S-01#/components/schemas/PaginationMeta
        '401': &id007
          $ref: S-01#/components/responses/Unauthorized
        '403': &id008
          $ref: S-01#/components/responses/Forbidden
        '422': &id009
          $ref: S-01#/components/responses/ValidationError
  /gamification/learners/export:
    get:
      operationId: export_gamification_learners
      summary: Mọi dòng của bộ lọc hiện tại
      description: Không phân trang, tối đa 50.000 dòng; vượt → 400|630013.
      x-permission:
        security:
        - group:
          - gamification_management
          name:
          - gr_view_gamification_learners
          display_name:
          - View gamification learners
          description:
          - Permission to view gamification learners, achievement history and campaign results
          isScan:
          - 'true'
        tags:
        - gr_view_gamification_learners
      parameters:
      - *id001
      - *id002
      - *id003
      - *id004
      - *id005
      - *id006
      x-curl: 'curl -s ''https://uplms-api.staging.upbase.asia/ops/api/v1/gamification/learners/export?range_code=THIS_MONTH'' -H ''Authorization: Bearer <auth-value>'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    $ref: '#/components/schemas/LearnerRow'
        '400':
          description: 630013 vượt giới hạn export
          content:
            application/json:
              schema:
                $ref: S-01#/components/schemas/ErrorResponse
        '401': *id007
        '403': *id008
        '422': *id009
components:
  schemas:
    LearnerRow:
      type: object
      required:
      - learner
      - activities
      - courses
      properties:
        learner:
          $ref: S-01#/components/schemas/Learner
        level:
          type: integer
          nullable: true
          description: null khi Levels tắt hoặc chọn khoảng (BR-12.4, BR-12.6)
        points:
          type: integer
          nullable: true
        badges:
          type: integer
          nullable: true
          description: Loại đang bật (BR-9.10)
        activities:
          type: integer
        courses:
          type: integer
        last_visit_date:
          type: string
          format: date
          nullable: true
```

## C-11 Quản lý campaign

US20. Không có cờ Courses (2.43 Q6). Đang chạy chỉ lưu tên, trả `ignored_fields` (BR-20.10).

```yaml
openapi: 3.0.3
info:
  title: Gamification campaigns (Ops)
  version: 1.0.0
  x-contract-id: C-11
  x-status: Agreed
  x-provider: lms-be ops · CampaignOpsApi
  x-consumer: ops-fe OpsCampaignPanels
  x-units: U15
servers:
- url: https://uplms-api.staging.upbase.asia/ops/api/v1
paths:
  /gamification/campaigns:
    get:
      operationId: get_gamification_campaigns
      summary: Danh sách campaign
      description: Ba quyền đều đọc (2.43 Q1). Gamification tắt vẫn đọc (BR-15.8).
      x-permission:
        security:
        - group:
          - gamification_management
          name:
          - gr_view_gamification_settings
          display_name:
          - View gamification settings
          description:
          - Permission to view gamification settings
          isScan:
          - 'true'
        tags: &id004
        - gr_view_gamification_settings
        - gr_update_gamification_settings
        - gr_view_gamification_learners
      parameters:
      - name: page_index
        in: query
        required: true
        schema:
          type: integer
          minimum: 1
      - name: page_size
        in: query
        required: true
        schema:
          type: integer
          minimum: 1
          maximum: 100
      x-curl: 'curl -s ''https://uplms-api.staging.upbase.asia/ops/api/v1/gamification/campaigns?page_index=1&page_size=10'' -H ''Authorization: Bearer <auth-value>'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    type: object
                    required:
                    - items
                    - metadata
                    properties:
                      items:
                        type: array
                        items:
                          $ref: '#/components/schemas/Campaign'
                      metadata:
                        $ref: S-01#/components/schemas/PaginationMeta
        '401': &id001
          $ref: S-01#/components/responses/Unauthorized
        '403': &id002
          $ref: S-01#/components/responses/Forbidden
        '422': &id003
          $ref: S-01#/components/responses/ValidationError
    post:
      operationId: create_gamification_campaign
      summary: Tạo campaign
      description: Gamification tắt → 630001 (cùng mã cho POST, PUT, DELETE).
      x-permission:
        security:
        - group:
          - gamification_management
          name:
          - gr_update_gamification_settings
          display_name:
          - Update gamification settings
          description:
          - Permission to update gamification settings
          isScan:
          - 'true'
        tags:
        - gr_update_gamification_settings
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CampaignInput'
      x-curl: 'curl -s -X POST ''https://uplms-api.staging.upbase.asia/ops/api/v1/gamification/campaigns'' -H ''Authorization: Bearer <auth-value>'' -H ''Content-Type: application/json'' -d ''{"name":"Thi
        đua tháng 11","start_date":"2026-11-01","end_date":"2026-11-30","point_sources":["CHECKIN","ACTIVITY_COMPLETED"],"is_show_activity_board":true}'''
      responses:
        '201':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    $ref: '#/components/schemas/Campaign'
        '400':
          description: 630001; 630014 ngày không hợp lệ
          content:
            application/json:
              schema:
                $ref: S-01#/components/schemas/ErrorResponse
        '401': *id001
        '403': *id002
        '422': *id003
  /gamification/campaigns/{id}:
    get:
      operationId: get_gamification_campaign
      summary: Chi tiết
      description: ''
      x-permission:
        security:
        - group:
          - gamification_management
          name:
          - gr_view_gamification_settings
          display_name:
          - View gamification settings
          description:
          - Permission to view gamification settings
          isScan:
          - 'true'
        tags: *id004
      parameters:
      - name: id
        in: path
        required: true
        schema:
          type: string
          format: uuid
      x-curl: 'curl -s ''https://uplms-api.staging.upbase.asia/ops/api/v1/gamification/campaigns/<id>'' -H ''Authorization: Bearer <auth-value>'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    $ref: '#/components/schemas/Campaign'
        '404':
          description: Không thuộc tenant
          content:
            application/json:
              schema:
                $ref: S-01#/components/schemas/ErrorResponse
        '401': *id001
        '403': *id002
    put:
      operationId: update_gamification_campaign
      summary: Sửa theo trạng thái lúc lưu
      description: 'NOT_STARTED: mọi field. IN_PROGRESS: chỉ name, field khác bỏ và trả ignored_fields. Gamification tắt → 630001; EXPIRED → 630015 (BR-20.6, BR-20.10).'
      x-permission:
        security:
        - group:
          - gamification_management
          name:
          - gr_update_gamification_settings
          display_name:
          - Update gamification settings
          description:
          - Permission to update gamification settings
          isScan:
          - 'true'
        tags:
        - gr_update_gamification_settings
      parameters:
      - name: id
        in: path
        required: true
        schema:
          type: string
          format: uuid
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CampaignInput'
      x-curl: 'curl -s -X PUT ''https://uplms-api.staging.upbase.asia/ops/api/v1/gamification/campaigns/<id>'' -H ''Authorization: Bearer <auth-value>'' -H ''Content-Type: application/json'' -d ''{"name":"Thi
        đua tháng 11 - Đợt 2","start_date":"2026-11-01","end_date":"2026-11-30","point_sources":["CHECKIN"],"is_show_activity_board":true}'''
      responses:
        '200':
          description: 'OK; data = Campaign + ignored_fields: string[]'
        '400':
          description: 630001 Gamification tắt; 630015 campaign đã khoá
          content:
            application/json:
              schema:
                $ref: S-01#/components/schemas/ErrorResponse
        '404':
          description: Không thuộc tenant
          content:
            application/json:
              schema:
                $ref: S-01#/components/schemas/ErrorResponse
        '401': *id001
        '403': *id002
        '422': *id003
    delete:
      operationId: delete_gamification_campaign
      summary: Xoá campaign chưa bắt đầu
      description: Gamification tắt → 630001; đã bắt đầu → 630015.
      x-permission:
        security:
        - group:
          - gamification_management
          name:
          - gr_update_gamification_settings
          display_name:
          - Update gamification settings
          description:
          - Permission to update gamification settings
          isScan:
          - 'true'
        tags:
        - gr_update_gamification_settings
      parameters:
      - name: id
        in: path
        required: true
        schema:
          type: string
          format: uuid
      x-curl: 'curl -s -X DELETE ''https://uplms-api.staging.upbase.asia/ops/api/v1/gamification/campaigns/<id>'' -H ''Authorization: Bearer <auth-value>'''
      responses:
        '200':
          description: OK, data null
        '400':
          description: 630001; 630015
          content:
            application/json:
              schema:
                $ref: S-01#/components/schemas/ErrorResponse
        '404':
          description: Không thuộc tenant
          content:
            application/json:
              schema:
                $ref: S-01#/components/schemas/ErrorResponse
        '401': *id001
        '403': *id002
components:
  schemas:
    Campaign:
      type: object
      required:
      - id
      - name
      - start_date
      - end_date
      - point_sources
      - is_show_activity_board
      - status
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
          maxLength: 100
        start_date:
          type: string
          format: date
        end_date:
          type: string
          format: date
        point_sources:
          type: array
          minItems: 1
          items:
            $ref: S-01#/components/schemas/ActionCode
        is_show_activity_board:
          type: boolean
        status:
          type: string
          enum:
          - NOT_STARTED
          - IN_PROGRESS
          - EXPIRED
          description: Suy từ ngày theo múi giờ tenant (BR-20.3)
        current_points:
          type: array
          description: Số điểm hiện tại từng hành động, chỉ đọc (US20)
          items:
            type: object
            properties:
              source:
                $ref: S-01#/components/schemas/ActionCode
              points:
                type: integer
              is_enabled:
                type: boolean
    CampaignInput:
      type: object
      required:
      - name
      - start_date
      - end_date
      - point_sources
      - is_show_activity_board
      properties:
        name:
          type: string
          minLength: 1
          maxLength: 100
        start_date:
          type: string
          format: date
          description: ≥ ngày mai theo múi giờ tenant
        end_date:
          type: string
          format: date
          description: ≥ start_date
        point_sources:
          type: array
          minItems: 1
          items:
            $ref: S-01#/components/schemas/ActionCode
        is_show_activity_board:
          type: boolean
```

## C-12 Kết quả campaign + export

US21. Không có dòng You. Export mọi bảng, dòng đầu ghi chính thức hay tạm tính; ops-fe dựng xlsx mỗi bảng một sheet (ADR-014).

```yaml
openapi: 3.0.3
info:
  title: Gamification campaign results (Ops)
  version: 1.0.0
  x-contract-id: C-12
  x-status: Agreed
  x-provider: lms-be ops · GamificationOpsDataApi
  x-consumer: ops-fe OpsCampaignPanels
  x-units: U17
servers:
- url: https://uplms-api.staging.upbase.asia/ops/api/v1
paths:
  /gamification/campaigns/{id}/results:
    get:
      operationId: get_gamification_campaign_results
      summary: Một bảng của campaign
      description: Bảng ACTIVITIES chỉ có khi is_show_activity_board.
      x-permission:
        security:
        - group:
          - gamification_management
          name:
          - gr_view_gamification_learners
          display_name:
          - View gamification learners
          description:
          - Permission to view gamification learners, achievement history and campaign results
          isScan:
          - 'true'
        tags:
        - gr_view_gamification_learners
      parameters:
      - name: id
        in: path
        required: true
        schema:
          type: string
          format: uuid
      - name: category
        in: query
        required: true
        schema:
          type: string
          enum:
          - POINTS
          - ACTIVITIES
          - COURSES
      - name: page_index
        in: query
        required: true
        schema:
          type: integer
          minimum: 1
      - name: page_size
        in: query
        required: true
        schema:
          type: integer
          minimum: 1
          maximum: 100
      x-curl: 'curl -s ''https://uplms-api.staging.upbase.asia/ops/api/v1/gamification/campaigns/<id>/results?category=POINTS&page_index=1&page_size=50'' -H ''Authorization: Bearer <auth-value>'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    $ref: '#/components/schemas/CampaignResult'
        '404':
          description: Không thuộc tenant, chưa bắt đầu, hoặc bảng không có
          content:
            application/json:
              schema:
                $ref: S-01#/components/schemas/ErrorResponse
        '401': &id001
          $ref: S-01#/components/responses/Unauthorized
        '403': &id002
          $ref: S-01#/components/responses/Forbidden
        '422':
          $ref: S-01#/components/responses/ValidationError
  /gamification/campaigns/{id}/results/export:
    get:
      operationId: export_gamification_campaign_results
      summary: Mọi bảng, mọi dòng
      description: data = CampaignResult[] (một phần tử mỗi bảng, không có metadata).
      x-permission:
        security:
        - group:
          - gamification_management
          name:
          - gr_view_gamification_learners
          display_name:
          - View gamification learners
          description:
          - Permission to view gamification learners, achievement history and campaign results
          isScan:
          - 'true'
        tags:
        - gr_view_gamification_learners
      parameters:
      - name: id
        in: path
        required: true
        schema:
          type: string
          format: uuid
      x-curl: 'curl -s ''https://uplms-api.staging.upbase.asia/ops/api/v1/gamification/campaigns/<id>/results/export'' -H ''Authorization: Bearer <auth-value>'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    $ref: '#/components/schemas/CampaignResult'
        '404':
          description: ''
          content:
            application/json:
              schema:
                $ref: S-01#/components/schemas/ErrorResponse
        '401': *id001
        '403': *id002
components:
  schemas:
    CampaignResult:
      type: object
      required:
      - campaign_id
      - category
      - is_final
      - rows
      properties:
        campaign_id:
          type: string
          format: uuid
        category:
          type: string
          enum:
          - POINTS
          - ACTIVITIES
          - COURSES
        is_final:
          type: boolean
          description: true khi đã đóng băng (version 0)
        last_updated_at:
          type: string
          format: date-time
          nullable: true
          description: Tạm tính
        frozen_at:
          type: string
          format: date-time
          nullable: true
        rows:
          type: array
          items:
            $ref: S-01#/components/schemas/LeaderboardRow
        metadata:
          $ref: S-01#/components/schemas/PaginationMeta
```

## C-13 Thông tin gamification của tôi

US1. 404 khi tắt hoặc Test Account là tín hiệu ẩn toàn bộ (BR-1.1). lms chưa có `@ApiOperation` (`apps/lms/src/courses/courses.controller.ts:132-139`) → khai operationId để Swagger có tên. Field ẩn theo cờ vẫn trả giá trị; FE ẩn (BR-1.8).

```yaml
openapi: 3.0.3
info:
  title: Gamification me (lms)
  version: 1.0.0
  x-contract-id: C-13
  x-status: Agreed
  x-provider: lms-be lms · LearnerGamificationApi
  x-consumer: lms-fe
  x-units: U5
servers:
- url: https://uplms-api.staging.upbase.asia/lms/api/v1
paths:
  /gamification/me:
    get:
      operationId: get_my_gamification
      summary: Điểm, hạng, chuỗi, số huy hiệu, cờ hiển thị
      description: LmsGuard. Đọc UserStats, không tính lại (US1 NFR).
      x-curl: 'curl -s ''https://uplms-api.staging.upbase.asia/lms/api/v1/gamification/me'' -H ''Authorization: Bearer <auth-value>'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    $ref: '#/components/schemas/GamificationMe'
        '401':
          $ref: S-01#/components/responses/Unauthorized
        '404':
          $ref: S-01#/components/responses/GamificationNotAvailable
components:
  schemas:
    GamificationMe:
      type: object
      required:
      - features
      - timezone
      - today
      - points
      - level
      - streak
      - badges
      properties:
        features:
          type: object
          required:
          - points
          - checkin
          - badges
          - levels
          - leaderboard
          description: Cờ ẩn hiện từng thành phần (BR-1.8)
          properties:
            points:
              type: boolean
            checkin:
              type: boolean
            badges:
              type: boolean
            levels:
              type: boolean
            leaderboard:
              type: boolean
        boards:
          type: array
          items:
            $ref: S-01#/components/schemas/BoardCategory
          description: Bảng đang chạy (bật ở US11 và không khoá, BR-11.4), theo thứ tự POINTS, ACTIVITIES, COURSES, BADGES, LEVEL (US6). Rỗng khi Leaderboard tắt. FE tự bỏ BADGES, LEVEL khi khung khác ALL_TIME
            (BR-6.2b)
        default_board:
          $ref: S-01#/components/schemas/BoardCategory
          nullable: true
          description: POINTS nếu đang chạy, không thì bảng đầu của boards (US6, BR-11.3)
        timezone:
          type: string
          example: Asia/Ho_Chi_Minh
        today:
          type: string
          format: date
          description: Ngày hiện tại theo múi giờ tenant, cho khoá check-in phía client (ADR-010)
        points:
          type: integer
        level:
          type: integer
        streak:
          type: integer
        badges:
          type: integer
          description: Loại đang bật (BR-9.10)
```

## C-14 Quy ước cho hai panel How to

US1 panel How to collect points, How to level up.

```yaml
openapi: 3.0.3
info:
  title: Gamification rules (lms)
  version: 1.0.0
  x-contract-id: C-14
  x-status: Agreed
  x-provider: lms-be lms · LearnerGamificationApi
  x-consumer: lms-fe
  x-units: U5
servers:
- url: https://uplms-api.staging.upbase.asia/lms/api/v1
paths:
  /gamification/rules:
    get:
      operationId: get_gamification_rules
      summary: Bảng điểm và tiêu chí đang chạy
      description: ''
      x-curl: 'curl -s ''https://uplms-api.staging.upbase.asia/lms/api/v1/gamification/rules'' -H ''Authorization: Bearer <auth-value>'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    $ref: '#/components/schemas/GamificationRules'
        '401':
          $ref: S-01#/components/responses/Unauthorized
        '404':
          $ref: S-01#/components/responses/GamificationNotAvailable
components:
  schemas:
    GamificationRules:
      type: object
      properties:
        point_rules:
          type: array
          items:
            type: object
            properties:
              source:
                $ref: S-01#/components/schemas/ActionCode
              points:
                type: integer
              checkin_cap:
                type: integer
                nullable: true
          description: Chỉ hành động đang bật (US1 panel)
        level_criteria:
          type: array
          items:
            type: object
            properties:
              category:
                $ref: S-01#/components/schemas/LevelCriterion
              multiplier:
                type: integer
          description: Chỉ tiêu chí đang chạy (BR-10.7)
```

## C-15 My Learning thêm field gamification

Endpoint có sẵn `GET /courses/my-learnings` (`apps/lms/src/courses/courses.controller.ts:132-139`, service `courses.service.ts:190-273` trả `{last_login, course_count, test_count}`, không có DTO). Thêm `gamification` (additive).

```yaml
openapi: 3.0.3
info:
  title: My learnings + gamification (lms)
  version: 1.0.0
  x-contract-id: C-15
  x-status: Agreed
  x-provider: lms-be lms (có sẵn)
  x-consumer: lms-fe
  x-units: U5
servers:
- url: https://uplms-api.staging.upbase.asia/lms/api/v1
x-backward-compatibility: 'Additive: thêm field gamification, null khi không hiển thị'
paths:
  /courses/my-learnings:
    get:
      operationId: get_my_learnings
      summary: Thêm gamification {points, level}
      description: gamification = null khi Gamification/Visibility tắt hoặc Test Account; points null khi Points tắt, level null khi Levels tắt (BR-1.8).
      x-curl: 'curl -s ''https://uplms-api.staging.upbase.asia/lms/api/v1/courses/my-learnings'' -H ''Authorization: Bearer <auth-value>'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              example:
                success: true
                data:
                  last_login: '2026-10-13T01:00:00.000Z'
                  course_count: 2/5
                  test_count: 1/3
                  gamification:
                    points: 475
                    level: 3
        '401':
          $ref: S-01#/components/responses/Unauthorized
```

## C-16 Check-in

ADR-010. Endpoint chỉ publish A-02 rồi `SET NX`; không chờ consumer. Gọi lặp trong ngày → 202, không làm gì.

```yaml
openapi: 3.0.3
info:
  title: Gamification check-in (lms)
  version: 1.0.0
  x-contract-id: C-16
  x-status: Agreed
  x-provider: lms-be lms · CheckinService
  x-consumer: lms-fe LmsCheckinTrigger
  x-units: U2
servers:
- url: https://uplms-api.staging.upbase.asia/lms/api/v1
paths:
  /gamification/check-in:
    post:
      operationId: create_gamification_checkin
      summary: Báo học viên vừa thao tác thật
      description: Không body. Bỏ qua (vẫn 202) khi Gamification tắt, Test Account, hoặc đã check-in hôm nay. Publish lỗi → ghi FailedEvent kind=CHECKIN, không đặt khoá, vẫn 202 (BR-5.11). Không trả 404
        để không lộ trạng thái.
      x-curl: 'curl -s -X POST ''https://uplms-api.staging.upbase.asia/lms/api/v1/gamification/check-in'' -H ''Authorization: Bearer <auth-value>'''
      responses:
        '202':
          description: Đã nhận, data null
        '401':
          $ref: S-01#/components/responses/Unauthorized
```

## C-17 Lịch sử ghi nhận của tôi

US3. 20 mục mỗi lần (2.43 Q11). Chỉ dòng điểm > 0, ẩn theo chức năng (BR-3.1a, BR-3.10).

```yaml
openapi: 3.0.3
info:
  title: Gamification my history (lms)
  version: 1.0.0
  x-contract-id: C-17
  x-status: Agreed
  x-provider: lms-be lms · LearnerGamificationApi
  x-consumer: lms-fe
  x-units: U7
servers:
- url: https://uplms-api.staging.upbase.asia/lms/api/v1
paths:
  /gamification/me/history:
    get:
      operationId: get_my_gamification_history
      summary: Lịch sử, mới nhất trước
      description: ''
      parameters:
      - name: page_index
        in: query
        required: true
        schema:
          type: integer
          minimum: 1
      - name: page_size
        in: query
        required: true
        schema:
          type: integer
          minimum: 1
          maximum: 100
      x-curl: 'curl -s ''https://uplms-api.staging.upbase.asia/lms/api/v1/gamification/me/history?page_index=1&page_size=20'' -H ''Authorization: Bearer <auth-value>'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    type: object
                    required:
                    - items
                    - metadata
                    properties:
                      items:
                        type: array
                        items:
                          $ref: '#/components/schemas/HistoryItem'
                      metadata:
                        $ref: S-01#/components/schemas/PaginationMeta
        '401':
          $ref: S-01#/components/responses/Unauthorized
        '404':
          $ref: S-01#/components/responses/GamificationNotAvailable
        '422':
          $ref: S-01#/components/responses/ValidationError
components:
  schemas:
    HistoryItem:
      type: object
      required:
      - id
      - occurred_at
      - event_type
      properties:
        id:
          type: string
          format: uuid
        occurred_at:
          type: string
          format: date-time
        event_type:
          type: string
          enum:
          - POINT
          - BADGE
          - LEVEL
        point_source:
          $ref: S-01#/components/schemas/ActionCode
        points:
          type: integer
          minimum: 1
        streak_day:
          type: integer
          nullable: true
        object_name:
          type: string
          nullable: true
          description: Tên lúc ghi (BR-3.11)
        course_name:
          type: string
          nullable: true
        badge:
          type: object
          nullable: true
          properties:
            name:
              type: string
            milestone:
              type: integer
            type:
              $ref: S-01#/components/schemas/BadgeType
        level:
          type: integer
          nullable: true
```

## C-18 Bộ huy hiệu của tôi

US4. Badges tắt → 404 riêng của tab (lms-fe ẩn tab).

```yaml
openapi: 3.0.3
info:
  title: Gamification my badges (lms)
  version: 1.0.0
  x-contract-id: C-18
  x-status: Agreed
  x-provider: lms-be lms · LearnerGamificationApi
  x-consumer: lms-fe
  x-units: U9
servers:
- url: https://uplms-api.staging.upbase.asia/lms/api/v1
paths:
  /gamification/me/badges:
    get:
      operationId: get_my_gamification_badges
      summary: Mọi mốc của loại đang bật
      description: ''
      x-curl: 'curl -s ''https://uplms-api.staging.upbase.asia/lms/api/v1/gamification/me/badges'' -H ''Authorization: Bearer <auth-value>'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    $ref: '#/components/schemas/MyBadges'
        '401':
          $ref: S-01#/components/responses/Unauthorized
        '404':
          $ref: S-01#/components/responses/GamificationNotAvailable
components:
  schemas:
    MyBadges:
      type: object
      properties:
        badge_types:
          type: array
          items:
            type: object
            properties:
              type:
                $ref: S-01#/components/schemas/BadgeType
              earned_count:
                type: integer
              total:
                type: integer
                example: 8
              badges:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: string
                      format: uuid
                    milestone:
                      type: integer
                    name:
                      type: string
                    description:
                      type: string
                      nullable: true
                    image_url:
                      type: string
                    is_earned:
                      type: boolean
          description: Chỉ loại đang bật (BR-4.4); không có ngày đạt (BR-4.2)
```

## C-19 Bảng xếp hạng

US6. Đọc snapshot theo con trỏ (ADR-018). LEVEL, BADGES chỉ ALL_TIME (BR-6.2b) → khác thì 422. Bảng tắt/khoá → 404|630016 (khác 630012 = cả tính năng không có). Danh sách bảng đang chạy lấy ở C-13 `boards`.

```yaml
openapi: 3.0.3
info:
  title: Gamification leaderboard (lms)
  version: 1.0.0
  x-contract-id: C-19
  x-status: Agreed
  x-provider: lms-be lms · LearnerGamificationApi + LeaderboardService
  x-consumer: lms-fe
  x-units: U11
servers:
- url: https://uplms-api.staging.upbase.asia/lms/api/v1
paths:
  /gamification/leaderboard:
    get:
      operationId: get_gamification_leaderboard
      summary: Một bảng theo khung
      description: Phân trang cho Show All; trang 1 page_size 5 cho phần mặc định.
      parameters:
      - name: category
        in: query
        required: true
        schema:
          type: string
          enum:
          - POINTS
          - ACTIVITIES
          - COURSES
          - BADGES
          - LEVEL
      - name: range_code
        in: query
        required: true
        schema:
          type: string
          enum:
          - ALL_TIME
          - THIS_WEEK
          - THIS_MONTH
          - THIS_QUARTER
          - THIS_YEAR
        description: Khung cố định (BR-6.3, BR-6.16 tuần từ thứ Hai, múi giờ tenant). Không có from/to (BR-6.15)
      - name: page_index
        in: query
        required: true
        schema:
          type: integer
          minimum: 1
      - name: page_size
        in: query
        required: true
        schema:
          type: integer
          minimum: 1
          maximum: 100
      x-curl: 'curl -s ''https://uplms-api.staging.upbase.asia/lms/api/v1/gamification/leaderboard?category=POINTS&range_code=ALL_TIME&page_index=1&page_size=5'' -H ''Authorization: Bearer <auth-value>'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    $ref: '#/components/schemas/Board'
        '401':
          $ref: S-01#/components/responses/Unauthorized
        '404':
          $ref: S-01#/components/responses/GamificationNotAvailable
        '422':
          $ref: S-01#/components/responses/ValidationError
components:
  schemas:
    Board:
      type: object
      required:
      - category
      - rows
      - last_updated_at
      properties:
        category:
          $ref: S-01#/components/schemas/BoardCategory
        date_range:
          type: object
          properties:
            from:
              type: string
              format: date
            to:
              type: string
              format: date
          description: Hiện khoảng ngày của khung (US6)
        last_updated_at:
          type: string
          format: date-time
          nullable: true
        rows:
          type: array
          items:
            $ref: S-01#/components/schemas/LeaderboardRow
        metadata:
          $ref: S-01#/components/schemas/PaginationMeta
```

## C-20 Vị trí của tôi

US7. Một người dưới + khoảng cách người trên (BR-7.2). 404|630012 khi tính năng không có; 404|630016 khi bảng tắt/khoá.

```yaml
openapi: 3.0.3
info:
  title: Gamification my position (lms)
  version: 1.0.0
  x-contract-id: C-20
  x-status: Agreed
  x-provider: lms-be lms · LeaderboardService
  x-consumer: lms-fe
  x-units: U12
servers:
- url: https://uplms-api.staging.upbase.asia/lms/api/v1
paths:
  /gamification/leaderboard/me:
    get:
      operationId: get_my_gamification_position
      summary: Dòng của tôi theo bảng và khung
      description: ''
      parameters:
      - name: category
        in: query
        required: true
        schema:
          type: string
          enum:
          - POINTS
          - ACTIVITIES
          - COURSES
          - BADGES
          - LEVEL
      - name: range_code
        in: query
        required: true
        schema:
          type: string
          enum:
          - ALL_TIME
          - THIS_WEEK
          - THIS_MONTH
          - THIS_QUARTER
          - THIS_YEAR
        description: Khung cố định (BR-6.3, BR-6.16 tuần từ thứ Hai, múi giờ tenant). Không có from/to (BR-6.15)
      x-curl: 'curl -s ''https://uplms-api.staging.upbase.asia/lms/api/v1/gamification/leaderboard/me?category=POINTS&range_code=THIS_MONTH'' -H ''Authorization: Bearer <auth-value>'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    $ref: '#/components/schemas/MyPosition'
        '401':
          $ref: S-01#/components/responses/Unauthorized
        '404':
          $ref: S-01#/components/responses/GamificationNotAvailable
        '422':
          $ref: S-01#/components/responses/ValidationError
components:
  schemas:
    MyPosition:
      type: object
      properties:
        me:
          $ref: S-01#/components/schemas/LeaderboardRow
        below:
          $ref: S-01#/components/schemas/LeaderboardRow
        gap_to_above:
          type: object
          nullable: true
          properties:
            value:
              type: integer
            learner:
              $ref: S-01#/components/schemas/Learner
        in_top:
          type: boolean
          description: true khi trong 5 dòng đầu (BR-7.1)
```

## C-21 Campaign phía học viên

US19. Chưa bắt đầu không trả (404). Đang chạy: tạm tính; đã kết thúc: version 0 khi đã đóng băng (BR-19.6 nghiệm thu ở U17). Không chịu công tắc Show (US19).

```yaml
openapi: 3.0.3
info:
  title: Gamification campaigns (lms)
  version: 1.0.0
  x-contract-id: C-21
  x-status: Agreed
  x-provider: lms-be lms · LearnerGamificationApi + CampaignLeaderboard
  x-consumer: lms-fe
  x-units: U16, U17
servers:
- url: https://uplms-api.staging.upbase.asia/lms/api/v1
paths:
  /gamification/campaigns:
    get:
      operationId: get_gamification_campaigns_learner
      summary: Đang chạy rồi đã kết thúc
      description: Gamification/Visibility tắt hoặc Leaderboard tắt → 404|630012 (BR-19.1). Bảng POINTS khi Points tắt hoặc ACTIVITIES khi campaign không có → 404|630016.
      x-curl: 'curl -s ''https://uplms-api.staging.upbase.asia/lms/api/v1/gamification/campaigns'' -H ''Authorization: Bearer <auth-value>'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    $ref: '#/components/schemas/LearnerCampaign'
        '401': &id001
          $ref: S-01#/components/responses/Unauthorized
        '404': &id002
          $ref: S-01#/components/responses/GamificationNotAvailable
  /gamification/campaigns/{id}/leaderboard:
    get:
      operationId: get_gamification_campaign_leaderboard
      summary: Một bảng của campaign
      description: ''
      parameters:
      - name: id
        in: path
        required: true
        schema:
          type: string
          format: uuid
      - name: category
        in: query
        required: true
        schema:
          type: string
          enum:
          - POINTS
          - ACTIVITIES
          - COURSES
      - name: page_index
        in: query
        required: true
        schema:
          type: integer
          minimum: 1
      - name: page_size
        in: query
        required: true
        schema:
          type: integer
          minimum: 1
          maximum: 100
      x-curl: 'curl -s ''https://uplms-api.staging.upbase.asia/lms/api/v1/gamification/campaigns/<id>/leaderboard?category=COURSES&page_index=1&page_size=5'' -H ''Authorization: Bearer <auth-value>'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    $ref: C-12#/components/schemas/CampaignResult
        '401': *id001
        '404': *id002
        '422': &id003
          $ref: S-01#/components/responses/ValidationError
  /gamification/campaigns/{id}/leaderboard/me:
    get:
      operationId: get_my_gamification_campaign_position
      summary: Vị trí của tôi trong campaign
      description: ''
      parameters:
      - name: id
        in: path
        required: true
        schema:
          type: string
          format: uuid
      - name: category
        in: query
        required: true
        schema:
          type: string
          enum:
          - POINTS
          - ACTIVITIES
          - COURSES
      x-curl: 'curl -s ''https://uplms-api.staging.upbase.asia/lms/api/v1/gamification/campaigns/<id>/leaderboard/me?category=POINTS'' -H ''Authorization: Bearer <auth-value>'''
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                required:
                - success
                - data
                properties:
                  success:
                    type: boolean
                    enum:
                    - true
                  data:
                    $ref: C-20#/components/schemas/MyPosition
        '401': *id001
        '404': *id002
        '422': *id003
components:
  schemas:
    LearnerCampaign:
      type: object
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        start_date:
          type: string
          format: date
        end_date:
          type: string
          format: date
        status:
          type: string
          enum:
          - IN_PROGRESS
          - EXPIRED
        point_sources:
          type: array
          items:
            $ref: S-01#/components/schemas/ActionCode
        boards:
          type: array
          items:
            type: string
            enum:
            - POINTS
            - ACTIVITIES
            - COURSES
          description: POINTS bỏ khi Points tắt (BR-19.8)
        is_final:
          type: boolean
```

## A-01 Sự kiện ghi nhận (Kafka)

Đã có ở WP1; thêm `object_name`, `course_name` tuỳ chọn (additive).

```yaml
asyncapi: 2.6.0
info:
  title: Gamification record event
  version: 1.0.0
  x-contract-id: A-01
  x-status: Agreed
  x-provider: LearningFlowHooks qua GamificationRecordPublisher (lms, mock-test-service, ops)
  x-consumer: event-processor · GamificationEngine
  x-units: U1
x-existing:
  producer: 'lms-be origin/feature/gamification @9006b80: libs/modules/src/lib/gamification/engine/gamification-record.publisher.ts:23-33'
  consumer: 'lms-be origin/feature/gamification @9006b80: apps/event-processor-service/src/app/app.controller.ts:58-61, gamification-record.handler.ts:5-17'
  dto: 'lms-be origin/feature/gamification @9006b80: libs/interface/src/lib/gamification/engine/gamification-record.dto.ts:18-61'
  topic: 'lms-be origin/feature/gamification @9006b80: libs/constants/src/lib/kafka/kafka.constants.ts:73'
x-transport: kafka
x-message-key: user_id (thứ tự theo học viên)
x-version-policy: 'Không có field version (Q5): chỉ thêm field tuỳ chọn; consumer bỏ qua field lạ'
x-idempotency: Unique index ledger (class_user_id, point_source, point_object_id) WHERE POINT; badge (user_id, badge_id); level (user_id, level) — migration 1789997000000:276-282. Trùng → outcome DUPLICATE,
  không lỗi
x-failure-path: Publish lỗi → gamification_failed_events kind=RECORD PENDING (publisher:35-58). Engine lỗi → rollback, log GAMIFICATION_RECORD_FAILED, FailedEvent kind=RECORD (payload sai → GAVE_UP); cron
  15 phút chạy lại tối đa 5 lần (ADR-012, S-03)
x-duplicate-scenario: Cùng payload gửi hai lần → lần hai DUPLICATE, ledger và UserStats không đổi, không thông báo
channels:
  process_gamification_record:
    subscribe:
      operationId: handleGamificationRecord
      message:
        name: GamificationRecordPayload
        payload:
          type: object
          required:
          - action
          - user_id
          - occurred_at
          - tenant_id
          properties:
            action:
              $ref: S-01#/components/schemas/ActionCode
            user_id:
              type: string
              format: uuid
            occurred_at:
              type: string
              format: date-time
              description: Thời điểm gốc (BR-13.8, C11)
            tenant_id:
              type: string
              format: uuid
              description: KafkaService gắn (libs/modules/src/lib/kafka/kafka.service.ts:81-88)
            requestId:
              type: string
            class_user_id:
              type: string
              format: uuid
              description: Bắt buộc khi không phải CHECKIN
            object_type:
              type: string
              enum:
              - COURSE_SECTION
              - QUIZ
              - COURSE
            object_id:
              type: string
              format: uuid
            object_name:
              type: string
              description: 'MỚI, tuỳ chọn: tên nội dung lúc ghi (BR-3.11); thiếu thì engine tự tra'
            course_name:
              type: string
              description: MỚI, tuỳ chọn
            streak_day:
              type: integer
              minimum: 1
              description: Bắt buộc khi CHECKIN
            checkin_date:
              type: string
              format: date
              description: Bắt buộc khi CHECKIN
```

## A-02 Sự kiện check-in (Kafka)

DTO mới `GamificationCheckinPayload` ở `libs/interface` (design gốc design.md:276 đã đặt tên).

```yaml
asyncapi: 2.6.0
info:
  title: Gamification check-in event
  version: 1.0.0
  x-contract-id: A-02
  x-status: Agreed
  x-provider: lms · CheckinService endpoint
  x-consumer: event-processor · CheckinService consumer
  x-units: U2
x-existing:
  topic: 'lms-be origin/feature/gamification @9006b80: kafka.constants.ts:72 GAMIFICATION_CHECKIN (chưa có producer, consumer)'
x-transport: kafka
x-message-key: user_id
x-version-policy: Như A-01
x-idempotency: Unique gamification_checkins (user_id, checkin_date) (migration :305); trùng → bỏ qua, không gọi engine
x-failure-path: Publish lỗi → FailedEvent kind=CHECKIN PENDING, không SET NX (ADR-010); consumer lỗi → FailedEvent kind=CHECKIN; cron chạy lại gọi lại handler check-in (S-03 FailedEventStore)
x-duplicate-scenario: Hai thiết bị cùng gọi check-in → một bản ghi ngày, một dòng điểm (BR-13.6)
channels:
  process_gamification_checkin:
    subscribe:
      operationId: handleGamificationCheckin
      message:
        name: GamificationCheckinPayload
        payload:
          type: object
          required:
          - user_id
          - checkin_date
          - occurred_at
          - tenant_id
          properties:
            user_id:
              type: string
              format: uuid
            checkin_date:
              type: string
              format: date
              description: Ngày theo múi giờ tenant (BR-5.3), tính ở endpoint
            occurred_at:
              type: string
              format: date-time
            tenant_id:
              type: string
              format: uuid
            requestId:
              type: string
```

## A-03 Thông báo thành tích (socket.io)

Hạ tầng mới (ADR-008). lms-fe chưa có socket.io-client.

```yaml
asyncapi: 2.6.0
info:
  title: Gamification achievements socket
  version: 1.0.0
  x-contract-id: A-03
  x-status: Agreed
  x-provider: lms-be AchievementNotifier (gateway app lms; emit từ event-processor qua redis-emitter)
  x-consumer: lms-fe LmsAchievementRealtime
  x-units: U6
servers:
  lms:
    url: wss://uplms-api.staging.upbase.asia
    protocol: socket.io
    description: path /lms/socket.io, namespace /gamification (Q6)
x-auth: handshake auth.token = Bearer token như LmsGuard; sai → connect_error UNAUTHORIZED. Join room user:{user_id}
x-delivery: Chỉ khi đang kết nối (BR-2.1); không lưu, không gửi lại. Không emit khi lần chạy lại, trao bù, điểm 0, Visibility tắt, chức năng tắt (BR-2.4, BR-2.5, BR-2.10, BR-1.8)
x-duplicate-scenario: 'Nhiều tab: mỗi tab nhận; lms-fe dedupe theo item.id (toastDeduper)'
x-version-policy: Thêm type mới hoặc field tuỳ chọn là additive; lms-fe bỏ qua type lạ
channels:
  gamification:achievements:
    subscribe:
      operationId: onGamificationAchievements
      message:
        name: AchievementsBatch
        payload:
          type: object
          required:
          - items
          properties:
            items:
              type: array
              description: Theo thứ tự phát sinh, không gộp (BR-2.9)
              items:
                type: object
                required:
                - id
                - type
                - occurred_at
                properties:
                  id:
                    type: string
                    format: uuid
                    description: id dòng ledger
                  type:
                    type: string
                    enum:
                    - POINTS
                    - BADGE
                    - LEVEL
                  occurred_at:
                    type: string
                    format: date-time
                  points:
                    type: integer
                  point_source:
                    $ref: S-01#/components/schemas/ActionCode
                  streak_day:
                    type: integer
                  object_name:
                    type: string
                  badge:
                    type: object
                    properties:
                      name:
                        type: string
                      milestone:
                        type: integer
                      type:
                        $ref: S-01#/components/schemas/BadgeType
                      image_url:
                        type: string
                  level:
                    type: integer
```

## A-04 Việc trao bù huy hiệu (Kafka)

Topic mới `process_gamification_badge_backfill` ở `libs/constants`.

```yaml
asyncapi: 2.6.0
info:
  title: Gamification badge backfill job
  version: 1.0.0
  x-contract-id: A-04
  x-status: Agreed
  x-provider: ops · GamificationSettingsOpsApi (sau khi bật Badges/loại)
  x-consumer: event-processor · BadgeBackfill
  x-units: U8
x-transport: kafka
x-message-key: tenant_id
x-version-policy: Như A-01
x-idempotency: Unique (user_id, badge_id) WHERE BADGE → chạy lại không trao trùng; loại đã tắt lại khi tới lượt thì bỏ qua
x-failure-path: Lỗi một học viên → FailedEvent kind=BADGE_BACKFILL (payload {tenant_id, user_id, badge_types, requested_at}), tiếp lô; cron chạy lại gọi awardBackfill cho học viên đó. Publish lỗi → API
  vẫn 200, FailedEvent kind=BADGE_BACKFILL_JOB, cron publish lại A-04
x-duplicate-scenario: Bấm bật hai lần nhanh → hai message, lần hai không chèn thêm dòng
x-rerun: Gửi lại message cho tenant + badge_types (ghi ở runbook 3.6)
channels:
  process_gamification_badge_backfill:
    subscribe:
      operationId: handleGamificationBadgeBackfill
      message:
        name: BadgeBackfillPayload
        payload:
          type: object
          required:
          - tenant_id
          - badge_types
          - requested_at
          properties:
            tenant_id:
              type: string
              format: uuid
            badge_types:
              type: array
              items:
                $ref: S-01#/components/schemas/BadgeType
              description: Mọi loại đang bật khi bật Badges; một loại khi bật loại
            requested_at:
              type: string
              format: date-time
              description: Thời điểm đạt = lúc trao bù (BR-9.9)
            requestId:
              type: string
```

## S-02 Dữ liệu dùng chung giữa Unit

Chủ ghi và Unit đọc của từng bảng; chi tiết cột ở design.dbml và 3.1.

```yaml
x-contract-id: S-02
x-kind: shared-schema
x-status: Agreed
x-source: lms-be openspec/changes/upbase-221099-gamification/design.dbml + lms-be origin/feature/gamification @9006b80 migration 1789997000000
tables:
  gamification_achievement_history:
    owner: U1 (GamificationEngine)
    readers:
    - U4
    - U5
    - U7
    - U11
    - U14
    - U16
    - U17
    rule: Chỉ INSERT; thêm cột object_name_snapshot (U1, BR-3.11)
  gamification_user_stats:
    owner: U1
    readers:
    - U5
    - U9
    - U10
    - U11
    - U14
    rule: Ghi trong transaction engine, khoá FOR UPDATE; total_badges_acquired chỉ tăng (ADR-011)
  gamification_checkins:
    owner: U2 (CheckinService)
    readers:
    - U14 (last_visit_date)
  gamification_settings + 4 bảng cấu hình:
    owner: U0 (GamificationConfig)
    writers_by_block:
      chung: U0
      points: U3
      badges: U8
      levels: U10
      leaderboard: U13
    rule: Đọc qua cache, ghi qua Config; leaderboard_version chỉ đổi qua Config (ADR-018)
  gamification_leaderboard_snapshops:
    owner: U11 (LeaderboardComputation)
    readers:
    - U12
    - U13
    - U16
    - U17
    rule: version 0 = campaign đóng băng (U17 ghi qua LeaderboardComputation)
  gamification_campaigns:
    owner: U15
    readers:
    - U16
    - U17
  gamification_campaign_participants (mới):
    owner: U17 (CampaignLeaderboard)
    rule: ADR-017; migration mới có RLS
  gamification_failed_events:
    owner: U1 (FailedEventStore)
    readers:
    - U17 (điều kiện đóng băng)
    rule: Thêm cột kind (S-03) và occurred_at chép từ payload (additive, 3.1 U1, ADR-013); chỉ kind RECORD, CHECKIN tính cho điều kiện đóng băng
```

## S-03 Giao diện trong tiến trình giữa Unit

Các cạnh DAG không qua REST/Kafka (R-05) và định tuyến chạy lại theo loại lỗi (R-06).

```yaml
x-contract-id: S-03
x-kind: in-process
x-transport: in-process-sync
x-status: Agreed
x-note: Lời gọi trong cùng tiến trình giữa component của các Unit (TypeScript interface ở libs/modules/src/lib/gamification). Đổi chữ ký là breaking.
interfaces:
  GamificationEngine.record:
    units: U1 cung cấp; U2 (consumer check-in), FailedEventRetry gọi
    signature: 'record(payload: GamificationRecordPayloadDto, options?: {isRetry?: boolean}) => Promise<{status: RECORDED | SKIPPED | DUPLICATE | FAILED}>'
    existing: 'lms-be origin/feature/gamification @9006b80: gamification-engine.service.ts:44-47, gamification-record.types.ts:5-10'
    rule: 'Không throw ra ngoài (trừ khi chạy trong transaction của caller); isRetry: không emit, không ghi thêm FailedEvent'
  GamificationEngine.awardBackfill:
    units: U8 thêm (mới); BadgeBackfill gọi
    signature: 'awardBackfill(input: {tenant_id, user_id, badge_types: BadgeType[], requested_at: string}) => Promise<{awarded: number}>'
    rule: Chỉ Badge → Level handler, achieved_at = requested_at, không emit, không điểm (BR-9.9); tăng total_badges_acquired (ADR-011)
  AchievementNotifier.notify:
    units: U1 khai interface + adapter no-op; U6 thay bằng SocketIo adapter
    signature: 'notify(user_id: string, items: AchievementItem[]) => Promise<void>'
    rule: Gọi sau commit; lỗi nuốt và log, không ảnh hưởng ghi nhận (NFR-GAM-01). items = A-03 payload
  LeaderboardComputation.computeRange:
    units: U11 cung cấp; U14 (danh sách Ops khoảng tự do), U16, U17 (campaign) gọi
    signature: 'computeRange(category: BoardCategory, from: Date, to: Date, opts?: {point_sources?: ActionCode[], participant_ids?: string[]}) => Promise<LeaderboardRow[]>'
    rule: Một định nghĩa chỉ số (mục Định nghĩa chỉ số PRD); loại Test Account; Block/rời loại trừ khi không truyền participant_ids (ADR-017)
  LeaderboardComputation.writeSnapshot / switchVersion:
    units: U11 cung cấp; U16 (tạm tính), U17 (version 0) gọi
    signature: 'writeSnapshot(version: number, rows: LeaderboardRow[] (S-01), scope: {date_range_code, category: BoardCategory, campaign_id?}) ; switchVersion(v) → GamificationConfig.setLeaderboardVersion(v)
      (xoá cache, ADR-018)'
    rule: Chỉ LeaderboardComputation ghi bảng snapshot
  FailedEventStore.save / retry routing:
    units: U1 cung cấp; U2, U8 ghi; FailedEventRetry định tuyến
    signature: 'save({kind: RECORD | CHECKIN | BADGE_BACKFILL | BADGE_BACKFILL_JOB, payload, error_message}) ; cột mới kind (mặc định RECORD cho dòng WP1)'
    rule: 'Cron: RECORD → engine.record(isRetry); CHECKIN → handler check-in (A-02 payload); BADGE_BACKFILL → engine.awardBackfill; BADGE_BACKFILL_JOB → publish lại A-04. Tối đa 5 lần rồi GAVE_UP (ADR-012)'
```

## Contract ownership rules
- lms-be (provider) giữ mọi contract; BE lead ký, FE lead soi chéo phía consumer. Contract nằm ở store; lms-be không viết `api-contract.md` riêng.
- **Additive**: thêm field response, thêm field tuỳ chọn ở request, thêm field tuỳ chọn ở payload Kafka/socket (consumer bỏ qua field lạ). Sửa ở store qua PR, không cần mở lại stage.
- **Breaking**: đổi / xoá field, đổi mã lỗi, siết validation, đổi topic → mở lại 2.8 `[R]`, BE lead ký lại, Bolt đang làm `/opsx:update`.
- **Code thấy contract sai**: dừng, sửa ở store, BE lead ký lại.
- **Final**: sau 3.6 mỗi `x-curl` chạy trên staging; event kiểm bằng scenario trùng message.
- Mỗi contract REST mới cần scenario thành công, lỗi validation, không quyền, khác tenant ở spec của change `run` (lms-be `openspec/config.yaml` rules.specs); mỗi event cần scenario trùng message (`x-duplicate-scenario`).

## Open questions

| Contract | Question | Blocks |
|---|---|---|
| C-21, A-03 | Design campaign phía học viên chưa có (OQ-45): shape có thể thêm field khi có design (additive) | U16 (ui-map Provisional) |
| C-10 | Số dòng mỗi trang theo chuẩn Ops (`DEFAULT_PAGE_SIZE` = 10 ở ops-fe) | Không chặn |

## Nguồn thay thế đã dùng
- `requirements.md` không có mã NFR riêng: NFR lấy từ PRD + 2.43 Q14.
- Bằng chứng: lms-be `origin/feature/gamification` @9006b80 (WP0, WP3, WP1) và `origin/staging` cho quy ước chung.

Approved by - [GIẢ LẬP] Đoàn Quang Cường (BE lead), 2026-10-13
