---
intent: 260923-gamification
artifact: decisions
stage: 2.6 domain-design
version: 2.0
status: approved
approved_at: 2026-10-13 (FE lead + [GIẢ LẬP] BE lead, DEC-T19)
review: review-domain-design-01 NOT-READY → sửa; review-domain-design-02 READY → sửa R-15…R-17
previous: 1.0 approved 2026-10-13 (DEC-T6), ADR-001…007
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
scope: cả intent, 19 US (DEC-T15)
---
# Decisions: Gamification, cả intent

ADR theo template AWS (`engine/tech/aidlc/knowledge/aidlc-architect-agent/adr-template.md`). Intent v1 không có HLD Brief nên hướng kỹ thuật của lát ghi ở đây. Thiết kế BE gốc: lms-be `openspec/changes/upbase-221099-gamification` (DEC-T1); ADR nào đổi bản đó ghi rõ "Đổi so với design gốc" và cần BE lead ký. `file:line` kiểm trên `origin/staging` (lms-be 610f100, ops-fe 1e01033bf).

## ADR Index

| ADR | Title | Status | Date |
|---|---|---|---|
| 001 | Dựng tiếp trên WP0 của team BE (`origin/feature/gamification`), chỉ làm delta của lát | Accepted (sửa sau review, DEC-T14) | 2026-10-13 |
| 002 | Quyền: `tags` mang mã quyền cho endpoint gamification (ngoại lệ `tags: []`) | Accepted | 2026-10-13 |
| 003 | Cache cấu hình chỉ ở Redis theo tenant, xoá khi ghi; bỏ cache trong bộ nhớ 30 giây | Accepted | 2026-10-13 |
| 004 | Ghi cấu hình bằng PATCH từng trường; múi giờ không nằm trong API cấu hình | Accepted | 2026-10-13 |
| 005 | Lưu mốc bật Visibility lần đầu để quyết popover ra mắt | Accepted | 2026-10-13 |
| 006 | Lát Nền tảng chạm lms-be + ops-fe, không chạm lms-fe | Accepted | 2026-10-13 |
| 007 | Giữ seed của WP0 cho tenant có sẵn; tenant mới tạo khi đọc lần đầu | Accepted (sửa sau review, DEC-T14) | 2026-10-13 |
| 008 | Mở rộng catalogue cả intent trên nhánh `feature/gamification` (WP0, WP3, WP1) | Accepted (DEC-T19) | 2026-10-13 |
| 009 | Ghi nhận qua Kafka như WP1 (lệch PRD "không qua hàng đợi") | Accepted (DEC-T19) | 2026-10-13 |
| 010 | Check-in bằng endpoint riêng do lms-fe gọi khi có tương tác thật | Accepted (DEC-T19) | 2026-10-13 |
| 011 | Tiêu chí hạng theo huy hiệu đọc bộ đếm chỉ tăng | Accepted (DEC-T19) | 2026-10-13 |
| 012 | Lần ghi nhận lỗi tự chạy lại, không có màn Ops | Accepted (DEC-T19) | 2026-10-13 |
| 013 | Đóng băng campaign sau biên kết thúc 24 giờ và hết sự kiện lỗi chờ | Accepted (DEC-T19) | 2026-10-13 |
| 014 | Dữ liệu Ops đọc ledger + stats có index; export trả JSON | Accepted (DEC-T19) | 2026-10-13 |
| 015 | lms-fe dựng tiếp từ nhánh WIP gamification-feature | Accepted (DEC-T19) | 2026-10-13 |
| 016 | Sửa WP3 theo ADR-002, ADR-004; mở lại plan B01 | Accepted (DEC-T19) | 2026-10-13 |
| 017 | Chốt người tham gia campaign tại biên kết thúc | Accepted (DEC-T19) | 2026-10-13 |
| 018 | Con trỏ leaderboard_version đổi qua GamificationConfig, đọc không qua cache dài | Accepted (DEC-T19) | 2026-10-13 |

---

## ADR-001: Dựng tiếp trên WP0 của team BE, chỉ làm delta của lát

### Status
Accepted (DEC-T14, sửa sau `construction/u0-foundation/code-generation/reviews/review-code-generation-01.md` R-01, R-02)

### Context
Design gốc của toàn intent là change `upbase-221099-gamification` (BE lead, PRD v0.14). Lần quét đầu chỉ tới `c279942` nên kết luận "chưa có code". Thực tế `origin/feature/gamification` có `65d3aad` "feat: gamification WP0 foundation" (VietLH, 12/10, 51 file): `tenant.timezone`, 10 bảng có RLS, seed mặc định, entity, repository, constants, module rỗng ở `apps/ops/src/gamification-setting/`. `assignment.md` giao WP0 cho vietlh, WP3 (cấu hình Ops) cho cuongdq. Convention `openspec/conventions/*` cũng chỉ có trên nhánh này, không có trên `origin/staging`.

### Decision
Phần lms-be của B01 cắt branch cá nhân từ `feature/gamification` và chỉ làm delta: cột `visibility_first_enabled_at` (ADR-005), service + controller cấu hình chung, khai quyền (ADR-002). Giữ nguyên lựa chọn của WP0: `GamificationSetting extends AbstractEntity`, seed, đường dẫn module `apps/ops/src/gamification-setting/`, key Redis `GAMIFICATION_REDIS_KEYS.CONFIG`. Phần "cấu hình chung + quyền" của WP3 chuyển sang B01; BE lead cập nhật `assignment.md` (ED-07). Nhánh `origin/draft/gamification` và nhánh ops-fe WIP không dùng.

### Consequences
- Không trùng việc với team BE; B01 merge vào feature branch chung theo `git.md`.
- `file:line` lms-be của plan kiểm ở `65d3aad`.

### Alternatives Rejected
- Dựng từ `staging` (bản đầu): bị loại, trùng migration timestamp và module với WP0.

---

## ADR-002: Quyền: `tags` mang mã quyền cho endpoint gamification

### Status
Accepted (DEC-T6, BE lead [GIẢ LẬP] trả lời OQ-T1, OQ-T2)

### Context
`openspec/conventions/backend.md` § 2 bắt `tags: []`. Code: `tags` là thứ duy nhất sinh dòng `p` gắn route vào quyền (`scan-operation.service.ts:101`, `:145-152`); route không có dòng `p` thì mọi staff qua (`permission.service.ts:94-105`). Vậy `tags: []` trái BR-15.3 ("mở thẳng đường dẫn cũng không vào được") và trái chính spec BE "Không có quyền nào → 403" (`specs/gamification/configuration/spec.md` Requirement Phân quyền Ops). Mã quyền trong PRD Solution lệch: `…_settings` (`prd.md:644-645`) và `…_config` (`prd.md:771`).

### Decision
- Mỗi endpoint gamification khai `security[0]` (group `gamification_management`, name, display_name, description) **và** `tags` = danh sách mã quyền được gọi endpoint đó. Ngoại lệ có chủ đích của `backend.md` § 2, chỉ áp cho nhóm gamification.
- Ba mã chuẩn (theo design BE): `gr_view_gamification_settings`, `gr_update_gamification_settings`, `gr_view_gamification_learners`. ops-fe dùng đúng ba mã này.
- C-01 GET settings: `tags` = cả ba mã ([2.43 Q1]: người chỉ có quyền học viên vẫn vào trang để thấy khối Campaign). C-02 PATCH: `tags` = `gr_update_gamification_settings`.
- Quyền chỉ xuất hiện trên màn role khi có endpoint khai `security[0]` với tên đó: lát này có hai quyền (C-01, C-02); `gr_view_gamification_learners` xuất hiện ở Unit có endpoint learners.

### Consequences
- Tới khi quản trị gán quyền, chỉ superadmin vào được (an toàn mặc định).
- `backend.md` § 2 cần ghi ngoại lệ (BE lead sửa convention, không thuộc store).
- Ở `NODE_ENV=LOCAL` quét quyền bị bỏ qua (`permission.service.ts:58-61`) → test chặn quyền làm trên staging.

### Alternatives Rejected
- Giữ `tags: []`: bị loại, route mở cho mọi staff.
- Kiểm quyền thủ công trong service: bị loại, đi vòng hệ phân quyền (BR-15.1).

---

## ADR-003: Cache cấu hình chỉ ở Redis theo tenant, xoá khi ghi

### Status
Accepted (DEC-T6). **Đổi so với design gốc** (đầu việc 3: "Redis + in-memory 30 giây"). Cả intent: áp cho năm khối cấu hình

### Context
[2.43 Q3]: công tắc có hiệu lực ngay khi lưu. Cache trong bộ nhớ 30 giây ở mỗi tiến trình (ops, lms, event-processor, background-job) không xoá được từ tiến trình khác → tới 30 giây ghi nhận sai trạng thái. `@Cache` decorator chỉ cache khi có row `caching_settings` (`cache.decorator.ts:41-65`) → hành vi phụ thuộc dữ liệu.

### Decision
`GamificationSettings` dùng `CacheService` trực tiếp (`cache.service.ts:34,44,56`), khoá `gamification:config:settings` (= `GAMIFICATION_REDIS_KEYS.CONFIG` của WP0 + `:settings`; tự có tiền tố tenant, `:16-19`), TTL 1 giờ; ghi DB xong thì `deleteCache` trong cùng request. Không cache trong bộ nhớ tiến trình, không dùng `@Cache`.

### Consequences
- Còn race nhỏ: một GET miss đọc DB cũ, PATCH xoá cache xen giữa, rồi GET `setCache` giá trị cũ → cũ tới TTL. Request HTTP không có transaction bọc chung (`request-query-runner.interceptor.ts` chỉ áp cho Kafka consumer, không cho HTTP). Accepted risk ở lát này (thao tác bật tắt hiếm); Unit Điểm xem lại (ghi đè cache bằng bản mới sau khi ghi, hoặc TTL ngắn).
- Mỗi thao tác gamification thêm một lần GET Redis — chấp nhận; đo lại ở Unit Điểm (NFR).
- App nào đọc cấu hình phải import `RedisCacheModule` (hiện chỉ Ops, `apps/ops/src/app/app.module.ts:114`); Unit sau thêm cho lms và event-processor.

### Alternatives Rejected
- Giữ in-memory + pub/sub xoá: đúng nhưng thêm hạ tầng; để Unit Điểm xem lại nếu Redis thành nút cổ chai.

---

## ADR-004: Ghi cấu hình bằng PATCH từng trường; múi giờ không nằm trong API cấu hình

### Status
Accepted (DEC-T6). **Đổi so với design gốc** (`PUT /gamification/settings` với `UpdateGamificationSettingDto` gồm 2 công tắc + `timezone`, `design.md:351`)

### Context
BR-14.10: bấm là lưu từng công tắc; PRD Frontend §7: "lưu dồn dập không được ghi đè lần sau, lưu một ô không kéo theo giá trị lỗi của ô khác". PUT cả khối vi phạm cả hai khi hai lần lưu chồng nhau. BR-14.9: múi giờ lấy theo tenant, không nhập trên màn Gamification.

### Decision
`PATCH /gamification/settings` nhận **đúng một** trong `is_enabled`, `is_visible`; server đọc bản ghi, áp rule, ghi một trường. Múi giờ chỉ là cột `tenant.timezone`, không có trong request hay response của C-01, C-02. Các khối US8–US11 ở Unit sau theo cùng kiểu PATCH từng trường.

### Consequences
- Không cần khoá phiên bản; hai PATCH khác trường không đè nhau.
- Đổi múi giờ (ngoài phạm vi PRD đợt này) làm sau ở module Tenant.

### Alternatives Rejected
- `PUT` cả khối + kiểm phiên bản (`updated_at`): đúng nhưng lần lưu thứ hai bị từ chối, FE phải tải lại và lưu lại, trái trải nghiệm tự lưu.
- Giữ `timezone` trong DTO cấu hình: trái BR-14.9.

---

## ADR-005: Lưu mốc bật Visibility lần đầu

### Status
Accepted (DEC-T6). **Thêm so với design gốc** (`design.dbml` không có cột này)

### Context
[2.43 Q2]: popover bật hiển thị chỉ hỏi một lần trong đời tổ chức (BR-14.13). Cần dữ liệu bền, không dựa vào trạng thái FE.

### Decision
Thêm `visibility_first_enabled_at timestamptz null` vào `gamification_settings`; ghi khi `is_visible` chuyển false → true lần đầu, không bao giờ xoá. C-01 trả `has_been_visible` (= cột khác null) để ops-fe quyết có hiện popover.

### Consequences
- Bật lại sau này không hỏi; câu chữ popover không cần nhánh "lần sau".

### Alternatives Rejected
- Suy ra từ `first_enabled_at` của Gamification: sai khi bật Gamification chạy ngầm rất lâu trước khi bật hiển thị.
- Nhớ ở FE (localStorage): mất khi đổi máy hoặc người vận hành khác.

---

## ADR-006: Lát Nền tảng chạm lms-be + ops-fe, không chạm lms-fe

### Status
Accepted (DEC-T6)

### Context
US14, US15 chỉ có màn Ops. Phía học viên chỉ đổi khi có màn Gamification (US1, Unit "Hiển thị cho học viên"). Walking skeleton (tech-protocol) yêu cầu lát đầu đi qua mọi điểm tích hợp thật của **lát**.

### Decision
Unit duy nhất của lát đi qua ops-fe → lms-be → PostgreSQL/Redis/Casbin. lms-fe không có thay đổi, không có change `run`. Đọc trạng thái hiển thị từ lms-fe làm cùng màn học viên.

### Consequences
- Không có code chết ở lms-fe; Unit "Hiển thị cho học viên" dựng endpoint đọc phía học viên.

### Alternatives Rejected
- Đưa cờ hiển thị sang lms-fe ngay trong lát Nền tảng: không có màn nào dùng, không kiểm được.

---

## ADR-007: Giữ seed của WP0 cho tenant có sẵn; tenant mới tạo khi đọc lần đầu

### Status
Accepted (DEC-T14)

### Context
[2.43 Q4]: tổ chức đang có lúc lên bản ở trạng thái tắt hẳn; BR-14.6 tổ chức mới cũng tắt. WP0 đã seed bản mặc định cho mọi tenant có sẵn (`1789998000000-seed-gamification-defaults.ts:53-55`, `ON CONFLICT DO NOTHING`).

### Decision
Giữ seed của WP0. Service vẫn `INSERT … ON CONFLICT (tenant_id) DO NOTHING` khi đọc mà chưa có bản ghi (tenant tạo sau migration), `tenant_id` gán tường minh. Mọi công tắc mặc định false.

### Consequences
- Tenant mới không cần hook khởi tạo; chịu được hai request đồng thời.

### Alternatives Rejected
- Hook khi tạo tenant: phải sửa luồng tạo tenant ở module khác, không cần thiết khi đã có upsert lúc đọc.

---

## ADR-008: Mở rộng catalogue cho cả intent trên nhánh `feature/gamification` gồm WP0, WP3, WP1

### Status
Accepted (DEC-T19) (2.6 `[R]`, DEC-T15)

### Context
Phạm vi mở thành 19 US. Nhánh lms-be `origin/feature/gamification` nay ở @9006b80, có thêm WP3 (`c235167`, API cấu hình Ops) và WP1 (`211afa6`, engine, Kafka publisher, consumer) sau lần quét của B01. Design gốc `upbase-221099-gamification` đã có campaign, năm bảng, đóng băng (khớp PRD v0.14 phần lớn).

### Decision
Catalogue 31 component lấy building block của design gốc (engine, config, leaderboard, campaign, notifier, retry) làm khung, thêm phần FE ba repo. Code đã có trên nhánh → `modified`, kèm `file:line` @9006b80. ADR-001…007 giữ nguyên; ADR-001 nay hiểu là "dựng trên nhánh chung", không chỉ WP0.

### Consequences
- Phần BE trùng tên với design gốc để BE lead đối chiếu.
- Chỗ lệch design gốc ghi ADR riêng (ADR-009 … ADR-018), BE lead sửa `design.md` theo (DEC-T1).
- Điểm hook luồng học giữ đủ danh sách đầu việc 8 của design gốc (`createCourseSectionProgress`, `saveUserProgressAfterSubmit`, `createTopicAttempt`, `createCaseStudyAttempt`, `finishGrading`) và thêm `updateUserCourseSectionProgress` (`class.service.ts:10395`, đường đánh dấu FINISHED không đổi `class_user`).
- Hạ tầng mới: `@socket.io/redis-adapter`, `@socket.io/redis-emitter` chưa có trong `package.json` lms-be.

### Alternatives Rejected
- Viết lại catalogue BE độc lập: bị loại, trái DEC-T1.

---

## ADR-009: Ghi nhận qua Kafka như WP1

### Status
Accepted (DEC-T19). **Lệch PRD** (`Solution › TDD`, `prd.md:211`: "không qua tác vụ nền, không qua hàng đợi"). Design gốc luồng 1 vẽ engine gọi trong luồng, còn WP1 (đã code, BE lead chọn) đi Kafka; ADR này chốt theo code

### Context
WP1 đã code: hook gọi `GamificationRecordPublisher.publish` → topic `process_gamification_record` → `GamificationEngineService.record` ở event-processor; publish lỗi thì lưu `gamification_failed_events` (`gamification-record.publisher.ts:23-60`). NFR-GAM-01: không làm hỏng, không làm chậm thao tác học.

### Decision
Giữ Kafka ([2.6 Q5]). Hook chỉ publish sau commit của luồng học, bọc try/catch. Mục tiêu từ thao tác tới thẻ thông báo ≤ 3 giây (2.43 Q14), đo ở 3.6. Ghi "Ghi chú cho PO" ở `tech-state.md`.

### Consequences
- Thao tác học không chờ transaction gamification.
- Điểm và thông báo trễ một nhịp Kafka; màn Gamification mở ngay sau thao tác có thể chưa thấy điểm mới (chấp nhận, thẻ thông báo tới sau).
- Thứ tự sự kiện của một học viên giữ nhờ key Kafka = `user_id`.

### Alternatives Rejected
- Gọi engine trực tiếp sau commit trong request học: đúng câu chữ PRD nhưng bỏ code WP1 đã verify, và transaction gamification (khoá dòng stats) cộng thêm vào thời gian của thao tác học.

---

## ADR-010: Check-in bằng endpoint riêng do lms-fe gọi khi có tương tác thật

### Status
Accepted (DEC-T19). **Đổi so với design gốc** (đầu việc 9: hook `LmsGuard` mọi request)

### Context
BR-5.1: chỉ tính khi học viên chủ động mở hoặc quay lại UpLMS; request nền (socket, refetch, tab treo qua đêm) không tính. BE không phân biệt được request nền (không có header client, `lms.guard.ts:38-82`). lms-fe đã có mẫu "first user interaction" (`apps/lms-pro/src/app/client-layout.tsx:38-45`).

### Decision
`LmsCheckinTrigger` (lms-fe) gọi endpoint check-in của `CheckinService` ở tương tác thật đầu tiên sau khi tải trang, hoặc sau khi tab quay lại visible rồi có tương tác, hoặc khi điều hướng route; khoá phía client theo (user, ngày theo múi giờ tổ chức) để không gọi lặp, chỉ là tối ưu. Endpoint publish topic có sẵn `process_gamification_checkin`, publish thành công mới `SET NX` theo `tenant:user:ngày`; publish lỗi thì ghi `FailedEvent`, không đặt khoá. Consumer check-in của `CheckinService` (event-processor) chèn `Checkin` unique `(user_id, checkin_date)`, tính chuỗi, gọi `engine.record` kiểu CHECKIN. Topic `process_gamification_record` chỉ dùng cho sự kiện hoàn thành (ADR-009). Bỏ hook trong `LmsGuard` ([2.6 Q6]).

### Consequences
- Chặn được tab treo qua đêm.
- Thêm một endpoint (2.8) và một phần FE chạy ở mọi màn.
- Client tự gọi: người dùng sửa client có thể tự check-in mỗi ngày mà không mở app; chấp nhận vì vẫn phải có phiên đăng nhập và tối đa một lần/ngày.

### Alternatives Rejected
- Header `x-user-active` trên request do người dùng gây ra: phải sửa mọi chỗ gọi API, dễ sót.

---

## ADR-011: Tiêu chí hạng theo huy hiệu đọc bộ đếm chỉ tăng

### Status
Accepted (DEC-T19) (2.43 Q5)

### Context
BR-9.10: số huy hiệu hiển thị chỉ đếm loại đang bật, nên giảm rồi tăng khi tắt bật loại. PO chốt mỗi huy hiệu chỉ góp một lần vào tiêu chí hạng.

### Decision
Tiêu chí `Badges` của `LevelHandler` đọc `UserStats.total_badges_acquired` (WP0 đã có), chỉ tăng khi chèn dòng `BADGE` mới (kể cả trao bù lần đầu, BR-9.9). Số huy hiệu hiển thị (US1, US6, US12) đếm dòng `BADGE` thuộc loại đang bật, không dùng cột này.

### Consequences
- Không cần cột mới; tắt bật loại không làm lên hạng lại.
- Hai con số "số huy hiệu" khác nhau có chủ đích; 3.1 ghi rõ ở `rules.md`.

### Alternatives Rejected
- Đếm theo loại đang bật cho cả tiêu chí hạng: PO loại (2.43 Q5 B).

---

## ADR-012: Lần ghi nhận lỗi: tự chạy lại, không có màn Ops

### Status
Accepted (DEC-T19) (2.43 Q9)

### Context
BR-13.8 bắt ghi lại lần lỗi để không mất âm thầm; BR-22.8 loại lần lỗi khỏi nhật ký Ops; `OQ-46` hỏi vận hành thấy lỗi ở đâu, PO chọn không có màn (A12: vận hành không cộng bù tay).

### Decision
Giữ đầu việc 6 design gốc (cron 15 phút, tối đa 5 lần, `RESOLVED` / `GAVE_UP`), tách kho lỗi `FailedEventStore` khỏi cron `FailedEventRetry` để đồ thị component không vòng (engine với `isRetry` không ghi thêm lỗi). `GAVE_UP` ghi log có mã `GAMIFICATION_RECORD_GAVE_UP` để đội kỹ thuật đặt cảnh báo. Không có API, màn Ops (BR-22.8).

### Consequences
- Vận hành không thấy lỗi; câu hỏi của học viên về điểm thiếu chuyển cho đội kỹ thuật.

### Alternatives Rejected
- Bộ lọc "Lỗi" trong US22: PO loại.

---

## ADR-013: Đóng băng campaign sau biên kết thúc 24 giờ và không còn sự kiện lỗi chờ

### Status
Accepted (DEC-T19). **Đổi so với design gốc** (luồng 6: 15 phút)

### Context
2.43 Q8: lần ghi lại mang thời điểm gốc phải kịp vào kết quả; ghi lại tới sau đóng băng thì không đổi kết quả (BR-21.1). ADR-009 thêm độ trễ Kafka.

### Decision
Job 15 phút chọn campaign đã qua `to + 24 giờ` và không còn `FailedEvent PENDING` có `occurred_at < to`; giữ advisory lock, `version = 0`, dọn version cũ chừa 0 của design gốc ([2.6 Q9]). Trong 24 giờ đó API trả `is_final = false`.

### Consequences
- Kết quả chính thức có sau một ngày; nhãn "tạm tính" kéo dài thêm một ngày sau khi hết campaign.
- Ghi lại tới sau đóng băng vẫn vào ledger, bảng chung; kết quả campaign lệch ledger có chủ đích.

### Alternatives Rejected
- 15 phút: đủ cho retry nhưng PO chọn 24 giờ.

---

## ADR-014: Dữ liệu Ops đọc ledger + stats có index; export trả JSON

### Status
Accepted (DEC-T19). **Đổi so với design gốc** (đầu việc 13, 14: server dựng `.xlsx`)

### Decision
`GamificationOpsDataApi`: All time đọc `UserStats`; khoảng khác dùng `computeRange` trên ledger; nhật ký đọc ledger. Thêm index `(tenant_id, occurred_at)` và `(tenant_id, user_id, occurred_at)` nếu WP0 chưa có. Export trả JSON không phân trang, tối đa 50.000 dòng, ops-fe dựng xlsx bằng helper sẵn có ([2.6 Q7, Q10]). Đo NFR 2.43 Q14 ở 3.2/3.6; bảng tổng hợp theo ngày chỉ thêm khi không đạt.

### Consequences
- Đúng pattern export hiện có của Ops; server không giữ file.
- Rủi ro chậm khi ledger lớn, có đường lui là bảng tổng hợp.

### Alternatives Rejected
- Bảng tổng hợp ngay: thêm đường ghi và đồng bộ khi chưa có số đo.

---

## ADR-015: lms-fe dựng tiếp từ nhánh WIP `feature/uplms-sprint-2/gamification-feature`

### Status
Accepted (DEC-T19)

### Context
Nhánh có 183 file UI phía học viên (màn, panel, bảng xếp hạng, tab Badges, banner My Learning, realtime) với dữ liệu mock. Đã theo BR-6.15 (`useLeaderboardParams.ts:14` chỉ nhận năm khung cố định, URL cũ khoảng tự do về `all_time`) và đã có bảng `activities` (`types/model.ts:90`). Chưa có API thật, chưa có socket.io (mock emitter), chưa có campaign; viết theo spec cũ trong `.claude/docs/features/gamification/` nên cần rà theo PRD v0.14.

### Decision
Unit có màn học viên cắt nhánh từ WIP này, thay mock bằng `LmsGamificationApiClient`, thay mock emitter bằng socket.io, thêm campaign, rà ẩn hiện theo bảng BR-1.8 v0.14. Mỗi Bolt FE ghi rõ phần dùng lại ở plan 3.5.

### Consequences
- Tiết kiệm phần lớn công UI; phải rà lại theo PRD v0.14 (nhánh viết theo spec cũ trong `.claude/docs/features/gamification/`).

### Alternatives Rejected
- Viết lại từ staging: bỏ phí 16,6k dòng đã có.

---

## ADR-016: Sửa WP3 theo ADR-002, ADR-004; mở lại plan B01

### Status
Accepted (DEC-T19) ([2.6 Q8])

### Context
WP3 (`apps/ops/src/gamification-setting/gamification-setting.controller.ts:18,35-196`) có `PUT` năm khối, `tags: []`, `security` chỉ có group (không tên quyền, nên màn role không có gì để gán), DTO khối chung nhận `timezone`. Trái ADR-002, ADR-004 đã duyệt. Plan B01 v1.1 viết như thể phần cấu hình chung chưa có.

### Decision
- B01 sửa WP3 tại chỗ: khối chung đổi `PATCH` một trường, bỏ `timezone`, thêm `visibility_first_enabled_at`; mọi endpoint của controller WP3 khai tên quyền + `tags` ngay trong B01 (để không có lúc nào API cấu hình mở cho mọi staff).
- Bốn khối Points, Badges, Levels, Leaderboard đổi sang `PATCH` từng trường ở Bolt của Unit tương ứng.
- Mở lại 3.5 plan B01 `[R]`, viết lại delta trên @9006b80 trước khi code. BE lead cập nhật `assignment.md`.

### Consequences
- B01 chậm lại một vòng plan; tránh code đè lên WP3.

### Alternatives Rejected
- Giữ PUT cả khối: trái BR-14.10 (hai lần lưu chồng nhau đè nhau).

---

## ADR-017: Chốt người tham gia campaign tại biên kết thúc

### Status
Accepted (DEC-T19) ([2.6 Q11])

### Context
C12: học viên bị Block hoặc rời tổ chức **trước** lúc kết thúc thì không có trong kết quả, **sau** lúc kết thúc thì vẫn có. `users` chỉ có `status` (`user.entity.ts:86-88`), không có mốc thời điểm Block hay rời. ADR-013 dời đóng băng tới `to + 24 giờ`, nên lúc đóng băng không còn phân biệt được.

### Decision
Job 15 phút của `CampaignLeaderboard`, ở lần chạy đầu tiên sau biên kết thúc, ghi danh sách học viên đủ điều kiện lúc đó (không Test Account, `status` không phải Block/rời) vào `CampaignParticipant` (entity mới). Đóng băng tính trên danh sách này. Sai số tối đa bằng chu kỳ job (15 phút).

### Consequences
- Đúng C12 với sai số 15 phút, không phải thêm cột lịch sử trạng thái vào `users`.
- Thêm một bảng nhỏ theo campaign.

### Alternatives Rejected
- Thêm `blocked_at` / `left_at` vào `users`: sửa module người dùng ngoài phạm vi, phải sửa mọi đường Block.
- Lấy trạng thái lúc đóng băng: sai C12 với người bị Block trong 24 giờ chờ.

---

## ADR-018: Con trỏ `leaderboard_version` đổi qua GamificationConfig, đọc không qua cache dài

### Status
Accepted (DEC-T19) ([2.6 Q12]). Bổ sung ADR-003

### Context
`leaderboard_version` nằm trong `gamification_settings`, được cache Redis TTL 1 giờ (ADR-003). Cron ghi version mới rồi xoá version cũ; nếu cron ghi thẳng bảng mà không xoá cache, API học viên đọc con trỏ cũ trỏ vào snapshot đã xoá → bảng rỗng tới 1 giờ.

### Decision
`LeaderboardComputation` đổi con trỏ bằng hàm của `GamificationConfig` (ghi DB + xoá cache trong cùng bước). Đọc con trỏ khi phục vụ bảng xếp hạng đi đường không cache hoặc cache ngắn; xoá version cũ chỉ sau khi con trỏ mới đã có hiệu lực, và giữ thêm version liền trước một chu kỳ.

### Consequences
- Không có lúc bảng rỗng; tốn thêm một lần đọc con trỏ mỗi request bảng xếp hạng.

### Alternatives Rejected
- Cron ghi thẳng cột và để cache tự hết hạn: bảng rỗng tới 1 giờ.
