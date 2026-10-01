# [BRD] Gamification — Điểm, huy hiệu, hạng và bảng xếp hạng

| | |
| --- | --- |
| **Tính năng** | Gamification |
| **Người viết** | Bùi Đức Huy (PO) |
| **Ngày** | 23/09/2026 |
| **Trạng thái** | ✅ **`Approved with Notes`** — Gate 1 duyệt 23/09/2026 |
| **Cỡ yêu cầu** | **L** — đủ 9 bước, đủ 4 Gate |

## Document version

| Version | Nội dung | Impact | Ngày |
| --- | --- | --- | --- |
| v0.1 | Bản đầu | — | 23/09 |
| v0.2 | Đưa bảng xếp hạng vào phạm vi · tách kỳ lịch khỏi chiến dịch | `CR-001` | 23/09 |
| v0.3 | Chốt 4 quyết định Gate 1 · bỏ phạm vi xếp hạng theo lớp · thêm chỉ số xếp hạng chiến dịch | `CR-002` `CR-003` | 23/09 |
| v0.4 | Gate 1 `Need Revision` · đổi cơ chế điểm đăng nhập · định nghĩa lại huy hiệu · thu hẹp thông báo | `CR-004` | 23/09 |
| **v0.5** | ✅ **Gate 1 `Approved with Notes`.** Điểm đăng nhập đổi thành **mỗi ngày một lần** · huy hiệu Test **chỉ tính bài đạt** · riêng tư bảng xếp hạng đã chốt · **phụ thuộc Keycloak giảm mạnh** | `CR-005` | 23/09 |

**Nguồn input:** `working/raw-inputs/yeu-cau-goc-20260923.md` · `change-requests.md` (CR-001…005) · `clarified-requirements-20260923.md` · `project-decisions.md`

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
| **Cách làm hiện tại** | Vận hành theo dõi tiến độ qua dashboard SIS (*Tiến độ học trên UpLMS*), thấy ai chậm thì thúc. 30 mail tự động đều là **mail sự kiện** — không có mail nào nhằm tạo động lực |
| **Công cụ sẵn có bị hạn chế** | Giao diện soạn và gửi thông báo thủ công trên Ops **đang ẩn** (3/4 page module Notification & Email) |
| **Tiêu chí quyết định** | Vận hành nhìn phần trăm tiến độ và thời hạn còn lại. Hai con số này **cho biết ai đang chậm, không cho biết ai đang cố gắng** — học viên đi đều mỗi ngày và học viên học dồn một buổi trông giống nhau khi đã cùng phần trăm |
| **Chỗ sai** | Việc thúc học phụ thuộc vào vận hành nhớ và làm thủ công. Không mở rộng được khi số lớp tăng, và **không tạo được thói quen** |

## Ba con số cần lấy trước khi viết PRD — `OQ-B4`

| # | Con số | Cách lấy |
|---|---|---|
| 1 | **Tỷ lệ học viên đứng yên** — đang có lớp còn hạn nhưng không phát sinh bản ghi tiến độ nào trong 14 ngày | `user_course_section_progress` + `class_user_instances` + hạn lớp. Phụ thuộc `OQ-B2` |
| 2 | **Mức độ học dồn** — phần trăm hoạt động hoàn thành trong 7 ngày cuối trước hạn lớp | `user_course_section_progress` + ngày kết thúc lớp. Phụ thuộc `OQ-B2` |
| 3 | **Tỷ lệ hoàn thành khoá** — số chứng chỉ đã cấp so với số lượt ghi danh | `courses_users_certificates` / `class_user_instances`. Lấy được ngay |

---

# 3. Objective

| # | Kết quả muốn đạt |
|---|---|
| O1 | **Học viên quay lại học đều đặn hơn** mà không cần vận hành nhắc thủ công |
| O2 | **Nỗ lực học được ghi nhận ngay lúc nó xảy ra** |
| O3 | **Học viên có mốc ngắn hạn để nhắm tới** |
| O4 | **Đội truyền thông nội bộ có kết quả chiến dịch để công bố** — việc đánh giá hiệu quả do họ tự làm bên ngoài |
| O5 | **Kết quả mỗi kỳ công bố được và không thay đổi về sau**, đủ tin cậy để làm căn cứ trao thưởng |
| O6 | **Điểm số đáng tin** — mỗi con số đều truy được nguồn, và không bị thổi lên bằng thao tác đối phó |

---

# 4. Stakeholder

| Stakeholder | Action |
| --- | --- |
| **Học viên (UpLMS)** | Nhận điểm · nhận huy hiệu · lên hạng · xem trang thành tích · tra lịch sử điểm · xem bảng xếp hạng và vị trí của mình |
| **Nhân sự vận hành (UpLMS Ops)** | Khai bảng điểm · tạo huy hiệu · đặt hạng và ngưỡng · tạo và quản lý chiến dịch · bật/tắt cơ chế |
| **Đội truyền thông nội bộ** | Thiết kế và chạy chiến dịch · lấy kết quả cuối kỳ để công bố và **trao thưởng ngoài hệ thống** |
| **L&D** | Dùng dữ liệu điểm, hạng, huy hiệu để đánh giá mức độ tham gia học tập ở quy mô tổ chức |
| **Quản lý trực tiếp** | Quản lý trực tiếp của học viên trong tổ chức — theo dõi tình hình học của nhân viên mình phụ trách |
| Dev | Xác nhận `OQ-B2` · `OQ-B9` · `OQ-B12` · `OQ-B15` |
| QA | Điền `Conner case` ở PRD |

> ⚠️ **Quản lý trực tiếp chưa có công cụ riêng trong đợt này.** Cần bộ lọc theo nhóm (`N1`), đã hoãn chờ đồng bộ sơ đồ tổ chức từ HRM. Ghi nhận, không đề nghị đổi.

---

# 5. Scope

## In scope

| # | Nội dung |
|---|---|
| S1 | **Cơ chế điểm** — khai hành động nào được bao nhiêu điểm, bật/tắt từng hành động |
| S2 | **Bốn hành động tính điểm từ việc học**: hoàn thành hoạt động · hoàn thành khoá · đạt bài kiểm tra · đạt điểm cao |
| **S3** | 🔄 **Hành động thứ năm — vào hệ thống hằng ngày.** **Mỗi ngày học viên vào hệ thống thì được điểm một lần.** Vào nhiều lần trong ngày không cộng thêm. Không dùng chuỗi ngày liên tiếp, không cần cơ chế chống spam riêng |
| S4 | **Huy hiệu** — tên, hình, mô tả, điều kiện đạt |
| **S5** | 🔄 **Bốn loại huy hiệu, mỗi loại đo bằng một chỉ số đếm:**<br>• **Tích cực** — **số ngày có vào hệ thống**<br>• **Học tập** — số lần hoàn thành hoạt động học<br>• **Test** — **số bài kiểm tra đạt** (xem `BR-TEST` dưới)<br>• **Course** — số khoá đã hoàn thành |
| S6 | **Hạng người học** — tên, hình, và **ngưỡng lên hạng dựa trên nhiều chỉ số**: điểm · số huy hiệu · số khoá hoàn thành |
| S7 | **Hai loại điểm tách nhau**: điểm tích luỹ vĩnh viễn (xét hạng) và điểm theo kỳ (xếp hạng) |
| S8 | **Chống cày điểm** — chống cộng trùng nội dung đã hoàn thành, trần điểm tối đa mỗi ngày |
| S9 | **Lịch sử điểm** — học viên tra được từng lần cộng đến từ đâu |
| S10 | **Thông báo thành tích** — **chỉ đẩy trong hệ thống khi học viên đang online.** Không gửi mail. Offline thì không gửi, thành tích vẫn ghi nhận và tra được ở lịch sử |
| S11 | **Trang "Thành tích của tôi"** — điểm, hạng, huy hiệu đã có, huy hiệu sắp đạt kèm phần còn thiếu |
| S12 | **Hai công tắc ở cấp tổ chức:** `Gamification` (bật/tắt lưu dữ liệu, bao gồm cả hiển thị) và `Visibility in UpLMS` (chỉ xuất hiện khi `Gamification` bật) |
| S13 | **Phân quyền cấu hình** |
| S14 | **Bảng xếp hạng theo kỳ lịch** — tuần · tháng · quý · năm. Hệ thống tự tính |
| S15 | **Chiến dịch** — vận hành khai khoảng thời gian bất kỳ, kèm tên và phạm vi người tham gia |
| S16 | **Chỉ số xếp hạng của chiến dịch chọn được** — điểm · số huy hiệu · số khoá hoàn thành |
| S17 | **Luật chỉnh sửa chiến dịch** — đang chạy thì không sửa được |
| S18 | **"Vị trí của tôi"** — luôn hiện thứ hạng người đang xem kèm vài người liền kề |
| S19 | **Chốt kỳ** — đóng băng bảng, lưu kết quả cuối kèm chỉ số đã dùng, mở kỳ mới về 0 |
| S20 | **Lịch sử các kỳ đã kết thúc** |
| S21 | **Tham số múi giờ ở cấp tổ chức** — biên kỳ cắt theo múi giờ tổ chức |
| S22 | **Tiêu chí phụ khi đồng hạng** — cùng chỉ số thì ai đạt sớm hơn xếp trên |
| S23 | **Danh mục chỉ số đo lường dùng chung** cho huy hiệu (S5), ngưỡng lên hạng (S6), chỉ số xếp hạng chiến dịch (S16). Xem §6.8 |

### 🆕 `BR-TEST` — quy tắc tính "bài kiểm tra đạt"

| Loại bài | Có `Pass Point`? | Tính khi nào |
|---|---|---|
| **Test** (Section / Midterm / Final) | **Luôn có** — mặc định `Auto 50%`, hoặc `Manual` do Admin nhập | **Chỉ tính khi đạt Pass Point** |
| **Quiz** (trong Activity hoặc trong Video) | Không có | **Tính khi hoàn thành** |
| **Case Study** | Không có | **Tính khi hoàn thành** |

> Nguồn: KB `03-assessment.md` §1–2. Áp cho cả hành động tính điểm *"đạt bài kiểm tra"* (S2) và huy hiệu loại **Test** (S5).
>
> ⚠️ `OQ-B16` — huy hiệu loại Test có đếm cả Quiz và Case Study không, hay chỉ đếm Test?

## Out of scope

| # | Không làm | Vì sao |
|---|---|---|
| N1 | **Bộ lọc bảng xếp hạng theo nhóm** — gồm cả theo lớp và theo phòng ban | Chờ chức năng nhóm **đồng bộ từ HRM** |
| N2 | **Chống cày riêng cho hoạt động chỉ có Text/Ảnh** | Chống cộng trùng và trần điểm/ngày vẫn áp cho mọi loại |
| N3 | **Nhiều chiến dịch chạy song song** | Đợt này mỗi lần một chiến dịch. Sau này mới tạo nhiều chiến dịch cho nhiều nhóm |
| N4 | **Điều kiện huy hiệu theo chuỗi ngày liên tiếp · mốc thời gian · nội dung cụ thể** | Thay bằng bốn loại đo bằng chỉ số đếm (S5) |
| N5 | **Thông báo thành tích qua email** | Chỉ đẩy trong hệ thống. Không đụng tới 30 mail hiện có |
| N6 | **Giới hạn nội dung được tính trong chiến dịch** | PO không yêu cầu |
| N7 | **Tính năng Lộ trình học** và hành động "hoàn thành lộ trình" | Tính năng riêng, làm sau |
| N8 | **Tính năng Khung năng lực / Skills** và huy hiệu theo kỹ năng | Tính năng riêng, làm sau |
| N9 | **Sửa logic hoàn thành Activity** | PO chốt giữ nguyên |
| N10 | **Quản lý phần thưởng trong hệ thống** | Trao thưởng là hành động ngoài hệ thống |
| N11 | **Trang đo hiệu quả chiến dịch** | Hệ thống chỉ cung cấp **kết quả**; đội truyền thông tự đo hiệu quả bên ngoài |
| N12 | **Gamification cho nhân sự Ops** | Chỉ áp dụng cho học viên |
| N13 | **Thi đua theo đội / nhóm** | Chỉ xếp hạng cá nhân |
| N14 | **Cấu hình gamification riêng theo lớp hoặc khoá** | Cấu hình ở cấp tổ chức |
| N15 | **Màn quản lý nhiều tổ chức** | Chưa có multi-tenant. Dữ liệu vẫn thiết kế theo tổ chức — `C1` |
| N16 | **Module Tenant (`TNT.CFG.02`) đầy đủ** | Đợt này chỉ khai tham số múi giờ (S21) |

## Potential scope

Bộ lọc theo nhóm sau khi đồng bộ HRM · nhiều chiến dịch song song · giới hạn nội dung chiến dịch · điểm cho lộ trình · huy hiệu theo kỹ năng · đổi điểm lấy phần thưởng

---

# 6. Solution (khung)

## 6.1 Hướng tổng thể

```
Lớp 1  Bắt sự kiện học tập      ← nghe các việc học viên đã làm, gồm cả việc vào hệ thống
Lớp 2  Quy đổi ra điểm          ← áp bảng cấu hình + luật chống cày
Lớp 3  Tích luỹ và xét ngưỡng   ← cộng dồn, đếm chỉ số, xét huy hiệu, xét hạng
Lớp 4  Xếp hạng theo kỳ         ← tính thứ hạng từ sổ giao dịch theo khoảng ngày
Lớp 5  Phản hồi cho học viên    ← đẩy khi online + trang thành tích + bảng xếp hạng
```

Nguyên tắc xuyên suốt: **gamification chỉ đọc, không sửa dữ liệu học tập.**

## 6.2 Hai loại kỳ

| | **Kỳ lịch** | **Chiến dịch** |
|---|---|---|
| Ai tạo | **Hệ thống tự tính** | **Vận hành khai tay** |
| Biên | Cố định theo lịch — tuần, tháng, quý, năm | Hai ngày bất kỳ, không cần trùng biên lịch |
| Chồng lấn | **Có** — tuần ⊂ tháng ⊂ quý ⊂ năm | **Không** — đợt này mỗi lần một chiến dịch |
| Cấu hình | Không cần màn nào | Tên · phạm vi người tham gia · chỉ số xếp hạng |
| Chỉnh sửa | — | Đang chạy thì không sửa được |
| Chỉ số xếp | **Luôn theo điểm** | **Chọn được** |

## 6.3 Ràng buộc thiết kế bắt buộc

| # | Ràng buộc | Vì sao |
|---|---|---|
| **C1** | Cấu hình gắn với **tổ chức**, không đóng cứng | Định hướng đa tenant |
| **C2** | **Mọi danh mục phải mở rộng được bằng cấu hình** | Lộ trình, kỹ năng, bộ lọc nhóm, nhiều chiến dịch song song đều sẽ thêm sau |
| **C3** | Lưu **từng lần cộng điểm kèm thời điểm** | Nền của lịch sử điểm, xếp hạng theo kỳ, tiêu chí phụ khi đồng hạng, luật chống cày |
| **C4** | Đổi cấu hình điểm → **áp dụng từ thời điểm đổi** | PO chốt |
| **C5** | Chống cộng trùng "đã học" tính theo **người học**, không theo lượt ghi danh lớp | Học viên có thể học cùng nội dung qua nhiều lớp |
| **C6** | **Biên kỳ cắt theo múi giờ của tổ chức**, không theo giờ máy chủ | Module Tenant chưa có → đợt này khai một tham số múi giờ cấp tổ chức |
| **C7** | **Một lần cộng điểm thuộc về nhiều kỳ lịch cùng lúc** → điểm theo kỳ tính từ sổ giao dịch theo khoảng ngày. **Kết quả cuối kỳ lưu cứng** | Kỳ lịch lồng nhau theo bản chất |
| **C8** | **Mọi mốc dùng để xếp hạng phải lưu được thời điểm đạt** | Cần cho S22 và cho mọi chỉ số đếm |
| **C9** 🆕 | **"Ngày" trong `S3` và trong trần điểm/ngày (`S8`) cắt theo múi giờ tổ chức**, cùng quy tắc với biên kỳ (`C6`) | Nếu không, học viên ở múi giờ khác sẽ được hoặc mất một ngày |

## 6.4 ✅ Ngữ nghĩa của việc tắt gamification *(đã chốt)*

| Trạng thái | `Gamification` | `Visibility in UpLMS` | Dùng khi nào |
|---|---|---|---|
| Tắt hẳn | Tắt | *(không hiện)* | Tổ chức không dùng cơ chế này |
| **Chạy ngầm** | Bật | Tắt | **Chạy thử trước khi mở cho học viên** |
| Bật đầy đủ | Bật | Bật | Vận hành bình thường |

**Luật kèm theo:**

1. Chuyển từ *Chạy ngầm* sang *Bật đầy đủ*: **không bắn thông báo hồi tố.** Dữ liệu đã ghi hiện đầy đủ ngay.
2. Bật lại sau khi *Tắt hẳn*: **tính từ thời điểm bật.** Giai đoạn tắt không ghi gì nên không có gì để bù.
3. Tắt `Visibility in UpLMS` → **không đẩy thông báo thành tích** (`A19`).

## 6.5 ✅ Chống cày điểm *(đã chốt)*

Không làm cơ chế riêng cho hoạt động chỉ có Text/Ảnh. Hai cơ chế chung áp cho mọi loại: **chống cộng trùng nội dung đã hoàn thành** (`C5`) và **trần điểm tối đa mỗi ngày** (`S8`).

## 6.6 ✅ Chỉ số xếp hạng chiến dịch và tiêu chí phụ *(đã chốt)*

Chiến dịch chọn xếp theo: điểm · số huy hiệu · số khoá hoàn thành. Ba chỉ số khác nhau về độ phân tán — "số khoá hoàn thành" chỉ ở khoảng 0–5 nên gây đồng hạng hàng loạt. Vì vậy **`S22` là bắt buộc**: cùng chỉ số thì ai đạt mức đó sớm hơn xếp trên.

## 6.7 ✅ Cơ chế điểm khi vào hệ thống *(đã chốt — đơn giản hoá lần hai)*

**Mỗi ngày học viên vào hệ thống thì được điểm một lần.** Vào nhiều lần trong ngày không cộng thêm.

| | v0.3 | v0.4 | **v0.5 (chốt)** |
|---|---|---|---|
| Cơ chế | Chuỗi ngày liên tiếp | Mỗi lần login + khoảng cách tối thiểu | **Mỗi ngày một lần** |
| Chống lạm dụng | Bản chất chuỗi | Khoảng cách thời gian | **Bản chất "một lần một ngày"** |
| Dữ liệu cần | Lịch sử đăng nhập, tính chuỗi | Thời điểm lần tính điểm gần nhất | **Ngày gần nhất đã tính điểm** |

### 🟢 Hệ quả quan trọng: phụ thuộc Keycloak giảm mạnh

*"Vào hệ thống hôm nay"* rộng hơn *"phát sinh sự kiện đăng nhập của Keycloak"*. Học viên đăng nhập SSO qua Lark có thể mở ứng dụng nhiều ngày liền mà **không sinh sự kiện đăng nhập mới** vì phiên còn sống.

→ Nên **không nên lấy sự kiện Keycloak làm nguồn.** Nguồn đúng là **sự hiện diện của học viên trong hệ thống trong ngày đó**, gamification tự ghi nhận khi thấy học viên hoạt động.

| | v0.4 | **v0.5** |
|---|---|---|
| Mức tác động User / Auth | 🔴 Cao | 🟡 **Thấp** |
| `OQ-B1` (Keycloak ghi sự kiện đăng nhập) | Chặn Gate 2 | ✅ **Đóng** — không còn cần |
| Câu hỏi thay thế | — | `OQ-B15` — ghi nhận "có mặt trong ngày" bằng cách nào |

Chỉ số **số ngày có vào hệ thống** cũng chính là chỉ số đo huy hiệu loại **Tích cực** (S5).

## 6.8 Một danh mục chỉ số dùng chung cho ba chỗ

| Nơi dùng | Chỉ số |
|---|---|
| **Điều kiện huy hiệu** (S5) | Số ngày có vào hệ thống · số hoạt động hoàn thành · số bài kiểm tra đạt · số khoá hoàn thành |
| **Ngưỡng lên hạng** (S6) | Điểm · số huy hiệu · số khoá hoàn thành |
| **Chỉ số xếp hạng chiến dịch** (S16) | Điểm · số huy hiệu · số khoá hoàn thành |

`Recommendation` — **định nghĩa một danh mục chỉ số duy nhất và dùng lại ở cả ba chỗ** (`S23`).

Lý do quan trọng nhất không phải gọn: *"số khoá hoàn thành"* phải được tính **giống hệt nhau** ở cả ba chỗ. Tách riêng là mở đường cho ba định nghĩa lệch nhau — loại lỗi rất khó phát hiện và phá thẳng `O6`. Thêm nữa, cả ba sẽ cùng phải mở rộng khi thêm lộ trình và kỹ năng.

Tập chỉ số tối thiểu: **điểm tích luỹ · số ngày có vào hệ thống · số hoạt động hoàn thành · số bài kiểm tra đạt · số khoá hoàn thành · số huy hiệu**.

---

# 7. Danh sách User Story dự kiến

## Phía học viên (UpLMS)

| ID | User Story | Nguồn | Ghi chú |
| --- | --- | --- | --- |
| **US1** | Là học viên, tôi cần xem điểm, hạng và huy hiệu đã đạt để biết nỗ lực học của mình được ghi nhận tới đâu | Dòng 10 · O2 | Trang "Thành tích của tôi" |
| **US2** | Là học viên, tôi cần được báo ngay khi nhận điểm, đạt huy hiệu hoặc lên hạng **trong lúc đang dùng hệ thống** | Dòng 9 · O2 · S10 | Không gửi khi offline — vẫn tra được ở lịch sử |
| **US3** | Là học viên, tôi cần tra được từng lần cộng điểm đến từ đâu để tin vào con số của mình | Dòng 8 · O6 · C3 | |
| **US4** | Là học viên, tôi cần biết huy hiệu nào sắp đạt và còn thiếu gì để có mục tiêu ngắn hạn | Dòng 10 · O3 | Tính tiến độ tới **mọi** huy hiệu chưa đạt |
| **US5** | Là học viên, tôi cần việc vào hệ thống mỗi ngày được ghi nhận thành điểm để có lý do mở ứng dụng hằng ngày | Dòng 2 · S3 · O1 | 🔄 Mỗi ngày một lần. `OQ-B15` |
| **US6** | Là học viên, tôi cần xem bảng xếp hạng của kỳ tôi chọn để biết mình đứng ở đâu so với người khác | CR-001 · S14 | Toàn tổ chức |
| **US7** | Là học viên, tôi cần luôn thấy vị trí của chính mình kèm vài người liền kề để biết mình cần hơn ai một chút là lên hạng | CR-001 · S18 | Cơ chế giảm nhẹ chính cho bảng toàn tổ chức |
| **US8** | Là học viên, tôi cần xem lại bảng xếp hạng của các kỳ đã kết thúc để nhìn lại thành tích đã đạt | CR-001 · S20 | |

## Phía vận hành (UpLMS Ops)

| ID | User Story | Nguồn | Ghi chú |
| --- | --- | --- | --- |
| **US9** | Là nhân sự vận hành, tôi cần khai hành động nào được bao nhiêu điểm và bật/tắt từng hành động để điều chỉnh cơ chế theo mục tiêu từng giai đoạn | Dòng 1, 2 | |
| **US10** | Là nhân sự vận hành, tôi cần tạo và quản lý huy hiệu theo bốn loại với ngưỡng số lượng để thiết kế các mốc mục tiêu cho học viên | Dòng 3, 4 · S5 | Chịu `BR-TEST` |
| **US11** | Là nhân sự vận hành, tôi cần đặt các hạng và ngưỡng lên hạng theo nhiều chỉ số để phân tầng mức độ tham gia của học viên | Dòng 5 · S6 | |
| **US12** | Là nhân sự vận hành, tôi cần tạo chiến dịch có thời hạn riêng, chọn phạm vi người tham gia và chọn chỉ số xếp hạng | CR-001 · CR-002 · S15, S16 | Đợt này mỗi lần một chiến dịch |
| **US13** | Là nhân sự vận hành, tôi cần chiến dịch đang chạy không sửa được để kết quả thi đua không bị thay đổi luật giữa chừng | CR-002 · S17 | |
| **US14** | Là nhân sự vận hành, tôi cần bảng xếp hạng được đóng băng và lưu lại khi hết kỳ để công bố kết quả không thay đổi và trao thưởng | CR-001 · S19 · O5 | Lưu kèm chỉ số đã dùng |
| **US15** | Là nhân sự vận hành, tôi cần điểm phản ánh việc học thật, không bị đẩy lên bằng thao tác đối phó | Dòng 7 · O6 | Chịu `C5` |
| **US16** | Là nhân sự vận hành, tôi cần bật/tắt gamification và bật/tắt hiển thị phía học viên riêng biệt, để chạy thử cơ chế trước khi mở | Dòng 11 · S12 | |
| **US17** | Là quản trị, tôi cần phân quyền để chỉ vai trò vận hành phù hợp mới sửa được cấu hình gamification | `[suy ra]` · S13 | |

## Chưa làm trong đợt này

| ID | User Story | Nguồn |
| --- | --- | --- |
| **US18** | *Bộ lọc bảng xếp hạng theo nhóm* — **chưa làm.** Là công cụ duy nhất phục vụ stakeholder Quản lý trực tiếp | N1 |
| **US19** | *Nhiều chiến dịch song song cho nhiều nhóm* — **chưa làm** | N3 |
| **US20** | *Giới hạn nội dung chiến dịch* — **chưa làm** | N6 |
| **US21** | *Điểm cho lộ trình* — **chưa làm** | N7 |
| **US22** | *Huy hiệu theo kỹ năng* — **chưa làm** | N8 |

---

# 8. Tác động tới hệ thống hiện tại

> **Chưa chạy Impact Analysis.** Đánh giá sơ bộ. **Chi tiết ở Gate 2.**

| Vùng ảnh hưởng | Mức | Ghi chú |
| --- | --- | --- |
| **Dữ liệu** | 🔴 Cao | Toàn bộ cấu trúc điểm, huy hiệu, hạng, kỳ, chiến dịch, sổ giao dịch, snapshot là mới. Chịu C1–C9 |
| **Hiệu năng** | 🔴 Cao | Xếp hạng tính từ sổ giao dịch theo khoảng ngày, toàn tổ chức, nhiều kỳ lồng nhau, ba chỉ số — `OQ-B9` |
| **Tổ chức / Tenant** | 🟠 Vừa | Tham số múi giờ cấp tổ chức (S21, C6, C9) |
| **Learning Experience** | 🟠 Vừa | Nguồn sự kiện chính. Chỉ đọc, không sửa |
| **Assessment / Grading** | 🟠 Vừa | Nguồn sự kiện. `BR-TEST` phụ thuộc `Pass Point` và cách phân biệt Test / Quiz / Case Study |
| **Course / Certificate** | 🟠 Vừa | "Số khoá hoàn thành" dùng ở ba chỗ |
| **User / Auth** | 🟡 **Thấp** | 🔄 **Giảm mạnh từ 🔴.** `S3` chuyển sang "có mặt trong ngày", không còn phụ thuộc sự kiện đăng nhập Keycloak |
| **Notification** | 🟢 Rất thấp | Chỉ đẩy trong hệ thống khi online. Không dùng cơ chế thông báo hiện có, không gửi mail |
| **Class** | 🟡 Thấp | Là lý do sinh ra `C5` |
| **Phân quyền** | 🟡 Thấp | Thêm nhóm quyền mới |

---

# 9. Assumptions

| # | Giả định | Trạng thái |
|---|---|---|
| A1 | Gamification chỉ áp dụng cho **học viên UpLMS** | ✅ PO xác nhận |
| A2 | Cấu hình đặt ở **UpLMS Ops** | ✅ PO xác nhận |
| A3 | **Hạng chỉ lên, không tụt** | ✅ PO xác nhận |
| A4 | Điểm tích luỹ **không hết hạn** | ✅ PO xác nhận |
| A5 | Huy hiệu **đạt rồi giữ vĩnh viễn**, không thu hồi | ✅ PO xác nhận |
| A6 | Một hành động đồng thời cộng vào **cả điểm tích luỹ và điểm theo kỳ** | ✅ PO xác nhận |
| A7 | Điểm là **số nguyên** | ✅ PO xác nhận |
| A9 | Ảnh huy hiệu và ảnh hạng dùng hạ tầng quản lý tài nguyên sẵn có | Gate 2 |
| A10 | **Dữ liệu tiến độ học có dấu thời gian** | Dev — `OQ-B2` |
| A12 | Vận hành **không cần sửa hay xoá điểm thủ công** của một học viên | ✅ PO xác nhận |
| A13 | **Bảng xếp hạng chỉ hiện học viên, không hiện nhân sự Ops** | ✅ PO xác nhận |
| A14 | **Học viên bị Block hoặc đã rời tổ chức không xuất hiện trong bảng đang chạy**, nhưng **giữ nguyên trong snapshot kỳ đã chốt** | ✅ PO xác nhận |
| **A15** | **Bảng xếp hạng công khai danh tính học viên** với nhau | ✅ **PO chốt 23/09: công khai bình thường, không sao** |
| A16 | **Kỳ lịch bắt đầu từ thời điểm bật tính năng**, không dựng lại bảng cho kỳ trước ngày go-live | ✅ PO xác nhận |
| A17 | **Kỳ lịch luôn xếp theo điểm.** Chọn chỉ số chỉ áp cho chiến dịch | ✅ PO xác nhận |
| A18 | **Chiến dịch chưa tới ngày bắt đầu thì sửa được**, chỉ khoá khi đã chạy | ✅ PO xác nhận |
| A19 | **Tắt `Visibility in UpLMS` thì không đẩy thông báo thành tích** | ✅ PO xác nhận |
| **A20** | **Phạm vi người tham gia chiến dịch ở đợt này là toàn bộ học viên** | ✅ **PO chốt 23/09** |
| ~~A21~~ | ~~"Đăng nhập" có tính lần khôi phục phiên không~~ | 🔄 **Không còn cần** — `S3` đổi sang "mỗi ngày vào hệ thống" |
| **A22** | **Huy hiệu loại Test chỉ đếm bài đạt**; bài không có setting pass thì tính khi hoàn thành | ✅ **PO chốt 23/09** → `BR-TEST` |

---

# 10. Open Questions

| # | Câu hỏi | Vì sao quan trọng | Người trả lời | Chặn bước sau? |
| --- | --- | --- | --- | --- |
| **OQ-B2** | **Dữ liệu tiến độ học có dấu thời gian không?** | Cần cho C5, C7, trần điểm/ngày, và hai con số ở §2 | Dev | **Yes** — trước Gate 2 |
| **OQ-B9** | **Bảng xếp hạng chịu tải được không?** Tính thứ hạng từ sổ giao dịch theo khoảng ngày, toàn tổ chức, nhiều kỳ lồng nhau, ba chỉ số | Quyết định giữa tính trực tiếp và tính sẵn theo chu kỳ | Dev | **Yes** — trước Gate 2 |
| **OQ-B12** | **Thời điểm đạt huy hiệu, hoàn thành khoá, đạt bài kiểm tra có lưu được không?** | `C8` — cần cho tiêu chí phụ khi đồng hạng và mọi chỉ số đếm | Dev | **Yes** — trước Gate 2 |
| **OQ-B15** 🆕 | **Ghi nhận "học viên có vào hệ thống hôm nay" bằng cách nào?** Sự kiện đăng nhập Keycloak **không đủ** vì SSO Lark giữ phiên sống nhiều ngày | Là nguồn dữ liệu cho `S3` và huy hiệu loại Tích cực | Dev | **Yes** — trước Gate 2 |
| **OQ-B16** 🆕 | **Huy hiệu loại Test đếm những gì?** Chỉ Test (Section/Midterm/Final), hay cả Quiz trong Activity và Case Study? | Ba loại có bản chất khác nhau: chỉ Test có `Pass Point`; Quiz không tính vào hoàn thành khoá; Case Study chỉ làm 1 lượt | PO | No — Field Intake |
| **OQ-B11** | **Múi giờ tổ chức khai ở đâu trong đợt này?** | `C6`, `C9` | PO + Dev | No — Gate 2 |

## ✅ Đã đóng

| # | Kết luận |
|---|---|
| `OQ-B1` | 🔄 **Không còn cần.** `S3` đổi sang "mỗi ngày vào hệ thống" nên không phụ thuộc sự kiện đăng nhập Keycloak. Thay bằng `OQ-B15` |
| `OQ-B3` | Đội truyền thông **tự đo hiệu quả bên ngoài** → `N11` |
| `OQ-B4` | Ba con số đã nêu cụ thể ở §2 kèm cách lấy |
| `OQ-B5` `OQ-B6` | **Chỉ đẩy trong hệ thống khi online. Không gửi mail** → `S10`, `N5` |
| `OQ-B7` | **Không bật lại 8 mail luồng chấm điểm** |
| `OQ-B8` | **Giữ `Point` = điểm, `Level` = hạng học viên.** Nhãn giao diện phải phân biệt với `Pass Point`, `Course Level`, `Staff Level` |
| `OQ-B10` | Đồng hạng xử lý theo **thời điểm đạt** |
| `OQ-B13` | **Chiến dịch không chồng lấn ở đợt này** → `N3` |
| `OQ-B14` | 🔄 **Không còn cần** — cùng lý do với `OQ-B1` |

---

# 11. References

| File KB | Dùng cho |
|---|---|
| `03-assessment.md` | **`BR-TEST`** — `Pass Point`, phân biệt Test / Quiz / Case Study |
| `07-learning-experience.md` | `KB-LX-03a`, `KB-LX-03b` — nền của §6.5. Đã cập nhật trong đợt này |
| `09-notification-email.md` | Nay chỉ để đối chiếu, không còn là phụ thuộc |
| `13-mail-events.md` | Xác nhận gamification **không đụng tới** 30 mail |
| `12-data-model.md` | Nền của `C5`, `C6`; phòng ban chỉ gắn nhân sự |
| `14-api-surface.md` | `Group Management`, `Department Management` |
| `15-product-direction.md` | Định hướng đa tenant — nền của `C1` |
| `01-course.md` · `04-class.md` · `06-user-account.md` · `08-certificate.md` | Nguồn sự kiện và các chỉ số đếm |

| Nguồn khác | |
|---|---|
| Yêu cầu gốc | `working/raw-inputs/yeu-cau-goc-20260923.md` |
| Change requests | `working/raw-inputs/change-requests.md` — CR-001…005 |
| Quyết định đã chốt | `project-decisions.md` |
| BRD bản trước | `docs/brd/brd-v0.1` … `v0.4` (23/09/2026) |
| Schema DB | [Lark → Data Architecture](https://upbasevn.sg.larksuite.com/wiki/MaFpweI68iKNMvkTioLlJ1uJgQd) |
| Swagger | `lms-be.staging.upbase.asia/api/v1/docs` · `ops-be.staging.upbase.asia/api/v1/docs` |
| Tham chiếu ngoài | `TNT.CFG.02` — Hồ sơ tổ chức và tham số, module Tenant *(chưa làm)* |
