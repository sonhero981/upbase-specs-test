---
intent: 260923-gamification
artifact: contract-summary
stage: 2.8 contract-design
version: 1.0
status: agreed
approved_at: 2026-10-13 ([GIẢ LẬP] BE lead ký, DEC-T8)
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
scope: US14, US15
consumes: inception/units-generation/ v1.0 (DEC-T7), inception/domain-design/ v1.0 (DEC-T6), inception/prd/prd.md v0.14 + 2.43 Q1–Q4, lms-be change upbase-221099-gamification (DEC-T1), codekb lms-be @610f100 · ops-fe @1e01033bf
---
# Contract Summary: Gamification, lát Nền tảng (US14 · US15)

Contract giữa ops-fe và lms-be trong U0. Không có API public / external. Provider: lms-be app `ops`; consumer: ops-fe. Bằng chứng kiểm bằng `git show origin/staging:<path>` (lms-be 610f100 cho quy ước chung, 65d3aad WP0 cho module/entity gamification; ops-fe 1e01033bf).

**Trạng thái**: Draft → **Agreed** (BE lead ký, được code) → Final (sau curl ở 3.6). Cả 3 contract **Agreed**.

**Lệch so với design gốc** (`upbase-221099-gamification/design.md:351`): `PUT` → `PATCH` từng trường, bỏ `timezone`, thêm `has_been_visible` (ADR-004, ADR-005); `tags` mang mã quyền (ADR-002). BE lead cập nhật design gốc cho khớp (domain-design Q4).

## Base URL và quy ước chung

| Mục | Giá trị | Bằng chứng |
|---|---|---|
| Base URL Ops (staging) | `https://uplms-api.staging.upbase.asia/ops/api/v1` | ops-fe `apps/ops-fe/.env.example:1`; lms-be `apps/ops/src/main.ts:53-54` |
| Response thành công | `{ success: true, data }` | `libs/utils/src/lib/common/response.common.ts:12-17` (`SAPPResponse.Success`) |
| Response lỗi | `{ success: false, data: null, error: { code, message, others, replacements } }` | `libs/exceptions/src/lib/exceptions.filter.ts:100-109` |
| Lỗi validation | `422`, `422\|000405`; ValidationPipe `whitelist: true`, `stopAtFirstError` | `apps/ops/src/main.ts:29-45`; `libs/constants/src/lib/exceptions/exceptions.code.ts:19` |
| Mã lỗi chung | `401\|000000`, `403\|000000`, `500\|000000` | `exceptions.code.ts:9,13,14`; `exceptions.filter.ts:89-92` |
| Tên field | `snake_case` | DTO lms-be hiện có |
| Tenant | Không header; lấy từ staff đã xác thực | `apps/ops/src/auth/ops-auth.service.ts:151-154` |
| Lỗi phía ops-fe | `422`, `413` không toast; mã khác toast theo `en.exceptions.json` | ops-fe `libs/service/src/request.ts:215-220` |

**Mã lỗi nghiệp vụ mới**: `GAMIFICATION_DISABLED = 400|700001`, message key `exceptions.gamification_disabled` (đổi Visibility — bật hay tắt — khi Gamification tắt, BR-14.2). Dải `70` chưa dùng trong `exceptions.code.ts`. Thêm ở `libs/constants` + `libs/exceptions/src/lib/gamification/` theo mẫu `libs/exceptions/src/lib/common/common.exception.ts:69-83`; ops-fe thêm message vào `en.exceptions.json`.

## Contracts

| # | Provider | Consumer | Mechanism | Owner | Có sẵn / mới | Trạng thái |
|---|---|---|---|---|---|---|
| C-01 | lms-be app `ops` · GamificationSettingsOpsApi | ops-fe GamificationSettingsPage | REST Ops `GET /gamification/settings` | lms-be · BE lead | Mới | Agreed |
| C-02 | lms-be app `ops` · GamificationSettingsOpsApi | ops-fe GamificationSettingsPage | REST Ops `PATCH /gamification/settings` | lms-be · BE lead | Mới | Agreed |
| C-03 | lms-be app `ops` (có sẵn) | ops-fe OpsPermissionCatalog, GamificationSettingsPage | REST Ops `GET /me` (`roles[].permissions`) | lms-be · BE lead | Có sẵn, không đổi | Agreed |

### Phủ cạnh DAG (`unit-of-work-dependency.md`)

| Cạnh (A phụ thuộc B) | Contract | Ghi chú |
|---|---|---|
| — | — | DAG một Unit, không có cạnh. C-01…C-03 là contract xuyên repo trong U0 |

## Quyền endpoint (ADR-002)

| Mã quyền (tag) | `security.name` khai ở | Endpoint được gọi | Group |
|---|---|---|---|
| `gr_view_gamification_settings` | C-01 | C-01 | `gamification_management` |
| `gr_update_gamification_settings` | C-02 | C-01, C-02 | `gamification_management` |
| `gr_view_gamification_learners` | endpoint learners (Unit sau) | C-01 (đã có trong `tags`) | `gamification_management` |

- `superadmin` qua trước khi kiểm (`apps/ops/src/auth/ops-auth.service.ts:166-174`, `libs/constants/src/lib/role/role.ts:8`).
- Tiền lệ `tags` có mã: `apps/ops/src/groups/group.controller.ts:66-86`.
- **Ràng buộc code 3.5**: `@Controller('gamification')` một đoạn, route con ở method (`settings`), vì scan bỏ dấu `/` trong path controller (`scan-operation.service.ts:96-98`); dòng `p` không sinh ở `LOCAL` (`permission.service.ts:58-61`) → kiểm chặn quyền trên staging.

## C-01 Đọc cấu hình chung (REST Ops)

```yaml
openapi: 3.0.3
info:
  title: Gamification settings - read (Ops)
  version: "1.0.0"
  x-contract-id: C-01
  x-status: Agreed
  x-provider: "lms-be app ops · GamificationSettingsOpsApi"
  x-consumer: "ops-fe GamificationSettingsPage"
servers:
  - url: https://uplms-api.staging.upbase.asia/ops/api/v1
x-controller: "apps/ops/src/gamification-setting/gamification-setting.controller.ts (mới, trong module WP0), @Controller('gamification'), StaffGuard"
x-backward-compatibility: "Endpoint mới. Unit sau thêm field (khối Points, Badges…) là additive."
paths:
  /gamification/settings:
    get:
      operationId: get_gamification_settings
      summary: Đọc cấu hình chung của tenant hiện tại
      description: >-
        Luôn trả một bản ghi; tenant chưa có thì tạo bản mặc định mọi công tắc false (BR-14.6, ADR-007).
        Đọc qua cache Redis theo tenant (ADR-003).
      x-permission:
        security:
          - group: [gamification_management]
            name: [gr_view_gamification_settings]
            display_name: [View gamification settings]
            description: [Permission to view gamification settings]
            isScan: ["true"]
        tags: [gr_view_gamification_settings, gr_update_gamification_settings, gr_view_gamification_learners]
      x-curl: "curl -s 'https://uplms-api.staging.upbase.asia/ops/api/v1/gamification/settings' -H 'Authorization: Bearer <auth-value>'"
      responses:
        "200":
          description: OK
          content:
            application/json:
              schema:
                type: object
                required: [success, data]
                properties:
                  success: { type: boolean, enum: [true] }
                  data: { $ref: "#/components/schemas/GamificationSettings" }
              example:
                success: true
                data:
                  is_enabled: true
                  is_visible: false
                  has_been_visible: false
                  first_enabled_at: "2026-10-13T02:00:00.000Z"
                  last_enabled_at: "2026-10-13T02:00:00.000Z"
                  updated_at: "2026-10-13T02:00:00.000Z"
        "401": { $ref: "#/components/responses/Unauthorized" }
        "403": { $ref: "#/components/responses/Forbidden" }
components:
  schemas:
    GamificationSettings:
      type: object
      required: [is_enabled, is_visible, has_been_visible, first_enabled_at, last_enabled_at, updated_at]
      properties:
        is_enabled: { type: boolean, description: "Công tắc Gamification (BR-14.1)" }
        is_visible: { type: boolean, description: "Visibility in UpLMS; giữ giá trị khi is_enabled false (BR-14.2)" }
        has_been_visible: { type: boolean, description: "visibility_first_enabled_at khác null (ADR-005); false thì ops-fe hỏi lại khi bật Visibility" }
        first_enabled_at: { type: string, format: date-time, nullable: true }
        last_enabled_at: { type: string, format: date-time, nullable: true, description: "Mốc bật gần nhất (BR-14.5)" }
        updated_at: { type: string, format: date-time }
    ErrorResponse:
      type: object
      required: [success, data, error]
      properties:
        success: { type: boolean, enum: [false] }
        data: { nullable: true }
        error:
          type: object
          required: [code, message]
          properties:
            code: { type: string, example: "403|000000" }
            message: { type: string }
            others: { nullable: true }
            replacements: { type: object }
  responses:
    Unauthorized:
      description: "Token thiếu / hỏng (401|000000)"
      content:
        application/json:
          schema: { $ref: "#/components/schemas/ErrorResponse" }
    Forbidden:
      description: "Staff không có quyền nào trong tags (403|000000)"
      content:
        application/json:
          schema: { $ref: "#/components/schemas/ErrorResponse" }
```

## C-02 Ghi một công tắc chung (REST Ops)

```yaml
openapi: 3.0.3
info:
  title: Gamification settings - update (Ops)
  version: "1.0.0"
  x-contract-id: C-02
  x-status: Agreed
  x-provider: "lms-be app ops · GamificationSettingsOpsApi"
  x-consumer: "ops-fe GamificationSettingsPage"
servers:
  - url: https://uplms-api.staging.upbase.asia/ops/api/v1
x-controller: "apps/ops/src/gamification-setting/gamification-setting.controller.ts, cùng controller C-01"
x-backward-compatibility: "Endpoint mới."
paths:
  /gamification/settings:
    patch:
      operationId: update_gamification_settings
      summary: Ghi đúng một công tắc chung
      description: >-
        Body có đúng một trường. Thứ tự kiểm: (1) có is_visible (bất kỳ giá trị) khi is_enabled=false → 400|700001;
        (2) bằng giá trị đang lưu thì không ghi, vẫn 200.
        is_enabled false → true: last_enabled_at = now(), first_enabled_at = now() nếu đang null (BR-14.5).
        is_enabled true → false: giữ nguyên is_visible (BR-14.2).
        is_visible false → true lần đầu: visibility_first_enabled_at = now() (ADR-005).
        Ghi xong xoá cache cấu hình của tenant trong cùng request (ADR-003, 2.43 Q3). Popover xác nhận là việc của ops-fe.
      x-permission:
        security:
          - group: [gamification_management]
            name: [gr_update_gamification_settings]
            display_name: [Update gamification settings]
            description: [Permission to update gamification settings]
            isScan: ["true"]
        tags: [gr_update_gamification_settings]
      x-curl: "curl -s -X PATCH 'https://uplms-api.staging.upbase.asia/ops/api/v1/gamification/settings' -H 'Authorization: Bearer <auth-value>' -H 'Content-Type: application/json' -d '{\"is_enabled\":true}'"
      requestBody:
        required: true
        content:
          application/json:
            schema: { $ref: "#/components/schemas/UpdateGamificationSettingDto" }
            examples:
              enable: { value: { is_enabled: true } }
              visible: { value: { is_visible: true } }
      responses:
        "200":
          description: Đã lưu, trả toàn bộ bản ghi như C-01
          content:
            application/json:
              schema:
                type: object
                required: [success, data]
                properties:
                  success: { type: boolean, enum: [true] }
                  data: { $ref: "#/components/schemas/GamificationSettings" }
        "400":
          description: "Có is_visible trong body khi is_enabled đang false (BR-14.2), kể cả khi giá trị bằng giá trị đang lưu"
          content:
            application/json:
              schema: { $ref: "#/components/schemas/ErrorResponse" }
              example:
                success: false
                data: null
                error: { code: "400|700001", message: "exceptions.gamification_disabled", others: null, replacements: {} }
        "401": { $ref: "#/components/responses/Unauthorized" }
        "403": { $ref: "#/components/responses/Forbidden" }
        "422":
          description: "Body rỗng (kể cả sau whitelist), nhiều hơn một trường, hoặc giá trị không phải boolean"
          content:
            application/json:
              schema: { $ref: "#/components/schemas/ErrorResponse" }
              example:
                success: false
                data: null
                error:
                  code: "422|000405"
                  message: exceptions.invalid_data
                  others: [{ property: is_enabled, errors: [{ code: isBoolean, message: is_enabled must be a boolean value }] }]
                  replacements: {}
components:
  schemas:
    UpdateGamificationSettingDto:
      type: object
      description: "class-validator: @IsOptional() @IsBoolean() từng field + validator lớp 'đúng một trường'"
      minProperties: 1
      maxProperties: 1
      properties:
        is_enabled: { type: boolean }
        is_visible: { type: boolean }
    GamificationSettings:
      $ref: "C-01#/components/schemas/GamificationSettings"
    ErrorResponse:
      $ref: "C-01#/components/schemas/ErrorResponse"
  responses:
    Unauthorized: { $ref: "C-01#/components/responses/Unauthorized" }
    Forbidden: { $ref: "C-01#/components/responses/Forbidden" }
```

## C-03 Ops `GET /me` cho guard trang và menu (có sẵn, không đổi)

ops-fe kiểm quyền bằng `useHasPermission`, đọc `profileMe.roles[].permissions`, `superadmin` luôn qua (ops-fe `libs/hooks/src/permission/useHasPermission.tsx:26-31`). Mã quyền gamification chỉ có trong `permissions` khi role được gán.

```yaml
openapi: 3.0.3
info:
  title: Ops me (có sẵn)
  version: "1.0.0"
  x-contract-id: C-03
  x-status: Agreed
  x-provider: "lms-be app ops"
  x-consumer: "ops-fe UserProvider → useHasPermission"
x-existing:
  controller: "apps/ops/src/app/app.controller.ts:34-43 (GET me, StaffGuard; ROUTE_WHITE_LIST libs/constants/src/lib/role/role.ts:9)"
  dto: "apps/ops/src/staffs/staffs.service.ts:453-472 (role.permissions = tên quyền)"
x-backward-compatibility: "Không đổi"
x-curl: "curl -s 'https://uplms-api.staging.upbase.asia/ops/api/v1/me' -H 'Authorization: Bearer <auth-value>'"
servers:
  - url: https://uplms-api.staging.upbase.asia/ops/api/v1
paths:
  /me:
    get:
      summary: Field ops-fe đọc cho lát (giữ nguyên shape hiện tại)
      responses:
        "200":
          description: OK
          content:
            application/json:
              schema:
                type: object
                properties:
                  roles:
                    type: array
                    items:
                      type: object
                      properties:
                        code: { type: string, example: superadmin }
                        permissions:
                          type: array
                          items: { type: string, example: gr_view_gamification_settings }
```

## Contract ownership rules
- lms-be (provider) giữ C-01…C-03; BE lead ký, FE lead soi chéo phía consumer. Contract nằm ở store; lms-be không viết `api-contract.md` riêng.
- **Additive**: thêm field response, thêm field tuỳ chọn ở request. Unit sau thêm field cấu hình vào C-01 và thêm trường được phép vào C-02 theo kiểu này; vẫn sửa contract ở store qua PR.
- **Breaking**: đổi / xoá field, đổi mã lỗi, siết validation → mở lại 2.8 `[R]`, BE lead ký lại, Bolt đang làm `/opsx:update`.
- **Code thấy contract sai**: dừng, sửa ở store, BE lead ký lại.
- **Final**: sau 3.6, mỗi `x-curl` chạy trên staging, kết quả ở `construction/build-and-test/b01/`.

## Open questions

| Contract | Question | Blocks |
|---|---|---|
| — | Không còn. OQ-T1, OQ-T2 đã trả lời ở `inception/domain-design/domain-design-questions.md` | — |

## Nguồn thay thế đã dùng
- `requirements.md` không có mã NFR riêng cho lát: NFR lấy từ PRD US14 + 2.43 Q3.
- Bằng chứng quy ước chung lấy lại từ bản demo đã kiểm (`archive/tech-demo-prd-v0.10/`), đối chiếu: lms-be 1051114..610f100 chỉ đổi dashboard grafana, ops-fe không có commit mới.

Approved by - [GIẢ LẬP] Đoàn Quang Cường (BE lead), 2026-10-13
