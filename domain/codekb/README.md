# codekb

Bản chụp code đã kiểm, dùng lại cho mọi intent. Sinh và cập nhật bởi stage 2.1 Reverse Engineering (chuẩn AWS AI-DLC,
`.claude/commands/tech/reverse-engineering.md`).

- **Chuẩn AWS**: `codekb/<repo>/` gồm 9 file `business-overview`, `architecture`, `code-structure`, `api-documentation`, `component-inventory`,
  `technology-stack`, `dependencies`, `code-quality-assessment`, `reverse-engineering-timestamp` (mục `## Scope of Analysis`: commit, analyzed.paths).
- **Đào sâu theo vùng**: `codekb/<repo>/areas/<area>.md`. File vùng layout cũ (trước 11/10/2026) đã chuyển vào `areas/` khi lms-be, lms-fe, ops-fe được quét theo chuẩn AWS (11/10/2026).
- CURRENT khi `git log <commit>..origin/staging -- <analyzed.paths>` rỗng; còn lại STALE.

Convention từng repo không chép vào đây: lms-fe / ops-fe ở `.claude/rules` + `.claude/inventory` của repo, lms-be ở `openspec/conventions/*` (backend, database, verification, git, patterns).

## Bức tranh xuyên repo
| Chủ đề | Tóm tắt | Chi tiết |
|---|---|---|
| Tenant | GUC tenant set ở lms-be `tenant-context.service.ts:41`; FE không gửi tenant | `lms-be/architecture.md`, `lms-fe/architecture.md`, `ops-fe/architecture.md` |
| Lỗi 403 | lms-fe redirect về `/` với mọi 403 kể cả `silent` → trạng thái ẩn không trả 403 | `lms-fe/architecture.md` |
| Cache | Cache key Ops không có tiền tố tenant, TTL tới 1 giờ | `lms-be/architecture.md` |
| Quyền | `security` sinh quyền trên màn role (ops-fe render chung); `tags` mới gắn route. `tags: []` → route mở cho mọi staff | `lms-be/areas/authz-tenant.md` § Đường sinh quyền, `ops-fe/areas/settings-screens.md` § Màn role |

## Danh mục vùng
Thêm vùng mới ở đây trước khi tạo file. Vùng xuyên repo đặt ở repo giữ logic chính.

| Area | Repo chính | Mô tả |
|---|---|---|
| group-department | lms-be | Nhóm phẳng hiện có, cây phòng ban (Nested Set), support group |
| class-enrollment | lms-be | Ghi danh / gỡ học viên khỏi lớp, Foundation, mail chào mừng, mentor của lớp |
| authz-tenant | lms-be | Phân quyền Casbin (metadata Swagger), tenant / RLS, data scope |
| user-lark-sync | lms-be | Đồng bộ user từ Lark (webhook, CLI), trạng thái nghỉ việc |
| reporting-audit | lms-be | SIS dashboard, report LMS, tiến độ section, log thay đổi, mail log |
| group-related-screens | ops-fe | Màn Ops liên quan nhóm, phòng ban, lớp, phân quyền FE; điểm chạm lms-fe hồ sơ học viên |
| tenant-config | lms-be | Bảng `tenant`, cấu hình theo tenant, múi giờ (đang hardcode), cache Redis theo tenant, cron theo tenant |
| learner-presence | lms-be | Tín hiệu học viên vào hệ thống (`GET /me`, last login từ Keycloak), `GET /courses/my-learnings`, đường ghi progress, cờ loại tài khoản, socket |
| learner-shell | lms-fe | Khung app học viên lms-pro: bootstrap, menu/Sidebar, routing `[page]`, HTTP client, My Learning header, My Profile tabs, FCM |
| settings-screens | ops-fe | Mẫu màn cấu hình Ops: switch, ô số, lưu ngay/blur, xác nhận, đăng ký module, menu có sub-item, guard quyền theo trang |

## Store chuẩn AWS (9 file)

| Repo | File | Commit origin/staging | kind | verified_date | Intent đã dùng |
|---|---|---|---|---|---|
| lms-be | `lms-be/*.md` (9 file, scope ở `lms-be/reverse-engineering-timestamp.md`) | 610f100 | partial | 2026-10-13 | 260923-gamification |
| lms-fe | `lms-fe/*.md` (9 file, scope ở `lms-fe/reverse-engineering-timestamp.md`) | b2cc49455 | partial | 2026-10-13 | 260923-gamification |
| ops-fe | `ops-fe/*.md` (9 file, scope ở `ops-fe/reverse-engineering-timestamp.md`) | 1e01033bf | partial | 2026-10-13 | 260923-gamification |

## Bảng file vùng (`areas/`)

| Repo | Area | File | verified_date | Intent đã dùng |
|---|---|---|---|---|
| lms-be | group-department | `lms-be/areas/group-department.md` | 2026-10-10 | 261005-group |
| lms-be | class-enrollment | `lms-be/areas/class-enrollment.md` | 2026-10-10 | 261005-group |
| lms-be | user-lark-sync | `lms-be/areas/user-lark-sync.md` | 2026-10-10 | 261005-group |
| lms-be | reporting-audit | `lms-be/areas/reporting-audit.md` | 2026-10-10 | 261005-group |
| ops-fe | group-related-screens | `ops-fe/areas/group-related-screens.md` (kèm điểm chạm lms-fe hồ sơ học viên) | 2026-10-10 | 261005-group |
| lms-be | authz-tenant | `lms-be/areas/authz-tenant.md` (+ § Đường sinh quyền, 610f100) | 2026-10-13 | 261005-group, 260923-gamification |
| lms-be | tenant-config | `lms-be/areas/tenant-config.md` | 2026-10-10 | 260923-gamification |
| lms-be | learner-presence | `lms-be/areas/learner-presence.md` | 2026-10-10 | 260923-gamification |
| lms-fe | learner-shell | `lms-fe/areas/learner-shell.md` | 2026-10-10 | 260923-gamification |
| ops-fe | settings-screens | `ops-fe/areas/settings-screens.md` (+ § Màn role) | 2026-10-13 | 260923-gamification |
