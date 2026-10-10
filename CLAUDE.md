# UpLnD PO/BA AI Workflow

**Mục đích:** nhận yêu cầu, phân tích, sinh **PRD theo template công ty** làm đầu vào cho Design, Dev, QA, và viết **User Guide** sau khi phát triển xong. Repo này chỉ phân tích yêu cầu và viết tài liệu.

Phương pháp và mapping sang AWS AI-DLC: [README.md](README.md) · Thao tác: [USER-GUIDE.md](USER-GUIDE.md) · Thuật ngữ và họ mã: [GLOSSARY.md](GLOSSARY.md). Quy tắc chi tiết nằm trong `.claude/protocol/` và từng command, không lặp lại ở đây.

## Luồng làm việc

Một luồng duy nhất theo AWS AI-DLC v2.10, mỗi yêu cầu là một intent trong `.claude/intents/`: `/new-intent` tạo, `/po` chạy stage kế tiếp, `/po-status` xem trạng thái, `/po-review` review độc lập. Nghi thức ở `.claude/protocol/*.md`, thuật ngữ ở `GLOSSARY.md`, bài học ở `.claude/memory/team.md`. Tên file artifact ổn định, version ở frontmatter, bản duyệt chụp vào `archive/` của intent theo `gate-protocol.md`; không tạo file `v0.x`. Ba intent chuyển từ luồng cũ ngày 09/10/2026 (Group, Gamification, Report-Phase-1) giữ họ mã cũ trong tài liệu của chúng, ghi ở `intent.md` mỗi intent. Luồng cũ nằm ở tag `pre-aidlc`.

## Phạm vi

Chỉ **UpLnD** = **UpLMS** (người học) + **UpLMS Ops** (vận hành). Ngoài phạm vi: UpAcademy, Admin, Super Admin, xem `.claude/knowledge/domain/15-product-direction.md`.

**Ràng buộc xuyên suốt:** tính năng làm cho UpBase, nhưng **dữ liệu và hạ tầng thiết kế cho đa tenant ngay từ đầu**. Mọi hằng số cứng phải khai báo rõ là hardcode hay cấu hình được.

## Knowledge

| Thư mục | Nội dung |
|---|---|
| `.claude/knowledge/domain/` | KB sản phẩm, 16 file. Đọc `00-index.md` trước. `01` đến `11` nghiệp vụ · `12` đến `14` data model 85 bảng, 30 mail event, 708 API operation · `15` định hướng, 4 portal, chỗ đóng cứng UpBase · `16` nguyên tắc mô hình hoá, đọc trước khi thiết kế thực thể mới |
| `.claude/knowledge/product/` | Kiến thức vai PO chép từ AWS AI-DLC; `corner-checklist.md` viết lại cho LMS. Command của stage ghi file nào cần đọc |
| `.claude/memory/team.md` | Bài học đã giữ lại tại gate, có ngày học. Đọc ở bước Load của mọi stage |

### Quy ước ký hiệu

| Ký hiệu | Nghĩa |
|---|---|
| `BR-COURSE-01` | Business rule **có sẵn trong User Guide**, giữ nguyên nguyên văn |
| `KB-COURSE-01` | Claude trích từ văn xuôi, **chưa được duyệt** |
| `❓BA` | Chưa rõ, **không dùng làm fact** |
| `[suy ra]` | Claude suy luận, không phải câu chữ trực tiếp |
| **Hidden** | Tính năng **đã có code nhưng tạm ẩn**, vẫn phải xét khi phân tích ảnh hưởng |

## Nguồn tra cứu

| Cần gì | Lấy ở đâu |
|---|---|
| Business rule, luồng nghiệp vụ | KB `01` đến `11` |
| Bảng, khoá ngoại, quan hệ | KB `12`, nguồn gốc: [Lark `Data Architecture`](https://upbasevn.sg.larksuite.com/wiki/MaFpweI68iKNMvkTioLlJ1uJgQd) |
| **Field, kiểu dữ liệu, required, enum** | Swagger `components.schemas`, nguồn tốt nhất cho field |
| Endpoint | `lms-be.staging.upbase.asia/api/v1/docs-json` · `ops-be.staging.upbase.asia/api/v1/docs-json` |
| Mail tự động theo event | KB `13`, 📌 bản chốt, không còn file gốc |
| **Vùng KB chưa phủ** | KB `14` §1 và §2, **đọc trước khi kết luận "không ảnh hưởng"** |

> ⚠️ **KB chỉ phủ khoảng một nửa hệ thống.** Ops có 25 nhóm API và LMS có 8 nhóm không có trong User Guide (lịch dạy, phòng học, thi cử, phòng ban, phân quyền). Vùng thuộc phần chưa phủ ghi `❓BA`, không kết luận.

### KB là bản chụp, biết khi nào phải đọc lại nguồn

| Loại | Gồm | Quy tắc |
|---|---|---|
| 🔄 **Nguồn sống** | Schema DB (Lark) · Swagger staging · GitBook UG | Yêu cầu **chạm tới vùng đó** thì đọc lại nguồn, không tin bản chép. Quá **1 tháng** kể từ "Đối chiếu lần cuối" thì đọc lại trước khi dùng |
| 📌 **Bản chốt** | 30 mail event (KB `13`) · SIS | Không còn file gốc. Nghi ngờ thì **hỏi PO**, không tự suy |

Đọc lại thấy **khác KB** thì cập nhật KB và sửa ngày "Đối chiếu lần cuối" ngay, đừng dùng tạm rồi bỏ qua.

## Cách làm việc

- Trả lời **tiếng Việt**; tên stage, mã, thuật ngữ theo `GLOSSARY.md`.
- **Thẳng vào trọng tâm trước**, giải thích sau. **Phản biện khi có lỗ hổng thật.** **Hỏi lại khi thiếu thông tin**, không đoán bừa.
- Tách rõ `Fact` / `Assumption` / `Open Question` / `Recommendation`. **Không bịa.** Thiếu nhẹ thì `Assumption`; thiếu ảnh hưởng phạm vi, rule, dữ liệu, luồng thì `Open Question`; ô không suy được thì `❓BA`.
- Không tự chốt quyết định thay PO; chỉ gợi ý dưới nhãn `Recommendation`. Lời duyệt và câu trả lời của PO ghi **nguyên văn**.
- **Không thiết kế kỹ thuật chi tiết.** Ghi *cái gì phải đúng*, để Dev quyết *làm thế nào*. Không hỏi câu kỹ thuật cho Dev; chỉ hỏi câu mà đáp án làm đổi phạm vi hoặc business rule. Cần biết một cơ chế kỹ thuật có tồn tại không thì hỏi PO; có endpoint không có nghĩa là có tính năng.
- **Tài liệu bàn giao** (Initiative Brief, HLD Brief, PRD, User Guide): không dấu vết quy trình, không viết tắt, mã nào cũng kèm nội dung, mã đứng cạnh nhau có dấu `·`. Trạng thái duyệt ghi ai duyệt, không ghi gate mấy. Giữ lại `❓BA` và bảng lịch sử phiên bản viết bằng tiếng người.
- **Trích mã trong trao đổi thì kèm nội dung** một dòng. Một intent cỡ L sinh hàng trăm mã, bắt người đọc mở file tra là lỗi của người viết.

Các quy tắc "đã sai một lần" và lý do của chúng nằm ở `.claude/memory/team.md`. Thêm bài học qua vòng học tại gate, không sửa tay giữa chừng một intent.

## Ranh giới

Phần PO của repo **chỉ làm phân tích yêu cầu và viết tài liệu**. Không bàn quy trình vận hành team, không đọc thư mục ngoài repo (trừ `LMS/User Guide/` khi cập nhật KB), không tự mở rộng phạm vi KB.

Gặp điều đáng chú ý nhưng ngoài phạm vi thì ghi một dòng vào KB mục "câu hỏi để sau", rồi quay lại việc chính.

## Bàn giao

Tài liệu đi lên **Lark** (doc + wiki). Không dùng Confluence. User Guide đi lên **GitBook** (`uplms` · `uplms-ops`).

## Phần Tech (OpenSpec store)

Thư mục `openspec/` là store OpenSpec `upbase-specs` của đội Tech: change cross-repo (lms-be, lms-fe, ops-fe, lms-package) lập từ intent đã duyệt. Lệnh `/opsx:*`; config `openspec/config.yaml`; bản đồ repo và owner `.claude/knowledge/tech/system-map.md`; cách đọc intent `.claude/knowledge/tech/intent-handoff.md`. Luật PO ở trên không áp cho `openspec/`; Tech không sửa `.claude/intents/**` trừ mục 9 và dòng Dev mục 12 của `hld-brief.md`.
