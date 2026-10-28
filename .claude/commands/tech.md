---
description: Điều phối phần Tech của intent theo AWS AI-DLC + plugin tech-workflow - Inception (reverse engineering, domain, units, contract, test case, delivery planning) rồi Construction cuốn chiếu theo Bolt (functional design, NFR, UI map, code generation, build and test). Đọc tech-state.md, chạy stage kế tiếp
argument-hint: [intent-slug] [tiếp tục | nhảy tới <stage> | bolt <Bnn> | mở rộng phạm vi <cả intent | USx,USy…>]
---
# /tech, điều phối phần Tech của intent

Chạy theo `engine/tech/protocol/tech-protocol.md` (bảng stage, điều chỉnh của sản phẩm). Stage AWS: đọc nguồn chuẩn file stage tương ứng trong `engine/tech/aidlc/stages/` trước.
Không tự quyết thay lead.

## 1. Chọn intent
- `git fetch` rồi rebase nhánh hiện tại lên `origin/main` trước khi đọc.
- Có slug: dùng.
- Không có slug: **menu tech lead — menu trước, quét sau**. Gọi AskUserQuestion ngay (chưa đọc file nào), 4 lựa chọn, thứ tự cố định (gate chờ người khác chặn nhiều việc nhất):
  1. **Chờ duyệt** — Tìm gate `[?]`, contract chờ BE lead ký, review READY chưa mở gate.
  2. **Đang làm** — Tìm stage `[-]` / `[R]`.
  3. **Intent mới** — Tìm intent PO đã duyệt gate 2.43 Design Alignment (`2.43 [x]`) chưa có `tech-state.md`, hoặc PRD lên version sau lần khởi tạo.
  4. **Construction** — Tìm Bolt cần thiết kế (Bolt phụ thuộc đã qua 3.5 plan) hoặc Bolt code xong chờ 3.6.
  Mô tả chỉ nói sẽ tìm gì, không khẳng định có việc (không con số, không `(Recommended)`); có / không có chỉ nói sau khi quét.
  Chọn xong mới quét `intents/*/` (chỉ đọc, chỉ phần của nhóm đó: `tech-state.md` cho 1, 2, 4; `state.md` PO cho 3) → AskUserQuestion danh sách intent / Bolt (description: stage hiện tại, ai đang chờ, ngày; tối đa 3 + "Intent khác" để gõ slug). Nhóm rỗng: báo và hỏi lại menu → chạy với slug (và `bolt <Bnn>` nếu chọn Bolt).

## 2. Khởi tạo
Chưa có `tech-state.md` ở gốc intent: kiểm `state.md` PO có **2.43 design-alignment `[x]`** (chưa thì dừng, báo PO: Tech vào việc sau khi Decision Brief đã ký). Đọc `inception/tech-design/tech-design.md` — mục 0 phải kết luận ĐỦ, mục 8 không còn dòng Chặn nào chưa chốt; còn thì dừng và nêu các dòng đó. Có thì tạo từ
`engine/tech/templates/state.md`, điền version PRD và version Tech Design 1, commit, lead theo `engine/tech/knowledge/system-map.md`; hỏi tech lead tác giả
(FE lead hay BE lead), danh sách dev code của team (owner Bolt, năng lực ngày công) và phạm vi đợt này. **Mặc định phạm vi = cả intent** (mọi US trừ US "chưa làm") để 2.9 chia đủ Bolt giao cho team; chỉ chọn một lát US khi chạy thử hoặc PO tách đợt release (ghi lý do vào `decisions.md` (mã `DEC-T<n>`)).

## 3. Định tuyến
0. `mở rộng phạm vi …`: sửa dòng "Phạm vi đợt này" trong `tech-state.md` (cả intent = mọi US trừ US "chưa làm"), hỏi danh sách dev + năng lực nếu chưa có, ghi `DEC-T` vào `decisions.md`; mở lại `[R]` 2.6, 2.7, 2.8, 2.81, 2.9; Bolt đã qua 3.5 plan giữ nguyên số (Bolt mới đánh số tiếp). Rồi chạy 2.6 `[R]`.
1. Stage `[?]`: trình lại gate.
2. Stage `[-]` / `[R]`: tiếp tục chỗ dở.
3. PRD lên version mới sau khi Tech đã vào việc: báo stage nào bị ảnh hưởng, đề xuất mở lại `[R]`; điểm cần PO chốt đi qua Decision Brief hoặc `/change-request`.
4. Inception: stage `[ ]` đầu tiên theo bảng trong `tech-state.md`. Cặp song song (2.81 + 2.9): hỏi người dùng chọn.
5. Inception xong: Construction theo `bolt-plan.md`. Lấy Bolt đầu tiên chưa "Xong" mà Bolt phụ thuộc đã qua 3.5 plan; với các Unit của Bolt
   chạy 3.1 → (3.2, 3.3, 3.4 nếu điều kiện) → 3.41 (Unit có UI) → 3.5 → 3.6. Ghi tiến độ từng Unit ở mục Construction của `tech-state.md`.
6. Mọi Bolt "Xong": intent xong phần Tech; gợi ý PO `/generate-user-guide`.

Stage command: `engine/tech/stages/<slug>.md` — reverse-engineering, domain-design, units-generation, contract-design,
test-cases, delivery-planning, functional-design, nfr-requirements, nfr-design, infrastructure-design, ui-map, code-generation, build-and-test.

## Luôn
- Một stage mỗi lượt, kết thúc ở gate.
- PRD đổi version giữa chừng (CR của PO): báo stage Tech nào bị ảnh hưởng, đề xuất mở lại.
