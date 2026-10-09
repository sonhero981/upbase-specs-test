---
intent: 260923-gamification
title: Gamification, điểm, huy hiệu, hạng và bảng xếp hạng
created: 2026-09-23
migrated: 2026-10-09
---
# Intent: Gamification

Dự án chạy luồng v1 từ 23/09/2026: bốn gate qua trong ngày đầu, PRD v0.2 duyệt 23/09, rồi 13 change request. Đang ở CR-013 (gộp CR-012) chạy lại từ BRD, bốn gate chờ PO duyệt lại. Chuyển sang luồng v2 ngày 09/10/2026; artifact giữ nguyên nội dung và họ mã v1, chỉ đổi chỗ, thêm frontmatter. File này thay cho `project-context.md` đã viết lại sau CR-007; bản gốc ở `archive/v1/`. Mapping ở cuối file.

## Request
Số liệu General Launch 8/9 đến 21/9/2026 cho thấy vấn đề ở ba tầng: không mở ứng dụng (activation 40,2%, tiêu chí 80%), mở rồi không học (45% người đăng nhập không bắt đầu), bắt đầu rồi bỏ dở (completion 64,1%, tiêu chí 80%). Yêu cầu gốc ở `inputs/yeu-cau-goc-20260923.md`.

Năm mục tiêu: `O1` học viên quay lại học đều, không cần nhắc thủ công · `O2` nỗ lực học được ghi nhận ngay · `O3` có mốc ngắn hạn để nhắm tới · `O4` đội truyền thông nội bộ có kết quả để công bố, qua campaign đóng băng và số liệu khoảng ngày bất kỳ bên Ops · `O5` điểm số đáng tin, truy được nguồn, không thổi bằng thao tác đối phó. Mã mục tiêu đánh số lại ngày 24/09 sau CR-007; `decisions.md` ghi chú chỗ lệch.

Phạm vi 18 user story cộng US19 đến US21 campaign (CR-013): cơ chế điểm, ba hành động học, check-in hằng ngày tăng theo chuỗi, huy hiệu bốn loại, bật tắt, hạng không tụt, chống cày điểm, lịch sử ghi nhận, thông báo thành tích, trang Thành tích, bảng xếp hạng năm khung cố định và năm bảng, campaign, tra cứu bên Ops, hai công tắc, trang cấu hình Ops tự lưu, múi giờ theo tenant, phân quyền. Out of scope và lý do: xem `ideation/brd.md` và mục Out of scope của PRD.

## Product boundary
UpLMS: trang thành tích, lịch sử, bảng xếp hạng, thông báo; My Learning bị sửa để hiện điểm và hạng. UpLMS Ops: cấu hình điểm, huy hiệu, hạng, hai công tắc, phân quyền. Module bị chạm: Learning Experience, Course, Assessment, Grading, Certificate, User, Class, phân quyền, tenant.

Ràng buộc: `C1` cấu hình gắn `tenant_id` · `C2` danh mục mở rộng bằng cấu hình · `C3` lưu từng lần cộng điểm kèm thời điểm · `C4` đổi cấu hình áp từ thời điểm đổi, không tính lại quá khứ · `C5` chống cộng trùng trong một lượt ghi danh · `C6` `C9` biên ngày theo múi giờ tổ chức · `C7` một lần cộng điểm thuộc mọi khoảng bao trùm nó · `C8` mốc xếp hạng lưu thời điểm đạt · `C10` Test Account bị loại khỏi toàn bộ logic · `NFR-GAM-01` lỗi gamification không làm hỏng thao tác học. Ba cơ chế cùng một luật: điểm, huy hiệu, hạng chỉ áp thay đổi từ thời điểm đổi, không có gì bị lấy lại.

Quyết định giải pháp đã chốt: tính trong luồng, độ trễ bằng 0 · bảng xếp hạng tính sẵn chu kỳ 8 tiếng, không có phép tính theo yêu cầu học viên · check-in ghi lúc vào hệ thống lần đầu trong ngày · lưu cấu hình Ops khi rời ô hoặc bấm Enter, cơ chế do Dev quyết · campaign tính sẵn cùng chu kỳ, đóng băng bằng tác vụ riêng, chờ Gate 3 (`OQ-44`).

## Related intents
| Intent hoặc dự án cũ | Liên quan ở đâu |
|---|---|
| 261005-group | `US16` của Gamification, bộ lọc bảng xếp hạng theo nhóm, lớp, phòng ban, hoãn chờ chức năng nhóm đồng bộ từ HRM. `CR-001` của dự án này là nơi phân biệt Nhóm với Lớp |
| 261006-report-phase-1 | "Điểm và hạng" ở chiều người học của báo cáo nhiều khả năng dùng lại `US1`, `US7` |

## References
| Loại | Nguồn |
|---|---|
| Figma | chưa có |
| Jira Epic / Story | chưa có |
| Design đã chốt | `design/` tám ảnh màn, `order.txt` liệt kê bảy ảnh chèn vào mục Design của PRD theo thứ tự; ảnh "Thông báo thành tích" chưa có trong order.txt |
| KB cần đọc | `03-assessment.md` (`BR-TEST`) · `06-user-account.md` §8b (Test Account) · `07-learning-experience.md` · `12-data-model.md` · `14-api-surface.md` · `15-product-direction.md` |
| Schema DB | [Lark Data Architecture](https://upbasevn.sg.larksuite.com/wiki/MaFpweI68iKNMvkTioLlJ1uJgQd), đối chiếu 23/09/2026 |
| Swagger | `uplms-api.staging.upbase.asia/{lms\|ops}/api/v1/docs`, tên miền mới từ 05/10/2026 |

## Lark
| | |
|---|---|
| Wiki space | `7660816820865093342` |
| Node cha chung | `02. Execution — Epics & Features`, token `X3hhwv2MxizpFgkVudVl7e52gUc` |
| Intent node | `Gamification`, token `LRVgwz5L9imG6WkQvJdllro5gNd` |
| Published | initiative-brief: — · hld-brief: — · prd: **v0.8** trên Lark ngày 05/10/2026, doc `KeT8dkIStofZ0axlTW5l4S94gre`, https://upbasevn.sg.larksuite.com/docx/KeT8dkIStofZ0axlTW5l4S94gre; bản v0.2 duyệt Gate 4 giữ ở node `J4NGwHIlmijgZBkqxpWlNS4qgxe` để đối chiếu |

Publish lại: dùng `lark-cli docs +update --command overwrite` vào doc v0.8, giữ tên trên Lark; sáu sơ đồ Mermaid tự thành bảng trắng; **ảnh design phải chèn lại** bằng `.claude/scripts/lark-insert-design-images.py` theo `design/order.txt` vì ảnh không nằm trong file `.md`.

## Việc còn treo
1. Bốn gate chờ PO duyệt lại sau CR-013: `brd.md` v0.7, `impact-matrix.md` v0.3, `solution-options.md` v0.2, `prd.md` v0.10.
2. `OQ-42` đến `OQ-45` về campaign ở mục Vấn đề tồn đọng của PRD: tắt Gamification khi campaign đang chạy; các mục `[đề xuất]` ở `US19` đến `US21`; cách tính bảng campaign; design cho campaign.
3. Lark đang v0.8, publish lại sau khi duyệt, kèm chèn ảnh.
4. Designer, Tech lead, QA, Jira trống. Stage 2.41 HLD Brief chưa chạy; nên chạy trước khi bàn giao Dev vì dự án từng sinh bốn CR sau PRD do lệch design và tech.

## Mapping từ luồng v1
| File v1 | Vị trí v2 | Stage | Ghi chú |
|---|---|---|---|
| `project-context.md`, `project-decisions.md` | `archive/v1/` | — | Bản gốc không sửa. `decisions.md` chuyển từ log cũ |
| `working/raw-inputs/yeu-cau-goc-20260923.md` | `inputs/` | — | |
| `working/raw-inputs/change-requests.md` | `inputs/change-requests.md` | — | Phân tích chi tiết CR-001 đến CR-013; bảng tóm tắt ở `decisions.md` |
| `design/*.png`, `order.txt` | `design/` | — | |
| `docs/brd/brd-v0.7-20261008.md` | `ideation/brd.md` | 1.1, 1.4, 1.7 | v0.1 đến v0.6 ở `archive/approval-handoff/`, v0.6 là bản Gate 1 duyệt |
| `working/ai-drafts/clarified-requirements-20260923.md` | `inception/requirements-analysis/requirements.md` | 2.3 | Không có mã RC; không cập nhật sau CR |
| `working/open-questions/open-questions-20260923.md` | `inception/requirements-analysis/requirements-analysis-questions.md` | 2.3 | 16 câu, `OQ-A`, `OQ-B` |
| `working/impact-analysis/related-map-v0.2-20260923.md` | `inception/impact-analysis/related-features-map.md` | 2.31 | v0.1 ở archive |
| `working/impact-analysis/impact-matrix-v0.3-20261008.md` | `inception/impact-analysis/impact-matrix.md` | 2.31 | v0.1, v0.2 ở archive; v0.2 là bản Gate 2 duyệt |
| `working/solution-options/solution-comparison-v0.2-20261008.md` | `inception/solution-options/solution-options.md` | 2.32 | v0.1 ở archive; v0.1 là bản Gate 3 duyệt |
| PRD §Danh sách user story và §Unit | trong `inception/prd/prd.md` | 2.4 | `U1` đến `U5` giữ tên Unit |
| không có | — | 2.41 | Stage chưa tồn tại khi chạy v1 |
| `docs/prd/prd-gamification-v0.10-20261008.md` | `inception/prd/prd.md` | 2.42 | Bản v0.2 duyệt Gate 4 không còn trên đĩa, chỉ còn trên Lark node `J4NGwHIlmijgZBkqxpWlNS4qgxe` |

Họ mã giữ theo v1: `A`, `N`, `C`, `OQ`, `OQ-A`, `OQ-B`, `CF`, `BI`, `U`, `BR-<US>.<n>`, `BR-TEST`, `NFR-GAM`, `CR-0xx`.
