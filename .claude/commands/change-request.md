---
description: Đổi hoặc bổ sung yêu cầu sau khi một stage đã duyệt. Ghi CR vào decisions.md, chụp archive, mở lại đúng stage, duyệt lại gate
argument-hint: <intent-slug> <mô tả thay đổi>
---
# /change-request

Dùng khi yêu cầu thay đổi hoặc bổ sung sau khi artifact đã qua gate. Tự kích hoạt khi PO nói *"tôi có thay đổi yêu cầu"*, *"bổ sung"*, *"đổi scope"*, *"thêm một rule"*, *"khách yêu cầu thêm"*.

Xác định intent: ưu tiên `$ARGUMENTS`; không có thì suy từ file đang mở; hơn một khả năng thì liệt kê cho chọn, không đoán. Echo và confirm trước khi chạy.

## 1. Phân loại
Thay đổi nhỏ trong stage đang mở (`[-]`, `[?]`, `[R]`): sửa và trình lại gate, không cần CR. Thay đổi chạm stage đã `[x]` mới đi đường CR.

## 2. Điểm re-entry
Hỏi: *thay đổi này làm sai lệch kết luận của stage nào?* Lấy stage thấp nhất bị sai, không lấy stage dễ sửa nhất.

| Loại thay đổi | Re-entry từ stage | Cascade |
|---|---|---|
| Vấn đề, mục tiêu, stakeholder | 1.1 | mọi stage sau |
| Phạm vi, Proto-Unit | 1.4 | 2.3 trở đi |
| FR, NFR, rule nghiệp vụ mới | 2.3 | 2.31 trở đi |
| Phát hiện ảnh hưởng mới | 2.31 | 2.32 trở đi |
| Đổi hướng giải | 2.32 | 2.4 trở đi |
| Danh sách US, Proto-Unit | 2.4 | 2.41, 2.42 |
| Định hướng Design, Tech, Test, quyết định ở họp liên team | 2.41 | 2.42. Phải lấy lại sign-off |
| Chi tiết US, field, rule, màn | 2.42 | chỉ US bị chạm |
| Chỉ đổi User Guide | user-guide | — |

Ví dụ: *"thêm rule học viên bị Block thì không nộp được bài"* là business rule mới, nhưng nó thêm một nhánh mà Impact Matrix chưa quét, nên re-entry từ 2.3 và chảy qua 2.31, không phải chỉ sửa PRD.

## 3. Ghi CR và chụp archive
- Thêm `CR<n>` vào bảng Change requests của `decisions.md` kèm một DEC ghi nguyên văn PO. Không có file change-requests riêng; phân tích dài thì viết vào `inputs/change-requests.md` và trỏ từ bảng.
- Trước khi sửa bất kỳ artifact nào: `python3 .claude/scripts/po-tools.py archive .claude/intents/<intent> <stage-slug> <artifact> --label pre-CR<n>`.

## 4. Impact preview, PO xác nhận
Trình bằng hộp chọn: stage re-entry kèm lý do, artifact sẽ đổi, gate phải duyệt lại. PO xác nhận rồi mới chạy. Nếu bảng này đã nằm trong thông điệp gate ngay trước và PO đã trả lời "theo đề xuất", không hỏi lại.

## 5. Chạy lại xuôi, chế độ sửa
- Mỗi stage mở lại: hỏi Giữ, Sửa, hay Làm lại từ đầu. `state.md` đặt stage đó `[R]`, stage sau bị chạm về `[ ]`.
- Chỉ sửa phần bị chạm, không viết lại cả artifact. Tăng version ở frontmatter, thêm dòng Document version với Impact `CR<n>`. PRD chỉ chạm US bị ảnh hưởng, Document status về `IN REVIEW`.
- Reviewer theo profile ở stage bị chạm; finding đi vào gate, không tự sửa theo finding.
- Trình lại gate theo `gate-protocol.md`. Nhiều stage nhỏ có thể gộp trong một thông điệp nhưng ghi rõ duyệt từng artifact.
- 2.41 bị chạm thì lead ký lại; 2.42 bị chạm thì publish lại PRD sau Approve.

## 6. Tác động ngược
Trước gate 2.42: chạy `po-tools.py trace`; kiểm business rule mồ côi (rule cũ còn US nào dùng không), mã tham chiếu gãy (`BR-2.3` bị xoá mà chỗ khác còn trỏ), Out of scope lỗi thời (thứ từng ghi "không làm" nay đã làm, hoặc ngược lại).

## 7. Sau khi duyệt
Chụp archive bản mới, đóng CR trong bảng, cập nhật Versions trong `state.md`, publish lại artifact bàn giao đã lên Lark.

## Output
CR đã ghi; stage mở lại; artifact đã sửa và version; gate chờ duyệt lại; tác động ngược phát hiện được. Tự kiểm theo `.claude/verification/change-request.md`.
