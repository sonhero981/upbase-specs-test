# Project Context

**Project:** Group
**Ngày tạo:** 05/10/2026
**Trạng thái:** ✅ **PRD đã duyệt** (06/10/2026) — 20 US · 122 business rule · 4 sơ đồ · 14.015 từ. Chín bước xong. **Chưa publish lên Lark**
**Cỡ yêu cầu:** **L** — đủ bốn dấu hiệu

---

## Background

<!-- Bối cảnh: vì sao có yêu cầu này, đang xảy ra chuyện gì -->

**Đây là chức năng NHÓM, không phải chức năng cây tổ chức.** Cây tổ chức chỉ là **một tập con**: hệ thống đồng bộ với HRM rồi tạo ra các nhóm học viên dựa trên cây đó. Ngoài nguồn này còn có nhóm do người dùng tự tạo, và có thể còn nguồn khác.

Đóng khung sai chỗ này dẫn tới thiết kế sai: nếu coi cây tổ chức là bản chất thì mọi thứ phải nằm trong cây, trong khi nhu cầu thật có cả những nhóm **cắt ngang cơ cấu** — ví dụ gom người theo chức danh ở nhiều phòng ban khác nhau.

Ba nền tảng lớn đều tách hai khái niệm này: TalentLMS và Docebo có `Branch` cho cơ cấu và `Group` cho nhóm tuỳ ý, Moodle có `Cohort` toàn site và `Group` trong khoá. Xem `working/ai-drafts/nghien-cuu-lms-khac-20261005.md`.

**Không có nền để kế thừa.** PO chốt 05/10 *(`BA-01`)*: **bỏ hẳn `Group Management` và Recipients List đang có, coi như chưa có gì.** Nhóm hiện tại là nhóm **phẳng** — chỉ tạo sửa xoá và gán người, không cha con, không nguồn, không quản lý. `Department Management` từng làm cây cho `staffs` nhưng hiện không chạy.

Khi mở lại chức năng gửi thông báo từ Ops, người nhận sẽ chọn thẳng từ chức năng Nhóm mới này.

**HRM là Lark.** Đã đồng bộ được học viên, và Lark cũng đã có sẵn cây tổ chức. Phần cần làm là mở rộng cơ chế đồng bộ sang cả cây.

Hệ quả đang thấy ở tính năng khác: bảng xếp hạng Gamification không lọc được theo nhóm, lớp hay phòng ban, nên `US16` của dự án đó phải hoãn. Quản lý trực tiếp cũng chưa có công cụ riêng vì cần đúng bộ lọc này.

## Objectives

| # | Kết quả muốn đạt |
|---|---|
| `O1` | Giao nội dung cho một tập người ổn định, không phải lập danh sách lại mỗi lần |
| `O2` | Người mới vào tập đó **tự nhận** nội dung đã giao |
| `O3` | Quản lý xem được tiến độ học của riêng người mình phụ trách |
| `O4` | Số liệu cộng dồn được theo cơ cấu, từ một phòng ban lên tới cả khối |
| `O5` | Dựng lại được ai thuộc nhóm nào tại một thời điểm quá khứ |

## Scope

<!-- Phạm vi sơ bộ, có thể chưa chắc -->

**Ranh giới đã chốt:** Nhóm gắn **người**, Lớp gắn **nội dung**. Nhóm không sinh nghĩa vụ học và không được chứa gì ngoài người. Gán nội dung cho nhóm là một **luật đứng** dẫn người vào Lớp, không phải sao chép thành viên một lần.

Bảng so sánh đầy đủ chín tiêu chí: `working/ai-drafts/clarified-requirements-20261005.md` §4.1

## Stakeholders

| Vai trò | Người | Ghi chú |
| --- | --- | --- |
| PO | Bùi Đức Huy | Chủ tài liệu |

## Phạm vi sản phẩm

**Cả hai portal.** Phần lớn việc nằm ở Ops.

| Portal | Việc | Số US |
|---|---|---|
| **UpLMS Ops** | Dựng nhóm, quản lý thành viên, đồng bộ HRM, gán nội dung, gán quản lý, nhật ký, lưu trữ | `US1`–`US15` |
| **UpLMS** | Quản lý xem tiến độ nhánh mình phụ trách; học viên xem quản lý của mình | `US16`–`US17` |
| **UpLMS Ops** | Báo cáo cộng dồn theo nhóm, xem được theo mốc quá khứ | `US18` |
| **Cả hai** | Vòng đời nhân sự — rời nhóm chưa học thì tự xử lý, còn nghĩa vụ học thì báo quản lý | `US19`–`US20` |

## Key References

| Loại | Nguồn |
|---|---|
| **PRD** | `docs/prd/prd-group-v0.1-20261006.md` — **20 US · 122 business rule · 4 sơ đồ.** ✅ Đã duyệt 06/10 |
| **BRD** | `docs/brd/brd-v0.2-20261006.md` — 20 US. ✅ Đã duyệt |
| **Impact Matrix** | `working/impact-analysis/impact-matrix-v0.2-20261006.md` — 12 vùng, 6 conflict đã quyết. ✅ Đã duyệt |
| **Bản đồ phạm vi** | `working/impact-analysis/related-features-map-20261005.md` |
| **Field Intake** | `working/field-intake-20261006.md` — 13 câu field, đã đóng hết |
| Yêu cầu gốc | `working/raw-inputs/yeu-cau-goc-20261005.md` — 19 hạng mục |
| Bản làm rõ | `working/ai-drafts/clarified-requirements-20261005.md` |
| Câu hỏi mở | `working/open-questions/open-questions-20261005.md` — **đóng hết**, kể cả nhóm D |
| **Dữ liệu HRM** | `working/raw-inputs/lark-users-by-department.csv` — 384 nhân sự, 53 phòng ban, cây sâu 4 cấp. **Đã cắt 16 cột cá nhân** |
| Nguyên tắc mô hình hoá | `.claude/_shared-knowledge-base/16-domain-principles.md` — nguyên tắc 6, ranh giới Nhóm với Lớp |
| Nghiên cứu LMS khác | `working/ai-drafts/nghien-cuu-lms-khac-20261005.md` — TalentLMS · Docebo · Moodle · mô hình tích hợp HRIS |
| **Dự án liên quan** | `.claude/projects/Gamification/` — `US16` bộ lọc bảng xếp hạng theo nhóm đang chờ chức năng này |
| Phân biệt Nhóm và Lớp | `Gamification/working/raw-inputs/change-requests.md` mục `CR-001`, phần đối chiếu hệ thống |
| Schema DB | [Lark → Data Architecture](https://upbasevn.sg.larksuite.com/wiki/MaFpweI68iKNMvkTioLlJ1uJgQd) |
| Swagger | `uplms-api.staging.upbase.asia/lms/api/v1/docs` · `/ops/api/v1/docs` — **tên miền mới, đọc lại 05/10**. Hai host cũ `lms-be` và `ops-be` đã bỏ |
| KB cần đọc | `04-class.md` (phân biệt với Lớp) · `06-user-account.md` · `12-data-model.md` · `14-api-surface.md` |

> ⚠️ Knowledge base **chưa phủ** vùng phòng ban và phân quyền. Xem `14-api-surface.md` §1–2. Nhiều câu về nhóm sẽ phải hỏi PO hoặc Dev thay vì tra KB.

## Lark

- **Wiki space:** `7660816820865093342`
- **Node cha chung:** [`02. Execution — Epics & Features`](https://upbasevn.sg.larksuite.com/wiki/X3hhwv2MxizpFgkVudVl7e52gUc) — `X3hhwv2MxizpFgkVudVl7e52gUc`
- **Node dự án:** `Group` — `FwwEwV4V7ilx77k6LColwj3OgDf`

Cấu trúc: tài liệu nằm **trong node dự án**, không nằm thẳng dưới node cha chung.

```
02. Execution — Epics & Features
├── Gamification
│   └── [PRD] Gamification
└── Group                      ← node dự án
    └── [PRD] Study Group      ← tài liệu
```

### Đã publish

| Artifact | Tên trên Lark | Node token | Document token | URL | Lần publish gần nhất |
| --- | --- | --- | --- | --- | --- |
| **PRD v0.1** | `[PRD] Study Group` | `UAIEw1tKfirmt3kUicZle3NTgfd` | `Jg7ld8UCzoeMiAxW5ielxlC4gGg` | https://upbasevn.sg.larksuite.com/docx/Jg7ld8UCzoeMiAxW5ielxlC4gGg | 06/10/2026 |

> ⚠️ **Tên trên Lark khác tên file.** File là `[PRD] Nhóm học viên`, trên Lark người dùng đặt là `[PRD] Study Group`. Lần publish sau **giữ nguyên tên trên Lark**, chỉ cập nhật nội dung.

Đối chiếu sau khi publish: **2.326 block** · heading 14/32/124/51 khớp file · **45 bảng** khớp · **4 bảng trắng** từ 4 sơ đồ · không còn khối mã sơ đồ nào sót · 205 gạch đầu dòng khớp.

## Jira

- **Epic:** <!-- link -->
- **Story:** <!-- link -->
