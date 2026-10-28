# Delivery Planning, câu hỏi
Intent: 260923-gamification · Người trả lời: họp FE lead, BE lead, PO, QA, owner Bolt · Cách trả lời: Chat · Đã trả lời: 7/7 ([GIẢ LẬP] họp, test workflow)

Phạm vi cả intent (DEC-T15). Một Bolt là một lượt xây trọn một phần việc, kết thúc bằng thứ chạy được trên staging. Đầu vào: 18 Unit (2.7 v2.0), 28 contract Agreed (2.8 v2.0), `assignment.md` lms-be.

## Q1. Xây gì trước?
A. Trộn: walking skeleton trước (B01 và các Bolt mở điểm tích hợp mới), rủi ro cao trước (engine, realtime, bảng xếp hạng), còn lại theo giá trị theo thứ tự PRD  [đề xuất]
B. Thuần giá trị theo thứ tự PRD
C. Chấm WSJF từng Bolt
X. Khác
Chặn: có
[Answer]: [GIẢ LẬP họp] A

## Q2. Một Bolt gồm mấy Unit?
A. Một Unit một Bolt (Unit đã ≤ ~3 ngày, trừ ngoại lệ có ký)  [đề xuất]
B. Gộp Unit nhỏ (vd U9 + U10)
X. Khác
Chặn: có
[Answer]: [GIẢ LẬP họp] A

## Q3. Owner Bolt khi team chia BE / FE?
Vì sao hỏi: tech-protocol muốn một owner làm trọn mọi repo của Bolt; team có hai dev BE (vietlh, cuongdq) và một dev FE (Sơn).
A. Owner BE chịu DoD và mở change `run`; Sơn làm phần FE trong cùng Bolt (ghi lệch protocol)  [đề xuất]
B. Mỗi dev làm trọn Bolt fullstack (BE dev tự làm FE)
X. Khác
Chặn: có
[Answer]: [GIẢ LẬP họp] A, "BE lead: hai dev BE chưa quen lms-fe; ops-fe đơn giản thì có thể giúp (xem Q5)."

## Q4. Song song?
A. Bolt không phụ thuộc nhau chạy song song khác owner BE; FE mock theo contract Agreed để không chờ BE  [đề xuất]
B. Tuần tự
X. Khác
Chặn: không
[Answer]: [GIẢ LẬP họp] A

## Q5. FE một người là đường găng — xử lý thế nào?
Vì sao hỏi: Sơn gánh phần FE của mọi Bolt (gần gấp đôi tải mỗi dev BE), kéo ngày xong.
A. Dev BE làm trọn các Bolt ops-fe đơn giản (đưa vào lịch, không chỉ "khi rảnh"); CTO xem xét thêm dev FE lms-fe ở họp sprint  [đề xuất]
B. Thêm một dev FE ngay
C. Cắt đợt: Campaign (B16–B18) sang đợt 2
X. Khác
Chặn: không
[Answer]: [GIẢ LẬP họp] A, "PO: giữ cả intent trong đợt này, chưa cắt; xem lại sau B12."

## Q6. Bật trên production theo mốc nào?
A. Theo mục Release constraints ở `risk-and-sequencing-rationale.md`: chạy ngầm sau B02, B03, B05, B06; hiển thị thêm B04, B07, B08; từng chức năng sau Bolt của nó  [đề xuất]
B. Bật một lần khi xong B18
X. Khác
Chặn: không
[Answer]: [GIẢ LẬP họp] A

## Q7. Gán owner BE theo mảng `assignment.md` hay theo lịch xong sớm nhất? (review R-03)
Vì sao hỏi: thử nhiều cách gán (owner BE vietlh/cuongdq, FE ops-fe Sơn hoặc dev BE), có tính 0,5 ngày thiết kế mỗi người mỗi Bolt: giữ mảng core cho vietlh (engine, check-in, realtime, huy hiệu, hạng, bảng xếp hạng) xong sau 26 ngày làm việc; gán tự do xong sau 23 ngày (16/11), tải lệch ≤ 2,5 ngày.
A. Gán theo lịch xong sớm nhất (bảng Bolts); `assignment.md` cập nhật theo  [đề xuất]
B. Giữ mảng core cho vietlh, chấp nhận chậm 3 ngày
X. Khác
Chặn: không
[Answer]: [GIẢ LẬP họp] A, "BE lead: hai dev đều đọc được engine; review chéo MR."

## Consolidated Summary
- Skeleton + rủi ro trước, còn lại theo giá trị; 18 Bolt, mỗi Bolt một Unit; B01 giữ số.
- Owner BE chịu DoD, Sơn làm FE lms-fe; dev BE làm trọn bốn Bolt ops-fe; owner gán theo lịch xong sớm nhất (16/11).
- Song song theo DAG, FE mock theo contract Agreed.
- Bật production từng nấc theo Release constraints.

Xác nhận: [GIẢ LẬP họp] Looks correct.
