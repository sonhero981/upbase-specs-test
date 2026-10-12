---
intent: <slug>
artifact: hld-brief
version: 0.1
status: draft
lark: <link bản cuối, điền sau sign-off>
---
# [HLD] <Tên tính năng>

| | |
|---|---|
| Owner | <PO> |
| Design lead | <tên> |
| Tech lead | <tên> |
| QA lead | <tên> |
| Họp | <ngày, hoặc "lead ghi vào repo tới ngày ..."> |

Tài liệu này tối đa ba trang. Mục 1 đọc trong một phút. Mục 8, 9, 10 do lead các team tự viết, trực tiếp trong file này trên repo; mỗi người chỉ sửa mục của mình và dòng của mình ở mục 12. AI chỉ viết PRD chi tiết sau khi mục 12 đủ chữ ký. Bản trên Lark là bản cuối sau khi ký.

Mục 1 đến 7 và 11 là bản tổng hợp từ artifact đã duyệt: muốn đổi nội dung thì sửa ở nguồn qua change request rồi tổng hợp lại, không sửa trực tiếp trong tài liệu này. Mục 8, 9, 10 là của lead; dòng in nghiêng đầu mỗi mục là gợi ý của AI, lead viết bên dưới.

## 1. Tóm tắt
<Mười dòng, mỗi dòng một ý: vấn đề · cho ai · mục tiêu đo được · phạm vi một câu · thay đổi lớn nhất trên hệ thống · rủi ro lớn nhất · phụ thuộc lớn nhất · thứ cần quyết hôm nay.>

## 2. Vấn đề và mục tiêu
<Vấn đề theo góc nhìn người dùng: ai gặp, khi nào, hậu quả. Số liệu nếu có.>

| Mục tiêu | Đo bằng |
|---|---|
| O1 <kết quả, không phải việc làm> | <chỉ số, nguồn số> |

## 3. Phạm vi
| In | Out | Để sau |
|---|---|---|
| | <kèm lý do một câu> | |

## 4. Giải pháp tổng thể
<Một sơ đồ Mermaid nếu luồng có nhiều cửa, kèm một dòng chú thích. Tối đa bảy gạch đầu dòng. Ràng buộc nghiệp vụ không được phá. Không có bảng dữ liệu, không có endpoint.>

## 5. User story theo nhóm bàn giao
| Proto-Unit | US | Tên | Ý chính | Ưu tiên |
|---|---|---|---|---|
| PU1 <tên nhóm> | US1 | <tên user story> | <một dòng: mục tiêu và luồng chính> | Must |

Thứ tự gợi ý: <PU1 rồi PU2>. Dev chốt thứ tự thật. Thẻ đầy đủ của từng US, gồm luồng chính, nhánh đáng kể, rule đã biết, dữ liệu chạm, ở `inception/user-stories/stories.md`; lead đọc thẻ trước khi ghi mục 8, 9, 10.

## 6. Ảnh hưởng tới hệ thống hiện có và rủi ro
| Vùng | Thay đổi | Mức |
|---|---|---|
| <module, màn, dữ liệu, mail, báo cáo> | <một dòng> | High / Medium / Low |

Migration và cutover: <một hai dòng, hoặc "không có">.

Rủi ro đã chấp nhận, giả định lớn chưa kiểm chứng, finding review còn treo, tối đa bảy dòng. Đây là điều kiện đi kèm quyết định, không phải việc để sau.

| # | Loại | Nội dung | Ai chấp nhận, ngày | Điều kiện kèm theo |
|---|---|---|---|---|
| 1 | Rủi ro chấp nhận · Giả định · Finding còn mở | | | <phải làm gì trước khi release, hoặc "không có"> |

## 7. Quyết định cần chốt
| # | Câu hỏi | Lựa chọn | Ai quyết | Hạn |
|---|---|---|---|---|

## 8. Design Direction
*Điểm cần lưu ý cho Design, AI gợi từ artifact đã duyệt, tối đa năm dòng: <màn mới hay sửa màn có sẵn · pattern đang dùng ở hệ · ràng buộc hiển thị bắt buộc · chỗ người dùng dễ nhầm>*

<Design lead viết theo khung dưới. Ý không áp dụng ghi "không áp dụng", không bỏ trống.>
- Luồng màn chính: <theo từng US hoặc Proto-Unit; màn mới hay sửa màn có sẵn>
- Pattern tái dùng: <thành phần, màn, quy ước đang có ở hệ sẽ dùng lại>
- Ràng buộc hiển thị: <điều bắt buộc phải thấy, phải không được làm>
- Cần nghiên cứu hoặc thử với người dùng: <màn, luồng, hoặc "không có">
- Cần PO quyết: <câu hỏi; chặn thì đưa vào mục 7>

## 9. Technical Direction
*Điểm cần lưu ý cho Tech, AI gợi từ Impact Matrix và constraints, tối đa năm dòng: <shared entity bị chạm · dữ liệu cũ và migration · hằng số cứng hay cấu hình · job nền, mail hàng loạt · điều không hoàn tác được>*

<Đây là HLD về kỹ thuật ở mức định hướng, đầu vào cho phần chi tiết của PRD. Tech lead viết theo khung dưới; ý không áp dụng ghi "không áp dụng", không bỏ trống.>
- Hướng tiếp cận: <làm theo cách nào, vì sao chọn so với hướng khác đã bàn ở Solution Options>
- Thành phần hiện có bị chạm: <module, service, bảng, job, mail; sửa hay thêm>
- Dữ liệu phải giữ lại: <thông tin nào phải lưu và vì sao, mức khái niệm, không thiết kế bảng>
- Điểm tích hợp và phụ thuộc kỹ thuật: <hệ ngoài, API bên thứ ba, thứ phải có trước>
- Ràng buộc và NFR mục tiêu: <hiệu năng, khối lượng, bảo mật, phân quyền, dữ liệu cũ và migration>
- Độ lớn và thứ tự từng Proto-Unit: <S, M, L tương đối; PU nào trước, vì sao>
- Dev tự quyết ở detailed design: <phần PRD để ngỏ cho Dev, không quy định>
- Cần PO quyết: <câu hỏi; chặn thì đưa vào mục 7>

## 10. Test Strategy
*Điểm cần lưu ý cho QA, AI gợi từ corner checklist và coverage gap, tối đa năm dòng: <góc đã thành rule · góc còn là giả định · vùng hồi quy · dữ liệu test cần có sẵn>*

<QA lead viết theo khung dưới. Ý không áp dụng ghi "không áp dụng", không bỏ trống.>
- Phạm vi test: <theo US hoặc Proto-Unit; mức test>
- Vùng hồi quy: <tính năng có sẵn phải kiểm lại, từ mục 6>
- Dữ liệu và môi trường test: <dữ liệu cần có sẵn, tài khoản, cấu hình>
- Tiêu chí vào và ra: <khi nào bắt đầu test, khi nào coi là xong>
- Góc cần PO chốt: <góc còn là giả định; chặn thì đưa vào mục 7>

## 11. Release và phụ thuộc
| Việc | Phụ thuộc | Mốc |
|---|---|---|

## 12. Sign-off
Trạng thái: **Đồng ý** là duyệt · **Có ý kiến** là duyệt kèm ghi chú đã viết ở mục của mình · **Yêu cầu sửa** là chưa duyệt, ghi rõ sửa gì ở cột Ghi chú · **Chưa xem**.

| Vai trò | Tên | Trạng thái | Ngày | Ghi chú |
|---|---|---|---|---|
| Product | | Đồng ý | | |
| Design | | Chưa xem / Có ý kiến / Đồng ý / Yêu cầu sửa | | |
| Dev | | Chưa xem / Có ý kiến / Đồng ý / Yêu cầu sửa | | |
| QA | | Chưa xem / Có ý kiến / Đồng ý / Yêu cầu sửa | | |
