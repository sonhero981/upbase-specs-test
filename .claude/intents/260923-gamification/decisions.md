# Decisions: 260923-gamification

Nhật ký quyết định của intent. Chuyển từ `archive/v1/project-decisions.md` ngày 2026-10-09: cột *Quyết định* giữ nguyên chữ của v1 kèm *Lý do*; *Nguyên văn* chỉ có khi v1 ghi lời PO trong ngoặc kép; *Stage* ghi stage v2 kèm bước hoặc CR của v1. Mã mục tiêu trong các dòng cũ là mã trước ngày 24/09 (`O5` cũ là "kết quả mỗi kỳ không đổi", nay bỏ; "điểm số đáng tin" từ `O6` thành `O5`). Không xoá dòng; quyết định bị thay thì thêm dòng mới và ghi "thay DECn".

| DEC | Ngày | Stage | Quyết định | Nguyên văn | Người quyết | Read when |
|---|---|---|---|---|---|---|
| DEC1 | 2026-09-23 | 0 | Profile L. v1 phân cỡ L: đủ 9 bước, đủ 4 Gate | — | PO | profile, phạm vi |
| DEC2 | 2026-09-23 | 2.3 (v1 Bước 2) · Bước 2 · OQ-01 | **Bảng xếp hạng (leaderboard) — làm sau**, ngoài phạm vi đợt này — Lý do: PO chốt thứ tự ưu tiên | — | PO | mọi stage |
| DEC3 | 2026-09-23 | 2.3 (v1 Bước 2) · Bước 2 · OQ-04 | **"Điểm theo kỳ" vẫn làm** dù leaderboard làm sau — kỳ = **chiến dịch**, hết kỳ thì **lưu lại**, không xoá — Lý do: Là nền dữ liệu cho leaderboard sau này | "Điểm theo kỳ" | PO | mọi stage |
| DEC4 | 2026-09-23 | 2.3 (v1 Bước 2) · Bước 2 · OQ-02 | **Lộ trình học — làm sau.** Bỏ hành động tính điểm "hoàn thành lộ trình" khỏi phạm vi — Lý do: Lộ trình là nội dung học tương tự khoá học, chưa có trong hệ thống | "hoàn thành lộ trình" | PO | mọi stage |
| DEC5 | 2026-09-23 | 2.3 (v1 Bước 2) · Bước 2 · OQ-06 | **Kỹ năng = Skills, thuộc tính năng Khung năng lực — làm sau.** Bỏ điều kiện huy hiệu "đạt kỹ năng" khỏi phạm vi — Lý do: Thuộc tính năng khác, không thuộc gamification | "đạt kỹ năng" | PO | mọi stage |
| DEC6 | 2026-09-23 | 2.3 (v1 Bước 2) · Bước 2 · OQ-03 | **Dữ liệu đăng nhập lấy từ Keycloak.** Chuỗi ngày liên tiếp **tính từ ngày go-live tính năng**, không hồi tố — Lý do: Hệ thống không có bảng lịch sử đăng nhập của học viên | — | PO | mọi stage |
| DEC7 | 2026-09-23 | 2.3 (v1 Bước 2) · Bước 2 · OQ-08 | **Cấu hình gamification do nhân sự vận hành có quyền tương ứng** thực hiện trên UpLMS Ops | — | PO | mọi stage |
| DEC8 | 2026-09-23 | 2.3 (v1 Bước 2) · Bước 2 · OQ-08 | **Đổi cách tính điểm → áp dụng từ thời điểm đổi trở đi.** Không tính lại lịch sử | — | PO | mọi stage |
| DEC9 | 2026-09-23 | 2.3 (v1 Bước 2) · Bước 2 · OQ-10 | **Giữ nguyên logic hoàn thành Activity hiện tại** — không sửa module Learning Experience | — | PO | mọi stage |
| DEC10 | 2026-09-23 | 2.3 (v1 Bước 2) · Bước 2 · OQ-10 | **Đính chính KB:** Activity chứa Video hoàn thành khi **xem ≥80% thời lượng** (UG cũ ghi "phải play video"). Activity Text/Ảnh **giữ nguyên** — hoàn thành khi mở hiển thị — Lý do: PO xác nhận hệ thống đã cập nhật | "phải play video" | PO | mọi stage |
| DEC11 | 2026-09-23 | 2.3 (v1 Bước 2) · Bước 2 · OQ-09 | **Vấn đề cần giải:** học viên không chủ động vào học. Gamification để duy trì động lực và **làm nền cho đội truyền thông nội bộ chạy chiến dịch** thúc đẩy tinh thần học | — | PO | mọi stage |
| DEC12 | 2026-09-23 | 2.3 (v1 Bước 2) | **Stakeholder bổ sung: Đội truyền thông nội bộ** — người dùng thật của cơ chế chiến dịch — Lý do: Phát hiện từ câu trả lời OQ-09 | — | PO | mọi stage |
| DEC13 | 2026-09-23 | 1.4 (v1 CR-001) | **Bảng xếp hạng LÀM trong đợt này** — đảo ngược quyết định hoãn ngày 23/09 — Lý do: PO chỉ định | — | PO | mọi stage |
| DEC14 | 2026-09-23 | 1.4 (v1 CR-001) | **Điểm re-entry = BRD (Bước 4).** BRD lên v0.2, trình lại Gate 1 — Lý do: BRD chưa được duyệt lần nào | — | PO | mọi stage |
| DEC15 | 2026-09-23 | 1.4 (v1 CR-001) | **Xếp hạng theo phòng ban — KHÔNG làm.** Phòng ban chính là chức năng nhóm, **đồng bộ từ HRM của tổ chức** thành cây sơ đồ tổ chức. Chưa làm — Lý do: Dữ liệu chưa có: `departments` chỉ gắn `staffs`, học viên không có phòng ban | — | PO | mọi stage |
| DEC16 | 2026-09-23 | 1.4 (v1 CR-001) | **`TNT.CFG.02` = cấu hình tenant trong module Tenant** (tên, mã định danh, **múi giờ**, ngôn ngữ, định dạng ngày/số). Chưa có multi-tenant → **làm cho tổ chức hiện tại** | — | PO | mọi stage |
| DEC17 | 2026-09-23 | 1.4 (v1 CR-001) | **Kỳ lịch ≠ Chiến dịch.** Tuần/tháng/quý/năm là **mốc snapshot hệ thống tự tính**. Chiến dịch là khoảng **do vận hành setup** | — | PO | mọi stage |
| DEC18 | 2026-09-23 | 1.4 (v1 CR-001) | **Trao thưởng là hành động ngoài hệ thống.** Hệ thống chỉ giữ bảng xếp hạng cuối kỳ | — | PO | mọi stage |
| DEC19 | 2026-09-23 | 1.4 (v1 CR-001) | **`A8` bị bác bỏ** — các kỳ CÓ chồng lấn (tuần ⊂ tháng ⊂ quý ⊂ năm, cộng chiến dịch song song) → ràng buộc `C7` — Lý do: Suy ra từ yêu cầu "xem lại tháng trước, quý trước, chiến dịch đã kết thúc" | "xem lại tháng trước, quý trước, chiến dịch đã kết thúc" | PO + phân tích | mọi stage |
| DEC20 | 2026-09-23 | 1.7 (v1 Gate 1) | **OQ-A1 ✅ Hai công tắc.** `Gamification` = bật/tắt **lưu dữ liệu**, bao gồm cả hiển thị. `Visibility in UpLMS` = **chỉ xuất hiện khi Gamification bật**, bật/tắt hiển thị phía học viên — Lý do: Cần giai đoạn chạy thử trước khi mở cho học viên | — | PO | mọi stage |
| DEC21 | 2026-09-23 | 1.7 (v1 Gate 1) | **OQ-A2 ✅ Không làm chống cày riêng cho hoạt động chỉ có Text/Ảnh.** Chống cộng trùng (`C5`) và trần điểm/ngày (`S8`) vẫn áp cho mọi loại — Lý do: Rủi ro chấp nhận có chủ đích | — | PO | mọi stage |
| DEC22 | 2026-09-23 | 1.7 (v1 Gate 1) | **OQ-A3 ✅ BỎ phạm vi/bộ lọc xếp hạng theo lớp.** Gộp cùng bộ lọc theo phòng ban thành một hạng mục hoãn: **bộ lọc theo nhóm** — Lý do: Bộ lọc theo lớp sau này chính là bộ lọc theo nhóm — làm riêng bây giờ thì trùng mục đích, sau phải làm lại | — | PO | mọi stage |
| DEC23 | 2026-09-23 | 1.7 (v1 Gate 1) | **OQ-A4 ✅ Giới hạn nội dung chiến dịch — KHÔNG làm.** Thay vào đó: **chỉ số xếp hạng của chiến dịch chọn được** (điểm · số huy hiệu · số khoá hoàn thành) + **luật chỉnh sửa chiến dịch** (đang chạy thì không sửa) — Lý do: PO làm rõ: điều cần là chọn *chỉ số xếp hạng*, không phải giới hạn *nội dung sinh điểm* | — | PO | mọi stage |
| DEC24 | 2026-09-23 | 1.7 (v1 Gate 1) | **Tiêu chí phụ khi đồng hạng (`S22`) thành BẮT BUỘC** — cùng chỉ số thì ai đạt sớm hơn xếp trên — Lý do: Hệ quả của CR-002: xếp theo "số khoá hoàn thành" (0–5) hay "số huy hiệu" (0–10) gây đồng hạng hàng loạt | "số khoá hoàn thành" · "số huy hiệu" | Phân tích | mọi stage |
| DEC25 | 2026-09-23 | 1.7 (v1 Gate 1 lần 2, CR-004) | **Stakeholder tách L&D và Quản lý trực tiếp.** Quản lý trực tiếp = quản lý của học viên trong tổ chức | — | PO | mọi stage |
| DEC26 | 2026-09-23 | 1.7 (v1 Gate 1 lần 2, CR-004) | ~~**Điểm đăng nhập: mỗi lần login được điểm**, chống spam bằng khoảng cách thời gian tối thiểu (ví dụ dưới 2 tiếng không tính). **Bỏ cơ chế chuỗi ngày liên tiếp**~~<br>⬅️ **`CR-009` ngày 01/10 đảo ngược phần chuỗi.** Nay điểm check-in tăng dần theo chuỗi ngày liên tiếp — Lý do: Đơn giản hơn, không phải tính và lưu chuỗi | — | PO | mọi stage |
| DEC27 | 2026-09-23 | 1.7 (v1 Gate 1 lần 2, CR-004) | **Bốn loại huy hiệu đo bằng chỉ số đếm:** Tích cực (số lần login) · Học tập (số hoạt động hoàn thành) · Test (số bài test hoàn thành) · Course (số khoá hoàn thành) | — | PO | mọi stage |
| DEC28 | 2026-09-23 | 1.7 (v1 Gate 1 lần 2, CR-004) | **Ngưỡng lên hạng dùng nhiều chỉ số**, không chỉ điểm — điểm, huy hiệu, số khoá hoàn thành | — | PO | mọi stage |
| DEC29 | 2026-09-23 | 1.7 (v1 Gate 1 lần 2, CR-004) | **Từ vựng giữ nguyên: `Point` = điểm, `Level` = hạng học viên** — Lý do: PO chốt, không đổi tên | — | PO | mọi stage |
| DEC30 | 2026-09-23 | 1.7 (v1 Gate 1 lần 2, CR-004) | **Thông báo thành tích: chỉ đẩy trong hệ thống khi học viên đang online. Không gửi mail.** Offline thì không gửi, thành tích vào lịch sử | — | PO | mọi stage |
| DEC31 | 2026-09-23 | 1.7 (v1 Gate 1 lần 2, CR-004) | **Không bật lại 8 mail luồng chấm điểm.** Lúc nào bật thì review lại logic | — | PO | mọi stage |
| DEC32 | 2026-09-23 | 1.7 (v1 Gate 1 lần 2, CR-004) | **Bỏ US "hiệu quả chiến dịch"** — hệ thống chỉ cung cấp **kết quả**, đội truyền thông tự đo hiệu quả bên ngoài | "hiệu quả chiến dịch" | PO | mọi stage |
| DEC33 | 2026-09-23 | 1.7 (v1 Gate 1 lần 2, CR-004) | **Bỏ US "tính bù điểm"** — chạy ngầm thì bật lên đã có sẵn; tắt hẳn thì không ghi gì nên không có gì để bù | "tính bù điểm" | PO | mọi stage |
| DEC34 | 2026-09-23 | 1.7 (v1 Gate 1 lần 2, CR-004) | **Đồng hạng xử lý theo thời điểm đạt** — ai đạt trước xếp trước | — | PO | mọi stage |
| DEC35 | 2026-09-23 | 1.7 (v1 Gate 1 lần 2, CR-004) | **Chiến dịch không chồng lấn ở đợt này.** Sau này mới tạo nhiều chiến dịch cho nhiều nhóm | — | PO | mọi stage |
| DEC36 | 2026-09-23 | 1.7 (v1 Gate 1 lần 2, CR-004) | **`OQ-B3` đóng** — đội truyền thông tự đo hiệu quả bên ngoài | — | PO | mọi stage |
| DEC37 | 2026-09-23 | 1.7 (v1 Gate 1, Approved with Notes) | **`A20` ✅ Phạm vi người tham gia chiến dịch = toàn bộ học viên** ở đợt này — Lý do: Chưa có chức năng nhóm | — | PO | mọi stage |
| DEC38 | 2026-09-23 | 1.7 (v1 Gate 1, Approved with Notes) | **`A21` → đổi: điểm khi vào hệ thống tính THEO NGÀY.** Mỗi ngày học viên vào hệ thống được điểm một lần. Bỏ cơ chế "mỗi lần login + khoảng cách tối thiểu" — Lý do: Đơn giản hơn; không cần cơ chế chống spam riêng | "mỗi lần login + khoảng cách tối thiểu" | PO | mọi stage |
| DEC39 | 2026-09-23 | 1.7 (v1 Gate 1, Approved with Notes) | **`A22` ✅ Huy hiệu loại Test chỉ đếm bài ĐẠT.** Bài không có setting pass thì tính khi hoàn thành → `BR-TEST` | — | PO | mọi stage |
| DEC40 | 2026-09-23 | 1.7 (v1 Gate 1, Approved with Notes) | **`A15` ✅ Bảng xếp hạng công khai danh tính học viên** — bình thường, không vấn đề | — | PO | mọi stage |
| DEC41 | 2026-09-23 | 1.7 (v1 Gate 1, Approved with Notes) | **`OQ-B1` đóng — không còn phụ thuộc sự kiện đăng nhập Keycloak.** `S3` chuyển sang "có mặt trong ngày" nên nguồn dữ liệu khác hẳn. Mức tác động User/Auth giảm từ 🔴 Cao xuống 🟡 Thấp — Lý do: Hệ quả trực tiếp của quyết định `A21` | "có mặt trong ngày" | Phân tích | mọi stage |
| DEC42 | 2026-09-23 | 1.7 (v1 Gate 1, Approved with Notes) | **Thêm `C9`** — "ngày" trong điểm-theo-ngày và trần-điểm-mỗi-ngày cắt theo **múi giờ tổ chức**, cùng quy tắc với biên kỳ — Lý do: Hệ quả của `A21` gặp `C6` | "ngày" | Phân tích | mọi stage |
| DEC43 | 2026-09-23 | 1.7 (v1 Gate 1, Approved with Notes) | **`OQ-B16` ✅ Chỉ đếm bài Test. Quiz và Case Study KHÔNG tính** — Lý do: PO xác nhận | — | PO | mọi stage |
| DEC44 | 2026-09-23 | 1.7 (v1 Gate 1, Approved with Notes) | **🔧 Đính chính `BR-TEST`: `Pass Point` chỉ tồn tại khi `Graded Assignment = Yes`.** Test có `Graded Assignment = No` thì **không có ngưỡng đạt** → tính khi hoàn thành — Lý do: PO xác nhận. KB `03` ghi thiếu ràng buộc liên trường này | — | PO | mọi stage |
| DEC45 | 2026-09-23 | 1.7 (v1 Gate 1, Approved with Notes) | **Cập nhật KB `03-assessment.md`** — thêm `KB-TEST-01a`, `KB-TEST-01b` và ràng buộc liên trường — Lý do: Đính chính từ PO | — | PO | mọi stage |
| DEC46 | 2026-09-23 | 1.7 (v1 Gate 1, Approved with Notes) | **`OQ-B17` bỏ** — hành động "đạt điểm cao" đã ra khỏi phạm vi — Lý do: PO chốt | "đạt điểm cao" | PO | mọi stage |
| DEC47 | 2026-09-23 | 2.31 (v1 Gate 2) | **`CF-1` ✅ `Test Account` bị loại khỏi TOÀN BỘ logic gamification** — không điểm, huy hiệu, hạng, xếp hạng — Lý do: Là tài khoản của L&D và QA dùng kiểm tra khoá học; về dữ liệu là học viên thật | — | PO | 2.31, 2.4, 2.42, CR |
| DEC48 | 2026-09-23 | 2.31 (v1 Gate 2) | **`CF-2` ✅ Không tồn tại.** Một khoá chỉ ở **một lớp tại một thời điểm**. Xoá ra thêm lại → học lại → **tính như khoá mới, được điểm** | — | PO | 2.31, 2.4, 2.42, CR |
| DEC49 | 2026-09-23 | 2.31 (v1 Gate 2) | **`C5` sửa:** chống cộng trùng trong phạm vi **một lượt ghi danh**, không cắt ngang lớp. Kèm rule: **chỉ cộng điểm khi bản ghi tiến độ chuyển trạng thái sang hoàn thành, tính từ lúc bật** — Lý do: Hệ quả của `CF-2` | — | PO + phân tích | 2.31, 2.4, 2.42, CR |
| DEC50 | 2026-09-23 | 2.31 (v1 Gate 2) | **`CF-3` ✅ Chấp nhận** — đổi ngưỡng hạng thì người cũ giữ hạng, người mới theo ngưỡng mới | — | PO | 2.31, 2.4, 2.42, CR |
| DEC51 | 2026-09-23 | 2.31 (v1 Gate 2) | **`CF-5` ✅ Có huy hiệu mặc định** — mất ảnh thì rơi về ảnh mặc định | — | PO | 2.31, 2.4, 2.42, CR |
| DEC52 | 2026-09-23 | 2.31 (v1 Gate 2) | **`CF-6` ✅ Đang có chiến dịch thì không tắt gamification được** — phải dừng chiến dịch trước | — | PO | 2.31, 2.4, 2.42, CR |
| DEC53 | 2026-09-23 | 2.31 (v1 Gate 2) | **`A24` ✅ Điểm bài Test chốt tại lần chấm đầu tiên.** Chấm lại không cộng thêm | — | PO | 2.31, 2.4, 2.42, CR |
| DEC54 | 2026-09-23 | 2.31 (v1 Gate 2) | **`A25` ✅ My Learning hiện điểm TÍCH LUỸ của cá nhân** (từ lúc vào hệ thống) và hạng — không hiện điểm theo kỳ | — | PO | 2.31, 2.4, 2.42, CR |
| DEC55 | 2026-09-23 | 2.31 (v1 Gate 2) | **`A26` ✅ Không có khoá Trial** trong hệ thống | — | PO | 2.31, 2.4, 2.42, CR |
| DEC56 | 2026-09-23 | 2.31 (v1 Gate 2) | **`A27` ✅ "Không tính bù" = tính từ lúc ghi nhận.** Bật `Visibility` thì học viên **thấy ngay điểm và hạng đã tích trong lúc chạy ngầm**, kèm lịch sử tra lý do | "Không tính bù" | PO | 2.31, 2.4, 2.42, CR |
| DEC57 | 2026-09-23 | 2.31 (v1 Gate 2) | **`OQ-B2` ✅ Dữ liệu tiến độ CÓ dấu thời gian** | — | PO | 2.31, 2.4, 2.42, CR |
| DEC58 | 2026-09-23 | 2.31 (v1 Gate 2) | **`OQ-B9` ✅ Bảng xếp hạng chịu được tải.** Bảng chỉ hiển thị một số kỳ gần nhất; cộng `S19` (kỳ đã chốt đọc từ snapshot) → tối đa 5 bảng tính trực tiếp. **`R1` hạ từ 🔴 xuống 🟡** — Lý do: PO phản biện đúng — tôi đã tính thiếu tác dụng của `S19` | — | PO | 2.31, 2.4, 2.42, CR |
| DEC59 | 2026-09-23 | 2.31 (v1 Gate 2) | **`OQ-B12` ✅ Lưu hết** thời điểm đạt huy hiệu / hoàn thành khoá / hoàn thành bài Test | — | PO | 2.31, 2.4, 2.42, CR |
| DEC60 | 2026-09-23 | 2.31 (v1 Gate 2) | **Cập nhật KB:** `06-user-account.md` §8b (`Test Account`, 3 rule) · `01-course.md` (`BR-EDIT-07` thêm ngoại lệ) · `14-api-surface.md` §2.2 (bảng endpoint có nhưng tính năng không có) — Lý do: Phát sinh từ Gate 2 | — | PO | 2.31, 2.4, 2.42, CR |
| DEC61 | 2026-09-23 | 2.32 (v1 Bước 7) | **Điểm hiện với học viên: chấp nhận trễ vài phút** sau khi hoàn thành hoạt động — Lý do: Nhẹ hệ thống, không rủi ro làm chậm việc học | — | PO | 2.32, 2.42, CR |
| DEC62 | 2026-09-23 | 2.32 (v1 Bước 7) | **Bảng xếp hạng cập nhật theo chu kỳ**, hiển thị rõ **lần cập nhật cuối** | — | PO | 2.32, 2.42, CR |
| DEC63 | 2026-09-23 | 2.32 (v1 Bước 7) | **"Ngày có mặt" = cứ vào hệ thống là tính, kiểu check-in.** Không đòi hỏi thao tác học thật — Lý do: Số liệu cho thấy Activation chỉ 40.2% — vấn đề bắt đầu ngay ở chỗ không mở ứng dụng | "Ngày có mặt" | PO | 2.32, 2.42, CR |
| DEC64 | 2026-09-23 | 2.32 (v1 Bước 7) | **`S23` bỏ khỏi phạm vi.** Mỗi chỗ (huy hiệu · hạng · chiến dịch) **tự tính**; vận hành tự cấu hình tham số ở từng nơi — Lý do: Cách tính vốn khác nhau — huy hiệu và hạng đếm trọn đời, chiến dịch đếm trong khoảng ngày | — | PO | 2.32, 2.42, CR |
| DEC65 | 2026-09-23 | 2.32 (v1 Bước 7) | **`OQ-B4` đóng — PO cung cấp số liệu General Launch 8/9–21/9/2026.** Activation 40.2% (53/132) · Course start 22% (29/132) · Completion 64.1% (93/145), cả ba **đều hụt mục tiêu 80%** | — | PO | 2.32, 2.42, CR |
| DEC66 | 2026-09-23 | 2.32 (v1 Gate 3) | **Chọn Option C — Tính trong luồng.** Cộng điểm ngay trong cùng thao tác hoàn thành hoạt động, độ trễ bằng 0 — Lý do: **Dev xác nhận làm được theo cách này**, PO chọn C | — | PO + Dev | 2.32, 2.42, CR |
| DEC67 | 2026-09-23 | 2.32 (v1 Gate 3) | **`G1` được giải luôn** — học viên luôn còn trong hệ thống khi điểm được cộng, nên `US2` thực hiện trọn vẹn, không nhóm nào bị lỡ thông báo — Lý do: Hệ quả của C | — | — | 2.32, 2.42, CR |
| DEC68 | 2026-09-23 | 2.32 (v1 Gate 3) | **`NFR-GAM-01` bắt buộc: lỗi ở gamification KHÔNG được làm hỏng thao tác học.** Học viên bấm Hoàn thành thì thao tác phải thành công kể cả khi cộng điểm lỗi. Cũng không được làm chậm cảm nhận — Lý do: Điều kiện đi kèm bắt buộc của C | — | Phân tích | 2.32, 2.42, CR |
| DEC69 | 2026-09-23 | 2.32 (v1 Gate 3) | **`CG-7` nâng mức** — hai thao tác song song đều có thể cộng điểm, phải chống trùng ngay tại chỗ ghi. **`CG-8` thu hẹp** — chỉ còn áp cho tác vụ chốt kỳ — Lý do: Hệ quả của C | — | Phân tích | 2.32, 2.42, CR |
| DEC70 | 2026-09-23 | 2.32 (v1 Gate 3) | **Giữ nguyên:** check-in ghi ngay (`S-1`) · chốt kỳ là tác vụ riêng đúng biên kỳ (`S-2`) · bảng xếp hạng tính sẵn theo chu kỳ (`S-3`) | — | PO | 2.32, 2.42, CR |
| DEC71 | 2026-09-23 | CR-007 → 1.4, 2.42 | **Bỏ hẳn chiến dịch, kỳ lịch như thực thể riêng, và cơ chế chốt kỳ.** Thay bằng **bộ chọn khoảng ngày tự do** trên bảng xếp hạng — Lý do: Một bộ chọn khoảng ngày bao trùm cả hai. Nút "tháng này" chỉ là lối tắt | "tháng này" | PO | 2.42, CR |
| DEC72 | 2026-09-23 | CR-007 → 1.4, 2.42 | **Chấp nhận số liệu sống.** Kết quả của cùng một khoảng ngày có thể đổi theo thời gian — Lý do: Trao thưởng vốn làm ngoài hệ thống. Bên công bố tự ghi lại số liệu lúc công bố | — | PO | 2.42, CR |
| DEC73 | 2026-09-23 | CR-007 → 1.4, 2.42 | ❌ **Bỏ mục tiêu `O5`** — kết quả không đổi về sau — Lý do: Hệ quả trực tiếp của quyết định trên | — | PO | 2.42, CR |
| DEC74 | 2026-09-23 | CR-007 → 1.4, 2.42 | **Khoá mốc huy hiệu sau khi tạo.** Vận hành không sửa được mốc | — | PO | 2.42, CR |
| DEC75 | 2026-09-23 | CR-007 → 1.4, 2.42 | 🔄 **Trả lại `A5`: huy hiệu đã nhận giữ vĩnh viễn.** Bỏ `BR-4.6` và `BR-4.7` về quét lại và gỡ huy hiệu — Lý do: Mốc khoá nên không còn tình huống phải gỡ | — | PO | 2.42, CR |
| DEC76 | 2026-09-23 | CR-007 → 1.4, 2.42 | **Hạng: ngưỡng sửa được, theo ba chỉ số** (điểm · huy hiệu · số khoá), **logic HOẶC** — đạt mốc nào trước thì lên hạng theo mốc đó. Hạng **không tụt**, đổi ngưỡng chỉ áp từ lúc đổi | — | PO | 2.42, CR |
| DEC77 | 2026-09-23 | CR-007 → 1.4, 2.42 | **Bảng xếp hạng: bốn chỉ số** điểm · huy hiệu · hạng · số khoá, học viên tự chọn. Gốc là `All time`, khoảng ngày là bộ lọc | — | PO | 2.42, CR |
| DEC78 | 2026-09-23 | CR-007 → 1.4, 2.42 | **Nổi bật top 3, danh sách đầy đủ cuộn được bên dưới.** Học viên chưa có chỉ số vẫn hiện, ô thứ hạng để trống | — | PO | 2.42, CR |
| DEC79 | 2026-09-23 | CR-007 → 1.4, 2.42 | **Chu kỳ tính lại bảng: 8 tiếng một lần, ba lần một ngày** | — | PO | 2.42, CR |
| DEC80 | 2026-09-23 | CR-007 → 1.4, 2.42 | **Sổ giao dịch điểm giữ toàn bộ, không dọn** — Lý do: Điều kiện để `O6` đứng vững | — | PO | 2.42, CR |
| DEC81 | 2026-09-23 | CR-007 → 1.4, 2.42 | **Danh sách US từ 22 xuống 16**, trong đó 13 US làm ở đợt này — Lý do: Hệ quả của CR-007 | — | — | 2.42, CR |
| DEC82 | 2026-09-23 | 2.42 (v1 Gate 4, Approved with Notes) | **`OQ-02` ✅ Cộng điểm lỗi thì ghi lại chỗ lỗi**, không để mất âm thầm → `BR-13.8` — Lý do: Giữ `O6` — điểm đáng tin | — | PO | 2.42, CR |
| DEC83 | 2026-09-23 | 2.42 (v1 Gate 4, Approved with Notes) | **`OQ-03` ✅ Tạm chốt `Metrics success`**: Activation 40.2% · Course start 22% · Completion 64.1%, đều nhắm 80%. `Retention` chưa có mốc nền | — | PO | 2.42, CR |
| DEC84 | 2026-09-23 | 2.42 (v1 Gate 4, Approved with Notes) | **`OQ-21` ✅ Chứng chỉ cấp THEO KHOÁ, không theo lượt ghi danh.** Một học viên một chứng chỉ cho một khoá, học lại không cấp thêm. Xoá khỏi lớp thì chứng chỉ vẫn còn. Thêm lại vào lớp thì vận hành chọn *ghi nhận đã xong* hoặc *học lại từ đầu* → `BR-13.12` | — | PO | 2.42, CR |
| DEC85 | 2026-09-23 | 2.42 (v1 Gate 4, Approved with Notes) | **`OQ-10`, `OQ-11` — PO tự điền** metadata Jira, link Figma, tài khoản staging | — | PO | 2.42, CR |
| DEC86 | 2026-10-01 | CR-009 → 2.42 | **Điểm check-in tăng dần theo chuỗi.** Công thức `min(nền + (n−1) × bước, trần)`. Đảo ngược `A21` ngày 23/09 và quyết định ở `CR-004` — Lý do: PO muốn cơ chế streak | — | PO | 2.42, CR |
| DEC87 | 2026-10-01 | CR-009 → 2.42 | **Chuỗi tăng theo ngày có ĐĂNG NHẬP**, không cần hoàn thành hoạt động nào — Lý do: PO chọn sau khi nghe khuyến nghị tính theo ngày có học | — | PO | 2.42, CR |
| DEC88 | 2026-10-01 | CR-009 → 2.42 | **Đếm mọi ngày dương lịch.** Thứ bảy, chủ nhật, ngày lễ, nghỉ phép đều làm đứt chuỗi — Lý do: PO chọn sau khi nghe hai phương án còn lại (bỏ qua ngày nghỉ, quỹ bảo vệ) | — | PO | 2.42, CR |
| DEC89 | 2026-10-01 | CR-009 → 2.42 | **Đứt chuỗi không thu hồi điểm đã nhận** — Lý do: Giữ nguyên tắc xuyên suốt: không lấy lại gì của học viên | — | Phân tích | 2.42, CR |
| DEC90 | 2026-10-01 | CR-009 → 2.42 | **Chạm trần điểm ngày thì chuỗi vẫn tăng.** Chuỗi đo việc có mặt, không đo điểm — Lý do: Phân tích | — | CR-009 | 2.42, CR |
| DEC91 | 2026-10-01 | CR-009 → 2.42 | **Bỏ cảnh báo đẩy sắp đứt chuỗi.** Thay bằng dòng nhắc tĩnh trên trang Thành tích — Lý do: `BR-2.1` chỉ đẩy khi học viên đang online, mà người sắp đứt chuỗi là người không vào | — | Phân tích | 2.42, CR |
| DEC92 | 2026-10-01 | CR-009 → 2.42 | **Đổi thuật ngữ: "khử trùng" → "chống cộng trùng"** ở toàn bộ tài liệu, 67 chỗ trên 15 file — Lý do: "Khử trùng" trong tiếng Việt nghĩa là sát khuẩn, không liên quan tới deduplication | "khử trùng" · "chống cộng trùng" · "Khử trùng" | PO phát hiện | 2.42, CR |
| DEC93 | 2026-10-01 | CR-010 → 2.42 | **Bỏ trần điểm mỗi ngày.** Không còn giới hạn tổng điểm một học viên nhận trong ngày — Lý do: PO chốt khi review design | — | PO | 2.42, CR |
| DEC94 | 2026-10-01 | CR-010 → 2.42 | **Bỏ sự kiện `No points` khỏi lịch sử.** Chạm trần là lý do duy nhất sinh ra nó. Lịch sử còn ba loại sự kiện — Lý do: Hệ quả trực tiếp | — | PO | 2.42, CR |
| DEC95 | 2026-10-01 | CR-010 → 2.42 | **Giữ trần điểm chuỗi** (`BR-8.5c`) — khác với trần điểm ngày, nó chặn mức điểm cao nhất của một lần check-in — Lý do: Hai tham số khác nhau, tên gần giống | — | Phân tích | 2.42, CR |
| DEC96 | 2026-10-01 | CR-010 → 2.42 | **Logic lên hạng chốt phương án A:** mỗi mốc chạm được ở bất kỳ tiêu chí nào đều cho một hạng. Không phải lấy tiêu chí cao nhất — Lý do: Với cách lấy cao nhất, hai trong ba tiêu chí không có tác dụng và các công tắc ở `US10` mất ý nghĩa | — | PO | 2.42, CR |
| DEC97 | 2026-10-01 | CR-010 → 2.42 | **Bỏ chữ "cộng dồn"** khỏi `BR-10.2` và sơ đồ. Diễn đạt lại theo trình tự thời gian — Lý do: Chữ cũ gây hiểu nhầm thành phải gộp ba chỉ số lại | "cộng dồn" | PO phát hiện | 2.42, CR |
| DEC98 | 2026-10-01 | CR-010 → 2.42 | **Màn lịch sử tên `Achievement history`**, là panel trượt từ cạnh phải. Bộ chuỗi tiếng Anh đã định nghĩa đủ bảy mẫu câu — Lý do: Design chốt | — | PO | 2.42, CR |
| DEC99 | 2026-10-01 | 2.42 (v1 chốt design 01/10) | **Bước tăng chuỗi cố định `5`**, không cho vận hành cấu hình ở đợt này — Lý do: Giảm số tham số phải khai | — | PO | 2.42, CR |
| DEC100 | 2026-10-01 | 2.42 (v1 chốt design 01/10) | **Trần điểm chuỗi `40`** — chạm đúng ngày thứ 7 — Lý do: Người giữ chuỗi trọn một tuần kể cả T7 CN thì từ đó về sau luôn nhận mức cao nhất | — | PO | 2.42, CR |
| DEC101 | 2026-10-01 | 2.42 (v1 chốt design 01/10) | **Bỏ chuỗi dài nhất** khỏi giao diện và khỏi dữ liệu — Lý do: Chỉ số quá khứ không giúp học viên quyết định gì hôm nay | — | PO | 2.42, CR |
| DEC102 | 2026-10-01 | 2.42 (v1 chốt design 01/10) | **Danh sách huy hiệu nằm ở `My Profile` → tab `Badges`**, không nằm trên màn Gamification. Màn Gamification chỉ hiện số lượng — Lý do: Design chốt | — | PO | 2.42, CR |
| DEC103 | 2026-10-01 | 2.42 (v1 chốt design 01/10) | **Ngày đạt huy hiệu tra ở `Achievement history`**, không hiện cạnh huy hiệu — Lý do: Tránh lặp thông tin | — | PO | 2.42, CR |
| DEC104 | 2026-10-01 | 2.42 (v1 chốt design 01/10) | **Tiến độ huy hiệu chưa đạt hiện khi trỏ chuột vào**, dạng `8 check-in` — Lý do: Design chốt | — | PO | 2.42, CR |
| DEC105 | 2026-10-01 | 2.42 (v1 chốt design 01/10) | **Cột `Nguồn` trong bảng US viết rõ nội dung**, không ghi `Yêu cầu gốc dòng N` — Lý do: Tài liệu trên Lark không đếm dòng nên mã đó vô nghĩa với người đọc | — | PO | 2.42, CR |
| DEC106 | 2026-10-06 | CR-011 → 2.42 | **Trang cấu hình tự lưu, bỏ nút lưu.** Ô nhập lưu khi **rời ô hoặc bấm Enter**, không lưu trong lúc gõ. Công tắc bấm là lưu — Lý do: PO muốn design không có nút Save. Lưu trong lúc gõ thì giá trị dở dang có hiệu lực ngay và không sửa lại được, ví dụ bội số lên hạng `5` thay vì `5000` | — | PO, sau khi nghe phân tích | 2.42, CR |
| DEC107 | 2026-10-06 | CR-011 → 2.42 | **Giữ đúng hai xác nhận, dạng popover cạnh công tắc:** tắt `Gamification` · bật `Visibility in UpLMS` lần đầu. Các công tắc khác không hỏi lại — Lý do: PO muốn không popup. Hai thao tác này không đảo ngược được và gần như chỉ xảy ra một lần | — | PO, sau khi nghe phân tích | 2.42, CR |
| DEC108 | 2026-10-06 | CR-011 → 2.42 | **Tắt `Points` hoặc `Badges` thì tiêu chí lên hạng tương ứng khoá theo.** Khoá giữ nguyên giá trị, bật lại thì chạy lại như cũ — Lý do: PO chỉ định. Cách khoá giữ giá trị theo nguyên tắc chung của `BR-14.7` | — | PO | 2.42, CR |
| DEC109 | 2026-10-06 | CR-011 → 2.42 | **"Chặn lưu" đổi thành không tắt được tiêu chí hoặc bảng đang chạy cuối cùng.** Tắt chức năng nguồn mà không còn gì chạy thì vẫn cho tắt, hiện cảnh báo cố định — Lý do: Vá lỗ: tiêu chí bị khoá vẫn được tính là "bật" nên `BR-10.8` không bắt được trường hợp không ai lên hạng | "Chặn lưu" · "bật" | Phân tích, PO đồng ý | 2.42, CR |
| DEC110 | 2026-10-06 | CR-011 → 2.42 | **Số điểm không giới hạn trên** — Lý do: PO chỉ định | — | PO | 2.42, CR |
| DEC111 | 2026-10-06 | CR-011 → 2.42 | **Múi giờ lấy theo tenant, không có ô chọn trên màn Gamification.** Cách lưu do BE quyết trong technical design. Thay quyết định ở `OQ-08` — Lý do: PO chỉ định | — | PO | 2.42, CR |
| DEC112 | 2026-10-06 | CR-011 → 2.42 | **Bỏ nhãn trạng thái tổng** *(tắt hẳn · chạy ngầm · bật đầy đủ)* — Lý do: Hai công tắc cùng dòng giải thích của `Visibility in UpLMS` đã đủ để đọc ra trạng thái | — | Phân tích, PO đồng ý | 2.42, CR |
| DEC113 | 2026-10-06 | CR-011 → 2.42 | **Không viết lại cơ chế lưu trong TD-FE.** Chỉ sửa dòng nêu business rule, phần còn lại đánh dấu để Dev cập nhật — Lý do: Ranh giới PO với Dev: PO ghi *cái gì phải đúng*, Dev quyết *làm thế nào* | — | Phân tích | 2.42, CR |
| DEC114 | 2026-10-08 | CR-012 → 2.42 | **`Badges` chỉ còn ở `All time`**, giống `Level` — Lý do: Mốc huy hiệu tăng gấp đôi, đếm trong một khoảng thì người mới luôn lợi hơn người cũ | — | PO | 2.42, CR |
| DEC115 | 2026-10-08 | CR-012 → 2.42 | **Thêm bảng `Activities`.** Năm bảng: `Points` · `Activities` · `Courses` theo khung, `Level` · `Badges` chỉ ở `All time` — Lý do: Bảng `Points` nghiêng về check-in. `Activities` là bảng duy nhất đo thuần việc học theo khung | — | PO | 2.42, CR |
| DEC116 | 2026-10-08 | CR-012 → 2.42 | **`US12` khi chọn khoảng ngày thì ẩn `Level` và `Badges`, thêm cột `Activities`** — Lý do: Cùng lý do | — | Phân tích, PO đồng ý | 2.42, CR |
| DEC117 | 2026-10-08 | CR-012 → 2.42 | **Xoá `BR-6.14`** — Lý do: Rule cũ còn sót, mâu thuẫn với `BR-6.2b` và `OQ-29` | — | Phân tích, PO đồng ý | 2.42, CR |
| DEC118 | 2026-10-08 | CR-012 → 2.42 | **Chỉ số đếm không phụ thuộc công tắc `Points`.** Đếm mọi lần xảy ra trong lúc `Gamification` bật, cách lấy dữ liệu do Dev quyết — Lý do: PO đồng ý "đếm từ dữ liệu học". Khi viết PRD, Claude chỉnh lại: đếm thẳng từ dữ liệu học thì tính cả thời gian `Gamification` tắt, trái `BR-14.5`. Mở rộng cho cả số hoạt động và số bài Test vì cùng một lỗi | "đếm từ dữ liệu học" | Phân tích — **PO cần xác nhận lại phần chỉnh này** | 2.42, CR |
| DEC119 | 2026-10-08 | CR-012 → 2.42 | **Câu chữ check-in không dùng `login` hay `sign-in`.** Học viên: `for visiting UpLMS each day…` · Ops: `…when users first visit, even if they're still signed in from before…` · mốc huy hiệu: `Awarded at … check-in days` — Lý do: Học viên còn phiên đăng nhập từ hôm trước thì mở UpLMS là được tính | — | PO | 2.42, CR |
| DEC120 | 2026-10-08 | CR-012 → 2.42 | **Request nền không tính là vào hệ thống** (`BR-5.1`) — Lý do: Treo tab qua đêm sẽ tự giữ chuỗi | — | Phân tích, PO đồng ý | 2.42, CR |
| DEC121 | 2026-10-08 | CR-013 → 1.4, 2.31, 2.32, 2.42 | **Học viên chỉ có năm khung cố định**, không có bộ chọn khoảng ngày tự do. Đảo một phần `CR-007` — Lý do: Khoảng tự chọn phải tính lúc chọn — học viên spam được phép tính nặng | — | PO | 2.42, CR |
| DEC122 | 2026-10-08 | CR-013 → 1.4, 2.31, 2.32, 2.42 | **Campaign quay lại:** chọn khoảng thời gian và loại hành động, **số điểm theo cấu hình chung** — Lý do: PO ban đầu muốn sửa số điểm riêng cho campaign, rồi đổi lại chỉ chọn loại hành động | — | PO | 2.42, CR |
| DEC123 | 2026-10-08 | CR-013 → 1.4, 2.31, 2.32, 2.42 | **Re-entry từ BRD, gộp với `CR-012`.** Cả bốn Gate duyệt lại — Lý do: Campaign đổi phạm vi và cách đạt `O4` | — | PO | 2.42, CR |
| DEC124 | 2026-10-08 | CR-013 → 1.4, 2.31, 2.32, 2.42 | **Hai bảng mỗi campaign:** điểm và số hoạt động — Lý do: PO chọn theo đề xuất | — | PO | 2.42, CR |
| DEC125 | 2026-10-08 | CR-013 → 1.4, 2.31, 2.32, 2.42 | **Toàn tổ chức** tham gia — Lý do: Theo nhóm chờ HRM | — | PO | 2.42, CR |
| DEC126 | 2026-10-08 | CR-013 → 1.4, 2.31, 2.32, 2.42 | **Kết thúc thì đóng băng.** Bài chấm đạt sau khi kết thúc không tính — Lý do: Campaign làm ra để trao thưởng | — | PO | 2.42, CR |
| DEC127 | 2026-10-08 | CR-013 → 1.4, 2.31, 2.32, 2.42 | **Đang chạy chỉ sửa tên và mô tả. Chỉ xoá khi chưa bắt đầu, không dừng sớm** — Lý do: Không đổi luật giữa chừng | — | PO | 2.42, CR |
| DEC128 | 2026-10-08 | CR-013 → 1.4, 2.31, 2.32, 2.42 | **Được chồng thời gian** — Lý do: Điểm campaign chỉ là phép lọc trên sổ giao dịch | — | PO | 2.42, CR |
| DEC129 | 2026-10-08 | CR-013 → 1.4, 2.31, 2.32, 2.42 | **Đổi số điểm chung giữa chừng thì campaign mang hai mức điểm** — Lý do: Không thêm rule khoá cấu hình | — | PO | 2.42, CR |
| DEC130 | 2026-10-08 | CR-013 → 1.4, 2.31, 2.32, 2.42 | **Học viên xem lại được campaign đã kết thúc** — Lý do: Kết quả đã đóng băng sẵn | — | PO | 2.42, CR |
| DEC131 | 2026-10-08 | CR-013 → 1.4, 2.31, 2.32, 2.42 | **Ops có màn xem và xuất Excel kết quả campaign** — Lý do: `US12` là số liệu sống, không lọc loại hành động | — | PO | 2.42, CR |
| DEC132 | 2026-10-08 | CR-013 → 1.4, 2.31, 2.32, 2.42 | **Campaign nằm trong trang bảng xếp hạng, tắt `Leaderboard` thì ẩn theo** — Lý do: Một công tắc cho mọi thứ thi đua | — | PO | 2.42, CR |
| DEC133 | 2026-10-08 | CR-013 → 1.4, 2.31, 2.32, 2.42 | **`US12` giữ bộ chọn khoảng ngày tự do** — Lý do: `O4` cần, người dùng Ops ít và có quyền | — | PO | 2.42, CR |
| DEC134 | 2026-10-08 | CR-013 → 1.4, 2.31, 2.32, 2.42 | **`CF-7`: tắt `Gamification` khi campaign đang chạy vẫn cho tắt** — Lý do: `CF-6` cũ bắt dừng campaign trước, nay không dừng được | — | Phân tích — **chờ PO, `OQ-42`** | 2.42, CR |
| DEC135 | 2026-10-09 | 0 | Chuyển dự án Gamification từ luồng v1 sang v2 cùng Gamification, Report-Phase-1 và gỡ luồng v1; artifact giữ nguyên nội dung và họ mã v1; bốn gate đang chờ duyệt lại giữ nguyên trạng thái chờ; 1.2 và 2.41 ghi bỏ qua | "migrate lại toàn bộ các project cũ sang chuẩn mới, xóa phần cũ rồi push lên git 1 lần luôn" | PO | mọi stage |

## Change requests
Phân tích chi tiết từng CR ở `inputs/change-requests.md` (nguyên văn PO, nhận định, điểm re-entry, trả lời của PO).

| CR | Nội dung | Phân tích | Trạng thái |
|---|---|---|---|
| CR-001 | Bảng xếp hạng | `inputs/change-requests.md` | Đóng ở v1 |
| CR-002 | Chỉ số xếp hạng chọn được cho chiến dịch | `inputs/change-requests.md` | Đóng ở v1 |
| CR-003 | Bỏ phạm vi xếp hạng theo lớp | `inputs/change-requests.md` | Đóng ở v1 |
| CR-004 | Phản hồi Gate 1 (Need Revision) | `inputs/change-requests.md` | Đóng ở v1 |
| CR-005 | Gate 1 Approved with Notes: điểm khi vào hệ thống tính theo ngày, gỡ phụ thuộc Keycloak (BRD v0.5) | BRD, PRD Document version | Đóng ở v1 |
| CR-006 | Đính chính BR-TEST, bỏ hành động "đạt điểm cao" (BRD v0.6) | BRD, PRD Document version | Đóng ở v1 |
| CR-007 | Bỏ chiến dịch và kỳ lịch, thay bằng khoảng ngày tự do | `inputs/change-requests.md` | Đóng ở v1 |
| CR-008 | Tách cấu hình thành bốn màn, khoá mốc huy hiệu, hạng tịnh tiến, bảng xếp hạng tách theo chỉ số (PRD v0.2) | BRD, PRD Document version | Đóng ở v1 |
| CR-009 | Điểm check-in tăng dần theo chuỗi | `inputs/change-requests.md` | Đóng ở v1 |
| CR-010 | Bỏ trần điểm ngày, làm rõ logic lên hạng | `inputs/change-requests.md` | Đóng ở v1 |
| CR-011 | Trang cấu hình Ops tự lưu | `inputs/change-requests.md` | Đóng ở v1 |
| CR-012 | Bảng xếp hạng theo huy hiệu chỉ còn ở All time, thêm bảng Activities | `inputs/change-requests.md` | Mở. Gộp CR-012 vào CR-013 (PO 08/10/2026), chạy lại từ BRD; chờ duyệt lại BRD v0.7, Impact v0.3, Solution v0.2, PRD v0.10 |
| CR-013 | Campaign trở lại, học viên bỏ khoảng ngày tự do | `inputs/change-requests.md` | Mở. Gộp CR-012 vào CR-013 (PO 08/10/2026), chạy lại từ BRD; chờ duyệt lại BRD v0.7, Impact v0.3, Solution v0.2, PRD v0.10 |

## Accepted risks
| DEC | Finding | Vì sao chấp nhận |
|---|---|---|
