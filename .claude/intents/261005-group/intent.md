---
intent: 261005-group
title: Nhóm học viên (Group)
created: 2026-10-05
migrated: 2026-10-09
---
# Intent: Nhóm học viên (Group)

Dự án chạy luồng v1 từ 05/10 đến 06/10/2026, PRD đã duyệt và đã publish Lark. Chuyển sang luồng v2 ngày 09/10/2026 làm thí điểm. Artifact giữ nguyên nội dung và họ mã của v1; chỉ đổi chỗ, thêm frontmatter và chụp archive. Bảng mapping ở cuối file.

## Request
PO đưa yêu cầu ngày 05/10/2026 dạng bảng 19 hạng mục, hai nhóm `Group` và `User Group Relationship`, mục đích nguyên văn: *"mục đích là tổ chức các nhóm học tập, để gán theo dõi đánh giá theo từng nhóm"*. Nguyên văn ở `inputs/yeu-cau-goc-20261005.md`.

Đóng khung đã chốt: đây là chức năng **Nhóm**, không phải cây tổ chức. Cây tổ chức đồng bộ từ HRM (Lark) chỉ là một nguồn tạo nhóm; nhóm tự tạo là nguồn thứ hai. Nhóm gắn **người**, Lớp gắn **nội dung**; gán nội dung cho nhóm là luật đứng dẫn người vào Lớp. Không có nền để kế thừa: `Group Management` và Recipients List hiện có bị bỏ, coi như chưa có gì (DEC về `BA-01`).

Năm mục tiêu: `O1` giao nội dung cho một tập người ổn định · `O2` người mới vào tự nhận nội dung đã giao · `O3` quản lý xem tiến độ người mình phụ trách · `O4` số liệu cộng dồn theo cơ cấu · `O5` dựng lại được ai thuộc nhóm nào tại một thời điểm quá khứ.

## Product boundary
Cả hai portal, phần lớn việc ở **UpLMS Ops** (dựng nhóm, thành viên, đồng bộ HRM, gán nội dung, quản lý, nhật ký, lưu trữ, báo cáo). **UpLMS** chỉ có `US17`, học viên xem quản lý của mình. Màn theo dõi nhánh `US16` nằm ở Ops, chốt ngày 09/10/2026 theo CR1; bảng phạm vi cũ của v1 từng xếp nhầm nó vào UpLMS.

Tenant: làm cho UpBase, dữ liệu và hạ tầng cho mọi tenant. Số cấp tối đa của cây mặc định 6, cấu hình được theo tổ chức. Đã kiểm chiều tenant ở Impact Matrix §9.

## Related intents
| Intent hoặc dự án cũ | Liên quan ở đâu |
|---|---|
| 260923-gamification | Chuyển sang v2 ngày 09/10/2026. `US16` của Gamification, bộ lọc bảng xếp hạng theo nhóm, chờ chức năng này. `CR-001` của Gamification là nơi hai khái niệm Nhóm và Lớp từng bị lẫn |
| 261006-report-phase-1 | Chuyển sang v2 ngày 09/10/2026. Tham chiếu PRD này ở `US16` và `US18` |

## References
| Loại | Nguồn |
|---|---|
| Figma | chưa có |
| Jira Epic / Story | chưa có |
| KB cần đọc | `04-class.md` (phân biệt với Lớp) · `06-user-account.md` · `12-data-model.md` · `14-api-surface.md` · `16-domain-principles.md` nguyên tắc 6, ranh giới Nhóm với Lớp |
| Schema DB | [Lark Data Architecture](https://upbasevn.sg.larksuite.com/wiki/MaFpweI68iKNMvkTioLlJ1uJgQd), đã đối chiếu 05/10/2026 |
| Swagger | `uplms-api.staging.upbase.asia/{lms\|ops}/api/v1/docs`, tên miền mới từ 05/10/2026; hai host cũ `lms-be`, `ops-be` đã bỏ |
| Dữ liệu HRM | `inputs/lark-users-by-department.csv`: 384 nhân sự, 53 phòng ban, cây sâu 4 cấp, đã cắt 16 cột cá nhân |
| Nghiên cứu LMS khác | `ideation/market-research/competitive-analysis.md` v0.2 (TalentLMS, Docebo, Moodle, mô hình tích hợp HRIS, bốn bài TalentLMS) và trích nguyên văn ở `inputs/talentlms-help-articles-20261007.md` |

> ⚠️ KB chưa phủ vùng phòng ban và phân quyền, xem `14-api-surface.md` §1 và §2. Nhiều câu về nhóm phải hỏi PO hoặc Dev.

## Lark
| | |
|---|---|
| Wiki space | `7660816820865093342` |
| Node cha chung | `02. Execution — Epics & Features`, token `X3hhwv2MxizpFgkVudVl7e52gUc` |
| Intent node | `Group`, token `FwwEwV4V7ilx77k6LColwj3OgDf` |
| Published | initiative-brief: — · hld-brief: — · prd: **v0.2** (09/10/2026, revision 31, cập nhật đúng doc cũ bằng `lark-cli docs +update --command overwrite`; v0.1 publish 06/10/2026); tên trên Lark `[PRD] Group` (hồ sơ v1 ghi `[PRD] Study Group`, đã được đổi trên Lark trước 09/10; publish lại không đổi tên), node `UAIEw1tKfirmt3kUicZle3NTgfd`, doc `Jg7ld8UCzoeMiAxW5ielxlC4gGg`, https://upbasevn.sg.larksuite.com/docx/Jg7ld8UCzoeMiAxW5ielxlC4gGg, publish 06/10/2026 |

Tên trên Lark khác tên file (`[PRD] Nhóm học viên`): lần publish sau giữ tên trên Lark, chỉ cập nhật nội dung. Đối chiếu sau publish 09/10 (v0.2, revision 31): heading 14/32/124/52, 46 bảng, 306 dòng bảng, 209 gạch đầu dòng khớp file; 4 bảng trắng, không còn code block sơ đồ. Lần 06/10 (v0.1): 2.326 block, heading 14/32/124/51, 45 bảng, 205 gạch đầu dòng.

## Việc còn treo
1. ~~`competitive-analysis.md` v0.2 §9.2, ba điểm chờ PO xem~~ Đã quyết 09/10/2026, CR1: `US16` ở Ops · thêm `MAIL-GRP-02` · câu cảnh báo trong `MAIL-GRP-01`. Duyệt lại và publish PRD v0.2 cùng ngày.
2. PRD chưa có Designer, Tech lead, QA. Stage 2.41 HLD Brief chưa chạy vì chưa tồn tại khi làm v1; chạy bổ sung nếu cần họp bàn giao trước khi Dev bắt đầu.
3. Jira Epic và Story trống. User Guide viết sau khi Dev xong, qua `/generate-user-guide`.

## Mapping từ luồng v1
| File v1 | Vị trí v2 | Stage | Ghi chú |
|---|---|---|---|
| `project-context.md` | `archive/v1/project-context.md`, nội dung sống chuyển vào file này | — | Bản gốc không sửa |
| `project-decisions.md` | `archive/v1/project-decisions.md`, chuyển thành `decisions.md` 71 dòng DEC, gồm hai dòng bổ sung cho Gate 1 và 9A mà v1 không ghi thành dòng | — | Cột Stage ghi stage v2 kèm bước v1 |
| `working/raw-inputs/*` | `inputs/` | — | Yêu cầu gốc, CSV HRM, trích bài TalentLMS |
| `docs/brd/brd-v0.2-20261006.md` | `ideation/brd.md` | 1.1, 1.4, 1.7 | BRD gộp cả ba stage Ideation của v2; không có bản một trang. Gate 1 duyệt 05/10, v0.2 gộp quyết định tới Bước 7 |
| `working/ai-drafts/nghien-cuu-lms-khac-v0.2-20261007.md` | `ideation/market-research/competitive-analysis.md` | 1.2 | v0.1 ở `archive/market-research/` |
| `working/ai-drafts/clarified-requirements-20261005.md` | `inception/requirements-analysis/requirements.md` | 2.3 | Mã `RC-01` đến `RC-19`, không đổi sang FR |
| `working/open-questions/open-questions-20261005.md` | `inception/requirements-analysis/requirements-analysis-questions.md` | 2.3 | Mã `OQ-xx`, `BA-xx`, đóng hết |
| `working/impact-analysis/related-features-map-20261005.md` | `inception/impact-analysis/related-features-map.md` | 2.31 | PO chốt Bước 5, 05/10 |
| `working/impact-analysis/impact-matrix-v0.2-20261006.md` | `inception/impact-analysis/impact-matrix.md` | 2.31 | Gate 2 duyệt 06/10, 6 conflict đã quyết |
| không có | — | 2.32 | v1 không làm so sánh phương án; Bước 7 dùng để chốt nhóm câu hỏi D |
| PRD §Danh sách user story và §Unit | trong `inception/prd/prd.md` | 2.4 | 20 US chốt ở 9A ngày 06/10; `U1` đến `U7` giữ tên Unit, tương đương Proto-Unit |
| không có | — | 2.41 | Stage chưa tồn tại khi chạy v1 |
| `working/field-intake-20261006.md` | `inception/prd/field-intake-questions.md` | 2.42 | 13 câu `F-xx`, đã đóng |
| `docs/prd/prd-group-v0.1-20261006.md` | `inception/prd/prd.md` | 2.42 | Gate 4 duyệt 06/10, publish Lark 06/10. Mục tên cũ: Preferences, TDD, Dữ liệu phải lưu, Unit, Vấn đề tồn đọng |
| bản đã duyệt | `archive/<stage>/<artifact>-v<N>-<ngày duyệt>.md` | — | Chụp lúc migration từ nội dung đã duyệt |

Họ mã giữ theo v1 cho intent này: `RC`, `OQ`, `BA`, `F`, `CF`, `BI`, `U`, `BR-<US>.<n>`, `MAIL-GRP`. Script `po-tools.py trace` không áp dụng vì không có bảng FR; truy vết làm tay khi có CR.
