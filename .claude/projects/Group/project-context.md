# Project Context

**Project:** Group
**Ngày tạo:** 05/10/2026
**Trạng thái:** ✅ Xong Bước 3. Mọi câu hỏi đã đóng hoặc có đề xuất. **Sẵn sàng viết BRD**
**Cỡ yêu cầu:** **L** — đủ bốn dấu hiệu

---

## Background

<!-- Bối cảnh: vì sao có yêu cầu này, đang xảy ra chuyện gì -->

Chức năng nhóm là **cây sơ đồ tổ chức đồng bộ từ HRM**, nên trong trao đổi hay gọi là "phòng ban".

**Nền đã có, chưa đủ.** `Group Management` đang chạy để tạo nhóm gửi thông báo từ Ops, nhưng là nhóm phẳng. Dự án này mở rộng nó thành cây nhiều cấp, phân loại theo nguồn, có quan hệ quản lý. `Department Management` từng làm cây cho `staffs` nhưng hiện không chạy.

**HRM là Lark.** Đã đồng bộ được học viên, và Lark cũng đã có sẵn cây tổ chức. Phần cần làm là mở rộng cơ chế đồng bộ sang cả cây.

Hệ quả đang thấy ở tính năng khác: bảng xếp hạng Gamification không lọc được theo nhóm, lớp hay phòng ban, nên `US16` của dự án đó phải hoãn. Quản lý trực tiếp cũng chưa có công cụ riêng vì cần đúng bộ lọc này.

## Objectives

<!-- Mục tiêu cần đạt -->

## Scope

<!-- Phạm vi sơ bộ, có thể chưa chắc -->

**Ranh giới đã chốt:** Nhóm gắn **người**, Lớp gắn **nội dung**. Nhóm không sinh nghĩa vụ học và không được chứa gì ngoài người. Gán nội dung cho nhóm là một **luật đứng** dẫn người vào Lớp, không phải sao chép thành viên một lần.

Bảng so sánh đầy đủ chín tiêu chí: `working/ai-drafts/clarified-requirements-20261005.md` §4.1

## Stakeholders

| Vai trò | Người | Ghi chú |
| --- | --- | --- |
| PO | Bùi Đức Huy | Chủ tài liệu |

## Phạm vi sản phẩm

<!-- Portal nào bị chạm: UpLMS (người học) / UpLMS Ops (vận hành) / cả hai -->

## Key References

| Loại | Nguồn |
|---|---|
| Yêu cầu gốc | `working/raw-inputs/yeu-cau-goc-20261005.md` — 19 hạng mục |
| Bản làm rõ | `working/ai-drafts/clarified-requirements-20261005.md` |
| Câu hỏi mở | `working/open-questions/open-questions-20261005.md` — đã đóng hết |
| **Dữ liệu HRM** | `working/raw-inputs/lark-users-by-department.csv` — 384 nhân sự, 53 phòng ban, cây sâu 4 cấp. **Đã cắt 16 cột cá nhân** |
| Nguyên tắc mô hình hoá | `.claude/_shared-knowledge-base/16-domain-principles.md` — nguyên tắc 6, ranh giới Nhóm với Lớp |
| **Dự án liên quan** | `.claude/projects/Gamification/` — `US16` bộ lọc bảng xếp hạng theo nhóm đang chờ chức năng này |
| Phân biệt Nhóm và Lớp | `Gamification/working/raw-inputs/change-requests.md` mục `CR-001`, phần đối chiếu hệ thống |
| Schema DB | [Lark → Data Architecture](https://upbasevn.sg.larksuite.com/wiki/MaFpweI68iKNMvkTioLlJ1uJgQd) |
| Swagger | `lms-be.staging.upbase.asia/api/v1/docs` · `ops-be.staging.upbase.asia/api/v1/docs` |
| KB cần đọc | `04-class.md` (phân biệt với Lớp) · `06-user-account.md` · `12-data-model.md` · `14-api-surface.md` |

> ⚠️ Knowledge base **chưa phủ** vùng phòng ban và phân quyền. Xem `14-api-surface.md` §1–2. Nhiều câu về nhóm sẽ phải hỏi PO hoặc Dev thay vì tra KB.

## Lark

- **Wiki space:** `7660816820865093342`
- **Parent node:** [`02. Execution — Epics & Features`](https://upbasevn.sg.larksuite.com/wiki/X3hhwv2MxizpFgkVudVl7e52gUc) — `X3hhwv2MxizpFgkVudVl7e52gUc`

### Đã publish

| Artifact | Node token | URL | Lần publish gần nhất |
| --- | --- | --- | --- |

## Jira

- **Epic:** <!-- link -->
- **Story:** <!-- link -->
