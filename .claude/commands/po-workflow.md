# PO Workflow – Từ yêu cầu thô đến tài liệu bàn giao

Điều phối toàn bộ quy trình phân tích của PO/BA: 9 bước + **4 Gate**. Dừng tại mỗi Gate chờ người dùng xác nhận trước khi đi tiếp.

**Workflow sinh ra 5 artifact, không phải một:**

| Artifact | Vai trò | Nơi lưu |
|---|---|---|
| Clarified Requirements + Open Questions | Làm rõ yêu cầu thô | `working/ai-drafts/` |
| **BRD** | Chốt hướng — Gate 1 | `docs/brd/` |
| **Impact Matrix** | Phân tích ảnh hưởng — Gate 2 | `working/impact-analysis/` |
| **Solution Comparison** | Chốt phương án — Gate 3 | `working/solution-options/` |
| **PRD** | **Tài liệu bàn giao** — Gate 4 | `docs/prd/` |
| User Guide | Sau khi dev xong | `docs/user-guide/` |

Chỉ **PRD** và **User Guide** là tài liệu bàn giao. Ba artifact còn lại là bản phân tích nội bộ — nhưng đều phải qua Gate, vì sai ở tầng nào thì tầng sau xây trên nền sai.

> ⚠️ **Gate KHÔNG phải để duyệt tài liệu — Gate để chặn sai sót ở từng tầng phân tích.**
> PRD gộp BRD + FS làm một, nhưng **các tầng phân tích vẫn phải được duyệt riêng**. Viết xong cả PRD rồi mới phát hiện Impact sai thì toàn bộ `Specific Requirement` phải làm lại.
>
> Artifact trung gian (BRD, Impact Matrix, Solution Comparison) là **bản phân tích nội bộ**. Sau khi được duyệt, nội dung nào thuộc template PRD thì đưa vào PRD.

---

## Sơ đồ

```
[Bước 1-3]  Làm rõ yêu cầu
                ↓
[Bước 4]    BRD ────────────────► GATE 1  Approved?  ──► Need Revision → về Bước 3
                ↓
[Bước 5]    Chốt phạm vi liên quan  (điểm dừng: người dùng confirm)
[Bước 6]    Impact Matrix ───────► GATE 2  Approved?  ──► Need Revision → về Bước 5
                ↓
[Bước 7-8]  So sánh solution ────► GATE 3  Approved?  ──► Need Revision → về Bước 7
                ↓
[Bước 9]    PRD
              9A  Khung + danh sách US   (điểm dừng: confirm US list)
              9A+ Chia Unit — nhóm bàn giao, phụ thuộc, thứ tự
              9B  Field Intake           (điểm dừng: hỏi field + rule)
              9C  Viết chi tiết từng US
                ─────────────────────► GATE 4  Approved?  ──► Need Revision → sửa theo mã cụ thể
                ↓
         Publish Lark · User Guide (sau khi dev xong)
```

**Cái gì chảy vào PRD:**

| Artifact được duyệt | Vào mục nào của PRD |
|---|---|
| BRD | `Problem` · `Analytics` · `Objective` · `Stakeholder` · `Out of scope` từng US |
| BRD + `project-context` + mọi `CR` | **`Out of scope` cấp tính năng** — gom thứ cả tính năng không làm, kèm thứ từng có rồi bị loại |
| Danh sách US đã chốt | **`Unit`** — nhóm US làm độc lập được, phụ thuộc giữa các nhóm, thứ tự đề xuất |
| Impact Matrix | `Solution` · `Database` · `API` · `Acceptance criteria → Data Field` · `Out of scope` |
| Solution Comparison | `Solution` · `TDD` |
| Chi tiết US | `Specific Requirement` |

---

## Phân loại cỡ yêu cầu — làm ngay sau Bước 2

**Không phải yêu cầu nào cũng cần đủ 9 bước.** Bắt một yêu cầu sửa nhỏ chạy qua BRD → Impact Matrix → Solution Comparison → PRD là cách chắc chắn khiến người dùng bỏ workflow và viết tay cho nhanh.

Sau khi làm rõ yêu cầu (Bước 2), **quét nhanh** KB + DB + Swagger để phân loại. Đây là quét sơ bộ, không phải Impact Matrix đầy đủ.

| Cỡ | Dấu hiệu — phải đúng **tất cả** | Đường đi | Gate |
|---|---|---|---|
| **S** | Chạm **1 màn** · không đổi data model · không đổi business rule hiện có · không chạm module khác · không chạm tính năng `hidden` | Bước 1–3 → **Bước 9 (PRD rút gọn, 1 US, bỏ `Unit`)** | **Gate 4** |
| **M** | Chạm **≤2 module** · có thể thêm field nhưng không đổi quan hệ bảng · không phát hiện conflict · đã rõ hướng giải quyết | Bước 1–6 → Bước 9 | **Gate 1 + Gate 2 + Gate 4** |
| **L** | Chạm **≥3 module**, HOẶC đổi data model/quan hệ, HOẶC có conflict, HOẶC chạm tính năng `hidden`, HOẶC có nhiều hướng giải quyết | **Đủ 9 bước** | **Đủ 4 Gate** |

### Ba quy tắc bắt buộc

1. **Nghi ngờ thì lên cỡ.** Không chắc S hay M → chọn M. Chi phí của việc phân loại thừa thấp hơn nhiều so với bỏ sót ảnh hưởng.

2. **Phát hiện giữa chừng thì nâng cỡ ngay.** Đang chạy đường S mà thấy chạm business rule hiện có, hoặc thấy `❓BA` về dữ liệu cũ → **dừng, báo người dùng, chuyển sang M hoặc L**. Không đi tiếp đường cũ.

3. **Echo phân loại + lý do trước khi chạy.** Trình bày:
   > *"Yêu cầu này tôi phân loại **M** vì: chạm 2 module (Class, Grading) · thêm 1 field vào `class_mentor_instances` nhưng không đổi quan hệ · không phát hiện conflict. Đường đi: bỏ bước Solution Comparison, chạy Gate 1 → Gate 2 → Gate 4. Đồng ý không?"*

   **Người dùng có quyền đổi cỡ.** Muốn chạy đủ 9 bước cho một yêu cầu S → theo người dùng.

### PRD rút gọn cho cỡ S

Giữ nguyên template nhưng chỉ điền: metadata · Document version · `Problem` · `Objective` · `Preferences` · `Specific Requirement` (1 US đầy đủ).

Xoá hẳn: `Analytics` · `Stakeholder` · `Metrics success` · `Solution` (TDD/Database/API) · `Unit`.

> `Out of scope` cấp tính năng thì **giữ** kể cả ở cỡ `S` — một màn vẫn có thứ người đọc tưởng là có mà không làm.

> Cỡ S vẫn phải qua **Field Intake** (Bước 9B). Đây là chỗ hay sai nhất kể cả với yêu cầu nhỏ — sửa một màn vẫn phải biết field nào đã tồn tại.

---

## Bước 0 – Xác định project

Thứ tự ưu tiên:

1. Tên nêu trong lệnh (`$ARGUMENTS`) — tin cậy nhất
2. File đang mở nằm trong folder project nào → suy ra project đó
3. Không rõ **hoặc có nhiều project khả dĩ** → **liệt kê `.claude/projects/` cho người dùng chọn, KHÔNG tự đoán**

**Luôn echo + confirm project trước khi chạy**, nêu rõ lý do chọn. Sai → chuyển ngay, không tiếp tục với project sai.

Sau khi xác định `<project>`, đọc theo thứ tự:

1. `.claude/projects/<project>/project-context.md`
2. `.claude/projects/<project>/project-decisions.md`
3. `.claude/projects/<project>/working/` — raw-inputs, open-questions, meeting-notes
4. `.claude/projects/<project>/docs/` — artifact đã có
5. `.claude/_shared-knowledge-base/00-index.md` → file KB liên quan

Tóm tắt ngắn những gì đã đọc, rồi hỏi: **bắt đầu từ bước nào?**

---

## Giai đoạn 1 – Làm rõ yêu cầu

### Bước 1 – Nhận input

Người dùng cung cấp yêu cầu thô: mô tả vấn đề, yêu cầu từ stakeholder, meeting note, tài liệu tham khảo.

Chưa có file → hướng dẫn đặt vào `.claude/projects/<project>/working/raw-inputs/`.

### Bước 2 – Phân tích và làm rõ

Áp dụng `/clarify-requirements`, tự kiểm theo `.claude/checklist/clarify-requirements.md`. Tạo:

- Bảng requirement candidates: `ID / Requirement / Type / Source / Confidence / Notes`
- Scope sơ bộ: In / Out / Potential
- Bảng open questions: `ID / Question / Why It Matters / Owner / Blocks Next Step?`

Lưu tại `working/ai-drafts/` và `working/open-questions/`.

**Dừng chờ phản hồi. Không sang Bước 3 khi còn blocking question về:** vấn đề cần giải quyết · phạm vi · người dùng/vai trò · business rule cốt lõi.

### Bước 3 – Bổ sung thông tin

Cập nhật theo câu trả lời. Còn blocking question → lặp lại Bước 2–3.

---

## Giai đoạn 2 – BRD

### Bước 4 – Viết BRD

Áp dụng `/generate-brd`. Dùng `.claude/_templates/brd/Template.md`.

Input: clarified requirements · open questions đã giải quyết · project-context · project-decisions.

Output: `docs/brd/brd-v0.1-YYYYMMDD.md`

Tự review theo `.claude/checklist/generate-brd.md`. Còn assumption lớn → đánh dấu `Draft - Pending Confirmation`.

> **BRD là bản nháp nội bộ để chốt hướng.** Nội dung sẽ được viết lại nguyên vào PRD — nên viết đúng ngay, đừng viết tắt.

---

## GATE 1 – Duyệt BRD

Trình bày:

- Problem · Analytics · Objective
- Scope: In / Out / Potential
- Hướng giải quyết ở mức khung
- **Danh sách US dự kiến**
- Assumption đáng chú ý
- Open question còn lại

Yêu cầu chọn một trong ba:

> **`Approved`** – tiếp tục Giai đoạn 3
> **`Approved with Notes`** – ghi notes vào `project-decisions.md` rồi tiếp tục
> **`Need Revision`** – quay lại Bước 3 với hướng dẫn cụ thể

**Không sang Giai đoạn 3 cho đến khi được `Approved` hoặc `Approved with Notes`.**
**Trả lời không rõ → hỏi lại, không tự suy đoán là duyệt.**

---

## Giai đoạn 3 – Phân tích ảnh hưởng

### Bước 5 – Chốt phạm vi liên quan

**Chủ động quét** BRD + `project-context.md` + KB + DB schema + Swagger, trình **"Related Features & Docs Map"**:

| Hệ | Tính năng / Module / Entity / Endpoint | New / Existing | Nguồn | Ghi chú |
| --- | --- | --- | --- | --- |

Bao quát: module · màn hình · data model/entity · API/integration/job · role/permission · business rule hiện tại · NFR. Mỗi dòng ghi rõ **nguồn** (KB nào · bảng nào · endpoint nào). Chưa chắc → `❓BA`.

Trình người dùng confirm: **đủ chưa · có sót · dòng nào không liên quan · KB/PRD cũ nào nên đọc thêm.** Mục `❓BA` phải được chốt — không để giả định trôi vào matrix.

> **Recognition > recall:** người dùng review một bản nháp, không phải nhớ từ đầu.
> Field/màn **Existing** phải được nhận diện ở đây để không bị coi là "mới" ở bước sau.

**Không sang Bước 6 cho đến khi phạm vi được chốt.**

### Bước 6 – Dựng Impact Matrix

> **Auto compact:** chạy `/compact` trước bước này. Impact Analysis phải đọc nhiều nguồn (KB, DB, Swagger), context đầy dễ bỏ sót. Báo người dùng rồi tiến hành.

Áp dụng `/impact-analysis`. Dùng `.claude/_templates/impact-matrix/Template.md`.

Thực hiện đúng thứ tự framework:

1. **STEP 1 — Extract Current Situation:** đọc input tìm **dependency** (không phải hiểu feature) → Dependency Map
2. **STEP 2 — Extract Desired Situation:** từ BRD rút ra feature mới, process mới, FR/NFR đã có
3. **STEP 3 — Impact & Gap Analysis:**
   - Quét **12 vùng**: Business process · Module · Screen · Data · API · Role · Business rule · NFR · Notification · Reporting · Test · Release
   - **3a Conflict Detection** (4 chiều: business rule · process · data · permission) → escalate, **không tự resolve**
   - **3b Bidirectional Impact** (New→Old, Old→New) → FR/NFR bổ sung, feed ngược vào BRD
   - **3c Coverage Check** (boundary · exception · shared entity · side effect) → FR bổ sung
4. **STEP 4 — Transition Requirements:** Data · Compatibility · Cutover

**Quét thêm chiều tenant:** thay đổi này có làm tăng chỗ đóng cứng cho UpBase không? Đối chiếu `15-product-direction.md` §6.

Thiếu context để đánh giá một bước → tạo Open Question, **không giả định**.

Output: `working/impact-analysis/impact-matrix-v0.1-YYYYMMDD.md`

---

## GATE 2 – Duyệt Impact Matrix

Trình bày:

- Tóm tắt vùng bị ảnh hưởng theo severity (High / Medium / Low)
- **Conflict phát hiện được** — cần escalate, không tự resolve
- **FR/NFR còn thiếu** — feed ngược vào BRD
- **Coverage gap** — case chưa được định nghĩa
- **Transition Requirements** (Data / Compatibility / Cutover)
- **Chỗ đóng cứng tenant** bị tăng thêm (nếu có)
- Risk đáng chú ý · Open question còn lại

Ba lựa chọn như Gate 1. `Need Revision` → quay lại Bước 5.

**Không sang Giai đoạn 4 cho đến khi được duyệt.**

---

## Giai đoạn 4 – Solution

### Bước 7 – Xác định tình huống và chuẩn bị options

**Hỏi trước:** *"Anh/chị đã có định hướng giải pháp cho yêu cầu này chưa? Nếu có, mô tả ngắn."* Rẽ nhánh:

**TH1 — đã có định hướng:**
- Nhận xét alignment với objective, chỉ ra điểm mạnh và gap
- Gợi ý thêm 1–2 option thay thế nếu cần, tham chiếu best practice
- Sang Bước 8 với tất cả options

**TH2 — chưa có định hướng:**
- Gợi ý 2–3 option dựa trên BRD, Impact Matrix và best practice
- Lưu vào `working/raw-inputs/solution-options-draft-YYYYMMDD.md`
- Sang Bước 8 (không chờ confirm từng option — Gate 3 là điểm review)

**Trả lời không rõ có/chưa → hỏi lại, không tự suy đoán.**

### Bước 8 – So sánh và đề xuất

Áp dụng `/compare-solutions`. Dùng `.claude/_templates/solution-comparison/Template.md`.

So sánh theo: business fit · tác động tới người dùng và quy trình · tác động hệ thống/data/API · effort · risk · dependency · pros-cons.

**Ghi recommendation có điều kiện — không ghi là quyết định cuối.**

Output: `working/solution-options/solution-comparison-v0.1-YYYYMMDD.md`

---

## GATE 3 – Duyệt Solution

Trình bày:

- (Nếu người dùng đã có định hướng) nhận xét ngắn về định hướng đó
- Danh sách options và nguồn gốc (người dùng / AI gợi ý / best practice)
- Bảng so sánh tóm tắt
- Recommendation kèm điều kiện và risk phải chấp nhận
- Open question trước khi approve

Ba lựa chọn như trên. `Need Revision` → quay lại Bước 7.

Duyệt xong → ghi solution decision vào `project-decisions.md` (option được chọn, lý do, trade-off chấp nhận).

---

## Giai đoạn 5 – Viết PRD

### Bước 9 – Sinh PRD

> **Auto compact:** chạy `/compact` trước bước này. PRD là output lớn nhất; viết nhiều US liên tiếp trong context đầy dễ sót section.

Áp dụng `/generate-prd`. Dùng `.claude/_templates/prd/Template.md`.

Input: BRD (Gate 1) · Impact Matrix (Gate 2) · Solution decision (Gate 3) · project-context · Figma nếu có.

**Ba giai đoạn:**

**9A — Khung + danh sách US.**
Dựng phần đầu PRD: bảng metadata · Document version · Problem · Analytics · Objective · Stakeholder · Information · Metrics success · Solution (TDD/Database/API).
Rút danh sách US từ BRD đã duyệt, gắn nguồn (yêu cầu nào / impact nào / coverage gap nào).
**→ Điểm dừng: confirm danh sách US trước khi viết chi tiết.**

**9B — Field Intake.**
**Tra Impact Matrix + KB + DB + Swagger trước** để biết field/màn nào **đã tồn tại** — hiện hữu thì chỉ hỏi delta và migration, không coi là mới.
Gom **một bảng** hỏi người dùng: field · rule chi phối · validate · visibility · edit constraint · filter/search/sort (màn danh sách).
Pre-fill `[đề xuất]`, chỗ chưa rõ → `❓BA` hoặc Open Question.
**→ Điểm dừng: chỉ viết chi tiết khi đã đủ.**

**9C — Viết chi tiết từng US.**
Viết liên tục, không dừng giữa từng US (trừ US rủi ro cao → review riêng).
Mỗi US đủ: User story → Pre-Condition → Scenario → Acceptance criteria (bảng UI/UX + Business rule + Data Field + NFR) → Out of scope.
**`Conner case` để trống — QA điền.**
Mỗi business rule gắn mã `BR-<số US>.<số thứ tự>`. Rule chạm tính năng có sẵn → dẫn mã rule trong KB.

Output: `docs/prd/prd-<feature>-v0.1-YYYYMMDD.md`

Tự review theo `.claude/checklist/generate-prd.md` trước khi trình bày.

---

## GATE 4 – Duyệt PRD

Trình bày:

- Tóm tắt từng US và điểm đáng chú ý
- Business rule mới đặt ra · rule hiện có bị chạm
- Field / bảng / endpoint bị ảnh hưởng
- Mục đã xoá vì không áp dụng (Metrics success, NFR…)
- Open question còn lại

Ba lựa chọn như trên. `Need Revision` → feedback trỏ **mã cụ thể** (US-ID + BR/field/màn) để sửa nhắm đích, không viết lại cả PRD.

Duyệt xong → gợi ý publish lên Lark qua `/publish-lark` (**hỏi trước, người dùng có thể skip**).

---

## Sau PRD

| Việc | Lệnh |
|---|---|
| Review lại tài liệu | `/review-output` |
| Đẩy lên Lark | `/publish-lark` — hỏi xác nhận trước, có thể skip |
| Bổ sung / đổi yêu cầu | `/change-request` |
| Viết User Guide sau khi dev xong | `/generate-user-guide` |

---

## Bổ sung yêu cầu giữa chừng

Khi người dùng đổi hoặc thêm yêu cầu sau khi đã có tài liệu — **không sửa lẻ tẻ**, dùng `/change-request`:

1. Ghi CR vào `working/raw-inputs/change-requests.md`
2. AI **đề xuất điểm re-entry** (tầng thấp nhất bị ảnh hưởng) → **người dùng confirm**
3. Chạy lại xuôi từ điểm đó ở **Update mode**: bump MINOR + Change Log, chỉ sửa phần bị ảnh hưởng
4. **Mọi Gate sau điểm re-entry phải duyệt lại**

> Chỉ cần nói trong cuộc trò chuyện ("tôi đổi yêu cầu…", "bổ sung…") — skill tự kích hoạt.

---

## Quy tắc chung trong toàn bộ workflow

- Luôn tách `Fact` / `Assumption` / `Open Question` / `Recommendation` trong mọi output
- **Không bịa.** Thiếu nhẹ → `Assumption`. Thiếu ảnh hưởng scope/rule/data/flow → `Open Question` và đánh dấu `Draft - Pending Confirmation`
- **Không sửa đè tài liệu người dùng đã xem; tạo version mới** (`v0.2`, `v0.3`). Trước khi sửa file trong `docs/` hay `working/`, tự hỏi **"người dùng đã đọc bản này chưa"** — rồi thì tạo file mới, chưa thì sửa tại chỗ.
  Mốc tăng version: **mỗi lần qua một Gate**, hoặc mỗi đợt người dùng trả lời một loạt câu hỏi. Không phải mỗi lần sửa một dòng.
  Version mới phải có mục **Lịch sử thay đổi** ghi đổi gì so với bản trước. Xem `CLAUDE.md` mục *Cách làm việc* để biết lần đã sai.
- Mỗi artifact ghi rõ nguồn input
- Không tự chốt quyết định thay người dùng; chỉ gợi ý dưới nhãn `Recommendation`
- **Gate decision phải rõ ràng.** Trả lời không rõ → hỏi lại, không suy đoán là duyệt
- **Mục không áp dụng thì xoá hẳn**, không để lại nội dung mẫu của template
- **`Conner case` là việc của QA** — PO/BA để trống
- **BRD scope rule:** BRD chỉ chứa vấn đề, mục tiêu, phạm vi, business rule mức nghiệp vụ — **không** chứa chi tiết màn hình, field, cơ chế hệ thống. Những thứ đó thuộc PRD `Specific Requirement`
- Ràng buộc sản phẩm: tính năng làm cho UpBase, nhưng **dữ liệu và hạ tầng thiết kế cho đa tenant**. Mọi hằng số cứng phải khai báo rõ là hardcode hay cấu hình được
