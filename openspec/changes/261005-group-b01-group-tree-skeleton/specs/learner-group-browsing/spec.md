# Spec Delta

## Purpose

Cho nhân sự vận hành tìm và xem nhóm học viên của tổ chức trên UpLMS Ops ở dạng cây hoặc bảng, với số thành viên tính cả nhánh, tìm kiếm có đường dẫn từ gốc và nhóm lưu trữ ẩn mặc định ở mọi màn chọn nhóm.

## ADDED Requirements

### Requirement: US6 Xem danh sách nhóm
Nhân sự vận hành có quyền xem nhóm SHALL xem được danh sách nhóm của tenant mình ở dạng cây (tải dần theo nhánh) hoặc bảng (lọc, sắp xếp, phân trang); số thành viên MUST tính cả nhánh con, không tính tài khoản kiểm thử, người nghỉ việc và nhóm con lưu trữ; nhóm lưu trữ MUST ẩn mặc định ở mọi màn chọn nhóm. Nguồn: PRD `## US6`, BR-6.1–6.5. TC-35..TC-40, TC-105, TC-106.

#### Scenario: AC d1 Công tắc dạng xem nhớ lựa chọn
- **WHEN** người vận hành mở Danh sách nhóm lần đầu, chuyển sang *Bảng*, rồi tải lại trang
- **THEN** lần đầu mở ở *Cây*; sau khi tải lại vẫn ở *Bảng* (TC-35)

#### Scenario: AC d2 Cây tải dần theo nhánh (BR-6.1)
- **WHEN** người vận hành mở dạng cây rồi bấm mũi tên một nhóm
- **THEN** ban đầu chỉ hiện nhóm gốc đã gấp; bấm mũi tên chỉ tải nhánh con trực tiếp của nhóm đó, không tải cả cây (TC-35)

#### Scenario: AC d3 Mỗi dòng của cây
- **WHEN** cây hiển thị một nhóm
- **THEN** dòng có tên nhóm, số thành viên, và nhãn nguồn nếu nhóm nguồn Đồng bộ (TC-35)

#### Scenario: AC d4 Cột của bảng
- **WHEN** người vận hành xem dạng bảng
- **THEN** bảng có đủ cột Tên nhóm · Mã · Nguồn · Số thành viên · Người quản lý · Trạng thái · Cập nhật lần cuối (TC-36)

#### Scenario: AC d5 Số thành viên tính cả nhánh (BR-6.2, BR-6.3)
- **WHEN** một nhóm có thành viên trực tiếp và thành viên ở nhóm con, trong đó có tài khoản kiểm thử, người nghỉ việc và một nhóm con đã lưu trữ
- **THEN** số thành viên ở cả hai dạng xem gồm người của mọi nhóm con đang dùng, đếm mỗi người một lần, không tính tài khoản kiểm thử, người nghỉ việc, thành viên nhóm con lưu trữ; hover hiện tooltip *Gồm thành viên của các nhóm con* (TC-37; đếm một lần theo TD `### API-1`, TC-37 còn chờ PO [2.61 Q1])

#### Scenario: AC d6 Tìm kiếm hiện đường dẫn từ gốc (BR-6.4)
- **WHEN** người vận hành tìm theo tên hoặc mã ra một nhóm con
- **THEN** kết quả hiện đường dẫn đầy đủ từ gốc, ví dụ `ECOM / Trung tâm vận hành 1 / Growth 1`, ở cả hai dạng xem (TC-38)

#### Scenario: AC d7 Bộ lọc bảng kết hợp
- **WHEN** người vận hành lọc bảng theo Nguồn, Cấp, Trạng thái, Người quản lý cùng lúc
- **THEN** bảng chỉ còn nhóm thoả mọi điều kiện; không nhóm nào thoả thì hiện trạng thái rỗng (TC-36)

#### Scenario: AC d8 Sắp xếp bảng
- **WHEN** người vận hành bấm sắp xếp theo tên, số thành viên hoặc ngày cập nhật
- **THEN** bảng sắp đúng theo cột đã chọn, tăng hoặc giảm (TC-36)

#### Scenario: AC d9 Phân trang bảng
- **WHEN** tenant có hơn 20 nhóm và người vận hành xem dạng bảng
- **THEN** mỗi trang mặc định 20 dòng, sang trang 2 hiện phần còn lại (TC-36)

#### Scenario: AC d10 Nhóm lưu trữ ẩn mặc định (BR-6.5)
- **WHEN** tenant có nhóm Lưu trữ và người vận hành xem danh sách hoặc mở ô chọn nhóm
- **THEN** nhóm lưu trữ ẩn mặc định; bật *Hiện nhóm đã lưu trữ* thì hiện chữ xám kèm nhãn *Lưu trữ*; ô chọn nhóm (Nhóm cha và các ô chọn nhóm khác) không bao giờ liệt nhóm lưu trữ (TC-39)

#### Scenario: Đa tenant
- **WHEN** staff tenant B xem danh sách, tìm theo mã nhóm của tenant A, hoặc gọi API chi tiết nhóm của tenant A
- **THEN** không thấy và không đọc được nhóm của tenant A (TC-40)

#### Scenario: Quyền xem và quản lý nhóm
- **WHEN** vai trò không có quyền nhóm mở Ops
- **THEN** không thấy menu Nhóm; vai trò có quyền mới thấy; quyền cũ của mọi vai trò không đổi. API từ chối vai trò không có quyền [NEEDS CLARIFICATION - TD Assumptions #3 để `tags: []` nên API mở cho mọi staff tới khi BA điền `tags`; TC-105 kỳ vọng API từ chối ngay. B01 có phải pass phần API không, hay để tới khi BA điền `tags`?] (TC-105)

#### Scenario: Menu nhóm cũ
- **WHEN** người vận hành tìm menu Recipients List hoặc tạo thông báo chọn nhóm cũ
- **THEN** menu Recipients List ẩn; màn tạo thông báo vẫn chọn được nhóm cũ và gửi được (TC-106)
