---
description: Viết User Guide cho người dùng cuối từ PRD đã duyệt, sau khi tính năng đã phát triển xong
argument-hint: <intent-slug>
---
# /generate-user-guide

Mắt xích cuối: yêu cầu, PRD, Dev làm xong, User Guide. Mô tả cái đang chạy, không mô tả cái sắp có; tính năng chưa dev xong thì dừng.

Xác định intent từ `$ARGUMENTS`; thiếu thì hỏi. Đọc theo thứ tự: `inception/prd/prd.md` bản approved; `.claude/knowledge/domain/` cho cách các module liên quan đang được mô tả; `.claude/templates/user-guide.md`.

## Nơi User Guide sống
| Repo GitBook | Đối tượng | Đường dẫn |
|---|---|---|
| `uplms` | Học viên | `LMS/User Guide/uplms/` |
| `uplms-ops` | Vận hành | `LMS/User Guide/uplms-ops/` |

Tính năng chạm cả hai thì viết hai bài riêng, hậu tố `-student` và `-ops`. Học viên và vận hành cần thông tin khác nhau.

## Cấu trúc bài viết
Theo template, đúng chuẩn 57 page hiện có: I. Thông tin chung với khối `Dành cho`, `Đường dẫn`, `Phạm vi & Module liên quan`, `Điều kiện tiên quyết` · II. Hướng dẫn chi tiết theo `{% stepper %}` · III. Lưu ý và quy tắc nghiệp vụ · IV. Lỗi thường gặp và cách xử lý. Mục `Phạm vi & Module liên quan` bắt buộc: 13 page cũ thiếu nó theo cụm, KB không dựng được quan hệ chéo và Impact Analysis bỏ sót đúng chỗ dày quan hệ nhất.

## Chuyển PRD sang User Guide
| PRD | User Guide |
|---|---|
| Scenario | §II các bước thao tác |
| Pre-Condition | §I Điều kiện tiên quyết |
| Business rule | §III Lưu ý và quy tắc nghiệp vụ |
| Bảng UI: validate, disable, tooltip | §IV Lỗi thường gặp |
| Out of scope | Không đưa vào |
| Conner case do QA điền | §IV nếu là tình huống người dùng gặp thật |

Đổi giọng: PRD viết cho Dev và QA, User Guide viết cho người dùng cuối. *"Field `status` disable khi `class.type = Foundation`"* thành *"Không đổi được trạng thái với lớp Foundation"*. Bỏ hết tên bảng, tên field kỹ thuật, endpoint, mã rule.

## Ảnh màn hình
Có Playwright MCP: chạy headless, viewport 1920×1080, đăng nhập bằng tài khoản test PO cung cấp, chụp theo từng bước của §II, lưu về `user-guide/screenshots/` trong intent với tên `NN-<role>-<mô-tả-ngắn>.png`, kiểm ảnh đạt khoảng 1920px và layout giống desktop thật. Ảnh trong thư mục tạm của Playwright không phải output. Không có Playwright hoặc PO gõ `skip-screenshot`: chèn `<!-- ẢNH: mô tả cảnh cần chụp -->` và liệt kê ảnh còn thiếu vào `user-guide/pending-screenshots.md`.

## Output
`user-guide/<slug>-<role>.md` trong intent. Tự kiểm theo `.claude/verification/generate-user-guide.md`.

## Sau khi viết xong
1. Trình PO review. Duyệt xong hỏi có đưa vào GitBook repo tương ứng không.
2. Cập nhật ngược KB trong `.claude/knowledge/domain/`: business rule mới, field đổi, quan hệ module mới, mã `KB-*` và ghi nguồn là PRD nào. Không làm thì KB đứng yên trong khi sản phẩm chạy tiếp.
3. Ghi dòng Log vào `state.md` của intent.
