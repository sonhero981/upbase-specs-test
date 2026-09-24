# Project Decisions

**Project:** Gamification

Nơi ghi mọi quyết định đã chốt. AI tra file này để **không hỏi lại câu đã có đáp án**.

> ⚠️ **Đây là bộ nhớ của dự án — đừng xoá trong quá trình làm việc.**

| Ngày | Quyết định | Lý do | Người quyết | Gate |
| --- | --- | --- | --- | --- |
| 23/09/2026 | **Bảng xếp hạng (leaderboard) — làm sau**, ngoài phạm vi đợt này | PO chốt thứ tự ưu tiên | PO | Bước 2 · OQ-01 |
| 23/09/2026 | **"Điểm theo kỳ" vẫn làm** dù leaderboard làm sau — kỳ = **chiến dịch**, hết kỳ thì **lưu lại**, không xoá | Là nền dữ liệu cho leaderboard sau này | PO | Bước 2 · OQ-04 |
| 23/09/2026 | **Lộ trình học — làm sau.** Bỏ hành động tính điểm "hoàn thành lộ trình" khỏi phạm vi | Lộ trình là nội dung học tương tự khoá học, chưa có trong hệ thống | PO | Bước 2 · OQ-02 |
| 23/09/2026 | **Kỹ năng = Skills, thuộc tính năng Khung năng lực — làm sau.** Bỏ điều kiện huy hiệu "đạt kỹ năng" khỏi phạm vi | Thuộc tính năng khác, không thuộc gamification | PO | Bước 2 · OQ-06 |
| 23/09/2026 | **Dữ liệu đăng nhập lấy từ Keycloak.** Chuỗi ngày liên tiếp **tính từ ngày go-live tính năng**, không hồi tố | Hệ thống không có bảng lịch sử đăng nhập của học viên | PO | Bước 2 · OQ-03 |
| 23/09/2026 | **Cấu hình gamification do nhân sự vận hành có quyền tương ứng** thực hiện trên UpLMS Ops | | PO | Bước 2 · OQ-08 |
| 23/09/2026 | **Đổi cách tính điểm → áp dụng từ thời điểm đổi trở đi.** Không tính lại lịch sử | | PO | Bước 2 · OQ-08 |
| 23/09/2026 | **Giữ nguyên logic hoàn thành Activity hiện tại** — không sửa module Learning Experience | | PO | Bước 2 · OQ-10 |
| 23/09/2026 | **Đính chính KB:** Activity chứa Video hoàn thành khi **xem ≥80% thời lượng** (UG cũ ghi "phải play video"). Activity Text/Ảnh **giữ nguyên** — hoàn thành khi mở hiển thị | PO xác nhận hệ thống đã cập nhật | PO | Bước 2 · OQ-10 |
| 23/09/2026 | **Vấn đề cần giải:** học viên không chủ động vào học. Gamification để duy trì động lực và **làm nền cho đội truyền thông nội bộ chạy chiến dịch** thúc đẩy tinh thần học | | PO | Bước 2 · OQ-09 |
| 23/09/2026 | **Stakeholder bổ sung: Đội truyền thông nội bộ** — người dùng thật của cơ chế chiến dịch | Phát hiện từ câu trả lời OQ-09 | PO | Bước 2 |
| | *(chờ)* **OQ-A1 — ngữ nghĩa của việc tắt gamification** | Đã phân tích, chờ PO chọn | PO | Gate 1 |
| | *(chờ)* **OQ-A2 — chống cày với hoạt động Text/Ảnh** | Đã phân tích, chờ PO chọn | PO | Gate 1 |

## CR-001 — Đưa bảng xếp hạng vào phạm vi (23/09/2026)

| Ngày | Quyết định | Lý do | Người quyết | Gate |
| --- | --- | --- | --- | --- |
| 23/09/2026 | **Bảng xếp hạng LÀM trong đợt này** — đảo ngược quyết định hoãn ngày 23/09 | PO chỉ định | PO | CR-001 |
| 23/09/2026 | **Điểm re-entry = BRD (Bước 4).** BRD lên v0.2, trình lại Gate 1 | BRD chưa được duyệt lần nào | PO | CR-001 |
| 23/09/2026 | **Xếp hạng theo phòng ban — KHÔNG làm.** Phòng ban chính là chức năng nhóm, **đồng bộ từ HRM của tổ chức** thành cây sơ đồ tổ chức. Chưa làm | Dữ liệu chưa có: `departments` chỉ gắn `staffs`, học viên không có phòng ban | PO | CR-001 |
| 23/09/2026 | **`TNT.CFG.02` = cấu hình tenant trong module Tenant** (tên, mã định danh, **múi giờ**, ngôn ngữ, định dạng ngày/số). Chưa có multi-tenant → **làm cho tổ chức hiện tại** | | PO | CR-001 |
| 23/09/2026 | **Kỳ lịch ≠ Chiến dịch.** Tuần/tháng/quý/năm là **mốc snapshot hệ thống tự tính**. Chiến dịch là khoảng **do vận hành setup** | | PO | CR-001 |
| 23/09/2026 | **Trao thưởng là hành động ngoài hệ thống.** Hệ thống chỉ giữ bảng xếp hạng cuối kỳ | | PO | CR-001 |
| 23/09/2026 | **`A8` bị bác bỏ** — các kỳ CÓ chồng lấn (tuần ⊂ tháng ⊂ quý ⊂ năm, cộng chiến dịch song song) → ràng buộc `C7` | Suy ra từ yêu cầu "xem lại tháng trước, quý trước, chiến dịch đã kết thúc" | PO + phân tích | CR-001 |
## Bốn quyết định Gate 1 (23/09/2026)

| Ngày | Quyết định | Lý do | Người quyết | Gate |
| --- | --- | --- | --- | --- |
| 23/09/2026 | **OQ-A1 ✅ Hai công tắc.** `Gamification` = bật/tắt **lưu dữ liệu**, bao gồm cả hiển thị. `Visibility in UpLMS` = **chỉ xuất hiện khi Gamification bật**, bật/tắt hiển thị phía học viên | Cần giai đoạn chạy thử trước khi mở cho học viên | PO | Gate 1 |
| 23/09/2026 | **OQ-A2 ✅ Không làm chống cày riêng cho hoạt động chỉ có Text/Ảnh.** Khử trùng (`C5`) và trần điểm/ngày (`S8`) vẫn áp cho mọi loại | Rủi ro chấp nhận có chủ đích | PO | Gate 1 |
| 23/09/2026 | **OQ-A3 ✅ BỎ phạm vi/bộ lọc xếp hạng theo lớp.** Gộp cùng bộ lọc theo phòng ban thành một hạng mục hoãn: **bộ lọc theo nhóm** | Bộ lọc theo lớp sau này chính là bộ lọc theo nhóm — làm riêng bây giờ thì trùng mục đích, sau phải làm lại | PO | Gate 1 · CR-003 |
| 23/09/2026 | **OQ-A4 ✅ Giới hạn nội dung chiến dịch — KHÔNG làm.** Thay vào đó: **chỉ số xếp hạng của chiến dịch chọn được** (điểm · số huy hiệu · số khoá hoàn thành) + **luật chỉnh sửa chiến dịch** (đang chạy thì không sửa) | PO làm rõ: điều cần là chọn *chỉ số xếp hạng*, không phải giới hạn *nội dung sinh điểm* | PO | Gate 1 · CR-002 |
| 23/09/2026 | **Tiêu chí phụ khi đồng hạng (`S22`) thành BẮT BUỘC** — cùng chỉ số thì ai đạt sớm hơn xếp trên | Hệ quả của CR-002: xếp theo "số khoá hoàn thành" (0–5) hay "số huy hiệu" (0–10) gây đồng hạng hàng loạt | Phân tích | Gate 1 |
| | *(chờ)* **A15 — bảng xếp hạng công khai danh tính học viên** | Vấn đề riêng tư, cần PO xác nhận rõ | PO | Gate 1 |

## Gate 1 lần 2 — `Need Revision`, CR-004 (23/09/2026)

| Ngày | Quyết định | Lý do | Người quyết | Gate |
| --- | --- | --- | --- | --- |
| 23/09/2026 | **Stakeholder tách L&D và Quản lý trực tiếp.** Quản lý trực tiếp = quản lý của học viên trong tổ chức | | PO | Gate 1 |
| 23/09/2026 | **Điểm đăng nhập: mỗi lần login được điểm**, chống spam bằng khoảng cách thời gian tối thiểu (ví dụ dưới 2 tiếng không tính). **Bỏ cơ chế chuỗi ngày liên tiếp** | Đơn giản hơn, không phải tính và lưu chuỗi | PO | Gate 1 |
| 23/09/2026 | **Bốn loại huy hiệu đo bằng chỉ số đếm:** Tích cực (số lần login) · Học tập (số hoạt động hoàn thành) · Test (số bài test hoàn thành) · Course (số khoá hoàn thành) | | PO | Gate 1 |
| 23/09/2026 | **Ngưỡng lên hạng dùng nhiều chỉ số**, không chỉ điểm — điểm, huy hiệu, số khoá hoàn thành | | PO | Gate 1 |
| 23/09/2026 | **Từ vựng giữ nguyên: `Point` = điểm, `Level` = hạng học viên** | PO chốt, không đổi tên | PO | Gate 1 |
| 23/09/2026 | **Thông báo thành tích: chỉ đẩy trong hệ thống khi học viên đang online. Không gửi mail.** Offline thì không gửi, thành tích vào lịch sử | | PO | Gate 1 |
| 23/09/2026 | **Không bật lại 8 mail luồng chấm điểm.** Lúc nào bật thì review lại logic | | PO | Gate 1 |
| 23/09/2026 | **Bỏ US "hiệu quả chiến dịch"** — hệ thống chỉ cung cấp **kết quả**, đội truyền thông tự đo hiệu quả bên ngoài | | PO | Gate 1 |
| 23/09/2026 | **Bỏ US "tính bù điểm"** — chạy ngầm thì bật lên đã có sẵn; tắt hẳn thì không ghi gì nên không có gì để bù | | PO | Gate 1 |
| 23/09/2026 | **Đồng hạng xử lý theo thời điểm đạt** — ai đạt trước xếp trước | | PO | Gate 1 |
| 23/09/2026 | **Chiến dịch không chồng lấn ở đợt này.** Sau này mới tạo nhiều chiến dịch cho nhiều nhóm | | PO | Gate 1 |
| 23/09/2026 | **`OQ-B3` đóng** — đội truyền thông tự đo hiệu quả bên ngoài | | PO | Gate 1 |
| | *(chờ)* **`S23` — một danh mục chỉ số dùng chung cho huy hiệu, hạng và xếp hạng chiến dịch** | Khuyến nghị mới, phát sinh từ CR-004 | PO | Gate 1 |

## ✅ GATE 1 — `Approved with Notes` (23/09/2026)

**BRD `v0.5` là bản được duyệt.** Bốn note kèm theo:

| Ngày | Quyết định | Lý do | Người quyết | Gate |
| --- | --- | --- | --- | --- |
| 23/09/2026 | **`A20` ✅ Phạm vi người tham gia chiến dịch = toàn bộ học viên** ở đợt này | Chưa có chức năng nhóm | PO | Gate 1 |
| 23/09/2026 | **`A21` → đổi: điểm khi vào hệ thống tính THEO NGÀY.** Mỗi ngày học viên vào hệ thống được điểm một lần. Bỏ cơ chế "mỗi lần login + khoảng cách tối thiểu" | Đơn giản hơn; không cần cơ chế chống spam riêng | PO | Gate 1 |
| 23/09/2026 | **`A22` ✅ Huy hiệu loại Test chỉ đếm bài ĐẠT.** Bài không có setting pass thì tính khi hoàn thành → `BR-TEST` | | PO | Gate 1 |
| 23/09/2026 | **`A15` ✅ Bảng xếp hạng công khai danh tính học viên** — bình thường, không vấn đề | | PO | Gate 1 |
| 23/09/2026 | **`OQ-B1` đóng — không còn phụ thuộc sự kiện đăng nhập Keycloak.** `S3` chuyển sang "có mặt trong ngày" nên nguồn dữ liệu khác hẳn. Mức tác động User/Auth giảm từ 🔴 Cao xuống 🟡 Thấp | Hệ quả trực tiếp của quyết định `A21` | Phân tích | Gate 1 |
| 23/09/2026 | **Thêm `C9`** — "ngày" trong điểm-theo-ngày và trần-điểm-mỗi-ngày cắt theo **múi giờ tổ chức**, cùng quy tắc với biên kỳ | Hệ quả của `A21` gặp `C6` | Phân tích | Gate 1 |
| | *(chờ)* **`OQ-B15`** — ghi nhận "học viên có vào hệ thống hôm nay" bằng cách nào | Nguồn dữ liệu cho `S3` và huy hiệu Tích cực | Dev | Gate 2 |
| 23/09/2026 | **`OQ-B16` ✅ Chỉ đếm bài Test. Quiz và Case Study KHÔNG tính** | PO xác nhận | PO | Gate 1 |
| 23/09/2026 | **🔧 Đính chính `BR-TEST`: `Pass Point` chỉ tồn tại khi `Graded Assignment = Yes`.** Test có `Graded Assignment = No` thì **không có ngưỡng đạt** → tính khi hoàn thành | PO xác nhận. KB `03` ghi thiếu ràng buộc liên trường này | PO | Gate 1 · CR-006 |
| 23/09/2026 | **Cập nhật KB `03-assessment.md`** — thêm `KB-TEST-01a`, `KB-TEST-01b` và ràng buộc liên trường | Đính chính từ PO | PO | CR-006 |
| | *(chờ)* **`A23`** — "đạt điểm cao" có chỉ áp cho bài có `Graded Assignment = Yes` không | Bài không có ngưỡng đạt thì không có khái niệm "điểm cao" | PO | Field Intake |
| 23/09/2026 | **`OQ-B17` bỏ** — hành động "đạt điểm cao" đã ra khỏi phạm vi | PO chốt | PO | Gate 1 |

## ✅ GATE 2 — `Approved` (23/09/2026)

**`impact-matrix-v0.2-20260923.md` (v0.2.1) là bản được duyệt.**

| Ngày | Quyết định | Lý do | Người quyết | Gate |
| --- | --- | --- | --- | --- |
| 23/09/2026 | **`CF-1` ✅ `Test Account` bị loại khỏi TOÀN BỘ logic gamification** — không điểm, huy hiệu, hạng, xếp hạng | Là tài khoản của L&D và QA dùng kiểm tra khoá học; về dữ liệu là học viên thật | PO | Gate 2 → `C10` |
| 23/09/2026 | **`CF-2` ✅ Không tồn tại.** Một khoá chỉ ở **một lớp tại một thời điểm**. Xoá ra thêm lại → học lại → **tính như khoá mới, được điểm** | | PO | Gate 2 |
| 23/09/2026 | **`C5` sửa:** khử trùng trong phạm vi **một lượt ghi danh**, không cắt ngang lớp. Kèm rule: **chỉ cộng điểm khi bản ghi tiến độ chuyển trạng thái sang hoàn thành, tính từ lúc bật** | Hệ quả của `CF-2` | PO + phân tích | Gate 2 → BRD v0.6.1 |
| 23/09/2026 | **`CF-3` ✅ Chấp nhận** — đổi ngưỡng hạng thì người cũ giữ hạng, người mới theo ngưỡng mới | | PO | Gate 2 |
| 23/09/2026 | **`CF-5` ✅ Có huy hiệu mặc định** — mất ảnh thì rơi về ảnh mặc định | | PO | Gate 2 |
| 23/09/2026 | **`CF-6` ✅ Đang có chiến dịch thì không tắt gamification được** — phải dừng chiến dịch trước | | PO | Gate 2 |
| 23/09/2026 | **`A24` ✅ Điểm bài Test chốt tại lần chấm đầu tiên.** Chấm lại không cộng thêm | | PO | Gate 2 → `BR-REGRADE-02` |
| 23/09/2026 | **`A25` ✅ My Learning hiện điểm TÍCH LUỸ của cá nhân** (từ lúc vào hệ thống) và hạng — không hiện điểm theo kỳ | | PO | Gate 2 |
| 23/09/2026 | **`A26` ✅ Không có khoá Trial** trong hệ thống | | PO | Gate 2 → KB `14` |
| 23/09/2026 | **`A27` ✅ "Không tính bù" = tính từ lúc ghi nhận.** Bật `Visibility` thì học viên **thấy ngay điểm và hạng đã tích trong lúc chạy ngầm**, kèm lịch sử tra lý do | | PO | Gate 2 |
| 23/09/2026 | **`OQ-B2` ✅ Dữ liệu tiến độ CÓ dấu thời gian** | | PO | Gate 2 |
| 23/09/2026 | **`OQ-B9` ✅ Bảng xếp hạng chịu được tải.** Bảng chỉ hiển thị một số kỳ gần nhất; cộng `S19` (kỳ đã chốt đọc từ snapshot) → tối đa 5 bảng tính trực tiếp. **`R1` hạ từ 🔴 xuống 🟡** | PO phản biện đúng — tôi đã tính thiếu tác dụng của `S19` | PO | Gate 2 |
| 23/09/2026 | **`OQ-B12` ✅ Lưu hết** thời điểm đạt huy hiệu / hoàn thành khoá / hoàn thành bài Test | | PO | Gate 2 |
| 23/09/2026 | **Cập nhật KB:** `06-user-account.md` §8b (`Test Account`, 3 rule) · `01-course.md` (`BR-EDIT-07` thêm ngoại lệ) · `14-api-surface.md` §2.2 (bảng endpoint có nhưng tính năng không có) | Phát sinh từ Gate 2 | PO | Gate 2 |

## Giai đoạn 4 — Bước 7: định hướng giải pháp (23/09/2026)

| Ngày | Quyết định | Lý do | Người quyết | Bước |
| --- | --- | --- | --- | --- |
| 23/09/2026 | **Điểm hiện với học viên: chấp nhận trễ vài phút** sau khi hoàn thành hoạt động | Nhẹ hệ thống, không rủi ro làm chậm việc học | PO | Bước 7 |
| 23/09/2026 | **Bảng xếp hạng cập nhật theo chu kỳ**, hiển thị rõ **lần cập nhật cuối** | | PO | Bước 7 |
| 23/09/2026 | **"Ngày có mặt" = cứ vào hệ thống là tính, kiểu check-in.** Không đòi hỏi thao tác học thật | Số liệu cho thấy Activation chỉ 40.2% — vấn đề bắt đầu ngay ở chỗ không mở ứng dụng | PO | Bước 7 |
| 23/09/2026 | **`S23` bỏ khỏi phạm vi.** Mỗi chỗ (huy hiệu · hạng · chiến dịch) **tự tính**; vận hành tự cấu hình tham số ở từng nơi | Cách tính vốn khác nhau — huy hiệu và hạng đếm trọn đời, chiến dịch đếm trong khoảng ngày | PO | Bước 7 |
| 23/09/2026 | **`OQ-B4` đóng — PO cung cấp số liệu General Launch 8/9–21/9/2026.** Activation 40.2% (53/132) · Course start 22% (29/132) · Completion 64.1% (93/145), cả ba **đều hụt mục tiêu 80%** | | PO | Bước 7 → BRD §2 |
| | *(chờ)* **`OQ-B4a`** — mẫu số 132 và 145 là hai nhóm người khác nhau, hay 145 gồm cả giai đoạn trước? | | PO | Trước PRD |
| | *(đề nghị)* **Đưa bộ Activation / Course start / Completion vào `Metrics success` của PRD** | Đã có đủ chỉ số · tiêu chí · mốc nền — không cần nghĩ chỉ số mới | PO | Gate 3 |

## Bước 8 — Chốt phương án giải pháp (23/09/2026)

| Ngày | Quyết định | Lý do | Người quyết | Bước |
| --- | --- | --- | --- | --- |
| 23/09/2026 | **Chọn Option C — Tính trong luồng.** Cộng điểm ngay trong cùng thao tác hoàn thành hoạt động, độ trễ bằng 0 | **Dev xác nhận làm được theo cách này**, PO chọn C | PO + Dev | Bước 8 |
| 23/09/2026 | **`G1` được giải luôn** — học viên luôn còn trong hệ thống khi điểm được cộng, nên `US2` thực hiện trọn vẹn, không nhóm nào bị lỡ thông báo | Hệ quả của C | — | Bước 8 |
| 23/09/2026 | **`NFR-GAM-01` bắt buộc: lỗi ở gamification KHÔNG được làm hỏng thao tác học.** Học viên bấm Hoàn thành thì thao tác phải thành công kể cả khi cộng điểm lỗi. Cũng không được làm chậm cảm nhận | Điều kiện đi kèm bắt buộc của C | Phân tích | Bước 8 |
| 23/09/2026 | **`CG-7` nâng mức** — hai thao tác song song đều có thể cộng điểm, phải chống trùng ngay tại chỗ ghi. **`CG-8` thu hẹp** — chỉ còn áp cho tác vụ chốt kỳ | Hệ quả của C | Phân tích | Bước 8 |
| 23/09/2026 | **Giữ nguyên:** check-in ghi ngay (`S-1`) · chốt kỳ là tác vụ riêng đúng biên kỳ (`S-2`) · bảng xếp hạng tính sẵn theo chu kỳ (`S-3`) | | PO | Bước 8 |
| | *(chờ)* **`OQ-D3`** — cộng điểm lỗi thì **mất âm thầm** hay **ghi lại chỗ lỗi để vận hành xử lý**? Đề xuất: ghi lại | Giữ `O6` (điểm đáng tin) | PO | Gate 3 |
| | *(đóng)* **`OQ-D1` `OQ-D2`** — không còn cần, chỉ áp cho option A và B | | — | Bước 8 |

## 🔄 CR-007 — Bỏ chiến dịch và kỳ lịch (23/09/2026)

**Đây là thay đổi phạm vi lớn nhất của dự án. Nó đảo ngược một số quyết định ở trên.**

| Ngày | Quyết định | Lý do | Người quyết | Nguồn |
| --- | --- | --- | --- | --- |
| 23/09/2026 | **Bỏ hẳn chiến dịch, kỳ lịch như thực thể riêng, và cơ chế chốt kỳ.** Thay bằng **bộ chọn khoảng ngày tự do** trên bảng xếp hạng | Một bộ chọn khoảng ngày bao trùm cả hai. Nút "tháng này" chỉ là lối tắt | PO | CR-007 |
| 23/09/2026 | **Chấp nhận số liệu sống.** Kết quả của cùng một khoảng ngày có thể đổi theo thời gian | Trao thưởng vốn làm ngoài hệ thống. Bên công bố tự ghi lại số liệu lúc công bố | PO | CR-007 |
| 23/09/2026 | ❌ **Bỏ mục tiêu `O5`** — kết quả không đổi về sau | Hệ quả trực tiếp của quyết định trên | PO | CR-007 |
| 23/09/2026 | **Khoá mốc huy hiệu sau khi tạo.** Vận hành không sửa được mốc | | PO | CR-007 |
| 23/09/2026 | 🔄 **Trả lại `A5`: huy hiệu đã nhận giữ vĩnh viễn.** Bỏ `BR-4.6` và `BR-4.7` về quét lại và gỡ huy hiệu | Mốc khoá nên không còn tình huống phải gỡ | PO | CR-007 |
| 23/09/2026 | **Hạng: ngưỡng sửa được, theo ba chỉ số** (điểm · huy hiệu · số khoá), **logic HOẶC** — đạt mốc nào trước thì lên hạng theo mốc đó. Hạng **không tụt**, đổi ngưỡng chỉ áp từ lúc đổi | | PO | CR-007 |
| 23/09/2026 | **Bảng xếp hạng: bốn chỉ số** điểm · huy hiệu · hạng · số khoá, học viên tự chọn. Gốc là `All time`, khoảng ngày là bộ lọc | | PO | CR-007 |
| 23/09/2026 | **Nổi bật top 3, danh sách đầy đủ cuộn được bên dưới.** Học viên chưa có chỉ số vẫn hiện, ô thứ hạng để trống | | PO | CR-007 |
| 23/09/2026 | **Chu kỳ tính lại bảng: 8 tiếng một lần, ba lần một ngày** | | PO | CR-007 |
| 23/09/2026 | **Sổ giao dịch điểm giữ toàn bộ, không dọn** | Điều kiện để `O6` đứng vững | PO | — |
| 23/09/2026 | **Danh sách US từ 22 xuống 16**, trong đó 13 US làm ở đợt này | Hệ quả của CR-007 | — | CR-007 |

> ⚠️ **Ba cơ chế nay cùng một luật:** điểm, huy hiệu và hạng đều chỉ áp thay đổi **từ thời điểm đổi trở đi**, và **không có gì bị lấy lại** khỏi học viên.

---

## ✅ GATE 4 — `Approved with Notes` (23/09/2026)

**`prd-gamification-v0.2-20260923.md` là bản được duyệt.** 15 US viết chi tiết, 132 business rule.

| Ngày | Quyết định | Lý do | Người quyết |
| --- | --- | --- | --- |
| 23/09/2026 | **`OQ-02` ✅ Cộng điểm lỗi thì ghi lại chỗ lỗi**, không để mất âm thầm → `BR-13.8` | Giữ `O6` — điểm đáng tin | PO |
| 23/09/2026 | **`OQ-03` ✅ Tạm chốt `Metrics success`**: Activation 40.2% · Course start 22% · Completion 64.1%, đều nhắm 80%. `Retention` chưa có mốc nền | | PO |
| 23/09/2026 | **`OQ-21` ✅ Chứng chỉ cấp THEO KHOÁ, không theo lượt ghi danh.** Một học viên một chứng chỉ cho một khoá, học lại không cấp thêm. Xoá khỏi lớp thì chứng chỉ vẫn còn. Thêm lại vào lớp thì vận hành chọn *ghi nhận đã xong* hoặc *học lại từ đầu* → `BR-13.12` | | PO |
| 23/09/2026 | **`OQ-10`, `OQ-11` — PO tự điền** metadata Jira, link Figma, tài khoản staging | | PO |

### Hệ quả của `BR-13.12` — sửa một chỗ tôi viết sai

| Hành động khi học viên bị xoá khỏi lớp rồi thêm lại | Có cộng điểm lại không |
|---|---|
| Hoàn thành hoạt động | ✅ Có, nếu chọn cho học lại từ đầu |
| Hoàn thành khoá | ❌ **Không** — chứng chỉ không cấp trùng |

Trước đó `BR-13.10` viết chung là *"lượt học mới được tính điểm mới, coi như khoá mới"*, áp cho cả hai hành động. Sai với hành động hoàn thành khoá.

Đây cũng là **lớp bảo vệ thứ hai có sẵn trong hệ thống**: đường cày điểm bằng cách học lại một khoá nhiều lần đã bị chặn ở tầng chứng chỉ, không phải do gamification làm.
