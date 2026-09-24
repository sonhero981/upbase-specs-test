# Sơ đồ trong PRD

Năm sơ đồ Mermaid đang nằm trong PRD trên Lark. **File `.md` nguồn không chứa chúng** — Lark dựng sơ đồ thành **bảng trắng**, là một loại block riêng mà Markdown không có.

> ⚠️ **Import lại PRD từ `.md` sẽ tạo tài liệu mới không có sơ đồ.** Muốn giữ thì phải chèn lại năm sơ đồ theo hướng dẫn dưới.

## Sơ đồ nào ở đâu

| File | Vẽ gì | Chèn sau mục |
|---|---|---|
| `01-hai-nhip.mmd` | Điểm cộng tức thì trong luồng thao tác, còn bảng xếp hạng tính nền 8 tiếng một lần. Giải thích vì sao học viên thấy điểm ngay nhưng thứ hạng đổi muộn | `Solution` → `Bốn luồng` |
| `02-luong-cong-diem.mmd` | Năm cửa kiểm trước khi cộng một điểm: `Test Account` → công tắc `Gamification` → công tắc hành động → khử trùng → trần ngày | `US13: Điểm phản ánh việc học thật` |
| `03-logic-len-hang.mmd` | Ba bội số cộng dồn, kèm ví dụ `9.000` điểm + `10` khoá + `5` huy hiệu ra hạng 7 | `US10: Cấu hình hạng` |
| `04-hai-cong-tac.mmd` | Ba trạng thái `Tắt hẳn` · `Chạy ngầm` · `Mở đầy đủ` và cách chuyển giữa chúng | `US14: Bật tắt gamification và hiển thị` |
| `05-quan-he-du-lieu.mmd` | Mười thực thể mới chia ba tầng: cấu hình → ghi nhận → đọc | `Solution` → `Database` |

## Chèn lại sau khi import mới

```bash
export PATH="$HOME/.local/node/bin:$PATH"

# 1 — lấy block_id của mục cần chèn sau
lark-cli docs +fetch --doc "<doc_token mới>" --scope outline --max-depth 2 --as user

# 2 — chèn từng sơ đồ
lark-cli docs +update --doc "<doc_token mới>" \
  --command block_insert_after --block-id "<block_id của mục>" \
  --content '<whiteboard type="mermaid" path="@./01-hai-nhip.mmd"></whiteboard>' --as user
```

`path="@./..."` chỉ nhận **đường dẫn tương đối trong thư mục đang chạy**, nên `cd` vào thư mục này trước, hoặc dán thẳng nội dung `.mmd` vào giữa cặp thẻ `<whiteboard>`.

## Sửa một sơ đồ đã có

Đừng tạo bảng trắng mới — ghi đè vào bảng trắng cũ để giữ nguyên vị trí trong tài liệu:

```bash
cat 03-logic-len-hang.mmd | lark-cli whiteboard +update \
  --whiteboard-token "<token>" --input_format mermaid --overwrite --source - --as user
```

Lấy `<token>` bằng `docs +fetch --detail with-ids` rồi tìm block `whiteboard`.

## Hai chỗ Mermaid trên Lark dựng sai

Gặp rồi, tránh đi:

- **`stateDiagram-v2` không dựng được dòng mô tả** kiểu `Tên: dòng mô tả`. Chỉ hiện mỗi tên trạng thái. Dùng `flowchart` với `<br/>` trong nhãn node thay thế.
- **`<br/>` trong nhãn mũi tên bị tách thành node rác.** Nhãn mũi tên phải viết một dòng.

Ngoài hai chỗ đó, tiếng Việt có dấu hiển thị bình thường. Chỉ cần giữ **tiêu đề `subgraph` ngắn** vì khung không giãn theo độ dài tiêu đề, và **chữ trong node hình thoi `{...}` phải ngắn** vì hình thoi cắt chữ sớm hơn hình chữ nhật.
