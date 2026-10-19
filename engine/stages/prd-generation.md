# 2.42 PRD Generation

| | |
|---|---|
| Stage | 2.42 PRD Generation |
| Slug | prd-generation |
| Thư mục | `inception/prd` |
| Phase | inception |
| Plugin | `po-workflow` |
| Lệch so với AWS | Stage thêm của PO-Workflow, không có trong AWS. Đánh số thập phân để chen giữa stage gốc; cơ chế plugin của AWS chỉ cho đánh số sau stage cuối của phase |
| Execution | always |
| Lead | product |
| Produces | `inception/prd/prd.md` · `field-intake-questions.md` · `traceability.md` · `verification/phase-check-inception.md` |
| Consumes | `hld-brief.md` đã approve (M, L bắt buộc) · `stories.md` · `requirements.md` · `impact-matrix.md` · `solution-options.md` · `decisions.md` · `design/` và Figma · KB, API spec và schema theo `domain.md` mục 4 phần 2.42 |
| Requires | hld-brief ở M, L. requirements-analysis ở S |
| Profiles | S, M, L |
| Reviewer | ai-reviewer |
| Summary confirmation | Field Intake, bắt buộc ở mọi profile |
| Template | `domain/templates/prd.md` (template công ty, theo `domain.md`) · `engine/templates/traceability.md` |
| Checklist | `engine/verification/prd-generation.md` |
| Knowledge | KB theo Impact Matrix · product: `corner-checklist.md` khi viết acceptance criteria và business rule, `user-story-patterns.md` §Given/When/Then |

Chạy theo `engine/protocol/stage-protocol.md`.

## Mục đích
Tài liệu bàn giao duy nhất cho Dev, QA, Design. Phần đầu chép từ HLD Brief đã chốt. Phần Specific Requirement viết chi tiết từng US. Plugin stage; AWS coi PRD là đầu vào, không sinh.

## Load
M, L: thiếu HLD Brief approved thì dừng. S: dùng requirements và inputs.

## Ask là Field Intake, Consolidated Summary của stage
Tra trước khi hỏi, để phân biệt field đã tồn tại với field thật sự mới:
1. Impact Matrix: entity và màn bị chạm.
2. File data model theo `domain.md`: bảng, khoá ngoại.
3. API spec, nguồn field ghi trong `domain.md` mục 4 phần 2.42: field hiện có, kiểu, required, enum.
4. KB theo module: rule chi phối.
5. Phân loại mỗi màn: **A** mới hoàn toàn, **B** sửa màn có sẵn, **C** chỉ đọc.
Một bảng duy nhất trong `field-intake-questions.md`: Màn · Field · Hiện có? · Kiểu · Bắt buộc · Giá trị hợp lệ · Validate · Rule chi phối · Ghi chú. Điền sẵn `[đề xuất]` từ KB và API spec; `❓PO` chỗ không suy được. Màn danh sách hỏi thêm filter, search, sort, pagination, cột hiển thị. Field hiện có chỉ hỏi delta và migration.
PO duyệt bảng là xác nhận tóm tắt. `❓PO` chưa quyết thành OQ, không tự điền. S cũng phải qua bước này, đây là bước dễ sai nhất kể cả với yêu cầu nhỏ.

## Generate
`prd.md` theo `domain/templates/prd.md`; tên mục chủ template cấm đổi ghi ở `domain.md` mục 4 phần 2.42:
- **Phần đầu chép từ HLD Brief**: Problem, Analytics, Objective, Out of scope cấp tính năng, Stakeholder, Metrics success, Solution gồm Technical Direction lấy từ mục 9 của brief và Data to Retain, Units từ mục 5. Không viết lại, chỉ chỉnh câu cho khớp template. S không có brief: viết từ requirements.
- **References**: link HLD Brief, Figma, tài liệu liên quan. Tài khoản staging để trống, người viết điền sau.
- **Specific Requirement**: mỗi US sáu mục theo template công ty: User story, Pre-Condition, Scenario, Acceptance criteria gồm danh sách tiêu chí chấp nhận có mã, bảng UI dạng A hoặc B với cột Yêu cầu đủ định dạng, placeholder, options, mặc định, disable, tooltip, validate, hành vi; Business rule mã `BR<US>.<n>`, rule chạm tính năng có sẵn dẫn mã KB; Data Field; NFR; Out of scope; Conner case để trống cho QA. Viết liên tục, không dừng giữa từng US, trừ US rủi ro cao.
- **Tiêu chí chấp nhận**, theo `engine/standards/id-conventions.md`: mã `AC<US>.<n>`, ổn định, không đánh lại. Mỗi AC là một câu kiểm được, có đạt hoặc không đạt, viết theo hành vi người dùng thấy: "Khi <điều kiện hoặc hành động>, <kết quả quan sát được>". AC ghi rõ BR mà nó kiểm. Phủ đủ: luồng chính và mỗi nhánh đáng kể trong thẻ US có ít nhất một AC; mỗi BR có ít nhất một AC trỏ tới; validate của cùng một màn gom thành một AC trỏ về bảng UI, không mỗi dòng bảng một AC; NFR đo được thì thành AC. Không viết AC cho điều không kiểm được. QA viết test case từ danh sách này, mỗi AC ít nhất một test case.
- **Mã tính năng**: frontmatter `feature:` và hàng Mã tính năng ở bảng đầu PRD, lấy từ `intent.md`. PRD dùng mã ngắn `US1`, `AC1.1`, `BR1.1`; story trên Jira dùng mã đầy đủ do script đổi.
- **Bám HLD Brief**, M và L: phần chi tiết của từng US phải dẫn được về brief. Scenario theo giải pháp mục 4 và luồng màn mục 8; Data Field, NFR, Data to Retain và điều kiện kỹ thuật trong AC theo Technical Direction mục 9; góc và vùng hồi quy theo Test Strategy mục 10. Chỗ PRD cần chi tiết mà brief chưa nói: viết đề xuất đánh dấu `[đề xuất]` và ghi OQ gắn tên PIC tương ứng. Chỗ PRD mâu thuẫn brief: không tự quyết, hỏi PO; đổi hướng thì `/change-request`, brief lấy lại sign-off. Mục 9 ghi "Dev tự quyết ở detailed design" thì PRD không quy định phần đó.
- **Sơ đồ**: khối Mermaid đặt đúng chỗ trong file, xem hai lỗi Mermaid trên Lark ở `/publish-lark`.
- **Frontmatter**: `inputs:` ghi version của HLD Brief, stories, requirements đã dùng; `services:` liệt kê service hoặc repo code bị chạm, chép từ HLD Brief mục 9, ý Thành phần hiện có bị chạm. Agent của Dev lọc PRD theo dòng này, xem `po-tools.py index`.
- **Traceability**: bảng FR, US, BR trong PRD; `traceability.md` với trạng thái OK, GAP, ORPHAN, Deferred, N/A.
- **Open Issues**, **Comments**.
Quy tắc cố định: không có mục Database và API; không sequence diagram, cấu trúc bảng, thuật toán, thư viện; hằng số ghi rõ cứng hay cấu hình; field hiện có không được mô tả như mới; không tự thêm field; mục không áp dụng xoá hẳn; không giữ bảng ví dụ của template; dọn dấu vết quy trình; không viết tắt; dấu `·` giữa các mã.
Profile S: PRD rút gọn gồm metadata, Document version, Problem, Objective, Out of scope, References, Specific Requirement một US. Bỏ Analytics, Stakeholder, Metrics success, Solution, Units.

## Verify
1. Checklist.
2. Truy vết: chạy `python3 engine/scripts/po-tools.py trace intents/<slug> --write`. Script dựng `traceability.md`, gồm cả lớp BR sang AC, và năm dòng đầu của `verification/phase-check-inception.md`; AI kiểm bốn dòng còn lại theo `engine/templates/phase-check.md`. Có GAP hoặc ORPHAN thì sửa trước gate. Không chạy được python thì làm tay theo template.
3. Reviewer ai-reviewer.

## Gate
Trình: từng US một dòng; BR mới và rule hiện có bị chạm; field, bảng, mail bị ảnh hưởng; chỗ PRD đi xa hơn brief kèm OQ gắn PIC; mục đã xoá và vì sao; kết quả truy vết; finding review; OQ. Request Changes trỏ mã cụ thể, ví dụ `US2 BR2.3`, sửa nhắm đích. Approve bằng `po-tools.py approve`: lần duyệt đầu prd lên 1.0, lần sau tăng số phụ; script chụp archive và in tên tag gợi ý. Sau khi commit thì gắn tag, chạy `/po-stories` để sinh Story List cho Jira, sau đó `po-tools.py index --write` để cập nhật bảng chỉ mục. Gợi ý `/publish-lark prd`, PO có thể bỏ qua.
Phần PO của intent hoàn tất. `/generate-user-guide` sau khi Dev xong, và cập nhật ngược KB.
