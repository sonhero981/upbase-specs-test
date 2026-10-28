# Units Generation, câu hỏi
Intent: 260923-gamification · Người trả lời: FE lead + BE lead · Cách trả lời: Chat · Đã trả lời: 7/7 ([GIẢ LẬP] BE lead, test workflow)

Phạm vi cả intent (DEC-T15), đầu vào `inception/domain-design/` v2.0 (DEC-T19). Không hỏi thứ tự làm, đường găng: đó là 2.9.

## Q1. Chia Unit theo cách nào?
Vì sao hỏi: team có 2 dev BE (vietlh, cuongdq theo `assignment.md` lms-be, chia theo tầng) và 1 dev FE (Nguyễn Hùng Sơn); PRD đề xuất 7 Proto-Unit theo cơ chế.
A. Lát dọc theo US: một US đúng một Unit, BE + FE cùng Unit khi xây và test được cùng nhau; 2.9 gán người theo phần BE/FE của từng Unit  [đề xuất, theo tech-protocol "mỗi US đúng một Unit", demo được từng Unit]
B. Theo tầng giống WP của `assignment.md` (libs, ops, lms, FE riêng)
X. Khác
Chặn: có
[Answer]: [GIẢ LẬP BE lead] A, "2.9 map lại WP của assignment sang Unit."

## Q2. Độ mịn Unit?
A. Mỗi Unit ≤ ~3 ngày công, tách Proto-Unit thành nhiều Unit (thường một US một Unit)  [đề xuất, theo trần của tech-protocol]
B. Giữ 7 Proto-Unit của PRD, Unit lớn hơn 3 ngày
X. Khác
Chặn: có
[Answer]: [GIẢ LẬP BE lead] A

## Q3. Walking skeleton cho cả intent?
Vì sao hỏi: intent chạm ≥ 2 repo nên skeleton bật mặc định; U0 là skeleton của nhánh Ops và đã có thiết kế Construction, nhưng chưa đi qua lms-fe, Kafka, socket, cron.
A. Giữ U0 là Unit gốc (ngoại lệ có ký); mỗi điểm tích hợp còn lại do Unit gần gốc nhất trong DAG chạm tới chạy thật đầu-cuối (bảng ở `unit-of-work.md` mục Walking skeleton), không dựng U0 mới  [đề xuất, không làm lại thiết kế đã có của U0]
B. Dựng thêm một Unit skeleton mỏng qua mọi điểm tích hợp trước mọi Unit nghiệp vụ
X. Khác
Chặn: có
[Answer]: [GIẢ LẬP BE lead] A

## Q4. Cho phép làm song song các Unit không phụ thuộc nhau?
A. Có, theo DAG; 2.9 quyết thứ tự thực tế  [đề xuất]
B. Chỉ tuần tự theo topo
X. Khác
Chặn: không
[Answer]: [GIẢ LẬP BE lead] A

## Q5. Mô hình triển khai?
A. Mọi Unit `embedded` trong app có sẵn (lms, ops, mock-test, event-processor, background-job; feature module FE), phát hành sau công tắc tắt mặc định  [đề xuất]
B. Tách service gamification riêng
X. Khác
Chặn: không
[Answer]: [GIẢ LẬP BE lead] A

## Q6. Unit vượt trần — ngày công (U1 3,5; U11 4,5) và nhóm AC (U0 7; U5 7) — xử lý thế nào? (review R-03, R-10)
Vì sao hỏi: story không chia được (mỗi US đúng một Unit); nhóm AC đo tái lập được = số bảng trong mục `4/` của PRD.
A. Chấp nhận ngoại lệ có ký cho U0, U1, U5, U11 (ghi lý do; 2.9 cho BE và FE làm song song trong cùng Unit; 3.1 xem lại ngày công U5, U17)  [đề xuất]
B. Tách US6 theo AC thành hai Unit (BE tính bảng, FE màn)
X. Khác
Chặn: có
[Answer]: [GIẢ LẬP BE lead] A, "Ngoại lệ có ký. Không tách US."

## Q7. Phần học viên xem kết quả campaign đã đóng băng (BR-19.6) nghiệm thu ở Unit nào? (review R-04)
A. Ở U17 (Unit đóng băng), story map vẫn giữ US19 ở U16; ghi ở bảng "AC nghiệm thu ở Unit khác"  [đề xuất]
B. Đảo cạnh: U16 phụ thuộc U17
X. Khác
Chặn: không
[Answer]: [GIẢ LẬP BE lead] A

## Consolidated Summary
- Lát dọc theo US, mỗi Unit ≤ ~3 ngày công trừ ngoại lệ Q6; 18 Unit (U0…U17), U0 giữ Unit đã có thiết kế.
- Skeleton: U0 gốc (ngoại lệ có ký), điểm tích hợp còn lại chạy thật ở Unit gần gốc nhất trong DAG.
- Song song theo DAG; mọi Unit `service`, `embedded`.
- U1, U11 vượt trần ngày công, U0, U5 vượt trần nhóm AC: ngoại lệ có ký; nhóm AC = số bảng trong mục `4/` PRD.
- AC nghiệm thu ở Unit khác ghi riêng (BR-14.13 campaign → U15, quyền xem học viên → U4, BR-19.6 → U17, BR-10.7 → U10).

Xác nhận: [GIẢ LẬP BE lead] Looks correct. Plan được duyệt (Step 4, Approve Plan).
