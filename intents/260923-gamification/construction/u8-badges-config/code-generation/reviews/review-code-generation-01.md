---
intent: 260923-gamification
unit: u8-badges-config
artifact: review-code-generation-plan
stage: 3.5 code-generation-plan
bolt: B09
version: review-01
reviewer: FE lead Nguyễn Hùng Sơn
date: 2026-10-15
verdict: READY
---
# Review 3.5 Code-Generation Plan: B09 `u8-badges-config`

## Verdict: READY

Không có Chặn. Plan đủ để vietlh/cuongdq code theo.

## Checklist

| Hạng mục | Kết quả |
|---|---|
| Phủ toàn bộ WF-1…WF-4 | Đạt — B1/C1 (WF-1), D1 (WF-2), C2 (WF-3), C4 (WF-4) |
| BR9.11…BR9.14 có bước tương ứng | Đạt — C2/C3 (BR9.11), D1 (BR9.12), C4 (BR9.13), C2 MILESTONE_LABELS (BR9.14) |
| BR-9.2 milestone chỉ đọc | Đạt — C3: span-only, không input |
| BR-9.8 xoá trắng tên | Đạt — C3 onBlur gửi '' + D1 update từ response |
| BR-1.7 ảnh 404 fallback | Đạt — C4 onError fallback src |
| BR-14.11 rollback toggle | Đạt — D1 rollback pattern |
| Contract C-05 | Đạt — B2 API methods dùng đúng endpoint /gamification/badges |
| Test coverage TC-301…TC-318 | Đạt — E1 12 TC, E2 2 integration |
| BE rõ ràng tách khỏi FE | Đạt — Nhóm A ghi nhận cuongdq, FE không làm thêm |
| File paths hợp lệ | Đạt — ModalUploadFile.tsx:48, GamificationSettingsPage.tsx đúng |

## Findings

### F-01 — Ghi nhận
`POST /lms/api/v1/resources/upload` là URL giả định. Cần cuongdq xác nhận path thực tế của ResourceLibrary upload endpoint trước khi code Bước C4.

**Xử lý**: Không chặn code — `ModalUploadFile.tsx:48` đã đóng gói endpoint; FE chỉ gọi hàm component, không hardcode URL.

## Điều kiện gate

Gate **conditional**:
- cuongdq xác nhận Nhóm A (Migration + Entities + OpsService): không chặn Sơn bắt đầu Nhóm B+C song song
- ResourceLibrary upload endpoint xác nhận trước khi merge C4

## Gate

**[x] FE lead approve** — Nguyễn Hùng Sơn (2026-10-15): plan v1.0 đủ để bắt đầu code FE. B09 3.5 PASS. B10 mở khoá sau khi B04 cũng pass 3.5.
