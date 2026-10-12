# Dựng quy trình cho một domain mới

Tài liệu này cho người sở hữu quy trình, làm một lần khi đưa quy trình sang một sản phẩm hoặc công ty khác. PO dùng hằng ngày đọc [USER-GUIDE.md](USER-GUIDE.md); phương pháp đọc [README.md](README.md).

## 1. Hai tầng của repo

Engine là phần không phụ thuộc sản phẩm: protocol, command, template chung, checklist, agent, script, gói kiến thức vai PO từ AWS. Domain pack là mọi thứ riêng của sản phẩm và công ty, nằm trọn trong một thư mục:

```
.claude/knowledge/domain/
├── domain.md                      manifest: sản phẩm, nguồn, bản đồ KB, dữ kiện cho từng stage
├── 00-index.md … 16-*.md          knowledge base của sản phẩm
├── corner-checklist.md            góc hay sót, viết lại theo nghiệp vụ của domain
└── templates/
    ├── prd.md                     template PRD theo chuẩn công ty
    ├── user-guide.md              template User Guide theo chuẩn tài liệu của công ty
    └── prd-template-goc-lark.md   bản gốc của chủ template, để đối chiếu
```

Hai thứ nằm ngoài thư mục đó nhưng thuộc về domain, phải làm mới khi đổi: `.claude/memory/team.md` chứa bài học của team hiện tại, và `.claude/intents/` chứa việc của sản phẩm hiện tại.

Command và checklist không ghi cứng dữ kiện sản phẩm; chúng trỏ về `domain.md` theo mục. Vì vậy đổi domain không ảnh hưởng tới engine. Lệnh `/new-domain` dựng phần khung của các bước dưới đây; phần cần con người quyết vẫn do người làm.

## 2. Tạo space mới

Mỗi domain một repo, AWS gọi là một space. Không dựng domain mới trên repo đang có intent.

1. Clone repo này sang thư mục mới, đặt tên theo sản phẩm, ví dụ `po-workflow-crm`
2. Xoá mọi thư mục trong `.claude/intents/`, giữ `.gitkeep`
3. Đưa `.claude/memory/team.md` về bản trống: giữ đoạn mở đầu và các heading, xoá mọi dòng bài học, thêm một dòng ghi ngày khởi tạo domain
4. Xoá thư mục `.claude/knowledge/domain/`, trừ `templates/` giữ làm điểm xuất phát nếu công ty mới chưa có template riêng
5. Tạo remote mới, push nhánh `main`

## 3. Thu nguồn sống

Quy trình chỉ vận hành được khi KB bám vào nguồn thật. Trước khi viết KB, liệt kê nguồn và phân loại:

| Loại nguồn | Ví dụ | Xếp vào |
|---|---|---|
| Tài liệu người dùng cuối | user guide, help center, GitBook | nguồn sống nếu còn cập nhật |
| Cấu trúc dữ liệu | schema DB, ERD, data dictionary | nguồn sống |
| Đặc tả API | Swagger, OpenAPI, Postman | nguồn sống, là nguồn tốt nhất cho field |
| Bảng sự kiện, thông báo, mail | danh sách mail tự động, event | bản chốt nếu không còn file gốc |
| Rule nghiệp vụ truyền miệng | ghi từ PO, Dev | bản chốt, ghi rõ người cung cấp |

Mỗi nguồn ghi vào `domain.md` mục 2 với đường dẫn hoặc link, loại, ngày đối chiếu. Nguồn sống được đọc lại khi yêu cầu chạm tới vùng đó hoặc quá một tháng; bản chốt thì hỏi PO khi nghi ngờ.

## 4. Dựng KB cùng AI

KB là bản chắt lọc, không phải bản chép. Mỗi file trả lời một câu hỏi: có gì, ràng buộc gì, chạm vào đâu. Thứ tự và quy ước, giữ cho mọi domain để command tra được:

| File | Nội dung | Bắt buộc |
|---|---|---|
| `00-index.md` | mục lục, bảng nguồn, trạng thái tính năng kể cả Hidden, mục "câu hỏi để sau" | có |
| `01` đến `NN` | mỗi module nghiệp vụ một file: khái niệm, luồng chính, rule có mã, màn, dữ liệu | có |
| `data-model` | bảng, khoá ngoại, quan hệ, shared entity dễ vỡ | có |
| `events` hoặc `mail-events` | sự kiện, thông báo, mail tự động và trạng thái bật tắt | nếu sản phẩm có |
| `api-surface` | nhóm API, vùng chưa phủ, endpoint có nhưng tính năng không có | có |
| `product-direction` | portal, tenant, chỗ đóng cứng, hướng sản phẩm | có |
| `domain-principles` | cái gì được chứa cái gì, ranh giới thực thể | có |

Số thứ tự tự do; tên file ghi vào bản đồ KB trong `domain.md` mục 3, command tra theo bản đồ chứ không theo số.

Cách làm với AI, từng file một:

1. Đưa AI một nguồn và nói viết file KB nào. AI chắt lọc, mỗi rule một mã
2. Mã rule: `BR-<MODULE>-NN` khi rule có trong tài liệu chính thức, `KB-<MODULE>-NN` khi AI trích từ văn xuôi và chưa ai duyệt. Hai loại này khác nhau về độ tin cậy, không gộp
3. Điểm nguồn không đề cập thì ghi `❓PO`, không để AI tự điền
4. PO duyệt từng file; duyệt xong ghi ngày đối chiếu vào `00-index.md`
5. Ghi rõ vùng KB chưa phủ ngay trong `api-surface`, để Impact Analysis không kết luận "không ảnh hưởng" ở vùng chưa có thông tin

Để hình dung khối lượng: KB của UpLnD có 16 file, khoảng 27.700 từ, chắt từ 57 page user guide, 85 bảng và 708 operation, và vẫn chỉ phủ khoảng một nửa hệ thống.

## 5. Điền manifest

`domain.md` có sáu mục; `/new-domain` dựng khung và hỏi PO để điền:

1. Sản phẩm và phạm vi: tên, portal, ràng buộc tenant, vai người dùng
2. Nguồn sống và bản chốt
3. Bản đồ KB: file nào trả lời câu gì, dùng ở stage nào; vùng chưa phủ; quy ước mã
4. Dữ kiện cho từng stage: KB đọc ở 1.1 và 1.4; sản phẩm so sánh mặc định cho 1.2; KB và ví dụ cho 2.3; shared entity, hệ thông báo, phân quyền, luồng tự sinh, tenant cho 2.31; nguồn field và template PRD cho 2.42; đích publish; đích User Guide
5. Ví dụ dùng trong engine, để command giữ chung
6. Thành phần của pack

Mục 4 là phần quan trọng nhất: mỗi command đọc đúng mục của stage mình, nên thiếu mục nào thì stage đó chạy thiếu dữ kiện.

## 6. Viết lại corner checklist

Chép `.claude/knowledge/product/corner-checklist-aws.md` thành `domain/corner-checklist.md`, giữ phần "Cách dùng", thay toàn bộ "Điều kiện theo bề mặt" bằng góc của domain mới. Corner case nên đưa vào là loại từng gây lỗi thật hoặc chắc chắn sẽ gặp: trạng thái kết thúc, người dùng bị khoá, dữ liệu cũ trước ngày bật tính năng, thao tác hàng loạt, hai người làm cùng lúc. Stage 2.3 và 2.42 quét theo file này.

## 7. Template của công ty

Template PRD: giữ tên mục do chủ template công ty quyết, ghi rõ danh sách đó trong `domain.md` mục 4 phần 2.42 để stage không đổi; phần mục do repo quyết dùng thuật ngữ AWS như Technical Direction, Data to Retain, Proto-Units, Traceability, Open Issues. Giữ bản gốc của công ty cạnh bên để đối chiếu.

Template User Guide: theo cấu trúc tài liệu người dùng mà công ty đang dùng, như GitBook, Confluence, Notion. Đích publish ghi ở `domain.md` phần Publish; nếu không dùng Lark thì `/publish-lark` không áp dụng và cần một lệnh publish khác cho công cụ đó.

## 8. Chạy thử

1. `/new-intent` một yêu cầu nhỏ, profile S, đi tới PRD. Mục tiêu là kiểm tra command tra đúng KB và manifest, chưa cần PRD hoàn chỉnh
2. `python3 .claude/scripts/po-tools.py status` phải báo khớp
3. Một intent profile M có HLD Brief, để kiểm vòng ký của lead
4. Bài học đầu tiên ghi vào `team.md` qua câu hỏi tại gate

## 9. Checklist domain đã sẵn sàng

- [ ] `domain.md` đủ sáu mục, mục 4 có đủ các stage
- [ ] `00-index.md` có bảng nguồn kèm ngày đối chiếu và mục vùng chưa phủ
- [ ] Mỗi file KB đã được PO duyệt
- [ ] `corner-checklist.md` viết theo domain, không còn ví dụ của UpLnD
- [ ] `templates/prd.md` đúng tên mục của chủ template công ty
- [ ] `team.md` trống, `intents/` trống
- [ ] Không còn tên sản phẩm cũ trong engine: `grep -rn "UpLnD\|UpLMS\|UpBase" .claude/commands .claude/protocol .claude/templates .claude/verification .claude/agents CLAUDE.md` trả về rỗng
- [ ] Chạy thử một intent S tới PRD, `po-tools.py status` khớp
