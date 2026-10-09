---
description: Đẩy artifact đã duyệt của một intent lên Lark wiki, cập nhật đúng doc cũ, đọc lại và đối chiếu
argument-hint: <intent-slug> <initiative-brief | hld-brief | prd>
---
# /publish-lark

Chỉ publish artifact có `status: approved` trong frontmatter. Input: `$ARGUMENTS` gồm intent và artifact; thiếu thì hỏi, không đoán. Echo và confirm trước khi đẩy.

| Artifact | Đường dẫn trong intent | Tên trên Lark | Khi nào |
|---|---|---|---|
| Initiative Brief | `ideation/approval-handoff/initiative-brief.md` | `[Brief] <tên tính năng>` | Sau gate 1.7, PO muốn |
| HLD Brief | `inception/hld-brief/hld-brief.md` | `[HLD] <tên tính năng>` | Sau gate 2.41, bản 1.0 đủ sign-off |
| PRD | `inception/prd/prd.md` | `[PRD] <tên tính năng>` | Sau gate 2.42 và sau mỗi CR đã duyệt |

## Tiền điều kiện
| Kiểm | Thiếu thì |
|---|---|
| Frontmatter `status: approved` | Dừng, không publish |
| Lark target trong `intent.md` mục Lark: wiki space, node cha chung, intent node | Hỏi PO rồi ghi lại |
| Intent node đã tồn tại | Tạo trước, xem B3 |
| Kết nối Lark | Xem bên dưới |

## Kết nối
Ưu tiên `lark-cli` ở `~/.local/node/bin`, chạy với `--as user`; token user tự làm mới, hết hạn refresh thì `lark-cli auth login` và hỏi PO cấp quyền lại, không báo "không kết nối được". Công cụ `mcp__lark__*` với `useUAT: true` dùng để tra cứu (document_get, wiki getNode); OAuth tự dựng chỉ khi cả hai không có.

```bash
export PATH="$HOME/.local/node/bin:$PATH"
lark-cli auth status
```

## B1. Xác nhận với PO
Trình trước khi đẩy: artifact và version, intent node đích, tạo mới hay cập nhật doc cũ, cảnh báo nếu References chứa tài khoản staging. PO có thể bỏ qua; không tự publish.

## B2. Fidelity 1:1
Không tóm tắt, không gộp mục, không lược dòng. Bảng giữ đủ cột và dòng, bảng UI trong acceptance criteria thường 30 dòng trở lên. Mã tham chiếu, link, code block giữ nguyên. Mục đã xoá không tự thêm lại. **Bỏ khối frontmatter YAML** đầu file trước khi đẩy, Lark không hiển thị nó.

Sơ đồ sống trong file dưới dạng khối ` ```mermaid `, đặt đúng chỗ từ lúc soạn. `lark-cli docs +create` và `+update --doc-format markdown` tự dựng Mermaid thành bảng trắng. Đẩy bằng `drive/v1/import_tasks` thì ra code block Plaintext, phải vá bằng `python3 .claude/scripts/lark-mermaid-to-whiteboard.py <doc_token>`. Hai chỗ Mermaid trên Lark dựng sai: `stateDiagram-v2` mất dòng mô tả, dùng `flowchart`; `<br/>` trong nhãn mũi tên tách thành node rác, nhãn mũi tên viết một dòng.

Ảnh design không nằm trong `.md`, mỗi lần đẩy lại phải chèn lại: `python3 .claude/scripts/lark-insert-design-images.py <doc_token> <intent>/design` theo `order.txt` (`<tên file>|<chú thích>` mỗi dòng), tài liệu phải có heading `Design`. Script chèn rồi kéo cả cụm vào đúng mục và đếm lại.

## B3. Tạo hay cập nhật
Wiki hai tầng, tài liệu không bao giờ nằm thẳng dưới node cha chung:
```
02. Execution — Epics & Features     node cha chung, X3hhwv2MxizpFgkVudVl7e52gUc
├── Group                            intent node
│   └── [PRD] Group                  tài liệu
└── Gamification
    └── [PRD] Gamification
```

| Trạng thái trong `intent.md` | Làm gì |
|---|---|
| Chưa có intent node | Tạo node dưới node cha chung, tên là tên intent, rồi tạo tài liệu bên trong, lưu cả hai token |
| Có node, chưa có tài liệu | Tạo tài liệu dưới intent node, lưu document token |
| Đã có tài liệu | Cập nhật đúng doc cũ bằng overwrite. Không tạo doc mới |

```bash
# tạo mới
cat <file-đã-bỏ-frontmatter>.md | lark-cli docs +create --doc-format markdown \
  --title "<tên tài liệu>" --parent-token <intent_node_token> --content - --as user

# cập nhật doc đã có, đã chạy được ngày 09/10/2026 cho PRD Group v0.2
lark-cli docs +update --doc <document_token> --command overwrite \
  --doc-format markdown --content @<file-đã-bỏ-frontmatter>.md --as user
```

`overwrite` thay toàn bộ nội dung, giữ nguyên token và tiêu đề trên Lark; lịch sử bản cũ còn trong `docs +history-list`, lùi bằng `+history-revert`. PO đổi tên tài liệu trên Lark là chuyện thường, lần publish sau giữ tên họ đặt; định danh là token, không phải tên.

## B4. Đọc lại và đối chiếu
API trả thành công không có nghĩa nội dung vào đúng chỗ. `lark-cli docs +fetch --doc <token> --scope full --doc-format markdown --as user`, rồi đếm và so với file nguồn: số heading từng cấp, số bảng, số dòng bảng, số gạch đầu dòng, số bảng trắng bằng số khối mermaid và không còn code block sơ đồ, số ảnh bằng số dòng `order.txt` và nằm trong mục Design. Bản xuất ghi bảng dạng `|  |` và `|-|`, đó không phải lệch nội dung. Lệch thật thì báo cụ thể mục nào trước khi kết thúc.

## B5. Lưu mapping
`intent.md` mục Lark: token node, token doc, tên trên Lark, version, ngày. `state.md` bảng Versions cột Lark: `v<N> · <doc_token>`. Thêm dòng Log.

## Output
Doc đã tạo hay cập nhật kèm link; kết quả đối chiếu; số ảnh đã chèn; PO bỏ qua thì ghi "chưa publish". Tự kiểm theo `.claude/verification/publish-lark.md`.
