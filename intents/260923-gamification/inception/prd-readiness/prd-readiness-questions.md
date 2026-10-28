# PRD Readiness, câu hỏi
Intent: 260923-gamification · Cách trả lời: Chat · Đã trả lời: Lô 1 4/4 (giả lập PO, test workflow) · Lô 2 13/13

Câu hỏi từ đội Tech sau khi kiểm PRD Gamification v0.14, phạm vi đợt này US14 (hai công tắc) và US15 (phân quyền cấu hình). Q1–Q4 ứng với finding RD1, RD2, RD3, RD6 trong `prd-readiness.md`. Q1, Q2 chặn việc viết thiết kế. Trả lời xong, chạy `/change-request` để đưa vào PRD.

## Lô 1

## Q1. Người chỉ có quyền "Xem danh sách học viên và hạng" mở danh sách campaign và kết quả campaign từ đâu?
Vì sao hỏi: bảng quyền bên Ops (BR-15.7) cho quyền này xem danh sách và kết quả campaign, nhưng danh sách campaign là khối cuối của trang cấu hình, và cùng bảng nói quyền này không xem được trang cấu hình (RD1). Đáp án quyết định menu, đường dẫn và cách chặn quyền bên Ops.
A. Quyền này vào được trang cấu hình nhưng chỉ thấy khối Campaign ở chế độ chỉ xem, các khối khác ẩn  [đề xuất, giữ design hiện có và dùng lại chế độ chỉ xem của khối Campaign ở BR-15.8]
B. Tách danh sách campaign thành một mục riêng trong menu Gamification; trang cấu hình chỉ cho quyền xem và sửa cấu hình
C. Quyền này không thấy danh sách campaign; kết quả campaign mở từ màn danh sách học viên (US12)
X. Khác, xin nói rõ
Chặn: có
[Answer]: [GIẢ LẬP PO] A, "Giữ một trang như design. Người chỉ có quyền xem danh sách học viên và hạng vào trang Gamification thì chỉ thấy khối Campaign ở chế độ chỉ xem, mở được kết quả campaign. Menu vẫn hiện khu vực Gamification cho họ theo BR-15.3."

## Q2. "Bật hiển thị cho học viên lần đầu" (popover xác nhận của US14) tính theo cách nào?
Vì sao hỏi: BR-14.13 bắt hỏi lại khi bật `Visibility in UpLMS` lần đầu vì đó là thời điểm ra mắt. Nếu "lần đầu" là một lần trong đời tổ chức thì hệ thống phải lưu thêm mốc đã từng bật (RD2).
A. Một lần trong đời tổ chức: đã bật một lần thì các lần bật lại sau không hỏi  [đề xuất, theo BR-14.13 "gần như chỉ xảy ra một lần trong vòng đời tính năng"]
B. Lần nào bật lại từ trạng thái tắt cũng hỏi
C. Lần đầu sau mỗi lần bật lại `Gamification`
X. Khác, xin nói rõ
Chặn: có
[Answer]: [GIẢ LẬP PO] A, "Một lần trong đời tổ chức. Đã ra mắt rồi thì bật lại không hỏi nữa."

## Q3. Tắt hoặc bật `Gamification` thì sau bao lâu hệ thống phải ngừng hoặc bắt đầu ghi nhận?
Vì sao hỏi: NFR của US14 yêu cầu giữ hai công tắc trong bộ nhớ; không nói thời gian có hiệu lực thì thao tác học xảy ra ngay sau khi tắt có thể vẫn được ghi, trái BR-14.5 "tính từ thời điểm bật" (RD3).
A. Ngay khi lưu xong: thao tác học xảy ra sau đó theo trạng thái mới  [đề xuất, theo BR-14.5; technical design của PRD đã có bước xoá cache sau khi lưu]
B. Chấp nhận trễ tối đa 1 phút
X. Khác, xin nói rõ
Chặn: không
[Answer]: [GIẢ LẬP PO] A, "Ngay khi lưu xong. Thao tác học sau thời điểm lưu theo trạng thái mới."

## Q4. Tổ chức đang chạy lúc lên bản có Gamification ở trạng thái nào?
Vì sao hỏi: BR-14.6 chỉ nói tổ chức mới khởi tạo thì tắt hẳn; tổ chức hiện có cũng cần một giá trị ban đầu khi lên bản (RD6).
A. Tắt hẳn, vận hành tự bật khi sẵn sàng  [đề xuất, theo BR-14.6 và cách dùng "chạy ngầm trước khi mở" ở Scenario US14]
B. Chạy ngầm ngay khi lên bản
X. Khác, xin nói rõ
Chặn: không
[Answer]: [GIẢ LẬP PO] A, "Tắt hẳn. Vận hành tự bật chạy ngầm khi sẵn sàng."

## Việc PO cần bổ sung
- Chuỗi tiếng Anh của hai popover xác nhận: tắt `Gamification`, bật `Visibility in UpLMS` lần đầu (`OQ-50`).
- Design hai popover và báo `Saved` trên trang cấu hình.
- Design hoặc câu chữ khi người không có quyền mở thẳng đường dẫn khu vực Gamification bên Ops (US15).
- Sửa AC "Menu Ops · Khu vực Gamification" của US15 cho khớp BR-15.3: "không có quyền nào trong ba quyền" (RD5).
- Điền metadata `Tech lead`, `QA` (`OQ-10`).

PO bổ sung (giả lập, trả lời mục "Việc PO cần bổ sung"):
- Chuỗi popover tắt `Gamification`: tiêu đề `Turn off gamification?` · nội dung `Points, badges and levels stop being recorded and all four features are locked. Existing data is kept. Turning it back on starts recording from that moment, nothing is backfilled.` · nút `Turn off` / `Cancel`.
- Chuỗi popover bật `Visibility in UpLMS` lần đầu: tiêu đề `Show gamification to your users?` · nội dung `They will immediately see all points, badges and levels earned so far. No notifications are sent for past achievements.` · nút `Show` / `Cancel`.
- Popover và báo `Saved`: dùng component chuẩn của Ops, không cần design riêng.
- Mở thẳng đường dẫn khi không có quyền: dùng màn 403 hiện có của Ops.
- AC menu US15 và metadata `Tech lead` = Nguyễn Hùng Sơn, `QA` = chưa có: sửa trong CR kế tiếp.

## Consolidated Summary
- Q1: quyền `Xem danh sách học viên và hạng` mở trang Gamification, chỉ thấy khối Campaign chỉ xem; menu hiện theo BR-15.3.
- Q2: popover bật hiển thị chỉ hỏi một lần trong đời tổ chức → lưu mốc đã từng bật hiển thị.
- Q3: công tắc có hiệu lực ngay khi lưu xong.
- Q4: tổ chức đang chạy lúc lên bản ở trạng thái tắt hẳn.
- Chuỗi hai popover như trên; popover, `Saved`, 403 dùng chuẩn Ops.

Xác nhận: [GIẢ LẬP PO] Looks correct. Chưa chạy `/change-request`; PRD vẫn v0.14 (DEC-T4).

## Lô 2 — mở rộng phạm vi cả intent (2026-10-13, DEC-T15)
Cách trả lời: Chat · Đã trả lời: 13/13 (giả lập PO, test workflow)

Đội Tech đã mở rộng phạm vi sang 17 US còn lại (US1–US13, US19–US22). Q5–Q9 chặn việc viết thiết kế (finding RD9–RD13). Q10–Q17 không chặn, Tech tạm dùng phương án `[đề xuất]`. Trả lời xong, chạy `/change-request` để đưa vào PRD (gộp cùng Q1–Q4).

## Q5. Tiêu chí lên hạng theo huy hiệu đếm huy hiệu thế nào khi một loại bị tắt rồi bật lại?
Vì sao hỏi: `BR-9.10` chỉ đếm huy hiệu thuộc loại đang bật, nên tắt một loại làm số huy hiệu giảm, bật lại làm tăng. Ghi chú `[đề xuất]` nói mỗi huy hiệu chỉ góp một lần cho tiêu chí lên hạng. Nếu chốt như vậy, hệ thống phải lưu thêm một bộ đếm riêng (RD9).
A. Mỗi huy hiệu chỉ góp một lần: tiêu chí lên hạng dùng bộ đếm riêng, chỉ tăng khi học viên nhận huy hiệu mới (kể cả huy hiệu trao bù lần đầu), tắt / bật loại không làm bộ đếm thay đổi  [đề xuất, theo ghi chú BR-9.10, tránh lên hạng hai lần từ cùng một huy hiệu]
B. Đếm theo số huy hiệu của loại đang bật: bật lại một loại có thể làm học viên chạm mốc và lên hạng thêm lần nữa
X. Khác, xin nói rõ
Chặn: có
[Answer]: [GIẢ LẬP PO] A, "Mỗi huy hiệu chỉ góp một lần. Tắt bật loại không làm ai lên hạng lại."

## Q6. Bảng `Courses` của campaign luôn có, hay tuỳ chọn như `Activities`?
Vì sao hỏi: PO đã chọn "Courses luôn có" (`BR-19.3a`), nhưng cột `Contribution` trong design danh sách campaign có dòng không có `Course` (`OQ-49`). Đáp án quyết định campaign có thêm cờ dữ liệu và form có thêm ô chọn hay không (RD10).
A. Luôn có, không có ô chọn; sửa design cột `Contribution` cho mọi dòng đều có `Course`  [đề xuất, theo quyết định PO ngày 12/10 ở BR-19.3a]
B. Tuỳ chọn: thêm ô `Course` cạnh ô `Activity`, mặc định bật
X. Khác, xin nói rõ
Chặn: có
[Answer]: [GIẢ LẬP PO] A, "Courses luôn có. Design sửa cột Contribution."

## Q7. Tắt `Gamification` khi đang có campaign chạy thì có cho tắt không?
Vì sao hỏi: `BR-20.8` đề xuất cho tắt, popover nêu thêm số campaign đang chạy, và campaign không nhận gì trong thời gian tắt (`OQ-42`). PRD ghi câu này phải trả lời trước khi bàn giao Unit Campaign (RD11).
A. Cho tắt. Popover tắt nêu thêm số campaign đang chạy; trong thời gian tắt, campaign không nhận thêm điểm, hoạt động, khoá  [đề xuất, theo BR-20.8; campaign đang chạy không dừng được và nhiều campaign chạy chồng nhau]
B. Không cho tắt khi còn campaign đang chạy; phải chờ mọi campaign kết thúc
X. Khác, xin nói rõ
Chặn: có
[Answer]: [GIẢ LẬP PO] A, "Cho tắt, popover nêu số campaign đang chạy. Thời gian tắt campaign không nhận gì."

## Q8. Lần ghi nhận lại sau lỗi tới muộn, sau khi campaign đã đóng băng, thì xử lý thế nào?
Vì sao hỏi: `BR-13.8` đề xuất lần ghi lại mang thời điểm hoàn thành gốc. Nếu lần ghi lại tới sau lúc campaign đóng băng mà thời điểm gốc nằm trong khoảng campaign, sổ điểm và kết quả đã công bố lệch nhau, trong khi `BR-21.1` cấm tính lại (RD12).
A. Tác vụ đóng băng chạy sau khi campaign kết thúc một khoảng chờ cố định (ví dụ 24 giờ) để các lần ghi lại kịp vào; lần ghi lại tới sau lúc đóng băng vẫn vào sổ điểm, lịch sử, bảng xếp hạng chung, nhưng không đổi kết quả campaign  [đề xuất, giữ C11 cho gần như mọi trường hợp và giữ BR-21.1 kết quả không đổi]
B. Đóng băng đúng lúc kết thúc; lần ghi lại tới sau không đổi kết quả campaign
C. Lần ghi lại mang thời điểm ghi lại (không phải thời điểm gốc), nên không bao giờ rơi vào campaign đã kết thúc
X. Khác, xin nói rõ
Chặn: có
[Answer]: [GIẢ LẬP PO] A, "Đóng băng sau khi kết thúc 24 giờ. Ghi lại tới sau đó thì không đổi kết quả campaign."

## Q9. Vận hành thấy các lần cộng điểm bị lỗi ở đâu?
Vì sao hỏi: `BR-13.8` bắt ghi lại lần lỗi để không mất âm thầm, nhưng không có màn nào hiện, và nhật ký US22 đã loại (`OQ-46`). Đáp án quyết định có thêm màn và API bên Ops hay không (RD13).
A. Không có màn cho vận hành ở đợt này: hệ thống tự ghi lại, lỗi còn lại sau số lần thử tối đa thì báo cho đội kỹ thuật qua log và cảnh báo  [đề xuất, theo A12 vận hành không cộng bù tay, nên màn chỉ để xem cũng không giúp vận hành làm gì]
B. Thêm một bộ lọc "Lỗi" trong nhật ký ghi nhận US22
C. Thêm một màn riêng trong khu vực Gamification bên Ops
X. Khác, xin nói rõ
Chặn: có
[Answer]: [GIẢ LẬP PO] A, "Đợt này không có màn. Tự ghi lại, còn lỗi thì báo đội kỹ thuật."

## Q10. Thông báo thành tích tự tắt sau bao lâu?
Vì sao hỏi: US2 còn `❓PO` (`OQ-53`), cần tính khi bốn, năm thẻ hiện cùng lúc (RD14).
A. Mỗi thẻ 5 giây, đếm riêng từng thẻ; hiện tối đa 4 thẻ, thẻ thứ 5 đẩy thẻ cũ nhất ra; trỏ chuột vào thì dừng đếm  [đề xuất]
B. Mỗi thẻ 8 giây, không giới hạn số thẻ
X. Khác, xin nói rõ
Chặn: không
[Answer]: [GIẢ LẬP PO] A

## Q11. Lịch sử ghi nhận của học viên tải bao nhiêu mục mỗi lần?
Vì sao hỏi: US3 còn `❓PO` (`OQ-19`) (RD14).
A. 20 mục mỗi lần, cuộn tới cuối thì tải tiếp  [đề xuất]
B. 50 mục mỗi lần
X. Khác, xin nói rõ
Chặn: không
[Answer]: [GIẢ LẬP PO] A

## Q12. Ảnh huy hiệu vận hành tải lên giới hạn thế nào?
Vì sao hỏi: US9 còn `❓PO` (`OQ-51`) (RD14).
A. Theo giới hạn hiện có của kho tài nguyên Ops; khuyến nghị ảnh vuông PNG hoặc SVG, hiển thị ở 96×96  [đề xuất, dùng lại kho tài nguyên theo BR-1.7]
B. Chỉ PNG / SVG, tối đa 1 MB, tối thiểu 256×256
X. Khác, xin nói rõ
Chặn: không
[Answer]: [GIẢ LẬP PO] A

## Q13. Tên campaign dài tối đa bao nhiêu ký tự?
Vì sao hỏi: US20 còn `❓PO` (`OQ-52`) (RD14).
A. 100 ký tự  [đề xuất]
B. 255 ký tự
X. Khác, xin nói rõ
Chặn: không
[Answer]: [GIẢ LẬP PO] A

## Q14. Các con số NFR nào áp cho gamification?
Vì sao hỏi: NFR của US2, US13, US12, US22 nói "không làm chậm", "nhanh" nhưng chưa có con số; xuất Excel ở US12, US21 chưa có giới hạn dòng (RD15).
A. Thông báo hiện trong 3 giây sau thao tác; gamification cộng thêm không quá 200 ms vào thao tác hoàn thành; US12, US22 trả một trang trong 2 giây với 10.000 học viên và 5 triệu dòng nhật ký; xuất Excel tối đa 50.000 dòng  [đề xuất]
B. Không đặt con số; Dev tự đặt và báo lại
X. Khác, xin nói rõ
Chặn: không
[Answer]: [GIẢ LẬP PO] A, "Đồng ý các con số này làm mục tiêu."

## Q15. Giá trị mặc định khi khởi tạo cấu hình lấy theo đâu?
Vì sao hỏi: PRD chỉ có điểm nền check-in `10`. Design trang cấu hình có thêm hoạt động `10`, khoá `150`, bài Test `25`, lên hạng mỗi `3000` điểm / `5` khoá / `5` huy hiệu, trần `100`, và tên + hình 8 mốc Check-in (RD16).
A. Theo design như trên; ba loại huy hiệu còn lại đặt tên theo cùng mẫu (`Activity Newbie` … `Activity Grandmaster`), hình do design cung cấp  [đề xuất]
B. PO gửi bảng giá trị mặc định riêng
X. Khác, xin nói rõ
Chặn: không
[Answer]: [GIẢ LẬP PO] A, "Theo design; ba loại còn lại đặt tên cùng mẫu, hình design gửi sau."

## Q16. Bảng xem trước dưới khối Leaderboard của trang cấu hình hiện gì?
Vì sao hỏi: design có bảng xem trước (năm tab, dòng `You`, bộ chọn khoảng ngày) nhưng US11 không có AC; `OQ-45` chỉ nói bỏ bộ chọn khoảng ngày (RD17).
A. Giữ bảng xem trước: các bảng `All time` theo công tắc `Show …` đang bật, số đã tính sẵn như học viên thấy, không có dòng `You`, không chọn khung  [đề xuất]
B. Bỏ bảng xem trước; vận hành xem số liệu ở US12
X. Khác, xin nói rõ
Chặn: không
[Answer]: [GIẢ LẬP PO] A, "Giữ bảng xem trước, chỉ All time, không có dòng You."

## Q17. Các dòng `[đề xuất]` trong 17 US (`OQ-43`) có giữ như PRD viết không?
Vì sao hỏi: Tech đang dùng đúng như PRD viết làm giả định (A6) để không chặn thiết kế (RD20).
A. Giữ toàn bộ như PRD viết; dòng nào PO đổi thì ghi ở `/change-request`  [đề xuất]
B. PO duyệt từng dòng trước khi Tech thiết kế
X. Khác, xin nói rõ
Chặn: không
[Answer]: [GIẢ LẬP PO] A, "Giữ như PRD viết."

## Việc PO cần bổ sung (Lô 2)
- Design còn thiếu hoặc lệch (`OQ-45`): campaign phía học viên (US19), nhật ký Ops (US22), khối My Learning (US1), tab `Activities` và lối vào campaign trên màn Gamification (US6), nút xuất + bỏ dòng `You` ở kết quả campaign (US21), nút xoá campaign (US20).
- Chuỗi tiếng Anh còn trống (`OQ-50`): trạng thái rỗng bảng `Activities`, `Courses` (US6) · gợi ý bắt đầu học (US7) · dòng giải thích dưới công tắc `Points`, `Badges` và dòng nhắc cố định (US8–US10) · tooltip, cảnh báo tiêu chí và bảng cuối cùng (US10, US11) · nhãn cập nhật, nhãn đóng băng, trạng thái rỗng campaign (US19).
- Tên và hình mặc định cho 24 mốc của `Activity badges`, `Test badges`, `Course badges` (nếu Q15 = A thì chỉ cần hình).
- Ghi nhận, sửa khi có CR: công tắc `Maximum level` trong design so với "bỏ trống = không trần" (RD21); tên cột `Last activity` ở US12 (RD22); `Test Account` thấy gì ở UpLMS (RD23); dòng truy vết cho US12 và dòng `A25` lạc chỗ (RD25).

PO bổ sung (giả lập, mục "Việc PO cần bổ sung" Lô 2):
- Design thiếu (`OQ-45`): làm sau, Tech dùng component chuẩn và ghi ui-map 3.41 `Provisional` cho tới khi có design.
- Chuỗi `OQ-50`: Tech viết nháp theo giọng các chuỗi đã có, PO duyệt ở `/change-request`.
- Hình mặc định 24 mốc: design gửi sau; tạm dùng hình mặc định của loại.
- RD21–RD25: sửa trong CR kế tiếp.

## Consolidated Summary (Lô 2)
- Q5: tiêu chí lên hạng theo huy hiệu dùng bộ đếm riêng, chỉ tăng khi nhận huy hiệu mới (kể cả trao bù lần đầu).
- Q6: bảng `Courses` campaign luôn có, không có ô chọn.
- Q7: cho tắt `Gamification` khi có campaign chạy; popover nêu số campaign; thời gian tắt campaign không nhận gì.
- Q8: đóng băng campaign sau kết thúc 24 giờ; ghi lại tới sau đó không đổi kết quả campaign.
- Q9: không có màn lỗi cho vận hành; tự ghi lại, lỗi còn lại báo đội kỹ thuật (log + cảnh báo).
- Q10: thông báo 5 giây mỗi thẻ, tối đa 4 thẻ, trỏ chuột thì dừng.
- Q11: lịch sử tải 20 mục mỗi lần.
- Q12: ảnh huy hiệu theo giới hạn kho tài nguyên Ops; khuyến nghị vuông PNG/SVG, hiển thị 96×96.
- Q13: tên campaign tối đa 100 ký tự.
- Q14: thông báo ≤ 3 giây; gamification thêm ≤ 200 ms vào thao tác hoàn thành; US12, US22 ≤ 2 giây/trang với 10.000 học viên, 5 triệu dòng; xuất Excel ≤ 50.000 dòng.
- Q15: mặc định theo design (10 / 10 / 150 / 25; 3000 / 5 / 5; trần 100); tên ba loại còn lại cùng mẫu Check-in.
- Q16: giữ bảng xem trước, chỉ `All time`, theo công tắc `Show …`, không dòng `You`, không chọn khung.
- Q17: giữ mọi dòng `[đề xuất]` như PRD viết.

Xác nhận: [GIẢ LẬP PO] Looks correct. Chưa chạy `/change-request`; PRD vẫn v0.14 (DEC-T17).
