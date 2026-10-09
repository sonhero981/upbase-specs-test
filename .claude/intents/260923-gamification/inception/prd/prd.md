---
intent: 260923-gamification
artifact: prd
version: 0.10
status: review
approved: 2026-09-23 (v0.2, Gate 4, Approved with Notes)
note: v0.10 mang CR-009 đến CR-013 và design đã chốt, chờ PO duyệt lại
lark: KeT8dkIStofZ0axlTW5l4S94gre
lark-title: [PRD] Gamification
lark-version: 0.8
migrated-from: .claude/projects/Gamification/docs/prd/prd-gamification-v0.10-20261008.md
---
# [PRD] Gamification — Điểm, huy hiệu, hạng và bảng xếp hạng

| | |
| --- | --- |
| **Target release** | ❓ *cần điền* |
| **Epic** | ❓ *link Jira* |
| **Story** | ❓ *link Jira* |
| **Related** | `brd-v0.7-20261008.md` · `impact-matrix-v0.3-20261008.md` · `solution-comparison-v0.2-20261008.md` |
| **Document status** | 🔄 **v0.10 chờ PO review lại** — mang `CR-009` đến `CR-013` và design đã chốt. Bản v0.2 đã được PO duyệt 23/09/2026 |
| **Document owner** | Bùi Đức Huy (PO) |
| **Designer** | ❓ *cần điền* |
| **Tech lead** | ❓ *cần điền* |
| **QA** | ❓ *cần điền* |
| **Reviewer** | ❓ *cần điền* |

---

# Document version

| Version | Người cập nhật | Nội dung | Impact | Ngày cập nhật |
| --- | --- | --- | --- | --- |
| v0.1 | Bùi Đức Huy | Bản khung: bối cảnh, giải pháp tổng thể và danh sách US | — | 23/09/2026 |
| v0.2 | Bùi Đức Huy | Viết chi tiết `US1` đến `US15`. Bỏ chiến dịch và kỳ lịch, thay bằng bộ chọn khoảng ngày (`CR-007`). Tách cấu hình thành bốn màn, khoá mốc huy hiệu, hạng thành số tịnh tiến, bảng xếp hạng tách theo chỉ số (`CR-008`) | `CR-007` · `CR-008` | 23/09/2026 |
| v0.3 | Bùi Đức Huy | Điểm check-in tăng dần theo chuỗi ngày đăng nhập liên tiếp, thêm khối chuỗi trên trang Thành tích (`CR-009`). Đổi thuật ngữ "khử trùng" thành "chống cộng trùng". Làm rõ `C5` bằng định nghĩa lượt ghi danh | `CR-009` | 01/10/2026 |
| v0.4 | Bùi Đức Huy | Bỏ trần điểm mỗi ngày, kéo theo bỏ sự kiện `No points`. Làm rõ logic lên hạng: mỗi mốc chạm được đều cho một hạng. Màn lịch sử thành panel `Achievement history` kèm bộ chuỗi tiếng Anh đầy đủ (`CR-010`) | `CR-010` | 01/10/2026 |
| v0.5 | Bùi Đức Huy | Áp design đã chốt: bước tăng chuỗi cố định `5`, trần `40` chạm đúng ngày thứ 7, bỏ chuỗi dài nhất. Danh sách huy hiệu chuyển sang `My Profile` → tab `Badges`. Thêm hành vi trỏ và bấm trên dải tóm tắt. Viết lại cột `Nguồn` thành nội dung đọc được | Design chốt 01/10 | 01/10/2026 |
| v0.6 | Bùi Đức Huy | Gộp bốn màn cấu hình Ops thành một trang bốn khối. Thêm mục **Design** kèm sáu ảnh màn đã chốt. Tooltip cho ô chuỗi | Design chốt 01/10 | 01/10/2026 |
| v0.7 | Bùi Đức Huy | Bỏ viết tắt: `Giải O2` thành `Giải quyết mục tiêu O2`, mã ràng buộc trần thành mã kèm nội dung. Thêm dấu phân cách giữa các mã đứng liền nhau | — | 01/10/2026 |
| v0.8 | Bùi Đức Huy | Thêm mục **Out of scope** cấp tính năng và mục **Unit** chia 15 US thành 5 nhóm bàn giao kèm phụ thuộc. Học từ phase Inception của AI-DLC | — | 05/10/2026 |
| v0.9 | Bùi Đức Huy | Trang cấu hình Ops **tự lưu, bỏ nút lưu**. Chỉ giữ hai xác nhận dạng popover cạnh công tắc. Tắt `Points` hoặc `Badges` thì tiêu chí lên hạng tương ứng khoá theo. Thay "chặn lưu" bằng "không tắt được tiêu chí và bảng cuối cùng". Bỏ giới hạn trên của số điểm. Bỏ ô chọn múi giờ và nhãn trạng thái — múi giờ lấy theo tenant | `CR-011` | 06/10/2026 |
| v0.10 | Bùi Đức Huy | **Campaign quay lại** (`US19` đến `US21`): vận hành chọn khoảng thời gian và loại hành động, số điểm theo cấu hình chung, hai bảng điểm và số hoạt động, đóng băng khi kết thúc. Học viên **bỏ bộ chọn khoảng ngày tự do**, chỉ còn khung cố định (`CR-013`).<br>Bảng xếp hạng thành **năm bảng**: thêm `Activities`, `Badges` chỉ còn ở `All time` như `Level`. Câu chữ check-in thay cho "login". Chỉ số đếm không phụ thuộc công tắc `Points`. Xoá `BR-6.14` (`CR-012`) | `CR-012` · `CR-013` | 08/10/2026 |

> ✅ **`Approved with Notes` — PO duyệt bản v0.2 ngày 23/09/2026.** Các bản từ v0.3 trở đi mang thay đổi mới, **chờ PO duyệt lại**. Còn **12 câu hỏi mở** ở mục `Vấn đề tồn đọng`. Bốn câu mới về campaign (`OQ-42` đến `OQ-45`) cần trả lời trước khi bàn giao Unit Campaign, không chặn các Unit khác.

---

# Problem

**Học viên đã được ghi danh vào khoá nhưng không chủ động quay lại học.**

| | |
|---|---|
| **Ai gặp** | Học viên trên UpLMS — đã có tài khoản, đã được thêm vào lớp, đã có nội dung để học |
| **Gặp khi nào** | Trong suốt thời gian học, đặc biệt ở giai đoạn giữa khoá khi không còn động lực ban đầu và chưa thấy đích |
| **Hậu quả** | Học viên học dở dang hoặc học dồn sát hạn. Vận hành phải thúc thủ công. Đội truyền thông nội bộ muốn tổ chức phong trào học tập nhưng không có số liệu nào để biết ai đang cố gắng |

Hệ thống hiện tại **chỉ ghi nhận việc học, không phản hồi lại việc học**. Học viên hoàn thành một hoạt động thì thanh tiến độ nhích lên — ngoài ra không có gì. Không có sự ghi nhận, không có mốc để nhắm tới, không có lý do để quay lại vào ngày hôm sau khi chưa tới hạn.

---

# Analytics

## Số liệu thật — General Launch, 8/9–21/9/2026

| Chỉ số | Tiêu chí đặt ra | Thực tế | |
|---|---|---|---|
| **Activation** | 80% nhân viên được gán khoá **đăng nhập lần đầu** trong 7 ngày kể từ General Launch | **40.2%** (53/132) | ❌ hụt một nửa |
| **Course start** | 80% người được gán đã **bắt đầu** khoá học trong 7 ngày | **22%** (29/132) | ❌ hụt gần 4 lần |
| **Completion** | 80% **hoàn thành** khoá bắt buộc đầu tiên trong 14 ngày | **64.1%** (93/145) | ❌ |

> ⚠️ Mẫu số khác nhau: Activation và Course start tính trên **132**, Completion tính trên **145** — hai nhóm người khác nhau. `OQ-01`

## Con số quan trọng nhất không nằm trong bảng

**53 người đăng nhập, chỉ 29 người bắt đầu học** — tức **24 người đã vào hệ thống rồi không bắt đầu gì cả**, bằng **45% số người đã chịu mở ứng dụng**.

Vấn đề tách thành **ba tầng riêng biệt**, mỗi tầng một nguyên nhân khác nhau:

| Tầng | Số đo | Nghĩa là gì |
|---|---|---|
| **1. Không mở ứng dụng** | Activation **40.2%** | 6/10 người được gán khoá không vào lấy một lần trong tuần đầu |
| **2. Mở rồi không học** | **45%** người đăng nhập không bắt đầu | Không phải vấn đề tiếp cận — vào tới nơi rồi vẫn không bắt đầu |
| **3. Bắt đầu rồi bỏ dở** | Completion **64.1%** | Đã bắt đầu nhưng không tới đích trong thời hạn |

## Vận hành đang xoay xở thế nào

| Hướng | Hiện trạng |
|---|---|
| **Cách làm hiện tại** | Theo dõi tiến độ qua dashboard SIS, thấy ai chậm thì thúc thủ công. 30 mail tự động đều là **mail sự kiện** — không có mail nào nhằm tạo động lực |
| **Công cụ bị hạn chế** | Giao diện soạn và gửi thông báo thủ công trên Ops **đang ẩn** (3/4 page module Notification & Email) |
| **Tiêu chí quyết định** | Vận hành nhìn phần trăm tiến độ và thời hạn còn lại — hai con số **cho biết ai đang chậm, không cho biết ai đang cố gắng** |
| **Chỗ sai** | Phụ thuộc vận hành nhớ và làm thủ công, không mở rộng được, và **không tạo được thói quen**. Số liệu cho thấy cách này **không đạt mục tiêu ở cả ba chỉ số** |

---

# Objective

| # | Kết quả muốn đạt |
|---|---|
| O1 | **Học viên quay lại học đều đặn hơn** mà không cần vận hành nhắc thủ công |
| O2 | **Nỗ lực học được ghi nhận ngay lúc nó xảy ra** |
| O3 | **Học viên có mốc ngắn hạn để nhắm tới** |
| O4 | **Đội truyền thông nội bộ có kết quả để công bố**: chạy campaign trong khoảng thời gian có chủ đích, kết quả đóng băng khi kết thúc; và lấy số liệu khoảng ngày bất kỳ ở màn danh sách học viên bên Ops. Việc đánh giá hiệu quả và trao thưởng do họ tự làm bên ngoài |
| O5 | **Điểm số đáng tin** — mỗi con số truy được nguồn, không bị thổi lên bằng thao tác đối phó |

---

# Out of scope

Những thứ **cả tính năng này không làm**. Gồm cả thứ người đọc dễ tưởng là có, và thứ từng nằm trong phạm vi rồi bị loại giữa chừng.

| Không làm | Vì sao |
|---|---|
| **Kỳ lịch như thực thể riêng · chốt kỳ cho khung cố định** | Khung cố định là số liệu sống. Chỉ campaign mới đóng băng (`US21`) |
| **Bộ chọn khoảng ngày tự do phía học viên** | Bỏ ở change request `CR-013`, để học viên không gọi được phép tính nặng tuỳ ý. Vận hành vẫn có ở `US12` |
| **Số điểm riêng cho từng campaign** | PO chốt ngày 08/10: số điểm theo cấu hình chung, campaign chỉ chọn loại hành động |
| **Chọn người tham gia campaign theo lớp, khoá hoặc nhóm** | Toàn tổ chức. Theo nhóm chờ chức năng nhóm đồng bộ từ HRM |
| **Dừng sớm campaign đang chạy** | Đang chạy thì luật không đổi, kể cả thời điểm kết thúc |
| **Trần điểm mỗi ngày** | Đã cân nhắc và loại ở change request `CR-010`. Chống cộng trùng (`BR-13.1`) đã chặn việc lặp lại cùng một nội dung, còn trần ngày thì phạt nhầm người học dồn |
| **Chuỗi dài nhất từng đạt** | PO chốt ngày 01/10 không hiện. Chỉ số quá khứ không giúp học viên quyết định gì hôm nay |
| **Bộ lọc bảng xếp hạng theo nhóm, lớp, phòng ban** | Chờ chức năng nhóm đồng bộ từ HRM. Xem `US16 — chưa làm` |
| **Tính điểm từ Quiz, Case Study, Storyline** | PO chốt không tính ở đợt này. Chỉ bài Test theo `BR-TEST` mới sinh điểm |
| **Huy hiệu cho điểm số cao** *(ví dụ bài Test đạt từ 90%)* | PO chốt tạm thời không có rule này |
| **Điểm cho lộ trình học · huy hiệu theo kỹ năng** | Thuộc tính năng Lộ trình và Khung năng lực, cả hai chưa làm |
| **Sửa logic hoàn thành Activity** | Giữ nguyên cơ chế hiện có. Gamification chỉ đọc dữ liệu học, không sửa |
| **Phần thưởng vật chất · gamification cho nhân sự Ops · thi đua theo đội** | Chưa yêu cầu |

---

# Stakeholder

| Stakeholder | Action |
| --- | --- |
| **Học viên (UpLMS)** | Nhận điểm · nhận huy hiệu · lên hạng · xem trang thành tích · tra lịch sử điểm · xem bảng xếp hạng và vị trí của mình |
| **Nhân sự vận hành (UpLMS Ops)** | Khai bảng điểm · tạo huy hiệu · đặt hạng và ngưỡng · bật/tắt cơ chế |
| **Đội truyền thông nội bộ** | Chọn khoảng ngày để lấy số liệu · công bố và **trao thưởng ngoài hệ thống** |
| **L&D** | Dùng dữ liệu điểm, hạng, huy hiệu để đánh giá mức độ tham gia học tập ở quy mô tổ chức |
| **Quản lý trực tiếp** | Theo dõi tình hình học của nhân viên mình phụ trách |
| **QA** | Điền mục `Conner case` của từng US |

> ⚠️ **Quản lý trực tiếp chưa có công cụ riêng trong phạm vi này.** Cần bộ lọc bảng xếp hạng theo nhóm (`US16 — chưa làm`), chờ đồng bộ sơ đồ tổ chức từ HRM.

---

# Preferences

❓ **Cần bổ sung trước khi bàn giao** — đây là nơi Dev và QA tìm mọi thứ để bắt đầu.

- **UX:** ❓ *link Figma — chưa có*. Ảnh design chốt ngày 01/10 nằm ở mục **Design** ngay dưới
- **Luồng giải pháp:** `working/solution-options/solution-comparison-v0.1-20260923.md` §9
- **Phân tích ảnh hưởng:** `working/impact-analysis/impact-matrix-v0.2-20260923.md`
- **Tài liệu nền:** `docs/brd/brd-v0.6-20260923.md` · `project-decisions.md`
- **API tham chiếu:** `lms-be.staging.upbase.asia/api/v1/docs` · `ops-be.staging.upbase.asia/api/v1/docs`
- **Tham chiếu ngoài:** `TNT.CFG.02` — Hồ sơ tổ chức và tham số *(module Tenant, chưa làm)*
- **KB liên quan:** `03-assessment.md` (`BR-TEST`) · `06-user-account.md` §8b (`Test Account`) · `07-learning-experience.md` (điều kiện hoàn thành) · `12-data-model.md` · `15-product-direction.md` §6
- **Tài khoản staging:** ❓ *chưa có*

---

# Metrics success

> Ba chỉ số dưới là **chỉ số thật đang đo của chính sản phẩm**, lấy từ General Launch 8/9–21/9/2026. Mốc nền là số đo trước khi có gamification.

| Factor (HEART) | Goal | Signal | Metrics |
| --- | --- | --- | --- |
| **Adoption** | Học viên được gán khoá chịu mở ứng dụng | Đăng nhập lần đầu trong 7 ngày | **Activation** — mốc nền **40.2%**, tiêu chí **80%** |
| **Engagement** | Vào rồi thì bắt đầu học, không bỏ đó | Bắt đầu khoá trong 7 ngày | **Course start** — mốc nền **22%**, tiêu chí **80%** |
| **Task Success** | Học tới đích trong thời hạn | Hoàn thành khoá bắt buộc đầu tiên trong 14 ngày | **Completion** — mốc nền **64.1%**, tiêu chí **80%** |
| **Retention** | Quay lại đều đặn, không học dồn | Số ngày có mặt trong tháng | ❓ *chưa có mốc nền — gamification tạo ra số này lần đầu* |

Hai factor còn lại (**Happiness**) **xoá vì chưa có cách đo** — không có khảo sát hài lòng trong phạm vi này.

---

# Design

Sáu màn đã chốt ngày 01/10/2026. Ảnh gốc nằm trong repo ở `.claude/projects/Gamification/design/`.

| Màn | Thuộc US | Chốt gì ở đây |
|---|---|---|
| **Gamification** | `US1` · `US6` · `US7` | Dải tóm tắt bốn ô · bảng xếp hạng bốn tab · khối vị trí của tôi với đường kẻ `Show All`. ⚠️ **Cần cập nhật theo `CR-012`, `CR-013`**: thêm tab `Activities`, bỏ bộ chọn khoảng ngày tự do, thêm lối vào campaign |
| **How to collect points** | `US1` | Panel trượt từ phải, bốn dòng theo bốn hành động tính điểm |
| **How to level up** | `US1` · `US10` | Panel trượt từ phải, ba tiêu chí lên hạng |
| **Achievement history** | `US3` | Panel trượt từ phải, nội dung dạng câu văn |
| **User Profile — Badges** | `US4` | Tab trong `My Profile`, bộ đếm `({đã đạt}/{tổng mốc})`, huy hiệu chưa đạt hiện xám |
| **Ops — Enable Setting** | `US8` · `US9` · `US10` · `US11` · `US14` | Một trang bốn khối, mốc huy hiệu chỉ đọc. **Tự lưu, không có nút lưu.** Không có ô chọn múi giờ |
| **Ops — Disable** | `US14` | `Gamification` tắt thì mọi khối khác biến mất |
| **Campaign** | `US19` · `US20` · `US21` | ❓ **Chưa có design** — học viên xem campaign, vận hành tạo campaign, vận hành xem và xuất kết quả |

# Solution

## TDD

### Nguyên tắc nền

**Gamification chỉ đọc dữ liệu học tập, không sửa.** Nó ghi ra bản ghi của riêng nó. Đây là điều kiện để giữ nguyên logic hoàn thành Activity hiện tại và để bật/tắt gamification không ảnh hưởng gì tới việc học.

### Cách bắt sự kiện: **tính trong luồng**

Điểm được cộng **ngay trong cùng thao tác** với việc hoàn thành hoạt động, không qua tác vụ nền, không qua hàng đợi. Học viên thấy điểm **tức thì**.

> **`NFR-GAM-01` — bắt buộc.** Lỗi ở gamification **không được làm hỏng thao tác học**. Học viên bấm Hoàn thành thì thao tác đó **phải thành công**, kể cả khi phần cộng điểm gặp lỗi. Phần cộng điểm cũng **không được làm chậm cảm nhận** của thao tác.
>
> Hệ quả phải xử lý: lỗi bị chặn lại thì **điểm lần đó mất mà không ai biết** → `OQ-02`.

### Năm luồng

```mermaid
flowchart TD
    subgraph TT["NHỊP TỨC THÌ"]
        A["Học viên hoàn thành<br/>hoạt động · khoá · bài Test"] --> B["Cộng điểm<br/>ghi vào sổ giao dịch"]
        V["Học viên vào hệ thống<br/>lần đầu trong ngày"] --> B
        B --> C["Xét huy hiệu"]
        C --> D["Xét hạng"]
        D --> E["Thông báo đẩy<br/>nếu đang online"]
        E --> H["Học viên thấy điểm<br/>NGAY LẬP TỨC"]
    end
    subgraph CK["NHỊP 8 TIẾNG"]
        F["Tác vụ nền đọc<br/>sổ giao dịch"] --> G["Tính bảng xếp hạng<br/>ghi đè kết quả cũ"]
        G --> I["Thứ hạng đổi ở<br/>lần cập nhật sau"]
    end
    B -.->|"nguồn dữ liệu"| F
```

*Hai nhịp chạy song song: mọi thứ học viên tự làm thì ghi nhận tức thì, riêng bảng xếp hạng tính nền 8 tiếng một lần.*

| # | Luồng | Cách chạy | Nhịp |
|---|---|---|---|
| 1 | **Cộng điểm khi hoàn thành hoạt động / khoá / bài Test** | Trong luồng | Tức thì |
| 2 | **Ghi nhận ngày có mặt (check-in)** | Trong luồng, **lần đầu trong ngày** học viên vào hệ thống | Tức thì |
| 3 | **Xét huy hiệu và xét hạng** | Sau khi cộng điểm, cùng luồng | Tức thì |
| 4 | **Tính bảng xếp hạng** | Tác vụ nền, **tính sẵn theo chu kỳ**, hiển thị nhãn *"cập nhật lúc HH:mm"*. Gồm cả campaign đang chạy | Theo chu kỳ |
| 5 | **Đóng băng campaign** | Tác vụ riêng, chạy khi campaign kết thúc, lọc đúng biên thời gian. **Không đi theo chu kỳ hiển thị** | Một lần mỗi campaign |

> ℹ️ **Điểm hiện ngay nhưng thứ hạng đổi ở lần cập nhật tiếp theo.** Hai nhịp khác nhau — cần nói rõ trên giao diện để học viên không thắc mắc.

### Mười hai ràng buộc bắt buộc

| # | Ràng buộc |
|---|---|
| Ràng buộc `C1` — cấu hình gắn `tenant_id`, không đóng cứng trong mã | Cấu hình gắn với **tổ chức**, không đóng cứng |
| Ràng buộc `C2` — mọi danh mục mở rộng được bằng cấu hình | Mọi danh mục **mở rộng được bằng cấu hình** |
| Ràng buộc `C3` — lưu từng lần cộng điểm kèm thời điểm | Lưu **từng lần cộng điểm kèm thời điểm**, không chỉ lưu tổng |
| Ràng buộc `C4` — đổi cấu hình chỉ áp dụng từ thời điểm đổi | Đổi cấu hình điểm → **áp dụng từ thời điểm đổi**, không tính lại quá khứ |
| Ràng buộc `C5` — chống cộng trùng trong phạm vi một lượt ghi danh | Chống cộng trùng trong phạm vi **một lượt ghi danh**. Chỉ cộng điểm khi bản ghi tiến độ **chuyển trạng thái** sang hoàn thành, tính từ lúc bật |
| Ràng buộc `C6` — biên khoảng cắt theo múi giờ tổ chức | **Biên kỳ cắt theo múi giờ tổ chức**, không theo giờ máy chủ |
| Ràng buộc `C7` — một lần cộng điểm thuộc mọi khoảng ngày bao trùm nó | Một lần cộng điểm thuộc **mọi khoảng ngày bao trùm nó**, nên bảng xếp hạng luôn tính từ sổ giao dịch theo khoảng ngày |
| Ràng buộc `C8` — mọi mốc dùng để xếp hạng phải lưu thời điểm đạt | **Mọi mốc dùng để xếp hạng phải lưu thời điểm đạt** |
| Ràng buộc `C9` — biên ngày cắt theo múi giờ tổ chức | **"Ngày"** trong check-in cắt theo **múi giờ tổ chức** |
| Ràng buộc `C10` — `Test Account` bị loại khỏi toàn bộ logic gamification | **`Test Account` bị loại khỏi TOÀN BỘ logic gamification** — lọc ngay từ tầng ghi nhận, không ghi rồi lọc sau |
| Ràng buộc `C11` — kết quả campaign tính đúng theo biên thời gian | Kết quả đóng băng **lọc theo thời điểm cộng điểm hoặc thời điểm hoàn thành**, không theo thời điểm tác vụ chạy. Tác vụ đóng băng chạy trễ vẫn phải ra đúng số |
| Ràng buộc `C12` — kết quả campaign đã đóng băng giữ nguyên mãi | Học viên bị `Block` hoặc rời tổ chức **sau khi campaign kết thúc** vẫn nằm trong kết quả. Người đã bị `Block` hoặc rời tổ chức **trước lúc kết thúc** thì không có mặt |

#### `C5` nói gì

**Lượt ghi danh** là một lần học viên được thêm vào một lớp chứa khoá học. Mỗi lần thêm vào sinh ra một bản ghi mới. Trong UpLnD, **toàn bộ tiến độ học treo vào bản ghi ghi danh chứ không treo vào con người** — hệ thống lưu *"lượt ghi danh số 1 đã xong bài 3"*, không lưu *"anh A đã học bài 3"*.

`C5` gồm hai lớp chặn độc lập:

| Lớp | Nội dung | Chặn được gì |
|---|---|---|
| **Chống cộng trùng** | Mỗi nội dung chỉ trả điểm **một lần trong một lượt ghi danh**. Trả rồi thì đóng dấu, lần sau thấy dấu là bỏ qua | Học viên mở lại bài đã xong để lấy thêm điểm |
| **Chỉ bắt lúc chuyển trạng thái** | Chỉ cộng khi bản ghi tiến độ **vừa chuyển** từ chưa hoàn thành sang hoàn thành. Không nhìn trạng thái hiện tại | Nội dung đã hoàn thành **trước khi bật** tính năng tự nó không sinh điểm, nên không phải nạp sẵn dấu cho toàn bộ lịch sử học của mọi người |

Dấu sống cùng lượt ghi danh, nên **xoá học viên khỏi lớp rồi thêm lại là lượt mới**: tiến độ về `0`, học lại từ đầu, và điểm được tính lại từ đầu. Chứng chỉ thì không, vì chứng chỉ cấp theo khoá chứ không theo lượt (`BR-13.12`).

> Hệ quả cho Dev: **"số khoá hoàn thành"** dùng để xét huy hiệu, lên hạng và xếp hạng phải đếm **theo lượt hoàn thành**, không đếm từ endpoint chứng chỉ. Học hai lượt thì tính hai lượt nhưng chỉ có một chứng chỉ. Đếm trong lúc nào: xem mục Định nghĩa chỉ số ngay dưới.

### Ba rule nền

| Mã | Nội dung |
|---|---|
| `BR-TEST` | Test `Graded Assignment = Yes` → tính khi **đạt Pass Point**. `= No` → tính khi **hoàn thành**. **Quiz · Case Study · Storyline → không tính** |
| `BR-REGRADE` | Chấm lại chỉ đi một chiều không-đạt → đạt. **Điểm chốt tại lần chấm đầu tiên**, chấm lại không cộng thêm. Không cần cơ chế thu hồi |
| `BR-SKIP` | **Khoá được đánh dấu bỏ qua thì không tính là hoàn thành** *(viết tổng quát thay vì gọi tên Foundation — tránh đóng cứng logic UpBase)* |

### Định nghĩa chỉ số — viết một lần, ba chỗ dùng lại

Mỗi chỗ **tự tính** — huy hiệu và hạng đếm trọn đời, bảng xếp hạng đếm trong khoảng ngày — nhưng **cái gì được đếm thì phải thống nhất**:

| Chỉ số | Đếm cái gì |
|---|---|
| **Điểm tích luỹ** | Tổng mọi lần cộng điểm, không hết hạn |
| **Số ngày có mặt** | Số ngày riêng biệt học viên vào hệ thống, cắt theo múi giờ tổ chức |
| **Số hoạt động hoàn thành** | Bản ghi tiến độ chuyển sang hoàn thành, trong phạm vi lượt ghi danh. Đếm theo quy tắc chung bên dưới |
| **Số bài Test** | Theo `BR-TEST` |
| **Số khoá hoàn thành** | **Số lượt hoàn thành khoá**, không phải số chứng chỉ. Đếm theo quy tắc chung bên dưới. Học lại một khoá thì tính thêm một lượt (`BR-13.10`), trong khi chứng chỉ không cấp lại — hai con số này khác nhau, xem `BR-13.12`. **Không tính khoá bỏ qua** (`BR-SKIP`) |
| **Số huy hiệu** | Huy hiệu đã đạt, giữ vĩnh viễn |
| **Điểm campaign** | Điểm tích luỹ, chỉ lấy các lần cộng có **thời điểm cộng** nằm trong khoảng campaign **và** loại hành động nằm trong danh sách campaign chọn (`US19`) |
| **Số hoạt động campaign** | Số hoạt động hoàn thành, chỉ lấy các lần hoàn thành nằm trong khoảng campaign (`US19`) |

🔑 **Quy tắc chung cho mọi chỉ số đếm** *(số ngày có mặt · số hoạt động · số bài Test · số khoá)*: đếm **mọi lần xảy ra trong lúc `Gamification` bật**, **không phụ thuộc công tắc `Points` hay công tắc từng hành động** ở `US8`. Không đếm phần xảy ra trước khi bật hoặc trong thời gian tắt hẳn (`BR-14.5`).

> Lý do: nếu đếm từ sổ giao dịch điểm thì tắt `Points` hoặc tắt một hành động sẽ làm bảng `Activities`, bảng `Courses` và tiến độ huy hiệu đứng im, dù học viên vẫn học. Nếu đếm thẳng từ dữ liệu học thì lại tính cả thời gian `Gamification` tắt, trái với `BR-14.5`. Cách lấy dữ liệu do Dev quyết, miễn đúng quy tắc trên.

## Database

```mermaid
flowchart LR
    subgraph A["1 · CẤU HÌNH — vận hành đặt"]
        direction TB
        C1["Cấu hình gamification<br/>2 công tắc chung<br/>4 công tắc chức năng"]
        C2["Quy tắc cộng điểm<br/>4 hành động<br/>check-in: 3 tham số chuỗi"]
        C3["Huy hiệu<br/>4 loại x 8 mốc"]
        C4["Cấu hình hạng<br/>3 bội số + trần"]
        C5["Campaign<br/>khoảng · loại hành động"]
    end
    subgraph B["2 · GHI NHẬN — hệ thống ghi"]
        direction TB
        L2["Dấu nội dung đã tính điểm<br/>chống cộng trùng theo lượt ghi danh"]
        L3["Ngày có mặt của học viên<br/>1 người 1 ngày 1 bản ghi<br/>nguồn dựng lại chuỗi"]
        L1["Sổ giao dịch điểm<br/>từng lần cộng kèm thời điểm"]
        L4["Huy hiệu đã đạt<br/>kèm thời điểm đạt"]
    end
    subgraph C["3 · ĐỌC — màn hình đọc"]
        direction TB
        R1["Thành tích của học viên<br/>điểm - hạng hiện tại<br/>chuỗi hiện tại"]
        R2["Bảng xếp hạng tính sẵn<br/>ghi đè mỗi 8 tiếng"]
        R3["Kết quả campaign<br/>đóng băng khi kết thúc"]
    end
    TN["tenant<br/>múi giờ tổ chức<br/>dùng để cắt biên ngày"]
    A --> B
    B --> C
    TN --> B
    L2 -.->|"chặn cộng trùng"| L1
    L3 --> L1
    L1 --> L4
    L1 --> R1
    L4 --> R1
    L1 --> R2
    L1 --> R3
```

*Mười hai thực thể mới chia ba tầng. Sổ giao dịch điểm là gốc — mọi con số hiển thị đều truy được về đây.*

**12 thực thể mới.** Múi giờ tổ chức lấy theo `tenant`. Cách lưu múi giờ, kể cả có sửa bảng `tenant` hay không, do BE quyết trong technical design.

| Bảng | Mới / Sửa | Mục đích | `tenant_id` |
| --- | --- | --- | --- |
| `tenant` | **Đọc** | Lấy **múi giờ tổ chức** để cắt biên ngày và biên khoảng (`C6`, `C9`). Không có ô chọn múi giờ trên màn Gamification. Cách lưu do BE quyết | *(là bảng gốc)* |
| Cấu hình gamification | Mới | Hai công tắc chung (`Gamification` · `Visibility in UpLMS`) · **bốn công tắc chức năng** (`Points` · `Badges` · `Levels` · `Leaderboard`) · năm công tắc bảng xếp hạng | ✅ Bắt buộc |
| Quy tắc cộng điểm | Mới | Bốn hành động, mỗi hành động một công tắc và một số điểm. Riêng check-in khai bằng **ba tham số** điểm chuỗi thay vì một số (`BR-8.5a`) | ✅ Bắt buộc |
| **Sổ giao dịch điểm** | Mới | **Từng lần cộng điểm kèm nguồn và thời điểm** (`C3`). Nền của lịch sử ghi nhận, bảng xếp hạng theo khoảng ngày, tiêu chí phụ khi đồng hạng, và chỉ số *số khoá hoàn thành* | ✅ **Bắt buộc — rò rỉ ở đây hậu quả nặng nhất** |
| Dấu nội dung đã tính điểm | Mới | Chống cộng trùng trong phạm vi lượt ghi danh (`C5`) | ✅ Bắt buộc |
| Ngày có mặt của học viên | Mới | Nguồn cho điểm check-in và huy hiệu loại Check-in. Một học viên một ngày một bản ghi | ✅ Bắt buộc |
| Huy hiệu | Mới | Bốn loại, mỗi loại tám mốc. **Giá trị mốc chỉ đọc sau khi khởi tạo** (`BR-9.2`). Tên, hình, mô tả sửa được. Công tắc bật tắt từng loại | ✅ Bắt buộc |
| Huy hiệu đã đạt | Mới | Học viên nào đạt mốc nào, **kèm thời điểm đạt** (`C8`) | ✅ Bắt buộc |
| Cấu hình hạng | Mới | Ba bội số lên hạng (điểm · số khoá · số huy hiệu), mỗi cái một công tắc, cộng trần hạng. **Không có tên hạng và hình hạng** — hạng là số thứ tự tịnh tiến | ✅ Bắt buộc |
| **Thành tích của học viên** | Mới | Điểm tích luỹ · hạng hiện tại · thời điểm lên hạng gần nhất · **chuỗi hiện tại, ngày có mặt gần nhất**. Đây là bảng `US1` và `US12` đọc | ✅ Bắt buộc |
| **Bảng xếp hạng tính sẵn** | Mới | Thứ hạng cho năm khung cố định nhân các bảng, cộng hai bảng cho mỗi campaign đang chạy. **Bị ghi đè mỗi chu kỳ 8 tiếng** (`BR-6.12`) | ✅ Bắt buộc |
| Campaign | Mới | Tên · mô tả · khoảng thời gian · loại hành động được tính điểm (`US20`). **Không có số điểm riêng** | ✅ Bắt buộc |
| **Kết quả campaign đã đóng băng** | Mới | Ghi **một lần** khi campaign kết thúc, không bao giờ ghi đè (`US21`, `C11`, `C12`) | ✅ Bắt buộc |

> **Ảnh huy hiệu** dùng hạ tầng `resources` sẵn có. Tài nguyên bị xoá thì rơi về **ảnh mặc định** (`BR-1.7`). Hạng không có hình nên không dùng `resources`.

## API

Đã đối chiếu Swagger — hệ thống có **692 operation** (LMS 144 / Ops 548), **không có nhóm nào liên quan gamification**. Tiền tố `/api/v1/gamification/` không trùng với đường dẫn nào đang tồn tại.

### UpLMS — phía học viên

| Method | Endpoint | Mới / Sửa | Mục đích |
| --- | --- | --- | --- |
| GET | `/api/v1/gamification/me` | Mới | Điểm tích luỹ · hạng hiện tại · huy hiệu đã đạt — `US1` |
| GET | `/api/v1/gamification/me/point-history` | Mới | Lịch sử từng lần cộng điểm — `US3` |
| GET | `/api/v1/gamification/me/badges` | Mới | Huy hiệu đã đạt + **sắp đạt kèm phần còn thiếu** — `US4` |
| GET | `/api/v1/gamification/leaderboard` | Mới | Bảng xếp hạng theo **khung cố định hoặc campaign** và **chỉ số** được chọn — `US6` · `US19`. **Không nhận khoảng ngày tự do** (`BR-6.15`) |
| GET | `/api/v1/gamification/campaigns` | Mới | Campaign đang chạy và đã kết thúc — `US19` |
| GET | `/api/v1/gamification/leaderboard/me` | Mới | Vị trí của tôi kèm vài người liền kề — `US7` |
| GET | `/api/v1/gamification/rules` | Mới | Bảng điểm và tiêu chí lên hạng đang áp dụng, để hiện phần *cách tính điểm* và *cách lên hạng* ở `US1` |
| PUT | `/api/v1/courses/**.../progress` | **Sửa** | Endpoint hiện có. Thêm phần cộng điểm **trong luồng**, chịu `NFR-GAM-01` |
| GET | `/api/v1/courses/my-learnings` | **Sửa** | Endpoint hiện có. **Thêm field** điểm tích luỹ và hạng — chỉ thêm, không phá contract cũ |

> **Điểm check-in (`US5`) không có endpoint riêng.** Hệ thống ghi nhận ngày có mặt ở lần đầu học viên vào hệ thống trong ngày, không có thao tác nào của học viên.

### UpLMS Ops — phía vận hành

| Method | Endpoint | Mới / Sửa | Mục đích |
| --- | --- | --- | --- |
| GET, PUT | `/api/v1/gamification/settings` | Mới | Hai công tắc chung — `US14` |
| GET, PUT | `/api/v1/gamification/point-rules` | Mới | Công tắc `Points` · bốn hành động · ba tham số điểm chuỗi — `US8` |
| GET, PUT | `/api/v1/gamification/badges` | Mới | Công tắc `Badges` · bật tắt bốn loại · sửa tên, hình, mô tả từng mốc — `US9`.<br>**Không có `POST` và `DELETE`**: không tạo, không xoá huy hiệu (`BR-9.7`). **Giá trị mốc không nhận sửa** (`BR-9.2`) |
| GET, PUT | `/api/v1/gamification/levels` | Mới | Công tắc `Levels` · ba bội số lên hạng · trần hạng — `US10`.<br>**Không có `POST` và `DELETE`**: hạng là số tịnh tiến, không phải danh sách bậc để tạo |
| GET, PUT | `/api/v1/gamification/leaderboard-settings` | Mới | Công tắc `Leaderboard` · bật tắt năm bảng — `US11` |
| GET | `/api/v1/gamification/learners` | Mới | Danh sách học viên kèm hạng, theo khoảng ngày — `US12` |
| GET | `/api/v1/gamification/learners/export` | Mới | Xuất danh sách ra **Excel** theo khoảng ngày đang chọn — `US12` |
| GET, POST | `/api/v1/gamification/campaigns` | Mới | Danh sách và tạo campaign — `US20` |
| GET, PUT, DELETE | `/api/v1/gamification/campaigns/{id}` | Mới | Xem, sửa, xoá campaign — `US20`. **Sửa và xoá bị giới hạn theo trạng thái** (`BR-20.6`) |
| GET | `/api/v1/gamification/campaigns/{id}/results` | Mới | Kết quả hai bảng của campaign — `US21` |
| GET | `/api/v1/gamification/campaigns/{id}/results/export` | Mới | Xuất kết quả campaign ra **Excel** — `US21` |

> Đường dẫn của các endpoint campaign là đề xuất, Dev chốt.

## Frontend

*Technical design phía FE: lms-fe (`apps/lms-pro`, `apps/lms-test`) và ops-fe. Shape request/response, enum, mã lỗi xem `[TD-short] Gamification` của BE.*

### 1. Overview

| App | Screen / feature | US |
|---|---|---|
| lms-pro | Page `/gamification` (summary strip + leaderboard), panel How-to, Achievement history, tab Badges trong My Profile, points/level widget ở My Learning, achievement toast | US1–US7 |
| lms-test | Achievement toast | US2 |
| ops-fe | Settings page (5 block + leaderboard preview), Learners list + export, permission | US8–US12, US14, US15 |

> ⚠️ **Chưa có technical design cho campaign** (`US19` đến `US21`, thêm ngày 08/10/2026). Dev bổ sung khi có design.

Dependency mới: `socket.io-client` v4 (lms-pro, lms-test). Env mới: `NEXT_PUBLIC_GAMIFICATION_SOCKET_URL`.

---

### 2. Module structure

#### 2.1. lms-fe

```
features/gamification/src/
  api/          GamificationAPI, mappers
  hooks/        useGamificationMe, useLeaderboard, useLeaderboardMe, useAchievementHistory, useMyBadges
  components/
    summary/    SummaryStrip
    panels/     HowToDrawer, AchievementHistory
    leaderboard/ LeaderboardCard, RangeFilter, TopThreeRow, LeaderboardRow, MyPosition
    badges/     BadgeGallery, BadgeImage
    my-learning/ GamificationStat
  realtime/     useGamificationSocket, toastDeduper, AchievementToast, achievementMessages
  pages/        GamificationPage
  mocks/
libs/hooks/useGamificationVisibility.ts
libs/utils/   formatThousands, pluralize, formatInOrgTz, toDateParam
apps/lms-pro/src/app/gamification/page.tsx
```

- `realtime/` export qua entry point riêng `@lms/feature-gamification/realtime` để lms-test chỉ kéo socket + toast.
- `useGamificationVisibility` đặt ở `libs/hooks` để Sidebar (`libs/ui`) dùng được mà không import `features/*`.

#### 2.2. ops-fe

```
features/gamification/src/
  index.ts · routes.tsx · constants/
  pages/settings/   SettingsPage
  pages/learners/   LearnersPage
  components/settings/  GeneralBlock, PointsBlock, BadgesBlock, BadgeMilestoneCard,
                        LevelsBlock, LeaderboardBlock, LeaderboardPreview, SettingsFooter
  components/learners/  LearnersFilter, exportLearners
  schema/settingsSchema.ts
  utils/mapSettings.ts · utils/dependency.ts · utils/saveOrder.ts
```

> ⚠️ `SettingsFooter` và `saveOrder.ts` dựng cho nút Save chung, không còn đúng khi trang tự lưu. Xem lưu ý đầu §7.

Đăng ký `AppModule` vào `module-registry.ts` và `scripts/generate-customer.js`.

---

### 3. Routing & navigation

#### 3.1. lms-pro

| Route | Component | Guard |
|---|---|---|
| `/gamification` | `GamificationPage` | `withAuthorization([STUDENT])` + `visible` (không thì `notFound()`) |
| `/overview?tab=badges` | Tab Badges trong My Profile | `visible && badges` |

- `/gamification` phải là route folder riêng, nếu không sẽ bị dynamic route `app/[page]` match.
- Menu: thêm item `GAMIFICATION` (icon trophy) vào `MENU_OPTIONS`; filter runtime trong `libs/ui/layout/Sidebar` theo `useGamificationVisibility()` vì `showMenu` chỉ tính 1 lần lúc load.
- My Profile (`apps/lms-pro/src/app/[page]/page.tsx`): thêm tab `badges` ở `items`, `getTabContent`, `mobileOverviewItems`; sync `?tab=` với URL bằng `router.replace`.

#### 3.2. ops-fe

| Route | Page | Permission |
|---|---|---|
| `/gamification/settings` | `SettingsPage` | `gr_view_gamification_config` hoặc `gr_update_gamification_config` |
| `/gamification/learners` | `LearnersPage` | `gr_view_gamification_learners` |

- Thêm `PermissionRoute` (check permission bằng `useHasPermission`, không có quyền → `AccessDenied`) và page `AccessDenied`.
- Menu: `ID_SIDE_BAR.GAMIFICATION` + item trong `useMenuData` (2 sub-item) + case trong `filterMenuEngagement`.

---

### 4. State & data fetching

#### 4.1. lms-fe

| Query key | API | Option |
|---|---|---|
| `['gamification','me']` | `GET /gamification/me` | `staleTime` 60s, `refetchOnWindowFocus: true`, `retry: false`, `silent` |
| `['gamification','rules']` | `GET /gamification/rules` | `staleTime` 10 phút |
| `['gamification','history']` | `GET /gamification/me/point-history` | `useInfiniteQuery`, `page_size` 10 |
| `['gamification','badges']` | `GET /gamification/me/badges` | `staleTime` 0 |
| `['gamification','leaderboard', params]` | `GET /gamification/leaderboard` | `keepPreviousData`, cancel bằng `signal` |
| `['gamification','leaderboard-me', params]` | `GET /gamification/leaderboard/me` | như trên |
| `['myLearnings']` (existing) | `GET /courses/my-learnings` | đọc thêm field `gamification` |

- Mọi response đi qua mapper ở `api/mappers.ts`; component chỉ dùng model đã map.
- Mock bật bằng `NEXT_PUBLIC_GAMIFICATION_MOCK=true`.
- Logout → `removeQueries(['gamification'])`.

#### 4.2. ops-fe

| Query key (`gamificationKeys`) | API | Option |
|---|---|---|
| `settings()` | `GET /gamification/settings` | `refetchOnWindowFocus: false` |
| `pointRules()` | `GET /gamification/point-rules` | như trên |
| `badges()` | `GET /gamification/badges` | như trên |
| `levels()` | `GET /gamification/levels` | như trên |
| `leaderboardSettings()` | `GET /gamification/leaderboard-settings` | như trên |
| `preview(params)` | leaderboard endpoint phía Ops | `keepPreviousData`, cancel bằng `signal` |
| `learners(query)` | `GET /gamification/learners` | `keepPreviousData` |

- Key factory `gamificationKeys` đặt ở `libs/core/src/constants/queryKeyFactory/` theo convention của ops-fe. Query dùng `select: res => res.data`.
- **Settings page:** react-hook-form là source of truth khi đang edit. Query cache chỉ dùng để load lần đầu và nhận lại data sau save — không auto-sync cache vào form (tránh ghi đè value đang edit), nên tắt `refetchOnWindowFocus`.
- Load: 5 query song song → `mapSettings` → `reset` form khi cả 5 đã có data.
- **Mutation:** mỗi block 1 `useAppMutation` (PUT). `saveOrder.ts` chạy tuần tự bằng `await mutateAsync`. `onSuccess`: `setQueryData` key của block bằng response, `reset` field của block đó, không invalidate cả trang.
- Save thành công `point-rules` / `badges` / `levels` / `leaderboard-settings` → invalidate `preview` (tab preview theo config đã save).
- ⚠️ Hai dòng mutation ở trên viết cho nút Save chung. Trang nay tự lưu — xem lưu ý đầu §7.
- **Learners:** query state (search, sort, range, page) lấy từ URL qua `useTableFilters`. Export gọi API trực tiếp với filter + sort hiện tại, không đi qua cache.
- Permission lấy từ `useHasPermission`, không fetch thêm.

---

### 5. Realtime — achievement toast (US2, US5)

#### 5.1. Flow

1. Có token → `useGamificationSocket` connect ngay, song song với `GET /gamification/me`. `/me` 404 → `disconnect()`.
2. BE emit `gamification:achievements { items }` sau mỗi learning action / check-in đầu ngày.
3. `toastDeduper` quyết định tab nào show toast.
4. Render mỗi `items[i]` thành 1 toast, delay 150ms giữa các toast.
5. Invalidate `me`; có event badge thì thêm `badges`; panel history đang mở thì thêm `history`.

#### 5.2. Socket client

| Item | Implementation |
|---|---|
| Init | `io(URL, { transports: ['websocket'], auth: cb => cb({ token: currentToken() }) })` |
| Token expired | `connect_error` `UNAUTHORIZED` → `getAuthManager().refreshToken()` → `connect()`, retry tối đa 3 lần |
| Lifecycle | 1 socket/tab, mount ở root layout lms-pro (`client-layout.tsx`) và lms-test (`providers.tsx`); logout → `disconnect()` |
| Disconnect | socket.io tự reconnect, không replay |
| Error | Wrap `try/catch`, chỉ log |

#### 5.3. Dedupe nhiều tab (`toastDeduper`)

1. Tab hidden (`document.visibilityState !== 'visible'`) → không show.
2. Tab visible → claim `event.id` qua `BroadcastChannel('gamification-toast')`; tab claim trước thì show.
3. Lưu `id` đã show vào `sessionStorage` (200 id gần nhất).

#### 5.4. `AchievementToast`

- `toast.custom(<AchievementToast/>, { id, duration: 5000, position: 'bottom-right' })`, không đổi config `<Toaster>` global.
- Progress bar countdown màu cam ở đáy toast; `zIndex` > 1000 để nằm trên popup course completed.

| Event | Message | Icon |
|---|---|---|
| Activity | `+{points} pts for completing the unit` | star |
| Course | `+{points} pts for completing the course` | star |
| Test | `+{points} pts for passing {test}` | star |
| Check-in | `+{points} pts · {streak_day}-day streak` | star |
| Badge | `You unlocked the {badge} badge by {condition}` | badge image |
| Level up | `Level up! You've just reached Level {level}` | crown |

- `achievementMessages` build message dạng `ReactNode` (dùng chung với Achievement history); points, badge name, `Level {n}` highlight màu cam.
- Số đếm dùng `pluralize()`. Tên source `null` → `this unit` / `this test` / `this course`.

---

### 6. Learner screens

#### 6.1. `GamificationPage`

```
GamificationPage
├─ Header (title + SummaryStrip)
├─ LeaderboardCard
└─ HowToDrawer (mở từ SummaryStrip)
```

#### 6.2. `SummaryStrip` (US1)

| Cell | Display | Hover | Click |
|---|---|---|---|
| Streaks | `{n} Streaks` | `Days you've signed in without a break.` | — |
| Points | `{n} Points` | `How to collect points?` | Open `HowToDrawer` (collect) |
| Badges | `{n} Badges` | `Go to badge gallery` | `/overview?tab=badges` |
| Level | `Level {n}` | `How to level up?` | Open `HowToDrawer` (level) |

#### 6.3. `HowToDrawer` (US1, US3, US10)

`UpBaseDrawerV3` slide từ phải, state `view: 'collect' | 'level' | 'history'`. Button `Achievement History` ở footer đổi `view`, không mở drawer thứ hai.

| View | Content |
|---|---|
| collect | Check-in: `{base}-{cap} pts` · `for visiting UpLMS each day, +{step} for each day in a row, up to {cap}`; 3 row `{n} pts` · `for each activity / course / successful test completion` |
| level | Progress bar tới level kế tiếp (ẩn khi đạt max level) + 3 row `Every {n} points` / `Every {n} completed courses` / `Every {n} badges` |
| history | `AchievementHistory` |

Chỉ render item BE trả về. Label điểm dạng pill, background cam nhạt.

#### 6.4. `AchievementHistory` (US3)

- `useInfiniteQuery`, load more khi item cuối vào viewport (IntersectionObserver).
- Mỗi item: timestamp `DD/MM/YYYY HH:mm` (`formatInOrgTz`), message từ `achievementMessages`, divider.
- Tên dài truncate 60 ký tự + tooltip.
- Empty state: `Nothing here yet. Start learning to earn your first points.`

| Event | Message (**bold**) |
|---|---|
| Check-in ngày đầu | You earned **{n} points** for checking in today. |
| Check-in đang giữ streak | You earned **{n} points** for checking in today. Day {d} of your streak. |
| Activity | You earned **{n} points** for completing **{activity}** in **{course}**. |
| Course | You earned **{n} points** for completing the course **{course}**. |
| Test | You earned **{n} points** for passing **{test}** in **{course}**. |
| Badge | You unlocked the **{badge}** badge for reaching {milestone} {unit}. |
| Level up | You reached **Level {n}**. |

#### 6.5. `LeaderboardCard` (US6, US7)

> ⚠️ **Dev cập nhật lại theo thay đổi ngày 08/10/2026** (`CR-012`, `CR-013`). Những gì PO đã chốt, Dev quyết cách làm:
> - **Bỏ bộ chọn khoảng ngày tự do.** Chỉ còn năm khung `All time` · `This week` · `This month` · `This quarter` · `This year` (`BR-6.15`). Các dòng về `custom range`, `disabledDate`, skeleton khi tính khoảng tự chọn không còn đúng
> - **Năm tab:** `Points` · `Activities` · `Courses` · `Level` · `Badges`. **`Level` và `Badges` chỉ có ở `All time`** (`BR-6.2b`)
> - **Thêm lối vào campaign** cạnh các khung cố định (`US19`)

```
LeaderboardCard
├─ Tabs (Points · Badges · Levels · Courses — theo metric BE trả)
├─ RangeFilter (RangePicker + 5 preset trong dropdown)
├─ TopThreeRow ×3 + LeaderboardRow ×n
├─ "Show All" divider
├─ MyPosition
└─ LastUpdated / Empty / Error
```

**State** — sync với URL: `?board=points&range=this_month` hoặc `&range=custom&from=YYYY-MM-DD&to=YYYY-MM-DD`. Mặc định `board=points`, `range=all_time`.

| Behavior | Implementation |
|---|---|
| Chọn preset | Gửi range code, không tự tính from/to |
| Chọn custom range | Gọi API khi chọn đủ 2 ngày; `disabledDate`: sau hôm nay hoặc trước ngày enable feature |
| Đổi range khi đang ở tab `Levels` / tab bị disable | Fallback về tab enable đầu tiên |
| Default | Top 5 (`page_size` 5) → `Show All` → `MyPosition` |
| Click `Show All` | `useInfiniteQuery` 20 row/page; `MyPosition` sticky bottom |
| User trong top 5 | Không render `MyPosition` |
| Custom range đang loading | Skeleton |

**Row display:** top 3 dùng medal icon + gradient background gold/silver/bronze; rank ≥ 4 `String(rank).padStart(2,'0')`; `rank = null` để trống; row của user hiện tên `You`; value dùng `formatThousands`.

**Label:** `Last updated {HH:mm}` cho preset; empty state `No one has earned points in this period yet.`

**`MyPosition`:** row của user + `neighbors`, dòng gap `{value} {unit} behind {name}`; chưa có metric → rank trống + hint text.

#### 6.6. `BadgeGallery` (US4)

- Group theo badge type: header `{Type} Badges ({achieved}/{total})`, grid 5 cột (mobile: collapse).
- Badge chưa đạt: `grayscale` + `opacity`; hover border cam + `{milestone} {unit}`.
- `BadgeImage`: `onError` → default image.

#### 6.7. `GamificationStat` — My Learning (US1)

`{points} Points · Level {n}` trong `MyLearningHeader`, click navigate tới `/gamification`. Field `gamification` `null` → không render; `points` / `level` `null` → ẩn value đó.

---

### 7. Ops — settings page (US8–US11, US14)

> ⚠️ **Dev cập nhật lại theo thay đổi ngày 06/10/2026: trang tự lưu, không có nút Save** (`BR-14.10` đến `BR-14.13`). Các phần dựng trên nút Save chung không còn đúng: `SettingsFooter` và `saveOrder.ts` ở §2.2 · mutation tuần tự ở §4.2 · toàn bộ §7.4 · dòng `Save to update preview` ở §7.5.
>
> PO chỉ chốt hành vi, cách lưu do Dev quyết. Hai điều phải đúng:
> 1. Lưu dồn dập trên cùng một khối **không được để lần lưu trước ghi đè lên lần lưu sau**.
> 2. Lưu một ô **không được kéo theo giá trị đang lỗi của ô khác** trong cùng khối.

#### 7.1. Form

Một form react-hook-form + zod cho cả page, mỗi block 1 component.

| Block | Field |
|---|---|
| `GeneralBlock` | `gamification` · `visibility` |
| `PointsBlock` | switch block · 4 action `{ enabled, points }` · step/cap check-in (read-only) |
| `BadgesBlock` | switch block · 4 badge type `{ enabled, badges[{ id, name, description, image_resource_id }] }` |
| `LevelsBlock` | switch block · `cap_enabled`, `cap` · 3 criteria `{ enabled, multiple }` |
| `LeaderboardBlock` | switch block · 4 board `{ enabled }` · `LeaderboardPreview` |

- Disable `gamification` → chỉ render `GeneralBlock` (ẩn `visibility`).
- `HookFormSwitch` (`@ops/ui`) thêm prop `disabled`.
- Badge name edit inline; click image → `ModalUploadFile` (`fileType='IMAGE'`, `maxCount=1`, location `GAMIFICATION`), lưu `image_resource_id`.

#### 7.2. Validation (`settingsSchema`)

| Field | Rule |
|---|---|
| Points mỗi action | Integer ≥ 1, **không giới hạn trên**, required khi enable |
| Multiple mỗi criteria | Integer ≥ 1, required khi enable |
| `cap` | Integer ≥ 2, required khi `cap_enabled` |
| Badge name | Cho phép empty (BE lưu default name) |
| Levels enable | Không tắt được criteria **đang chạy** cuối cùng (enable và không bị lock), theo `BR-10.8` |
| Leaderboard enable | Không tắt được board **đang chạy** cuối cùng, theo `BR-11.5` |

Field của item đang disable thì skip validate, giữ value.

#### 7.3. Cross-field dependency (`dependency.ts`)

| Khi disable | Disable / lock |
|---|---|
| Points | 4 action · criteria `Points` · `Show points` |
| Badges | 4 badge type · criteria `Badges` · `Show badges` |
| Levels | criteria + `cap` · `Show levels` |
| Leaderboard | 4 switch board |

- Khi load: lock theo `locked_reason` BE trả. Khi edit: tính bằng `dependency.ts` từ `useWatch`.
- Lock = disabled + helper text; không đổi value.

**Popover xác nhận** gắn cạnh switch, không phải modal. Chỉ có hai trường hợp, theo `BR-14.13`. Huỷ thì switch về như cũ, không lưu:

| Trigger | Content |
|---|---|
| Disable `Gamification` | Ngừng ghi nhận, dữ liệu giữ nguyên, bật lại không tính bù |
| Enable `Visibility` lần đầu | Học viên thấy ngay số đã tích, không có thông báo hồi tố |

- Disable `Points` hoặc `Badges` khi criteria tương ứng đang enable: **không hỏi lại**, hệ quả nêu bằng helper text dưới switch (`BR-10.7`).
- Levels hoặc Leaderboard không còn item nào đang chạy vì bị lock → hiện cảnh báo cố định trong block (`BR-10.8`, `BR-11.5`).

#### 7.4. Load & Save

- Load: 5 GET song song → `mapSettings` → `reset` → baseline `useFormDirtyGuard`.
- Save: validate → PUT các block dirty, mỗi PUT gửi full block, `reset` block đó từ response.
- Save order (`saveOrder.ts`):

| Case | PUT order |
|---|---|
| Enable Gamification | `settings` → block con |
| Disable Gamification | Chỉ `settings` |
| Không đổi Gamification | `point-rules → badges → levels → leaderboard-settings → settings` |

- PUT fail → stop, giữ form state các block chưa save.
- Save disabled khi `!isDirty || isSubmitting || !canEdit`; rời page khi dirty → confirm leave.

#### 7.5. `LeaderboardPreview`

> ⚠️ **Dev cập nhật lại theo thay đổi ngày 08/10/2026:** preview đi theo phía học viên — **chỉ năm khung cố định, không có `RangePicker`**, năm tab với `Level` và `Badges` chỉ ở `All time`. Thêm công tắc `Show activities` vào `LeaderboardBlock` (`US11`).

- Tab + RangePicker + top + `Show All`, read-only, không có `MyPosition`.
- Gọi leaderboard endpoint phía Ops; tab theo config **đã save**. Có thay đổi chưa save ở `Show …` → hiện `Save to update preview`.
- Gamification hoặc Leaderboard disable → không render.

---

### 8. Feature visibility (lms-pro)

`useGamificationBootstrap()` gọi `useGamificationMe` khi mount app (chỉ `STUDENT`). `useGamificationVisibility()` trả về:

```ts
{ ready: boolean; visible: boolean; points: boolean; badges: boolean; levels: boolean; leaderboard: boolean }
```

| `/me` | Kết quả |
|---|---|
| 200 | `visible = true`, từng flag theo `features` |
| 404 | `visible = false` (disabled / hidden / Test Account) — thêm error code vào `toastExceptions` |
| Error khác / loading | `visible = false` |

| Component | Render khi |
|---|---|
| Menu, route `/gamification`, widget My Learning, socket | `visible` |
| Cell Streaks, cell Points, panel collect | `visible && points` |
| Cell Badges, tab Badges | `visible && badges` |
| Cell Level, panel level | `visible && levels` |
| Leaderboard card | `visible && leaderboard` |

Các API learner khác trả 404 → invalidate `me`.

---

# Unit — nhóm bàn giao

Mười tám US chia thành bảy nhóm. Mỗi nhóm phục vụ một cơ chế và release được độc lập, trừ phần phụ thuộc ghi ở cột bên.

| Unit | Gồm US | Phụ thuộc | Release độc lập? |
|---|---|---|---|
| **Nền tảng** | `US14` phân quyền và hai công tắc · `US15` phân quyền cấu hình | — | ❌ Chạm mọi Unit khác. Phải xong trước tiên |
| **Điểm** | `US5` điểm check-in theo chuỗi · `US8` cấu hình điểm · `US13` điểm phản ánh việc học thật | Nền tảng | ✅ Là nguồn dữ liệu cho mọi thứ còn lại |
| **Huy hiệu** | `US4` huy hiệu sắp đạt · `US9` cấu hình huy hiệu | Điểm | ✅ Cần chỉ số đếm từ Unit Điểm |
| **Hạng** | `US10` cấu hình hạng | Điểm · Huy hiệu | ✅ Ba tiêu chí lên hạng lấy từ hai Unit kia |
| **Hiển thị cho học viên** | `US1` màn Gamification · `US2` thông báo · `US3` lịch sử ghi nhận | Điểm | ✅ Hiện được ngay khi có điểm, huy hiệu và hạng bổ sung sau |
| **Bảng xếp hạng** | `US6` bảng xếp hạng · `US7` vị trí của tôi · `US11` cấu hình bảng · `US12` danh sách học viên bên Ops | Điểm | ✅ Bảng theo hạng chỉ chạy được sau Unit Hạng, bảng theo huy hiệu sau Unit Huy hiệu. Ba bảng còn lại không cần |
| **Campaign** | `US19` campaign phía học viên · `US20` tạo và quản lý campaign · `US21` kết quả campaign | Điểm · Bảng xếp hạng | ✅ Dùng lại cơ chế tính sẵn của Unit Bảng xếp hạng |

**Thứ tự đề xuất:** Nền tảng → Điểm → Hiển thị cho học viên → Huy hiệu → Hạng → Bảng xếp hạng → Campaign

Lý do xếp `Hiển thị cho học viên` lên trước `Huy hiệu`: ngay khi Unit Điểm chạy, học viên đã thấy được điểm và lịch sử. Đó là phần thưởng sớm nhất cho người học, và cũng là cách kiểm chứng cơ chế điểm chạy đúng trước khi xây tiếp.

> Đây chỉ là đề xuất. Thứ tự thật do Dev chốt theo năng lực đội và ràng buộc kỹ thuật.

---

# Specific Requirement

> **Quy ước đánh số:**
> - User Story: `US1`, `US2`… liên tục
> - Business rule: `BR-<số US>.<số thứ tự>` → `BR-1.1`, `BR-2.1`… unique toàn PRD
> - US chưa làm → ghi rõ trong tiêu đề

## Danh sách US

### Phía học viên (UpLMS) — 8 US

| ID | User Story | Nguồn |
| --- | --- | --- |
| **US1** | Là học viên, tôi cần xem điểm, hạng và huy hiệu đã đạt để biết nỗ lực học của mình được ghi nhận tới đâu | Giải quyết mục tiêu `O2` — nỗ lực học được ghi nhận ngay lúc nó xảy ra |
| **US2** | Là học viên, tôi cần được báo ngay khi nhận điểm, đạt huy hiệu hoặc lên hạng, trong lúc đang dùng hệ thống | Giải quyết mục tiêu `O2` — nỗ lực học được ghi nhận ngay lúc nó xảy ra |
| **US3** | Là học viên, tôi cần tra được từng lần cộng điểm đến từ đâu để tin vào con số của mình | Giải quyết mục tiêu `O5` — điểm số đáng tin, mỗi con số truy được nguồn.<br>Dựa trên ràng buộc `C3` — lưu từng lần cộng điểm kèm thời điểm |
| **US4** | Là học viên, tôi cần biết huy hiệu nào sắp đạt và còn thiếu gì để có mục tiêu ngắn hạn | Giải quyết mục tiêu `O3` — học viên có mốc ngắn hạn để nhắm tới |
| **US5** | Là học viên, tôi cần việc vào hệ thống mỗi ngày được ghi nhận thành điểm để có lý do mở ứng dụng hằng ngày | Giải quyết mục tiêu `O1` — học viên quay lại học đều đặn mà không cần nhắc thủ công.<br>**Nhắm thẳng vào Activation 40.2%**, chỉ số yếu nhất trong mục `Analytics` |
| **US6** | Là học viên, tôi cần xem bảng xếp hạng theo khung thời gian cố định để biết mình đứng ở đâu so với người khác | Yêu cầu bổ sung ở change request `CR-001` — đưa bảng xếp hạng vào phạm vi đợt này. Khung cố định thay bộ chọn tự do ở `CR-013` |
| **US7** | Là học viên, tôi cần luôn thấy vị trí của chính mình kèm vài người liền kề, kể cả khi không ở nhóm đầu | Yêu cầu bổ sung ở change request `CR-001`.<br>Là cơ chế giảm nhẹ chính cho bảng xếp hạng toàn tổ chức: người hạng thấp vẫn thấy được mình |
| **US19** | Là học viên, tôi cần xem các campaign đang chạy và đã kết thúc trong trang bảng xếp hạng, để biết mình đứng đâu trong một đợt thi đua và xem lại kết quả đợt đã qua | Giải quyết mục tiêu `O4` — kết quả công bố được. Thêm ở change request `CR-013` |

### Phía vận hành (UpLMS Ops) — 10 US

> Cấu hình nằm trên **một trang duy nhất trong Ops, chia bốn khối, mỗi khối một chức năng có công tắc riêng**: Points · Badges · Levels · Leaderboard. `US8` đến `US11` mô tả bốn khối đó.
>
> `CR-008` ban đầu chốt tách bốn màn. Design chốt ngày 01/10 gộp lại một trang vì lượng cấu hình ít, bắt vận hành nhảy bốn màn thì bất tiện hơn.

| ID | User Story | Nguồn |
| --- | --- | --- |
| **US8** | Là nhân sự vận hành, tôi cần bật/tắt cơ chế điểm và khai mỗi hành động được bao nhiêu điểm, để điều chỉnh theo mục tiêu từng giai đoạn | Nền của mọi cơ chế còn lại. Không khai được điểm thì không có gì để xếp hạng |
| **US9** | Là nhân sự vận hành, tôi cần bật/tắt từng loại huy hiệu và **đặt tên cùng hình cho từng mốc**, để bộ huy hiệu mang ngôn ngữ của tổ chức mình | Đã chốt ở change request `CR-008` — mốc do hệ thống định sẵn, vận hành chỉ đặt tên và hình |
| **US10** | Là nhân sự vận hành, tôi cần đặt mỗi bao nhiêu điểm, bao nhiêu khoá, bao nhiêu huy hiệu thì học viên lên một hạng, và đặt trần hạng | Đã chốt ở change request `CR-008` — hạng là số thứ tự tịnh tiến, không có tên và hình |
| **US11** | Là nhân sự vận hành, tôi cần chọn bảng xếp hạng hiện những cột nào, để kiểm soát học viên nhìn thấy gì về nhau | Đã chốt ở change request `CR-008` — mỗi chỉ số một bảng riêng, bật tắt độc lập |
| **US12** | Là nhân sự vận hành, tôi cần xem danh sách học viên kèm hạng của họ, để nắm tình hình chung | Đã chốt ở change request `CR-008` — vận hành cần tra cứu hạng của từng người |
| **US13** | Là nhân sự vận hành, tôi cần điểm phản ánh việc học thật, không bị đẩy lên bằng thao tác đối phó | Giải quyết mục tiêu `O5` — điểm không bị thổi lên bằng thao tác đối phó |
| **US14** | Là nhân sự vận hành, tôi cần bật/tắt gamification và bật/tắt hiển thị phía học viên riêng biệt, để chạy thử cơ chế trước khi mở | Cần giai đoạn chạy ngầm để thử cơ chế trước khi mở cho học viên |
| **US15** | Là quản trị, tôi cần phân quyền để chỉ vai trò vận hành phù hợp mới sửa được cấu hình gamification | `[suy ra]` — không có trong yêu cầu gốc, nhưng mọi cấu hình đều cần kiểm soát ai sửa được |
| **US20** | Là nhân sự vận hành, tôi cần tạo campaign có thời hạn riêng và chọn loại hành động được tính điểm, để tổ chức phong trào học tập theo mục tiêu từng đợt | Thêm ở change request `CR-013` |
| **US21** | Là nhân sự vận hành, tôi cần xem và xuất kết quả của từng campaign, để đội truyền thông công bố và trao thưởng | Giải quyết mục tiêu `O4`. Thêm ở change request `CR-013` |

### Chưa làm trong phạm vi này — 3 US

| ID | User Story | Chờ gì |
| --- | --- | --- |
| **US16** | *Bộ lọc bảng xếp hạng theo nhóm* — **chưa làm** | Chức năng nhóm đồng bộ từ HRM. **Là công cụ duy nhất phục vụ Quản lý trực tiếp** |
| **US17** | *Tính điểm và huy hiệu từ Quiz, Case Study, Storyline* — **chưa làm** | PO chốt không tính ở đợt này |
| **US18** | *Điểm cho lộ trình · huy hiệu theo kỹ năng* — **chưa làm** | Tính năng Lộ trình và Khung năng lực |

> **Danh sách gồm 21 US, trong đó 18 US làm ở đợt này.**
>
> **Hai cách xem thời gian.** Bảng xếp hạng chung dùng **khung cố định**, là số liệu sống. Muốn một đợt thi đua có chủ đích, có kết quả không đổi để trao thưởng, thì dùng **campaign** (`US19` đến `US21`). Học viên không có bộ chọn khoảng ngày tự do.

---

## US1: Trang Thành tích của tôi

### 1/ User story

Là học viên, tôi cần xem điểm, hạng và huy hiệu đã đạt của mình để biết nỗ lực học được ghi nhận tới đâu.

### 2/ Pre - Condition

| Điều kiện | Nguồn |
|---|---|
| `Gamification` đang bật và `Visibility in UpLMS` đang bật ở cấp tổ chức | Hai công tắc `Gamification` và `Visibility in UpLMS`, cấu hình ở `US14` |
| Học viên đăng nhập được vào UpLMS | KB `06` |
| Tài khoản không phải `Test Account` | Ràng buộc `C10` — `Test Account` bị loại khỏi toàn bộ logic gamification.<br>Chi tiết ở KB `06-user-account.md` quy tắc `KB-USER-TA-01` |
| Vận hành đã tạo ít nhất một hạng. Chưa có hạng nào thì khối hạng không hiện | `US11` |

### 3/ Scenario

Học viên vào UpLMS, mở trang Thành tích của tôi từ menu chính hoặc từ màn My Learning. Trang hiện ba khối theo thứ tự: điểm tích luỹ, hạng hiện tại kèm tiến độ tới hạng kế tiếp, và danh sách huy hiệu đã đạt.

Học viên chưa có điểm nào vẫn vào được trang. Lúc đó điểm hiện 0, hạng là hạng thấp nhất, phần huy hiệu hiện trạng thái rỗng.

### 4/ Acceptance criteria

**UI / UX / Rule UX / Rule UI**

| Màn hình | Giao diện | Field | Yêu cầu |
|---|---|---|---|
| Thành tích của tôi | Điểm vào trang | Mục menu | Hiện ở menu chính của UpLMS. `Visibility in UpLMS` tắt thì mục menu biến mất, và mở thẳng đường dẫn trả về không tìm thấy |
| Thành tích của tôi | Điểm vào trang | Lối tắt ở My Learning | Từ khối điểm và hạng trên My Learning, bấm vào mở sang trang này. Xem `US5` cho chi tiết khối đó |
| Thành tích của tôi | Khối tổng quan | Điểm tích luỹ | Số nguyên, phân cách hàng nghìn bằng dấu chấm. Giá trị nhỏ nhất 0, không có số âm. Không kèm đơn vị sau số. Chưa có điểm thì hiện `0`, không hiện trạng thái rỗng |
| Thành tích của tôi | Khối tổng quan | Hạng hiện tại | **Một con số thứ tự tịnh tiến**, bắt đầu từ `1`. **Không có tên hạng, không có hình hạng.** Học viên mới vào hệ thống ở hạng `1` |
| Thành tích của tôi | Khối tổng quan | Tiến độ tới hạng kế tiếp | Thanh tiến độ kèm dòng nêu phần còn thiếu của **tiêu chí sắp chạm mốc nhất**. Chạm **trần hạng** rồi thì ẩn cả khối, không hiện thanh đầy |
| Gamification | Dải tóm tắt | `{n} Streaks` | **Chuỗi hiện tại** — số ngày vào hệ thống liên tiếp đang giữ. Chưa vào ngày nào thì hiện `0`. Cách tính ở `US5` |
| Gamification | Dải tóm tắt | Chuỗi dài nhất | **Không hiện.** Chỉ số quá khứ không giúp học viên quyết định gì hôm nay |
| Gamification | Dải tóm tắt | Khi `Points` tắt | Ẩn ô chuỗi. Không còn điểm thì chuỗi mất ý nghĩa |
| Thành tích của tôi | Cách lên hạng | Rule chung | Ngoài tiêu chí gần nhất, hiện **đầy đủ các tiêu chí lên hạng đang chạy** kèm bội số của từng cái. Ví dụ: `Every 3,000 points` · `Every 5 completed courses` · `Every 5 badges`. Tiêu chí đang tắt, hoặc đang bị khoá vì chức năng nguồn tắt (`BR-10.7`), thì không hiện |
| Thành tích của tôi | Cách tính điểm | Rule chung | Hiện **bảng điểm đang áp dụng**: mỗi hành động đang bật được bao nhiêu điểm. Ví dụ: `Activity completion: 25` · `Course completion: 150` · `Successful test: 50`. Hành động đang tắt thì không hiện |
| Gamification | Panel `How to collect points?` | Dòng check-in | Nhãn `10–40 pts`, mô tả `for visiting UpLMS each day, +5 for each day in a row, up to 40`. Hiện khoảng thay vì một số vì điểm thay đổi theo chuỗi.<br>**Không dùng chữ `login` hay `sign-in`**: học viên đang còn phiên đăng nhập từ hôm trước, mở UpLMS là được tính, không phải đăng xuất rồi đăng nhập lại. Cũng không dùng `check in` ở câu này, vì dễ hiểu thành phải bấm một nút (`BR-5.2`) |
| Gamification | Dải tóm tắt | `{n} Badges` | **Chỉ hiện số lượng huy hiệu đã đạt.** Danh sách đầy đủ nằm ở màn khác, xem `US4` |

**Bốn ô tóm tắt — trỏ vào và bấm**

| Ô | Hiện gì | Trỏ chuột vào | Bấm vào |
|---|---|---|---|
| **Chuỗi** | `5 Streaks` | Tooltip `Days you've signed in without a break.` | Không có hành động. Ô này chỉ để xem |
| **Điểm** | `475 Points` | Gợi ý `How to collect points?` | Mở panel `How to collect points?` trượt từ phải |
| **Huy hiệu** | `3 Badges` | Gợi ý `Go to badge gallery` | **Chuyển màn** sang `My Profile` → tab `Badges` (`US4`) |
| **Hạng** | `Level 1` | Gợi ý `How to level up?` | Mở panel `How to level up?` trượt từ phải |

**Hai panel mở ra từ dải tóm tắt**

| Màn hình | Giao diện | Field | Yêu cầu |
|---|---|---|---|
| Gamification | Panel `How to collect points?` | Bố cục | Trượt từ cạnh phải. Mỗi dòng gồm nhãn điểm bên trái và mô tả hành động bên phải |
| Gamification | Panel `How to collect points?` | Ba dòng còn lại | `for each activity completion` · `for each course completion` · `for each successful test completion`. Số điểm lấy từ cấu hình đang áp dụng |
| Gamification | Panel `How to collect points?` | Hành động đang tắt | Không hiện dòng tương ứng |
| Gamification | Panel `How to level up?` | Nội dung | Các tiêu chí đang chạy, **mỗi dòng mở đầu bằng `Every`**: `Every 3,000 points` · `Every 5 completed courses` · `Every 5 badges`. Thiếu chữ `Every` thì học viên hiểu thành đạt mốc đó một lần là lên hạng, trong khi mỗi lần chạm thêm một mốc đều cho một hạng (`BR-10.2`) |
| Gamification | Panel `How to level up?` | Tiêu chí đang tắt hoặc bị khoá | Không hiện dòng tương ứng. Bị khoá là khi `Points` hoặc `Badges` tắt, theo `BR-10.7` |
| Gamification | Cả hai panel | Đóng | Nút `✕` ở góc phải tiêu đề |

**Business requirement — Business rule**

- `BR-1.1` Trang chỉ tồn tại khi `Gamification` bật **và** `Visibility in UpLMS` bật. Tắt một trong hai thì trang không truy cập được bằng bất kỳ đường nào.
- `BR-1.2` Điểm hiển thị là **điểm tích luỹ** của cá nhân tính từ lúc vào hệ thống, không phải điểm theo kỳ.
- `BR-1.3` **Hạng chỉ lên, không tụt.** Vận hành đổi ngưỡng hạng thì cấu hình mới **chỉ áp từ thời điểm đổi trở đi**. Học viên đang ở một hạng **giữ nguyên hạng đó**, kể cả khi không còn đủ ngưỡng mới. Theo `C4`.
  > Riêng điểm tích luỹ không bao giờ giảm, nên hạng chỉ xét theo điểm thì thực tế không tụt trừ khi vận hành đổi ngưỡng.
- `BR-1.4` **Huy hiệu đã nhận không bị lấy lại bởi việc đổi cấu hình.** Mốc của một huy hiệu **khoá ngay sau khi tạo**, và **không có thao tác xoá huy hiệu**. Nên không có cách nào để vận hành làm học viên mất một huy hiệu đã đạt.
- `BR-1.4a` Huy hiệu **không còn hiện** trong đúng hai trường hợp:
  | Trường hợp | Dữ liệu |
  |---|---|
  | Vận hành **tắt chức năng huy hiệu**, hoặc **tắt rule của riêng huy hiệu đó** | Giữ nguyên. Bật lại thì hiện lại đầy đủ |
  | Học viên **rời tổ chức** | Theo vòng đời tài khoản, không phải cơ chế của gamification |
- `BR-1.5` Tài khoản có `Test Account = Yes` không phát sinh dữ liệu gamification nên không vào được trang này. Theo `KB-USER-TA-01`.
- `BR-1.6` Điểm là số nguyên.
- `BR-1.7` Ảnh huy hiệu lấy từ kho tài nguyên dùng chung. Tài nguyên bị xoá thì rơi về ảnh mặc định, huy hiệu của học viên không mất.

**Data Field**

| Field | Kiểu | Bắt buộc | Giá trị hợp lệ | Ghi chú |
|---|---|---|---|---|
| Điểm tích luỹ | Số nguyên | Có | `>= 0` | Mới. Đọc từ bảng điểm của học viên |
| Hạng hiện tại | Khoá ngoại tới bảng Hạng | Không | Rỗng khi chưa có hạng nào được tạo | Mới |
| Thời điểm lên hạng | Thời gian | Không | | Mới. Cần cho `C8` |
| Huy hiệu đã đạt | Danh sách | Không | | Mới. Mỗi dòng gồm mã huy hiệu và **thời điểm đạt** (`C8`) |

> Trang này **chỉ đọc**. Không có field nào học viên sửa được.

**NFR**

Trang đọc giá trị đã lưu sẵn. Không tính lại điểm hay xét lại hạng khi mở trang.

### 5/ Out of scope

| Không làm ở US này | Thuộc về |
|---|---|
| Hiển thị điểm theo khoảng ngày | `US6` |
| Hiển thị huy hiệu **chưa đạt** và phần còn thiếu | `US4` |
| Hiển thị lịch sử từng lần cộng điểm | `US3` |
| So sánh thứ hạng với học viên khác | `US6`, `US7` |
| Cho học viên đổi ảnh huy hiệu, tên hạng, hay bất kỳ cấu hình nào | `US10`, `US11` |

### 6/ Conner case

*(QA điền)*

---

## US2: Thông báo thành tích

### 1/ User story

Là học viên, tôi cần được báo ngay khi nhận điểm, đạt huy hiệu hoặc lên hạng, trong lúc đang dùng hệ thống, để cảm nhận được sự ghi nhận đúng lúc nó xảy ra.

### 2/ Pre - Condition

| Điều kiện | Nguồn |
|---|---|
| `Gamification` bật và `Visibility in UpLMS` bật | Hai công tắc `Gamification` và `Visibility in UpLMS`, cấu hình ở `US14` |
| Học viên **đang mở UpLMS** tại thời điểm thành tích phát sinh | Bảng xếp hạng tính sẵn theo chu kỳ 8 tiếng, xem `BR-6.12` |
| Tài khoản không phải `Test Account` | Ràng buộc `C10` — `Test Account` bị loại khỏi toàn bộ logic gamification |
| Vận hành đã khai ít nhất một hành động tính điểm | `US9` |

### 3/ Scenario

Học viên hoàn thành một hoạt động học. Điểm được cộng ngay trong chính thao tác đó, và thông báo hiện lên trong lúc học viên vẫn đang ở trong hệ thống.

Nếu lần cộng điểm này đủ ngưỡng một huy hiệu, huy hiệu được trao và báo kèm. Nếu đủ ngưỡng hạng kế tiếp, học viên lên hạng và nhận thông báo nổi bật hơn.

Học viên không ở trong hệ thống thì không nhận thông báo nào. Thành tích vẫn được ghi, tra lại được ở lịch sử điểm (`US3`) và trang thành tích (`US1`).

> Trường hợp offline hay gặp nhất là **bài kiểm tra chấm tay**. Mentor chấm xong sau vài ngày, điểm được cộng lúc đó, học viên thường không đang online.

### 4/ Acceptance criteria

**UI / UX / Rule UX / Rule UI**

| Màn hình | Giao diện | Field | Yêu cầu |
|---|---|---|---|
| Mọi màn UpLMS | Thông báo nhận điểm | Nội dung | Một dòng, tiếng Anh, theo mẫu `+ {điểm} for {mô tả hành động}`.<br>Ví dụ: `+ 25 for completing the unit` · `+ 150 for completing the course` |
| Mọi màn UpLMS | Thông báo đạt huy hiệu | Nội dung | Hai dòng, tiếng Anh. Dòng đầu `Congratulations!` in đậm. Dòng sau theo mẫu `You unlocked the {tên huy hiệu} badge by {mô tả điều kiện}`.<br>Ví dụ: `You unlocked the Learning Newbie badge by completing 1 course` |
| Mọi màn UpLMS | Thông báo lên hạng | Nội dung | Cùng dạng hai dòng như huy hiệu, thay tên huy hiệu bằng tên hạng. Câu chữ chính xác: `❓BA` |
| Mọi màn UpLMS | Biểu tượng | Thông báo điểm | Một biểu tượng chung cho mọi thông báo điểm |
| Mọi màn UpLMS | Biểu tượng | Thông báo huy hiệu | Hình của chính huy hiệu vừa đạt |
| Mọi màn UpLMS | Nhiều thông báo cùng lúc | Cách hiển thị | **Không gộp.** Mỗi thành tích là một thẻ riêng, xếp chồng theo đúng thứ tự phát sinh. Một thao tác sinh ra bốn thành tích thì hiện bốn thẻ |
| Mọi màn UpLMS | Danh từ trong câu | Số ít và số nhiều | Câu phải đúng ngữ pháp theo số lượng: `1 course` chứ không phải `1 courses`. Áp cho mọi mẫu câu có số đếm |
| Mọi màn UpLMS | Vị trí và hướng xếp chồng | | `❓BA` — chờ Figma |
| Mọi màn UpLMS | Thời gian tự tắt | | `❓BA` — chờ Figma. Cần tính tới trường hợp bốn năm thẻ xuất hiện cùng lúc |
| Mọi màn UpLMS | Khi `Visibility in UpLMS` tắt | | Không đẩy thông báo nào, kể cả khi điểm vẫn đang được ghi ngầm |

**Business requirement — Business rule**

- `BR-2.1` Thông báo chỉ đẩy khi học viên **đang mở UpLMS**. Học viên không online thì **không gửi và không xếp hàng chờ gửi sau**.
- `BR-2.2` Không gửi email cho bất kỳ thông báo thành tích nào. Gamification không chạm vào 30 mail event hiện có.
- `BR-2.3` Không dùng cơ chế Notification hiện có của Ops. Cơ chế đó là soạn tay gửi theo nhóm, gửi theo job nửa tiếng (`KB-NOTI-05`), không phù hợp với thông báo theo từng người.
- `BR-2.4` `Visibility in UpLMS` tắt thì không đẩy thông báo nào, dù `Gamification` vẫn đang bật và điểm vẫn được ghi.
- `BR-2.5` Khi chuyển từ **chạy ngầm** sang **bật đầy đủ**, **không bắn thông báo hồi tố** cho dữ liệu đã tích trong giai đoạn chạy ngầm. Học viên thấy điểm và hạng đã có sẵn ở trang thành tích, kèm lịch sử để tra nguồn.
- `BR-2.6` Lỗi ở phần hiển thị thông báo **không được làm hỏng thao tác học**. Học viên bấm Hoàn thành thì thao tác đó phải thành công dù thông báo không hiện được. Theo `NFR-GAM-01`.
- `BR-2.7` Tài khoản có `Test Account = Yes` không nhận thông báo, vì không phát sinh dữ liệu gamification.
- `BR-2.8` Không có thông báo tụt hạng, vì hạng chỉ lên không tụt (`BR-1.3`).
- `BR-2.9` **Không gộp thông báo.** Mỗi thành tích phát sinh một thẻ riêng, kể cả khi nhiều thành tích đến từ cùng một thao tác.

**NFR**

Việc đẩy thông báo nằm trong cùng thao tác với việc hoàn thành hoạt động. Phần này không được làm chậm cảm nhận của thao tác đó, và lỗi ở đây phải được chặn lại tại chỗ.

### 5/ Out of scope

| Không làm ở US này | Lý do |
|---|---|
| Gửi email thông báo thành tích | PO chốt chỉ đẩy trong hệ thống |
| Lưu thông báo vào hộp thư để đọc lại sau | Thành tích tra được ở `US1` và `US3`. Hộp thư thông báo hiện có không dùng |
| Gửi bản tóm tắt *"bạn đã nhận X điểm khi vắng mặt"* khi học viên quay lại | PO chốt: không online thì thôi, thành tích vào lịch sử |
| Thông báo cho người khác, ví dụ quản lý trực tiếp hay mentor | Ngoài phạm vi. Xem `US16 — chưa làm` |
| Cho học viên tắt hoặc chỉnh thông báo thành tích | Chưa yêu cầu. Xem `OQ-12` |

### 6/ Conner case

*(QA điền)*

---

## US3: Lịch sử ghi nhận

### 1/ User story

Là học viên, tôi cần tra được từng lần cộng điểm đến từ đâu, và mọi thay đổi về huy hiệu hay hạng của mình, để tin vào con số của mình.

> Lịch sử gồm cả điểm, mốc đạt huy hiệu và lên hạng — một dòng thời gian duy nhất về mọi thứ học viên đã đạt được.

> Đây là US giữ cho `O5` đứng vững. Yêu cầu gốc nói thẳng: *"Điểm không giải thích được thì không ai tin bảng xếp hạng."*

### 2/ Pre - Condition

| Điều kiện | Nguồn |
|---|---|
| `Gamification` bật và `Visibility in UpLMS` bật | Hai công tắc `Gamification` và `Visibility in UpLMS`, cấu hình ở `US14` |
| Tài khoản không phải `Test Account` | Ràng buộc `C10` — `Test Account` bị loại khỏi toàn bộ logic gamification |

### 3/ Scenario

Học viên ở màn Gamification, mở `Achievement history`. Một panel trượt ra từ cạnh phải, liệt kê từng lần ghi nhận theo thứ tự **mới nhất lên trước**.

Mỗi mục gồm hai dòng: dòng trên là thời điểm, dòng dưới là một câu kể rõ học viên nhận được gì và vì sao.

Học viên cuộn xuống để xem các lần trước đó. Chưa có lần nào thì hiện trạng thái rỗng.

### 4/ Acceptance criteria

**UI / UX / Rule UX / Rule UI**

| Màn hình | Giao diện | Field | Yêu cầu |
|---|---|---|---|
| Achievement history | Điểm vào | Vị trí | **Panel trượt từ cạnh phải**, mở từ màn Gamification. Không phải trang riêng, không phải tab |
| Achievement history | Panel | Tiêu đề | `Achievement history`, kèm nút `✕` đóng ở góc phải |
| Achievement history | Mục | Dòng thời gian | `HH:mm • dd/mm/yyyy`, chữ nhỏ màu nhạt, cắt theo múi giờ tổ chức |
| Achievement history | Mục | Dòng nội dung | Một câu hoàn chỉnh. Số điểm, tên huy hiệu và số hạng **in đậm**, phần còn lại chữ thường. Bộ chuỗi đầy đủ ở bảng dưới |
| Achievement history | Mục | Thứ tự | **Mới nhất lên trước** |
| Achievement history | Mục | Tên dài | Tên hoạt động và tên khoá cắt ở `60` ký tự rồi thêm `…`. Trỏ chuột vào hiện đầy đủ |
| Achievement history | Panel | Số mục một lần tải | Tải thêm khi cuộn tới cuối. Số mục mỗi lần: `❓BA` |
| Achievement history | Panel | Trạng thái rỗng | `Nothing here yet. Start learning to earn your first points.` |
| Lịch sử ghi nhận | Bảng | Thao tác | Chỉ đọc. Không sửa, không xoá, không có nút thao tác nào trên dòng |

**Bộ chuỗi đầy đủ**

Mẫu chung: `You earned **{điểm}** for {hành động}.` Phần trong `{…}` là giá trị hệ thống điền.

*Nhận điểm*

| Nguồn | Chuỗi |
|---|---|
| Check-in, ngày đầu của chuỗi | `You earned **{n} points** for checking in today.` |
| Check-in, đang giữ chuỗi | `You earned **{n} points** for checking in today. Day {d} of your streak.` |
| Hoàn thành hoạt động | `You earned **{n} points** for completing **{tên hoạt động}** in {tên khoá}.` |
| Hoàn thành khoá | `You earned **{n} points** for completing the course **{tên khoá}**.` |
| Qua bài Test | `You earned **{n} points** for passing **{tên bài Test}** in {tên khoá}.` |

*Huy hiệu và hạng*

| Sự kiện | Chuỗi |
|---|---|
| Đạt huy hiệu | `You unlocked the **{tên huy hiệu}** badge for reaching {mốc} {đơn vị}.` |
| Lên hạng | `You reached **Level {n}**.` |

`{đơn vị}` thay theo loại huy hiệu: `sign-ins` · `activities` · `passed tests` · `completed courses`.

> **Ba loại sự kiện, không hơn.** Nhận điểm · đạt huy hiệu · lên hạng.
>
> Không có sự kiện **không được điểm** vì `CR-010` bỏ trần điểm ngày, mà chạm trần vốn là lý do duy nhất sinh ra nó.
>
> Không có sự kiện **tụt hạng** và **gỡ huy hiệu**. Hạng chỉ lên (`BR-1.3`), huy hiệu đã nhận giữ vĩnh viễn (`BR-1.4`).

**Business requirement — Business rule**

- `BR-3.1` Lịch sử hiện **mọi lần hệ thống cộng điểm**. Không còn trần điểm ngày nên không còn trường hợp xét mà không được điểm.
- `BR-3.3` Mỗi dòng nêu **nguồn cụ thể**, không chỉ loại hành động. Học viên phải đối chiếu được với việc mình đã làm.
- `BR-3.4` Sắp xếp theo thời điểm, mới nhất trước.
- `BR-3.5` Lịch sử **không sửa và không xoá được**, kể cả bởi vận hành.
- `BR-3.6` Vận hành đổi bảng điểm thì **các dòng lịch sử cũ giữ nguyên số điểm đã ghi**. Theo `C4`, cấu hình mới chỉ áp cho lần cộng sau đó.
- `BR-3.7` Điểm ghi trong giai đoạn **chạy ngầm** hiện đầy đủ trong lịch sử ngay khi bật `Visibility in UpLMS`.
- `BR-3.8` Tài khoản có `Test Account = Yes` không có lịch sử, vì không phát sinh dữ liệu gamification.
- `BR-3.9` **Lịch sử giữ toàn bộ, không giới hạn thời gian, không dọn.** Học viên tra được mọi lần ghi nhận từ ngày đầu tiên. Đây là điều kiện để `O5` đứng vững: một con số chỉ đáng tin khi truy được tới tận nguồn.

**Data Field**

| Field | Kiểu | Bắt buộc | Giá trị hợp lệ | Ghi chú |
|---|---|---|---|---|
| Thời điểm ghi nhận | Thời gian | Có | | Mới. Nền của `C3`, `C7`, `C8` |
| Học viên | Khoá ngoại tới `users` | Có | | Mới |
| Loại hành động | Danh mục | Có | Một trong các hành động khai ở `US9` | Mới |
| Nội dung nguồn | Khoá ngoại | Không | Hoạt động, khoá, hoặc bài Test. Rỗng với hành động check-in | Mới |
| Số điểm | Số nguyên | Có | `>= 0` | Mới. `0` khi chạm trần ngày |
| Lý do không được điểm | Danh mục | Không | Chỉ điền khi số điểm `= 0` | Mới |
| `tenant_id` | Khoá ngoại | Có | | `C1`. Bảng này là nơi rò rỉ gây hậu quả nặng nhất |

> Đây là **sổ giao dịch điểm**, bảng nền của gần như mọi thứ trong tính năng: lịch sử ở US này, xếp hạng theo kỳ (`C7`), tiêu chí phụ khi đồng hạng (`S22`), và kiểm tra luật chống cày.

**NFR**

Danh sách tải theo trang, không tải toàn bộ lịch sử của học viên trong một lần.

### 5/ Out of scope

| Không làm ở US này | Lý do |
|---|---|
| Lọc hoặc tìm kiếm trong lịch sử | Chưa yêu cầu. Xem `OQ-18` |
| Xuất lịch sử ra file | Chưa yêu cầu |
| Hiện huy hiệu đã đạt và lần lên hạng trong cùng dòng thời gian | Huy hiệu và hạng nằm ở `US1` |
| Xem lịch sử điểm của học viên khác | Không ai có quyền này, kể cả vận hành |
| Vận hành sửa hoặc cộng bù điểm thủ công | `A12`. Nếu sau này cần thì là một US riêng |

### 6/ Conner case

*(QA điền)*

---

## US4: Huy hiệu sắp đạt

### 1/ User story

Là học viên, tôi cần biết huy hiệu nào mình sắp đạt và còn thiếu bao nhiêu, để có mục tiêu ngắn hạn để nhắm tới.

### 2/ Pre - Condition

| Điều kiện | Nguồn |
|---|---|
| `Gamification` bật và `Visibility in UpLMS` bật | Hai công tắc `Gamification` và `Visibility in UpLMS`, cấu hình ở `US14` |
| Vận hành đã tạo ít nhất một huy hiệu | `US10` |
| Tài khoản không phải `Test Account` | Ràng buộc `C10` — `Test Account` bị loại khỏi toàn bộ logic gamification |

### 3/ Scenario

Học viên bấm ô `{n} Badges` trên màn Gamification, hệ thống chuyển sang **`My Profile` → tab `Badges`**.

Tab này hiện **toàn bộ huy hiệu của từng loại đang bật**, cả đã đạt lẫn chưa đạt. Huy hiệu đã đạt hiện màu, chưa đạt hiện xám. Tiêu đề mỗi loại kèm bộ đếm dạng `Check-in Badges (2/8)`.

Trỏ chuột vào một huy hiệu bất kỳ thì hiện **mốc của nó**, ví dụ `8 check-in`. Đó là cách học viên biết còn thiếu bao nhiêu.

### 4/ Acceptance criteria

**UI / UX / Rule UX / Rule UI**

| Màn hình | Giao diện | Field | Yêu cầu |
|---|---|---|---|
| My Profile → Badges | Điểm vào | Vị trí | **Một tab trong màn `My Profile`**, cạnh `My profile` và `Security`. Vào từ ô `{n} Badges` trên màn Gamification |
| My Profile → Badges | Tiêu đề loại | Bộ đếm | `{Tên loại} Badges ({đã đạt}/{tổng mốc})`, ví dụ `Check-in Badges (2/8)` |
| My Profile → Badges | Huy hiệu | Hình | Đã đạt hiện màu, **chưa đạt hiện xám**. Ảnh vận hành tải lên ở `US9`. Ảnh gốc bị xoá thì rơi về ảnh mặc định |
| My Profile → Badges | Huy hiệu | Tên | Hiện dưới hình |
| My Profile → Badges | Huy hiệu | Mốc | Hiện khi **trỏ chuột vào huy hiệu**, dạng `{mốc} {đơn vị}` — ví dụ `8 check-in`. Đây là cách học viên biết còn thiếu bao nhiêu |
| My Profile → Badges | Huy hiệu | Ngày đạt | **Không hiện ở đây.** Học viên tra trong `Achievement history` (`US3`), nơi có đủ thời điểm của mọi mốc |
| My Profile → Badges | Huy hiệu | Thứ tự | Nhóm theo loại, trong mỗi loại sắp theo **mốc tăng dần**. Mọi học viên thấy cùng một thứ tự |
| My Profile → Badges | Loại đang tắt | Hiển thị | Không hiện cả nhóm. Vận hành tắt loại nào ở `US9` thì loại đó biến mất khỏi tab |
| Thành tích của tôi | Danh sách huy hiệu | Phạm vi hiển thị | **Hiện toàn bộ huy hiệu vận hành đã tạo**, cả đã đạt lẫn chưa đạt, kèm mốc của từng cái. Học viên thấy hết bản đồ để biết phấn đấu tới đâu |
| Thành tích của tôi | Danh sách huy hiệu | Nhóm và thứ tự | Nhóm theo loại. Trong mỗi loại sắp theo mốc tăng dần, mốc thấp trước |
| Thành tích của tôi | Danh sách huy hiệu | Huy hiệu đã đạt | Hình đầy đủ màu, kèm ngày đạt |
| Thành tích của tôi | Danh sách huy hiệu | Huy hiệu chưa đạt | Hình hiển thị khác để phân biệt với đã đạt. Cách phân biệt: `❓BA`, chờ Figma |
| Thành tích của tôi | Danh sách huy hiệu | Tên huy hiệu | Hiện đầy đủ với cả huy hiệu chưa đạt. Không giấu tên |
| Thành tích của tôi | Danh sách huy hiệu | Tiến độ | Chỉ hiện với huy hiệu **chưa đạt**. Thanh tiến độ kèm số dạng `{hiện tại}/{ngưỡng}`, ví dụ `12/20` |
| Thành tích của tôi | Danh sách huy hiệu | Phần còn thiếu | Chỉ hiện với huy hiệu chưa đạt. Một dòng tiếng Anh theo mẫu `{N} more {đơn vị} to unlock`.<br>Ví dụ: `8 more activities to unlock`. Chuỗi cho từng loại: `❓BA` |
| Thành tích của tôi | Danh sách huy hiệu | Trạng thái rỗng | Vận hành chưa tạo huy hiệu nào thì ẩn cả phần này |

**Business requirement — Business rule**

- `BR-4.1` Hiện **toàn bộ huy hiệu vận hành đã tạo**, cả đã đạt lẫn chưa đạt, kèm mốc của từng cái.
- `BR-4.2` Huy hiệu chưa đạt hiện thêm tiến độ và phần còn thiếu. Huy hiệu đã đạt hiện ngày đạt.
- `BR-4.3` 🔑 **Số đếm hiển thị ở đây phải dùng đúng định nghĩa chỉ số đã khai trong `Solution`, giống hệt lúc hệ thống xét trao huy hiệu.** Sai lệch giữa hai chỗ tạo ra tình huống học viên thấy *"còn 1 nữa"*, làm xong, rồi không được huy hiệu.
- `BR-4.4` Vận hành chưa tạo huy hiệu nào cho một loại thì loại đó **không hiện**.
- `BR-4.5` Tài khoản có `Test Account = Yes` không có phần này.

**Đổi ngưỡng huy hiệu — quét lại toàn bộ**

- `BR-4.6` **Mốc của một huy hiệu khoá ngay sau khi tạo**, vận hành không sửa được. **Cũng không có thao tác xoá huy hiệu.** Nên không có tình huống nào khiến học viên mất huy hiệu đã có, và không có tình huống phải quét lại cấp bù.
- `BR-4.7` Vận hành tạo thêm huy hiệu mới với mốc khác thì huy hiệu đó được xét **từ thời điểm tạo trở đi**, theo `C4`. Học viên đã vượt mốc từ trước được trao ở lần xét tiếp theo.
- `BR-4.8` Huy hiệu bị **tắt** thì biến khỏi danh sách với mọi học viên, kể cả người đã đạt. Dữ liệu giữ nguyên, bật lại thì hiện lại đầy đủ. Xem `BR-1.4a`.
- `BR-4.9` **Tắt cả chức năng huy hiệu** thì toàn bộ phần huy hiệu biến khỏi trang Thành tích của tôi, và chỉ số `Badges` biến khỏi bộ chọn chỉ số của bảng xếp hạng (`US6`).

> **Ba cơ chế cùng một luật.** Điểm, huy hiệu và hạng đều chỉ áp thay đổi **từ thời điểm đổi trở đi**, và **không có gì bị lấy lại** khỏi học viên. Hạng không tụt, huy hiệu không mất, điểm đã ghi không đổi.

**Data Field**

Không có field mới. Phần này tính từ dữ liệu đã có:

| Cần gì | Lấy ở đâu |
|---|---|
| Ngưỡng và loại của từng huy hiệu | Bảng Huy hiệu (`US10`) |
| Huy hiệu học viên đã đạt | Bảng Huy hiệu đã đạt (`US1`) |
| Số ngày có mặt | Bảng Ngày có mặt (`US5`) |
| Số hoạt động hoàn thành | Theo mục Định nghĩa chỉ số — **không phụ thuộc công tắc `Points`** |
| Số bài Test | Theo mục Định nghĩa chỉ số, lọc theo `BR-TEST` |
| Số khoá hoàn thành | **Số lượt hoàn thành khoá**, theo mục Định nghĩa chỉ số. ⚠️ **Không dùng** `GET /api/v1/users/course-certificate/count`, vì endpoint đó đếm chứng chỉ mà chứng chỉ không cấp lại khi học lại — xem `BR-13.12` |

**NFR**

Số đếm của mỗi loại chỉ tính **một lần** cho mỗi lần mở trang, rồi so với mọi mốc của loại đó. Không tính lại cho từng huy hiệu.

Việc quét lại khi đổi ngưỡng (`BR-4.6`, `BR-4.7`) chạy nền, không chặn thao tác lưu cấu hình của vận hành.

### 5/ Out of scope

| Không làm ở US này | Lý do |
|---|---|
| Gợi ý nội dung cụ thể để đạt huy hiệu, ví dụ *"học khoá X"* | Chưa yêu cầu. Cần logic đề xuất nội dung, là bài toán khác |
| Hiện tiến độ tới **hạng** kế tiếp | Đã có ở `US1` |
| Thông báo khi sắp đạt một huy hiệu, ví dụ *"còn 1 nữa"* | Chưa yêu cầu. `US2` chỉ báo khi đã đạt |

### 6/ Conner case

*(QA điền)*

---

## US5: Điểm khi vào hệ thống hằng ngày

### 1/ User story

Là học viên, tôi cần việc vào hệ thống mỗi ngày được ghi nhận thành điểm, để có lý do mở ứng dụng hằng ngày.

> Đây là hành động nhắm thẳng vào chỉ số yếu nhất trong `Analytics`: **Activation 40.2%** so với tiêu chí 80%. Sáu trên mười người được gán khoá không vào lấy một lần trong tuần đầu.

### 2/ Pre - Condition

| Điều kiện | Nguồn |
|---|---|
| `Gamification` bật ở cấp tổ chức | Hai công tắc `Gamification` và `Visibility in UpLMS`, cấu hình ở `US14` |
| Vận hành đã bật hành động **vào hệ thống hằng ngày** và khai ba tham số điểm chuỗi | `US8` |
| Tài khoản không phải `Test Account` | Ràng buộc `C10` — `Test Account` bị loại khỏi toàn bộ logic gamification |
| Tổ chức đã có **múi giờ** | Ràng buộc `C9` — biên ngày cắt theo múi giờ tổ chức. Múi giờ lấy theo tenant, xem `BR-14.9` |

> `Visibility in UpLMS` tắt thì **vẫn ghi nhận và vẫn cộng điểm**, chỉ không hiện gì cho học viên. Đây là giai đoạn chạy ngầm.

### 3/ Scenario

Học viên mở UpLMS. Ở lần đầu tiên trong ngày, hệ thống ghi nhận ngày có mặt, tăng chuỗi thêm một, rồi cộng điểm theo độ dài chuỗi mới. Thông báo hiện lên theo `US2`.

Học viên vào lại lần thứ hai, thứ ba trong cùng ngày thì không cộng thêm, không tăng chuỗi, không có thông báo.

Sang ngày mới, tính theo múi giờ tổ chức, lần vào đầu tiên lại được cộng với mức điểm cao hơn hôm trước, cho tới khi chạm trần.

Học viên bỏ trọn một ngày không vào thì chuỗi về `0`. Lần vào kế tiếp bắt đầu chuỗi mới, điểm quay về mức nền. Điểm đã nhận trong chuỗi cũ vẫn giữ nguyên.

### 4/ Acceptance criteria

**UI / UX / Rule UX / Rule UI**

| Màn hình | Giao diện | Field | Yêu cầu |
|---|---|---|---|
| Mọi màn UpLMS | Thông báo nhận điểm | Nội dung | Theo mẫu của `US2`, kèm độ dài chuỗi sau khi tăng. Chuỗi tiếng Anh: `❓BA`. Gợi ý: `+ {điểm} · {n}-day streak` |
| Gamification | Dải tóm tắt | `{n} Streaks` | Chuỗi hiện tại. Đứt thì về `0` |
| Gamification | Dải tóm tắt | Số ngày có mặt | **Không hiện riêng.** Nó là chỉ số nền cho huy hiệu loại Check-in, học viên thấy qua tiến độ huy hiệu ở `US4`. Khác với chuỗi: con số này **không về `0`** khi nghỉ |
| Toàn hệ thống | Thao tác của học viên | | **Không có thao tác nào.** Học viên không bấm nút check-in. Hệ thống tự ghi khi thấy học viên vào |

**Business requirement — Business rule**

- `BR-5.1` Mỗi ngày ghi nhận **một lần duy nhất**, ở lần đầu tiên học viên vào hệ thống trong ngày đó. Vào nhiều lần trong ngày không cộng thêm điểm và không tăng chuỗi.
  - **Vào hệ thống là học viên chủ động mở hoặc quay lại UpLMS.** Còn phiên đăng nhập từ hôm trước thì mở UpLMS là được tính, không cần đăng nhập lại.
  - **Request nền tự chạy không tính**, ví dụ kết nối thông báo hoặc tự làm mới dữ liệu khi tab để mở. Nếu không, học viên treo tab qua đêm sẽ tự giữ chuỗi kể cả thứ bảy, chủ nhật.
- `BR-5.2` **Không có thao tác check-in thủ công.** Học viên không bấm gì. Hệ thống ghi nhận khi thấy học viên có mặt.
- `BR-5.3` **"Ngày" cắt theo múi giờ tổ chức** (`C9`). Không dùng giờ máy chủ và không dùng múi giờ của thiết bị học viên.
- `BR-5.4` **Điểm tăng dần theo độ dài chuỗi.** Gọi `n` là ngày thứ mấy của chuỗi đang giữ:<br>`điểm = min( điểm nền + (n − 1) × 5 , trần điểm chuỗi )`<br>**Bước tăng cố định `5`, không cấu hình được.** Vận hành chỉ khai hai tham số ở `US8`: điểm nền và trần.<br>Với `10 / 40`: `10 · 15 · 20 · 25 · 30 · 35 · 40`, chạm trần đúng **ngày thứ 7**. Trọn một tuần được `175` điểm.
- `BR-5.5` **Chuỗi tăng thêm một mỗi ngày có mặt.** Ngày mở đầu một chuỗi có `n = 1` và nhận đúng mức điểm nền.
- `BR-5.6` **Bỏ trọn một ngày thì chuỗi về `0`.** Lần vào kế tiếp mở chuỗi mới từ `n = 1`. Hệ thống đếm **mọi ngày dương lịch**, nên thứ bảy, chủ nhật, ngày lễ và ngày nghỉ phép đều làm đứt chuỗi nếu học viên không vào.
- `BR-5.7` **Đứt chuỗi không thu hồi điểm đã nhận.** Điểm nằm lại trong sổ giao dịch, chuỗi về `0` chỉ ảnh hưởng mức điểm của những ngày sau.
- `BR-5.9` Đổi ba tham số ở `US8` **chỉ áp dụng từ thời điểm đổi** (`C4`). Chuỗi đang giữ không bị cắt và không bị tính lại; ngày kế tiếp dùng tham số mới với đúng `n` hiện có.
- `BR-5.10` **Trần điểm chuỗi** ở `BR-5.4` chỉ chặn mức điểm của riêng một ngày check-in. Nó không phải trần cho tổng điểm trong ngày — hệ thống không có trần đó.
- `BR-5.11` Ghi nhận ngày có mặt nằm trong cùng thao tác với việc học viên vào hệ thống. Lỗi ở đây **không được chặn học viên vào hệ thống**, theo `NFR-GAM-01`.
- `BR-5.12` `Gamification` tắt thì **không ghi nhận gì**. Bật lại chỉ tính từ thời điểm bật: chuỗi mở lại từ `n = 1`, không dựng lại những ngày đã qua.
- `BR-5.13` `Visibility in UpLMS` tắt thì **vẫn ghi nhận, vẫn cộng điểm, vẫn tăng chuỗi**, chỉ không hiện và không thông báo.
- `BR-5.14` Tài khoản có `Test Account = Yes` không được ghi nhận ngày có mặt và không có chuỗi.

**Data Field**

| Field | Kiểu | Bắt buộc | Giá trị hợp lệ | Ghi chú |
|---|---|---|---|---|
| Học viên | Khoá ngoại tới `users` | Có | | Mới |
| Ngày có mặt | Ngày | Có | Cắt theo múi giờ tổ chức | Mới. Không lưu giờ phút, chỉ lưu ngày |
| `tenant_id` | Khoá ngoại | Có | | Ràng buộc `C1` — cấu hình gắn `tenant_id`, không đóng cứng trong mã |

Một học viên một ngày chỉ có **một bản ghi**. Đây cũng là cách chặn cộng điểm hai lần khi học viên mở hai thiết bị cùng lúc, xử lý luôn `CG-7`.

Số ngày có mặt dùng ở hai nơi: hành động tính điểm này, và **huy hiệu loại Tích cực** (`US4`, `US9`).

Trạng thái chuỗi **không lưu ở bảng này** mà lưu ở `Thành tích của học viên`, vì nó là trạng thái của một người chứ không phải của một ngày:

| Field | Kiểu | Bắt buộc | Giá trị hợp lệ | Ghi chú |
|---|---|---|---|---|
| Chuỗi hiện tại | Số nguyên | Có | `>= 0` | Mới. `0` nghĩa là chưa có chuỗi hoặc vừa đứt |
| Ngày có mặt gần nhất | Ngày | Không | Cắt theo múi giờ tổ chức | Mới. Dùng để biết chuỗi đã đứt chưa |

Bảng `Ngày có mặt của học viên` giữ nguyên cấu trúc. Nó vẫn là nguồn để dựng lại chuỗi khi cần đối chiếu.

**NFR**

Việc ghi nhận chạy ở lần vào đầu tiên trong ngày. Những lần vào sau trong cùng ngày không được tạo thêm thao tác ghi.

Việc xác định chuỗi đã đứt hay chưa đọc từ `Ngày có mặt gần nhất`, không quét lại bảng `Ngày có mặt của học viên`.

### 5/ Out of scope

| Không làm ở US này | Lý do |
|---|---|
| Miễn trừ thứ bảy, chủ nhật, ngày lễ và nghỉ phép khỏi việc đứt chuỗi | `BR-5.6` đếm mọi ngày dương lịch. PO chốt ở `CR-009` sau khi cân nhắc phương án theo lịch làm việc |
| Quỹ bảo vệ chuỗi, cho phép vắng vài ngày mỗi tháng mà không đứt | Đã nêu ở `CR-009`, PO không chọn |
| Thông báo đẩy cảnh báo sắp đứt chuỗi | `BR-2.1` chỉ đẩy thông báo khi học viên **đang mở UpLMS**. Người sắp đứt chuỗi theo định nghĩa là người không vào, nên sẽ không bao giờ nhận được. Thay bằng dòng nhắc tĩnh trên trang Thành tích |
| Huy hiệu trao theo độ dài chuỗi | Chưa yêu cầu. Huy hiệu loại Tích cực vẫn đo tổng số ngày có mặt |
| Nút check-in cho học viên tự bấm | `BR-5.2`. Vào hệ thống là đủ |
| Lấy dữ liệu từ sự kiện đăng nhập của Keycloak | Học viên dùng SSO Lark, phiên sống nhiều ngày nên có thể không sinh sự kiện đăng nhập mới. Người chăm nhất lại là người ít sinh sự kiện nhất |
| Dựng lại số ngày có mặt trước khi bật tính năng | `BR-5.12`. Không tính bù, và chuỗi cũng mở lại từ đầu |
| Phân biệt vào hệ thống bằng máy tính hay điện thoại | Chưa yêu cầu |

### 6/ Conner case

*(QA điền)*

---

## US6: Bảng xếp hạng

### 1/ User story

Là học viên, tôi cần xem bảng xếp hạng theo khung thời gian cố định, để biết mình đứng ở đâu so với người khác.

### 2/ Pre - Condition

| Điều kiện | Nguồn |
|---|---|
| `Gamification` bật và `Visibility in UpLMS` bật | Hai công tắc `Gamification` và `Visibility in UpLMS`, cấu hình ở `US14` |
| Tổ chức đã có **múi giờ** | Ràng buộc `C6` — biên khoảng cắt theo múi giờ tổ chức. Múi giờ lấy theo tenant, xem `BR-14.9` |
| Tài khoản không phải `Test Account` | Ràng buộc `C10` — `Test Account` bị loại khỏi toàn bộ logic gamification |

### 3/ Scenario

Học viên mở trang Bảng xếp hạng. Mặc định hiện `All time`.

Học viên đổi khung thời gian bằng một trong năm lựa chọn cố định: toàn thời gian, tuần này, tháng này, quý này, năm này. **Không có bộ chọn khoảng ngày tự do.** Muốn xem một đợt thi đua có chủ đích thì chọn campaign, xem `US19`.

Bảng hiện thứ hạng, tên và chỉ số của từng học viên, kèm nhãn thời điểm cập nhật gần nhất.

### 4/ Acceptance criteria

**UI / UX / Rule UX / Rule UI**

| Màn hình | Giao diện | Field | Yêu cầu |
|---|---|---|---|
| Bảng xếp hạng | Điểm vào | Vị trí | Mục riêng ở menu chính UpLMS. `Visibility in UpLMS` tắt thì mục biến mất |
| Bảng xếp hạng | Chọn khung thời gian | Các lựa chọn | `All time` · `This week` · `This month` · `This quarter` · `This year`. **Không có bộ chọn khoảng ngày tự do**, xem `BR-6.15` |
| Bảng xếp hạng | Chọn khung thời gian | Mặc định | `All time` — từ ngày bật tính năng tới hôm nay |
| Bảng xếp hạng | Chọn khung thời gian | Hiển thị | Luôn hiện khoảng ngày của khung đang chọn, ví dụ `1–30 Sep 2026` |
| Bảng xếp hạng | Chọn khung thời gian | Campaign | Lối vào campaign nằm cạnh các khung cố định. Chi tiết ở `US19` |
| Bảng xếp hạng | Chọn bảng | Các lựa chọn | Năm bảng riêng: `Points` · `Activities` · `Courses` · `Level` · `Badges`. Chỉ hiện những bảng vận hành đã bật ở `US11`. **`Level` và `Badges` chỉ có ở `All time`**, biến mất khi chọn khung khác |
| Bảng xếp hạng | Chọn bảng | Đổi khung làm bảng đang xem biến mất | Chuyển về bảng đầu tiên còn hiện. `[đề xuất]` |
| Bảng xếp hạng | Chọn bảng | Mặc định | `Points`. `[đề xuất]` |
| Bảng xếp hạng | Bảng | Top 3 | Ba vị trí đầu hiển thị nổi bật, tách khỏi danh sách bên dưới |
| Bảng xếp hạng | Bảng | Danh sách đầy đủ | Bên dưới top 3, cuộn được, gồm **toàn bộ học viên** kể cả người chưa có chỉ số nào. Người chưa có chỉ số nằm cuối |
| Bảng xếp hạng | Bảng | Cột `#` | Thứ hạng, số nguyên bắt đầu từ 1. Không có hai người cùng thứ hạng, xem `BR-6.4`. **Học viên chưa có chỉ số nào để trống ô này** |
| Bảng xếp hạng | Bảng | Cột học viên | Ảnh đại diện và tên học viên |
| Bảng xếp hạng | Bảng | Cột giá trị | Một cột duy nhất, đúng chỉ số của bảng đang xem |
| Bảng xếp hạng | Bảng | Dòng của chính người đang xem | Làm nổi bật trong danh sách. Chi tiết ở `US7` |
| Bảng xếp hạng | Nhãn cập nhật | Nội dung | `Last updated {HH:mm}` theo múi giờ tổ chức. Luôn hiện, kể cả khi bảng vừa mới tính xong |
| Bảng xếp hạng | Trạng thái rỗng | Khung chưa có ai được ghi nhận | `No one has earned points in this period yet.` Chuỗi cho bảng `Activities` và `Courses`: `❓BA` |

**Business requirement — Business rule**

- `BR-6.1` Phạm vi xếp hạng là **toàn tổ chức**. Không có bộ lọc theo lớp, phòng ban hay nhóm ở phạm vi này.
- `BR-6.2` **Mỗi chỉ số là một bảng xếp hạng riêng**, không phải một bảng nhiều cột. Năm bảng: theo điểm · theo số hoạt động hoàn thành · theo số khoá hoàn thành · theo hạng · theo số huy hiệu. Học viên chuyển giữa các bảng.
- `BR-6.2a` **Bảng nào hiện ra do vận hành cấu hình** ở `US11`. Tắt bảng nào thì học viên không chuyển sang được.
- `BR-6.2b` 🔑 **Bảng theo hạng và bảng theo số huy hiệu chỉ có ở `All time`**, biến mất khi chọn khung khác. Theo `BR-11.2`.
  > **Vì sao huy hiệu không đếm theo khung được.** Mốc huy hiệu tăng gấp đôi, nên đếm huy hiệu trong một khoảng đo độ mới, không đo độ chăm. Ví dụ với `Activity badges` trong một tháng: người mới làm 30 hoạt động nhận 2 huy hiệu (mốc 10, 25), còn người cũ đang ở 420 làm 300 hoạt động nhận 0 huy hiệu vì mốc kế tiếp là 800.
- `BR-6.3` Các khung là **khoảng theo lịch**, không phải cửa sổ trượt. `This week` là tuần theo lịch, không phải bảy ngày gần nhất. Biên ngày cắt theo **múi giờ tổ chức**.
- `BR-6.4` **Cùng chỉ số thì ai đạt mức đó sớm hơn xếp trên.** Không hiển thị hai người cùng thứ hạng. Quy tắc này bắt buộc vì hai trong năm chỉ số có khoảng giá trị rất hẹp: số huy hiệu thường từ 0 đến 10, số khoá hoàn thành từ 0 đến 5.
- `BR-6.5` Bảng **tính sẵn theo chu kỳ**, không tính lại mỗi lần học viên mở trang. Nhãn `Last updated` cho biết số liệu tính tới lúc nào.
- `BR-6.6` Học viên **chưa có chỉ số nào trong khung vẫn xuất hiện** trong bảng, nhưng **cột thứ hạng để trống**. Nhiều người cùng ở trạng thái này thì vẫn nằm trên dưới nhau trong danh sách, chỉ là không ai có số thứ hạng.
- `BR-6.12` 🔑 **Mọi bảng đều tính sẵn, 8 tiếng một lần**, gồm năm khung cố định và các campaign đang chạy. Mở là thấy ngay, kèm nhãn `Last updated {HH:mm}`. **Không có phép tính nào chạy theo yêu cầu của học viên.**
- `BR-6.13` **Gốc của bảng là toàn thời gian**, tính từ ngày bật tính năng tới hôm nay. Khung thời gian là **bộ lọc** đặt lên trên, không phải một bảng riêng biệt.
- `BR-6.15` 🔑 **Học viên không chọn được khoảng ngày tự do.** Khoảng tự chọn phải tính lúc chọn, nên ai cũng gọi được một phép tính nặng tuỳ ý, và gọi liên tục là làm chậm cả hệ thống. Chỉ còn khung cố định thì mọi thứ phía học viên đều tính sẵn, học viên gọi bao nhiêu lần cũng chỉ là đọc.
  > Nhu cầu xem một đợt có chủ đích thì dùng campaign (`US19`). Vận hành vẫn có bộ chọn khoảng ngày tự do ở `US12`.
- `BR-6.7` Tài khoản có `Test Account = Yes` **không xuất hiện**, vì không phát sinh dữ liệu gamification.
- `BR-6.8` Học viên bị `Block` hoặc đã rời tổ chức **không xuất hiện trong bảng đang chạy**. Kết quả campaign đã đóng băng thì giữ nguyên, xem `US21`.
- `BR-6.9` Bảng **công khai tên và ảnh** của học viên với mọi học viên khác trong tổ chức.
- `BR-6.10` ⚠️ **Khung cố định là số liệu sống, không đóng băng.** Xem cùng một khung vào hai thời điểm khác nhau **có thể ra kết quả khác nhau**, vì bài chấm tay có thể được chấm muộn, và học viên bị `Block` hay rời tổ chức sẽ biến mất khỏi bảng.
  > Muốn kết quả không đổi để trao thưởng thì dùng campaign — kết quả đóng băng khi kết thúc (`US21`).
- `BR-6.11` Một lần cộng điểm thuộc **mọi khoảng bao trùm nó**. Điểm nhận ngày 15/09 xuất hiện khi xem tuần đó, tháng 9, quý III, năm 2026, và ở mọi campaign có khoảng chứa ngày 15/09 nếu hành động đó thuộc loại campaign chọn.

**Data Field**

| Field | Kiểu | Bắt buộc | Ghi chú |
|---|---|---|---|
| Khung thời gian hoặc campaign | Danh mục hoặc khoá ngoại tới campaign | Có | Năm khung cố định, hoặc một campaign đang chạy |
| Chỉ số | Danh mục | Có | Một trong năm. Campaign chỉ có `Points` và `Activities` |
| Học viên | Khoá ngoại tới `users` | Có | |
| Giá trị chỉ số | Số nguyên | Có | |
| Thời điểm đạt mức hiện tại | Thời gian | Có | Nền của `BR-6.4`. Theo `C8` |
| Thứ hạng | Số nguyên | Không | Để trống với học viên chưa có chỉ số, theo `BR-6.6` |
| Thời điểm tính | Thời gian | Có | Nguồn của nhãn `Last updated` |
| `tenant_id` | Khoá ngoại | Có | Ràng buộc `C1` — cấu hình gắn `tenant_id`, không đóng cứng trong mã |

Bảng này bị **ghi đè mỗi chu kỳ tính**. Kết quả đóng băng chỉ có ở campaign, lưu riêng, xem `US21`.

**NFR**

| Loại bảng | Cách tính |
|---|---|
| Năm khung cố định, nhân các bảng đang bật | **Tính sẵn** theo chu kỳ 8 tiếng (`BR-6.12`) |
| Mỗi campaign đang chạy, hai bảng | **Tính sẵn** cùng chu kỳ (`US19`) |
| Campaign đã kết thúc | Đọc kết quả đã đóng băng, không tính lại (`US21`) |

`All time` là khoảng nặng nhất và **càng ngày càng nặng**, vì nó gom toàn bộ sổ giao dịch từ ngày bật tính năng.

### 5/ Out of scope

| Không làm ở US này | Lý do |
|---|---|
| Lọc bảng xếp hạng theo lớp, phòng ban hay nhóm | Chờ chức năng nhóm đồng bộ từ HRM. Xem `US16 — chưa làm` |
| Hiện vị trí của người đang xem kèm người liền kề | `US7` |
| **Bộ chọn khoảng ngày tự do** | `BR-6.15`. Vận hành có ở `US12` |
| **Đóng băng kết quả của khung cố định** | Khung cố định là số liệu sống, xem `BR-6.10`. Cần kết quả không đổi thì dùng campaign |
| Xuất bảng xếp hạng ra file phía học viên | Chưa yêu cầu. Kết quả campaign xuất được ở `US21` |

### 6/ Conner case

*(QA điền)*

---

## US7: Vị trí của tôi

### 1/ User story

Là học viên, tôi cần luôn thấy vị trí của chính mình kèm vài người liền kề, kể cả khi mình không nằm trong nhóm đầu, để biết cần hơn ai một chút là lên hạng.

> Đây là cơ chế giảm nhẹ chính cho việc bảng xếp hạng chỉ có phạm vi toàn tổ chức. Với hàng nghìn học viên, phần lớn không bao giờ ở gần top 3, nên nếu không có khối này thì bảng xếp hạng gần như vô nghĩa với họ.

### 2/ Pre - Condition

| Điều kiện | Nguồn |
|---|---|
| Học viên đang mở trang Bảng xếp hạng (`US6`) | |
| `Gamification` bật và `Visibility in UpLMS` bật | Hai công tắc `Gamification` và `Visibility in UpLMS`, cấu hình ở `US14` |
| Tài khoản không phải `Test Account` | Ràng buộc `C10` — `Test Account` bị loại khỏi toàn bộ logic gamification |

### 3/ Scenario

Học viên mở trang Bảng xếp hạng. Ngoài top 3 ở trên và danh sách đầy đủ ở giữa, có một khối riêng luôn hiện vị trí của chính học viên kèm vài người ngay trên và ngay dưới.

Học viên cuộn danh sách đi đâu thì khối này vẫn ở đó. Đổi khung thời gian, đổi campaign hoặc đổi chỉ số thì khối này tính lại theo.

Học viên chưa có chỉ số nào trong kỳ thì khối vẫn hiện, nhưng không có số thứ hạng.

### 4/ Acceptance criteria

**UI / UX / Rule UX / Rule UI**

| Màn hình | Giao diện | Field | Yêu cầu |
|---|---|---|---|
| Bảng xếp hạng | Khối Vị trí của tôi | Vị trí trên màn | Luôn nhìn thấy được, không phụ thuộc vị trí cuộn của danh sách. Cách thể hiện: `❓BA`, chờ Figma |
| Bảng xếp hạng | Khối Vị trí của tôi | Dòng của chính học viên | Thứ hạng, ảnh, tên, giá trị chỉ số. Làm nổi bật khác với các dòng liền kề |
| Bảng xếp hạng | Khối Vị trí của tôi | Người liền kề | Vài người ngay trên và ngay dưới. Số lượng mỗi bên: `❓BA` |
| Bảng xếp hạng | Khối Vị trí của tôi | Khoảng cách tới người trên | Một dòng nêu còn thiếu bao nhiêu để vượt người ngay trên, theo mẫu `{N} {đơn vị} behind {tên}`. `[đề xuất]` |
| Bảng xếp hạng | Khối Vị trí của tôi | Học viên đang trong top 3 | Khối vẫn hiện, không ẩn đi. `[đề xuất]` |
| Bảng xếp hạng | Khối Vị trí của tôi | Học viên chưa có chỉ số | Khối vẫn hiện, ô thứ hạng để trống, kèm một dòng gợi ý bắt đầu học. Chuỗi tiếng Anh: `❓BA` |
| Bảng xếp hạng | Khối Vị trí của tôi | Khi đổi khung, campaign hoặc chỉ số | Tính lại theo khung hoặc campaign và chỉ số đang chọn ở `US6`, `US19` |

**Business requirement — Business rule**

- `BR-7.1` Khối này **luôn hiện**, kể cả khi học viên nằm ngoài top 3 và ngoài vùng danh sách đang cuộn tới.
- `BR-7.2` Hiện kèm **vài người ngay trên và ngay dưới**, để học viên thấy khoảng cách gần nhất chứ không chỉ thấy con số thứ hạng.
- `BR-7.3` Học viên **chưa có chỉ số nào trong kỳ** thì khối vẫn hiện với ô thứ hạng để trống, theo `BR-6.6`. Không ẩn khối, vì ẩn đi thì đúng nhóm học viên cần được kéo vào lại là nhóm không thấy gì.
- `BR-7.4` Khối cập nhật **cùng nhịp với bảng**, 8 tiếng một lần theo `BR-6.12`. Không tính riêng theo thời gian thực.
- `BR-7.5` Đổi kỳ hoặc đổi chỉ số ở `US6` thì khối tính lại theo. Kỳ và chỉ số của khối luôn khớp với bảng đang xem.
- `BR-7.6` Người liền kề hiển thị **tên và ảnh công khai**, giống bảng chính, theo `BR-6.9`.
- `BR-7.7` Tài khoản có `Test Account = Yes` không có khối này, và cũng không xuất hiện trong danh sách người liền kề của ai.

**Data Field**

Không có field mới. Khối này đọc từ **bảng xếp hạng đã tính sẵn** của `US6`, lấy dòng của học viên và các dòng liền kề.

**NFR**

Việc tìm dòng của học viên và các dòng liền kề dựa trên thứ hạng đã tính sẵn, không xếp hạng lại toàn bộ khi mở trang.

> Đây là lý do `US6` phải lưu **thứ hạng** thành một giá trị, không chỉ lưu giá trị chỉ số. Muốn biết vị trí của một người thì phải so với tất cả, nên nếu không tính sẵn thì mỗi lần mở trang lại phải xếp hạng lại cả tổ chức.

### 5/ Out of scope

| Không làm ở US này | Lý do |
|---|---|
| Xem vị trí của học viên khác trong danh sách người liền kề của họ | Chỉ có vị trí của chính mình |
| Thông báo khi thứ hạng thay đổi | Chưa yêu cầu. `US2` chỉ báo điểm, huy hiệu, lên hạng |
| Hiện lịch sử thứ hạng theo thời gian, ví dụ biểu đồ lên xuống | Chưa yêu cầu |
| So sánh với một người cụ thể do học viên chọn | Chưa yêu cầu |

### 6/ Conner case

*(QA điền)*

---

## US8: Cấu hình điểm

### 1/ User story

Là nhân sự vận hành, tôi cần bật tắt cơ chế điểm và khai mỗi hành động được bao nhiêu điểm, để điều chỉnh theo mục tiêu từng giai đoạn.

### 2/ Pre - Condition

| Điều kiện | Nguồn |
|---|---|
| `Gamification` đang bật ở cấp tổ chức | `US14` |
| Người dùng có quyền cấu hình gamification | `US15` |

### 3/ Scenario

Nhân sự vận hành mở màn cấu hình `Points` trong khu vực Gamification trên Ops.

Đầu khối là công tắc bật tắt cả cơ chế điểm. Bên dưới là bốn hành động, mỗi hành động có công tắc riêng và một ô nhập số điểm. Riêng check-in là ô điểm nền của chuỗi.

Mỗi thay đổi **tự lưu** khi rời ô hoặc khi bấm công tắc, không có nút lưu (`BR-14.10`). Cấu hình mới áp dụng cho các lần cộng điểm **từ thời điểm lưu trở đi**, không tính lại quá khứ.

### 4/ Acceptance criteria

**UI / UX / Rule UX / Rule UI**

| Màn hình | Giao diện | Field | Yêu cầu |
|---|---|---|---|
| Cấu hình điểm | Đầu màn | Công tắc `Points` | Bật tắt cả cơ chế điểm. Tắt thì mọi hành động bên dưới **chuyển sang trạng thái không thao tác được**, nhưng giữ nguyên giá trị đã khai. Tiêu chí lên hạng theo điểm ở `US10` **khoá theo**, xem `BR-10.7` |
| Cấu hình điểm | Đầu màn | Dòng giải thích dưới công tắc `Points` | Nêu rõ tắt `Points` thì tiêu chí lên hạng theo điểm cũng ngừng. **Không có hộp xác nhận.** Chuỗi tiếng Anh: `❓BA` |
| Cấu hình điểm | Đầu màn | Mô tả chức năng | `Award users with points for different learning activities and encourage healthy competition.` |
| Cấu hình điểm | Danh sách hành động | `On each daily check-in` | Công tắc riêng + **một ô nhập điểm nền**. Mô tả dưới tiêu đề: `Award points once a day when users first visit, even if they're still signed in from before. Each day in a row adds 5 more, up to 40 on day 7.` Ứng với `US5` |
| Cấu hình điểm | Điểm chuỗi check-in | Ô nhập | **Điểm nền** — số điểm của ngày đầu tiên trong một chuỗi. Số nguyên dương, nhỏ nhất `1`. Mặc định `10` |
| Cấu hình điểm | Điểm chuỗi check-in | Bước tăng | **Cố định `5`, không hiện ô nhập.** Nêu trong câu mô tả |
| Cấu hình điểm | Điểm chuỗi check-in | Trần điểm chuỗi | **Mặc định `40`**, chạm đúng ngày thứ 7. Chưa cho vận hành sửa ở đợt này, nêu trong câu mô tả |
| Cấu hình điểm | Danh sách hành động | `On each activity completion` | Công tắc riêng + ô nhập số điểm |
| Cấu hình điểm | Danh sách hành động | `On each course completion` | Công tắc riêng + ô nhập số điểm |
| Cấu hình điểm | Danh sách hành động | `On each successful test completion` | Công tắc riêng + ô nhập số điểm. **Chỉ tính bài Test đạt**, theo `BR-TEST` |
| Cấu hình điểm | Ô nhập số điểm | Định dạng | Số nguyên dương. Nhỏ nhất `1`, **không giới hạn trên**. Không nhận số âm, không nhận số thập phân, không nhận `0` |
| Cấu hình điểm | Ô nhập số điểm | Khi hành động đang tắt | Không nhập được, giữ nguyên giá trị cũ |
| Cấu hình điểm | Ô nhập số điểm | Bỏ trống | Không lưu được. Báo lỗi ngay tại ô, theo `BR-14.11` |
| Cấu hình điểm | Cách lưu | | **Tự lưu, không có nút lưu.** Ô nhập lưu khi rời ô hoặc bấm Enter, công tắc lưu khi bấm. Theo `BR-14.10` |
| Cấu hình điểm | Đầu khối | Dòng nhắc cố định | Nêu rằng thay đổi **chỉ áp dụng từ bây giờ trở đi**, không tính lại điểm đã cộng. **Luôn hiện**, không bật lên sau mỗi lần lưu. Chuỗi tiếng Anh: `❓BA` |

**Business requirement — Business rule**

- `BR-8.1` Bốn hành động tính điểm là **danh sách cố định** trong phạm vi này: check-in hằng ngày · hoàn thành hoạt động · hoàn thành khoá · hoàn thành bài Test đạt. Vận hành **không tự thêm hành động mới**.
  > Nhưng danh sách này phải **mở rộng được bằng cấu hình** ở tầng dữ liệu, theo ràng buộc `C2`. Sau này thêm hành động cho lộ trình học thì chỉ thêm bản ghi, không sửa cấu trúc.
- `BR-8.2` Tắt công tắc `Points` thì **ngừng cộng điểm mới**, nhưng điểm đã có **giữ nguyên** và học viên vẫn xem được ở trang thành tích. Tiêu chí lên hạng theo điểm khoá theo, xem `BR-10.7`.
- `BR-8.3` Tắt một hành động riêng lẻ thì chỉ hành động đó ngừng sinh điểm. Ba hành động còn lại chạy bình thường.
- `BR-8.4` Đổi số điểm của một hành động thì **áp dụng từ thời điểm lưu trở đi**. Các lần cộng điểm trước đó **giữ nguyên số điểm đã ghi** trong lịch sử, theo `C4`.
- `BR-8.5` Số điểm là **số nguyên dương**, nhỏ nhất `1`, **không có giới hạn trên**. Muốn một hành động không sinh điểm thì **tắt công tắc**, không đặt giá trị `0`.
  > ⚠️ **Rủi ro PO chấp nhận ngày 06/10/2026.** Không có giới hạn trên mà lại tự lưu khi rời ô, nên gõ nhầm `1500` thay vì `150` cũng có hiệu lực ngay. Điểm đã cộng theo số nhầm **không tính lại**, theo `C4`.
- `BR-8.5a` Check-in khai bằng **một ô điểm nền**. Bước tăng `5` và trần `40` là **hằng số của đợt này**, không hiện ô nhập.
  > Hai hằng số này vẫn phải **lưu ở tầng dữ liệu chứ không đóng cứng trong mã**, theo `C2`. Đợt sau mở ô cho vận hành sửa thì chỉ cần hiện ô, không phải đổi cấu trúc.
- `BR-8.5b` **Trần `40` chạm đúng ngày thứ 7** của chuỗi. Con số chọn theo chủ đích: người giữ chuỗi trọn một tuần, kể cả thứ bảy và chủ nhật, thì từ đó về sau luôn nhận mức cao nhất.
- `BR-8.5c` Đổi điểm nền **không cắt chuỗi của học viên nào**. Chuỗi đang giữ chạy tiếp, ngày kế tiếp tính theo giá trị mới (`BR-5.9`).
- `BR-8.8` Mọi giá trị trên màn này **gắn với tổ chức** (`C1`), không đóng cứng trong mã.

**Data Field**

| Field | Kiểu | Bắt buộc | Giá trị hợp lệ | Ghi chú |
|---|---|---|---|---|
| Cơ chế điểm bật hay tắt | Đúng/sai | Có | Mặc định **tắt** khi khởi tạo tổ chức | Mới |
| Mã hành động | Danh mục | Có | Bốn giá trị cố định ở phạm vi này | Mới. Chịu `C2` |
| Hành động bật hay tắt | Đúng/sai | Có | Mặc định **tắt** | Mới |
| Số điểm | Số nguyên | Có | `>= 1`, không giới hạn trên | Mới. Tổng điểm tích luỹ của học viên phải chứa được mà không tràn |
| `tenant_id` | Khoá ngoại | Có | | Ràng buộc `C1` — cấu hình gắn `tenant_id`, không đóng cứng trong mã |

**NFR**

Cấu hình đọc rất nhiều lần, vì mỗi lần cộng điểm đều phải tra. Cần tính tới việc giữ sẵn trong bộ nhớ thay vì đọc lại mỗi lần.

### 5/ Out of scope

| Không làm ở US này | Lý do |
|---|---|
| Thêm hành động tính điểm mới ngoài bốn hành động đã khai | `BR-8.1`. Thêm hành động cần có nguồn sự kiện tương ứng, là việc phát triển |
| Đặt số điểm khác nhau theo loại hoạt động, theo khoá, hay theo lớp | Chưa yêu cầu. Một hành động một số điểm, áp cho cả tổ chức |
| Lên lịch đổi cấu hình vào một thời điểm trong tương lai | Chưa yêu cầu |
| Xem lịch sử ai đã đổi cấu hình và đổi gì | Chưa yêu cầu. Xem `OQ-34` |
| Tính lại điểm đã cộng theo cấu hình mới | `BR-8.4`. Không bao giờ tính lại quá khứ |

### 6/ Conner case

*(QA điền)*

---

## US9: Cấu hình huy hiệu

### 1/ User story

Là nhân sự vận hành, tôi cần bật tắt từng loại huy hiệu và đặt tên cùng hình cho từng mốc, để bộ huy hiệu mang ngôn ngữ của tổ chức mình.

### 2/ Pre - Condition

| Điều kiện | Nguồn |
|---|---|
| `Gamification` đang bật ở cấp tổ chức | `US14` |
| Người dùng có quyền cấu hình gamification | `US15` |

### 3/ Scenario

Nhân sự vận hành mở màn cấu hình `Badges`. Đầu màn là công tắc bật tắt cả chức năng huy hiệu.

Bên dưới là bốn loại huy hiệu, mỗi loại có công tắc riêng và một danh sách mốc. Mốc là con số hệ thống định sẵn, không sửa được. Với mỗi mốc, vận hành đặt tên và chọn hình.

Ví dụ loại Course có mốc `1, 2, 4, 8, 16, 32, 64, 128`. Vận hành đặt mốc đầu tên `Newbie`, mốc thứ tư tên `Pro`, mốc cuối tên `Legend`, mỗi cái một hình riêng.

### 4/ Acceptance criteria

**UI / UX / Rule UX / Rule UI**

| Màn hình | Giao diện | Field | Yêu cầu |
|---|---|---|---|
| Cấu hình huy hiệu | Đầu màn | Công tắc `Badges` | Bật tắt cả chức năng huy hiệu. Tiêu chí lên hạng theo huy hiệu ở `US10` **khoá theo**, xem `BR-10.7` |
| Cấu hình huy hiệu | Đầu màn | Dòng giải thích dưới công tắc `Badges` | Nêu rõ tắt `Badges` thì tiêu chí lên hạng theo huy hiệu cũng ngừng. **Không có hộp xác nhận.** Chuỗi tiếng Anh: `❓BA` |
| Cấu hình huy hiệu | Đầu màn | Mô tả chức năng | `Award users with badges to highlight the milestones in their learning journey.` |
| Cấu hình huy hiệu | Bốn loại | Danh sách | `Check-in badges` (số ngày có mặt) · `Activity badges` (số hoạt động hoàn thành) · `Test badges` (số bài Test đạt) · `Course badges` (số khoá hoàn thành). Tên tiếng Anh chính xác: `❓BA` |
| Cấu hình huy hiệu | Mỗi loại | Công tắc riêng | Bật tắt riêng từng loại, không phụ thuộc ba loại còn lại |
| Cấu hình huy hiệu | Mỗi loại | Dòng tóm tắt mốc | Nêu dãy mốc của loại đó, mở đầu bằng `Awarded at`, ví dụ `Awarded at 4, 8, 16, 32, 64, 128, 256, 512 check-in days.` · `Awarded at 1, 2, 4, 8, 16, 32, 64, 128 completed courses.`<br>**Không dùng `every`**: mốc là một danh sách cố định, còn `Every` ở khối `Levels` mang nghĩa lặp lại mỗi bội số (`BR-10.2`). Huy hiệu `Check-in` đếm **số ngày**, không đếm số lần đăng nhập |
| Cấu hình huy hiệu | Từng mốc | Giá trị mốc | **Chỉ đọc.** Không sửa được, không có ô nhập. Xem `BR-9.2` |
| Cấu hình huy hiệu | Từng mốc | Tên huy hiệu | Nhập được. Có sẵn giá trị mặc định do hệ thống đặt, vận hành đổi nếu muốn. Bỏ trống thì quay về tên mặc định, không lưu trống |
| Cấu hình huy hiệu | Từng mốc | Hình huy hiệu | Chọn từ kho tài nguyên hoặc tải lên. Có sẵn hình mặc định. Định dạng, kích thước, dung lượng: `❓BA` |
| Cấu hình huy hiệu | Từng mốc | Mô tả | Nhập được, không bắt buộc. Hiện trong tooltip ở `US1` |
| Cấu hình huy hiệu | Khi loại đang tắt | Các mốc bên dưới | Không thao tác được, giữ nguyên nội dung đã đặt |
| Cấu hình huy hiệu | Thao tác không có | Tạo, xoá, thêm mốc | **Không có nút tạo huy hiệu, không có nút xoá, không thêm bớt được số mốc trong một loại** |
| Cấu hình huy hiệu | Cách lưu | | **Tự lưu, không có nút lưu.** Tên và mô tả lưu khi rời ô, hình lưu khi tải lên xong, công tắc lưu khi bấm. Theo `BR-14.10` |

**Business requirement — Business rule**

- `BR-9.1` **Bốn loại huy hiệu là danh sách cố định** ở phạm vi này. Vận hành không tạo loại mới.
- `BR-9.2` 🔑 **Giá trị mốc do hệ thống định sẵn và không sửa được.** Lý do: mốc là căn cứ đã dùng để trao huy hiệu trong quá khứ. Sửa mốc nghĩa là đổi logic của những lần trao đã xảy ra, và khi đó hoặc phải gỡ huy hiệu của người không còn đủ, hoặc để hai chuẩn cùng tồn tại. Cả hai đều hỏng.
  > ⚠️ **Hệ quả: dãy mốc chọn lúc ra mắt là vĩnh viễn.** Không sửa được về sau, nên cần cân nhắc kỹ trước khi chốt. Xem `OQ-35`.
- `BR-9.3` Vận hành đặt được **tên, hình và mô tả** cho từng mốc. Đây là phần nội dung, không phải phần logic.
- `BR-9.4` Đổi tên hoặc hình của một mốc thì **áp ngay cho cả huy hiệu học viên đã đạt**. Vẫn là cùng một huy hiệu, chỉ đổi cách hiển thị. Không phải trao lại, không sinh thông báo.
- `BR-9.5` Tắt một loại huy hiệu thì huy hiệu loại đó **biến khỏi giao diện học viên**, kể cả với người đã đạt. **Dữ liệu giữ nguyên**, bật lại thì hiện lại đầy đủ. Theo `BR-1.4a`.
- `BR-9.6` Tắt công tắc `Badges` thì **toàn bộ phần huy hiệu biến khỏi giao diện học viên**, và hệ thống **ngừng xét trao huy hiệu mới**. Tiêu chí lên hạng theo huy hiệu khoá theo, xem `BR-10.7`.
- `BR-9.7` **Không có thao tác tạo mới hoặc xoá huy hiệu.** Bộ huy hiệu là cố định, chỉ bật tắt và đổi nội dung.
- `BR-9.8` Tên và hình **luôn có giá trị**. Hệ thống đặt sẵn mặc định cho cả bốn loại và mọi mốc, nên tổ chức bật chức năng lên là dùng được ngay, không phải điền trước.

**Data Field**

| Field | Kiểu | Bắt buộc | Giá trị hợp lệ | Ghi chú |
|---|---|---|---|---|
| Chức năng huy hiệu bật hay tắt | Đúng/sai | Có | Mặc định **tắt** khi khởi tạo tổ chức | Mới |
| Mã loại huy hiệu | Danh mục | Có | Bốn giá trị cố định | Mới. Chịu `C2` |
| Loại bật hay tắt | Đúng/sai | Có | Mặc định **tắt** | Mới |
| Giá trị mốc | Số nguyên | Có | **Chỉ đọc sau khi khởi tạo** | Mới |
| Tên mốc | Chuỗi | Có | Có mặc định | Mới |
| Hình mốc | Khoá ngoại tới `resources` | Có | Có mặc định | Mới. Tài nguyên bị xoá thì rơi về hình mặc định, theo `BR-1.7` |
| Mô tả mốc | Chuỗi | Không | | Mới |
| `tenant_id` | Khoá ngoại | Có | | Ràng buộc `C1` — cấu hình gắn `tenant_id`, không đóng cứng trong mã |

**NFR**

Mỗi lần cộng điểm đều kéo theo một lần xét huy hiệu cho bốn loại. Cấu hình này đọc nhiều, cần giữ sẵn trong bộ nhớ.

### 5/ Out of scope

| Không làm ở US này | Lý do |
|---|---|
| Tạo loại huy hiệu mới ngoài bốn loại | `BR-9.1`. Loại mới cần chỉ số đếm tương ứng, là việc phát triển |
| Sửa giá trị mốc | `BR-9.2`. Đổi mốc là đổi logic quá khứ |
| Thêm hoặc bớt số mốc trong một loại | Cùng lý do với `BR-9.2` |
| Xoá huy hiệu | `BR-9.7`. Muốn ẩn thì tắt loại đó |
| Huy hiệu gắn với một nội dung cụ thể, ví dụ *"hoàn thành khoá An toàn thông tin"* | Chưa yêu cầu. Bốn loại hiện tại đều đếm số lượng, không xét nội dung nào |
| Trao huy hiệu thủ công cho một học viên | Chưa yêu cầu |

### 6/ Conner case

*(QA điền)*

---

## US10: Cấu hình hạng

```mermaid
flowchart TD
    ST["Học viên bắt đầu ở HẠNG 1"] --> CFG["Vận hành đặt 3 bội số
mỗi cái bật tắt độc lập"]
    CFG --> P["Mỗi 3.000 điểm
lên 1 hạng"]
    CFG --> Q["Mỗi 5 khoá hoàn thành
lên 1 hạng"]
    CFG --> R["Mỗi 5 huy hiệu
lên 1 hạng"]
    P --> SUM["Chạm mốc nào cũng lên 1 hạng
không cần đủ cả ba"]
    Q --> SUM
    R --> SUM
    SUM --> EX["Ví dụ: 9.000 điểm · 10 khoá · 5 huy hiệu
Hạng = 1 + 3 + 2 + 1 = HẠNG 7"]
    EX --> CAP{"Vượt trần hạng
vận hành đặt?"}
    CAP -->|"Có"| CAPPED["Dừng ở trần
ẩn thanh tiến độ"]
    CAP -->|"Không"| OK["Lên hạng mới
ghi vào lịch sử"]
    OK --> RULE["HẠNG CHỈ LÊN, KHÔNG TỤT
đổi cấu hình chỉ áp dụng
từ thời điểm đổi trở đi"]
```

*Mỗi mốc chạm được ở bất kỳ tiêu chí nào đều cho một hạng. Không phải chỉ lấy tiêu chí cao nhất.*

### 1/ User story

Là nhân sự vận hành, tôi cần đặt mỗi bao nhiêu điểm, bao nhiêu khoá, bao nhiêu huy hiệu thì học viên lên một hạng, và đặt trần hạng, để phân tầng mức độ tham gia.

### 2/ Pre - Condition

| Điều kiện | Nguồn |
|---|---|
| `Gamification` đang bật ở cấp tổ chức | `US14` |
| Người dùng có quyền cấu hình gamification | `US15` |

### 3/ Scenario

Nhân sự vận hành mở màn cấu hình `Levels`. Đầu màn là công tắc bật tắt chức năng hạng.

Bên dưới là ba tiêu chí lên hạng, mỗi tiêu chí có công tắc riêng và một ô nhập bội số: cứ mỗi bấy nhiêu điểm thì lên một hạng, cứ mỗi bấy nhiêu khoá hoàn thành thì lên một hạng, cứ mỗi bấy nhiêu huy hiệu thì lên một hạng.

Cuối màn là trần hạng, con số cao nhất học viên có thể đạt tới.

### 4/ Acceptance criteria

**UI / UX / Rule UX / Rule UI**

| Màn hình | Giao diện | Field | Yêu cầu |
|---|---|---|---|
| Cấu hình hạng | Đầu màn | Công tắc `Levels` | Bật tắt chức năng hạng |
| Cấu hình hạng | Đầu màn | Mô tả chức năng | `Levels represent the stages in a user's learning journey.` |
| Cấu hình hạng | Tiêu đề nhóm | | `Increase the user's level every` |
| Cấu hình hạng | Ba tiêu chí | `Points` | Công tắc riêng + ô nhập bội số. Cứ mỗi bấy nhiêu điểm tích luỹ thì lên một hạng. **Không thao tác được khi chức năng điểm đang tắt**, xem `BR-10.7` |
| Cấu hình hạng | Ba tiêu chí | `Completed courses` | Công tắc riêng + ô nhập bội số |
| Cấu hình hạng | Ba tiêu chí | `Badges` | Công tắc riêng + ô nhập bội số. **Không thao tác được khi chức năng huy hiệu đang tắt**, xem `BR-10.7` |
| Cấu hình hạng | Ô nhập bội số | Định dạng | Số nguyên dương, nhỏ nhất `1`. Bỏ trống thì không lưu được |
| Cấu hình hạng | Trần hạng | Ô nhập | Số nguyên dương, nhỏ nhất `2`. Bỏ trống nghĩa là **không có trần** |
| Cấu hình hạng | Tiêu chí cuối cùng | Công tắc | Khi chỉ còn **một tiêu chí đang chạy**, công tắc của nó **không tắt được**. Trỏ chuột vào thì hiện lý do: cần ít nhất một tiêu chí. Xem `BR-10.8`. Chuỗi tiếng Anh: `❓BA` |
| Cấu hình hạng | Cảnh báo | Không còn tiêu chí nào chạy | Xảy ra khi tiêu chí bị khoá do tắt `Points` hoặc `Badges`. Khối `Levels` hiện **dòng cảnh báo cố định**: học viên sẽ không lên hạng cho tới khi có lại ít nhất một tiêu chí chạy. Xem `BR-10.8`. Chuỗi tiếng Anh: `❓BA` |
| Cấu hình hạng | Cách lưu | | **Tự lưu, không có nút lưu.** Ô nhập lưu khi rời ô hoặc bấm Enter, công tắc lưu khi bấm. Theo `BR-14.10` |
| Cấu hình hạng | Đầu khối | Dòng nhắc cố định | Nêu rằng thay đổi chỉ áp từ bây giờ, hạng đã đạt giữ nguyên. **Luôn hiện**, không bật lên sau mỗi lần lưu. Chuỗi tiếng Anh: `❓BA` |

**Business requirement — Business rule**

- `BR-10.1` **Hạng bắt đầu từ `1`.** Học viên mới vào hệ thống ở hạng `1`, kể cả khi chưa có điểm nào.
- `BR-10.2` 🔑 **Mỗi lần bất kỳ tiêu chí nào chạm thêm một mốc, học viên lên một hạng ngay lúc đó.** Không cần đạt cả ba tiêu chí. Tiêu chí nào chạm mốc trước thì lên hạng trước, chạm tiếp mốc nào nữa thì lại lên tiếp.

  > **Ví dụ theo dòng thời gian.** Cấu hình: mỗi `3.000` điểm, mỗi `5` khoá, mỗi `5` huy hiệu. Lan bắt đầu ở hạng `1`.
  >
  > | Khi nào | Lan đang có | Vừa chạm mốc gì | Hạng |
  > |---|---|---|---|
  > | Tháng 1 | `1.500` điểm · **`5` khoá** · `4` huy hiệu | mốc 5 khoá | `2` |
  > | Tháng 2 | `2.000` điểm · `5` khoá · **`5` huy hiệu** | mốc 5 huy hiệu | `3` |
  > | Tháng 3 | **`3.000` điểm** · `5` khoá · `5` huy hiệu | mốc 3.000 điểm | `4` |
  > | Tháng 4 | `5.000` điểm · **`10` khoá** · `5` huy hiệu | mốc 10 khoá | `5` |
  > | Tháng 6 | **`9.000` điểm** · `10` khoá · `5` huy hiệu | mốc 6.000 rồi 9.000 điểm | `7` |
  >
  > Tính nhanh ở một thời điểm bất kỳ: **hạng = `1` + tổng số mốc đã chạm của cả ba tiêu chí.** Ở tháng 6 là `1 + 3 + 2 + 1 = 7`.
  >
  > **Không phải lấy tiêu chí cao nhất.** Nếu chỉ lấy cái cao nhất thì tháng 2 và tháng 3 Lan chạm mốc mà hạng vẫn đứng im ở `2`, vì tiêu chí khoá đang dẫn với 1 mốc. PO chốt phương án A ngày 01/10 để mọi mốc chạm được đều có tác dụng.

- `BR-10.3` **Hạng chỉ lên, không tụt.** Theo `BR-1.3`.
- `BR-10.4` Đổi bội số của một tiêu chí thì **áp dụng từ thời điểm lưu trở đi**, theo `C4`. Hạng học viên đang có **giữ nguyên**, kể cả khi theo cấu hình mới họ chưa đủ điều kiện cho hạng đó.
- `BR-10.5` **Trần hạng** là số cao nhất học viên đạt tới. Chạm trần rồi thì vượt thêm bội số nào cũng không lên nữa. Bỏ trống trần nghĩa là không giới hạn.
- `BR-10.6` Hạ trần xuống dưới hạng hiện tại của một số học viên thì những người đó **giữ nguyên hạng đang có**, theo `BR-10.3`. Chỉ người chưa chạm trần mới bị chặn ở trần mới.
- `BR-10.7` 🔗 **Tắt chức năng điểm hoặc huy hiệu thì tiêu chí lên hạng tương ứng khoá theo.**

  | Tắt gì ở đâu | Tiêu chí nào khoá |
  |---|---|
  | `Points` ở `US8` | Lên hạng theo điểm |
  | `Badges` ở `US9` | Lên hạng theo huy hiệu |

  Tiêu chí theo số khoá hoàn thành không phụ thuộc chức năng nào.

  **Khoá nghĩa là ngừng xét và không thao tác được, nhưng giá trị giữ nguyên.** Công tắc và bội số của tiêu chí không bị đổi. Bật lại chức năng nguồn thì tiêu chí chạy lại đúng như trước khi khoá, vận hành không phải bật lại bằng tay. Cùng nguyên tắc với `BR-14.7`.

  Không có hộp xác nhận khi tắt. Hệ quả nêu bằng dòng giải thích dưới công tắc `Points` và `Badges`. Hạng học viên đã đạt nhờ tiêu chí bị khoá **giữ nguyên**.
- `BR-10.8` **Tiêu chí đang chạy** là tiêu chí đang bật và không bị khoá theo `BR-10.7`. Khi `Levels` đang bật:
  - Vận hành **không tắt được tiêu chí đang chạy cuối cùng**. Muốn đổi từ tiêu chí này sang tiêu chí khác thì bật tiêu chí mới trước, rồi tắt tiêu chí cũ.
  - Tắt `Points` hoặc `Badges` mà khiến khối không còn tiêu chí nào chạy thì **vẫn cho tắt**. Khối `Levels` hiện cảnh báo cố định cho tới khi có lại ít nhất một tiêu chí chạy. Trong thời gian đó không ai lên hạng, hạng đã đạt giữ nguyên.
  > Không chặn việc tắt `Points` hay `Badges`, vì tắt cả một chức năng là quyết định lớn hơn chuyện lên hạng. Chặn ở đây thì vận hành phải vòng sang khối `Levels` gỡ trước rồi mới tắt được.
- `BR-10.9` Tắt công tắc `Levels` thì **ngừng xét lên hạng** và **hạng biến khỏi giao diện học viên**. Dữ liệu giữ nguyên, bật lại thì hiện lại. Cột `Level` cũng biến khỏi bảng xếp hạng (`US11`).

**Data Field**

| Field | Kiểu | Bắt buộc | Giá trị hợp lệ | Ghi chú |
|---|---|---|---|---|
| Chức năng hạng bật hay tắt | Đúng/sai | Có | Mặc định **tắt** khi khởi tạo tổ chức | Mới |
| Mã tiêu chí | Danh mục | Có | Ba giá trị: điểm · số khoá hoàn thành · số huy hiệu | Mới. Chịu `C2` |
| Tiêu chí bật hay tắt | Đúng/sai | Có | | Mới |
| Bội số | Số nguyên | Có | `>= 1` | Mới |
| Trần hạng | Số nguyên | Không | `>= 2`. Rỗng nghĩa là không giới hạn | Mới |
| Hạng hiện tại của học viên | Số nguyên | Có | `>= 1` | Mới. Nằm ở bảng thành tích của học viên |
| Thời điểm lên hạng gần nhất | Thời gian | Có | | Mới. Cần cho `C8` và cho sự kiện `Rank up` ở `US3` |
| `tenant_id` | Khoá ngoại | Có | | Ràng buộc `C1` — cấu hình gắn `tenant_id`, không đóng cứng trong mã |

**NFR**

Xét hạng chạy sau mỗi lần cộng điểm và sau mỗi lần trao huy hiệu. Phép tính là ba phép chia lấy phần nguyên rồi cộng lại, không cần duyệt dữ liệu.

### 5/ Out of scope

| Không làm ở US này | Lý do |
|---|---|
| **Đặt tên và hình cho từng hạng** | Hạng là một con số theo mô hình đã chốt. Yêu cầu gốc có nhắc tên và hình — xem `OQ-38` |
| Đặt ngưỡng riêng cho từng hạng, ví dụ hạng 2 cần 1000 còn hạng 3 cần 3000 | Mô hình là **bội số đều**, không phải bậc thang tuỳ ý |
| Thêm tiêu chí lên hạng ngoài ba tiêu chí | Cần chỉ số đếm tương ứng, là việc phát triển |
| Hạ hạng, hoặc đặt lại hạng thủ công cho một học viên | `BR-10.3`. Hạng chỉ lên |
| Thưởng thêm khi lên hạng, ví dụ tặng điểm | Chưa yêu cầu |

### 6/ Conner case

*(QA điền)*

---

## US11: Cấu hình bảng xếp hạng

### 1/ User story

Là nhân sự vận hành, tôi cần chọn bảng xếp hạng hiện những cột nào, để kiểm soát học viên nhìn thấy gì về nhau.

### 2/ Pre - Condition

| Điều kiện | Nguồn |
|---|---|
| `Gamification` đang bật ở cấp tổ chức | `US14` |
| Người dùng có quyền cấu hình gamification | `US15` |

### 3/ Scenario

Nhân sự vận hành mở màn cấu hình `Leaderboard`. Đầu màn là công tắc bật tắt cả bảng xếp hạng.

Bên dưới là năm công tắc chọn bảng hiện ra: hạng, điểm, số hoạt động, huy hiệu, số khoá hoàn thành. Tắt bảng nào thì học viên không thấy bảng đó.

### 4/ Acceptance criteria

**UI / UX / Rule UX / Rule UI**

| Màn hình | Giao diện | Field | Yêu cầu |
|---|---|---|---|
| Cấu hình bảng xếp hạng | Đầu màn | Công tắc `Leaderboard` | Bật tắt cả bảng xếp hạng |
| Cấu hình bảng xếp hạng | Đầu màn | Mô tả chức năng | `Leaderboards offer users an overview of their learning progress compared to everyone else's.` |
| Cấu hình bảng xếp hạng | Năm bảng | `Show levels` | Bật tắt **bảng xếp hạng theo hạng**. Chỉ có ở `All time` |
| Cấu hình bảng xếp hạng | Năm bảng | `Show points` | Bật tắt **bảng xếp hạng theo điểm** |
| Cấu hình bảng xếp hạng | Năm bảng | `Show activities` | Bật tắt **bảng xếp hạng theo số hoạt động hoàn thành** |
| Cấu hình bảng xếp hạng | Năm bảng | `Show badges` | Bật tắt **bảng xếp hạng theo số huy hiệu**. Chỉ có ở `All time` |
| Cấu hình bảng xếp hạng | Năm bảng | `Show courses` | Bật tắt **bảng xếp hạng theo số khoá hoàn thành** |
| Cấu hình bảng xếp hạng | Năm bảng | Phạm vi | Năm công tắc này chỉ áp cho bảng xếp hạng chung. **Campaign luôn có đủ hai bảng** `Points` và `Activities` (`US19`) |
| Cấu hình bảng xếp hạng | Bảng bị khoá | Khi chức năng nguồn đang tắt | Công tắc **không thao tác được** và có dòng giải thích vì sao. Ví dụ: tắt `Levels` ở `US10` thì `Show levels` khoá lại |
| Cấu hình bảng xếp hạng | Bảng cuối cùng | Công tắc | Khi chỉ còn **một bảng đang chạy**, công tắc của nó **không tắt được**. Trỏ chuột vào thì hiện lý do: cần ít nhất một bảng. Xem `BR-11.5`. Chuỗi tiếng Anh: `❓BA` |
| Cấu hình bảng xếp hạng | Cảnh báo | Không còn bảng nào chạy | Xảy ra khi các bảng đang bật đều bị khoá do chức năng nguồn tắt. Khối `Leaderboard` hiện **dòng cảnh báo cố định**: học viên không còn bảng nào để xem. Xem `BR-11.5`. Chuỗi tiếng Anh: `❓BA` |
| Cấu hình bảng xếp hạng | Cách lưu | | **Tự lưu, không có nút lưu.** Công tắc lưu khi bấm. Theo `BR-14.10` |

**Business requirement — Business rule**

- `BR-11.1` **Mỗi chỉ số là một bảng xếp hạng riêng**, bật tắt độc lập: theo hạng · theo điểm · theo số hoạt động · theo số huy hiệu · theo số khoá hoàn thành. Không phải một bảng nhiều cột.
- `BR-11.2` 🔑 **Bảng theo hạng và bảng theo số huy hiệu tự ẩn khi học viên chọn khung khác `All time`**, kể cả khi vận hành đang bật. Chỉ có ở `All time`.
  > Lý do: điểm, số hoạt động và số khoá đếm được trong một khoảng. Hạng là trạng thái tích luỹ từ ngày đầu, đặt vào một khoảng thì không có nghĩa. Huy hiệu có mốc tăng gấp đôi, đếm trong một khoảng thì người mới luôn lợi hơn người cũ — xem `BR-6.2b`.
- `BR-11.3` Học viên **chuyển giữa các bảng đang bật**. Bảng nào tắt thì không xuất hiện trong danh sách chọn. Bảng mặc định khi mở trang là bảng theo điểm.
- `BR-11.4` **Bảng phụ thuộc vào chức năng sinh ra nó.** Tắt chức năng ở màn khác thì bảng tương ứng khoá lại và không hiện:

  | Tắt gì ở đâu | Bảng nào khoá |
  |---|---|
  | `Points` ở `US8` | Bảng theo điểm |
  | `Badges` ở `US9` | Bảng theo huy hiệu |
  | `Levels` ở `US10` | Bảng theo hạng |

  Bảng theo số hoạt động và bảng theo số khoá hoàn thành **không phụ thuộc chức năng nào**. Hai chỉ số này đếm không phụ thuộc công tắc `Points`, theo mục Định nghĩa chỉ số.
- `BR-11.5` **Bảng đang chạy** là bảng đang bật và không bị khoá theo `BR-11.4`. Khi `Leaderboard` đang bật:
  - Vận hành **không tắt được bảng đang chạy cuối cùng**.
  - Tắt một chức năng nguồn mà khiến khối không còn bảng nào chạy thì **vẫn cho tắt**. Khối `Leaderboard` hiện cảnh báo cố định cho tới khi có lại ít nhất một bảng chạy. Cùng cách xử lý với `BR-10.8`.
- `BR-11.6` Tắt công tắc `Leaderboard` thì **toàn bộ trang bảng xếp hạng biến khỏi UpLMS**, gồm cả khối vị trí của tôi ở `US7`. Dữ liệu điểm vẫn ghi bình thường.
- `BR-11.7` Đổi cấu hình cột **áp dụng ngay ở lần học viên mở trang tiếp theo**. Không phải chờ chu kỳ tính lại 8 tiếng, vì đây là thay đổi hiển thị chứ không phải thay đổi số liệu.

**Data Field**

| Field | Kiểu | Bắt buộc | Giá trị hợp lệ | Ghi chú |
|---|---|---|---|---|
| Bảng xếp hạng bật hay tắt | Đúng/sai | Có | Mặc định **tắt** khi khởi tạo tổ chức | Mới |
| Hiện cột hạng | Đúng/sai | Có | | Mới |
| Hiện cột điểm | Đúng/sai | Có | | Mới |
| Hiện cột huy hiệu | Đúng/sai | Có | | Mới |
| Hiện cột số hoạt động | Đúng/sai | Có | | Mới |
| Hiện cột số khoá | Đúng/sai | Có | | Mới |
| `tenant_id` | Khoá ngoại | Có | | Ràng buộc `C1` — cấu hình gắn `tenant_id`, không đóng cứng trong mã |

**NFR**

Cấu hình này chỉ ảnh hưởng hiển thị, không ảnh hưởng việc tính toán. Bảng vẫn tính đủ năm chỉ số theo chu kỳ 8 tiếng, chỉ là hiện ra hay không.

> Cách này tốn thêm chút tính toán cho cột đang tắt, đổi lại bật cột lên là có số liệu ngay, không phải chờ chu kỳ sau.

### 5/ Out of scope

| Không làm ở US này | Lý do |
|---|---|
| Đổi thứ tự các bảng trong danh sách chọn | Chưa yêu cầu |
| Cấu hình riêng cho từng nhóm học viên | Chờ chức năng nhóm. Xem `US16 — chưa làm` |
| Đặt số người hiện ở phần nổi bật, hiện đang cố định là top 3 | Chưa yêu cầu |
| Đổi chu kỳ tính lại bảng, đang cố định 8 tiếng | Chưa yêu cầu. Xem `BR-6.12` |
| Ẩn tên hoặc ảnh học viên trên bảng | PO chốt bảng công khai danh tính, theo `BR-6.9` |

### 6/ Conner case

*(QA điền)*

---

## US12: Danh sách học viên và hạng

### 1/ User story

Là nhân sự vận hành, tôi cần xem danh sách học viên kèm hạng của họ, để nắm tình hình chung.

### 2/ Pre - Condition

| Điều kiện | Nguồn |
|---|---|
| `Gamification` đang bật ở cấp tổ chức | `US14` |
| Người dùng có quyền xem dữ liệu gamification | `US15` |

### 3/ Scenario

Nhân sự vận hành mở danh sách học viên trong khu vực Gamification trên Ops. Danh sách hiện mọi học viên của tổ chức kèm hạng, điểm tích luỹ, số huy hiệu và số khoá hoàn thành.

Vận hành tìm theo tên, sắp xếp theo cột bất kỳ, và xem theo trang.

### 4/ Acceptance criteria

**UI / UX / Rule UX / Rule UI**

| Màn hình | Giao diện | Field | Yêu cầu |
|---|---|---|---|
| Danh sách học viên | Bảng | Cột `Learner` | Ảnh đại diện và tên học viên |
| Danh sách học viên | Bảng | Cột `Level` | Số hạng hiện tại. Ẩn cột nếu chức năng hạng đang tắt |
| Danh sách học viên | Bảng | Cột `Points` | Điểm tích luỹ toàn thời gian. Ẩn cột nếu chức năng điểm đang tắt |
| Danh sách học viên | Bảng | Cột `Badges` | Số huy hiệu đã đạt. Ẩn cột nếu chức năng huy hiệu đang tắt |
| Danh sách học viên | Bảng | Cột `Activities` | Số hoạt động hoàn thành. Luôn hiện |
| Danh sách học viên | Bảng | Cột `Courses` | Số khoá hoàn thành. Luôn hiện |
| Danh sách học viên | Bảng | Cột `Last activity` | Ngày gần nhất học viên có mặt trong hệ thống. Chưa vào lần nào thì để trống |
| Danh sách học viên | Chọn khoảng ngày | Cách chọn | Bộ chọn khoảng ngày tự do, kèm nút nhanh `All time` · `This week` · `This month` · `This quarter` · `This year`. Mặc định `All time` |
| Danh sách học viên | Chọn khoảng ngày | Ảnh hưởng tới cột | Chọn một khoảng cụ thể thì `Points`, `Activities`, `Courses` tính **trong khoảng đó**, còn cột `Level` và `Badges` **ẩn đi**, cùng lý do với `BR-11.2` |
| Danh sách học viên | Xuất file | Nút `Export` | Xuất đúng danh sách đang hiện, theo khoảng ngày và thứ tự sắp xếp hiện tại. **Định dạng Excel** |
| Danh sách học viên | Xuất file | Nội dung | Gồm mọi dòng của kết quả lọc hiện tại, không chỉ trang đang xem |
| Danh sách học viên | Tìm kiếm | Theo tên | Một ô tìm theo tên học viên |
| Danh sách học viên | Sắp xếp | Theo cột | Bấm tiêu đề cột để sắp xếp. Mặc định sắp theo hạng giảm dần |
| Danh sách học viên | Phân trang | Số dòng mỗi trang | Theo chuẩn các màn danh sách khác của Ops |
| Danh sách học viên | Thao tác | | **Chỉ đọc.** Không có nút sửa, không có nút xoá, không mở được chi tiết để chỉnh |
| Danh sách học viên | Trạng thái rỗng | Chưa có học viên nào | Theo chuẩn màn danh sách của Ops |

**Business requirement — Business rule**

- `BR-12.1` Màn này **chỉ đọc**. Vận hành không sửa hạng, không cộng trừ điểm, không trao hay gỡ huy hiệu thủ công. Theo `A12`.
- `BR-12.2` Hiện **mọi học viên của tổ chức**, kể cả người chưa có điểm nào. Người chưa có gì thì các cột số hiện `0`.
- `BR-12.3` Tài khoản có `Test Account = Yes` **không xuất hiện**, theo `C10`.
- `BR-12.4` **Có bộ lọc khoảng ngày tự do**, mặc định toàn thời gian. Chọn một khoảng cụ thể thì điểm, số hoạt động và số khoá tính trong khoảng đó, còn **cột hạng và cột huy hiệu ẩn đi**, cùng lý do với `BR-11.2`.
  > Vận hành giữ được bộ chọn tự do dù học viên không có (`BR-6.15`): người dùng Ops ít, phải có quyền, và mục tiêu `O4` cần lấy số liệu khoảng bất kỳ.
- `BR-12.8` 🆕 **Xuất file theo khoảng ngày đang chọn.** Đây là cách đội truyền thông lấy số liệu để công bố và trao thưởng ngoài hệ thống.
  > File xuất ra là **bản ghi lại tại thời điểm xuất**. Vì số liệu là sống (`BR-6.10`), xuất lại cùng khoảng ngày vào lúc khác có thể ra kết quả khác. Bên công bố cần giữ file đã xuất làm căn cứ.
- `BR-12.5` Số liệu đọc **thẳng từ bản ghi thành tích của học viên**, nên **cập nhật tức thì**, không chờ chu kỳ 8 tiếng như bảng xếp hạng.
  > Hai màn hiển thị hai con số có thể lệch nhau trong vòng 8 tiếng. Đây là chủ đích: bảng xếp hạng cần ổn định để học viên không thấy thứ hạng nhảy liên tục, còn vận hành cần số đúng tại thời điểm tra.
- `BR-12.6` Cột ẩn theo chức năng đang tắt, cùng nguyên tắc với `BR-11.4`. Chức năng tắt thì con số không còn được cập nhật, hiện ra sẽ gây hiểu nhầm.
- `BR-12.7` Học viên bị `Block` hoặc đã rời tổ chức **không xuất hiện**, cùng quy tắc với bảng xếp hạng ở `BR-6.8`.

**Data Field**

Không có field mới. Màn này đọc từ bản ghi thành tích của học viên đã có ở `US1`, `US3`, `US10`, cộng thêm ngày có mặt gần nhất từ bảng ở `US5`.

**NFR**

Danh sách đọc theo trang. Không tính lại hạng hay đếm lại huy hiệu khi mở màn, chỉ đọc giá trị đã lưu.

### 5/ Out of scope

| Không làm ở US này | Lý do |
|---|---|
| Sửa hạng, cộng trừ điểm, trao huy hiệu thủ công | `BR-12.1`. Nếu sau này cần thì là một US riêng, và phải xử lý cả việc ghi vào lịch sử |
| Xem lịch sử ghi nhận của một học viên cụ thể | Chưa yêu cầu. Học viên tự xem ở `US3` |
| Lọc theo lớp, khoá, phòng ban | Chờ chức năng nhóm. Xem `US16 — chưa làm` |

### 6/ Conner case

*(QA điền)*

---

## US13: Điểm phản ánh việc học thật

```mermaid
flowchart TD
    S["Bản ghi tiến độ chuyển<br/>trạng thái sang hoàn thành"] --> T1{"Test Account?"}
    T1 -->|"Có"| X1["Bỏ qua hoàn toàn<br/>không ghi gì"]
    T1 -->|"Không"| T2{"Gamification bật?"}
    T2 -->|"Tắt"| X2["Không ghi nhận"]
    T2 -->|"Bật"| T3{"Hành động này<br/>bật tính điểm?"}
    T3 -->|"Tắt"| X3["Không cộng điểm"]
    T3 -->|"Bật"| T4{"Đã cộng điểm<br/>nội dung này<br/>trong lượt học này?"}
    T4 -->|"Rồi"| X4["Không cộng lại<br/>chống cộng trùng theo C5"]
    T4 -->|"Chưa"| W["Cộng điểm<br/>ghi sổ giao dịch"]
    W --> B1["Xét huy hiệu"]
    B1 --> B2["Xét hạng"]
```

*Năm cửa kiểm trước khi cộng một điểm. Trượt ở cửa nào thì dừng ở đó.*

### 1/ User story

Là nhân sự vận hành, tôi cần điểm phản ánh việc học thật, không bị đẩy lên bằng thao tác đối phó, để cơ chế còn đáng tin.

> US này **không có màn hình riêng và không có tham số cấu hình nào**. Nó gom các quy tắc chạy ngầm bảo vệ tính đúng đắn của điểm, trải suốt cả tính năng.
>
> Đây là US giữ cho `O5` đứng vững: *điểm số đáng tin, mỗi con số truy được nguồn và không bị thổi lên bằng thao tác đối phó*.

### 2/ Pre - Condition

| Điều kiện | Nguồn |
|---|---|
| `Gamification` đang bật và cơ chế điểm đang bật | `US8` · `US14` |

### 3/ Scenario

Học viên hoàn thành một hoạt động. Trước khi cộng điểm, hệ thống kiểm ba điều: nội dung này đã trả điểm cho học viên trong lượt ghi danh hiện tại chưa, bản ghi tiến độ có thật sự vừa chuyển sang hoàn thành không, và tài khoản có phải tài khoản kiểm thử không.

Qua hết ba cửa thì cộng điểm. Vướng cửa nào thì không cộng và không ghi gì vào lịch sử.

### 4/ Acceptance criteria

**UI / UX / Rule UX / Rule UI**

**US này không lộ ra ở màn nào.** Toàn bộ là quy tắc chạy ngầm, và sau khi bỏ trần điểm ngày thì cũng không còn tham số nào để vận hành cấu hình.

**Business requirement — Business rule**

**Ba cửa kiểm trước khi cộng điểm**

- `BR-13.1` **Chống cộng trùng nội dung.** Mỗi nội dung chỉ trả điểm **một lần trong một lượt ghi danh**. Học viên mở lại hoạt động đã hoàn thành thì không cộng thêm.
- `BR-13.2` **Chỉ cộng khi chuyển trạng thái.** Điểm chỉ sinh ra khi bản ghi tiến độ **chuyển từ chưa hoàn thành sang hoàn thành**, và chỉ tính các lần chuyển xảy ra **từ thời điểm bật tính năng trở đi**.
  > Đây là rule thay cho việc phải nạp sẵn dữ liệu chống cộng trùng khi ra mắt. Nội dung học viên đã hoàn thành từ trước không chuyển trạng thái nữa nên không phát sinh điểm, kể cả khi họ mở lại vào ngày đầu tiên.
- `BR-13.4` **Loại trừ tài khoản kiểm thử.** Tài khoản có `Test Account = Yes` không phát sinh điểm, và **lọc ngay từ tầng ghi nhận**, không ghi rồi lọc sau. Theo `C10`.

**Chống cộng trùng khi thao tác song song**

- `BR-13.5` Học viên mở hai thiết bị hoặc hai tab và hoàn thành cùng một hoạt động gần như đồng thời thì **chỉ cộng điểm một lần**. Việc kiểm và ghi phải là một thao tác không tách rời.
  > Điểm cộng ngay trong luồng (`Option C`) nên hai thao tác song song đều có thể chạy tới bước cộng điểm cùng lúc. Nếu chỉ dựa vào chống cộng trùng ở `BR-13.1` thì cả hai đều thấy "chưa trả điểm" và cùng cộng.
- `BR-13.6` Với **điểm khi vào hệ thống hằng ngày**, ràng buộc một học viên một ngày một bản ghi ở `US5` đã tự chặn trùng. Không cần cơ chế thêm.

**Khi cộng điểm gặp lỗi**

- `BR-13.7` Lỗi ở phần cộng điểm **không được làm hỏng thao tác học**, theo `NFR-GAM-01`. Học viên bấm Hoàn thành thì thao tác đó phải thành công.
- `BR-13.8` ✅ Lỗi bị chặn lại thì **ghi lại chỗ lỗi để vận hành thấy và xử lý**, không để mất âm thầm. Học viên học thật mà không có điểm và không ai giải thích được là đúng thứ `O5` muốn tránh. PO chốt 23/09.

**Những gì KHÔNG chặn, có chủ đích**

- `BR-13.9` Hoạt động chỉ có **Text hoặc Ảnh** được tính hoàn thành ngay khi mở hiển thị, theo `KB-LX-03b`. Học viên bấm lướt vẫn nhận điểm. **Không làm cơ chế chống cày riêng cho loại này.**
  > Rủi ro chấp nhận có chủ đích. Thiệt hại bị chặn bởi hai lớp: chống cộng trùng khiến mỗi nội dung chỉ trả điểm một lần, và trần ngày chặn việc dồn toàn bộ trong một buổi. Hoạt động chứa Video đã chặt sẵn vì phải xem đủ 80% thời lượng (`KB-LX-03a`).
- `BR-13.10` **Học viên bị xoá khỏi lớp rồi thêm lại thì lượt học mới được tính điểm mới**, cho cả hoàn thành hoạt động lẫn hoàn thành khoá. Coi như một khoá mới.

  Vận hành thêm lại học viên vào lớp thì chọn **ghi nhận đã xong khoá** hoặc **học lại từ đầu**. Chọn ghi nhận đã xong thì không có tiến độ nào chuyển trạng thái, nên **không phát sinh điểm nào**.

  Việc này cần thao tác của vận hành nên không phải đường cày điểm tự phục vụ.
- `BR-13.12` 🔑 **Chứng chỉ cấp theo KHOÁ, không theo lượt ghi danh.** Một học viên chỉ nhận **một chứng chỉ cho một khoá**, dù học lại bao nhiêu lần. Xoá khỏi lớp thì chứng chỉ vẫn còn.

  > ⚠️ **Hệ quả quan trọng cho Dev: chỉ số "số khoá hoàn thành" KHÔNG đếm bằng số chứng chỉ.**
  >
  > Học viên hoàn thành khoá A hai lần thì được điểm hai lần (`BR-13.10`) nhưng chỉ có một chứng chỉ. Nếu đếm bằng chứng chỉ thì con số sẽ thấp hơn thực tế và lệch với điểm đã cộng.
  >
  > Chỉ số này đếm **số lượt hoàn thành khoá** trong sổ giao dịch điểm, không đếm chứng chỉ.
- `BR-13.11` Học viên **không tự huỷ ghi danh được** sau khi đã học ít nhất một hoạt động, theo `KB-LX-08`. Đường cày điểm ghi danh rồi huỷ rồi ghi danh lại **đã bị hệ thống chặn sẵn**, không cần làm gì thêm.

**Data Field**

Không có field mới. US này dùng ba thứ đã khai ở nơi khác:

| Cần gì | Ở đâu |
|---|---|
| Dấu nội dung đã tính điểm | Bảng chống cộng trùng, `US3` |
| Tổng điểm đã nhận trong ngày | Tính từ sổ giao dịch điểm theo ngày, `US3` |

**NFR**

Bốn cửa kiểm chạy trong cùng thao tác với việc hoàn thành hoạt động, nên phải nhẹ. Việc tính tổng điểm đã nhận trong ngày cần tránh quét lại toàn bộ sổ giao dịch mỗi lần.

### 5/ Out of scope

| Không làm ở US này | Lý do |
|---|---|
| Đo thời gian học viên ở lại một hoạt động | `BR-13.9`. Đo thời gian là sửa logic hoàn thành, điều PO chốt không làm |
| Phát hiện hành vi bất thường và cảnh báo vận hành | Chưa yêu cầu |
| Thu hồi điểm đã cộng khi phát hiện gian lận | Chưa yêu cầu. Cũng mâu thuẫn với `BR-3.5` — lịch sử không sửa được |
| Trần điểm mỗi ngày, mỗi tuần hoặc mỗi tháng | Bỏ theo `CR-010`. Chống cộng trùng (`BR-13.1`) đã chặn việc lặp lại cùng một nội dung |

### 6/ Conner case

*(QA điền)*

---

## US14: Bật tắt gamification và hiển thị

```mermaid
flowchart LR
    T["TẮT HẲN<br/>Gamification = OFF<br/>Không ghi nhận gì<br/>Học viên không thấy gì"]
    N["CHẠY NGẦM<br/>Gamification = ON<br/>Visibility = OFF<br/>CÓ ghi nhận điểm<br/>Học viên chưa thấy"]
    M["MỞ ĐẦY ĐỦ<br/>Gamification = ON<br/>Visibility = ON<br/>Ghi nhận và hiển thị"]
    T -->|"bật Gamification"| N
    N -->|"bật Visibility"| M
    M -->|"tắt Visibility"| N
    N -->|"tắt Gamification"| T
    M -->|"tắt Gamification, tắt luôn Visibility"| T
    NOTE["Bật Visibility thì học viên thấy ngay<br/>điểm đã tích được trong lúc chạy ngầm.<br/>KHÔNG có tính bù cho giai đoạn<br/>trước khi bật Gamification."]
    N -.-> NOTE
```

*Ba trạng thái và đường đi giữa chúng. Chạy ngầm là trạng thái để chạy thử trước khi mở cho học viên.*

### 1/ User story

Là nhân sự vận hành, tôi cần bật tắt gamification và bật tắt hiển thị phía học viên riêng biệt, để chạy thử cơ chế trước khi mở cho học viên.

### 2/ Pre - Condition

| Điều kiện | Nguồn |
|---|---|
| Người dùng có quyền cấu hình gamification | `US15` |

### 3/ Scenario

Nhân sự vận hành mở màn cấu hình chung của Gamification. Có hai công tắc xếp theo tầng.

Công tắc thứ nhất bật tắt cả cơ chế. Bật lên thì hệ thống bắt đầu ghi nhận và tính điểm, nhưng học viên chưa thấy gì. Công tắc thứ hai xuất hiện, quyết định học viên có nhìn thấy hay không.

Cách dùng thông thường: bật công tắc thứ nhất, chạy ngầm hai tới bốn tuần, xem phân bố điểm thật, chỉnh cấu hình, rồi mới bật công tắc thứ hai.

### 4/ Acceptance criteria

**UI / UX / Rule UX / Rule UI**

| Màn hình | Giao diện | Field | Yêu cầu |
|---|---|---|---|
| Cấu hình chung | Công tắc 1 | `Gamification` | Bật tắt cả cơ chế. Tắt thì ngừng ghi nhận và ngừng hiển thị |
| Cấu hình chung | Công tắc 2 | `Visibility in UpLMS` | **Chỉ xuất hiện khi công tắc 1 đang bật.** Quyết định học viên có nhìn thấy gamification hay không |
| Cấu hình chung | Công tắc 2 | Dòng giải thích | Nêu rõ tắt công tắc này thì hệ thống **vẫn ghi nhận bình thường**, chỉ là học viên không thấy. Dòng này cùng hai công tắc là đủ để đọc ra trạng thái hiện tại, **không có nhãn trạng thái riêng**: `Show points, badges and ranks to your users. While this is off, they still accrue but stay hidden.` |
| Cấu hình chung | Xác nhận khi tắt công tắc 1 | Hình thức | **Popover nhỏ gắn cạnh công tắc**, không phải modal. Huỷ thì công tắc về như cũ, không lưu. Xem `BR-14.13` |
| Cấu hình chung | Xác nhận khi tắt công tắc 1 | Nội dung | Nêu rõ: ngừng ghi nhận mọi thứ, bốn chức năng con khoá lại, dữ liệu đã có giữ nguyên, và **bật lại sẽ tính từ thời điểm bật chứ không tính bù**. Có campaign đang chạy thì nêu thêm số campaign, và campaign không nhận thêm gì trong thời gian tắt (`BR-20.8`). Chuỗi tiếng Anh: `❓BA` |
| Cấu hình chung | Xác nhận khi bật công tắc 2 lần đầu | Hình thức | Popover như trên |
| Cấu hình chung | Xác nhận khi bật công tắc 2 lần đầu | Nội dung | Nêu rõ học viên sẽ **thấy ngay toàn bộ điểm, hạng và huy hiệu đã tích trong giai đoạn chạy ngầm**, và hệ thống **không gửi thông báo hồi tố**. Chuỗi tiếng Anh: `❓BA` |
| Cả trang cấu hình | Cách lưu | | **Tự lưu, không có nút lưu**, áp cho cả `US8` đến `US11`. Xem `BR-14.10` đến `BR-14.12` |
| Cả trang cấu hình | Sau mỗi lần lưu | Báo đã lưu | Báo nhỏ `Saved`, tự ẩn, **không phải modal** |

**Business requirement — Business rule**

- `BR-14.1` **Hai công tắc cho ba trạng thái:**

  | Trạng thái | `Gamification` | `Visibility in UpLMS` | Hệ thống làm gì |
  |---|---|---|---|
  | **Tắt hẳn** | Tắt | *(không hiện)* | Không ghi nhận, không hiển thị |
  | **Chạy ngầm** | Bật | Tắt | **Ghi nhận đầy đủ**, học viên không thấy gì |
  | **Bật đầy đủ** | Bật | Bật | Ghi nhận và hiển thị |

- `BR-14.2` Công tắc `Visibility in UpLMS` **chỉ tồn tại khi `Gamification` đang bật**. Tắt công tắc 1 thì công tắc 2 biến mất khỏi giao diện, giá trị của nó giữ nguyên để lần sau bật lại vẫn như cũ.
- `BR-14.3` Ở trạng thái **chạy ngầm**, hệ thống ghi nhận đầy đủ: cộng điểm, trao huy hiệu, xét hạng, tính bảng xếp hạng. Chỉ có ba thứ không xảy ra: học viên không thấy trang thành tích, không thấy bảng xếp hạng, và **không nhận thông báo** (`A19`).
- `BR-14.4` 🔑 Chuyển từ **chạy ngầm** sang **bật đầy đủ** thì **không bắn thông báo hồi tố**. Học viên thấy ngay điểm, hạng và huy hiệu đã tích, kèm lịch sử để tra nguồn. Không có thông báo nào cho những gì đã xảy ra trong giai đoạn chạy ngầm.
  > Không có rule này thì mỗi học viên nhận hàng trăm thông báo cùng lúc vào đúng ngày ra mắt.
- `BR-14.5` Bật lại sau khi **tắt hẳn** thì **tính từ thời điểm bật trở đi**. Giai đoạn tắt không ghi gì nên không có gì để bù. Dữ liệu trước khi tắt giữ nguyên và hiện lại đầy đủ.
- `BR-14.6` **Mặc định khi khởi tạo một tổ chức mới là tắt hẳn.** Tổ chức chủ động bật khi sẵn sàng.
- `BR-14.7` Tắt `Gamification` thì **bốn công tắc chức năng ở `US8` đến `US11` khoá lại**, giữ nguyên mọi giá trị đã cấu hình. Bật lại thì trở về đúng cấu hình cũ.
- `BR-14.8` Hai công tắc này **gắn với tổ chức** (`C1`). Đợt này chỉ có một tổ chức nên không cần màn quản lý nhiều tổ chức, nhưng dữ liệu phải thiết kế theo tổ chức ngay từ đầu.
- `BR-14.9` **Múi giờ tổ chức** quyết định biên ngày cho điểm check-in và chuỗi (`US5`), và biên khoảng cho bảng xếp hạng (`US6`). Không dùng giờ máy chủ và không dùng múi giờ thiết bị của học viên.
  > Múi giờ **lấy theo tenant**, không có ô chọn trên màn Gamification. Cách lưu do BE quyết trong technical design. Tham số này thuộc **hồ sơ tổ chức** trong module Tenant (`TNT.CFG.02`).

**Cách lưu trên trang cấu hình — áp cho cả `US8` đến `US11`**

- `BR-14.10` 🔑 **Trang cấu hình tự lưu, không có nút lưu.**

  | Thành phần | Lưu khi nào |
  |---|---|
  | Ô nhập số | **Rời ô hoặc bấm Enter.** Không lưu trong lúc đang gõ, kể cả khi người dùng dừng tay giữa chừng |
  | Tên và mô tả huy hiệu | Rời ô |
  | Hình huy hiệu | Tải lên xong |
  | Công tắc | Bấm là lưu, trừ hai trường hợp ở `BR-14.13` |

  > **Vì sao không lưu trong lúc gõ.** Cấu hình có hiệu lực ngay khi lưu và không tính lại quá khứ (`C4`). Ví dụ vận hành đổi bội số lên hạng từ `3000` thành `5000`: xoá hết rồi gõ `5`. Nếu lưu ngay lúc đó thì cấu hình thành *"mỗi 5 điểm lên 1 hạng"*, học viên nào được cộng điểm đúng lúc ấy nhảy thẳng lên trần hạng. Hạng không tụt (`BR-10.3`) nên không sửa lại được.
- `BR-14.11` Giá trị không hợp lệ thì **không lưu**, báo lỗi ngay tại ô. Rời trang khi ô đang lỗi thì ô quay về giá trị đã lưu gần nhất. Riêng tên huy hiệu bỏ trống thì quay về tên mặc định, theo `US9`.
- `BR-14.12` Lưu xong thì hiện báo nhỏ `Saved`. Lưu lỗi thì ô quay về giá trị đã lưu gần nhất và báo lỗi. **Không có cảnh báo khi rời trang**, vì không có thay đổi nào nằm chờ lưu.
- `BR-14.13` Chỉ **hai thao tác** phải xác nhận trước khi lưu, dạng **popover nhỏ gắn cạnh công tắc**, không phải modal:

  | Thao tác | Vì sao phải hỏi lại |
  |---|---|
  | Tắt `Gamification` | Thời gian tắt không được ghi nhận và không tính bù (`BR-14.5`). Bấm nhầm là để lại khoảng trống dữ liệu vĩnh viễn cho cả tổ chức |
  | Bật `Visibility in UpLMS` lần đầu | Là thời điểm ra mắt: toàn bộ học viên thấy ngay mọi thứ đã tích (`BR-14.4`) |

  Hai thao tác này gần như chỉ xảy ra một lần trong vòng đời tính năng, nên hỏi lại không gây phiền. Các công tắc khác **không hỏi lại**, hệ quả nêu bằng dòng giải thích dưới công tắc.

**Data Field**

| Field | Kiểu | Bắt buộc | Giá trị hợp lệ | Ghi chú |
|---|---|---|---|---|
| `Gamification` bật hay tắt | Đúng/sai | Có | Mặc định **tắt** | Mới |
| `Visibility in UpLMS` bật hay tắt | Đúng/sai | Có | Mặc định **tắt** | Mới |
| Múi giờ tổ chức | Múi giờ | Có | Chuẩn múi giờ quốc tế | **Lấy theo tenant**, không nhập trên màn này. Cách lưu do BE quyết trong technical design |
| `tenant_id` | Khoá ngoại | Có | | Ràng buộc `C1` — cấu hình gắn `tenant_id`, không đóng cứng trong mã |

**NFR**

Hai công tắc này đọc ở gần như mọi thao tác của gamification. Cần giữ sẵn trong bộ nhớ thay vì đọc lại mỗi lần.

### 5/ Out of scope

| Không làm ở US này | Lý do |
|---|---|
| Màn quản lý nhiều tổ chức | Chưa có multi-tenant. Dữ liệu vẫn thiết kế theo tổ chức |
| Lên lịch bật tắt vào một thời điểm định trước | Chưa yêu cầu |
| Bật gamification cho một nhóm học viên thử nghiệm trước | Chờ chức năng nhóm. Xem `US16 — chưa làm` |
| Xoá toàn bộ dữ liệu gamification khi tắt | Tắt là ngừng ghi, không xoá |
| Khai đầy đủ hồ sơ tổ chức theo `TNT.CFG.02` | Thuộc module Tenant |
| Chọn múi giờ trên màn Gamification | Múi giờ lấy theo tenant, xem `BR-14.9` |
| Nhãn trạng thái tổng *(tắt hẳn · chạy ngầm · bật đầy đủ)* | Hai công tắc cùng dòng giải thích của `Visibility in UpLMS` đã đủ để đọc ra trạng thái |
| Nút lưu · cảnh báo rời trang khi chưa lưu | Trang tự lưu, xem `BR-14.10` |

### 6/ Conner case

*(QA điền)*

---

## US15: Phân quyền cấu hình gamification

### 1/ User story

Là quản trị, tôi cần phân quyền để chỉ vai trò vận hành phù hợp mới sửa được cấu hình gamification.

### 2/ Pre - Condition

| Điều kiện | Nguồn |
|---|---|
| Hệ phân quyền hiện có của Ops đang hoạt động | KB `06` · bảng `casbin_rule` |
| Người dùng có quyền quản trị phân quyền | Cơ chế hiện có |

### 3/ Scenario

Quản trị mở màn phân quyền hiện có của Ops. Trong danh sách quyền xuất hiện nhóm quyền mới cho Gamification.

Quản trị gán quyền cho vai trò phù hợp. Vai trò không có quyền thì không thấy khu vực Gamification trong menu Ops.

### 4/ Acceptance criteria

**UI / UX / Rule UX / Rule UI**

| Màn hình | Giao diện | Field | Yêu cầu |
|---|---|---|---|
| Phân quyền (màn hiện có) | Danh sách quyền | Nhóm `Gamification` | Xuất hiện như một nhóm quyền mới. **Không làm màn phân quyền riêng** |
| Phân quyền (màn hiện có) | Quyền | `Xem cấu hình gamification` | Mở được trang cấu hình và danh sách học viên, nhưng không sửa được |
| Phân quyền (màn hiện có) | Quyền | `Sửa cấu hình gamification` | Sửa được cả bốn khối cấu hình ở `US8` đến `US11`, công tắc chung ở `US14`, và **tạo, sửa, xoá campaign** ở `US20`. `[đề xuất]` dùng chung quyền này cho campaign |
| Phân quyền (màn hiện có) | Quyền | `Xem danh sách học viên và hạng` | Mở được màn ở `US12` và xuất file. Xem và xuất **kết quả campaign** ở `US21`. `[đề xuất]` |
| Menu Ops | Khu vực Gamification | Hiển thị | Không có quyền xem thì **không thấy khu vực này trong menu**, và mở thẳng đường dẫn cũng không vào được |

**Business requirement — Business rule**

- `BR-15.1` Thêm nhóm quyền mới vào **hệ phân quyền hiện có**, không dựng cơ chế riêng và không làm màn riêng.
- `BR-15.2` **Tách quyền xem và quyền sửa.** Cấu hình gamification ảnh hưởng tới điểm của toàn bộ học viên, nên cần có vai trò xem được để đối chiếu mà không sửa được.
- `BR-15.3` Không có quyền xem thì khu vực Gamification **không xuất hiện trong menu Ops**, và mở thẳng đường dẫn cũng không vào được.
- `BR-15.4` Phân quyền này **chỉ áp cho Ops**. Học viên trên UpLMS không chịu ảnh hưởng: khi `Visibility in UpLMS` bật thì mọi học viên đều thấy phần của mình và thấy bảng xếp hạng.
- `BR-15.5` **L&D, Mentor, Giáo viên là vai trò trong Ops như mọi vai trò khác.** Họ thấy được gì hoàn toàn do quản trị gán quyền, không có xử lý riêng cho từng vai trò.
- `BR-15.6` Đổi quyền có hiệu lực theo đúng cơ chế của hệ phân quyền hiện có. Gamification không tự làm khác.

**Data Field**

Không có field mới. Dùng cấu trúc phân quyền hiện có, chỉ thêm bản ghi cho ba quyền mới.

**NFR**

Không có yêu cầu riêng. Theo chuẩn của hệ phân quyền hiện có.

### 5/ Out of scope

| Không làm ở US này | Lý do |
|---|---|
| Làm màn phân quyền riêng cho gamification | `BR-15.1`. Dùng màn hiện có |
| Phân quyền tới từng khối cấu hình, ví dụ chỉ sửa được huy hiệu mà không sửa được điểm | Chưa yêu cầu. Cả bốn khối dùng chung một quyền sửa |
| Quy trình duyệt trước khi cấu hình có hiệu lực | Chưa yêu cầu |
| Ghi lại ai đã đổi cấu hình gì | PO chốt không cần, xem `OQ-34` |

### 6/ Conner case

*(QA điền)*

---

## US19: Campaign trong bảng xếp hạng

```mermaid
flowchart LR
    S["Sổ giao dịch điểm<br/>đã có, không ghi thêm"] --> F1{"Thời điểm cộng<br/>trong khoảng campaign?"}
    F1 -->|"Có"| F2{"Loại hành động<br/>campaign có chọn?"}
    F1 -->|"Không"| X["Không tính"]
    F2 -->|"Có"| P["Bảng Points<br/>của campaign"]
    F2 -->|"Không"| X
    A["Hoàn thành hoạt động<br/>trong lúc Gamification bật"] --> F3{"Trong khoảng<br/>campaign?"}
    F3 -->|"Có"| AC["Bảng Activities<br/>của campaign"]
    F3 -->|"Không"| X
    P --> R{"Campaign<br/>đã kết thúc?"}
    AC --> R
    R -->|"Chưa"| L["Tính sẵn 8 tiếng một lần<br/>số tạm tính"]
    R -->|"Rồi"| Z["Đóng băng<br/>kết quả chính thức"]
```

*Điểm campaign không phải một loại điểm mới — nó là điểm chung, lọc theo khoảng thời gian và loại hành động.*

### 1/ User story

Là học viên, tôi cần xem các campaign đang chạy và đã kết thúc ngay trong trang bảng xếp hạng, để biết mình đứng đâu trong một đợt thi đua và xem lại kết quả đợt đã qua.

### 2/ Pre - Condition

| Điều kiện | Nguồn |
|---|---|
| `Gamification` bật và `Visibility in UpLMS` bật | Hai công tắc ở `US14` |
| Công tắc `Leaderboard` bật | `BR-11.6` — tắt thì campaign ẩn theo |
| Có ít nhất một campaign đang chạy hoặc đã kết thúc | `US20` |
| Tài khoản không phải `Test Account` | Ràng buộc `C10` — `Test Account` bị loại khỏi toàn bộ logic gamification |

### 3/ Scenario

Trong trang Bảng xếp hạng, cạnh năm khung cố định có lối vào campaign. Học viên chọn một campaign đang chạy và thấy tên, mô tả, khoảng thời gian, các loại hành động được tính điểm, hai bảng `Points` và `Activities`, cùng khối vị trí của mình.

Bảng của campaign đang chạy cập nhật 8 tiếng một lần, như khung cố định. Kèm một dòng nhắc rằng kết quả chính thức chốt lúc campaign kết thúc.

Campaign kết thúc thì học viên vẫn xem lại được. Bảng lúc đó là kết quả đã đóng băng, không đổi nữa.

### 4/ Acceptance criteria

**UI / UX / Rule UX / Rule UI**

| Màn hình | Giao diện | Field | Yêu cầu |
|---|---|---|---|
| Bảng xếp hạng | Lối vào campaign | Vị trí | Cạnh năm khung cố định. Cách thể hiện: `❓BA`, chờ design |
| Bảng xếp hạng | Danh sách campaign | Gồm những gì | Campaign **đang chạy** và **đã kết thúc**. Campaign chưa bắt đầu không hiện. `[đề xuất]` |
| Bảng xếp hạng | Danh sách campaign | Thứ tự | Đang chạy trước, đã kết thúc sau. Trong mỗi nhóm, campaign kết thúc gần nhất lên trước. `[đề xuất]` |
| Campaign | Thông tin | Nội dung | Tên · mô tả · khoảng thời gian · các loại hành động được tính điểm |
| Campaign | Trạng thái | Nhãn | Đang chạy hoặc đã kết thúc. Chuỗi tiếng Anh: `❓BA` |
| Campaign | Chọn bảng | Các lựa chọn | Hai bảng: `Points` · `Activities`. **Không chịu năm công tắc `Show …` ở `US11`** |
| Campaign | Bảng | Top 3, danh sách đầy đủ, cột `#`, cột học viên, cột giá trị | Giống `US6` |
| Campaign | Khối vị trí của tôi | | Giống `US7` |
| Campaign đang chạy | Nhãn cập nhật | Nội dung | `Last updated {HH:mm}`, kèm dòng nhắc kết quả chính thức chốt lúc kết thúc. Chuỗi tiếng Anh: `❓BA` |
| Campaign đã kết thúc | Nhãn | Nội dung | Thay `Last updated` bằng thời điểm đóng băng. Chuỗi tiếng Anh: `❓BA` |
| Campaign | Trạng thái rỗng | Chưa ai có chỉ số | Chuỗi tiếng Anh: `❓BA` |

**Business requirement — Business rule**

- `BR-19.1` Campaign nằm **trong trang bảng xếp hạng**. Tắt công tắc `Leaderboard` (`BR-11.6`) thì campaign ẩn theo, dữ liệu giữ nguyên.
- `BR-19.2` 🔑 **Bảng `Points` của campaign** là tổng điểm từ các lần cộng có **thời điểm cộng nằm trong khoảng campaign** và **loại hành động nằm trong danh sách campaign chọn**. Số điểm là số đã ghi trong sổ giao dịch, theo cấu hình chung tại lúc cộng.
- `BR-19.3` **Bảng `Activities` của campaign** là số hoạt động hoàn thành trong khoảng campaign, theo mục Định nghĩa chỉ số. **Không phụ thuộc danh sách loại hành động** campaign chọn cho phần điểm.
- `BR-19.4` Bài Test nộp trong campaign mà **chấm đạt sau khi campaign kết thúc thì không tính**, vì thời điểm cộng điểm là lúc chấm đạt.
- `BR-19.5` Campaign đang chạy **tính sẵn 8 tiếng một lần**, cùng nhịp với khung cố định (`BR-6.12`). Không tính lúc học viên mở.
- `BR-19.6` Campaign kết thúc thì **đọc kết quả đã đóng băng**, không tính lại (`US21`).
- `BR-19.7` Tiêu chí phụ `BR-6.4` áp cho cả hai bảng: cùng chỉ số thì ai đạt sớm hơn xếp trên.
- `BR-19.8` Campaign **phụ thuộc cấu hình chung**:
  - Tắt `Points` hoặc tắt một hành động ở `US8` thì phần đó ngừng đóng góp cho mọi campaign đang chạy
  - Đổi số điểm ở `US8` thì campaign mang hai mức điểm, theo `C4`. PO chấp nhận ngày 08/10
- `BR-19.9` Học viên bị `Block` hoặc rời tổ chức: trước lúc kết thúc thì không có mặt, sau lúc kết thúc thì vẫn trong kết quả (`C12`).
- `BR-19.10` **Không thông báo** khi campaign bắt đầu hoặc kết thúc. `[đề xuất]` — thông báo chỉ dành cho thành tích (`US2`).

**Data Field**

Không có field mới phía học viên. Đọc campaign ở `US20`, bảng tính sẵn ở `US6`, kết quả đóng băng ở `US21`.

**NFR**

Mỗi campaign đang chạy thêm hai bảng vào lượt tính sẵn 8 tiếng. Campaign đã kết thúc chỉ đọc kết quả đã lưu, chi phí gần bằng 0.

### 5/ Out of scope

| Không làm ở US này | Lý do |
|---|---|
| Hiện campaign chưa bắt đầu | `[đề xuất]` — chưa có gì để xếp hạng |
| Thông báo khi campaign bắt đầu, sắp kết thúc hoặc kết thúc | `BR-19.10` |
| Lọc campaign theo nhóm | Toàn tổ chức. Chờ chức năng nhóm từ HRM |
| Xuất kết quả campaign phía học viên | Vận hành xuất ở `US21` |

### 6/ Conner case

*(QA điền)*

---

## US20: Tạo và quản lý campaign

### 1/ User story

Là nhân sự vận hành, tôi cần tạo campaign có thời hạn riêng và chọn loại hành động được tính điểm, để tổ chức phong trào học tập theo mục tiêu từng đợt.

### 2/ Pre - Condition

| Điều kiện | Nguồn |
|---|---|
| `Gamification` đang bật ở cấp tổ chức | `US14` |
| Người dùng có quyền sửa cấu hình gamification | `US15` |

### 3/ Scenario

Vận hành mở khu vực Campaign trong Gamification trên Ops, thấy danh sách campaign kèm trạng thái.

Tạo mới: nhập tên, mô tả, ngày bắt đầu, ngày kết thúc, rồi chọn loại hành động được tính điểm. Mỗi loại hiện kèm số điểm theo cấu hình chung, chỉ để xem, không sửa được.

Campaign chưa bắt đầu thì sửa mọi thứ và xoá được. Đang chạy thì chỉ sửa tên và mô tả. Đã kết thúc thì chỉ xem.

### 4/ Acceptance criteria

**UI / UX / Rule UX / Rule UI**

| Màn hình | Giao diện | Field | Yêu cầu |
|---|---|---|---|
| Danh sách campaign | Bảng | Cột | Tên · khoảng thời gian · trạng thái · loại hành động được tính |
| Danh sách campaign | Bảng | Trạng thái | Ba trạng thái: chưa bắt đầu · đang chạy · đã kết thúc. **Tính từ ngày hiện tại**, theo múi giờ tổ chức. Chuỗi tiếng Anh: `❓BA` |
| Tạo campaign | Form | Tên | Bắt buộc. Độ dài tối đa: `❓BA` |
| Tạo campaign | Form | Mô tả | Không bắt buộc |
| Tạo campaign | Form | Ngày bắt đầu | Bắt buộc. **Không được ở quá khứ.** `[đề xuất]` |
| Tạo campaign | Form | Ngày kết thúc | Bắt buộc. Không nhỏ hơn ngày bắt đầu. **Bắt đầu và kết thúc cùng một ngày là hợp lệ.** `[đề xuất]` |
| Tạo campaign | Form | Loại hành động | Chọn nhiều trong bốn hành động: check-in hằng ngày · hoàn thành hoạt động · hoàn thành khoá · hoàn thành bài Test đạt. **Phải chọn ít nhất một.** `[đề xuất]` |
| Tạo campaign | Form | Số điểm | **Không có ô sửa số điểm.** Mỗi loại hành động hiện số điểm theo cấu hình chung ở `US8`, chỉ đọc |
| Tạo campaign | Form | Hành động đang tắt ở `US8` | Vẫn chọn được, kèm dòng nhắc: hành động này đang tắt nên chưa sinh điểm cho tới khi bật lại. `[đề xuất]` |
| Tạo campaign | Form | Cách lưu | **Có nút tạo, không tự lưu.** Campaign tạo xong là có hiệu lực từ ngày bắt đầu, nên cần một thao tác chủ động. Khác với trang cấu hình ở `BR-14.10`. `[đề xuất]` |
| Sửa campaign | Chưa bắt đầu | Mọi field | Sửa được |
| Sửa campaign | Đang chạy | Tên, mô tả | Sửa được. Ngày bắt đầu, ngày kết thúc, loại hành động **chỉ đọc** |
| Sửa campaign | Đã kết thúc | Mọi field | Chỉ xem |
| Xoá campaign | Chưa bắt đầu | Nút xoá | Có. Xác nhận bằng popover cạnh nút, giống `BR-14.13` |
| Xoá campaign | Đang chạy hoặc đã kết thúc | Nút xoá, nút dừng | **Không có** |

**Business requirement — Business rule**

- `BR-20.1` Campaign gồm: tên · mô tả · ngày bắt đầu · ngày kết thúc · danh sách loại hành động được tính điểm.
- `BR-20.2` 🔑 **Không có số điểm riêng cho campaign.** Số điểm theo cấu hình chung ở `US8`. Campaign chỉ chọn loại hành động nào được tính. PO chốt ngày 08/10.
- `BR-20.3` Khoảng campaign tính **theo ngày trọn**, biên ngày cắt theo múi giờ tổ chức (`C6`). `[đề xuất]`
- `BR-20.4` Người tham gia là **toàn tổ chức**. Không chọn theo lớp, khoá hay nhóm.
- `BR-20.5` **Nhiều campaign được chạy chồng thời gian.** Mỗi campaign chỉ là một cách lọc trên sổ giao dịch, nên không xung đột nhau.
- `BR-20.6` 🔑 **Luật sửa theo trạng thái:**

  | Trạng thái | Sửa | Xoá | Dừng |
  |---|---|---|---|
  | Chưa bắt đầu | Mọi thứ | ✅ | — |
  | Đang chạy | **Chỉ tên và mô tả** | ❌ | ❌ |
  | Đã kết thúc | ❌ | ❌ | — |

  > Đang chạy thì luật không đổi, kể cả thời điểm kết thúc, để học viên đang thi đua không bị đổi luật giữa chừng.
- `BR-20.7` ⚠️ **Đổi cấu hình chung là đổi luật của mọi campaign đang chạy.** Tắt một hành động hay đổi số điểm ở `US8` thì campaign đổi theo (`BR-19.8`). Vận hành cần biết điều này trước khi sửa cấu hình chung.
- `BR-20.8` **Tắt `Gamification` khi có campaign đang chạy: vẫn cho tắt.** Campaign không nhận thêm gì trong thời gian tắt. Popover xác nhận ở `BR-14.13` nêu thêm số campaign đang chạy. `[đề xuất]` — chờ PO xác nhận, xem `OQ-42`.
- `BR-20.9` Campaign gắn với tổ chức (`C1`). Loại hành động là danh mục hệ thống, mở rộng được (`C2`).

**Data Field**

| Field | Kiểu | Bắt buộc | Giá trị hợp lệ | Ghi chú |
|---|---|---|---|---|
| Tên | Chuỗi | Có | Độ dài tối đa `❓BA` | Mới |
| Mô tả | Chuỗi | Không | | Mới |
| Ngày bắt đầu | Ngày | Có | Không ở quá khứ khi tạo | Mới |
| Ngày kết thúc | Ngày | Có | `>=` ngày bắt đầu | Mới |
| Loại hành động | Danh sách danh mục | Có | Ít nhất một trong bốn hành động của `US8` | Mới. Chịu `C2` |
| Trạng thái | Danh mục | — | Chưa bắt đầu · đang chạy · đã kết thúc | `[suy ra]` tính từ ngày, không cần lưu |
| `tenant_id` | Khoá ngoại | Có | | Ràng buộc `C1` — cấu hình gắn `tenant_id`, không đóng cứng trong mã |

**NFR**

Không có yêu cầu riêng.

### 5/ Out of scope

| Không làm ở US này | Lý do |
|---|---|
| Số điểm riêng cho từng campaign | `BR-20.2` |
| Chọn người tham gia theo lớp, khoá hoặc nhóm | `BR-20.4`. Theo nhóm chờ HRM |
| Dừng sớm campaign đang chạy | `BR-20.6` |
| Giới hạn nội dung được tính, ví dụ chỉ tính khoá An toàn thông tin | Chưa yêu cầu |
| Nhân bản campaign cũ | Chưa yêu cầu |
| Thưởng thêm điểm khi đứng đầu campaign | Chưa yêu cầu. Trao thưởng làm ngoài hệ thống |

### 6/ Conner case

*(QA điền)*

---

## US21: Kết quả campaign

### 1/ User story

Là nhân sự vận hành, tôi cần xem và xuất kết quả của từng campaign, để đội truyền thông công bố và trao thưởng.

### 2/ Pre - Condition

| Điều kiện | Nguồn |
|---|---|
| Có campaign đang chạy hoặc đã kết thúc | `US20` |
| Người dùng có quyền xem danh sách học viên và hạng | `US15` |

### 3/ Scenario

Từ danh sách campaign, vận hành mở một campaign và thấy hai bảng `Points` và `Activities` với toàn bộ học viên.

Campaign đang chạy thì đây là số tạm tính, có nhãn cập nhật. Campaign đã kết thúc thì đây là kết quả chính thức, đã đóng băng.

Vận hành xuất Excel để gửi đội truyền thông.

### 4/ Acceptance criteria

**UI / UX / Rule UX / Rule UI**

| Màn hình | Giao diện | Field | Yêu cầu |
|---|---|---|---|
| Kết quả campaign | Bảng | Tab | `Points` · `Activities` |
| Kết quả campaign | Bảng | Cột | Thứ hạng · học viên · giá trị chỉ số |
| Kết quả campaign | Đang chạy | Nhãn | Số tạm tính, kèm `Last updated {HH:mm}` |
| Kết quả campaign | Đã kết thúc | Nhãn | Kết quả chính thức, kèm thời điểm đóng băng |
| Kết quả campaign | Xuất | Nút xuất | Xuất **Excel**, gồm cả hai bảng. Campaign đang chạy vẫn xuất được, nhưng file ghi rõ là số tạm tính. `[đề xuất]` |

**Business requirement — Business rule**

- `BR-21.1` 🔑 **Kết quả đóng băng ghi một lần khi campaign kết thúc**, tính đúng theo biên thời gian (`C11`), không bao giờ tính lại.
- `BR-21.2` Tác vụ đóng băng **chạy riêng**, không đi theo chu kỳ 8 tiếng của bảng xếp hạng. Kết quả công bố phải khớp đúng thời điểm kết thúc.
- `BR-21.3` **Kết quả giữ nguyên mãi** (`C12`). Học viên bị `Block` hoặc rời tổ chức sau khi campaign kết thúc vẫn nằm trong kết quả.
- `BR-21.4` **Xuất đúng kết quả đã đóng băng.** Không dùng `US12` thay được, vì `US12` không lọc theo loại hành động và là số liệu sống — số xuất ra sẽ lệch với bảng campaign đã công bố.
- `BR-21.5` Thứ hạng theo `BR-6.4`: cùng chỉ số thì ai đạt sớm hơn xếp trên.

**Data Field**

| Field | Kiểu | Bắt buộc | Ghi chú |
|---|---|---|---|
| Campaign | Khoá ngoại | Có | |
| Bảng | Danh mục | Có | `Points` · `Activities` |
| Học viên | Khoá ngoại tới `users` | Có | |
| Giá trị chỉ số | Số nguyên | Có | |
| Thời điểm đạt mức | Thời gian | Có | Nền của `BR-6.4` |
| Thứ hạng | Số nguyên | Không | Để trống với học viên chưa có chỉ số |
| Thời điểm đóng băng | Thời gian | Có | |
| `tenant_id` | Khoá ngoại | Có | Ràng buộc `C1` — cấu hình gắn `tenant_id`, không đóng cứng trong mã |

**NFR**

Tác vụ đóng băng tính trễ vẫn phải ra đúng số, vì lọc theo thời điểm cộng chứ không theo thời điểm chạy (`C11`).

### 5/ Out of scope

| Không làm ở US này | Lý do |
|---|---|
| Sửa kết quả thủ công | Kết quả đóng băng không đổi |
| Trao thưởng trong hệ thống | Làm ngoài hệ thống |
| So sánh nhiều campaign với nhau | Chưa yêu cầu |

### 6/ Conner case

*(QA điền)*

---

# Vấn đề tồn đọng

| # | Nội dung | Người trả lời | Chặn việc gì |
| --- | --- | --- | --- |
| **OQ-01** | Mẫu số **132** và **145** ở Analytics là hai nhóm người khác nhau, hay 145 gồm cả giai đoạn trước? | PO | Độ chính xác mục `Analytics` |
| ~~OQ-02~~ | ✅ **Đã chốt 23/09: cộng điểm lỗi thì ghi lại**, không để mất âm thầm. Xem `BR-13.8` | PO | — |
| ~~OQ-03~~ | ✅ **Tạm chốt 23/09** bộ Activation · Course start · Completion, kèm `Retention` chưa có mốc nền | PO | — |
| ~~OQ-07~~ | ✅ **Đã chốt 23/09: sổ giao dịch điểm giữ toàn bộ, không dọn.** Xem `BR-3.9` | PO | — |
| ~~OQ-08~~ | ✅ **Đã chốt 06/10: múi giờ lấy theo tenant**, không có ô chọn trên màn Gamification. Cách lưu do BE quyết trong technical design. Xem `BR-14.9` | PO | — |
| ~~OQ-09~~ | ✅ **Đã rõ:** mọi học viên bắt đầu ở `0` điểm và **hạng `1`**, theo `BR-10.1` | — | — |
| **OQ-10** | Metadata đầu tài liệu: `Target release` · `Epic` · `Story` · `Tech lead` · `QA` · `Reviewer` | PO | Bàn giao |
| **OQ-11** | Link Figma và tài khoản staging để đối chiếu giao diện | PO | `US1`–`US12` |
| **OQ-12** | Học viên có tắt hoặc chỉnh được thông báo thành tích không? | PO | `US2` |
| **OQ-16** | Câu chữ tiếng Anh cho thông báo **lên hạng** | PO | `US2` |
| **OQ-17** | Câu chữ tiếng Anh mô tả từng loại hành động trong cột `Source` của lịch sử điểm | PO | `US3` |
| **OQ-18** | Lịch sử điểm có cần **lọc theo khoảng ngày hoặc theo loại hành động** không? Hiện tôi để ngoài phạm vi | PO | `US3` |
| **OQ-19** | Số dòng mỗi trang của lịch sử điểm | PO | `US3` |
| **OQ-42** | **Tắt `Gamification` khi có campaign đang chạy thì vẫn cho tắt, đúng không?** Quy định cũ bắt phải dừng chiến dịch trước, nhưng nay campaign đang chạy không dừng được và nhiều campaign được chồng thời gian — giữ quy định cũ thì gần như không bao giờ tắt được. Xem `BR-20.8` | PO | `US14` · `US20` |
| **OQ-43** | **Các mục ghi `[đề xuất]` ở `US19`, `US20`, `US21`** — biên ngày trọn, ngày bắt đầu không ở quá khứ, chọn ít nhất một loại hành động, không thông báo, không hiện campaign chưa bắt đầu, có nút tạo thay vì tự lưu, dùng chung quyền ở `US15` | PO | `US19` · `US20` · `US21` |
| **OQ-44** | **Cách tính bảng campaign:** tính sẵn 8 tiếng một lần và đóng băng bằng tác vụ riêng. Đề xuất ở `solution-comparison-v0.2` §10, chờ PO duyệt | PO + Dev | `US19` · `US21` |
| **OQ-45** | **Design cho campaign** và cập nhật design bảng xếp hạng: thêm tab `Activities`, bỏ bộ chọn khoảng ngày tự do, thêm lối vào campaign, thêm `Show activities` bên Ops | PO | `US6` · `US11` · `US19` đến `US21` |
| ~~OQ-20~~ | ✅ **Đã chốt 23/09: hạ ngưỡng thì quét lại cấp bù, nâng ngưỡng thì gỡ huy hiệu.** Xem `BR-4.6`, `BR-4.7` | PO | — |
| ~~OQ-22~~ | ✅ **Đã chốt 23/09: không báo khi gỡ huy hiệu.** Sau `CR-008` thì tình huống này không còn phát sinh — mốc huy hiệu khoá sau khi tạo nên không có thao tác gỡ, và lịch sử cũng không có sự kiện `Badge removed`. Xem `BR-1.4` | PO | — |
| ~~OQ-23~~ | ✅ **Đã chốt 23/09: hạng KHÔNG tụt.** Đổi ngưỡng hạng chỉ áp từ thời điểm đổi trở đi. Khác với huy hiệu, cố ý. Xem `BR-1.3` | PO | — |
| ~~OQ-21~~ | ✅ **Đã làm rõ 23/09: chứng chỉ cấp theo KHOÁ, không theo lượt ghi danh.** Một học viên một chứng chỉ cho một khoá, học lại không cấp thêm. Xem `BR-13.12`. *(Còn lại một chi tiết cho Dev: endpoint đếm chứng chỉ đã loại khoá bỏ qua theo `BR-SKIP` chưa — kiểm lúc làm.)* | PO | — |
| ~~OQ-25~~ | ✅ **Đã chốt 23/09: vẫn hiện, nhưng cột thứ hạng để trống.** Xem `BR-6.6` | PO | — |
| ~~OQ-26~~ | ✅ **Đã chốt 23/09: nổi bật top 3.** Danh sách đầy đủ bên dưới — xem `OQ-28` | PO | — |
| ~~OQ-27~~ | ✅ **Đã chốt 23/09: tính lại 8 tiếng một lần, ba lần một ngày.** Xem `BR-6.12` | PO | — |
| ~~OQ-28~~ | ✅ **Đã chốt 23/09: nổi bật top 3, danh sách đầy đủ cuộn được bên dưới**, người chưa có chỉ số nằm cuối với ô thứ hạng để trống | PO | — |
| ~~OQ-29~~ | ✅ **Đã chốt 23/09: chọn khoảng ngày thì không có bảng theo hạng.** Bảng `Level` chỉ tồn tại ở `All time`. **Ngày 08/10 thêm bảng `Badges` cùng quy tắc.** Xem `BR-11.2` | PO | — |
| ~~OQ-30~~ | ✅ **Đảo ngày 08/10: học viên không còn khoảng ngày tự chọn**, mọi bảng tính sẵn 8 tiếng một lần. Xem `BR-6.12`, `BR-6.15` | PO | — |
| ~~OQ-31~~ | ✅ **Đã chốt 23/09: không có thao tác xoá huy hiệu.** Huy hiệu chỉ không còn hiện khi tắt chức năng huy hiệu, tắt rule của huy hiệu đó, hoặc học viên rời tổ chức. Xem `BR-1.4a` | PO | — |
| ~~OQ-32~~ | ✅ **Đã chốt 23/09: hai cấp** — một công tắc `Badges` cho cả chức năng, và một công tắc cho từng loại huy hiệu | PO | — |
| ~~OQ-33~~ | ✅ **Đã chốt 23/09: có, cả bốn chức năng đều có công tắc riêng** — `Points` · `Badges` · `Levels` · `Leaderboard` | PO | — |
| ~~OQ-34~~ | ✅ **Đã chốt 23/09: không cần lịch sử ai đổi cấu hình gamification** | PO | — |
| ~~OQ-35~~ | ✅ **Đã chốt 23/09.** Dãy mốc: Check-in `4, 8, 16, 32, 64, 128, 256, 512` · Activity `10, 25, 50, 100, 200, 400, 800, 1600` · Test `2, 4, 8, 16, 32, 64, 128, 256` · Course `1, 2, 4, 8, 16, 32, 64, 128` | PO | — |
| ~~OQ-36~~ | ✅ **Đã chốt 06/10: tắt huy hiệu hoặc điểm thì tiêu chí lên hạng tương ứng khoá theo**, giữ nguyên giá trị, bật lại thì chạy lại như cũ. Không có hộp xác nhận, hệ quả nêu bằng dòng giải thích dưới công tắc. Xem `BR-10.7` | PO | — |
| ~~OQ-37~~ | ✅ **Đã chốt 23/09: `Check-in badges` · `Activity badges` · `Test badges` · `Course badges`** | PO | — |
| ~~OQ-38~~ | ✅ **Đã chốt 23/09: hạng chỉ là số thứ tự tịnh tiến, không có tên và hình** | PO | — |
| ~~OQ-39~~ | ✅ **Đã chốt 23/09: tách thành các bảng riêng**, mỗi chỉ số một bảng, không phải một bảng nhiều cột | PO | — |
| ~~OQ-40~~ | ✅ **Đã chốt 23/09: có xuất file.** Chọn khoảng ngày rồi export, ở màn danh sách học viên `US12`. Xem `BR-12.8` | PO | — |
| ~~OQ-41~~ | ✅ **Đã chốt 23/09: xuất Excel** | PO | — |

> ✅ `OQ-13` đã đóng: **giao diện UpLMS dùng tiếng Anh.** Mọi chuỗi hiển thị trong PRD viết bằng tiếng Anh.
> ✅ `OQ-14` không còn cần: PO chốt **không gộp thông báo**.
> ✅ `OQ-15` đã đóng: **hoàn thành khoá và được cấp chứng chỉ là MỘT hành động**, cộng điểm một lần. Ảnh PO gửi chỉ là ví dụ về cách hiển thị.

---

# Comments

*Trao đổi trong quá trình review.*
