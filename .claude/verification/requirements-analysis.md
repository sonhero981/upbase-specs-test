# Checklist: 2.3 Requirements Analysis

## Tra KB trước khi hỏi
- [ ] **[BLOCK]** Mỗi hạng mục đã tra: đã có chưa, rule hiện có, Hidden, mail event, vùng KB chưa phủ
- [ ] Yêu cầu trùng thứ đã có được nêu ngay, kèm mã KB
- [ ] Chạm dữ liệu: nguồn sống đã đọc lại nếu quá một tháng kể từ Last verified
- [ ] Vùng KB chưa phủ ghi `❓BA`, không kết luận "chưa có" hay "không ảnh hưởng"

## FR, NFR
- [ ] **[BLOCK]** Mỗi FR kiểm chứng được, có mã ổn định, ưu tiên, cờ Existing, New, Changed, nguồn
- [ ] **[BLOCK]** Không có FR mô tả bảng, endpoint, thuật toán. FR nói cái gì phải đúng
- [ ] NFR chỉ ghi khi đo được
- [ ] Constraints ghi hằng số cứng hay cấu hình

## Góc
- [ ] Mỗi góc áp dụng (rỗng, trùng, đồng thời, dữ liệu cũ, Block, lớp kết thúc, nhiều nhóm, mail hàng loạt) đã thành FR, assumption có lý do, hoặc out of scope

## Câu hỏi và nguồn
- [ ] Không hỏi kỹ thuật cho Dev. Chỉ hỏi câu đổi phạm vi hoặc rule
- [ ] Câu chặn đã trả lời. Nguyên văn
- [ ] **[BLOCK]** Thẻ nguồn ở mọi khối. Assumptions & Open Questions có cờ Chặn và owner
- [ ] Sources read có Last verified và mục chưa tra được

## Giao
- [ ] Reviewer product-lead đã chạy ở M, L
- [ ] Profile S: PRD rút gọn là stage kế, không chạy 2.31
