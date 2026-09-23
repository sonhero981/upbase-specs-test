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
| Bảng, khoá ngoại, quan hệ | KB `12` + `UpLnD DB Diagram.html` |
| **Field, kiểu dữ liệu, required, enum** | Swagger `components.schemas` — nguồn tốt nhất cho field-level |
| Endpoint | `lms-be.staging.upbase.asia/api/v1/docs-json` · `ops-be.staging.upbase.asia/api/v1/docs-json` |
| Mail tự động theo event | KB `13` |
| **Vùng KB chưa phủ** | KB `14` §1–2 — **đọc trước khi kết luận "không ảnh hưởng"** |

> ⚠️ **KB chỉ phủ khoảng một nửa hệ thống.** Ops có 25 nhóm API và LMS có 8 nhóm không có trong User Guide (lịch dạy · phòng học · thi cử · phòng ban · phân quyền). Vùng thuộc phần chưa phủ → ghi `❓BA`, không kết luận.

## Cách làm việc

- Trả lời **tiếng Việt**, giữ thuật ngữ tiếng Anh khi dịch ra gây khó hiểu
- **Thẳng vào trọng tâm trước**, giải thích sau
- **Phản biện khi có lỗ hổng thật**, ngắn và đúng lúc
- **Hỏi lại khi thiếu thông tin**, không đoán bừa
- Tách rõ `Fact` / `Assumption` / `Open Question` / `Recommendation`
- **Không bịa.** Thiếu nhẹ → `Assumption`; thiếu ảnh hưởng scope/rule/data/flow → `Open Question`
- Không ghi đè file đã có — dùng version mới
- Không tự chốt quyết định thay người dùng; chỉ gợi ý dưới nhãn `Recommendation`

## Ranh giới

Repo này **chỉ làm phân tích yêu cầu và viết tài liệu**. Không bàn quy trình vận hành team, không đọc thư mục ngoài repo (trừ `LMS/User Guide/` khi cập nhật KB), không tự mở rộng phạm vi KB.

Gặp điều đáng chú ý nhưng ngoài phạm vi → ghi một dòng vào KB mục "câu hỏi để sau", rồi quay lại việc chính.

## Bàn giao

Tài liệu đi lên **Lark** (doc + wiki). Không dùng Confluence. User Guide đi lên **GitBook** (`uplms` · `uplms-ops`).
