---
domain: uplnd
product: UpLnD
company: UpBase
code: LMS
names: UpLnD, UpLMS, UpBase
jira_project_key: UPLND
jira_project_name: UpLnD
jira_project_type: software
updated: 2026-10-09
---
# Domain: UpLnD

File này là manifest của domain pack. Engine đọc nó ở đầu mỗi phiên và ở bước Load của mọi stage. Mọi dữ kiện riêng của sản phẩm nằm ở đây hoặc trong KB cùng thư mục, không nằm trong command. Đổi sang sản phẩm khác là thay cả thư mục `domain/`, xem `DOMAIN-SETUP.md`.

## 1. Sản phẩm và phạm vi

- Sản phẩm: UpLnD, gồm UpLMS cho người học và UpLMS Ops cho vận hành. Ngoài phạm vi: UpAcademy, Admin, Super Admin, xem `15-product-direction.md`
- Portal: UpLMS, UpLMS Ops. Mỗi intent ghi rõ chạm portal nào
- Tenant: tính năng làm cho UpBase, nhưng dữ liệu và hạ tầng thiết kế cho đa tenant ngay từ đầu. Mọi hằng số cứng phải khai báo là cứng hay cấu hình được. Bốn câu kiểm chiều tenant ở `15-product-direction.md` mục 6
- Vai người dùng hay gặp: học viên, mentor và mentor chính, nhân sự vận hành, L&D, quản lý trực tiếp, admin tenant
- Ngôn ngữ tài liệu: tiếng Việt, thuật ngữ sản phẩm giữ tiếng Anh
- Thiết bị và accessibility mặc định cho mọi intent: ❓PO. Ghi thiết bị hỗ trợ, ví dụ web máy tính và điện thoại, và mức accessibility, ví dụ WCAG 2.1 AA; 2.3 chỉ hỏi khi intent khác mặc định

## 2. Nguồn sống và bản chốt

| Nguồn | Loại | Ở đâu | Đối chiếu lần cuối | Phiên bản nguồn |
|---|---|---|---|---|
| User Guide, GitBook `uplms` và `uplms-ops` | sống | `LMS/User Guide/`, 57 page | 22/09/2026 | chưa ghi |
| Schema DB, 85 bảng, 173 quan hệ, chỉ có khoá chính và khoá ngoại | sống | [Lark Data Architecture](https://upbasevn.sg.larksuite.com/wiki/MaFpweI68iKNMvkTioLlJ1uJgQd) | 23/09/2026 | chưa ghi |
| Swagger LMS và Ops, 708 operation gồm 555 LMS và 153 Ops, 267 DTO | sống | `uplms-api.staging.upbase.asia/{lms\|ops}/api/v1/docs`, tên miền mới từ 05/10/2026; `components.schemas` là nguồn tốt nhất cho field | 05/10/2026 | 708 operation |
| 30 mail event và trạng thái bật tắt | chốt | `13-mail-events.md`, BA xác nhận ngày 23/09/2026 | không còn file gốc | không áp dụng |
| SIS | chốt | `11-dashboard-sis.md`, BA xác nhận ngày 23/09/2026 | không còn file gốc | không áp dụng |

Cột Phiên bản nguồn ghi dấu để biết nguồn đã đổi chưa mà không phải đọc lại cả nguồn: commit của repo tài liệu, số operation hoặc ngày build của API spec, ngày sửa của trang Lark. `po-tools.py status` và `doctor` cảnh báo nguồn sống quá 30 ngày chưa đối chiếu.

Nguồn sống: yêu cầu chạm tới vùng nào thì đọc lại nguồn vùng đó, quá một tháng kể từ lần đối chiếu cuối cũng đọc lại; đọc thấy khác KB thì sửa KB và ngày đối chiếu ngay. Bản chốt: nghi ngờ thì hỏi PO, không tự suy. Thư mục nguồn ngoài repo được phép đọc: `LMS/User Guide/`.

## 3. Bản đồ KB

| File | Trả lời câu gì | Stage dùng |
|---|---|---|
| `00-index.md` | mục lục, trạng thái tính năng kể cả Hidden, câu hỏi để sau | mọi stage |
| `01` đến `11` | nghiệp vụ theo module: Course, Question Bank, Assessment, Class, Grading, User, Learning Experience, Certificate, Notification, Storyline, Dashboard và SIS | 2.3, 2.31, 2.42 |
| `12-data-model.md` | 85 bảng, khoá ngoại, quan hệ | 2.31, 2.42 |
| `13-mail-events.md` | 30 mail tự động, mail nào đang bật hay tắt | 2.3, 2.31 |
| `14-api-surface.md` | 708 operation; mục 1 và 2 là vùng KB chưa phủ; mục 2.2 là endpoint có nhưng tính năng không có | 1.4, 2.3, 2.31 |
| `15-product-direction.md` | bốn portal, điểm đóng cứng UpBase, mục 6 bốn câu tenant | 1.1, 1.4, 2.31 |
| `16-domain-principles.md` | quan hệ chứa và ranh giới giữa các thực thể | 1.1, 2.3 |

Vùng KB chưa phủ: Ops có 25 nhóm API và LMS có 8 nhóm không có trong User Guide, gồm lịch dạy, phòng học, thi cử, phòng ban, phân quyền. KB chỉ phủ khoảng một nửa hệ thống; vùng chưa phủ ghi `❓PO`, không kết luận. 110 rule `KB-*` do AI trích, chưa duyệt. Mã trong KB: `BR-<MODULE>-NN` là rule có trong User Guide, `KB-<MODULE>-NN` là rule AI trích từ văn xuôi.

## 4. Dữ kiện cho từng stage

### 1.1 Intent Capture
Đọc `15-product-direction.md` và `16-domain-principles.md` để biết yêu cầu thuộc tầng nào, phục vụ riêng UpBase hay mọi tenant, có đụng nguyên tắc mô hình hoá nào. Hỏi portal theo mục 1.

### 1.2 Market Research
Sản phẩm so sánh mặc định: TalentLMS, Docebo, Moodle. Trang trợ giúp `help.talentlms.com` chặn tải tự động; lấy bài qua API Zendesk `https://help.talentlms.com/api/v2/help_center/en-us/articles/<id>.json` và lưu nguyên văn vào `inputs/`.

### 1.4 Scope Definition
Vùng chưa phủ: `14-api-surface.md` mục 1 và 2. Định hướng: `15-product-direction.md`.

### 2.3 Requirements Analysis
KB theo module `01` đến `11`; mail event `13`; data model `12` khi chạm dữ liệu. Ví dụ yêu cầu trùng thứ đã có trong domain này: "thêm thông báo khi chấm xong" trong khi mail số 19 đã tồn tại nhưng đang tắt. Góc hay sót: `corner-checklist.md` cùng thư mục.

### 2.31 Impact Analysis
- Shared entity dễ vỡ: `course_categories` là khoá ngoại của sáu bảng; Question Bank được bốn nơi tiêu thụ
- Hệ thông báo: 30 mail event ở `13`, có mail chạy bằng cronjob; gán hàng loạt sinh mail hàng loạt
- Phân quyền: Casbin, `06-user-account.md` mục 9, bảng `casbin_rule`
- Luồng tự sinh: lớp Foundation, `04-class.md`
- Tính năng Hidden: `00-index.md` mục Trạng thái
- Tenant: bốn câu ở `15-product-direction.md` mục 6

### 2.42 PRD Generation
Nguồn field: Swagger `components.schemas`, sau đó `12-data-model.md`, cuối cùng là KB theo module. Template PRD: template chuẩn `engine/templates/prd.md`, theo ADR 0004 ngày 20/10/2026; domain không có template PRD riêng. Template gốc của công ty giữ ở `templates/prd-template-goc-lark.md` để đối chiếu; ánh xạ tên mục cũ sang mới ở ADR 0004. PRD đã duyệt theo template cũ, như Gamification, giữ nguyên cho tới khi có change request.

### Publish
Lark wiki space `7660816820865093342`; node cha chung `02. Execution — Epics & Features`, token `X3hhwv2MxizpFgkVudVl7e52gUc`; mỗi intent một node con, tài liệu nằm trong node đó. Tên tài liệu: `[Brief]`, `[PRD]`, `[Decision Brief]` kèm tên tính năng. Công cụ: `lark-cli`, xem `/publish-lark`.

### User Guide
GitBook repo `uplms` cho học viên ở `LMS/User Guide/uplms/`, `uplms-ops` cho vận hành ở `LMS/User Guide/uplms-ops/`. Template: `templates/user-guide.md`. Ví dụ đổi giọng từ PRD sang User Guide: "Field `status` disable khi `class.type = Foundation`" thành "Không đổi được trạng thái với lớp Foundation"; "`BR-EDIT-06`: không xoá Test đã có attempt" thành "Không xoá được bài kiểm tra đã có học viên làm".

## 5. Ví dụ dùng trong engine
- Change request cần re-entry từ 2.3: "thêm rule học viên bị Block thì không nộp được bài" là rule mới nhưng mở một nhánh Impact Matrix chưa quét
- Câu trả lời nguyên văn kèm chữ cái: `A, "tính theo lượt ghi danh như SIS đang làm"`
- Góc hay sót của LMS: lớp đã kết thúc, học viên bị Block, một người thuộc nhiều nhóm, dữ liệu cũ trước ngày bật tính năng, mail gửi hàng loạt

## 6. Thành phần của domain pack
- `domain.md`, file này
- `00-index.md` đến `16-domain-principles.md`
- `corner-checklist.md`, viết lại từ `engine/knowledge/corner-checklist-aws.md`
- `templates/user-guide.md`, và `templates/prd-template-goc-lark.md` để đối chiếu

Ngoài pack nhưng thuộc về domain này, phải làm mới khi đổi domain: `memory/project.md` và `intents/`.
