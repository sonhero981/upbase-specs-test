---
intent: 260923-gamification
unit: u9-badge-gallery
artifact: functional-spec
stage: 3.1 functional-design
bolt: B10
version: 1.0
status: draft
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
consumes: unit-of-work.md v2.0 (U9), contract-summary.md v2.0 (C-18), PRD v0.14 US4
---
# Functional Spec: U9 `u9-badge-gallery`

**FE focus.** Nghiệm thu qua TC-501…TC-519 (US4). Nguồn sự thật cho tab Badges trong My Profile phía học viên. Dữ liệu ở `entities.md`, rule ở `rules.md`. B10/U9 phủ **US4** (bolt-plan xác nhận "Units U9 (US4)").

## Phạm vi

| Có ở U9 (B10 FE) | Không ở U9 |
|---|---|
| Tab `Badges` trong My Profile | Cấu hình huy hiệu (U8/B09 — OpsSettingsPage) |
| Grid huy hiệu nhóm theo loại, earned/locked state | Thanh tiến độ tới huy hiệu kế tiếp |
| Bộ đếm `({earned_count}/{total})` theo loại | Ngày đạt cạnh huy hiệu |
| Hover tooltip: milestone + description | Gợi ý nội dung để đạt huy hiệu |
| Fallback ảnh mặc định (BR-1.7) | Thông báo khi sắp đạt (US2/B07) |
| Ẩn tab khi Badges tắt (BR-4.4, BR-1.8) | Ghi nhận, trao huy hiệu (U1/B05) |
| Navigation từ GamificationPage (B04) | Thay đổi tên/hình huy hiệu (chỉ đọc với học viên) |

## Điểm vào (Entry Point)

**Từ GamificationPage (B04/U5):**
- Học viên click ô `{n} Badges` trên GamificationPage
- B04 navigate đến My Profile với active tab = `badges` (route cụ thể cần xác nhận — xem OQ bên dưới)
- B10 nhận route param/state, mount tab Badges, fetch C-18

**Từ My Profile trực tiếp:**
- Học viên vào My Profile, click tab `Badges`
- Tab `Badges` chỉ render nếu `features.badges = true` (đọc từ C-13 đã cache ở LmsGamificationVisibility/B04)

**Tab position trong My Profile:** `My profile` · `Security` · **`Badges`** (thứ tự từ trái; `Badges` chỉ hiện khi Badges bật)

## WF-1: Tải tab Badges

```
Học viên click tab Badges (hoặc navigate từ B04 ô Badges)
  → Tab Badges mount
  → Kiểm tra features.badges từ LmsGamificationVisibility
       └─ features.badges = false → không render tab (return null)
  → GET /lms/api/v1/gamification/me/badges (C-18)
     ┌─ 200 → parse MyBadges → render BadgeGallery
     ├─ 404|630012 → ẩn tab (coi Badges tắt), không render tab nữa
     └─ network error → skeleton → error state + Retry button trong tab
```

**Loading state:** skeleton grid cho 4 loại (4 header placeholder + 8 badge card placeholder mỗi nhóm).
**Error state (network):** inline error message trong tab, nút `Retry` gọi lại API. Không crash trang.
**404:** ẩn tab im lặng (không alert, không crash). Tab My Profile quay về tab mặc định.

## WF-2: Render BadgeGallery

### Cấu trúc UI

```
┌─ My Profile ─────────────────────────────────────────────┐
│  [My profile]  [Security]  [Badges]                       │
│                                                           │
│  ┌─ Badges ─────────────────────────────────────────┐    │
│  │                                                   │    │
│  │  Check-in Badges (2/8)                            │    │
│  │  ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐                  │    │
│  │  │ ■ │ │ ■ │ │░░░│ │░░░│ │░░░│  …(8 total)       │    │
│  │  │ 4 │ │ 8 │ │16 │ │32 │ │64 │                   │    │
│  │  └───┘ └───┘ └───┘ └───┘ └───┘                   │    │
│  │  [■ earned, ░ locked/grayscale]                   │    │
│  │                                                   │    │
│  │  Activity Badges (0/8)                            │    │
│  │  ┌───┐ ┌───┐ ┌───┐ …                             │    │
│  │  │░░░│ │░░░│ │░░░│                               │    │
│  │  └───┘ └───┘ └───┘                               │    │
│  │                                                   │    │
│  │  Test Badges (1/8)                                │    │
│  │  …                                                │    │
│  │                                                   │    │
│  │  Course Badges (0/8)                              │    │
│  │  …                                                │    │
│  └───────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────┘
```

### Sections và header

- Mỗi `BadgeTypeRow` trong response → một section
- Header: `{Tên loại} Badges ({earned_count}/{total})`
  - CHECKIN → `Check-in Badges`
  - ACTIVITY → `Activity Badges`
  - TEST → `Test Badges`
  - COURSE → `Course Badges`
- Thứ tự sections: theo thứ tự server trả (CHECKIN → ACTIVITY → TEST → COURSE)
- Loại tắt: không có trong response → không render section

### Badge card

Mỗi `BadgeItem` → một card trong grid:

| Trạng thái | Ảnh | Tên (dưới ảnh) | Hover |
|---|---|---|---|
| `is_earned = true` | Màu, opacity 100% | Hiện đủ | Khung nổi, tooltip milestone [+ description] |
| `is_earned = false` | Grayscale + opacity thấp | Hiện đủ (không ẩn) | Khung nổi, tooltip milestone [+ description] |

**Grid layout:** 5 cột ở desktop (≥768px); responsive collapse mobile.
**Thứ tự cards:** theo thứ tự server trả (milestone tăng dần — server sort).

### WF-3: Hover badge (tooltip)

```
Học viên hover vào badge card (desktop)
  → Border nổi lên
  → Hiện milestone label dưới tên: "{milestone} {unit}"
     Ví dụ: "8 check-in days", "25 activities", "4 passed tests", "2 completed courses"
  → Nếu description != null: hiện thêm dòng mô tả bên dưới
  → Di chuột ra ngoài → về trạng thái bình thường
```

**Mobile:** tap để reveal tooltip hoặc dùng native tooltip (theo convention lms-fe).
**Áp dụng cho cả earned và locked badge.**

### WF-4: Ảnh fallback (BR-1.7)

```
Render <img src={image_url}>
  → img onError event
  → FE set src = DEFAULT_BADGE_IMAGE (static asset lms-fe)
  → Render ảnh mặc định, badge không biến mất
```

`DEFAULT_BADGE_IMAGE` là constant trong codebase lms-fe, dùng chung cho mọi badge.

## Kịch bản (TC-501 … TC-519)

| Kịch bản | Kết quả | Rule | TC |
|---|---|---|---|
| Click ô Badges trên GamificationPage | Navigate sang My Profile → tab Badges active | BR4.16, US1-AC6, US4-AC điểm vào | TC-501 |
| Tab Badges load thành công | Hiện 4 section loại, đúng badge từ API | BR-4.1, C-18 | TC-502 |
| Header section mỗi loại | Format `{Type} Badges ({earned_count}/{total})`, ví dụ `Check-in Badges (2/8)` | BR4.13, US4-AC tiêu đề loại | TC-503 |
| Badge is_earned = true | Hình màu, opacity 100% | BR-4.2 | TC-504 |
| Badge is_earned = false | Hình grayscale + opacity thấp | BR-4.2 | TC-505 |
| Tên badge hiện dưới hình | Hiện cho cả earned và locked | BR4.15, US4-AC Tên | TC-506 |
| Hover badge earned | Tooltip `{milestone} {unit}` hiện | BR4.14, US4-AC Trỏ chuột vào | TC-507 |
| Hover badge locked | Tooltip `{milestone} {unit}` hiện (không bị chặn vì locked) | BR4.14 | TC-508 |
| Badge có description | Tooltip hiện thêm mô tả bên dưới milestone | BR4.14, US4-AC [đề xuất] | TC-509 |
| Thứ tự badge trong loại | Milestone tăng dần (server-side sort) | US4-AC Thứ tự | TC-510 |
| Loại chưa đạt huy hiệu nào | Hiện đủ 8 mốc, tất cả grayscale, header `(0/8)` | BR-4.1, US4-AC 'Loại chưa đạt huy hiệu nào' | TC-511 |
| Ảnh badge 404 | Fallback ảnh mặc định, badge vẫn render | BR-1.7 | TC-512 |
| Loại huy hiệu tắt | Section của loại đó không hiện | BR-4.4, BR-9.5 | TC-513 |
| Badges (tổng) tắt | Tab `Badges` biến mất khỏi My Profile | BR-4.4, BR-9.6, BR-1.8 | TC-514 |
| Test Account vào My Profile | Tab `Badges` không hiện | BR-4.5, C10 | TC-515 |
| Không có thao tác write | Không có nút/form nào trên tab | BR-4.6 | TC-516 |
| Loading state khi fetch C-18 | Skeleton grid hiện | BR4.12 | TC-517 |
| Network error khi fetch C-18 | Inline error + nút Retry | BR4.12 | TC-518 |
| Retry sau network error | Re-fetch C-18, render bình thường | BR4.12 | TC-519 |

## Ghi chú

- **SP ước tính 3.5**: 1,5 ngày (Sơn FE) — tab Badges trong My Profile, BadgeGallery component, API integration C-18, skeleton/error states, fallback image, hover tooltip. Xem 3.5 plan.
- **Tab đã có WIP**: nhánh WIP lms-fe (ADR-015) có skeleton tab Badges trong My Profile. B10 hoàn thiện từ skeleton này.
- **Không có thanh tiến độ**: design chốt 01/10 không có. Panel `How to level up?` đã nêu cách lên hạng (BR-4.2).
- **Không hiện ngày đạt**: học viên tra trong lịch sử ghi nhận U7/B08 (BR-4.2, US4-AC Ngày đạt).
- **B04 responsibility**: ô Badges click → navigate. B10 chỉ cần route param/state đúng → activate tab. B04 không làm gì với nội dung tab.

## Câu hỏi mở (cần trả lời trước 3.6)

| ID | Hỏi | Hỏi ai | Mức chặn |
|---|---|---|---|
| OQ-B10-1 | Route/state chính xác để navigate từ GamificationPage sang My Profile + active tab Badges là gì? Hiện lms-fe dùng `/profile?tab=badges` hay query param hay router state? | Tech lead / code review nhánh WIP | Chặn code-gen nếu khác convention hiện tại |
| OQ-B10-2 | Mobile: hover tooltip hiện thế nào? Tap để reveal, hay longpress, hay tooltip tự động collapse? Cần design xác nhận. | Designer / PO | Chặn nếu mobile UX quan trọng với PO |
| OQ-B10-3 | `DEFAULT_BADGE_IMAGE` là asset nào cụ thể trong lms-fe? Path/URL cần xác nhận để không hard-code sai. | Tech lead | Chặn code-gen |
| OQ-B10-4 | Grid 5 cột collapse mobile thế nào? 2 cột? Scroll horizontal? Cần design spec chi tiết. | Designer | Chặn CSS nếu chưa có spec |
