---
intent: <slug>
phase: <ideation | inception>
date: <YYYY-MM-DD>
result: <Đạt | Không đạt>
---
# Phase check: <IDEATION | INCEPTION> · <slug>

Kiểm ranh giới phase trước khi mở gate cuối của phase. Giữ bảng của phase đang kiểm, xoá bảng kia. Không đạt thì sửa stage tương ứng trước, không mở gate.

## Ideation sang Inception, kiểm ở 1.7
| # | Điều kiện | Kết quả | Chi tiết |
|---|---|---|---|
| 1 | Mọi objective trong intent-statement có ít nhất một hạng mục In scope phục vụ | Đạt / Không đạt | |
| 2 | Mọi Proto-Unit truy về một objective | | |
| 3 | Out of scope không mâu thuẫn In scope | | |
| 4 | Câu hỏi mở có cờ Chặn đã đóng, hoặc chuyển thành assumption có lý do | | |
| 5 | Mọi khối khẳng định có thẻ nguồn | | |

## Inception, kiểm ở 2.42
Phần máy kiểm: chạy `python3 .claude/scripts/po-tools.py trace <intent-dir> --write`, script điền bốn dòng đầu.
| # | Điều kiện | Kết quả | Chi tiết |
|---|---|---|---|
| 1 | Mọi FR có US, hoặc Deferred, N/A có lý do | | |
| 2 | Mọi US truy về FR có thật | | |
| 3 | Mọi US làm đợt này có trong PRD | | |
| 4 | Mọi BR thuộc một US có trong PRD | | |
| 5 | HLD Brief đủ chữ ký, hoặc Accept as-is có DEC (M, L) | | |
| 6 | Conflict trong Impact Matrix đều có DEC | | |
| 7 | Field Intake không còn `❓BA` chưa chuyển thành OQ | | |
| 8 | Câu hỏi mở có cờ Chặn đã đóng | | |

## Kết luận
<Đạt: mở gate. Không đạt: liệt kê stage phải sửa và vì sao.>
