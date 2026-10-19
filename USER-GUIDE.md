# Hướng dẫn sử dụng PO-Workflow

Tài liệu này hướng dẫn thao tác. Phương pháp và lý do của từng stage ở [README.md](README.md); thuật ngữ và họ mã ở [GLOSSARY.md](GLOSSARY.md).

| Người đọc | Đọc mục |
|---|---|
| PO, BA | 1 tới 7, 10 tới 12 |
| Design PIC, Tech PIC, QA PIC | 1, 8 |
| Dev và agent AI của Dev | 9 |
| Người phụ trách quy trình | 2, 11, và [DOMAIN-SETUP.md](DOMAIN-SETUP.md) |

## Mục lục

1. [Quy trình tóm tắt](#1-quy-trình-tóm-tắt)
2. [Cài đặt](#2-cài-đặt)
3. [Cấu trúc thư mục](#3-cấu-trúc-thư-mục)
4. [Chạy một intent tới PRD](#4-chạy-một-intent-tới-prd)
5. [Trả lời AI](#5-trả-lời-ai)
6. [Đổi yêu cầu giữa chừng](#6-đổi-yêu-cầu-giữa-chừng)
7. [Bàn giao sau khi PRD được duyệt](#7-bàn-giao-sau-khi-prd-được-duyệt)
8. [Dành cho Design PIC, Tech PIC, QA PIC](#8-dành-cho-design-pic-tech-pic-qa-pic)
9. [Dành cho Dev](#9-dành-cho-dev)
10. [Lệnh](#10-lệnh)
11. [Domain pack](#11-domain-pack)
12. [Xử lý tình huống](#12-xử-lý-tình-huống)

## 1. Quy trình tóm tắt

Một yêu cầu là một intent. Intent đi qua 2 phase: Ideation xác định vấn đề và phạm vi; Inception chuyển phạm vi thành yêu cầu, phân tích ảnh hưởng, chia user story, thống nhất định hướng với các team, sau đó viết PRD. Mỗi stage sinh một artifact và dừng ở một gate cho tới khi PO duyệt.

| Stage | Artifact | Gate | Thư mục trong intent |
|---|---|---|---|
| 1.1 Intent Capture & Framing | `intent-statement.md` | L: gate riêng. M: duyệt chung với 1.4 | `ideation/intent-capture/` |
| 1.2 Market Research | `competitive-analysis.md` | Chỉ khi cần so sánh với sản phẩm khác | `ideation/market-research/` |
| 1.4 Scope Definition | `scope-document.md`, danh sách Unit | Có | `ideation/scope-definition/` |
| 1.7 Approval & Handoff | Initiative Brief một trang | Có, kèm lựa chọn dừng intent | `ideation/approval-handoff/` |
| 2.3 Requirements Analysis | `requirements.md`, mã `FR1`, `NFR1` | Có | `inception/requirements-analysis/` |
| 2.31 Impact Analysis | `related-features-map.md`, `impact-matrix.md` | Có | `inception/impact-analysis/` |
| 2.32 Solution Options | `solution-options.md` | Chỉ khi có nhiều hướng giải | `inception/solution-options/` |
| 2.4 User Stories | `stories.md`, mã `US1` | Có | `inception/user-stories/` |
| 2.41 HLD Brief & Alignment | HLD Brief tối đa 3 trang | Alignment gate, 3 PIC ký | `inception/hld-brief/` |
| 2.42 PRD Generation | PRD, `traceability.md` | Có | `inception/prd/` |
| Sau khi PRD được duyệt | Story List để import lên Jira | Không | `stories/` |
| Sau khi Dev làm xong | User Guide | Không | `user-guide/` |

Profile quyết định số stage. Khi tạo intent, AI đề xuất profile kèm lý do; PO có quyền đổi. Phân vân giữa hai profile thì chọn profile lớn hơn.

| Profile | Khi nào | Stage chạy | Số gate |
|---|---|---|---|
| S | Một màn, không đổi data model, không đổi rule có sẵn, không chạm module khác | 2.3 và 2.42, PRD rút gọn | 2 |
| M | Tối đa 2 module, thêm field nhưng không đổi quan hệ bảng, không conflict, hướng giải đã rõ | 1.1 và 1.4 duyệt chung, 2.3, 2.31, 2.4, 2.41, 2.42 | 6 |
| L | Từ 3 module, đổi data model, có conflict, nhiều hướng giải, tích hợp ngoài hoặc migration | Đủ 10 stage; 1.2 và 2.32 khi cần | 8 tới 10 |

Gate là điểm dừng bắt buộc. AI không sang stage sau khi chưa có lời duyệt rõ ràng, vì mỗi artifact là nền cho artifact sau: lỗi ở requirements không được chặn sẽ đi thẳng vào Impact Matrix và PRD.

Đầu ra cho các team gồm HLD Brief, PRD và Story List để import lên Jira. Chuẩn chung về cách chia story, mã, tiêu chí chấp nhận và điều kiện giao Dev ở README mục 6 và trong `engine/standards/`.

## 2. Cài đặt

### 2.1 Công cụ AI

Quy trình nằm trong `engine/` và `AGENTS.md`, không phụ thuộc công cụ. Với Claude Code, bản terminal, ứng dụng desktop hoặc extension cho IDE đều dùng được; các lệnh `/po`, `/new-intent` có sẵn trong `.claude/commands/`. Với công cụ khác, yêu cầu AI đọc `AGENTS.md`, sau đó đọc `engine/commands/<lệnh>.md` hoặc `engine/stages/<stage>.md` và làm theo.

Mở công cụ AI tại thư mục gốc của repo, nơi có `AGENTS.md` và `engine/`. Mở sai thư mục thì AI không thấy domain pack và lệnh không chạy.

### 2.2 Git

Windows tải tại https://git-scm.com/download/win, giữ mặc định. Mac có sẵn, hoặc chạy `xcode-select --install`.

Cấu hình một lần. Tên này được ghi vào cột Người quyết của mọi quyết định, nên dùng tên thật:

```bash
git config --global user.name "Họ Tên"
git config --global user.email "email@congty.vn"
```

### 2.3 Python

Script `engine/scripts/po-tools.py` cần Python 3.9 trở lên. Không có Python thì quy trình vẫn chạy, nhưng AI phải kiểm thủ công và mất các bước kiểm bằng máy.

Kiểm môi trường sau khi cài và mỗi khi thấy bất thường:

```bash
python3 engine/scripts/po-tools.py doctor
```

Lệnh kiểm tên git, Python, `lark-cli`, thư mục đang mở, file chưa commit, nguồn KB quá hạn đối chiếu, domain pack, mã tính năng trùng, và tên sản phẩm lọt vào engine. Mỗi dòng không đạt có gợi ý cách sửa.

### 2.4 Lark CLI

`/publish-lark` cần `lark-cli` chạy được từ terminal. Lần đầu dùng, hoặc khi AI báo token hết hạn, chạy `lark-cli auth login` và cấp quyền trong trình duyệt.

### 2.5 Chụp màn hình cho User Guide

`.mcp.json` cấu hình sẵn Playwright để chụp màn hình. Lần đầu mở repo, Claude Code hỏi có cho phép MCP server này không; chọn đồng ý. Không dùng thì khi viết User Guide gõ `skip-screenshot`.

## 3. Cấu trúc thư mục

```
po-workflow/
├── AGENTS.md                  luật cho mọi công cụ AI
├── CLAUDE.md                  một dòng, nhập AGENTS.md cho Claude Code
├── README.md                  phương pháp, chuẩn bàn giao, mức độ trưởng thành
├── USER-GUIDE.md              file này
├── DOMAIN-SETUP.md            đưa một sản phẩm mới vào quy trình
├── GLOSSARY.md                thuật ngữ, tên stage, họ mã
├── CHANGELOG.md · VERSION     phiên bản engine và cách nâng cấp
├── engine/                    quy trình, không phụ thuộc sản phẩm và công cụ
│   ├── stages/                mỗi stage một file
│   ├── commands/              lệnh: po, new-intent, po-status, po-review, po-replay, po-stories, change-request, publish-lark, generate-user-guide, new-domain
│   ├── protocol/              nghi thức chung: stage, gate, review, câu hỏi, profile
│   ├── templates/             mẫu artifact, mẫu yêu cầu
│   ├── verification/          checklist của từng stage và từng lệnh
│   ├── agents/ai-reviewer.md  reviewer độc lập
│   ├── standards/             quy ước mã, quy tắc bàn giao, quyết định nơi lưu story
│   ├── knowledge/             kiến thức vai PO lấy từ AWS
│   ├── scripts/po-tools.py    kiểm tra, truy vết, duyệt, sinh story, chỉ mục
│   └── tests/                 intent mẫu để kiểm script
├── domain/                    domain pack: domain.md, KB, corner checklist, template của công ty
├── memory/
│   ├── team.md                bài học dùng chung, đi theo engine
│   └── project.md             bài học của sản phẩm đang cài
├── .claude/                   cấu hình riêng cho Claude Code: lối tắt cho lệnh, trỏ tới engine/
└── intents/
    ├── INDEX.md               chỉ mục PRD đã duyệt cho Dev
    └── 261009-ten-intent/
        ├── intent.md          bối cảnh, mã tính năng, Figma, Jira, Lark
        ├── state.md           đang ở stage nào, việc kế tiếp
        ├── decisions.md       quyết định nguyên văn, người quyết
        ├── memory.md          quan sát của AI, PO đọc tại gate
        ├── inputs/            tài liệu đầu vào
        ├── ideation/  inception/
        ├── stories/           Story List để import lên Jira
        └── reviews/  verification/  archive/  design/  user-guide/
```

`state.md` cho biết intent đang ở đâu và ai làm gì tiếp. `decisions.md` là bộ nhớ của intent; AI tra file này để không hỏi lại câu đã có đáp án. Không xoá hai file này. `archive/` chứa bản đã duyệt và không được sửa.

## 4. Chạy một intent tới PRD

### 4.1 Tạo intent

```
/new-intent Báo cáo giai đoạn 1
```

AI tạo thư mục `intents/<YYMMDD>-bao-cao-giai-doan-1/`, cấp mã tính năng, đọc nhanh KB để ước lượng vùng bị chạm, sau đó hỏi một câu để chốt profile, ví dụ "Profile M: 7 stage, 6 gate. Đồng ý, đổi profile, hay đổi depth?".

Tài liệu đầu vào như mô tả yêu cầu, email, biên bản họp, ảnh đặt vào `inputs/`. Chưa có mô tả thì AI chép mẫu `inputs/request.md` gồm hiện trạng, muốn đổi gì, trong và ngoài phạm vi, điều không được thay đổi, mốc, câu hỏi mở. Gửi mẫu cho người yêu cầu điền. Mục "Điều không được thay đổi" quyết định nhiều nhất tới phân tích ảnh hưởng ở sản phẩm đang vận hành. Link Figma, Jira ghi vào `intent.md`.

### 4.2 Gọi /po

```
/po 261009-bao-cao-giai-doan-1
```

Mỗi lần gọi, AI đọc `state.md` và chạy stage kế tiếp hoặc tiếp tục stage đang dở. Khi làm nhiều intent song song, luôn ghi tên intent trong lệnh. Không có lệnh riêng cho từng stage; muốn chạy một stage cụ thể thì nói "chạy 2.3" hoặc "làm lại 2.4".

Mỗi stage đi qua 7 bước: AI đọc nền, hỏi, tóm tắt để PO xác nhận, viết artifact, tự kiểm, ghi quan sát, trình gate. Cách trả lời ở mục 5.

### 4.3 Ideation, profile M và L

Ở 1.1 và 1.4, AI hỏi về vấn đề, cách người dùng xử lý hiện tại, mục tiêu đo được, stakeholder, sau đó hỏi về phạm vi In, Out, Potential và cách chia nhu cầu thành Unit. Profile M duyệt hai artifact này chung một gate.

1.2 chỉ chạy khi PO muốn so sánh với sản phẩm khác; danh sách mặc định ghi trong `domain/domain.md`.

Ở 1.7, chỉ profile L, AI tóm tắt thành Initiative Brief một trang. Gate này có thêm lựa chọn Reject Initiative để dừng intent. Khi cần, đẩy lên Lark với tên `[Brief] <tên tính năng>`.

### 4.4 Inception

2.3 Requirements Analysis. AI tra KB trước, chỉ hỏi phần còn thiếu, sau đó viết yêu cầu có mã `FR1`, `FR1.1`, `NFR1`. Yêu cầu trùng tính năng đã có được nêu ngay kèm mã KB. Profile S bắt đầu từ đây.

2.31 Impact Analysis. AI trình Related Features Map: module, màn, bảng, endpoint, thông báo, rule liên quan. PO rà soát và bổ sung phần thiếu; nhận ra phần thiếu trong một bản nháp nhanh hơn liệt kê từ đầu. Sau đó AI dựng Impact Matrix 12 vùng và chuyển mọi conflict cho PO quyết.

2.32 Solution Options, khi có nhiều hướng giải. Nếu PO đã có định hướng, AI nhận xét và đề xuất thêm; nếu chưa, AI dựng 2 tới 3 option, so theo 7 tiêu chí và đưa khuyến nghị. Duyệt gate là chọn option.

2.4 User Stories. AI chia story theo `engine/standards/story-splitting.md`: dựng bản đồ story theo vai và bước trong hành trình, xét dấu hiệu story quá lớn, đề xuất cách tách. Mỗi US gắn một Unit, mỗi FR có US phủ. Mỗi US có một thẻ 9 mục: vai và mục tiêu, bối cảnh, luồng chính, nhánh đáng kể, rule đã biết, dữ liệu và vùng chạm, ngoài phạm vi, phụ thuộc, chưa rõ. Thẻ chưa có tiêu chí chấp nhận. PO duyệt cả danh sách lẫn từng thẻ.

2.41 HLD Brief & Alignment. AI viết bản tối đa 3 trang từ những gì đã duyệt và chừa mục 8, 9, 10 cho Design PIC, Tech PIC, QA PIC. PO commit, push và gửi các PIC đường dẫn file; cách ghi của PIC ở mục 8. Khi các PIC ghi xong, PO gọi lại `/po`; AI trình phần thay đổi và mở Alignment gate. Gate chỉ duyệt được khi cả 3 PIC ghi Đồng ý hoặc Có ý kiến. Sau khi duyệt, AI đẩy bản cuối lên Lark với tên `[HLD] <tên tính năng>`.

2.42 PRD Generation. AI tra Impact Matrix, data model, API spec, KB, sau đó lập bảng Field Intake về field, rule, validate cho từng màn; PO điền và duyệt. Sau đó AI viết PRD theo template công ty: phần đầu chép từ HLD Brief, phần Specific Requirement viết từng US với 6 mục, bám mục 4, 8, 9, 10 của brief. Mỗi US có danh sách tiêu chí chấp nhận mã `AC1.1`, mỗi tiêu chí ghi rõ business rule mà nó kiểm. Điểm brief chưa nói, AI ghi đề xuất kèm câu hỏi gắn tên PIC. Trước gate, AI chạy kiểm truy vết FR, US, BR, AC và sửa phần thiếu.

## 5. Trả lời AI

### 5.1 Questions file

Mỗi stage có một file câu hỏi, ví dụ `requirements-analysis-questions.md`. Mỗi câu gồm:

- Nhãn người trả lời: `[PO]`, `[Người yêu cầu]`, `[Design]`, `[Tech]`, `[QA]`, hoặc vai khác ghi trong `domain.md`
- Tối đa 4 lựa chọn và `X. Khác`; lựa chọn AI đề xuất có ghi nguồn
- Dòng `Chặn: có` khi thiếu đáp án thì AI không viết tiếp được
- Dòng `[Answer]:` để ghi câu trả lời

Lần đầu, AI hỏi PO muốn trả lời theo cách nào và dùng cách đó cho cả intent:

| Cách | PO làm gì |
|---|---|
| Guide me | AI hỏi từng câu trong chat, PO chọn, AI ghi vào file |
| Edit file | PO mở file, điền sau `[Answer]:`, báo "xong" |
| Chat | PO viết tự nhiên một lượt, AI tách ra từng câu |

AI ghi câu trả lời nguyên văn. Câu trả lời mơ hồ hoặc mâu thuẫn với câu trước thì AI hỏi lại một câu ngắn. Câu cùng nhãn đứng cạnh nhau, để PO chuyển cả nhóm cho đúng người, hoặc họp theo nhóm, sau đó điền theo cách Edit file.

PO có thể để AI chọn theo đề xuất ở một câu hỏi. AI ghi `[uỷ quyền]` kèm nguyên văn và báo đã chọn gì. Uỷ quyền chỉ áp cho câu hỏi của stage đang chạy, không áp cho bước xác nhận tóm tắt, xác nhận giả định hoặc gate.

### 5.2 Tóm tắt và giả định

Trước khi viết artifact, AI tóm tắt mọi câu trả lời và hỏi Looks correct hoặc Request changes. Ở 1.1 và 2.3, AI liệt kê thêm các giả định để PO chấp nhận hoặc chuyển thành câu hỏi. Đây là bước phát hiện hiểu nhầm với chi phí thấp nhất.

### 5.3 Gate

AI trình thông điệp hoàn thành gồm: artifact ở đâu, điểm chính, giả định và câu hỏi mở, finding của reviewer, dòng tiến độ. Trước khi hỏi duyệt, AI hỏi PO có bài học nào cần giữ. PO trả lời một trong năm lựa chọn:

| Lựa chọn | Kết quả |
|---|---|
| Approve | Đi tiếp. Script đặt phiên bản, chụp bản duyệt vào `archive/`, ghi quyết định |
| Request Changes | AI sửa theo nội dung PO nêu và trình lại |
| Accept as-is | Từ lần Request Changes thứ ba, nhận bản hiện tại kèm điều kiện và lý do |
| Add stage | Chạy thêm một stage ngoài profile, ví dụ thêm 2.32 |
| Reject Initiative | Chỉ ở 1.7, dừng intent |

Lời duyệt bằng câu tự nhiên được hiểu theo ý. "Ok nhưng đổi tên trường X" là Approve kèm chỉ thị; AI sửa và báo một dòng. Câu trả lời không rõ thì AI hỏi lại, không tự coi là duyệt.

Bản nháp mang phiên bản 0.x. Lần duyệt đầu là 1.0; mỗi lần duyệt lại sau change request tăng số phụ.

### 5.4 Bài học

Tại gate, AI đưa vài quan sát và hỏi có gì cần giữ cho lần sau. Dòng PO chọn được ghi vào `memory/project.md`. AI hỏi thêm một câu: bài học có đúng cho mọi sản phẩm không; có thì chuyển sang `memory/team.md`, file đi theo engine. Bài học có hiệu lực từ stage kế tiếp, không áp ngược cho stage đã duyệt.

## 6. Đổi yêu cầu giữa chừng

Mọi thay đổi chạm stage đã duyệt đi qua `/change-request`. Lệnh cũng tự kích hoạt khi PO nói "đổi yêu cầu" hoặc "bổ sung". AI làm theo thứ tự:

1. Ghi `CR<n>` vào `decisions.md` kèm nguyên văn của PO.
2. Chụp artifact bị chạm vào `archive/` với nhãn pre-CR.
3. Đề xuất stage phải quay lại và các gate phải duyệt lại, chờ PO xác nhận.
4. Chạy xuôi từ stage đó, chỉ sửa phần bị chạm.

HLD Brief đổi thì các PIC ký lại. PRD đổi thì phiên bản tăng, Story List được sinh lại và PRD được đẩy lại lên Lark sau khi duyệt.

## 7. Bàn giao sau khi PRD được duyệt

### 7.1 Sinh Story List

```
/po-stories <intent>
```

AI xem trước danh sách: mỗi US trong PRD một story, kèm Unit, Epic và kết quả điều kiện giao Dev. PO đồng ý thì AI ghi `intents/<intent>/stories/story-list-prd-v<phiên bản>.csv`, chỉ khi PRD đã duyệt. File có 11 cột theo mẫu import CSV của Jira; PO import lên Jira bằng chức năng import CSV.

Trước lần đầu, kiểm 2 điểm:
- `domain/domain.md` có `jira_project_key` và `jira_project_name` ở frontmatter. Hai khoá này khai khi dựng domain pack, theo DOMAIN-SETUP.md mục 5.
- Dòng Jira Epic trong `intent.md` có mã Epic. Intent có nhiều Epic thì ghi thêm `U2: <mã Epic>` để story của Unit đó gắn đúng Epic.

### 7.2 Gắn tag và cập nhật chỉ mục

Mỗi lần duyệt PRD hoặc HLD Brief, script in tên tag gợi ý. PO commit PRD cùng file CSV, gắn tag và đẩy tag lên:

```bash
git tag <intent>/prd-v1.0
git push origin <intent>/prd-v1.0
python3 engine/scripts/po-tools.py index --write
```

Lệnh cuối cập nhật `intents/INDEX.md` với mã tính năng, bản PRD đã duyệt, ngày duyệt, service bị chạm, tag, link Lark và số story đạt điều kiện giao Dev. Commit file này.

### 7.3 Trước khi giao Dev

```bash
python3 engine/scripts/po-tools.py dor intents/<intent>
```

Script in story nào đạt, story nào chưa và vì sao, theo 4 điều kiện: PRD đã duyệt; US có tiêu chí chấp nhận; mọi business rule có tiêu chí chấp nhận trỏ tới; US không còn `❓PO` và không còn câu chặn trong Open Issues. Kết quả cũng ghi ở cột Comment của file CSV. Chỉ giao Dev các story đạt. Độ phủ test case do QA theo dõi trên Jira.

### 7.4 Trước khi mở quyền repo cho các team

Các PIC cần quyền ghi repo của PO để viết HLD Brief, nên họ cũng thấy `decisions.md`, `memory.md` và questions file. Rà thông tin nhạy cảm như tài khoản staging trước khi mở quyền. Workflow gitleaks trong `.github/` quét mỗi lần đẩy lên.

## 8. Dành cho Design PIC, Tech PIC, QA PIC

PIC làm việc ở 2 nơi: HLD Brief trên repo của PO trước khi có PRD, và story trên Jira sau khi PRD được duyệt. Sửa repo bằng Claude Code, công cụ AI khác hoặc giao diện web của GitHub đều được. Không cần chạy quy trình của PO.

### 8.1 Ghi định hướng vào HLD Brief, stage 2.41

Buổi checkpoint là buổi PO làm việc với 3 PIC trên HLD Brief, trước khi viết PRD. Tech PIC xác nhận cỡ story ở mục 9: story nào quá lớn để làm trong một sprint thì ghi ra để PO tách trước khi viết PRD.

1. Pull, mở `intents/<intent>/inception/hld-brief/hld-brief.md`. Đọc mục 1 tới 7 do AI viết từ phân tích đã duyệt.
2. Chỉ sửa mục của mình: Design mục 8, Tech mục 9, QA mục 10. Đầu mỗi mục có tối đa 5 dòng in nghiêng nêu điểm cần lưu ý cho vai đó; trả lời các điểm này, sau đó điền khung bên dưới. Ý không áp dụng ghi "không áp dụng".
3. Design PIC cấp mã màn hình `SCR-<tính năng>-<NN>` ngay ở mục 8. Tech PIC ghi service hoặc repo code bị chạm bằng đúng tên Dev dùng.
4. Câu hỏi hoặc ý kiến về mục khác ghi một dòng vào mục 7, gắn người phải trả lời và có chặn hay không. Không sửa mục của người khác.
5. Ký ở mục 12 bằng một trong bốn trạng thái: Chưa xem, Có ý kiến, Đồng ý, Yêu cầu sửa. Chọn Yêu cầu sửa thì ghi rõ cần sửa gì.
6. Commit với message `hld(<intent>): design direction`, `tech direction` hoặc `qa direction`, sau đó push.

PIC không mở được repo thì gửi nội dung cho PO. PO dán nguyên văn, mở đầu bằng "(ghi theo <tên>, <ngày>)", và lưu tin nhắn xác nhận vào `decisions.md`.

### 8.2 Làm việc trên story Jira

Sau khi PRD được duyệt, PO import Story List lên Jira. Mỗi US trong PRD là một story; phần Description chép từ PRD, gồm tiêu chí chấp nhận và business rule có mã đầy đủ.

| Người | Việc trên story |
|---|---|
| Design PIC | Gắn mã màn hình `SCR` và link thiết kế |
| Tech PIC | Gom story vào Unit of work, chia sub-task, ước lượng story point, ghi nhánh code |
| QA PIC | Viết test case mã `TC`, mỗi test case ghi mã AC mà nó kiểm và bản PRD đã dùng khi chạy |

Quy tắc:

1. Không sửa phần Description. Nội dung nghiệp vụ chỉ đổi khi PRD đổi qua change request; khi đó PO sửa story theo danh sách story đổi mà script in ra.
2. Câu hỏi nghiệp vụ ghi bằng comment trên story, gắn người phải trả lời. Câu trả lời làm đổi PRD thì PO đi qua change request.
3. Cột Comment của story ghi kết quả điều kiện giao Dev lúc import. Story chưa đạt thì chờ PO xử lý lý do ghi ở đó trước khi nhận việc.

### 8.3 Mã và cách trỏ

Từ story trên Jira trở đi, mọi team chỉ dùng mã đầy đủ. Design cấp `SCR-<tính năng>-<NN>`; QA cấp `TC-<tính năng>-<NN>`, mỗi test case ghi tiêu chí chấp nhận `AC-<tính năng>-<NN>.<n>` mà nó kiểm. Mã đã cấp không đổi, không dùng lại. Chi tiết ở `engine/standards/id-conventions.md`; quy tắc bàn giao ở `engine/standards/handoff-rules.md`.

## 9. Dành cho Dev

Lark là bản để người đọc. Việc được giao qua story trên Jira. Agent AI của Dev đọc PRD trong repo theo tag của bản đã duyệt, nên luôn lấy đúng bản đã chốt.

1. Đọc `intents/INDEX.md` để biết tính năng nào đã có PRD duyệt, tag nào, service nào bị chạm, bao nhiêu story đạt điều kiện giao Dev.
2. Lấy đúng bản theo tag, bằng `git show <tag>:<đường dẫn>` hoặc qua GitHub MCP server của công cụ đang dùng.
3. Đặt tên nhánh `feat/<tính năng>-<mô tả>`, ví dụ `feat/LMS-F012-quiz-retake`.
4. Thêm trailer vào commit: `Feature: <tính năng>`, và `Story: <US>` khi commit thuộc một story.

Unit trong PRD là cách PO nhóm user story theo giá trị và ưu tiên. Dev chia việc trong phase Construction theo kiến trúc và có thể chia khác. Thiết kế kỹ thuật của Dev ghi ở tài liệu riêng của Dev và gắn link vào story trên Jira, không ghi đè mục nghiệp vụ trong PRD.

## 10. Lệnh

| Lệnh | Dùng khi |
|---|---|
| `/new-intent <tên>` | Tạo intent, cấp mã tính năng, chọn profile |
| `/po <intent>` | Chạy stage kế tiếp hoặc tiếp tục stage đang dở |
| `/po-status [intent]` | Xem trạng thái mọi intent, phát hiện lệch giữa `state.md` và file |
| `/po-review <file>` | Review độc lập bằng AI Reviewer; thêm `--shadow` cho tài liệu người khác viết |
| `/po-replay <intent>` | Kể lại intent theo dòng thời gian: quyết định, review, việc còn chặn. Dùng khi chuyển intent cho PO khác |
| `/po-stories <intent>` | Sinh Story List để import lên Jira từ PRD đã duyệt |
| `/change-request <intent>` | Đổi hoặc bổ sung yêu cầu sau khi đã duyệt |
| `/publish-lark <intent> <artifact>` | Đẩy Initiative Brief, HLD Brief hoặc PRD đã duyệt lên Lark |
| `/generate-user-guide <intent>` | Viết User Guide sau khi Dev làm xong |
| `/new-domain <sản phẩm>` | Dựng khung domain pack trong repo của sản phẩm mới |

Lệnh của script, chạy từ thư mục gốc:

| Lệnh | Việc |
|---|---|
| `po-tools.py doctor` | Kiểm môi trường và domain pack |
| `po-tools.py status` | Trạng thái mọi intent, artifact bị sửa ngoài change request, mã tính năng trùng, nguồn quá hạn |
| `po-tools.py check <intent> <stage>` | Kiểm bằng máy trước gate |
| `po-tools.py trace <intent>` | Truy vết FR, US, BR, AC |
| `po-tools.py approve <intent> <stage>` | Ghi chép sau khi PO duyệt |
| `po-tools.py stories <intent> [--write]` | Xem trước hoặc ghi Story List cho Jira |
| `po-tools.py dor <intent>` | Kiểm điều kiện giao Dev |
| `po-tools.py index --write` | Cập nhật `intents/INDEX.md` |
| `po-tools.py migrate <intent> [--feature <mã>] [--write]` | Chuyển intent tạo từ bản engine cũ |
| `po-tools.py engine-check` | Liệt kê file engine đã bị sửa tay, trước khi nâng cấp |

## 11. Domain pack

Mọi dữ kiện riêng của sản phẩm nằm trong `domain/`. AI đọc `domain/domain.md` đầu mỗi phiên. File này có 6 mục:

| Mục | Nội dung |
|---|---|
| 1. Sản phẩm và phạm vi | Sản phẩm là gì, phần nào ngoài phạm vi |
| 2. Nguồn sống và bản chốt | Nguồn nào còn cập nhật, đọc ở đâu, đối chiếu lần cuối ngày nào |
| 3. Bản đồ KB | File KB nào trả lời câu gì, stage nào dùng |
| 4. Dữ kiện cho từng stage | Sản phẩm so sánh, shared entity dễ vỡ, nguồn field, nơi đăng Lark, đích User Guide |
| 5. Ví dụ dùng trong engine | Ví dụ thật của sản phẩm để AI hiểu đúng quy tắc |
| 6. Thành phần của domain pack | Danh sách file |

Cùng thư mục có KB theo module, `corner-checklist.md` liệt kê corner case thường bị bỏ sót của sản phẩm, và `templates/` chứa template PRD và User Guide của công ty. Kiến thức vai PO không phụ thuộc sản phẩm nằm ở `engine/knowledge/`.

Ba giới hạn của KB:

- KB thường không phủ toàn hệ thống. Vùng chưa phủ ghi trong bản đồ KB; trước khi kết luận một vùng không bị ảnh hưởng, AI đối chiếu với danh sách này.
- Rule do AI trích từ văn xuôi chưa được duyệt. PO xác nhận trước khi dùng làm ràng buộc trong PRD.
- KB là bản chụp. Yêu cầu chạm vùng nào thì AI đọc lại nguồn sống của vùng đó. Bản chốt không còn nguồn gốc thì AI hỏi PO thay vì suy đoán. `doctor` cảnh báo nguồn quá 30 ngày chưa đối chiếu.

Ký hiệu chung trong artifact:

| Ký hiệu | Nghĩa |
|---|---|
| `❓PO` | Chưa rõ, không dùng làm căn cứ |
| `[suy ra]` | AI suy luận ra; nguồn không nói trực tiếp |
| `[Q3]`, `[DEC5]`, `[KB-04 §3]` | Thẻ nguồn: câu trả lời, quyết định, đoạn KB |
| Hidden | Tính năng có code nhưng đang ẩn, vẫn phải xét khi phân tích ảnh hưởng |

Đưa một sản phẩm khác vào quy trình: đọc [DOMAIN-SETUP.md](DOMAIN-SETUP.md) , sau đó chạy `/new-domain` trong repo mới. Engine giữ nguyên, chỉ thay domain pack và `memory/project.md`.

## 12. Xử lý tình huống

| Tình huống | Cách xử lý |
|---|---|
| AI chọn nhầm intent | Báo intent đúng; AI chuyển ngay |
| AI hỏi lại câu đã trả lời | Kiểm `decisions.md` và questions file; câu trả lời có thể chưa được ghi |
| Không biết intent đang ở đâu | `/po-status` |
| AI viết dài hoặc mở rộng phạm vi | Yêu cầu AI quay về phạm vi đã duyệt |
| Phiên làm việc dài, AI bắt đầu sót | Nén phiên, sau đó gọi lại `/po`. Trạng thái và câu trả lời đã ghi vào file thì không mất; nén ngay sau một gate là an toàn nhất |
| Xung đột git ở `state.md`, `decisions.md` hoặc `memory/` | Với `decisions.md`, giữ dòng của cả hai bên và đánh lại số DEC trùng; với `state.md`, lấy trạng thái mới hơn, sau đó chạy `/po-status` |
| Lỡ sửa tay artifact đã duyệt | `/po-status` báo lệch. Thay đổi có chủ đích thì chạy `/change-request`; nếu không, lấy lại bản trong `archive/` |
| Chọn nhầm tại gate | Báo ngay; AI ghi một dòng đính chính và trình lại gate |
| Reviewer báo NOT-READY nhưng PO chấp nhận | Nêu finding nào chấp nhận; AI ghi Accepted risk vào `decisions.md` |
| PIC chưa ký HLD Brief | Chờ, hoặc Accept as-is kèm lý do |
| Story không đạt điều kiện giao Dev | Chạy `po-tools.py dor`, xử lý theo lý do script in ra |
| Lark báo hết hạn đăng nhập | Chạy `lark-cli auth login` |
| Không chụp được màn hình | Gõ `skip-screenshot`; AI để trống vị trí ảnh và liệt kê ảnh còn thiếu |

Các hành vi sau là đúng thiết kế:

| Hiện tượng | Nguyên nhân |
|---|---|
| AI dừng, không sang stage sau | Đang chờ PO duyệt gate |
| AI hỏi nhiều câu `Chặn: có` | Thiếu thông tin làm đổi phạm vi, rule, dữ liệu hoặc luồng |
| Artifact có nhiều `❓PO` | KB chưa phủ vùng đó và AI không được đoán |
| AI không tự sửa theo finding của reviewer | PO quyết sửa hoặc chấp nhận rủi ro |

Người mới nên chạy một intent profile S với một yêu cầu nhỏ có thật trước, thử Request Changes ở một gate, đọc lại `decisions.md` và `state.md`, sau đó mới chạy intent profile M có HLD Brief với các PIC.
