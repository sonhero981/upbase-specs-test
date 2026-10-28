# Review: inception/prd/prd.md §Danh sách user story, §Unit, US1 đến US20 (v0.3, CR2) · 2.4 User Stories · lần 02
**Verdict:** READY
**Reviewer:** product-lead · **Date:** 2026-10-12

## Prior findings
| ID | Now | Severity | Note |
|---|---|---|---|
| R-01 | Rejected | Critical | PO bác theo `DEC80`: template PRD công ty (`.claude/knowledge/domain/templates/prd.md` mục "6/ Conner case") ghi nguyên văn *"Để trống. QA điền."* — mục để trống đúng quy ước công ty, không phải lỗi của PRD. Không chấm lại |
| R-02 | Fixed | Critical | Đúng luật `DEC81`. `BR-3.7` (US3) và `BR-19.7` (US19) đều kiểm "còn nhóm nào người đó vẫn là thành viên đang giao đúng lớp đó không" trước khi gỡ/báo quản lý; còn thì giữ nguyên lượt ghi danh, không gửi `MAIL-GRP-01`. `BR-7.9` (US7) mở rộng đúng: "một lượt có thể có nhiều nguồn". Khối "Không bắn khi" của `MAIL-GRP-01` (US20) thêm đúng điều kiện loại trừ theo từng khoá. Mã tham chiếu `BR-3.7` ↔ `BR-7.9` ↔ `BR-19.7` trỏ hai chiều, không gãy. Không mâu thuẫn với `C2` (BRD §6: vẫn là một lượt ghi danh, chỉ nhiều nguồn ghi nhận), không mâu thuẫn `BR-7.3`, `BR-3.4`, `BR-19.2`–`BR-19.5`, `BR-20.x` — luật mới đứng *trước* các luật đó, chỉ chạy khi không còn nhóm nào giao thì mới xét tiếp |
| R-03 | Fixed | Major | Đoạn mở đầu "Danh sách user story" đã trỏ `traceability.md`. Cột Nguồn của `US3`, `US6`, `US9`, `US16`, `US18` đã dẫn thêm `RC-02`, `RC-07` (x3), `RC-11`, `RC-20` kèm nội dung ngắn. Đối chiếu `traceability.md`: 20/20 RC có US, 0 GAP, 0 ORPHAN, không nội dung nào không có nguồn |
| R-04 | Fixed | Major | "Vấn đề tồn đọng" #2 đã ghi lý do `OQ-31` không chặn viết PRD (màn `US16` đọc theo quan hệ quản lý theo `CF-5`/`BR-16.4`, không theo ma trận quyền; ma trận chỉ cần cho Dev khi nối hai phạm vi). `impact-matrix.md` §11 dòng `OQ-31` ghi đúng khớp. Thêm #7 đúng ba góc `CG-7`, `CG-9`, `CG-14` từ Impact Matrix, không chặn, có người trả lời |
| R-05 | Still applies | Minor | Accepted risk theo `DEC80`: `US13` vẫn nối hai việc bằng "và" trong tiêu đề, không sửa. Đúng lý do chấp nhận: tách sẽ đổi mã `US13`/`BR-13.x` trên PRD đã publish Lark |

## New findings
| ID | Severity | Location | Finding | Required action |
|---|---|---|---|---|

## Summary
Cả ba sửa đổi của CR2 (`R-02`, `R-03`, `R-04`) đúng nguyên văn `DEC81`/`DEC80`, có nguồn, không gãy mã tham chiếu, không mâu thuẫn với `C2`, `BR-7.3`, `BR-3.4`, `BR-19.2`–`BR-19.5`, `BR-20.x`. `R-01` đã được PO bác có lý do xác đáng (template công ty), `R-05` là rủi ro đã chấp nhận. Không có finding mới. READY.
