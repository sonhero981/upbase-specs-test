# Clarify Requirements – Làm rõ yêu cầu từ input thô

Dùng khi input còn thô, thiếu, mâu thuẫn, lẫn giải pháp vào yêu cầu, hoặc chưa đủ để viết BRD.

**Tương đương Bước 2–3 trong `/po-workflow`.**

---

## Đầu vào

`$ARGUMENTS` — tên project hoặc input cụ thể.

> **Xác định project:** ưu tiên `$ARGUMENTS`; không có → suy từ file đang mở; >1 khả dĩ → liệt kê cho chọn, **không đoán**. **Echo + confirm trước khi chạy.**

Đọc theo thứ tự:

1. `project-context.md` · `project-decisions.md`
2. `working/raw-inputs/` — email, meeting note, mô tả yêu cầu
3. `working/meeting-notes/`
4. Artifact đã có trong `docs/`
5. `.claude/_shared-knowledge-base/00-index.md` → KB liên quan

Chưa xác định được project → hỏi trước khi tiếp tục.

---

## Cách làm

### 1. Chuẩn hoá input

Tách input thô thành các nhóm:

| Nhóm | Nội dung |
|---|---|
| Stakeholder request | Ai yêu cầu, yêu cầu gì |
| Problem | Vấn đề thật đằng sau yêu cầu |
| Expected outcome | Kết quả họ mong đợi |
| Users / roles | Ai dùng |
| Systems / modules / screens | Chạm tới đâu |
| Constraints / dependencies | Ràng buộc, phụ thuộc |
| **Proposed solution** | Giải pháp người yêu cầu đã nghĩ sẵn |

> ⚠️ **Tách `Proposed solution` ra khỏi `Problem`.** Stakeholder thường mô tả giải pháp thay vì vấn đề — *"cho tôi thêm nút export"* là giải pháp, vấn đề có thể là *"không lấy được dữ liệu ra ngoài để đối chiếu"*. Giải pháp họ đưa ra là **`Recommendation`**, không phải yêu cầu đã chốt.

### 2. Phân loại mọi mệnh đề

| Nhãn | Nghĩa |
|---|---|
| `Fact` | Có trong input hoặc tài liệu — ghi rõ nguồn |
| `Assumption` | Suy luận chưa xác nhận |
| `Open Question` | Cần trả lời trước bước sau |
| `Recommendation` | Gợi ý của AI hoặc giải pháp stakeholder đề xuất — chưa phải quyết định |

### 3. Bảng requirement candidates

| ID | Requirement Candidate | Type | Source | Confidence | Notes |
|---|---|---|---|---|---|

**Type:** Business · Process · Functional · Data · Screen-Report · API-Integration · Role-Permission · Business Rule · NFR

**Confidence:**
- `High` — rõ và có nguồn
- `Medium` — được nhắc tới nhưng thiếu chi tiết
- `Low` — suy luận hoặc mơ hồ

### 4. Đối chiếu KB — bước này tạo giá trị lớn nhất

Với mỗi requirement candidate, tra KB xem:

| Câu hỏi | Tra ở đâu |
|---|---|
| Tính năng này **đã có chưa**? | KB `01`–`11` |
| Có **rule hiện tại** nào chi phối không? | KB, mã `BR-*` / `KB-*` |
| Có **đang ẩn** (`hidden`) không? | KB `00-index` §Trạng thái |
| Vùng này KB **đã phủ chưa**? | KB `14-api-surface.md` §1–2 |

> Phát hiện yêu cầu **trùng với thứ đã có** → nêu ngay ở bước này, đừng để tới Impact Analysis. Ví dụ: yêu cầu "thêm thông báo khi chấm xong" — KB `13-mail-events.md` cho thấy mail #19 đã tồn tại nhưng **đang tắt**. Đó là bài toán bật lại, không phải làm mới.
>
> Vùng KB chưa phủ (lịch dạy, phòng học, thi cử, phân quyền) → ghi `❓BA`, **không kết luận là chưa có**.

### 5. Tách scope sơ bộ

- `In Scope`
- `Out Of Scope`
- `Potential Scope`

### 6. Bảng open questions

| ID | Question | Why It Matters | Suggested Owner | Blocks Next Step? |
|---|---|---|---|---|

Đặt `Blocks Next Step? = Yes` khi thiếu câu trả lời ảnh hưởng tới: **scope · business rule cốt lõi · user/role · dữ liệu bắt buộc · tích hợp quan trọng · phân quyền**.

**Không đặt câu hỏi kỹ thuật cho Dev.** Hiệu năng truy vấn, cấu hình phân quyền, cách lưu trữ, chịu tải bao nhiêu — đó là việc Dev tự xác định khi làm, và hỏi sớm chỉ tạo danh sách chờ không ai trả lời. Chỉ hỏi khi **câu trả lời làm đổi phạm vi hoặc đổi business rule**, ví dụ *"cơ chế đồng bộ HRM đã có chưa"* đổi phạm vi, còn *"truy vấn chịu được cây sâu mấy cấp"* thì không.

Câu hỏi phải **cụ thể và trả lời được**. Tránh câu hỏi mở kiểu *"anh muốn tính năng này thế nào?"* — thay bằng *"khi học viên bị Block giữa lúc đang làm bài, bài đang làm xử lý ra sao: huỷ, giữ nguyên, hay vẫn cho nộp?"*

---

## Output

- `working/ai-drafts/clarified-requirements-YYYYMMDD.md`
- `working/open-questions/open-questions-YYYYMMDD.md`

Người dùng chỉ cần phân tích nhanh → trả structured summary trong chat, hỏi có cần lưu file không.

Tự kiểm theo `.claude/checklist/clarify-requirements.md` trước khi trả kết quả.

---

## Dừng khi

**Không sang bước viết BRD nếu còn blocking question về:** mục tiêu nghiệp vụ · phạm vi · user/role · business rule cốt lõi · dữ liệu bắt buộc · tích hợp quan trọng · phân quyền.

Sau khi trình bày, hỏi:

- Còn gì cần làm rõ thêm không?
- Sẵn sàng viết BRD chưa? → `/generate-brd`
