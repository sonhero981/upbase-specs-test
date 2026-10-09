---
description: Stage 1.1 Intent Capture & Framing của luồng v2 theo AWS AI-DLC. Gọi qua /po
argument-hint: <intent-slug>
---
# 1.1 Intent Capture & Framing

| | |
|---|---|
| Stage | 1.1 Intent Capture & Framing |
| Slug | intent-capture |
| Phase | ideation |
| Plugin | (stage gốc AWS) |
| Execution | always ở M và L |
| Lead | product |
| Produces | `ideation/intent-capture/intent-statement.md` · `intent-capture-questions.md` |
| Consumes | `inputs/*` (bắt buộc) · `intent.md` · KB 15 product direction · KB 16 domain principles |
| Requires | không |
| Profiles | M, L |
| Reviewer | product-lead ở L. M: none |
| Summary confirmation | required |
| Template | `.claude/templates/intent-statement.md` |
| Checklist | `.claude/verification/intent-capture.md` |
| Knowledge | `.claude/knowledge/domain/00-index.md`, `15-product-direction.md`, `16-domain-principles.md` · product: `product-guide.md` §Persona Development, `requirements-elicitation.md` §Stakeholder Interviews |

Chạy theo `.claude/protocol/stage-protocol.md`. Dưới đây chỉ là phần riêng của stage.

## Mục đích
Khung vấn đề trước khi bàn giải pháp: ai gặp vấn đề gì, vì sao bây giờ, đo thành công bằng gì, ai liên quan và ai quyết. AWS: stage 1.1 do Product Agent dẫn. Thay cho phần đầu của Bước 1 đến 3 và BRD mục 1 đến 4 của luồng cũ.

## Load
- Đọc nguyên văn `inputs/`. Tách **giải pháp người yêu cầu đã nghĩ sẵn** ra khỏi **vấn đề**. "Thêm nút export" là giải pháp; vấn đề có thể là "không lấy được dữ liệu ra để đối chiếu". Giải pháp đó là Recommendation, chưa phải yêu cầu.
- KB 15 và 16: yêu cầu thuộc tầng nào của UpLnD, phục vụ UpBase hay mọi tenant, có đụng nguyên tắc mô hình hoá nào.
- `intent.md` mục Related intents: trùng hay phụ thuộc intent khác không.

## Ask
Gợi ý, không phải kịch bản. Bỏ câu đã có đáp án trong inputs.
1. Vấn đề nghiệp vụ, theo góc nhìn người dùng: ai gặp, khi nào, hậu quả.
2. Người dùng đang xoay xở thế nào khi chưa có tính năng: làm gì, theo thứ tự nào, dựa vào tiêu chí gì, mất bao lâu, hay sai ở đâu.
3. Thành công trông như thế nào, đo bằng chỉ số nào, lấy số ở đâu.
4. Vì sao làm lúc này: áp lực, cơ hội, hay nợ cũ.
5. Stakeholder: ai quan tâm điều gì, ai quyết phạm vi và ưu tiên, ai chỉ cần được báo.
6. Bản đầu tiên không làm gì. Hỏi về sản phẩm, không hỏi lại profile.
7. Portal nào: UpLMS, Ops, hay cả hai. Hằng số nào phải cấu hình theo tenant.
Mỗi câu có lựa chọn "Chưa xác định" khi PO có thể chưa biết. Không bịa stakeholder.

## Generate
`intent-statement.md` theo template. Thẻ nguồn ở mọi khối: `[desc]`, `[Q3]`, `[KB-15 §6]`, `[assumption]`. Stakeholder map có cột Nguồn. Mục Assumptions & Open Questions bắt buộc.
Success metrics: tự đề xuất ít nhất một cách đo cho mỗi objective, chỉ giữ cái đo được từ dữ liệu hệ thống sẽ có. Không có số thì mô tả cách làm hiện tại đủ rõ, không bỏ trống.

## Verify
Checklist của stage. Reviewer product-lead ở L.

## Gate
- Profile L: gate riêng. Trình: vấn đề một đoạn, objective kèm cách đo, stakeholder, ràng buộc, assumption đáng chú ý, OQ còn chặn.
- Profile M: không hỏi gate ở đây. Đánh dấu 1.1 `[?]`, chạy tiếp 1.4 trong cùng lượt, gate chung ở cuối 1.4 theo `gate-protocol.md`.

Stage kế: 1.2 nếu PO muốn so với sản phẩm khác, không thì 1.4.
