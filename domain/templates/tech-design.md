---
intent: <slug>
artifact: tech-design
feature: <mã tính năng>
owner: <Tech PIC>
version: 0.1
status: draft
inputs: <prd@1.0>
---
# Tech Design: <Tên tính năng>

<Template của sản phẩm, ghi đè `engine/templates/tech-design.md` (thêm mục 0). Tech PIC viết từ PRD đã duyệt, trỏ về mã trong PRD.

Đây là **Technical Design 1**: bản sơ lược mô tả cấu trúc và làm rõ các vấn đề, đem đi họp 2.43 Design Alignment để chốt. Chưa phải thiết kế chi tiết — thiết kế chi tiết chạy sau buổi họp, ở các stage Tech 2.6 Domain Design, 2.7 Units Generation, 2.8 Contract Design, 3.1 Functional Design, 3.3 NFR Design.

Bắt buộc điền mục 0 trước khi trình họp: gate 2.43 và `/tech` đều đọc mục này. Xoá dòng hướng dẫn khi viết.>

## 0. PRD đã đủ để thiết kế chưa

**Kết luận: <ĐỦ | CHƯA ĐỦ>.** <Một câu: nếu chưa, thiếu nhóm nào.>

| # | Tiêu chí | Đạt | Ghi chú |
|---|---|---|---|
| R1 | Mọi US có Pre-condition, Scenario, Acceptance criteria | | |
| R2 | AC kiểm chứng được: có giá trị, điều kiện, kết quả cụ thể; không "phù hợp", "nhanh" | | |
| R3 | Business rule `BR` có mã, không mâu thuẫn nhau | | |
| R4 | Data to Retain đủ để suy ra entity: field, kiểu, bắt buộc, lịch sử | | |
| R5 | Quyền: ai được xem, sửa, cấu hình; Ops và học viên tách rõ | | |
| R6 | Trạng thái rỗng, lỗi, giới hạn (max, min, phân trang) có rule | | |
| R7 | Dữ liệu cũ và migration: ảnh hưởng tới dữ liệu đang có đã nói | | |
| R8 | NFR đo được: hiệu năng, thời gian thực hay trễ được, đa tenant | | |
| R9 | Design: mỗi US có UI có màn trong `design/` hoặc link Figma | | |
| R10 | Không còn `❓PO` hay Open Question chặn ở US thuộc đợt này | | |
| R11 | Truy vết FR ↔ US ↔ BR không GAP (`po-tools.py trace`) | | |

Mỗi tiêu chí không đạt là một dòng ở mục 7 *Ý kiến về PRD* (lập trường **Đề xuất sửa**, vị trí cụ thể: `US5 · AC bảng UI · field "Ngày tạo"`). Điểm chặn thiết kế ghi thêm ở mục 8 *Rủi ro và câu hỏi cần chốt*, cờ Chặn. Cả hai mục chảy vào Decision Brief để chốt trong buổi họp 2.43; không mở gate riêng và không sửa PRD ở đây. Mức mặc định: thiếu data, quyền, rule, luồng, trạng thái (R3–R7, R10) là Chặn; AC mơ hồ (R2) và NFR (R8) là Đề xuất sửa, trừ khi làm đổi data hoặc quyền thì Chặn; thiếu design (R9) là Đề xuất sửa, chỉ chặn ở bước UI Map; chữ nghĩa và trình bày là Ghi nhận. Lệch mặc định thì ghi lý do.

Câu kỹ thuật thuần (chọn thư viện, cấu trúc bảng) không hỏi PO: để lại cho 2.6 Domain Design.

## 1. Thành phần bị chạm
| Service hoặc repo | Thay đổi | US |
|---|---|---|

## 2. Quyết định kỹ thuật
<Mỗi quyết định: bối cảnh, phương án đã xét, chọn gì, hệ quả. Dạng ADR.>

## 3. Dữ liệu
<Entity mới hoặc đổi, quan hệ, migration dữ liệu cũ.>

## 4. API và hợp đồng giữa thành phần <!-- tuỳ chọn -->
<Endpoint mới hoặc đổi, sự kiện, hợp đồng với hệ ngoài.>

## 5. Đáp ứng business rule và NFR
| Mã | Cách đáp ứng | Ghi chú |
|---|---|---|

<Mỗi BR và NFR trong PRD một dòng.>

## 6. Unit of work, thứ tự và độ lớn
| Unit of work | Gồm US | Phụ thuộc | Độ lớn ước lượng |
|---|---|---|---|

<Story nào quá lớn để làm trong một sprint thì ghi ở đây, theo `engine/standards/story-splitting.md` mục 4.>

## 7. Ý kiến về PRD
| Mã | Lập trường | Nội dung | Lý do |
|---|---|---|---|

<Lập trường: Đồng ý, Đề xuất sửa, Phản đối. Không có ý kiến thì ghi một dòng "Đồng ý với PRD bản <version>".>

## 8. Rủi ro và câu hỏi cần chốt
| # | Nội dung | Cần ai trả lời | Chặn |
|---|---|---|---|
