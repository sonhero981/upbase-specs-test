---
description: Stage 2.3 Requirements Analysis của luồng v2 theo AWS AI-DLC. Yêu cầu FR, NFR có mã ổn định. Gọi qua /po
argument-hint: <intent-slug>
---
# 2.3 Requirements Analysis

| | |
|---|---|
| Stage | 2.3 Requirements Analysis |
| Slug | requirements-analysis |
| Phase | inception |
| Plugin | (stage gốc AWS) |
| Execution | always. Ở S đây là stage đầu tiên |
| Lead | product |
| Produces | `inception/requirements-analysis/requirements.md` · `requirements-analysis-questions.md` |
| Consumes | `scope-document.md`, `intent-statement.md` (M, L bắt buộc) · `inputs/*` (S) · KB |
| Requires | scope-definition ở M, L |
| Profiles | S, M, L |
| Reviewer | product-lead ở M, L |
| Summary confirmation | required. S: off |
| Template | `.claude/templates/requirements.md` |
| Checklist | `.claude/verification/requirements-analysis.md` |
| Knowledge | `.claude/knowledge/domain/domain.md` mục 3 và mục 4 phần 2.3: KB theo module bị chạm, sự kiện và mail, API surface, data model khi chạm dữ liệu · product: `requirements-guide.md`, `requirements-elicitation.md` §Validation Checklist, `corner-checklist.md` |

Chạy theo `.claude/protocol/stage-protocol.md`.

## Mục đích
Biến phạm vi thành yêu cầu có mã ổn định: FR, NFR, ràng buộc, giả định, câu hỏi mở. AWS: stage 2.3.

## Load
- S: đọc `inputs/` trực tiếp, viết intent summary gọn trong requirements.
- Tra KB cho từng hạng mục của scope theo bản đồ KB trong `domain.md`: **đã có chưa** (file theo module); **rule hiện có chi phối** (`BR-*`, `KB-*`); **Hidden** (index mục Trạng thái); **sự kiện, mail liên quan**, đang bật hay tắt; **vùng KB chưa phủ** thì ghi `❓PO`, không kết luận.
- Phát hiện yêu cầu trùng tính năng đã có: nêu ngay, kèm mã KB, không để tới Impact Analysis. Ví dụ của domain đang cài ở `domain.md` mục 4 phần 2.3.
- Chạm dữ liệu: đọc lại nguồn sống nếu quá một tháng kể từ ngày đối chiếu của file data model.

## Ask
Chỉ hỏi lỗ hổng còn lại sau khi đã tra KB. Quét sáu chiều của AWS để tìm lỗ hổng: hành vi chức năng; phi chức năng đo được; kịch bản người dùng và góc; bối cảnh nghiệp vụ; tích hợp và dữ liệu; chất lượng.
Góc hay sót: quét từng thành phần theo `.claude/knowledge/domain/corner-checklist.md`, phần Điều kiện theo bề mặt. Mỗi góc áp dụng thành FR, assumption có lý do, hoặc out of scope; không thành câu hỏi nếu một mặc định hợp lý giải quyết được.
Gợi ý câu hỏi: hành vi nào phải giữ nguyên; dữ liệu bắt buộc và dữ liệu phải lưu lại; vai nào làm gì; hằng số nào cứng, nào cấu hình; ngoại lệ xử lý ra sao; yêu cầu trùng thứ đã có thì mở rộng hay làm mới.
Không hỏi kỹ thuật cho Dev. Depth Minimal ở S: chỉ câu chặn.

## Generate
`requirements.md` theo template:
1. Intent summary.
2. Functional requirements, nhóm theo khả năng. `FR1`, `FR1.1`. Mỗi FR: câu khẳng định kiểm chứng được, ưu tiên MoSCoW, cờ Existing, New hay Changed kèm mã KB, thẻ nguồn.
3. Non-functional requirements, chỉ khi đo được.
4. Constraints: nghiệp vụ, tenant và hằng số, tích hợp, dữ liệu cũ.
5. Assumptions & Open Questions: `OQ1`... có cờ Chặn và owner.
6. Out of scope.
7. Sources read kèm Last verified, và mục "chưa tra được".
FR viết **điều phải đúng**, không viết cách làm. Không có FR mô tả bảng, endpoint, hay thuật toán.

## Verify
Checklist của stage. Quét góc nội bộ: mỗi góc áp dụng phải thành FR, assumption có lý do, hoặc out of scope. Reviewer product-lead ở M, L.

## Gate
Trình: số FR theo nhóm, NFR, OQ còn chặn, FR trùng thứ đã có, vùng `❓PO`, finding review. Stage kế: 2.31 ở M, L; 2.42 ở S.
