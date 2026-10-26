---
intent: 261005-group
artifact: brd
version: 0.6
status: draft
cr: CR8 ngày 2026-10-26, báo cáo theo nhóm đợt này chỉ ở hiện tại, mốc quá khứ để sau; CR7 ngày 2026-10-25, thông báo theo nhóm vào In scope, bỏ phòng ban và đơn vị kinh doanh của nhân sự, đồng bộ theo sự kiện kèm chạy toàn bộ mỗi đêm, chữ giao diện tiếng Anh; CR6 ngày 2026-10-21
approved: 2026-10-12 (v0.3); 2026-10-06 (v0.2)
review: lần 01 NOT-READY, Request Changes (DEC78); lần 02 READY, Approve (DEC79), ngày 2026-10-12
gate: v1 Gate 1 ngày 2026-10-05, cập nhật v0.2 sau Gate 2 và Bước 7
migrated-from: pre-aidlc:.claude/projects/Group/docs/brd/brd-v0.2-20261006.md
note: Artifact phase Ideation theo luồng v1. Thay cho intent-statement, scope-document và initiative-brief của v2
approved_at: 2026-10-25T14:24
---
# [BRD] Group — Nhóm học viên

| | |
| --- | --- |
| **Tính năng** | Group |
| **Người viết** | Bùi Đức Huy (PO) |
| **Version** | **v0.6** — 26/10/2026, CR8 |
| **Trạng thái** | `Draft` — v0.6 chờ duyệt lại sau CR8. v0.5 duyệt 25/10/2026. v0.4 duyệt 22/10/2026; v0.3 duyệt 12/10/2026 sau review AI Reviewer; v0.2 qua Gate 1 *(05/10)*, Gate 2 *(06/10)*, Bước 7 *(06/10)* |

> Bản nháp nội bộ để chốt hướng trước khi viết PRD.

## Lịch sử thay đổi

| Version | Ngày | Nội dung |
|---|---|---|
| `v0.1` | 05/10/2026 | Bản đầu, 19 US. ⚠️ **Không được lưu lại** — xem ghi chú dưới |
| `v0.2` | 06/10/2026 | Gộp toàn bộ quyết định từ Gate 1, Bước 5, Gate 2 và Bước 7 |
| `v0.3` | 12/10/2026 | Cập nhật theo CR1 *(09/10)* và review AI Reviewer lần 01. Không đổi phạm vi |
| `v0.4` | 21/10/2026 | CR6: bỏ giới hạn số cấp nhóm; một người được đồng thời là quản lý, mentor và thành viên bằng một tài khoản học viên; báo cáo theo nhóm đặt ở chi tiết nhóm, báo cáo trên dashboard để sau |
| `v0.5` | 25/10/2026 | CR7, sau khi Design PIC và Tech PIC nộp file thiết kế: thông báo Ops chọn người nhận theo nhóm chuyển từ Potential scope vào In scope, thành `US21`; bỏ phòng ban và đơn vị kinh doanh của nhân sự vận hành; đồng bộ cơ cấu theo sự kiện kèm một lần chạy toàn bộ mỗi đêm; chữ giao diện bằng tiếng Anh *(`DEC116` đến `DEC118`)* |
| **`v0.6`** | 26/10/2026 | CR8: đợt này báo cáo theo nhóm chỉ ở thời điểm hiện tại; báo cáo tại một mốc quá khứ chuyển sang Potential scope *(`DEC135`)* |

**Đổi gì ở `v0.2`:**

| Vùng | Thay đổi |
|---|---|
| Số US | 19 → **20**. Thêm `US18` *(báo cáo cộng dồn — `O4` trước đó không có US nào)*. `US19` đổi từ *nhóm động* thành *rời nhóm chưa học*. `US20` đổi từ *chưa làm* thành *phải làm* |
| §5 Scope | Thêm *thành viên theo thời gian* · *báo cáo theo nhóm* · *vòng đời nhân sự*. Chuyển **nhóm động** sang Out of scope. Thêm **chức năng chuyển lớp** vào Out of scope |
| §6 Solution | Thêm 5 mục: *vòng đời nhóm* · *lịch sử thành viên* · *báo cáo đọc qua lớp nào* · *ba trường hợp rời nhóm* · *người thuộc nhóm nào khi đồng bộ* |
| §10 | 13 Open Question đóng. Không còn câu nào chặn PRD |
| Việc mới | **`MAIL-GRP-01`** — một mail event mới phải làm. 30 mail hiện có không có cái nào cho việc này |
| Bị thay thế | `BA-06` *(giữ người nghỉ việc trong nhóm)* → `CF-4` *(gỡ khỏi nhóm, đánh dấu lượt ghi danh)* |

**Đổi gì ở `v0.3`:**

| Vùng | Thay đổi |
|---|---|
| §1 | Thêm mục **Product boundary**: portal, tenant, tầng, hằng số, chỗ đóng cứng chạm tới |
| Mentor | §4, §5, `US12` viết lại theo `CF-6` *(06/10)*: mentor của nhóm chính là mentor của lớp. Bản v0.2 còn giữ khung ban đầu *"loại quan hệ thứ hai, dùng chung cơ chế"* |
| `US16` | Chuyển sang **UpLMS Ops** theo `DEC73` *(09/10)*. Bản v0.2 xếp nhầm vào UpLMS |
| Mail | Thêm **`MAIL-GRP-02`** theo `DEC74` *(09/10)*; `MAIL-GRP-01` thêm câu cảnh báo mất tiến độ theo `DEC75` |
| §8, §10, §11 | Đường dẫn chuyển sang cấu trúc intent; §8 trỏ sang Impact Matrix đã có; §10 thêm bảng Gate 2 và CR1 |
| Ký hiệu | `❓BA` đổi thành `❓PO` theo GLOSSARY |

> ⚠️ **`v0.1` không được lưu lại.** Bản đó bị sửa đè nhiều lần trong ngày 05–06/10 thay vì tạo version mới, và chưa từng được commit, nên không mở lại được nội dung đúng lúc Gate 1 duyệt.
>
> Truy vết **vẫn còn** ở `decisions.md` *(bản v1: `archive/v1/project-decisions.md`)* — mọi quyết định ghi kèm ngày và gate. Thứ mất là bản chụp toàn văn, không phải lý do.

---

# 1. Problem

Hệ thống không có cách gom học viên thành một tập hợp ổn định để gán nội dung và theo dõi. Mọi thứ hiện phải làm qua **Lớp**, mà Lớp gắn với đúng một khoá học và có thời hạn, nên nó không thay thế được.

Ba nhóm người gặp vấn đề, theo ba cách khác nhau.

**L&D khi giao bài học.** Muốn giao một khoá cho toàn bộ phòng Fulfillment HCM thì phải chọn tay 55 người, hoặc nhập một file danh sách. Làm xong, tuần sau có người mới vào phòng thì không ai nhớ phải gán bổ sung, trừ khi có người rà lại bằng tay.

**Quản lý trực tiếp khi theo dõi.** Không có cách nào xem tiến độ học của riêng những người mình phụ trách. Hệ thống không biết ai quản lý ai, nên cũng không lọc được.

**Vận hành khi làm báo cáo.** Không cộng dồn được số liệu theo phòng ban hay theo khối, vì không có cấu trúc nào để cộng theo.

Hệ quả đã thấy ở tính năng khác: dự án Gamification phải hoãn `US16` *(bộ lọc bảng xếp hạng theo nhóm)*, và ghi nhận trong tài liệu rằng **quản lý trực tiếp chưa có công cụ riêng** — cả hai đều chờ đúng chức năng này.

## Product boundary

| | |
|---|---|
| **Portal** | Cả hai. Phần lớn việc ở **UpLMS Ops**: dựng nhóm, thành viên, đồng bộ HRM, gán nội dung, quản lý, nhật ký, lưu trữ, báo cáo — `US1` đến `US16`, `US18` đến `US20`. **UpLMS** chỉ có `US17`, học viên xem quản lý của mình. Màn theo dõi nhánh `US16` nằm ở **UpLMS Ops** *(`DEC73`)*. Quản lý và mentor là tài khoản học viên của chính người đó: được gán vai nào thì đăng nhập UpLMS Ops để dùng đúng màn của vai đó *(21/10/2026, `DEC101`)*. `US21` chọn nhóm làm người nhận thông báo cũng ở UpLMS Ops *(`DEC116`)*. Màn theo dõi của quản lý và khối quản lý của học viên có bản điện thoại *(`DEC120`)* |
| **Ngôn ngữ giao diện** | Tiếng Anh, như UpLMS Ops và UpLMS hiện có *(25/10/2026, `DEC118`)* |
| **UpBase hay mọi tenant** | Làm cho UpBase, nhưng dữ liệu và hạ tầng cho **mọi tenant**. Nhóm, quan hệ thành viên, quan hệ quản lý và mentor đều thuộc về một tổ chức; mô hình không mang giả định riêng của UpBase. Đã kiểm chiều tenant ở Impact Matrix §9 |
| **Tầng** | Tầng **LMS đang có**, mở rộng từ Lớp và User. Không thuộc tầng năng lực định hướng |
| **Hằng số** | Không giới hạn số cấp của cây nhóm *(21/10/2026, `DEC100`)*. Độ dài tên nhóm 255 và mô tả 1000 ký tự là giới hạn field, cố định *(`F-11`)* |
| **Chỗ đóng cứng UpBase chạm tới** | Nguồn cơ cấu là **Lark**, qua cơ chế đồng bộ HRIS một chiều đang có — KB `15-product-direction.md` §6 xếp đây là chỗ đóng cứng mức cao, vì mỗi tenant một HRIS. Dự án này **mở rộng** cơ chế đó sang tầng cơ cấu, không gỡ nó. Nhóm tự tạo không phụ thuộc Lark |

---

# 2. Analytics

## Dữ liệu cơ cấu hiện có

Xuất từ Lark ngày 05/10/2026, file `inputs/lark-users-by-department.csv`:

| | Số |
|---|---|
| Nhân sự trong cây tổ chức | 384 |
| Phòng ban riêng biệt | 53 |
| Khối ở cấp 1 | 5 — `ECOM` · `VẬN HÀNH` · `Tech` · `CHUYỂN ĐỔI SỐ` · `BOD` |
| Độ sâu cây | 4 cấp |

Phân bố nhân sự theo độ sâu phòng ban:

| Cấp | Phòng ban | Người |
|---|---|---|
| 1 | 2 | 6 |
| 2 | 22 | 203 |
| 3 | 27 | 166 |
| 4 | 2 | 9 |

Phòng ban đông nhất có **55 người** (`ECOM / Fulfillment HCM`). Hơn một nửa nhân sự nằm ở cấp 2.

**Cơ cấu này đã tồn tại đầy đủ trên Lark, nhưng UpLnD không có nó.** Hệ thống hiện chỉ đồng bộ được danh sách người, không đồng bộ cơ cấu.

## Cách vận hành đang xoay xở

❓`PO` — chưa khảo sát trực tiếp. Phần dưới là suy luận từ những gì hệ thống hiện có, cần PO xác nhận hoặc bổ sung số liệu thật:

| Hướng | Hiện trạng suy ra |
|---|---|
| **Cách làm hiện tại** | Tạo Lớp rồi thêm học viên, chọn tay hoặc nhập file danh sách |
| **Tiêu chí quyết định** | Dựa vào danh sách phòng ban giữ ngoài hệ thống, có thể là file Excel hoặc tra trên Lark |
| **Chi phí** | Mỗi lần giao một khoá cho một phòng ban là một lần lập danh sách. Phòng 55 người thì thao tác tương ứng |
| **Chỗ sai** | Người mới vào phòng sau khi đã giao bài thì bị bỏ sót. Người chuyển phòng vẫn còn trong lớp cũ |

> Con số đáng bổ sung nếu có: một tháng vận hành giao bài bao nhiêu lần, mỗi lần mất bao lâu, đã từng sót người chưa và hậu quả thế nào.

---

# 3. Objective

| # | Kết quả muốn đạt |
|---|---|
| `O1` | Giao nội dung cho một tập người ổn định, không phải lập danh sách lại mỗi lần |
| `O2` | Người mới vào tập đó **tự nhận** nội dung đã giao, không cần ai nhớ gán bổ sung |
| `O3` | Quản lý xem được tiến độ học của riêng những người mình phụ trách |
| `O4` | Số liệu cộng dồn được theo cơ cấu tổ chức, từ một phòng ban lên tới cả khối |
| `O5` | Biết được tại một thời điểm trong quá khứ ai thuộc nhóm nào, để báo cáo cũ vẫn đọc được |

---

# 4. Stakeholder

| Stakeholder | Action |
|---|---|
| **Nhân sự vận hành (Ops)** | Dựng nhóm, quản lý thành viên, gán nội dung cho nhóm, gán người quản lý |
| **L&D** | Giao bài học theo nhóm thay vì theo danh sách người |
| **Quản lý trực tiếp** | Xem tiến độ học của người trong nhánh mình phụ trách |
| **Học viên (UpLMS)** | Nhận nội dung qua nhóm; xem ai là quản lý của mình |
| **Mentor** | Gắn vào nhóm. Khi nhóm được giao lớp thì tự thành mentor của lớp đó, phụ trách đúng người từ nhóm đó. Không có phạm vi dữ liệu riêng như quản lý |
| Hệ HRM (Lark) | Nguồn cơ cấu tổ chức. Hệ gốc, UpLnD chỉ đọc |

---

# 5. Scope

## In scope

| Nhóm việc | Nội dung |
|---|---|
| **Khung nhóm** | Nhóm nhiều cấp, mỗi nhóm có mã, tên, mô tả, nhóm cha. Nhiều cây gốc song song |
| **Nguồn nhóm** | Nhóm đồng bộ từ HRM và nhóm tự tạo. Nguồn quyết định ai sửa được gì. Đồng bộ chạy theo sự kiện từ HRM, cộng một lần đồng bộ toàn bộ mỗi đêm để tự sửa chênh lệch *(`DEC117`)* |
| **Thành viên** | Thêm gỡ thủ công một hoặc nhiều người; thêm gỡ theo lô bằng tệp |
| **Quan hệ nhiều-nhiều** | Một người thuộc nhiều nhóm ở nhiều nhánh |
| **Phạm vi bao trùm** | Nhóm cha gồm người ở toàn bộ nhánh con, ở mọi màn đọc dữ liệu |
| **Gán nội dung** | Gán cho nhóm, tuỳ chọn chảy xuống nhánh con. Công tắc tự ghi danh người vào sau |
| **Quan hệ quản lý** | Gán quản lý cho nhóm; suy ra quản lý theo cây; chỉ định đích danh trên hồ sơ |
| **Quan hệ mentor** | Gán mentor cho nhóm. Mentor của nhóm **chính là** mentor của lớp mà nhóm được giao, phụ trách đúng người từ nhóm đó; mentor đầu tiên vào lớp là người chịu trách nhiệm chính, đổi lại được. Không có cơ chế phạm vi dữ liệu riêng — chốt 06/10/2026 *(`CF-6`)* |
| **Phạm vi dữ liệu** | Quản lý chỉ xem được nhóm mình quản lý |
| **Thành viên theo thời gian** | Ghi mọi thay đổi thành viên kèm thời điểm, giữ không giới hạn. **Nền của báo cáo**, không chỉ để tra tay |
| **Báo cáo theo nhóm** | Cộng dồn số liệu học theo nhóm và theo cả nhánh, ở thời điểm hiện tại. Đặt ở tab Báo cáo của chi tiết nhóm, ba danh sách: theo thành viên, theo nhóm con, theo khoá *(`DEC104`, `DEC135`)* |
| **Một người nhiều vai** | Trong một nhóm, một người được đồng thời là quản lý, mentor và thành viên. Thông báo gửi quản lý không gửi cho chính người đó mà lên quản lý của nhóm cha gần nhất, hết cây thì quản trị viên hệ thống *(`DEC101`, `DEC102`)* |
| **Người nghỉ việc** | Gỡ khỏi nhóm theo đồng bộ. Lượt ghi danh **đánh dấu kết thúc**, không xoá dữ liệu |
| **Vòng đời nhân sự** | Rời nhóm mà chưa học khoá nào → hệ thống tự xử lý. Đang học dở hoặc đã xong → báo quản lý |
| **Hai mail event mới** | `MAIL-GRP-01` — báo quản lý khi người rời nhóm còn nghĩa vụ học · `MAIL-GRP-02` — báo người được gán làm quản lý, nhận chuyển phụ trách, hoặc được chỉ định quản lý chính, để họ biết có nhánh phải theo dõi *(thêm 09/10/2026, CR1)*. 30 mail hiện có không có cái nào cho hai việc này |
| **Màn danh sách** | Xem dạng cây hoặc bảng, lọc theo nguồn, cấp, trạng thái, người quản lý |
| **Lưu trữ** | Nhóm lưu trữ ngừng nhận nội dung mới, giữ nguyên lịch sử. Chỉ nhóm chưa có lịch sử gì mới xoá được |
| **Thông báo theo nhóm** | Thông báo Ops chọn người nhận theo nhóm mới, gồm cả nhánh con. Nhóm cũ của thông báo bỏ hẳn *(25/10/2026, `DEC116`, `US21`)* |
| **Bỏ phòng ban và đơn vị kinh doanh của nhân sự** | Chức năng phòng ban và đơn vị kinh doanh của nhân sự vận hành đã không chạy; bỏ hẳn cùng dữ liệu. API và tệp nhập của module Staff đổi, phá tương thích *(25/10/2026, `DEC116`)* |

## Out of scope

| Không làm | Vì sao |
|---|---|
| **Đồng bộ ngược từ UpLnD về HRM** | HRM là hệ gốc, UpLnD chỉ đọc |
| **Nhóm cho nhân sự vận hành** | Dự án này nhắm học viên. `Department Management` từng phục vụ `staffs` nhưng hiện không chạy; đợt này bỏ hẳn *(`DEC116`)* |
| **Cơ chế phạm vi dữ liệu nhiều mức của `ORG.ROL.04`** | PO đơn giản hoá ngày 05/10: quản lý chỉ xem được nhóm mình quản lý. Không phụ thuộc vào một module chưa làm |
| **Nhóm chứa nội dung** | Vỡ nguyên tắc 6. Nhóm chỉ chứa người. Xem KB `16-domain-principles.md` |
| **Sửa cơ chế ghi danh của Lớp** | Gán qua nhóm vẫn đi qua Lớp và vẫn sinh một lượt ghi danh |
| **Xoá nhóm đã có lịch sử** | PO chốt 05/10: phá `O5`. Chỉ cho lưu trữ. Xem §6 |
| **Dọn lịch sử thành viên theo thời gian** | PO chốt 05/10: giữ toàn bộ. Xem §6 |
| **Chia dữ liệu học theo nhánh cho từng quản lý** | PO chốt 05/10: tiến độ treo vào lượt ghi danh, không chia theo nhánh được. Xem §6 |
| **Nhóm động theo điều kiện** | PO chốt 06/10 *(`OQ-24`)*: đúng **hai** cách vào nhóm — đồng bộ từ HRM theo cây tổ chức, và tự tạo thủ công |
| **Chức năng chuyển lớp** | PO chốt 06/10 *(`OQ-29`)*: hệ thống chưa có. Muốn chuyển thì xoá khỏi lớp cũ, thêm lớp mới, **học lại từ đầu** |
| **Tổ chức tự thêm loại quan hệ** | PO chốt 12/10 *(`DEC84`)*: loại quan hệ cố định, gồm quản lý và mentor |

## Potential scope

| Có thể làm sau | Ghi chú |
|---|---|
| **Báo cáo theo nhóm trên dashboard** | Đợt này chỉ làm tab Báo cáo trong chi tiết nhóm *(`DEC104`)* |
| **Báo cáo theo nhóm tại một mốc quá khứ** | Đợt này chỉ làm báo cáo ở thời điểm hiện tại. Dữ liệu trạng thái học chỉ có từ khi làm phần này; lịch sử thành viên vẫn ghi từ đầu *(`DEC135`, PRD `US22`)* |
| **Chặn tự chấm bài khi một người vừa là mentor vừa là thành viên của lớp** | Đợt này tạm cho phép, rủi ro đã chấp nhận *(`DEC103`)* |

> Mục *Dùng nhóm làm nguồn người nhận cho thông báo Ops* chuyển vào In scope ngày 25/10/2026 *(`DEC116`)*.
>
> Hai mục từng nằm ở đây đã được quyết dứt điểm ngày 06/10: **nhóm động theo điều kiện** chuyển sang *Out of scope* · **xử lý vòng đời nhân sự** chuyển vào *In scope*, thành `US19` và `US20`.

---

# 6. Solution (khung)

> Mục này nêu **khung nghiệp vụ**, không đi vào màn hình hay cách làm. Mọi mục đánh dấu *"PO chốt"* là quyết định đã có — 05/10 ở Gate 1, 06/10 ở Gate 2 và Bước 7. **Không còn chỗ nào chờ quyết ở mức khung.**

## Nhóm là gì trong hệ này

**Nhóm là một tập hợp người.** Nó không chứa nội dung, không có thời hạn, và không sinh nghĩa vụ học.

Cây tổ chức đồng bộ từ HRM là **một nguồn** tạo nhóm, không phải bản chất của chức năng. Nhóm còn có thể do người dùng tự tạo, và có thể cắt ngang cơ cấu.

## Nhóm nối với việc học qua Lớp

```
Nhóm  ──gán nội dung──►  Lớp  ──ghi danh──►  Người học có nghĩa vụ
 (ai)                     (ai + học gì + khi nào)
```

Gán nội dung cho nhóm là một **luật đứng**: ai thuộc nhóm này thì vào lớp này. Người gia nhập sau khi đã gán vẫn tự nhận, nếu công tắc tự ghi danh đang bật. Nếu chỉ sao chép thành viên một lần thì không khác gì nhập file, và `O2` không đạt.

Tiến độ học vẫn treo vào **lượt ghi danh của Lớp** như hiện nay. Nhóm không giữ tiến độ.

## Ba thứ phải đúng, bất kể làm theo cách nào

| # | Ràng buộc |
|---|---|
| `C1` | Nhóm **chỉ chứa người**. Không chứa khoá, không chứa lộ trình. Theo nguyên tắc 6 |
| `C2` | Người vừa ở Lớp vừa ở Nhóm, cùng được gán một khoá, vẫn chỉ sinh **một lượt ghi danh** |
| `C3` | Mọi thay đổi thành viên phải **lưu kèm thời điểm**, đủ để dựng lại trạng thái tại một mốc quá khứ.<br>🔴 **Đây là nền của báo cáo, không phải một màn hình tra cứu.** `O4` và `O5` đều phụ thuộc hoàn toàn vào đây — xem mục *Báo cáo phải đọc qua lớp nào* |

## Số cấp của cây

PO chốt ngày 21/10/2026: **không giới hạn số cấp** *(`DEC100`)*, thay quyết định 6 cấp ngày 05/10/2026. Cây thật trên Lark hiện sâu 4 cấp. Chặn vòng lặp khi di chuyển nhánh vẫn giữ.

## Vòng đời của một nhóm

PO chốt ngày 05/10/2026. Hệ thống **không cho xoá một nhóm đã có lịch sử**, vì xoá là phá chính `O5`:

| Nhóm thế nào | Cho làm gì |
|---|---|
| **Chưa từng** có thành viên và **chưa từng** gán nội dung | **Xoá được.** Đây là nhóm tạo nhầm, không có gì để mất |
| Đã từng có thành viên **hoặc** đã từng gán nội dung | **Chỉ lưu trữ.** Nhóm ngừng nhận nội dung mới, giữ nguyên toàn bộ lịch sử. Không cho xoá, kèm giải thích vì sao |

Lưu trữ một nhóm **không đụng tới lượt ghi danh đã sinh ra**, vì chúng sống ở Lớp. Người đang học dở vẫn học tiếp. Thứ mất đi là luật đứng *"ai vào nhóm này thì vào lớp kia"*, nên từ đó không ai mới được thêm vào lớp qua đường này.

## Lịch sử thành viên giữ bao lâu

PO chốt ngày 05/10/2026: **giữ toàn bộ, không giới hạn thời gian, không dọn.**

Khối lượng quá nhỏ để phải lo — 384 nhân sự, mỗi lần vào ra một nhóm là một dòng, cỡ vài trăm dòng mỗi năm. Đổi lại, đặt hạn lưu trữ tạo ra loại lỗi khó chịu: báo cáo năm ngoái chạy được, năm kia thì không, và không ai nhớ vì sao. Nhất quán với `BR-3.9` của Gamification.

## Báo cáo phải đọc qua lớp nào

PO chốt ngày 05/10/2026: **báo cáo theo nhóm phải xem lại được theo mốc quá khứ.** Mở số liệu quý trước thì vẫn ra đúng con số đã chốt lúc đó.

Việc này quyết định thứ tự phụ thuộc giữa các mục tiêu:

```
Dữ liệu thành viên theo thời gian  ──►  Báo cáo theo nhóm   (O4)
          (C3)                     ──►  Tra nhật ký         (O5, US15)
```

Không có lớp dưới thì lớp trên sai số. Ví dụ:

> Quý 3 chốt: *"Fulfillment HCM — 48/55 người hoàn thành khoá An toàn lao động"*.
> Tháng 10 phòng nhận thêm 6 người. Mở lại báo cáo quý 3.

| Có dữ liệu thành viên theo thời gian | Không có |
|---|---|
| **48/55** — tính theo 55 người có mặt ngày 30/09 | **48/61** — tính theo danh sách hôm nay |

Hai điều rút ra:

| | |
|---|---|
| 1 | **Mọi báo cáo theo nhóm đều phải đi qua lớp này**, kể cả báo cáo của ngày hôm nay. Không có đường tắt nào đọc thẳng danh sách thành viên hiện tại |
| 2 | **`US15` là màn tra cứu nhẹ.** PO chốt nhật ký chỉ dùng khi có vấn đề cần làm rõ, không phải công cụ vận hành hằng ngày. Nó đọc lại cùng dữ liệu mà báo cáo dùng |

> ⚠️ Nhóm API `Report LMS` hiện có *(6 endpoint)* đều lấy `class_id` làm khoá, **không có chiều nào theo người hay theo nhóm**. `O4` không tận dụng được gì ở đó.

## Ba trường hợp rời nhóm, ba luật khác nhau

PO chốt ngày 06/10/2026. Áp một luật cho cả ba sẽ hoặc mất dữ liệu học, hoặc chặn việc hợp lệ.

| Trường hợp | Quan hệ với nhóm | Nghĩa vụ học đã nhận |
|---|---|---|
| **Nghỉ việc** | **Gỡ** theo đồng bộ | **Đánh dấu lượt ghi danh đã kết thúc**, giữ nguyên dữ liệu |
| **Rời nhóm, chưa học khoá nào** | Gỡ | **Chuyển được**, không vướng gì — `US19` |
| **Rời nhóm, đang học dở hoặc đã xong** | Gỡ | **Báo quản lý và L&D**, người quyết chứ không phải hệ thống — `US20` |

### Vì sao nghỉ việc không xoá lượt ghi danh

Báo cáo trong hệ này **được tính ra từ dữ liệu**, không lưu sẵn ở đâu. Xoá lượt ghi danh là xoá chính thứ mà báo cáo đọc.

> Quý 3 chốt: *"Fulfillment HCM — 48/55 hoàn thành khoá An toàn lao động"*.
> Tháng 10, bảy người nghỉ việc. Mở lại báo cáo quý 3.

Nếu xoá thì hệ thống tính lại từ dữ liệu còn lại và ra **41/48**, không phải 48/55. Đánh dấu thì con số cũ giữ nguyên.

Cách này cũng nhất quán với cách hệ thống đối xử với tài khoản: nhân sự nghỉ việc thì tài khoản **tự chuyển `Block`** *(`KB-USER-03`)*, không bị xoá.

> ⚠️ **Luật đồng bộ đi kèm:** người nghỉ việc biến mất khỏi cây tổ chức trên Lark, nên lần đồng bộ kế tiếp sẽ gỡ họ khỏi nhóm. Quan hệ thành viên phải ghi là **rời nhóm kèm thời điểm**, không xoá dòng — nếu không thì ràng buộc `C3` vỡ và báo cáo quá khứ sai.

## Người thuộc nhóm nào khi đồng bộ

PO chốt ngày 06/10/2026: **chỉ thuộc nhóm sâu nhất** trên nhánh của họ.

> Người ở `ECOM / Trung tâm vận hành 1 / Growth 1 / Sub-Growth 1` là thành viên của **`Sub-Growth 1`**, không phải của cả bốn nhóm trên đường đi.

Nhóm cha vẫn bao trùm toàn bộ nhánh con **ở mức đọc** — báo cáo cộng dồn và phạm vi quản lý tính theo cả nhánh. Chỉ quan hệ thành viên là không nhân bản theo độ sâu.

Người thuộc nhiều nhánh *(cơ cấu ma trận)* thì có nhiều nhóm sâu nhất, mỗi nhánh một cái.

## Quản lý thấy được gì

PO chốt ngày 05/10/2026: **xem được một người thì xem toàn bộ dữ liệu học của người đó**, kể cả nội dung người đó nhận qua nhánh khác.

Lý do nằm ở cách dữ liệu đang lưu: tiến độ treo vào **lượt ghi danh của Lớp**, không treo vào nhóm. Một khoá có một tiến độ, không chia được theo nhánh. Cách chia phần sẽ khiến hai quản lý mở cùng một hồ sơ, thấy hai con số khác nhau, và không ai biết con số nào đúng.

> ⚠️ **Hệ quả phải chấp nhận:** người thuộc hai nhánh thì **cả hai quản lý cùng thấy toàn bộ** dữ liệu học của họ. Đây là hệ quả của cơ cấu ma trận mà dự án cố ý cho phép, không phải lỗi phân quyền. Tổ chức không muốn vậy thì không xếp người đó vào hai nhánh.

## Hai chỗ từng mở, nay đã chốt

| Chỗ từng mở | Chốt 06/10/2026 |
|---|---|
| Khi đồng bộ, người ở nhánh sâu thuộc **một** nhóm sâu nhất hay **cả đường đi** | ✅ **Nhóm sâu nhất.** Một người một quan hệ thành viên, không nhân bản theo độ sâu. Nhóm cha vẫn bao trùm nhánh con ở mức **đọc** — báo cáo và phạm vi quản lý |
| Có làm **nhóm động theo điều kiện** không | ✅ **Không.** Đúng hai cách vào nhóm: đồng bộ từ HRM theo cây tổ chức, và tự tạo thủ công |

---

# 7. Danh sách User Story dự kiến

> Nhóm bàn giao, phụ thuộc và thứ tự release của 21 US nằm ở `inception/prd/prd.md` mục *Unit — nhóm bàn giao*, bảng `U1` đến `U8`. BRD không lặp lại bảng đó.

## Phía vận hành và quản lý — UpLMS Ops

| ID | User Story | Nguồn |
|---|---|---|
| `US1` | Là vận hành, tôi cần tạo và sửa nhóm nhiều cấp, để dựng được cơ cấu mà tổ chức đang dùng | Hạng mục 1, 4 |
| `US2` | Là vận hành, tôi cần di chuyển một nhánh sang nhóm cha khác, để cơ cấu đổi thì hệ thống theo kịp | Hạng mục 4 |
| `US3` | Là vận hành, tôi cần thêm và gỡ thành viên thủ công, để xử lý trường hợp lẻ | Hạng mục 5 |
| `US4` | Là vận hành, tôi cần thêm và gỡ thành viên theo lô bằng tệp, để không phải thao tác từng người với nhóm hàng chục người | Hạng mục 6 |
| `US5` | Là vận hành, tôi cần nhóm đồng bộ từ HRM được đánh dấu riêng, để biết nhóm nào sửa được và nhóm nào không | Hạng mục 3 |
| `US6` | Là vận hành, tôi cần xem danh sách nhóm dạng cây hoặc bảng kèm bộ lọc, để tìm được nhóm trong số hàng chục nhóm | Hạng mục 10 |
| `US7` | Là vận hành, tôi cần gán nội dung cho một nhóm, tuỳ chọn chảy xuống nhánh con, để giao bài cho cả phòng bằng một thao tác | Hạng mục 8 · giải `O1` |
| `US8` | Là vận hành, tôi cần bật tắt việc người mới vào nhóm tự nhận nội dung đã gán, để kiểm soát ai phải học gì | Hạng mục 9 · giải `O2` |
| `US9` | Là vận hành, tôi cần gán một hoặc nhiều người quản lý cho nhóm, để hệ thống biết ai phụ trách ai | Hạng mục 13 |
| `US10` | Là vận hành, tôi cần hệ thống tự suy ra quản lý theo cây khi nhóm con chưa gán, để không phải gán lại cho từng nhánh | Hạng mục 14 |
| `US11` | Là vận hành, tôi cần chỉ định quản lý đích danh trên hồ sơ một người, để xử lý trường hợp báo cáo chéo nhánh | Hạng mục 15 |
| `US12` | Là vận hành, tôi cần gán mentor cho nhóm, để khi nhóm được giao lớp thì mentor tự vào lớp đó và phụ trách đúng người từ nhóm | Hạng mục 19 · `CF-6` |
| `US13` | Là vận hành, tôi cần được cảnh báo khi một nhóm trống quản lý và chuyển được toàn bộ quan hệ sang người khác | Hạng mục 18 |
| `US14` | Là vận hành, tôi cần lưu trữ một nhóm để nó ngừng nhận nội dung mới mà vẫn giữ lịch sử, và chỉ xoá được nhóm tạo nhầm chưa có lịch sử gì | Hạng mục 12 · `OQ-07` |
| `US15` | Là vận hành, tôi cần tra được nhật ký thay đổi thành viên khi có vấn đề cần làm rõ, không giới hạn thời gian | Hạng mục 11 · `OQ-08` · `BA-05` · giải `O5` |
| `US16` | Là quản lý, tôi cần xem toàn bộ dữ liệu học của người trong nhánh mình phụ trách, và chỉ những người đó. Màn này ở **UpLMS Ops**; quản lý đăng nhập bằng tài khoản học viên của mình | Hạng mục 16 · `OQ-09` · giải `O3` · `DEC73` · `DEC101` |

### `MAIL-GRP-02` — mail event thứ hai, thêm 09/10/2026 theo CR1

Không có mail này thì người được gán không biết mình có nhánh phải theo dõi, màn `US16` không có cửa vào và `O3` treo *(`DEC74`, `RC-20`)*.

| | |
|---|---|
| **Khi nào bắn** | Một người được gán **trực tiếp** làm quản lý của một nhóm *(`US9`)* · nhận chuyển toàn bộ phụ trách từ người khác *(`US13`)* · được chỉ định làm quản lý chính trên hồ sơ một người *(`US11`)* |
| **Ai nhận** | Người được gán. Không đồng gửi ai |
| **Nói gì** | Nhóm nào hoặc người nào, ai gán, lúc nào · với nhóm: số người trong nhánh tính cả nhóm con · đường dẫn tới màn theo dõi nhánh `US16` |
| **Để làm gì** | Người nhận biết mình đã có nhánh phải theo dõi và vào đúng màn |

> Không bắn khi quan hệ **kế thừa** từ nhóm cha, vì không có thao tác gán nào xảy ra · người đó **đã là** quản lý của chính nhóm đó · gán hoặc chuyển **mentor** *(`US12`)*.
>
> Chuyển phụ trách nhiều nhóm thì **một** email gộp, chỉ liệt nhóm người nhận chưa quản lý trước đó; không còn nhóm mới nào thì không gửi. Câu chữ cụ thể ở PRD `US9`.

## Phía học viên — UpLMS

| ID | User Story | Nguồn |
|---|---|---|
| `US17` | Là học viên, tôi cần thấy ai là quản lý của mình và cách liên hệ | Hạng mục 17 |

## Báo cáo

| ID | User Story | Nguồn |
|---|---|---|
| `US18` | Là vận hành, tôi cần xem số liệu học cộng dồn theo nhóm và theo cả nhánh, ở thời điểm hiện tại hoặc tại một mốc quá khứ, để báo cáo theo cơ cấu tổ chức | `BA-05a` · giải `O4` |

> `US18` chỉ chạy được khi ràng buộc `C3` *(thành viên lưu kèm thời điểm)* đã có. Xem §6 *Báo cáo phải đọc qua lớp nào*.

## Vòng đời nhân sự

| ID | User Story | Nguồn |
|---|---|---|
| `US19` | Là vận hành, tôi cần hệ thống **tự** gỡ người khỏi các khoá chưa học rồi thêm vào nhóm mới, để không phải can thiệp vào việc đơn giản | `OQ-22` · `OQ-23` · `OQ-37` |
| `US20` | Là quản lý, tôi cần nhận **email** khi một người tôi phụ trách rời nhóm mà **đang học dở hoặc đã học xong**, để tự quyết xử lý thay vì để hệ thống tự làm | `OQ-22` · `OQ-23` · `OQ-38` |

### `MAIL-GRP-01` — mail event mới phải làm

30 mail tự động hiện có không có cái nào cho việc này, nên bổ sung một cái mới *(PO chốt 06/10)*.

| | |
|---|---|
| **Khi nào bắn** | Một người rời nhóm *(bị gỡ, hoặc đồng bộ gỡ do điều chuyển)* mà **còn ít nhất một khoá đang học dở hoặc đã học xong** |
| **Ai nhận** | **Quản lý** của người đó. Tạm thời chưa gửi L&D |
| **Nói gì** | Ai rời nhóm nào, sang nhóm nào, còn những khoá nào ở tình trạng gì, và cần người nhận vào quyết. Kèm một câu cảnh báo cố định: **gỡ khỏi lớp sẽ xoá tiến độ đã học, không khôi phục được** *(thêm 09/10/2026, `DEC75`)* |
| **Để làm gì** | Người nhận vào xử lý thủ công. Hệ thống **không tự quyết** trong trường hợp này |

> Không bắn khi người đó **chưa học khoá nào** — trường hợp đó `US19` xử lý tự động.
>
> Không bắn khi **nghỉ việc** — trường hợp đó lượt ghi danh chỉ đánh dấu kết thúc, không cần ai quyết.

Câu chữ cụ thể để PRD.

### Ba trường hợp rời nhóm, ba luật khác nhau

| Trường hợp | Luật | Chốt ở |
|---|---|---|
| **Nghỉ việc** | Gỡ khỏi nhóm. Lượt ghi danh **đánh dấu kết thúc**, giữ nguyên dữ liệu | `CF-4` · `OQ-36` |
| **Rời nhóm, chưa học khoá nào** | Chuyển được, không vướng gì — `US19` | `OQ-22` |
| **Rời nhóm, đang học dở hoặc đã xong** | **Báo quản lý và L&D**, người quyết chứ không phải hệ thống — `US20` | `OQ-22` |

> Áp một luật cho cả ba sẽ hoặc mất dữ liệu học, hoặc chặn việc hợp lệ.

## Thông báo Ops

| ID | User Story | Nguồn |
|---|---|---|
| `US21` | Là vận hành, tôi cần chọn nhóm làm người nhận khi tạo thông báo trên UpLMS Ops, để gửi cho cả một phòng ban mà không chọn từng người | `DEC4` · `DEC116` |

## Đã bỏ khỏi phạm vi

| Việc | Vì sao |
|---|---|
| **Nhóm động theo điều kiện** | PO chốt 06/10 *(`OQ-24`)*: đúng **hai** cách vào nhóm — đồng bộ từ HRM theo cây tổ chức, và tự tạo thủ công. Không có cách thứ ba |

---

# 8. Tác động tới hệ thống hiện tại

> Bảng dưới là bản quét sơ bộ lúc viết BRD, chỉ liệt kê module bị chạm tới và lý do chạm, lấy từ KB. Mức ảnh hưởng, 12 vùng gốc và 6 conflict đã quyết nằm ở `inception/impact-analysis/impact-matrix.md` v0.6; vùng 9 *(mail `MAIL-GRP-02`)* thêm ở CR1 ngày 09/10/2026, vùng 13 đến 15 thêm ở CR6 ngày 21/10/2026, vùng 16 đến 18 thêm ở CR7 ngày 25/10/2026.

| Module | Chạm vào vì |
|---|---|
| **Class / ghi danh** | Thêm một đường gán nội dung mới song song với đường hiện tại. Ràng buộc `C2` bắt hai đường không được sinh ghi danh trùng |
| **User** | Thêm quan hệ nhiều-nhiều giữa người và nhóm, thêm quan hệ quản lý và mentor |
| **Phân quyền** | Thêm phạm vi dữ liệu theo nhánh nhóm |
| **Tích hợp Lark** | Mở rộng cơ chế đồng bộ hiện có từ tầng người sang tầng cơ cấu |
| **Báo cáo** | Mọi báo cáo theo nhóm phải tính theo quy tắc cha bao trùm toàn bộ nhánh con |
| **Gamification** | `US16` của dự án đó *(bộ lọc bảng xếp hạng theo nhóm)* đang chờ chức năng này |
| **Thông báo Ops** | Chọn người nhận theo nhóm mới, gồm cả nhánh con; nhóm cũ của thông báo bỏ, API tạo, sửa, xem thông báo đổi phá tương thích *(CR7, `DEC116`, `US21`)* |
| **Staff** | Bỏ phòng ban và đơn vị kinh doanh của nhân sự vận hành cùng dữ liệu; API nhân sự, vị trí, cơ sở và tệp nhập nhân sự đổi, phá tương thích *(CR7, `DEC116`)* |
| **Chấm điểm** | Danh sách mentor của lớp và người chấm nhận tài khoản học viên; người vừa là mentor vừa là thành viên tạm được tự chấm bài của mình *(CR6, `DEC101`, `DEC103`)* |
| **Đăng nhập UpLMS Ops** | Tài khoản học viên được gán quản lý hoặc mentor vào được UpLMS Ops, chỉ thấy màn của vai đó *(CR6, `DEC101`)* |

---

# 9. Assumptions

| # | Giả định | Cần ai xác nhận |
|---|---|---|
| `A1` | Cơ chế đồng bộ người dùng từ Lark mở rộng được sang đồng bộ cơ cấu, không phải dựng lại từ đầu | Dev, khi làm |
| `A2` | Cây tổ chức trên Lark là nguồn đủ tin cậy, không cần đối soát thủ công sau mỗi lần đồng bộ | PO |
| ~~`A3`~~ | ~~Số cấp 6 đủ cho ít nhất hai tới ba năm tới~~ Không còn áp dụng: bỏ giới hạn số cấp *(`DEC100`)* | PO |
| `A4` | Người quản lý luôn là một tài khoản có trong hệ thống, không phải người ngoài | PO |
| `A5` | Danh sách mentor của lớp và người chấm bài nhận được tài khoản học viên mà không phải đổi luồng chấm hiện có | Tech PIC |

---

# 10. Open Questions

Danh sách đầy đủ: `inception/requirements-analysis/requirements-analysis-questions.md`

✅ **Bốn câu nhóm D đã đóng hết ngày 06/10/2026 ở Bước 7.**

| # | Câu hỏi | Owner | Chặn |
|---|---|---|---|
| ~~`OQ-21`~~ ✅ | Khi đồng bộ, người ở nhánh sâu thuộc một nhóm sâu nhất hay cả đường đi | PO | **Đóng 06/10 — nhóm sâu nhất.** Nhóm cha vẫn bao trùm nhánh con ở mức đọc |
| ~~`OQ-22`~~ ✅ | Một người rời nhóm thì nghĩa vụ học đã nhận xử lý thế nào | PO | **Đóng 06/10 — xét theo tình trạng học từng khoá.** Xem §7 *Vòng đời nhân sự* |
| ~~`OQ-23`~~ ✅ | Học viên bị điều chuyển phòng ban thì xử lý thế nào | PO | **Đóng 06/10 — cùng luật với `OQ-22`** |
| ~~`OQ-24`~~ ✅ | Có làm nhóm động theo điều kiện không | PO | **Đóng 06/10 — không làm** |

## Đã đóng tại Gate 1 — 05/10/2026

| # | Quyết định | Vào đâu trong tài liệu |
|---|---|---|
| ~~`OQ-07`~~ ✅ | Nhóm chưa có lịch sử thì xoá được; nhóm đã có thành viên hoặc đã gán nội dung thì **chỉ lưu trữ** | §5 Out of scope · §6 *Vòng đời của một nhóm* · `US14` |
| ~~`OQ-08`~~ ✅ | **Giữ toàn bộ** lịch sử thành viên, không giới hạn thời gian, không dọn | §5 In scope · §6 *Lịch sử thành viên giữ bao lâu* · `US15` |
| ~~`OQ-09`~~ ✅ | Quản lý xem được một người thì xem **toàn bộ** dữ liệu học của người đó | §6 *Quản lý thấy được gì* · `US16` |

## Đã đóng ở Bước 5 — 05/10/2026

| # | Quyết định | Vào đâu trong tài liệu |
|---|---|---|
| ~~`BA-01`~~ ✅ | Bỏ hẳn `Group Management` và Recipients List đang có, **coi như chưa có gì** | §1 Problem · §6 |
| ~~`BA-02`~~ ✅ | `Test Account` **loại khỏi mọi báo cáo và mọi logic** | `US18` và mọi US có báo cáo |
| ~~`BA-03`~~ ✅ | Luật đứng **theo luật của Lớp**, không có ngoại lệ riêng | §6 *Nhóm nối với việc học qua Lớp* · `US7` |
| ~~`BA-04`~~ ✅ | Gán vào **đúng lớp đã gắn với nhóm**, hệ thống không tự đi tìm | `US7` |
| ~~`BA-05`~~ ✅ | **Báo cáo phải xem lại được theo mốc quá khứ.** Nhật ký chỉ tra khi có vấn đề | §6 *Báo cáo phải đọc qua lớp nào* · `C3` · `US15` · `US18` |
| ~~`BA-06`~~ ⚠️ | ~~Người nghỉ việc giữ nguyên trong nhóm~~ — **đã bị thay thế bởi `CF-4` ngày 06/10**: gỡ khỏi nhóm, lượt ghi danh đánh dấu kết thúc | §6 *Ba trường hợp rời nhóm* |
| ~~`BA-07`~~ ✅ | Vượt sức chứa lớp **chỉ cảnh báo**, vẫn thêm được | `US7` |

## Đã đóng ở Gate 2 — 06/10/2026

| # | Quyết định | Vào đâu trong tài liệu |
|---|---|---|
| ~~`CF-6`~~ ✅ | **Mentor của nhóm chính là mentor của lớp**, không phải hai khái niệm. Thêm nhóm vào lớp thì mentor của nhóm được gán luôn làm mentor trong lớp, phụ trách đúng nhóm đó. Mentor đầu tiên vào lớp là người chịu trách nhiệm chính, đổi lại được | §4 · §5 In scope *Quan hệ mentor* · `US12` |
| ~~`CF-4`~~ ✅ | Người nghỉ việc gỡ khỏi nhóm, lượt ghi danh **đánh dấu kết thúc**, giữ dữ liệu — thay `BA-06` | §6 *Ba trường hợp rời nhóm* |

## Đã đóng ở CR1 — 09/10/2026

| # | Quyết định | Vào đâu trong tài liệu |
|---|---|---|
| ~~`DEC73`~~ ✅ | Màn theo dõi nhánh `US16` ở **UpLMS Ops**, quản lý dùng tài khoản nhân sự vận hành như `US9`. Phần tài khoản thay bởi `DEC101` ngày 21/10/2026: quản lý dùng tài khoản học viên | §1 *Product boundary* · §7 |
| ~~`DEC74`~~ ✅ | Thêm mail event **`MAIL-GRP-02`** báo người được gán quản lý, nhận chuyển phụ trách, hoặc được chỉ định quản lý chính; quan hệ kế thừa không gửi | §5 In scope · §7 *`MAIL-GRP-02`* |
| ~~`DEC75`~~ ✅ | `MAIL-GRP-01` thêm câu cảnh báo: gỡ khỏi lớp sẽ xoá tiến độ, không khôi phục được | §7 *`MAIL-GRP-01`* |

## Đã đóng ở CR6 — 21/10/2026

| # | Quyết định | Vào đâu trong tài liệu |
|---|---|---|
| ~~`DEC100`~~ ✅ | Không giới hạn số cấp của cây nhóm | §1 *Product boundary* · §6 *Số cấp của cây* |
| ~~`DEC101`~~ ✅ | Một người được đồng thời là quản lý, mentor, thành viên bằng một tài khoản học viên; tài khoản đó vào UpLMS Ops cho đúng màn của vai | §1 *Product boundary* · §5 In scope · §7 `US16` |
| ~~`DEC102`~~ ✅ | Thông báo gửi quản lý không gửi cho chính người đó, lên quản lý của nhóm cha gần nhất | §5 In scope |
| ~~`DEC103`~~ ✅ | Tạm cho tự chấm khi vừa là mentor vừa là thành viên | §5 Potential scope |
| ~~`DEC104`~~ ✅ | Báo cáo theo nhóm ở tab Báo cáo trong chi tiết nhóm; dashboard để sau | §5 In scope · Potential scope |

## Đã đóng ở CR7 — 25/10/2026

| # | Quyết định | Vào đâu trong tài liệu |
|---|---|---|
| ~~`DEC116`~~ ✅ | Thông báo Ops chọn người nhận theo nhóm, `US21`; bỏ phòng ban và đơn vị kinh doanh của nhân sự | §5 In scope · Potential scope · §7 · §8 |
| ~~`DEC117`~~ ✅ | Đồng bộ theo sự kiện, cộng một lần chạy toàn bộ mỗi đêm | §5 In scope |
| ~~`DEC118`~~ ✅ | Chữ giao diện bằng tiếng Anh | §1 *Product boundary* |

---

# 11. References

| Loại | Nguồn |
|---|---|
| Yêu cầu gốc | `inputs/yeu-cau-goc-20261005.md` — 19 hạng mục |
| Bản làm rõ | `inception/requirements-analysis/requirements.md` v0.5 — `RC-01` đến `RC-30` |
| Câu hỏi đã đóng | `inception/requirements-analysis/requirements-analysis-questions.md` — `OQ-xx`, `BA-xx` |
| Nghiên cứu LMS khác | `ideation/market-research/competitive-analysis.md` v0.2 — TalentLMS · Docebo · Moodle · bốn bài TalentLMS; nguyên văn ở `inputs/talentlms-help-articles-20261007.md` |
| Dữ liệu HRM | `inputs/lark-users-by-department.csv` — 384 nhân sự, 53 phòng ban |
| Quyết định đã chốt | `decisions.md` — `DEC1` đến `DEC135`; bản v1 ở `archive/v1/project-decisions.md` |
| Phạm vi hiện hành chi tiết | `inception/prd/prd.md` v0.8 — 22 US, `US22` để sau |
| Thiết kế của các team | `inception/ux-design/ux-design.md` · `inception/tech-design/be-technical-design.md` · `inception/tech-design/fe-technical-design.md` |
| Ảnh hưởng | `inception/impact-analysis/impact-matrix.md` v0.6 — 18 vùng, 6 conflict đã quyết |
| Nguyên tắc mô hình hoá | KB `domain/16-domain-principles.md` — nguyên tắc 6, ranh giới Nhóm với Lớp |
| KB liên quan | `domain/` — `04-class.md` · `06-user-account.md` · `12-data-model.md` · `14-api-surface.md` · `15-product-direction.md` §6 và §7 |
| Intent liên quan | `intents/260923-gamification/` — `US16` của intent đó *(bộ lọc bảng xếp hạng theo nhóm)* chờ chức năng này · `intents/261006-report-phase-1/` — tham chiếu `US16` và `US18` |
