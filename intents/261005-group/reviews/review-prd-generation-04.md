# Review: prd.md · 2.42 PRD Generation · lần 04
**Verdict:** READY
**Verdict Dictated:** no
**Reviewer:** ai-reviewer · **Date:** 2026-10-21

## Prior findings
| ID | Severity | Now | Note |
|---|---|---|---|

Sổ finding `findings-prd-generation.md` và `findings-user-stories.md` không có finding nào ở trạng thái Open hoặc Reopened; mọi finding đã là Fixed, Rejected hoặc Accepted risk — không chấm lại theo đúng luật của stage.

## New findings
| Severity | Location | Finding | Required action |
|---|---|---|---|
| Major | prd.md > US12 > BR-12.2 · AC12.2 · AC12.6 | `BR-12.2` nói mentor đến từ nhóm "chỉ phụ trách những người đến từ nhóm đó, không phụ trách cả lớp". Domain `05-grading.md` (KB-GRAD-03, KB-GRAD-05, KB-GRAD-07) mô tả cơ chế khác: Mentor thường chỉ thấy bài **được giao** qua thao tác Assign Grader của Mentor chính, danh sách người chấm khi Assign Grader lấy từ toàn bộ Mentor của lớp chứ không ràng buộc theo nhóm nào; còn Mentor chính (`BR-12.4`: mentor đầu tiên vào lớp) xem được **toàn bộ** bài test/quiz của lớp. PRD không nói "chỉ phụ trách nhóm mình" là giới hạn truy cập hệ thống thực thi (mentor không thấy/chấm được bài ngoài nhóm) hay chỉ là nhãn hiển thị song song với Assign Grader thủ công sẵn có; cũng không nói khi người này đồng thời là Mentor chính thì quyền "xem toàn lớp, Assign Grader" của domain có bị thu hẹp theo nhóm hay vẫn giữ nguyên. QA không viết được test rõ cho `AC12.2`/`AC12.6` vì hai cách hiểu cho hai hành vi hệ thống khác nhau. | Ghi rõ trong `BR-12.2` hoặc thêm một business rule: phạm vi "chỉ phụ trách nhóm" có chặn mentor xem/chấm bài ngoài nhóm hay không; nếu mentor đó đồng thời là Mentor chính thì quyền xem toàn lớp và Assign Grader theo domain hiện có còn áp dụng hay bị thu hẹp theo nhóm. |
| Minor | prd.md > US7 · impact-matrix.md > BI-7 | `impact-matrix.md` mục 6 (`BI-7`) nêu câu hỏi nghiệp vụ "lớp `Flexible` mà học viên chưa Activate thì không set được thời hạn riêng; người vào nhóm sau 6 tháng vẫn nhận đủ N ngày" và đánh dấu "Feed ngược BRD? ✅ Có", nhưng PRD không có business rule, tiêu chí chấp nhận hay câu hỏi mở nào trích dẫn lại điểm này. Hiện chỉ suy ra gián tiếp được từ `BR-7.4` (luật đứng theo luật của Lớp, không ngoại lệ) — đúng nhưng không tường minh cho QA viết test riêng cho trường hợp `Duration = Flexible`. | Thêm một dòng ở Business rule của `US7` hoặc ở mục Giả định/Câu hỏi mở, xác nhận: lớp `Duration = Flexible` tính N ngày từ ngày từng học viên tự Activate, không đổi vì vào nhóm muộn; trích `impact-matrix.md BI-7` làm nguồn. |

## Summary
PRD lần 04 giữ vững chất lượng truy vết (traceability 0 GAP/0 ORPHAN ở cả hai lớp) và đã dọn sạch các vết số cấp cũ sau CR6; vấn đề còn lại là ranh giới chấm bài của mentor theo nhóm ở `US12` chưa khớp rõ với cơ chế Assign Grader sẵn có của module Grading, cần làm rõ trước khi giao Dev. Một Major có cách xử lý rõ ràng nên verdict là READY.
