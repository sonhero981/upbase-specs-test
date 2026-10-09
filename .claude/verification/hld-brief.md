# Checklist: 2.41 HLD Brief & Alignment

## Nội dung
- [ ] **[BLOCK]** Không quá 1.500 từ, tính bằng đếm từ
- [ ] Mục 1 mười dòng, đọc một phút hiểu được
- [ ] Mục 1 đến 7, 11 chép từ artifact đã duyệt, không có nội dung mới
- [ ] **[BLOCK]** Mục 8, 9, 10 để trống cho lead khi giao. AI không viết thay lead, kể cả khi PO yêu cầu
- [ ] Đầu mục 8, 9, 10 có tối đa năm dòng "Điểm cần lưu ý cho <vai>", in nghiêng, lấy từ artifact đã duyệt
- [ ] Mục 6 có bảng rủi ro đã chấp nhận, giả định lớn, finding còn treo, tối đa bảy dòng, mỗi dòng có điều kiện kèm theo
- [ ] Mục 7 có quyết định thật cần chốt, mỗi dòng có ai quyết và hạn
- [ ] Mục 12 có tên ba lead, trạng thái Chưa xem

## Văn phong
- [ ] **[BLOCK]** Không thẻ nguồn, không từ quy trình, không viết tắt, mã kèm nội dung, dấu `·` giữa mã
- [ ] Mục 4 không có bảng dữ liệu, endpoint

## Lead làm trên repo
- [ ] Trước khi giao: đã chụp bản nháp vào `archive/hld-brief/`, `state.md` ghi hạn chờ lead
- [ ] Mục 8, 9, 10 là nguyên văn của lead. Lead gửi qua PO thì mở đầu "(ghi theo <tên>, <ngày>)" và có tin nhắn xác nhận lưu trong `decisions.md`
- [ ] Lead sửa mục 1 đến 7 hoặc 11: PO đã quyết nhận hay trả lại, có DEC nếu nhận
- [ ] Quyết định trong họp ghi DEC, người quyết là lead tương ứng
- [ ] Định hướng của lead mâu thuẫn artifact đã duyệt đi qua `/change-request`

## Gate
- [ ] **[BLOCK]** Approve chỉ khi ba lead ghi Đồng ý hoặc Có ý kiến ở mục 12, hoặc PO Accept as-is kèm lý do khi thiếu chữ ký. Có "Yêu cầu sửa" thì không Approve
- [ ] Request Changes: AI chỉ sửa mục của PO
- [ ] **[BLOCK]** Publish Lark chỉ sau Approve, bản 1.0, tên `[HLD] <tên>`, link ghi vào frontmatter, `intent.md`, `state.md`
