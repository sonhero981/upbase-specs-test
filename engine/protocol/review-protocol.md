# Review Protocol

Review độc lập do `ai-reviewer` làm. Bám theo AWS AI-DLC `stage-protocol-reviewer.md` và `knowledge/aidlc-product-lead-agent/reviewing.md`. Ở các stage văn bản của PO, review là tham vấn: finding đi vào gate, PO quyết, không có vòng tự sửa.

## Khi nào chạy
- Stage có Reviewer `ai-reviewer` và profile bật reviewer: sau kiểm bằng máy và checklist ở bước Verify, trước Gate.
- Sau Request Changes mà artifact đổi: một lượt nữa.
- PO yêu cầu ("review lại cái này"): chạy, không giới hạn số lần.
- `/po-review <file>`: review một tài liệu bất kỳ. `/po-review --shadow <file>`: tài liệu người khác viết, xem mục Shadow.

## Gọi reviewer
- Reviewer không được thấy cuộc hội thoại. Đó là chủ đích, để phán đoán độc lập với người viết. Cách gọi theo công cụ:
  - Claude Code: subagent `ai-reviewer` trong `.claude/agents/`. Môi trường không liệt kê subagent này thì gọi một agent mới, dặn dòng đầu tiên: đọc `engine/agents/ai-reviewer.md` và làm đúng theo đó.
  - Công cụ không có subagent: mở một phiên mới, không mang hội thoại, đưa `engine/agents/ai-reviewer.md` và danh sách đường dẫn.
- Trước khi gọi, AI điều phối chạy kiểm bằng máy và lưu kết quả vào `verification/<slug>-machine.md`: `po-tools.py check` của stage, cộng `po-tools.py trace` với stage 2.4 và 2.42. Reviewer dùng kết quả này thay cho việc tự đếm.
- Truyền đường dẫn, không dán nội dung: file stage trong `engine/stages/`, questions file, artifact cần review, artifact đầu vào, `GLOSSARY.md`, file KB liên quan, `verification/<slug>-machine.md`, và sổ finding `reviews/findings-<slug>.md` từ lần thứ hai.
- Không truyền: `memory.md`, file review cũ, bản nháp, lý luận của AI soạn thảo.
- Nói với PO một câu: "Để AI Reviewer xem qua trước khi anh/chị đọc."

## Reviewer làm gì
- Đọc file stage để biết stage phải sinh gì. Đọc questions file để biết bối cảnh. Đọc artifact để đánh giá.
- Chỉ ghi một file: `reviews/review-<slug>-<NN>.md`. Không sửa artifact. Không trả lời câu hỏi của stage.
- Lần sau: đọc sổ finding, ghi mỗi finding Open hoặc Reopened là *Fixed* hay *Still applies*. Finding đã có quyết định của PO thì chỉ đọc. Finding mới không có ID.

## Sổ finding
AI điều phối giữ một sổ cho mỗi stage, `reviews/findings-<slug>.md`, theo cách AWS giữ danh sách finding của từng stage. Reviewer không ghi sổ.

```markdown
# Sổ finding: <slug>
| ID | Lần | Mức | Vị trí | Finding | Trạng thái | Quyết định của PO |
|---|---|---|---|---|---|---|
| R-01 | 01 | Major | requirements.md > FR4 | Chưa nói dữ liệu trước 01/09 xử lý sao | Open | |
```

- Sau mỗi review: cấp ID tiếp theo cho finding mới, `R-NN`; cập nhật trạng thái finding cũ theo review: Fixed, Open.
- Tại gate: PO chấp nhận rủi ro thì *Accepted risk* kèm lý do; PO bác thì *Rejected* kèm lý do nguyên văn; PO nói đã sửa mà chưa sửa thì *Reopened*.
- Finding Accepted risk hoặc Rejected là quyết định đã chốt. Review sau không được chấm lại hay diễn đạt lại. Thông điệp hoàn thành chỉ trình finding Open và Reopened.

## Review không hoàn tất
Reviewer dừng mà không có file review, hoặc file không có dòng Verdict: gọi lại đúng một lần với cùng đầu vào. Lần hai vẫn hỏng thì ghi `reviews/review-<slug>-<NN>.md` với Verdict NOT-READY và một dòng "Review chưa hoàn tất", rồi đưa ra gate để PO quyết chạy lại hay chấp nhận rủi ro.

## Tiêu chí của AI Reviewer
1. Dev đọc có biết phải làm gì không. Không thì NOT-READY.
2. QA có viết được test từ acceptance criteria không. Không thì NOT-READY.
3. Có gì ngầm hiểu mà chưa viết. Giả định là lỗ hổng.
4. Mọi mục có giá trị với người dùng hay nghiệp vụ không. Thừa là lấn phạm vi.
5. Biên có rõ không: In, Out, để sau.
6. Góc đã chốt chưa, theo `corner-checklist.md` của domain. Mỗi góc phải là rule, giả định có lý do, hoặc ngoài phạm vi.
7. Mọi FR truy được về nhu cầu, mọi US truy được về FR. Mồ côi là finding.
8. Thẻ nguồn còn đủ, assumption chưa bị nâng thành fact.
9. Vùng KB chưa phủ có `❓PO`, không kết luận bừa.

## File review
```markdown
# Review: <artifact> · <stage> · lần <NN>
**Verdict:** READY | NOT-READY
**Reviewer:** ai-reviewer · **Date:** <ISO>

## Prior findings
| ID | Now | Note |
|---|---|---|

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
- Trình finding Open và Reopened trong thông điệp hoàn thành.
- Approve: mọi finding mở ghi *Accepted risk* vào `decisions.md` và vào sổ finding.
- PO bác một finding: ghi `Rejected: <lý do nguyên văn>` vào sổ.
- PO nói finding "đã sửa" thực ra chưa sửa: ghi `Reopened`, lần review sau xét lại.
- Không chép lịch sử review vào artifact. Artifact không có mục "trạng thái review".

## Shadow, tài liệu người khác viết
Giữ cách làm hiện có: tóm tắt tài liệu trước để PO xác nhận hiểu đúng; quét KB và API spec xem tài liệu bỏ sót vùng nào; findings chia ba nhóm sai, thiếu, mơ hồ; phụ lục nguồn đã đọc; phụ lục câu AI tự trả lời được kèm nguồn. Mục đích là tìm chỗ sai so với hệ thống thật, không chấm cách viết.
