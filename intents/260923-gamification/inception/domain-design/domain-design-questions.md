# Domain Design, câu hỏi
Intent: 260923-gamification · Người trả lời: BE lead · Cách trả lời: Chat · Đã trả lời: Lô 1 4/4, Lô 2 8/8 ([GIẢ LẬP] BE lead, test workflow)

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

## Lô 2 — cả intent (2026-10-13, DEC-T15)
Người trả lời: BE lead · Đã trả lời: 8/8 ([GIẢ LẬP] BE lead, test workflow)

Chỗ catalogue cả intent lệch design gốc `upbase-221099-gamification` hoặc lệch code đã có trên `origin/feature/gamification` @9006b80 (WP0, WP3, WP1), cộng OQ-T3, OQ-T4 chuyển từ 2.43. Không hỏi PO.

## Q5. Ghi nhận qua Kafka (WP1 đã code) hay gọi engine trong luồng như PRD và design gốc?
Vì sao hỏi: PRD `Solution › TDD` (`prd.md:211`) chốt "tính trong luồng, không qua hàng đợi"; design gốc luồng 1 vẽ hook gọi engine trong luồng. WP1 đã làm `GamificationRecordPublisher.publish` → Kafka `process_gamification_record` → event-processor (`gamification-record.publisher.ts:23`, `gamification-record.handler.ts:14`). Học viên thấy điểm trễ thêm một nhịp Kafka.
A. Giữ Kafka như WP1: publish sau commit, không chặn thao tác học; mục tiêu thông báo ≤ 3 giây (2.43 Q14); báo PO lệch câu "không qua hàng đợi"  [đề xuất, ADR-009: code đã có, bảo vệ NFR-GAM-01 tốt hơn, có failed_events khi publish lỗi]
B. Gọi `engine.record` trực tiếp trong request học sau commit (như luồng 1 design gốc), bỏ publisher của WP1
X. Khác
Chặn: có
[Answer]: [GIẢ LẬP BE lead] A, "Giữ Kafka, WP1 đã verify. Ghi chú cho PO là được."

## Q6. Check-in bắt ở đâu để chỉ tính khi học viên chủ động mở UpLMS? (OQ-T3)
Vì sao hỏi: design gốc hook `LmsGuard` ở mọi request đã xác thực (`lms.guard.ts:38`), trái BR-5.1 (request nền, socket, refetch không tính). BE không phân biệt được request nền: không có header client riêng.
A. lms-fe gọi một endpoint check-in riêng khi có tương tác thật (lần thao tác đầu sau khi tải trang hoặc sau khi tab quay lại visible, hoặc điều hướng route), tối đa một lần mỗi ngày phía client; BE giữ `SET NX` + Kafka + unique theo ngày; bỏ hook trong `LmsGuard`  [đề xuất, ADR-010]
B. Giữ hook `LmsGuard`, lms-fe gắn header `x-user-active: 1` cho request do người dùng gây ra
X. Khác
Chặn: có
[Answer]: [GIẢ LẬP BE lead] A, "Endpoint riêng dễ kiểm hơn header. Bỏ hook ở LmsGuard."

## Q7. US12 khoảng tự do và US22 nhật ký đọc thẳng ledger hay cần bảng tổng hợp? (OQ-T4)
Vì sao hỏi: ledger ghi cả dòng 0 điểm cho mọi hoạt động, giữ vĩnh viễn; 2.43 Q14 đặt ≤ 2 giây/trang với 10.000 học viên, 5 triệu dòng.
A. Đọc ledger + `user_stats` với index hiện có (WP0 migration :285-291) cộng index `(tenant_id, occurred_at)`, `(tenant_id, user_id, occurred_at)`; đo ở 3.2/3.6, chỉ thêm bảng tổng hợp theo ngày nếu không đạt  [đề xuất, ADR-014]
B. Thêm ngay bảng tổng hợp theo (user, ngày, chỉ số)
X. Khác
Chặn: có
[Answer]: [GIẢ LẬP BE lead] A, "Đo trước, tối ưu sau."

## Q8. WP3 đã code `PUT` năm khối, `tags: []`, nhận `timezone`, `security` chỉ có group — sửa thế nào, và B01 có phải đổi plan không?
Vì sao hỏi: ADR-002 (tags mang mã quyền) và ADR-004 (PATCH từng trường, bỏ timezone) đã duyệt cho B01 (DEC-T6), nhưng WP3 (`gamification-setting.controller.ts:18,35-196`) làm ngược cả ba; `security` không có tên quyền nên màn role không có quyền nào để gán. Plan B01 v1.1 viết như thể phần cấu hình chung chưa có.
A. Sửa WP3 tại chỗ: khối chung theo B01 (PATCH, bỏ timezone, có `visibility_first_enabled_at`); mọi endpoint WP3 khai tên quyền + `tags` ngay trong B01; bốn khối còn lại đổi sang PATCH ở Bolt của Unit tương ứng. Mở lại 3.5 plan B01 `[R]` để viết lại delta trên WP3 trước khi code  [đề xuất, ADR-016]
B. Giữ PUT cả khối của WP3, ops-fe gửi cả khối và tự gom lần lưu
X. Khác
Chặn: có
[Answer]: [GIẢ LẬP BE lead] A, "Đồng ý. cuongdq viết WP3 trước khi có ADR-002/004; B01 sửa lại, tôi cập nhật assignment."

## Q9. Đóng băng campaign: chờ 24 giờ (2.43 Q8) hay 15 phút + hết sự kiện lỗi như design gốc?
Vì sao hỏi: design gốc luồng 6 chờ 15 phút và không còn `failed_events PENDING` trước biên (tối đa ~75 phút vì 5 lần × 15 phút); PO giả lập chọn chờ 24 giờ.
A. Theo PO: đóng băng khi đã qua biên kết thúc 24 giờ **và** không còn PENDING trước biên; giữ advisory lock và `version = 0` của design gốc  [đề xuất, ADR-013]
B. Giữ 15 phút, báo PO
X. Khác
Chặn: không
[Answer]: [GIẢ LẬP BE lead] A

## Q10. Export US12, US21: server dựng xlsx (design gốc, exceljs) hay trả JSON cho ops-fe dựng như các màn Ops khác?
Vì sao hỏi: mọi export Ops hiện có trả JSON, ops-fe dựng bằng exceljs (`apps/ops/src/users/users.controller.ts:496`, ops-fe `libs/utils/src/helpers/export.ts:409,585`); design gốc đầu việc 13, 14 dựng `.xlsx` ở server.
A. Trả JSON không phân trang (giới hạn 50.000 dòng, 2.43 Q14), ops-fe dựng xlsx theo helper sẵn có  [đề xuất, ADR-014, theo pattern repo]
B. Server dựng xlsx
X. Khác
Chặn: không
[Answer]: [GIẢ LẬP BE lead] A


## Q11. Phân biệt học viên bị Block trước hay sau lúc campaign kết thúc bằng cách nào? (review R-05)
Vì sao hỏi: C12 cần mốc, nhưng `users` chỉ có `status` (`user.entity.ts:86-88`), và đóng băng dời tới 24 giờ sau kết thúc (ADR-013).
A. Chốt danh sách người tham gia đủ điều kiện ở lần chạy job đầu tiên sau biên kết thúc (bảng `CampaignParticipant` mới), đóng băng tính trên danh sách đó; sai số ≤ 15 phút  [đề xuất, ADR-017]
B. Thêm `blocked_at`, `left_at` vào `users`
X. Khác
Chặn: có
[Answer]: [GIẢ LẬP BE lead] A, "Không đụng bảng users. Sai số 15 phút chấp nhận."

## Q12. Con trỏ `leaderboard_version` nằm trong bản ghi cấu hình có cache 1 giờ — đổi và đọc thế nào? (review R-06)
A. Đổi qua hàm của `GamificationConfig` (ghi + xoá cache cùng bước), đọc con trỏ không qua cache dài, giữ thêm version liền trước một chu kỳ  [đề xuất, ADR-018]
B. Tách con trỏ ra key Redis riêng không TTL
X. Khác
Chặn: không
[Answer]: [GIẢ LẬP BE lead] A

## Consolidated Summary (Lô 2)
- Ghi nhận qua Kafka như WP1 (lệch câu PRD "không qua hàng đợi", báo PO).
- Check-in qua endpoint riêng do lms-fe gọi khi có tương tác thật; bỏ hook `LmsGuard`.
- US12, US22 đọc ledger + stats với index; đo rồi mới thêm bảng tổng hợp.
- Sửa WP3 theo ADR-002/004 trong B01; mở lại 3.5 plan B01 `[R]`.
- Đóng băng campaign sau biên kết thúc 24 giờ và hết PENDING.
- Export trả JSON, ops-fe dựng xlsx, ≤ 50.000 dòng.
- Chốt người tham gia campaign ở biên kết thúc (bảng mới), đóng băng tính trên danh sách đó.
- Con trỏ leaderboard đổi qua Config, đọc không qua cache dài.

Xác nhận: [GIẢ LẬP BE lead] Looks correct.
