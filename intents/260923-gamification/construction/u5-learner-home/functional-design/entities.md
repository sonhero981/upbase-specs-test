---
intent: 260923-gamification
unit: u5-learner-home
artifact: entities
stage: 3.1 functional-design
bolt: B04
version: 1.0
status: draft
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
consumes: bolt-plan.md (B04), components.md v2.0, contract-summary.md v2.0 (C-13, C-14, C-15), PRD v0.14 US1
note: B04/U5 map sang US1 trong PRD ("Màn Gamification"). bolt-plan.md xác nhận "Units U5 (US1)". Nhiệm vụ brief ghi nhầm US5 — cần PO/tech lead xác nhận nếu phạm vi thực sự khác.
---
# Entities: U5 `u5-learner-home`

**FE focus.** Màn Gamification học viên (lms-fe) — chỉ đọc. FE không sở hữu bất kỳ entity nào; mọi dữ liệu đọc từ API. Bảng và migration cụ thể ở BE (`../code-generation/`). Nguồn sự thật: `lms-be origin/feature/gamification` (ADR-008).

```yaml
entities:
  - name: GamificationMe
    kind: api-response-shape
    status: new (C-13)
    description: "Snapshot trạng thái gamification hiện tại của học viên đang đăng nhập. FE đọc 1 lần khi mount GamificationPage và LmsGamificationVisibility. Không tính lại khi đọc — US1 NFR."
    source: "GET /lms/api/v1/gamification/me (C-13, LearnerGamificationApi)"
    attributes:
      - {name: features, type: object, required: true, note: "Cờ ẩn hiện (BR-1.8): points, checkin, badges, levels, leaderboard. FE dùng để quyết định hiện/ẩn từng ô tóm tắt và panel."}
      - {name: boards, type: array, required: false, note: "Bảng xếp hạng đang chạy (US6, không thuộc B04 FE scope)."}
      - {name: default_board, type: object, required: false, nullable: true, note: "Bảng mặc định (US6)."}
      - {name: timezone, type: string, required: true, note: "Múi giờ tenant, dùng cho LmsCheckinTrigger (U2/B06)."}
      - {name: today, type: string, format: date, required: true, note: "Ngày hôm nay theo múi giờ tenant, dùng khoá check-in phía client (ADR-010, U2/B06)."}
      - {name: points, type: integer, required: true, note: "Điểm tích luỹ. >= 0. Phân cách hàng nghìn bằng dấu chấm (BR-1.2, BR-1.6)."}
      - {name: level, type: integer, required: true, note: "Hạng hiện tại >= 1. Không có tên hạng, không có hình hạng."}
      - {name: streak, type: integer, required: true, note: "Chuỗi ngày vào hệ thống liên tiếp đang giữ. >= 0."}
      - {name: badges, type: integer, required: true, note: "Số huy hiệu đã đạt, chỉ đếm loại đang bật (BR-9.10). >= 0."}
    constraints:
      - "404|630012 khi Gamification tắt hoặc Visibility tắt — FE xử lý bằng ẩn toàn bộ giao diện (BR-1.1)"
      - "Không có endpoint PATCH — màn Gamification là chỉ đọc với học viên"
      - "Test Account nhận 404|630012 — FE không được render trang (BR-1.5)"

  - name: GamificationRules
    kind: api-response-shape
    status: new (C-14)
    description: "Danh sách hành động đang bật và điểm, tiêu chí lên hạng. FE tải lazily khi người dùng mở panel How to. Không tải trước khi trang mount."
    source: "GET /lms/api/v1/gamification/rules (C-14, LearnerGamificationApi)"
    attributes:
      - {name: point_rules, type: array, required: false, note: "Mỗi dòng: {source: ActionCode, points, checkin_cap}. Hành động tắt không có trong mảng — FE không hiện dòng tương ứng (US1-AC8)."}
      - {name: level_criteria, type: array, required: false, note: "Tiêu chí lên hạng đang chạy. Mỗi dòng bắt đầu bằng 'Every' trên UI (BR-10.2). Tiêu chí tắt/khoá không có trong mảng."}
    constraints:
      - "FE tải đúng một lần khi panel mở, không refetch khi đóng mở lại trong cùng phiên (BR1.12)"
      - "Không hiển thị nếu fetch lỗi — panel hiện trạng thái lỗi, không crash trang"

  - name: MyLearningGamification
    kind: api-response-shape-extension
    status: existing + extension (C-15)
    description: "Field gamification được thêm additive vào GET /courses/my-learnings hiện có. FE My Learning đọc khi tải màn. null khi Gamification/Visibility tắt hoặc Test Account."
    source: "GET /lms/api/v1/courses/my-learnings (C-15, endpoint có sẵn thêm field)"
    attributes:
      - {name: points, type: integer, required: false, nullable: true, note: "null khi Points tắt (BR-1.8)."}
      - {name: level, type: integer, required: false, nullable: true, note: "null khi Levels tắt (BR-1.8)."}
    constraints:
      - "gamification = null → FE không render widget trên My Learning (BR1.13)"
      - "Backward-compatible: field mới, FE cũ bỏ qua được"
      - "points null → ẩn phần điểm; level null → ẩn phần hạng trong widget"
```

## Dữ liệu API (FE đọc)

| API | Method | FE dùng để | Contract | Component FE |
|---|---|---|---|---|
| `GET /lms/api/v1/gamification/me` | GET | Tải snapshot điểm/chuỗi/huy hiệu/hạng + cờ hiển thị | C-13 | LmsGamificationVisibility, LmsGamificationFeature |
| `GET /lms/api/v1/gamification/rules` | GET | Tải nội dung hai panel How to (lazy khi mở panel) | C-14 | LmsGamificationFeature |
| `GET /lms/api/v1/courses/my-learnings` | GET | Tải khối điểm+hạng nhỏ trên My Learning | C-15 | LmsAppShellIntegration |

## Tóm tắt

- **FE không sở hữu entity nào** — chỉ đọc qua LmsGamificationApiClient.
- **C-13** là API chính, tải một lần khi mount, phủ mọi dữ liệu trên dải tóm tắt.
- **C-14** là API lazy (chỉ gọi khi mở panel How to), tránh tải thừa.
- **C-15** là API có sẵn mở rộng — FE chỉ cần đọc thêm field `gamification` từ response.
- `today` và `timezone` trong C-13 dùng cho U2 (B06 check-in trigger), không phải B04.
- `boards` và `default_board` trong C-13 dùng cho US6 (B04 không bao gồm leaderboard full feature).
