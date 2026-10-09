# Stage Protocol

Nghi thức chung cho mọi stage của luồng v2, áp cho intent nằm trong `.claude/intents/`. Mỗi stage command chỉ mô tả phần riêng của nó và trỏ về đây. Bám theo AWS AI-DLC Workflows v2.10, file `core/aidlc-common/protocols/stage-protocol.md`, rút gọn cho phạm vi PO/BA.

File đi kèm: `gate-protocol.md` (duyệt), `question-format.md` (hỏi và ghi câu trả lời), `review-protocol.md` (review độc lập), `profiles.md` (S, M, L). Thuật ngữ và họ mã: `GLOSSARY.md` ở gốc repo.

## Người dùng là PO

PO đang làm tài liệu của họ, không học quy trình. Nói về công việc: tên stage, artifact, câu hỏi, quyết định. Không nói về máy móc: "protocol", "metadata", "đã chạy checklist", "đang ghi state". Việc chỉ là ghi chép thì làm trong im lặng.

## Khối metadata ở đầu mỗi stage command

Ngay sau frontmatter của Claude Code (`description`, `argument-hint`), command có một bảng:

| Khoá | Nghĩa |
|---|---|
| Stage | Mã và tên: `2.3 Requirements Analysis` |
| Slug | kebab-case, trùng tên file command và tên thư mục artifact |
| Phase | `ideation` hoặc `inception` |
| Plugin | `upbase-po` với stage repo thêm (2.31, 2.32, 2.41, 2.42). Bỏ trống với stage gốc AWS |
| Execution | `always`, hoặc `conditional` kèm điều kiện |
| Lead | Agent dẫn stage, luôn là `product` trong phạm vi PO. Với 2.41 ghi thêm lead các team góp và ký |
| Produces | Artifact sinh ra, kèm questions file |
| Consumes | Artifact đọc vào, ghi rõ bắt buộc hay tuỳ |
| Requires | Stage phải xong trước |
| Profiles | S, M, L |
| Reviewer | `product-lead` hoặc `none` |
| Summary confirmation | `required`, `field-intake-only`, `off` |
| Template · Checklist · Knowledge | Đường dẫn file |

## Bảy bước

### 1. Load
- Đọc `state.md` của intent. Stage này phải là stage kế tiếp hoặc stage đang dở. Nếu không, dừng và hỏi PO.
- Đọc `decisions.md`, chỉ những dòng có cột *Read when* khớp stage hoặc chủ đề đang làm.
- Đọc `intent.md`, artifact trong Consumes, file KB mà command liệt kê, `.claude/memory/team.md`.
- Tra `decisions.md` và mọi questions file trước đó. Không hỏi lại câu đã có đáp án. Còn mơ hồ thì hỏi hẹp, nêu đáp án cũ.
- Đánh dấu stage `[-]` trong `state.md`. Stage đang `[-]` hoặc `[R]` từ phiên trước: đọc questions file, tiếp từ câu còn trống hoặc bước đang dở. Stage `[?]`: trình lại gate, không làm lại.

### 2. Ask
- Tạo `<slug>-questions.md` theo `question-format.md`, trong thư mục của stage.
- Lần đầu trong intent: hỏi PO chọn cách trả lời, Guide me, Edit file, hoặc Chat. Ghi vào `state.md`. Stage sau dùng lại và nói một dòng đang dùng cách nào.
- Ghi câu trả lời **nguyên văn** vào `[Answer]:` ngay sau mỗi lô. Diễn giải của AI đứng dòng dưới, nếu cần.
- Có đủ câu trả lời: quét từ mơ hồ, mâu thuẫn giữa các câu, dữ kiện còn thiếu. Có thì hỏi tiếp trong cùng file, đánh số tiếp.
- PO uỷ quyền ("tuỳ anh"): chọn theo `[đề xuất]`, ghi `[uỷ quyền]` kèm nguyên văn, nói một dòng đã chọn gì.
- Câu có cờ *Chặn* còn trống: dừng ở bước này.

### 3. Confirm
- Tóm tắt mọi câu trả lời thành gạch đầu dòng. Hỏi: **Looks correct** hoặc **Request changes**.
- Request changes: hỏi "sửa gì" nếu PO chưa nói, sửa file, hỏi lại.
- `off` thì bỏ bước này. `field-intake-only` chỉ áp cho 2.42.

### 4. Generate
- Viết artifact theo template, giữ đúng heading. Xoá mọi chữ hướng dẫn mẫu. Mục không có nội dung thì bỏ hẳn.
- Artifact nội bộ (intent-statement, scope-document, requirements, impact-matrix, solution-options, stories): thẻ nguồn ở mỗi khối khẳng định theo `question-format.md`. Mục **Assumptions & Open Questions** bắt buộc, không có thì ghi "None".
- Artifact bàn giao (initiative-brief, hld-brief, prd): không thẻ nguồn, không từ ngữ quy trình, mã kèm nội dung, dấu `·` giữa các mã đứng liền.
- Mã ổn định theo `GLOSSARY.md`. Mã đã cấp không đánh lại, kể cả khi xoá một mục ở giữa.
- Tên file ổn định. Phiên bản và trạng thái ghi ở frontmatter `version`, `status`. Không tạo file `v0.x`.
- Không sửa file trong `archive/`.

### 5. Verify
- Chạy checklist của stage. Mục blocking chưa đạt thì sửa trước, chưa trình gate.
- Reviewer `product-lead` và profile bật reviewer: gọi review theo `review-protocol.md`. Chờ file review. Không tự sửa theo finding, finding đi vào gate.

### 6. Learn
- Trong lúc làm, thêm dòng vào `memory.md` của intent: `- <ISO time> [<stage>] <một câu>; <hai câu ngữ cảnh>` dưới một trong bốn mục Interpretations, Deviations, Tradeoffs, Open questions.
- Trước gate, profile bật learnings: đưa các dòng mới của stage thành danh sách chọn, hỏi "Có gì cần nhớ cho lần sau không?" với hai lựa chọn Không có, Thêm ghi chú. Hỏi kể cả khi danh sách rỗng.
- Dòng được giữ: đối chiếu với `CLAUDE.md`. Mâu thuẫn thì hỏi PO sửa, bỏ, hay nâng lên luật tổ chức. Ghi vào `.claude/memory/team.md` dưới heading phù hợp, dạng `- <nội dung> (learned YYYY-MM-DD)`. Open questions không ghi, chúng là việc cần tra.
- Bài học áp dụng từ intent sau. Không đổi luật giữa chừng intent đang chạy.

### 7. Gate
Theo `gate-protocol.md`: đánh dấu `[?]`, thông điệp hoàn thành, câu hỏi duyệt, ghi quyết định nguyên văn, chụp bản duyệt vào `archive/`, đánh dấu `[x]`, dòng tiến độ, tên stage kế.

## Stage có điều kiện không áp dụng
Execution `conditional` và điều kiện không xảy ra: ghi `[S]` kèm lý do vào `state.md`, nói một dòng, sang stage kế. Không mở gate.

## Vượt profile giữa chừng
Phát hiện dấu hiệu vượt profile theo `profiles.md`: nói ngay, và tại gate gần nhất đưa lựa chọn **Add [stage]**. Không tự chạy tiếp đường cũ.

## Luôn đúng
- Tách `Fact`, `Assumption`, `Open Question`, `Recommendation`. Không bịa. Thiếu nhẹ ghi Assumption. Thiếu làm đổi phạm vi, rule, dữ liệu, luồng thì ghi Open Question và dừng.
- Ô không suy được: `❓BA`. Suy luận: `[suy ra]`.
- Không chốt thay PO. Không thiết kế kỹ thuật chi tiết. Không hỏi kỹ thuật cho Dev. Chỉ hỏi câu mà đáp án làm đổi phạm vi hoặc business rule.
- KB là bản chụp. Chạm vùng nào thì đọc lại nguồn vùng đó. Quá một tháng kể từ *Last verified* thì đọc lại trước. Vùng KB chưa phủ: `❓BA`, không kết luận.
- Có endpoint không có nghĩa là có tính năng. Hidden vẫn phải xét.
- Một stage một lượt. Mỗi stage kết thúc ở gate.
