# PO-Workflow

**Mục đích:** nhận yêu cầu, phân tích, sinh **PRD theo template công ty** làm đầu vào cho Design, Dev, QA, và viết **User Guide** sau khi phát triển xong. Repo này chỉ phân tích yêu cầu và viết tài liệu. Engine không phụ thuộc sản phẩm; sản phẩm nằm trong domain pack.

Quy tắc chi tiết nằm trong `.claude/protocol/` và từng command, không lặp lại ở đây. Tài liệu liên quan:

- [README.md](README.md): phương pháp, từng stage, mapping sang AWS AI-DLC
- [USER-GUIDE.md](USER-GUIDE.md): thao tác
- [GLOSSARY.md](GLOSSARY.md): thuật ngữ và họ mã
- [DOMAIN-SETUP.md](DOMAIN-SETUP.md): dựng quy trình cho một domain mới

## Luồng làm việc

Một luồng duy nhất theo AWS AI-DLC v2.10, mỗi yêu cầu là một intent trong `.claude/intents/`.

- Lệnh: `/new-intent` tạo, `/po` chạy stage kế tiếp, `/po-status` xem trạng thái, `/po-review` review độc lập
- Nghi thức ở `.claude/protocol/*.md`, thuật ngữ ở `GLOSSARY.md`, bài học ở `.claude/memory/team.md`
- Tên file artifact ổn định, version ở frontmatter, bản duyệt chụp vào `archive/` của intent theo `gate-protocol.md`; không tạo file `v0.x`
- Ba intent chuyển từ luồng cũ ngày 09/10/2026 (Group, Gamification, Report-Phase-1) giữ họ mã cũ trong tài liệu của chúng, ghi ở `intent.md` mỗi intent. Luồng cũ nằm ở tag `pre-aidlc`

## Domain đang cài

Mọi dữ kiện riêng của sản phẩm nằm trong domain pack `.claude/knowledge/domain/`: manifest `domain.md`, KB, corner checklist, template PRD và User Guide của công ty. Đọc `domain.md` ở đầu mỗi phiên và ở bước Load của mọi stage; command không ghi cứng dữ kiện sản phẩm. Domain đang cài: UpLnD của UpBase. Đổi domain theo [DOMAIN-SETUP.md](DOMAIN-SETUP.md).

## Knowledge

| Thư mục | Nội dung |
|---|---|
| `.claude/knowledge/domain/` | Domain pack. `domain.md` là manifest, chỉ KB nào trả lời câu gì, nguồn sống và bản chốt, dữ kiện cho từng stage, đích publish |
| `.claude/knowledge/product/` | Kiến thức vai PO chép từ AWS AI-DLC, không phụ thuộc sản phẩm; `corner-checklist-aws.md` là bản gốc để mỗi domain viết lại |
| `.claude/memory/team.md` | Bài học đã giữ lại tại gate, có ngày học. Đọc ở bước Load của mọi stage |

### Quy ước ký hiệu

| Ký hiệu | Nghĩa |
|---|---|
| `BR-<MODULE>-NN` | Business rule **có trong tài liệu chính thức**, giữ nguyên nguyên văn |
| `KB-<MODULE>-NN` | Claude trích từ văn xuôi, **chưa được duyệt** |
| `❓PO` | Chưa rõ, **không dùng làm fact** |
| `[suy ra]` | Claude suy luận, không phải câu chữ trực tiếp |
| **Hidden** | Tính năng **đã có code nhưng tạm ẩn**, vẫn phải xét khi phân tích ảnh hưởng |

### KB là bản chụp, biết khi nào phải đọc lại nguồn

Nguồn sống là nguồn còn bản gốc ở ngoài, như schema DB, API spec, tài liệu người dùng; yêu cầu chạm tới vùng đó thì đọc lại nguồn, không tin bản chép, và quá một tháng kể từ ngày đối chiếu cuối thì đọc lại trước khi dùng. Bản chốt là nguồn không còn file gốc; nghi ngờ thì hỏi PO, không tự suy. Danh sách nguồn và vùng KB chưa phủ nằm trong `domain.md` mục 2 và 3; vùng chưa phủ ghi `❓PO`, không kết luận "không ảnh hưởng". Đọc lại thấy khác KB thì cập nhật KB và sửa ngày đối chiếu ngay.

## Cách làm việc

- Trả lời **tiếng Việt**; tên stage, mã, thuật ngữ theo `GLOSSARY.md`.
- **Thẳng vào trọng tâm trước**, giải thích sau. **Phản biện khi có lỗ hổng thật.** **Hỏi lại khi thiếu thông tin**, không đoán bừa.
- Tách rõ `Fact` / `Assumption` / `Open Question` / `Recommendation`. **Không tự điền dữ kiện.** Thiếu nhẹ thì `Assumption`; thiếu ảnh hưởng phạm vi, rule, dữ liệu, luồng thì `Open Question`; ô không suy được thì `❓PO`.
- Không tự chốt quyết định thay PO; chỉ gợi ý dưới nhãn `Recommendation`. Lời duyệt và câu trả lời của PO ghi **nguyên văn**.
- **Không thiết kế kỹ thuật chi tiết.** Ghi *điều phải đúng*, để Dev quyết *cách làm*. Không hỏi câu kỹ thuật cho Dev; chỉ hỏi câu mà đáp án làm đổi phạm vi hoặc business rule. Cần biết một cơ chế kỹ thuật có tồn tại không thì hỏi PO; có endpoint không có nghĩa là có tính năng.
- **Tài liệu bàn giao** (Initiative Brief, HLD Brief, PRD, User Guide): không dấu vết quy trình, không viết tắt, mã nào cũng kèm nội dung, mã đứng cạnh nhau có dấu `·`. Trạng thái duyệt ghi ai duyệt, không ghi gate mấy. Giữ lại `❓PO` và bảng lịch sử phiên bản viết bằng tiếng người.
- **Trích mã trong trao đổi thì kèm nội dung** một dòng. Một intent cỡ L sinh hàng trăm mã, bắt người đọc mở file tra là lỗi của người viết.

Các quy tắc "đã sai một lần" và lý do của chúng nằm ở `.claude/memory/team.md`. Thêm bài học qua vòng học tại gate, không sửa tay giữa chừng một intent.

## Ranh giới

Repo này **chỉ làm phân tích yêu cầu và viết tài liệu**. Không bàn quy trình vận hành team, không đọc thư mục ngoài repo trừ thư mục nguồn ghi trong `domain.md` khi cập nhật KB, không tự mở rộng phạm vi KB.

Gặp điều đáng chú ý nhưng ngoài phạm vi thì ghi một dòng vào KB mục "câu hỏi để sau", rồi quay lại việc chính.

## Bàn giao

Đích publish tài liệu và đích User Guide ghi trong `domain.md` mục 4. Với domain đang cài: tài liệu lên Lark wiki, User Guide lên GitBook.
