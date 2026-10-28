---
intent: <slug>
status: Running
---
# Tech state: <slug>

| | |
|---|---|
| PRD dùng | `inception/prd/prd.md` version <x.y>, commit <hash> |
| Tech Design 1 | `inception/tech-design/tech-design.md` version <x.y> · Decision Brief đã ký <YYYY-MM-DD> |
| Phạm vi đợt này | <mặc định: cả intent; lát nhỏ ghi danh sách US + lý do (DEC-T)> |
| Tech lead tác giả | <FE lead hoặc BE lead, tên> |
| FE lead | <tên> |
| BE lead | <tên> |
| QA lead | <tên> |
| Dev code (owner Bolt) | <tên người 1>, <tên người 2> |

## Inception
Ký hiệu: `[ ]` chưa làm · `[-]` đang làm · `[?]` chờ duyệt · `[R]` đang sửa · `[x]` đã duyệt · `[S]` bỏ qua kèm lý do

- [ ] 2.1 reverse-engineering
- [ ] 2.6 domain-design
- [ ] 2.7 units-generation
- [ ] 2.8 contract-design
- [ ] 2.81 test-cases
- [ ] 2.9 delivery-planning

## Construction
| Bolt | Unit | 3.1 functional | 3.2 nfr-req | 3.3 nfr-design | 3.4 infra | 3.41 ui-map | 3.5 code-gen | 3.6 build-test | Owner | Change |
|---|---|---|---|---|---|---|---|---|---|---|

Trạng thái Bolt: Dự kiến · Thiết kế · Plan duyệt · Đang code · Chờ demo · Xong.

## Quyết định
Ghi vào `decisions.md` ở gốc intent, mã `DEC-T<n>`, cột *Read when* ghi stage Tech. Không mở sổ riêng.

## Current
| | |
|---|---|
| Stage | <mã slug> |
| Next action | <ai làm gì> |
| Chờ PO | <none / điểm còn mở trong Decision Brief> |

## Ghi chú cho PO
<Câu hỏi để sau, chỗ code lệch KB domain.>

## Log
- <YYYY-MM-DD> <việc>
