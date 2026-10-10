# System Map

Store OpenSpec `upbase-specs` nằm trong repo chung `upbase-specs` (trước là repo PO `po_workflow_upbase`; thư mục `openspec/`), chứa change cross-repo của Tech. Requirement nằm ở intent của PO (`.claude/intents/`). Code nằm ở 4 repo riêng dưới đây.

## Repo

| Repo | Path local | Remote | Vai trò | Gate implement |
|---|---|---|---|---|
| lms-be | `E:\UP_BASE\lms-be` | `UpBase-Tech/lms-be` | Backend NestJS (Nx, TypeORM, Kafka, socket) | curl verify + checkpoint `.agents/` |
| lms-package | `E:\UP_BASE\lms-package` | `UpBase-Tech/lms-package` | Package dùng chung `@upbase-tech/*` (GitHub Packages) | build → bump version → publish |
| lms-fe | `E:\UP_BASE\lms-fe` | `UpBase-Tech/lms-fe` | App học viên: lms-pro, lms-test, lms-zoom (Next.js 14) | Figma diff (Playwright) + `pnpm --filter <app> check-types` |
| ops-fe | `E:\UP_BASE\ops-fe` | `UpBase-Tech/ops-fe` | App vận hành (Vite + React Router) | Figma diff + unit test |

## Space chung

| Phần | Path | Owner | Quyền của Tech |
|---|---|---|---|
| Intent (requirement, HLD Brief, PRD) | `.claude/intents/<slug>/` | PO | Chỉ đọc theo `origin/main`, trừ mục 9 + dòng Dev mục 12 của `hld-brief.md` — xem `intent-handoff.md` |
| Knowledge domain | `.claude/knowledge/domain/` | PO | Đọc; sai thì báo PO |
| Store OpenSpec | `openspec/` | Tech | Ghi qua PR |
| Knowledge tech | `.claude/knowledge/tech/` | Tech | Ghi qua PR |

## Phụ thuộc

```
intent (PO) ──(PRD đã duyệt)──> openspec/ (Tech) ──(change impl-*)──> lms-package, lms-be, lms-fe, ops-fe
lms-package ──(npm @upbase-tech/*)──> lms-fe, ops-fe
lms-be ──(REST + socket)──> lms-fe, ops-fe
```

Thứ tự implement một change cross-repo: **lms-package → lms-be → lms-fe / ops-fe**.

## Package `@upbase-tech/*`

| Package | Dùng ở |
|---|---|
| `auth-package` | lms-fe, ops-fe (Keycloak) |
| `upbase-common-package` | lms-fe (editor, type lịch) |
| `upbase-notification` | lms-fe (notification drawer) |
| `quiz-result-package` | lms-fe |
| `explanation-package` | lms-fe |

## Owner

| Phạm vi | Owner |
|---|---|
| API contract (mục trong `design.md`), lms-be | BE lead — Đoàn Quang Cường |
| FE (lms-fe, ops-fe) | FE lead — Nguyễn Hùng Sơn |
| lms-package | FE lead — Nguyễn Hùng Sơn |
