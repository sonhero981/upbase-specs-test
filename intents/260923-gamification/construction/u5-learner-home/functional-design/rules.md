---
intent: 260923-gamification
unit: u5-learner-home
artifact: rules
stage: 3.1 functional-design
bolt: B04
version: 1.0
status: draft
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
note: Mã BR-1.x = PRD v0.14 US1. Rule kỹ thuật FE đánh tiếp BR1.11+. Bolt-plan xác nhận B04/U5 map US1 (không phải US5 như ghi nhầm trong task brief).
---
# Business Rules: U5 `u5-learner-home`

Mã `BR-1.x` = PRD v0.14 US1. Rule kỹ thuật FE đánh tiếp `BR1.11`. Thẻ `[C-n]` = contract-summary.md; `[BR-n.n]` = rule PRD US khác liên quan.

```yaml
rules:
  # ---- Rules từ PRD US1 (phần FE liên quan) ----
  - id: BR-1.1
    statement: "Màn Gamification chỉ truy cập được khi cả hai công tắc Gamification VÀ Visibility in UpLMS đang bật."
    category: constraint
    applies_to: LmsGamificationFeature, LmsAppShellIntegration (menu)
    trigger: "Mount LmsGamificationVisibility; điều hướng tới /gamification"
    logic: "API GET /me trả 404|630012 khi một trong hai tắt. FE ẩn menu item Gamification và redirect hoặc hiện not-found khi vào thẳng URL. Mọi sub-route của /gamification đều bị chặn theo."
    source: "PRD BR-1.1, US1-AC1, TC-402, TC-403"

  - id: BR-1.2
    statement: "Điểm hiển thị là điểm tích luỹ cá nhân, không phải điểm theo khung thời gian."
    category: display
    applies_to: LmsGamificationFeature (ô Points)
    trigger: "Render dải tóm tắt"
    logic: "Ô Points hiện `{n} Points` với n lấy từ C-13 `points` (tích luỹ). Không có bộ lọc thời gian trên dải tóm tắt."
    source: "PRD BR-1.2, US1-AC3"

  - id: BR-1.3
    statement: "Hạng chỉ lên, không tụt. Hiển thị hạng lưu trong UserStats, không tính lại."
    category: display
    applies_to: LmsGamificationFeature (ô Level)
    trigger: "Render dải tóm tắt"
    logic: "Ô Level hiện `Level {n}` với n từ C-13 `level`. FE không có logic xét ngưỡng — đây là đọc trực tiếp từ snapshot UserStats (NFR US1)."
    source: "PRD BR-1.3, C4"

  - id: BR-1.5
    statement: "Test Account không thể vào màn Gamification."
    category: constraint
    applies_to: LmsGamificationFeature
    trigger: "GET /me trả 404|630012"
    logic: "Giống Gamification/Visibility tắt — FE xử lý cùng một handler: ẩn menu, not-found khi vào URL. Không phân biệt lý do 404|630012 từ phía FE."
    source: "PRD BR-1.5, C10, TC-419"

  - id: BR-1.6
    statement: "Điểm là số nguyên. Format phân cách hàng nghìn bằng dấu chấm."
    category: display
    applies_to: LmsGamificationFeature (ô Points, My Learning widget)
    trigger: "Render điểm"
    logic: "Ví dụ: 1.475 Points. Dùng Intl.NumberFormat hoặc utility đang dùng trong lms-fe cho các số tương tự."
    source: "PRD BR-1.6, US1-AC3"

  - id: BR-1.7
    statement: "Ảnh huy hiệu bị xoá từ kho tài nguyên → rơi về ảnh mặc định, huy hiệu của học viên không mất."
    category: fault-tolerance
    applies_to: LmsGamificationFeature (tab Badges — U9/B10)
    trigger: "Ảnh trả 404"
    logic: "FE dùng onError → fallback src cho <img> của huy hiệu. Áp dụng ở B10 (U9), ghi nhận ở B04 vì rule xuất phát từ US1."
    source: "PRD BR-1.7, TC-313 (B09)"

  - id: BR-1.8
    statement: "Mỗi thành phần phía học viên ẩn theo công tắc của chức năng sinh ra nó."
    category: visibility
    applies_to: LmsGamificationVisibility, LmsGamificationFeature, LmsAppShellIntegration
    trigger: "Đọc features từ C-13"
    logic: |
      Bảng ẩn hiện (FE đọc features.* từ /me):
        - features.checkin = false → ẩn ô Streaks
        - features.points = false → ẩn ô Points, panel How to collect points?, phần điểm trên My Learning
        - features.badges = false → ẩn ô Badges
        - features.levels = false → ẩn ô Level, panel How to level up?, phần hạng trên My Learning
        - features.leaderboard = false → ẩn Bảng xếp hạng và khối vị trí của tôi
      Nút Achievement History: nếu Points tắt và Levels còn bật → chuyển vào panel How to level up?. Cả hai tắt → không có lối vào lịch sử.
      FE đọc features một lần từ /me response, lưu ở LmsGamificationVisibility, không re-fetch riêng.
    source: "PRD BR-1.8, US1 bảng ẩn hiện, TC-416, TC-417, TC-418"

  # ---- Rules kỹ thuật FE ----
  - id: BR1.11
    statement: "GET /gamification/me gọi một lần khi GamificationPage mount; LmsGamificationVisibility dùng kết quả này cho toàn app shell."
    category: performance
    applies_to: LmsGamificationFeature, LmsGamificationVisibility
    trigger: "Mount GamificationPage / Mount LmsGamificationVisibility"
    logic: "Không gọi lại /me khi chuyển tab trong trang Gamification. Refetch chỉ khi học viên reload trang hoặc rời đi và quay lại màn. LmsGamificationVisibility chia sẻ response với LmsGamificationFeature qua store hoặc context."
    source: "US1 NFR, C-13"

  - id: BR1.12
    statement: "GET /gamification/rules tải lazy — chỉ gọi khi học viên mở một trong hai panel How to."
    category: performance
    applies_to: LmsGamificationFeature (hai panel)
    trigger: "Click ô Points hoặc ô Level lần đầu"
    logic: "Tải một lần cho cả phiên (cache in-memory). Đóng rồi mở lại panel không gọi lại API. Hiện skeleton trong panel khi đang tải. Lỗi network → hiện thông báo lỗi trong panel, không crash trang."
    source: "C-14, US1 NFR"

  - id: BR1.13
    statement: "My Learning widget chỉ render khi gamification != null trong response C-15."
    category: conditional-render
    applies_to: LmsAppShellIntegration (My Learning page)
    trigger: "Đọc response /courses/my-learnings"
    logic: "gamification = null: không render widget (Gamification/Visibility tắt, Test Account). gamification.points = null: ẩn phần điểm trong widget. gamification.level = null: ẩn phần hạng trong widget. Tránh sửa layout My Learning khi không có dữ liệu gamification."
    source: "C-15, BR-1.8, TC-421, TC-422"

  - id: BR1.14
    statement: "Điểm chuỗi hiện dạng nguyên, không thêm đơn vị nào khác ngoài 'Streaks'. Level hiện dạng 'Level {n}' — không có tên hạng."
    category: display
    applies_to: LmsGamificationFeature (dải tóm tắt)
    trigger: "Render 4 ô tóm tắt"
    logic: "Ô Streaks: '{n} Streaks' (không hiện 'days', không có thêm text). Ô Level: 'Level {n}' (không có tên, không có hình hạng). Ô Points: '{n} Points' (format số với dấu chấm nghìn). Ô Badges: '{n} Badges'."
    source: "PRD US1-AC3, US1-AC4, OQ-38"

  - id: BR1.15
    statement: "Dòng check-in trong panel How to collect points? dùng format khoảng '{nền}–{trần} pts' khi chuỗi có tác dụng; dùng '{nền} pts' khi điểm nền >= 40."
    category: display
    applies_to: LmsGamificationFeature (panel How to collect points?)
    trigger: "Render panel từ /gamification/rules response"
    logic: "Lấy base_points và checkin_cap từ C-14 point_rules cho CHECKIN action. Nếu base_points >= 40: nhãn '{base_points} pts', mô tả 'for visiting each day'. Nếu base_points < 40: nhãn '{base_points}–{cap} pts', mô tả 'for visiting each day, +5 in a row, up to {cap}'. Tuyệt đối không dùng 'login', 'sign-in', hay 'check in' ở đây."
    source: "PRD US1 bảng Two panels, BR-8.5a, TC-407"

  - id: BR1.16
    statement: "Mỗi dòng trong panel How to level up? bắt đầu bằng 'Every'. Tiêu chí tắt hoặc khoá không hiện."
    category: display
    applies_to: LmsGamificationFeature (panel How to level up?)
    trigger: "Render panel từ /gamification/rules response"
    logic: "Ví dụ: 'Every 3,000 points', 'Every 5 completed courses', 'Every 5 badges'. Chữ 'Every' bắt buộc — thiếu thì học viên hiểu nhầm thành mốc một lần (BR-10.2). Tiêu chí không có trong level_criteria mảng → không hiện dòng."
    source: "PRD US1 bảng Two panels, BR-10.2, TC-409, TC-410"
```

## Tóm tắt

| ID | Rule | Loại | Thuộc |
|---|---|---|---|
| BR-1.1 | Màn chỉ tồn tại khi cả hai công tắc bật | constraint | UI + BE |
| BR-1.2 | Điểm tích luỹ, không theo khung thời gian | display | UI |
| BR-1.3 | Hạng chỉ lên, đọc từ snapshot | display | BE (FE chỉ đọc) |
| BR-1.5 | Test Account không vào được | constraint | UI + BE |
| BR-1.6 | Điểm số nguyên, format dấu chấm nghìn | display | UI |
| BR-1.7 | Ảnh huy hiệu fallback | fault-tolerance | UI (áp dụng B10) |
| BR-1.8 | Ẩn theo công tắc chức năng | visibility | UI |
| BR1.11 | GET /me: gọi một lần, chia sẻ | performance | UI |
| BR1.12 | GET /rules: lazy khi mở panel | performance | UI |
| BR1.13 | My Learning widget: render khi gamification != null | conditional-render | UI |
| BR1.14 | Format 4 ô tóm tắt | display | UI |
| BR1.15 | Format dòng check-in trong panel | display | UI |
| BR1.16 | Format dòng level-up trong panel ("Every") | display | UI |
