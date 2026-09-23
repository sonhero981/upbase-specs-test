# Impact Analysis – Dựng Impact Matrix

Dùng sau khi BRD được Gate 1 duyệt, để phân tích đầy đủ ảnh hưởng trước khi chốt solution và viết PRD.

**Tương đương Bước 5–6 + Gate 2 trong `/po-workflow`.**

---

## Mục tiêu

1. **Phát hiện conflict** giữa tính năng mới và hệ thống hiện tại
2. **Bổ sung FR/NFR còn thiếu** do ảnh hưởng qua lại giữa mới và cũ
3. **Đảm bảo coverage** đủ case để solution đủ logic
4. **Xác định Transition Requirements** để golive an toàn
5. **Kiểm tra chiều tenant** — thay đổi có làm tăng chỗ đóng cứng cho UpBase không

> Output là **bản phân tích nội bộ**, không phải mục trong PRD. Kết quả chảy vào `Solution`, `Database`, `API`, `Data Field`, `Out of scope`.

---

## Đầu vào

`$ARGUMENTS` — tên project hoặc input cụ thể.

> **Xác định project:** ưu tiên tên trong `$ARGUMENTS`; không có → suy từ file đang mở; >1 project khả dĩ → liệt kê cho người dùng chọn, **không đoán**. **Echo + confirm trước khi chạy.**

Đọc theo thứ tự:

1. `docs/brd/brd-v*.md` — bản mới nhất đã qua Gate 1
2. `project-context.md` · `project-decisions.md`
3. `working/raw-inputs/` — context hệ thống người dùng đã bổ sung
4. PRD cũ liên quan trong `docs/prd/`
5. `.claude/_shared-knowledge-base/00-index.md` → các file KB liên quan
6. `.claude/_templates/impact-matrix/Template.md` — cấu trúc output

### Bốn nguồn tra cứu bắt buộc

| Cần gì | Nguồn |
|---|---|
| Business rule, luồng nghiệp vụ, tính năng ẩn | KB `01`–`11` |
| Bảng, khoá ngoại, quan hệ | KB `12-data-model.md` + `UpLnD DB Diagram.html` |
| **Field, kiểu dữ liệu, required, enum** | Swagger `components.schemas` — **nguồn tốt nhất cho field-level** |
| Endpoint đã có | `lms-be.staging.upbase.asia/api/v1/docs-json` · `ops-be.staging.upbase.asia/api/v1/docs-json` |
| Mail tự động theo event | KB `13-mail-events.md` |
| **Vùng KB chưa phủ** | KB `14-api-surface.md` §1–2 — **đọc trước khi kết luận "không ảnh hưởng"** |
| Chỗ đóng cứng UpBase | KB `15-product-direction.md` §6 |

> ⚠️ **KB dựng từ User Guide chỉ phủ khoảng một nửa hệ thống.** Ops có 25 nhóm API và LMS có 8 nhóm không có trong UG (lịch dạy, phòng học, thi cử, phòng ban, phân quyền). Trước khi kết luận một vùng "không bị ảnh hưởng", kiểm tra `14-api-surface.md` xem vùng đó có nằm trong phần KB chưa phủ không. Nếu có → ghi `❓BA`, không kết luận.

---

## Bước 5 – Chốt phạm vi liên quan

Trước khi phân tích, **chủ động quét** rồi trình **"Related Features & Docs Map"**:

| Hệ | Tính năng / Module / Entity / Endpoint | New / Existing | Nguồn | Ghi chú |
| --- | --- | --- | --- | --- |
| UpLMS / Ops | | New / Existing | KB 04 §3 · bảng `classes` · `GET /api/v1/classes` | `❓BA` nếu chưa chắc |

Bao quát: module/feature · màn hình · data model/entity · API/integration/job · role & permission · business rule hiện tại · NFR/constraint · **mail event liên quan**.

Trình người dùng confirm: **đủ chưa · có sót · dòng nào không liên quan · KB/PRD cũ nào nên đọc thêm.**

Mục `❓BA` — giả định về hệ thống cũ, dữ liệu cũ, cơ chế — **phải được chốt**, không để trôi vào matrix dưới dạng đoán.

> **Recognition > recall:** người dùng review và bổ sung một bản nháp, không phải nhớ từ đầu.
> Map này là đầu vào cho STEP 1. Field/màn **Existing** phải nhận diện ở đây để không bị coi là "mới" ở bước sau.
>
> **Caveat:** nếu `project-context` và KB quá mỏng, hỏi người dùng **seed trước** danh sách hệ thống liên quan rồi AI mở rộng.

**Không dựng Impact Matrix cho đến khi phạm vi được chốt.**

---

## Bước 6 – Phân tích theo framework

### STEP 1 — Extract Current Situation

Đọc input để rút ra bức tranh hệ thống hiện tại **liên quan đến thay đổi**.

> **Mindset:** đọc để tìm **dependency**, không phải để hiểu feature.

| Loại | Cần tìm | Tra ở đâu |
|---|---|---|
| Module / Feature | Module hiện hữu bị chạm | KB 01–11 |
| Data / Entity / Field | Bảng, field, khoá ngoại liên quan | KB 12 + Swagger schemas |
| Business Rule | Rule / invariant hiện tại | KB, mã `BR-*` và `KB-*` |
| Process / Workflow | Approval, flow hiện tại | KB 01–11 |
| Permission | Model phân quyền | KB 06 §9 · `casbin_rule` |
| Integration / Consumer | Hệ đang phụ thuộc | KB 14 · mail event KB 13 |
| **Tính năng ẩn** | Page `hidden` bị chạm | KB 00-index §Trạng thái |

> ⚠️ **Tính năng `Hidden` vẫn phải xét.** Đã có code, chỉ tạm ẩn. Đây là nhóm dễ bỏ sót nhất. 5 page đang ẩn: Storyline · Quản lý bài kiểm tra trong lớp · Notification & Email List · Recipients List · Mail Logs.

### STEP 2 — Extract Desired Situation

Từ BRD rút ra: tính năng mới làm gì · process mới ra sao · FR/NFR đã có.

### STEP 3 — Impact & Gap Analysis

**3.0 — Impact Matrix, quét 12 vùng** (New → Old):

| Vùng | Ví dụ cần kiểm |
|---|---|
| Business process | Quy trình vận hành, approval flow |
| Module / function | Feature mới, đổi behavior hiện tại |
| Screen / report | UI mới, layout đổi, báo cáo đổi |
| Data | Bảng/field mới, đổi kiểu, migration |
| API | Endpoint mới, đổi contract, breaking change |
| Role / permission | Ai được làm gì, policy Casbin |
| Business rule | Rule hiện tại bị mâu thuẫn hoặc phải sửa |
| NFR | Hiệu năng, tải, bảo mật |
| **Notification / Email** | Mail event nào bị chạm — tra KB 13 |
| Reporting | Dashboard, export, SIS |
| Test | Vùng cần test lại |
| Release | Thứ tự deploy, phụ thuộc |

Mỗi dòng ghi **severity** (High / Medium / Low) + **nguồn**.

**3a — Conflict Detection** (4 chiều): business rule · process · data · permission.
Phát hiện conflict → **escalate cho người dùng quyết, KHÔNG tự resolve**.

**3b — Bidirectional Impact**: New→Old và **Old→New**.
Chiều Old→New hay bị bỏ: tính năng cũ ràng buộc gì lên tính năng mới.
FR/NFR phát sinh → **feed ngược vào BRD**.

**3c — Coverage Check**: boundary · exception · shared entity · side effect.
Tìm case chưa được định nghĩa → FR bổ sung.

> **Shared entity là chỗ dễ vỡ nhất của hệ này.** `course_categories` là khoá ngoại của 6 bảng (`courses`, `users`, `staffs`, `quizzes`, `certificates`, `support-groups`). Question Bank được tiêu thụ bởi Test, Quiz, Case Study, Storyline. Chạm vào chúng là chạm nhiều nơi.

### STEP 4 — Transition Requirements

| Loại | Nội dung |
|---|---|
| **Data** | Migration, backfill, dữ liệu cũ xử lý sao |
| **Compatibility** | Bản cũ và mới chạy song song được không |
| **Cutover** | Thứ tự bật, rollback, ẩn/hiện khi golive |

### STEP 5 — Kiểm tra chiều tenant

Đối chiếu `15-product-direction.md` §6:

| Câu hỏi | Ghi vào matrix |
|---|---|
| Thay đổi này có nhúng thêm logic riêng của UpBase vào code không? | Nếu có → ghi rõ, đề xuất cách tách |
| Có hằng số cứng mới không (số ngày, ngưỡng, danh mục cố định)? | Khai báo rõ: hardcode hay cấu hình được |
| Bảng mới có `tenant_id` không? | Bảng thiếu `tenant_id` là rủi ro rò rỉ dữ liệu |
| Enum/danh mục mới do hệ thống định nghĩa hay tenant tự định nghĩa? | |

---

## Output

`working/impact-analysis/impact-matrix-v0.1-YYYYMMDD.md` theo `.claude/_templates/impact-matrix/Template.md`.

Thiếu context để đánh giá một bước → **tạo Open Question, không giả định**.

Tự kiểm theo `.claude/checklist/impact-analysis.md` trước khi trình bày.

---

## Trình bày tại Gate 2

- Tóm tắt vùng bị ảnh hưởng theo severity
- **Conflict** phát hiện được — escalate, không tự resolve
- **FR/NFR còn thiếu** — feed ngược vào BRD
- **Coverage gap** — case chưa định nghĩa
- **Transition Requirements**
- **Chỗ đóng cứng tenant** bị tăng thêm
- Risk đáng chú ý · Open question còn lại
- **Phụ lục: nguồn đã đọc** — KB nào, bảng nào, endpoint nào. Để người dùng biết phân tích dựa trên gì và thiếu gì.

Ba lựa chọn: `Approved` / `Approved with Notes` / `Need Revision` (quay lại Bước 5).
