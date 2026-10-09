# Review Protocol

Review độc lập do agent `product-lead` làm. Bám theo AWS AI-DLC `stage-protocol-reviewer.md` và `knowledge/aidlc-product-lead-agent/reviewing.md`. Ở các stage văn bản của PO, review là **tham vấn**: finding đi vào gate, PO quyết, không có vòng tự sửa.

## Khi nào chạy
- Stage có Reviewer `product-lead` và profile bật reviewer: sau bước Verify checklist, trước Learn và Gate.
- Sau Request Changes mà artifact đổi: một lượt nữa.
- PO yêu cầu ("review lại cái này"): chạy, không giới hạn số lần.
- `/po-review <file>`: review một tài liệu bất kỳ. `/po-review --shadow <file>`: tài liệu người khác viết, xem mục Shadow.

## Gọi reviewer
- Dùng Task gọi agent `product-lead` trong `.claude/agents/`. Agent này không thấy cuộc hội thoại. Đó là chủ đích.
- Truyền đường dẫn, không dán nội dung: stage command, questions file, artifact cần review, artifact đầu vào, `GLOSSARY.md`, file KB liên quan, file review lần trước nếu có.
- Không truyền: `memory.md`, bản nháp, lý luận của AI soạn thảo.
- Nói với PO một câu: "Để Product Lead xem qua trước khi anh/chị đọc."

## Reviewer làm gì
- Đọc stage command để biết stage phải sinh gì. Đọc questions file để biết bối cảnh. Đọc artifact để đánh giá.
- Chỉ ghi một file: `reviews/review-<slug>-<NN>.md`. Không sửa artifact. Không trả lời câu hỏi của stage.
- Lần sau: nhận file review trước, ghi lại từng finding cũ là *Fixed* hay *Still applies*. Finding mới không có ID, AI điều phối cấp ID tiếp theo.

## Tiêu chí của Product Lead
1. Dev đọc có biết phải làm gì không. Không thì NOT-READY.
2. QA có viết được test từ acceptance criteria không. Không thì NOT-READY.
3. Có gì ngầm hiểu mà chưa viết. Giả định là lỗ hổng.
4. Mọi mục có giá trị với người dùng hay nghiệp vụ không. Thừa là lấn phạm vi.
5. Biên có rõ không: In, Out, để sau.
6. Góc đã chốt chưa: rỗng, trùng, đồng thời, dữ liệu cũ, người bị Block, lớp đã kết thúc. Mỗi góc phải là rule, giả định có lý do, hoặc ngoài phạm vi.
7. Mọi FR truy được về nhu cầu, mọi US truy được về FR. Mồ côi là finding.
8. Thẻ nguồn còn đủ, assumption chưa bị nâng thành fact.
9. Vùng KB chưa phủ có `❓BA`, không kết luận bừa.

## File review
```markdown
# Review: <artifact> · <stage> · lần <NN>
**Verdict:** READY | NOT-READY
**Reviewer:** product-lead · **Date:** <ISO>

## Prior findings
| ID | Now | Severity | Note |
|---|---|---|---|

## New findings
| Severity | Location | Finding | Required action |
|---|---|---|---|
| Major | requirements.md > FR4 | Chưa nói dữ liệu trước 01/09 xử lý sao | Thêm một dòng ở FR4 hoặc đưa vào Out of scope |

## Summary
Một hai câu: điều lớn nhất đang cản, hoặc vì sao đã sẵn sàng.
```

| Mức | Nghĩa | Chặn READY |
|---|---|---|
| Critical | Không làm được từ bản này, thiếu hoặc mâu thuẫn cơ bản | Có |
| Major | Làm được nhưng sẽ phải làm lại hoặc gây hiểu lầm | Có, khi quá hai Major |
| Minor | Nên sửa, không chặn | Không |

READY khi không có Critical và tối đa hai Major. Location trỏ đúng mục, đúng mã. Required action là việc cụ thể bằng ngôn ngữ tài liệu, không viết "vi phạm checklist".

## Tại gate
- Trình finding còn mở trong thông điệp hoàn thành.
- Approve: mọi finding mở ghi *Accepted risk* vào `decisions.md`.
- PO bác một finding: ghi `Rejected: <lý do nguyên văn>`.
- PO nói finding "đã sửa" thực ra chưa sửa: ghi `Reopened`, lần review sau xét lại.
- Không chép lịch sử review vào artifact. Artifact không có mục "trạng thái review".

## Shadow, tài liệu người khác viết
Giữ cách làm hiện có: tóm tắt tài liệu trước để PO xác nhận hiểu đúng; quét KB và Swagger xem tài liệu bỏ sót vùng nào; findings chia ba nhóm sai, thiếu, mơ hồ; phụ lục nguồn đã đọc; phụ lục câu AI tự trả lời được kèm nguồn. Mục đích là tìm chỗ sai so với hệ thống thật, không chấm cách viết.
