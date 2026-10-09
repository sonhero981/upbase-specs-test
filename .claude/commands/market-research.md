---
description: Stage 1.2 Market Research của luồng v2. Có điều kiện, chạy khi PO muốn so với sản phẩm khác. Gọi qua /po
argument-hint: <intent-slug>
---
# 1.2 Market Research

| | |
|---|---|
| Stage | 1.2 Market Research |
| Slug | market-research |
| Phase | ideation |
| Plugin | (stage gốc AWS) |
| Execution | conditional: PO yêu cầu so với sản phẩm khác, hoặc 1.1 cho thấy cách làm chuẩn trên thị trường ảnh hưởng tới phạm vi |
| Lead | product |
| Produces | `ideation/market-research/competitive-analysis.md` · `market-research-questions.md` |
| Consumes | `intent-statement.md` (bắt buộc) |
| Requires | intent-capture |
| Profiles | L |
| Reviewer | none |
| Summary confirmation | required |
| Template | `.claude/templates/competitive-analysis.md` |
| Checklist | `.claude/verification/market-research.md` |
| Knowledge | `.claude/knowledge/product/market-research-methods.md` §Competitive Analysis Framework, §Build vs Buy Assessment |

Chạy theo `.claude/protocol/stage-protocol.md`.

## Mục đích
Xem sản phẩm khác giải bài toán này thế nào, để đặt tên khái niệm đúng, không phát minh lại, và biết đâu là chuẩn người dùng đã quen. AWS: stage 1.2. Thay cho "nghiên cứu LMS khác" từng làm tự phát ở dự án Group.

## Ask
1. So với sản phẩm nào, tối đa ba. Mặc định với LMS: TalentLMS, Docebo, Moodle.
2. Xem khía cạnh nào: mô hình khái niệm, thuật ngữ, luồng chính, giới hạn, cách tích hợp.
3. Quyết định nào phụ thuộc vào kết quả này. Không có thì ghi `[S]` và không chạy.

## Generate
`competitive-analysis.md`: mỗi sản phẩm một mục ngắn; bảng so sánh theo khía cạnh đã chọn; thuật ngữ nên dùng; điều đáng mượn và vì sao hợp UpLnD; điều không mượn và vì sao; đối chiếu với yêu cầu hiện tại, chỗ nào làm đổi phạm vi hay rule; nguồn kèm link và ngày đọc. Trích đúng, không suy diễn tính năng từ tên menu.
Thu thập: `help.talentlms.com` chặn tải tự động, lấy bài qua API Zendesk `/api/v2/help_center/en-us/articles/<id>.json`. Bài đã lấy lưu nguyên văn vào `inputs/` để tra lại.

## Gate
Trình bảng so sánh và danh sách điều đáng mượn. Stage kế: 1.4.
