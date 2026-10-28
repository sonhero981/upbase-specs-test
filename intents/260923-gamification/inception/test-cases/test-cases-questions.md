# Test Cases, câu hỏi cho PO
Intent: 260923-gamification · Người trả lời: PO · Cách trả lời: theo `state.md` PO (Chat) · Đã trả lời: 0

Câu QA gặp khi viết TC cả intent (2.81 v1.1) mà PRD v0.14 + 2.43 Q1–Q17 chưa có rule. Không chặn thiết kế: TC liên quan ghi "chờ PO"; PO trả lời thì mở lại TC đó `[R]`. Câu nào PO thấy cần đổi PRD thì đưa vào `/change-request` cùng Q1–Q17.

## Điểm (US13, US5, US8, US22)

- **TQ-1.** **US5 · đổi múi giờ tenant giữa chuỗi.** `BR-14.9` lấy múi giờ theo tenant nhưng không nói khi tenant đổi múi giờ thì chuỗi đang giữ và bản ghi ngày đã có xử lý ra sao (một "ngày" có thể bị lặp hoặc mất). Đề xuất: không tính lại, ngày kế tiếp cắt theo múi giờ mới, chuỗi không đứt nếu ngày mới liền kề ngày cuối đã ghi. Có giữ vậy không?
- **TQ-2.** **US5 · `Gamification` tắt lúc lần vào đầu ngày rồi bật lại trong cùng ngày.** C-16 bỏ qua (202) khi tắt; chưa rõ có đặt khoá SET NX hay không. Nếu không đặt, lần vào sau khi bật lại trong cùng ngày sẽ được check-in n=1. Theo `BR-5.12` ("tính từ thời điểm bật") và Q3 ("ngay khi lưu xong") thì lần vào sau khi bật có được ghi nhận ngay trong ngày đó không? (Khác `BR-5.15`, nơi ngày đã được ghi khi `Points` tắt.)
- **TQ-3.** **US13 / US22 · tài khoản đổi `Test Account`.** HV2 đã có điểm, sau đó được đặt `users.is_operator=true` (hoặc ngược lại). Các dòng cũ trong ledger, nhật ký Ops (`BR-22.4`), bảng xếp hạng có bị ẩn không? Lần học tiếp theo sau khi gỡ cờ có tính lại từ đầu không? PRD chưa có rule.
- **TQ-4.** **US13 · lần ghi lại sau lỗi khi cấu hình đã đổi.** FailedEvent gốc lúc 09:00 khi `ACTIVITY` = 10 (hoặc `Points` bật, hoặc `Gamification` bật); cron chạy lại lúc 09:15 khi đã đổi thành 20 (hoặc đã tắt). Lần ghi lại dùng cấu hình tại thời điểm gốc hay tại lúc ghi lại? `BR-13.8` chỉ nói mang thời điểm gốc.
- **TQ-5.** **US13 · học viên bị `Block` hoặc rời tổ chức khi đang có FailedEvent PENDING.** Cron có ghi lại cho người này không?
- **TQ-6.** **US5 / US22 · dòng check-in khi `Points` tắt.** `BR-5.15` ghi ngày có mặt nhưng không tăng chuỗi; `BR-13.13` (dòng 0 điểm) chỉ nói về lần hoàn thành. Ngày check-in lúc `Points` tắt có sinh dòng 0 điểm trong nhật ký Ops không? Nếu có, Details hiện gì khi không có `day {d} of streak` (ví dụ `Daily check-in · points off`)?
- **TQ-7.** **US22 · biên khoảng ngày.** Bộ lọc `from`/`to` là ngày theo múi giờ tenant; ngày `to` có bao gồm trọn ngày (đến 23:59:59) không? Đề xuất: biên đóng hai đầu, giống US12. `This week` bắt đầu thứ hai hay chủ nhật?
- **TQ-8.** **US22 · sắp xếp hoà.** Hai dòng cùng `occurred_at` (huy hiệu và dòng điểm sinh ra cùng thao tác) xếp theo tiêu chí phụ nào? Đề xuất: Level up > Badge > Points (theo thứ tự xử lý), rồi `id`.
- **TQ-9.** **US22 · tìm học viên.** Ô tìm theo tên có bỏ dấu tiếng Việt và không phân biệt hoa thường không (gõ `lan` ra `Lan`, `Lân`)? Có tìm theo email không?
- **TQ-10.** **US22 · lọc hành động khi chưa chọn `Points`.** Chọn hành động (check-in, bài Test…) mà bỏ chọn loại `Points` thì bộ lọc hành động bị ẩn / vô hiệu, hay vẫn áp?
- **TQ-11.** **US8 · hai người E sửa cùng ô cùng lúc.** Tự lưu theo từng trường nên lần lưu sau thắng lặng lẽ; màn của người kia vẫn hiện giá trị cũ. Chấp nhận "lần sau thắng", không cảnh báo xung đột?
- **TQ-12.** **US8 · giá trị nhập `010`, `1e3`, dán `1,000`.** Có chuẩn hoá (`010` → 10) hay báo lỗi? Đề xuất: chỉ nhận chữ số, bỏ số 0 đầu.

## Hiển thị (US1, US2, US3)

- **TQ-13.** **Dấu phân cách hàng nghìn không thống nhất** (TC-208, TC-224, TC-227): ô điểm dùng dấu chấm (`1.250 Points`), panel `How to level up?` dùng dấu phẩy (`Every 3,000 points`). Thông báo `+1,250 pts` và lịch sử `You earned **1,250 points**` dùng dấu nào? Đề xuất: dùng chung một kiểu cho mọi chỗ.
- **TQ-14.** **Thông báo check-in ngày đầu chuỗi** (TC-234): bộ chuỗi thông báo chỉ có `+{n} pts for visiting today · {d}-day streak`. Ngày đầu có hiện `· 1-day streak` không, hay bỏ phần chuỗi như lịch sử (lịch sử có chuỗi riêng cho ngày đầu)?
- **TQ-15.** **Cắt tên dài trong thẻ thông báo**: PRD chỉ quy định cắt 60 ký tự ở lịch sử, và chỉ cho tên hoạt động, tên khoá. Thẻ thông báo cắt thế nào? Tên bài Test và tên huy hiệu trong lịch sử có cắt ở 60 ký tự không?
- **TQ-16.** **Thứ tự khi trùng thời điểm** (TC-256): một thao tác hoàn thành khoá sinh 4 dòng có cùng `occurred_at`. Lịch sử xếp các dòng này theo thứ tự nào? Đề xuất: ngược thứ tự phát sinh (lên hạng → huy hiệu → điểm khoá → điểm hoạt động).
- **TQ-17.** **Các ô có tự cập nhật không**: đang ở màn Gamification hoặc My Learning mà nhận thẻ điểm, các ô và khối My Learning có cập nhật ngay không, hay phải tải lại?
- **TQ-18.** **Khối My Learning khi tắt cả `Points` và `Levels`**: khối ẩn hẳn hay còn một khối rỗng? Contract trả `{points:null, level:null}`. Đề xuất: ẩn hẳn.
- **TQ-19.** **Dòng check-in khi nền = trần và dưới 40** (ví dụ nền 30, trần 30): hiện `30–30 pts` hay `30 pts`? Panel `How to level up?` có áp quy tắc số ít không (`Every 1 completed course`, `Every 1 badge`)?
- **TQ-20.** **Trỏ chuột vào thẻ** (TC-240): chỉ dừng thẻ đang trỏ hay dừng cả chồng? Bản đã test giả định là chỉ dừng thẻ đang trỏ.
- **TQ-21.** **Trạng thái đang tải và trạng thái lỗi**: `/gamification/me`, `/rules`, `/me/history` trả 500 hoặc quá thời gian thì màn, panel và lịch sử hiện gì? PRD chỉ quy định trạng thái rỗng.
- **TQ-22.** **Nhiều tab** (TC-249): mỗi tab đang mở đều hiện thẻ (theo A-03). PO có muốn thẻ chỉ hiện ở tab đang dùng không?
- **TQ-23.** **Học viên bị Block khi đang mở UpLMS**: kết nối socket có bị cắt ngay không, và các thao tác còn dở có tiếp tục sinh thông báo không?
- **TQ-24.** **Có dòng mới trong lúc đang cuộn lịch sử**: phân trang theo `page_index` sẽ bị lệch, có thể lặp một mục ở trang sau. Có cần chống lặp không? Đề xuất: lms-fe bỏ trùng theo `id`.
- **TQ-25.** **Hạng khi `Levels` tắt**: hạng có tiếp tục được xét ngầm không? Nếu có thì bật lại sẽ nhảy nhiều hạng mà không có thông báo. Cần chốt để viết TC kèm theo TC-219.

## Huy hiệu, Hạng (US9, US4, US10)

- **TQ-26.** US9 tên mốc chỉ gồm khoảng trắng (`"   "`): coi như bỏ trống (về tên mặc định) hay lưu nguyên? Tên có khoảng trắng đầu/cuối có tự cắt không?
- **TQ-27.** US9 dòng tóm tắt mốc: chưa có câu chữ cho `Activity badges` và `Test badges` (đơn vị "activities"/"completed activities", "passed tests"). US4 hover với mốc `1` hiện `1 completed courses` hay số ít `1 completed course`?
- **TQ-28.** US9-AC11 chỉ chặn ở UI. Gọi thẳng `PATCH /badges/{id}` cho mốc của loại đang tắt thì cho lưu hay từ chối?
- **TQ-29.** Hai nhân sự E sửa cùng tên một mốc cùng lúc: chấp nhận "lần lưu sau thắng" lặng lẽ không?
- **TQ-30.** Đang gõ tên/mô tả mà rời trang hoặc hết phiên trước khi rời ô: lưu hay mất? Có cảnh báo không?
- **TQ-31.** US4: `Badges` bật nhưng cả 4 loại tắt thì tab `Badges` ẩn hay hiện rỗng (có chuỗi trạng thái rỗng)? Mở thẳng URL tab `Badges` khi tab không còn thì chuyển về đâu?
- **TQ-32.** Học viên bị Block, hoặc đã rời tổ chức, có được trao bù huy hiệu khi bật lại loại không?
- **TQ-33.** "Trao bù ngay" (BR-9.9) có giới hạn thời gian không, ví dụ tổ chức 10.000 học viên phải xong trong bao lâu? Trong lúc job chạy, học viên có thể thấy bộ đếm chưa đủ.
- **TQ-34.** US10: khi `Levels` đang tắt, có cho tắt tiêu chí chạy cuối cùng không (BR-10.8 chỉ nói "khi Levels đang bật")? Nếu cho, bật `Levels` lên mà 0 tiêu chí chạy thì chặn hay chỉ cảnh báo?
- **TQ-35.** Khi khởi tạo tổ chức, tiêu chí nào trong ba tiêu chí bật sẵn (Q15 chỉ chốt giá trị 3000/5/5 và trần 100)?
- **TQ-36.** Ranh giới mã lỗi (cho BE xác nhận): `multiplier:0`, `level_cap:1` trả `422\|000405` (DTO) hay `400\|630006`? `badge_type.type` ngoài enum trả `422` hay `400\|630003`? `630003` dùng cho trường hợp nào khác?
- **TQ-37.** C-18 ghi "Badges tắt → 404 riêng của tab" nhưng không nêu mã. Dùng `404\|630012` hay mã riêng?

## Bảng xếp hạng (US6, US7, US11, US12)

- **TQ-38.** **Ngày cuối của nhãn khoảng ngày (US6-AC4, C-19 `date_range.to`).** Hôm nay 14/10: `This month` hiện `1–31 Oct 2026` (hết kỳ lịch, theo mẫu `1–30 Sep 2026`) hay `1–14 Oct 2026` (tới hôm nay)? `All time` hiện `1 Sep–14 Oct 2026`? TC-404 đang để mở phần ngày cuối.
- **TQ-39.** **Học viên cuối bảng không có người ngay dưới (US7).** HV7 #7/7 trong `Points All time`: khối chỉ hiện dòng của HV7, hay lấy người ngay trên thay vào? `C-20.below` có thể null. Đề xuất: chỉ hiện dòng của mình.
- **TQ-40.** **Dòng khoảng cách khi bằng điểm người trên (US7-AC4).** HV3 và HV4 cùng 300 (khác thời điểm hoặc tên): hiện `0 points behind An Lê`, hay đổi câu (ví dụ cần thêm 1)? Và học viên chưa có chỉ số thì có dòng khoảng cách không?
- **TQ-41.** **Thứ tự A–Z với tên tiếng Việt (BR-6.4, BR-6.6).** Sắp theo tên đầy đủ hay tên gọi (từ cuối)? "Đ" đứng sau "D" (bảng chữ cái tiếng Việt) hay sau "Z" (thứ tự Unicode)? Có phân biệt hoa thường, dấu không?
- **TQ-42.** **Không còn bảng nào chạy (BR-11.5) phía học viên.** Khi `running_board_count = 0` mà `Leaderboard` vẫn bật, học viên thấy gì: ẩn cả khu Bảng xếp hạng như `BR-11.6`, hay hiện trạng thái rỗng? Và vận hành tắt được bảng cuối khi `Leaderboard` đang tắt không (`BR-11.5` chỉ nói "khi `Leaderboard` đang bật")? Nếu được, bật `Leaderboard` lại với 0 bảng thì xử lý sao?
- **TQ-43.** **Biên khoảng ngày tự do của US12.** `from`, `to` là biên đóng cả hai đầu (gồm trọn ngày `to` tới 23:59:59 UTC+7)? TC-475 đang giả định đóng.
- **TQ-44.** **`from > to` hoặc khoảng ở tương lai (US12).** API trả 422 hay đảo/hiện rỗng? Có giới hạn độ dài khoảng không?
- **TQ-45.** **Tìm kiếm tên (US12-AC12).** Có tìm không dấu ("an le" ra "An Lê") và tìm theo email/mã học viên không?
- **TQ-46.** **Sắp xếp hoà ở US12 (US12-AC13).** Hai học viên cùng `Courses` thì tiêu chí phụ là gì (tên A–Z?) để phân trang và file xuất ổn định?
- **TQ-47.** **Học viên bị Block hoặc rời tổ chức giữa chu kỳ (BR-6.8).** Biến khỏi bảng ngay lúc đọc hay chờ chu kỳ 8 tiếng kế tiếp? Mở Block lại thì xuất hiện lại với số cũ? TC-431 đang kiểm sau chu kỳ.
- **TQ-48.** **Học viên mới tạo giữa chu kỳ (BR-6.6).** Tài khoản tạo 10:00 có xuất hiện (ô `#` trống) trước chu kỳ 16:00 không? Khối Vị trí của tôi của người đó hiện gì trước khi có snapshot?
- **TQ-49.** **Trạng thái đang tải và lỗi của Bảng xếp hạng (US6, US7).** C-19/C-20 lỗi 5xx thì hiện gì, có nút thử lại không? PRD chỉ có trạng thái rỗng.
- **TQ-50.** **Chuỗi tiếng Anh còn mở (`OQ-50`):** trạng thái rỗng `Activities`, `Courses` (US6); gợi ý bắt đầu học (US7); tooltip bảng cuối và cảnh báo không còn bảng (US11). TC-424, TC-439, TC-455, TC-457 chưa kiểm được nguyên văn.

## Campaign (US20, US19, US21)

- **TQ-51.** Tên campaign chỉ gồm khoảng trắng, hoặc có khoảng trắng đầu cuối: chặn hay tự cắt? Có cho trùng tên giữa hai campaign không? (PRD chỉ nói bắt buộc, ≤100 ký tự.)
- **TQ-52.** Bấm `Save` hai lần nhanh, hoặc hai nhân sự E cùng sửa một campaign `Not started`: chặn bản ghi trùng / ai thắng (ghi đè lặng hay báo xung đột)? PRD không có rule.
- **TQ-53.** Đóng panel `Campaign Settings` (bấm ra ngoài, `Esc`, rời trang) khi đang nhập dở: có cảnh báo mất dữ liệu không?
- **TQ-54.** Sửa campaign `Not started`: ngày bắt đầu mới có chịu luật "sớm nhất là ngày mai" như lúc tạo không (ví dụ 14/10 đổi CP-A sang bắt đầu 14/10)? Contract chỉ ghi 630014 cho `POST`.
- **TQ-55.** Có giới hạn ngày bắt đầu xa nhất hoặc độ dài tối đa campaign (ví dụ 01/01/2030–31/12/2035) không?
- **TQ-56.** Thứ tự trong nhóm **đang chạy** ở US19: "kết thúc gần nhất lên trước" nghĩa là campaign sắp kết thúc sớm nhất lên trước (CP-B 20/10 trước CP-F 25/10)? TC-531 đang giả định như vậy.
- **TQ-57.** Panel kết quả bên Ops (US21) khi `Points` tắt: tab `Points` ẩn như phía học viên, hay vận hành vẫn thấy? File xuất có sheet `Points` không?
- **TQ-58.** Học viên bị Block **trong lúc** campaign đang chạy: bảng tạm tính ẩn ngay ở lần tính kế hay vẫn hiện tới khi đóng băng? Bị Block trước kết thúc rồi được mở Block trước lần job chốt người tham gia thì có mặt không?
- **TQ-59.** ADR-017 sai số 15 phút: học viên bị Block lúc 21/10 00:05 (sau biên, trước lần job đầu) có thể bị loại khỏi kết quả. PO chấp nhận sai lệch này với C12 không?
- **TQ-60.** Campaign kết thúc trong lúc `Gamification` đang tắt: tác vụ đóng băng vẫn chạy đúng hạn (biên + 24 giờ) không?
- **TQ-61.** Nếu sự kiện lỗi PENDING không bao giờ xử lý xong (lỗi vĩnh viễn), đóng băng chờ tới bao giờ? Có hạn chót hay cảnh báo cho vận hành?
- **TQ-62.** File xuất Excel: tên file, có trần số dòng không, cột thời điểm đạt mức có xuất không?
- **TQ-63.** Thời điểm đóng băng hiển thị theo múi giờ tổ chức hay múi giờ trình duyệt?

## Ghi chú cho PO (không phải câu hỏi)

**Điểm (US13, US5, US8, US22)**

- US13 không có bảng "UI / UX / Rule UX / Rule UI" nên TC của US13 chỉ trỏ BR; đã thêm TC cho ba rule nền `BR-TEST`, `BR-REGRADE`, `BR-SKIP` và quy tắc chung "Định nghĩa chỉ số" vì US13 là nơi các rule này chạy.
- Chuỗi tiếng Anh còn trống ở US8 (dòng giải thích dưới công tắc `Points`, dòng nhắc cố định — `OQ-50`): TC chỉ kiểm có hiện và đúng ý; chuỗi chính xác kiểm lại khi PO duyệt ở `/change-request`.
- Vị trí mục `Achievement history` (US22-AC1) và giao diện nhật ký chưa có design (`OQ-45`); TC kiểm theo component chuẩn Ops, cần chạy lại khi có design.
- Các dòng `[đề xuất]` (mẫu thông báo check-in US5-AC1, câu mô tả check-in khi nền ≥ 40, thời điểm gốc của lần ghi lại `BR-13.8`, bật lại giữa ngày `BR-5.15`, chuỗi Details US22, lọc theo hành động, mở nhật ký từ US12) được kiểm như PRD viết theo Q17.
- Số NFR lấy từ Q14: thông báo ≤ 3 giây, gamification thêm ≤ 200 ms vào thao tác hoàn thành, US22 ≤ 2 giây/trang với 10.000 học viên và 5 triệu dòng. Mặc định 10/10/150/25 lấy từ Q15; PRD US8 chỉ nêu nền 10.
- Q9: không có màn lỗi cho vận hành; TC lỗi (TC kiểm `GAVE_UP`) kiểm bằng DB, log và cảnh báo kỹ thuật.
- PRD US8 Data Field ghi Points và hành động mặc định **tắt**; TC mặc định kiểm `points_enabled:false`, `is_enabled:false` với điểm 10/10/150/25. Nếu design muốn mặc định bật thì cần CR.
- C-04 trả 403 cho L ở GET point-rules (tags chỉ `view_settings` + `update_settings`, `BR-15.7`); TC quyền US8 kiểm theo đó.

**Hiển thị (US1, US2, US3)**

- `US2-AC10` (thời gian tự tắt) và `US3-AC7` (số mục mỗi lần tải) trong PRD vẫn ghi `❓PO`. TC dùng câu trả lời Lô 2: Q10 (mỗi thẻ 5 giây, tối đa 4 thẻ, trỏ chuột thì dừng đếm) và Q11 (20 mục mỗi lần). NFR dùng Q14 (thẻ hiện trong 3 giây, cộng thêm không quá 200 ms). Đề nghị đưa các con số này vào PRD ở `/change-request`.
- Mã BR giữ đúng như PRD: US2 có `BR-2.10` đứng trước `BR-2.9`, US3 không có `BR-3.2`. TC không đổi số.
- `BR-2.8` (không thông báo tụt hạng) được kiểm chung với `BR-1.3` ở TC-212, ghi dưới US1.
- TC-234 giả định số điểm check-in theo cách tính ở US5 (nền + 5 mỗi ngày giữ chuỗi, có trần). QA đối chiếu dòng sổ điểm, không cố định một con số.
- Tên `Course Newbie` (TC-233) theo mẫu tên ở Q15. Nếu tên mặc định đổi thì chỉ cần thay chuỗi mong đợi.
- `Test Account` được hiểu là `users.is_operator = true` (theo `C10`).
- Mã lỗi theo S-01: `404|630012` cho cả trường hợp tắt và Test Account; `422|000405` cho tham số phân trang sai.

**Huy hiệu, Hạng (US9, US4, US10)**

- Q12 PO chọn A (theo giới hạn kho tài nguyên Ops); TC-312 lấy giới hạn hiện có trong contract C-05: `.png/.jpg/.jpeg/.webp/.svg`, tối đa 1 MB. Chưa kiểm kích thước pixel tối thiểu vì không có rule.
- Trần hạng: PRD nói "bỏ trống = không trần", design và C-06 có công tắc `level_cap_enabled` (RD21, sửa ở CR kế tiếp). TC-363 chấp nhận cả hai cách thể hiện, cần chốt lại khi CR xong.
- Q5: tiêu chí lên hạng theo huy hiệu dùng bộ đếm chỉ tăng (`total_badges_acquired`); TC-326, TC-327 kiểm hai chiều (trao bù lần đầu có tính, tắt/bật loại không tính lại).
- Tắt `Badges` không ghi `is_enabled=false` cho tiêu chí `BADGES`, chỉ khoá; không còn lỗi `630011` (TC-302, TC-366).
- Các chuỗi OQ-50 (dòng giải thích dưới `Badges`, tooltip tiêu chí cuối, cảnh báo 0 tiêu chí, dòng nhắc cố định) kiểm theo bản nháp Tech sau khi PO duyệt ở `/change-request`; TC-303, TC-364, TC-366, TC-369 cập nhật nguyên văn khi có.
- Hình mặc định 24 mốc Activity, Test, Course: design gửi sau, tạm dùng hình mặc định của loại; TC-301 chỉ kiểm có hình, không kiểm hình cụ thể.

**Bảng xếp hạng (US6, US7, US11, US12)**

- **Bộ dữ liệu:** D1 (TC-401) dùng cho US6, US7, US11; D2 (TC-468) dùng cho US12. HV7 trong D2 là học viên chưa đăng nhập, khác vai HV7 trong D1. Hôm nay giả định thứ Tư 2026-10-14, chu kỳ tính 00:00 · 08:00 · 16:00 UTC+7.
- **Phủ:** US6 17 dòng AC, US7 7, US11 12, US12 17 — mỗi dòng ≥ 1 TC. Mọi BR có TC: `BR-6.1`…`BR-6.16` (gồm bốn dòng bảng `BR-6.16`: TC-426, TC-428, TC-427, TC-429; tie-break `BR-6.4`: TC-413 sớm hơn xếp trên, TC-414 cùng thời điểm theo tên A–Z, TC-415 khoảng giá trị hẹp), `BR-7.1`…`BR-7.7`, `BR-11.1`…`BR-11.7`, `BR-12.1`…`BR-12.8`. Q16 (bảng xem trước) ở TC-465…TC-467; Q14 ở TC-480, TC-483.
- **Mã lỗi khi `Leaderboard` tắt:** C-19/C-20 ghi `630016` cho "bảng tắt/khoá"; TC-459 giả định tắt cả khối cũng trả `404\|630016` (khác `630012` của cả tính năng). Đề nghị Dev xác nhận để không lệch.
- **TC-403:** C-19 không khai `from`/`to`; TC giả định tham số thừa bị bỏ qua. Nếu BE bật `forbidNonWhitelisted` thì kết quả đúng là 422 — cần Dev chốt một cách.
- **TC-480, TC-483, TC-446** cần môi trường perf có 10.000–50.001 học viên; không chạy được ở `LOCAL`.
- Theo quy định bảo mật của tổ chức, file xuất ở TC-477…TC-480 chỉ chứa dữ liệu gamification theo C-10 (`Learner` = tên + ảnh); không có email, số điện thoại.

**Campaign (US20, US19, US21)**

- US19-AC1 (lối vào campaign), chuỗi tiếng Anh nhãn cập nhật / đóng băng / trạng thái rỗng (US19-AC9…AC11) chờ design OQ-45 và chuỗi OQ-50; TC-531, TC-535…TC-537 kiểm hành vi, chuỗi sẽ chốt khi có.
- Design hiện thiếu nút xoá (US20-AC4, OQ-45), thiếu nút xuất (US21-AC8), còn dòng `You` trong kết quả Ops (US21-AC4) và cột `Contribution` có dòng không có `Course` (Q6). TC-503, TC-516, TC-551, TC-559 sẽ fail cho tới khi design sửa.
- Các TC biên thời gian (TC-508, TC-514, TC-521, TC-522, TC-540, TC-553…TC-556) cần giả lập giờ tenant trên staging hoặc chèn dữ liệu sổ giao dịch với thời điểm định sẵn; tenant `Asia/Ho_Chi_Minh` (UTC+7).
- Mốc đóng băng dùng trong TC: kết thúc 20/10 → biên 21/10 00:00 giờ tổ chức → đóng băng sớm nhất 22/10 00:00 (Q8, ADR-013), người tham gia chốt ở lần job 15 phút đầu sau biên (ADR-017).
- TC-529 dùng thêm tài khoản L = staff chỉ có `gr_view_gamification_learners`.
