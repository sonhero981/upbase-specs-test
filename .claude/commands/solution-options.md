---
description: Stage 2.32 Solution Options, plugin upbase-po của luồng v2. Có điều kiện. So sánh hướng giải, khuyến nghị có điều kiện. Gọi qua /po
argument-hint: <intent-slug>
---
# 2.32 Solution Options

| | |
|---|---|
| Stage | 2.32 Solution Options |
| Slug | solution-options |
| Phase | inception |
| Plugin | `upbase-po` |
| Execution | conditional: có từ hai hướng giải, hoặc PO chưa có hướng |
| Lead | product |
| Produces | `inception/solution-options/solution-options.md` · `solution-options-questions.md` |
| Consumes | `requirements.md`, `impact-matrix.md` (bắt buộc) · KB |
| Requires | impact-analysis |
| Profiles | L. M khi 2.31 phát hiện nhiều hướng, qua lựa chọn Add stage |
| Reviewer | none |
| Summary confirmation | required |
| Template | `.claude/templates/solution-options.md` |
| Checklist | `.claude/verification/solution-options.md` |

Chạy theo `.claude/protocol/stage-protocol.md`.

## Mục đích
So sánh các hướng giải trước khi chốt, trên nền Impact Matrix đã duyệt. Recommendation có điều kiện, PO quyết tại gate. Plugin stage; AWS chỉ có ADR ở tầng kiến trúc.

## Ask
1. PO đã có định hướng chưa. Có thì mô tả ngắn: AI nhận xét alignment với objective, điểm mạnh, gap theo Impact Matrix, gợi ý thêm một hai option. Định hướng của PO vẫn vào bảng như mọi option, quyết định dựa trên đánh đổi, không dựa trên thứ tự đề xuất.
2. Ràng buộc nào loại ngay một option: thời gian, đội, dữ liệu cũ, tenant.
3. Điều PO lo nhất.
Ép option từ góc khác nhau để tránh "hai option là một": đổi quy trình không cần code; cấu hình; mở rộng cái có sẵn; làm mới; cắt phạm vi.

## Generate
`solution-options.md` theo template: tình huống; bảng option kèm nguồn gốc (PO, AI, cách hệ đang làm); so sánh cùng bộ bảy tiêu chí: business fit, tác động người dùng và quy trình, tác động hệ thống và dữ liệu lấy từ Impact Matrix, effort tương đối, risk, dependency, nợ đóng cứng tenant; pros và cons; Recommendation gồm option, điều kiện, risk phải chấp nhận, cái gì sẽ đổi kết luận. Effort và risk ghi Cao, Trung bình, Thấp kèm lý do, không bịa số giờ.

## Gate
Trình: nhận xét định hướng của PO nếu có; bảng so sánh; recommendation. Approve nghĩa là chọn option: ghi DEC với option, lý do, trade-off chấp nhận. Stage kế: 2.4.
