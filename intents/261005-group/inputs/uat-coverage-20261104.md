---
intent: 261005-group
artifact: uat-coverage-audit
status: draft
date: 2026-11-04
baseline: prd@0.11 draft, requirements@0.7 draft, impact-matrix@0.8 draft, CR9 đang mở
---
# Đối chiếu nhận xét UAT với PRD Group

## 1. Kết luận và cách đọc

Sau khi đối chiếu bản PO rút gọn, đã đồng bộ PRD về mã nhóm tự tạo do hệ thống cấp, nhãn Graph và mặc định Table, phạm vi xem Membership log theo nhóm đang chọn. Account status vẫn thiếu định nghĩa và chưa tự bổ sung trạng thái. PO đã chốt giữ tên cột Reason và bỏ cột Performed by khỏi bảng nhật ký; dữ liệu người thao tác vẫn được lưu để truy vết. Cách đếm Subgroups, Group by Parent, phạm vi nhánh con của log và lối nhật ký từ hồ sơ người được để sau; không coi là yêu cầu phải chốt trong đợt này.

Đây là bản kiểm tra độ phủ tài liệu, không phải biên bản xác nhận UAT đã đạt. “Đã có” nghĩa là PRD đã mô tả, không chứng minh giao diện hoặc xử lý thực tế đã đúng. Các phần mới được áp dụng vào PRD được ghi rõ tại từng mục; các phần còn lại chỉ là đối chiếu hoặc đề xuất. File thiết kế chưa được sửa.

Nguồn đối chiếu: PRD v0.11 đang sửa theo CR9, requirements v0.7 và impact-matrix v0.8 cùng bản nháp; bản rà soát prd-group-revision-analysis-20261103.md; decisions.md; ux-design.md; thiết kế giao diện fe-technical-design.md; requirements.md; bốn ảnh và danh sách nhận xét PO cung cấp. Account status được đối chiếu thêm với domain/06-user-account.md như một bản chụp kiến thức, chưa xác minh lại nguồn sống nên không dùng để tự chốt quy tắc mới.

Các trạng thái trong bảng: Đã có; Một phần; Chưa có hoặc trái PRD; Thuần giao diện; Cần làm rõ; Để sau theo quyết định trước. Các mục trùng nhau trong danh sách UAT được đối chiếu cùng một nơi, không tạo yêu cầu mới cho mỗi lần nhắc lại.

## 2. Danh sách nhóm: Graph và Table

| Nhận xét UAT | Trạng thái hiện tại | Vị trí và việc cần làm |
|---|---|---|
| Bỏ code trên Tree | Đã có trong đặc tả hiển thị | US6 xem danh sách nhóm, dòng SCR1 dạng Cây: không liệt kê mã nhóm trong nội dung mỗi dòng. Nếu giao diện vẫn có code thì sửa giao diện; không xoá dữ liệu mã nhóm hoặc cột Code ở Table. |
| Thêm subgroup và members trên Tree | Một phần; cách đếm Subgroups để sau | US6 đã có số Members cộng dồn không trùng toàn nhánh; chưa có số Subgroups. PO chưa chốt đếm nhóm con trực tiếp hay toàn bộ hậu duệ và yêu cầu để sau. Không tự thêm một công thức hoặc tiêu chí đếm Subgroups trong đợt này. |
| Icon Learner Groups bé | Thuần giao diện | Design điều chỉnh kích thước và khả năng nhận diện; PRD không cần quy định số pixel. |
| Đổi Tree thành Graph | Đã đồng bộ PRD | Theo câu trả lời “Chỉ đổi tên thành Graph”, các tham chiếu giao diện hiện hành dùng Graph; giữ cấu trúc phân cấp, mở nhánh và kéo thả. Không phát sinh sơ đồ mới. |
| Mặc định Table | Đã đồng bộ PRD | Luồng chính US6, AC6.1 và lựa chọn dạng xem thống nhất Table trong lần mở đầu; lần sau nhớ lựa chọn gần nhất. Graph là tên mới của cây hiện có. |
| Đổi vị trí nút Graph/Table | Thuần giao diện | Design bố trí lại điều khiển. PRD chỉ cần tên hai lựa chọn và mặc định, không cần cố định vị trí bằng toạ độ. |
| Archived cạnh Manual, tên dài rút gọn và hover | Đã có | US6, AC6.3 hiển thị đường dẫn và nhãn, dòng SCR1 dạng Cây. Giữ cả nguồn Synced đối với nhóm đồng bộ; không đổi ngược nhãn nguồn người dùng đã sửa. |
| Graph có filter như Table | Đã có | US6, AC6.4 lọc trạng thái, AC6.5 kết hợp bộ lọc và dòng Bộ lọc cả hai dạng. Đổi nhãn Tree sang Graph không làm mất hành vi này. |
| Tự sinh code trong Table | Đã đồng bộ yêu cầu tạo nhóm và PRD | Mã nhóm tự tạo do hệ thống cấp trong US1, Table chỉ hiển thị mã. Không sinh mã riêng ở Table hoặc đổi mã nhóm đã tồn tại. |
| Bỏ Show archived | Đã có | US6 và phần hiển thị nhóm lưu trữ của US14. Dùng Status: Active, Archived, All; không còn công tắc riêng. |
| Thêm Parent trong Table | Đã có | US6 ghi Parent group là nhóm cha trực tiếp, nhóm gốc No parent; tooltip đường dẫn để phân biệt tên trùng. |
| Có thể group theo Parent | Để sau | PO chưa chốt có làm Group by Parent không và yêu cầu để sau. Giữ cột Parent group đã có; không tự bổ sung chức năng gom nhóm trong đợt này. |
| Vị trí các cột và Source thành badge sau tên | Đã có phần chính | US6: Group name, Code, Parent group, Members, Người quản lý, Status, Last updated; nguồn là badge cạnh tên, không còn cột Source riêng. Cột Người quản lý đang được giữ vì chưa có quyết định bỏ. Chỉ cần sửa tiếp nếu PO muốn bỏ cột này. |
| Bỏ Level filter | Đã có | US6 ghi rõ không có Level; bộ lọc chung còn Nguồn, Trạng thái, Người quản lý. |

## 3. Tạo, sửa và chi tiết nhóm

| Nhận xét UAT | Trạng thái hiện tại | Vị trí và việc cần làm |
|---|---|---|
| Tự sinh code khi tạo nhóm | Đã đồng bộ requirements, impact-matrix và PRD | US1 không yêu cầu người dùng nhập mã; hệ thống cấp mã duy nhất trong tổ chức, không cho sửa sau tạo. Giữ mã hiện có và cách nhận diện nhóm đồng bộ; không tự chốt định dạng hoặc cách sinh mã kỹ thuật. |
| Kéo dài input text | Thuần giao diện | Design điều chỉnh độ rộng field. Giữ yêu cầu độ dài dữ liệu và validate hiện có; tăng chiều rộng ô nhập không đồng nghĩa tăng giới hạn ký tự. |
| Logic chuyển nhóm và nhánh có người học | Đã có phần đã chốt | US2 di chuyển nhánh: vẫn cho chuyển khi có hoạt động học, giữ thành viên, lượt ghi danh, tiến độ, kết quả; không hồi tố lớp của cha mới; tính lại quản lý kế thừa và phạm vi xem dữ liệu. Không đồng nhất di chuyển nhánh với điều chuyển học viên. |
| Thông báo khi chuyển nhánh | Đã có | SCR3 hộp xác nhận có chuỗi tiếng Anh PO đã chọn, tên cha cũ và mới, số nhóm con và số người không trùng. Không tự thêm email mới. |

## 4. Members và Add members

| Nhận xét UAT | Trạng thái hiện tại | Vị trí và việc cần làm |
|---|---|---|
| Members bỏ Staff code | Đã có | US3, SCR6. Bảng Full name, Email, Subgroup, Joined date, Account status; search theo tên hoặc email. |
| Member list thay Department bằng Subgroup | Đã có | US3, dòng Subgroup đã phân biệt người trực tiếp thuộc nhóm và người thuộc nhánh con. Người thuộc nhánh con không gỡ tại nhóm cha. |
| Xem thứ tự Member list | Đã có | Checkbox, #, Full name, Email, Subgroup, Joined date, Account status, thao tác theo quyền. Joined date khi một người có nhiều quan hệ nhóm con còn mở ở câu hỏi #22. |
| Add Member đồng bộ Staff code, member, department | Đã có theo ảnh mới nhất | US3, SCR7: Checkbox, #, Full name, Email, Current groups. Không có Staff code, Department, Phone hoặc Date. Full name thống nhất với Members; Current groups ở số nhiều vì một người có nhiều nhóm. Mẫu ảnh mới thay mẫu Add Student cũ, không khôi phục các cột cũ. |
| Check Account status | Một phần | PRD mới ghi cột và bộ lọc, chưa định nghĩa các nhãn, nguồn trạng thái, ý nghĩa và quan hệ với người nghỉ việc. KB mô tả tài khoản Active/Block nhưng là bản chụp; không tự coi Block đồng nghĩa nghỉ việc. Cần đối chiếu nguồn vùng tài khoản trước khi chốt; không tự thêm trạng thái tài khoản mới. |

## 5. Membership log và các cột nhật ký

Phần PO giữ lại trong bản đã chỉnh gồm giới hạn xem log theo nhóm hiện tại và câu hỏi về tên cột Reason. Các nhận xét đã bị PO bỏ khỏi bảng không được khôi phục vào phạm vi sửa.

| Nhận xét UAT | Trạng thái hiện tại | Vị trí và việc cần làm |
|---|---|---|
| Log chỉ của nhóm đang xem | Đã chốt và đồng bộ PRD | Khi mở nhật ký từ chi tiết nhóm, phạm vi cố định theo nhóm đang chọn, không xoá điều kiện hoặc đổi sang nhóm khác trong ngữ cảnh đó. Lối vào từ hồ sơ người giữ hành vi hiện có. Log nhánh con và thay đổi lối nhật ký từ hồ sơ người tiếp tục để sau; không tự chuyển log thành tab riêng. |
| Reason và các giá trị | Đã đồng bộ với PRD | Giữ tên cột Reason và đúng năm giá trị hiện có: Thêm tay, Nhập tệp, Đồng bộ, Nghỉ việc, Điều chuyển (Transferred). Không dùng các nhãn tiếng Anh từng đề xuất trước đó. Bốn chuỗi tiếng Anh đầu vẫn do Design dịch như PRD, chưa coi là đã được PO chốt. |
| Performed by | Đã bỏ khỏi bảng nhật ký trong PRD | Bỏ cột hiển thị Performed by cùng mô tả hiển thị System. Thông tin người thao tác vẫn được lưu theo yêu cầu dữ liệu hiện có; không xoá lịch sử hoặc thay quy tắc ghi log. |

### 5.1. Reason và các giá trị theo PRD

Giữ tên cột Reason, nghĩa là lý do vào hoặc rời nhóm. Action thể hiện Joined hoặc Left group. Bảng nhật ký không có cột Performed by; thông tin người thao tác vẫn được lưu theo yêu cầu dữ liệu.

| Giá trị trong PRD | Nhãn tiếng Anh trong PRD |
|---|---|
| Thêm tay | Chưa chốt bản dịch; Design dịch theo PRD |
| Nhập tệp | Chưa chốt bản dịch; Design dịch theo PRD |
| Đồng bộ | Chưa chốt bản dịch; Design dịch theo PRD |
| Nghỉ việc | Chưa chốt bản dịch; Design dịch theo PRD |
| Điều chuyển | Transferred |

Danh sách trên khớp dòng Reason trong bảng giao diện SCR17 của US15 nhật ký. Không dùng nhãn đề xuất mới thay các giá trị này và không lấy Reason của nhật ký làm lý do Skipped của giao lớp.

## 6. Assigned Classes và Assign classes

| Nhận xét UAT | Trạng thái hiện tại | Vị trí và việc cần làm |
|---|---|---|
| Có người học rồi có Remove lớp được không | Đã có quyết định và đã sửa | US7, BR-7.10 điều kiện gỡ lớp và AC7.6: chặn khi phát sinh hoạt động học, kể cả đã hoàn thành; chỉ ghi danh chưa đủ để chặn; kiểm tra lại trước khi hoàn tất. Còn định nghĩa cụ thể hoạt động học và hệ quả với lượt chưa học ở câu hỏi #21. |
| Enrolled via this group là gì | Đã được PO chốt và đã sửa | US7, SCR11: Enrolled by group đếm lượt ghi danh có nguồn nhóm đang xem; mỗi lượt tính một lần tại nhóm đó, không tính lượt chỉ có nguồn thủ công hoặc nhóm khác. Không dùng số này làm điều kiện chặn Remove. Phạm vi và vòng đời nguồn còn ở câu hỏi #22. |
| Already in class là gì | Đã có | US7: đã có lượt ghi danh ở đúng lớp, dù thêm tay hoặc qua nhóm khác; không có nghĩa đã học, không tính chỉ vì đã học cùng khoá ở lớp khác, không tạo lượt ghi danh trùng. |
| Khối Preview và các nhãn | Đã có nhưng cần đối chiếu giao diện | New enrollments, Already in class, Skipped. Đếm phân biệt theo lớp; tổng nhiều lớp là lượt ghi danh. Auto-enroll không làm mất nghĩa vụ giao cho thành viên hiện tại. |
| Lý do Skipped | Chưa đủ định nghĩa | Câu hỏi #21: không tự coi lớp đầy, thành viên ngoài phạm vi Cascade hoặc người đã ở lớp là Skipped. Không lấy các Reason của nhật ký để điền. |

## 7. Danh sách sửa tài liệu tiếp theo và tác động

| Nhóm việc | Artifact cần đối chiếu hoặc sửa | Giới hạn |
|---|---|---|
| Mã tự sinh | Đã đồng bộ requirements v0.7, impact-matrix v0.8 và US1 trong PRD v0.11 | CR9 mở rộng điểm re-entry tới 2.3, đối chiếu 2.31; các bản sửa là draft. Không đổi mã cũ hoặc quy tắc đồng bộ. |
| Graph/Table, mặc định khi truy cập giao diện là Table | Đã đồng bộ US6 danh sách nhóm trong PRD | Graph chỉ đổi nhãn; mặc định Table lần đầu, nhớ lựa chọn gần nhất. Cách đếm Subgroups để sau. |
| Membership log theo nhóm | Đã đồng bộ US15 nhật ký và yêu cầu RC-11 | Giới hạn nhóm hiện tại khi vào từ nhóm; giữ nguyên các mục để sau, không tự chuyển thành tab hoặc xoá lối vào theo người. |
| Account status | US3 thành viên, nguồn tài khoản hiện có và phần câu hỏi mở liên quan | Phân biệt trạng thái tài khoản, quan hệ thành viên và nghỉ việc; không tự đồng nhất. |

Các mục đã được PRD bao phủ giữ nguyên, tránh sửa lại chỉ vì danh sách UAT nhắc lần nữa. Các thay đổi trên nằm trong CR9 đang mở, không tạo CR riêng cho từng dòng. Đã mở rộng điểm re-entry tới 2.3 và đối chiếu 2.31 cho mã tự sinh; chưa duyệt lại hoặc publish các bản sửa.

## 8. Câu hỏi cần quyết

- Đã trả lời: Graph chỉ là đổi tên chế độ Tree hiện tại. Nguyên văn: “Chỉ đổi tên thành Graph”.
- Đã trả lời: “membership log chỉ cho xem nhóm hiện tại đang chọn”. Giới hạn ngữ cảnh xem theo nhóm được chọn; chưa suy phạm vi nhánh con.
- Để sau theo yêu cầu PO: Subgroups đếm con trực tiếp hay toàn bộ hậu duệ; có làm Group by Parent không; log của nhóm có bao gồm nhánh con không; giữ lối nhật ký từ hồ sơ người thế nào. Các nội dung này chưa được quyết và không làm điều kiện phải trả lời ngay của đợt sửa hiện tại.
- Đã chốt: giữ Reason, bỏ cột Performed by; các giá trị ở mục 5.1 khớp đúng PRD v0.11. Không còn giữ bộ nhãn tiếng Anh đề xuất khác với PRD. Bốn bản dịch chưa có vẫn để Design xử lý theo quy định trong PRD.

Các câu hỏi cũ của PRD về Skipped, hoạt động học, Joined date và vòng đời nguồn ghi danh vẫn còn hiệu lực ở phạm vi chưa được trả lời. Không đánh dấu hoàn tất chỉ vì đã thêm nhãn cột.

## 9. Kết quả đồng bộ lần này

Đã sửa mục 5.1 theo đúng giá trị của PRD và đồng bộ các điểm đã được giữ lại: mã tự sinh, Graph/Table, giới hạn nhật ký theo nhóm và badge nguồn giữa US5 với US6. Cập nhật các trạng thái trong bản audit để không ghi “chưa sửa” đối với phần đã áp dụng. Account status và các định nghĩa còn mở không được tự điền; các mục PO xoá hoặc để sau không được đưa lại. Các file thiết kế và bản publish chưa thay đổi.
