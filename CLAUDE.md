# UpLnD PO/BA AI Workflow

**Mục đích:** nhận yêu cầu → phân tích → sinh tài liệu **PRD theo template công ty**, làm đầu vào cho Tester · UI/UX · Dev, và viết **User Guide** sau khi phát triển xong.

Hướng dẫn cho người dùng: [HUONG-DAN-SU-DUNG.md](HUONG-DAN-SU-DUNG.md) · Quy tắc chi tiết nằm trong từng command, không lặp lại ở đây.

## Phạm vi

Chỉ **UpLnD** = **UpLMS** (người học) + **UpLMS Ops** (vận hành).
Ngoài phạm vi: UpAcademy · Admin · Super Admin — xem `.claude/_shared-knowledge-base/15-product-direction.md`.

**Ràng buộc xuyên suốt:** tính năng làm cho UpBase, nhưng **dữ liệu và hạ tầng thiết kế cho đa tenant ngay từ đầu**. Mọi hằng số cứng phải khai báo rõ là hardcode hay cấu hình được.

## Knowledge Base

Đọc `.claude/_shared-knowledge-base/00-index.md` trước.

| Nhóm | File | Nội dung |
|---|---|---|
| Nghiệp vụ | `01`–`11` | Course · Question Bank · Assessment · Class · Grading · User · Learning Experience · Certificate · Notification · Storyline · Dashboard |
| Kỹ thuật | `12`–`14` | Data Model (85 bảng) · Mail Events (30 mail) · API Surface (708 operation) |
| Định hướng | `15` | UpLnD Platform, 4 portal, chỗ đóng cứng UpBase |

### Quy ước ký hiệu

| Ký hiệu | Nghĩa |
|---|---|
| `BR-COURSE-01` | Business rule **có sẵn trong User Guide** — giữ nguyên nguyên văn |
| `KB-COURSE-01` | Claude trích từ văn xuôi — **chưa được duyệt** |
| `❓BA` | Chưa rõ — **không dùng làm fact** |
| `[suy ra]` | Claude suy luận, không phải câu chữ trực tiếp |
| **Hidden** | Tính năng **đã có code nhưng tạm ẩn** — vẫn phải xét khi phân tích impact |

## Nguồn tra cứu

| Cần gì | Lấy ở đâu |
|---|---|
| Business rule, luồng nghiệp vụ | KB `01`–`11` |
| Bảng, khoá ngoại, quan hệ | KB `12` → nguồn gốc: [Lark `Data Architecture`](https://upbasevn.sg.larksuite.com/wiki/MaFpweI68iKNMvkTioLlJ1uJgQd) |
| **Field, kiểu dữ liệu, required, enum** | Swagger `components.schemas` — nguồn tốt nhất cho field-level |
| Endpoint | `lms-be.staging.upbase.asia/api/v1/docs-json` · `ops-be.staging.upbase.asia/api/v1/docs-json` |
| Mail tự động theo event | KB `13` — 📌 bản chốt, không còn file gốc |
| **Vùng KB chưa phủ** | KB `14` §1–2 — **đọc trước khi kết luận "không ảnh hưởng"** |

> ⚠️ **KB chỉ phủ khoảng một nửa hệ thống.** Ops có 25 nhóm API và LMS có 8 nhóm không có trong User Guide (lịch dạy · phòng học · thi cử · phòng ban · phân quyền). Vùng thuộc phần chưa phủ → ghi `❓BA`, không kết luận.

### KB là bản chụp — biết khi nào phải đọc lại nguồn

| Loại | Gồm | Quy tắc |
|---|---|---|
| 🔄 **Nguồn sống** | Schema DB (Lark) · Swagger staging · GitBook UG | Yêu cầu **chạm tới vùng đó** → đọc lại nguồn, không tin bản chép. Quá **1 tháng** kể từ "Đối chiếu lần cuối" → đọc lại trước khi dùng |
| 📌 **Bản chốt** | 30 mail event (KB `13`) · SIS | Không còn file gốc. Nghi ngờ → **hỏi người dùng**, không tự suy |

Đọc lại thấy **khác KB** → cập nhật KB và sửa ngày "Đối chiếu lần cuối" ngay, đừng dùng tạm rồi bỏ qua.

## Cách làm việc

- Trả lời **tiếng Việt**, giữ thuật ngữ tiếng Anh khi dịch ra gây khó hiểu
- **Thẳng vào trọng tâm trước**, giải thích sau
- **Phản biện khi có lỗ hổng thật**, ngắn và đúng lúc
- **Hỏi lại khi thiếu thông tin**, không đoán bừa
- Tách rõ `Fact` / `Assumption` / `Open Question` / `Recommendation`
- **Không bịa.** Thiếu nhẹ → `Assumption`; thiếu ảnh hưởng scope/rule/data/flow → `Open Question`
- Không ghi đè file đã có — dùng version mới
- Không tự chốt quyết định thay người dùng; chỉ gợi ý dưới nhãn `Recommendation`
- **Dừng ở mức phân tích, đừng lấn sang việc của Dev.** Cần biết một cơ chế kỹ thuật có tồn tại không → **hỏi PO xác nhận**, không tự đào Swagger/DB để kết luận. Bề mặt API **không** đồng nghĩa với tính năng đang chạy — có endpoint không có nghĩa là có tính năng (xem KB `14` §2.2)
- **Dọn dấu vết quy trình trước khi bàn giao.** Ký hiệu nội bộ (`9A`, `9C`, `Gate 3`, `Bước 5`), nhãn chờ (`🟡 chờ PO chốt`), ghi chú thay đổi (`🔄 Cấu trúc lại 23/09`, `Ban đầu tôi gộp…`) là **giàn giáo để làm việc, không phải nội dung**. Tài liệu bàn giao đọc bởi Dev, QA, Design — họ không tra được ký hiệu của workflow và không cần biết tôi đã sửa gì giữa chừng. Trạng thái duyệt thì ghi **ai duyệt**, không ghi *Gate mấy*.<br>Giữ lại: `❓BA` (ô trống thật, có người chịu trách nhiệm điền) và bảng lịch sử phiên bản viết bằng tiếng người.
- **Không viết tắt trong tài liệu bàn giao.** `Giải O2` phải là `Giải quyết mục tiêu O2`. Ô bảng chỉ chứa mã trần (`C10`, `S12`) phải kèm nội dung ngắn, vì người đọc trên Lark không cuộn ngược đi tra được. Viết tắt tiết kiệm được vài chữ nhưng bắt người đọc trả giá.
- **Mã đứng liền nhau phải có dấu phân cách.** `` `US1` `US6` `` render trên Lark thành `US1US6` dính liền. Dùng `` `US1` · `US6` ``.
- **Trích mã thì phải kèm nội dung.** Khi nhắc tới một mã trong trao đổi với người dùng — `OQ-29`, `BR-4.7`, `C5`, `US12`, `A17` — **luôn viết kèm nội dung của nó**, dù chỉ một dòng. Một dự án cỡ L sinh ra hàng trăm mã; không ai nhớ hết, và người dùng phải mở file tra là lỗi của người viết, không phải của người đọc.<br>Trong tài liệu thì mã đứng một mình được, vì người đọc tra ngay tại chỗ.

## Ranh giới

Repo này **chỉ làm phân tích yêu cầu và viết tài liệu**. Không bàn quy trình vận hành team, không đọc thư mục ngoài repo (trừ `LMS/User Guide/` khi cập nhật KB), không tự mở rộng phạm vi KB.

Gặp điều đáng chú ý nhưng ngoài phạm vi → ghi một dòng vào KB mục "câu hỏi để sau", rồi quay lại việc chính.

## Bàn giao

Tài liệu đi lên **Lark** (doc + wiki). Không dùng Confluence. User Guide đi lên **GitBook** (`uplms` · `uplms-ops`).
