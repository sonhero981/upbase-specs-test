# Spec Delta

## Purpose

Cho nhân sự vận hành dựng và giữ cơ cấu nhóm học viên nhiều cấp của một tổ chức (tenant) trên UpLMS Ops: tạo, sửa, di chuyển nhánh, với luật mã nhóm, nguồn nhóm và số cấp tối đa cấu hình được.

## ADDED Requirements

### Requirement: US1 Tạo và sửa nhóm
Nhân sự vận hành có quyền quản lý nhóm SHALL tạo được nhóm nhiều cấp (tên, mã, mô tả, nhóm cha tuỳ chọn) và sửa nhóm tự tạo; hệ thống MUST giữ mã duy nhất trong tenant, không cho sửa mã, chỉ nhận nhóm cha cùng nguồn đang dùng, chặn nhánh vượt số cấp tối đa của tenant và không cho sửa nhóm nguồn Đồng bộ. Nguồn: PRD `## US1`, BR-1.1–1.6. TC-1..TC-7.

#### Scenario: AC d1 Tên nhóm bắt buộc, tối đa 255 ký tự
- **WHEN** người vận hành để trống Tên nhóm, nhập chỉ dấu cách, hoặc nhập quá 255 ký tự (qua form hoặc gọi API trực tiếp)
- **THEN** hệ thống chặn lưu, form báo *Tên nhóm không được để trống* với tên rỗng/chỉ dấu cách; ô có placeholder *Nhập tên nhóm* (TC-1, TC-2)

#### Scenario: AC d2 Mã nhóm duy nhất trong tổ chức (BR-1.1)
- **WHEN** người vận hành lưu nhóm có mã đã tồn tại trong cùng tenant (không phân biệt hoa thường)
- **THEN** hệ thống không lưu và báo *Mã nhóm đã tồn tại* gắn vào field Mã nhóm; cùng mã ở tenant khác vẫn lưu được; bấm Lưu hai lần liên tiếp chỉ sinh một nhóm (TC-3)

#### Scenario: AC d3 Mô tả không bắt buộc, tối đa 1000 ký tự
- **WHEN** người vận hành nhập Mô tả nhiều dòng quá 1000 ký tự (qua form hoặc API)
- **THEN** hệ thống chặn lưu; bỏ trống Mô tả vẫn lưu được (TC-1, TC-2)

#### Scenario: AC d4 Nhóm cha chỉ là nhóm tự tạo đang dùng (BR-1.2)
- **WHEN** người vận hành mở ô Nhóm cha và tìm kiếm, hoặc gọi API tạo nhóm với nhóm cha nguồn Đồng bộ hoặc đang Lưu trữ
- **THEN** ô chỉ liệt nhóm nguồn Tự tạo trạng thái Đang dùng, có tìm kiếm, tooltip *Để trống nếu đây là nhóm cấp cao nhất*; API từ chối nhóm cha khác nguồn hoặc đã lưu trữ; để trống thì nhóm thành gốc (TC-1, TC-4)

#### Scenario: AC d5 Nút Lưu mờ khi thiếu field bắt buộc
- **WHEN** form Tạo nhóm còn thiếu Tên nhóm hoặc Mã nhóm
- **THEN** nút *Lưu* mờ, không bấm được (TC-1)

#### Scenario: AC d6 Mã nhóm không sửa được sau khi tạo
- **WHEN** người vận hành mở Sửa một nhóm tự tạo, hoặc gọi API sửa kèm field mã
- **THEN** ô Mã nhóm mờ với tooltip *Mã nhóm không thay đổi được*; Tên, Mô tả, Nhóm cha lưu được; API bỏ qua field mã, mã giữ nguyên (TC-6)

#### Scenario: AC d7 Nhóm nguồn Đồng bộ không sửa được (BR-1.5)
- **WHEN** người vận hành mở chi tiết nhóm nguồn Đồng bộ, hoặc gọi API sửa nhóm đó
- **THEN** không hiện nút *Sửa*, thay bằng dòng *Nhóm này đồng bộ từ hệ thống nhân sự, không chỉnh sửa trên UpLMS*; API từ chối (TC-7)

#### Scenario: BR-1.3 BR-1.4 Số cấp tối đa theo tenant
- **WHEN** tạo nhóm con làm nhánh sâu hơn số cấp tối đa của tenant (mặc định 6, gốc là cấp 1), rồi quản trị tổ chức đổi số cấp tối đa của tenant đó và tạo lại
- **THEN** lần đầu bị chặn với thông báo *Nhánh này đã đạt số cấp tối đa*; sau khi tăng cấu hình thì tạo được; tenant khác giữ giới hạn của mình; đặt số cấp nhỏ hơn nhánh sâu nhất đang có hoặc ngoài 2..10 bị từ chối; người không phải quản trị tổ chức không đổi được cấu hình (TC-5)

#### Scenario: BR-1.6 Nguồn và trạng thái của nhóm mới
- **WHEN** người vận hành tạo nhóm
- **THEN** nhóm có nguồn Tự tạo và trạng thái Đang dùng; form không có ô chọn nguồn hay trạng thái (TC-1)

### Requirement: US2 Di chuyển một nhánh
Nhân sự vận hành SHALL di chuyển được một nhánh nguồn Tự tạo sang nhóm cha khác (kéo thả ở dạng cây hoặc sửa field Nhóm cha) sau khi hệ thống kiểm tra và người dùng xác nhận; hệ thống MUST chặn vòng, chặn vượt số cấp, chặn nhóm Đồng bộ, giữ nguyên thành viên và nội dung đã giao, và ghi lại mỗi lần di chuyển. Nguồn: PRD `## US2`, BR-2.1–2.6. TC-8..TC-12.

#### Scenario: AC d1 Kéo thả có báo hợp lệ
- **WHEN** người vận hành kéo một nhóm tự tạo qua các nhóm khác ở dạng cây
- **THEN** vị trí thả hợp lệ hiện viền xanh; không hợp lệ hiện viền đỏ kèm lý do; nhóm nguồn Đồng bộ không kéo được (TC-8, TC-9, TC-11)

#### Scenario: AC d2 Hộp xác nhận di chuyển
- **WHEN** người vận hành thả nhóm vào vị trí hợp lệ
- **THEN** hiện hộp xác nhận gồm tên nhánh, số nhóm con, số người bị ảnh hưởng, nhóm cha cũ và mới, nút *Di chuyển* và *Huỷ*; *Huỷ* không đổi gì; *Di chuyển* đặt nhánh dưới cha mới (TC-8)

#### Scenario: AC d3 Đổi nhóm cha ở form sửa
- **WHEN** người vận hành đổi Nhóm cha ở form sửa rồi lưu
- **THEN** hệ thống áp cùng bộ kiểm tra và cùng hộp xác nhận như kéo thả (TC-9)

#### Scenario: BR-2.1 Không di chuyển vào chính nó hoặc nhánh con
- **WHEN** di chuyển một nhóm vào chính nó hoặc vào nhóm thuộc nhánh con của nó (kéo thả, form hoặc API)
- **THEN** hệ thống chặn, báo *Không thể di chuyển một nhóm vào nhánh con của chính nó*, cây không đổi (TC-9)

#### Scenario: BR-2.2 Không vượt số cấp tối đa khi di chuyển
- **WHEN** di chuyển làm nhánh sâu hơn số cấp tối đa của tenant
- **THEN** hệ thống chặn và báo rõ nhánh sẽ sâu bao nhiêu cấp; đúng bằng số cấp tối đa thì cho phép (TC-10)

#### Scenario: BR-2.3 Nhóm Đồng bộ không di chuyển bằng tay
- **WHEN** di chuyển nhóm nguồn Đồng bộ, hoặc thả nhóm tự tạo vào nhóm Đồng bộ (kéo thả hoặc API)
- **THEN** hệ thống từ chối (TC-11)

#### Scenario: BR-2.4 BR-2.5 Giữ thành viên và nội dung đã giao
- **WHEN** một nhánh được di chuyển thành công
- **THEN** mọi nhóm trong nhánh giữ nguyên thành viên; không ai được ghi danh hay gỡ khỏi lớp lúc di chuyển; nội dung giao ở cấp trên mới chỉ áp cho người vào nhánh sau đó (TC-8; phần nội dung đã giao kiểm ở B04 qua TC-12)

#### Scenario: BR-2.6 Ghi lại mỗi lần di chuyển
- **WHEN** một nhánh được di chuyển thành công
- **THEN** hệ thống lưu nhánh nào, cha cũ, cha mới, người làm và thời điểm; bản ghi truy vấn được (chưa có màn đọc ở intent này) (TC-8)
