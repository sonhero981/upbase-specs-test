# [BRD] Gamification — Điểm, huy hiệu, hạng và bảng xếp hạng

> # ⚠️ Hai lớp thay đổi sau khi tài liệu này được duyệt lần đầu
>
> **`CR-007` — 23/09/2026.** Bỏ chiến dịch, kỳ lịch và cơ chế chốt kỳ, thay bằng **bộ chọn khoảng ngày tự do**. Khoá mốc huy hiệu sau khi tạo, nên huy hiệu đã nhận không bao giờ bị lấy lại.
>
> **`CR-013` — 08/10/2026.** Phía học viên **bỏ bộ chọn khoảng ngày tự do**, chỉ còn khung cố định. **Campaign quay lại ở dạng mới**, viết ở §6.9. Bản v0.7 chỉ cập nhật những phần campaign chạm tới.
>
> **Những mục sau KHÔNG còn hiệu lực:**
> - **Mô hình chiến dịch cũ**: vận hành chọn chỉ số xếp hạng, mỗi lần một chiến dịch, chọn phạm vi người tham gia. Thay bằng §6.9
> - **Kỳ lịch như một thực thể riêng**, chốt kỳ lịch, snapshot kỳ lịch. Khung cố định là số liệu sống. **Chỉ campaign mới đóng băng**
> - Quyết định **gỡ huy hiệu khi nâng ngưỡng** — không còn, vì mốc nay khoá
>
> Các thay đổi từ `CR-008` đến `CR-012` chỉ nằm ở PRD. Trạng thái đúng nằm ở `working/raw-inputs/change-requests.md` và ở PRD.

---


| | |
| --- | --- |
| **Tính năng** | Gamification |
| **Người viết** | Bùi Đức Huy (PO) |
| **Ngày** | 23/09/2026 · cập nhật 08/10/2026 |
| **Trạng thái** | 🔄 **v0.7 chờ PO duyệt lại** — mang `CR-013`. Bản v0.6 được PO duyệt `Approved with Notes` ngày 23/09/2026 |
| **Cỡ yêu cầu** | **L** — đủ 9 bước, đủ 4 Gate |

## Document version

| Version | Nội dung | Impact | Ngày |
| --- | --- | --- | --- |
| v0.1 | Bản đầu | — | 23/09 |
| v0.2 | Đưa bảng xếp hạng vào phạm vi · tách kỳ lịch khỏi chiến dịch | `CR-001` | 23/09 |
| v0.3 | Chốt 4 quyết định Gate 1 · bỏ phạm vi xếp hạng theo lớp · thêm chỉ số xếp hạng chiến dịch | `CR-002` · `CR-003` | 23/09 |
| v0.4 | Gate 1 `Need Revision` · định nghĩa lại huy hiệu · thu hẹp thông báo | `CR-004` | 23/09 |
| v0.5 | Gate 1 `Approved with Notes` · điểm khi vào hệ thống tính theo ngày · gỡ phụ thuộc Keycloak | `CR-005` | 23/09 |
| **v0.6** | 🔧 **Đính chính `BR-TEST`.** `Pass Point` chỉ tồn tại khi `Graded Assignment = Yes`. **Quiz và Case Study không tính.** Đóng `OQ-B16`.<br>🗑️ **Bỏ hành động tính điểm "đạt điểm cao"** — PO chốt tạm thời không có rule này. Gỡ `A23` và `OQ-B17` | `CR-006` | 23/09 |
| **v0.6.1** | 🔁 **Feed ngược từ Impact Analysis (Gate 2).** Sửa `C5` — chống cộng trùng trong phạm vi một lượt ghi danh, không cắt ngang lớp. Thêm `C10` loại trừ `Test Account`. Thêm `BR-REGRADE-02`. Chốt `A24`, `A25`. Bỏ khoá Trial khỏi phạm vi | `impact-matrix-v0.1` | 23/09 |
| **v0.7** | **Campaign quay lại ở dạng mới** (§6.9): vận hành chọn khoảng thời gian và loại hành động tính điểm, số điểm theo cấu hình chung, hai bảng điểm và số hoạt động, đóng băng khi kết thúc, được chồng thời gian. Học viên chỉ chọn khung cố định. Cập nhật `O4`, Scope, Out of scope, danh sách US | `CR-013` | 08/10 |

**Nguồn input:** `working/raw-inputs/yeu-cau-goc-20260923.md` · `change-requests.md` (CR-001…006, CR-013) · `clarified-requirements-20260923.md` · `project-decisions.md`

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

## 2.1 Số liệu thật — General Launch, 8/9–21/9/2026

PO cung cấp 23/09/2026. Đo trên nhóm nhân viên được gán khoá học.

| Chỉ số | Tiêu chí đặt ra | Thực tế | |
|---|---|---|---|
| **Activation** | 80% nhân viên được gán khoá **đăng nhập lần đầu** trong 7 ngày kể từ General Launch | **40.2%** (53/132) | ❌ **hụt một nửa** |
| **Course start** | 80% người được gán đã **bắt đầu** khoá học trong 7 ngày | **22%** (29/132) | ❌ **hụt gần 4 lần** |
| **Completion** | 80% **hoàn thành** khoá bắt buộc đầu tiên trong 14 ngày | **64.1%** (93/145) | ❌ |

> ⚠️ Mẫu số khác nhau: Activation và Course start tính trên **132**, Completion tính trên **145** — hai nhóm người khác nhau, không gộp chung. `OQ-B4a`

## 2.2 🔑 Con số quan trọng nhất không nằm trong bảng

**53 người đăng nhập, chỉ 29 người bắt đầu học.**

Nghĩa là **24 người đã vào hệ thống rồi không bắt đầu gì cả** — **45% số người đã chịu mở ứng dụng**.

Đây là *"không chủ động vào học"* ở dạng số, và nó tách `Problem` thành **ba tầng riêng biệt**:

| Tầng | Số đo | Nghĩa là gì |
|---|---|---|
| **1. Không mở ứng dụng** | Activation **40.2%** | 6/10 người được gán khoá **không vào lấy một lần** trong tuần đầu |
| **2. Mở rồi không học** | **45%** người đăng nhập không bắt đầu | Không phải vấn đề tiếp cận — vào tới nơi rồi vẫn không bắt đầu |
| **3. Bắt đầu rồi bỏ dở** | Completion **64.1%** | Đã bắt đầu nhưng không tới đích trong thời hạn |

## 2.3 Dùng lại bộ chỉ số này để đo sau khi ra mắt

Ba chỉ số trên **đã có tiêu chí và có mốc nền** — dùng thẳng, không cần nghĩ chỉ số mới:

| Chỉ số | Mốc nền | Gamification nhắm bằng |
|---|---|---|
| Activation | 40.2% | Điểm **check-in hằng ngày** (`S3`) |
| Course start | 22% | Điểm theo **hoạt động hoàn thành** · huy hiệu · hạng |
| Completion | 64.1% | **Chiến dịch** · bảng xếp hạng |

`Recommendation` — đưa bộ này vào `Metrics success` của PRD. Trước đây để ngỏ vì chưa có chỉ số; nay đủ cả ba yếu tố: chỉ số · tiêu chí · mốc nền.

## 2.4 Vận hành đang xoay xở thế nào

| Hướng | Hiện trạng |
|---|---|
| **Cách làm hiện tại** | Vận hành theo dõi tiến độ qua dashboard SIS (*Tiến độ học trên UpLMS*), thấy ai chậm thì thúc. 30 mail tự động đều là **mail sự kiện** — không có mail nào nhằm tạo động lực |
| **Công cụ sẵn có bị hạn chế** | Giao diện soạn và gửi thông báo thủ công trên Ops **đang ẩn** (3/4 page module Notification & Email) |
| **Tiêu chí quyết định** | Vận hành nhìn phần trăm tiến độ và thời hạn còn lại. Hai con số này **cho biết ai đang chậm, không cho biết ai đang cố gắng** — học viên đi đều mỗi ngày và học viên học dồn một buổi trông giống nhau khi đã cùng phần trăm |
| **Chỗ sai** | Việc thúc học phụ thuộc vào vận hành nhớ và làm thủ công. Không mở rộng được khi số lớp tăng, và **không tạo được thói quen**. Số liệu §2.1 cho thấy cách làm này **không đạt mục tiêu ở cả ba chỉ số** |

> ✅ **`OQ-B4` đã đóng** — PO cung cấp số liệu General Launch ngày 23/09/2026. Ba con số tôi đề xuất lấy trước đó (tỷ lệ đứng yên · mức độ học dồn · tỷ lệ hoàn thành khoá) **không còn cần** — bộ chỉ số Activation / Course start / Completion mạnh hơn vì đã có tiêu chí và mốc nền sẵn.

---

# 3. Objective

| # | Kết quả muốn đạt |
|---|---|
| O1 | **Học viên quay lại học đều đặn hơn** mà không cần vận hành nhắc thủ công |
| O2 | **Nỗ lực học được ghi nhận ngay lúc nó xảy ra** |
| O3 | **Học viên có mốc ngắn hạn để nhắm tới** |
| O4 | **Đội truyền thông nội bộ có kết quả để công bố**: chạy campaign trong khoảng thời gian có chủ đích, và lấy số liệu khoảng ngày bất kỳ từ Ops. Việc đánh giá hiệu quả do họ tự làm bên ngoài |
| ~~O5~~ | ~~Kết quả mỗi kỳ công bố được và không thay đổi về sau~~ — bỏ ở `CR-007`. `CR-013` **khôi phục riêng cho campaign**: kết quả đóng băng khi campaign kết thúc. Khung cố định vẫn là số liệu sống |
| O6 | **Điểm số đáng tin** — mỗi con số đều truy được nguồn, và không bị thổi lên bằng thao tác đối phó |

> PRD đánh số lại mục tiêu sau khi bỏ `O5`: `O6` ở đây là `O5` trong PRD.

---

# 4. Stakeholder

| Stakeholder | Action |
| --- | --- |
| **Học viên (UpLMS)** | Nhận điểm · nhận huy hiệu · lên hạng · xem trang thành tích · tra lịch sử điểm · xem bảng xếp hạng và vị trí của mình |
| **Nhân sự vận hành (UpLMS Ops)** | Khai bảng điểm · tạo huy hiệu · đặt hạng và ngưỡng · tạo và quản lý chiến dịch · bật/tắt cơ chế |
| **Đội truyền thông nội bộ** | Thiết kế và chạy campaign · lấy kết quả campaign khi kết thúc để công bố và **trao thưởng ngoài hệ thống** |
| **L&D** | Dùng dữ liệu điểm, hạng, huy hiệu để đánh giá mức độ tham gia học tập ở quy mô tổ chức |
| **Quản lý trực tiếp** | Quản lý trực tiếp của học viên trong tổ chức — theo dõi tình hình học của nhân viên mình phụ trách |
| Dev | Xác nhận `OQ-B2` · `OQ-B9` · `OQ-B12` · `OQ-B15` |
| QA | Điền `Conner case` ở PRD |

> ⚠️ **Quản lý trực tiếp chưa có công cụ riêng trong đợt này.** Cần bộ lọc theo nhóm (`N1`), đã hoãn chờ đồng bộ sơ đồ tổ chức từ HRM.

---

# 5. Scope

## In scope

| # | Nội dung |
|---|---|
| S1 | **Cơ chế điểm** — khai hành động nào được bao nhiêu điểm, bật/tắt từng hành động |
| **S2** | 🔧 **Ba hành động tính điểm từ việc học**: hoàn thành hoạt động · hoàn thành khoá · **hoàn thành bài Test** (theo `BR-TEST`).<br>🗑️ *"Đạt điểm cao" đã bỏ — PO chốt tạm thời không có rule này* |
| S3 | **Hành động thứ năm — vào hệ thống hằng ngày.** Mỗi ngày học viên vào hệ thống được điểm một lần. Vào nhiều lần trong ngày không cộng thêm |
| S4 | **Huy hiệu** — tên, hình, mô tả, điều kiện đạt |
| **S5** | 🔧 **Bốn loại huy hiệu, mỗi loại đo bằng một chỉ số đếm:**<br>• **Tích cực** — số ngày có vào hệ thống<br>• **Học tập** — số lần hoàn thành hoạt động học<br>• **Test** — **số bài Test tính theo `BR-TEST`** *(không đếm Quiz, không đếm Case Study)*<br>• **Course** — số khoá đã hoàn thành |
| S6 | **Hạng người học** — tên, hình, và **ngưỡng lên hạng dựa trên nhiều chỉ số**: điểm · số huy hiệu · số khoá hoàn thành |
| S7 | **Hai loại điểm tách nhau**: điểm tích luỹ vĩnh viễn (xét hạng) và điểm theo kỳ (xếp hạng) |
| S8 | **Chống cày điểm** — chống cộng trùng nội dung đã hoàn thành, trần điểm tối đa mỗi ngày |
| S9 | **Lịch sử điểm** — học viên tra được từng lần cộng đến từ đâu |
| S10 | **Thông báo thành tích** — chỉ đẩy trong hệ thống khi học viên đang online. Không gửi mail. Offline thì không gửi, thành tích vẫn ghi nhận và tra được ở lịch sử |
| S11 | **Trang "Thành tích của tôi"** — điểm, hạng, huy hiệu đã có, huy hiệu sắp đạt kèm phần còn thiếu |
| S12 | **Hai công tắc ở cấp tổ chức:** `Gamification` (bật/tắt lưu dữ liệu, bao gồm cả hiển thị) và `Visibility in UpLMS` (chỉ xuất hiện khi `Gamification` bật) |
| S13 | **Phân quyền cấu hình** |
| S14 | 🔧 **Bảng xếp hạng theo khung cố định** — `All time` · tuần · tháng · quý · năm theo lịch. Hệ thống tự tính sẵn. **Học viên không chọn được khoảng ngày tự do**, để không ai gọi được phép tính nặng tuỳ ý (`CR-013`) |
| S15 | 🔧 **Campaign** — vận hành khai tên, mô tả và khoảng thời gian bất kỳ. Người tham gia là **toàn tổ chức**. Nhiều campaign được chạy chồng thời gian |
| S16 | 🔧 **Hai cấu phần của campaign, mỗi cấu phần một bảng:**<br>• **Điểm** — vận hành **chỉ chọn loại hành động nào được tính**. **Số điểm theo cấu hình chung**, campaign không sửa<br>• **Số hoạt động hoàn thành** |
| S17 | 🔧 **Luật chỉnh sửa campaign** — chưa bắt đầu thì sửa và xoá được. Đang chạy thì **chỉ sửa tên và mô tả**, không dừng và không xoá |
| S18 | **"Vị trí của tôi"** — luôn hiện thứ hạng người đang xem kèm vài người liền kề |
| S19 | 🔧 **Đóng băng kết quả campaign** khi kết thúc. Khung cố định **không đóng băng**, là số liệu sống |
| S20 | 🔧 **Xem lại campaign đã kết thúc** — học viên thấy kết quả đã đóng băng |
| S24 | 🆕 **Ops xem và xuất Excel kết quả từng campaign** — đúng số đã đóng băng |
| S21 | **Tham số múi giờ ở cấp tổ chức** — biên kỳ cắt theo múi giờ tổ chức |
| S22 | **Tiêu chí phụ khi đồng hạng** — cùng chỉ số thì ai đạt sớm hơn xếp trên |
| ~~S23~~ | ~~Danh mục chỉ số đo lường dùng chung~~ 🗑️ **PO chốt 23/09: mỗi chỗ tự tính, vận hành tự cấu hình tham số.** Xem §6.8 |

### 🔧 `BR-TEST` — quy tắc tính bài kiểm tra *(đính chính v0.6)*

| Loại bài | Điều kiện | Tính khi nào |
|---|---|---|
| **Test** có `Graded Assignment = Yes` | **Có `Pass Point`** (mặc định `Auto 50%`, hoặc `Manual`) | **Chỉ tính khi đạt `Pass Point`** |
| **Test** có `Graded Assignment = No` | **Không có `Pass Point`** — không có khái niệm đạt/trượt | **Tính khi hoàn thành** |
| **Quiz** (trong Activity hoặc trong Video) | Không có ngưỡng đạt | ❌ **Không tính** |
| **Case Study** | Không có ngưỡng đạt | ❌ **Không tính** |

> **Nguồn:** PO xác nhận 23/09/2026 → KB `03-assessment.md` `KB-TEST-01a`, `KB-TEST-01b` *(đã cập nhật trong đợt này)*.
>
> Áp cho **cả hành động tính điểm** *"hoàn thành bài Test"* (S2) **và huy hiệu loại Test** (S5).
>
> 🟢 **Một tính chất tốt cho thiết kế:** `KB-TEST-01` ép `Manual Grading = Yes → Graded Assignment = Yes`, và `BR-EDIT-07` cấm sửa `Graded Assignment` sau khi đã có người làm bài. Nghĩa là **một bài Test không thể đổi giữa "có ngưỡng đạt" và "không có ngưỡng đạt"** khi đã có học viên làm — quy tắc đếm ổn định, không có nguy cơ điểm và huy hiệu bị tính lại ngược.

## Out of scope

| # | Không làm | Vì sao |
|---|---|---|
| N1 | **Bộ lọc bảng xếp hạng theo nhóm** — gồm cả theo lớp và theo phòng ban | Chờ chức năng nhóm **đồng bộ từ HRM** |
| N2 | **Chống cày riêng cho hoạt động chỉ có Text/Ảnh** | Chống cộng trùng và trần điểm/ngày vẫn áp cho mọi loại |
| ~~N3~~ | ~~Nhiều chiến dịch chạy song song~~ | 🗑️ **Đưa vào phạm vi ở `CR-013`.** Điểm campaign chỉ là điểm chung lọc theo khoảng và loại hành động, nên hai campaign chồng nhau không xung đột |
| N4 | **Điều kiện huy hiệu theo chuỗi ngày liên tiếp · mốc thời gian · nội dung cụ thể** | Thay bằng bốn loại đo bằng chỉ số đếm (S5) |
| N5 | **Thông báo thành tích qua email** | Chỉ đẩy trong hệ thống |
| **N6** | 🔧 **Tính điểm và tính huy hiệu từ Quiz và Case Study** | PO chốt: hai loại này **không tính**. Quiz không tính vào hoàn thành khoá học; Case Study chỉ làm được một lượt |
| N7 | **Giới hạn nội dung được tính trong chiến dịch** | PO không yêu cầu |
| N8 | **Tính năng Lộ trình học** và hành động "hoàn thành lộ trình" | Tính năng riêng, làm sau |
| N9 | **Tính năng Khung năng lực / Skills** và huy hiệu theo kỹ năng | Tính năng riêng, làm sau |
| N10 | **Sửa logic hoàn thành Activity** | PO chốt giữ nguyên |
| N11 | **Quản lý phần thưởng trong hệ thống** | Trao thưởng là hành động ngoài hệ thống |
| N12 | **Trang đo hiệu quả chiến dịch** | Hệ thống chỉ cung cấp **kết quả**; đội truyền thông tự đo bên ngoài |
| N13 | **Gamification cho nhân sự Ops** | Chỉ áp dụng cho học viên |
| N14 | **Thi đua theo đội / nhóm** | Chỉ xếp hạng cá nhân |
| N15 | **Cấu hình gamification riêng theo lớp hoặc khoá** | Cấu hình ở cấp tổ chức |
| N16 | **Màn quản lý nhiều tổ chức** | Chưa có multi-tenant. Dữ liệu vẫn thiết kế theo tổ chức — `C1` |
| N17 | **Module Tenant (`TNT.CFG.02`) đầy đủ** | Đợt này chỉ khai tham số múi giờ (S21) |
| **N18** | 🆕 **Hành động tính điểm "đạt điểm cao"** | PO chốt **tạm thời không có rule này**. Nhờ `C2`, thêm sau chỉ cần cấu hình |
| **N19** | 🆕 **Số điểm riêng cho từng campaign** | PO chốt 08/10: số điểm theo cấu hình chung, campaign chỉ chọn loại hành động |
| **N20** | 🆕 **Chọn người tham gia campaign theo lớp, khoá hoặc nhóm** | Toàn tổ chức. Theo nhóm chờ đồng bộ HRM, cùng lý do với `N1` |
| **N21** | 🆕 **Bộ chọn khoảng ngày tự do phía học viên** | Tránh học viên gọi phép tính nặng tuỳ ý. Vận hành vẫn có bộ chọn này ở màn danh sách học viên |
| **N22** | 🆕 **Dừng sớm campaign đang chạy** | Đang chạy thì luật không đổi, kể cả thời điểm kết thúc |
| **N23** | 🆕 **Thông báo khi campaign bắt đầu hoặc kết thúc** | `Recommendation` — thông báo chỉ dành cho thành tích (`S10`). Chờ PO duyệt |

## Potential scope

Bộ lọc theo nhóm sau khi đồng bộ HRM · giới hạn nội dung chiến dịch · điểm cho lộ trình · huy hiệu theo kỹ năng · đổi điểm lấy phần thưởng · tính điểm từ Quiz và Case Study

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

## 6.2 🔧 Khung cố định và campaign *(viết lại ở `CR-013`)*

| | **Khung cố định** | **Campaign** |
|---|---|---|
| Ai tạo | **Hệ thống tự tính** | **Vận hành khai tay** |
| Biên | `All time` · tuần · tháng · quý · năm theo lịch | Hai ngày bất kỳ, không cần trùng biên lịch |
| Chồng lấn | **Có** — tuần ⊂ tháng ⊂ quý ⊂ năm | **Có** — nhiều campaign được chồng thời gian |
| Cấu hình | Không cần màn nào | Tên · mô tả · khoảng thời gian · loại hành động tính điểm |
| Số điểm | Cấu hình chung | **Cấu hình chung** — campaign không sửa |
| Bảng | Theo khung: điểm · số hoạt động · số khoá. Chỉ ở `All time`: hạng · số huy hiệu *(chi tiết ở PRD, `CR-012`)* | **Hai bảng**: điểm từ các loại hành động được chọn · số hoạt động |
| Chỉnh sửa | — | Chưa bắt đầu: sửa và xoá được. Đang chạy: chỉ sửa tên, mô tả |
| Khi hết khoảng | **Số liệu sống**, không đóng băng | **Đóng băng** |
| Người tham gia | Toàn tổ chức | Toàn tổ chức |

## 6.3 Ràng buộc thiết kế bắt buộc

| # | Ràng buộc | Vì sao |
|---|---|---|
| **C1** | Cấu hình gắn với **tổ chức**, không đóng cứng | Định hướng đa tenant |
| **C2** | **Mọi danh mục phải mở rộng được bằng cấu hình** | Lộ trình, kỹ năng, bộ lọc nhóm, nhiều chiến dịch song song, và **tính điểm từ Quiz/Case Study** đều có thể thêm sau |
| **C3** | Lưu **từng lần cộng điểm kèm thời điểm** | Nền của lịch sử điểm, xếp hạng theo kỳ, tiêu chí phụ khi đồng hạng, luật chống cày |
| **C4** | Đổi cấu hình điểm → **áp dụng từ thời điểm đổi** | PO chốt |
| **C5** | 🔧 **Chống cộng trùng "đã học" tính trong phạm vi MỘT LƯỢT GHI DANH.** Học viên bị xoá khỏi lớp rồi thêm lại → lượt học mới **được tính điểm mới**, coi như khoá mới.<br>Chỉ cộng điểm khi bản ghi tiến độ **chuyển trạng thái** sang hoàn thành, tính từ thời điểm bật tính năng | PO xác nhận 23/09: **một khoá chỉ ở một lớp tại một thời điểm**, nên không có kịch bản học song song hai lớp. *(Sửa từ "chống cộng trùng cắt ngang lớp" của v0.1–v0.6 — xem Impact Matrix `CF-2`)* |
| **C6** | **Biên kỳ cắt theo múi giờ của tổ chức**, không theo giờ máy chủ | Module Tenant chưa có → đợt này khai một tham số múi giờ cấp tổ chức |
| **C7** | **Một lần cộng điểm thuộc về nhiều kỳ lịch cùng lúc** → điểm theo kỳ tính từ sổ giao dịch theo khoảng ngày. **Kết quả cuối kỳ lưu cứng** | Kỳ lịch lồng nhau theo bản chất |
| **C8** | **Mọi mốc dùng để xếp hạng phải lưu được thời điểm đạt** | Cần cho S22 và mọi chỉ số đếm |
| **C9** | **"Ngày" trong `S3` và trong trần điểm/ngày (`S8`) cắt theo múi giờ tổ chức**, cùng quy tắc với biên kỳ | Tránh hai định nghĩa "ngày" khác nhau trong cùng một cơ chế |
| **C10** 🆕 | **Tài khoản `Test Account` bị loại khỏi TOÀN BỘ logic gamification** — không điểm, không huy hiệu, không hạng, không lên bảng xếp hạng | `KB-USER-TA-01` — đây là tài khoản của L&D và QA dùng để kiểm tra khoá học, nhưng về mặt dữ liệu là học viên thật |

### 🔧 `BR-REGRADE` — quy tắc chấm lại *(cập nhật v0.6.1)*

| Rule | Nội dung |
|---|---|
| `BR-REGRADE-01` | Chấm lại **chỉ đi một chiều**: không-đạt → đạt. Không có trường hợp đạt → không-đạt. **Không cần cơ chế thu hồi điểm hay huy hiệu** |
| **`BR-REGRADE-02`** 🆕 | **Điểm được chốt tại LẦN CHẤM ĐẦU TIÊN.** Chấm lại **không ghi nhận thêm điểm** cho bài đó |

> ⚠️ **Hệ quả cần biết:** học viên trượt ở lần chấm đầu, chấm lại thành đạt → **không có điểm cho bài đó**. Nếu mentor chấm sai lần đầu thì học viên chịu thiệt. PO đã chốt, ghi lại để không ai hiểu nhầm là lỗi.

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

## 6.6 🔧 Tiêu chí phụ khi đồng hạng *(viết lại ở `CR-013`)*

Campaign không còn cho chọn chỉ số. Mỗi campaign có đúng hai bảng: điểm và số hoạt động. **`S22` vẫn bắt buộc** cho mọi bảng, cả khung cố định lẫn campaign: cùng chỉ số thì ai đạt mức đó sớm hơn xếp trên. Số khoá và số huy hiệu có khoảng giá trị rất hẹp, không có `S22` thì đồng hạng hàng loạt.

## 6.7 ✅ Cơ chế điểm khi vào hệ thống *(đã chốt)*

**Mỗi ngày học viên vào hệ thống thì được điểm một lần.** Vào nhiều lần trong ngày không cộng thêm.

*"Vào hệ thống hôm nay"* rộng hơn *"phát sinh sự kiện đăng nhập của Keycloak"* — học viên đăng nhập SSO qua Lark có thể mở ứng dụng nhiều ngày liền mà không sinh sự kiện đăng nhập mới. Nên nguồn đúng là **sự hiện diện của học viên trong hệ thống trong ngày đó**, không phải sự kiện Keycloak. → `OQ-B15`.

Chỉ số **số ngày có vào hệ thống** cũng chính là chỉ số đo huy hiệu loại **Tích cực** (S5).

## 6.8 Một danh mục chỉ số dùng chung cho ba chỗ

| Nơi dùng | Chỉ số |
|---|---|
| **Điều kiện huy hiệu** (S5) | Số ngày có vào hệ thống · số hoạt động hoàn thành · **số bài Test tính theo `BR-TEST`** · số khoá hoàn thành |
| **Ngưỡng lên hạng** (S6) | Điểm · số huy hiệu · số khoá hoàn thành |
| **Cấu phần campaign** (S16) | Điểm, chỉ từ các loại hành động được chọn · số hoạt động hoàn thành |

✅ **PO chốt 23/09/2026: mỗi chỗ tự tính. Vận hành tự cấu hình tham số ở từng nơi.**

Lý do hợp lý: **cách tính ở ba chỗ vốn đã khác nhau** — huy hiệu và ngưỡng hạng đếm **trọn đời**, chỉ số xếp hạng chiến dịch đếm **trong khoảng ngày của kỳ**. Gộp làm một cơ chế chung là gộp hai thứ khác bản chất.

Tập chỉ số dùng trong đợt này: **điểm tích luỹ · số ngày có mặt · số hoạt động hoàn thành · số bài Test (theo `BR-TEST`) · số khoá hoàn thành · số huy hiệu**. Danh sách do **hệ thống định nghĩa**; vận hành chọn dùng chỉ số nào và đặt ngưỡng bao nhiêu.

> 📌 **Một việc cần làm ở PRD dù mỗi chỗ tự tính:** viết **định nghĩa của từng chỉ số đúng một lần** trong `Solution`, rồi ba chỗ cùng dẫn về đó.
>
> Cái cần thống nhất không phải *cách tính* (khác nhau là đúng) mà là *cái gì được đếm* — ví dụ *"số khoá hoàn thành"* có tính khoá bỏ qua Foundation không (`BR-SKIP`), có tính khoá đã hết hạn không. Nếu ba chỗ tự hiểu thì học viên sẽ thấy *"5 khoá"* ở trang thành tích nhưng chiến dịch ghi 4 — và không ai biết chỗ nào sai.
>
> Đây là việc viết tài liệu, không phải ràng buộc thiết kế. Chi phí bằng 0.

## 6.9 🆕 Campaign *(`CR-013`)*

**Vì sao campaign quay lại.** `CR-007` bỏ chiến dịch vì bộ chọn khoảng ngày tự do đã bao trùm nó. `CR-013` bỏ bộ chọn tự do phía học viên, nên cần một cách khác để diễn tả **những khoảng thời gian có chủ đích**, ví dụ *"tháng học tập 15/10 – 15/11"*, mà khung cố định không diễn tả được.

### Điểm campaign không phải một loại điểm mới

Điểm campaign là **điểm chung, lọc theo hai điều kiện**: thời điểm cộng nằm trong khoảng campaign, và loại hành động nằm trong danh sách vận hành chọn. `C3` đã lưu từng lần cộng kèm nguồn và thời điểm, nên **không phải ghi thêm gì** khi học viên hành động.

```
Sổ giao dịch điểm (đã có)
   │
   ├── lọc: thời điểm cộng ∈ [bắt đầu, kết thúc]
   ├── lọc: loại hành động ∈ danh sách campaign chọn
   ▼
Bảng điểm của campaign
```

Bảng số hoạt động lọc tương tự trên dữ liệu học: hoạt động chuyển sang hoàn thành trong khoảng campaign.

### Rule

| # | Rule | Nguồn |
|---|---|---|
| 1 | Một lần cộng điểm thuộc campaign khi **thời điểm cộng** nằm trong khoảng campaign | PO chốt 08/10 |
| 2 | Bài Test nộp trong campaign mà **chấm đạt sau khi kết thúc thì không tính** — thời điểm cộng điểm là lúc chấm đạt | PO chốt 08/10 |
| 3 | Kết thúc thì **đóng băng**. Học viên bị `Block` hoặc rời tổ chức vẫn nằm trong kết quả đã đóng băng | PO chốt 08/10 · `A14` |
| 4 | Campaign **phụ thuộc cấu hình chung**. Tắt `Points` hoặc tắt một hành động thì phần đó ngừng đóng góp cho mọi campaign đang chạy | Hệ quả của `S16` |
| 5 | Đổi số điểm chung khi campaign đang chạy thì **campaign mang hai mức điểm**, theo `C4` | PO chấp nhận 08/10 |
| 6 | Campaign nằm **trong trang bảng xếp hạng**. Tắt bảng xếp hạng thì campaign ẩn theo, dữ liệu giữ nguyên | PO chốt 08/10 |
| 7 | `Test Account` không có mặt trong campaign | `C10` |

### `Recommendation` — bốn mặc định chưa hỏi PO, duyệt ở Gate 1

| # | Mặc định | Lý do |
|---|---|---|
| a | Khoảng campaign tính **theo ngày trọn**, biên ngày cắt theo múi giờ tổ chức | Cùng quy tắc với khung cố định (`C6`) |
| b | **Ngày bắt đầu không được ở quá khứ** | Campaign tính hồi tố thì học viên không biết mình đang thi đua |
| c | Phải chọn **ít nhất một loại hành động** | Không chọn gì thì bảng điểm rỗng |
| d | **Không thông báo** khi campaign bắt đầu hoặc kết thúc (`N23`) | Thông báo chỉ dành cho thành tích (`S10`) |

---

# 7. Danh sách User Story dự kiến

## Phía học viên (UpLMS)

| ID | User Story | Nguồn | Ghi chú |
| --- | --- | --- | --- |
| **US1** | Là học viên, tôi cần xem điểm, hạng và huy hiệu đã đạt để biết nỗ lực học của mình được ghi nhận tới đâu | Dòng 10 · O2 | Trang "Thành tích của tôi" |
| **US2** | Là học viên, tôi cần được báo ngay khi nhận điểm, đạt huy hiệu hoặc lên hạng **trong lúc đang dùng hệ thống** | Dòng 9 · O2 · S10 | Không gửi khi offline |
| **US3** | Là học viên, tôi cần tra được từng lần cộng điểm đến từ đâu để tin vào con số của mình | Dòng 8 · O6 · C3 | |
| **US4** | Là học viên, tôi cần biết huy hiệu nào sắp đạt và còn thiếu gì để có mục tiêu ngắn hạn | Dòng 10 · O3 | Tính tiến độ tới **mọi** huy hiệu chưa đạt |
| **US5** | Là học viên, tôi cần việc vào hệ thống mỗi ngày được ghi nhận thành điểm để có lý do mở ứng dụng hằng ngày | Dòng 2 · S3 · O1 | `OQ-B15` |
| **US6** | Là học viên, tôi cần xem bảng xếp hạng theo khung cố định hoặc theo campaign đang chạy để biết mình đứng ở đâu so với người khác | CR-001 · CR-013 · S14 · S15 | Toàn tổ chức. Không có khoảng ngày tự do |
| **US7** | Là học viên, tôi cần luôn thấy vị trí của chính mình kèm vài người liền kề để biết mình cần hơn ai một chút là lên hạng | CR-001 · S18 | Cơ chế giảm nhẹ chính cho bảng toàn tổ chức |
| **US8** | Là học viên, tôi cần xem lại kết quả các campaign đã kết thúc để nhìn lại thành tích đã đạt | CR-001 · CR-013 · S20 | Kết quả đã đóng băng |

## Phía vận hành (UpLMS Ops)

| ID | User Story | Nguồn | Ghi chú |
| --- | --- | --- | --- |
| **US9** | Là nhân sự vận hành, tôi cần khai hành động nào được bao nhiêu điểm và bật/tắt từng hành động để điều chỉnh cơ chế theo mục tiêu từng giai đoạn | Dòng 1, 2 | Chịu `BR-TEST` |
| **US10** | Là nhân sự vận hành, tôi cần tạo và quản lý huy hiệu theo bốn loại với ngưỡng số lượng để thiết kế các mốc mục tiêu cho học viên | Dòng 3, 4 · S5 | Chịu `BR-TEST` |
| **US11** | Là nhân sự vận hành, tôi cần đặt các hạng và ngưỡng lên hạng theo nhiều chỉ số để phân tầng mức độ tham gia của học viên | Dòng 5 · S6 | |
| **US12** | Là nhân sự vận hành, tôi cần tạo campaign có thời hạn riêng và chọn loại hành động được tính điểm, để tổ chức phong trào học tập theo mục tiêu từng đợt | CR-013 · S15 · S16 | Toàn tổ chức. Được chồng thời gian. Số điểm theo cấu hình chung |
| **US13** | Là nhân sự vận hành, tôi cần campaign đang chạy không đổi được luật để kết quả thi đua công bằng | CR-002 · CR-013 · S17 | Chỉ sửa tên, mô tả. Chỉ xoá khi chưa bắt đầu |
| **US14** | Là nhân sự vận hành, tôi cần kết quả campaign được đóng băng khi kết thúc, xem và xuất được, để công bố và trao thưởng | CR-013 · S19 · S24 · O4 | Xuất Excel |
| **US15** | Là nhân sự vận hành, tôi cần điểm phản ánh việc học thật, không bị đẩy lên bằng thao tác đối phó | Dòng 7 · O6 | Chịu `C5` |
| **US16** | Là nhân sự vận hành, tôi cần bật/tắt gamification và bật/tắt hiển thị phía học viên riêng biệt, để chạy thử cơ chế trước khi mở | Dòng 11 · S12 | |
| **US17** | Là quản trị, tôi cần phân quyền để chỉ vai trò vận hành phù hợp mới sửa được cấu hình gamification | `[suy ra]` · S13 | |

## Chưa làm trong đợt này

| ID | User Story | Nguồn |
| --- | --- | --- |
| **US18** | *Bộ lọc bảng xếp hạng theo nhóm* — **chưa làm.** Là công cụ duy nhất phục vụ stakeholder Quản lý trực tiếp | N1 |
| **US19** | *Campaign riêng cho từng nhóm* — **chưa làm.** Chồng thời gian đã có, phạm vi theo nhóm thì chưa | N20 |
| **US20** | *Tính điểm và huy hiệu từ Quiz và Case Study* — **chưa làm** | N6 |
| **US21** | *Giới hạn nội dung chiến dịch* — **chưa làm** | N7 |
| **US22** | *Điểm cho lộ trình* — **chưa làm** | N8 |
| **US23** | *Huy hiệu theo kỹ năng* — **chưa làm** | N9 |

---

# 8. Tác động tới hệ thống hiện tại

> **Chưa chạy Impact Analysis.** Đánh giá sơ bộ. **Chi tiết ở Gate 2.**

| Vùng ảnh hưởng | Mức | Ghi chú |
| --- | --- | --- |
| **Dữ liệu** | 🔴 Cao | Toàn bộ cấu trúc điểm, huy hiệu, hạng, kỳ, chiến dịch, sổ giao dịch, snapshot là mới. Chịu C1–C9 |
| **Hiệu năng** | 🔴 Cao | Xếp hạng tính từ sổ giao dịch theo khoảng ngày, toàn tổ chức, nhiều kỳ lồng nhau — `OQ-B9`. 🔧 `CR-013`: học viên chỉ chọn khung cố định nên mọi bảng phía học viên tính sẵn được. Mỗi campaign đang chạy thêm hai bảng phải tính |
| **Assessment** | 🟠 Vừa | 🔧 `BR-TEST` phụ thuộc `Graded Assignment` và `Pass Point`. Phải phân biệt được Test / Quiz / Case Study khi bắt sự kiện — **Quiz và Case Study phải bị loại ra** |
| **Tổ chức / Tenant** | 🟠 Vừa | Tham số múi giờ cấp tổ chức (S21, C6, C9) |
| **Learning Experience** | 🟠 Vừa | Nguồn sự kiện chính. Chỉ đọc, không sửa |
| **Course / Certificate** | 🟠 Vừa | "Số khoá hoàn thành" dùng ở ba chỗ |
| **User / Auth** | 🟡 Thấp | `S3` chuyển sang "có mặt trong ngày", không phụ thuộc sự kiện đăng nhập Keycloak |
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
| A15 | **Bảng xếp hạng công khai danh tính học viên** | ✅ PO chốt: công khai bình thường |
| A16 | **Kỳ lịch bắt đầu từ thời điểm bật tính năng** | ✅ PO xác nhận |
| ~~A17~~ | ~~Kỳ lịch luôn xếp theo điểm. Chọn chỉ số chỉ áp cho chiến dịch~~ | 🗑️ **Không còn đúng.** Khung cố định có nhiều bảng (`CR-012`, xem PRD). Campaign có đúng hai bảng, không chọn chỉ số (`CR-013`) |
| A18 | **Chiến dịch chưa tới ngày bắt đầu thì sửa được**, chỉ khoá khi đã chạy | ✅ PO xác nhận |
| A19 | **Tắt `Visibility in UpLMS` thì không đẩy thông báo thành tích** | ✅ PO xác nhận |
| A20 | **Phạm vi người tham gia chiến dịch ở đợt này là toàn bộ học viên** | ✅ PO chốt |
| A22 | **Huy hiệu và điểm chỉ tính từ bài Test**, theo `BR-TEST` | ✅ PO chốt |
| ~~A23~~ | ~~"Đạt điểm cao" chỉ áp cho bài có `Graded Assignment = Yes`~~ | 🗑️ **Không còn cần** — hành động đã bỏ khỏi phạm vi |
| **A24** | **Điểm bài Test chốt tại lần chấm đầu tiên**; chấm lại không cộng thêm | ✅ **PO chốt 23/09** → `BR-REGRADE-02` |
| **A25** | **My Learning hiện điểm TÍCH LUỸ của cá nhân** (tính từ lúc vào hệ thống) và hạng hiện tại — **không hiện điểm theo kỳ** | ✅ **PO chốt 23/09** |
| **A26** | 🆕 **Không có khoá Trial trong hệ thống** — endpoint `trial/upgrade-now` tồn tại nhưng tính năng không có | ✅ **PO chốt 23/09** → KB `14` §2.2 |
| **A27** | 🆕 **Chạy ngầm không phải tính bù.** Dữ liệu ghi trong giai đoạn chạy ngầm là ghi **theo thời gian thực**, nên khi bật `Visibility` thì hiện đầy đủ. *"Không có tính bù"* nghĩa là **không dựng lại lịch sử trước khi bật `Gamification`** | ⚠️ **Cách hiểu của tôi** — PO xác nhận lại ở Gate 2 |

---

# 10. Open Questions

| # | Câu hỏi | Vì sao quan trọng | Người trả lời | Chặn bước sau? |
| --- | --- | --- | --- | --- |
| **OQ-B2** | **Dữ liệu tiến độ học có dấu thời gian không?** | Cần cho C5, C7, trần điểm/ngày, và hai con số ở §2 | Dev | **Yes** — trước Gate 2 |
| **OQ-B9** | **Bảng xếp hạng chịu tải được không?** | Quyết định giữa tính trực tiếp và tính sẵn theo chu kỳ | Dev | **Yes** — trước Gate 2 |
| **OQ-B12** | **Thời điểm đạt huy hiệu, hoàn thành khoá, hoàn thành bài Test có lưu được không?** | `C8` — cần cho tiêu chí phụ khi đồng hạng và mọi chỉ số đếm | Dev | **Yes** — trước Gate 2 |
| **OQ-B15** | **Ghi nhận "học viên có vào hệ thống hôm nay" bằng cách nào?** Sự kiện đăng nhập Keycloak **không đủ** vì SSO Lark giữ phiên sống nhiều ngày | Nguồn dữ liệu cho `S3` và huy hiệu loại Tích cực | Dev | **Yes** — trước Gate 2 |
| **OQ-B11** | **Múi giờ tổ chức khai ở đâu trong đợt này?** | `C6`, `C9` | PO + Dev | No — Gate 2 |

## ✅ Đã đóng

| # | Kết luận |
|---|---|
| `OQ-B1` `OQ-B14` | **Không còn cần** — `S3` đổi sang "mỗi ngày vào hệ thống", không phụ thuộc sự kiện đăng nhập Keycloak |
| `OQ-B3` | Đội truyền thông **tự đo hiệu quả bên ngoài** → `N12` |
| `OQ-B4` | Ba con số đã nêu cụ thể ở §2 kèm cách lấy |
| `OQ-B5` `OQ-B6` | **Chỉ đẩy trong hệ thống khi online. Không gửi mail** → `S10`, `N5` |
| `OQ-B7` | **Không bật lại 8 mail luồng chấm điểm** |
| `OQ-B8` | **Giữ `Point` = điểm, `Level` = hạng học viên** |
| `OQ-B10` | Đồng hạng xử lý theo **thời điểm đạt** |
| `OQ-B13` | ~~Chiến dịch không chồng lấn ở đợt này~~ → 🔄 **Đảo ở `CR-013`: campaign được chồng thời gian** |
| `OQ-B16` | 🔧 **Chỉ đếm bài Test. Quiz và Case Study không tính** → `BR-TEST`, `N6` |
| `OQ-B17` | 🗑️ **Không còn cần** — PO chốt **bỏ hành động "đạt điểm cao"** khỏi phạm vi đợt này → `N18` |

---

# 11. References

| File KB | Dùng cho |
|---|---|
| `03-assessment.md` | **`BR-TEST`** — `Graded Assignment`, `Pass Point`, `KB-TEST-01a`, `KB-TEST-01b`. **Đã cập nhật trong đợt này** |
| `07-learning-experience.md` | `KB-LX-03a`, `KB-LX-03b` — nền của §6.5. **Đã cập nhật trong đợt này** |
| `01-course.md` | `BR-EDIT-07` — không sửa `Graded Assignment` sau khi có người làm bài |
| `09-notification-email.md` | Nay chỉ để đối chiếu, không còn là phụ thuộc |
| `13-mail-events.md` | Xác nhận gamification **không đụng tới** 30 mail |
| `12-data-model.md` | Nền của `C5`, `C6`; phòng ban chỉ gắn nhân sự |
| `14-api-surface.md` | `Group Management`, `Department Management` |
| `15-product-direction.md` | Định hướng đa tenant — nền của `C1` |
| `04-class.md` · `06-user-account.md` · `08-certificate.md` | Nguồn sự kiện và các chỉ số đếm |

| Nguồn khác | |
|---|---|
| Yêu cầu gốc | `working/raw-inputs/yeu-cau-goc-20260923.md` |
| Change requests | `working/raw-inputs/change-requests.md` — CR-001…006, CR-013 |
| Quyết định đã chốt | `project-decisions.md` |
| BRD bản trước | `docs/brd/brd-v0.1` … `v0.6` (23/09/2026) |
| Schema DB | [Lark → Data Architecture](https://upbasevn.sg.larksuite.com/wiki/MaFpweI68iKNMvkTioLlJ1uJgQd) |
| Swagger | `lms-be.staging.upbase.asia/api/v1/docs` · `ops-be.staging.upbase.asia/api/v1/docs` |
| Tham chiếu ngoài | `TNT.CFG.02` — Hồ sơ tổ chức và tham số, module Tenant *(chưa làm)* |
