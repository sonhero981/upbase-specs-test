# Project Context

**Project:** Report Phase 1
**Ngày tạo:** 06/10/2026
**Trạng thái:** 🔄 Đang làm rõ yêu cầu — bản v0.1 xong 06/10/2026, **chờ PO trả lời 12 câu hỏi chặn** `OQ-01` → `OQ-12`
**Cỡ yêu cầu:** **L** *(đề xuất, chờ PO đồng ý)* — đủ 9 bước, đủ 4 Gate

---

## Background

<!-- Bối cảnh: vì sao có yêu cầu này, đang xảy ra chuyện gì -->

PO yêu cầu *"xây dựng báo cáo và dashboard"* theo bốn chiều: **người học · nhóm/quản lý · khoá học · lớp học**, tổng 16 chỉ số. Yêu cầu nhấn mạnh **mỗi chỉ số bấm được sang danh sách người hoặc lớp để xử lý** — đây là dashboard để hành động, không phải báo cáo để đọc.

**Vấn đề gốc chưa được nêu.** Bốn vấn đề AI suy ra, chờ PO xác nhận ở `OQ-12`, xem `working/ai-drafts/clarified-requirements-20261006.md` §3.

**Hai dự án liên quan chưa xây:**

| Dự án | Chạm vào đâu |
|---|---|
| **Group** — PRD v0.1 duyệt 06/10/2026 | Chiều nhóm/quản lý trùng phần lớn với `US16` *(quản lý theo dõi nhánh mình phụ trách)* và `US18` *(báo cáo cộng dồn theo nhóm)* |
| **Gamification** — PRD v0.8 chờ PO review | *"Điểm và hạng"* ở chiều người học nhiều khả năng là khối điểm và hạng của Gamification `US1` |

## Objectives

<!-- Mục tiêu cần đạt -->

*(Chưa có — viết ở BRD sau khi PO trả lời `OQ-12` về vấn đề gốc)*

## Scope

<!-- Phạm vi sơ bộ, có thể chưa chắc -->

**Sơ bộ, chưa chốt.** Bốn chiều trong yêu cầu gốc là bức tranh chung. Phase 1 gồm những gì còn chờ `OQ-01`.

Đề xuất đang chờ PO quyết: cắt theo phụ thuộc — khoá học, lớp học, người học trước; chiều nhóm/quản lý đi cùng hoặc ngay sau Group. Xem `clarified-requirements` §8.

## Stakeholders

| Vai trò | Người | Ghi chú |
| --- | --- | --- |
| PO | Bùi Đức Huy | Chủ tài liệu |
| Học viên | — | Xem việc cần làm, hạn sắp tới, tiến độ, điểm và hạng |
| Quản lý trực tiếp | — | Một người dùng được gán quản lý nhóm, không phải một vai trò *(theo Group)* |
| Người phụ trách khoá học | `❓BA` | Chưa rõ là ai — `OQ-08` |
| Người phụ trách lớp | `❓BA` | Vận hành, mentor hay mentor chính — `OQ-08` |

## Phạm vi sản phẩm

<!-- Portal nào bị chạm: UpLMS (người học) / UpLMS Ops (vận hành) / cả hai -->

**Cả hai portal** *(giả định `A-05`, chờ PO xác nhận)*

| Portal | Chiều |
|---|---|
| **UpLMS** | Người học · nhóm/quản lý |
| **UpLMS Ops** | Khoá học · lớp học |

## Key References

<!-- Link Figma, tài liệu nền, PRD liên quan, KB cần đọc -->

| Loại | Nguồn |
|---|---|
| Yêu cầu gốc | `working/raw-inputs/yeu-cau-goc-20261006.md` · ảnh gốc `yeu-cau-goc-20261006.png` |
| Bản làm rõ | `working/ai-drafts/clarified-requirements-20261006.md` — 24 requirement ứng viên |
| Câu hỏi mở | `working/open-questions/open-questions-20261006.md` — 12 câu chặn, 4 câu không chặn, 7 giả định |
| **Dự án liên quan** | `.claude/projects/Group/` — PRD `docs/prd/prd-group-v0.1-20261006.md`, `US16` · `US18` |
| **Dự án liên quan** | `.claude/projects/Gamification/` — PRD `docs/prd/prd-gamification-v0.8-20261005.md`, `US1` · `US7` |
| KB chính | `07-learning-experience.md` · `04-class.md` · `05-grading.md` · `11-dashboard-sis.md` · `15-product-direction.md` *(năng lực)* · `14-api-surface.md` *(vùng lịch dạy chưa phủ)* |
| Schema DB | [Lark → Data Architecture](https://upbasevn.sg.larksuite.com/wiki/MaFpweI68iKNMvkTioLlJ1uJgQd) |
| Swagger | `uplms-api.staging.upbase.asia/lms/api/v1/docs` · `/ops/api/v1/docs` |
| Figma | *(chưa có)* |

## Lark

- **Wiki space:** <!-- space chứa tài liệu của project này --> *(Group và Gamification dùng chung space `7660816820865093342` — chốt lúc publish)*
- **Parent node:** <!-- node cha để đặt PRD --> *(Group và Gamification nằm dưới node `02. Execution — Epics & Features` — chốt lúc publish)*

### Đã publish

| Artifact | Node token | URL | Lần publish gần nhất |
| --- | --- | --- | --- |

## Jira

- **Epic:** <!-- link -->
- **Story:** <!-- link -->
