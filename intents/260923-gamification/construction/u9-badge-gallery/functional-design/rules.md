---
intent: 260923-gamification
unit: u9-badge-gallery
artifact: rules
stage: 3.1 functional-design
bolt: B10
version: 1.1
status: draft
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
consumes: unit-of-work.md v2.0 (U9), contract-summary.md v2.0 (C-18), PRD v0.14 US4
---
# Business Rules: U9 `u9-badge-gallery`

Mã `BR-4.x` = PRD v0.14 US4. Rule kỹ thuật FE đánh tiếp `BR4.11`. Thẻ `[C-n]` = contract-summary.md; `[BR-n.n]` = rule PRD US khác liên quan.

```yaml
rules:
  # ---- Rules từ PRD US4 (phần FE liên quan) ----
  - id: BR-4.1
    statement: "Tab Badges hiện toàn bộ huy hiệu của mọi loại đang bật, cả đã đạt lẫn chưa đạt, kèm mốc của từng cái."
    category: display
    applies_to: LmsGamificationFeature (BadgeGallery tab)
    trigger: "Tải tab Badges"
    logic: "FE render mọi BadgeItem trong response C-18 cho từng BadgeTypeRow. Không lọc is_earned. Mỗi loại có đúng 8 mốc (total = 8, BR-9.2). Loại tắt không xuất hiện trong response (server-side filter BR-9.5)."
    source: "PRD BR-4.1, US4-AC row 'Loại chưa đạt huy hiệu nào'"

  - id: BR-4.2
    statement: "Đã đạt và chưa đạt phân biệt bằng màu. Không có thanh tiến độ, không hiện phần còn thiếu, không hiện ngày đạt."
    category: display
    applies_to: LmsGamificationFeature (BadgeGallery — từng BadgeItem)
    trigger: "Render mỗi ô huy hiệu"
    logic: "is_earned = true → hình màu, opacity 100%. is_earned = false → grayscale filter + opacity thấp hơn (design chốt 01/10). Tuyệt đối không có: progress bar, '2 more to go', ngày đạt."
    source: "PRD BR-4.2, US4-AC row 'Huy hiệu — Hình', Design chốt 01/10"

  - id: BR-4.4
    statement: "Loại huy hiệu đang tắt không hiện trong gallery. Chức năng Badges tắt → tab biến mất."
    category: visibility
    applies_to: LmsGamificationFeature (BadgeGallery tab, tab header)
    trigger: "C-18 trả 404|630012 hoặc badge_types rỗng"
    logic: "Badges (features.badges) tắt → FE không render tab 'Badges' trong My Profile. Loại tắt → server không trả loại đó (BR-9.5); FE không cần filter thêm. Nếu C-18 trả 404|630012, FE cũng ẩn tab (coi như features.badges = false)."
    source: "PRD BR-4.4, BR-9.5, BR-9.6, BR-1.8 bảng"

  - id: BR-4.5
    statement: "Tài khoản Test Account không có tab này."
    category: constraint
    applies_to: LmsGamificationFeature (tab Badges)
    trigger: "C-18 trả 404|630012"
    logic: "Giống BR-4.4 — FE xử lý cùng handler: 404|630012 → ẩn tab. Không phân biệt lý do từ phía FE (cùng pattern BR-1.5 ở B04/U5)."
    source: "PRD BR-4.5, C10"

  - id: BR-4.6
    statement: "Huy hiệu đã đạt không bao giờ mất; không có thao tác tạo hay xoá huy hiệu trên tab này."
    category: constraint
    applies_to: LmsGamificationFeature (BadgeGallery tab)
    trigger: "Toàn bộ tab"
    logic: "UI chỉ đọc. Không có nút, không có form, không có drag. Hiển thị mốc cố định (BE-side). FE không cần guard chống write."
    source: "PRD BR-4.6, BR-9.2, BR-9.7"

  - id: BR-4.7
    statement: "Vận hành đổi tên, hình hoặc mô tả của mốc → áp ngay cho mọi học viên. FE không cache badge data vô thời hạn giữa các phiên."
    category: policy
    applies_to: LmsGamificationFeature (BadgeGallery tab)
    trigger: "Mở lại tab sau khi vận hành thay đổi cấu hình"
    logic: "FE fetch C-18 khi tab mount lần đầu trong phiên (BR4.11). Cache in-memory trong phiên đó (tránh re-fetch khi chuyển tab — BR4.11). Re-fetch khi: reload trang, navigate ra ngoài app rồi quay lại, hoặc staleTime hết (React Query). Không cần WebSocket — đổi tên/hình không phải real-time event của học viên."
    source: "PRD BR-4.7, BR-9.4"

  - id: BR-1.7
    statement: "Ảnh huy hiệu bị xoá từ kho tài nguyên → rơi về ảnh mặc định, huy hiệu của học viên không mất."
    category: fault-tolerance
    applies_to: LmsGamificationFeature (BadgeGallery — BadgeImage component)
    trigger: "img onError (HTTP 404 trên image_url)"
    logic: "FE dùng onError → fallback src trỏ tới ảnh mặc định của hệ thống. Ảnh mặc định không cần fetch từ server — có thể là static asset trong lms-fe. Áp dụng cho cả badge earned và locked."
    source: "PRD BR-1.7, B04/rules.md BR-1.7, TC-313 (B09)"

  # ---- Rules kỹ thuật FE ----
  - id: BR4.11
    statement: "GET /gamification/me/badges gọi một lần khi tab Badges mount; không gọi lại khi chuyển tab rồi quay lại trong cùng phiên làm việc."
    category: performance
    applies_to: LmsGamificationFeature (BadgeGallery)
    trigger: "Mount tab Badges"
    logic: "Kết quả C-18 cache in-memory (hoặc React Query stale-while-revalidate với staleTime phù hợp). Unmount rồi mount lại trong cùng session: dùng cache, không re-fetch. Reload trang hoặc điều hướng ra ngoài rồi quay lại: fetch mới. Lý do: danh sách huy hiệu ít thay đổi trong phiên; tránh gọi API trùng lặp."
    source: "C-18, PRD US4 NFR"

  - id: BR4.12
    statement: "Skeleton hiện khi đang tải tab Badges lần đầu; lỗi mạng hiện thông báo lỗi trong tab kèm nút Retry."
    category: loading-state
    applies_to: LmsGamificationFeature (BadgeGallery)
    trigger: "Fetch C-18 đang chạy / thất bại"
    logic: "Loading: skeleton grid placeholder cho từng nhóm loại (4 skeleton header + 8 skeleton badge card mỗi nhóm). Error: hiện inline error message trong tab, có nút 'Retry' gọi lại API. Không crash trang, không blank screen. 404 là handled error → ẩn tab (BR-4.4), không hiện retry."
    source: "C-18, UX standard lms-fe"

  - id: BR4.13
    statement: "Grid huy hiệu: 5 cột desktop, collapse về mobile. Header section format '{Type} Badges ({earned_count}/{total})'."
    category: layout
    applies_to: LmsGamificationFeature (BadgeGallery — layout)
    trigger: "Render badge_types"
    logic: "Mỗi BadgeTypeRow tạo một section: tiêu đề '{Tên loại} Badges ({earned_count}/{total})'. Badge grid: 5 cột ở viewport >= 768px; responsive về ít cột hơn (hoặc scroll horizontal) ở mobile (theo design system lms-fe). Thứ tự sections: theo thứ tự server trả (CHECKIN, ACTIVITY, TEST, COURSE — cố định từ seed)."
    source: "PRD US4-AC row 'Tiêu đề loại', BadgeGallery design PRD §6.6"

  - id: BR4.14
    statement: "Tooltip hover badge hiện '{milestone} {unit}'. Nếu badge có description thì hiện thêm mô tả."
    category: display
    applies_to: LmsGamificationFeature (BadgeGallery — hover state)
    trigger: "Học viên hover vào ô huy hiệu (desktop) hoặc tap (mobile)"
    logic: "Desktop hover: khung badge nổi lên (border nổi), hiện milestone dưới tên dạng '{milestone} {unit}'. Nếu description != null: hiện thêm 1-2 dòng mô tả bên dưới milestone. Mobile: fallback về tap-to-reveal hoặc tooltip nhỏ (theo convention lms-fe). Áp dụng cho cả badge earned và locked."
    source: "PRD US4-AC row 'Huy hiệu — Trỏ chuột vào', BadgeGallery design PRD §6.6"

  - id: BR4.15
    statement: "Tên badge hiện dưới hình cho mọi badge, kể cả chưa đạt. Không giấu tên."
    category: display
    applies_to: LmsGamificationFeature (BadgeGallery — BadgeItem)
    trigger: "Render badge card"
    logic: "name luôn hiện dưới ảnh. is_earned = false không ẩn tên — chỉ ảnh bị grayscale + opacity. Học viên chưa đạt vẫn cần biết đây là huy hiệu gì để có mục tiêu."
    source: "PRD US4-AC row 'Huy hiệu — Tên'"

  - id: BR4.16
    statement: "Navigation entry point: ô Badges (B04) click → navigate đến My Profile → tab Badges (B10). Tab Badges là tab thứ ba trong My Profile, cạnh 'My profile' và 'Security'."
    category: navigation
    applies_to: LmsGamificationFeature (GamificationPage — ô Badges), LmsAppShellIntegration (My Profile)
    trigger: "Click ô '{n} Badges' trên GamificationPage"
    logic: "B04 (U5) phát navigate đến route My Profile với query/state chỉ định active tab là 'badges'. B10 (U9) nhận param và activate tab Badges khi mount. Route cụ thể xác nhận với tech lead trước 3.6 (OQ xem mục Câu hỏi). Tab 'Badges' chỉ xuất hiện khi features.badges = true (BR-4.4)."
    source: "PRD US4-AC row 'Điểm vào', B04/functional-spec.md WF-2 ô Badges TC-411, US1-AC6"
```

## Tóm tắt

| ID | Rule | Loại | Thuộc |
|---|---|---|---|
| BR-4.1 | Hiện mọi badge của mọi loại đang bật | display | UI |
| BR-4.2 | Earned màu, locked grayscale; không có progress bar | display | UI |
| BR-4.4 | Loại tắt → ẩn section; Badges tắt → ẩn tab | visibility | UI |
| BR-4.5 | Test Account không có tab | constraint | UI + BE |
| BR-4.6 | Tab chỉ đọc, không có write action | constraint | UI |
| BR-4.7 | Fetch lại mỗi lần mount; không cache quá phiên | policy | UI |
| BR-1.7 | Ảnh 404 → fallback ảnh mặc định | fault-tolerance | UI |
| BR4.11 | Fetch C-18 một lần per tab mount; cache in-session | performance | UI |
| BR4.12 | Skeleton loading; error + retry; 404 → ẩn tab | loading-state | UI |
| BR4.13 | Grid 5 cột, section header format | layout | UI |
| BR4.14 | Hover tooltip: milestone + description | display | UI |
| BR4.15 | Tên badge luôn hiện kể cả locked | display | UI |
| BR4.16 | Navigation entry từ B04; tab param khi mount | navigation | UI |
