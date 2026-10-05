# Project Context

**Project:** Group
**Ngày tạo:** 05/10/2026
**Trạng thái:** 🆕 Mới khởi tạo, chưa có yêu cầu gốc
**Cỡ yêu cầu:** *(xác định sau Bước 2)*

> Phần dưới đây ghi những gì **đã biết từ dự án Gamification**, nơi chức năng nhóm bị nhắc tới nhiều lần như một thứ chưa có. Mọi dòng đều đánh dấu nguồn. PO xác nhận lại trước khi dùng làm căn cứ.

---

## Background

<!-- Bối cảnh: vì sao có yêu cầu này, đang xảy ra chuyện gì -->

**Đã biết từ Gamification** *(cần PO xác nhận)*:

Chức năng nhóm là **cây sơ đồ tổ chức đồng bộ từ HRM**, nên trong trao đổi hay gọi là "phòng ban". Hiện chưa có trong UpLnD.

Hệ quả đang thấy ở tính năng khác: bảng xếp hạng Gamification không lọc được theo nhóm, lớp hay phòng ban, nên `US16` của dự án đó phải hoãn. Quản lý trực tiếp cũng chưa có công cụ riêng vì cần đúng bộ lọc này.

## Objectives

<!-- Mục tiêu cần đạt -->

## Scope

<!-- Phạm vi sơ bộ, có thể chưa chắc -->

**Câu hỏi phạm vi cần trả lời sớm** *(suy ra từ Gamification, chưa phải phạm vi đã chốt)*:

| # | Câu hỏi |
|---|---|
| 1 | Nhóm đồng bộ một chiều từ HRM, hay vận hành sửa được trong UpLMS Ops? |
| 2 | Một học viên thuộc được nhiều nhóm cùng lúc không? |
| 3 | Nhóm có cấp bậc (cây) hay phẳng? Trao đổi ở Gamification nói là **cây sơ đồ tổ chức** |
| 4 | Nhóm khác gì với **Lớp** đang có? Hai khái niệm này từng bị lẫn ở `CR-001` của Gamification |
| 5 | Người rời tổ chức thì nhóm xử lý thế nào? |

## Stakeholders

| Vai trò | Người | Ghi chú |
| --- | --- | --- |
| PO | Bùi Đức Huy | Chủ tài liệu |

## Phạm vi sản phẩm

<!-- Portal nào bị chạm: UpLMS (người học) / UpLMS Ops (vận hành) / cả hai -->

## Key References

| Loại | Nguồn |
|---|---|
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
