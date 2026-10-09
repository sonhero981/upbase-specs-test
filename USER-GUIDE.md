# User Guide: UpLnD PO/BA AI Workflow

Hệ thống hỗ trợ PO/BA đi từ yêu cầu thô tới **PRD bàn giao** theo template công ty, rồi User Guide sau khi Dev xong. Bạn nói chuyện với AI bằng tiếng Việt. Không cần biết lập trình.

Từ 09/10/2026 mọi intent chạy luồng **v2** theo AWS AI-DLC. Ba dự án Group, Gamification, Report-Phase-1 đã chuyển từ luồng cũ sang luồng này ngày 09/10/2026 và giữ họ mã cũ trong tài liệu của chúng.

---

## Mục lục

1. [Workflow làm gì](#1-workflow-làm-gì)
2. [Cài đặt](#2-cài-đặt)
3. [Cấu trúc thư mục](#3-cấu-trúc-thư-mục)
4. [Chạy một intent từ đầu tới PRD](#4-chạy-một-intent-từ-đầu-tới-prd)
5. [Trả lời AI: câu hỏi, tóm tắt, gate](#5-trả-lời-ai-câu-hỏi-tóm-tắt-gate)
6. [Tham khảo lệnh](#6-tham-khảo-lệnh)
7. [Knowledge](#7-knowledge)
8. [Xử lý vấn đề thường gặp](#8-xử-lý-vấn-đề-thường-gặp)
9. [Git và lead các team](#9-git-và-lead-các-team)

---

## 1. Workflow làm gì

Hai phase, mười stage, mỗi stage một artifact. Chỉ **Initiative Brief**, **HLD Brief**, **PRD** và **User Guide** là tài liệu bàn giao; còn lại là bản phân tích nội bộ.

| Stage | Artifact | Gate | Nơi lưu trong intent |
|---|---|---|---|
| 1.1 Intent Capture & Framing | `intent-statement.md` | L: gate riêng. M: duyệt chung với 1.4 | `ideation/intent-capture/` |
| 1.2 Market Research | `competitive-analysis.md` | chỉ khi bạn muốn so với sản phẩm khác | `ideation/market-research/` |
| 1.4 Scope Definition | `scope-document.md`, danh sách Proto-Unit | gate | `ideation/scope-definition/` |
| 1.7 Approval & Handoff | **Initiative Brief**, một trang | gate, có lựa chọn dừng intent | `ideation/approval-handoff/` |
| 2.3 Requirements Analysis | `requirements.md`, mã `FR1`, `NFR1` | gate | `inception/requirements-analysis/` |
| 2.31 Impact Analysis | `related-features-map.md`, `impact-matrix.md` | gate | `inception/impact-analysis/` |
| 2.32 Solution Options | `solution-options.md` | gate, chỉ khi có nhiều hướng giải | `inception/solution-options/` |
| 2.4 User Stories | `stories.md`, mã `US1` | gate | `inception/user-stories/` |
| 2.41 HLD Brief & Alignment | **HLD Brief**, tối đa ba trang | alignment gate, ba lead ký | `inception/hld-brief/` |
| 2.42 PRD Generation | **PRD**, `traceability.md` | gate | `inception/prd/` |
| Sau khi Dev xong | User Guide | | `user-guide/` |

Stage 2.31, 2.32, 2.41, 2.42 là phần repo thêm, gọi là plugin `upbase-po`. Sáu stage còn lại lấy từ AWS AI-DLC.

### Profile quyết định đi mấy stage

Khi tạo intent, AI đề xuất profile kèm lý do. Bạn có quyền đổi. Không chắc S hay M thì chọn M.

| Profile | Dấu hiệu | Stage chạy | Gate |
|---|---|---|---|
| **S** | Một màn, không đổi data model, không đổi rule có sẵn, không chạm module khác | 2.3 rồi 2.42, PRD rút gọn một US | 2 |
| **M** | Tối đa hai module, thêm field nhưng không đổi quan hệ bảng, không conflict, đã rõ hướng giải | 1.1 và 1.4 duyệt chung, 2.3, 2.31, 2.4, 2.41, 2.42 | 6 |
| **L** | Từ ba module, hoặc đổi data model, hoặc có conflict, hoặc nhiều hướng giải | Đủ mười stage; 1.2 và 2.32 chỉ khi cần | 8 đến 10 |

### Gate là gì

Gate là **điểm dừng bắt buộc**. AI không chuyển sang stage sau cho tới khi bạn duyệt rõ ràng. Gate không phải để duyệt cho xong; mỗi artifact là nền cho artifact sau, sai ở dưới thì mọi thứ phía trên viết trên nền sai.

---

## 2. Cài đặt

### 2.1 VS Code + Claude Code

1. Tải VS Code: https://code.visualstudio.com
2. Trong VS Code, nhấn `Ctrl+Shift+X` (Windows) hoặc `Cmd+Shift+X` (Mac), tìm **Claude Code** của **Anthropic**, Install
3. Click icon Claude ở thanh bên trái, **Sign in with Anthropic**
4. Kiểm tra: gõ `Xin chào` vào ô chat, AI trả lời tiếng Việt là được

### 2.2 Git

- **Windows:** https://git-scm.com/download/win, giữ mặc định, chỉ chọn *"Use Visual Studio Code as Git's default editor"*
- **Mac:** đã có sẵn, hoặc `xcode-select --install`

Cấu hình một lần:

```bash
git config --global user.name "Tên của bạn"
git config --global user.email "email@upbase.vn"
```

### 2.3 Mở đúng thư mục

**Bắt buộc:** File → Open Folder → chọn thư mục **`po-workflow-upbase`**. Claude Code chỉ đọc được file trong thư mục đang mở. Kiểm tra: panel Explorer hiện `po-workflow-upbase`, bên dưới có `.claude/` và `CLAUDE.md`.

### 2.4 Python cho script kiểm tra

Script `.claude/scripts/po-tools.py` cần Python 3.9 trở lên, Mac có sẵn. Không có cũng chạy được workflow, AI sẽ kiểm tay.

### 2.5 Chụp màn hình cho User Guide (tuỳ chọn)

`.mcp.json` đã cấu hình sẵn Playwright. Lần đầu mở project, Claude Code hỏi approve MCP server, chọn đồng ý. Không dùng thì khi viết User Guide gõ `skip-screenshot`.

---

## 3. Cấu trúc thư mục

```
po-workflow-upbase/
├── CLAUDE.md                  AI đọc mỗi phiên: phạm vi, quy ước, nguồn tra cứu
├── README.md                  phương pháp, mapping sang AWS AI-DLC
├── USER-GUIDE.md              file này
├── GLOSSARY.md                thuật ngữ, tên stage, họ mã
└── .claude/
    ├── commands/              mỗi stage một lệnh, cộng tiện ích
    ├── protocol/              nghi thức chung: stage, gate, review, câu hỏi, profile
    ├── templates/             mẫu artifact, kể cả template PRD gốc của công ty
    ├── verification/          checklist từng stage và tiện ích
    ├── agents/product-lead.md reviewer độc lập
    ├── knowledge/
    │   ├── domain/            KB sản phẩm UpLnD, 16 file
    │   └── product/           kiến thức vai PO từ AWS, corner checklist cho LMS
    ├── memory/team.md         bài học đã giữ lại tại gate
    ├── scripts/po-tools.py    truy vết, chụp archive, kiểm trạng thái
    ├── intents/               luồng v2
    │   └── 261009-ten-intent/
    │       ├── intent.md          bối cảnh, Figma, Jira, Lark
    │       ├── state.md           đang ở stage nào, việc kế tiếp
    │       ├── decisions.md       mọi quyết định, lời bạn nguyên văn
    │       ├── memory.md          AI ghi quan sát, bạn đọc tại gate
    │       ├── inputs/            ĐẶT TÀI LIỆU ĐẦU VÀO Ở ĐÂY
    │       └── ideation/  inception/  reviews/  verification/  archive/  design/  user-guide/
```

Hai file quan trọng nhất của mỗi intent: **`state.md`** cho biết đang ở đâu và ai phải làm gì tiếp; **`decisions.md`** là bộ nhớ của intent, AI tra để không hỏi lại câu đã có đáp án. Đừng xoá.

---

## 4. Chạy một intent từ đầu tới PRD

### Bước 0: tạo intent

```
/new-intent Báo cáo giai đoạn 1
```

Tên tự do. AI tạo thư mục `.claude/intents/261009-bao-cao-giai-doan-1/`, đọc nhanh KB để đoán vùng bị chạm, rồi hỏi một câu duy nhất để chốt profile, ví dụ: *"Profile M: 7 stage, 6 gate. Đồng ý, đổi profile, hay đổi depth?"*

Sau đó bạn:
1. Đặt tài liệu đầu vào (mô tả yêu cầu, email, biên bản họp, ảnh) vào `inputs/`. Có thể viết mô tả ngay trong lệnh, AI lưu nguyên văn.
2. Điền link Figma, Jira trong `intent.md` nếu đã có.

### Bước 1 trở đi: gọi `/po`

```
/po 261009-bao-cao-giai-doan-1
```

Mỗi lần gọi, AI đọc `state.md`, chạy stage kế tiếp, hoặc tiếp tục stage đang dở. Làm nhiều intent song song thì luôn ghi tên intent trong lệnh.

Mỗi stage đi qua bảy bước: AI đọc nền, **hỏi** bằng questions file, **tóm tắt** để bạn xác nhận, **viết** artifact, **tự kiểm** bằng checklist và reviewer, **ghi bài học**, rồi **trình gate**. Cách trả lời ở mục 5.

### Ideation, profile M và L

**1.1 và 1.4.** AI hỏi về vấn đề, cách người dùng đang xoay xở, mục tiêu đo được, stakeholder, rồi về phạm vi In, Out, Potential và cách chia hạng mục thành Proto-Unit. Profile M duyệt hai artifact này chung một gate.

**1.2.** Chỉ khi bạn muốn so với TalentLMS, Docebo, Moodle hay sản phẩm khác. Không cần thì AI ghi bỏ qua.

**1.7, profile L.** AI gói mọi thứ thành Initiative Brief một trang và hỏi ba câu. Gate này có ba đường: đi tiếp, sửa, hoặc **Reject Initiative** để dừng hẳn. Muốn thì publish lên Lark với tên `[Brief] <tên tính năng>`.

### Inception

**2.3 Requirements Analysis.** AI tra KB trước, chỉ hỏi lỗ hổng còn lại, rồi viết yêu cầu có mã `FR1`, `FR1.1`, `NFR1`. Yêu cầu trùng tính năng đã có được nêu ngay kèm mã KB. Profile S bắt đầu từ đây.

**2.31 Impact Analysis.** AI trình **Related Features Map** trước: module, màn, bảng, endpoint, mail, rule nào liên quan. Bạn xem và bổ sung chỗ sót, đây là chỗ dễ đóng góp nhất vì bạn chỉ cần nhận ra cái thiếu. Rồi AI dựng Impact Matrix 12 vùng, tìm conflict, FR còn thiếu, coverage gap, transition, tenant. Conflict thì AI hỏi bạn quyết, không tự giải.

**2.32 Solution Options.** Khi có nhiều hướng giải. AI hỏi bạn đã có định hướng chưa; có thì nhận xét và gợi thêm, chưa thì dựng hai ba option, so theo bảy tiêu chí, đưa khuyến nghị có điều kiện. Duyệt gate là chọn option.

**2.4 User Stories.** Danh sách US gắn vào Proto-Unit, mỗi FR có US phủ. Bạn xác nhận danh sách; chi tiết viết ở PRD.

**2.41 HLD Brief & Alignment.** AI viết bản tối đa ba trang từ mọi thứ đã duyệt, để trống ba mục cho lead Design, Dev, QA. Bạn gửi lead đường dẫn file trong repo; họ ghi mục của mình và ký ở mục 12 (xem mục 9). Họp xong, gọi lại `/po`, AI trình diff và mở alignment gate. Đủ ba chữ ký mới duyệt; sau duyệt AI publish bản cuối lên Lark với tên `[HLD] <tên tính năng>`.

**2.42 PRD Generation.** AI tra KB, Swagger, Impact Matrix rồi gom **một bảng Field Intake** về field, rule, validate cho từng màn; bạn điền. Rồi AI viết PRD: phần đầu chép từ HLD Brief, phần Specific Requirement chi tiết từng US với sáu mục theo template công ty. Trước gate AI chạy kiểm truy vết FR, US, BR; có lỗ hổng thì sửa trước. Duyệt xong:

```
/publish-lark prd          đẩy PRD lên Lark wiki
/generate-user-guide       viết User Guide sau khi Dev xong
/change-request            khi yêu cầu đổi giữa chừng
```

---

## 5. Trả lời AI: câu hỏi, tóm tắt, gate

### Questions file

Mỗi stage có một file câu hỏi, ví dụ `requirements-analysis-questions.md`. Mỗi câu có lựa chọn A, B, C, lựa chọn `X. Khác`, dòng `Chặn: có` nếu thiếu đáp án thì không viết tiếp được, và dòng `[Answer]:` để ghi câu trả lời. Lựa chọn AI đề xuất có ghi nguồn.

Lần đầu AI hỏi bạn muốn trả lời theo cách nào, rồi dùng cách đó cho cả intent:

| Cách | Bạn làm gì |
|---|---|
| **Guide me** | AI hỏi từng câu trong chat, bạn trả lời, AI ghi vào file |
| **Edit file** | Bạn mở file, điền sau `[Answer]:`, nói "xong" |
| **Chat** | Bạn viết tự nhiên một lượt, AI tách ra từng câu |

AI ghi câu trả lời **nguyên văn**, không diễn giải. Trả lời mơ hồ hoặc mâu thuẫn với câu trước, AI hỏi lại một câu ngắn.

### Tóm tắt xác nhận

Trước khi viết artifact, AI tóm tắt mọi câu trả lời thành gạch đầu dòng và hỏi: **Looks correct** hay **Request changes**. Đây là chỗ bắt hiểu nhầm rẻ nhất.

### Gate

AI trình thông điệp hoàn thành năm phần: artifact ở đâu, điểm chính, giả định và câu hỏi mở, finding của reviewer, dòng tiến độ. Bạn trả lời:

| Trả lời | Nghĩa |
|---|---|
| **Approve** | Ổn, đi tiếp. AI chụp bản duyệt vào `archive/`, ghi DEC |
| **Request Changes** | Nói rõ sửa gì, AI sửa và trình lại |
| **Accept as-is** | Từ lần trình thứ ba, nhận bản hiện tại kèm lý do ghi lại |
| **Add [stage]** | Chạy thêm một stage ngoài profile, ví dụ thêm 2.32 |
| **Reject Initiative** | Chỉ ở 1.7, dừng intent |

Viết tự nhiên cũng được: *"ok nhưng đổi tên trường X"* là duyệt kèm chỉ thị, AI làm rồi báo một dòng. *"Duyệt, hôm nay dừng ở đây"* là duyệt và tạm dừng. Trả lời không rõ thì AI hỏi lại, không tự coi là duyệt.

### Bài học

Tại gate AI hỏi *"Có gì cần nhớ cho lần sau không?"* kèm vài quan sát của nó. Chọn dòng đáng giữ hoặc trả lời "không có". Dòng giữ lại vào `.claude/memory/team.md`, áp dụng từ intent sau.

---

## 6. Tham khảo lệnh

| Lệnh | Dùng khi |
|---|---|
| `/new-intent <tên>` | Tạo intent mới, chọn profile |
| `/po <intent>` | **Chạy stage kế tiếp hoặc tiếp tục**, lệnh chính |
| `/po-status [intent]` | Bảng trạng thái mọi intent, kiểm lệch giữa state và file |
| `/po-review <file>` | Review độc lập bằng agent Product Lead; thêm `--shadow` cho tài liệu người khác viết |
| `/change-request` | Đổi hoặc bổ sung yêu cầu giữa chừng; tự kích hoạt khi bạn nói "tôi đổi yêu cầu", "bổ sung" |
| `/publish-lark <artifact>` | Đẩy Initiative Brief, HLD Brief, PRD đã duyệt lên Lark |
| `/generate-user-guide` | Viết User Guide sau khi Dev xong |

Lệnh của từng stage (`/intent-capture`, `/requirements-analysis`, `/prd-generation`...) tồn tại nhưng gọi qua `/po` để state được cập nhật đúng.

### Đổi yêu cầu giữa chừng

Đừng sửa lẻ tẻ. AI sẽ ghi `CR1` vào `decisions.md` kèm lời bạn, chụp artifact bị ảnh hưởng vào `archive/`, đề xuất stage phải quay lại và gate phải duyệt lại, chờ bạn xác nhận, rồi chạy xuôi từ đó chỉ sửa phần bị chạm. HLD Brief đổi thì lead ký lại.

---

## 7. Knowledge

**KB sản phẩm:** 16 file trong `.claude/knowledge/domain/`, bắt đầu từ `00-index.md`. `01` đến `11` nghiệp vụ; `12` data model; `13` mail event; `14` API surface; `15` định hướng và ràng buộc đa tenant; `16` nguyên tắc mô hình hoá.

**Kiến thức vai PO:** `.claude/knowledge/product/`, chép từ AWS AI-DLC. `corner-checklist.md` là danh sách góc hay sót viết riêng cho LMS: lớp đã kết thúc, học viên bị Block, một người nhiều nhóm, dữ liệu cũ trước ngày bật tính năng, mail hàng loạt. AI quét nó ở 2.3 và 2.42.

### Quy ước ký hiệu

| Ký hiệu | Nghĩa |
|---|---|
| `BR-COURSE-01` | Business rule **có sẵn trong User Guide**, đáng tin |
| `KB-COURSE-01` | AI trích từ văn xuôi, **chưa được duyệt**, cần bạn xác nhận |
| `❓BA` | Chưa rõ, **không dùng làm căn cứ** |
| `[suy ra]` | AI suy luận, không phải câu chữ trực tiếp |
| **Hidden** | Tính năng **đã có code nhưng tạm ẩn**, vẫn phải xét khi phân tích |

### Ba giới hạn cần nhớ

**KB chỉ phủ khoảng một nửa hệ thống.** Ops có 25 nhóm chức năng và LMS có 8 nhóm không có trong User Guide. Trước khi tin "vùng này không bị ảnh hưởng", xem `14-api-surface.md` §1 và §2.

**Rule `KB-*` chưa được duyệt.** 110 rule loại này do AI trích ra, cần bạn xác nhận trước khi dùng làm ràng buộc trong PRD.

**KB là bản chụp, không phải bản gốc.** Schema DB trên [Lark `Data Architecture`](https://upbasevn.sg.larksuite.com/wiki/MaFpweI68iKNMvkTioLlJ1uJgQd), Swagger staging và GitBook là nguồn sống: yêu cầu chạm tới dữ liệu thì AI tự đọc lại. 30 mail event và SIS là bản chốt, không còn file gốc: AI sẽ hỏi bạn, không tự suy. Nguồn sống nên kiểm lại mỗi tháng một lượt: mở phiên mới và bảo *"đọc lại schema DB trên Lark, đối chiếu với KB 12"*.

---

## 8. Xử lý vấn đề thường gặp

| Tình huống | Cách xử lý |
|---|---|
| AI chọn nhầm intent | Nói *"sai rồi, tôi muốn làm intent X"*, AI chuyển ngay |
| AI hỏi lại câu đã trả lời | Kiểm `decisions.md` và questions file, có thể câu trả lời chưa được ghi |
| Không biết đang ở đâu | `/po-status` |
| AI viết dài, sai trọng tâm | Nhắc thẳng. AI có xu hướng mở rộng phạm vi, cứ kéo về |
| Tài liệu dài, AI bắt đầu sót | Gõ `/compact` rồi gọi lại `/po`, state trên đĩa nên không mất gì |
| Reviewer báo NOT-READY nhưng bạn thấy ổn | Nói rõ finding nào chấp nhận, AI ghi Accepted risk vào `decisions.md` |
| Lead chưa ký HLD Brief | Chờ, hoặc **Accept as-is** kèm lý do; lý do được ghi lại |
| Lark không kết nối được | AI hỏi bạn cấp quyền lại qua browser, việc bình thường |
| Không chụp được màn hình | Gõ `skip-screenshot`, AI để placeholder và liệt kê ảnh còn thiếu |
| Muốn biết AI dựa vào đâu | Hỏi thẳng. Mọi artifact nội bộ có thẻ nguồn và mục nguồn đã đọc |

### Khi AI nói "không chắc"

Đó là hành vi đúng. Workflow ép AI đánh dấu `❓BA` và `Open Question` thay vì đoán. Thấy nhiều `❓BA` nghĩa là yêu cầu còn thiếu thông tin, không phải AI kém.

---

## 9. Git và lead các team

```bash
git pull                      # lấy bản mới nhất trước khi làm
git add .
git commit -m "HLD Brief báo cáo giai đoạn 1, bản chờ ký"
git push
```

Xung đột khi pull thì hỏi AI, đừng tự sửa tay nếu không quen.

### Lead Design, Dev, QA ghi vào HLD Brief

Lead làm trực tiếp trên repo, không cần Claude Code, sửa trên GitHub web cũng được:

1. Pull, mở `.claude/intents/<intent>/inception/hld-brief/hld-brief.md`.
2. Chỉ sửa mục của mình: Design mục 8, Tech mục 9, QA mục 10, và dòng của mình ở mục 12 (Chưa xem, Có ý kiến, Đồng ý, Yêu cầu sửa). Đầu mỗi mục có vài dòng in nghiêng AI gợi ý điểm cần lưu ý cho vai của bạn, trả lời chúng rồi viết định hướng bên dưới. Có ý kiến về mục khác thì ghi ở cuối mục của mình dưới tiêu đề "Ý kiến với mục N".
3. Commit ngay, message `hld(<intent>): design direction` hoặc `tech direction`, `qa direction`. Push.

Lead không mở được repo thì gửi nội dung cho PO. PO dán nguyên văn, mở đầu bằng "(ghi theo tên, ngày)", và lưu tin nhắn xác nhận vào `decisions.md`.

