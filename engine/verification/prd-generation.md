# Checklist: 2.42 PRD Generation

## Tiền điều kiện
- [ ] **[BLOCK]** M, L: stories approved. S: requirements approved
- [ ] **[BLOCK]** Field Intake đã PO xác nhận. `❓PO` chưa quyết thành OQ

## Phần đầu
- [ ] Problem, Analytics, Objective, Out of scope, Stakeholder, Metrics success, Solution, Units lấy từ artifact đã duyệt, không viết lại. Technical Direction chỉ có ràng buộc nghiệp vụ
- [ ] **[BLOCK]** Metrics success là chỉ số thật của tính năng, hoặc đã xoá. Không còn bảng ví dụ
- [ ] References có link Figma và tài liệu liên quan. Tài khoản staging để trống
- [ ] **[BLOCK]** Không có mục Database và API. Không sequence diagram, cấu trúc bảng, thuật toán, thư viện

## Specific Requirement
- [ ] US đánh số liên tục. US chưa làm ghi rõ trong tiêu đề
- [ ] Mỗi US đủ sáu mục. Conner case để trống
- [ ] Mỗi US có dòng Ưu tiên Must, Should hoặc Could, khớp `stories.md`
- [ ] Bảng UI đúng dạng A hoặc B, cột Yêu cầu đủ định dạng, placeholder, options, mặc định, disable, tooltip, validate, hành vi
- [ ] BR mã `BR<US>.<n>`, không trùng. Rule chạm tính năng có sẵn dẫn mã KB
- [ ] **[BLOCK]** Mỗi US có danh sách AC mã `AC<US>.<n>`, không trùng. Mỗi AC kiểm được, có đạt hoặc không đạt, dạng "Khi..., ..."
- [ ] **[BLOCK]** Mọi BR có ít nhất một AC trỏ tới. Luồng chính và mỗi nhánh đáng kể trong thẻ US có AC
- [ ] **[BLOCK]** Mỗi US có ít nhất một AC cho nhánh lỗi hoặc bị từ chối. Mỗi ngưỡng số có AC ở giá trị biên
- [ ] US phụ thuộc US khác ghi mã `US<n>` ở Pre-Condition
- [ ] Validate của một màn gom thành một AC trỏ về bảng UI, không mỗi dòng bảng một AC
- [ ] **[BLOCK]** Frontmatter `feature:` và hàng Mã tính năng có mã tính năng của intent
- [ ] **[BLOCK]** Field hiện có ghi là hiện có. Không tự thêm field
- [ ] Hằng số ghi cứng hay cấu hình
- [ ] Sự kiện, mail bị chạm đối chiếu file sự kiện trong KB
- [ ] **[BLOCK]** M, L: điểm phụ thuộc thiết kế hay kỹ thuật mà artifact đã duyệt chưa nói có `[đề xuất]` và OQ gắn tên PIC ở Open Issues. PRD không quy định cách làm kỹ thuật
- [ ] PRD không quy định phần mục 9 ghi "Dev tự quyết ở detailed design"

## Truy vết và review
- [ ] **[BLOCK]** Traceability: không GAP, không ORPHAN. `verification/phase-check-inception.md` đạt
- [ ] Reviewer ai-reviewer đã chạy, sau `po-tools.py review-start`, và artifact không đổi sau lần review đó

## Bàn giao
- [ ] **[BLOCK]** Không còn chữ mẫu template. Mục không áp dụng đã xoá
- [ ] **[BLOCK]** Không dấu vết quy trình. Không viết tắt. Dấu `·` giữa mã
- [ ] Sơ đồ Mermaid đặt đúng vị trí, tránh hai lỗi trên Lark
- [ ] Profile S: PRD rút gọn đúng danh mục mục
