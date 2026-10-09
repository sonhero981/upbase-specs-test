---
description: Stage 2.41 HLD Brief & Alignment, plugin upbase-po của luồng v2. Tài liệu ba trang để họp liên team; lead Design, Dev, QA ghi định hướng trực tiếp trong repo; sign-off rồi mới viết PRD; Lark là bản cuối. Gọi qua /po
argument-hint: <intent-slug>
---
# 2.41 HLD Brief & Alignment

| | |
|---|---|
| Stage | 2.41 HLD Brief & Alignment |
| Slug | hld-brief |
| Phase | inception |
| Plugin | `upbase-po` |
| Execution | always ở M và L |
| Lead | product. Design lead, Tech lead, QA lead là người góp và ký |
| Produces | `inception/hld-brief/hld-brief.md` · `hld-brief-questions.md` |
| Consumes | `stories.md`, `requirements.md`, `impact-matrix.md` (bắt buộc) · `solution-options.md`, `intent-statement.md`, `scope-document.md`, `competitive-analysis.md` (tuỳ) · `decisions.md` |
| Requires | user-stories |
| Profiles | M, L |
| Reviewer | none, lead các team là người review |
| Summary confirmation | required |
| Template | `.claude/templates/hld-brief.md` |
| Checklist | `.claude/verification/hld-brief.md` |

Chạy theo `.claude/protocol/stage-protocol.md`.

## Mục đích
Một tài liệu tối đa ba trang để họp với lead Design, Dev, QA; để họ ghi định hướng của mình; và để chốt tầng cao trước khi viết PRD chi tiết. Gate của stage là Alignment gate, cần sign-off ba lead. Nguồn sự thật là file trong repo cho tới khi ký; Lark chỉ nhận bản cuối. Plugin stage; AWS có Initiative Brief ở Ideation và mob agent ở 2.4, không có bản đồng thuận nhiều vai.

## Load
Mọi artifact trên. `decisions.md`: Accepted risks và conflict đã quyết. OQ còn mở ở mọi stage là ứng viên cho mục 7.

## Ask
1. Lead Design, Dev, QA là ai. Điền `intent.md` nếu trống.
2. Họp ngày nào, hay lead ghi vào repo tới hạn nào.
3. Quyết định nào cần chốt trong họp: AI đề xuất từ OQ mở và conflict chưa quyết, PO chọn và thêm.
4. Điều PO muốn nhấn mạnh, hoặc chưa muốn đưa vào.

## Generate
`hld-brief.md` theo template, mười hai mục. AI viết mục 1 đến 7 và 11 từ artifact đã duyệt, không viết nội dung mới. Mục 6 có thêm bảng rủi ro đã chấp nhận, giả định lớn chưa kiểm chứng và finding review còn treo, lấy từ Accepted risks trong `decisions.md`, mục Assumptions & Open Questions của các artifact và file review mới nhất; tối đa bảy dòng, mỗi dòng ghi điều kiện kèm theo, vì rủi ro đã chấp nhận là điều kiện đi kèm quyết định chứ không phải việc để sau. Mục 8, 9, 10 để trống cho lead, nhưng đầu mỗi mục AI ghi tối đa năm dòng in nghiêng "Điểm cần lưu ý cho <vai>" lấy từ Impact Matrix, constraints, corner checklist và coverage gap; đó là gợi ý để lead trả lời, không phải nội dung thay lead. Mục 12 điền tên và trạng thái "Chưa xem". Giới hạn 1.500 từ, kiểm bằng đếm từ. Văn phong bàn giao: không thẻ nguồn, không từ quy trình, mã kèm nội dung, không viết tắt. Mục 4 có thể một sơ đồ Mermaid kèm một dòng chú thích.

## Giao cho lead, sau Verify và trước gate
1. Chụp bản nháp để sau này so diff: `python3 .claude/scripts/po-tools.py archive .claude/intents/<slug> hld-brief inception/hld-brief/hld-brief.md --label draft`.
2. Đánh dấu stage `[-]`, ghi vào `state.md` mục Current: "Chờ lead ghi mục 8, 9, 10 và ký mục 12, hạn <ngày>".
3. Báo PO gửi lead đường dẫn file và quy ước dưới đây. AI không viết mục 8, 9, 10 trong bất kỳ trường hợp nào.

Quy ước cho lead làm trên repo:
- Pull trước khi sửa. Chỉ sửa mục của mình: Design mục 8, Tech mục 9, QA mục 10, và dòng của mình ở mục 12 với một trong bốn trạng thái Chưa xem, Có ý kiến, Đồng ý, Yêu cầu sửa. Không sửa mục khác; có ý kiến về mục khác thì ghi ở cuối mục của mình dưới tiêu đề "Ý kiến với mục N". Yêu cầu sửa thì ghi rõ sửa gì.
- Commit ngay sau khi ghi, message `hld(<slug>): <design|tech|qa> direction`. Sửa trên GitHub web cũng được, không cần mở Claude Code.
- Lead không mở được repo: gửi nội dung cho PO. PO dán nguyên văn, mở đầu bằng "(ghi theo <tên>, <ngày>)". Sign-off của lead đó ghi theo tin nhắn xác nhận, lưu nguyên văn vào `decisions.md`.

## Khi lead ghi xong, hoặc sau họp
PO gọi `/po <slug>`. Stage đang `[-]` nên tiếp tục ở đây:
1. So file hiện tại với bản chụp ở `archive/`, trình diff theo mục.
2. Mục 8, 9, 10 giữ nguyên văn của lead. Lead sửa mục 1 đến 7 hoặc 11 thì nêu riêng, PO quyết nhận hay trả lại; nhận thì ghi DEC kèm tên lead.
3. Định hướng của lead mâu thuẫn với artifact đã duyệt, ví dụ Tech lead cắt một US, QA thêm điều kiện làm đổi rule: đi qua `/change-request`, không sửa tay.
4. Mỗi quyết định trong họp hoặc trong mục 7 đã có đáp án: một DEC, người quyết là lead tương ứng, nguyên văn nếu có.
5. Mục 7 còn dòng chưa quyết: giữ, đưa vào thông điệp gate.

## Gate, Alignment
Trình: mục 1 nguyên văn, trạng thái sign-off từng lead, quyết định đã chốt, diff đã nhận, mục 7 còn mở. **Approve** chỉ khi Design, Dev, QA đều ghi "Đồng ý" hoặc "Có ý kiến" ở mục 12. Một lead ghi "Yêu cầu sửa" thì gate là **Request Changes**, không có Accept as-is cho trường hợp này. Thiếu chữ ký thì PO chọn **Accept as-is** kèm lý do, hoặc chờ. **Request Changes**: AI sửa mục của PO, không đụng mục của lead; mục của lead mất tiền đề thì báo lead ký lại.
Sau Approve: hld-brief lên version 1.0, `status: approved`, chụp archive, rồi publish Lark bằng `/publish-lark hld-brief` với tên `[HLD] <tên tính năng>`. Đây là bản cuối để mọi người đọc; link ghi vào frontmatter `lark`, `intent.md` và `state.md`. Đổi brief sau đó đi qua CR, lấy lại sign-off, publish lại cả file.

Stage kế: 2.42.
