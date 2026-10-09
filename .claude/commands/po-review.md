---
description: Review độc lập bằng agent Product Lead cho một artifact của luồng v2, hoặc tài liệu bất kỳ ở chế độ shadow
argument-hint: <đường dẫn file> [--shadow] [--stage <slug>]
---
# /po-review

Theo `.claude/protocol/review-protocol.md`. Không sửa artifact. Không ghi `state.md` trừ khi được gọi từ một stage.

1. Xác định artifact và stage. Thư mục stage cho biết slug; `--stage` để chỉ rõ. File ngoài `.claude/intents/` hoặc có `--shadow` thì chạy chế độ shadow.
2. Input Readiness Gate, giữ từ luồng cũ: artifact có đủ nền chưa, stage trước đã approve chưa. Thiếu thì báo và hỏi có review tiếp không. Review PRD trên Impact Matrix chưa duyệt là review trên cát.
3. Gọi agent `product-lead` bằng Task. Truyền đường dẫn, không dán nội dung: stage command, questions file, artifact, artifact đầu vào, `GLOSSARY.md`, KB liên quan, file review lần trước nếu có. Yêu cầu ghi `reviews/review-<slug>-<NN>.md`, NN là số lần trước cộng một. Nói với PO một câu: "Để Product Lead xem qua trước khi anh/chị đọc."
4. Đọc file review, trình verdict, bảng finding, summary. PO quyết: sửa, hoặc ghi disposition vào `decisions.md` (Accepted risk, Rejected kèm lý do, Reopened).

## Chế độ shadow, tài liệu người khác viết
Trước khi gọi agent: tóm tắt tài liệu để PO xác nhận hiểu đúng. Agent nhận thêm nhiệm vụ: quét KB, Swagger, so với hệ thống thật; findings chia ba nhóm sai, thiếu, mơ hồ; phụ lục A nguồn đã đọc kể cả chưa tra được; phụ lục B câu AI tự trả lời được kèm nguồn và độ chắc. Mục đích là tìm chỗ sai so với hệ thống thật, không chấm cách viết.
