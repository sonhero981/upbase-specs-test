# Generate PRD – Viết Product Requirement Document

Dùng sau khi BRD (Gate 1), Impact Matrix (Gate 2) và Solution (Gate 3) đã được duyệt.

**Tương đương Bước 9 + Gate 4 trong `/po-workflow`.**

PRD là **tài liệu bàn giao duy nhất** — Tester, UI/UX, Dev đều đọc từ đây.

---

## Đầu vào

`$ARGUMENTS` — tên project hoặc feature.

> **Xác định project:** ưu tiên `$ARGUMENTS`; không có → suy từ file đang mở; >1 khả dĩ → liệt kê cho chọn. **Echo + confirm trước khi chạy.**

Đọc theo thứ tự:

1. `docs/brd/brd-v*.md` — bản đã qua Gate 1
2. `working/impact-analysis/impact-matrix-v*.md` — đã qua Gate 2
3. `working/solution-options/solution-comparison-v*.md` + `project-decisions.md` — solution đã chốt ở Gate 3
4. `project-context.md`
5. `.claude/_shared-knowledge-base/` — KB liên quan
6. Figma / design nếu có
7. `.claude/_templates/prd/Template.md` — cấu trúc bắt buộc

**Thiếu một trong ba artifact đã duyệt → dừng và báo.** Không viết PRD trên nền chưa được chốt.

---

## Ba giai đoạn

### 9A — Khung + danh sách US

Dựng phần đầu PRD theo template:

| Mục | Lấy từ đâu | Lưu ý |
|---|---|---|
| Bảng metadata | Hỏi người dùng | Target release · Epic/Story link Jira · Document owner · Designer · Tech lead · QA · Reviewer · Document status |
| Document version | Tự tạo | `v0.1` + ngày + nội dung |
| Problem | BRD §1 | Viết lại nguyên, không tóm tắt |
| Analytics | BRD §2 | Chưa có số liệu → ghi rõ, không bỏ trống |
| Objective | BRD §3 | |
| **Out of scope** | BRD + `project-context.md` + mọi `CR` đã áp | Cấp **tính năng**, không phải cấp US. Xem quy tắc bên dưới |
| Stakeholder | BRD §4 | Bảng `Stakeholder │ Action` |
| **Preferences** | Hỏi người dùng | Link Figma · BRD liên quan · tài liệu đối tác · API tham chiếu · tài khoản staging |
| Metrics success | **Hỏi người dùng** | Xem quy tắc bên dưới |
| Solution | Solution Comparison + Impact Matrix | Tách `TDD` · `Database` · `API` |

**Quy tắc Metrics success:**

> **Hỏi trước khi viết:** *"Tính năng này có cần định nghĩa chỉ số đo ngay từ đầu không?"*
> - Có → điền chỉ số **thật của chính tính năng này**, chỉ giữ factor HEART thực sự đo được
> - Không → **xoá hẳn mục này khỏi PRD**
>
> 🚫 **Tuyệt đối không giữ lại bảng ví dụ của template.** Hai PRD đang lưu hành mang nguyên chỉ số của app ghi chép thu chi (`NPS > 50`, `Transaction Input Time < 30s`) vào tài liệu về routing kho và quảng cáo Shopee. Để lại ví dụ còn tệ hơn bỏ trống.

**Quy tắc `Out of scope` cấp tính năng:**

Mục này trả lời câu hỏi *"tính năng này có bao gồm X không"* mà không bắt người đọc lục hết các US. Khác hẳn `Out of scope` của từng US — cái đó nói về một màn, cái này nói về cả phạm vi.

Gom từ ba nguồn:

| Nguồn | Lấy gì |
|---|---|
| `project-context.md` mục `Out of scope` | Thứ đã chốt ngoài phạm vi từ đầu |
| Mọi `CR` đã áp | Thứ **từng nằm trong phạm vi rồi bị loại** — đây là nhóm hay bị quên nhất |
| `Out of scope` của từng US | Thứ lặp lại ở nhiều US thì nâng lên cấp tính năng |

Mỗi dòng một thứ, kèm lý do **một câu**. Lý do phải thuộc một trong bốn loại: chưa yêu cầu · chờ tính năng khác · đã cân nhắc và loại ở `CR` nào · thuộc phạm vi tính năng khác.

> Không có mục này thì người đọc PRD trên Lark phải đọc hết 15 US mới ghép lại được bức tranh, mà thứ bị loại giữa chừng theo `CR` thì không US nào nhắc tới.

**Danh sách US:** lấy từ BRD §7, mỗi US gắn nguồn (yêu cầu nào · impact nào · coverage gap nào).

Đánh số `US1`, `US2`, `US3`… liên tục. US chưa làm trong phạm vi này → ghi rõ trong tiêu đề: `US3: Sao chép quy tắc — chưa làm`.

**→ Dừng, confirm danh sách US với người dùng trước khi viết chi tiết.**

---

### 9A+ — Chia Unit

Làm **sau khi chốt danh sách US**, trước khi viết chi tiết.

Chia các US thành nhóm **làm độc lập được**. Một Unit là nhóm US cùng phục vụ một cơ chế, release được mà không cần chờ Unit khác xong.

Cách chia:

1. **Nhóm theo cơ chế, không nhóm theo màn hình.** US cấu hình và US hiển thị của cùng một cơ chế thuộc cùng Unit
2. **Tìm Unit nền** — cái mọi Unit khác phụ thuộc vào. Thường là cơ chế ghi nhận dữ liệu gốc
3. **Tách Unit nền tảng** — những US chạm mọi Unit (phân quyền, bật tắt, lịch sử) không release độc lập được, gom riêng
4. **Ghi phụ thuộc theo chiều một hướng.** Phụ thuộc vòng là dấu hiệu chia sai

| Unit | Gồm US | Phụ thuộc | Release độc lập? |
|---|---|---|---|
| *Tên nhóm* | `US1` · `US2` | *Unit nào xong trước* | ✅ / ❌ kèm lý do |

Kèm **thứ tự đề xuất** và một câu nói rõ đây chỉ là đề xuất, Dev chốt thứ tự thật.

> **Cỡ `S` bỏ mục này.** Một US thì không có gì để nhóm.

### 9B — Field Intake

**Tra trước khi hỏi.** Mục đích: phân biệt field/màn **đã tồn tại** với **thực sự mới**, để không mô tả lại cái đã có thành "mới".

| Bước | Làm gì |
|---|---|
| 1 | Đọc Impact Matrix → danh sách entity/màn bị chạm |
| 2 | Tra KB `12-data-model.md` → bảng và khoá ngoại liên quan |
| 3 | Tra **Swagger `components.schemas`** → field hiện có, kiểu, required, enum |
| 4 | Tra KB `01`–`11` → rule chi phối field đó |
| 5 | Phân loại mỗi màn: **A** = mới hoàn toàn · **B** = sửa màn có sẵn · **C** = chỉ đọc/hiển thị |

Rồi gom **một bảng duy nhất** hỏi người dùng:

| Màn | Field | Hiện có? | Kiểu | Bắt buộc | Giá trị hợp lệ | Validate | Rule chi phối | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| | | Có / Mới | | | | | `BR-*` hoặc KB ref | `[đề xuất]` hoặc `❓BA` |

Màn danh sách hỏi thêm: **filter · search · sort · pagination · cột hiển thị**.

Quy ước điền:
- `[đề xuất]` — AI tự điền từ KB/Swagger, chờ người dùng review
- `❓BA` — không suy được, cần người dùng cung cấp
- Field **hiện có** → chỉ hỏi **delta** (đổi gì) và **migration**, không hỏi lại từ đầu

**→ Dừng. Chỉ viết chi tiết khi bảng đã đủ.** Ô `❓BA` chưa quyết → chuyển thành Open Question, **không bịa**.

---

### 9C — Viết chi tiết từng US

Viết **liên tục**, không dừng giữa từng US — trừ US rủi ro cao hoặc phức tạp thì review riêng.

Mỗi US đầy đủ sáu mục theo template:

**1/ User story** — một câu tiếng Việt tự nhiên theo vai trò.
*Ví dụ: "Là vận hành, tôi cần mapping kho vật lý với kho kênh bán để xử lý đơn và trừ tồn đúng kho."*
Không ép khuôn `As a / I want / So that` — 4 PRD đang lưu hành đều viết tự nhiên.

**2/ Pre - Condition** — điều kiện cần trước khi thực hiện: trạng thái dữ liệu · quyền · cấu hình · US khác đã xong.

**3/ Scenario** — kịch bản vận hành: đi từ đâu, làm gì, theo thứ tự nào.

**4/ Acceptance criteria** — mục nặng nhất, gồm bốn phần:

| Phần | Dạng | Lưu ý |
|---|---|---|
| **UI / UX / Rule UX / Rule UI** | **Bảng** | Dạng A `Màn hình │ Giao diện │ Field │ Yêu cầu` cho tính năng mới · Dạng B `Thay đổi │ Section │ Field │ Validate` cho sửa tính năng có sẵn |
| **Business requirement — Business rule** | Gạch đầu dòng | Mỗi rule gắn mã `BR-<số US>.<số thứ tự>` |
| **Data Field** | Bảng | Field mới/đổi. US không đụng dữ liệu → bỏ mục này |
| **NFR** | Gạch đầu dòng | Không có → xoá |

Cột `Yêu cầu` trong bảng UI phải đủ: **định dạng · placeholder · options · giá trị mặc định · điều kiện disable · tooltip · validate · hành vi khi thao tác**. Đây là mức chi tiết mà PRD thật đang viết (bảng dài 33 dòng cho một màn cấu hình).

Rule chạm tính năng có sẵn → **dẫn mã rule trong KB**: `BR-EDIT-07`, `KB-CLASS-03`.

### Sơ đồ — viết ở đây, không vẽ sau khi publish

Template có mục `Giải pháp nghiệp vụ: User flow, screen flow, BPMN, Activity diagram` nhưng nó hay bị bỏ trống vì "tài liệu chữ không vẽ được". Vẽ được: đặt khối ` ```mermaid ` thẳng vào file `.md`, đúng chỗ nó thuộc về. Lúc publish, `/publish-lark` tự đổi thành bảng trắng.

**File `.md` là bản duy nhất.** Không tách "bản duyệt" và "bản đẹp cho Lark" — thứ người dùng duyệt ở Gate 4 phải đúng là thứ lên Lark.

Vẽ chỗ nào thì đáng:

| Nên vẽ | Đừng vẽ |
|---|---|
| Luồng nhiều cửa kiểm nối tiếp — người đọc không dựng lại được thứ tự từ các rule rời | Thứ bảng đã nói đủ |
| Cơ chế chạy **song song ở hai nhịp khác nhau** | Quan hệ hai ba thực thể |
| Công thức **cộng dồn nhiều tiêu chí** — chỗ dễ đọc "HOẶC" thành "lấy cái lớn nhất" | Danh sách tuần tự |
| Máy trạng thái vài trạng thái và đường đi giữa chúng | |
| Quan hệ **nhiều thực thể phân tầng** | |

Sơ đồ nào cũng kèm **một dòng chú thích bên dưới** nói ý chính, để người đọc lướt không phải giải mã hình.

**Duyệt trước khi publish:** render ra ảnh cho người dùng xem, đừng bắt họ đọc mã Mermaid.

```bash
npx -y @mermaid-js/mermaid-cli@latest -i so-do.mmd -o so-do.png
```

Hai chỗ Mermaid trên Lark dựng sai và cách né: xem `/publish-lark` mục `B2b`.

---

**5/ Out of scope** — những gì US này **không** làm, dù người đọc có thể tưởng là có.

**6/ Conner case** — **để trống. QA điền.** PO/BA không viết mục này.

---

## Output

`docs/prd/prd-<feature>-v0.1-YYYYMMDD.md`

Phần còn chờ xác nhận → đánh dấu `Draft - Pending Confirmation`.

Cuối PRD: **Vấn đề tồn đọng** (câu hỏi chưa có lời giải, việc đẩy sang sprint sau) và **Comments**.

Tự review theo `.claude/checklist/generate-prd.md` trước khi trình bày.

---

## Trình bày tại Gate 4

- Tóm tắt từng US và điểm đáng chú ý
- **Business rule mới** đặt ra · **rule hiện có bị chạm**
- Field / bảng / endpoint bị ảnh hưởng
- **Mục đã xoá vì không áp dụng** (Metrics success, NFR, Data Field…) — nói rõ để người dùng biết là xoá có chủ đích, không phải quên
- Open question còn lại

Ba lựa chọn: `Approved` / `Approved with Notes` / `Need Revision`.

`Need Revision` → yêu cầu feedback trỏ **mã cụ thể** (`US2 → BR-2.3`, `US1 → bảng UI, field Trạng thái`) để sửa nhắm đích, không viết lại cả PRD.

Duyệt xong → gợi ý `/publish-lark` (**hỏi trước, có thể skip**).

---

## Quy tắc riêng của PRD

- **Mục không áp dụng thì xoá hẳn**, không để lại nội dung mẫu của template
- **Không bịa field.** Không tra được trong KB/Swagger và người dùng chưa trả lời → `Open Question`
- Field **hiện có** phải được nhận diện là hiện có — viết lại thành "mới" là lỗi nặng, vì Dev sẽ tạo trùng
- Mọi **hằng số cứng** (số ngày, ngưỡng, giới hạn) phải ghi rõ: hardcode hay cấu hình được
- Bảng mới trong `Database` phải khai báo có `tenant_id` hay không
- Endpoint mới phải **đối chiếu Swagger trước** — hệ thống đã có 708 operation, tránh khai trùng
