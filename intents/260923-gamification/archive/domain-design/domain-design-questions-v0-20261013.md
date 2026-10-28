# Domain Design, câu hỏi
Intent: 260923-gamification · Người trả lời: BE lead · Cách trả lời: Chat · Đã trả lời: 4/4 ([GIẢ LẬP] BE lead, test workflow)

Câu kỹ thuật chuyển từ 2.43 (OQ-T1, OQ-T2) và chỗ lát này đổi so với design gốc `upbase-221099-gamification`. Không hỏi PO.

## Q1. Endpoint gamification bên Ops giữ `tags: []` theo `backend.md` § 2, hay `tags` mang mã quyền? (OQ-T1)
Vì sao hỏi: `tags: []` → route không có dòng `p` → mọi staff gọi được (`permission.service.ts:94-105`), trái BR-15.3 và spec BE "không có quyền → 403".
A. `tags` mang mã quyền, ngoại lệ chỉ cho nhóm gamification  [đề xuất, ADR-002]
B. Giữ `tags: []`, chấp nhận mở tới khi BA điền
C. Giữ `tags: []`, kiểm quyền trong service
X. Khác
Chặn: có
[Answer]: [GIẢ LẬP BE lead] A, "Đồng ý ngoại lệ cho gamification vì spec của tôi cũng ghi 403. Tôi sẽ ghi ngoại lệ vào backend.md."

## Q2. Bộ mã quyền nào là chuẩn? (OQ-T2)
A. `gr_view_gamification_settings`, `gr_update_gamification_settings`, `gr_view_gamification_learners`  [đề xuất, theo design.md:367-369]
B. `gr_view_gamification_config`, `gr_update_gamification_config`, `gr_view_gamification_learners` (prd.md:771)
X. Khác
Chặn: có
[Answer]: [GIẢ LẬP BE lead] A, "Dùng bộ settings; phần FE trong PRD viết nhầm."

## Q3. Bỏ cache trong bộ nhớ 30 giây (đầu việc 3 design gốc), chỉ giữ Redis xoá khi ghi?
Vì sao hỏi: PO chốt công tắc có hiệu lực ngay khi lưu (2.43 Q3); cache 30 giây ở từng tiến trình không xoá được từ tiến trình khác.
A. Chỉ Redis, xoá khi ghi  [đề xuất, ADR-003]
B. Giữ in-memory, thêm pub/sub xoá
X. Khác
Chặn: có
[Answer]: [GIẢ LẬP BE lead] A, "Đồng ý. Đo lại tải Redis ở Unit Điểm."

## Q4. Đổi `PUT /settings` (2 công tắc + timezone) thành `PATCH` từng trường, bỏ timezone khỏi API, thêm `visibility_first_enabled_at`?
A. Đồng ý cả ba  [đề xuất, ADR-004, ADR-005]
B. Giữ PUT, thêm kiểm phiên bản
X. Khác
Chặn: có
[Answer]: [GIẢ LẬP BE lead] A, "Đồng ý. Tôi cập nhật design.md, design.dbml của change upbase-221099 cho khớp."

## Consolidated Summary
- `tags` mang mã quyền cho endpoint gamification (ngoại lệ ghi vào `backend.md`).
- Mã quyền chuẩn: `gr_view_gamification_settings`, `gr_update_gamification_settings`, `gr_view_gamification_learners`.
- Cache cấu hình chỉ Redis theo tenant, xoá khi ghi.
- PATCH từng trường; timezone chỉ là cột tenant; thêm `visibility_first_enabled_at`.

Xác nhận: [GIẢ LẬP BE lead] Looks correct.
