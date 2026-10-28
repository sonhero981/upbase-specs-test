# Review: prd.md (v0.7) · 2.42 PRD Generation · lần 07
**Verdict:** READY
**Verdict Dictated:** no
**Reviewer:** ai-reviewer · **Date:** 2026-10-25

## Prior findings
| ID | Severity | Now | Note |
|---|---|---|---|
| R-15 | Major | Fixed | `BR-20.9`, `AC20.3` và bảng *Nội dung email: MAIL-GRP-01* đều ghi email gửi quản lý không có đường dẫn hồ sơ, chỉ email gửi quản trị viên hệ thống có `View profile`. Khớp `BR-16.8`, không còn mâu thuẫn trong PRD |
| R-16 | Major | Fixed | `BR-13.9` định nghĩa tài khoản khoá không tính là quản lý hay mentor có hiệu lực; `BR-13.1`, `BR-10.1`, `BR-20.2` đến `BR-20.4` trỏ về; `AC13.1` kiểm nhãn `No manager` và email gửi quản trị viên. Phần kiểm chưa đủ nhánh, xem finding mới thứ nhất |
| R-17 | Major | Fixed | `BR-14.1` thêm điều kiện không có nhóm con; `BR-14.9` và `AC14.5` định nghĩa khôi phục cả nhánh, nhóm con không khôi phục riêng, luật đứng chạy tiếp; `AC14.1` có nhánh bị từ chối |
| R-18 | Minor | Fixed | `BR-18.9` định nghĩa Hoàn thành, Quá hạn, Đang học, Chưa bắt đầu, Số khoá có nghĩa vụ, Tiến độ; `AC18.4` kiểm ba khoá. Còn vài chỉ số ở bảng báo cáo chưa định nghĩa, xem finding mới thứ hai |
| R-19 | Minor | Fixed | Chỉ còn một nhãn `[đề xuất]` ở câu hỏi mở #17, và chính hàng đó là câu hỏi mở có người trả lời |
| R-20 | Minor | Fixed | `BR-18.7` ghi mọi mốc ngày tính theo giờ Việt Nam, UTC+7, gồm cuối ngày T |
| R-21 | Minor | Fixed | `BR-2.5` và `AC2.5` nói rõ người vào nhánh sau thời điểm di chuyển được ghi danh khi nhóm cha mới bật `Cascade to sub-groups` và `Auto-enroll` |
| R-22 | Minor | Fixed | `BR-6.2` đếm người không trùng và áp cho `US18`, `US21`; `AC6.2` có ví dụ hai nhóm con của cùng một nhóm cha; `BR-18.3`, `BR-21.5` trỏ về |
| R-23 | Minor | Fixed | `AC16.2` có nhánh mở `SCR25` của người ngoài nhánh bằng đường dẫn trực tiếp: trang không có quyền, không lộ dữ liệu |
| R-24 | Minor | Fixed | `traceability.md` có `RC-29` và `RC-30`; `US19` truy về `RC-29`, `US20` truy về `RC-30` và `RC-22`; `requirements.md` v0.5 có hai mã này. Kết quả kiểm bằng máy không có cảnh báo; tôi dò lại 153 BR, 116 AC, mọi BR có AC trích dẫn, không mã nào trích mà chưa định nghĩa |
| R-25 | Minor | Fixed | `SC5` đổi cách đo: chạy lại cùng mốc T ở hai thời điểm, loại trừ thay đổi do di chuyển nhánh theo `BR-18.2`; không còn dựa vào bản chốt |
| R-26 | Minor | Fixed | Frontmatter có dòng `services` |
| R-27 | Minor | Fixed | Cột Màn hình ở `US6` và `US18` đã ghi mã `SCR` ở mọi dòng. `US21` còn ba màn chưa có mã nhưng đã ghi ở câu hỏi mở #19 |
| R-28 | Minor | Still applies | Mục 3 đã ghi 21 user story. Còn dấu vết quy trình ở thân PRD: mục 6 đoạn đầu "Quy ước giao diện từ CR7"; mục 10 hàng #2 "Từ CR6", #7 "đã giải ở CR7", #8 "CR7 đưa…" và "QA tạm bỏ qua ở CR7 (DEC114)", #10 "đã có tiêu chí ở CR7", #20 "ở gate CR7". Nhiều mã `DEC` đứng một mình không kèm nội dung ở mục 4, mục 8 cột Nguồn, `US6` `US15` `US16` `US17` `US18`. Hàng #8 và #12 còn chữ "Đã quyết 25/10/2026" |
| R-29 | Minor | — | Accepted risk, quyết định của PO, không chấm lại |

## New findings
| Severity | Location | Finding | Required action |
|---|---|---|---|
| Minor | prd.md > US13 > `BR-13.9` · `AC13.1` · US10 > `BR-10.1` | `BR-13.9` có năm hệ quả (không tính nhóm trống quản lý, kế thừa bỏ qua rồi đi lên nhóm cha, không nhận email, không tính mentor phụ trách nhóm trong lớp, mở khoá thì có hiệu lực lại) nhưng bảng truy vết chỉ trỏ `AC13.1`, và `AC13.1` chỉ kiểm trường hợp quản lý duy nhất của nhóm và mọi nhóm cha đều bị khoá. QA không có tiêu chí cho: nhóm con kế thừa bỏ qua quản lý khoá và lấy quản lý của nhóm cha cao hơn; mentor khoá; mở khoá lại; quản lý chính bị khoá ở `MAIL-GRP-01` | Thêm tiêu chí vào `US13` hoặc `US10` cho ba nhánh: kế thừa bỏ qua người bị khoá và đi tiếp lên; mentor bị khoá không được tính phụ trách; mở khoá thì quan hệ có hiệu lực trở lại. Ghi rõ quản lý chính bị khoá có bị bỏ qua ở `BR-20.2` không |
| Minor | prd.md > US18 > bảng Giao diện và validate `SCR16` · `BR-18.9` | Ba chỉ số của báo cáo chưa có định nghĩa: Số người có nghĩa vụ (nhóm con, khoá), Tỉ lệ hoàn thành, Tiến độ trung bình. `BR-18.9` chỉ định nghĩa Số khoá có nghĩa vụ và Tiến độ của một lượt. Tiến độ trung bình của một người lấy trung bình theo lượt ghi danh hay theo khoá; của nhóm con lấy trung bình theo người hay theo lượt thì Dev phải đoán, hai cách cho hai con số khác nhau | Thêm vào `BR-18.9` công thức bằng lời: Số người có nghĩa vụ là số người không trùng có ít nhất một lượt đang tính; Tỉ lệ hoàn thành là số lượt hoàn thành trên số lượt đang tính; Tiến độ trung bình lấy trung bình theo lượt hay theo người, và thêm một tiêu chí có số cụ thể |
| Minor | prd.md > US8 · US3 > `BR-3.6` · `BR-5.7` · `BR-16.6` · `BR-13.9` · mục 4 | PRD dùng hai cách gọi: "người đã nghỉ việc" (ẩn khỏi danh sách, lượt ghi danh kết thúc) và "tài khoản đã khoá" (không tính là quản lý, không nhận email). Thiết kế BE ghi nghỉ việc nhận ra qua tài khoản bị khoá, không có đánh dấu riêng; PRD chỉ nói ở mục 4 rằng nghỉ việc thì tài khoản tự khoá. Một học viên bị khoá thủ công vì lý do khác có bị coi là nghỉ việc ở danh sách thành viên, báo cáo, `My Team` không thì PRD không nói. Góc "bị Block giữa chừng" của corner checklist chưa chốt thành một luật | Thêm một câu vào mục 4 hoặc `BR-6.3`: người nghỉ việc là người có tài khoản khoá, hay chỉ khoá do đồng bộ; nếu là mọi tài khoản khoá thì ghi vậy, nếu không thì chuyển thành câu hỏi mở gắn tên Tech PIC |
| Minor | prd.md > mục 10 · US20 > `BR-20.9` · US14 > `BR-14.1` · `BR-14.9` ↔ ux-design.md > SCR29 · EC-08 · mục 2 luồng email | `ux-design.md` v0.1 vẫn ghi email `SCR29` có `View profile` mở hồ sơ cho quản lý, luồng `E1 -.-> PV`, và `Delete` chỉ điều kiện chưa có thành viên, chưa giao nội dung (không có điều kiện nhóm con), không có khôi phục cả nhánh. PRD v0.7 đã đổi cả ba theo DEC123 nhưng mục 10 chỉ ghi lệch ở #17. Design PIC và Dev đọc hai file sẽ gặp hai luật | Thêm một câu hỏi mở gắn tên Design PIC: cập nhật `SCR29`, `SCR4`, `SCR5`, luồng email theo `BR-20.9`, `BR-14.1`, `BR-14.9`; ghi PRD là nguồn khi hai file lệch |
| Minor | prd.md > US21 > Tiêu chí chấp nhận · mục 10 #8 | `US21` không có tiêu chí cho nhánh lỗi hoặc bị từ chối, và câu hỏi mở #8 không kể `US21` trong ví dụ. Góc danh sách rỗng chưa có luật: chọn một nhóm mà mọi thành viên là tài khoản kiểm thử hoặc tài khoản khoá thì số người nhận bằng 0, không nói có cho lưu thông báo không | Thêm một tiêu chí cho nhóm có 0 người nhận: hệ thống hiện số 0 và cho lưu hay chặn, ghi rõ một trong hai; hoặc ghi `US21` vào câu hỏi mở #8 |

## Summary
Ba Major và các Minor của lần 06 đã sửa đúng theo DEC123; còn một Minor cũ là R-28 (dấu vết quy trình trong thân PRD) và năm Minor mới, không Critical, không Major, nên READY: Dev và QA làm được từ bản này mà không phải đoán những điểm lớn. Đầu vào không gợi sẵn verdict; chấm độc lập.
