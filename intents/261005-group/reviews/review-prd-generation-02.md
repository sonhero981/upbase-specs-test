# Review: prd.md · 2.42 PRD Generation · lần 02
**Verdict:** READY
**Verdict Dictated:** yes
**Reviewer:** ai-reviewer · **Date:** 2026-10-20

## Prior findings
| ID | Severity | Now | Note |
|---|---|---|---|
| R-01 | Major | Fixed | `BR-11.7` đã thêm, `AC11.5` trỏ tới; chỉ định quản lý chính qua `US11` gửi `MAIL-GRP-02` như DEC76 yêu cầu |
| R-02 | Major | Fixed | `BR-13.6` đã ghi rõ: email gộp chỉ liệt nhóm người nhận chưa quản lý trực tiếp trước đó, không còn nhóm mới thì không gửi |
| R-03 | Minor | Fixed | `BR-9.7` và `BR-13.6` đã có câu nối hai trục: `BR-9.7` tính theo số người nhận, `BR-13.6` tính theo số nhóm, hai trục độc lập |
| R-04 | Minor | Fixed | `BR-13.7` đã ghi rõ phần quan hệ mentor được chuyển không báo qua `MAIL-GRP-02` |

## New findings
| Severity | Location | Finding | Required action |
|---|---|---|---|
| Major | `prd.md` > Document version v0.4 · `US5` · `US6` · `US8` · `US9` · `US10` · `US12` · `US13` · `US19` · `US20` | Dòng v0.4 trong Document version khẳng định "mỗi user story có tiêu chí cho nhánh bị từ chối hoặc lỗi", nhưng nhiều US không có `AC` nào cho nhánh đó. Cụ thể các US có hành động người dùng chủ động mà không có `AC` nào cho trường hợp bị chặn hoặc sai: `US8` bật tắt công tắc tự ghi danh, `US9` gán quản lý, `US12` gán mentor, `US13` chuyển phụ trách. `US5` còn rõ hơn: mục NFR tự nêu tình huống "Đồng bộ lỗi giữa chừng thì lần chạy sau phải tự sửa được chênh lệch" nhưng không `AC` nào kiểm hành vi đó. Đây đúng là loại nhánh mà CR3 được mở ra để phủ, nên khoảng trống này nằm ngay giữa phạm vi CR3, không phải việc để lại từ trước | Rà lại các US nêu trên, thêm `AC` cho nhánh lỗi hoặc bị từ chối nếu nhánh đó có thật trong luồng nghiệp vụ (ví dụ: `AC` cho `US5` khi đồng bộ lỗi giữa chừng, `AC` cho `US9`/`US12` khi gán người không hợp lệ hoặc gán trùng, `AC` cho `US13` khi chưa chọn người nhận hoặc không có nhóm nào để chuyển). Với US nào thật sự không có nhánh lỗi hoặc bị từ chối, ghi rõ lý do trong Comments thay vì để trống. Sau khi bổ sung, sửa câu khẳng định ở Document version v0.4 cho khớp đúng những gì đã làm |
| Major | `prd.md` > Vấn đề tồn đọng #3, #4 | Hai dòng vẫn ghi "Người trả lời: Người viết" như câu hỏi còn mở, nhưng PO đã chốt cả hai ở `DEC84` (loại quan hệ quản lý và mentor do hệ thống định nghĩa cố định, tổ chức không tự thêm loại mới) và `DEC85` (tài khoản kiểm thử và tài khoản trả lời bình luận tạo hoặc chọn thẳng trong UpLMS Ops, không qua cây Lark), cả hai ngày 12/10/2026. Cả `DEC84` và `DEC85` đều ghi rõ "PRD cập nhật dòng này ở lần sửa kế tiếp sau 2.41" — CR3 chính là lần sửa kế tiếp đó nhưng bảng Vấn đề tồn đọng chưa cập nhật. Đội Design, Tech, QA đọc PRD ở 2.43 sẽ tưởng hai điểm này còn treo, có thể hỏi lại một việc đã chốt hoặc tự đoán sai hướng đã quyết | Xoá hai dòng #3, #4 khỏi bảng Vấn đề tồn đọng hoặc sửa thành đã trả lời, dẫn đúng `DEC84` và `DEC85`. Nếu nội dung quyết định cần phản ánh thêm vào business rule hoặc Data Field của `US12`, mở change request riêng cho việc đó thay vì để câu hỏi nằm lẫn trong bảng như chưa có đáp án |

## Summary
PRD v0.4 đã thêm đủ khối Tiêu chí chấp nhận và dòng Ưu tiên cho cả 20 US như CR3 yêu cầu; 104 `AC` phủ đúng 130 `BR` theo kiểm bằng máy và đối chiếu tay, không GAP không ORPHAN ở lớp `BR` sang `AC`, và bốn finding của lần review 01 đã sửa đúng theo quyết định của PO (R-01 đến R-04 đều Fixed). Đầu vào mô tả CR3 là một thay đổi hẹp, chỉ thêm `AC` và dòng Ưu tiên, không đổi business rule hay màn hình — cách mô tả này gợi ý một lượt kiểm nhanh, nên tôi đánh dấu Verdict Dictated. Dù vậy khi rà theo đúng yêu cầu của chính CR3 thì lộ ra khoảng trống thật: nhiều US thiếu AC cho nhánh lỗi hoặc bị từ chối dù changelog khẳng định đã phủ đủ, và hai dòng Vấn đề tồn đọng đã lỗi thời so với quyết định đã chốt từ 12/10/2026. Cả hai finding đều có cách xử lý rõ và không chạm lại business rule, màn hình hay field đã duyệt, nên verdict vẫn READY.
