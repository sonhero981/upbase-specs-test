# Publish Lark – Đẩy tài liệu đã duyệt lên Lark

Publish artifact **đã được duyệt** (BRD sau Gate 1, PRD sau Gate 4) lên Lark Wiki.

**Chỉ publish tài liệu đã qua Gate.** Không publish bản còn `Draft - Pending Confirmation`.

Input: artifact cần publish + project — `$ARGUMENTS`

> **Xác định project:** ưu tiên `$ARGUMENTS`; không có → suy từ file đang mở; >1 khả dĩ → liệt kê cho chọn. **Echo + confirm trước khi chạy.**

---

## Tiền điều kiện

| Kiểm | Xử lý nếu thiếu |
|---|---|
| Artifact ở trạng thái **confirmed** (đã qua Gate) | Chưa → **dừng, không publish** |
| **Lark target** — wiki space + parent node | Đọc từ `project-context.md` mục `Lark`. Thiếu → hỏi người dùng rồi ghi lại vào đó |
| **Kết nối Lark** | Xem §Kết nối bên dưới |

---

## Kết nối Lark

### Cách 1 — MCP (ưu tiên)

Nếu phiên có tool `mcp__lark__*`:
- `wiki_v2_spaceNode_create` → tạo node
- `docx_builtin_import` → import markdown thành doc mới
- `documentBlockChildren_create` / `documentBlockDescendant_create` → chèn block
- Mọi call dùng `useUAT: true`

Token hết hạn → **hỏi người dùng cấp quyền lại, không báo "không kết nối được"**.

### Cách 2 — OAuth trực tiếp (khi MCP không có)

MCP server chỉ spawn lúc phiên khởi động. Nếu nó chết mà không restart được, tự chạy OAuth:

1. Dựng HTTP server ở `localhost:3000`, callback `/callback` (đã đăng ký sẵn trong app)
2. Mở browser:
   `https://open.larksuite.com/open-apis/authen/v1/authorize?app_id=<APP_ID>&redirect_uri=http://localhost:3000/callback&scope=docx:document wiki:wiki drive:drive offline_access`
3. Nhận `code` → POST `https://open.larksuite.com/open-apis/authen/v2/oauth/token`
   (`grant_type=authorization_code`, `client_id`, `client_secret`, `code`, `redirect_uri`)
4. Gọi API với header `Authorization: Bearer <access_token>`

> **Không dùng `tenant_access_token`** cho wiki/docx — scope `wiki:wiki` cấp ở cấp *user*, không phải cấp *app*. Trả lỗi `99991672`.
>
> **Hết hạn thì hỏi lại người dùng để cấp quyền.** Đây là việc bình thường, không phải lỗi.

---

## B1 — Xác nhận với người dùng (BẮT BUỘC)

Publish là hành động **đẩy ra ngoài**. Trình trước khi làm:

- Artifact + version
- Wiki space + parent node đích
- Sẽ **tạo mới** hay **cập nhật** node đã có
- **Cảnh báo nếu PRD có `Preferences` chứa credentials staging** — phạm vi người đọc trên Lark rộng hơn thư mục local

> **Người dùng có thể skip.** Chưa muốn publish → **bỏ qua, không đẩy gì cả**. Gọi lại bất cứ lúc nào. Không tự động publish.

---

## B2 — Chuyển Markdown → Lark

Quy tắc **fidelity 1:1** — không tóm tắt, không gộp section, không lược bỏ heading/row/dòng nào.

| Thành phần | Yêu cầu |
|---|---|
| **Heading** | Giữ nguyên cấp và thứ tự |
| **Bảng** | Giữ đủ mọi cột và mọi dòng. Bảng UI trong AC thường dài 30+ dòng — **không rút gọn** |
| **Mã tham chiếu** | `US1`, `BR-2.3` giữ nguyên |
| **Code block** | Giữ dạng code, không chuyển thành đoạn văn |
| **Link** | Giữ nguyên, đặc biệt link Figma và tài liệu đối tác trong `Preferences` |
| **Mục đã xoá** | Không tự thêm lại. Mục bị xoá là xoá có chủ đích |

## B2c — Ảnh design

**Ảnh đẩy được, nhưng chỉ qua `lark-cli`.** MCP thiếu tool upload media; CLI có scope `docs:document.media:upload`.

Ảnh là file nhị phân nên **không nằm được trong `.md`**. Mỗi lần import tạo một doc mới là mất sạch ảnh, phải chèn lại. Khác với sơ đồ — sơ đồ sống trong nguồn dưới dạng mermaid, ảnh thì không.

```bash
export PATH="$HOME/.local/node/bin:$PATH"
python3 .claude/scripts/lark-insert-design-images.py <doc_token> <thư mục ảnh>
```

Script đọc `order.txt` trong thư mục ảnh (`<tên file>|<chú thích>` mỗi dòng), chèn từng ảnh kèm caption, rồi kéo cả cụm vào mục `Design`. Cuối cùng đọc lại đếm xem đủ ảnh và đúng chỗ chưa. Thêm `--dry-run` để xem trước.

**Tài liệu phải có heading `Design`** làm điểm neo. Không có thì script dừng.

`docs +media-insert` luôn ghi vào **cuối tài liệu**, không có tham số vị trí — đó là lý do phải có bước kéo cụm.

---

## B2b — Sơ đồ: code block → bảng trắng

Sơ đồ sống trong file `.md` dưới dạng khối ` ```mermaid `, **đặt sẵn đúng vị trí từ lúc soạn ở Bước 9**, không phải vẽ thêm sau khi publish. File nguồn là bản duy nhất; người dùng duyệt đúng thứ sẽ lên Lark.

**Cách đẩy quyết định sơ đồ có dựng được hay không.** Đã đo cả hai:

| Cách đẩy | Mermaid thành gì |
|---|---|
| `lark-cli docs +create --doc-format markdown` | ✅ **Bảng trắng, tự động.** Không cần làm gì thêm |
| `drive/v1/files/upload_all` → `drive/v1/import_tasks` | ❌ Code block `Plaintext`. Phải chạy bước vá bên dưới |

Dùng cách thứ nhất:

```bash
export PATH="$HOME/.local/node/bin:$PATH"
cat <file.md> | lark-cli docs +create --doc-format markdown \
  --title "<tên tài liệu>" --parent-token <wiki_node_token> --content - --as user
```

`--parent-token` nhận thẳng **wiki node token**, nên tài liệu vào đúng chỗ trong Wiki mà không cần bước `move_docs_to_wiki` riêng.

Lỡ đẩy bằng cách thứ hai thì vá:

```bash
python3 .claude/scripts/lark-mermaid-to-whiteboard.py <doc_token>
```

Script đọc lại tài liệu, tìm code block mở đầu bằng từ khoá Mermaid (`flowchart`, `sequenceDiagram`, `erDiagram`…), thay từng cái bằng block `whiteboard`, rồi đọc lại lần nữa để xác nhận không còn sót. Thêm `--dry-run` để xem trước.

**Duyệt sơ đồ trước khi publish** — render ở máy rồi đưa người dùng xem:

```bash
npx -y @mermaid-js/mermaid-cli@latest -i so-do.mmd -o so-do.png
```

### Hai chỗ Mermaid trên Lark dựng sai

| Hiện tượng | Cách tránh |
|---|---|
| `stateDiagram-v2` **mất hết dòng mô tả** kiểu `Tên: nội dung`, chỉ còn tên trạng thái | Dùng `flowchart`, đưa mô tả vào nhãn node bằng `<br/>` |
| `<br/>` trong **nhãn mũi tên** bị tách thành node rác trôi lơ lửng | Nhãn mũi tên viết một dòng |

Tiếng Việt có dấu hiển thị bình thường. Hai chỗ cần ngắn gọn: **tiêu đề `subgraph`** (khung không giãn theo tiêu đề) và **chữ trong node hình thoi `{...}`** (cắt chữ sớm hơn hình chữ nhật).

---

## B3 — Tạo / cập nhật (idempotent)

Tra node đã lưu ở `project-context.md` mục `Lark → Đã publish`:

| Trạng thái | Làm gì |
|---|---|
| Chưa có | Tạo node mới dưới parent → **lưu lại node token + URL** |
| Đã có | Cập nhật nội dung node đó |

**Không tạo trùng.** Publish lại cùng một artifact phải cập nhật đúng node cũ.

---

## B4 — Đọc lại và đối chiếu

API trả `200` **không có nghĩa nội dung vào đúng chỗ**. Sau khi publish:

1. Đọc lại node vừa tạo/cập nhật
2. Đối chiếu:
   - Số heading trên Lark khớp số heading trong file
   - Số dòng của từng bảng khớp
   - **Số bảng trắng khớp số khối ` ```mermaid ` trong file, và không còn code block mermaid nào sót**
   - **Số ảnh khớp số dòng trong `order.txt`, và nằm đúng trong mục `Design`**
   - Không mục nào bị gộp hoặc mất
3. Lệch → **báo cụ thể mục nào thiếu** trước khi kết thúc

> ⚠️ **Script đếm bảng dễ sai, đừng tin số đầu tiên.** Hai chỗ đã cắn: bảng có **header rỗng** (`| | |`) bị bỏ qua khi tách theo ô, và bảng nằm trong **blockquote thụt lề** (`  > |`) không khớp mẫu `^>`. Lệch một hai dòng thì soi đúng bảng đó trước khi kết luận mất nội dung.

---

## B5 — Lưu mapping

Cập nhật `project-context.md`:

```markdown
### Đã publish

| Artifact | Node token | URL | Lần publish gần nhất |
| --- | --- | --- | --- |
| PRD v0.1 | | | |
```

---

## Output

- Node đã **tạo / cập nhật** + **link Lark**
- Đối chiếu sau publish: khớp hay lệch chỗ nào
- **Ảnh phải chèn tay** (nếu có) — liệt kê đường dẫn
- Người dùng **skip** → ghi rõ *"chưa publish lên Lark"*, không coi là lỗi

Tự kiểm theo `.claude/checklist/publish-lark.md` trước khi báo kết quả.
