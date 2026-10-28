---
intent: 260923-gamification
artifact: unit-of-work
stage: 2.7 units-generation
version: 1.0
status: approved
approved_at: 2026-10-13 ([GIẢ LẬP] BE lead, DEC-T7)
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
scope: US14, US15
consumes: inception/domain-design/components.md v1.0, decisions.md v1.0 (DEC-T6)
---
# Unit of Work: Gamification, lát Nền tảng (US14 · US15)

Một Unit. Lát chạm hai repo (lms-be, ops-fe) nên walking skeleton bật; lát đã đủ mỏng (một bảng, hai endpoint, một màn) nên Unit skeleton **mang luôn** US14, US15 thay vì tách một U0 rỗng US. Proto-Unit PU1 "Nền tảng" của PRD (`# Unit — nhóm bàn giao`, dòng 1).

## Units

| Unit ID | Directory | Kind | US | Repo chạm | Cỡ | Ngày công | Deployment | Proto-Unit |
|---|---|---|---|---|---|---|---|---|
| U0 | `u0-foundation` | service | US14, US15 | lms-be, ops-fe | S | 3 | embedded | PU1 "Nền tảng" |

- **Kind `service`**: có phần lms-be chạy được (bảng, endpoint) kèm màn ops-fe → áp đủ 3.1, 3.41 (có màn), 3.5.
- **Deployment `embedded`**: không deployable mới; lms-be trong app `ops` + `libs/*`, ops-fe là feature module. Phát hành an toàn vì Gamification mặc định tắt (BR-14.6) và route chỉ superadmin qua tới khi gán quyền (ADR-002).
- **Ngày công**: 1 dev fullstack, gồm test tay; lms-be 1,5 · ops-fe 1,5.

## U0 — `u0-foundation`
**Mô tả.** Vận hành có quyền mở trang Gamification bên Ops, bật tắt `Gamification` và `Visibility in UpLMS`; lms-be lưu theo tổ chức, chặn người không có quyền, cache có hiệu lực ngay.

**Ranh giới và trách nhiệm**
| Component | Repo | Phần làm ở U0 |
|---|---|---|
| TenantProfile (dùng lại) | lms-be | Cột múi giờ đã có ở WP0 (`1789996500000-add-timezone-to-tenant.ts`), không sửa |
| GamificationSettings (sửa, trên WP0) | lms-be | Bảng có sẵn ở WP0; thêm `visibility_first_enabled_at`; service đọc / tạo mặc định / ghi một công tắc; cache Redis |
| GamificationSettingsOpsApi (mới) | lms-be | C-01 GET, C-02 PATCH, khai quyền (ADR-002) |
| OpsAccessControl (dùng lại) | lms-be | Không sửa code |
| GamificationModule, GamificationSettingsPage, GamificationApiClient (mới) | ops-fe | Route, menu, trang khối chung, popover, Saved |
| OpsPermissionCatalog (sửa) | ops-fe | Ba mã quyền, mục menu theo quyền |
| RolePermissionScreen (dùng lại) | ops-fe | Không sửa code |

**Điểm tích hợp skeleton**
| Mã | Điểm |
|---|---|
| U0-IC1 | ops-fe → lms-be C-01, C-02 qua guard Ops thật |
| U0-IC2 | lms-be → PostgreSQL bảng mới có RLS + bypass |
| U0-IC3 | lms-be → Redis cache có tiền tố tenant, xoá khi ghi |
| U0-IC4 | Casbin: quyền mới hiện trên màn role, route bị chặn với role không có quyền |

**Unit sau dựng tiếp**: Unit Điểm thêm khối Points vào cùng trang và đọc `GamificationSettings` trong luồng ghi nhận; Unit Hiển thị cho học viên thêm endpoint đọc phía lms và màn lms-fe.

## Code Organization (brownfield)
- lms-be: theo `openspec/conventions/backend.md` § 1, `database.md`; change `run` cùng tên Bolt ở lms-be.
- ops-fe: theo `.claude/rules/01-code-placement.md` (feature ở `features/gamification/`, API class ở `apps/ops-fe/src/apis/gamification/`).
