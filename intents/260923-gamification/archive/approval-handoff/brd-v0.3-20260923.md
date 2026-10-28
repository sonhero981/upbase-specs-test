---
intent: 260923-gamification
artifact: brd
version: 0.3
status: superseded
migrated-from: .claude/projects/Gamification/docs/brd/brd-v0.3-20260923.md
---
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
| v0.2 | Đưa bảng xếp hạng vào phạm vi · tách kỳ lịch khỏi chiến dịch · bác bỏ `A8` · thêm `C6`, `C7` | `CR-001` | 23/09/2026 |
| **v0.3** | **Chốt 4 quyết định Gate 1.** Hai công tắc có tên rõ · bỏ chống cày riêng cho hoạt động Text/Ảnh · **bỏ phạm vi xếp hạng theo lớp** · **thêm chỉ số xếp hạng chọn được cho chiến dịch** + luật chỉnh sửa chiến dịch | `CR-002` · `CR-003` + quyết định `OQ-A1`, `OQ-A2` | 23/09/2026 |

**Nguồn input:** `working/raw-inputs/yeu-cau-goc-20260923.md` · `working/raw-inputs/change-requests.md` (CR-001…003) · `working/ai-drafts/clarified-requirements-20260923.md` · `project-decisions.md`

---

# 1. Problem

**Học viên đã được ghi danh vào khoá nhưng không chủ động quay lại học.**

| | |
|---|---|
| **Ai gặp** | Học viên trên UpLMS — đã có tài khoản, đã được thêm vào lớp, đã có nội dung để học |
| **Gặp khi nào** | Trong suốt thời gian học, đặc biệt ở giai đoạn giữa khoá khi không còn động lực ban đầu và chưa thấy đích |
| **Hậu quả** | Học viên học dở dang hoặc học dồn sát hạn. Vận hành phải thúc thủ công. Đội truyền thông nội bộ muốn tổ chức phong trào học tập nhưng không có cơ chế nào để gắn hoạt động của học viên vào một chiến dịch theo dõi được |

Hệ thống hiện tại **chỉ ghi nhận việc học, không phản hồi lại việc học**. Học viên hoàn thành một hoạt động thì thanh tiến độ nhích lên — ngoài ra không có gì. Không có sự ghi nhận, không có mốc để nhắm tới, không có lý do để quay lại vào ngày hôm sau khi chưa tới hạn.

---

# 2. Analytics

> ⚠️ **Chưa có dữ liệu định lượng.** Căn cứ định tính từ PO cộng với quan sát hệ thống. Xem `OQ-B4`.

| Hướng | Hiện trạng |
|---|---|
| **Cách làm hiện tại** | Vận hành theo dõi tiến độ qua dashboard SIS (*Tiến độ học trên UpLMS*), thấy ai chậm thì thúc. 30 mail tự động đều là **mail sự kiện** — chào mừng, nhắc lịch kiểm tra, báo hết hạn — không có mail nào nhằm tạo động lực |
| **Công cụ sẵn có bị hạn chế** | Giao diện soạn và gửi thông báo thủ công trên Ops **đang ẩn** (3/4 page module Notification & Email). Đội truyền thông muốn gửi thông điệp khích lệ tới nhóm học viên cụ thể thì không có đường tự phục vụ |
| **Tiêu chí quyết định** | Vận hành nhìn phần trăm tiến độ và thời hạn còn lại. Hai con số này **cho biết ai đang chậm, không cho biết ai đang cố gắng** — học viên đi đều mỗi ngày và học viên học dồn một buổi trông giống nhau khi đã cùng phần trăm |
| **Chỗ sai** | Việc thúc học phụ thuộc vào vận hành nhớ và làm thủ công. Không mở rộng được khi số lớp tăng, và **không tạo được thói quen** — học viên phản ứng với lời nhắc, không tự quay lại |

**Còn thiếu** (`OQ-B4`): tỷ lệ học viên đứng yên >14 ngày · tỷ lệ hoạt động hoàn thành trong 7 ngày cuối trước hạn · tỷ lệ khoá hoàn thành so với khoá được ghi danh.

---

# 3. Objective

| # | Kết quả muốn đạt |
|---|---|
| O1 | **Học viên quay lại học đều đặn hơn** mà không cần vận hành nhắc thủ công |
| O2 | **Nỗ lực học được ghi nhận ngay lúc nó xảy ra** |
| O3 | **Học viên có mốc ngắn hạn để nhắm tới**, thay vì chỉ có đích cuối là hoàn thành khoá |
| O4 | **Đội truyền thông nội bộ tổ chức được chiến dịch học tập có thể đo được** |
| O5 | **Kết quả mỗi kỳ công bố được và không thay đổi về sau**, đủ tin cậy để làm căn cứ trao thưởng |
| O6 | **Điểm số đáng tin** — mỗi con số đều truy được nguồn, và không bị thổi lên bằng thao tác đối phó |

---

# 4. Stakeholder

| Stakeholder | Action |
| --- | --- |
| **Học viên (UpLMS)** | Nhận điểm · nhận huy hiệu · lên hạng · xem trang thành tích · tra lịch sử điểm · xem bảng xếp hạng và vị trí của mình |
| **Nhân sự vận hành (UpLMS Ops)** | Khai bảng điểm · tạo huy hiệu · đặt hạng và ngưỡng · tạo và quản lý chiến dịch · bật/tắt cơ chế |
| **Đội truyền thông nội bộ** | Thiết kế và chạy chiến dịch · công bố kết quả cuối kỳ và **trao thưởng ngoài hệ thống** |
| **Quản lý đào tạo / L&D** | Dùng dữ liệu điểm, hạng và xếp hạng để đánh giá mức độ tham gia |
| Dev | Xác nhận `OQ-B1` (Keycloak) · `OQ-B2` (dấu thời gian) · `OQ-B9` (tải) · `OQ-B12` (thời điểm đạt huy hiệu / hoàn thành khoá) |
| QA | Điền `Conner case` ở PRD |

---

# 5. Scope

## In scope

| # | Nội dung |
|---|---|
| S1 | **Cơ chế điểm** — khai hành động nào được bao nhiêu điểm, bật/tắt từng hành động |
| S2 | **Bốn hành động tính điểm**: hoàn thành hoạt động · hoàn thành khoá · đạt bài kiểm tra · đạt điểm cao |
| S3 | **Hành động thứ năm**: đăng nhập nhiều ngày liên tiếp — nguồn Keycloak, tính từ ngày go-live |
| S4 | **Huy hiệu** — tên, hình, mô tả, điều kiện đạt |
| S5 | **Bốn loại điều kiện huy hiệu**: số lượng hoàn thành · chuỗi ngày liên tiếp · mốc thời gian · hoàn thành một nội dung cụ thể |
| S6 | **Hạng người học** — tên, hình, ngưỡng điểm |
| S7 | **Hai loại điểm tách nhau**: điểm tích luỹ vĩnh viễn (xét hạng) và điểm theo kỳ (xếp hạng) |
| S8 | **Chống cày điểm** — chống cộng trùng nội dung đã hoàn thành, trần điểm tối đa mỗi ngày |
| S9 | **Lịch sử điểm** — học viên tra được từng lần cộng đến từ đâu |
| S10 | **Thông báo thành tích** — nhận điểm, nhận huy hiệu, lên hạng |
| S11 | **Trang "Thành tích của tôi"** — điểm, hạng, huy hiệu đã có, huy hiệu sắp đạt kèm phần còn thiếu |
| **S12** | 🔄 **Hai công tắc ở cấp tổ chức:**<br>• **`Gamification`** — bật/tắt việc **lưu dữ liệu**, bao gồm cả việc hiển thị<br>• **`Visibility in UpLMS`** — chỉ xuất hiện khi `Gamification` đang bật; bật/tắt hiển thị phía học viên |
| S13 | **Phân quyền cấu hình** |
| S14 | **Bảng xếp hạng theo kỳ lịch** — tuần · tháng · quý · năm. Hệ thống tự tính, không cần cấu hình |
| S15 | **Chiến dịch** — vận hành khai khoảng thời gian bất kỳ (không cần trùng biên lịch), kèm tên và phạm vi người tham gia |
| **S16** | 🆕 **Chỉ số xếp hạng của chiến dịch chọn được** — theo **điểm**, theo **số huy hiệu**, hoặc theo **số khoá hoàn thành** |
| **S17** | 🆕 **Luật chỉnh sửa chiến dịch** — chiến dịch **đang chạy thì không sửa được** |
| S18 | **"Vị trí của tôi"** — luôn hiện thứ hạng người đang xem kèm vài người liền kề, kể cả khi không ở nhóm đầu |
| S19 | **Chốt kỳ** — hết kỳ thì đóng băng bảng, lưu kết quả cuối **kèm chỉ số đã dùng để xếp**, mở kỳ mới về 0 |
| S20 | **Lịch sử các kỳ đã kết thúc** — xem lại bảng xếp hạng tháng trước, quý trước, chiến dịch đã xong |
| S21 | **Tham số múi giờ ở cấp tổ chức** — biên kỳ cắt theo múi giờ tổ chức, không theo giờ máy chủ |
| **S22** | 🆕 **Tiêu chí phụ khi đồng hạng** — cùng chỉ số thì **ai đạt mức đó sớm hơn xếp trên**. Bắt buộc, xem §6.6 |

## Out of scope

| # | Không làm | Vì sao |
|---|---|---|
| **N1** | 🔄 **Bộ lọc bảng xếp hạng theo nhóm** — gồm cả **theo lớp** và **theo phòng ban** | PO chốt gộp làm một hạng mục hoãn. Làm riêng cho lớp bây giờ thì trùng mục đích với bộ lọc theo nhóm sau này, phải làm lại. Phòng ban = chức năng nhóm, **đồng bộ từ HRM** — chưa làm |
| **N2** | 🔄 **Chống cày riêng cho hoạt động chỉ có Text/Ảnh** | PO chốt không cần. Chống cộng trùng (`C5`) và trần điểm/ngày (`S8`) vẫn áp cho mọi loại hoạt động |
| N3 | **Giới hạn nội dung được tính trong chiến dịch** | PO không yêu cầu — xem `CR-002`, tôi từng hỏi nhầm hướng |
| N4 | **Tính năng Lộ trình học** và hành động "hoàn thành lộ trình" | Tính năng riêng, làm sau |
| N5 | **Tính năng Khung năng lực / Skills** và điều kiện huy hiệu "đạt kỹ năng" | Tính năng riêng, làm sau |
| N6 | **Sửa logic hoàn thành Activity** | PO chốt giữ nguyên |
| N7 | **Tính bù điểm cho giai đoạn gamification bị tắt** | Cần phát lại theo từng ngày để áp đúng trần điểm |
| N8 | **Quản lý phần thưởng trong hệ thống** | PO xác nhận **trao thưởng là hành động ngoài hệ thống** |
| N9 | **Gamification cho nhân sự Ops** | Chỉ áp dụng cho học viên |
| N10 | **Thi đua theo đội / nhóm** | Chỉ xếp hạng cá nhân |
| N11 | **Cấu hình gamification riêng theo lớp hoặc khoá** | Cấu hình ở cấp tổ chức |
| N12 | **Màn quản lý nhiều tổ chức** | Chưa có multi-tenant. Dữ liệu vẫn thiết kế theo tổ chức — `C1` |
| N13 | **Module Tenant (`TNT.CFG.02`) đầy đủ** | Đợt này chỉ khai **tham số múi giờ** (S21) |
| N14 | **Trang theo dõi hiệu quả chiến dịch cho đội truyền thông** | Chưa có trong yêu cầu — `OQ-B3` |

## Potential scope

Bộ lọc theo nhóm sau khi đồng bộ HRM · giới hạn nội dung chiến dịch · tính bù điểm · trang hiệu quả chiến dịch · điểm cho lộ trình · huy hiệu theo kỹ năng · đổi điểm lấy phần thưởng

---

# 6. Solution (khung)

## 6.1 Hướng tổng thể

```
Lớp 1  Bắt sự kiện học tập      ← nghe các việc học viên đã làm
Lớp 2  Quy đổi ra điểm          ← áp bảng cấu hình + luật chống cày
Lớp 3  Tích luỹ và xét ngưỡng   ← cộng dồn, xét huy hiệu, xét hạng
Lớp 4  Xếp hạng theo kỳ         ← tính thứ hạng từ sổ giao dịch theo khoảng ngày
Lớp 5  Phản hồi cho học viên    ← thông báo + trang thành tích + bảng xếp hạng
```

Nguyên tắc xuyên suốt: **gamification chỉ đọc, không sửa dữ liệu học tập.** Nó nghe việc đã xảy ra và ghi ra bản ghi của riêng nó. Đây là điều kiện để giữ được `N6` và để bật/tắt không ảnh hưởng gì tới việc học.

## 6.2 Hai loại kỳ — khác bản chất, không gộp

| | **Kỳ lịch** | **Chiến dịch** |
|---|---|---|
| Ai tạo | **Hệ thống tự tính** | **Vận hành khai tay** |
| Biên | Cố định theo lịch — tuần, tháng, quý, năm. **Không dùng cửa sổ trượt** | Hai ngày bất kỳ, **không cần trùng biên lịch** |
| Cấu hình | Không cần màn nào | Tên · phạm vi người tham gia · **chỉ số xếp hạng** (S16) |
| Chỉnh sửa | — | **Đang chạy thì không sửa được** (S17) |
| Ví dụ | Tháng 9 · Quý III · Năm 2026 | *"Tháng an toàn thông tin 10/9–15/10"* |

Cả hai đều bị chốt và đóng băng khi hết kỳ (S19), đều xem lại được (S20).

## 6.3 Ràng buộc thiết kế bắt buộc

| # | Ràng buộc | Vì sao |
|---|---|---|
| **C1** | Cấu hình gắn với **tổ chức**, không đóng cứng | Định hướng đa tenant. Hiện một tổ chức nên chi phí bằng 0 |
| **C2** | **Danh mục hành động tính điểm, danh mục điều kiện huy hiệu, và danh mục chỉ số xếp hạng phải mở rộng được bằng cấu hình** | Lộ trình (N4), kỹ năng (N5), bộ lọc nhóm (N1), giới hạn nội dung (N3) đều sẽ thêm sau |
| **C3** | Lưu **từng lần cộng điểm kèm thời điểm**, không chỉ lưu tổng | Nền của lịch sử điểm (S9), xếp hạng theo kỳ (C7), tiêu chí phụ khi đồng hạng (S22), và luật chống cày |
| **C4** | Đổi cấu hình điểm → **áp dụng từ thời điểm đổi** | PO chốt |
| **C5** | Chống cộng trùng "đã học" tính theo **người học**, không theo lượt ghi danh lớp | Học viên có thể học cùng nội dung qua nhiều lớp |
| **C6** | **Biên kỳ cắt theo múi giờ của tổ chức**, không theo giờ máy chủ | Module Tenant (`TNT.CFG.02`) chưa có → đợt này khai một tham số múi giờ cấp tổ chức, thiết kế để module Tenant sau tiếp quản |
| **C7** | **Một lần cộng điểm thuộc về nhiều kỳ cùng lúc** → điểm theo kỳ **tính từ sổ giao dịch theo khoảng ngày**. **Nhưng kết quả cuối kỳ phải được lưu cứng** | Kỳ lịch lồng nhau (tuần ⊂ tháng ⊂ quý ⊂ năm) và chiến dịch chạy song song |
| **C8** 🆕 | **Mọi mốc dùng để xếp hạng phải lưu được thời điểm đạt** — không chỉ điểm, mà cả **thời điểm đạt huy hiệu** và **thời điểm hoàn thành khoá** | S16 cho phép xếp theo huy hiệu và theo số khoá; S22 cần thời điểm đạt để phá đồng hạng. `OQ-B12` |

## 6.4 ✅ Quyết định 1 — Ngữ nghĩa của việc tắt gamification *(đã chốt)*

**Hai công tắc, đặt ở cấp tổ chức:**

| Công tắc | Ý nghĩa |
|---|---|
| **`Gamification`** | Bật/tắt việc **lưu dữ liệu**, bao gồm cả việc hiển thị. Tắt = không ghi nhận gì, không hiện gì |
| **`Visibility in UpLMS`** | **Chỉ xuất hiện khi `Gamification` đang bật.** Bật/tắt hiển thị phía học viên trên UpLMS |

Ba trạng thái dùng được:

| Trạng thái | `Gamification` | `Visibility in UpLMS` | Dùng khi nào |
|---|---|---|---|
| Tắt hẳn | Tắt | *(không hiện)* | Tổ chức không dùng cơ chế này |
| **Chạy ngầm** | Bật | Tắt | **Chạy thử trước khi mở cho học viên** |
| Bật đầy đủ | Bật | Bật | Vận hành bình thường |

**Hai luật kèm theo:**

1. Khi chuyển từ *Chạy ngầm* sang *Bật đầy đủ*: **không bắn thông báo hồi tố**. Nếu không, mỗi học viên nhận hàng trăm thông báo cùng lúc. Lịch sử điểm vẫn hiển thị đầy đủ để tra nguồn.
2. Bật lại sau khi tắt hẳn: **tính từ thời điểm bật**, không tính bù (N7).

## 6.5 ✅ Quyết định 2 — Chống cày điểm *(đã chốt)*

**Không làm cơ chế chống cày riêng cho hoạt động chỉ có Text/Ảnh.**

Hai cơ chế chung vẫn áp cho mọi loại hoạt động:

| Cơ chế | Tác dụng |
|---|---|
| **Chống cộng trùng nội dung đã hoàn thành** (`C5`) | Mỗi nội dung chỉ trả điểm **một lần duy nhất trong đời**, kể cả khi học lại qua lớp khác |
| **Trần điểm tối đa mỗi ngày** (`S8`) | Chặn việc dồn toàn bộ trong một buổi để vượt lên trong chiến dịch |

> **Rủi ro chấp nhận có chủ đích:** `KB-LX-03b` — hoạt động chỉ có Text/Ảnh vẫn được tính hoàn thành ngay khi mở hiển thị. Học viên bấm lướt vẫn nhận điểm. Chống cộng trùng giới hạn thiệt hại ở đúng một lần cho mỗi nội dung.

## 6.6 ✅ Quyết định 3 — Chỉ số xếp hạng của chiến dịch *(đã chốt, có hệ quả)*

Chiến dịch chọn được xếp hạng theo: **điểm** · **số huy hiệu** · **số khoá hoàn thành** (S16).

### 🚨 Hệ quả: tiêu chí phụ khi đồng hạng thành bắt buộc

Ba chỉ số không giống nhau về độ phân tán:

| Chỉ số | Khoảng giá trị thực tế trong một kỳ | Nguy cơ đồng hạng |
|---|---|---|
| Điểm | Hàng trăm đến hàng nghìn | Thấp |
| Số huy hiệu | 0–10 | **Cao** |
| Số khoá hoàn thành | 0–5 | **Rất cao** |

Xếp hạng theo "số khoá hoàn thành" trong một chiến dịch một tháng thì phần lớn học viên cùng ở mức 1–2 khoá — **hàng chục người đồng hạng nhất**. Bảng xếp hạng mất ý nghĩa.

→ **`S22` — cùng chỉ số thì ai đạt mức đó sớm hơn xếp trên** — từ chỗ *nên có* thành **bắt buộc**. Không có nó thì hai trong ba chỉ số không dùng được.

Rule này cũng phục vụ đúng `Problem`: học viên học sớm xếp trên học viên học dồn sát hạn, dù cùng chỉ số.

**Kéo theo `C8`:** cần thời điểm đạt cho cả ba loại mốc — cộng điểm, đạt huy hiệu, hoàn thành khoá. `C3` mới bao được loại đầu. `OQ-B12`.

**Và snapshot phải ghi kèm chỉ số đã dùng** (S19) — chiến dịch xếp theo huy hiệu và chiến dịch xếp theo điểm cho ra hai bảng không so sánh được với nhau.

## 6.7 ✅ Quyết định 4 — Phạm vi xếp hạng *(đã chốt)*

**Đợt này chỉ có một bảng xếp hạng toàn tổ chức.** Bộ lọc theo lớp và theo phòng ban gộp thành một hạng mục hoãn duy nhất (N1), chờ chức năng nhóm đồng bộ từ HRM.

Lý do: bộ lọc theo lớp **sau này chính là bộ lọc theo nhóm**. Làm riêng cho lớp bây giờ thì trùng mục đích, sau phải làm lại.

> ⚠️ **Rủi ro ghi nhận để theo dõi sau ra mắt, không phải để đổi quyết định:** với hàng nghìn học viên, phần lớn sẽ không bao giờ ở gần nhóm đầu. Chu kỳ ngắn không đổi được điều đó vì người chăm nhất vẫn đứng đầu mọi chu kỳ. Cơ chế giảm nhẹ duy nhất là **"Vị trí của tôi"** (S18).

---

# 7. Danh sách User Story dự kiến

## Phía học viên (UpLMS)

| ID | User Story | Nguồn | Ghi chú |
| --- | --- | --- | --- |
| **US1** | Là học viên, tôi cần xem điểm, hạng và huy hiệu đã đạt để biết nỗ lực học của mình được ghi nhận tới đâu | Dòng 10 · O2 | Trang "Thành tích của tôi" |
| **US2** | Là học viên, tôi cần được báo ngay khi nhận điểm, đạt huy hiệu hoặc lên hạng để cảm nhận được sự ghi nhận đúng lúc | Dòng 9 · O2 | `OQ-B5` về độ trễ |
| **US3** | Là học viên, tôi cần tra được từng lần cộng điểm đến từ đâu để tin vào con số của mình | Dòng 8 · O6 · C3 | |
| **US4** | Là học viên, tôi cần biết huy hiệu nào sắp đạt và còn thiếu gì để có mục tiêu ngắn hạn | Dòng 10 · O3 | Tính tiến độ tới **mọi** huy hiệu chưa đạt |
| **US5** | Là học viên, tôi cần việc quay lại học đều đặn mỗi ngày được ghi nhận thành chuỗi ngày liên tiếp để có lý do duy trì thói quen | Dòng 2, 4 · O1 | ⚠️ Phụ thuộc Keycloak — `OQ-B1` |
| **US6** | Là học viên, tôi cần xem bảng xếp hạng của kỳ tôi chọn để biết mình đứng ở đâu so với người khác | CR-001 · S14 | **Toàn tổ chức.** Kỳ lịch + chiến dịch |
| **US7** | Là học viên, tôi cần luôn thấy vị trí của chính mình kèm vài người liền kề, kể cả khi không ở nhóm đầu, để biết mình cần hơn ai một chút là lên hạng | CR-001 · S18 | Cơ chế giảm nhẹ chính cho bảng toàn tổ chức |
| **US8** | Là học viên, tôi cần xem lại bảng xếp hạng của các kỳ đã kết thúc để nhìn lại thành tích đã đạt | CR-001 · S20 | |

## Phía vận hành (UpLMS Ops)

| ID | User Story | Nguồn | Ghi chú |
| --- | --- | --- | --- |
| **US9** | Là nhân sự vận hành, tôi cần khai hành động nào được bao nhiêu điểm và bật/tắt từng hành động để điều chỉnh cơ chế theo mục tiêu từng giai đoạn | Dòng 1, 2 | Chịu `C2`, `C4` |
| **US10** | Là nhân sự vận hành, tôi cần tạo và quản lý huy hiệu cùng điều kiện đạt để thiết kế các mốc mục tiêu cho học viên | Dòng 3, 4 | 4 loại điều kiện (S5) |
| **US11** | Là nhân sự vận hành, tôi cần đặt các hạng và ngưỡng điểm để phân tầng mức độ tham gia của học viên | Dòng 5 | |
| **US12** | Là nhân sự vận hành, tôi cần tạo chiến dịch có thời hạn riêng, chọn phạm vi người tham gia và **chọn chỉ số xếp hạng**, để đội truyền thông chạy đợt thi đua phù hợp với mục tiêu từng đợt | CR-001 · CR-002 · S15, S16 | **Chỉ áp cho chiến dịch.** Kỳ lịch không cần màn quản lý |
| **US13** 🆕 | Là nhân sự vận hành, tôi cần chiến dịch đang chạy không sửa được để kết quả thi đua không bị thay đổi luật giữa chừng | CR-002 · S17 | Chi tiết trạng thái để ở PRD |
| **US14** | Là nhân sự vận hành, tôi cần bảng xếp hạng được đóng băng và lưu lại khi hết kỳ để công bố kết quả không thay đổi và trao thưởng | CR-001 · S19 · O5 | Lưu kèm **chỉ số đã dùng**. Trao thưởng làm ngoài hệ thống (N8) |
| **US15** | Là nhân sự vận hành, tôi cần điểm phản ánh việc học thật, không bị đẩy lên bằng thao tác đối phó, để cơ chế còn đáng tin | Dòng 7 · O6 | Chịu `C5`. Quyết định §6.5 |
| **US16** | Là nhân sự vận hành, tôi cần bật/tắt gamification và bật/tắt hiển thị phía học viên riêng biệt, để chạy thử cơ chế trước khi mở cho học viên | Dòng 11 · S12 | Quyết định §6.4 |
| **US17** | Là quản trị, tôi cần phân quyền để chỉ vai trò vận hành phù hợp mới sửa được cấu hình gamification | `[suy ra]` · S13 | |

## Chưa làm trong đợt này

| ID | User Story | Nguồn | Ghi chú |
| --- | --- | --- | --- |
| **US18** | *Bộ lọc bảng xếp hạng theo nhóm* — Là quản lý, tôi cần lọc bảng xếp hạng theo lớp hoặc phòng ban để biết học viên trong nhóm đó học thế nào — **chưa làm** | N1 · CR-003 | Chờ chức năng nhóm **đồng bộ từ HRM**. Gộp cả lớp và phòng ban để không làm hai lần |
| **US19** | *Giới hạn nội dung chiến dịch* — Là nhân sự vận hành, tôi cần chỉ định nội dung nào được tính vào chiến dịch — **chưa làm** | N3 | PO không yêu cầu ở đợt này |
| **US20** | *Điểm cho lộ trình* — Là học viên, tôi cần được cộng điểm khi hoàn thành một lộ trình học — **chưa làm** | N4 | Chờ tính năng Lộ trình |
| **US21** | *Huy hiệu theo kỹ năng* — Là học viên, tôi cần nhận huy hiệu khi đạt được một kỹ năng cụ thể — **chưa làm** | N5 | Chờ tính năng Khung năng lực |
| **US22** | *Hiệu quả chiến dịch* — Là đội truyền thông nội bộ, tôi cần theo dõi chiến dịch có làm tăng mức độ tham gia hay không — **chưa làm** | N14 · O4 | ⚠️ Khoảng trống thật — `OQ-B3` |
| **US23** | *Tính bù điểm* — Là nhân sự vận hành, tôi cần tính bù điểm cho giai đoạn gamification bị tắt — **chưa làm** | N7 · §6.4 | |

> **US22 vẫn là khoảng trống.** `O4` nói mục tiêu là để đội truyền thông chạy chiến dịch **đo được**. Họ tạo được chiến dịch (US12) và thấy được bảng xếp hạng (US6) — nhưng bảng xếp hạng cho biết *ai đứng đầu*, không cho biết *chiến dịch có tác dụng*.

---

# 8. Tác động tới hệ thống hiện tại

> **Chưa chạy Impact Analysis.** Đánh giá sơ bộ từ KB, DB schema và Swagger. **Chi tiết ở Gate 2.**

| Vùng ảnh hưởng | Mức | Ghi chú |
| --- | --- | --- |
| **Dữ liệu** | 🔴 Cao | Toàn bộ cấu trúc điểm, huy hiệu, hạng, kỳ, chiến dịch, sổ giao dịch, snapshot cuối kỳ là mới. Chịu C1–C8 |
| **Hiệu năng** | 🔴 Cao | Xếp hạng tính từ sổ giao dịch theo khoảng ngày, trên toàn tổ chức, cho nhiều kỳ lồng nhau, **theo ba chỉ số khác nhau**. Chưa ước lượng được tải — `OQ-B9` |
| **Tổ chức / Tenant** | 🟠 Vừa | Thêm tham số múi giờ cấp tổ chức (S21, C6). Bảng `tenant` hiện không có trường này |
| **Learning Experience** | 🟠 Vừa | Nguồn sự kiện chính. Chỉ đọc, không sửa. `KB-LX-03b` là rủi ro đã chấp nhận (§6.5) |
| **Notification** | 🟠 Vừa | US2 cần thông báo theo sự kiện cho từng người. Cơ chế hiện có là soạn tay gửi theo nhóm, theo job nửa tiếng (`KB-NOTI-05`). Hộp thư và push phía học viên tái dùng được. 3/4 page module này **đang ẩn** |
| **Assessment / Grading** | 🟠 Vừa | Nguồn sự kiện. ⚠️ 8 mail luồng chấm điểm **đang tắt** (`KB-MAIL-03`) |
| **Course / Certificate** | 🟠 Vừa | Nguồn sự kiện. Mail #10 và #29 đã chạy cho cùng sự kiện. 🆕 Thêm vai trò: **thời điểm hoàn thành khoá** là dữ liệu xếp hạng (C8) |
| **User / Auth** | 🟠 Vừa | US5 phụ thuộc sự kiện đăng nhập Keycloak — `OQ-B1` |
| **Class** | 🟡 Thấp | 🔄 Giảm từ 🟠 xuống 🟡 sau khi bỏ bộ lọc theo lớp (N1). Vẫn là lý do sinh ra `C5` |
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
| ~~A8~~ | ~~Các chiến dịch không chồng lấn thời gian~~ | ❌ Bị bác bỏ bởi `CR-001` → thay bằng `C7` |
| A9 | Ảnh huy hiệu và ảnh hạng dùng hạ tầng quản lý tài nguyên sẵn có | Gate 2 |
| A10 | **Dữ liệu tiến độ học có dấu thời gian** | Dev — `OQ-B2` |
| A11 | **Keycloak ghi và giữ được sự kiện đăng nhập** | Dev — `OQ-B1` |
| A12 | Vận hành **không cần sửa hay xoá điểm thủ công** của một học viên | PO xác nhận |
| A13 | **Bảng xếp hạng chỉ hiện học viên, không hiện nhân sự Ops** | PO xác nhận |
| A14 | **Học viên bị Block hoặc đã rời tổ chức không xuất hiện trong bảng đang chạy**, nhưng **vẫn giữ nguyên trong snapshot kỳ đã chốt** | PO xác nhận |
| A15 | **Bảng xếp hạng công khai danh tính học viên** với nhau (tên, ảnh) | PO xác nhận — **vấn đề riêng tư, không phải chi tiết kỹ thuật** |
| A16 | **Kỳ lịch bắt đầu từ thời điểm bật tính năng**, không dựng lại bảng cho tháng/quý trước ngày go-live | PO xác nhận |
| **A17** 🆕 | **Kỳ lịch luôn xếp theo điểm.** Việc chọn chỉ số (S16) chỉ áp cho chiến dịch | PO xác nhận |
| **A18** 🆕 | **Chiến dịch chưa tới ngày bắt đầu thì sửa được**, chỉ khoá khi đã chạy | PO xác nhận — S17 chỉ nói "đang chạy thì không sửa" |
| **A19** 🆕 | **Tắt `Visibility in UpLMS` không dừng việc gửi thông báo thành tích** — hoặc có? | PO xác nhận. Nếu vẫn gửi thì học viên nhận thông báo về thứ họ không xem được |

---

# 10. Open Questions

| # | Câu hỏi | Vì sao quan trọng | Người trả lời | Chặn bước sau? |
| --- | --- | --- | --- | --- |
| **OQ-B1** | **Keycloak có bật ghi sự kiện đăng nhập không, giữ bao lâu, lấy ra bằng cách nào?** | Không có thì US5 và điều kiện huy hiệu "chuỗi ngày" không làm được | Dev | **Yes** — trước Gate 2 |
| **OQ-B2** | **Dữ liệu tiến độ học có dấu thời gian không?** | Cần cho C5, C7, trần điểm/ngày | Dev | **Yes** — trước Gate 2 |
| **OQ-B9** | **Bảng xếp hạng chịu tải được không?** Tính thứ hạng từ sổ giao dịch theo khoảng ngày, toàn tổ chức, nhiều kỳ lồng nhau, ba chỉ số | Quyết định giữa tính trực tiếp và tính sẵn theo chu kỳ. Ảnh hưởng thẳng tới thiết kế dữ liệu | Dev | **Yes** — trước Gate 2 |
| **OQ-B12** 🆕 | **Thời điểm đạt huy hiệu và thời điểm hoàn thành khoá có lưu được không?** | `C8` — cần cho tiêu chí phụ khi đồng hạng (S22), mà S22 là bắt buộc để hai trong ba chỉ số dùng được | Dev | **Yes** — trước Gate 2 |
| **OQ-B3** | **Đội truyền thông nội bộ cần gì để biết chiến dịch có tác dụng?** (US22) | `O4` là một trong sáu mục tiêu | PO | No — ảnh hưởng phạm vi |
| **OQ-B4** | **Ba con số ở §2** | Mục `Analytics` của PRD cần dữ liệu | PO + Dev | No — trước khi viết PRD |
| **OQ-B5** | **Thông báo thành tích chấp nhận trễ tới mức nào?** | Trễ 30 phút thì mất tác dụng khích lệ | PO | No — Gate 2 |
| **OQ-B6** | **Hoàn thành khoá đã có mail #10 và #29.** Gộp hay tách kênh? | Tránh hai thông báo cho một sự kiện | PO | No — Gate 2 |
| **OQ-B7** | **Luồng chấm điểm đang tắt toàn bộ thông báo.** Có bật lại mail #19 không? | *Quyết định của luồng Grading* | PO | No — nêu để biết |
| **OQ-B8** | **Chốt từ vựng.** "Point" đã là điểm đậu; "Level" đã là độ khó khoá và cấp bậc nhân sự | Tên đi vào cấu trúc dữ liệu và tài liệu bàn giao | PO | No — trước khi viết PRD |
| **OQ-B10** | **Đồng hạng xử lý thế nào khi trùng cả thời điểm đạt?** | Thứ hạng hiển thị phải xác định, không nhảy mỗi lần tải lại | PO | No — Field Intake |
| **OQ-B11** | **Múi giờ tổ chức khai ở đâu trong đợt này?** Đề xuất: một tham số cấp tổ chức, để module Tenant sau tiếp quản | `C6`. Đóng cứng rồi gỡ sau thì đắt | PO + Dev | No — Gate 2 |
| **OQ-B13** 🆕 | **Chiến dịch có chồng lấn nhau được không?** Hai chiến dịch cùng chạy một lúc, mỗi cái một chỉ số khác nhau | Ảnh hưởng cách học viên chọn bảng để xem và cách tính snapshot | PO | No — Gate 2 |

---

# 11. References

## Knowledge Base đã đọc

| File | Dùng cho |
|---|---|
| `07-learning-experience.md` | `KB-LX-03a`, `KB-LX-03b` — nền của §6.5. **Đã cập nhật trong đợt này** |
| `09-notification-email.md` | Cơ chế thông báo, `KB-NOTI-05`, trạng thái ẩn |
| `13-mail-events.md` | 30 mail tự động, mail #10/#29, `KB-MAIL-03` |
| `12-data-model.md` | Cấu trúc dữ liệu — nền của `C5`, `C6`; phát hiện phòng ban chỉ gắn nhân sự |
| `14-api-surface.md` | `Group Management` (9 endpoint), `Department Management` (9 endpoint) |
| `15-product-direction.md` | Định hướng đa tenant — nền của `C1` |
| `01-course.md` · `03-assessment.md` · `04-class.md` · `08-certificate.md` | Nguồn sự kiện tính điểm |

## Nguồn khác

| Nguồn | |
|---|---|
| Yêu cầu gốc | `working/raw-inputs/yeu-cau-goc-20260923.md` |
| Change requests | `working/raw-inputs/change-requests.md` — **CR-001 · CR-002 · CR-003** |
| Bản làm rõ | `working/ai-drafts/clarified-requirements-20260923.md` |
| Open questions | `working/open-questions/open-questions-20260923.md` |
| Quyết định đã chốt | `project-decisions.md` |
| BRD bản trước | `docs/brd/brd-v0.1-20260923.md` · `docs/brd/brd-v0.2-20260923.md` |
| Schema DB | [Lark → Data Architecture](https://upbasevn.sg.larksuite.com/wiki/MaFpweI68iKNMvkTioLlJ1uJgQd) — đối chiếu 23/09/2026 |
| Swagger | `lms-be.staging.upbase.asia/api/v1/docs` · `ops-be.staging.upbase.asia/api/v1/docs` |
| Tham chiếu ngoài | `TNT.CFG.02` — Hồ sơ tổ chức và tham số, thuộc module Tenant *(chưa làm)* |
