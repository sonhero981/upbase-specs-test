---
description: Stage 2.42 PRD Generation, plugin upbase-po của luồng v2. Field Intake rồi PRD theo template công ty, phần đầu chép từ HLD Brief. Gọi qua /po
argument-hint: <intent-slug>
---
# 2.42 PRD Generation

| | |
|---|---|
| Stage | 2.42 PRD Generation |
| Slug | prd-generation |
| Phase | inception |
| Plugin | `upbase-po` |
| Execution | always |
| Lead | product |
| Produces | `inception/prd/prd.md` · `field-intake-questions.md` · `traceability.md` · `verification/phase-check-inception.md` |
| Consumes | `hld-brief.md` đã approve (M, L bắt buộc) · `stories.md` · `requirements.md` · `impact-matrix.md` · `solution-options.md` · `decisions.md` · `design/` và Figma · KB · Swagger `components.schemas` · schema Lark |
| Requires | hld-brief ở M, L. requirements-analysis ở S |
| Profiles | S, M, L |
| Reviewer | product-lead |
| Summary confirmation | Field Intake, bắt buộc ở mọi profile |
| Template | `.claude/templates/prd.md` · `.claude/templates/traceability.md` |
| Checklist | `.claude/verification/prd-generation.md` |
| Knowledge | KB theo Impact Matrix · product: `corner-checklist.md` khi viết acceptance criteria và business rule, `user-story-patterns.md` §Given/When/Then |

Chạy theo `.claude/protocol/stage-protocol.md`.

## Mục đích
Tài liệu bàn giao duy nhất cho Dev, QA, Design. Phần đầu chép từ HLD Brief đã chốt. Phần Specific Requirement viết chi tiết từng US. Plugin stage; AWS coi PRD là đầu vào, không sinh.

## Load
M, L: thiếu HLD Brief approved thì dừng. S: dùng requirements và inputs.

## Ask là Field Intake, Consolidated Summary của stage
Tra trước khi hỏi, để phân biệt field đã tồn tại với field thật sự mới:
1. Impact Matrix: entity và màn bị chạm.
2. KB 12: bảng, khoá ngoại.
3. Swagger `components.schemas`: field hiện có, kiểu, required, enum. Nguồn tốt nhất cho field.
4. KB 01 đến 11: rule chi phối.
5. Phân loại mỗi màn: **A** mới hoàn toàn, **B** sửa màn có sẵn, **C** chỉ đọc.
Một bảng duy nhất trong `field-intake-questions.md`: Màn · Field · Hiện có? · Kiểu · Bắt buộc · Giá trị hợp lệ · Validate · Rule chi phối · Ghi chú. Điền sẵn `[đề xuất]` từ KB và Swagger; `❓BA` chỗ không suy được. Màn danh sách hỏi thêm filter, search, sort, pagination, cột hiển thị. Field hiện có chỉ hỏi delta và migration.
PO duyệt bảng là xác nhận tóm tắt. `❓BA` chưa quyết thành OQ, không bịa. S cũng phải qua bước này, đây là chỗ hay sai nhất kể cả với yêu cầu nhỏ.

## Generate
`prd.md` theo `.claude/templates/prd.md`:
- **Phần đầu chép từ HLD Brief**: Problem, Analytics, Objective, Out of scope cấp tính năng, Stakeholder, Metrics success, Solution gồm Technical Direction lấy từ mục 9 của brief và Data to Retain, Proto-Units từ mục 5. Không viết lại, chỉ chỉnh câu cho khớp template. S không có brief: viết từ requirements.
- **References**: link HLD Brief, Figma, tài liệu liên quan. Tài khoản staging để trống, người viết điền sau.
- **Specific Requirement**: mỗi US sáu mục theo template công ty: User story, Pre-Condition, Scenario, Acceptance criteria gồm bảng UI dạng A hoặc B với cột Yêu cầu đủ định dạng, placeholder, options, mặc định, disable, tooltip, validate, hành vi; Business rule mã `BR<US>.<n>`, rule chạm tính năng có sẵn dẫn mã KB; Data Field; NFR; Out of scope; Conner case để trống cho QA. Viết liên tục, không dừng giữa từng US, trừ US rủi ro cao.
- **Sơ đồ**: khối Mermaid đặt đúng chỗ trong file, xem hai lỗi Mermaid trên Lark ở `/publish-lark`.
- **Traceability**: bảng FR, US, BR trong PRD; `traceability.md` với trạng thái OK, GAP, ORPHAN, Deferred, N/A.
- **Open Issues**, **Comments**.
Quy tắc giữ nguyên từ luồng cũ: không có mục Database và API; không sequence diagram, cấu trúc bảng, thuật toán, thư viện; hằng số ghi rõ cứng hay cấu hình; field hiện có không được mô tả như mới; không bịa field; mục không áp dụng xoá hẳn; không giữ bảng ví dụ của template; dọn dấu vết quy trình; không viết tắt; dấu `·` giữa các mã.
Profile S: PRD rút gọn gồm metadata, Document version, Problem, Objective, Out of scope, References, Specific Requirement một US. Bỏ Analytics, Stakeholder, Metrics success, Solution, Proto-Units.

## Verify
1. Checklist.
2. Truy vết: chạy `python3 .claude/scripts/po-tools.py trace .claude/intents/<slug> --write`. Script dựng `traceability.md` và bốn dòng đầu của `verification/phase-check-inception.md`; AI kiểm bốn dòng còn lại theo `.claude/templates/phase-check.md`. Có GAP hoặc ORPHAN thì sửa trước gate. Không chạy được python thì làm tay theo template.
3. Reviewer product-lead.

## Gate
Trình: từng US một dòng; BR mới và rule hiện có bị chạm; field, bảng, mail bị ảnh hưởng; mục đã xoá và vì sao; kết quả truy vết; finding review; OQ. Request Changes trỏ mã cụ thể, ví dụ `US2 BR2.3`, sửa nhắm đích. Approve thì prd lên version 1.0, chụp archive, gợi ý `/publish-lark prd`, PO có thể bỏ qua.
Phần PO của intent hoàn tất. `/generate-user-guide` sau khi Dev xong, và cập nhật ngược KB.
