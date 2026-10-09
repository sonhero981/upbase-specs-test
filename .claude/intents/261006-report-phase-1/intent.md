---
intent: 261006-report-phase-1
title: Report Phase 1, báo cáo và dashboard bốn chiều
created: 2026-10-06
migrated: 2026-10-09
---
# Intent: Report Phase 1

Dự án bắt đầu ở luồng v1 ngày 06/10/2026, mới qua bước làm rõ yêu cầu; chưa có quyết định nào của PO. Chuyển sang luồng v2 ngày 09/10/2026. Mapping ở cuối file.

## Request
PO yêu cầu *"xây dựng báo cáo và dashboard theo các chiều sau"*: người học · nhóm/quản lý · khoá học · lớp học, tổng 16 chỉ số, nhấn mạnh mỗi chỉ số bấm được sang danh sách người hoặc lớp để xử lý. Đây là dashboard để hành động, không phải báo cáo để đọc. Nguyên văn và ảnh gốc ở `inputs/`.

Vấn đề gốc chưa được nêu; bốn vấn đề AI suy ra chờ PO xác nhận ở `OQ-12`, xem `inception/requirements-analysis/requirements.md` §3. Mục tiêu viết ở Ideation sau khi có đáp án.

## Product boundary
Cả hai portal, theo giả định `A-05` chờ PO xác nhận: UpLMS cho chiều người học và nhóm/quản lý, UpLMS Ops cho chiều khoá học và lớp học. Hai chỉ số nằm ở vùng KB chưa phủ hoặc chưa rõ nghĩa: "buổi chưa xếp lịch" thuộc lịch dạy, "hàng chờ duyệt" chưa rõ luồng nào.

## Related intents
| Intent hoặc dự án cũ | Liên quan ở đâu |
|---|---|
| 261005-group | Chiều nhóm/quản lý trùng phần lớn với `US16` (quản lý theo dõi nhánh) và `US18` (báo cáo cộng dồn theo nhóm) của Group, PRD v0.2 duyệt 09/10/2026. Hai PRD đặc tả cùng một màn thì Dev không biết theo bản nào, xem `OQ-02` |
| 260923-gamification | "Điểm và hạng" ở chiều người học nhiều khả năng là `US1`, `US7` của Gamification, chịu hai công tắc bật tắt, xem `OQ-04` |

## References
| Loại | Nguồn |
|---|---|
| Figma | chưa có |
| Jira Epic / Story | chưa có |
| KB cần đọc | `07-learning-experience.md` · `04-class.md` · `05-grading.md` · `11-dashboard-sis.md` · `15-product-direction.md` (năng lực) · `14-api-surface.md` (vùng lịch dạy chưa phủ) |
| Schema DB | [Lark Data Architecture](https://upbasevn.sg.larksuite.com/wiki/MaFpweI68iKNMvkTioLlJ1uJgQd) |
| Swagger | `uplms-api.staging.upbase.asia/{lms\|ops}/api/v1/docs` |

## Lark
| | |
|---|---|
| Wiki space | `7660816820865093342`, dùng chung với Group và Gamification |
| Node cha chung | `02. Execution — Epics & Features`, token `X3hhwv2MxizpFgkVudVl7e52gUc` |
| Intent node | chưa tạo, tạo trước lần publish đầu |
| Published | initiative-brief: — · hld-brief: — · prd: — |

## Việc còn treo
1. PO xác nhận profile L.
2. 12 câu chặn `OQ-01` đến `OQ-12` trong `inception/requirements-analysis/requirements-analysis-questions.md`; mỗi câu có đề xuất sẵn, trả lời "theo đề xuất" là đủ. Ngoài ra 4 câu không chặn và 7 giả định đang dùng.
3. Phase 1 gồm gì: đề xuất cắt theo phụ thuộc, khoá học, lớp học, người học trước; chiều nhóm/quản lý đi cùng hoặc ngay sau Group (`requirements.md` §8).

## Mapping từ luồng v1
| File v1 | Vị trí v2 | Stage | Ghi chú |
|---|---|---|---|
| `project-context.md`, `project-decisions.md` | `archive/v1/` | — | Log quyết định trống |
| `working/raw-inputs/yeu-cau-goc-20261006.md`, `.png` | `inputs/` | — | |
| `working/ai-drafts/clarified-requirements-20261006.md` | `inception/requirements-analysis/requirements.md` | 2.3 | v0.1 nháp, chứa cả phần Ideation (vấn đề gốc, phạm vi sơ bộ, phân cỡ) |
| `working/open-questions/open-questions-20261006.md` | `inception/requirements-analysis/requirements-analysis-questions.md` | 2.3 | 12 câu chặn chưa trả lời |

Họ mã giữ theo v1 tới khi Ideation chạy: `OQ`, `A`, requirement ứng viên theo mục. Khi chạy 1.1 và 1.4 ở v2 thì dùng mã v2 (`FR`, `PU`, `OQ1`).
