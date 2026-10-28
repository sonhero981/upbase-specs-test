---
intent: 260923-gamification
artifact: decisions
stage: 2.6 domain-design
version: 1.0
status: approved
approved_at: 2026-10-13 ([GIẢ LẬP] BE lead, DEC-T6)
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
scope: US14, US15
---
# Decisions: Gamification, lát Nền tảng (US14 · US15)

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

### Alternatives Considered
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

### Alternatives Considered
- Giữ `tags: []`: bị loại, route mở cho mọi staff.
- Kiểm quyền thủ công trong service: bị loại, đi vòng hệ phân quyền (BR-15.1).

---

## ADR-003: Cache cấu hình chỉ ở Redis theo tenant, xoá khi ghi

### Status
Accepted (DEC-T6). **Đổi so với design gốc** (đầu việc 3: "Redis + in-memory 30 giây")

### Context
[2.43 Q3]: công tắc có hiệu lực ngay khi lưu. Cache trong bộ nhớ 30 giây ở mỗi tiến trình (ops, lms, event-processor, background-job) không xoá được từ tiến trình khác → tới 30 giây ghi nhận sai trạng thái. `@Cache` decorator chỉ cache khi có row `caching_settings` (`cache.decorator.ts:41-65`) → hành vi phụ thuộc dữ liệu.

### Decision
`GamificationSettings` dùng `CacheService` trực tiếp (`cache.service.ts:34,44,56`), khoá `gamification:config:settings` (= `GAMIFICATION_REDIS_KEYS.CONFIG` của WP0 + `:settings`; tự có tiền tố tenant, `:16-19`), TTL 1 giờ; ghi DB xong thì `deleteCache` trong cùng request. Không cache trong bộ nhớ tiến trình, không dùng `@Cache`.

### Consequences
- Còn race nhỏ: một GET miss đọc DB cũ, PATCH xoá cache xen giữa, rồi GET `setCache` giá trị cũ → cũ tới TTL. Request không bọc transaction (`libs/database/src/lib/extends/request-query-runner.interceptor.ts:6-12`). Accepted risk ở lát này (thao tác bật tắt hiếm); Unit Điểm xem lại (ghi đè cache bằng bản mới sau khi ghi, hoặc TTL ngắn).
- Mỗi thao tác gamification thêm một lần GET Redis — chấp nhận; đo lại ở Unit Điểm (NFR).
- App nào đọc cấu hình phải import `RedisCacheModule` (hiện chỉ Ops, `apps/ops/src/app/app.module.ts:114`); Unit sau thêm cho lms và event-processor.

### Alternatives Considered
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
