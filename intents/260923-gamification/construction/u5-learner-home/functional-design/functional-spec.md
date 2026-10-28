---
intent: 260923-gamification
unit: u5-learner-home
artifact: functional-spec
stage: 3.1 functional-design
bolt: B04
version: 1.1
status: draft
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
---
# Functional Spec: U5 `u5-learner-home`

**FE focus.** Nghiệm thu qua TC-401…TC-422 (US1). Nguồn sự thật cho GamificationPage phía học viên. Dữ liệu ở `entities.md`, rule ở `rules.md`. B04/U5 phủ **US1** (bolt-plan xác nhận "Units U5 (US1)").

## Phạm vi

| Có ở U5 (B04 FE) | Không ở U5 |
|---|---|
| GamificationPage: dải tóm tắt 4 ô (Streaks, Points, Badges, Level) | Ghi nhận check-in (U2/B06 — LmsCheckinTrigger) |
| Menu item "Gamification" và route guard | Bảng xếp hạng full feature (US6/B04 phần BE; US6 FE mở dần từ B06+) |
| Tooltip ô Streaks; click Points → panel How to collect | Tab Badges ở My Profile (U9/B10) |
| Click Level → panel How to level up | Lịch sử ghi nhận (U7/B08) |
| My Learning widget: {n} Points · Level {k} | Thông báo realtime (U6/B07) |
| Ẩn hiện theo BR-1.8 (features.* từ /me) | Cấu hình điểm/huy hiệu/hạng (Ops — B01, B09, B11) |
| LmsGamificationVisibility: phân phối cờ hiển thị | Campaign (US19/B12) |

## Điểm vào

- **GamificationPage**: route `/gamification` trong lms-fe (mới). Component tree: `LmsAppShellIntegration` → menu item → route → `LmsGamificationFeature` → `GamificationPage`.
- **My Learning**: màn hiện có `apps/lms/src/...MyLearningPage` — chỉ thêm widget nhỏ đầu màn (BR1.13). Không đổi layout hiện có.

## WF-1: Tải GamificationPage

```
Học viên bấm menu "Gamification"
  → GamificationPage mount
  → GET /lms/api/v1/gamification/me (C-13)
     ┌─ 200 → parse GamificationMe → render 4 ô, ẩn ô theo features.*
     ├─ 404|630012 → ẩn menu, hiện not-found (BR-1.1, BR-1.5)
     └─ network error → skeleton + retry message, không crash
```

**Skeleton**: hiện 4 ô placeholder khi đang tải. Lỗi mạng: skeleton chuyển thành thông báo lỗi, có nút "Retry". Không hiện ô trắng.

## WF-2: Dải tóm tắt 4 ô

### Cấu trúc UI

```
┌─ Gamification ─────────────────────────────────────────────────┐
│ Gamification                                                    │
│ Keep learning and climb the leaderboard.                        │
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌────────────┐  ┌────────┐ │
│  │ {n} Streaks │  │ {n} Points  │  │ {n} Badges │  │Level{n}│ │
│  │ (tooltip)   │  │ (→ panel)   │  │ (→ Badges) │  │(→panel)│ │
│  └─────────────┘  └─────────────┘  └────────────┘  └────────┘ │
│                                                                 │
│  [Leaderboard — US6, xem ghi chú phạm vi]                      │
└─────────────────────────────────────────────────────────────────┘
```

### Hành vi từng ô

| Ô | Hiện | Hover | Click | Ẩn khi |
|---|---|---|---|---|
| Streaks | `{n} Streaks` | Tooltip: `Days in a row you've visited.` | Không có hành động | `features.checkin = false` |
| Points | `{n} Points` (dấu chấm nghìn) | `How to collect points?` | Mở panel How to collect points (WF-3) | `features.points = false` |
| Badges | `{n} Badges` | `Go to badge gallery` | Navigate → My Profile → tab Badges (U9/B10) | `features.badges = false` |
| Level | `Level {n}` | `How to level up?` | Mở panel How to level up (WF-4) | `features.levels = false` |

**Ghi chú ô hiện `0`**: học viên mới chưa có điểm → mọi ô hiện `0`, Level hiện `Level 1` (BR-10.1, TC-420).

## WF-3: Panel "How to collect points?"

```
Click ô Points
  → Panel trượt từ phải
  → Nếu chưa tải rules: GET /lms/api/v1/gamification/rules (C-14, lazy)
     ┌─ 200 → render danh sách hành động
     └─ error → hiện thông báo lỗi trong panel
  → Đóng: click ✕ hoặc click ngoài panel
```

**Cấu trúc panel:**

```
┌─ How to collect points?  [✕] ─────────────────────────────┐
│  {nền}–{trần} pts   for visiting each day, +5 in a row,   │
│                      up to {trần}  [chỉ khi nền < 40]      │
│  {n} pts             for each activity completion           │
│  {n} pts             for each course completion             │
│  {n} pts             for each successful test completion    │
│                                                             │
│  Hành động tắt → không hiện dòng tương ứng                 │
│                                                             │
│  [Achievement History]  ← ở cuối panel                     │
└─────────────────────────────────────────────────────────────┘
```

**Dòng Check-in** (BR1.15):
- Điểm nền < 40: nhãn `{nền}–{trần} pts`, mô tả `for visiting each day, +5 in a row, up to {trần}`
- Điểm nền >= 40: nhãn `{nền} pts`, mô tả `for visiting each day`
- Tuyệt đối **không dùng**: `login`, `sign-in`, `check in`

**Nút "Achievement History"**:
- `features.points = true` → nút nằm cuối panel How to collect points (mở U7/B08 panel)
- `features.points = false` AND `features.levels = true` → nút chuyển vào panel How to level up
- Cả hai tắt → không có lối vào lịch sử (BR-1.8 bảng Nút Achievement History)

## WF-4: Panel "How to level up?"

```
Click ô Level
  → Panel trượt từ phải
  → Dùng /gamification/rules đã cache (hoặc fetch nếu chưa tải)
  → Render danh sách level_criteria đang chạy
  → Đóng: click ✕ hoặc click ngoài panel
```

**Cấu trúc panel:**

```
┌─ How to level up?  [✕] ─────────────────────────────────────┐
│  Every 3,000 points                                          │
│  Every 5 completed courses                                   │
│  Every 5 badges                                              │
│                                                              │
│  Tiêu chí tắt hoặc khoá → không hiện dòng (BR1.16)         │
└──────────────────────────────────────────────────────────────┘
```

Mỗi dòng **bắt buộc mở đầu bằng `Every`** (BR-10.2, BR1.16).

## WF-5: My Learning widget

```
My Learning mount
  → GET /lms/api/v1/courses/my-learnings (C-15, endpoint có sẵn)
     ┌─ gamification = null → không render widget
     ├─ gamification != null → render widget "{n} Points · Level {k}"
     │    points null → ẩn phần điểm
     │    level null → ẩn phần hạng
     └─ network error → không render widget (fail silently)
Click widget → navigate /gamification
```

**Widget:**

```
┌─ My Learning ────────────────────────────────────────────┐
│  [Widget] 1.475 Points · Level 3     [→ Gamification]    │
│  ─────────────────────────────────────                   │
│  [Phần khoá học hiện có, không đổi]                      │
└──────────────────────────────────────────────────────────┘
```

Widget đặt **đầu màn My Learning**, trên danh sách khoá. Không thay đổi phần hiện có (BR US1-AC11).

## Kịch bản

| Kịch bản | Kết quả | Rule | TC |
|---|---|---|---|
| Tải trang với dữ liệu thật từ B02 | 4 ô hiện đúng điểm/streak/badge/level từ /me | C-13 | TC-401 |
| Menu "Gamification" khi Visibility bật | Menu item hiện; điều hướng được | BR-1.1, US1-AC1 | TC-402 |
| Visibility tắt → menu item | Biến khỏi menu; vào trực tiếp URL → not-found | BR-1.1, BR-1.5 | TC-403 |
| 4 ô tóm tắt hiện đúng label | "5 Streaks", "1.475 Points", "3 Badges", "Level 2" | BR-1.6, BR1.14 | TC-404 |
| Hover ô Streaks | Tooltip "Days in a row you've visited." | US1-AC4 | TC-405 |
| Click ô Points | Panel How to collect points? trượt từ phải | US1-AC5 | TC-406 |
| Panel how to collect: đúng dòng và số điểm | Dòng check-in format đúng, dòng hành động tắt không hiện | BR1.15 | TC-407 |
| Điểm nền >= 40 → format check-in panel | Hiện "{nền} pts for visiting each day" (không dải) | BR1.15 | TC-408 |
| Click ô Level | Panel How to level up? trượt từ phải | US1-AC7 | TC-409 |
| Panel how to level up: mỗi dòng bắt đầu "Every" | Không có dòng thiếu "Every" | BR1.16, BR-10.2 | TC-410 |
| Click ô Badges | Navigate sang My Profile → tab Badges | US1-AC6 | TC-411 |
| Click ô Streaks | Không có hành động (không mở panel, không navigate) | US1-AC4 | TC-412 |
| Nút ✕ đóng panel | Panel đóng, trang không reload | US1-AC10 | TC-413 |
| My Learning widget hiện điểm + hạng | Widget đầu màn, format "{n} Points · Level {k}" | C-15, BR1.13 | TC-414 |
| Click My Learning widget | Navigate /gamification | US1-AC11 | TC-415 |
| Points tắt → ô Points và panel ẩn | Ô Points biến mất; nút Achievement History chuyển sang panel Level | BR-1.8 | TC-416 |
| Badges tắt → ô Badges ẩn | Ô Badges biến mất | BR-1.8 | TC-417 |
| Levels tắt → ô Level và panel ẩn | Ô Level biến mất; panel How to level up? không mở được | BR-1.8 | TC-418 |
| Test Account → vào /gamification | Not-found; không có menu item | BR-1.5, C10 | TC-419 |
| Học viên mới (chưa có điểm) | 0 Streaks, 0 Points, 0 Badges, Level 1 | US1 Scenario | TC-420 |
| My Learning: Gamification/Visibility tắt | Widget không render; layout My Learning không vỡ | BR1.13 | TC-421 |
| My Learning: Points tắt | Widget hiện "Level {k}" không có "Points" | C-15, BR-1.8 | TC-422 |

## Ghi chú

- **SP ước tính 3.5**: 2 ngày (Sơn FE) — GamificationPage (dải tóm tắt, 2 panel How to, menu guard), My Learning widget, visibility flag. Xem 3.5 plan.
- **Leaderboard (US6)**: B04 tải `boards` và `default_board` từ C-13 nhưng **full leaderboard UI** (bảng xếp hạng, vị trí của tôi) phụ thuộc vào các bolt sau (B06, B12). B04 cần xác nhận từ PO/tech lead mức độ render leaderboard trong phạm vi B04.
- **Cho PO — OQ-Streaks-tooltip**: chuỗi tooltip ô Streaks `"Days in a row you've visited."` dùng "visited" thay "signed in/checked in". Cần PO duyệt text tiếng Anh trước 3.6.
- **Cho PO — OQ-Achievement-History-btn**: nút Achievement History khi cả Points lẫn Levels đều tắt → không có lối vào lịch sử ghi nhận. Xác nhận đây là hành vi mong muốn (BR-1.8 bảng).
- **Code có sẵn**: nhánh WIP lms-fe (ADR-015) có skeleton GamificationPage. B04 merge nhánh này vào staging mà không vỡ (confidence hypothesis).
- **Dependency B10**: ô Badges click → navigate My Profile Badges. Tab Badges của My Profile là scope B10 (U9). B04 chỉ cần **route đúng và điều hướng được**; nội dung tab do B10 điền.
