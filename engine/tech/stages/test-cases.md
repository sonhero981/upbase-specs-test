---
description: Stage 2.81 Test Cases (plugin tech-workflow, lead QA). QA viết test case trỏ về US/AC/BR từ PRD, Unit và contract; lộ chỗ PRD thiếu thì gửi PO. Gọi qua /tech
argument-hint: <intent-slug>
---
# 2.81 Test Cases

| | |
|---|---|
| Stage | 2.81 Test Cases (plugin; AWS để QA ở 3.6 Build and Test, khung này cần TC trước khi chia Bolt) |
| Plugin | `tech-workflow` |
| Lead | QA. Gate: QA lead |
| Produces | `inception/test-cases/test-cases.md` · `inception/test-cases/test-cases-questions.md` |
| Consumes | PRD (AC, BR, Conner case), `inception/units-generation/unit-of-work-story-map.md`, `inception/contract-design/contract-summary.md` (mã lỗi, shape), HLD Brief mục 10 Test Strategy, `domain/corner-checklist.md`, `engine/tech/aidlc/knowledge/aidlc-quality-agent/` |
| Requires | 2.8 `[x]` (contract Agreed). Chạy song song 2.9 |
| Template | `engine/tech/templates/test-cases.md` |

Chạy theo `engine/tech/protocol/tech-protocol.md`, người dùng là QA.

## Generate
- Mỗi dòng AC và mỗi BR có ít nhất một TC. Mỗi US có ít nhất một Happy và một Negative/Edge.
- Góc trong corner checklist (rỗng, trùng, đồng thời, dữ liệu cũ, quyền) mà PRD có rule: thành TC. PRD không có rule: câu hỏi cho PO trong `inception/test-cases/test-cases-questions.md`, không tự đặt kết quả mong đợi.
- Vùng hồi quy lấy từ impact matrix và mục 2 của HLD.
- Mã `TC-n` ổn định, không đánh lại. TC hồi quy không thuộc US: cột US ghi `REG`.
- Ghi mục "Góc đã quét không áp dụng". PRD trống "Conner case" thì corner checklist là nguồn chính.
- Lỗi PRD lộ ra khi viết TC: chặn → câu hỏi cho PO; không chặn → "Ghi chú cho PO" ở `tech-state.md`.

## Verify
`python engine/tech/scripts/tech-tools.py trace intents/<slug> --stage=tc` không còn dòng `TC-GAP` (US thiếu TC, thiếu Happy + Negative/Edge, BR chưa có TC). Không tự kết luận "phủ đủ" khi chưa chạy.

## Gate
QA lead duyệt. Còn câu chặn cho PO vẫn Approve được: TC liên quan ghi "chờ PO", liệt kê ở `decisions.md` (mã `DEC-T<n>`) là Accepted risk; PO trả lời thì mở lại `[R]` các TC đó. Sau Approve: lên version số nguyên kế tiếp, archive, `[x]`.
