---
description: Tạo intent mới theo luồng v2. Tương đương phase Initialization của AWS AI-DLC, gồm scaffold, nhận diện bối cảnh, chọn profile
argument-hint: <tên tự do> [mô tả yêu cầu]
---
# /new-intent

Tương đương ba stage Initialization của AWS: Workspace Scaffold, Workspace Detection, State Init. Chạy một mạch, chỉ hỏi PO ở cuối để chốt profile.

## Đầu vào
`$ARGUMENTS`: tên do PO đặt, tự do, có thể kèm mô tả yêu cầu. Không ép định dạng, không hỏi năm hay bộ phận. Thiếu tên thì hỏi một câu.

Slug: bỏ dấu, chữ thường, gạch nối, tiền tố ngày `YYMMDD-`. Ví dụ "Báo cáo giai đoạn 1" ngày 09/10/2026 thành `261009-bao-cao-giai-doan-1`. Trùng slug đã có: báo và hỏi dùng tiếp hay đặt tên khác.

## 0.1 Scaffold
Tạo `.claude/intents/<slug>/`:
```
intent.md        từ .claude/templates/intent.md
state.md         từ .claude/templates/state.md
decisions.md     từ .claude/templates/decisions.md
memory.md        từ .claude/templates/memory.md
inputs/          PO đặt yêu cầu gốc, ảnh, csv vào đây
ideation/  inception/  reviews/  verification/  archive/  design/  user-guide/
```
Thư mục con của stage tạo khi stage chạy, không tạo trước. Thư mục rỗng có `.gitkeep`.

Có mô tả yêu cầu trong `$ARGUMENTS` thì ghi nguyên văn vào `inputs/request-<YYYYMMDD>.md`. Chưa có thì nói PO đặt file vào `inputs/` rồi gọi `/po`.

## 0.2 Detection
Quét nhanh để chọn profile, không phải Impact Analysis:
- Đọc `inputs/`, `.claude/knowledge/domain/00-index.md`, `.claude/memory/team.md`.
- Đoán module, màn, bảng, mail event bị chạm. Kiểm vùng có thuộc phần KB chưa phủ không, có tính năng Hidden không, có tích hợp ngoài không, có dữ liệu cũ cần migration không.
- Tìm intent và dự án cũ liên quan: so module bị chạm với `intent.md` của intent khác. Có thì ghi vào Related intents.
- Điền `intent.md`: Request, Product boundary, Related intents, KB cần đọc. Figma và Jira để trống cho PO.

## 0.3 State init
- Đề xuất profile theo `.claude/protocol/profiles.md`, kèm lý do theo từng dấu hiệu. Nghi ngờ thì chọn lớn hơn.
- Hỏi bằng hộp chọn, nội dung một dòng: *"Profile M: 7 stage, 6 gate, Depth Standard, reviewer ở 3 stage. Đồng ý, đổi profile, hay đổi depth?"*
- Ghi `state.md`: profile, depth, switches theo profile, bảng Stages với mọi stage, stage ngoài profile ghi `[S] ngoài profile <X>`, stage có điều kiện ghi `[ ]` kèm điều kiện.
- Ghi `DEC1` vào `decisions.md`: profile và lý do, nguyên văn PO.

## Kết thúc
Nói: cây đã tạo ở đâu, việc PO làm tiếp (đặt input, điền Figma và Jira trong `intent.md` nếu có), và lệnh bắt đầu: `/po <slug>`. Stage đầu tiên là 1.1 với M và L, 2.3 với S.
