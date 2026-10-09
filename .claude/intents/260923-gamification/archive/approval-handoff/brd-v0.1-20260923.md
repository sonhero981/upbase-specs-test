---
intent: 260923-gamification
artifact: brd
version: 0.1
status: superseded
migrated-from: .claude/projects/Gamification/docs/brd/brd-v0.1-20260923.md
---
# [BRD] Gamification — Cơ chế điểm, huy hiệu và hạng cho học viên

> **Bản nháp nội bộ để chốt hướng trước khi viết PRD.** Không phải tài liệu bàn giao.

| | |
| --- | --- |
| **Tính năng** | Gamification |
| **Người viết** | Bùi Đức Huy (PO) |
| **Ngày** | 23/09/2026 |
| **Trạng thái** | `Draft - Pending Confirmation` |
| **Cỡ yêu cầu** | **L** — đủ 9 bước, đủ 4 Gate |
| **Nguồn input** | `working/raw-inputs/yeu-cau-goc-20260923.md` · `working/ai-drafts/clarified-requirements-20260923.md` (v0.2) · `project-decisions.md` |

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

> ⚠️ **Chưa có dữ liệu định lượng.** Phần dưới là căn cứ định tính từ PO cộng với những gì quan sát được trong hệ thống. Xem `OQ-B4` — cần bổ sung trước khi viết mục `Analytics` của PRD.

## Vận hành đang xoay xở thế nào

| Hướng | Hiện trạng |
|---|---|
| **Cách làm hiện tại** | Vận hành theo dõi tiến độ học qua dashboard SIS (*Tiến độ học trên UpLMS* — một trong ba loại dashboard đang chạy), thấy ai chậm thì thúc. Hệ thống có 30 mail tự động nhưng đều là **mail sự kiện** — chào mừng, nhắc lịch kiểm tra, báo hết hạn khoá — không có mail nào nhằm tạo động lực |
| **Công cụ sẵn có bị hạn chế** | Giao diện soạn và gửi thông báo thủ công trên Ops **đang ẩn** (3/4 page của module Notification & Email). Đội truyền thông nội bộ muốn gửi một thông điệp khích lệ tới nhóm học viên cụ thể thì hiện không có đường tự phục vụ |
| **Tiêu chí quyết định** | Vận hành nhìn phần trăm tiến độ và thời hạn còn lại. Đây là hai con số **cho biết ai đang chậm, không cho biết ai đang cố gắng** — học viên đi đều mỗi ngày và học viên học dồn một buổi trông giống nhau khi đã cùng phần trăm |
| **Chỗ sai** | Việc thúc học phụ thuộc vào vận hành nhớ và làm thủ công. Không mở rộng được khi số lớp tăng, và **không tạo được thói quen** — học viên phản ứng với lời nhắc, không tự quay lại |

## Vì sao tin rằng cơ chế ghi nhận sẽ có tác dụng

`Assumption` — chưa được kiểm chứng bằng dữ liệu của chính sản phẩm:

Hệ thống đã có đủ dấu vết để ghi nhận nỗ lực (từng hoạt động hoàn thành, từng bài kiểm tra, từng chứng chỉ) nhưng **chưa dùng những dấu vết đó để phản hồi lại cho học viên**. Khoảng cách giữa "hệ thống biết bạn vừa làm gì" và "học viên cảm thấy việc đó được ghi nhận" là chỗ gamification lấp vào.

## Còn thiếu để mục này đủ chắc

Ba câu hỏi cụ thể, trả lời được bằng dữ liệu đã có trong hệ thống — xem `OQ-B4`:

1. Tỷ lệ học viên có tiến độ đứng yên quá 14 ngày liên tiếp là bao nhiêu?
2. Phân bố thời điểm học — bao nhiêu phần trăm hoạt động được hoàn thành trong 7 ngày cuối trước hạn?
3. Tỷ lệ khoá được hoàn thành so với số khoá được ghi danh?

---

# 3. Objective

| # | Kết quả muốn đạt |
|---|---|
| O1 | **Học viên quay lại học đều đặn hơn** mà không cần vận hành nhắc thủ công |
| O2 | **Nỗ lực học được ghi nhận ngay lúc nó xảy ra** — học viên biết việc mình vừa làm được hệ thống công nhận |
| O3 | **Học viên có mốc ngắn hạn để nhắm tới**, thay vì chỉ có đích cuối là hoàn thành khoá |
| O4 | **Đội truyền thông nội bộ tổ chức được chiến dịch học tập có thể đo được** — biết chiến dịch có tác dụng hay không |
| O5 | **Có nền dữ liệu cho bảng xếp hạng** ở đợt sau, không phải làm lại từ đầu |
| O6 | **Điểm số đáng tin** — mỗi con số đều truy được nguồn, và không bị thổi lên bằng thao tác đối phó |

> O6 không phải mục tiêu phụ. Một cơ chế điểm mà học viên không tin thì tệ hơn là không có cơ chế nào — nó biến việc học thành trò chơi hình thức.

---

# 4. Stakeholder

| Stakeholder | Action |
| --- | --- |
| **Học viên (UpLMS)** | Nhận điểm khi học · nhận huy hiệu · lên hạng · xem trang thành tích · tra lịch sử điểm |
| **Nhân sự vận hành (UpLMS Ops)** | Khai bảng điểm theo hành động · tạo huy hiệu và điều kiện đạt · đặt hạng và ngưỡng · tạo chiến dịch · bật/tắt cơ chế |
| **Đội truyền thông nội bộ** | Thiết kế và chạy chiến dịch thúc đẩy tinh thần học dựa trên cơ chế điểm theo kỳ |
| **Quản lý đào tạo / L&D** | Dùng dữ liệu điểm và hạng để đánh giá mức độ tham gia của học viên |
| Dev | Xác nhận phụ thuộc Keycloak (`OQ-B1`) và dấu thời gian dữ liệu tiến độ (`OQ-B2`) |
| QA | Điền `Conner case` ở PRD |

> **Đội truyền thông nội bộ là stakeholder mới lộ ra ở Bước 2**, không có trong yêu cầu gốc. Đây là nhóm sẽ dùng cơ chế chiến dịch nhiều nhất — nhưng phạm vi hiện tại **chưa có gì phục vụ riêng họ**. Xem `US15` và `OQ-B3`.

---

# 5. Scope

## In scope

| # | Nội dung |
|---|---|
| S1 | **Cơ chế điểm** — khai hành động nào được bao nhiêu điểm, bật/tắt từng hành động |
| S2 | **Bốn hành động tính điểm**: hoàn thành hoạt động · hoàn thành khoá · đạt bài kiểm tra · đạt điểm cao |
| S3 | **Hành động thứ năm**: đăng nhập nhiều ngày liên tiếp — nguồn dữ liệu Keycloak, tính từ ngày go-live |
| S4 | **Huy hiệu** — tên, hình, mô tả, điều kiện đạt |
| S5 | **Bốn loại điều kiện huy hiệu**: số lượng hoàn thành · chuỗi ngày liên tiếp · mốc thời gian · hoàn thành một nội dung cụ thể |
| S6 | **Hạng người học** — tên, hình, ngưỡng điểm từng hạng |
| S7 | **Hai loại điểm tách nhau**: điểm tích luỹ vĩnh viễn (xét hạng) và điểm theo kỳ/chiến dịch |
| S8 | **Quản lý chiến dịch** — tạo kỳ tính điểm; hết kỳ thì lưu lại kết quả, không xoá |
| S9 | **Chống cày điểm** — chống cộng trùng nội dung đã hoàn thành, trần điểm tối đa mỗi ngày |
| S10 | **Lịch sử điểm** — học viên tra được từng lần cộng đến từ đâu |
| S11 | **Thông báo thành tích** — khi nhận điểm, nhận huy hiệu, lên hạng |
| S12 | **Trang "Thành tích của tôi"** — điểm, hạng, huy hiệu đã có, huy hiệu sắp đạt kèm phần còn thiếu |
| S13 | **Bật/tắt gamification ở cấp tổ chức** |
| S14 | **Phân quyền cấu hình** — vai trò vận hành nào được sửa cấu hình gamification |

## Out of scope

| # | Không làm | Vì sao |
|---|---|---|
| N1 | **Bảng xếp hạng (leaderboard)** | PO chốt làm sau. Nhưng dữ liệu điểm theo kỳ **vẫn làm ở đợt này** để sau không phải dựng lại |
| N2 | **Tính năng Lộ trình học** và hành động tính điểm "hoàn thành lộ trình" | Lộ trình là nội dung học tương tự khoá học, chưa có trong hệ thống, là tính năng riêng |
| N3 | **Tính năng Khung năng lực / Skills** và điều kiện huy hiệu "đạt kỹ năng" | Thuộc tính năng riêng, làm sau |
| N4 | **Sửa logic hoàn thành Activity** của module Learning Experience | PO chốt giữ nguyên |
| N5 | **Tính bù điểm cho giai đoạn gamification bị tắt** | Cần phát lại theo từng ngày để áp đúng trần điểm — là bài toán riêng |
| N6 | **Phần thưởng vật chất** — đổi điểm lấy quà, voucher, ưu đãi | Yêu cầu gốc không nhắc |
| N7 | **Gamification cho nhân sự Ops** | Chỉ áp dụng cho học viên |
| N8 | **Thi đua theo đội / nhóm / phòng ban** | Yêu cầu gốc chỉ nói cá nhân |
| N9 | **Cấu hình gamification riêng theo từng lớp hoặc từng khoá** | Cấu hình ở cấp tổ chức |
| N10 | **Màn quản lý nhiều tổ chức** | PO chốt chỉ làm bật/tắt cho hệ thống hiện tại. *Nhưng dữ liệu vẫn thiết kế theo tổ chức — xem C1* |
| N11 | **Trang theo dõi hiệu quả chiến dịch cho đội truyền thông** | Chưa có trong yêu cầu — xem `OQ-B3` |

## Potential scope

Bảng xếp hạng · thi đua theo phòng ban · tính bù điểm · trang hiệu quả chiến dịch · gamification cho UpAcademy · đổi điểm lấy phần thưởng

---

# 6. Solution (khung)

## 6.1 Hướng tổng thể

Cơ chế gồm **bốn lớp**, xếp theo thứ tự phụ thuộc:

```
Lớp 1  Bắt sự kiện học tập      ← nghe các việc học viên đã làm
Lớp 2  Quy đổi ra điểm          ← áp bảng cấu hình + luật chống cày
Lớp 3  Tích luỹ và xét ngưỡng   ← cộng dồn, xét huy hiệu, xét hạng
Lớp 4  Phản hồi cho học viên    ← thông báo + trang thành tích + lịch sử
```

Nguyên tắc xuyên suốt: **gamification chỉ đọc, không sửa dữ liệu học tập.** Nó nghe việc đã xảy ra và ghi ra bản ghi điểm của riêng nó. Không đụng vào tiến độ học, điểm bài kiểm tra, hay trạng thái hoàn thành — những thứ đó do các module hiện có làm chủ.

Đây là điều kiện để N4 (không sửa logic hoàn thành Activity) giữ được, và để bật/tắt gamification không ảnh hưởng gì tới việc học.

## 6.2 Ràng buộc thiết kế bắt buộc

| # | Ràng buộc | Vì sao |
|---|---|---|
| **C1** | Cấu hình gắn với **tổ chức**, không đóng cứng | Định hướng đa tenant của sản phẩm. Hiện chỉ một tổ chức dùng nên chi phí bằng 0; đóng cứng rồi gỡ sau thì đắt |
| **C2** | **Danh mục hành động tính điểm và danh mục điều kiện huy hiệu phải mở rộng được bằng cấu hình**, không đóng cứng danh sách trong code | Lộ trình (N2), kỹ năng (N3) và leaderboard (N1) đều sẽ thêm sau. Đóng cứng thì mỗi lần thêm một loại phải sửa cấu trúc dữ liệu và triển khai lại |
| **C3** | Lưu **từng lần cộng điểm**, không chỉ lưu tổng | Yêu cầu gốc: *"Điểm không giải thích được thì không ai tin bảng xếp hạng"*. Không có sổ chi tiết thì không có lịch sử điểm (S10), và không kiểm được luật chống cày |
| **C4** | Đổi cấu hình điểm → **áp dụng từ thời điểm đổi**, không tính lại quá khứ | PO chốt. Tính lại quá khứ khiến điểm học viên nhảy mỗi lần vận hành chỉnh cấu hình |
| **C5** | Chống cộng trùng "đã học" tính theo **người học**, không theo lượt ghi danh lớp | Một học viên có thể học cùng một nội dung qua nhiều lớp. Chống cộng trùng theo lượt ghi danh sẽ cộng điểm nhiều lần cho cùng một nội dung — đúng kịch bản cày điểm mà S9 muốn chặn |

> **C5 là ràng buộc dễ bỏ sót nhất.** Toàn bộ dữ liệu tiến độ học của hệ thống hiện gắn với *lượt ghi danh vào lớp* chứ không gắn với *người*. Chi tiết kỹ thuật ở `clarified-requirements-20260923.md` §6.

## 6.3 Quyết định 1 — "Tắt gamification" nghĩa là gì

> Đây là quyết định của Gate 1. Phân tích đầy đủ ở `clarified-requirements-20260923.md` §13.

Không phải chọn một trong ba phương án, mà là **hai công tắc khác bản chất**: *có tiếp tục ghi nhận không* và *hiển thị cho ai*.

| Hướng | Nội dung | Đánh đổi |
|---|---|---|
| **A. Một công tắc — tắt là dừng hẳn** | Tắt thì không ghi nhận, không hiển thị | Đơn giản nhất. Nhưng không có cách chạy thử: số điểm đặt lần đầu sai thì học viên là người phát hiện ra |
| **B. Một công tắc — tắt chỉ ẩn hiển thị** | Vẫn ghi nhận ngầm, chỉ ẩn khỏi học viên | Bật lại là có sẵn dữ liệu. Nhưng tổ chức không dùng cơ chế này vẫn phải chịu toàn bộ chi phí tính toán và lưu trữ — không có trạng thái "tắt thật" |
| **C. Hai công tắc** ⭐ | `Ghi nhận` + `Hiển thị cho học viên` → ba trạng thái: *Tắt hẳn* · *Chạy ngầm* · *Bật đầy đủ* | Thêm một cờ cấu hình và một luật bắt buộc (không bắn thông báo hồi tố khi chuyển sang bật). Đổi lại có được giai đoạn chạy thử |

`Recommendation` — **hướng C**, vì hai lý do:

1. **Số điểm cho mỗi hành động gần như chắc chắn sai ở lần đặt đầu tiên.** Không có cách nào biết trước 10 điểm cho một hoạt động là quá dễ hay quá khó — phải nhìn phân bố thật mới biết. Mà một khi học viên đã thấy điểm và hạng của mình, chỉnh xuống là lấy đi thứ họ đã có. Kể cả với C4 (chỉ áp dụng từ lúc đổi), họ vẫn thấy tốc độ lên hạng chậm lại và sẽ hỏi.
2. **Đội truyền thông nội bộ cần số liệu thật để thiết kế chiến dịch đầu tiên** (O4), thay vì đoán ngưỡng rồi sửa giữa chiến dịch.

Chi phí của công tắc thứ hai gần bằng 0. Giá trị là **không phải sửa cơ chế trước mặt học viên**.

**Phải chấp nhận nếu chọn C:** một luật bắt buộc — khi chuyển từ *Chạy ngầm* sang *Bật đầy đủ*, **không bắn thông báo hồi tố**. Nếu không, mỗi học viên nhận hàng trăm thông báo cùng lúc. Lịch sử điểm vẫn hiển thị đầy đủ để tra nguồn (C3).

**Và một điều phải ghi rõ trong PRD dù chọn hướng nào:** bật lại sau khi tắt hẳn thì **tính từ thời điểm bật**, không tính bù (N5).

## 6.4 Quyết định 2 — Chống cày điểm với hoạt động dạng Text/Ảnh

> Phân tích ở `clarified-requirements-20260923.md` §14.2.

Bối cảnh: sau khi PO chốt giữ nguyên logic hoàn thành (N4), hoạt động chứa **Video** nay đã chặt (xem ≥80% thời lượng — `KB-LX-03a`), nhưng hoạt động chứa **Text/Ảnh** vẫn được tính hoàn thành **ngay khi mở hiển thị** (`KB-LX-03b`).

Nghĩa là trong ba cơ chế chống cày ở S9, cơ chế *"không cộng điểm cho hoạt động bỏ qua quá nhanh"* **không áp dụng được** cho loại nội dung này — trừ khi đo thời gian, mà đo thời gian chính là sửa logic hoàn thành.

| Hướng | Nội dung | Đánh đổi |
|---|---|---|
| **A. Chấp nhận, dựa vào hai cơ chế còn lại** ⭐ | Trần điểm/ngày + chống cộng trùng nội dung đã học. Thêm: **cho phép khai số điểm khác nhau theo loại hoạt động** | Không thêm cơ chế nào mới. Học viên bấm lướt vẫn được điểm, nhưng mỗi nội dung chỉ trả điểm **một lần duy nhất trong đời** và tổng mỗi ngày bị chặn trần |
| **B. Gamification tự đo thời gian riêng** | Đo thời gian ở hoạt động chỉ để quyết định cộng điểm, không đụng trạng thái hoàn thành | Chính xác hơn. Nhưng tạo ra tình huống học viên thấy hoạt động ✅ hoàn thành mà không được điểm, **không hiểu vì sao** — và không có chỗ nào giải thích |
| **C. Không cộng điểm cho hoạt động dạng Text/Ảnh** | Chỉ cộng cho Quiz, Video, và các mốc lớn | Đơn giản và an toàn. Nhưng mất phần lớn cơ hội cộng điểm thường xuyên — mà chính những lần cộng nhỏ đều đặn mới tạo thói quen (O1, O3) |

`Recommendation` — **hướng A**, vì:

- Chống cộng trùng (C5) đã chặn được phần lớn thiệt hại: **mỗi nội dung chỉ trả điểm một lần**. Học viên bấm lướt qua một khoá chỉ lấy được đúng số điểm của khoá đó, không lặp lại được
- Trần điểm/ngày chặn được việc một người dồn toàn bộ trong một buổi để vượt lên trong chiến dịch
- Phần còn lại giải quyết được **bằng cấu hình chứ không cần cơ chế mới**: hệ thống đã phân biệt ba loại hoạt động (Learning Activity / Test Activity / Case Study Activity), nên có thể khai hoạt động dạng đọc ít điểm hơn hoạt động có bài kiểm tra
- Hướng B tạo ra một mâu thuẫn hiển thị không giải thích được cho học viên — đúng loại vấn đề mà O6 (điểm đáng tin) muốn tránh

---

# 7. Danh sách User Story dự kiến

> Đánh số liên tục `US1`, `US2`… US chưa làm trong đợt này vẫn được định nghĩa đủ, ghi rõ trong tiêu đề.

## Phía học viên (UpLMS)

| ID | User Story | Nguồn | Ghi chú |
| --- | --- | --- | --- |
| **US1** | Là học viên, tôi cần xem điểm, hạng và các huy hiệu đã đạt của mình để biết nỗ lực học của mình đang được ghi nhận tới đâu | Yêu cầu gốc dòng 10 · O2 | Trang "Thành tích của tôi" |
| **US2** | Là học viên, tôi cần được báo ngay khi nhận điểm, đạt huy hiệu hoặc lên hạng để cảm nhận được sự ghi nhận đúng lúc nó xảy ra | Yêu cầu gốc dòng 9 · O2 | Phụ thuộc `OQ-B5` về độ trễ chấp nhận được |
| **US3** | Là học viên, tôi cần tra được từng lần cộng điểm đến từ đâu để tin vào con số của mình | Yêu cầu gốc dòng 8 · O6 · C3 | |
| **US4** | Là học viên, tôi cần biết huy hiệu nào mình sắp đạt và còn thiếu gì để có mục tiêu ngắn hạn để nhắm tới | Yêu cầu gốc dòng 10 · O3 | Tách khỏi US1 vì cần tính tiến độ tới **mọi** huy hiệu chưa đạt |
| **US5** | Là học viên, tôi cần việc quay lại học đều đặn mỗi ngày được ghi nhận thành chuỗi ngày liên tiếp để có lý do duy trì thói quen | Yêu cầu gốc dòng 2, 4 · O1 | ⚠️ Phụ thuộc Keycloak — `OQ-B1` |

## Phía vận hành (UpLMS Ops)

| ID | User Story | Nguồn | Ghi chú |
| --- | --- | --- | --- |
| **US6** | Là nhân sự vận hành, tôi cần khai hành động nào được bao nhiêu điểm và bật/tắt từng hành động để điều chỉnh cơ chế theo mục tiêu từng giai đoạn | Yêu cầu gốc dòng 1, 2 | Chịu ràng buộc C2 (mở rộng bằng cấu hình) và C4 (không hồi tố) |
| **US7** | Là nhân sự vận hành, tôi cần tạo và quản lý huy hiệu cùng điều kiện đạt để thiết kế các mốc mục tiêu cho học viên | Yêu cầu gốc dòng 3, 4 | 4 loại điều kiện (S5) |
| **US8** | Là nhân sự vận hành, tôi cần đặt các hạng và ngưỡng điểm để phân tầng mức độ tham gia của học viên | Yêu cầu gốc dòng 5 | |
| **US9** | Là nhân sự vận hành, tôi cần tạo và quản lý chiến dịch để chạy các đợt thi đua có thời hạn | Yêu cầu gốc dòng 6 · O4, O5 | Hết kỳ **lưu lại kết quả**, không xoá |
| **US10** | Là nhân sự vận hành, tôi cần điểm phản ánh việc học thật, không bị đẩy lên bằng thao tác đối phó, để cơ chế còn đáng tin | Yêu cầu gốc dòng 7 · O6 | Chịu ràng buộc C5. Chờ quyết định §6.4 |
| **US11** | Là nhân sự vận hành, tôi cần bật/tắt gamification cho tổ chức để kiểm soát việc cơ chế có chạy và có hiện với học viên hay không | Yêu cầu gốc dòng 11 | Chờ quyết định §6.3 |
| **US12** | Là quản trị, tôi cần phân quyền để chỉ vai trò vận hành phù hợp mới sửa được cấu hình gamification | `[suy ra]` · S14 | Cấu hình sai ảnh hưởng toàn bộ học viên |

## Chưa làm trong đợt này

| ID | User Story | Nguồn | Ghi chú |
| --- | --- | --- | --- |
| **US13** | *Bảng xếp hạng* — Là học viên, tôi cần thấy vị trí của mình so với người khác trong chiến dịch để có động lực thi đua — **chưa làm** | `OQ-01` | Dữ liệu điểm theo kỳ (US9) **đã làm ở đợt này** để sau chỉ cần dựng phần hiển thị |
| **US14** | *Điểm cho lộ trình* — Là học viên, tôi cần được cộng điểm khi hoàn thành một lộ trình học — **chưa làm** | `OQ-02` | Chờ tính năng Lộ trình. Nhờ C2 nên chỉ cần thêm cấu hình |
| **US15** | *Huy hiệu theo kỹ năng* — Là học viên, tôi cần nhận huy hiệu khi đạt được một kỹ năng cụ thể — **chưa làm** | `OQ-06` | Chờ tính năng Khung năng lực. Nhờ C2 nên chỉ cần thêm cấu hình |
| **US16** | *Hiệu quả chiến dịch* — Là đội truyền thông nội bộ, tôi cần theo dõi chiến dịch có làm tăng mức độ tham gia hay không để quyết định lần sau làm gì — **chưa làm** | `[suy ra]` từ O4 | ⚠️ **Khoảng trống thật** — xem `OQ-B3` |
| **US17** | *Tính bù điểm* — Là nhân sự vận hành, tôi cần tính bù điểm cho giai đoạn gamification bị tắt để học viên không thiệt — **chưa làm** | N5 · §6.3 | Phải phát lại theo từng ngày để áp đúng trần điểm |

> **US16 là khoảng trống đáng chú ý.** O4 nói mục tiêu là để đội truyền thông chạy chiến dịch đo được, và họ là stakeholder chính thức — nhưng phạm vi hiện tại không có gì phục vụ riêng họ. Họ tạo được chiến dịch (US9) nhưng không có chỗ nào xem chiến dịch có tác dụng không.

---

# 8. Tác động tới hệ thống hiện tại

> **Chưa chạy Impact Analysis.** Dưới đây là đánh giá sơ bộ từ KB, DB schema và Swagger ở Bước 2. **Chi tiết và đầy đủ sẽ có ở Gate 2** — không dùng bảng này thay cho Impact Matrix.

| Vùng ảnh hưởng | Mức | Ghi chú |
| --- | --- | --- |
| **Dữ liệu** | 🔴 Cao | Toàn bộ cấu trúc lưu điểm, huy hiệu, hạng, chiến dịch, sổ giao dịch điểm là mới. Chịu C1, C2, C3, C5 |
| **Learning Experience** | 🟠 Vừa | Nguồn sự kiện chính. Chỉ đọc, không sửa (§6.1). Nhưng `KB-LX-03b` chi phối §6.4 |
| **Notification** | 🟠 Vừa | US2 cần thông báo theo sự kiện cho từng người. Cơ chế hiện có là **soạn tay gửi theo nhóm**, gửi theo job nửa tiếng (`KB-NOTI-05`). Phần hộp thư và push phía học viên tái dùng được. 3/4 page module này **đang ẩn** |
| **Assessment / Grading** | 🟠 Vừa | Nguồn sự kiện cho "đạt bài kiểm tra" và "đạt điểm cao". ⚠️ 8 mail của luồng chấm điểm **đang tắt** (`KB-MAIL-03`) — học viên sẽ biết mình được điểm thưởng trước khi biết bài đã chấm |
| **Course / Certificate** | 🟡 Thấp | Nguồn sự kiện "hoàn thành khoá". Đã có mail #10 và #29 đang chạy cho cùng sự kiện — cần tránh trùng thông báo |
| **User / Auth** | 🟠 Vừa | US5 phụ thuộc sự kiện đăng nhập từ Keycloak — phụ thuộc ngoài, chưa xác nhận (`OQ-B1`) |
| **Class** | 🟡 Thấp | Không sửa, nhưng cấu trúc lớp là lý do sinh ra C5 |
| **Phân quyền** | 🟡 Thấp | Thêm nhóm quyền mới cho cấu hình gamification |
| **Hiệu năng** | ❓ Chưa rõ | Mỗi hoạt động hoàn thành sinh một lần xử lý điểm. Chưa ước lượng được tải — để Gate 2 |

---

# 9. Assumptions

| # | Giả định | Kiểm chứng thế nào |
|---|---|---|
| A1 | Gamification chỉ áp dụng cho **học viên UpLMS**, không cho nhân sự Ops | PO xác nhận |
| A2 | Cấu hình đặt ở **UpLMS Ops**, không phải màn riêng | PO xác nhận |
| A3 | **Hạng chỉ lên, không tụt** — vì điểm tích luỹ là vĩnh viễn | PO xác nhận |
| A4 | Điểm tích luỹ **không hết hạn** | PO xác nhận |
| A5 | Huy hiệu **đạt rồi giữ vĩnh viễn**, không thu hồi | PO xác nhận |
| A6 | Một hành động có thể đồng thời cộng vào **cả điểm tích luỹ và điểm theo kỳ** | PO xác nhận |
| A7 | Điểm là **số nguyên** | PO xác nhận |
| A8 | **Các chiến dịch không chồng lấn thời gian** — tại một thời điểm chỉ có tối đa một kỳ đang chạy | PO xác nhận. Nếu chồng lấn được thì US9 phức tạp hơn hẳn |
| A9 | Ảnh huy hiệu và ảnh hạng dùng hạ tầng quản lý tài nguyên sẵn có | Kiểm ở Gate 2 |
| A10 | **Dữ liệu tiến độ học có dấu thời gian** — cần cho chống cộng trùng theo thời gian và cho khả năng tính bù | Dev xác nhận — `OQ-B2` |
| A11 | **Keycloak có ghi và giữ được sự kiện đăng nhập** | Dev xác nhận — `OQ-B1` |
| A12 | Vận hành **không cần sửa hay xoá điểm thủ công** của một học viên cụ thể | PO xác nhận. Nếu cần thì là một US nữa |

---

# 10. Open Questions

| # | Câu hỏi | Vì sao quan trọng | Người trả lời | Chặn bước sau? |
| --- | --- | --- | --- | --- |
| **OQ-A1** | **Chọn hướng nào cho "tắt gamification"?** A (một công tắc, dừng hẳn) · B (một công tắc, ẩn hiển thị) · C (hai công tắc) — xem §6.3 | Quyết định cấu trúc cấu hình và luật thông báo. Đổi sau khi đã triển khai thì phải sửa dữ liệu | PO | **Yes** — chốt tại Gate 1 |
| **OQ-A2** | **Chọn hướng nào cho chống cày với hoạt động Text/Ảnh?** A (trần + chống cộng trùng + phân biệt điểm theo loại) · B (tự đo thời gian) · C (không cộng điểm) — xem §6.4 | Ảnh hưởng tới cấu trúc cấu hình điểm và trải nghiệm học viên | PO | **Yes** — chốt tại Gate 1 |
| **OQ-B1** | **Keycloak có bật ghi sự kiện đăng nhập không, giữ được bao lâu, lấy ra bằng cách nào?** Keycloak mặc định **tắt** event logging và có hạn lưu riêng | Nếu không có thì US5 và điều kiện huy hiệu "chuỗi ngày liên tiếp" không làm được — phải bỏ hoặc tự ghi log riêng | Dev | **Yes** — trước Gate 2 |
| **OQ-B2** | **Dữ liệu tiến độ học có dấu thời gian không?** | Cần cho chống cộng trùng theo thời gian (C5), cho trần điểm/ngày, và cho khả năng tính bù sau này | Dev | **Yes** — trước Gate 2 |
| **OQ-B3** | **Đội truyền thông nội bộ cần gì để biết chiến dịch có tác dụng?** Hiện họ tạo được chiến dịch nhưng không có chỗ xem kết quả (US16) | O4 là một trong sáu mục tiêu. Không có gì phục vụ thì mục tiêu này không đạt được, dù mọi US khác đều xong | PO | No — nhưng ảnh hưởng phạm vi |
| **OQ-B4** | **Ba con số ở §2** — tỷ lệ học viên đứng yên >14 ngày · phân bố thời điểm học · tỷ lệ hoàn thành khoá | Mục `Analytics` của PRD cần dữ liệu. Ba con số này lấy được từ hệ thống hiện tại | PO + Dev | No — trước khi viết PRD |
| **OQ-B5** | **Thông báo thành tích chấp nhận trễ tới mức nào?** Cơ chế hiện tại gửi theo job nửa tiếng | Trễ 30 phút thì mất phần lớn tác dụng khích lệ của US2 | PO | No — Gate 2 |
| **OQ-B6** | **Hoàn thành khoá đã có mail #10 và #29 đang chạy.** Gộp thông tin điểm vào mail sẵn có hay tách kênh riêng? | Tránh gửi hai thông báo cho cùng một sự kiện | PO | No — Gate 2 |
| **OQ-B7** | **Luồng chấm điểm đang tắt toàn bộ thông báo** (8 mail, gồm mail báo học viên bài đã chấm xong). Có bật lại không? | Học viên sẽ nhận "+N điểm" trước khi biết bài đã chấm. *Đây là quyết định của luồng Grading, không thuộc gamification* | PO | No — nêu để biết |
| **OQ-B8** | **Chốt từ vựng.** "Point" đã là điểm đậu và điểm bài kiểm tra; "Level" đã là độ khó khoá học và cấp bậc nhân sự | Tên đi vào cấu trúc dữ liệu, giao diện và tài liệu bàn giao. Đổi sau khi đã triển khai thì đắt | PO | No — trước khi viết PRD |

---

# 11. References

## Knowledge Base đã đọc

| File | Dùng cho |
|---|---|
| `07-learning-experience.md` | Logic hoàn thành Activity (`KB-LX-03a`, `KB-LX-03b`) — nền của §6.4. **Đã cập nhật trong đợt này** |
| `09-notification-email.md` | Cơ chế thông báo, `KB-NOTI-05`, trạng thái ẩn của module |
| `13-mail-events.md` | 30 mail tự động, mail #10/#29, `KB-MAIL-03` (8 mail chấm điểm đang tắt) |
| `12-data-model.md` | Cấu trúc dữ liệu hiện tại — nền của C5 |
| `14-api-surface.md` | Kiểm vùng KB chưa phủ trước khi kết luận |
| `15-product-direction.md` | Định hướng đa tenant — nền của C1 |
| `01-course.md` · `03-assessment.md` · `08-certificate.md` | Nguồn sự kiện tính điểm |

## Nguồn khác

| Nguồn | |
|---|---|
| Yêu cầu gốc | `working/raw-inputs/yeu-cau-goc-20260923.md` |
| Bản làm rõ | `working/ai-drafts/clarified-requirements-20260923.md` (v0.2) |
| Open questions | `working/open-questions/open-questions-20260923.md` |
| Quyết định đã chốt | `project-decisions.md` |
| Schema DB | [Lark → Data Architecture](https://upbasevn.sg.larksuite.com/wiki/MaFpweI68iKNMvkTioLlJ1uJgQd) — đối chiếu 23/09/2026 |
| Swagger | `lms-be.staging.upbase.asia/api/v1/docs` · `ops-be.staging.upbase.asia/api/v1/docs` |
| Jira | *(chưa có)* |
| Figma | *(chưa có)* |
