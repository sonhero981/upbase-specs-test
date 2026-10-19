# Yêu cầu gốc — Gamification

| | |
|---|---|
| Nguồn | PO cung cấp trực tiếp (ảnh chụp bảng + mô tả bối cảnh) |
| Ngày nhận | 23/09/2026 |
| Dạng gốc | Bảng 11 dòng + 1 câu bối cảnh |

> ⚠️ **Đây là bản chép nguyên văn.** Không diễn giải, không bổ sung, không sắp xếp lại.
> Mọi suy luận nằm ở `working/ai-drafts/`, không nằm ở đây.

---

## Bối cảnh (PO nói)

> hệ thống đã có các khóa học, đã có học viên, bây giờ làm chức năng gamification để thúc đẩy động lực học của các học viên

---

## Bảng yêu cầu (chép nguyên văn từ ảnh)

| Hạng mục | Nội dung |
|---|---|
| Hệ thống điểm | Khai hành động nào được bao nhiêu điểm, bật tắt từng hành động |
| Danh mục hành động tính điểm | Hoàn thành hoạt động, hoàn thành khóa, hoàn thành lộ trình, đạt bài kiểm tra, đạt điểm cao, đăng nhập nhiều ngày liên tiếp,... |
| Huy hiệu | Tên, hình, mô tả, điều kiện đạt |
| Các loại điều kiện huy hiệu | Theo số lượng hoàn thành, theo chuỗi ngày liên tiếp, theo mốc thời gian, theo hoàn thành một nội dung cụ thể, theo đạt một kỹ năng cụ thể |
| Hạng người học | Ngưỡng điểm cho từng hạng, tên và hình từng hạng |
| Chu kỳ tính điểm | Điểm tích lũy vĩnh viễn để xét hạng, và điểm theo kỳ để xếp hạng thi đua. Hai con số tách nhau, vì người vào sau không bao giờ đuổi kịp điểm tích lũy |
| Chống cày điểm | Không cộng điểm khi học lại nội dung đã hoàn thành, giới hạn điểm tối đa mỗi ngày, không cộng điểm cho hoạt động bỏ qua quá nhanh |
| Lịch sử điểm | Người học xem được từng lần cộng điểm đến từ đâu. Điểm không giải thích được thì không ai tin bảng xếp hạng |
| Thông báo thành tích | Nhận điểm, nhận huy hiệu, lên hạng đều có thông báo. Dùng hệ thống thông báo sẵn có, chỉ thêm sự kiện mới |
| Trang thành tích của tôi | Phía người học: điểm, hạng, huy hiệu đã có và huy hiệu sắp đạt kèm còn thiếu gì |
| Bật tắt gamification | Bật tắt ở cấp tổ chức. Có tenant không muốn dùng cơ chế này |
