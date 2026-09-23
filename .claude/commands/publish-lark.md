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

**Ảnh:** server Lark hiện chưa bật tool upload media. Có ảnh → đẩy phần chữ, rồi **báo rõ ảnh nào phải chèn tay** kèm đường dẫn file ở máy. **Không lặng lẽ bỏ ảnh.**

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
   - Không mục nào bị gộp hoặc mất
3. Lệch → **báo cụ thể mục nào thiếu** trước khi kết thúc

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
