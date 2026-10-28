---
intent: 260923-gamification
unit: u8-badges-config
artifact: functional-spec
stage: 3.1 functional-design
bolt: B09
version: 1.1
status: draft
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
---
# Functional Spec: U8 `u8-badges-config`

**FE focus.** Nghiệm thu qua TC-301…TC-322 (US9). Nguồn sự thật cho OpsSettingsPage khối Badges. Dữ liệu ở `entities.md`, rule ở `rules.md`.

## Phạm vi

| Có ở U8 | Không ở U8 |
|---|---|
| OpsSettingsPage khối Badges: toggle Badges, 4 loại, 8 mốc | Trao huy hiệu khi học viên học (U1 engine) |
| PATCH toggle Badges / từng loại | Hiện huy hiệu học viên (U9 `u9-badge-gallery`) |
| PATCH tên / mô tả / hình từng mốc | Thông báo huy hiệu thật (U6) |
| Upload ảnh mốc → ResourceLibrary | Bảng xếp hạng theo huy hiệu (U12) |
| BadgeBackfill job khi bật (BE cuongdq) | Cấu hình Levels khoá tiêu chí BADGES (U10) |

## Điểm vào

OpsSettingsPage (`features/gamification/src/pages/GamificationSettingsPage.tsx`) hiện có khối Points (B01). U8 thêm **khối Badges** cùng trang, layout tương tự.

## WF-1: Tải khối Badges

1. `OpsSettingsPage` mount (hoặc điều hướng tới) → `GET /ops/api/v1/gamification/badges`.
2. Response 200: `badges_enabled`, mảng `badge_types` (4 phần tử, mỗi phần tử có `type`, `is_enabled`, mảng `badges` 8 mốc với `id`, `milestone`, `name`, `description`, `image_url`).
3. Render khối theo cấu trúc bên dưới (WF-3).
4. Lỗi mạng: hiện skeleton → retry message, không crash trang.

## WF-2: Ghi cấu hình (auto-save, BR9.12)

```
Người dùng thao tác → PATCH → 200 → Saved
                             → 4xx/5xx → rollback + báo lỗi
```

| Thao tác | Trigger | Payload PATCH | Endpoint |
|---|---|---|---|
| Bật/tắt toggle `Badges` | click toggle | `{badges_enabled: true/false}` | `PATCH /gamification/badges` |
| Bật/tắt toggle loại | click toggle | `{badge_type: {type: "ACTIVITY", is_enabled: true/false}}` | `PATCH /gamification/badges` |
| Sửa tên mốc | blur (rời ô) | `{name: "Newbie"}` (rỗng → gửi `""`, BE trả defaultName) | `PATCH /gamification/badges/{id}` |
| Sửa mô tả mốc | blur | `{description: "..."}` hoặc `{description: null}` | `PATCH /gamification/badges/{id}` |
| Tải / chọn ảnh mốc | upload done / chọn từ kho | `{image_resource_id: "r-123"}` | `PATCH /gamification/badges/{id}` |

**Rollback toggle khi lỗi**: toggle trở về trạng thái trước, hiện toast lỗi (BR-14.11, TC-318).
**Debounce text**: không gửi khi đang gõ, chỉ gửi 1 request khi rời ô.

## WF-3: Cấu trúc UI khối Badges

```
┌─ Khối Badges ─────────────────────────────────────────────────────┐
│ [🔵 Toggle] Badges                                                  │
│ Award users with badges to highlight the milestones in their        │
│ learning journey.                                                   │
│ Ghi chú: Tắt Badges thì tiêu chí lên hạng theo huy hiệu cũng ngừng│
│                                                                     │
│ ┌─ Check-in badges [Toggle] ───────────────────────────────────┐   │
│ │ Awarded at 4, 8, 16, 32, 64, 128, 256, 512 check-in days.   │   │
│ │  Mốc 4  | [Hình] | [Ô tên] | [Ô mô tả]                     │   │
│ │  Mốc 8  | [Hình] | [Ô tên] | [Ô mô tả]                     │   │
│ │  ...                                                          │   │
│ └───────────────────────────────────────────────────────────────┘   │
│ ┌─ Activity badges [Toggle] ─── (tương tự) ────────────────────┐   │
│ ┌─ Test badges [Toggle] ──────── (tương tự) ────────────────────┐  │
│ ┌─ Course badges [Toggle] ─────── (tương tự) ───────────────────┐  │
└────────────────────────────────────────────────────────────────────┘
```

### Trạng thái UI theo toggle

| Trạng thái | Hành vi UI |
|---|---|
| `badges_enabled = false` | Toggle Badges tắt; mọi ô tên/hình/mô tả của cả 4 loại **không** bị khoá (vẫn chỉnh được — tắt Badges chỉ ẩn với học viên; vận hành vẫn cấu hình trước). Toggle từng loại vẫn hoạt động bình thường. Ghi chú cảnh báo luôn hiện. |
| `badge_type.is_enabled = false` | Toggle loại tắt; **8 mốc bên dưới loại đó bị disabled** (ô tên/mô tả disabled, nút hình disabled, nội dung cũ vẫn hiển thị — BR9.11, TC-315) |
| `badge_type.is_enabled = true` | Toggle loại bật; mọi ô sửa được; dòng "Awarded at …" hiện |

### Mốc (Badge row)

Mỗi mốc (hàng trong một loại):

| Phần tử | Mô tả |
|---|---|
| Giá trị mốc | Hiện dạng chỉ đọc (số), không có ô nhập (BR-9.2) |
| Hình | Hiện thumbnail ảnh hiện tại; nút chọn từ kho / tải lên; định dạng .png/.jpg/.jpeg/.webp/.svg ≤ 1MB (BR9.13) |
| Tên | Ô text; placeholder = defaultName; lưu khi blur; rỗng → về defaultName (BR-9.8) |
| Mô tả | Ô text đa dòng; không bắt buộc; xoá về null (TC-314) |

## WF-4: Upload ảnh mốc

1. Người dùng bấm "Chọn ảnh" / kéo thả.
2. FE kiểm định dạng và kích thước ở client (BR9.13); lỗi → hiện thông báo, không upload.
3. Tải lên ResourceLibrary qua `POST /lms/api/v1/resources/upload` (hàm `ModalUploadFile.tsx:48`) → nhận `resource_id`.
4. Tự động PATCH /badges/{id} `{image_resource_id: resource_id}` → 200.
5. FE cập nhật thumbnail từ response.
6. Xoá tài nguyên từ kho (ops khác) → ảnh mốc rơi về mặc định (BR-1.7, TC-313): FE xử lý khi ảnh 404 bằng fallback src.

## Kịch bản

| Kịch bản | Kết quả | Rule | TC |
|---|---|---|---|
| Tải khối: tenant mới | badges_enabled:false, 4 loại tắt, 32 mốc có tên/hình mặc định | BR-9.1, BR-9.2, BR-9.8 | TC-301 |
| Tắt Badges (không confirm) | PATCH 200, không modal; tiêu chí BADGES bị khoá (BE) | BR-9.6, BR-10.7 | TC-302 |
| Kiểm dòng giải thích | Nội dung cố định OQ-50 luôn hiện | US9-AC2 | TC-303 |
| Bật/tắt từng loại độc lập | PATCH cho loại đó, không ảnh hưởng loại khác | BR-9.5 | TC-304 |
| Dòng "Awarded at" bốn loại | Đúng dãy mốc, không dùng "every" | BR9.14 | TC-305 |
| Thử sửa milestone | Không có ô nhập; API trả 630004 | BR-9.2 | TC-307 |
| Nhập tên, rời ô | PATCH 200, "Saved"; tải lại vẫn đúng | BR-9.3, BR9.12 | TC-308 |
| Xoá trắng tên | Ô hiện lại tên mặc định; không lưu chuỗi rỗng | BR-9.8 | TC-309 |
| Tên 256 ký tự | 422|000405, tên giữ 255 | C-05 | TC-310 |
| Upload ảnh hợp lệ | PATCH image_resource_id 200 | BR9.13 | TC-311 |
| Upload ảnh sai định dạng/quá 1MB | 400|630005, hình không đổi | BR9.13, C-05 | TC-312 |
| Xoá tài nguyên ảnh | thumbnail → fallback mặc định, không vỡ | BR-1.7 | TC-313 |
| Nhập và xoá mô tả | Lần 1 lưu; lần 2 trả null, không lỗi bắt buộc | US9-AC10 | TC-314 |
| Loại tắt → ô mốc disabled | Ô không sửa được, nội dung vẫn hiển thị | BR9.11 | TC-315 |
| Tìm nút tạo/xoá | UI không có; API không có route | BR-9.7 | TC-316 |
| Không có nút lưu | Network log: PATCH khi blur/click | BR9.12 | TC-317 |
| PATCH trả 500 khi bấm toggle | Toggle rollback, hiện toast lỗi | BR-14.11 | TC-318 |
| SA đổi tên/hình mốc → học viên thấy ngay | Học viên xem My Profile Badges thấy tên/hình mới | BR-9.4 | TC-319 |
| Tắt Check-in badges → HV tải Badges | Nhóm Check-in biến; DB giữ 2 huy hiệu; bật lại hiện đủ | BR-9.5 | TC-320 |
| Tắt Badges → HV học hoàn thành | Không trao huy hiệu, không tab Badges | BR-9.6 | TC-321 |
| Bật Badges + loại → học viên nhận huy hiệu bù | Huy hiệu đủ điều kiện xuất hiện, không thông báo | BR-9.9 | TC-322 |

## Ghi chú

- **SP ước tính 3.5**: 2 ngày (Sơn FE) — OpsSettingsPage khối Badges (toggle, 4 loại, mốc, auto-save, upload ảnh). Xem 3.5 plan.
- **Cho PO — OQ-50 (chuỗi toggle Badges)**: chuỗi giải thích tắt Badges cần PO duyệt text tiếng Anh trước 3.6. TC-303 cần text chốt.
- **Cho PO — OQ-51 (định dạng/kích thước ảnh)**: đã chốt .png/.jpg/.jpeg/.webp/.svg ≤ 1MB (2.43 Q12, C-05).
- **Code có sẵn**: `GamificationSettingsPage.tsx` (WT B01) có layout khối Points làm mẫu. `ModalUploadFile` (`libs/ui/src/base/upload-file/ModalUploadFile/ModalUploadFile.tsx:48`) dùng lại cho chọn ảnh.
