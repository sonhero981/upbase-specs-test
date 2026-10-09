# Glossary

Thuật ngữ và họ mã của po-workflow-upbase, chuẩn theo AWS AI-DLC Workflows v2.10, file `docs/guide/glossary.md` của repo `awslabs/aidlc-workflows`. Phần repo thêm ngoài AWS đóng gói thành plugin `upbase-po`, theo đúng cách AWS cho phép thêm stage. Áp cho intent trong `.claude/intents/`. Dự án cũ trong `.claude/projects/` giữ thuật ngữ cũ tới khi xong.

## Khung
| Thuật ngữ | Nghĩa ở đây | Nguồn |
|---|---|---|
| AI-DLC | AI-Driven Development Life Cycle, phương pháp của AWS. Repo này theo phase Ideation và phần Inception do Product Agent dẫn | AWS |
| Space | Toàn bộ repo, một team | AWS |
| Intent | Một yêu cầu đi trọn vòng phân tích, có thư mục riêng | AWS. Thay "project" |
| Phase | Ideation, Inception. Construction và Operation ngoài phạm vi | AWS |
| Stage | Một bước có artifact và approval gate riêng, đánh số theo AWS: `1.1`, `2.3`. Stage repo thêm mang số thập phân `2.31`, `2.32`, `2.41`, `2.42`, là số gợi ý thứ tự theo quy ước plugin của AWS, không đánh lại số stage gốc | AWS |
| Plugin stage | Stage repo thêm, gói trong plugin `upbase-po`: 2.31, 2.32, 2.41, 2.42. Ghi `plugin: upbase-po` trong metadata | AWS gọi gói stage thêm vào là plugin. Ta không có bước compose, nên đây là quy ước ghi nhãn |
| Workflow profile | `S`, `M`, `L`. Tập stage, công tắc nghi thức, depth | AWS gọi là scope trong engine. Không dùng chữ Scope vì đã dùng cho phạm vi tính năng |
| Depth | Minimal, Standard, Comprehensive. Mức chi tiết artifact | AWS |
| Approval gate | Điểm duyệt cuối mỗi stage | AWS. Thay "Gate 1 đến 4" và "điểm dừng" |
| Alignment gate | Gate của 2.41, cần sign-off ba lead | Plugin `upbase-po` |
| Summary confirmation | Xác nhận tóm tắt câu trả lời trước khi sinh artifact | AWS |
| Field Intake | Summary confirmation riêng của 2.42 về field, rule, validate | Repo |
| Questions file | `<stage>-questions.md`, nguồn sự thật của câu trả lời | AWS |
| Answer mode | Guide me, Edit file, Chat | AWS |
| Record dir | `.claude/intents/<slug>/` | AWS |
| State file | `state.md` | AWS |
| Decision Log | `decisions.md` | AWS |
| Memory | `memory.md` của intent, `.claude/memory/team.md` của repo | AWS |
| Learnings | Vòng học tại gate | AWS |
| Knowledge | KB sản phẩm, hiện ở `.claude/knowledge/domain/`, và kiến thức vai PO | AWS |
| Live source · Pinned record · Last verified | Nguồn sống, bản chốt, ngày đối chiếu của KB | Repo |
| Product Lead review | Review độc lập, READY hoặc NOT-READY | AWS |
| Verification checklist | Checklist tự kiểm của stage, mục blocking | AWS gọi là compartment 2. Không gọi là Sensor, Sensor là script |
| Archive | Bản chụp tại gate và trước CR, không sửa | AWS |
| Initiative Brief | Tài liệu chốt hướng một trang, stage 1.7 | AWS. Thay BRD |
| HLD Brief | Tài liệu đồng thuận liên team, stage 2.41 | Plugin `upbase-po` |
| Proto-Unit `PU` | Hạng mục trong intent backlog, sinh ở stage 1.4, ứng viên để Dev chia Unit thật ở stage 2.7. Ở 2.4 mỗi US gắn vào một Proto-Unit | AWS, stage 1.4 Scope Definition. Thay Unit, tránh trùng `U1` Dev sinh ở 2.7 |
| Impact Analysis · Solution Options · Hidden · KB · CR · PRD · US · BR | Giữ nguyên | |

## Stage
| Mã | Stage | Artifact chính | Thay cho |
|---|---|---|---|
| 1.1 | Intent Capture & Framing | intent-statement.md | Bước 1 đến 3 phần vấn đề, BRD mục 1 đến 4 |
| 1.2 | Market Research | competitive-analysis.md | Nghiên cứu LMS khác |
| 1.4 | Scope Definition | scope-document.md, có intent backlog gồm các Proto-Unit | BRD mục 5 đến 7 |
| 1.7 | Approval & Handoff | initiative-brief.md | BRD, Gate 1 |
| 2.3 | Requirements Analysis | requirements.md | clarified-requirements |
| 2.31 | Impact Analysis | related-features-map.md, impact-matrix.md | Bước 5 và 6, Gate 2 |
| 2.32 | Solution Options | solution-options.md | Bước 7 và 8, Gate 3 |
| 2.4 | User Stories | stories.md | 9A, 9A+ |
| 2.41 | HLD Brief & Alignment | hld-brief.md | mới |
| 2.42 | PRD Generation | prd.md, traceability.md | 9B, 9C, Gate 4 |

Tiện ích: `/new-intent`, `/po`, `/po-status`, `/po-review`, `/change-request`, `/publish-lark`, `/user-guide`, `/kb-sync`. Script: `.claude/scripts/po-tools.py` với `trace` (truy vết FR, US, BR), `archive` (chụp bản duyệt), `status` (kiểm lệch state và đĩa).

## Họ mã
| Họ | Dạng | Phạm vi | Ví dụ | Thay cho |
|---|---|---|---|---|
| Requirement | `FR1`, `FR1.2`, `NFR1` | intent | FR3 | RC |
| User story | `US1` | intent | US12 | giữ |
| Business rule | `BR1.1` | intent, số đầu là số US | BR12.3 | BR-12.3 |
| Proto-Unit | `PU1` | intent | PU2 | U1 |
| Objective | `O1` | intent | O3 | giữ |
| Câu hỏi | `Q1` | một questions file. Stage khác trích `[2.3 Q4]` | Q4 | OQ, F, BA |
| Câu hỏi mở còn treo | `OQ1` | intent, nằm trong Assumptions & Open Questions | OQ2 | OQ-B, OQ-C |
| Quyết định | `DEC1` | intent | DEC7 | mới |
| Change request | `CR1` | intent | CR2 | CR-001 |
| Finding review | `R-01` | một stage | R-03 | mới |
| Trong Impact Matrix | `CF`, `BI`, `CG`, `TR` | một artifact | CF-2 | giữ |
| KB | `BR-COURSE-01`, `KB-CLASS-03` | KB | | giữ |

Quy tắc: mã đã cấp không đánh lại. Trích mã thì kèm nội dung. Mã đứng liền nhau có dấu `·` ở giữa.

## Ký hiệu
| Ký hiệu | Nghĩa |
|---|---|
| `[ ]` `[-]` `[?]` `[R]` `[x]` `[S]` | Stage chưa làm, đang làm, chờ duyệt, đang sửa, đã duyệt, bỏ qua |
| `❓BA` | Ô không suy được, cần người điền. Không dùng làm dữ kiện |
| `[suy ra]` | AI suy luận, không phải câu chữ trực tiếp |
| `[đề xuất]` | Đáp án AI đề xuất trong câu hỏi |
| `[uỷ quyền]` | PO để AI chọn |
| `[desc]` `[Q3]` `[KB-04 §3]` `[DEC5]` `[assumption]` | Thẻ nguồn trong artifact nội bộ |

## Dùng sai hay gặp
- "Scope" chỉ phạm vi tính năng In, Out, Potential. Cỡ yêu cầu là "profile".
- "Unit" là của Dev ở stage 2.7. PO viết "Proto-Unit", sinh ở 1.4.
- "Extension" là chữ trong nguyên lý 8 của spec 2.0. Tên cơ chế là "plugin"; stage ta thêm là "plugin stage".
- "Sensor" là script kiểm tự động. Checklist tự kiểm gọi là "verification checklist".
- "Bolt", "swarm", "walking skeleton" không dùng.
- "Gate 1" đến "Gate 4" là tên cũ. Gọi theo stage: "gate của 2.3".
