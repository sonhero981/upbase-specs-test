# [BRD] Gamification — Điểm, huy hiệu, hạng và bảng xếp hạng

> **Bản nháp nội bộ để chốt hướng trước khi viết PRD.** Không phải tài liệu bàn giao.

| | |
| --- | --- |
| **Tính năng** | Gamification |
| **Người viết** | Bùi Đức Huy (PO) |
| **Ngày** | 23/09/2026 |
| **Trạng thái** | `Draft - Pending Confirmation` |
| **Cỡ yêu cầu** | **L** — đủ 9 bước, đủ 4 Gate |

## Document version

| Version | Nội dung | Impact | Ngày |
| --- | --- | --- | --- |
| v0.1 | Bản đầu | — | 23/09/2026 |
| v0.2 | Đưa bảng xếp hạng vào phạm vi · tách kỳ lịch khỏi chiến dịch · bác bỏ `A8` | `CR-001` | 23/09/2026 |
| v0.3 | Chốt 4 quyết định Gate 1 · bỏ phạm vi xếp hạng theo lớp · thêm chỉ số xếp hạng cho chiến dịch | `CR-002` `CR-003` | 23/09/2026 |
| **v0.4** | **Gate 1 `Need Revision`.** Tách stakeholder L&D và Quản lý · **đổi cơ chế điểm đăng nhập** từ chuỗi ngày sang mỗi lần + chống spam · **định nghĩa lại 4 loại huy hiệu theo chỉ số đếm** · **ngưỡng lên hạng dùng nhiều chỉ số** · thông báo chỉ đẩy khi đang online, không gửi mail · bỏ US hiệu quả chiến dịch và US tính bù · chiến dịch không chồng lấn ở đợt này | `CR-004` + phản hồi Gate 1 | 23/09/2026 |

**Nguồn input:** `working/raw-inputs/yeu-cau-goc-20260923.md` · `working/raw-inputs/change-requests.md` (CR-001…004) · `working/ai-drafts/clarified-requirements-20260923.md` · `project-decisions.md`

---

# 1. Problem

**Học viên đã được ghi danh vào khoá nhưng không chủ động quay lại học.**

| | |
|---|---|
| **Ai gặp** | Học viên trên UpLMS — đã có tài khoản, đã được thêm vào lớp, đã có nội dung để học |
| **Gặp khi nào** | Trong suốt thời gian học, đặc biệt ở giai đoạn giữa khoá khi không còn động lực ban đầu và chưa thấy đích |
| **Hậu quả** | Học viên học dở dang hoặc học dồn sát hạn. Vận hành phải thúc thủ công. Đội truyền thông nội bộ muốn tổ chức phong trào học tập nhưng không có cơ chế nào để gắn hoạt động của học viên vào một chiến dịch có kết quả công bố được |

Hệ thống hiện tại **chỉ ghi nhận việc học, không phản hồi lại việc học**. Học viên hoàn thành một hoạt động thì thanh tiến độ nhích lên — ngoài ra không có gì. Không có sự ghi nhận, không có mốc để nhắm tới, không có lý do để quay lại vào ngày hôm sau khi chưa tới hạn.

---

# 2. Analytics

> ⚠️ **Chưa có dữ liệu định lượng.** Căn cứ định tính từ PO cộng với quan sát hệ thống.

| Hướng | Hiện trạng |
|---|---|
| **Cách làm hiện tại** | Vận hành theo dõi tiến độ qua dashboard SIS (*Tiến độ học trên UpLMS*), thấy ai chậm thì thúc. 30 mail tự động đều là **mail sự kiện** — chào mừng, nhắc lịch kiểm tra, báo hết hạn — không có mail nào nhằm tạo động lực |
| **Công cụ sẵn có bị hạn chế** | Giao diện soạn và gửi thông báo thủ công trên Ops **đang ẩn** (3/4 page module Notification & Email). Đội truyền thông muốn gửi thông điệp khích lệ tới nhóm học viên cụ thể thì không có đường tự phục vụ |
| **Tiêu chí quyết định** | Vận hành nhìn phần trăm tiến độ và thời hạn còn lại. Hai con số này **cho biết ai đang chậm, không cho biết ai đang cố gắng** — học viên đi đều mỗi ngày và học viên học dồn một buổi trông giống nhau khi đã cùng phần trăm |
| **Chỗ sai** | Việc thúc học phụ thuộc vào vận hành nhớ và làm thủ công. Không mở rộng được khi số lớp tăng, và **không tạo được thói quen** |

## Ba con số cần lấy trước khi viết PRD — `OQ-B4`

| # | Con số | Cách lấy |
|---|---|---|
| 1 | **Tỷ lệ học viên đứng yên** — đang có lớp còn hạn nhưng không phát sinh bản ghi tiến độ nào trong 14 ngày | `user_course_section_progress` + `class_user_instances` + hạn lớp. **Cần dấu thời gian** — phụ thuộc `OQ-B2` |
| 2 | **Mức độ học dồn** — phần trăm hoạt động được hoàn thành trong 7 ngày cuối trước hạn lớp | `user_course_section_progress` + ngày kết thúc lớp. Phụ thuộc `OQ-B2` |
| 3 | **Tỷ lệ hoàn thành khoá** — số chứng chỉ đã cấp so với số lượt ghi danh | `courses_users_certificates` / `class_user_instances`. Lấy được ngay |

> Con số 1 và 2 là hai con số nói thẳng vào `Problem`. Con số 3 là mốc để đo sau khi ra mắt.

---

# 3. Objective

| # | Kết quả muốn đạt |
|---|---|
| O1 | **Học viên quay lại học đều đặn hơn** mà không cần vận hành nhắc thủ công |
| O2 | **Nỗ lực học được ghi nhận ngay lúc nó xảy ra** |
| O3 | **Học viên có mốc ngắn hạn để nhắm tới**, thay vì chỉ có đích cuối là hoàn thành khoá |
| O4 | 🔄 **Đội truyền thông nội bộ có kết quả chiến dịch để công bố** — hệ thống cung cấp kết quả, việc đánh giá hiệu quả do đội truyền thông tự làm bên ngoài |
| O5 | **Kết quả mỗi kỳ công bố được và không thay đổi về sau**, đủ tin cậy để làm căn cứ trao thưởng |
| O6 | **Điểm số đáng tin** — mỗi con số đều truy được nguồn, và không bị thổi lên bằng thao tác đối phó |

---

# 4. Stakeholder

| Stakeholder | Action |
| --- | --- |
| **Học viên (UpLMS)** | Nhận điểm · nhận huy hiệu · lên hạng · xem trang thành tích · tra lịch sử điểm · xem bảng xếp hạng và vị trí của mình |
| **Nhân sự vận hành (UpLMS Ops)** | Khai bảng điểm · tạo huy hiệu · đặt hạng và ngưỡng · tạo và quản lý chiến dịch · bật/tắt cơ chế |
| **Đội truyền thông nội bộ** | Thiết kế và chạy chiến dịch · lấy kết quả cuối kỳ để công bố và **trao thưởng ngoài hệ thống** |
| **L&D** 🆕 | Dùng dữ liệu điểm, hạng, huy hiệu để đánh giá mức độ tham gia học tập ở quy mô tổ chức |
| **Quản lý trực tiếp** 🆕 | Quản lý trực tiếp của học viên trong tổ chức — theo dõi tình hình học của nhân viên mình phụ trách |
| Dev | Xác nhận `OQ-B1` (Keycloak) · `OQ-B2` (dấu thời gian) · `OQ-B9` (tải) · `OQ-B12` (thời điểm đạt các mốc) |
| QA | Điền `Conner case` ở PRD |

> ⚠️ **Quản lý trực tiếp chưa có công cụ riêng trong đợt này.** Để xem "nhân viên của tôi học thế nào" thì cần bộ lọc theo nhóm — đã hoãn (`N1`), chờ đồng bộ sơ đồ tổ chức từ HRM. Đợt này họ chỉ xem được bảng xếp hạng toàn tổ chức như mọi người. Ghi nhận, không đề nghị đổi.

---

# 5. Scope

## In scope

| # | Nội dung |
|---|---|
| S1 | **Cơ chế điểm** — khai hành động nào được bao nhiêu điểm, bật/tắt từng hành động |
| S2 | **Bốn hành động tính điểm từ việc học**: hoàn thành hoạt động · hoàn thành khoá · đạt bài kiểm tra · đạt điểm cao |
| **S3** | 🔄 **Hành động thứ năm — đăng nhập.** **Mỗi lần đăng nhập được điểm**, kèm **cơ chế chống spam theo khoảng cách thời gian** (ví dụ: lần đăng nhập cách lần gần nhất dưới 2 tiếng thì không tính điểm). **Không dùng cơ chế chuỗi ngày liên tiếp** |
| S4 | **Huy hiệu** — tên, hình, mô tả, điều kiện đạt |
| **S5** | 🔄 **Bốn loại huy hiệu, mỗi loại đo bằng một chỉ số đếm:**<br>• **Tích cực** — số lần đăng nhập<br>• **Học tập** — số lần hoàn thành hoạt động học<br>• **Test** — số bài kiểm tra đã hoàn thành<br>• **Course** — số khoá đã hoàn thành |
| **S6** | 🔄 **Hạng người học** — tên, hình, và **ngưỡng lên hạng dựa trên nhiều chỉ số**, không chỉ điểm: điểm · số huy hiệu · số khoá hoàn thành |
| S7 | **Hai loại điểm tách nhau**: điểm tích luỹ vĩnh viễn (xét hạng) và điểm theo kỳ (xếp hạng) |
| S8 | **Chống cày điểm** — khử trùng nội dung đã hoàn thành, trần điểm tối đa mỗi ngày |
| S9 | **Lịch sử điểm** — học viên tra được từng lần cộng đến từ đâu |
| **S10** | 🔄 **Thông báo thành tích** — **chỉ đẩy trong hệ thống khi học viên đang ở trong hệ thống**. Không gửi mail. Học viên không online thì **không gửi**, thành tích vẫn được ghi nhận và tra được ở lịch sử |
| S11 | **Trang "Thành tích của tôi"** — điểm, hạng, huy hiệu đã có, huy hiệu sắp đạt kèm phần còn thiếu |
| S12 | **Hai công tắc ở cấp tổ chức:**<br>• **`Gamification`** — bật/tắt việc **lưu dữ liệu**, bao gồm cả việc hiển thị<br>• **`Visibility in UpLMS`** — chỉ xuất hiện khi `Gamification` bật; bật/tắt hiển thị phía học viên |
| S13 | **Phân quyền cấu hình** |
| S14 | **Bảng xếp hạng theo kỳ lịch** — tuần · tháng · quý · năm. Hệ thống tự tính, không cần cấu hình |
| S15 | **Chiến dịch** — vận hành khai khoảng thời gian bất kỳ (không cần trùng biên lịch), kèm tên và phạm vi người tham gia |
| S16 | **Chỉ số xếp hạng của chiến dịch chọn được** — theo điểm · số huy hiệu · số khoá hoàn thành |
| S17 | **Luật chỉnh sửa chiến dịch** — chiến dịch **đang chạy thì không sửa được** |
| S18 | **"Vị trí của tôi"** — luôn hiện thứ hạng người đang xem kèm vài người liền kề |
| S19 | **Chốt kỳ** — hết kỳ thì đóng băng bảng, lưu kết quả cuối **kèm chỉ số đã dùng để xếp**, mở kỳ mới về 0 |
| S20 | **Lịch sử các kỳ đã kết thúc** — xem lại bảng xếp hạng tháng trước, quý trước, chiến dịch đã xong |
| S21 | **Tham số múi giờ ở cấp tổ chức** — biên kỳ cắt theo múi giờ tổ chức, không theo giờ máy chủ |
| S22 | **Tiêu chí phụ khi đồng hạng** — cùng chỉ số thì **ai đạt mức đó sớm hơn xếp trên** |
| **S23** | 🆕 **Danh mục chỉ số đo lường dùng chung** — một tập chỉ số duy nhất phục vụ cả ba chỗ: điều kiện huy hiệu (S5) · ngưỡng lên hạng (S6) · chỉ số xếp hạng chiến dịch (S16). Xem §6.8 |

## Out of scope

| # | Không làm | Vì sao |
|---|---|---|
| N1 | **Bộ lọc bảng xếp hạng theo nhóm** — gồm cả theo lớp và theo phòng ban | Chờ chức năng nhóm **đồng bộ từ HRM**. Làm riêng cho lớp bây giờ thì trùng mục đích |
| N2 | **Chống cày riêng cho hoạt động chỉ có Text/Ảnh** | PO chốt không cần. Khử trùng và trần điểm/ngày vẫn áp cho mọi loại |
| **N3** | 🆕 **Nhiều chiến dịch chạy song song** | PO chốt: đợt này **mỗi lần chỉ một chiến dịch**. Sau này mới tạo nhiều chiến dịch cho nhiều nhóm khác nhau |
| **N4** | 🆕 **Điều kiện huy hiệu theo chuỗi ngày liên tiếp · theo mốc thời gian · theo nội dung cụ thể** | Thay bằng bốn loại huy hiệu đo bằng chỉ số đếm (S5) |
| **N5** | 🆕 **Thông báo thành tích qua email** | PO chốt chỉ đẩy trong hệ thống. Không đụng tới 30 mail hiện có |
| N6 | **Giới hạn nội dung được tính trong chiến dịch** | PO không yêu cầu |
| N7 | **Tính năng Lộ trình học** và hành động "hoàn thành lộ trình" | Tính năng riêng, làm sau |
| N8 | **Tính năng Khung năng lực / Skills** và huy hiệu theo kỹ năng | Tính năng riêng, làm sau |
| N9 | **Sửa logic hoàn thành Activity** | PO chốt giữ nguyên |
| N10 | **Quản lý phần thưởng trong hệ thống** | Trao thưởng là hành động ngoài hệ thống |
| **N11** | 🆕 **Trang đo hiệu quả chiến dịch** | PO chốt: hệ thống chỉ cung cấp **kết quả** chiến dịch (S19, S20). Đội truyền thông **tự đo hiệu quả bên ngoài** |
| N12 | **Gamification cho nhân sự Ops** | Chỉ áp dụng cho học viên |
| N13 | **Thi đua theo đội / nhóm** | Chỉ xếp hạng cá nhân |
| N14 | **Cấu hình gamification riêng theo lớp hoặc khoá** | Cấu hình ở cấp tổ chức |
| N15 | **Màn quản lý nhiều tổ chức** | Chưa có multi-tenant. Dữ liệu vẫn thiết kế theo tổ chức — `C1` |
| N16 | **Module Tenant (`TNT.CFG.02`) đầy đủ** | Đợt này chỉ khai tham số múi giờ (S21) |

> 🗑️ **Đã gỡ khỏi v0.3:** *"tính bù điểm cho giai đoạn tắt"* — khái niệm này không tồn tại. Chạy ngầm thì dữ liệu đã có sẵn, bật lên là hiện. Tắt hẳn thì không ghi gì, không có gì để bù.

## Potential scope

Bộ lọc theo nhóm sau khi đồng bộ HRM · nhiều chiến dịch song song cho nhiều nhóm · giới hạn nội dung chiến dịch · điểm cho lộ trình · huy hiệu theo kỹ năng · đổi điểm lấy phần thưởng

---

# 6. Solution (khung)

## 6.1 Hướng tổng thể

```
Lớp 1  Bắt sự kiện học tập      ← nghe các việc học viên đã làm, gồm cả đăng nhập
Lớp 2  Quy đổi ra điểm          ← áp bảng cấu hình + luật chống cày + chống spam
Lớp 3  Tích luỹ và xét ngưỡng   ← cộng dồn, đếm chỉ số, xét huy hiệu, xét hạng
Lớp 4  Xếp hạng theo kỳ         ← tính thứ hạng từ sổ giao dịch theo khoảng ngày
Lớp 5  Phản hồi cho học viên    ← đẩy khi online + trang thành tích + bảng xếp hạng
```

Nguyên tắc xuyên suốt: **gamification chỉ đọc, không sửa dữ liệu học tập.**

## 6.2 Hai loại kỳ

| | **Kỳ lịch** | **Chiến dịch** |
|---|---|---|
| Ai tạo | **Hệ thống tự tính** | **Vận hành khai tay** |
| Biên | Cố định theo lịch — tuần, tháng, quý, năm. Không dùng cửa sổ trượt | Hai ngày bất kỳ, không cần trùng biên lịch |
| Chồng lấn | **Có** — tuần ⊂ tháng ⊂ quý ⊂ năm | **Không** — đợt này mỗi lần chỉ một chiến dịch (`N3`) |
| Cấu hình | Không cần màn nào | Tên · phạm vi người tham gia · chỉ số xếp hạng |
| Chỉnh sửa | — | **Đang chạy thì không sửa được** |
| Chỉ số xếp | **Luôn theo điểm** | **Chọn được** (S16) |

## 6.3 Ràng buộc thiết kế bắt buộc

| # | Ràng buộc | Vì sao |
|---|---|---|
| **C1** | Cấu hình gắn với **tổ chức**, không đóng cứng | Định hướng đa tenant |
| **C2** | **Mọi danh mục phải mở rộng được bằng cấu hình** — hành động tính điểm, loại huy hiệu, chỉ số đo lường, chỉ số xếp hạng | Lộ trình, kỹ năng, bộ lọc nhóm, nhiều chiến dịch song song đều sẽ thêm sau |
| **C3** | Lưu **từng lần cộng điểm kèm thời điểm** | Nền của lịch sử điểm, xếp hạng theo kỳ, tiêu chí phụ khi đồng hạng, và luật chống cày |
| **C4** | Đổi cấu hình điểm → **áp dụng từ thời điểm đổi** | PO chốt |
| **C5** | Khử trùng "đã học" tính theo **người học**, không theo lượt ghi danh lớp | Học viên có thể học cùng nội dung qua nhiều lớp |
| **C6** | **Biên kỳ cắt theo múi giờ của tổ chức**, không theo giờ máy chủ | Module Tenant chưa có → đợt này khai một tham số múi giờ cấp tổ chức |
| **C7** | **Một lần cộng điểm thuộc về nhiều kỳ lịch cùng lúc** → điểm theo kỳ **tính từ sổ giao dịch theo khoảng ngày**. **Kết quả cuối kỳ phải lưu cứng** | Kỳ lịch lồng nhau theo bản chất |
| **C8** | **Mọi mốc dùng để xếp hạng phải lưu được thời điểm đạt** — cộng điểm, đạt huy hiệu, hoàn thành khoá, đăng nhập | Cần cho S22 và cho luật chống spam đăng nhập. `OQ-B12` |

## 6.4 ✅ Ngữ nghĩa của việc tắt gamification *(đã chốt)*

| Công tắc | Ý nghĩa |
|---|---|
| **`Gamification`** | Bật/tắt việc **lưu dữ liệu**, bao gồm cả việc hiển thị |
| **`Visibility in UpLMS`** | **Chỉ xuất hiện khi `Gamification` đang bật.** Bật/tắt hiển thị phía học viên |

| Trạng thái | `Gamification` | `Visibility` | Dùng khi nào |
|---|---|---|---|
| Tắt hẳn | Tắt | *(không hiện)* | Tổ chức không dùng cơ chế này |
| **Chạy ngầm** | Bật | Tắt | **Chạy thử trước khi mở cho học viên** |
| Bật đầy đủ | Bật | Bật | Vận hành bình thường |

**Luật kèm theo:**

1. Chuyển từ *Chạy ngầm* sang *Bật đầy đủ*: **không bắn thông báo hồi tố.** Dữ liệu đã ghi trong giai đoạn chạy ngầm **hiện đầy đủ ngay** — điểm, huy hiệu, hạng, lịch sử.
2. Bật lại sau khi *Tắt hẳn*: **tính từ thời điểm bật.** Giai đoạn tắt không ghi gì nên không có gì để bù.

## 6.5 ✅ Chống cày điểm *(đã chốt)*

Không làm cơ chế riêng cho hoạt động chỉ có Text/Ảnh. Hai cơ chế chung áp cho mọi loại:

| Cơ chế | Tác dụng |
|---|---|
| **Khử trùng nội dung đã hoàn thành** (`C5`) | Mỗi nội dung chỉ trả điểm **một lần duy nhất trong đời** |
| **Trần điểm tối đa mỗi ngày** (`S8`) | Chặn việc dồn toàn bộ trong một buổi |

## 6.6 ✅ Chỉ số xếp hạng chiến dịch và tiêu chí phụ *(đã chốt)*

Chiến dịch chọn xếp theo: **điểm** · **số huy hiệu** · **số khoá hoàn thành**.

Ba chỉ số khác nhau về độ phân tán — "số khoá hoàn thành" trong một kỳ chỉ ở khoảng 0–5 nên gây đồng hạng hàng loạt. Vì vậy **`S22` là bắt buộc**: cùng chỉ số thì ai đạt mức đó sớm hơn xếp trên.

Trùng cả thời điểm thì hiếm tới mức bỏ qua được, nhưng thứ hạng hiển thị vẫn phải xác định — chốt một quy tắc phụ cố định ở PRD để không nhảy mỗi lần tải lại.

## 6.7 ✅ Cơ chế điểm đăng nhập *(mới — thay cho chuỗi ngày liên tiếp)*

**Mỗi lần đăng nhập được điểm**, chặn spam bằng **khoảng cách thời gian tối thiểu giữa hai lần tính điểm**.

| | v0.3 (cũ) | **v0.4 (mới)** |
|---|---|---|
| Cơ chế | Đếm chuỗi ngày đăng nhập liên tiếp | Mỗi lần đăng nhập một điểm |
| Chống lạm dụng | Bản chất chuỗi đã chặn | **Khoảng cách tối thiểu** — ví dụ dưới 2 tiếng thì không tính |
| Dữ liệu cần | Lịch sử đăng nhập theo ngày, tính chuỗi | **Thời điểm đăng nhập gần nhất có tính điểm** |

**Đơn giản hơn đáng kể.** Không phải tính và lưu chuỗi, không phải xử lý việc chuỗi bị đứt, không phải quyết định chuỗi tính theo múi giờ nào.

Vẫn phụ thuộc Keycloak (`OQ-B1`) — nhưng chỉ cần **sự kiện đăng nhập kèm thời điểm**, không cần lịch sử dài.

> Chỉ số "số lần đăng nhập" này cũng chính là chỉ số đo huy hiệu loại **Tích cực** (S5).

## 6.8 🆕 Một danh mục chỉ số dùng chung cho ba chỗ

Sau phản hồi Gate 1, cùng một khái niệm **"chỉ số đo lường"** xuất hiện ở ba nơi:

| Nơi dùng | Chỉ số |
|---|---|
| **Điều kiện huy hiệu** (S5) | Số lần đăng nhập · số hoạt động hoàn thành · số bài test hoàn thành · số khoá hoàn thành |
| **Ngưỡng lên hạng** (S6) | Điểm · số huy hiệu · số khoá hoàn thành |
| **Chỉ số xếp hạng chiến dịch** (S16) | Điểm · số huy hiệu · số khoá hoàn thành |

`Recommendation` — **định nghĩa một danh mục chỉ số duy nhất và dùng lại ở cả ba chỗ** (`S23`), thay vì xây ba cơ chế riêng.

Lý do không chỉ là gọn:

- Ba chỗ này sẽ **cùng phải mở rộng** khi thêm lộ trình (N7) hay kỹ năng (N8). Ba cơ chế riêng nghĩa là mỗi lần thêm phải sửa ba chỗ
- `C8` (lưu thời điểm đạt) áp cho mọi chỉ số — định nghĩa một lần thì luật này áp một lần
- Cách tính "số khoá hoàn thành" phải giống hệt nhau ở cả ba chỗ. Tách riêng là mở đường cho ba định nghĩa lệch nhau — loại lỗi rất khó phát hiện và phá thẳng `O6`

Tập chỉ số tối thiểu cho đợt này: **điểm tích luỹ · số lần đăng nhập · số hoạt động hoàn thành · số bài test hoàn thành · số khoá hoàn thành · số huy hiệu**.

---

# 7. Danh sách User Story dự kiến

## Phía học viên (UpLMS)

| ID | User Story | Nguồn | Ghi chú |
| --- | --- | --- | --- |
| **US1** | Là học viên, tôi cần xem điểm, hạng và huy hiệu đã đạt để biết nỗ lực học của mình được ghi nhận tới đâu | Dòng 10 · O2 | Trang "Thành tích của tôi" |
| **US2** | Là học viên, tôi cần được báo ngay khi nhận điểm, đạt huy hiệu hoặc lên hạng **trong lúc đang dùng hệ thống** để cảm nhận được sự ghi nhận đúng lúc | Dòng 9 · O2 · S10 | Không gửi khi offline — vẫn tra được ở lịch sử |
| **US3** | Là học viên, tôi cần tra được từng lần cộng điểm đến từ đâu để tin vào con số của mình | Dòng 8 · O6 · C3 | |
| **US4** | Là học viên, tôi cần biết huy hiệu nào sắp đạt và còn thiếu gì để có mục tiêu ngắn hạn | Dòng 10 · O3 | Tính tiến độ tới **mọi** huy hiệu chưa đạt |
| **US5** | Là học viên, tôi cần việc quay lại hệ thống được ghi nhận thành điểm để có lý do mở ứng dụng mỗi ngày | Dòng 2 · S3 · O1 | 🔄 Đổi từ chuỗi ngày sang mỗi lần đăng nhập. Phụ thuộc `OQ-B1` |
| **US6** | Là học viên, tôi cần xem bảng xếp hạng của kỳ tôi chọn để biết mình đứng ở đâu so với người khác | CR-001 · S14 | Toàn tổ chức. Kỳ lịch + chiến dịch |
| **US7** | Là học viên, tôi cần luôn thấy vị trí của chính mình kèm vài người liền kề để biết mình cần hơn ai một chút là lên hạng | CR-001 · S18 | Cơ chế giảm nhẹ chính cho bảng toàn tổ chức |
| **US8** | Là học viên, tôi cần xem lại bảng xếp hạng của các kỳ đã kết thúc để nhìn lại thành tích đã đạt | CR-001 · S20 | |

## Phía vận hành (UpLMS Ops)

| ID | User Story | Nguồn | Ghi chú |
| --- | --- | --- | --- |
| **US9** | Là nhân sự vận hành, tôi cần khai hành động nào được bao nhiêu điểm và bật/tắt từng hành động để điều chỉnh cơ chế theo mục tiêu từng giai đoạn | Dòng 1, 2 | Gồm cả khoảng cách tối thiểu giữa hai lần tính điểm đăng nhập (S3) |
| **US10** | Là nhân sự vận hành, tôi cần tạo và quản lý huy hiệu theo bốn loại với ngưỡng số lượng để thiết kế các mốc mục tiêu cho học viên | Dòng 3, 4 · S5 | 🔄 Bốn loại đo bằng chỉ số đếm |
| **US11** | Là nhân sự vận hành, tôi cần đặt các hạng và ngưỡng lên hạng theo nhiều chỉ số để phân tầng mức độ tham gia của học viên | Dòng 5 · S6 | 🔄 Không chỉ theo điểm |
| **US12** | Là nhân sự vận hành, tôi cần tạo chiến dịch có thời hạn riêng, chọn phạm vi người tham gia và chọn chỉ số xếp hạng, để chạy đợt thi đua phù hợp với mục tiêu từng đợt | CR-001 · CR-002 · S15, S16 | Đợt này mỗi lần một chiến dịch (`N3`) |
| **US13** | Là nhân sự vận hành, tôi cần chiến dịch đang chạy không sửa được để kết quả thi đua không bị thay đổi luật giữa chừng | CR-002 · S17 | |
| **US14** | Là nhân sự vận hành, tôi cần bảng xếp hạng được đóng băng và lưu lại khi hết kỳ để công bố kết quả không thay đổi và trao thưởng | CR-001 · S19 · O5 | Lưu kèm chỉ số đã dùng |
| **US15** | Là nhân sự vận hành, tôi cần điểm phản ánh việc học thật, không bị đẩy lên bằng thao tác đối phó, để cơ chế còn đáng tin | Dòng 7 · O6 | Chịu `C5` |
| **US16** | Là nhân sự vận hành, tôi cần bật/tắt gamification và bật/tắt hiển thị phía học viên riêng biệt, để chạy thử cơ chế trước khi mở cho học viên | Dòng 11 · S12 | |
| **US17** | Là quản trị, tôi cần phân quyền để chỉ vai trò vận hành phù hợp mới sửa được cấu hình gamification | `[suy ra]` · S13 | |

## Chưa làm trong đợt này

| ID | User Story | Nguồn | Ghi chú |
| --- | --- | --- | --- |
| **US18** | *Bộ lọc bảng xếp hạng theo nhóm* — Là quản lý trực tiếp, tôi cần lọc bảng xếp hạng theo nhóm để biết nhân viên mình phụ trách học thế nào — **chưa làm** | N1 | Chờ chức năng nhóm đồng bộ từ HRM. **Đây là công cụ duy nhất phục vụ stakeholder Quản lý trực tiếp** |
| **US19** | *Nhiều chiến dịch song song* — Là nhân sự vận hành, tôi cần chạy nhiều chiến dịch cùng lúc cho nhiều nhóm khác nhau — **chưa làm** | N3 | Phụ thuộc chức năng nhóm |
| **US20** | *Giới hạn nội dung chiến dịch* — **chưa làm** | N6 | |
| **US21** | *Điểm cho lộ trình* — **chưa làm** | N7 | Chờ tính năng Lộ trình |
| **US22** | *Huy hiệu theo kỹ năng* — **chưa làm** | N8 | Chờ tính năng Khung năng lực |

---

# 8. Tác động tới hệ thống hiện tại

> **Chưa chạy Impact Analysis.** Đánh giá sơ bộ. **Chi tiết ở Gate 2.**

| Vùng ảnh hưởng | Mức | Ghi chú |
| --- | --- | --- |
| **Dữ liệu** | 🔴 Cao | Toàn bộ cấu trúc điểm, huy hiệu, hạng, kỳ, chiến dịch, sổ giao dịch, snapshot là mới. Chịu C1–C8 |
| **Hiệu năng** | 🔴 Cao | Xếp hạng tính từ sổ giao dịch theo khoảng ngày, toàn tổ chức, nhiều kỳ lồng nhau, ba chỉ số — `OQ-B9` |
| **User / Auth** | 🔴 Cao | 🔄 Lên từ 🟠. `S3` và huy hiệu loại **Tích cực** đều đo bằng số lần đăng nhập → Keycloak thành **nguồn dữ liệu chính**, không còn là phụ thuộc phụ. `OQ-B1` |
| **Tổ chức / Tenant** | 🟠 Vừa | Thêm tham số múi giờ cấp tổ chức (S21, C6) |
| **Learning Experience** | 🟠 Vừa | Nguồn sự kiện chính. Chỉ đọc, không sửa |
| **Notification** | 🟢 **Rất thấp** | 🔄 **Giảm mạnh từ 🟠.** `S10` chỉ đẩy trong hệ thống khi học viên đang online, **không gửi mail, không dùng cơ chế thông báo hiện có**. Gỡ được toàn bộ phụ thuộc vào module Notification đang ẩn và ràng buộc job nửa tiếng (`KB-NOTI-05`) |
| **Assessment / Grading** | 🟠 Vừa | Nguồn sự kiện. Huy hiệu loại **Test** đo bằng số bài kiểm tra hoàn thành |
| **Course / Certificate** | 🟠 Vừa | Nguồn sự kiện. "Số khoá hoàn thành" dùng ở ba chỗ: huy hiệu loại Course, ngưỡng lên hạng, chỉ số xếp hạng |
| **Class** | 🟡 Thấp | Là lý do sinh ra `C5` |
| **Phân quyền** | 🟡 Thấp | Thêm nhóm quyền mới |

---

# 9. Assumptions

| # | Giả định | Kiểm chứng thế nào |
|---|---|---|
| A1 | Gamification chỉ áp dụng cho **học viên UpLMS** | PO xác nhận |
| A2 | Cấu hình đặt ở **UpLMS Ops** | PO xác nhận |
| A3 | **Hạng chỉ lên, không tụt** | PO xác nhận |
| A4 | Điểm tích luỹ **không hết hạn** | PO xác nhận |
| A5 | Huy hiệu **đạt rồi giữ vĩnh viễn**, không thu hồi | PO xác nhận |
| A6 | Một hành động đồng thời cộng vào **cả điểm tích luỹ và điểm theo kỳ** | PO xác nhận |
| A7 | Điểm là **số nguyên** | PO xác nhận |
| A9 | Ảnh huy hiệu và ảnh hạng dùng hạ tầng quản lý tài nguyên sẵn có | Gate 2 |
| A10 | **Dữ liệu tiến độ học có dấu thời gian** | Dev — `OQ-B2` |
| A11 | **Keycloak ghi và giữ được sự kiện đăng nhập kèm thời điểm** | Dev — `OQ-B1` |
| A12 | Vận hành **không cần sửa hay xoá điểm thủ công** của một học viên | PO xác nhận |
| A13 | **Bảng xếp hạng chỉ hiện học viên, không hiện nhân sự Ops** | PO xác nhận |
| A14 | **Học viên bị Block hoặc đã rời tổ chức không xuất hiện trong bảng đang chạy**, nhưng **vẫn giữ nguyên trong snapshot kỳ đã chốt** | PO xác nhận |
| A15 | **Bảng xếp hạng công khai danh tính học viên** với nhau | PO xác nhận — **vấn đề riêng tư** |
| A16 | **Kỳ lịch bắt đầu từ thời điểm bật tính năng**, không dựng lại bảng cho kỳ trước ngày go-live | PO xác nhận |
| A17 | **Kỳ lịch luôn xếp theo điểm.** Chọn chỉ số chỉ áp cho chiến dịch | PO xác nhận |
| A18 | **Chiến dịch chưa tới ngày bắt đầu thì sửa được**, chỉ khoá khi đã chạy | PO xác nhận |
| **A19** | 🔄 **Tắt `Visibility in UpLMS` thì không đẩy thông báo thành tích** — học viên không xem được thì không báo | PO xác nhận |
| **A20** | 🆕 **Phạm vi người tham gia chiến dịch ở đợt này là toàn bộ học viên** — chưa có chức năng nhóm nên chưa khoanh được | PO xác nhận |
| **A21** | 🆕 **"Đăng nhập" tính cả phiên tự động khôi phục** (mở lại app còn phiên) hay **chỉ tính lần nhập thông tin đăng nhập thật**? | PO xác nhận — ảnh hưởng thẳng tới `S3` và huy hiệu Tích cực |
| **A22** | 🆕 **Huy hiệu loại Test đếm số bài kiểm tra *hoàn thành***, không phân biệt đạt hay trượt | PO xác nhận |

---

# 10. Open Questions

| # | Câu hỏi | Vì sao quan trọng | Người trả lời | Chặn bước sau? |
| --- | --- | --- | --- | --- |
| **OQ-B1** | **Keycloak có ghi sự kiện đăng nhập kèm thời điểm không, lấy ra bằng cách nào?** | 🔺 **Mức độ quan trọng tăng.** Giờ là nguồn cho cả `S3` (điểm đăng nhập) lẫn huy hiệu loại Tích cực. Không có thì mất hai hạng mục | Dev | **Yes** — trước Gate 2 |
| **OQ-B2** | **Dữ liệu tiến độ học có dấu thời gian không?** | Cần cho C5, C7, trần điểm/ngày, và cho hai con số ở §2 | Dev | **Yes** — trước Gate 2 |
| **OQ-B9** | **Bảng xếp hạng chịu tải được không?** | Quyết định giữa tính trực tiếp và tính sẵn theo chu kỳ | Dev | **Yes** — trước Gate 2 |
| **OQ-B12** | **Thời điểm đạt huy hiệu, hoàn thành khoá, hoàn thành bài test có lưu được không?** | `C8` — cần cho tiêu chí phụ khi đồng hạng và cho mọi chỉ số đếm | Dev | **Yes** — trước Gate 2 |
| **OQ-B11** | **Múi giờ tổ chức khai ở đâu trong đợt này?** Đề xuất: một tham số cấp tổ chức, để module Tenant sau tiếp quản | `C6` | PO + Dev | No — Gate 2 |
| **OQ-B14** 🆕 | **`A21` — "đăng nhập" là gì?** Mở lại app khi còn phiên có tính là một lần đăng nhập không? | Với SSO Lark, học viên có thể hiếm khi nhập lại thông tin đăng nhập. Nếu chỉ tính lần đăng nhập thật thì cả `S3` lẫn huy hiệu Tích cực gần như không phát sinh | PO + Dev | No — nhưng ảnh hưởng lớn tới giá trị của S3 |

## ✅ Đã đóng ở vòng này

| # | Kết luận |
|---|---|
| `OQ-B3` | Đội truyền thông **tự đo hiệu quả bên ngoài**. Hệ thống chỉ cung cấp kết quả chiến dịch → `N11`, gỡ US hiệu quả chiến dịch |
| `OQ-B4` | Ba con số đã nêu cụ thể ở §2 kèm cách lấy |
| `OQ-B5` + `OQ-B6` | **Chỉ đẩy trong hệ thống khi học viên đang online. Không gửi mail.** Offline thì không gửi, thành tích vẫn vào lịch sử → `S10`, `N5`. Gỡ luôn nguy cơ trùng với mail #10/#29 |
| `OQ-B7` | **Không bật lại 8 mail luồng chấm điểm.** Lúc nào bật thì review lại logic |
| `OQ-B8` | **Giữ từ vựng: `Point` = điểm, `Level` = hạng học viên.** Nhãn giao diện phải phân biệt được với `Pass Point`, `Course Level`, `Staff Level` |
| `OQ-B10` | Đồng hạng xử lý theo **thời điểm đạt — ai đạt trước xếp trước** |
| `OQ-B13` | **Chiến dịch không chồng lấn ở đợt này** → `N3`. Sau này mới tạo nhiều chiến dịch cho nhiều nhóm |

---

# 11. References

## Knowledge Base đã đọc

| File | Dùng cho |
|---|---|
| `07-learning-experience.md` | `KB-LX-03a`, `KB-LX-03b` — nền của §6.5. **Đã cập nhật trong đợt này** |
| `09-notification-email.md` | `KB-NOTI-05`, trạng thái ẩn — nay chỉ còn để đối chiếu, không còn là phụ thuộc |
| `13-mail-events.md` | 30 mail tự động — xác nhận gamification **không đụng tới** |
| `12-data-model.md` | Cấu trúc dữ liệu — nền của `C5`, `C6`; phòng ban chỉ gắn nhân sự |
| `14-api-surface.md` | `Group Management`, `Department Management` |
| `15-product-direction.md` | Định hướng đa tenant — nền của `C1` |
| `01-course.md` · `03-assessment.md` · `04-class.md` · `06-user-account.md` · `08-certificate.md` | Nguồn sự kiện tính điểm và các chỉ số đếm |

## Nguồn khác

| Nguồn | |
|---|---|
| Yêu cầu gốc | `working/raw-inputs/yeu-cau-goc-20260923.md` |
| Change requests | `working/raw-inputs/change-requests.md` — **CR-001…CR-004** |
| Bản làm rõ | `working/ai-drafts/clarified-requirements-20260923.md` |
| Quyết định đã chốt | `project-decisions.md` |
| BRD bản trước | `docs/brd/brd-v0.1` · `v0.2` · `v0.3` (23/09/2026) |
| Schema DB | [Lark → Data Architecture](https://upbasevn.sg.larksuite.com/wiki/MaFpweI68iKNMvkTioLlJ1uJgQd) — đối chiếu 23/09/2026 |
| Swagger | `lms-be.staging.upbase.asia/api/v1/docs` · `ops-be.staging.upbase.asia/api/v1/docs` |
| Tham chiếu ngoài | `TNT.CFG.02` — Hồ sơ tổ chức và tham số, thuộc module Tenant *(chưa làm)* |
