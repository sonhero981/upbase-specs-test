# Review: prd.md · 2.42 PRD Generation · lần 05
**Verdict:** READY
**Verdict Dictated:** no
**Reviewer:** ai-reviewer · **Date:** 2026-10-21

## Prior findings
| ID | Severity | Now | Note |
|---|---|---|---|

Sổ finding `findings-prd-generation.md` không còn mục nào ở trạng thái Open hoặc Reopened: R-01 đến R-12 đều đã Fixed, Rejected hoặc Accepted risk qua các DEC trước đó. Không có gì cần kiểm lại ở mục này.

## New findings
| Severity | Location | Finding | Required action |
|---|---|---|---|
| Major | prd.md > US12 > `BR-12.4` · `BR-12.8` · mục 4 "Một người nhiều vai trong một nhóm"; domain/05-grading.md §2 §5, `KB-GRAD-03` | `BR-12.8` cho mentor tự chấm bài của chính mình và ghi nhận rủi ro là "không có người chấm độc lập", nhưng không nói rõ việc tự chấm có còn đi qua bước Mentor chính review trước khi `Finish` hay không — bước này vốn có sẵn trong luồng chấm hiện tại (`KB-GRAD-03`, luồng ở `05-grading.md` §5: mentor chấm → submit to review → Mentor chính review → Finish). Nếu bước review vẫn áp dụng, rủi ro thực tế chỉ còn đáng kể trong đúng một tình huống chưa được PRD nhắc tới: người tự chấm lại chính là Mentor chính của lớp (`BR-12.4`: mentor đầu tiên được thêm vào lớp) — khi đó họ vừa chấm vừa là người duyệt cuối, không ai kiểm. Domain tự nó cũng đang treo đúng câu hỏi này ở `05-grading.md` §10 Q5 ("Mentor chính tự chấm bài của mình rồi tự Finish được không, hay bắt buộc qua bước review"). Thiếu chỗ này, Dev có thể hiểu nhầm thành bỏ hẳn bước review cho mọi trường hợp tự chấm, còn QA không biết phải test riêng tình huống người tự chấm là Mentor chính. | Bổ sung ở `BR-12.8` hoặc mục 9 Giả định: nêu rõ mentor tự chấm vẫn đi qua luồng review hiện có của Mentor chính như bình thường; nêu riêng trường hợp người tự chấm chính là Mentor chính của lớp là tình huống rủi ro cao nhất vì không có bước review độc lập nào; thêm một câu hỏi mở ở mục 10 nối với `05-grading.md` §10 Q5 để Dev xác nhận hành vi hệ thống hiện có cho trường hợp này. |
| Minor | prd.md > US12 > `AC12.5`; US13 > `BR-13.7` | `BR-13.7` viết "nhất quán với US12: gán mentor không gửi email", coi như đây là một rule đã định nghĩa ở US12, nhưng mục Business rule của US12 không có dòng nào nói việc gán mentor không gửi email — sự kiện này chỉ xuất hiện ở `AC12.5` dưới dạng tiêu chí, không có mã BR để `BR-13.7` trỏ tới. | Thêm một business rule trong US12 ghi rõ gán hoặc gỡ mentor không gửi email cho mentor, để `AC12.5` và `BR-13.7` trỏ về đúng mã thay vì một câu mô tả không có mã. |

## Summary
PRD v0.6 đã khớp đầy đủ các thay đổi của CR6 (bỏ giới hạn cấp, một người nhiều vai một tài khoản học viên, gửi thông báo lên quản lý cấp gần nhất, tạm cho tự chấm, US18 thành tab Báo cáo), và mọi finding của bốn lần review trước đều đã đóng. Một Major mới phát sinh từ việc đối chiếu với domain Grading: PRD chưa làm rõ luồng review của Mentor chính có còn áp dụng khi mentor tự chấm bài của chính mình hay không, và rủi ro thực sự tập trung ở đúng trường hợp người tự chấm là Mentor chính — chỗ này có cách xử lý rõ ràng ở cột Required action nên không chặn gate.
