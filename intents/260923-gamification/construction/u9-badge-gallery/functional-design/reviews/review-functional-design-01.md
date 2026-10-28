---
intent: 260923-gamification
unit: u9-badge-gallery
artifact: review-functional-design
stage: 3.1 functional-design
bolt: B10
version: review-01
reviewer: FE lead Nguyễn Hùng Sơn
date: 2026-10-15
verdict: READY
---
# Review 3.1 Functional Design: B10 `u9-badge-gallery`

## Verdict: READY

Không có Chặn. Một mâu thuẫn đã fix (F-01). Hai OQ chặn code-gen — cần trả lời trước 3.6.

## Checklist

| Hạng mục | Kết quả |
|---|---|
| Phủ US4 scope (badge gallery học viên) | Đạt — WF-1…WF-4, TC-501…519 |
| BR-4.1, 4.2, 4.4–4.7 + BR-1.7 | Đạt — rules.md đủ, BR-4.3 ghi nhận (F-02) |
| BR4.11…BR4.16 kỹ thuật (dạng số, sensor-safe) | Đạt |
| API đúng contract C-18 | Đạt — entities.md |
| Navigation entry từ B04 rõ | Đạt — BR4.16, WF điểm vào |
| BR4.7 vs BR4.11 mâu thuẫn | Đã fix lên v1.1 (F-01) |

## Findings

### F-01 — Đã fix (v1.1)
BR4.7 gốc nói "fetch mỗi lần tab mount" — mâu thuẫn với BR4.11 "cache in-session". Đã sửa BR4.7 thành: cache in-session (BR4.11), re-fetch khi reload trang / navigate ra ngoài / staleTime hết (React Query).

### F-02 — Ghi nhận
BR-4.3 không có trong rules.md. Nếu PRD US4 có BR-4.3 cần bổ sung; nếu không tồn tại hoặc N/A cần ghi chú. Kiểm tra khi có PRD ref đầy đủ.

### F-03 — Chuyển gate (chặn 3.6)
**OQ-B10-1** (route navigate) + **OQ-B10-3** (DEFAULT_BADGE_IMAGE path): hai câu hỏi này chặn code-gen. Cần tech lead xác nhận trước khi Sơn bắt đầu code bước D1 (navigate) và D3 (fallback image).

### F-04 — Ghi nhận
**OQ-B10-2** (mobile tooltip UX) + **OQ-B10-4** (grid mobile layout): không chặn bắt đầu code, nhưng chặn merge nếu chưa có design spec. Sơn có thể làm placeholder responsive trước.

## Gate

**[x] FE lead approve** — Nguyễn Hùng Sơn (2026-10-15): v1.1 đủ để lên 3.5 plan. F-03 (OQ-B10-1, OQ-B10-3) phải trả lời trước khi merge code 3.6. B10 3.1 PASS.
