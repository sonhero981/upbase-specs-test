---
description: Stage 2.4 User Stories của luồng v2 theo AWS AI-DLC. Danh sách US gắn Proto-Unit, phủ FR; mỗi US một thẻ chín mục đủ cho lead viết HLD. Gọi qua /po
argument-hint: <intent-slug>
---
# 2.4 User Stories

| | |
|---|---|
| Stage | 2.4 User Stories |
| Slug | user-stories |
| Phase | inception |
| Plugin | (stage gốc AWS) |
| Execution | always ở M và L. S gộp vào 2.42 |
| Lead | product |
| Produces | `inception/user-stories/stories.md` · `user-stories-questions.md` |
| Consumes | `requirements.md` (bắt buộc) · `scope-document.md` (Proto-Unit) · `impact-matrix.md` · `solution-options.md` (tuỳ) · `decisions.md` |
| Requires | requirements-analysis, impact-analysis |
| Profiles | M, L |
| Reviewer | product-lead |
| Summary confirmation | required |
| Template | `.claude/templates/stories.md` |
| Checklist | `.claude/verification/user-stories.md` |
| Knowledge | `.claude/knowledge/product/user-story-patterns.md` §INVEST, §Story Splitting Patterns, §Anti-Patterns, §Definition of Ready Checklist · `product-guide.md` §Story Decomposition Patterns |

Chạy theo `.claude/protocol/stage-protocol.md`.

## Mục đích
Danh sách user story đầy đủ, mỗi US gắn vào một Proto-Unit, mỗi FR có US phủ, và mỗi US có một thẻ đủ để lead Design, Tech, QA hiểu và viết HLD ở 2.41. Thẻ là đầu vào của HLD, nên phải tả đủ luồng, rule và vùng chạm; acceptance criteria thì chưa, vì phần đó viết ở PRD sau khi có HLD. AWS: stage 2.4 chạy mob với Design, Developer, Quality agent; PO-Workflow để lead các team góp ý ở 2.41.

## Load
requirements (FR, OQ); scope-document (Proto-Unit); impact-matrix (coverage gap sinh US); solution-options (option đã chọn); decisions.

## Ask
1. Cách chia: theo luồng công việc, theo vai, hay theo khả năng. Đề xuất sẵn một cách.
2. Độ mịn: một US là một mục tiêu hoàn chỉnh của người dùng. Không chia theo màn hình, không chia theo rule.
3. US nào làm đợt này, US nào định nghĩa nhưng chưa làm.
4. Vai nào xuất hiện. Có cần vai mới không.
5. Proto-Unit từ 1.4 còn đúng không. Cần tách, gộp không, vì sao.
6. Nhánh đáng kể nào phải có trong thẻ US, tức ngoại lệ làm đổi luồng. AI đề xuất từ requirements và Impact Matrix, PO thêm bớt.

## Generate
`stories.md` theo template: bảng `US1`... với tên một câu tự nhiên theo vai, không ép khuôn As a, I want; vai; Proto-Unit; MoSCoW; FR nguồn; đợt này hay chưa làm. Mỗi US một thẻ chín mục theo template: vai và mục tiêu, bối cảnh, luồng chính ba đến bảy bước ở mức hành vi, nhánh đáng kể, rule đã biết kèm mã, dữ liệu và vùng chạm từ Impact Matrix, ngoài phạm vi của US, phụ thuộc, chưa rõ. Thẻ phải đủ để lead đọc rồi viết mục 8, 9, 10 của HLD Brief mà không cần mở requirements; mục không có ghi "không có". Không acceptance criteria, không validate theo field, không kiểu dữ liệu, phần đó ở PRD. Bảng FR sang US với trạng thái OK, GAP, Deferred, N/A, GAP phải xử lý trước gate. Bảng Proto-Unit: gồm US, phụ thuộc, release độc lập được không, thứ tự gợi ý, thay đổi so với 1.4 kèm lý do. Thẻ nguồn. Assumptions & Open Questions.
INVEST nhẹ: Valuable, Small, Testable. Story có chữ "và" nối hai việc thì tách.

## Verify
Checklist. Chạy `python3 .claude/scripts/po-tools.py trace .claude/intents/<slug>` (chưa có PRD nên script chỉ kiểm FR sang US và US mồ côi); GAP hoặc ORPHAN thì sửa trước. Reviewer product-lead.

## Gate
Trình: danh sách US theo Proto-Unit, số US đợt này và chưa làm, FR chưa có US, Proto-Unit đổi so với 1.4, US có nhánh đáng kể hoặc mục chưa rõ, finding review. Approve là xác nhận cả danh sách lẫn nội dung thẻ, vì lead sẽ thiết kế từ thẻ này. Stage kế: 2.41.
