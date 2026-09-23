# [PRD] <Tên tính năng>

> **Template chuẩn UpLnD.** Hợp nhất từ:
> - `Template-goc-Lark.md` — template chính thức công ty (Lark wiki `Arz6w5xvpihQcRkBLe0ljJghgsl`)
> - Thực tế 4 PRD đang dùng: SPX Express · Cấu trúc luồng thanh toán · Routing kho · Shopee Quy tắc từ khóa
>
> Phần *in nghiêng* là hướng dẫn — **xoá khi viết thật**. Mục nào không áp dụng thì **xoá hẳn mục đó**, không để lại nội dung mẫu.

| | |
| --- | --- |
| **Target release** | *Sprint / Quý* |
| **Epic** | *Link Jira* |
| **Story** | *Link Jira* |
| **Related** | *Link PRD / tài liệu liên quan* |
| **Document status** | `DRAFT` / `IN REVIEW` / `PUBLISH` |
| **Document owner** | |
| **Designer** | |
| **Tech lead** | |
| **QA** | |
| **Reviewer** | |

---

# Document version

| Version | Người cập nhật | Nội dung | Impact | Ngày cập nhật |
| --- | --- | --- | --- | --- |
| v0.1 | | *Bản đầu* | | |

---

# Problem

*Vấn đề người dùng đang gặp. Viết theo góc nhìn người dùng, không mô tả giải pháp.*

*Nêu rõ: ai gặp · gặp khi nào · hậu quả là gì.*

---

# Analytics

*Chứng minh vấn đề ở `Problem` là thật, bằng cách **mô tả người dùng đang xoay xở thế nào**.*

*Viết đủ chi tiết để người đọc hiểu ngay vì sao cần thay đổi: họ làm gì · theo thứ tự nào · dựa vào tiêu chí gì · mất bao lâu · sai ở đâu.*

*Ví dụ từ PRD thật (Shopee — không có một con số nào mà vẫn thuyết phục):*

> - Ngày D-1 thường tăng bid hàng loạt cho từ khóa để tăng cạnh tranh cho ngày camp
> - ROAS chiến dịch thấp → check từ khóa tiêu nhiều nhưng doanh số thấp → giảm bid 20-30%, xem có giữ được thứ hạng không

*Có số liệu thì càng tốt — thêm vào. Không có cũng không sao, miễn mô tả hiện trạng đủ rõ.*

---

# Objective

*Mục tiêu đạt được khi triển khai. Viết dạng kết quả, không phải danh sách việc làm.*

---

# Stakeholder

| Stakeholder | Action |
| --- | --- |
| *Vai trò / nhóm người dùng* | *Họ làm gì với tính năng này* |

---

# Preferences

*Tập hợp mọi tài nguyên tham chiếu để đọc PRD và bắt tay làm. Dạng danh sách link.*

- **UX:** *link Figma*
- **Luồng giải pháp:** *link BRD / tài liệu phân tích liên quan*
- **Tài liệu kỹ thuật bên thứ 3:** *spec, PDF, docs của đối tác*
- **API tham chiếu:** *endpoint của hệ thống ngoài đang tích hợp*
- **Tài khoản tích hợp staging:**
  - `app_id`: *…*
  - `secret`: *…*
  - *phạm vi áp dụng*
- **Tài liệu nền khác:** *KB, PRD liên quan, quyết định đã chốt*

> Đây là nơi Dev và QA tìm mọi thứ cần để bắt đầu. Thiếu link ở đây thì họ phải đi hỏi.

---

# Metrics success

*Chỉ làm khi tính năng cần đo ngay từ đầu. **Không áp dụng → xoá hẳn mục này.***

> ⚠️ **Tuyệt đối không giữ lại bảng ví dụ của template.** Hai PRD đang lưu hành mang nguyên chỉ số của app ghi chép thu chi (`NPS > 50`, `Transaction Input Time < 30s`) vào tài liệu về routing kho và quảng cáo Shopee. Hoặc điền chỉ số thật của chính tính năng này, hoặc xoá.

| Factor (HEART) | Goal | Signal | Metrics |
| --- | --- | --- | --- |
| Happiness | | | |
| Engagement | | | |
| Adoption | | | |
| Retention | | | |
| Task Success | | | |

*Không cần đủ 5 factor — chỉ giữ factor thực sự đo được.*

---

# Solution

*Giải pháp tổng thể, cả nghiệp vụ lẫn kỹ thuật. Đủ để người đọc hình dung cách làm trước khi vào chi tiết từng US.*

## TDD

*Thiết kế kỹ thuật: luồng xử lý, sequence, cơ chế. Kèm sơ đồ nếu có.*

## Database

*Bảng mới / bảng bị sửa. Mỗi bảng ghi: tên · mục đích · field chính · quan hệ.*

*Đối chiếu `.claude/_shared-knowledge-base/12-data-model.md` — hệ thống có 85 bảng, `tenant_id` gần như ở mọi bảng nghiệp vụ.*

| Bảng | Mới / Sửa | Mục đích | Ghi chú |
| --- | --- | --- | --- |

## API

*Endpoint mới / endpoint bị đổi. Đối chiếu Swagger trước khi khai báo mới — hệ thống đã có 708 operation.*

| Method | Endpoint | Mới / Sửa | Mục đích |
| --- | --- | --- | --- |

---

# Specific Requirement

> **Quy ước đánh số:**
> - User Story: `US1`, `US2`, `US3`… — đánh liên tục trong PRD
> - Business rule: `BR-<số US>.<số thứ tự>` → `BR-1.1`, `BR-1.2`, `BR-2.1`… unique toàn PRD
> - US chưa làm trong phạm vi này: ghi rõ trong tiêu đề, ví dụ `US3: Sao chép quy tắc — chưa làm`

## US1: <Tên user story>

### 1/ User story

*Viết một câu tự nhiên theo vai trò. Ví dụ: "Là vận hành, tôi cần mapping kho vật lý với kho kênh bán để xử lý đơn và trừ tồn đúng kho."*

### 2/ Pre - Condition

*Điều kiện cần có trước khi thực hiện US này: trạng thái dữ liệu, quyền, cấu hình, US khác đã xong.*

### 3/ Scenario

*Kịch bản vận hành: người dùng đi từ đâu, làm gì, theo thứ tự nào.*

### 4/ Acceptance criteria

**UI / UX / Rule UX / Rule UI**

*Chọn một trong hai dạng bảng:*

*Dạng A — tính năng mới:*

| Màn hình | Giao diện | Field | Yêu cầu |
| --- | --- | --- | --- |
| | | | *Định dạng · placeholder · options · giá trị mặc định · điều kiện disable · tooltip · validate · hành vi khi thao tác* |

*Dạng B — sửa tính năng đã có:*

| Thay đổi | Section | Field | Validate |
| --- | --- | --- | --- |
| | | | |

**Business requirement — Business rule**

- `BR-1.1` *Rule nghiệp vụ, viết dạng khẳng định kiểm chứng được*
- `BR-1.2` *…*

*Rule chạm tới tính năng đang có → dẫn mã rule trong KB, ví dụ `BR-EDIT-07`, `KB-CLASS-03`.*

**Data Field**

*Field dữ liệu mới / bị đổi. Bỏ mục này nếu US không đụng tới dữ liệu.*

| Field | Kiểu | Bắt buộc | Giá trị hợp lệ | Ghi chú |
| --- | --- | --- | --- | --- |

**NFR**

*Hiệu năng, tải, bảo mật, tương thích. Không có → xoá.*

### 5/ Out of scope

*Những gì US này **không** làm, dù người đọc có thể tưởng là có.*

### 6/ Conner case

*Để trống — **QA điền**. PO/BA không viết mục này.*

---

## US2: <Tên user story>

*(Lặp đầy đủ cấu trúc US1: User story → Pre-Condition → Scenario → Acceptance criteria → Out of scope → Conner case)*

---

# Vấn đề tồn đọng

*Câu hỏi chưa có lời giải, quyết định còn treo, việc đẩy sang sprint sau.*

| # | Nội dung | Người trả lời | Chặn việc gì |
| --- | --- | --- | --- |

---

# Comments

*Trao đổi trong quá trình review.*
