# Business Overview

> Repo `ops-fe` · `origin/staging` @ `1e01033bf` · focused scan cho intent `260923-gamification` (US14, US8, US5). Mọi `file:line` theo `origin/staging`.

## Business Context

`ops-fe` là app vận hành (UpLMS Ops) cho nhân sự nội bộ: quản lý lớp, khoá, học viên, nhân sự, thông báo… Mỗi nghiệp vụ là một `AppModule` cắm vào app shell (`apps/ops-fe/src/module-registry.ts:18-34`). Người dùng đăng nhập qua Keycloak (`apps/ops-fe/src/services/auth.ts:16-27`); ai không được vào Ops bị chặn toàn app bởi `OpsAccessGate` (`apps/ops-fe/src/components/access-denied/index.tsx:44-57`).

Gamification là năng lực **mới hoàn toàn** với ops-fe: trên `origin/staging` không có file, permission hay route nào chứa `gamif` (git grep rỗng trên `apps libs features scripts`).

## Lát nghiệp vụ trong phạm vi

| US | Phía ops-fe cần gì | Hiện trạng code |
|---|---|---|
| US14 — hai công tắc `Gamification` / `Visibility in UpLMS`, tự lưu, popover xác nhận 2 trường hợp | Màn cấu hình chung, switch lưu khi bấm, popover cạnh switch, báo `Saved` | Không có màn cấu hình hệ thống/tenant: `apps/ops-fe/src/pages/setting/index.tsx:6-25` chỉ in chữ "Setting", không route nào trỏ tới (`AppRouter.tsx:45-69`) |
| US8 — cấu hình điểm: switch khối `Points`, 4 hành động (switch + ô số ≥1, không trần), lưu khi blur/Enter | Ô số nguyên dương, lỗi tại ô khi rỗng, rollback về giá trị đã lưu khi lỗi | Có `HookFormNumberField` nhưng hành vi rỗng → `minNumber` (`libs/ui/src/base/numberfield/NumberField.tsx:82-85`), không phát onBlur/onKeyDown tuỳ biến ra ngoài (xem `component-inventory.md`) |
| US5 — điểm check-in hằng ngày | Chỉ là **ô điểm nền** trong khối `Points` (US8). Biên ngày theo múi giờ tổ chức là việc của BE | FE không biết múi giờ tổ chức: `ITenantInfo` không có timezone (`libs/core/src/types/tenant-theme.ts:26-36`) |

## Key Business Rules ảnh hưởng thiết kế FE (từ PRD)

- `BR-14.10` tự lưu, không nút Save; ô số lưu khi rời ô / Enter, không lưu khi đang gõ.
- `BR-14.11` / `BR-14.12` giá trị lỗi không lưu, báo tại ô; lưu lỗi → về giá trị đã lưu gần nhất; báo `Saved` nhỏ, tự ẩn.
- `BR-14.13` chỉ 2 thao tác cần popover (tắt `Gamification`, bật `Visibility` lần đầu).
- PRD §7: lưu dồn dập không được để lần trước ghi đè lần sau; lưu một ô không kéo theo giá trị lỗi ô khác.
- `BR-8.5` điểm nguyên ≥1, không trần; `BR-8.5a` check-in chỉ một ô điểm nền.

## Actors & quyền

- Nhân sự Ops có quyền cấu hình gamification (US15 ngoài lát). Hiện FE chỉ có cơ chế quyền theo `roles[].permissions` từ `GET /me`, `superadmin` luôn qua (`libs/hooks/src/permission/useHasPermission.tsx:26-31`).

## Tenant

Đợt này một tổ chức; tenant do BE suy ra từ token, FE chỉ nhận lại qua `GET /me` (`apps/ops-fe/src/index.tsx:11-14`, `libs/utils/src/tenant-theme.ts:50-64`). Chi tiết ở `architecture.md` › Infrastructure Constraints.

## Codekb vùng cũ

Điểm xuất phát `knowledge/tech/codekb/ops-fe/areas/settings-screens.md` (verified 1e01033bf) — đã kiểm lại; điểm lệch ghi ở `code-quality-assessment.md` › Lệch so với settings-screens.md. Đã chuyển vào `areas/` (11/10/2026).
