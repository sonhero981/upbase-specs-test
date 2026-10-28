---
intent: 260923-gamification
unit: u8-badges-config
artifact: rules
stage: 3.1 functional-design
bolt: B09
version: 1.1
status: draft
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
---
# Business Rules: U8 `u8-badges-config`

Mã `BR-9.x` = PRD v0.14 US9. Rule kỹ thuật FE đánh tiếp `BR9.11`. Thẻ `[C-n]` = contract-summary.md; `[BR-n.n]` = rule PRD US khác liên quan.

```yaml
rules:
  # ---- Cấu trúc dữ liệu ----
  - id: BR-9.1
    statement: "Bốn loại huy hiệu là danh sách cố định; vận hành không tạo loại mới."
    category: constraint
    applies_to: OpsSettingsPage (khối Badges)
    trigger: "Tải khối Badges"
    logic: "API luôn trả đúng bốn phần tử CHECKIN, ACTIVITY, TEST, COURSE theo thứ tự đó. UI không có nút tạo thêm."
    source: "PRD BR-9.1, US9-AC12"

  - id: BR-9.2
    statement: "Giá trị mốc do hệ thống định sẵn và không sửa được."
    category: constraint
    applies_to: OpsSettingsPage (mốc huy hiệu)
    trigger: "Hiển thị mốc"
    logic: "UI hiện giá trị mốc dạng chỉ đọc (không có ô nhập). PATCH {milestone:n} bị từ chối 400|630004. Dãy cố định: Check-in 4,8,16,32,64,128,256,512 · Activity 10,25,50,100,200,400,800,1600 · Test 2,4,8,16,32,64,128,256 · Course 1,2,4,8,16,32,64,128"
    violation: "Không có ô nhập milestone trên UI; API trả 630004"
    source: "PRD BR-9.2, US9-AC7, TC-307"

  - id: BR-9.3
    statement: "Vận hành đặt được tên, hình và mô tả cho từng mốc."
    category: policy
    applies_to: OpsSettingsPage (ô tên, hình, mô tả của từng mốc)
    trigger: "Chỉnh sửa tên / tải hình / nhập mô tả"
    logic: "Tên, mô tả: ô nhập text; lưu khi rời ô (BR9.12). Hình: chọn từ ResourceLibrary hoặc tải lên (BR9.13). Mỗi thay đổi một PATCH đến /badges/{id}."
    source: "PRD BR-9.3, US9-AC8, US9-AC9, US9-AC10"

  - id: BR-9.4
    statement: "Đổi tên hoặc hình áp ngay cho tất cả học viên kể cả người đã đạt."
    category: policy
    applies_to: OpsSettingsPage (ghi nhận sau lưu)
    trigger: "Sau PATCH 200"
    logic: "Không trao lại, không sinh thông báo. BE áp ngay; FE không cần invalidate cache đặc biệt ngoài refetch dữ liệu thường."
    source: "PRD BR-9.4, TC-319"

  - id: BR-9.5
    statement: "Tắt một loại huy hiệu → huy hiệu loại đó biến khỏi giao diện học viên; dữ liệu giữ nguyên."
    category: policy
    applies_to: OpsSettingsPage (toggle từng loại)
    trigger: "Bật/tắt toggle loại"
    logic: "PATCH {badge_type: {type: X, is_enabled: false}}. FE không xoá dữ liệu. Học viên không thấy loại đó. Bật lại: hiện lại đủ."
    source: "PRD BR-9.5, BR-1.4a, TC-320"

  - id: BR-9.6
    statement: "Tắt công tắc Badges → toàn bộ phần huy hiệu biến khỏi giao diện học viên; tiêu chí lên hạng theo huy hiệu khoá theo."
    category: policy
    applies_to: OpsSettingsPage (toggle Badges)
    trigger: "Tắt toggle Badges"
    logic: "PATCH {badges_enabled: false}. Không có hộp xác nhận (US9-AC1). Tiêu chí BADGES bị khoá (BR-10.7) — BE xử lý; FE hiện cảnh báo cố định ở khối Levels. Toggle loại bên dưới không khoá nhưng không ảnh hưởng vì Badges tổng đang tắt."
    source: "PRD BR-9.6, BR-10.7, TC-302, TC-321"

  - id: BR-9.7
    statement: "Không có thao tác tạo mới hoặc xoá huy hiệu."
    category: constraint
    applies_to: OpsSettingsPage
    trigger: "Toàn bộ khối Badges"
    logic: "UI không có nút tạo/xoá. API không có POST /badges hay DELETE /badges/{id}."
    source: "PRD BR-9.7, US9-AC12, TC-316"

  - id: BR-9.8
    statement: "Tên và hình luôn có giá trị; xoá trắng tên → quay về tên mặc định."
    category: validation
    applies_to: OpsSettingsPage (ô tên mốc)
    trigger: "Rời ô tên với giá trị rỗng"
    logic: "PATCH {name: ''} → BE trả về name = default_name. FE update lại ô từ response (không lưu chuỗi rỗng). Hình: có ảnh mặc định, xoá tài nguyên → rơi về mặc định (BR-1.7)."
    source: "PRD BR-9.8, TC-309, TC-313"

  - id: BR-9.9
    statement: "Bật Badges hoặc bật lại một loại thì trao bù ngay; không thông báo."
    category: policy
    applies_to: GamificationSettingsOpsApi, BadgeBackfill (BE)
    trigger: "PATCH {badges_enabled: true} hoặc {badge_type: {type, is_enabled: true}}"
    logic: "FE chỉ phát PATCH và xử lý 200. BE phát việc trao bù (BadgeBackfill A-04). FE không cần làm gì thêm; học viên tự thấy huy hiệu bù khi tải My Profile."
    source: "PRD BR-9.9, TC-322"

  - id: BR-9.10
    statement: "Số huy hiệu (ô {n} Badges) chỉ đếm loại đang bật."
    category: calculation
    applies_to: LearnerGamificationApi, LmsGamificationFeature (U5, B04)
    trigger: "API /me đọc số huy hiệu"
    logic: "Không phải FE của U8 tính. Ghi nhận để biết tắt/bật loại ảnh hưởng chỉ số học viên ngay."
    source: "PRD BR-9.10"

  # ---- Rules kỹ thuật FE ----
  - id: BR9.11
    statement: "Khối Badges khoá toàn bộ ô tên/hình/mô tả của một loại khi loại đó đang tắt."
    category: policy
    applies_to: OpsSettingsPage (khối từng loại)
    trigger: "is_enabled = false của loại"
    logic: "Tám mốc của loại đang tắt: ô tên và mô tả disabled, nút chọn hình disabled. Nội dung đã đặt vẫn hiển thị (không ẩn). Bật lại loại: ô sửa được lại."
    source: "PRD US9-AC11, TC-315"

  - id: BR9.12
    statement: "Tự lưu khi rời ô (tên, mô tả) hoặc khi bấm toggle (Badges, từng loại); không có nút lưu."
    category: policy
    applies_to: OpsSettingsPage
    trigger: "blur event (text) / click (toggle)"
    logic: "Tên và mô tả: gửi PATCH khi rời ô (không gửi khi đang gõ). Hình: gửi PATCH khi tải lên xong. Toggle: gửi PATCH khi bấm, không hỏi lại. Mỗi lần lưu thành công hiện 'Saved'. Lỗi: toggle về trạng thái đã lưu, báo lỗi tại ô (BR-14.10, BR-14.11)."
    source: "PRD BR-14.10, BR-14.11, US9-AC13, TC-317, TC-318"

  - id: BR9.13
    statement: "Hình mốc chọn từ ResourceLibrary hoặc tải lên; định dạng .png/.jpg/.jpeg/.webp/.svg ≤ 1MB."
    category: validation
    applies_to: OpsSettingsPage (chọn hình)
    trigger: "Chọn / tải ảnh"
    logic: "Sai định dạng hoặc quá 1MB → báo lỗi 400|630005, hình giữ nguyên (C-05). Tải thành công → PATCH {image_resource_id} ngay sau."
    source: "PRD US9-AC9, C-05, 2.43 Q12, TC-311, TC-312"

  - id: BR9.14
    statement: "Dòng tóm tắt mốc dùng format 'Awarded at {dãy} {đơn vị}.' — không dùng 'every'."
    category: display
    applies_to: OpsSettingsPage (mỗi loại)
    trigger: "Render loại"
    logic: "Ví dụ: 'Awarded at 4, 8, 16, 32, 64, 128, 256, 512 check-in days.' Bốn đơn vị: check-in days · activities · passed tests · completed courses. Tuyệt đối không dùng 'every' (dễ lẫn với Levels BR-10.2)."
    source: "PRD US9-AC6, TC-305, TC-306"
```

## Tóm tắt

| ID | Rule | Loại | Thuộc |
|---|---|---|---|
| BR-9.1 | 4 loại cố định | constraint | UI |
| BR-9.2 | Mốc chỉ đọc | constraint | UI + BE |
| BR-9.3 | Tên/hình/mô tả chỉnh được | policy | UI |
| BR-9.4 | Đổi nội dung áp ngay | policy | BE (FE không làm thêm) |
| BR-9.5 | Tắt loại → ẩn với học viên | policy | BE (FE phát PATCH) |
| BR-9.6 | Tắt Badges → khoá tiêu chí | policy | BE (FE phát PATCH) |
| BR-9.7 | Không tạo/xoá | constraint | UI |
| BR-9.8 | Xoá trắng → về mặc định | validation | UI |
| BR-9.9 | Bật → trao bù ngay (BE) | policy | BE |
| BR-9.10 | Đếm chỉ loại đang bật | calculation | BE |
| BR9.11 | Loại tắt → ô disabled | policy | UI |
| BR9.12 | Auto-save (blur/toggle) | policy | UI |
| BR9.13 | Định dạng/kích thước ảnh | validation | UI |
| BR9.14 | Format "Awarded at" | display | UI |
