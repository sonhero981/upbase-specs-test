# Review: ideation/brd.md (v0.3) · 1.1 Intent Capture · 1.4 Scope Definition · 1.7 Approval & Handoff · lần 02
**Verdict:** READY
**Reviewer:** product-lead · **Date:** 2026-10-12

## Prior findings
| ID | Now | Severity | Note |
|---|---|---|---|
| R-01 | Fixed | Critical | §4 Stakeholder, §5 In scope, §7 `US12` viết lại đúng `CF-6`: mentor gắn vào nhóm, tự động thành mentor của lớp khi nhóm được giao lớp, chỉ phụ trách người từ nhóm đó, không có cơ chế phạm vi dữ liệu riêng. Khớp PRD `BR-12.1`–`BR-12.4`, `BR-9.5`. §10 đã thêm `CF-6` vào bảng "Đã đóng ở Gate 2" |
| R-02 | Fixed | Critical | Thêm mục "Product boundary" cuối §1: trả lời đủ hai câu KB `15-product-direction.md` §7 (UpBase hay mọi tenant; tầng LMS hay tầng năng lực), nêu rõ hằng số và chỗ đóng cứng. §7 đổi tiêu đề nhóm US, `US16` chuyển vào bảng "Phía vận hành và quản lý — UpLMS Ops", khớp `DEC73` và PRD `BR-16.7` |
| R-03 | Fixed | Critical | §5 In scope đổi thành "Hai mail event mới", thêm `MAIL-GRP-02`; §7 có khối mô tả riêng (khi nào bắn, ai nhận, nói gì, không bắn khi) — đối chiếu gần như nguyên văn với PRD §*Nội dung email — MAIL-GRP-02* (`BR-9.6`, `BR-9.7`, `BR-11.7`, `BR-13.6`), không thấy nội dung không có nguồn. `MAIL-GRP-01` đã thêm câu cảnh báo theo `DEC75` |
| R-04 | Still applies | Major | Accepted risk theo `DEC78`. Đúng là PRD đã có bảng Unit `U1`–`U7` kèm phụ thuộc và thứ tự release, nhưng BRD v0.3 không có dòng nào trỏ cụ thể tới mục đó — kể cả §11 References chỉ ghi chung "prd.md v0.2 — 20 US, 128 business rule", không nêu tên mục *Unit — nhóm bàn giao*. Không chặn, đã được PO chấp nhận, nhưng lý do chấp nhận ("BRD trỏ sang bảng đó") chưa khớp hẳn với văn bản hiện tại |
| R-05 | Still applies | Minor | Accepted risk theo `DEC78`. §3 Objective vẫn chỉ có cột "Kết quả muốn đạt", không có cột đo. Đúng như lý do chấp nhận: PRD mục *Metrics success* đã có cách đo cho cả `O1`–`O5` |
| R-06 | Still applies | Minor | Accepted risk theo `DEC78`. §4 Stakeholder vẫn chỉ có hai cột "Stakeholder \| Action", không thêm cột Nguồn. Đúng như lý do chấp nhận: nguồn là yêu cầu gốc 19 hạng mục, PO là người quyết duy nhất |
| R-07 | Fixed | Minor | §11 References và §2 đã đổi sang đường dẫn v2 hiện hành (`inputs/`, `inception/requirements-analysis/requirements.md` v0.3, `inception/prd/prd.md`, `inception/impact-analysis/impact-matrix.md`, `.claude/intents/260923-gamification/`, `.claude/intents/261006-report-phase-1/`) — đã kiểm, mọi đường dẫn tồn tại |
| R-08 | Fixed | Minor | §2 đổi "❓`BA`" thành "❓`PO`", đúng ký hiệu GLOSSARY |

## New findings
| Severity | Location | Finding | Required action |
|---|---|---|---|

## Summary
Cả 3 Critical và 2 trong 5 Major/Minor còn lại của lần 01 đã được sửa đúng nguồn (`CF-6`, `DEC73`, `DEC74`, `DEC75`), không thấy nội dung mới không có nguồn hay mâu thuẫn mới phát sinh từ các chỗ sửa. 3 finding còn lại (`R-04`, `R-05`, `R-06`) là rủi ro PO đã chấp nhận ở `DEC78`, không chặn gate. READY.
