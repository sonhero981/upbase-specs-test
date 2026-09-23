# Hướng dẫn sử dụng UpLnD PO/BA AI Workflow

Hệ thống hỗ trợ PO/BA làm toàn bộ việc phân tích: từ yêu cầu thô → làm rõ → phân tích ảnh hưởng → chọn giải pháp → **PRD bàn giao** → User Guide sau khi dev xong.

Bạn giao tiếp với AI bằng tiếng Việt tự nhiên. **Không cần biết lập trình.**

---

## Mục lục

1. [Workflow này làm gì](#1-workflow-này-làm-gì)
2. [Cài đặt](#2-cài-đặt)
3. [Cấu trúc thư mục](#3-cấu-trúc-thư-mục)
4. [Chạy một dự án từ đầu đến cuối](#4-chạy-một-dự-án-từ-đầu-đến-cuối)
5. [Tham khảo lệnh](#5-tham-khảo-lệnh)
6. [Knowledge Base](#6-knowledge-base)
7. [Xử lý vấn đề thường gặp](#7-xử-lý-vấn-đề-thường-gặp)
8. [Đồng bộ Git](#8-đồng-bộ-git)

---

## 1. Workflow này làm gì

### Sinh ra 5 artifact, không phải một

| Giai đoạn | Artifact | Gate | Nơi lưu |
|---|---|---|---|
| 1. Làm rõ yêu cầu | Clarified Requirements + Open Questions | — | `working/ai-drafts/` |
| 2. Chốt hướng | **BRD** | **Gate 1** | `docs/brd/` |
| 3. Phân tích ảnh hưởng | **Impact Matrix** | **Gate 2** | `working/impact-analysis/` |
| 4. Chọn giải pháp | **Solution Comparison** | **Gate 3** | `working/solution-options/` |
| 5. Đặc tả | **PRD** | **Gate 4** | `docs/prd/` |
| Sau khi dev xong | User Guide | — | `docs/user-guide/` |

Chỉ **PRD** và **User Guide** là tài liệu bàn giao. Ba cái còn lại là bản phân tích nội bộ.

### Gate là gì

Gate là **điểm dừng bắt buộc**. AI không tự chuyển sang giai đoạn sau cho đến khi bạn duyệt rõ ràng.

> **Gate không phải để duyệt tài liệu — Gate để chặn sai sót ở từng tầng.**
> Nếu Impact Matrix sai mà không ai chặn, toàn bộ PRD viết trên nền sai, phát hiện ra thì phải làm lại hết.

Mỗi Gate có ba lựa chọn:

| Trả lời | Nghĩa |
|---|---|
| `Approved` | Ổn, đi tiếp |
| `Approved with Notes` | Duyệt kèm ghi chú — AI ghi vào `project-decisions.md` rồi đi tiếp |
| `Need Revision` | Cần sửa — nói rõ sửa gì, AI quay lại bước trước |

Trả lời không rõ → AI **hỏi lại**, không tự coi là duyệt.

### Ngoài 4 Gate còn 3 điểm dừng nhỏ

| Điểm dừng | Ở đâu | Bạn làm gì |
|---|---|---|
| Chốt phạm vi liên quan | Bước 5 | Xem bản đồ tính năng bị chạm, bổ sung chỗ AI sót |
| Confirm danh sách US | Bước 9A | Duyệt danh sách User Story trước khi AI viết chi tiết |
| Field Intake | Bước 9B | Trả lời bảng hỏi về field, rule, validate |

---

## 2. Cài đặt

### 2.1 VS Code + Claude Code

1. Tải VS Code: https://code.visualstudio.com
2. Trong VS Code, nhấn `Ctrl+Shift+X` (Windows) / `Cmd+Shift+X` (Mac) → tìm **Claude Code** của **Anthropic** → Install
3. Click icon Claude ở thanh bên trái → **Sign in with Anthropic**
4. Kiểm tra: gõ `Xin chào` vào ô chat, AI trả lời tiếng Việt là được

### 2.2 Git

- **Windows:** https://git-scm.com/download/win — giữ mặc định, chỉ chọn *"Use Visual Studio Code as Git's default editor"*
- **Mac:** đã có sẵn, hoặc `xcode-select --install`

Cấu hình một lần:

```bash
git config --global user.name "Tên của bạn"
git config --global user.email "email@upbase.vn"
```

### 2.3 Mở đúng thư mục

**Bắt buộc:** File → Open Folder → chọn thư mục **`po-workflow-upbase`**.

Claude Code chỉ đọc được file trong thư mục đang mở. Mở sai thì AI không tìm thấy KB và các lệnh sẽ không chạy đúng.

Kiểm tra: panel Explorer bên trái hiện `po-workflow-upbase`, bên dưới có `.claude/` và `CLAUDE.md`.

### 2.4 Chụp màn hình cho User Guide (tuỳ chọn)

`.mcp.json` đã cấu hình sẵn Playwright. Lần đầu mở project, Claude Code sẽ hỏi approve MCP server — chọn đồng ý. Không dùng cũng không sao, khi viết User Guide gõ `skip-screenshot`.

---

## 3. Cấu trúc thư mục

```
po-workflow-upbase/
├── CLAUDE.md                      ← AI đọc mỗi phiên: phạm vi, quy ước, nguồn tra cứu
├── HUONG-DAN-SU-DUNG.md           ← file này
└── .claude/
    ├── commands/                  ← 11 lệnh
    ├── checklist/                 ← tiêu chí AI tự kiểm trước khi trả kết quả
    ├── _templates/                ← mẫu tài liệu
    ├── _shared-knowledge-base/    ← KB sản phẩm, 16 file
    └── projects/
        └── <tên-dự-án>/
            ├── project-context.md     ← bạn điền thông tin nền
            ├── project-decisions.md   ← log quyết định đã chốt
            ├── working/               ← bản phân tích nội bộ
            │   ├── raw-inputs/            ← ĐẶT TÀI LIỆU ĐẦU VÀO Ở ĐÂY
            │   ├── ai-drafts/
            │   ├── open-questions/
            │   ├── meeting-notes/
            │   ├── impact-analysis/
            │   └── solution-options/
            └── docs/                  ← tài liệu chính thức
                ├── brd/
                ├── prd/
                └── user-guide/
```

### Hai file quan trọng nhất trong mỗi dự án

**`project-context.md`** — AI đọc đầu tiên ở mọi lệnh. Điền càng đầy đủ thì AI càng ít hỏi lại.

**`project-decisions.md`** — AI tra file này để **không hỏi lại câu đã có đáp án**. Đây là bộ nhớ của dự án. **Đừng xoá.**

---

## 4. Chạy một dự án từ đầu đến cuối

### Bước 0 — Tạo dự án

```
/new-project Phan-quyen-mentor-cham-diem
```

Tên do bạn tự đặt, không có format bắt buộc.

Sau đó:
1. Mở `project-context.md` từ Explorer, điền Background · Objectives · Stakeholders
2. Đặt tài liệu đầu vào (email, meeting note, mô tả yêu cầu) vào `working/raw-inputs/`

### Bước 1 — Khởi động workflow

```
/po-workflow Phan-quyen-mentor-cham-diem
```

AI echo lại dự án đã chọn và hỏi bắt đầu từ đâu. Trả lời `Bước 1`.

> **Làm nhiều dự án song song:** luôn nêu tên dự án trong lệnh để tránh nhầm.
> **Tiếp tục dự án đang dở:** gõ cùng lệnh, AI tự đọc artifact đã có rồi hỏi tiếp từ đâu.

### Bước 2–3 — Làm rõ yêu cầu

AI phân tích input và tạo hai file: bảng requirement candidates và bảng open questions.

Bạn trả lời câu hỏi **viết tự nhiên trong chat**, không cần format:

```
Rule này chỉ áp cho mentor chính, mentor thường không thấy nút.
Bài đã chấm xong thì không cho assign lại.
Không cần thông báo email, giai đoạn này làm thủ công.
```

AI lặp lại cho đến khi hết **blocking question** — câu hỏi mà thiếu đáp án thì không viết BRD chính xác được.

### Bước 4 + Gate 1 — BRD

AI viết BRD rồi trình bày: Problem · Analytics · Objective · Scope · danh sách US dự kiến.

Bạn trả lời `Approved` / `Approved with Notes` / `Need Revision`.

### Bước 5–6 + Gate 2 — Impact Matrix

**Bước 5:** AI quét KB + DB + API rồi trình bản đồ tính năng bị chạm. Bạn xem và bổ sung chỗ sót. Đây là lúc dễ đóng góp nhất — bạn chỉ cần **nhận ra cái thiếu**, không phải nhớ từ đầu.

**Bước 6:** AI dựng Impact Matrix — quét 12 vùng, tìm conflict, tìm FR/NFR còn thiếu, tìm coverage gap.

Trình Gate 2 kèm **phụ lục nguồn đã đọc** — để bạn biết phân tích dựa trên gì và **thiếu gì**.

### Bước 7–8 + Gate 3 — Solution

AI hỏi bạn đã có định hướng chưa.

- **Có** → AI nhận xét định hướng đó, gợi ý thêm option nếu cần
- **Chưa** → AI gợi ý 2–3 option

Rồi so sánh theo 7 tiêu chí và đưa `Recommendation` kèm điều kiện và risk.

### Bước 9 + Gate 4 — PRD

**9A:** AI dựng khung PRD và trình danh sách US → bạn confirm
**9B:** AI tra KB/DB/Swagger rồi gom **một bảng hỏi** về field, rule, validate → bạn điền
**9C:** AI viết chi tiết từng US

Trình Gate 4. Nếu `Need Revision`, nói rõ mã cần sửa:

```
US2 → BR-2.3 sai, mentor thường cũng xem được
US1 → bảng UI thiếu trạng thái disable của nút Assign
```

AI sửa nhắm đích, không viết lại cả PRD.

### Sau PRD

```
/publish-lark          → đẩy PRD lên Lark Wiki
/generate-user-guide   → viết User Guide (sau khi dev xong)
/change-request        → khi có thay đổi yêu cầu
```

---

## 5. Tham khảo lệnh

| Lệnh | Dùng khi |
|---|---|
| `/new-project <tên>` | Tạo dự án mới |
| `/po-workflow <tên>` | **Chạy toàn luồng** — dùng lệnh này là chính |
| `/clarify-requirements` | Làm rõ yêu cầu thô (Bước 2–3) |
| `/generate-brd` | Viết BRD (Bước 4) |
| `/impact-analysis` | Phân tích ảnh hưởng (Bước 5–6) |
| `/compare-solutions` | So sánh phương án (Bước 7–8) |
| `/generate-prd` | Viết PRD (Bước 9) |
| `/review-output` | Review tài liệu — **kể cả tài liệu người khác viết** |
| `/change-request` | Đổi hoặc bổ sung yêu cầu giữa chừng |
| `/publish-lark` | Đẩy tài liệu đã duyệt lên Lark |
| `/generate-user-guide` | Viết hướng dẫn người dùng sau khi dev xong |

> **`/change-request` tự kích hoạt** khi bạn nói *"tôi đổi yêu cầu…"*, *"bổ sung…"*, *"khách yêu cầu thêm…"* — không cần gõ lệnh.

### Đổi yêu cầu giữa chừng

Đừng sửa lẻ tẻ. AI sẽ:

1. Ghi CR vào `working/raw-inputs/change-requests.md`
2. **Đề xuất điểm re-entry** — tầng thấp nhất bị ảnh hưởng → bạn confirm
3. Chạy lại xuôi từ đó, chỉ sửa phần bị chạm, bump version, ghi Change Log
4. Mọi Gate sau điểm đó phải duyệt lại

---

## 6. Knowledge Base

16 file trong `.claude/_shared-knowledge-base/`. Bắt đầu từ `00-index.md`.

| Nhóm | File | Nội dung |
|---|---|---|
| Nghiệp vụ | `01`–`11` | Course · Question Bank · Assessment · Class · Grading · User · Learning Experience · Certificate · Notification · Storyline · Dashboard |
| Kỹ thuật | `12`–`14` | Data Model (85 bảng) · Mail Events (30 mail) · API Surface (708 operation) |
| Định hướng | `15` | UpLnD Platform, 4 portal, ràng buộc đa tenant |

### Quy ước ký hiệu

| Ký hiệu | Nghĩa |
|---|---|
| `BR-COURSE-01` | Business rule **có sẵn trong User Guide** — đáng tin |
| `KB-COURSE-01` | AI trích từ văn xuôi — **chưa được duyệt**, cần bạn xác nhận |
| `❓BA` | Chưa rõ — **không dùng làm căn cứ** |
| `[suy ra]` | AI suy luận, không phải câu chữ trực tiếp |
| **Hidden** | Tính năng **đã có code nhưng tạm ẩn** — vẫn phải xét khi phân tích |

### Ba giới hạn cần nhớ

**KB chỉ phủ khoảng một nửa hệ thống.** Ops có 25 nhóm chức năng và LMS có 8 nhóm không có trong User Guide — lịch dạy, phòng học, thi cử, phòng ban, phân quyền. Trước khi tin "vùng này không bị ảnh hưởng", xem `14-api-surface.md` §1–2.

**Rule `KB-*` chưa được duyệt.** 110 rule loại này do AI trích ra, cần bạn xác nhận trước khi dùng làm ràng buộc trong PRD.

**KB là bản chụp, không phải bản gốc.** Repo không giữ file nguồn — xem bảng `Nguồn` trong `00-index.md`:

| Loại | Nghĩa | Khi nghi ngờ |
|---|---|---|
| 🔄 **Nguồn sống** — schema DB ([Lark `Data Architecture`](https://upbasevn.sg.larksuite.com/wiki/MaFpweI68iKNMvkTioLlJ1uJgQd)), Swagger staging, GitBook | Có bản gốc ngoài repo | Bảo AI **đọc lại nguồn**. Yêu cầu chạm tới dữ liệu thì AI tự đọc lại, không cần nhắc |
| 📌 **Bản chốt** — 30 mail event, SIS | Không còn file gốc, KB chính là nguồn | AI sẽ **hỏi bạn**, không tự suy |

Nguồn sống nên **kiểm lại mỗi tháng một lượt**: mở phiên mới và bảo *"đọc lại schema DB trên Lark, đối chiếu với KB 12"*. Lệch thì AI cập nhật KB và sửa ngày "Đối chiếu lần cuối".

---

## 7. Xử lý vấn đề thường gặp

| Tình huống | Cách xử lý |
|---|---|
| AI chọn nhầm dự án | Nói *"sai rồi, tôi muốn làm dự án X"* — AI chuyển ngay |
| AI hỏi lại câu đã trả lời | Kiểm `project-decisions.md` — có thể quyết định chưa được ghi vào |
| AI viết dài, sai trọng tâm | Nhắc thẳng. AI có xu hướng mở rộng phạm vi — cứ kéo về |
| Tài liệu dài, AI bắt đầu sót | Gõ `/compact` rồi tiếp tục. Workflow tự chạy `/compact` trước Bước 6 và Bước 9 |
| Lark không kết nối được | AI sẽ hỏi bạn cấp quyền lại qua browser. Đây là việc bình thường, không phải lỗi |
| Không chụp được màn hình | Gõ `skip-screenshot`, AI để placeholder và liệt kê ảnh còn thiếu |
| Muốn biết AI dựa vào đâu | Hỏi thẳng. Mọi artifact đều có mục nguồn đã đọc |

### Khi AI nói "không chắc"

Đó là hành vi đúng. Workflow ép AI đánh dấu `❓BA` và `Open Question` thay vì đoán. Thấy nhiều `❓BA` nghĩa là yêu cầu còn thiếu thông tin — không phải AI kém.

---

## 8. Đồng bộ Git

```bash
# Lấy bản mới nhất
git pull

# Đẩy thay đổi
git add .
git commit -m "PRD tính năng phân quyền mentor chấm điểm"
git push
```

Xung đột khi pull → hỏi AI, đừng tự sửa tay nếu không quen.

> Repo này **không** dùng chung remote với `ba-ai` cũ (GitLab công ty trước). Kiểm tra bằng `git remote -v` trước lần push đầu tiên.
