# Contract Design, câu hỏi
Intent: 260923-gamification · Người trả lời: BE lead · Cách trả lời: Chat · Đã trả lời: 6/6 ([GIẢ LẬP] BE lead, test workflow)

Phạm vi cả intent (DEC-T15). Đầu vào: 2.7 v2.0 (DEC-T20), 2.6 v2.0 (DEC-T19), code lms-be `origin/feature/gamification` @9006b80. Không API public / external.

## Q1. Mã lỗi gamification dùng dải nào?
Vì sao hỏi: contract C-02 v1.0 (B01) dùng `400|700001`; WP3 đã dùng dải `630xxx` (`libs/constants/src/lib/exceptions/exceptions.code.ts:635-645`), `630001` còn trống.
A. Dùng dải `630xxx`: `GAMIFICATION_DISABLED = 400|630001`, mã mới tiếp theo `630012…630015`; C-02 đổi theo (B01 chưa code nên không ảnh hưởng code)  [đề xuất]
B. Giữ `700001` cho khối chung, WP3 giữ `630xxx`
X. Khác
Chặn: có
[Answer]: [GIẢ LẬP BE lead] A

## Q2. Giới hạn giá trị của WP3 trái PRD — giữ hay bỏ?
Vì sao hỏi: WP3 chặn điểm hành động 1–1000, điểm nền check-in 1–40 (`gamification-point-rule.service.ts:11-16`), bội số POINTS ≤ 1.000.000, COURSES ≤ 1000, BADGES ≤ 32, trần hạng 2–1000 (`gamification-level-setting.service.ts:11-17`). PRD: điểm, điểm nền không giới hạn trên (BR-8.5, BR-8.5a, rủi ro PO chấp nhận 06/10); trần hạng ≥ 2, không có trần trên.
A. Bỏ trần trên nghiệp vụ, giữ trần kỹ thuật int32 (2.147.483.647) để tổng điểm không tràn; giữ BADGES ≤ 32 vì chỉ có 32 mốc  [đề xuất]
B. Giữ giới hạn WP3, báo PO đổi PRD
X. Khác
Chặn: có
[Answer]: [GIẢ LẬP BE lead] A, "Giới hạn đó tôi đặt tạm, theo PRD."

## Q3. Ghi cấu hình huy hiệu: PATCH một khối hay tách?
Vì sao hỏi: ADR-004 bắt ghi từng trường; khối Badges có hai cấp công tắc và 32 mốc mỗi mốc ba trường.
A. `PATCH /gamification/badges` (badges_enabled hoặc một loại) + `PATCH /gamification/badges/{id}` (một trường của một mốc)  [đề xuất]
B. Một PATCH với đường dẫn trường trong body
X. Khác
Chặn: có
[Answer]: [GIẢ LẬP BE lead] A

## Q4. Shape phân trang?
Vì sao hỏi: Ops trả `Success({ metadata, <khoá danh sách> })` với tên khoá không thống nhất (`apps/ops/src/caching-settings/caching-settings.service.ts:32-57` dùng `caching_setttings`), chỗ khác dùng `meta`; `PaginationSuccess` trả `{ data, meta }`; `next_page` là boolean (`response.dto.ts:12-18`).
A. Mọi list gamification (Ops và lms) trả `{ success, data: { items, metadata: PaginationMeta } }`, query `page_index`, `page_size` theo `PaginationDto`  [đề xuất, theo mẫu Ops gần nhất]
B. `PaginationSuccess` `{ success, data, meta }`
X. Khác
Chặn: không
[Answer]: [GIẢ LẬP BE lead] A

## Q5. Version payload Kafka và socket?
Vì sao hỏi: `backend.md` § 4 không có rule version; payload WP1 không có field version.
A. Không thêm field version; chỉ thay đổi additive, consumer bỏ qua field lạ; breaking thì topic mới  [đề xuất]
B. Thêm `schema_version` vào mọi payload
X. Khác
Chặn: không
[Answer]: [GIẢ LẬP BE lead] A

## Q6. Kết nối socket.io (gateway mới ở app lms)?
A. Cùng host API lms, path `/lms/socket.io`, namespace `/gamification`, `auth.token` = Bearer như LmsGuard, room `user:{id}`, event `gamification:achievements`  [đề xuất, ADR-008]
B. Host riêng cho realtime
X. Khác
Chặn: có
[Answer]: [GIẢ LẬP BE lead] A, "DevOps cần mở route websocket qua gateway; tôi ghi vào 3.4 của U6."

## Consolidated Summary
- Mã lỗi `630xxx`; C-02 đổi `700001` → `630001`; mới `630012…630015`.
- Bỏ trần trên của WP3 cho điểm, điểm nền, bội số POINTS/COURSES, trần hạng; giữ int32 và BADGES ≤ 32.
- Badges: PATCH loại + PATCH từng mốc.
- Phân trang `{ items, metadata }`; không version payload, additive.
- Socket `/lms/socket.io`, namespace `/gamification`, room theo user; U6 cần 3.4 cho route websocket.

Xác nhận: [GIẢ LẬP BE lead] Looks correct.
