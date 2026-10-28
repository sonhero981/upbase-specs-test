---
intent: <slug>
artifact: test-cases
version: 0.1
status: draft
prd_version: <x.y>
hld_version: <x.y>
---
# Test Cases: <Tên tính năng>

Mỗi test case trỏ về US và dòng AC (`USn-ACk`) hoặc BR nó kiểm. Bolt nhận test case qua cột US ở `bolt-plan.md`. TC hồi quy không thuộc US nào ghi `REG` ở cột US.

| TC | US | AC / BR | Tiền điều kiện + dữ liệu | Bước | Kết quả mong đợi | Loại | Ưu tiên |
|---|---|---|---|---|---|---|---|
| TC-1 | US1 | US1-AC1 · BR-1.1 | | | | Happy / Edge / Negative / Regression | P0 / P1 / P2 |

## Hồi quy
| Vùng | Lý do | TC |
|---|---|---|

## Dữ liệu và môi trường
<Tài khoản, tenant, dữ liệu mẫu cần có sẵn.>

## Góc đã quét không áp dụng
<Mục của corner checklist đã xét mà không thành TC, kèm lý do một dòng.>

## Nguồn thay thế đã dùng
<Intent v1: không có HLD Brief mục 10, … Không có thì bỏ mục.>

## Assumptions & Open Questions
| # | Nội dung | Loại | Chặn | Owner |
|---|---|---|---|---|

## Sign-off
| Vai trò | Tên | Trạng thái | Ngày |
|---|---|---|---|
| QA lead | | | |
