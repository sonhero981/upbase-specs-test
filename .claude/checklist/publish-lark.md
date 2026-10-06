# Checklist: Publish Lark

## Tiền điều kiện
- [ ] **[BLOCK]** Artifact đã qua Gate tương ứng. Còn `Draft - Pending Confirmation` → **không publish**
- [ ] Đã đọc Lark target từ `project-context.md`. Thiếu → đã hỏi và ghi lại
- [ ] Kết nối Lark: dùng MCP nếu có, không có → tự chạy OAuth
- [ ] **Token hết hạn → hỏi người dùng cấp quyền lại**, không báo "không kết nối được"

## Xác nhận trước khi đẩy
- [ ] **[BLOCK]** Đã trình người dùng: artifact + version · space + parent node · tạo mới hay cập nhật
- [ ] **Đã cảnh báo nếu `Preferences` chứa credentials staging** — phạm vi người đọc trên Lark rộng hơn local
- [ ] Người dùng skip → **không đẩy gì cả**, không coi là lỗi

## Chuyển đổi
- [ ] **[BLOCK]** Fidelity 1:1 — không tóm tắt, không gộp section, không lược bỏ dòng nào
- [ ] Bảng giữ **đủ mọi cột và mọi dòng** — bảng UI trong AC thường 30+ dòng
- [ ] Mã tham chiếu (`US1`, `BR-2.3`) giữ nguyên
- [ ] Link giữ nguyên, đặc biệt link trong `Preferences`
- [ ] **Không tự thêm lại mục đã xoá** — xoá là có chủ đích
- [ ] Có ảnh → đã **báo rõ ảnh nào phải chèn tay** kèm đường dẫn. **Không lặng lẽ bỏ ảnh**

## Idempotent
- [ ] **[BLOCK]** Đã tra node đã lưu trước khi tạo — **không tạo trùng**
- [ ] Đã có node → cập nhật đúng node cũ

## Sau khi publish
- [ ] **[BLOCK]** Đã **đọc lại** node và đối chiếu: số heading · số dòng từng bảng · không mục nào bị gộp/mất
- [ ] Lệch → đã **báo cụ thể mục nào thiếu**
- [ ] Đã cập nhật `project-context.md` mục `Lark → Đã publish` (node token · URL · ngày)

## Cấu trúc wiki
- [ ] **[BLOCK]** **Node dự án đã tồn tại?** Chưa → **tạo node dự án trước**, rồi mới publish tài liệu vào trong nó
- [ ] Tài liệu **không** nằm thẳng dưới node cha chung — một dự án sinh nhiều tài liệu, phải gom lại
- [ ] Người dùng đã đổi tên tài liệu trên Lark → **giữ nguyên tên họ đặt**, chỉ cập nhật nội dung
- [ ] Lưu **cả node token lẫn document token** vào `project-context.md`

