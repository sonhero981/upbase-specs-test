# Đề xuất chuẩn hoá po-workflow-upbase theo AWS AI-DLC

| | |
|---|---|
| **Trạng thái** | `DRAFT v0.2`. D1 đến D11 đã được PO duyệt ngày 09/10/2026. Bổ sung stage 2.41 HLD Brief theo yêu cầu PO. Điều chỉnh lần hai cùng ngày: số thập phân thay tiền tố X, plugin `upbase-po` thay chữ extension, Proto-Unit sinh ở 1.4. D12 xác nhận cùng ngày, D12b đổi: lead ghi trong repo, Lark là bản cuối. Đợt 0 đến 4 đã dựng trên nhánh `aidlc-alignment`, chưa commit. Thí điểm đổi theo ý PO ngày 09/10/2026: chuyển Group (đã duyệt PRD) sang v2 thay vì chạy Report Phase 1; cùng ngày chuyển nốt Gamification và Report-Phase-1, gỡ luồng v1, bỏ `projects/`, push nhánh |
| **Ngày** | 08/10/2026, cập nhật 09/10/2026 |
| **Chuẩn tham chiếu** | AWS AI-DLC Workflows v2.10, repo `awslabs/aidlc-workflows`, giấy phép MIT-0 |
| **Phạm vi** | Phần việc của PO/BA. Đầu ra cuối vẫn là PRD theo template công ty |
| **Người duyệt** | Bùi Đức Huy (PO) |
| **Cách đọc** | Mục 0 và mục 6 đủ để quyết. Mục 2 là thiết kế chi tiết. Phụ lục là bản nháp file để hình dung |

---

## 0. Tóm tắt cho người duyệt

**Giữ nguyên:** toàn bộ nội dung phân tích của repo. Impact Matrix 12 vùng, Solution Options, Field Intake, KB có hạn đối chiếu, quy tắc "không bịa", quy tắc ranh giới PO với Dev, publish Lark có đối chiếu, User Guide, cập nhật ngược KB.

**Đổi theo AWS:** thuật ngữ và cách đánh số stage, một nghi thức chung cho mọi stage, gate hai lựa chọn kèm ba lối thoát, file câu hỏi là nguồn sự thật, review độc lập bằng agent Product Lead, vòng học sau mỗi gate, file trạng thái, lưu trữ bản đã duyệt, mã truy vết ổn định có kiểm tra.

**Bỏ hẳn:** không mượn engine, hook, sensor dạng mã, Bolt, swarm, walking skeleton, số câu hỏi theo Depth thay cho logic câu chặn.

**Bổ sung 09/10/2026 theo yêu cầu PO:** stage `2.41 HLD Brief & Alignment`. Một tài liệu tối đa ba trang cho người đọc, dùng đi họp với lead Design, Dev, QA. Lead các team ghi định hướng của mình vào đó. Chốt tầng này xong mới sinh PRD chi tiết. Chi tiết ở mục 2.15.

**Kết quả mong đợi:** người ngoài đọc repo nhận ra đúng khung AI-DLC của AWS. PO vẫn làm việc bằng tiếng Việt, số lần phải trả lời tương đương hiện nay. Ba lỗi đã gặp (ghi đè bản đã duyệt, hai file lệch nhau, bảng mẫu lọt vào PRD) bị chặn bằng cơ chế thay vì bằng lời dặn.

**Triển khai:** bốn đợt, thí điểm trên intent Report Phase 1, hai intent đang chạy giữ nguyên. Có đường lùi.

**Cần bạn quyết 11 điểm ở mục 6.** Mỗi điểm có khuyến nghị sẵn, bạn chỉ cần đồng ý hoặc sửa.

---

## 1. Mục tiêu và ràng buộc

| Mục tiêu | Tiêu chí đạt |
|---|---|
| Uy tín | Mọi khái niệm trong repo dùng đúng tên và đúng nghĩa trong glossary của AWS. Phần repo thêm đóng gói thành plugin `upbase-po` |
| Toàn cầu | Tên file, heading cấu trúc, mã, tên stage bằng tiếng Anh. Nội dung nghiệp vụ tiếng Việt |
| Đầu ra | Vẫn là PRD theo template công ty. AI-DLC coi PRD là đầu vào, nên PRD Generation là plugin stage cuối cùng |
| Phạm vi | Chỉ các stage AWS giao cho Product Agent, cộng Approval & Handoff, cộng bốn plugin stage. Không có Construction, Operation |
| An toàn | Không chạm hai intent đang chạy. Có đường lùi bằng git |

Ràng buộc kỹ thuật: chạy trên Claude Code hiện có, không cài engine AWS. Mọi cơ chế mô tả bên dưới là Markdown, command, agent file, và vài script nhỏ tuỳ chọn.

---

## 2. Thiết kế đề xuất

### 2.1 Thuật ngữ chuẩn

| Thuật ngữ | Nghĩa trong repo | Thay cho | Nguồn |
|---|---|---|---|
| Space | Toàn bộ repo, một team | repo | AWS |
| Intent | Một yêu cầu đi trọn vòng phân tích | Project | AWS |
| Phase | Ideation, Inception | Giai đoạn | AWS |
| Stage | Một bước có artifact và gate riêng, đánh số theo AWS | Bước | AWS |
| Plugin stage | Stage repo thêm ngoài AWS, gói trong plugin `upbase-po`, số thập phân 2.31, 2.32, 2.41, 2.42 theo quy ước số gợi ý của AWS | | AWS gọi cơ chế thêm stage là plugin |
| Workflow profile `S` `M` `L` | Tập stage, nghi thức và Depth cho một intent | Cỡ yêu cầu | AWS gọi là scope, phía người dùng gọi là workflow profile. Không dùng chữ Scope vì đã dùng cho phạm vi tính năng |
| Depth | Minimal, Standard, Comprehensive | | AWS |
| Approval gate | Điểm duyệt cuối mỗi stage | Gate 1 đến 4, điểm dừng | AWS |
| Approve · Request Changes · Accept as-is · Add [stage] · Reject Initiative | Lựa chọn tại gate | Approved · Approved with Notes · Need Revision | AWS |
| Summary confirmation | Xác nhận tóm tắt câu trả lời trước khi sinh artifact | Field Intake, xác nhận danh sách US | AWS |
| Questions file | `<stage>-questions.md`, nguồn sự thật của câu trả lời | open-questions, bản làm rõ | AWS |
| Record dir | Thư mục của một intent | Thư mục project | AWS |
| State file `state.md` | Trạng thái intent, sáu ký hiệu stage | Dòng Trạng thái trong project-context | AWS |
| Decision Log `decisions.md` | Nhật ký quyết định, có nguyên văn PO | project-decisions | AWS |
| Memory | `memory.md` của intent và `.claude/memory/team.md` của repo | Ghi tay vào CLAUDE.md | AWS |
| Knowledge | `knowledge/domain/` là KB sản phẩm, `knowledge/product/` là kiến thức vai PO | knowledge/domain | AWS |
| Product Lead review | Review độc lập, kết luận READY hoặc NOT-READY, finding `R-01` | /review-output | AWS |
| Verification checklist | Checklist tự kiểm, mục blocking | checklist `[BLOCK]` | AWS gọi là compartment 2. Không gọi là Sensor vì Sensor là script |
| Live source · Pinned record · Last verified | Nguồn sống, bản chốt, ngày đối chiếu | | Repo, dịch tên |
| Initiative Brief | Tài liệu chốt hướng một trang | BRD | AWS |
| `FR` `NFR` | Requirement | `RC` | AWS |
| Proto-Unit `PU` | Nhóm US bàn giao, gợi ý cho Dev | Unit | AWS. Tránh trùng `U1` mà Dev sinh ở stage 2.7 |
| Impact Analysis · Solution Options · Field Intake · Hidden · KB · CR · PRD · US · BR | Giữ nguyên | | Đã là thuật ngữ chung hoặc AWS không có |

### 2.2 Cấu trúc thư mục

```
po-workflow-upbase/
├── CLAUDE.md                       luật cấp tổ chức, ngắn, bất biến trong một lần chạy
├── README.md                       phương pháp, mapping sang AWS AI-DLC, ghi nguồn
├── USER-GUIDE.md                   hướng dẫn thao tác cho PO
├── GLOSSARY.md                     thuật ngữ và họ mã
└── .claude/
    ├── commands/                   mỗi stage một command, cộng tiện ích
    ├── agents/
    │   └── product-lead.md         reviewer độc lập
    ├── protocol/
    │   ├── stage-protocol.md       nghi thức chung, mọi command trỏ tới
    │   ├── gate-protocol.md
    │   ├── review-protocol.md
    │   └── question-format.md
    ├── verification/               checklist theo stage
    ├── templates/                  prd, initiative-brief, requirements, impact-matrix, solution-options, stories, state, questions
    ├── knowledge/
    │   ├── domain/                 16 file KB hiện tại
    │   └── product/                kiến thức vai PO chép từ AWS, có chỉnh cho LMS
    ├── memory/
    │   └── team.md                 bài học đã giữ lại, áp dụng từ intent sau
    ├── scripts/                    lark, tuỳ chọn thêm status-check
    └── intents/
        └── 261008-report-phase-1/
            ├── intent.md           bối cảnh, ràng buộc, mapping Lark, Jira
            ├── state.md
            ├── decisions.md
            ├── memory.md
            ├── inputs/             yêu cầu gốc, ảnh, csv
            ├── ideation/
            │   ├── intent-capture/        intent-statement.md, intent-capture-questions.md
            │   ├── market-research/       competitive-analysis.md
            │   ├── scope-definition/      scope-document.md, scope-definition-questions.md
            │   └── approval-handoff/      initiative-brief.md
            ├── inception/
            │   ├── requirements-analysis/ requirements.md, requirements-analysis-questions.md
            │   ├── impact-analysis/       related-features-map.md, impact-matrix.md
            │   ├── solution-options/      solution-options.md
            │   ├── user-stories/          stories.md
            │   ├── hld-brief/             hld-brief.md, hld-brief-questions.md
            │   └── prd/                   prd.md, field-intake-questions.md, traceability.md
            ├── reviews/            review-<stage>-NN.md
            ├── verification/       phase-check-inception.md
            ├── archive/            bản đã duyệt, bản trước khi CR
            ├── design/             ảnh màn + order.txt
            └── user-guide/
```

Tên thư mục intent theo AWS: `YYMMDD-slug`. Tài liệu bàn giao được đánh dấu trong `state.md`, không cần tách `docs/` và `working/` nữa.

### 2.3 Workflow profiles

| Profile | Dấu hiệu, phải đúng tất cả với S, một trong số với L | Stage chạy | Depth | Summary confirmation | Reviewer | Learnings | Số gate |
|---|---|---|---|---|---|---|---|
| **S** | Chạm 1 màn · không đổi data model · không đổi rule hiện có · không chạm module khác · không chạm Hidden · không tích hợp ngoài · không migration | 2.3, 2.42 | Minimal | Chỉ Field Intake | 2.42 | Tắt | 2 |
| **M** | Chạm tối đa 2 module · thêm field không đổi quan hệ · không conflict · đã rõ hướng giải | 1.1 và 1.4 duyệt chung, 2.3, 2.31, 2.4, 2.41, 2.42 | Standard | Bật | 2.3, 2.4, 2.42 | Bật | 6 |
| **L** | Từ 3 module, hoặc đổi data model, hoặc conflict, hoặc Hidden, hoặc nhiều hướng giải, hoặc tích hợp ngoài và job nền, hoặc migration, hoặc không hoàn tác được | 1.1, 1.2 nếu cần, 1.4, 1.7, 2.3, 2.31, 2.32 nếu cần, 2.4, 2.41, 2.42 | Standard, Comprehensive khi PO yêu cầu | Bật | 1.1, 2.3, 2.4, 2.42 | Bật | 8 đến 10 |

So với hiện nay: L có 4 gate cộng 3 điểm dừng, tức 7 lần PO phải trả lời. L mới có 8 đến 10 gate nhưng mỗi gate nhỏ hơn, và một gate trong đó là buổi họp liên team vốn vẫn phải diễn ra. S giảm còn 2.

Ba quy tắc giữ nguyên, đổi cách thực hiện:

1. Nghi ngờ thì lên cỡ.
2. Nâng cỡ giữa chừng: tại gate có thêm lựa chọn `Add Impact Analysis` hay `Add Solution Options` khi stage phát hiện dấu hiệu vượt cỡ. Đây là cơ chế "Add skipped stage" của AWS.
3. Trước khi chạy, in một dòng xác nhận giống AWS: *"Profile M: 5 stage, 5 gate, Depth Standard, reviewer ở 3 stage. Đồng ý không?"*

### 2.4 Danh sách stage trong phạm vi PO

| # | Stage | Nguồn | Đọc vào | Sinh ra | Thay cho hiện tại | Profile |
|---|---|---|---|---|---|---|
| 1.1 | Intent Capture & Framing | AWS | inputs, KB 15 và 16 | `intent-statement.md` gồm problem, analytics, objective, success metrics, stakeholder map, constraints. `intent-capture-questions.md` | Bước 1 đến 3 phần vấn đề và mục tiêu. BRD mục 1 đến 4 | M, L |
| 1.2 | Market Research | AWS, có điều kiện | intent-statement | `competitive-analysis.md` | Nghiên cứu LMS khác | L khi PO yêu cầu |
| 1.4 | Scope Definition | AWS | intent-statement | `scope-document.md` gồm In, Out, Potential, intent backlog gồm các Proto-Unit có MoSCoW | BRD mục 5 đến 7 | M, L |
| 1.7 | Approval & Handoff | AWS | mọi artifact Ideation | `initiative-brief.md` một trang, có lựa chọn Reject Initiative | BRD, Gate 1 | L |
| 2.3 | Requirements Analysis | AWS | scope-document, KB, Swagger, DB | `requirements.md` gồm FR, NFR, constraints, assumptions, out of scope, open questions. Mã ổn định | clarified-requirements, `RC` | S, M, L |
| 2.31 | Impact Analysis | Plugin `upbase-po` | requirements, KB 12 đến 15, Swagger, DB | `related-features-map.md` chốt bằng summary confirmation, rồi `impact-matrix.md` | Bước 5 và 6, Gate 2 | M, L |
| 2.32 | Solution Options | Plugin `upbase-po`, có điều kiện | requirements, impact-matrix | `solution-options.md` | Bước 7 và 8, Gate 3 | L |
| 2.4 | User Stories | AWS | requirements, impact, solution | `stories.md` gồm danh sách US, vai trò, MoSCoW, bảng FR sang US, mỗi US gắn vào Proto-Unit từ 1.4 | 9A và 9A+, điểm dừng xác nhận US | M, L. Ở S gộp vào 2.42 |
| 2.41 | HLD Brief & Alignment | Plugin `upbase-po` | stories, impact, solution, intent-statement | `hld-brief.md` tối đa ba trang, mục của Design, Dev, QA do lead tự điền, bảng sign-off. Lead ghi trong repo, họp, ký, rồi publish Lark bản cuối | Chưa có. Gamification từng sinh 4 CR sau khi PRD đã viết vì lệch với design và tech | M, L |
| 2.42 | PRD Generation | Plugin `upbase-po` | mọi artifact, Figma, KB | `field-intake-questions.md` chốt bằng summary confirmation, `prd.md`, `traceability.md` | 9B, 9C, Gate 4 | S, M, L |

Không thuộc phạm vi PO, chỉ ghi để mapping: 1.3 Feasibility và 2.6 Domain Design do kiến trúc sư; 1.5 Team Formation và 2.9 Delivery Planning do delivery; 1.6 và 2.5 Mockups do design; 2.1 Reverse Engineering ứng với KB, có tiện ích `/kb-sync` để đối chiếu nguồn sống; 2.2 Practices Discovery ứng với `memory/team.md`; 2.7 Units Generation do Dev, lấy Proto-Units làm gợi ý; 2.8 Contract Design do Dev.

Tiện ích không đánh số: `/po` điều phối và tiếp tục, `/po-status`, `/new-intent`, `/po-review` kèm chế độ shadow, `/change-request`, `/publish-lark`, `/user-guide`, `/kb-sync`. Script hỗ trợ: `.claude/scripts/po-tools.py` với `trace`, `archive`, `status`.

### 2.5 Nghi thức stage

Mọi command chỉ còn phần riêng của stage. Bảy bước dưới đây nằm trong `protocol/stage-protocol.md` và chạy giống nhau ở mọi stage. Công tắc theo profile ở mục 2.3.

```
1 Load      state.md, decisions.md theo cột "Read when", intent.md, artifact đầu vào,
            KB mà stage khai báo, memory/team.md. Không hỏi câu đã có đáp án.
2 Ask       tạo <stage>-questions.md; PO chọn cách trả lời một lần cho cả intent;
            thu câu trả lời, ghi nguyên văn; quét từ mơ hồ, mâu thuẫn, thiếu; hỏi tiếp.
3 Confirm   tóm tắt mọi câu trả lời thành gạch đầu dòng, hỏi "Looks correct / Request changes".
            Chỉ sinh artifact sau khi "Looks correct".
4 Generate  theo template; gắn thẻ nguồn ở artifact nội bộ; mục Assumptions & Open Questions bắt buộc;
            mã ổn định; không để lại chữ mẫu.
5 Verify    chạy checklist của stage, sửa mục blocking;
            rồi gọi agent Product Lead review độc lập nếu profile bật.
6 Learn     ghi memory.md trong lúc làm; tại gate hỏi "Có gì cần nhớ cho lần sau không?".
7 Gate      thông điệp hoàn thành năm phần; câu hỏi duyệt; ghi quyết định nguyên văn;
            cập nhật state.md; lưu bản đã duyệt vào archive; nêu tên stage kế tiếp.
```

Thay đổi hành vi đáng chú ý so với hiện nay:

- Câu trả lời của PO được ghi **nguyên văn** vào questions file trước khi AI diễn giải. Hiện nay AI chép lại theo cách hiểu của mình.
- Có bước Confirm ở mọi stage M và L, không chỉ ở PRD.
- Review do agent khác làm, không phải AI vừa viết tự chấm.
- Bản được duyệt được chụp vào `archive/` ngay tại gate, nên không thể bị ghi đè.

### 2.6 Gate

| Lựa chọn | Khi nào hiện | Hệ quả |
|---|---|---|
| Approve | Luôn | Finding còn mở ghi là Accepted risk vào decisions.md. Sang stage kế |
| Request Changes | Luôn | Lời PO là phản hồi. AI sửa, chạy lại review nếu artifact đổi, trình lại gate |
| Accept as-is | Từ lần Request Changes thứ ba | Duyệt và lưu bản hiện tại, ghi rõ là chấp nhận có điều kiện |
| Add [stage] | Ở Ideation và Inception khi có stage đã bỏ qua | Thêm stage vào kế hoạch, tiếp tục bình thường |
| Reject Initiative | Chỉ ở 1.7 | Kết thúc intent, ghi lý do |

Quy tắc đọc câu trả lời, lấy từ AWS: "ok nhưng đổi tên trường X" là Approve kèm chỉ thị, AI làm rồi nói một dòng. "Duyệt, hôm nay dừng ở đây" là Approve kèm park. Trả lời không rõ thì hỏi một câu ngắn. Mọi câu trả lời tại gate được ghi nguyên văn.

Sau Approve in một dòng tiến độ: `Progress: 3/5 stages | INCEPTION 1/3. Next: User Stories`.

### 2.7 File câu hỏi

Mỗi stage có `<stage>-questions.md`. Mỗi câu: ngữ cảnh một dòng, lựa chọn A đến E, luôn có `X. Khác`, đáp án AI đề xuất đánh dấu `[đề xuất]`, cờ `Chặn: có/không`, thẻ `[Answer]:` để trống. Ba cách trả lời:

| Cách | PO làm gì | AI làm gì |
|---|---|---|
| Guide me | Trả lời từng lô tối đa 4 câu qua hộp chọn | Ghi vào file ngay sau mỗi lô |
| Edit file | Mở file, điền `[Answer]:`, gõ "xong" | Đọc file, hỏi tiếp câu còn trống |
| Chat | Nói tự nhiên | Trích quyết định, ghi vào file, trình lại để xác nhận |

Giữ các quy tắc tốt của repo: chỉ hỏi câu làm đổi phạm vi hoặc đổi rule, không hỏi kỹ thuật cho Dev, câu hỏi phải cụ thể và trả lời được, mã trích dẫn phải kèm nội dung. Thêm từ AWS: PO nói "tuỳ anh" thì AI chọn, ghi `[uỷ quyền]` kèm nguyên văn, và nói một dòng đã chọn gì.

### 2.8 Review độc lập

Agent `product-lead` là file trong `.claude/agents/`, được gọi bằng Task, nhận đường dẫn stage file, questions file, artifact và artifact đầu vào. Không được đọc hội thoại soạn thảo và `memory.md`. Chỉ ghi một file `reviews/review-<stage>-NN.md`.

| Thành phần | Quy định |
|---|---|
| Kết luận | READY khi không có Critical và tối đa hai Major. Ngược lại NOT-READY |
| Finding | Bảng: mức, vị trí cụ thể trong artifact, vấn đề, hành động cần làm. Mã `R-01`, `R-02` giữ ổn định qua các lần review |
| Tính chất | Tham vấn. Finding hiện ở gate, PO quyết. Không có vòng tự sửa |
| Disposition | Approve ghi mọi finding mở thành Accepted risk. PO bác một finding thì ghi `Rejected: lý do`. Finding ghi đã sửa mà chưa sửa thì `Reopened` |
| Tiêu chí riêng vai PO | Lấy từ AWS: Dev đọc có làm được không, QA có viết test được không, có gì ngầm hiểu mà chưa viết, mọi mục có giá trị không, biên có rõ không, góc đã chốt chưa |

Chế độ Shadow của repo giữ nguyên trong `/po-review --shadow` vì AWS không có.

### 2.9 Vòng học

- Trong lúc làm, AI ghi `memory.md` của intent theo bốn mục: Interpretations, Deviations, Tradeoffs, Open questions. Mỗi dòng có thời gian và tên stage.
- Tại gate, AI đưa các dòng mới thành danh sách chọn, kèm câu "Có gì cần nhớ cho lần sau không?" với hai lựa chọn Không có và Thêm ghi chú.
- Dòng PO giữ lại đi vào `.claude/memory/team.md` dưới heading theo chủ đề, kèm ngày học. Trước khi ghi, AI đối chiếu với CLAUDE.md, mâu thuẫn thì hỏi PO sửa, bỏ, hay nâng lên luật tổ chức.
- Bài học áp dụng từ intent sau, không đổi luật giữa chừng intent đang chạy.
- CLAUDE.md thu gọn còn luật tổ chức. Các đoạn "đã sai một lần" chuyển thành dòng practice trong team.md. Ví dụ: *"Mốc tăng version là mỗi lần qua gate, không phải mỗi lần sửa một dòng (learned 2026-10-06)"*.

### 2.10 Trạng thái, phiên bản, lưu trữ

`state.md` của mỗi intent có: profile, depth, công tắc nghi thức, bảng stage với sáu ký hiệu `[ ]` `[-]` `[?]` `[R]` `[x]` `[S]`, stage hiện tại, việc kế tiếp, phiên bản mới nhất của từng artifact, phiên bản đang ở trên Lark, CR đang mở.

`/po-status` in bảng này cho mọi intent và kiểm tra lệch: artifact có trên đĩa mà state không ghi, state ghi mà file không có, phiên bản trong state khác phiên bản trong file, gate đã duyệt mà decisions.md không có dòng. Phát hiện thì hỏi, không tự sửa.

Phiên bản, đề xuất đổi cách làm:

| Hiện nay | Đề xuất |
|---|---|
| Mỗi lần PO đã xem thì tạo file `v0.x` mới. Group có 6 bản BRD | Tên file ổn định, ví dụ `prd.md`. Phiên bản và trạng thái ghi ở frontmatter và bảng Document version trong file |
| Không có bản chụp | Tại mỗi Approve, chụp artifact vào `archive/<stage>/<artifact>-v<N>-<date>.md`. Trước mỗi CR re-entry cũng chụp. Bản trong archive không bao giờ sửa |
| Lark tra token theo file version | Tên file ổn định nên publish luôn cập nhật đúng node |

Cơ chế này chặn đúng sự cố 06/10: bản PO đã duyệt nằm trong archive do bước gate tạo ra, AI sửa file làm việc thoải mái mà không mất bản duyệt. Nếu bạn vẫn muốn giữ file `v0.x`, mục 6 có lựa chọn.

### 2.11 Mã và truy vết

| Họ mã | Dạng | Phạm vi | Ghi chú |
|---|---|---|---|
| Requirement | `FR1`, `FR1.2`, `NFR1` | intent | Thay `RC` |
| User story | `US1` | intent | Giữ theo template công ty |
| Business rule | `BR1.1` | intent | Bỏ dấu gạch, khớp AWS |
| Proto-Unit | `PU1` | intent | Thay `U1` |
| Câu hỏi | `Q1` trong từng questions file | stage | |
| Câu hỏi mở còn treo | `OQ1` | intent | Gộp `F`, `BA`, `OQ-B`, `OQ-C` vào một sổ |
| Quyết định | `DEC1` | intent | Mỗi dòng decisions.md có mã và cột "Read when" |
| Change request | `CR1` | intent | |
| Finding review | `R-01` | stage | Theo AWS |

Giữ các họ mã nội bộ của Impact Matrix (`CF`, `BI`, `CG`, `TR`) vì chúng chỉ sống trong một artifact. Áp cho intent mới, không đổi mã của Group và Gamification.

Truy vết: `stories.md` có bảng FR sang US; `prd.md` có bảng Traceability FR, US, BR; `traceability.md` ghi trạng thái từng mã theo AWS: OK, GAP, ORPHAN, Deferred, N/A. Trước gate 2.42, AI chạy kiểm tra và ghi `verification/phase-check-inception.md`. Có GAP hoặc ORPHAN thì không mở gate. Đợt đầu làm bằng checklist, đợt sau có thể viết script.

Thẻ nguồn: `[desc]` lời yêu cầu gốc, `[Q3]` câu trả lời, `[KB-04 §3]` nguồn KB, `[DEC5]` quyết định, `[assumption]` giả định. Bắt buộc ở intent-statement, scope-document, requirements. Không đưa vào PRD, vì PRD là tài liệu bàn giao và đã có bảng Traceability.

### 2.12 Change request

Giữ luồng hiện có: ghi CR, đề xuất điểm re-entry là tầng thấp nhất bị ảnh hưởng, PO xác nhận, chạy lại xuôi, mọi gate sau đó duyệt lại, kiểm rule mồ côi và mã gãy. Thêm từ AWS:

- Phân loại trước: thay đổi nhỏ trong stage hiện tại thì sửa và trình lại gate; thay đổi lớn mới đi đường re-entry.
- Trước khi ghi đè, chụp artifact bị ảnh hưởng vào `archive/`.
- Mỗi stage bị mở lại hỏi một câu: Giữ, Sửa, hay Làm lại từ đầu.
- CR ghi nguyên văn lời PO.
- Chạy lại kiểm tra truy vết trước gate 2.42.

### 2.13 Template PRD

| Hiện tại | Đề xuất | Ai quyết |
|---|---|---|
| Conner case | Corner Cases | Chủ template công ty |
| Metrics success | Success Metrics | Chủ template công ty |
| Pre - Condition, Post - Condition | Preconditions, Postconditions | Chủ template công ty |
| Specific Requirement | Specific Requirements | Chủ template công ty |
| Consult, Inform | Consulted, Informed | Chủ template công ty |
| Preferences | References | Repo |
| TDD | Technical Direction | Repo |
| Dữ liệu phải lưu, Vấn đề tồn đọng | Data to Retain, Open Issues | Repo |
| Unit, nhóm bàn giao | Proto-Units | Repo |
| Chưa có | Traceability, bảng FR, US, BR | Repo |
| Chưa có | Phần đầu PRD chép từ HLD Brief đã chốt, References có link HLD Brief | Repo |
| PUBLISH | PUBLISHED | Repo |

Corner Cases: AWS cho Product Agent quét từng thành phần theo một danh sách điều kiện cố định, mỗi điều kiện chốt thành rule, giả định có lý do, hoặc ngoài phạm vi. Đề xuất PO làm phần nghiệp vụ, QA thêm test case. Việc này đổi quy ước "QA điền", nên chỉ làm sau khi chủ template đồng ý. Trước đó, danh sách góc dùng nội bộ ở bước Verify để tìm BR còn thiếu.

### 2.14 Knowledge pack

Chép từ AWS vào `knowledge/product/`, ghi một dòng nguồn: requirements-guide, requirements-elicitation, user-story-patterns, prioritization-frameworks, product-guide, corner-checklist. Corner checklist được viết lại theo LMS: lớp đã kết thúc, học viên bị Block, nhóm rỗng, một người thuộc nhiều nhóm, mail hàng loạt, dữ liệu cũ trước ngày bật tính năng. Các command trỏ tới file nào cần đọc ở stage nào.

---

### 2.15 HLD Brief, tài liệu đồng thuận liên team

Bổ sung ngày 09/10/2026 theo yêu cầu PO.

**Vấn đề:** PRD quá dài để lead Design, Dev, QA đọc hết. PRD Group dài 14.000 từ, phần lớn là chi tiết từng user story. Buổi họp liên team cần một bản nắm nhanh. Lead các team cần chỗ ghi định hướng của mình. Và tầng cao nên được chốt trước khi viết chi tiết: Gamification có 11 CR, trong đó bốn CR phát sinh sau khi PRD đã viết, hai cái từ lúc làm design.

**Thiết kế:**

| Khía cạnh | Quy định |
|---|---|
| Vị trí | Stage `2.41 HLD Brief & Alignment`, sau 2.4 User Stories, trước 2.42 PRD Generation. Profile M và L. S bỏ |
| Artifact | `hld-brief.md`, tối đa ba trang, khoảng 1.500 từ. Mục nào không có nội dung thì bỏ, không để trống |
| Mười hai mục | 1 Tóm tắt mười dòng · 2 Vấn đề và mục tiêu · 3 Phạm vi · 4 Giải pháp tổng thể · 5 User story theo Proto-Unit, chỉ tên và ưu tiên · 6 Ảnh hưởng tới hệ thống hiện có · 7 Quyết định cần chốt trong buổi họp · 8 Design Direction · 9 Technical Direction · 10 Test Strategy · 11 Release và phụ thuộc · 12 Sign-off |
| Ai viết | Mục 1 đến 7 và 11 do AI soạn từ artifact trước đó. Mục 8, 9, 10 do lead Design, Dev, QA tự viết, AI chỉ để sẵn gợi ý nội dung cần có. AI không bao giờ ghi đè mục của người khác |
| Nguồn sự thật | Repo, từ lúc soạn đến lúc ký. Lead Design, Dev, QA ghi mục của mình trực tiếp vào `hld-brief.md` trên repo (remote GitHub `buidhui/po_workflow_upbase`), mỗi người chỉ sửa mục của mình; lead không mở được repo thì gửi PO dán nguyên văn kèm ghi chú. Trước khi giao, AI chụp bản nháp vào `archive/` để so diff khi lead ghi xong. Sau Alignment gate mới publish Lark, và Lark là bản cuối để mọi người đọc. Quyết định trong họp ghi Decision Log kèm tên người quyết |
| Gate Alignment | Approve khi bảng sign-off có Design, Dev, QA ghi "Đồng ý". PO được Accept as-is kèm lý do khi một lead vắng. Request Changes thì AI sửa mục của PO, không đụng mục của lead |
| Sau gate | HLD Brief là nguồn duy nhất cho phần đầu PRD: Problem, Analytics, Objective, Out of scope, Stakeholder, Success Metrics, Solution, Technical Direction, Proto-Units. 2.42 chép từ đó, không viết lại. Đổi phần đầu sau này đi qua CR, sửa brief trước rồi mới tới PRD |
| Dùng khi họp | Mục 1 đọc trong một phút. Mục 7 là agenda. Mục 12 là biên bản |
| Văn phong | Cho người đọc, không có từ ngữ quy trình nội bộ, mã nào cũng kèm nội dung, không viết tắt |

**Bổ sung 09/10/2026 từ `mob-review.md`** (báo cáo họp Mob Review của dự án HRM, cùng ý với Mob Elaboration của AWS): mỗi vai có "điểm cần đặc biệt lưu ý" do người tổng hợp gợi trước, nên đầu mục 8, 9, 10 có tối đa năm dòng AI gợi cho lead; rủi ro đã chấp nhận là điều kiện chặn release chứ không phải backlog, nên mục 6 thêm bảng rủi ro, giả định, finding còn treo kèm điều kiện; quyết định họp có ba mức chứ không chỉ đồng ý, nên mục 12 thêm trạng thái "Yêu cầu sửa" và gate coi nó là Request Changes; bản tổng hợp không được sửa thẳng, sửa ở nguồn rồi tổng hợp lại, ghi thành ghi chú đầu template. Không mượn phần kiến trúc, API contract, database của mob-review vì ngoài phạm vi PO.

**Mapping sang AWS:** Initiative Brief ở stage 1.7 là bản một trang kết thúc Ideation. HLD Brief là bản một trang kết thúc phần Inception của PO. AWS cho ba agent Design, Developer, Quality góp ý song song vào User Stories theo kiểu mob và dùng Domain Design, Refined Mockups cho tầng thiết kế cao. Ở đây mob là người thật, nên cần sign-off nhiều vai, điều AWS không có. Ghi rõ là plugin stage.

**Các lựa chọn cần PO xác nhận:** D12 ở mục 6.

---

## 3. Những gì không làm

- Không chạy engine, hook, sensor của AWS. Không cài binary `aidlc`.
- Không có Bolt, swarm, walking skeleton, Construction, Operation.
- Không đặt số câu hỏi theo Depth. Giữ logic câu chặn.
- Không bắt S chạy gate ở mọi stage.
- Không dịch nội dung nghiệp vụ sang tiếng Anh.
- Không sửa tài liệu của Group và Gamification.
- Không tự ý sửa template công ty trên Lark.

---

## 4. Kế hoạch triển khai

Ước lượng tính bằng phiên làm việc với AI, mỗi phiên khoảng hai giờ. Con số là ước lượng của tôi, sai số lớn.

| Đợt | Nội dung | File chạm | Phiên | Tiêu chí xong |
|---|---|---|---|---|
| 0. Chuẩn bị | Commit việc dở của Group, tag `pre-aidlc`, tạo nhánh `aidlc-alignment`, chép command cũ vào `commands/legacy/` | git | 0.5 | Có đường lùi |
| 1. Nền | GLOSSARY.md, protocol bốn file, template state và questions, decisions.md có cột Read when, CLAUDE.md thu gọn, memory/team.md, `/po` và `/po-status`, `/new-intent` theo cấu trúc mới, bảng profile | khoảng 12 file mới, 3 file sửa | 3 | `/new-intent` tạo đúng cây, `/po-status` đọc được |
| 2. Hỏi và sinh | Command 1.1, 1.4, 1.7, 2.3, 2.31, 2.32, 2.4, 2.41, 2.42 theo nghi thức; questions file ba cách trả lời; summary confirmation; thẻ nguồn; template initiative-brief, requirements, stories, hld-brief; publish-lark theo đường dẫn mới, có mục tiêu HLD Brief | 8 command, 11 checklist, 4 template, 1 script | 5 | Chạy thử một intent giả từ đầu tới PRD |
| 3. Kiểm chứng | Agent product-lead, review-protocol, `/po-review` mới kèm shadow; bảng Traceability và phase check; archive tại gate; `/po-status` kiểm lệch; corner checklist nội bộ | 1 agent, 2 protocol, 1 command | 3 | Review chạy được bằng Task, phase check bắt được GAP cố ý |
| 4. Học và dọn | Learnings loop; chép knowledge pack; README và USER-GUIDE viết lại; đổi tên thư mục; OVERVIEW cũ thành README | 6 file knowledge, 3 doc, đổi tên 4 thư mục | 2 | Thí điểm xong một intent thật |

Thí điểm: ban đầu dự kiến Report Phase 1. PO đổi ngày 09/10/2026: migrate Group sang v2 (`.claude/intents/261005-group/`), artifact giữ nguyên, mapping ghi trong `intent.md`. Gamification và Report-Phase-1 chuyển sang v2 cùng ngày; luồng v1 gỡ, giữ ở tag `pre-aidlc`. Lùi: `git checkout main`.

---

## 5. Rủi ro

| Rủi ro | Mức | Giảm nhẹ |
|---|---|---|
| Mệt vì nghi thức, PO bỏ quy trình | Cao | Công tắc theo profile. S chỉ 2 gate. Đo số lượt trả lời ở intent thí điểm, nếu vượt hiện nay thì tắt bớt |
| AI không theo protocol vì file dài | Trung bình | Protocol dưới 150 dòng, command dưới 120 dòng. Checklist trỏ về protocol. Đợt sau thêm script cho state và archive |
| Tốn token cho reviewer | Trung bình | Chỉ ba stage ở M và L, một lần mỗi stage, advisory |
| Chủ template không duyệt đổi tên mục | Trung bình | Phần repo làm trước. Phần template để sau, không chặn đợt nào |
| AWS đổi tài liệu, repo lệch chuẩn | Thấp | Ghi "theo v2.10" trong README. Rà lại mỗi quý |
| Đường dẫn mới làm hỏng publish-lark | Thấp | Sửa script ở đợt 2, thử dry-run trên PRD Group |

---

## 6. Điểm cần bạn quyết

Đánh dấu vào ô, hoặc ghi ý khác bên cạnh.

| # | Quyết định | Khuyến nghị | Bạn chọn |
|---|---|---|---|
| D1 | Cấu trúc thư mục intent theo phase `ideation/` `inception/`, bỏ tách `docs/` và `working/` | Có. Mapping sang AWS hiện ngay trên cây thư mục | [x] |
| D2 | Đổi tên thư mục hệ thống: `projects` thành `intents`, `_templates` thành `templates`, `_shared-knowledge-base` thành `knowledge/domain`, `checklist` thành `verification` | Có, ở đợt 4. Đã làm 09/10/2026: `_shared-knowledge-base` thành `knowledge/domain`, `_templates` thành `templates/legacy`, `checklist` thành `verification/legacy` (hai cái sau vào `legacy/` vì tên file trùng với v2). `projects` bỏ ngày 09/10/2026 sau khi cả ba dự án chuyển sang `intents/` | [x] |
| D3 | Tên file ổn định cộng archive tại gate, thay cho file `v0.x` | Có. Chặn đúng sự cố cũ bằng cơ chế | [x] |
| D4 | Profile M duyệt chung 1.1 và 1.4 trong một gate | Có. AWS có cơ chế approve together | [x] |
| D5 | Bật reviewer product-lead ở 2.3, 2.4, 2.42 cho M và L | Có | [x] |
| D6 | Bật vòng học mặc định, tắt ở S | Có | [x] |
| D7 | Họ mã mới ở mục 2.11, chỉ áp cho intent mới | Có | [x] |
| D8 | Gửi chủ template công ty đề nghị sửa năm mục tiếng Anh và Corner Cases | Có. Làm phần repo trước, không chờ | [x] |
| D9 | Group và Gamification giữ quy trình cũ, thí điểm ở Report Phase 1 | Có | [x] |
| D10 | README ghi một câu nguồn AWS AI-DLC v2.10 và giấy phép MIT-0 | Có, dù MIT-0 không bắt buộc | [x] |
| D11 | Tiếng Anh cho tên file, heading cấu trúc, mã, tên stage. Tiếng Việt cho nội dung | Có | [x] |

Đã duyệt D1 đến D11 ngày 09/10/2026.

**D12, bổ sung HLD Brief, PO xác nhận ngày 09/10/2026. D12b khác đề xuất ban đầu:**

| # | Lựa chọn | Khuyến nghị | Bạn chọn |
|---|---|---|---|
| D12a | HLD Brief là file riêng `hld-brief.md`, phần đầu PRD chép từ nó. Không nhúng vào PRD | Có. File ngắn mới mang đi họp và cho lead khác sửa được | [x] |
| D12b | Lead các team ghi mục của mình trực tiếp trong repo. Lark chỉ là bản cuối sau sign-off | PO chọn khác đề xuất ban đầu (đề xuất: Lark là nơi sửa, `/hld-brief sync` kéo về). Nguyên văn PO: "lead các team làm việc trên repo, lark là nơi cuối cùng". Bỏ `/hld-brief sync` | [x] |
| D12c | Gate Alignment cần sign-off Design, Dev, QA. PO được Accept as-is kèm lý do | Có | [x] |
| D12d | Chạy ở M và L, S bỏ | Có. S là một màn, không cần họp | [x] |
| D12e | Giới hạn ba trang, khoảng 1.500 từ. Vượt thì checklist chặn | Có | [x] |
| D12f | Tên stage `HLD Brief & Alignment`, tên artifact `HLD Brief`. Trên Lark đặt `[HLD] <tên tính năng>` | Có | [x] |

Câu tuyên bố đề xuất cho README: *"Aligned with AWS AI-DLC Workflows v2.10: Ideation and product-owned Inception stages, AI-DLC terminology and approval protocol, plus the `upbase-po` plugin: four stages for impact analysis, solution options, HLD brief and PRD generation. Construction and Operation are out of scope."*

---

## Phụ lục A. Nháp `protocol/stage-protocol.md`

```markdown
# Stage Protocol

Mọi stage command đều chạy theo nghi thức này. Command chỉ mô tả phần riêng:
frontmatter, câu hỏi gợi ý, template, checklist.

## Frontmatter của một stage command

slug · phase · number · lead (product) · execution (always|conditional) · condition ·
produces · consumes · requires_stage · profiles · reviewer (product-lead|none) ·
summary_confirmation (required|field-intake-only|off) · template · checklist

## 1. Load
- Đọc state.md. Stage này phải là stage kế tiếp trong state; nếu không, dừng và hỏi.
- Đọc decisions.md, chỉ các dòng có "Read when" khớp stage này.
- Đọc intent.md, artifact trong `consumes`, KB mà command liệt kê, memory/team.md.
- Không hỏi câu đã có đáp án trong decisions.md hoặc questions file trước.
- Đánh dấu stage `[-]` trong state.md.

## 2. Ask
- Tạo `<stage>-questions.md` theo question-format.md.
- Lần đầu trong intent, hỏi PO chọn cách trả lời: Guide me, Edit file, Chat. Ghi vào state.md,
  các stage sau dùng lại và nói một dòng đang dùng cách nào.
- Ghi câu trả lời nguyên văn vào `[Answer]:` ngay sau mỗi lô.
- Quét: từ mơ hồ, mâu thuẫn giữa các câu, thiếu dữ kiện cho artifact. Có thì hỏi tiếp.
- PO uỷ quyền: chọn theo [đề xuất], ghi `[uỷ quyền]` kèm nguyên văn, nói một dòng.
- Câu chặn còn trống: dừng ở đây, không sang bước 3.

## 3. Confirm
- Tóm tắt mọi câu trả lời thành gạch đầu dòng. Hỏi: Looks correct / Request changes.
- Request changes: hỏi "sửa gì" nếu PO chưa nói, sửa file, hỏi lại.
- Tắt theo profile thì bỏ qua bước này.

## 4. Generate
- Viết artifact theo template, giữ đúng heading. Xoá mọi chữ hướng dẫn mẫu.
- Artifact nội bộ: thẻ nguồn ở mỗi khối khẳng định. Mục "Assumptions & Open Questions" bắt buộc.
- Mã ổn định theo GLOSSARY.md. Trích mã thì kèm nội dung.
- Không sửa artifact đã nằm trong archive.

## 5. Verify
- Chạy checklist của stage. Mục blocking chưa đạt thì sửa trước.
- Nếu reviewer = product-lead và profile bật: gọi agent theo review-protocol.md.
  Chờ file review. Không tự sửa theo finding; finding đi vào gate.

## 6. Learn
- Trong lúc làm, thêm dòng vào memory.md: thời gian, [stage], mục Interpretations,
  Deviations, Tradeoffs, hoặc Open questions.
- Trước gate, nếu profile bật: đưa các dòng mới thành danh sách chọn,
  hỏi "Có gì cần nhớ cho lần sau không?" với lựa chọn Không có / Thêm ghi chú.
- Dòng được giữ: đối chiếu CLAUDE.md, mâu thuẫn thì hỏi. Ghi vào memory/team.md
  dưới heading phù hợp, kèm "(learned YYYY-MM-DD)".

## 7. Gate
- Đánh dấu `[?]`. Thông điệp hoàn thành năm phần theo gate-protocol.md.
- Hỏi: Approve / Request Changes, cộng Accept as-is sau ba lần, Add [stage] nếu có,
  Reject Initiative chỉ ở 1.7.
- Approve: ghi DEC vào decisions.md với nguyên văn PO; finding mở thành Accepted risk;
  chụp artifact vào archive/; `[x]`; in dòng tiến độ; nêu stage kế.
- Request Changes: `[R]`; sửa; chạy lại bước 5 nếu artifact đổi; trình lại gate.
- Trả lời không rõ: hỏi một câu ngắn. Không suy đoán là duyệt.
- Stage 2.41: gate Alignment, Approve cần bảng sign-off đủ ba lead, xem gate-protocol.md.

## Luôn đúng
- Tách Fact, Assumption, Open Question, Recommendation. Không bịa.
- Không chốt thay PO. Không thiết kế kỹ thuật chi tiết. Không hỏi kỹ thuật cho Dev.
- Dọn dấu vết quy trình khỏi tài liệu bàn giao.
```

## Phụ lục B. Nháp command `requirements-analysis.md`

```markdown
---
slug: requirements-analysis
phase: inception
number: "2.3"
lead: product
execution: always
condition: Chạy ở mọi profile. Ở S đây là stage đầu tiên.
produces: [requirements.md, requirements-analysis-questions.md]
consumes: [scope-document.md (M, L), inputs/* (S)]
requires_stage: [scope-definition]
profiles: [S, M, L]
reviewer: product-lead
summary_confirmation: required
template: templates/requirements.md
checklist: verification/requirements-analysis.md
knowledge: [knowledge/product/requirements-guide.md, knowledge/product/corner-checklist.md,
            knowledge/domain/00-index.md]
---

# 2.3 Requirements Analysis

Theo `protocol/stage-protocol.md`. Phần riêng của stage:

## Câu hỏi gợi ý cho bước Ask
Chọn theo profile, không hỏi câu đã có trong scope-document hoặc decisions.md.
- Hành vi hiện tại nào phải giữ nguyên? Tra KB trước, chỉ hỏi chỗ KB chưa phủ hoặc Hidden.
- Dữ liệu nào bắt buộc phải có, dữ liệu nào bắt buộc phải lưu lại?
- Vai trò nào được làm gì, vai trò nào không?
- Trường hợp biên: rỗng, trùng, đồng thời, dữ liệu cũ trước ngày bật, người dùng bị Block.
- Ràng buộc đa tenant: hằng số nào cứng, hằng số nào cấu hình?
- Yêu cầu nào trùng với thứ đã có? Nêu ngay, kèm mã KB.

## Cấu trúc requirements.md
1. Intent summary, một đoạn, thẻ nguồn.
2. Functional requirements: `FR1`, `FR1.1`, mỗi dòng có nguồn, ưu tiên MoSCoW,
   ghi "existing" nếu KB cho thấy đã có.
3. Non-functional requirements: `NFR1`, chỉ ghi khi đo được.
4. Constraints: nghiệp vụ, tenant, nguồn.
5. Assumptions & Open Questions: `OQ` kèm cờ chặn và người trả lời.
6. Out of scope.
7. Sources read: KB, Swagger, DB, kèm ngày đối chiếu.

## Checklist riêng
- Mỗi FR truy được về scope-document hoặc câu trả lời.
- Không có FR mô tả giải pháp kỹ thuật.
- Vùng KB chưa phủ được đánh `❓BA`, không kết luận.
- Mail event và tính năng Hidden đã tra.

## Gate
Thông điệp hoàn thành liệt kê số FR, NFR, OQ còn chặn. Finding của product-lead nếu có.
Stage kế: Impact Analysis (M, L) hoặc PRD Generation (S).
```

## Phụ lục C. Mẫu file

**questions file**

```markdown
# Requirements Analysis, câu hỏi
Intent: report-phase-1 · Cách trả lời: Guide me · Trạng thái: 2/6 đã trả lời

## Q1. Chỉ số "tỷ lệ hoàn thành" tính trên lượt ghi danh hay trên học viên?
Vì sao hỏi: hai cách cho hai con số khác nhau khi một người học nhiều lớp.
A. Trên lượt ghi danh, mỗi lớp một dòng  [đề xuất, theo KB-11 §2]
B. Trên học viên, lấy khoá gần nhất
C. Cả hai, có bộ chọn
X. Khác
Chặn: có
[Answer]: A, "tính theo lượt ghi danh như SIS đang làm"
```

**state.md**

```markdown
# State: 261008-report-phase-1
Profile: L · Depth: Standard · Answer mode: Guide me
Summary confirmation: on · Reviewer: on · Learnings: on

## Stages
### IDEATION
- [x] 1.1 intent-capture
- [S] 1.2 market-research, PO bỏ qua
- [x] 1.4 scope-definition
- [x] 1.7 approval-handoff
### INCEPTION
- [?] 2.3 requirements-analysis, chờ duyệt
- [ ] 2.31 impact-analysis
- [ ] 2.32 solution-options
- [ ] 2.4 user-stories
- [ ] 2.41 hld-brief
- [ ] 2.42 prd-generation

## Current
Stage: 2.3 · Next action: PO duyệt requirements.md · Open CR: none
Latest versions: initiative-brief v1.0 (approved 10/10) · requirements v0.3
Lark: initiative-brief v1.0 published 10/10 · prd not yet
```

**Thông điệp hoàn thành**

```markdown
# Requirements Analysis hoàn thành

| Artifact | Nội dung |
|---|---|
| requirements.md | 14 FR trong 5 nhóm, 3 NFR, 4 OQ trong đó 1 chặn |
| requirements-analysis-questions.md | 6 câu, đã trả lời hết |

Review của Product Lead: READY, 2 finding Minor.
R-01 Minor · requirements.md > FR4 · chưa nói dữ liệu cũ trước 01/09 xử lý sao · thêm một dòng.

Xem tại: intents/261008-report-phase-1/inception/requirements-analysis/

Approve: sang Impact Analysis, finding mở ghi là Accepted risk.
Request Changes: nói cần sửa gì.
```

**decisions.md**

```markdown
| DEC | Ngày | Stage | Quyết định | Nguyên văn PO | Read when |
|---|---|---|---|---|---|
| DEC7 | 10/10/2026 | 2.3 | Tỷ lệ hoàn thành tính trên lượt ghi danh | "tính theo lượt ghi danh như SIS đang làm" | báo cáo, chỉ số, SIS |
```

## Phụ lục D. Nguồn AWS đã đối chiếu

Repo `awslabs/aidlc-workflows` tại commit ngày 08/10/2026, v2.10.

| Cơ chế trong đề xuất | File nguồn |
|---|---|
| Nghi thức stage, gate, câu hỏi, state, audit | `core/aidlc-common/protocols/stage-protocol.md` |
| Review độc lập, READY và NOT-READY, finding | `core/aidlc-common/protocols/stage-protocol-reviewer.md`, `core/knowledge/aidlc-product-lead-agent/reviewing.md` |
| Vòng học | `core/aidlc-common/protocols/stage-protocol-learnings.md`, `docs/guide/09-rules-and-the-learning-loop.md` |
| Khôi phục, CR, archive | `core/aidlc-common/protocols/stage-protocol-recovery.md` |
| Định nghĩa stage | `core/aidlc-common/protocols/stage-definition.md` |
| Các stage của Product Agent | `core/aidlc-common/stages/ideation/*.md`, `core/aidlc-common/stages/inception/requirements-analysis.md`, `user-stories.md` |
| Kiến thức vai PO | `core/knowledge/aidlc-product-agent/*.md` |
| Truy vết | `core/knowledge/aidlc-shared/verification.md` |
| Thuật ngữ | `docs/guide/glossary.md` |
| Profile và stage | `docs/guide/05-scopes-and-depth.md`, `docs/guide/04-phases-and-stages.md` |
| Nguyên tắc 2.0 | `assets/AI-DLC-Workflows-2.0-Specification.pdf` |
