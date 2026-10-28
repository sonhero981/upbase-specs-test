# Specs Workflow

Khung tài liệu của một sản phẩm, từ yêu cầu tới code. Sản phẩm đang cài, danh sách repo code và người ghi ở `workspace.yaml`. **Phần PO** nhận yêu cầu, phân tích, viết PRD theo template chuẩn, sinh Story List để import lên Jira, viết User Guide sau khi Dev xong. **Phần Tech** nhận PRD đã duyệt, chạy các stage thiết kế của AWS AI-DLC và mở Bolt trong store OpenSpec cho dev code ở các repo khác. Engine không phụ thuộc sản phẩm; dữ kiện sản phẩm nằm trong domain pack, repo và người nằm trong `workspace.yaml`.

File này là luật chung cho mọi công cụ AI làm việc trên repo; `CLAUDE.md` chỉ nhập lại file này cho Claude Code. Quy tắc chi tiết nằm trong `engine/protocol/` và từng file stage, không lặp lại ở đây. Tài liệu liên quan:

- [README.md](README.md): phương pháp, từng stage, chuẩn bàn giao, đối chiếu với AWS AI-DLC
- [USER-GUIDE.md](USER-GUIDE.md): thao tác
- [GLOSSARY.md](GLOSSARY.md): thuật ngữ và họ mã
- [DOMAIN-SETUP.md](DOMAIN-SETUP.md): đưa một sản phẩm mới vào quy trình
- [SETUP.md](SETUP.md): cài khung, thêm repo, thêm người
- [CHANGELOG.md](CHANGELOG.md): phiên bản engine và cách nâng cấp
- [engine/tech/knowledge/workflow.md](engine/tech/knowledge/workflow.md): luồng phần Tech, bảng stage, bảng cổng, bảng tra lệnh

## Cấu trúc repo

| Thư mục | Nội dung | Thuộc về |
|---|---|---|
| `engine/` | Stage, lệnh, protocol, template, checklist, agent, script, kiến thức vai PO. Không phụ thuộc sản phẩm, không phụ thuộc công cụ | Engine |
| `engine/standards/` | Chuẩn bàn giao chung với Design, Tech, QA: nguyên tắc chia story, quy ước mã, quy tắc bàn giao, ADR | Engine |
| `engine/tech/` | Phần Tech: `aidlc/` chuẩn AWS chép nguyên văn (MIT-0, không sửa), `stages/` 13 stage, `protocol/`, `templates/`, `agents/`, `scripts/`, `knowledge/`. Không phụ thuộc sản phẩm | Engine |
| `domain/` | Domain pack của sản phẩm đang cài. `codekb/<repo>/` là bản quét code do stage 2.1 sinh | Sản phẩm |
| `workspace.yaml` | Sản phẩm đang cài, danh sách repo code, người, bản công cụ. **File duy nhất phải sửa khi thêm repo hoặc thêm người** | Sản phẩm |
| `openspec/` | Store OpenSpec: `config.yaml`, `schemas/bolt/`, mỗi change là một Bolt. Định dạng do OpenSpec quy định, không tự đổi | Công cụ |
| `scripts/` | `setup.py` sinh `.claude/` từ `engine/` + `workspace.yaml`; `settings.base.json` là nền của `.claude/settings.json` (quyền, luật chặn, hook) — **sửa quyền và hook ở đây**; `doctor.py` kiểm không ghi | Công cụ |
| `intents/` | Hồ sơ từng yêu cầu | Sản phẩm |
| `memory/` | `team.md` bài học dùng chung, gộp theo dòng khi nâng cấp engine; `project.md` bài học của sản phẩm | Cả hai |
| `.claude/` | **Bản sinh ra, không sửa tay.** `python scripts/setup.py` chép `engine/commands/` + `engine/tech/commands/` thành `commands/`, `engine/agents/` + `engine/tech/agents/` thành `agents/`, và sinh `settings.json` từ `scripts/settings.base.json` cộng `repos:` trong `workspace.yaml`, với lệnh python đã dò được. Stage chạy qua `/po` và `/tech` nên không có lệnh riêng cho từng stage | Công cụ |
| `.po/` | Sổ lượt người `turns.jsonl` và giờ chạy hook trên máy này. Không commit, AI không đọc và không sửa | Công cụ |
| `.mcp.json` | MCP server cho Claude Code, ví dụ trình duyệt để chụp màn hình User Guide. Phải nằm ở gốc repo vì Claude Code chỉ đọc ở đó | Công cụ |

Công cụ AI khác: đọc file này, sau đó chạy lệnh bằng cách đọc `engine/commands/<lệnh>.md` hoặc `engine/stages/<stage>.md` và làm theo. Phần cấu hình riêng cho công cụ khác chỉ dựng khi dùng công cụ đó.

## Luồng làm việc

Một luồng duy nhất theo AWS AI-DLC Workflows, phiên bản ghi trong `engine/knowledge/README.md`. Mỗi yêu cầu là một intent trong `intents/`.

- Lệnh: `/new-intent` tạo intent, `/po` chạy stage kế tiếp, `/po-status` xem trạng thái, `/po-review` review độc lập, `/po-replay` tóm lược diễn biến của intent khi bàn giao cho người khác, `/po-stories` sinh Story List để import lên Jira sau gate 2.43, profile S thì sau gate 2.42. Phần Tech: `/tech` chạy stage Tech kế tiếp, `/bolt` code trọn một Bolt.
- Đầu ra của PO là đầu vào của Design, Tech và QA, nên theo chuẩn trong `engine/standards/`: mã tính năng cấp khi tạo intent, tiêu chí chấp nhận có mã trong PRD, mỗi user story một story trên Jira.
- Script: `python3 engine/scripts/po-tools.py` với `next`, `check`, `review-start`, `approve`, `trace`, `status`, `doctor`, `index`, `replay`, `feature-id`, `stories`, `dor`, `migrate`. Số liệu, tiến độ và stage kế lấy từ script, không tự đếm.
- Nghi thức ở `engine/protocol/*.md`, thuật ngữ ở `GLOSSARY.md`, bài học ở `memory/team.md` và `memory/project.md`.
- Tên file artifact ổn định, phiên bản ở frontmatter, bản duyệt chụp vào `archive/` của intent theo `gate-protocol.md`. Không tạo file `v0.x`.
- Intent chuyển từ luồng cũ giữ họ mã cũ trong tài liệu của chúng, ghi ở `intent.md` của từng intent. Luồng cũ nằm ở tag `pre-aidlc`.

## Domain pack

Mọi dữ kiện riêng của sản phẩm nằm trong `domain/`: manifest `domain.md`, KB, corner checklist, template User Guide của công ty; template PRD riêng chỉ khi công ty bắt buộc, khi đó ghi đè template chuẩn `engine/templates/prd.md`. Đọc `domain.md` ở đầu mỗi phiên và ở bước Load của mọi stage. Engine không ghi cứng dữ kiện sản phẩm, kể cả tên sản phẩm; sản phẩm đang cài ghi ở frontmatter của `domain.md`. Đổi domain theo [DOMAIN-SETUP.md](DOMAIN-SETUP.md).

## Knowledge

| Thư mục | Nội dung |
|---|---|
| `domain/` | Domain pack. `domain.md` là manifest: KB nào trả lời câu gì, nguồn sống và bản chốt, dữ kiện cho từng stage, đích publish |
| `engine/knowledge/` | Kiến thức vai PO chép từ AWS AI-DLC, không phụ thuộc sản phẩm; `corner-checklist-aws.md` là bản gốc để mỗi domain viết lại |
| `memory/team.md` | Bài học dùng chung đã giữ lại tại gate, đi theo engine. Đọc ở bước Load của mọi stage |
| `memory/project.md` | Bài học riêng của sản phẩm đang cài. Đọc ở bước Load của mọi stage, làm mới khi đổi domain |

### Quy ước ký hiệu

| Ký hiệu | Nghĩa |
|---|---|
| `BR-<MODULE>-NN` | Business rule trong KB, có trong tài liệu chính thức, giữ nguyên văn |
| `KB-<MODULE>-NN` | Rule AI trích từ văn xuôi, chưa được duyệt |
| `❓PO` | Chưa rõ, không dùng làm căn cứ |
| `[suy ra]` | AI suy luận ra; nguồn không nói trực tiếp |
| Hidden | Tính năng có code nhưng đang ẩn, vẫn phải xét khi phân tích ảnh hưởng |

### Khi nào đọc lại nguồn

KB là bản chụp. Nguồn sống là nguồn còn bản gốc bên ngoài, như schema DB, API spec, tài liệu người dùng: yêu cầu chạm tới vùng nào thì đọc lại nguồn của vùng đó, và quá 30 ngày kể từ lần đối chiếu cuối thì đọc lại trước khi dùng. Bản chốt là nguồn không còn file gốc: nghi ngờ thì hỏi PO, không tự suy. Danh sách nguồn và vùng KB chưa phủ nằm trong `domain.md` mục 2 và 3. Vùng chưa phủ ghi `❓PO`, không kết luận "không ảnh hưởng". Đọc lại thấy khác KB thì cập nhật KB và ngày đối chiếu ngay.

## Cách làm việc

- Trả lời bằng tiếng Việt. Tên stage, mã và thuật ngữ theo `GLOSSARY.md`.
- Nêu kết luận trước, giải thích sau. Phản biện khi thấy lỗ hổng. Hỏi lại khi thiếu thông tin, không đoán.
- Tách rõ Fact, Assumption, Open Question, Recommendation. Không tự điền dữ kiện: thiếu thông tin nhỏ thì ghi Assumption; thiếu thông tin làm đổi phạm vi, rule, dữ liệu hoặc luồng thì ghi Open Question; ô không suy ra được thì ghi `❓PO`.
- Không tự chốt quyết định thay PO; chỉ gợi ý dưới nhãn Recommendation. Lời duyệt và câu trả lời của PO ghi nguyên văn.
- Gate: đánh `[?]`, trình, kết thúc lượt và chờ PO. Chỉ `po-tools.py approve` được đánh `[x]`, và lệnh này chỉ ghi khi `--words` có nguyên văn trong một lượt PO gõ hoặc chọn sau lần sửa artifact cuối. Không tự duyệt, không chép lời duyệt từ lượt cũ. Công cụ không có hook thì PO tự chạy approve trong terminal.
- Sửa artifact đã duyệt phải qua `/change-request`; `decisions.md` chỉ thêm dòng; file review chỉ AI Reviewer ghi; ba file thiết kế `ux-design.md`, `tech-design.md`, `test-design.md` chỉ các team ghi, AI của PO đọc để đối chiếu và viết Decision Brief. Hook của Claude Code chặn các việc trái quy tắc này, trừ việc sửa ba file thiết kế: hook không phân biệt được phiên của PO với phiên của PIC, nên quy tắc đó AI tự giữ. Hook chỉ chặn lỗi vô ý, nên AI không tìm cách đi vòng qua lệnh shell.
- Không thiết kế kỹ thuật chi tiết. Ghi điều phải đúng, để Dev quyết cách làm. Không hỏi câu kỹ thuật thay Dev; chỉ hỏi câu mà đáp án làm đổi phạm vi hoặc business rule. Cần biết một cơ chế kỹ thuật có tồn tại không thì hỏi PO; có endpoint không có nghĩa là có tính năng.
- Tài liệu bàn giao, gồm Initiative Brief, PRD, Decision Brief, Story List và User Guide: không để lại dấu vết quy trình, không viết tắt, mã nào cũng kèm nội dung, các mã đứng cạnh nhau ngăn bằng dấu `·`. Trạng thái duyệt ghi ai duyệt, không ghi số gate. Giữ `❓PO` và bảng lịch sử phiên bản viết bằng lời.
- Trích mã trong trao đổi thì kèm nội dung một dòng. Một intent profile L sinh hàng trăm mã; buộc người đọc mở file để tra là lỗi của người viết.
- Viết tài liệu bằng văn viết: câu đầy đủ chủ vị, không dùng khẩu ngữ, không in đậm trong đoạn văn, không dùng gạch ngang dài để nối ý.

Các quy tắc rút từ lỗi đã gặp và lý do nằm ở `memory/team.md` và `memory/project.md`. Thêm bài học qua vòng học tại gate, không sửa tay giữa chừng một intent.

## Ranh giới

Repo giữ tài liệu, không giữ code. Không bàn quy trình vận hành team. Không tự mở rộng phạm vi KB.

Thư mục ngoài repo chỉ đọc khi: cập nhật KB từ nguồn ghi trong `domain.md`; hoặc làm việc trên repo code khai trong `repos:` của `workspace.yaml` (stage 2.1 Reverse Engineering, 3.5 Code Generation, `/bolt`). Repo nào ngoài hai danh sách đó thì không đọc.

Luật của phần PO ở trên không áp cho phần Tech. Tech không sửa file của PO ngoài `tech-state.md`, dòng `DEC-T<n>` trong `decisions.md`, các thư mục stage Tech và `archive/`. Không ai sửa `engine/tech/aidlc/`.

Gặp điều đáng chú ý nhưng ngoài phạm vi thì ghi một dòng vào mục "câu hỏi để sau" của KB, sau đó quay lại việc chính.

## Bàn giao

Đích publish tài liệu và đích User Guide ghi trong `domain.md` mục 4. Bản publish dành cho người đọc. Story List để import lên Jira nằm trong `intents/<intent>/stories/`, theo `engine/standards/handoff-rules.md`. Agent của Dev đọc PRD trong repo theo tag đã gắn, qua chỉ mục `intents/INDEX.md` do `po-tools.py index` sinh. Chi tiết ở README mục 6.

## Phần Tech

Sau gate 2.43 Design Alignment, Tech chạy `/tech <slug>` theo **đúng stage và artifact của AWS AI-DLC** (bản chép nguyên văn ở `engine/tech/aidlc/`):

- **Inception**, một lần: 2.1 Reverse Engineering → 2.6 Domain Design → 2.7 Units Generation → 2.8 Contract Design → (2.81 Test Cases ∥ 2.9 Delivery Planning).
- **Construction**, cuốn chiếu theo Bolt: 3.1 Functional Design → 3.2/3.3/3.4 NFR và Infrastructure nếu cần → 3.41 UI Map → 3.5 Code Generation (mở Bolt ở `openspec/`, code ở repo dev) → 3.6 Build and Test.

Artifact nằm ở `inception/<stage>/`, `construction/<unit>/<stage>/` và `tech-state.md` của intent. Luồng và bảng cổng: `engine/tech/knowledge/workflow.md`. Nghi thức: `engine/tech/protocol/tech-protocol.md`. Repo, owner và convention từng repo: `workspace.yaml` và `engine/tech/knowledge/system-map.md`.

Hai điểm nối với phần PO:

- **Điều kiện vào.** `/tech` chỉ khởi tạo khi `state.md` của PO có `2.43 [x]`, mục 0 của `inception/tech-design/tech-design.md` kết luận ĐỦ và mục 8 không còn dòng Chặn chưa chốt. Tech Design 1 là bản sơ lược mô tả cấu trúc và làm rõ vấn đề, Tech PIC viết ở 2.43; thiết kế chi tiết chạy sau khi họp chốt. Không có stage riêng để kiểm PRD.
- **Một sổ quyết định.** Quyết định của Tech ghi `DEC-T<n>` vào `decisions.md` của intent, cùng sổ với PO, cột *Read when* ghi stage Tech.

Owner Bolt (dev fullstack) chạy cả Bolt FE + BE từ store bằng `/bolt [change]`; quyền sửa repo code lấy từ `repos:` trong `workspace.yaml`.

## Sửa engine

Phần này cho người giữ engine và AI được giao sửa engine, theo mục Working on This Project trong `AGENTS.md` của AWS. Engine là mọi file trong `engine/` và các file tài liệu ở gốc ghi trong `engine/MANIFEST.txt`. `.claude/` là bản sinh ra: sửa `engine/` xong phải chạy `python scripts/setup.py` để `.claude/` khớp lại, không sửa `.claude/` tay.

Thứ tự mỗi lần sửa:
1. Sửa lỗi script: thêm ca tái hiện lỗi vào `engine/tests/fixtures/` trước, chạy để xác nhận ca đó hỏng, sau đó mới sửa.
2. Chạy `python3 engine/scripts/po-tools.py selftest`. Phải đạt.
3. Chạy `python3 engine/scripts/po-tools.py manifest --write`.
4. Ghi vào CHANGELOG, dưới bản chưa phát hành. VERSION chỉ tăng khi phát hành: đổi VERSION, đổi tiêu đề mục CHANGELOG, chạy lại `manifest --write`, commit, gắn tag `engine-v<X.Y.Z>`.
5. Push. GitHub Actions chạy `selftest` trên Python 3.9 và bản mới nhất, cùng `engine-check --strict`.

Selftest bắt được và không bắt được:

| Việc | Selftest bắt | Phải tự kiểm |
|---|---|---|
| Thêm lệnh cho `po-tools.py` | Lệnh chưa có ca kiểm; tài liệu nhắc lệnh không có | Câu chữ hướng dẫn trong USER-GUIDE |
| Thêm stage | Bảng metadata thiếu dòng; đường dẫn Template, Checklist không có; README mục 3.2 thiếu dòng stage; reviewer lệch `profiles.md` | Nội dung stage so với AWS; dòng Lệch so với AWS |
| Sửa template | Không bắt, trừ heading bắt buộc khi có fixture dùng template đó | Các stage và checklist nhắc tới mục đã đổi |
| Đổi tên file trong `engine/` | Đường dẫn `engine/...` gãy trong mọi tài liệu | Liên kết ngoài repo, deck |
| Phát hành | VERSION khác mục mới nhất của CHANGELOG hoặc đầu MANIFEST; thiếu mục Nâng cấp hoặc dòng Tương thích | Hướng dẫn nâng cấp đúng với intent đang chạy |

Mỗi bản trong CHANGELOG có dòng `Tương thích:` với một trong ba giá trị: chỉ chép engine; chép engine và chạy migrate; phải sửa intent bằng tay. Repo sản phẩm khác đọc dòng này để biết phải làm gì khi nâng cấp.
