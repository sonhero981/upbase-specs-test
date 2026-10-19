# Changelog

Phiên bản của engine PO-Workflow. Số phiên bản ở file `VERSION`. Mỗi bản có mục Nâng cấp nói rõ intent đang làm dở được xử lý như thế nào. Repo của sản phẩm khác nhận bản mới theo 3 bước: chạy `python3 engine/scripts/po-tools.py engine-check` để biết file engine nào đã bị sửa tay; chép đè các file có trong `engine/MANIFEST.txt`; gộp `memory/team.md` theo dòng, giữ bài học của cả hai bên, không chép đè. `memory/project.md`, `domain/` và `intents/` giữ nguyên.

## [2.1.0] - 2026-10-19

Đối chiếu lại toàn bộ với AWS AI-DLC Workflows v2.11, commit `0488aff`, theo chín nhóm tiêu chí.

### Cấu trúc
- Engine chuyển ra khỏi `.claude/`: `engine/stages/` cho mười stage, `engine/commands/` cho lệnh tiện ích, cùng `engine/protocol/`, `engine/templates/`, `engine/verification/`, `engine/agents/`, `engine/knowledge/`, `engine/scripts/`.
- Domain pack ở `domain/`, intent ở `intents/`, bộ nhớ ở `memory/`, ngoài mọi thư mục công cụ, theo cách AWS đặt dữ liệu của team ở `aidlc/spaces/`.
- `.claude/` chỉ còn phần cấu hình riêng cho Claude Code: mỗi lệnh tiện ích và AI Reviewer là một lối tắt trỏ tới file trong `engine/`. Bỏ mười lệnh riêng của stage như `/requirements-analysis`: `/po` là lối vào duy nhất, như `/aidlc` của AWS; chạy một stage cụ thể bằng "nhảy tới 2.3".
- `CLAUDE.md` thành `AGENTS.md`, hướng dẫn chung cho mọi công cụ AI; `CLAUDE.md` chỉ còn dòng `@AGENTS.md`.
- Dòng mô tả sản phẩm đang cài rút khỏi `AGENTS.md`; tên sản phẩm chỉ còn trong `domain/`.

### Sửa lỗi
- `po-tools.py trace` báo "Đạt" khi mã FR, US viết trong dấu backtick vì không đọc ra mã nào. Nay nhận mã có backtick, báo lỗi khi không đọc ra mã nào, bắt Deferred và N/A phải có lý do, và cho FR cha đạt khi mọi FR con đạt.
- Câu hỏi bài học được hỏi trước thông điệp hoàn thành. Nay hỏi sau, thành một lượt riêng.
- Dựng domain mới làm mất bài học dùng chung vì `team.md` bị xoá trắng. Nay tách `memory/team.md` dùng chung và `memory/project.md` riêng sản phẩm.
- Checklist cuối của DOMAIN-SETUP không thể đạt vì `CLAUDE.md` còn tên sản phẩm. Nay kiểm bằng `po-tools.py doctor`.
- Kho knowledge vai PO ghi nguồn v2.10 nhưng nội dung là bản 2.11. Nay ghi commit đối chiếu.
- Profile M không có phase check Ideation. Nay chạy ở gate chung của 1.1 và 1.4.
- Reviewer lần sau chấm lại finding PO đã chấp nhận rủi ro. Nay reviewer nhận sổ finding, không nhận file review cũ.
- README ghi bốn stage thêm là plugin "không sửa stage gốc" trong khi 2.4 có sửa. Nay mỗi stage có hàng "Lệch so với AWS"; chữ plugin chỉ là nhãn.
- Câu "Unit của Dev được tách, gộp từ hạng mục ở 1.4" sai so với AWS: stage 2.7 không đọc intent backlog. Đã sửa ở README, GLOSSARY, USER-GUIDE.
- Bảng nguồn và ngày đối chiếu có ở cả `domain.md` mục 2 và `domain/00-index.md`, và đã lệch nhau: Swagger ghi 05/10 ở một nơi, 23/09 ở nơi kia. Nay chỉ còn ở `domain.md`; `/new-domain` và DOMAIN-SETUP không tạo bảng thứ hai.
- USER-GUIDE ghi `/compact` không mất dữ liệu, trong khi câu trả lời chưa ghi file thì mất. Nay có quy tắc ghi file trước khi hết lượt.

### Thêm
- `po-tools.py`: `check` kiểm phần máy kiểm được, `approve` làm trọn ghi chép sau gate, `next` chọn stage kế, `doctor` kiểm môi trường, `index` sinh bảng chỉ mục PRD cho Dev, `replay` kể lại intent, `manifest` và `engine-check` cho nâng cấp, `selftest` chạy bộ intent mẫu trong `engine/tests/`. `status` thêm kiểm tra artifact lệch đầu vào và nguồn KB quá 30 ngày.
- Lệnh `/po-replay`.
- Bước xác nhận giả định ở 1.1 và 2.3.
- Câu hỏi gắn nhãn người trả lời; tối đa bốn lựa chọn để vừa hộp chọn; uỷ quyền chỉ trong stage đang chạy.
- Định nghĩa depth, mục tuỳ chọn đánh dấu trong template, frontmatter `inputs:` ghi version đầu vào.
- Quy tắc phiên bản: nháp 0.x, lần duyệt đầu 1.0, duyệt lại tăng số phụ. Gắn git tag cho bản PRD và HLD Brief đã duyệt.
- Mẫu yêu cầu `engine/templates/request.md` cho `inputs/`.
- Bài học ghi kèm ngày, intent, stage, người duyệt; bài học kiểm được thì đề xuất thêm vào checklist. Bài học có hiệu lực từ stage kế tiếp, theo AWS.
- Cột Người quyết ghi tên thật từ `git config user.name`, kèm giờ.
- `.claude/settings.json`: chặn sửa file trong `archive/`, cho phép chạy `po-tools.py` không hỏi, in trạng thái intent khi mở phiên.
- Workflow GitHub quét lộ thông tin nhạy cảm bằng gitleaks.
- Cột phiên bản nguồn trong `domain.md` mục 2; mã sản phẩm `code` và danh sách `names` trong frontmatter.
- AI Reviewer có giới hạn 60 lượt và ngân sách lượt; review không hoàn tất thì gọi lại một lần.
- Quy tắc nói với PO: bảng từ không nói và cách nói thay, cách báo khi script từ chối.

### Bàn giao liên team
- Chuẩn chung với Design, Tech, QA trong `engine/standards/`: nguyên tắc chia story, quy ước mã, quy tắc bàn giao, ADR 0002 chọn giao việc theo story trên Jira. ADR 0001 chọn file story trong repo được thay bằng ADR 0002 trong cùng bản này.
- Checkpoint là buổi PO làm việc với Design PIC, Tech PIC, QA PIC trên HLD Brief ở 2.41, trước khi viết PRD. Tech PIC ghi story quá lớn ở mục 9 của HLD Brief.
- Mã tính năng `<mã sản phẩm>-F<NNN>` cấp khi tạo intent; mã sản phẩm chốt khi dựng domain pack, domain đang cài dùng `LMS`.
- PRD có khối tiêu chí chấp nhận mã `AC<US>.<n>` ở đầu mục Acceptance criteria. Mỗi AC kiểm được và ghi BR mà nó kiểm; mọi BR có AC; validate của một màn gom thành một AC. Checklist 2.42 chặn khi BR chưa có AC.
- Story List: sau khi PRD được duyệt, `/po-stories` sinh `intents/<intent>/stories/story-list-prd-v<phiên bản>.csv` theo mẫu import CSV của Jira, mỗi US trong PRD một dòng, 11 cột: Project key, Project name, Project type, Issue Type, Summary, Description, Epic Link, 3 cột Labels, Comment. Description theo cú pháp Jira với mã đầy đủ; Comment ghi nguồn PRD, kết quả điều kiện giao Dev và câu hỏi còn mở. Script so với bản CSV trước và in story đổi, story mới.
- Dự án Jira khai ở bước dựng domain: `/new-domain` hỏi, DOMAIN-SETUP mục 5 hướng dẫn, frontmatter `domain.md` có `jira_project_key`, `jira_project_name`, `jira_project_type`, `doctor` cảnh báo khi thiếu. Dòng Jira Epic của `intent.md` nhận `U<n>: <mã Epic>` để gán Epic theo Unit.
- Nguyên tắc chia story ở `engine/standards/story-splitting.md`: định nghĩa story, tiêu chí INVEST và nơi kiểm, các bước chia ở 2.4, dấu hiệu quá lớn, 8 cách tách, dấu hiệu quá nhỏ, các cách không chia, ví dụ, so sánh với AWS. Stage 2.4 và checklist 2.4 dùng nguyên tắc này.
- `po-tools.py`: `feature-id` cấp mã tính năng; `stories` sinh Story List; `dor` kiểm điều kiện giao Dev trên PRD, gồm PRD đã duyệt, US có AC, mọi BR có AC, không còn `❓PO` và câu chặn; `trace` kiểm thêm lớp BR sang AC; `index` dùng mã tính năng và đếm story đạt điều kiện giao Dev; `check` cảnh báo nhóm Cỡ story khi tên US có chữ "và" ở 2.4 hoặc US có hơn 6 AC ở 2.42.
- HLD Brief: câu hỏi và ý kiến về mục của người khác ghi vào mục 7; Design PIC cấp mã màn hình `SCR-` ở mục 8.
- Fixture mới: `story-list` cho Story List và điều kiện giao Dev, `split-signals` cho dấu hiệu story quá lớn.

### Tài liệu
- README.md viết lại, trung lập sản phẩm. Thêm mục 6 Đầu ra chuẩn cho các phase sau: mỗi team nhận gì, checkpoint và giao Dev, nguyên tắc chia story, mã chung, cách viết tiêu chí chấp nhận, Story List, điều kiện giao Dev, tag và chỉ mục, thay đổi sau bàn giao. Thêm mục 9 Mức độ trưởng thành theo 2 trục: phạm vi sử dụng, từ cá nhân tới nhân rộng; và giao tiếp, từ người với người tới máy với máy. Kèm hiện trạng, việc cần làm để lên mức kế và chỉ số cần thu.
- USER-GUIDE.md viết lại theo người đọc: thêm mục cho Design PIC, Tech PIC, QA PIC, mục cho Dev, bảng lệnh của script; mục domain pack không còn dữ kiện của sản phẩm đang cài.
- AGENTS.md, DOMAIN-SETUP.md, GLOSSARY.md viết lại bằng văn viết, bỏ in đậm. DOMAIN-SETUP.md thêm mục Chuẩn bàn giao cho các team. GLOSSARY.md thêm checkpoint, điều kiện giao Dev, Story List, nguyên tắc chia story, tiêu chí chấp nhận, tag bản duyệt, phiên bản artifact, mức độ trưởng thành.
- Sửa chữ PU còn sót thành Unit trong template `scope-document`, `stories` và 2 checklist.

### Đổi tên
- Proto-Unit thành Unit, mã `PU1` thành `U1`, mục PRD Proto-Units thành Units, theo quyết định ngày 19/10/2026. GLOSSARY ghi khác biệt với Unit of work của AWS ở 2.7.
- Agent `product-lead` thành `ai-reviewer`, gọi là AI Reviewer.
- Lead các team thành Design PIC, Tech PIC, QA PIC. Hàng "Lead" trong bảng metadata giữ nghĩa agent dẫn stage của AWS.

### Nâng cấp
- Intent đang dở chuyển cùng thư mục, nội dung không đổi. Đường dẫn `.claude/...` còn trong artifact và archive của intent cũ là lịch sử: `.claude/knowledge/domain/` nay là `domain/`, `.claude/intents/` nay là `intents/`.
- Đường dẫn HLD Brief đã gửi cho PIC đổi thành `intents/<intent>/inception/hld-brief/hld-brief.md`. Gửi lại đường dẫn mới.
- Review đã có giữ nguyên. Lần review sau của một stage: AI dựng sổ finding `reviews/findings-<slug>.md` từ các file review cũ và quyết định trong `decisions.md`, sau đó mới gọi reviewer.
- Intent đã duyệt ở 0.x giữ nhánh 0.x và tăng số phụ ở lần duyệt sau; quy tắc 1.0 áp cho artifact chưa duyệt lần nào.
- PRD đã duyệt trước bản này chưa có khối AC, nên `trace` báo mỗi US "chưa có AC". Thêm AC qua change request khi PRD đó còn được bàn giao tiếp; PRD đã xong thì giữ nguyên.
- Dữ liệu cũ chuyển bằng `po-tools.py migrate intents/<intent> --write`: đổi đường dẫn và thuật ngữ trong file đang dùng, cấp mã tính năng, chuyển file câu hỏi luồng v1 sang dạng `## Q<n>` nếu stage chưa duyệt, chụp lại bản duyệt kèm một DEC. Không sửa `archive/`, `reviews/`, `verification/`, `decisions.md`, `memory.md`, `state.md` ngoài một dòng Log. Đã chạy cho Group, mã `LMS-F002`, và Report Phase 1, mã `LMS-F003`.
- Gamification chưa chạy vì repo chính có thay đổi chưa commit của CR-014. Sau khi commit và gộp nhánh: `po-tools.py migrate intents/260923-gamification --feature LMS-F001 --write`, sau đó sửa khoá `lark` trong frontmatter PRD theo doc đang dùng ghi ở `state.md`.
- Khối AC và hàng Mã tính năng là phần thêm vào template PRD của công ty, chưa đổi tên mục nào; cần chủ template xác nhận trước khi áp cho mọi PRD.
- Có thay đổi chưa commit ở repo cũ thì commit trước khi gộp nhánh này; git nhận ra file đã dời và áp thay đổi vào đúng vị trí mới.

## [2.0.0] - 2026-10-09

Luồng chuẩn hoá theo AWS AI-DLC: hai phase Ideation và Inception, mười stage, profile S, M, L, bảy bước mỗi stage, gate, review độc lập, domain pack tách khỏi engine. Ba intent Group, Gamification, Report-Phase-1 chuyển từ luồng cũ. Luồng cũ giữ ở tag `pre-aidlc`.
