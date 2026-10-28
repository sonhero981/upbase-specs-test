---
intent: 260923-gamification
unit: u5-learner-home
artifact: review-functional-design
stage: 3.1 functional-design
bolt: B04
version: review-01
reviewer: FE lead Nguyễn Hùng Sơn
date: 2026-10-15
verdict: READY
---
# Review 3.1 Functional Design: B04 `u5-learner-home`

## Verdict: READY

Không có Chặn. Ba Ghi nhận nhỏ cần fix trước hoặc khi bước vào 3.5.

## Checklist

| Hạng mục | Kết quả |
|---|---|
| Phủ US1-AC1…AC12 | Đạt — traceability.json map đầy đủ |
| BR-1.1…1.8 FE scope | Đạt — rules.md phủ hết các BR có tác động FE |
| BR1.11…BR1.16 kỹ thuật (dạng số, sensor-safe) | Đạt — không hậu tố chữ cái |
| API đúng contract (C-13, C-14, C-15) | Đạt — entities.md bảng API đúng |
| WF flows phủ màn học viên | Đạt — WF-1 tải, WF-2 dải 4 ô, WF-3 panel Points, WF-4 panel Level, WF-5 My Learning |
| TC dãy 401–422 không trùng | Đạt — 22 TC |
| B04 ≠ US5 (phát hiện sửa brief sai) | Ghi nhận — bolt-plan.md xác nhận B04/U5 = US1 ✓ |

## Findings

### F-01 — Ghi nhận
**TC-403 kịch bản**: cột Rule ghi `"BR-1.1, TC-403"` — tự tham chiếu TC-403 trong chính dòng TC-403. Sửa thành `"BR-1.1, BR-1.5"`.

### F-02 — Ghi nhận
**WF-2 ô Streaks — điều kiện ẩn không nhất quán**:
- `rules.md` BR-1.8: `features.checkin = false → ẩn ô Streaks` (chỉ checkin).
- `functional-spec.md` WF-2: `"Ẩn khi features.checkin = false hoặc features.points = false"` (thêm điều kiện points).

Nếu Points tắt nhưng check-in vẫn bật → Streaks có hiện không? Cần nhất quán. **Đề xuất**: giữ theo BR-1.8 (chỉ `features.checkin`); xoá `hoặc features.points = false` khỏi WF-2.

### F-03 — Chuyển gate
**OQ-B04-1 Leaderboard scope**: B04 FE chưa rõ cần render leaderboard đến mức nào trong phạm vi B04. Cần PO/tech lead trả lời trước 3.6 — ảnh hưởng trực tiếp đến lượng code cần làm (placeholder vs bảng đầy đủ).

## Điều kiện gate

Gate **conditional**:
- Sửa F-01 + F-02 (nhỏ, FE tự fix — không chặn gating)
- F-03 (OQ-B04-1) trả lời trước bước 3.6; không chặn gate 3.1

## Gate

**[x] FE lead approve** — Nguyễn Hùng Sơn (2026-10-15): v1.0 đủ nội dung để lên 3.5 plan. Sửa F-01 + F-02 trong v1.1 khi tiện. B04 3.1 PASS. B10 mở khoá sau khi B04 + B09 đều pass 3.5.
