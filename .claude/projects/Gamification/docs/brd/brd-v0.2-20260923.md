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

| Version | Người cập nhật | Nội dung | Impact | Ngày |
| --- | --- | --- | --- | --- |
| v0.1 | PO | Bản đầu | — | 23/09/2026 |
| **v0.2** | PO | **Đưa bảng xếp hạng vào phạm vi.** Tách kỳ lịch khỏi chiến dịch · bác bỏ `A8` · thêm `C6` (múi giờ tổ chức) và `C7` (một điểm thuộc nhiều kỳ) · hoãn "giới hạn nội dung chiến dịch" · US từ 17 lên 22 | `CR-001` | 23/09/2026 |

**Nguồn input:** `working/raw-inputs/yeu-cau-goc-20260923.md` · `working/raw-inputs/change-requests.md` (CR-001) · `working/ai-drafts/clarified-requirements-20260923.md` · `project-decisions.md`

---

# 1. Problem

**Học viên đã được ghi danh vào khoá nhưng không chủ động quay lại học.**

| | |
|---|---|
| **Ai gặp** | Học viên trên UpLMS — người đã có tài khoản, đã được thêm vào lớp, đã có nội dung để học |
| **Gặp khi nào** | Trong suốt thời gian học, đặc biệt ở giai đoạn giữa khoá khi không còn động lực ban đầu và chưa thấy đích |
| **Hậu quả** | Học viên học dở dang hoặc học dồn sát hạn. Vận hành phải thúc thủ công. Đội truyền thông nội bộ muốn tổ chức phong trào học tập nhưng không có cơ chế nào để gắn hoạt động của học viên vào một chiến dịch có thể theo dõi được |

Hệ thống hiện tại **chỉ ghi nhận việc học, không phản hồi lại việc học**. Học viên hoàn thành một hoạt động thì thanh tiến độ nhích lên — ngoài ra không có gì. Không có sự ghi nhận, không có mốc để nhắm tới, không có lý do để quay lại vào ngày hôm sau khi chưa tới hạn.

---

# 2. Analytics

> ⚠️ **Chưa có dữ liệu định lượng.** Phần dưới là căn cứ định tính từ PO cộng với những gì quan sát được trong hệ thống. Xem `OQ-B4`.

## Vận hành đang xoay xở thế nào

| Hướng | Hiện trạng |
|---|---|
| **Cách làm hiện tại** | Vận hành theo dõi tiến độ học qua dashboard SIS (*Tiến độ học trên UpLMS*), thấy ai chậm thì thúc. Hệ thống có 30 mail tự động nhưng đều là **mail sự kiện** — chào mừng, nhắc lịch kiểm tra, báo hết hạn khoá — không có mail nào nhằm tạo động lực |
| **Công cụ sẵn có bị hạn chế** | Giao diện soạn và gửi thông báo thủ công trên Ops **đang ẩn** (3/4 page module Notification & Email). Đội truyền thông nội bộ muốn gửi thông điệp khích lệ tới nhóm học viên cụ thể thì hiện không có đường tự phục vụ |
| **Tiêu chí quyết định** | Vận hành nhìn phần trăm tiến độ và thời hạn còn lại. Hai con số này **cho biết ai đang chậm, không cho biết ai đang cố gắng** — học viên đi đều mỗi ngày và học viên học dồn một buổi trông giống nhau khi đã cùng phần trăm |
| **Chỗ sai** | Việc thúc học phụ thuộc vào vận hành nhớ và làm thủ công. Không mở rộng được khi số lớp tăng, và **không tạo được thói quen** — học viên phản ứng với lời nhắc, không tự quay lại |

## Còn thiếu để mục này đủ chắc

Ba câu hỏi lấy được ngay từ dữ liệu hệ thống — `OQ-B4`:

1. Tỷ lệ học viên có tiến độ đứng yên quá 14 ngày liên tiếp?
2. Bao nhiêu phần trăm hoạt động được hoàn thành trong 7 ngày cuối trước hạn?
3. Tỷ lệ khoá được hoàn thành so với số khoá được ghi danh?

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

> `O5` thay cho *"có nền dữ liệu cho bảng xếp hạng ở đợt sau"* của v0.1 — bảng xếp hạng nay làm luôn trong đợt này.

---

# 4. Stakeholder

| Stakeholder | Action |
| --- | --- |
| **Học viên (UpLMS)** | Nhận điểm · nhận huy hiệu · lên hạng · xem trang thành tích · tra lịch sử điểm · **xem bảng xếp hạng và vị trí của mình** |
| **Nhân sự vận hành (UpLMS Ops)** | Khai bảng điểm · tạo huy hiệu · đặt hạng và ngưỡng · **tạo chiến dịch** · bật/tắt cơ chế |
| **Đội truyền thông nội bộ** | Thiết kế và chạy chiến dịch thúc đẩy tinh thần học · **công bố kết quả cuối kỳ và trao thưởng ngoài hệ thống** |
| **Quản lý đào tạo / L&D** | Dùng dữ liệu điểm, hạng và xếp hạng để đánh giá mức độ tham gia |
| Dev | Xác nhận `OQ-B1` (Keycloak), `OQ-B2` (dấu thời gian dữ liệu tiến độ) |
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
| S8 | **Chống cày điểm** — khử trùng nội dung đã hoàn thành, trần điểm tối đa mỗi ngày |
| S9 | **Lịch sử điểm** — học viên tra được từng lần cộng đến từ đâu |
| S10 | **Thông báo thành tích** — nhận điểm, nhận huy hiệu, lên hạng |
| S11 | **Trang "Thành tích của tôi"** — điểm, hạng, huy hiệu đã có, huy hiệu sắp đạt kèm phần còn thiếu |
| S12 | **Bật/tắt gamification ở cấp tổ chức** |
| S13 | **Phân quyền cấu hình** |
| **S14** | 🆕 **Bảng xếp hạng theo kỳ lịch** — tuần · tháng · quý · năm. Hệ thống tự tính, không cần cấu hình |
| **S15** | 🆕 **Chiến dịch** — vận hành khai khoảng thời gian bất kỳ (không cần trùng biên lịch), kèm tên và phạm vi người tham gia |
| **S16** | 🆕 **Phạm vi xếp hạng** — toàn tổ chức và trong lớp. Học viên chọn được phạm vi muốn xem |
| **S17** | 🆕 **"Vị trí của tôi"** — luôn hiện thứ hạng người đang xem kèm vài người liền kề, kể cả khi không ở nhóm đầu |
| **S18** | 🆕 **Chốt kỳ** — hết kỳ thì đóng băng bảng, lưu kết quả cuối, mở kỳ mới về 0 |
| **S19** | 🆕 **Lịch sử các kỳ đã kết thúc** — xem lại bảng xếp hạng tháng trước, quý trước, chiến dịch đã xong |
| **S20** | 🆕 **Tham số múi giờ ở cấp tổ chức** — biên kỳ cắt theo múi giờ tổ chức, không theo giờ máy chủ |

## Out of scope

| # | Không làm | Vì sao |
|---|---|---|
| N1 | **Xếp hạng theo phòng ban** | Phòng ban = chức năng nhóm, **đồng bộ từ HRM của tổ chức** thành cây sơ đồ tổ chức — chưa làm. Hiện `departments` chỉ gắn với nhân sự, học viên không có phòng ban |
| N2 | **Giới hạn nội dung được tính trong chiến dịch** | Hoãn — xem quyết định §6.5 |
| N3 | **Tính năng Lộ trình học** và hành động "hoàn thành lộ trình" | Tính năng riêng, làm sau |
| N4 | **Tính năng Khung năng lực / Skills** và điều kiện huy hiệu "đạt kỹ năng" | Tính năng riêng, làm sau |
| N5 | **Sửa logic hoàn thành Activity** | PO chốt giữ nguyên |
| N6 | **Tính bù điểm cho giai đoạn gamification bị tắt** | Cần phát lại theo từng ngày để áp đúng trần điểm |
| N7 | **Quản lý phần thưởng trong hệ thống** | PO xác nhận **trao thưởng là hành động ngoài hệ thống**. Hệ thống chỉ giữ lại bảng xếp hạng cuối kỳ |
| N8 | **Gamification cho nhân sự Ops** | Chỉ áp dụng cho học viên |
| N9 | **Thi đua theo đội / nhóm** | Chỉ xếp hạng cá nhân |
| N10 | **Cấu hình gamification riêng theo lớp hoặc khoá** | Cấu hình ở cấp tổ chức |
| N11 | **Màn quản lý nhiều tổ chức** | Chưa có multi-tenant. Nhưng dữ liệu vẫn thiết kế theo tổ chức — `C1` |
| N12 | **Module Tenant (`TNT.CFG.02`) đầy đủ** | Đợt này chỉ khai **tham số múi giờ** (S20), phần còn lại của hồ sơ tổ chức thuộc module Tenant |
| N13 | **Trang theo dõi hiệu quả chiến dịch cho đội truyền thông** | Chưa có trong yêu cầu — `OQ-B3` |

## Potential scope

Xếp hạng theo phòng ban sau khi đồng bộ HRM · giới hạn nội dung chiến dịch · tính bù điểm · trang hiệu quả chiến dịch · điểm cho lộ trình · huy hiệu theo kỹ năng · đổi điểm lấy phần thưởng

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

Nguyên tắc xuyên suốt: **gamification chỉ đọc, không sửa dữ liệu học tập.** Nó nghe việc đã xảy ra và ghi ra bản ghi của riêng nó. Đây là điều kiện để giữ được `N5` và để bật/tắt không ảnh hưởng gì tới việc học.

## 6.2 Hai loại kỳ — khác bản chất, không gộp

| | **Kỳ lịch** | **Chiến dịch** |
|---|---|---|
| Ai tạo | **Hệ thống tự tính** | **Vận hành khai tay** |
| Biên | Cố định theo lịch — tuần, tháng, quý, năm. **Không dùng cửa sổ trượt** | Hai ngày bất kỳ, **không cần trùng biên lịch** |
| Cấu hình | Không cần màn nào | Có tên, phạm vi người tham gia |
| Ví dụ | Tháng 9 · Quý III · Năm 2026 | *"Tháng an toàn thông tin 10/9–15/10"* |

Cả hai đều bị chốt và đóng băng khi hết kỳ (S18), đều xem lại được (S19).

## 6.3 Ràng buộc thiết kế bắt buộc

| # | Ràng buộc | Vì sao |
|---|---|---|
| **C1** | Cấu hình gắn với **tổ chức**, không đóng cứng | Định hướng đa tenant. Hiện một tổ chức nên chi phí bằng 0 |
| **C2** | **Danh mục hành động tính điểm và danh mục điều kiện huy hiệu phải mở rộng được bằng cấu hình** | Lộ trình (N3), kỹ năng (N4), phòng ban (N1), giới hạn nội dung (N2) đều sẽ thêm sau |
| **C3** | Lưu **từng lần cộng điểm kèm thời điểm**, không chỉ lưu tổng | Nền của lịch sử điểm (S9), của xếp hạng theo kỳ (C7), và của luật chống cày |
| **C4** | Đổi cấu hình điểm → **áp dụng từ thời điểm đổi** | PO chốt |
| **C5** | Khử trùng "đã học" tính theo **người học**, không theo lượt ghi danh lớp | Học viên có thể học cùng nội dung qua nhiều lớp |
| **C6** | 🆕 **Biên kỳ cắt theo múi giờ của tổ chức**, không theo giờ máy chủ | Yêu cầu CR-001. Module Tenant (`TNT.CFG.02`) chưa có → đợt này khai một tham số múi giờ cấp tổ chức, thiết kế để module Tenant sau tiếp quản |
| **C7** | 🆕 **Một lần cộng điểm thuộc về nhiều kỳ cùng lúc** → điểm theo kỳ **tính từ sổ giao dịch theo khoảng ngày**, không cộng dồn vào một con số. **Nhưng kết quả cuối kỳ phải được lưu cứng**, không tính lại mỗi lần xem | Kỳ lịch lồng nhau (tuần ⊂ tháng ⊂ quý ⊂ năm) và chiến dịch chạy song song. Bác bỏ `A8` của v0.1 |

> **C5 và C7 là hai ràng buộc dễ bỏ sót nhất.** C5 vì dữ liệu tiến độ hiện gắn với lượt ghi danh lớp chứ không gắn với người. C7 vì cách gọi "điểm theo kỳ" dễ khiến người đọc tưởng đó là một con số được cộng dồn.

## 6.4 Quyết định 1 — "Tắt gamification" nghĩa là gì

*(Không đổi so với v0.1. Phân tích đầy đủ ở `clarified-requirements-20260923.md` §13.)*

| Hướng | Nội dung | Đánh đổi |
|---|---|---|
| A | Một công tắc — tắt là dừng hẳn | Đơn giản nhất. Nhưng không có cách chạy thử |
| B | Một công tắc — tắt chỉ ẩn hiển thị | Bật lại có sẵn dữ liệu. Nhưng không có trạng thái "tắt thật" |
| **C** ⭐ | **Hai công tắc** (`Ghi nhận` + `Hiển thị cho học viên`) → *Tắt hẳn* · *Chạy ngầm* · *Bật đầy đủ* | Thêm một cờ + luật không bắn thông báo hồi tố. Đổi lại có giai đoạn chạy thử |

`Recommendation` — **C**. Số điểm đặt lần đầu gần như chắc chắn sai, mà một khi học viên đã thấy điểm và hạng thì chỉnh xuống là lấy đi thứ họ đã có.

> **Bảng xếp hạng làm lý do này mạnh hơn.** Một bảng xếp hạng ra mắt với cấu hình điểm sai thì không chỉ gây thắc mắc — nó tạo ra thứ hạng sai công khai giữa các học viên với nhau.

**Phải chấp nhận nếu chọn C:** khi chuyển từ *Chạy ngầm* sang *Bật đầy đủ*, **không bắn thông báo hồi tố**.
**Ghi rõ trong PRD dù chọn hướng nào:** bật lại sau khi tắt hẳn thì tính từ thời điểm bật, không tính bù (N6).

## 6.5 Quyết định 2 — Chống cày điểm với hoạt động Text/Ảnh

*(Không đổi so với v0.1.)*

Video nay đã chặt (xem ≥80% thời lượng — `KB-LX-03a`), nhưng Text/Ảnh vẫn hoàn thành khi mở hiển thị (`KB-LX-03b`). Nên cơ chế *"không cộng điểm cho hoạt động bỏ qua quá nhanh"* không áp dụng được cho loại này.

| Hướng | Nội dung | Đánh đổi |
|---|---|---|
| **A** ⭐ | Trần điểm/ngày + khử trùng + **cho phép khai số điểm khác nhau theo loại hoạt động** | Không thêm cơ chế mới. Mỗi nội dung chỉ trả điểm **một lần duy nhất trong đời** |
| B | Gamification tự đo thời gian riêng | Chính xác hơn, nhưng học viên thấy hoạt động ✅ mà không được điểm, không hiểu vì sao |
| C | Không cộng điểm cho hoạt động Text/Ảnh | An toàn nhưng mất phần lớn cơ hội cộng điểm đều đặn |

`Recommendation` — **A**.

## 6.6 Quyết định 3 — 🆕 Chiến dịch có giới hạn nội dung không

**Vấn đề PO nêu:** nếu chiến dịch chỉ tính một khoá, điểm có trần. Ai hoàn thành cũng bằng điểm nhau → đồng hạng hàng loạt → bảng xếp hạng vô nghĩa. Thêm tiêu chí thời gian hoàn thành thì giải được nhưng phức tạp.

**Nhận định:** vấn đề chỉ xảy ra **khi nội dung bị giới hạn**. Kỳ lịch tính mọi hoạt động nên điểm phân tán tự nhiên.

| Hướng | Nội dung | Đánh đổi |
|---|---|---|
| A | Giữ giới hạn nội dung, thêm tiêu chí phụ theo thời điểm | Vẫn không cứu được khi mọi người cùng hoàn thành 100% |
| **B** ⭐ | **Hoãn "giới hạn nội dung" sang đợt sau.** Chiến dịch = khoảng thời gian + phạm vi người tham gia, mọi nội dung đều tính. Nhu cầu *"cùng học khoá X trước ngày Y"* dùng **huy hiệu** | Bỏ một tính năng khỏi đợt này, nhưng dùng đúng công cụ hơn |
| C | Chiến dịch giới hạn nội dung xếp theo **thời điểm hoàn thành** thay vì theo điểm | Là cơ chế thứ hai phải xây và phải giải thích cho học viên |

`Recommendation` — **B, kèm một rule chung lấy từ A**:

**Vì sao B:** nhu cầu *"tháng này cả công ty cùng học khoá An toàn thông tin"* **vốn không phải bài toán xếp hạng** — nó là bài toán *đạt hay chưa đạt trước hạn*. Công cụ đúng là **huy hiệu có điều kiện thời gian**, mà `S5` đã có sẵn: ghép điều kiện *"hoàn thành một nội dung cụ thể"* với *"theo mốc thời gian"* là ra đúng *"hoàn thành khoá X trước 15/10 thì được huy hiệu Y"*.

Dùng bảng xếp hạng cho việc này là dùng sai công cụ — và chính vì sai công cụ nên mới sinh ra bài toán đồng hạng.

**Rule chung lấy từ A:** cùng số điểm thì **ai đạt mức đó sớm hơn xếp trên**. Rẻ hơn tưởng — `C3` đã bắt lưu từng lần cộng điểm kèm thời điểm, nên đây chỉ là sắp xếp theo `(điểm giảm dần, thời điểm đạt tăng dần)`. Không cần dữ liệu mới, không cần cơ chế mới. Và nó phục vụ đúng `Problem`: học viên học sớm xếp trên học viên học dồn sát hạn.

## 6.7 🆕 Phạm vi xếp hạng — vì sao giữ lại phạm vi lớp

Phòng ban bỏ (N1). Còn lại **toàn tổ chức** và **trong lớp**.

`Recommendation` — **giữ phạm vi lớp**, không phải vì dữ liệu sẵn có, mà vì chính lập luận trong yêu cầu gốc: *"Chu kỳ ngắn cho người mới cơ hội đứng đầu"*.

Xếp hạng toàn tổ chức với hàng nghìn học viên thì gần như không ai đứng gần đầu — **chu kỳ ngắn không cứu được điều đó**, vì người chăm nhất vẫn đứng đầu mọi chu kỳ. Xếp hạng trong lớp 20–40 người mới thật sự cho người mới cơ hội. Dòng *"Vị trí của tôi"* (S17) là cách giảm đau cho bảng quá lớn, không phải cách tạo động lực.

> Chưa được PO xác nhận rõ — `OQ-A3`.

---

# 7. Danh sách User Story dự kiến

## Phía học viên (UpLMS)

| ID | User Story | Nguồn | Ghi chú |
| --- | --- | --- | --- |
| **US1** | Là học viên, tôi cần xem điểm, hạng và huy hiệu đã đạt để biết nỗ lực học của mình được ghi nhận tới đâu | Dòng 10 · O2 | Trang "Thành tích của tôi" |
| **US2** | Là học viên, tôi cần được báo ngay khi nhận điểm, đạt huy hiệu hoặc lên hạng để cảm nhận được sự ghi nhận đúng lúc | Dòng 9 · O2 | `OQ-B5` về độ trễ |
| **US3** | Là học viên, tôi cần tra được từng lần cộng điểm đến từ đâu để tin vào con số của mình | Dòng 8 · O6 · C3 | |
| **US4** | Là học viên, tôi cần biết huy hiệu nào sắp đạt và còn thiếu gì để có mục tiêu ngắn hạn | Dòng 10 · O3 | Cần tính tiến độ tới **mọi** huy hiệu chưa đạt |
| **US5** | Là học viên, tôi cần việc quay lại học đều đặn mỗi ngày được ghi nhận thành chuỗi ngày liên tiếp để có lý do duy trì thói quen | Dòng 2, 4 · O1 | ⚠️ Phụ thuộc Keycloak — `OQ-B1` |
| **US6** 🆕 | Là học viên, tôi cần xem bảng xếp hạng theo kỳ và theo phạm vi tôi chọn để biết mình đứng ở đâu so với người khác | CR-001 · S14, S16 | Kỳ lịch + chiến dịch · phạm vi tổ chức + lớp |
| **US7** 🆕 | Là học viên, tôi cần luôn thấy vị trí của chính mình kèm vài người liền kề, kể cả khi không ở nhóm đầu, để biết mình cần hơn ai một chút là lên hạng | CR-001 · S17 | |
| **US8** 🆕 | Là học viên, tôi cần xem lại bảng xếp hạng của các kỳ đã kết thúc để nhìn lại thành tích đã đạt | CR-001 · S19 | |

## Phía vận hành (UpLMS Ops)

| ID | User Story | Nguồn | Ghi chú |
| --- | --- | --- | --- |
| **US9** | Là nhân sự vận hành, tôi cần khai hành động nào được bao nhiêu điểm và bật/tắt từng hành động để điều chỉnh cơ chế theo mục tiêu từng giai đoạn | Dòng 1, 2 | Chịu `C2`, `C4` |
| **US10** | Là nhân sự vận hành, tôi cần tạo và quản lý huy hiệu cùng điều kiện đạt để thiết kế các mốc mục tiêu cho học viên | Dòng 3, 4 | 4 loại điều kiện (S5). **Là công cụ đúng cho chiến dịch "cùng học khoá X"** — §6.6 |
| **US11** | Là nhân sự vận hành, tôi cần đặt các hạng và ngưỡng điểm để phân tầng mức độ tham gia của học viên | Dòng 5 | |
| **US12** 🆕 | Là nhân sự vận hành, tôi cần tạo chiến dịch có thời hạn riêng kèm phạm vi người tham gia để đội truyền thông chạy đợt thi đua không trùng biên lịch | CR-001 · S15 | **Chỉ áp cho chiến dịch.** Kỳ lịch không cần màn quản lý |
| **US13** 🆕 | Là nhân sự vận hành, tôi cần bảng xếp hạng được đóng băng và lưu lại khi hết kỳ để công bố kết quả không thay đổi và trao thưởng | CR-001 · S18 · O5 | Trao thưởng làm ngoài hệ thống (N7) |
| **US14** | Là nhân sự vận hành, tôi cần điểm phản ánh việc học thật, không bị đẩy lên bằng thao tác đối phó, để cơ chế còn đáng tin | Dòng 7 · O6 | Chịu `C5`. Quyết định §6.5 |
| **US15** | Là nhân sự vận hành, tôi cần bật/tắt gamification cho tổ chức để kiểm soát việc cơ chế có chạy và có hiện với học viên hay không | Dòng 11 | Quyết định §6.4 |
| **US16** | Là quản trị, tôi cần phân quyền để chỉ vai trò vận hành phù hợp mới sửa được cấu hình gamification | `[suy ra]` · S13 | |

## Chưa làm trong đợt này

| ID | User Story | Nguồn | Ghi chú |
| --- | --- | --- | --- |
| **US17** | *Xếp hạng theo phòng ban* — Là học viên, tôi cần xem bảng xếp hạng trong phòng ban của mình — **chưa làm** | N1 | Chờ **đồng bộ sơ đồ tổ chức từ HRM**. Nhờ `C2` nên chỉ cần thêm một phạm vi |
| **US18** | *Giới hạn nội dung chiến dịch* — Là nhân sự vận hành, tôi cần chỉ định nội dung nào được tính điểm trong một chiến dịch — **chưa làm** | N2 · §6.6 | Cần giải bài toán đồng hạng trước |
| **US19** | *Điểm cho lộ trình* — Là học viên, tôi cần được cộng điểm khi hoàn thành một lộ trình học — **chưa làm** | N3 | Chờ tính năng Lộ trình |
| **US20** | *Huy hiệu theo kỹ năng* — Là học viên, tôi cần nhận huy hiệu khi đạt được một kỹ năng cụ thể — **chưa làm** | N4 | Chờ tính năng Khung năng lực |
| **US21** | *Hiệu quả chiến dịch* — Là đội truyền thông nội bộ, tôi cần theo dõi chiến dịch có làm tăng mức độ tham gia hay không — **chưa làm** | N13 · O4 | ⚠️ Khoảng trống thật — `OQ-B3` |
| **US22** | *Tính bù điểm* — Là nhân sự vận hành, tôi cần tính bù điểm cho giai đoạn gamification bị tắt — **chưa làm** | N6 · §6.4 | |

> **US21 vẫn là khoảng trống.** `O4` nói mục tiêu là để đội truyền thông chạy chiến dịch **đo được**, và họ là stakeholder chính thức. Sau CR-001 họ tạo được chiến dịch (US12) và thấy được bảng xếp hạng (US6) — nhưng vẫn **không có chỗ nào cho biết chiến dịch có làm tăng mức độ tham gia hay không**. Bảng xếp hạng cho biết *ai đứng đầu*, không cho biết *chiến dịch có tác dụng*.

---

# 8. Tác động tới hệ thống hiện tại

> **Chưa chạy Impact Analysis.** Đánh giá sơ bộ từ KB, DB schema và Swagger ở Bước 2. **Chi tiết ở Gate 2.**

| Vùng ảnh hưởng | Mức | Ghi chú |
| --- | --- | --- |
| **Dữ liệu** | 🔴 Cao | Toàn bộ cấu trúc điểm, huy hiệu, hạng, kỳ, chiến dịch, sổ giao dịch, snapshot cuối kỳ là mới. Chịu C1, C2, C3, C5, C7 |
| **Hiệu năng** 🆕 | 🔴 Cao | Xếp hạng tính từ sổ giao dịch theo khoảng ngày (C7), trên toàn tổ chức, cho nhiều kỳ lồng nhau. **Chưa ước lượng được tải** — để Gate 2 |
| **Tổ chức / Tenant** 🆕 | 🟠 Vừa | Thêm tham số múi giờ cấp tổ chức (S20, C6). Bảng `tenant` hiện không có trường này |
| **Learning Experience** | 🟠 Vừa | Nguồn sự kiện chính. Chỉ đọc, không sửa. `KB-LX-03b` chi phối §6.5 |
| **Notification** | 🟠 Vừa | US2 cần thông báo theo sự kiện cho từng người. Cơ chế hiện có là soạn tay gửi theo nhóm, theo job nửa tiếng (`KB-NOTI-05`). Hộp thư và push phía học viên tái dùng được. 3/4 page module này **đang ẩn** |
| **Assessment / Grading** | 🟠 Vừa | Nguồn sự kiện. ⚠️ 8 mail luồng chấm điểm **đang tắt** (`KB-MAIL-03`) |
| **Course / Certificate** | 🟡 Thấp | Nguồn sự kiện. Mail #10 và #29 đã chạy cho cùng sự kiện — tránh trùng thông báo |
| **User / Auth** | 🟠 Vừa | US5 phụ thuộc sự kiện đăng nhập Keycloak — `OQ-B1` |
| **Class** 🆕 | 🟠 Vừa | Từ "chỉ là lý do sinh ra C5" lên thành **nguồn dữ liệu cho phạm vi xếp hạng theo lớp** (S16) |
| **Phân quyền** | 🟡 Thấp | Thêm nhóm quyền mới |

---

# 9. Assumptions

| # | Giả định | Kiểm chứng thế nào |
|---|---|---|
| A1 | Gamification chỉ áp dụng cho **học viên UpLMS** | PO xác nhận |
| A2 | Cấu hình đặt ở **UpLMS Ops** | PO xác nhận |
| A3 | **Hạng chỉ lên, không tụt** — điểm tích luỹ là vĩnh viễn | PO xác nhận |
| A4 | Điểm tích luỹ **không hết hạn** | PO xác nhận |
| A5 | Huy hiệu **đạt rồi giữ vĩnh viễn**, không thu hồi | PO xác nhận |
| A6 | Một hành động đồng thời cộng vào **cả điểm tích luỹ và điểm theo kỳ** | PO xác nhận |
| A7 | Điểm là **số nguyên** | PO xác nhận |
| ~~A8~~ | ~~Các chiến dịch không chồng lấn thời gian~~ | ❌ **Bị bác bỏ bởi CR-001** → thay bằng `C7` |
| A9 | Ảnh huy hiệu và ảnh hạng dùng hạ tầng quản lý tài nguyên sẵn có | Gate 2 |
| A10 | **Dữ liệu tiến độ học có dấu thời gian** | Dev — `OQ-B2` |
| A11 | **Keycloak ghi và giữ được sự kiện đăng nhập** | Dev — `OQ-B1` |
| A12 | Vận hành **không cần sửa hay xoá điểm thủ công** của một học viên | PO xác nhận |
| **A13** 🆕 | **Bảng xếp hạng chỉ hiện học viên, không hiện nhân sự Ops** | PO xác nhận |
| **A14** 🆕 | **Học viên bị Block hoặc đã rời tổ chức không xuất hiện trong bảng xếp hạng đang chạy**, nhưng **vẫn giữ nguyên trong snapshot kỳ đã chốt** | PO xác nhận. Ảnh hưởng tính đúng đắn của bảng |
| **A15** 🆕 | **Bảng xếp hạng công khai danh tính học viên** với nhau (tên, ảnh) | PO xác nhận — đây là vấn đề riêng tư, không phải chi tiết kỹ thuật |
| **A16** 🆕 | **Kỳ lịch bắt đầu từ thời điểm bật tính năng**, không dựng lại bảng xếp hạng cho tháng/quý trước ngày go-live | PO xác nhận |

---

# 10. Open Questions

| # | Câu hỏi | Vì sao quan trọng | Người trả lời | Chặn bước sau? |
| --- | --- | --- | --- | --- |
| **OQ-A1** | **Chọn hướng nào cho "tắt gamification"?** A · B · C — §6.4 | Quyết định cấu trúc cấu hình và luật thông báo | PO | **Yes** — Gate 1 |
| **OQ-A2** | **Chọn hướng nào cho chống cày với hoạt động Text/Ảnh?** A · B · C — §6.5 | Ảnh hưởng cấu trúc cấu hình điểm và trải nghiệm học viên | PO | **Yes** — Gate 1 |
| **OQ-A3** 🆕 | **Giữ phạm vi xếp hạng theo lớp không?** — §6.7 | Quyết định phạm vi. Nếu chỉ toàn tổ chức thì bảng xếp hạng gần như không với tới được với phần lớn học viên | PO | **Yes** — Gate 1 |
| **OQ-A4** 🆕 | **Chốt hướng cho chiến dịch có giới hạn nội dung** — §6.6. Đề xuất: hoãn (B) | Quyết định phạm vi US18 | PO | **Yes** — Gate 1 |
| **OQ-B1** | **Keycloak có bật ghi sự kiện đăng nhập không, giữ bao lâu, lấy ra bằng cách nào?** | Không có thì US5 và điều kiện huy hiệu "chuỗi ngày" không làm được | Dev | **Yes** — trước Gate 2 |
| **OQ-B2** | **Dữ liệu tiến độ học có dấu thời gian không?** | Cần cho C5, C7, trần điểm/ngày | Dev | **Yes** — trước Gate 2 |
| **OQ-B9** 🆕 | **Bảng xếp hạng chịu tải được không?** Tính thứ hạng từ sổ giao dịch theo khoảng ngày, trên toàn tổ chức, cho nhiều kỳ lồng nhau, mỗi lần học viên mở trang | Quyết định giữa tính trực tiếp và tính sẵn theo chu kỳ. Ảnh hưởng thẳng tới thiết kế dữ liệu | Dev | **Yes** — trước Gate 2 |
| **OQ-B3** | **Đội truyền thông nội bộ cần gì để biết chiến dịch có tác dụng?** (US21) | `O4` là một trong sáu mục tiêu | PO | No — ảnh hưởng phạm vi |
| **OQ-B4** | **Ba con số ở §2** | Mục `Analytics` của PRD cần dữ liệu | PO + Dev | No — trước khi viết PRD |
| **OQ-B5** | **Thông báo thành tích chấp nhận trễ tới mức nào?** | Trễ 30 phút thì mất tác dụng khích lệ | PO | No — Gate 2 |
| **OQ-B6** | **Hoàn thành khoá đã có mail #10 và #29.** Gộp hay tách kênh? | Tránh hai thông báo cho một sự kiện | PO | No — Gate 2 |
| **OQ-B7** | **Luồng chấm điểm đang tắt toàn bộ thông báo.** Có bật lại mail #19 không? | *Quyết định của luồng Grading, không thuộc gamification* | PO | No — nêu để biết |
| **OQ-B8** | **Chốt từ vựng.** "Point" đã là điểm đậu; "Level" đã là độ khó khoá và cấp bậc nhân sự | Tên đi vào cấu trúc dữ liệu và tài liệu bàn giao | PO | No — trước khi viết PRD |
| **OQ-B10** 🆕 | **Đồng hạng trong bảng xếp hạng xử lý thế nào?** Đề xuất: cùng điểm thì ai đạt sớm hơn xếp trên (§6.6). Nhưng nếu trùng cả thời điểm? | Hiển thị thứ hạng phải xác định, không được nhảy mỗi lần tải lại | PO | No — Field Intake |
| **OQ-B11** 🆕 | **Múi giờ tổ chức khai ở đâu trong đợt này?** Module Tenant chưa có. Đề xuất: một tham số cấp tổ chức, thiết kế để module Tenant sau tiếp quản | `C6`. Đóng cứng rồi gỡ sau thì đắt | PO + Dev | No — Gate 2 |

---

# 11. References

## Knowledge Base đã đọc

| File | Dùng cho |
|---|---|
| `07-learning-experience.md` | Logic hoàn thành Activity (`KB-LX-03a`, `KB-LX-03b`) — nền của §6.5. **Đã cập nhật trong đợt này** |
| `09-notification-email.md` | Cơ chế thông báo, `KB-NOTI-05`, trạng thái ẩn |
| `13-mail-events.md` | 30 mail tự động, mail #10/#29, `KB-MAIL-03` |
| `12-data-model.md` | Cấu trúc dữ liệu — nền của `C5`, `C6`, và phát hiện phòng ban chỉ gắn nhân sự |
| `14-api-surface.md` | `Group Management` (9 endpoint), `Department Management` (9 endpoint) |
| `15-product-direction.md` | Định hướng đa tenant — nền của `C1` |
| `01-course.md` · `03-assessment.md` · `04-class.md` · `08-certificate.md` | Nguồn sự kiện tính điểm · phạm vi xếp hạng theo lớp |

## Nguồn khác

| Nguồn | |
|---|---|
| Yêu cầu gốc | `working/raw-inputs/yeu-cau-goc-20260923.md` |
| Change request | `working/raw-inputs/change-requests.md` — **CR-001** |
| Bản làm rõ | `working/ai-drafts/clarified-requirements-20260923.md` |
| Open questions | `working/open-questions/open-questions-20260923.md` |
| Quyết định đã chốt | `project-decisions.md` |
| BRD bản trước | `docs/brd/brd-v0.1-20260923.md` |
| Schema DB | [Lark → Data Architecture](https://upbasevn.sg.larksuite.com/wiki/MaFpweI68iKNMvkTioLlJ1uJgQd) — đối chiếu 23/09/2026 |
| Swagger | `lms-be.staging.upbase.asia/api/v1/docs` · `ops-be.staging.upbase.asia/api/v1/docs` |
| Tham chiếu ngoài | `TNT.CFG.02` — Hồ sơ tổ chức và tham số, thuộc module Tenant *(chưa làm)* |
