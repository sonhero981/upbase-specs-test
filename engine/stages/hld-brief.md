# 2.41 HLD Brief & Alignment

| | |
|---|---|
| Stage | 2.41 HLD Brief & Alignment |
| Slug | hld-brief |
| Thư mục | `inception/hld-brief` |
| Phase | inception |
| Plugin | `po-workflow` |
| Lệch so với AWS | Stage thêm của PO-Workflow, không có trong AWS. Đánh số thập phân để chen giữa stage gốc; cơ chế plugin của AWS chỉ cho đánh số sau stage cuối của phase |
| Execution | always ở M và L |
| Lead | product. Design PIC, Tech PIC, QA PIC là người góp và ký |
| Produces | `inception/hld-brief/hld-brief.md` · `hld-brief-questions.md` |
| Consumes | `stories.md`, `requirements.md`, `impact-matrix.md` (bắt buộc) · `solution-options.md`, `intent-statement.md`, `scope-document.md`, `competitive-analysis.md` (tuỳ) · `decisions.md` |
| Requires | user-stories |
| Profiles | M, L |
| Reviewer | none, các PIC là người review |
| Summary confirmation | required |
| Template | `engine/templates/hld-brief.md` |
| Checklist | `engine/verification/hld-brief.md` |

Chạy theo `engine/protocol/stage-protocol.md`.

## Mục đích
Một tài liệu tối đa ba trang cho buổi checkpoint, tức buổi họp với Design PIC, Tech PIC, QA PIC; để họ ghi định hướng của mình; và để chốt tầng cao trước khi viết PRD chi tiết. Gate của stage là Alignment gate, cần sign-off ba PIC. Nguồn sự thật là file trong repo cho tới khi ký; Lark chỉ nhận bản cuối. Plugin stage; AWS có Initiative Brief ở Ideation và mob agent ở 2.4, không có bản đồng thuận nhiều vai.

## Load
Mọi artifact trên. `stories.md`: thẻ từng US, nguồn cho cột Ý chính ở mục 5; PIC đọc thẻ trước khi ghi mục của mình. `decisions.md`: Accepted risks và conflict đã quyết. OQ còn mở ở mọi stage là ứng viên cho mục 7.

## Ask
1. Design PIC, Tech PIC, QA PIC là ai. Điền `intent.md` nếu trống.
2. Họp ngày nào, hay PIC ghi vào repo tới hạn nào.
3. Quyết định nào cần chốt trong họp: AI đề xuất từ OQ mở và conflict chưa quyết, PO chọn và thêm.
4. Điều PO muốn nhấn mạnh, hoặc chưa muốn đưa vào.

## Generate
`hld-brief.md` theo template, mười hai mục. AI viết mục 1 đến 7 và 11 từ artifact đã duyệt, không viết nội dung mới. Mục 6 có thêm bảng rủi ro đã chấp nhận, giả định lớn chưa kiểm chứng và finding review còn treo, lấy từ Accepted risks trong `decisions.md`, mục Assumptions & Open Questions của các artifact và file review mới nhất; tối đa bảy dòng, mỗi dòng ghi điều kiện kèm theo, vì rủi ro đã chấp nhận là điều kiện đi kèm quyết định. Mục 5 có cột Ý chính một dòng mỗi US, rút từ thẻ US trong `stories.md`. Mục 8, 9, 10 giữ nguyên khung của template cho PIC điền, AI không điền khung; đầu mỗi mục AI ghi tối đa năm dòng in nghiêng "Điểm cần lưu ý cho <vai>" lấy từ Impact Matrix, constraints, corner checklist và coverage gap; đó chỉ là gợi ý để PIC trả lời; nội dung mục 8, 9, 10 do PIC viết. Mục 12 điền tên và trạng thái "Chưa xem". Giới hạn 1.500 từ, kiểm bằng đếm từ. Văn phong bàn giao: không thẻ nguồn, không từ quy trình, mã kèm nội dung, không viết tắt. Mục 4 có thể một sơ đồ Mermaid kèm một dòng chú thích.

## Giao cho PIC, sau Verify và trước gate
1. Chụp bản nháp để sau này so diff: `python3 engine/scripts/po-tools.py archive intents/<slug> hld-brief inception/hld-brief/hld-brief.md --label draft`.
2. Đánh dấu stage `[-]`, ghi vào `state.md` mục Current: "Chờ PIC ghi mục 8, 9, 10 và ký mục 12, hạn <ngày>".
3. Báo PO gửi PIC đường dẫn file và quy ước dưới đây. AI không viết mục 8, 9, 10 trong bất kỳ trường hợp nào.

Quy ước cho PIC làm trên repo:
- Pull trước khi sửa. Chỉ sửa mục của mình: Design mục 8, Tech mục 9, QA mục 10, và dòng của mình ở mục 12 với một trong bốn trạng thái Chưa xem, Có ý kiến, Đồng ý, Yêu cầu sửa. Không sửa mục khác; có ý kiến hoặc câu hỏi về mục khác thì ghi một dòng vào mục 7, gắn người phải trả lời và có chặn hay không. Yêu cầu sửa thì ghi rõ sửa gì.
- Commit ngay sau khi ghi, message `hld(<slug>): <design|tech|qa> direction`. Sửa trên GitHub web cũng được, không cần mở Claude Code.
- PIC không mở được repo: gửi nội dung cho PO. PO dán nguyên văn, mở đầu bằng "(ghi theo <tên>, <ngày>)". Sign-off của PIC đó ghi theo tin nhắn xác nhận, lưu nguyên văn vào `decisions.md`.

## Khi PIC ghi xong, hoặc sau họp
PO gọi `/po <slug>`. Stage đang `[-]` nên tiếp tục tại bước này:
1. So file hiện tại với bản chụp ở `archive/`, trình diff theo mục.
2. Mục 8, 9, 10 giữ nguyên văn của PIC. Khung còn ý bỏ trống, nhất là mục 9, thì báo PO hỏi PIC; AI không tự điền, vì 2.42 viết chi tiết bám theo các ý này. PIC sửa mục 1 đến 7 hoặc 11 thì nêu riêng, PO quyết nhận hoặc trả lại; nhận thì ghi DEC kèm tên PIC.
3. Định hướng của PIC mâu thuẫn với artifact đã duyệt, ví dụ Tech PIC cắt một US, QA thêm điều kiện làm đổi rule: đi qua `/change-request`, không sửa tay.
4. Mỗi quyết định trong họp hoặc trong mục 7 đã có đáp án: một DEC, người quyết là PIC tương ứng, nguyên văn nếu có.
5. Mục 7 còn dòng chưa quyết: giữ, đưa vào thông điệp gate.

## Gate, Alignment
Trình: mục 1 nguyên văn, trạng thái sign-off từng PIC, quyết định đã chốt, diff đã nhận, mục 7 còn mở, và độ lớn Tech PIC ghi ở mục 9 so với mốc cứng của scope-document; vượt mốc thì nêu rõ để PO quyết cắt phạm vi hay dời mốc. Approve chỉ khi Design PIC, Tech PIC, QA PIC đều ghi "Đồng ý" hoặc "Có ý kiến" ở mục 12. Một PIC ghi "Yêu cầu sửa" thì gate là Request Changes, không có Accept as-is cho trường hợp này. Thiếu chữ ký thì PO chọn Accept as-is kèm lý do, hoặc chờ. Request Changes: AI sửa mục của PO, không đụng mục của PIC; mục của PIC mất tiền đề thì báo PIC ký lại.
Sau Approve: hld-brief lên version 1.0, `status: approved`, chụp archive, sau đó publish Lark bằng `/publish-lark hld-brief` với tên `[HLD] <tên tính năng>`. Đây là bản cuối để mọi người đọc; link ghi vào frontmatter `lark`, `intent.md` và `state.md`. Đổi brief sau đó đi qua CR, lấy lại sign-off, publish lại cả file.

Stage kế: 2.42.
