---
intent: 261005-group
artifact: requirements
version: 0.2
status: approved
approved: 2026-10-05
ids: RC-01 đến RC-19 theo họ mã v1, không đổi
migrated-from: .claude/projects/Group/working/ai-drafts/clarified-requirements-20261005.md
---
# Làm rõ yêu cầu — Group

**Ngày:** 05/10/2026 · **Phiên bản:** v0.2 — cập nhật 05/10 sau khi PO trả lời 5 câu hỏi chặn
**Input:** `working/raw-inputs/yeu-cau-goc-20261005.md` — 19 hạng mục, hai nhóm `Group` và `User Group Relationship`
**Mục đích PO nêu:** tổ chức các nhóm học tập, để gán, theo dõi và đánh giá theo từng nhóm

---

## 1. Nền để mở rộng — đã xác nhận

PO trả lời `OQ-01` ngày 05/10:

| Nhóm API | Trạng thái thật | Dùng được không |
|---|---|---|
| **`Group Management`** (9 operation) | ✅ **Đang chạy.** Phục vụ việc tạo nhóm để **gửi thông báo từ Ops** | ✅ **Đây là nền để mở rộng** |
| **`Department Management`** (9 operation) | ❌ **Không chạy.** Trước đây chỉ dành cho `staffs` | ❌ Không phải nền |

Nên dự án này là **mở rộng một chức năng đang chạy**, không phải dựng mới từ đầu. Khác biệt lớn về rủi ro: có dữ liệu thật và có người đang dùng.

Hai hệ quả:

**Nhóm trở thành một nguồn duy nhất cho nhiều mục đích.** PO chốt: khi mở lại chức năng gửi thông báo từ Ops, màn đó chọn người nhận từ chính chức năng nhóm này. Nhóm không còn là thứ riêng của một tính năng.

**Phải biết `Group Management` hiện có gì trước khi thiết kế phần thêm.** Nó đang là nhóm phẳng (CRUD group, gán user), còn yêu cầu cần cây nhiều cấp, phân loại theo nguồn, quan hệ quản lý. Phần chênh lệch đó là phạm vi thật của dự án — xem `OQ-16`.

Ghi lại để không mất: `14-api-surface.md` cần cập nhật `Department Management` vào bảng *"endpoint có nhưng tính năng không có"*, cùng chỗ với `Examination` và `Entrance Test`.

---

## 1b. Đóng khung lại — nhóm là chính, cây tổ chức là một nguồn

PO đính chính ngày 05/10: **đây là chức năng Nhóm, không phải chức năng cây tổ chức.**

Cây tổ chức là **một tập con**. Hệ thống đồng bộ với HRM rồi tạo ra các nhóm học viên dựa trên cây đó, và có thể đánh dấu những nhóm này là loại được đồng bộ để phân biệt với nhóm tạo tay. Nhưng nhóm không chỉ có vậy.

Vì sao chỗ này quan trọng:

| Nếu đóng khung là "cây tổ chức" | Nếu đóng khung là "nhóm" |
|---|---|
| Mọi nhóm phải nằm trong cây | Cây chỉ là một cách tạo nhóm |
| Nhóm cắt ngang cơ cấu không biểu diễn được | Nhóm cắt ngang là trường hợp bình thường |
| Nguồn duy nhất là HRM | HRM là một nguồn, còn nguồn khác |

Ba nền tảng lớn đều tách hai khái niệm này thay vì gộp: TalentLMS và Docebo có `Branch` cho cơ cấu và `Group` cho nhóm tuỳ ý, Moodle có `Cohort` phạm vi site và `Group` phạm vi khoá. Docebo mô tả group là thứ *"có thể là tập con bên trong cơ cấu, hoặc cắt ngang nhiều phần của cơ cấu"*.

Chi tiết: `working/ai-drafts/nghien-cuu-lms-khac-20261005.md`

> Cách đồng bộ và cách đánh dấu nhóm là **ví dụ PO đưa ra để làm rõ khái niệm**, không phải giải pháp đã chốt. Bước 7 và 8 mới so sánh phương án.

---

## 2. Chuẩn hoá input

| Nhóm | Nội dung |
|---|---|
| **Stakeholder request** | PO yêu cầu dựng chức năng nhóm với 19 hạng mục |
| **Problem** | *(chưa nêu rõ)* Hiện không gom được học viên thành nhóm để gán nội dung và theo dõi. `US16` của Gamification phải hoãn vì thiếu cái này, và quản lý trực tiếp không có công cụ xem người mình phụ trách |
| **Expected outcome** | Gán nội dung theo nhóm · theo dõi tiến độ theo nhóm · đánh giá theo nhóm · quản lý xem được người thuộc nhánh mình |
| **Users / roles** | Nhân sự vận hành (dựng cây, quản thành viên) · **người quản lý** (vai trò mới, là người dùng chứ không phải role) · học viên (xem quản lý của mình) |
| **Systems / modules** | UpLMS Ops: quản lý nhóm, gán nội dung, phân quyền · UpLMS: trang người học · tích hợp HRM |
| **Constraints** | Đồng bộ từ HRM quyết định ai sửa được gì · phạm vi dữ liệu gắn với `ORG.ROL.04` · phạm vi nhóm cha bao trùm nhánh con là quy tắc nền của mọi báo cáo |
| **Proposed solution** | Toàn bộ 19 hạng mục là mô tả giải pháp, không phải mô tả vấn đề. Chúng là `Recommendation`, chưa phải yêu cầu đã chốt |

> ⚠️ Input mô tả **giải pháp đã nghĩ sẵn** khá chi tiết, nhưng không nêu vấn đề gốc. Ví dụ hạng mục 15 *"Chỉ định quản lý trực tiếp trên hồ sơ, dùng cho báo cáo chéo nhánh và giai đoạn bàn giao"* là một giải pháp cho tình huống nào đó chưa được mô tả. Biết tình huống thật có thể dẫn tới cách làm khác đơn giản hơn.

---

## 3. Requirement candidates

| ID | Requirement | Type | Source | Confidence | Ghi chú |
|---|---|---|---|---|---|
| `RC-01` | Cây nhóm nhiều cấp, số cấp tối đa cấu hình được. Mỗi nhóm có mã, tên, mô tả, nhóm cha | Data · Functional | Mục 1 | High | `Department Management` đã chết nên không dùng lại được. Mở rộng từ `Group Management` đang phẳng |
| `RC-02` | Quan hệ người và nhóm là nhiều-nhiều. Nhiều cây gốc song song để thể hiện cơ cấu ma trận | Data | Mục 2 | High | `Group Management` hiện gán được user, nhưng chưa rõ có cho một người ở nhiều nhóm không — xem `OQ-16` |
| `RC-03` | Phân loại nhóm theo nguồn: đồng bộ HRM và tự tạo. Nguồn quyết định quyền sửa | Business Rule | Mục 3 | Medium | HRM là **Lark**. Đã đồng bộ được học viên, Lark cũng đã có sẵn cây tổ chức. Cần mở rộng sang đồng bộ cây |
| `RC-04` | Tạo, sửa, di chuyển nhóm. Di chuyển nhánh thì nhánh con đi theo và quan hệ quản lý tính lại | Functional | Mục 4 | High | |
| `RC-05` | Thêm gỡ thành viên thủ công, một hoặc nhiều người, có tìm kiếm | Functional | Mục 5 | High | |
| `RC-06` | Thêm gỡ thành viên theo lô: tệp mẫu, tải lên, đối soát từng dòng, báo lỗi theo dòng | Functional | Mục 6 | High | |
| `RC-07` | Phạm vi nhóm cha bao trùm toàn bộ nhánh con ở mọi màn đọc dữ liệu | Business Rule | Mục 7 | High | **Rule nền**, chi phối mọi báo cáo. Ảnh hưởng hiệu năng truy vấn |
| `RC-08` | Gán nội dung cho nhóm, có tuỳ chọn chảy xuống nhánh con, mặc định tắt | Functional | Mục 8 | High | Gán cho nhóm là **luật đứng**, không phải sao chép một lần. Vẫn đi qua Lớp để sinh lượt ghi danh |
| `RC-09` | Cấu hình từng nhóm: người vào sau có tự nhận nội dung đã gán không, toàn bộ hay chỉ còn hiệu lực | Business Rule | Mục 9 | Medium | Chạm logic ghi danh hiện có |
| `RC-10` | Danh sách nhóm dạng cây hoặc bảng, lọc theo nguồn, cấp, trạng thái, người quản lý | Screen | Mục 10 | High | |
| `RC-11` | Nhật ký thay đổi thành viên, đủ để dựng lại ai thuộc nhóm nào tại một thời điểm quá khứ | Data · NFR | Mục 11 | High | Yêu cầu lưu lịch sử có dấu thời gian, giống ràng buộc `C3` ở Gamification |
| `RC-12` | Lưu trữ nhóm: ngừng nhận nội dung mới, giữ lịch sử. Xoá nhóm: xử lý thành viên và nội dung đã gán | Business Rule | Mục 12 | Medium | *"Xử lý"* chưa định nghĩa — xem `OQ-07` |
| `RC-13` | Một nhóm có một hoặc nhiều người quản lý, là người dùng chứ không phải vai trò | Data | Mục 13 | High | |
| `RC-14` | Quản lý suy ra theo cây: không chỉ định đích danh thì lấy quản lý của nhóm cha gần nhất. Tính động | Business Rule | Mục 14 | High | Quan hệ tính lúc đọc, không lưu cứng |
| `RC-15` | Chỉ định quản lý đích danh trên hồ sơ, ghi đè kết quả suy ra từ cây | Functional | Mục 15 | Medium | Tình huống dùng chưa rõ — xem mục 2 |
| `RC-16` | Người quản lý đọc được dữ liệu của nhánh mình, không đọc nhánh khác cùng cấp. Chọn được ở `ORG.ROL.04` | Role-Permission | Mục 16 | Low | `ORG.ROL.04` là mã chức năng chưa làm: mỗi vai trò gắn một phạm vi. Vùng KB chưa phủ, hệ dùng Casbin |
| `RC-17` | Trang người học hiện quản lý trực tiếp và đường liên hệ | Screen | Mục 17 | High | Phần duy nhất chạm UpLMS phía học viên |
| `RC-18` | Quản lý bị khoá hoặc rời nhóm thì cảnh báo nhóm trống quản lý, cho chuyển quan hệ sang người khác | Functional | Mục 18 | Medium | |
| `RC-19` | Khai thêm loại quan hệ ngoài quản lý, ví dụ mentor, dùng chung cơ chế gán và phạm vi dữ liệu | Data · Functional | Mục 19 | Medium | Yêu cầu thiết kế mở rộng được từ đầu |

---

## 4. Ba chỗ nhóm mới đụng thứ đang chạy

### 4.1 Nhóm và Lớp — PO đã chốt

Khác nhau ở **đối tượng gắn vào**: Nhóm gắn **người**, Lớp gắn **nội dung**.

| | Nhóm | Lớp |
|---|---|---|
| Trả lời câu hỏi | **Ai** thuộc về đâu | Ai học **cái gì**, trong **khoảng nào** |
| Gắn với | Người. Không có nội dung | Đúng một đối tượng nội dung: một khoá hoặc một lộ trình |
| Thời gian | Không có. Phòng Marketing không có hạn | Có. Thời hạn, ngày kích hoạt riêng từng người |
| Sinh ra gì | **Không sinh nghĩa vụ học.** Chỉ là địa chỉ để gán | **Sinh nghĩa vụ học.** Vào lớp là có việc phải làm |
| Tiến độ học nằm ở đâu | Không có | Treo vào lượt ghi danh của lớp, không treo vào người |
| Quan hệ với người | Nhiều-nhiều, lồng nhau. Một người ở nhiều nhánh | Một người vào một lớp là một lượt ghi danh |
| Nguồn gốc | Có thể đến từ HRM, chỉ đọc | Luôn do L&D tạo |
| Vòng đời | Lâu dài, theo cơ cấu tổ chức | Theo khoá, mở rồi đóng |
| Dùng cho | Giao hàng loạt, cộng dồn báo cáo, suy ra quản lý, phạm vi dữ liệu | Theo dõi tiến độ, chốt kết quả, cấp chứng chỉ |

**Quan hệ giữa hai cái:**

```
Nhóm  ──gán nội dung──►  Lớp  ──ghi danh──►  Người học có nghĩa vụ
 (ai)                     (ai + học gì + khi nào)
```

**Gán nội dung cho nhóm không phải là sao chép thành viên nhóm vào lớp một lần.** Nó là một **luật đứng**: ai thuộc nhóm này thì vào lớp này. Người gia nhập nhóm sau khi đã gán vẫn tự nhận được, đó là `ORG.GRP.09`. Nếu chỉ sao chép một lần thì không khác gì nhập file.

**Hai cách dùng sai hay gặp**, PO nêu để tránh:

| Cách dùng sai | Vỡ ở đâu |
|---|---|
| **Dùng Lớp làm Nhóm** — tạo *"lớp phòng Marketing"* rồi nhét mọi khoá vào | Lớp gắn đúng một nội dung và có thời hạn, phòng ban thì không. Đổi cơ cấu là phải sửa hàng chục lớp |
| **Nhét nội dung vào Nhóm** — để nhóm *"chứa"* khoá học | Vỡ nguyên tắc 6: quan hệ nội dung với nội dung chỉ sống trong Lộ trình, quan hệ người với nội dung chỉ sống trong Lớp và Automation. **Nhóm không được chứa gì ngoài người** |

`OQ-03` đã chốt: người vừa ở Lớp vừa ở Nhóm, cùng được gán một khoá, vẫn chỉ sinh **một lượt ghi danh**. Điều này nhất quán với bảng trên — nhóm không sinh nghĩa vụ học, nó chỉ dẫn người vào lớp.

### 4.2 Nhóm và phạm vi dữ liệu

`RC-16` là yêu cầu phân quyền thật sự, không phải hiển thị. Hệ thống dùng **Casbin** (`casbin_rule` với `ptype`, `v0`–`v6`), và KB **chưa phủ vùng phân quyền**.

Phạm vi dữ liệu theo nhánh cây là loại phân quyền động: quyền đọc của một người đổi khi cây đổi, không phải khi role đổi. Casbin làm được nhưng cần thiết kế riêng.

### 4.3 Nhóm và báo cáo hồi tố

`RC-11` nói báo cáo phải dựng lại được *"tại một thời điểm trong quá khứ ai thuộc nhóm nào"*. Đây là yêu cầu **lưu lịch sử quan hệ theo thời gian**, nặng hơn nhiều so với lưu trạng thái hiện tại.

Nó chi phối cả `RC-07` (phạm vi cha bao trùm con): báo cáo của tháng trước phải dùng cây của tháng trước, không dùng cây hôm nay.

---

## 5. Phạm vi sơ bộ

### In scope

Khung nhóm và cây · thành viên thủ công và theo lô · quan hệ quản lý · gán nội dung cho nhóm · nhật ký thay đổi · màn danh sách và tìm kiếm.

### Out of scope

| | Vì sao |
|---|---|
| Đồng bộ HRM hai chiều | Yêu cầu chỉ nói đồng bộ *từ* HRM |
| Nhóm cho nhân sự vận hành | `Department Management` đã phục vụ staff. Dự án này nhắm học viên |

### Potential scope — chờ `OQ-01`

Toàn bộ phần khung nhóm (`RC-01`, `RC-04`, `RC-05`, `RC-10`) có thể chuyển từ *làm mới* sang *mở rộng cái đã có*, tuỳ `Group Management` và `Department Management` còn sống hay không.

---

## 6. Phân cỡ đề xuất

**Cỡ `L`.** Đủ cả bốn dấu hiệu, chỉ cần một là đã `L`:

| Dấu hiệu | Ở đây |
|---|---|
| Chạm từ 3 module trở lên | User · Class · Course assignment · Phân quyền · Report · tích hợp HRM |
| Đổi data model | Quan hệ nhiều-nhiều người với nhóm, bảng lịch sử thành viên, bảng quan hệ quản lý |
| Có conflict | Hai đường gán nội dung song song (Lớp và Nhóm) |
| Nhiều hướng giải quyết | Mở rộng `departments` hay dựng bảng mới, là hai hướng khác hẳn nhau |

→ Chạy đủ 9 bước, đủ 4 Gate.

Chi tiết câu hỏi mở: `working/open-questions/open-questions-20261005.md`
