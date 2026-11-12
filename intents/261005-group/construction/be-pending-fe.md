# Phần BE còn thiếu mà FE đang chờ

Lập ngày 2026-11-02, soát lại cùng ngày sau commit `e32176a`. Gom mọi chỗ FE
phải đi vòng vì BE chưa có, để lane BE làm một lượt thay vì nhặt rải rác trong
`tasks.md`, `progress.md` và `CLAUDE.md`.

**Cách đọc**: cột *FE đang làm gì* là cách sống tạm hiện tại. Cột *Xong thì xoá
gì* là việc duy nhất phải làm ở FE khi BE giao — đã cố ý gói vào một chỗ.

## 1. Chặn tiêu chí chấp nhận — làm trước

| # | Thiếu | Hệ quả | FE đang làm gì | Xong thì xoá gì |
|---|---|---|---|---|
| B1 | `member_count` trong `GroupPathItemDto` (`GET groups/options`) | `BR-21.5` cần tên + đường dẫn + số người nhận trên một dòng, mà `GET groups` có số thì không có `path` | Gọi thêm `GET groups?status=ACTIVE&page_size=100` rồi ghép theo `id` | Hàm `fetchCountFallback` trong `features/notification/src/hooks/useRecipientGroups.ts`, và dấu `?` của `member_count` trong `ILearnerGroupPathItem` |
| B2 | `q` trong `GroupMemberListQueryDto` (`GET groups/:id/members`) | `SCR6` chỉ lọc được **trên trang hiện tại**, sang trang là mất kết quả | Lọc phía client trong `useGroupMembers` | Nhánh lọc client trong `useGroupMembers` |
| B4 | `performed_by` và `id` trong `GroupMembershipLogItemDto` | Cột *Performed by* của `SCR17` luôn ghi *Hệ thống* | `id` ghép từ `occurred_at + user_id + group_id + action` | Hàm ghép `id` và giá trị cứng *Hệ thống* trong `api-adapter.ts` |
| B5 | Số thứ ba trong `GroupMemberRemovePreviewDto` | Câu thứ ba của `BR-3.7` (người còn thuộc nhóm khác cùng được giao lớp đó) bị bỏ | Không hiện câu đó | — |
| B6 | Cờ nhóm rỗng trong preview giao lớp | `EC-16` không cảnh báo được | `emptyWithoutCascade` để cứng `false` | Giá trị cứng đó |

## 2. Lệch hình dữ liệu — sửa rẻ, nên gộp luôn

| # | Thiếu | FE đang làm gì |
|---|---|---|
| B7 | `group-member.controller.ts:192` trả `{ log_id }`, trong khi `class`, `staffs`, `users`, `staff-position` đều trả `{ logId }` | `ModalImport` đọc `logId ?? log_id`. Đổi xong thì bỏ nhánh `??` |
| B8 | Dòng `JOINED` do nhập tệp trả `reason: null` | Nhật ký hiện *Manual* thay vì *Imported*. BE chỉ ghi lý do cho nhánh rời nhóm |
| B9 | `import_logs.status = FAILED` ngay cả khi phần lớn dòng chạy được (2/4 thành công vẫn `FAILED`) | FE không đọc trường này nên chưa hỏng gì, nhưng tên trạng thái gây hiểu nhầm |
| B10 | `GroupListItemDto` thiếu `allowed_actions`; `GroupListQueryDto` thiếu `include_archived` | `GroupDetailDto` đã có `allowed_actions`, danh sách thì chưa |
| B11 | `GET notifications` **không trả** `notification_groups`, chỉ `id, title, type, status` | Cột *Send to* của bảng danh sách thông báo luôn hiện `-`. FE đã viết sẵn theo hình đích, BE trả là cột tự hiện |
| B15 | `AssignableClassQueryDto` (`GET groups/assignable-classes`) chỉ **đánh dấu** `is_assigned`, không có tham số loại trừ. Hộp chọn mentor có `to_add`, hộp chọn học viên có `except_user_id`, đều để server loại | Modal *Assign classes* lọc `!isAssigned` ở FE sau khi đọc `page_size: 100` lớp đầu. Lớp đã giao chiếm chỗ của lớp chưa giao nằm ngoài trang đầu, nên phân trang và `total` lệch khi có hơn 100 lớp. Xoá dòng `.filter` trong `useClassOptions` khi BE giao |
| B17 | `GroupTreeItemDto` (`GET groups/tree`) **không trả quản lý** và không có `has_no_manager`, trong khi `GroupListItemDto` (`GET groups`) có cả hai. `SCR1` dạng Cây đòi nhãn `No manager` khi trống quản lý (`AC13.1`) | Hàng Manager ở thẻ cây bị ẩn cùng cờ `SUPERVISORS_TAB`. Bật cờ lên mà BE chưa thêm thì hàng này luôn ra `—` vì FE gán cứng `managers: []`. Phải thêm hai trường vào DTO cây trước khi bật cờ |
| B18 | `GroupListQueryDto` (`GET groups`) **không có `q`**; chỉ `groups/search` và `groups/options` tìm được theo tên hoặc mã | Ô tìm của dạng Bảng ở `SCR1` không lọc gì: từ khoá chỉ nằm trong khoá truy vấn, không gửi đi. Cần thêm `q` vào DTO danh sách (mẫu `applyKeyword` có sẵn ở service). Dạng Cây không bị ảnh hưởng vì nó tìm trên cây đã tải |
| B20 | `GroupMembershipLogItemDto` (`GET groups/membership-logs`) **không có người thao tác** | Cột `Performed by` luôn ra "Hệ thống" nên FE đã bỏ cột (03/11). BE trả người thao tác (id + tên, hoặc `SYSTEM` cho tác vụ tự động) thì thêm cột lại |
| B21 | `GroupCandidateItemDto` (`GET groups/:id/candidates`) chỉ trả họ tên, mã NV, email, `is_member`, `roles_in_group`, `related_groups`. **Thiếu `account_status`** (và ngày vào nhóm với người đã là thành viên) | Modal Add members muốn giống Member list (Full name · Email · Subgroup · Joined date · Account status). Hiện chỉ có Full name, Email, Current group (từ `related_groups`). Người dùng chốt 03/11: thiếu phần nào thì xin BE. Cần thêm `account_status` (bắt buộc, để người nghỉ việc/bị khoá nhìn thấy được), `joined_at` (tuỳ chọn) |
| B12 | Không có cách tra nhóm theo **danh sách id** | Mở thẳng một URL đã lọc mà nhóm nằm ngoài trang đầu thì ô lọc hiện UUID thay vì tên. Hiện nạp sẵn một trang để che phần lớn trường hợp |

## 3. BE đã giao

| # | Thiếu | Giao ở | FE đã ghép |
|---|---|---|---|
| B3 | `candidates` loại hẳn người đã ở trong nhóm | `e32176a` — mỗi dòng kèm `is_member`, `roles_in_group`, `related_groups` (`ANCESTOR`/`DESCENDANT`) | `AC3.1` dựng xong: `PeoplePickerModal` khoá ô chọn và hiện lý do ngay dưới tên. `related_groups` nhiều hơn phần đã xin, dùng luôn để chặn cả người ở nhóm tổ tiên, hậu duệ thay vì để BE lặng lẽ bỏ qua |
| — | Dòng vượt sức chứa lớp (`AC7.5`, `BR-7.6`) | `f6943d1` — `GET /classes/:id/students` nay trả `meta.capacity`, `current_count`, `is_over_capacity` | Dòng cảnh báo ở `ListStudent` của tab `Students` lớp giờ đọc số của BE, không tự suy từ `classDetail.capacity` + `totalStudents` nữa. Chữ cũng đổi về đúng khuôn của PRD |
| — | Cột nguồn ghi danh (`AC7.3`, `BR-7.9`) | `f6943d1` — mỗi học viên kèm `source_groups` | Thêm cột *Nguồn* ở `ListStudent`, hiện tên các nhóm đã giao lớp mà học viên đang là thành viên; trống hiện `—`, nghĩa là lượt thêm tay |

## 4. Chưa có module — còn mock hoàn toàn

| # | Thiếu | Ảnh hưởng |
|---|---|---|
| B13 | `apps/ops/src/groups/relations/` còn `.module.ts` rỗng | Tab **Người phụ trách** (quản lý, mentor) chạy mock |
| B14 | `apps/ops/src/groups/report/`, `tracking/`, `user-relations/` còn rỗng | Tab **Báo cáo** chạy mock |

## 5. Ghi chú

- `GroupLeaveReason` của BE có **7** giá trị, `toMemberReason` của FE map 4; hai
  giá trị `ROLE_REVOKED` và `RESPONSIBILITY_TRANSFERRED` rơi vào `default →
  MANUAL`. Hai cái đó thuộc người phụ trách chứ không phải học viên, và PRD chỉ
  nêu 5 lý do, nên để nguyên — nhưng nếu chúng lọt vào nhật ký học viên thì sẽ
  bị dán nhãn sai.
- `AC21.2` (người nhận gồm cả nhánh con, loại tài khoản kiểm thử và đã khoá) và
  `AC21.3` (một người ở hai nhóm chỉ nhận một thông báo) là **luật phía BE**.
  FE không kiểm được, phải đọc hộp thư thật.
- DB ở máy có **0 lớp** mặc định. 02/11 đã seed một danh mục + một khoá +
  hai lớp (sức chứa 1 và không giới hạn), đo xong luồng giao lớp đầu-cuối cho
  `UPLND-427` rồi dọn. Câu `BR-4.4` của `6.5` vẫn chưa đo vì cần người đang
  **học dở** một lớp giao qua nhóm.
- `GET/PUT /groups/settings` BE đã có đủ (`group-feature-settings.controller.ts`)
  trả `{ hr_sync_enabled, class_assignment_enabled }`. **FE không khai client**
  **theo đúng PRD `DEC121`**: *"Đợt này chưa có màn cấu hình hai cờ; nhân sự
  kỹ thuật bật theo từng tổ chức"*. Cờ `class_assignment_enabled` phải bật tay
  qua DB khi muốn giao lớp — luồng onboarding tenant, không phải luồng Ops.
- Luồng ghi danh qua Kafka (`process_group_enrollment_requested`) consumer có
  cache Redis cho feature settings. Khi bật cờ trong DB, phải **xoá key**
  `group:feature-settings:<tenant_id>` thì consumer mới đọc giá trị mới.
- **03/11:** BE commit `5b94c0e` cho `code` tuỳ chọn ở `POST /groups`, bỏ trống thì tự sinh từ tên (bỏ dấu, viết hoa, nối `_`, trùng thì `_1`, `_2`…). FE đã nối: ô `Group code` ẩn khi tạo nhóm, không gửi `code`; khi sửa vẫn hiện mã, khoá.
- **03/11:** BE commit `37d18fe` trả `parent: { id, name, code } | null` ở `GroupListItemDto` (B19 đã giao). FE đọc thẳng từ DTO cho cột `Parent group`, bỏ phần suy từ cây đã làm tạm.
