---
intent: 261005-group
artifact: decision-brief
feature: LMS-F002
version: 0.1
status: draft
inputs: prd@0.8, ux-design@0.1, tech-design@0.1, test-design@0.1, fe-technical-design@2.2, be-technical-design (23/10/2026)
---
# [Decision Brief] Nhóm học viên

## 1. Tóm tắt
Nhóm học viên gom người thành cây nhóm, giao lớp cho cả nhóm bằng luật đứng, gán quản lý và mentor, cho quản lý theo dõi nhánh của mình và xem báo cáo theo nhóm. PRD v0.8: 22 user story, 153 business rule, 116 tiêu chí chấp nhận; báo cáo quá khứ để sau. Thiết kế đầu vào gồm `ux-design.md` v0.1 của Design, `be-technical-design.md` và `fe-technical-design.md` v2.2 của Tech. QA chưa có kế hoạch test. Không có mốc phát hành cứng. Còn 6 điểm cần quyết ở mục 2 và 8 chỗ thiết kế lệch PRD v0.7 ở mục 4.

## 2. Điểm cần quyết
| # | Vấn đề | Ai nêu | Lựa chọn và hệ quả | Đề xuất |
|---|---|---|---|---|
| D1 | Chưa có kế hoạch test cho 116 tiêu chí | PO | (a) Đi tiếp: story lên Jira ngay, QA viết test case song song với các story đầu. Rủi ro là story vào sprint trước khi có test case. (b) Chờ QA viết xong rồi mới giao story: chậm toàn bộ | (a), kèm luật: một story chỉ vào sprint khi QA đã có test case cho mọi tiêu chí của story đó |
| D2 | Nhóm đồng bộ từ hệ thống nhân sự có lưu trữ tay được không | Tech, Design | (a) Chặn như mọi thao tác sửa khác của nhóm đồng bộ; nhóm chỉ chuyển lưu trữ khi phòng ban biến mất khỏi nguồn. Thiết kế BE đang chặn. (b) Cho lưu trữ tay: lần đồng bộ sau có thể đưa nhóm về trạng thái đang dùng, gây lệch | (a). Design bỏ nút `Archive` ở nhóm đồng bộ |
| D3 | Màn tạo, sửa nhóm là modal hay drawer | Design, Tech | UX vẽ modal; bản demo FE đã dựng drawer | Giữ drawer đã dựng nếu Design đồng ý |
| D4 | Gán story vào ba Epic trên Jira | PO | Bảng ở mục 6. Story quản lý nhóm, mentor và theo dõi nhánh vào Epic Role & Permission vì chúng cấp quyền và phạm vi xem; nếu xếp theo màn thao tác thì hai story đầu sang Epic Group | Theo bảng mục 6 |
| D5 | Story kỹ thuật chung gom nhiều việc không liên quan | PO | Một story gồm: bỏ nhóm cũ, nhóm của thông báo, phòng ban và đơn vị kinh doanh; tạo bảng nhóm mới; hai cờ cấu hình theo tổ chức; vai phụ trách nhóm để vào UpLMS Ops; lệnh sửa cây; cấu hình Lark và Keycloak | Giữ một story; Tech PIC chia sub-task |
| D6 | Chức năng gửi thông báo trên UpLMS Ops hiện đang bật hay chưa | PO | Đang bật: việc bỏ nhóm cũ của thông báo làm hỏng chức năng này nếu story thông báo theo nhóm (`US21`) ra sau. Chưa bật: `US21` ra đợt nào cũng được | Tech PIC trả lời. Mục 6 đang xếp `US21` ở `ORD-1` để an toàn |

## 3. Đề xuất sửa PRD
PO đã nhận cả bảy đề xuất ở PRD v0.7; không còn đề xuất chờ quyết.

| # | Mã trong PRD | Đề xuất | Ai đề xuất | PO quyết |
|---|---|---|---|---|
| 1 | Năm loại ghi nhật ký ngoài nhật ký thành viên | Ghi rõ là nhật ký hệ thống, chưa có màn | Design | Nhận, `BR-15.5` |
| 2 | `US3` modal thêm thành viên | Theo mẫu Add Student, phân trang 20 dòng | Design | Nhận |
| 3 | `US7` chuỗi công tắc tự ghi danh | `New members of this group will be automatically enrolled in this class` | Design | Nhận |
| 4 | `US16` thiết bị | Thêm bản điện thoại 375 px | Design | Nhận cho màn theo dõi nhánh, hồ sơ chỉ xem, khối quản lý của học viên |
| 5 | `US14` xoá nhóm | Thêm hộp xác nhận xoá | Design | Nhận, `BR-14.8` |
| 6 | `US18` báo cáo quá khứ | Gom theo cây hiện tại, chỉ số từ bản chụp cuối ngày | Tech | Nhận, `BR-18.2`, `BR-18.7` |
| 7 | Phạm vi | Bỏ phòng ban, đơn vị kinh doanh của nhân sự; thông báo chọn người nhận theo nhóm | Tech | Nhận, mục 8 của PRD và `US21` |

## 4. Thiết kế lệch PRD v0.7
| # | Giữa | Nội dung | Đề xuất xử lý |
|---|---|---|---|
| 1 | Cả ba file ↔ PRD | Ba file thiết kế còn dựng từ PRD v0.6 | Mỗi team đối chiếu với v0.7, đổi `inputs` sang `prd@0.7` |
| 2 | Design ↔ `BR-20.9` | Email báo người rời nhóm còn đường dẫn hồ sơ cho quản lý; PRD bỏ đường dẫn này, chỉ email gửi quản trị viên hệ thống có `View profile` | Design sửa màn email |
| 3 | Design, Tech ↔ `BR-14.1`, `BR-14.9` | Nút `Delete` thiếu điều kiện "không có nhóm con"; khôi phục nhóm cha phải khôi phục cả nhánh và chạy lại luật đứng cho người vào lúc lưu trữ | Design sửa màn chi tiết nhóm; BE thêm khôi phục cả nhánh |
| 4 | Tech ↔ `US15` | Nhật ký thành viên chưa lưu lý do và người thao tác | BE lưu hai thông tin này cho mỗi lần vào, rời nhóm |
| 5 | Tech ↔ `BR-5.9` | Đồng bộ cơ cấu chỉ có lệnh chạy tay | BE thêm lần đồng bộ toàn bộ tự chạy mỗi đêm |
| 6 | Tech ↔ `BR-20.5` | Email báo người rời nhóm có thể gửi hai lần khi sự kiện bị xử lý lại | BE chống gửi trùng |
| 7 | Tech ↔ `BR-13.9` | Chưa có luật tài khoản đã khoá không tính là quản lý, mentor có hiệu lực | BE áp ở kiểm nhóm trống quản lý, kế thừa và chọn người nhận email |
| 8 | Tech FE ↔ `BR-9.8`, `US3`, `US13` | Bản FE ghi quản lý là tài khoản nhân sự vận hành, ô thêm thành viên cuộn để tải thêm, khối phụ trách nằm trên hồ sơ nhân sự | FE sửa: tài khoản học viên, phân trang 20 dòng, khối phụ trách trên hồ sơ học viên |

## 5. Độ phủ
- Giao diện: `US21` thông báo theo nhóm chưa có màn trong thiết kế UX (ô chọn nhóm, khối nhóm đã chọn, bộ lọc nhóm). Các user story khác có màn.
- Kế hoạch test: chưa có; cả 116 tiêu chí chưa có test case. Xử lý theo D1.
- Thiết kế kỹ thuật: `tech-design.md` còn khung trống; nội dung của Tech nằm ở hai file BE và FE nên máy không đối chiếu được. Đọc tay: hai file phủ cả 21 user story.

## 6. Phụ thuộc và thứ tự làm
14 story trên Jira, gộp từ 22 user story. Mỗi story một label mã tính năng và một label thứ tự. Điểm theo thang của team, Tech PIC chốt ở Planning Poker.

| # | Story | US | Epic | Điểm | Label |
|---|---|---|---|---|---|
| 1 | Nền kỹ thuật chung | — | G | 5 | `LMS-F002` · `ORD-1` |
| 2 | Tạo, sửa và xem danh sách nhóm | US1 · US6 | G | 3 | `ORG.GRP.01` · `ORD-2` |
| 3 | Quản lý thành viên nhóm: thủ công, theo lô, nhật ký | US3 · US4 · US15 | G | 3 | `ORG.GRP.05` · `ORD-3` |
| 4 | Thông báo gửi theo nhóm | US21 | G | 1 | `LMS-F002` · `ORD-4` |
| 5 | Giao nội dung cho nhóm và tự ghi danh | US7 · US8 | G | 5 | `ORG.GRP.08` · `ORD-5` |
| 6 | Di chuyển, lưu trữ, khôi phục, xoá nhóm | US2 · US14 | G | 3 | `ORG.GRP.12` · `ORD-6` |
| 7 | Đồng bộ nhóm từ hệ thống nhân sự | US5 | G | 5 | `ORG.GRP.03` · `ORD-7` |
| 8 | Báo cáo theo nhóm ở thời điểm hiện tại | US18 | G | 2 | `ORG.GRP.07` · `ORD-8` |
| 9 | Gán quản lý nhóm, kế thừa, chuyển phụ trách | US9 · US10 · US13 | R | 5 | `ORG.ROL.01` · `ORD-9` |
| 10 | Gán mentor cho nhóm | US12 | R | 3 | `ORG.ROL.02` · `ORD-10` |
| 11 | Quản lý trên hồ sơ học viên | US11 · US17 | U | 2 | `ORG.USR.01` · `ORD-11` |
| 12 | Quản lý theo dõi nhánh mình phụ trách | US16 | R | 5 | `ORG.ROL.03` · `ORD-12` |
| 13 | Xử lý khi người rời nhóm | US19 · US20 | G | 3 | `LMS-F002` · `ORD-13` |
| 14 | Báo cáo theo nhóm tại một mốc quá khứ, để sau | US22 | G | 2 | `ORG.GRP.07` · `ORD-14` |

G: Epic `UpLMS_User & Organization_Group`. R: `UpLMS_User & Organization_Role & Permission`. U: `UpLMS_User & Organization_User (Student)`.

Phụ thuộc: story 1 đi trước mọi story; story 4 đi cùng việc bỏ nhóm cũ của thông báo; story 7 cần cấu hình Lark; story 9 đến 11 cần cấu hình Keycloak; story 13 cần đồng bộ và giao nội dung.

## 7. Độ lớn so với mốc
47 điểm, so với mốc là story 3 (3 điểm); đợt này 45, story 14 ở backlog. Không có mốc cứng nên không cần cắt phạm vi. Story lớn nhất là giao nội dung và tự ghi danh, 5 điểm. Story không lọt một sprint thì tách qua change request.

## 8. Rủi ro
| # | Rủi ro | Ai nêu | Cách giảm | Chấp nhận |
|---|---|---|---|---|
| 1 | Story vào sprint khi chưa có test case | PO | Luật ở D1 | Chờ quyết D1 |
| 2 | Bỏ phòng ban làm hỏng màn hoặc tích hợp còn gọi API phòng ban | Tech | Rà mọi nơi gọi; FE đổi form nhân sự và form support group cùng đợt | Chưa |
| 3 | Lỡ sự kiện từ Lark làm nhóm đồng bộ lệch tới lần chạy toàn bộ của đêm đó | Tech | Đồng bộ toàn bộ mỗi đêm | Đã chấp nhận, lệch tối đa một ngày |
| 4 | Việc chụp trạng thái cuối ngày lỡ một ngày làm báo cáo quá khứ lệch | Tech | Ghi log, cảnh báo khi lỗi | Đã chấp nhận, lệch tối đa một ngày |
| 5 | Người vừa là mentor vừa là thành viên tự chấm bài của mình | PO | Chặn tự chấm để đợt sau | Đã chấp nhận |
| 6 | UpLMS Ops chưa chạy được trên điện thoại cho màn theo dõi nhánh | Design | Dev kiểm sớm, trước `ORD-6` | Chưa |

## 9. Ý kiến phản đối
Không có.

## 10. Ký
| Vai | Người | Trạng thái | Ngày | Ghi chú |
|---|---|---|---|---|
| Design PIC | | Chưa xem | | |
| Tech PIC | | Chưa xem | | |
| QA PIC | | Chưa xem | | |

Trạng thái: Chưa xem, Có ý kiến, Đồng ý, Yêu cầu sửa.
