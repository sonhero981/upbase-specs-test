---
intent: 260923-gamification
artifact: prd-readiness
version: 1.2
status: approved
approved_at: 2026-10-13 ([GIẢ LẬP] BE lead, DEC-T18)
prd_version: 0.14 + câu trả lời Q1–Q17 (chưa CR, DEC-T4, DEC-T17)
result: READY
scope: cả intent (DEC-T15); v1.0 READY cho US14, US15 giữ nguyên
---
# PRD Readiness: Gamification — cả intent (19 US)

PRD `inception/prd/prd.md` version 0.14 (approved 2026-10-12, commit 18ba56a) · kiểm ngày 2026-10-13 · người kiểm FE lead Nguyễn Hùng Sơn (tech lead tác giả) · phạm vi đợt này US14, US15 (`tech-state.md`, DEC-T2)

## Kết luận
**READY cả intent** (v1.2, lần kiểm lại Lô 2, cuối file). Lần kiểm mở rộng phạm vi 2026-10-13 (DEC-T15) ra NOT READY cho 17 US mới; PO (giả lập) trả lời Q5–Q17 thì hết chặn. US14, US15 vẫn READY (v1.0), B01 không bị ảnh hưởng.

Lát Nền tảng (v1.0): **READY** (lần kiểm lại 2026-10-13, xem cuối file). Lần đầu: **NOT READY**. Hai chỗ chặn thiết kế: quyền xem danh sách và kết quả campaign mâu thuẫn với vị trí của danh sách campaign (RD1), và "bật `Visibility in UpLMS` lần đầu" chưa rõ nghĩa, quyết định có phải lưu thêm dữ liệu hay không (RD2). Phần còn lại của US14, US15 đủ để viết thiết kế.

## Checklist
| # | Tiêu chí | Đạt | Ghi chú |
|---|---|---|---|
| R1 | Mọi US có Pre-condition, Scenario, Acceptance criteria | Đạt | US14, US15 đủ ba mục; Conner case để QA điền (2.81) |
| R2 | AC kiểm chứng được | Không | RD2 "lần đầu" mơ hồ, đổi dữ liệu; RD4 chuỗi popover trống |
| R3 | Business rule có mã, không mâu thuẫn | Không | RD1: `BR-15.7` cho quyền `Xem danh sách học viên và hạng` xem danh sách campaign, nhưng danh sách nằm trong trang cấu hình mà quyền này không mở được; RD5 AC menu lệch `BR-15.3` |
| R4 | Data to Retain đủ để suy ra entity | Đạt (trừ RD2) | Hai công tắc, múi giờ theo tenant, `tenant_id`; US15 không có field mới |
| R5 | Quyền tách rõ | Không | RD1 |
| R6 | Rỗng, lỗi, giới hạn | Đạt | Lưu lỗi `BR-14.11`, `BR-14.12`; không có danh sách nên không có phân trang |
| R7 | Dữ liệu cũ và migration | Đạt có giả định | `BR-14.6` nói tổ chức mới; tổ chức đang chạy lúc lên bản giả định tắt hẳn (RD6, Q4) |
| R8 | NFR đo được | Nên sửa | RD3: "giữ sẵn trong bộ nhớ" chưa nói tắt công tắc có hiệu lực sau bao lâu |
| R9 | Design | Nên sửa | Có `design/Gamification - Enable - Setting.png`, `Gamification - Disable.png`; thiếu hai popover, báo `Saved`, trạng thái mở thẳng đường dẫn khi không có quyền (RD4) |
| R10 | Không còn `❓PO` / `OQ` chặn | Không | `OQ-50` chuỗi hai popover (RD4); `OQ-42` tắt khi có campaign chạy — ngoài lát (RD7) |
| R11 | Traceability | Đạt, truy vết tay | `S12` → US14, `S13` → US15, `S21` → US14 (PRD "Truy vết phạm vi trong BRD sang US") |

## Finding
| Mã | Mức | Vị trí | Vấn đề | Cần PO làm gì |
|---|---|---|---|---|
| RD1 | Chặn → Đã giải (Q1) | US15 · `BR-15.7` dòng "Danh sách campaign (US20): xem" và "Kết quả campaign (US21)" · `BR-15.8` · design `Gamification - Enable - Setting.png` khối Campaign | Quyền `Xem danh sách học viên và hạng` được xem danh sách và kết quả campaign, nhưng danh sách campaign là khối cuối của trang cấu hình, và cùng bảng nói quyền này **không** xem được trang cấu hình. Chưa rõ người chỉ có quyền này mở campaign từ đâu; quyết định route, menu, guard của Ops | Trả lời Q1 |
| RD2 | Chặn → Đã giải (Q2) | US14 · AC "Xác nhận khi bật công tắc 2 lần đầu" · `BR-14.13` | "Lần đầu" là lần đầu trong đời tổ chức hay mỗi lần bật lại. Nếu là đời tổ chức thì phải lưu mốc đã từng bật (dữ liệu mới) | Trả lời Q2 |
| RD3 | Nên sửa → Đã giải (Q3) | US14 · NFR | "Giữ sẵn trong bộ nhớ" không nói thời gian hiệu lực khi tắt / bật; `BR-14.5` "tính từ thời điểm bật" cần biên rõ khi có cache ở nhiều service | Trả lời Q3 |
| RD4 | Nên sửa → Đã giải (PO bổ sung) | US14 · AC hai popover, báo `Saved` · US15 AC "mở thẳng đường dẫn cũng không vào được" | Chuỗi tiếng Anh hai popover còn `❓PO` (`OQ-50`); chưa có design popover, `Saved`, màn hoặc thông báo khi không có quyền | Bổ sung, xem "Việc PO cần bổ sung" |
| RD5 | Ghi nhận | US15 · AC "Menu Ops · Khu vực Gamification" | AC ghi "không có quyền **xem**" còn `BR-15.3` ghi "không có quyền nào trong **ba** quyền". Tech theo `BR-15.3` | Sửa câu AC khi có CR |
| RD6 | Ghi nhận → Đã giải (Q4) | US14 · `BR-14.6` | Chỉ nói tổ chức mới; tổ chức đang chạy lúc lên bản giả định tắt hẳn | Xác nhận Q4 |
| RD7 | Ghi nhận | US14 · AC popover tắt công tắc 1 (số campaign đang chạy) · `OQ-42` | Phụ thuộc campaign (US20) ngoài lát: lát này popover chưa có phần campaign | — |
| RD8 | Ghi nhận | Metadata PRD · `OQ-10` | `Tech lead`, `QA` còn trống; Tech lead intent: Nguyễn Hùng Sơn (FE lead) | Điền metadata |

**Phụ thuộc ra ngoài lát** (tech lead chốt trước 2.6, Assumption A1–A5):
- `BR-14.7` khoá bốn công tắc chức năng US8–US11: lát này trang cấu hình chỉ có khối chung; các khối sau gắn vào khi tới Unit của chúng.
- `BR-14.3` chạy ngầm ghi nhận điểm, huy hiệu, hạng: lát này chưa có gì để ghi nhận; hiệu lực của công tắc chỉ kiểm được qua trạng thái đọc từ API cho tới Unit Điểm.
- `BR-14.9` múi giờ dùng cho US5, US6: lát này chỉ lưu và đọc được múi giờ tổ chức.
- US15 quyền `Xem danh sách học viên và hạng` phục vụ US12, US21, US22: lát này khai báo quyền, màn đến sau.
- `BR-15.8` khối Campaign chỉ xem khi tắt `Gamification`: theo US20, ngoài lát.
- `Visibility in UpLMS` quyết định học viên thấy gì ở UpLMS (US1…): lát này lms-fe chỉ đọc được trạng thái hiển thị, chưa có màn.

## Rủi ro kỹ thuật thấy sớm
1. **`tags: []` làm route mới mở cho mọi staff.** Quy ước lms-be `openspec/conventions/backend.md` § 2 bắt `tags: []`; `libs/modules/src/lib/scan-operation/scan-operation.service.ts:101` lấy `group` từ `tags`, và `libs/modules/src/lib/permission/permission.service.ts:94-105` cho qua route chưa có rule trong Casbin. Tới khi quản trị gán quyền, mọi staff gọi được API cấu hình — trái `BR-15.3` ở tầng API. BE lead quyết ở 2.6 (system-map BE-1).
2. **Mã quyền lệch ngay trong PRD Solution:** `gr_view_gamification_settings` / `gr_update_gamification_settings` (`prd.md:644-645`, lms-be `openspec/changes/upbase-221099-gamification/design.md:367-368`) và `gr_view_gamification_config` / `gr_update_gamification_config` (`prd.md:771`, phần ops-fe). Chốt một bộ ở 2.8.
3. **`PUT /gamification/settings` nhận cả `timezone`** (`prd.md:635`, `design.md:351`) trong khi `BR-14.9` chốt múi giờ theo tenant, không nhập trên màn Gamification; `tenant` chưa có cột múi giờ (`libs/database/src/lib/entities/tenant/tenant.entity.ts:6-26`). Contract 2.8 tách múi giờ khỏi DTO cấu hình.
4. **Tự lưu từng ô với `PUT` cả khối** (`BR-14.10`; PRD Frontend §7 "hai điều phải đúng"): hai lần lưu gần nhau dễ ghi đè. Contract 2.8 cần partial update hoặc kiểm phiên bản.
5. **Cache công tắc ở nhiều service** (ops, lms, event-processor, background-job theo PRD Solution §Luồng xử lý): xoá cache khi lưu phải tới mọi nơi đọc; liên quan Q3.

Code kiểm ở lms-be `c279942` (chứa `origin/staging` `1051114`).

## Nguồn thay thế đã dùng
- Intent chuyển từ v1: thiếu `inception/user-stories/stories.md`, `inception/hld-brief/hld-brief.md` (2.41 `[S]` ở `state.md` PO). US lấy từ PRD `## US14`, `## US15`; R11 truy vết tay từ bảng "Truy vết phạm vi trong BRD sang US" của PRD (`po-tools.py trace` báo thiếu `stories.md`).
- Hướng kỹ thuật thay mục 9 HLD Brief: ghi ở `inception/domain-design/decisions.md` (2.6).
- Việc PRD giao Dev quyết (cách lưu múi giờ `BR-14.9`, cơ chế tự lưu `BR-14.10`, hai điều phải đúng ở PRD Frontend §7): không hỏi PO, chuyển sang `inception/domain-design/domain-design-questions.md`.

## Assumptions & Open Questions
| # | Nội dung | Loại | Chặn | Owner |
|---|---|---|---|---|
| A1 | Lát Nền tảng: trang cấu hình Ops chỉ có khối chung (hai công tắc); khối US8–US11 gắn sau | Assumption | Không | Tech lead |
| A2 | Hiệu lực công tắc ở lát này kiểm bằng trạng thái đọc qua API (Ops và UpLMS), chưa có ghi nhận điểm | Assumption | Không | Tech lead |
| A3 | Ba quyền US15 khai báo đủ ở lát này, màn US12, US21, US22 làm ở Unit sau | Assumption | Không | Tech lead |
| A4 | Popover tắt công tắc 1 chưa có phần campaign (`OQ-42`, US20 ngoài lát) | Assumption | Không | Tech lead |
| A5 | lms-fe ở lát này chỉ đọc trạng thái hiển thị, chưa có màn | Assumption | Không | Tech lead |
| OQ-T1 | `tags: []` vs `BR-15.3` (Rủi ro 1) | Open Question | Có, cho 2.8 | BE lead |
| OQ-T2 | Mã quyền nào là chuẩn (Rủi ro 2) | Open Question | Có, cho 2.8 | BE lead |

## Lần kiểm lại 2026-10-13 (`[R]`)
Chỉ kiểm finding cũ; PRD chưa lên version mới vì PO (giả lập) chưa chạy `/change-request`, câu trả lời lấy từ `prd-readiness-questions.md` (DEC-T4).

| Finding | Kết quả | Hệ quả cho thiết kế |
|---|---|---|
| RD1 | Q1 = A | Một trang Gamification bên Ops; quyền `Xem danh sách học viên và hạng` chỉ thấy khối Campaign chỉ xem. Guard trang chấp nhận một trong ba quyền, từng khối hiện theo quyền |
| RD2 | Q2 = A | Lưu mốc tổ chức đã từng bật `Visibility in UpLMS`; popover chỉ hiện khi chưa có mốc |
| RD3 | Q3 = A | Công tắc có hiệu lực ngay khi lưu; mọi service đọc công tắc phải thấy giá trị mới ngay (rủi ro 5 thành yêu cầu) |
| RD4 | PO bổ sung | Chuỗi hai popover đã có; popover, `Saved`, 403 dùng chuẩn Ops (ui-map 3.41 ghi Provisional) |
| RD5 | Còn, Ghi nhận | Tech theo `BR-15.3`; PO sửa AC trong CR kế tiếp |
| RD6 | Q4 = A | Migration để tổ chức hiện có ở trạng thái tắt hẳn |
| RD7, RD8 | Còn, Ghi nhận | Không chặn |

Không còn finding Chặn → **READY**. OQ-T1 (`tags: []`), OQ-T2 (mã quyền) chuyển sang `inception/domain-design/domain-design-questions.md` cho BE lead.

## Lần kiểm mở rộng phạm vi 2026-10-13 (`[R]`, DEC-T15)
Phạm vi: 17 US mới = US1–US13, US19–US22 (US14, US15 đã READY ở v1.0, chỉ kiểm lại chỗ US mới chạm vào). PRD vẫn v0.14 + Q1–Q4. Người kiểm: FE lead Nguyễn Hùng Sơn.

**NOT READY.** Có năm chỗ chặn thiết kế, đều là rule hoặc dữ liệu chưa chốt: cách đếm huy hiệu cho tiêu chí lên hạng (RD9), bảng `Courses` của campaign luôn có hay tuỳ chọn (RD10), tắt `Gamification` khi có campaign đang chạy (RD11), lần ghi nhận lại sau lỗi so với kết quả campaign đã đóng băng (RD12), và nơi vận hành thấy lần cộng điểm lỗi (RD13). Phần còn lại đủ để viết thiết kế. Năm chỗ chặn dồn vào Unit Huy hiệu, Hạng, Campaign và phần lỗi của Unit Điểm.

### Checklist (17 US mới)
| # | Tiêu chí | Đạt | Ghi chú |
|---|---|---|---|
| R1 | Pre-condition, Scenario, AC | Đạt | 17 US đủ ba mục; US13 không có UI (đúng chủ đích); Conner case để QA điền (2.81) |
| R2 | AC kiểm chứng được | Nên sửa | Chuỗi tiếng Anh còn `❓PO` (`OQ-50`, RD19); nhiều dòng `[đề xuất]` chưa xác nhận (`OQ-43`, RD20); bảng xem trước trên trang cấu hình không có AC (RD17) |
| R3 | BR có mã, không mâu thuẫn | Không | RD9 `BR-9.10` ↔ `BR-10.4a`; RD10 `BR-19.3a` ↔ design cột `Contribution`; RD12 `BR-13.8` ↔ `BR-21.1` |
| R4 | Data to Retain đủ | Nên sửa | Đủ entity (sổ giao dịch, ngày có mặt, chuỗi, thành tích, cấu hình bốn khối, campaign, kết quả đóng băng); thiếu giá trị mặc định của ba hành động, ba bội số, trần hạng, tên và hình 24 mốc huy hiệu ngoài Check-in (RD16) |
| R5 | Quyền tách rõ | Đạt | `BR-15.7` + Q1; US12, US21, US22 dùng quyền `Xem danh sách học viên và hạng` (`BR-22.7`) |
| R6 | Rỗng, lỗi, giới hạn | Nên sửa | Trạng thái rỗng có (trừ chuỗi `OQ-50`); thiếu giới hạn: thời gian tự tắt thông báo (`OQ-53`), số mục mỗi lần tải lịch sử (`OQ-19`), ảnh huy hiệu (`OQ-51`), độ dài tên campaign (`OQ-52`) (RD14) |
| R7 | Dữ liệu cũ, migration | Đạt có giả định | Bốn chức năng mặc định tắt (Data Field US8–US11); `BR-13.2` không nạp lịch sử; tổ chức hiện có cần seed tên và hình mặc định (RD16) |
| R8 | NFR đo được | Nên sửa | "Không làm chậm cảm nhận" (US2, US13), "nhanh kể cả khi nhật ký đã lớn" (US22), xuất Excel không giới hạn số dòng (US12, US21) chưa có con số (RD15) |
| R9 | Design | Nên sửa | Thiếu: campaign phía học viên, nhật ký Ops (US22), khối My Learning; lệch: tab `Activities`, bộ chọn khoảng ngày, nút xuất, dòng `You` (`OQ-45`, RD18) |
| R10 | Không còn `❓PO` / `OQ` chặn | Không | `OQ-42` (RD11), `OQ-46` (RD13), `OQ-49` (RD10). PRD tự ghi `OQ-42`, `OQ-49`, `OQ-52` cần trả lời trước khi bàn giao Unit Campaign |
| R11 | Traceability | Đạt, truy vết tay | Bảng "Truy vết phạm vi trong BRD sang US" phủ 16/17 US mới; US12 không có dòng `S` (RD25) |

### Finding
| Mã | Mức | Vị trí | Vấn đề | Cần PO làm gì |
|---|---|---|---|---|
| RD9 | Chặn | US9 · `BR-9.10` ghi chú `[đề xuất]` · US10 · `BR-10.4a` · `BR-9.9` gạch cuối | "Số huy hiệu chỉ đếm loại đang bật" làm số huy hiệu giảm khi tắt một loại rồi tăng lại khi bật; ghi chú `[đề xuất]` nói "mỗi huy hiệu chỉ góp một lần" cho tiêu chí lên hạng. Chưa chốt thì không biết có phải lưu thêm bộ đếm riêng cho tiêu chí lên hạng hay không (dữ liệu mới) | Trả lời Q5 |
| RD10 | Chặn | US19 · `BR-19.3a` · US20 AC "Bảng `Courses`" · design `Gamification - Enable - Setting.png` cột `Contribution` · `OQ-49` | PO chọn "Courses luôn có" nhưng design có campaign không có `Course`. Quyết định campaign có thêm một cờ dữ liệu hay không và form có ô chọn hay không | Trả lời Q6 |
| RD11 | Chặn | US14 popover tắt công tắc 1 · US20 · `BR-20.8` `[đề xuất]` · `OQ-42` | Tắt `Gamification` khi có campaign đang chạy: cho tắt hay chặn. Đổi luồng popover (RD7 cũ) và luật campaign | Trả lời Q7 |
| RD12 | Chặn | US13 · `BR-13.8` gạch 2 `[đề xuất]` · US21 · `BR-21.1`, `BR-21.2` · `C11` | Lần ghi nhận lại mang **thời điểm hoàn thành gốc**. Nếu lần ghi lại tới sau khi campaign đã đóng băng mà thời điểm gốc nằm trong khoảng campaign, thì sổ giao dịch và kết quả đóng băng lệch nhau, trong khi `BR-21.1` cấm tính lại | Trả lời Q8 |
| RD13 | Chặn | US13 · `BR-13.8` gạch 4 · US22 · `BR-22.8` · `OQ-46` | Lần cộng điểm lỗi phải được ghi lại để vận hành thấy, nhưng không có màn nào hiện, và US22 đã loại. Quyết định có thêm màn / API bên Ops hay chỉ là log kỹ thuật | Trả lời Q9 |
| RD14 | Nên sửa | US2 "Thời gian tự tắt" (`OQ-53`) · US3 "Số mục một lần tải" (`OQ-19`) · US9 "Hình huy hiệu" (`OQ-51`) · US20 "Tên" (`OQ-52`) | Bốn giới hạn còn `❓PO` | Trả lời Q10–Q13 |
| RD15 | Nên sửa | US2 NFR · US13 NFR · US12 NFR · US22 NFR · US12, US21 nút xuất | NFR chưa có con số: độ trễ thông báo, thời gian gamification được cộng thêm vào thao tác học, thời gian trả trang của US12, US22 khi dữ liệu lớn, giới hạn dòng khi xuất | Trả lời Q14 |
| RD16 | Nên sửa | US8 "Ô nhập số điểm" · US10 "Ô nhập bội số", "Trần hạng" · US9 `BR-9.8` | PRD chỉ có mặc định điểm nền `10`. Design có `10 / 150 / 25`, `3000 / 5 / 5`, trần `100` và tên + hình 8 mốc Check-in; ba loại còn lại chưa có tên, hình mặc định | Trả lời Q15; bổ sung tên, hình mặc định |
| RD17 | Nên sửa | US11 · design `Gamification - Enable - Setting.png` bảng xem trước dưới khối Leaderboard · PRD Frontend §7.5 `LeaderboardPreview` | Trang cấu hình có bảng xem trước (kèm dòng `You`, bộ chọn khoảng ngày) nhưng US11 không có AC nào cho nó; `OQ-45` chỉ nói bỏ bộ chọn khoảng ngày | Trả lời Q16 |
| RD18 | Nên sửa | `OQ-45` | Design thiếu hoặc lệch: campaign phía học viên (US19), nhật ký Ops (US22), khối My Learning (US1), tab `Activities` + lối vào campaign (US6), nút xuất + bỏ `You` (US21), nút xoá campaign (US20). Chặn ở 3.41 ui-map, không chặn 2.6 | Bổ sung design |
| RD19 | Nên sửa | `OQ-50` (trừ hai popover US14 đã có) | Chuỗi tiếng Anh còn trống ở US6, US7, US8–US11, US19 | Bổ sung chuỗi |
| RD20 | Nên sửa | `OQ-43` | Khoảng 20 dòng `[đề xuất]` trong 17 US chưa xác nhận. Tech dùng đúng như PRD viết làm Assumption (A6) | Trả lời Q17 |
| RD21 | Ghi nhận | US10 "Trần hạng" · design `Maximum level` có công tắc riêng | PRD: bỏ trống = không trần; design: công tắc + ô. Tech hiểu công tắc tắt = không trần, giữ giá trị ô | Sửa design hoặc AC khi có CR |
| RD22 | Ghi nhận | US12 cột `Last activity` | Nội dung là "ngày có mặt gần nhất" (check-in), không phải hoạt động học gần nhất; tên cột dễ hiểu nhầm | Cân nhắc đổi thành `Last visit` |
| RD23 | Ghi nhận | US1 `BR-1.5` | Không nói `Test Account` thấy gì khi mở UpLMS. Tech xử lý như `Visibility in UpLMS` tắt: ẩn menu, đường dẫn trả không tìm thấy (A7) | Xác nhận khi có CR |
| RD24 | Ghi nhận | `OQ-12`, `OQ-18` | Đã để ngoài phạm vi US2, US3, không chặn | — |
| RD25 | Ghi nhận | Bảng "Truy vết phạm vi trong BRD sang US" | US12 không có dòng `S`; dòng `Giả định A25` nằm lạc dưới ghi chú | Sửa trình bày khi có CR |

### Rủi ro kỹ thuật thấy sớm
1. **Thiết kế BE gốc lệch PRD v0.14.** PRD `Solution › Backend` (`prd.md:322-350`) tự ghi technical design viết trước `CR-012`, `CR-013`, `US22`: còn nhánh `from/to` phía học viên, check-in ở mọi request đã xác thực, bốn bảng thay năm, chỉ số đếm từ sổ điểm, chưa có campaign, chưa có US22. 2.6 phải đối chiếu lms-be `openspec/changes/upbase-221099-gamification/design.md` từng điểm (theo DEC-T1, sửa ở change lms-be).
2. **Check-in "chủ động mở" (`BR-5.1`)** cần tín hiệu từ lms-fe để tách request nền (socket, refetch khi focus) khỏi thao tác thật: chạm contract lms-fe ↔ lms-be, không làm được chỉ ở BE.
3. **Chỉ số đếm độc lập với `Points` nhưng phụ thuộc `Gamification`** (mục Định nghĩa chỉ số, `BR-13.13`): dòng 0 điểm thành nguồn đếm chính, sổ giao dịch phình theo mọi hoạt động; `All time` và bộ lọc khoảng tự do của US12, US22 quét trên bảng này, cần index hoặc bảng tổng hợp (liên quan RD15).
4. **Đóng băng campaign + ghi nhận lại** (RD12, `C11`): tác vụ đóng băng phải chờ hàng ghi lại hoặc chấp nhận lệch; quyết định ảnh hưởng background-job-service.
5. **Thông báo realtime nhiều tab** (PRD Frontend §5.3 `toastDeduper`, `BR-2.9` không gộp): socket gateway lms + dedupe phía lms-fe; lỗi không được chặn thao tác học (`NFR-GAM-01`).

### Phụ thuộc giữa các nhóm US (đầu vào cho 2.7, 2.9)
Theo PRD "# Unit — nhóm bàn giao": Nền tảng (B01) → Điểm (US5, US8, US13, US22) → Hiển thị (US1, US2, US3) ∥ Huy hiệu (US4, US9) → Hạng (US10) → Bảng xếp hạng (US6, US7, US11, US12) → Campaign (US19, US20, US21). RD9 chặn Huy hiệu + Hạng; RD10, RD11, RD12 chặn Campaign; RD13 chặn phần lỗi của Unit Điểm. Unit Điểm và Hiển thị thiết kế được trước nếu tech lead chấp nhận Assumption A8.

### Assumptions & Open Questions (bổ sung)
| # | Nội dung | Loại | Chặn | Owner |
|---|---|---|---|---|
| A6 | Mọi dòng `[đề xuất]` trong 17 US dùng đúng như PRD viết cho tới khi PO trả lời Q17 | Assumption | Không | Tech lead |
| A7 | `Test Account` ở UpLMS được xử lý như `Visibility in UpLMS` tắt (RD23) | Assumption | Không | Tech lead |
| A8 | Trong lúc chờ Q9: lần cộng điểm lỗi ghi vào bảng lỗi riêng và tự ghi lại, chưa có màn Ops | Assumption | Không | Tech lead |
| A9 | Giá trị mặc định lấy theo design (Q15 phương án A) | Assumption | Không | Tech lead |
| OQ-T3 | Tín hiệu "chủ động mở" từ lms-fe (Rủi ro 2) | Open Question | Có, cho 2.8 | FE lead + BE lead |
| OQ-T4 | Bảng tổng hợp chỉ số hoặc index cho `All time`, US12, US22 (Rủi ro 3) | Open Question | Có, cho 2.6 | BE lead |

## Lần kiểm lại Lô 2 2026-10-13 (`[R]`)
Chỉ kiểm finding RD9–RD25; PRD chưa lên version mới, câu trả lời lấy từ `prd-readiness-questions.md` Lô 2 (DEC-T17).

| Finding | Kết quả | Hệ quả cho thiết kế |
|---|---|---|
| RD9 | Q5 = A | Lưu bộ đếm riêng "số huy hiệu đã góp vào hạng" theo học viên, chỉ tăng; tiêu chí lên hạng theo huy hiệu đọc bộ đếm này, không đọc số huy hiệu loại đang bật |
| RD10 | Q6 = A | Campaign không có cờ `Courses`; mọi campaign có bảng `Courses` |
| RD11 | Q7 = A | Popover tắt công tắc 1 thêm số campaign đang chạy (RD7 hết treo); chỉ số campaign chỉ đếm lúc `Gamification` bật |
| RD12 | Q8 = A | Tác vụ đóng băng chạy lúc `kết thúc + 24 giờ`, lọc theo thời điểm gốc (`C11`); ghi lại tới sau không đụng kết quả đóng băng |
| RD13 | Q9 = A | Bảng lỗi + tự ghi lại + log/cảnh báo kỹ thuật; không có API/màn Ops (A8 thành quyết định) |
| RD14 | Q10–Q13 = A | 5 giây/thẻ, tối đa 4 thẻ; 20 mục/lần; ảnh theo kho tài nguyên; tên campaign ≤ 100 |
| RD15 | Q14 = A | NFR thành con số, đưa vào 3.2 nfr-requirements của Unit liên quan |
| RD16 | Q15 = A | Seed mặc định theo design cho tổ chức mới và tổ chức hiện có; hình 24 mốc tạm dùng hình mặc định của loại |
| RD17 | Q16 = A | Bảng xem trước Ops đọc bảng `All time` tính sẵn, theo công tắc `Show …` |
| RD18 | PO: làm sau | ui-map 3.41 `Provisional` cho màn chưa có design |
| RD19 | PO: Tech viết nháp | Chuỗi nháp ghi ở ui-map, PO duyệt ở CR |
| RD20 | Q17 = A | A6 thành quyết định |
| RD21–RD25 | Còn, Ghi nhận | Không chặn |

Không còn finding Chặn → **READY**. OQ-T3 (tín hiệu "chủ động mở"), OQ-T4 (bảng tổng hợp chỉ số) chuyển sang `inception/domain-design/domain-design-questions.md` ở 2.6.
