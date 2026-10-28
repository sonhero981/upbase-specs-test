# Bàn giao intent → Tech

Intent trong `intents/<slug>/` là nguồn gốc requirement. Tech chỉ đọc artifact đã qua gate của PO; lệch nhau thì
intent thắng: sửa artifact Tech hoặc hỏi PO, không tự chọn. Luồng đầy đủ: `workflow.md`. Nghi thức: `engine/tech/protocol/tech-protocol.md`.

## 1. Khi nào Tech vào

| Mốc trong `state.md` của PO | Tech làm gì |
|---|---|
| 2.41 `[-]` HLD Brief đang chạy | Tech lead viết mục 9 Technical Direction và dòng Dev ở mục 12 của `hld-brief.md` |
| 2.42 `[x]` PRD đã duyệt | `/tech <slug>` → 2.43 PRD Readiness |

Stage PO còn `[?]` hoặc `[R]` → artifact chưa chốt, không dùng làm input. 2.41 `[S]` (không có HLD Brief): tech lead ghi Technical Direction ở `hld.md` mục 7.
Intent chuyển từ v1 thiếu `stories.md` / `hld-brief.md`: xem mục "Intent chuyển từ luồng v1" trong `tech-protocol.md`.

## 2. Đọc gì của PO

| File trong intent | Dùng cho |
|---|---|
| `intent.md` | Jira, link Lark, mapping họ mã (intent chuyển từ luồng cũ giữ họ mã cũ) |
| `state.md` | Trạng thái gate, version từng artifact |
| `inception/requirements-analysis/requirements.md` | `FR`, `NFR`, Constraints, Out of scope |
| `inception/user-stories/stories.md` | `US` ↔ `PU` ↔ `FR`, MoSCoW, đợt này |
| `inception/hld-brief/hld-brief.md` | Mục 4 giải pháp, 6 ảnh hưởng + rủi ro, 9 Technical Direction, 10 Test Strategy, 11 Release |
| `inception/prd/prd.md` | Acceptance criteria, `BR`, Data to Retain, Proto-Units, Traceability, Open Issues |
| `inception/impact-analysis/impact-matrix.md` | Vùng bị chạm, conflict |
| `decisions.md`, `design/` | Quyết định PO, ảnh màn + `order.txt` |

Luôn `git fetch` và rebase lên `origin/main` trước khi đọc. `git show origin/main:<path>` trên Git Bash cần `MSYS_NO_PATHCONV=1`.
Đánh dấu của PO: `❓BA`, `OQ` mở → câu hỏi ở 2.43; `Assumption`, `[suy ra]` → ghi `(đề xuất)` khi dùng.

## 3. Quyền

Tech ghi: `tech-state.md`, `decisions.md` (mã `DEC-T<n>`), `inception/{tech-design,domain-design,units-generation,contract-design,test-cases,delivery-planning}/`, `construction/`, `archive/` của intent; `openspec/`, `engine/tech/knowledge/`. Ngoài ra chỉ `inception/tech-design/tech-design.md`
của `hld-brief.md`. Không sửa file khác của PO; thấy sai thì đưa vào 2.43 hoặc báo PO chạy `/change-request`.
