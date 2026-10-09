---
description: Bảng trạng thái mọi intent của luồng v2, kèm kiểm tra lệch giữa state và file. Chỉ đọc, không sửa
argument-hint: [intent-slug]
---
# /po-status

Chỉ đọc. Không sửa file nào. Phát hiện lệch thì báo, không tự sửa.

## Bảng tổng
Với mỗi `.claude/intents/*/state.md`, một dòng:

| Intent | Profile | Stage hiện tại | Trạng thái | Việc kế tiếp | Câu chặn | CR mở | Lark |
|---|---|---|---|---|---|---|---|

Trạng thái lấy từ ký hiệu stage: chờ duyệt, đang làm, đang sửa, dừng, xong.
Có `$ARGUMENTS` thì chỉ in intent đó, kèm bảng Stages đầy đủ và bảng Versions.

## Kiểm tra lệch
Chạy trước: `python3 .claude/scripts/po-tools.py status`. Script in bảng tổng, dự án cũ, và tám kiểm tra dưới đây bằng máy. AI đọc kết quả, bổ sung phần máy không thấy (Next action còn hợp lý không, Related intents đúng nội dung không), rồi trình. Không chạy được python thì kiểm tay.
Với mỗi intent, kiểm và liệt kê mọi phát hiện, không dừng ở phát hiện đầu:
1. Stage `[x]` không có artifact, hoặc không có bản chụp trong `archive/`.
2. Artifact có trên đĩa nhưng stage vẫn `[ ]`.
3. Phiên bản trong `state.md` khác frontmatter artifact.
4. Stage `[x]` không có dòng DEC nào cùng stage trong `decisions.md`.
5. Questions file có câu chặn còn trống nhưng stage đã qua `[?]`.
6. `[?]` hoặc `[-]` quá 7 ngày không thay đổi: nhắc.
7. Lark: phiên bản đã publish khác phiên bản hiện tại của artifact bàn giao.
8. `intent.md` có Related intents trỏ tới intent hoặc dự án không tồn tại.

Kết quả:
| # | Intent | Lệch | Gợi ý xử lý |
|---|---|---|---|

Không lệch thì ghi một dòng "state khớp với đĩa".
