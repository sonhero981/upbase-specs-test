# Bàn giao intent → Tech (OpenSpec)

Intent trong `.claude/intents/<slug>/` là **nguồn gốc requirement**. Tech chỉ đọc artifact đã qua gate; change OpenSpec
ở `openspec/` diễn giải lại để implement. Lệch nhau → artifact của intent thắng: sửa change hoặc hỏi PO, không tự chọn.

## 1. Khi nào Tech vào

| Mốc trong `state.md` | Tech làm gì |
|---|---|
| 2.41 `[-]` HLD Brief đang chạy | Tech lead viết mục 9 Technical Direction và dòng Dev ở mục 12 của `hld-brief.md`, chỉ sửa phần của mình |
| 2.41 `[x]` | Có thể bắt đầu Domain Design, Units, Contract (stage 2.6 → 2.8 phía Dev) |
| 2.42 `[x]` PRD đã duyệt | Được tạo change ở `openspec/changes/` |

Stage còn `[?]` hoặc `[R]` → artifact chưa chốt, không dùng làm input.

## 2. Đọc gì

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

Artifact của PO luôn đọc theo `main`: `git fetch` rồi rebase nhánh Tech lên `origin/main` trước khi đọc.
`git show origin/main:<path>` trên Git Bash cần `MSYS_NO_PATHCONV=1`.

## 3. Map intent → change

| Nguồn | Vào artifact | Ghi chú |
|---|---|---|
| Intent slug, version `prd.md`, Jira | `proposal.md` | Version là mốc để biết PRD đổi |
| Problem, Objective (`O`) | `proposal.md` — Why, tóm tắt | Không chép nguyên |
| Out of scope | `proposal.md` | |
| Bảng US | `proposal.md` — bảng US ↔ repo ↔ trạng thái (mục 4) | Gồm cả US ngoài đợt |
| `USn` — Acceptance criteria | `specs/<capability>/spec.md` — mỗi US 1 Requirement, mỗi dòng AC 1 Scenario đặt ID `USn-ACm` | Giữ chuỗi UI tiếng Anh trong backtick |
| `BR` | Requirement / Scenario, giữ mã | |
| `NFR`, Constraints | `design.md` — Constraints; NFR kiểm được thì thêm Scenario | |
| Technical Direction (HLD Brief mục 9) | `design.md` — điểm xuất phát | Tech lead đã ký, không viết ngược lại |
| Proto-Unit `PU` | Gợi ý chia Unit ở stage 2.7 | Tech chốt Unit thật |
| Data to Retain | `design.md` — data model | Shape thật lấy từ code lms-be |
| Conner case "(QA điền)" | Bỏ trống | Không tự bịa |

Đánh dấu: `❓BA`, `OQ` còn mở → `[NEEDS CLARIFICATION - …]`, giữ mã. `Assumption`, `[suy ra]` → Scenario gắn `(đề xuất)`.

## 4. Gate chống sót US

1. `N_list` = số dòng bảng Danh sách trong `stories.md` (kể cả "Đợt này? Không").
2. `N_detail` = số heading `## USn:` trong `prd.md`.
3. Lệch → flag cho user.
4. Bảng US trong `proposal.md` đúng `N_list` dòng, cột repo: học viên (UpLMS) → lms-fe · vận hành (UpLMS Ops) → ops-fe · không có màn hình → lms-be · ngoài đợt → `⏸ out-of-scope`.

US phía Ops ảnh hưởng hiển thị phía học viên → ghi vào spec lms-fe dạng "FE đọc cấu hình X từ API, X do Ops đặt".

## 5. PRD đổi sau khi đã có change

PO đổi qua change request (`CR`) và chụp bản cũ vào `archive/` của intent. Tech: so `archive/` với bản hiện tại,
chạy `/opsx:update <change>`, ghi version mới vào `proposal.md`.

## 6. Quyền

Tech không sửa file trong `.claude/intents/**`, trừ mục 9 và dòng Dev mục 12 của `hld-brief.md`. Thấy sai/thiếu →
ghi `[NEEDS CLARIFICATION - …]` và báo PO. Phần của Tech nằm ở `openspec/` và `.claude/knowledge/tech/`.
