# Memory: 261005-group
Nhật ký quan sát trong lúc làm. AI ghi, PO đọc tại gate. Mỗi dòng: thời gian, stage, một câu, hai câu ngữ cảnh. Dòng được giữ tại gate sẽ chuyển sang `memory/project.md`, và sang `memory/team.md` nếu PO xác nhận đúng cho mọi sản phẩm.

## Interpretations
- 2026-10-12T14:30 [1.1·1.4·1.7] "Chạy lại Group với po-workflow mới" được hiểu là review lại artifact đã migrate rồi trình gate theo nghi thức v2, không viết lại artifact. Ba cách hiểu khác nhau nhiều về khối lượng nên hỏi PO bằng hộp chọn trước; PO chọn cách này, theo tiền lệ Gamification cùng ngày.
- 2026-10-09T11:30 [CR1] Lời PO "tiếp tục" sau gate có khuyến nghị Request Changes được hiểu là chọn đúng khuyến nghị đó. PO đã hai lần trả lời bằng cách chấp nhận khuyến nghị; nếu muốn khác, lời trả lời sẽ nói rõ.
- 2026-10-09T10:00 [migration] BRD v1 được xem là artifact của cả ba stage 1.1, 1.4, 1.7; không tách thành intent-statement, scope-document, initiative-brief. Tách sẽ phải viết lại nội dung đã duyệt. Người đọc cần bản một trang thì chạy bổ sung 2.41 HLD Brief, nó phục vụ đúng việc đó.
- 2026-10-09T10:00 [migration] competitive-analysis v0.2 đánh dấu `[?]` dù là stage Ideation, vì §9.2 đang chờ PO đọc và có thể sinh CR cho PRD. Trạng thái chờ duyệt mô tả đúng việc đang treo.

## Deviations
- 2026-10-12T17:10 [2.41] Giới hạn 1.500 từ của checklist HLD Brief là đếm từ tiếng Anh theo AWS; tiếng Việt đếm âm tiết cho số cao hơn khoảng 1,4 lần. Với 20 US, 7 rủi ro và các bảng bắt buộc, bản tối giản nhất vẫn 1.887. PO chấp nhận; đề xuất ở vòng học: ghi giới hạn theo trang hoặc nhân hệ số cho tiếng Việt.
- 2026-10-12T16:05 [2.4] Reviewer chấm mục Conner case trống là Critical, nhưng template PRD của công ty ghi rõ mục đó để trống cho QA điền. Lỗi ở người điều phối: danh sách đường dẫn cho reviewer thiếu templates/prd.md, nên reviewer không biết quy ước. Lần sau review PRD hay US trong PRD thì đưa template vào danh sách đọc.
- 2026-10-09T11:00 [CR1] Lời PO "theo đề xuất, tiếp tục" được hiểu là duyệt 1.2 kèm chỉ thị và xác nhận luôn bảng ảnh hưởng đã trình ở gate, nên không trình lại impact preview trước khi sửa. Bảng ảnh hưởng đã nằm trong thông điệp gate, hỏi lại là hỏi hai lần.
- 2026-10-09T10:00 [migration] Giữ họ mã v1 (RC, OQ, BA, F, U, BR-x.y) thay vì đổi sang FR, PU, BR1.1 theo GLOSSARY. Đổi mã trên PRD đã publish sẽ làm lệch bản Lark và mọi tham chiếu trong Gamification, Report-Phase-1.

## Tradeoffs
- 2026-10-12T15:40 [2.4] Truy vết RC sang US làm tay và ghi inception/prd/traceability.md vì intent giữ họ mã v1, script trace không đọc được. Kiểm BR bằng máy riêng: 128 BR, mã đều trỏ US có thật. Lần sau intent mới dùng FR thì script làm thay.
- 2026-10-12T14:40 [1.7] Phase check Ideation chạy trên BRD v1 cho kết quả Không đạt ở điều kiện thẻ nguồn và Proto-Unit. Sửa cho đạt là viết lại BRD đã duyệt, nên đưa lên gate cho PO chọn chấp nhận rủi ro hay sửa, thay vì chặn gate theo chữ của template.
- 2026-10-09T10:00 [migration] Chụp archive cho bản đã duyệt từ nội dung hiện tại, không có bản chụp đúng thời điểm duyệt. BRD v0.1 lúc Gate 1 đã mất từ v1; archive chỉ bảo vệ từ hôm nay trở đi.

## Open questions
- 2026-10-12T15:40 [2.4] Bảng RC-01 đến RC-20 không có dòng cho US18 báo cáo cộng dồn, US19 tự gỡ khoá chưa học, US20 báo quản lý; ba US này sinh từ quyết định Bước 5 và Bước 7 của v1. Có nên thêm RC-21 đến RC-23 ở CR kế tiếp để bảng yêu cầu khớp 20 US, hay chấp nhận truy vết qua O4 và OQ?
- 2026-10-12T14:40 [1.4·1.7] BRD v0.2 chưa phản ánh CR1 (US16 ở Ops, MAIL-GRP-02, RC-20, §8 và §11 cũ). Sửa BRD tại chỗ bốn chỗ đó, hay để HLD Brief 2.41 làm bản tóm tắt hiện hành và BRD giữ nguyên làm mốc 06/10? PO quyết ở gate.
- 2026-10-09T10:00 [migration] Mục tên cũ trong PRD (Preferences, TDD, Dữ liệu phải lưu, Unit, Vấn đề tồn đọng) có đổi theo template v2 khi có CR kế tiếp không, hay giữ nguyên tới khi chủ template duyệt D8.
