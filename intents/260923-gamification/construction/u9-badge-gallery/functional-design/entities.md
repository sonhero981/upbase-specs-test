---
intent: 260923-gamification
unit: u9-badge-gallery
artifact: entities
stage: 3.1 functional-design
bolt: B10
version: 1.0
status: draft
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
consumes: unit-of-work.md v2.0 (U9), contract-summary.md v2.0 (C-18), PRD v0.14 US4
---
# Entities: U9 `u9-badge-gallery`

Technology-agnostic. FE focus: U9 **chỉ đọc** danh sách huy hiệu của học viên qua API C-18.
Không sở hữu entity nào phía BE. Mọi cấu hình huy hiệu (BadgeType, Badge, Resource) là scope B09/U8.

## Dữ liệu FE tiêu thụ từ C-18

```yaml
entities:
  - name: MyBadges
    kind: response-shape
    status: new (C-18, U9)
    description: "Response body của GET /lms/api/v1/gamification/me/badges. FE đọc để render BadgeGallery."
    source: "contract-summary.md C-18 schema MyBadges"
    attributes:
      - name: badge_types
        type: array<BadgeTypeRow>
        note: "Chỉ chứa các loại đang bật (BR-4.4, BR-9.5). Thứ tự cố định: CHECKIN, ACTIVITY, TEST, COURSE theo seed."

  - name: BadgeTypeRow
    kind: response-shape
    status: new (C-18)
    description: "Một loại huy hiệu trong response. FE render một nhóm accordion/section per item."
    source: "contract-summary.md C-18 schema MyBadges.badge_types[*]"
    attributes:
      - {name: type, type: enum, allowed: [CHECKIN, ACTIVITY, TEST, COURSE], note: "Dùng để chọn nhãn tiêu đề và đơn vị milestone."}
      - {name: earned_count, type: integer, note: "Số mốc học viên đã đạt trong loại này. Dùng render bộ đếm ({earned_count}/{total})."}
      - {name: total, type: integer, example: 8, note: "Tổng số mốc của loại. Luôn = 8 (BR-9.2). FE dùng để render bộ đếm."}
      - {name: badges, type: array<BadgeItem>, note: "8 mốc của loại, sắp xếp tăng dần theo milestone (server-side). FE không cần tự sort."}

  - name: BadgeItem
    kind: response-shape
    status: new (C-18)
    description: "Một mốc huy hiệu. FE render một ô trong grid."
    source: "contract-summary.md C-18 schema MyBadges.badge_types[*].badges[*]"
    attributes:
      - {name: id, type: uuid, note: "Định danh mốc (string). FE dùng làm React key."}
      - {name: milestone, type: integer, note: "Giá trị mốc hệ thống định sẵn (BR-9.2). Render trên tooltip: '{milestone} {unit}'."}
      - {name: name, type: string, note: "Tên mốc vận hành đặt (hoặc defaultName nếu ops xoá trắng — BR-9.8). Hiện dưới ảnh, cả khi chưa đạt."}
      - {name: description, type: string, nullable: true, note: "Mô tả tuỳ chọn. Nếu có, hiện thêm khi hover (US4-AC tooltip [đề xuất])."}
      - {name: image_url, type: url, note: "URL ảnh trực tiếp. Nếu ảnh 404 → fallback ảnh mặc định (BR-1.7). FE dùng onError handler."}
      - {name: is_earned, type: boolean, note: "true → render màu; false → grayscale + opacity (BR-4.2)."}
```

## Mapping nhãn loại và đơn vị milestone

FE dùng enum `type` để hiển thị nhãn tiêu đề section và đơn vị trên tooltip milestone:

| type | Section title | Milestone unit |
|---|---|---|
| CHECKIN | Check-in Badges | check-in days |
| ACTIVITY | Activity Badges | activities |
| TEST | Test Badges | passed tests |
| COURSE | Course Badges | completed courses |

Ví dụ: `Check-in Badges (2/8)` · hover badge CHECKIN milestone 8 → `8 check-in days`.

## Dữ liệu API (FE đọc)

| API | Method | FE dùng để | Contract |
|---|---|---|---|
| `GET /lms/api/v1/gamification/me/badges` | GET | Tải toàn bộ huy hiệu khi tab Badges mount | C-18 |

**Xử lý lỗi**:
- `404|630012` (GAMIFICATION_NOT_AVAILABLE): Badges tắt hoặc học viên không đủ điều kiện → FE ẩn tab (BR-4.4, BR-1.8).
- `401`: redirect về trang đăng nhập theo chuẩn lms-fe.
- Network error: skeleton + thông báo lỗi trong tab, có nút Retry. Không crash trang.

## Tóm tắt

- **FE không sở hữu entity nào** — chỉ đọc qua C-18.
- **Mới hoàn toàn**: MyBadges, BadgeTypeRow, BadgeItem (client-side type definitions).
- **Cấu hình nguồn** (BadgeType, Badge, Resource) là scope B09/U8; U9 chỉ nhận kết quả đã tính sẵn qua API.
- **Số lượng cố định**: BE chỉ trả các loại đang bật; mỗi loại luôn có đúng 8 mốc.
