# Glossary

Thuật ngữ và họ mã của PO-Workflow, theo AWS AI-DLC Workflows 2.11, file `docs/guide/glossary.md` của repo `awslabs/aidlc-workflows`. Phần PO-Workflow thêm ngoài AWS gắn nhãn `po-workflow`; đây là nhãn, PO-Workflow không đóng gói theo cơ chế plugin của AWS. Intent chuyển từ luồng cũ giữ họ mã cũ trong tài liệu của chúng.

## Khung
| Thuật ngữ | Nghĩa trong PO-Workflow | Nguồn |
|---|---|---|
| AI-DLC | AI-Driven Development Life Cycle, phương pháp của AWS. PO-Workflow theo phase Ideation và phần Inception do Product Agent dẫn | AWS |
| Space | Toàn bộ repo, một team. Mỗi domain một space, xem DOMAIN-SETUP.md | AWS |
| Intent | Một yêu cầu đi trọn vòng phân tích, có thư mục riêng | AWS. Thay "project" |
| Phase | Ideation, Inception. Construction và Operation ngoài phạm vi | AWS |
| Stage | Một bước có artifact và approval gate riêng, đánh số theo AWS: `1.1`, `2.3`. Stage PO-Workflow thêm mang số thập phân `2.31`, `2.32`, `2.41`, `2.42`, là quy ước riêng của PO-Workflow để chen giữa stage gốc, không đánh lại số stage gốc. Cơ chế plugin của AWS chỉ đánh số sau stage cuối của phase và chưa cho chen trước stage gốc | AWS, số thập phân là của PO-Workflow |
| Plugin stage | Stage PO-Workflow thêm: 2.31, 2.32, 2.41, 2.42. Ghi `po-workflow` ở hàng Plugin trong bảng metadata | Chỉ là nhãn. Plugin thật của AWS là một repo riêng có manifest, chỉ được cộng thêm vào stage gốc; PO-Workflow không đóng gói như vậy, và còn chỉnh hai stage gốc 1.4, 2.4, ghi ở hàng Lệch so với AWS |
| Workflow profile | `S`, `M`, `L`. Tập stage, công tắc nghi thức, depth | AWS gọi là scope trong engine. Không dùng chữ Scope vì đã dùng cho phạm vi tính năng |
| Depth | Minimal, Standard, Comprehensive. Mức chi tiết artifact | AWS |
| Approval gate | Điểm duyệt cuối mỗi stage | AWS. Thay "Gate 1 đến 4" và "điểm dừng" |
| Alignment gate | Gate của 2.41, cần chữ ký của 3 PIC | PO-Workflow |
| Summary confirmation | Xác nhận tóm tắt câu trả lời trước khi sinh artifact | AWS |
| Field Intake | Summary confirmation riêng của 2.42 về field, rule, validate | Repo |
| Questions file | `<stage>-questions.md`, nguồn sự thật của câu trả lời | AWS |
| Answer mode | Guide me, Edit file, Chat | AWS |
| Record dir | `intents/<slug>/` | AWS |
| State file | `state.md` | AWS |
| Decision Log | `decisions.md` | AWS |
| Memory | `memory.md` của intent; `memory/team.md` bài học dùng chung, đi theo engine; `memory/project.md` bài học của sản phẩm đang cài | AWS, cùng cách chia team và project |
| Learnings | Vòng học tại gate | AWS |
| Knowledge | Domain pack ở `domain/` và kiến thức vai PO ở `engine/knowledge/` | AWS |
| Engine | Phần không phụ thuộc sản phẩm: protocol, lệnh, template chung, checklist, agent, script, chuẩn bàn giao | PO-Workflow |
| Domain pack | Toàn bộ phần riêng của sản phẩm: manifest `domain.md`, KB, corner checklist, template công ty. Đổi sản phẩm là thay thư mục này, engine giữ nguyên | PO-Workflow |
| Live source · Pinned record · Last verified | Nguồn sống, bản chốt, ngày đối chiếu của KB | Repo |
| AI Reviewer | Agent `ai-reviewer` review độc lập, không thấy hội thoại, kết luận READY hoặc NOT-READY. Không phải người | AWS gọi vai này là Product Lead |
| Sổ finding | `reviews/findings-<slug>.md`, danh sách finding của một stage và quyết định của PO; finding đã quyết không bị chấm lại | AWS, engine giữ danh sách finding |
| Mã tính năng | `<mã sản phẩm>-F<NNN>`, ví dụ `LMS-F012`. Cấp khi tạo intent, đi theo tính năng tới PRD, story trên Jira, test case, nhánh code | Quy ước chung các team, `engine/standards/id-conventions.md` |
| Story List | `intents/<intent>/stories/story-list-prd-v<phiên bản>.csv`, mỗi US trong PRD một dòng theo mẫu import CSV của Jira. Sinh bằng `/po-stories` sau khi PRD được duyệt; các team làm việc trên story Jira | Quy ước chung các team, `engine/standards/handoff-rules.md`, ADR 0002 |
| Checkpoint | Buổi PO làm việc với Design PIC, Tech PIC, QA PIC trên HLD Brief ở 2.41, trước khi viết PRD | Quy ước chung các team |
| Điều kiện giao Dev, DoR | Điều kiện để giao một story cho Dev: PRD đã duyệt, US có AC, mọi BR có AC, không còn `❓PO` và câu chặn. Kiểm bằng `po-tools.py dor` | Quy ước chung các team; Definition of Ready của AWS |
| Nguyên tắc chia story | Định nghĩa story, tiêu chí INVEST, dấu hiệu quá lớn, 8 cách tách, các cách không chia, ở `engine/standards/story-splitting.md` | PO-Workflow, theo AWS user-story-patterns |
| Tiêu chí chấp nhận, AC | Câu kiểm được, đạt hoặc không đạt, viết theo hành vi người dùng thấy, ghi rõ BR mà nó kiểm. Viết trong PRD ở 2.42, sau khi các PIC đã ký HLD Brief | Quy ước chung các team; ISO/IEC/IEEE 29148 |
| PIC | Người phụ trách một mảng của tính năng: Design PIC, Tech PIC, QA PIC. Ghi định hướng và ký HLD Brief ở 2.41 | PO-Workflow |
| Verification checklist | Checklist tự kiểm của stage cho phần cần phán đoán, mục blocking | AWS gọi là compartment 2 |
| Kiểm bằng máy | `po-tools.py check` và `trace`: phần kiểm được bằng script, chạy trước checklist | Tương đương sensor của AWS |
| Bản chỉ mục cho Dev | `intents/INDEX.md` do `po-tools.py index` sinh: mã tính năng, bản PRD đã duyệt, service bị chạm, tag, số story đạt điều kiện giao Dev | PO-Workflow |
| Tag bản duyệt | `<intent>/prd-v<X.Y>`, gắn mỗi lần PRD hoặc HLD Brief được duyệt; agent của Dev đọc theo tag | PO-Workflow |
| Phiên bản artifact | 0.x là bản nháp; lần duyệt đầu là 1.0; mỗi lần duyệt lại sau change request tăng số phụ | PO-Workflow |
| Mức độ trưởng thành | Quy trình đã sẵn sàng tới đâu, theo 2 trục: phạm vi sử dụng (cá nhân, team, liên team, nhân rộng) và giao tiếp (người với người, người với máy, máy với máy). Đánh giá ở README mục 9 | PO-Workflow |
| Archive | Bản chụp tại gate và trước CR, không sửa | AWS |
| Initiative Brief | Tài liệu chốt hướng một trang, stage 1.7 | AWS. Thay BRD |
| HLD Brief | Tài liệu đồng thuận liên team, stage 2.41 | PO-Workflow |
| Mob, Mob Elaboration | Không dùng làm tên stage hoặc artifact. Hai nghĩa ở AWS: bài blog AI-DLC (Raja SP, 07/2025) gọi Mob Elaboration là cả team người cùng kiểm câu hỏi và đề xuất của AI trong Inception; bản Workflows từ v2.10 gọi mob là chế độ nhiều agent ở stage 2.4 User Stories; từ v2.11 chế độ này mặc định tắt, chỉ bật ở scope `enterprise`. Trong PO-Workflow, 2.41 HLD Brief & Alignment là bản do người thật thực hiện theo nghĩa trong bài blog; mob agent không chạy | AWS, hai nguồn |
| Unit `U` | Hạng mục trong intent backlog, sinh ở stage 1.4, nhóm user story theo giá trị và ưu tiên để chốt phạm vi và thứ tự. Ở 2.4 mỗi US gắn vào một Unit. PRD có mục Units. Unit of work của Dev ở 2.7 chia theo kiến trúc, có thể khác | AWS gọi là proto-Unit, stage 1.4. PO-Workflow gọi gọn là Unit, quyết định ngày 19/10/2026 |
| Thẻ US | Mô tả 9 mục của một user story ở 2.4: vai và mục tiêu, bối cảnh, luồng chính, nhánh đáng kể, rule đã biết, dữ liệu và vùng chạm, ngoài phạm vi, phụ thuộc, chưa rõ. Đủ cho PIC viết HLD, chưa có acceptance criteria | Repo, theo Definition of Ready của AWS |
| Impact Analysis · Solution Options · Hidden · KB · CR · PRD · US · BR | Giữ nguyên | |

## Stage
| Mã | Stage | Artifact chính | Thay cho |
|---|---|---|---|
| 1.1 | Intent Capture & Framing | intent-statement.md | Bước 1 đến 3 phần vấn đề, BRD mục 1 đến 4 |
| 1.2 | Market Research | competitive-analysis.md | Nghiên cứu sản phẩm cùng loại |
| 1.4 | Scope Definition | scope-document.md, có intent backlog gồm các Unit | BRD mục 5 đến 7 |
| 1.7 | Approval & Handoff | initiative-brief.md | BRD, Gate 1 |
| 2.3 | Requirements Analysis | requirements.md | clarified-requirements |
| 2.31 | Impact Analysis | related-features-map.md, impact-matrix.md | Bước 5 và 6, Gate 2 |
| 2.32 | Solution Options | solution-options.md | Bước 7 và 8, Gate 3 |
| 2.4 | User Stories | stories.md | 9A, 9A+ |
| 2.41 | HLD Brief & Alignment | hld-brief.md | mới |
| 2.42 | PRD Generation | prd.md, traceability.md | 9B, 9C, Gate 4 |

Tiện ích:

- `/new-intent`: tạo intent, chọn profile
- `/po`: chạy stage kế tiếp hoặc tiếp tục
- `/po-status`: trạng thái mọi intent, kiểm lệch
- `/po-review`: review độc lập bằng AI Reviewer
- `/po-replay`: kể lại một intent khi bàn giao giữa các PO
- `/po-stories`: sinh Story List để import lên Jira từ PRD đã duyệt, kiểm điều kiện giao Dev
- `/change-request`: đổi yêu cầu sau khi đã duyệt
- `/publish-lark`: đẩy artifact đã duyệt lên Lark
- `/generate-user-guide`: viết User Guide sau khi Dev xong
- `/new-domain`: dựng khung domain pack cho sản phẩm mới
- Script `engine/scripts/po-tools.py`: `next` stage kế tiếp; `check` kiểm bằng máy; `approve` ghi chép sau khi duyệt; `trace` truy vết FR, US, BR, AC; `archive` chụp bản duyệt; `status` kiểm lệch giữa state và file; `feature-id` cấp mã tính năng; `stories` sinh Story List cho Jira; `dor` kiểm điều kiện giao Dev; `index` sinh chỉ mục; `replay` kể lại intent; `migrate` chuyển intent từ bản engine cũ; `doctor` kiểm môi trường

## Họ mã
| Họ | Dạng | Phạm vi | Ví dụ | Thay cho |
|---|---|---|---|---|
| Requirement | `FR1`, `FR1.2`, `NFR1` | intent | FR3 | RC |
| User story | `US1` | intent | US12 | giữ |
| Acceptance criteria | `AC1.1` | intent, số đầu là số US, trong PRD | AC12.2 | mới |
| Business rule | `BR1.1` | intent, số đầu là số US | BR12.3 | BR-12.3 |
| Unit | `U1` | intent | U2 | PU1, trước 19/10/2026 |
| Objective | `O1` | intent | O3 | giữ |
| Câu hỏi | `Q1` | một questions file. Stage khác trích `[2.3 Q4]` | Q4 | OQ, F, BA |
| Câu hỏi mở còn treo | `OQ1` | intent, nằm trong Assumptions & Open Questions | OQ2 | OQ-B, OQ-C |
| Quyết định | `DEC1` | intent | DEC7 | mới |
| Change request | `CR1` | intent | CR2 | CR-001 |
| Finding review | `R-01` | một stage | R-03 | mới |
| Trong Impact Matrix | `CF`, `BI`, `CG`, `TR` | một artifact | CF-2 | giữ |
| KB | `BR-<MODULE>-NN`, `KB-<MODULE>-NN` | KB | | giữ |

Quy tắc: mã đã cấp không đánh lại. Trích mã thì kèm nội dung. Mã đứng liền nhau có dấu `·` ở giữa.

Mã trên là mã ngắn, dùng trong artifact của PO và PRD. Ra ngoài, trên story Jira, test case, nhánh code, mọi team dùng mã đầy đủ có mã tính năng, theo `engine/standards/id-conventions.md`:

| Họ | Mã đầy đủ | Ví dụ | Ai cấp |
|---|---|---|---|
| Tính năng | `<SP>-F<NNN>` | `LMS-F012` | PO, khi tạo intent |
| User story | `US-<tính năng>-<NN>` | `US-LMS-F012-01` | Script đổi từ `US1` |
| Acceptance criteria | `AC-<tính năng>-<NN>.<n>` | `AC-LMS-F012-01.1` | Script đổi từ `AC1.1` |
| Business rule | `BR-<tính năng>-<NN>.<n>` | `BR-LMS-F012-01.2` | Script đổi từ `BR1.2` |
| Câu hỏi trên story Jira | `Q-<tính năng>-<NN>.<n>` | `Q-LMS-F012-01.3` | Người hỏi |
| Màn hình | `SCR-<tính năng>-<NN>` | `SCR-LMS-F012-02` | Design PIC |
| Test case | `TC-<tính năng>-<NN>` | `TC-LMS-F012-01` | QA PIC |

## Ký hiệu
| Ký hiệu | Nghĩa |
|---|---|
| `[ ]` `[-]` `[?]` `[R]` `[x]` `[S]` | Stage chưa làm, đang làm, chờ duyệt, đang sửa, đã duyệt, bỏ qua |
| `❓PO` | Ô không suy được, cần người điền. Không dùng làm dữ kiện |
| `[suy ra]` | AI suy luận ra; nguồn không nói trực tiếp |
| `[đề xuất]` | Đáp án AI đề xuất trong câu hỏi |
| `[uỷ quyền]` | PO để AI chọn |
| `[desc]` `[Q3]` `[KB-04 §3]` `[DEC5]` `[assumption]` | Thẻ nguồn trong artifact nội bộ |

## Cách dùng sai thường gặp
- "Scope" chỉ phạm vi tính năng In, Out, Potential. Cỡ yêu cầu là "profile".
- Story là đơn vị nghiệm thu. Story List giữ nguyên cách chia của 2.4, mỗi US một story; Design chia việc theo màn hình, Dev theo Unit of work, QA theo tiêu chí chấp nhận.
- "Unit" trong PO-Workflow là nhóm user story PO chia ở 1.4, theo giá trị và ưu tiên. "Unit of work" của AWS ở 2.7 là phần việc Dev chia theo ranh giới kỹ thuật. Hai cách chia có thể khác nhau; nói với Dev mà dễ nhầm thì ghi rõ "Unit trong PRD".
- "Extension" là chữ trong nguyên lý 8 của spec 2.0. Tên cơ chế là "plugin"; stage PO-Workflow thêm là "plugin stage".
- "Sensor" là kiểm tự động của AWS; trong repo này là `po-tools.py check` và `trace`. Checklist tự kiểm gọi là "verification checklist".
- "Lead" trong bảng metadata là agent dẫn stage theo AWS. Người phụ trách Design, Tech, QA gọi là PIC.
- "Gate 1" đến "Gate 4" là tên cũ. Gọi theo stage: "gate của 2.3".
- Dữ kiện sản phẩm không ghi vào lệnh hoặc checklist. Ghi vào `domain.md` hoặc KB, để lệnh trỏ tới.
- Mã ngắn `US1`, `AC1.1` chỉ dùng trong tài liệu của PO. Trao đổi với Design, Tech, QA và trên Jira dùng mã đầy đủ `US-<tính năng>-<NN>`.
- "Mob" không phải tên của 2.41. Buổi ký HLD Brief tương đương Mob Elaboration trong bài blog AWS, nhưng tên stage giữ là HLD Brief & Alignment để không trùng chữ mob của AWS ở 2.4.
