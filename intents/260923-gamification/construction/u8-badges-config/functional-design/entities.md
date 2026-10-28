---
intent: 260923-gamification
unit: u8-badges-config
artifact: entities
stage: 3.1 functional-design
bolt: B09
version: 1.1
status: draft
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
consumes: unit-of-work.md v2.0 (U8), components.md v2.0, contract-summary.md v2.0 (C-05, C-06, C-07), PRD v0.14 US9
---
# Entities: U8 `u8-badges-config`

Technology-agnostic. Bảng, cột, migration cụ thể ở `../code-generation/code-generation-plan.md` (3.5). Bằng chứng "có sẵn" theo lms-be `origin/feature/gamification` @9006b80 (ADR-008).

FE focus: U8 **chỉ đọc và ghi** cấu hình huy hiệu (không sở hữu AchievementHistory, UserStats). Các entity dưới đây là những gì `OpsSettingsPage` khối Badges cần đọc/ghi qua API.

```yaml
entities:
  - name: GamificationSetting
    kind: entity
    status: existing (WP0/WP3), sửa (thêm badgesEnabled)
    description: "Cấu hình chung của tổ chức. U8 đọc/ghi `badges_enabled`."
    source: "libs/database/src/lib/entities/gamification/gamification-setting.entity.ts; gamification-config.service.ts:55"
    attributes:
      - {name: badgesEnabled, type: boolean, default: false, note: "Công tắc Badges toàn tổ chức (BR-9.6). API GET /gamification/badges trả badges_enabled; PATCH cập nhật."}

  - name: BadgeType
    kind: entity
    status: new (WP0 có bảng gamification_badge_types theo design.dbml)
    description: "Bốn loại huy hiệu cố định của tổ chức: CHECKIN, ACTIVITY, TEST, COURSE. Chỉ bật/tắt được, không tạo/xoá (BR-9.1)."
    source: "libs/database/src/lib/entities/gamification/gamification-badge-type.entity.ts (tạo mới)"
    attributes:
      - {name: type, type: enum, required: true, allowed: [CHECKIN, ACTIVITY, TEST, COURSE], note: "Chỉ đọc sau khi khởi tạo (BR-9.1)"}
      - {name: isEnabled, type: boolean, default: false, note: "Bật/tắt từng loại (BR-9.5). PATCH /gamification/badges {badge_type: {type, is_enabled}}"}
    constraints:
      - "Bốn bản ghi cố định mỗi tenant (BR-9.1); tạo ở seed 1789998000000"
      - "Tắt một loại → không trao huy hiệu loại đó, không hiện với học viên (BR-9.5)"
      - "Tắt Badges → tất cả loại ngừng trao, tiêu chí hạng BADGES bị khoá (BR-9.6, BR-10.7)"

  - name: Badge
    kind: entity
    status: new (WP0 có bảng gamification_badges theo design.dbml)
    description: "Mỗi mốc của một loại huy hiệu. Mốc là chỉ đọc; tên, hình, mô tả do vận hành đặt."
    source: "libs/database/src/lib/entities/gamification/gamification-badge.entity.ts (tạo mới)"
    attributes:
      - {name: milestone, type: integer, required: true, note: "Giá trị mốc do hệ thống định sẵn, không sửa (BR-9.2). 630004 nếu cố ghi."}
      - {name: defaultName, type: text, required: true, note: "Tên mặc định hệ thống đặt (BR-9.8); dùng khi name bị xoá trắng."}
      - {name: name, type: text, required: true, note: "Tên mốc vận hành có thể đổi (BR-9.3). Xoá trắng → quay về defaultName (BR-9.8). Max 255 ký tự (C-05)."}
      - {name: description, type: text, required: false, note: "Mô tả tuỳ chọn, hiện khi học viên hover ở US4."}
      - {name: imageResourceId, type: reference, required: true, references: Resource, note: "Trỏ ảnh trong ResourceLibrary; xoá ảnh → rơi về mặc định (BR-1.7). Định dạng: .png/.jpg/.jpeg/.webp/.svg ≤ 1MB (C-05, 2.43 Q12)."}
    constraints:
      - "Mỗi BadgeType có đúng 8 mốc theo dãy cố định (BR-9.2)"
      - "Milestone không sửa được; chỉ name, description, imageResourceId thay đổi được (BR-9.3)"
      - "Thay đổi tên/hình áp ngay cho mọi học viên kể cả người đã đạt (BR-9.4)"

  - name: Resource
    kind: entity
    status: existing (ResourceLibrary), chỉ đọc
    description: "Kho tài nguyên dùng chung. U8 dùng để chọn hoặc tải ảnh cho từng mốc huy hiệu."
    source: "libs/database/src/lib/entities/resource/resource.entity.ts"
    attributes:
      - {name: url, type: url, note: "URL ảnh để render trực tiếp"}
      - {name: mimeType, type: text, note: "Kiểm định dạng trước khi upload"}
```

## Dữ liệu API (FE đọc/ghi)

| API | Method | FE dùng để | Contract |
|---|---|---|---|
| `GET /ops/api/v1/gamification/badges` | GET | Tải khối Badges: badges_enabled, 4 badge_types, 8 mốc mỗi loại | C-05 |
| `PATCH /ops/api/v1/gamification/badges` | PATCH | Bật/tắt badges_enabled hoặc bật/tắt một badge_type | C-05 |
| `PATCH /ops/api/v1/gamification/badges/{id}` | PATCH | Đổi name, description, image_resource_id của một mốc | C-05 |

## Tóm tắt
- **FE không sở hữu entity nào** — đọc/ghi qua GamificationSettingsOpsApi.
- **Mới**: BadgeType, Badge (WP0 có bảng theo design.dbml nhưng chưa có entity TypeORM).
- **Sửa**: GamificationSetting thêm `badges_enabled`.
- **Cố định**: 4 loại × 8 mốc = 32 Badge mỗi tenant, tạo ở seed.
