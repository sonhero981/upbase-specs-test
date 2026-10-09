# Checklist: 2.42 PRD Generation

## Tiền điều kiện
- [ ] **[BLOCK]** M, L: HLD Brief approved. S: requirements approved
- [ ] **[BLOCK]** Field Intake đã PO xác nhận. `❓BA` chưa quyết thành OQ

## Phần đầu
- [ ] Problem, Analytics, Objective, Out of scope, Stakeholder, Metrics success, Solution, Proto-Units chép từ HLD Brief, không viết lại
- [ ] **[BLOCK]** Metrics success là chỉ số thật của tính năng, hoặc đã xoá. Không còn bảng ví dụ
- [ ] References có link HLD Brief, Figma. Tài khoản staging để trống
- [ ] **[BLOCK]** Không có mục Database và API. Không sequence diagram, cấu trúc bảng, thuật toán, thư viện

## Specific Requirement
- [ ] US đánh số liên tục. US chưa làm ghi rõ trong tiêu đề
- [ ] Mỗi US đủ sáu mục. Conner case để trống
- [ ] Bảng UI đúng dạng A hoặc B, cột Yêu cầu đủ định dạng, placeholder, options, mặc định, disable, tooltip, validate, hành vi
- [ ] BR mã `BR<US>.<n>`, không trùng. Rule chạm tính năng có sẵn dẫn mã KB
- [ ] **[BLOCK]** Field hiện có ghi là hiện có. Không bịa field
- [ ] Hằng số ghi cứng hay cấu hình
- [ ] Mail event bị chạm đối chiếu KB 13

## Truy vết và review
- [ ] **[BLOCK]** Traceability: không GAP, không ORPHAN. `verification/phase-check-inception.md` đạt
- [ ] Reviewer product-lead đã chạy

## Bàn giao
- [ ] **[BLOCK]** Không còn chữ mẫu template. Mục không áp dụng đã xoá
- [ ] **[BLOCK]** Không dấu vết quy trình. Không viết tắt. Dấu `·` giữa mã
- [ ] Sơ đồ Mermaid đặt đúng chỗ, tránh hai lỗi trên Lark
- [ ] Profile S: PRD rút gọn đúng danh mục mục
