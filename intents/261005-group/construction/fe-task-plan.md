---
intent: 261005-group
artifact: fe-task-plan
feature: LMS-F002
version: 0.30
status: draft
inputs: prd@0.7, fe-technical-design@2.2, ux-design@0.1, be-technical-design (23/10/2026)
repos: ops-fe (chính), lms-fe (US17)
owner: Nguyễn Hùng Sơn
---
# Chia task Frontend — Nhóm học viên (Group)

Bản chia việc cho lane FE, dựng theo **đường ngắn** (DEC-T1): lấy Unit U1–U7 và ánh xạ US → component có sẵn
trong `inception/tech-design/fe-technical-design.md` mục 7, đối chiếu lại với **PRD v0.7** để bắt phần CR7 mà
thiết kế v2.2 chưa phủ. Thay cho 2.7 Units Generation, 2.9 Delivery Planning và phần kế hoạch của 3.5.

Luật nghiệp vụ nằm ở PRD, cách hiện thực nằm ở thiết kế FE. File này **chỉ chia việc và xếp thứ tự**, không chép lại hai nơi đó.

## 1. Điểm xuất phát

| | |
|---|---|
| Nhánh nền | Cắt mới từ `ops-fe/staging` |
| Nhánh demo cũ | `feature/manager-group` — **port sang dùng lại** (DEC-T4). 48 file trong `features/group/`, `package.json` đã đúng convention hiện tại. Nhánh lùi `staging` 13.016 commit nhưng code trong package không lạc hậu |
| `features/group/` trên staging | **Rỗng**, chưa có source. Dựng mới từ đầu |
| Cách làm | **Port demo rồi sửa theo PRD v0.7**, không dựng lại từ đầu. **Mock-first**: viết `group.service.ts` + `mock-data.ts` in-memory có độ trễ giả, UI chạy đủ trên mock; khi có contract BE thì chỉ thay thân hàm service bằng `useFeature().GroupAPI`, không sửa component/hook (thiết kế FE mục 4) |
| Chưa mở được change OpenSpec | `ops-fe` chưa có thư mục `openspec/` (xem `domain/system-map.md` mục "Nối store"). Tạm theo dõi task bằng file này và Jira |

## 2. Cái đã lộ ra khi đối chiếu PRD v0.7

| # | Việc | Vì sao |
|---|---|---|
| G1 | **US21 chưa có trong thiết kế FE v2.2** | v2.2 dựa trên PRD v0.6; US21 do CR7 thêm. Task US21 dưới đây dựng thẳng từ PRD v0.7, cần Tech PIC cập nhật thiết kế lên v2.3 |
| G2 | **Phải gỡ "nhóm người nhận" cũ của thông báo** | `BR-21.1`: nhóm cũ bỏ hẳn, không chuyển đổi. Code cũ nằm ở `features/notification/src/components/recipients/CreateGroupComponent.tsx`, `pages/recipients/ListGroupReceiver.tsx`, `routes.tsx`, `constant/index.ts` |
| G3 | **Menu `LIST_GROUP` hiện thuộc nhóm Thông báo** | `libs/hooks/src/permission/useMenuData.tsx:813` — đó là menu của nhóm người nhận cũ. Feature mới dùng `ID_SIDE_BAR.GROUP` riêng (thiết kế FE mục 1.3), không tái dùng id cũ |
| G4 | **`ux-design.md` chưa có mã màn cho ba thay đổi của US21** | Câu hỏi mở #19 của PRD. F6 chưa chốt được giao diện cho tới khi PO trả lời |

## 3. Phụ thuộc BE — quyết định Bolt nào chạy được ngay

Theo mục 13 của thiết kế FE. Cột *Chặn* là Bolt bị chặn **ở bước nối API thật**; mock vẫn dựng trước được.

| # | Phụ thuộc | Cần ai | Chặn |
|---|---|---|---|
| 1 | API contract đầy đủ cho `IGroupAPI` | BE | Mọi Bolt, chỉ ở bước bỏ mock |
| 2 | Danh sách quyền `gr_*` đầy đủ | BE · PO | F3, F6 |
| 3 | Cờ `isManager` trên profile | BE | F6 (US16) |
| 4 | Error code cho luật nghiệp vụ | BE | Hoàn thiện UX lỗi, mọi Bolt |
| 5 | `type` import `GROUP_MEMBER` + job import + file mẫu | BE · FE | F2 (US4) |

## 4.0 Một người làm — thứ tự chạy

FE hiện chỉ có **một người**: toàn bộ lane FE do Nguyễn Hùng Sơn làm, gồm cả phần đụng `features/user`,
`features/class-and-course` và `lms-fe`. Không có việc chạy song song, nên sáu đợt dưới đây là **một hàng đợi nối tiếp**.

Hai luật xếp thứ tự khi chỉ có một người:

1. **Không chờ BE.** Mọi task dựng trên mock trước. Task nào cần API thật thì làm phần UI và luật hiển thị trước,
   chừa lời gọi service; khi BE giao contract thì chỉ thay thân hàm trong `group.service.ts` (thiết kế FE mục 4).
2. **Việc bị chặn bởi người khác xếp sau cùng.** Task cần PO trả lời hoặc cần đụng module của team khác
   dồn về cuối, để phần tự quyết được chạy liên tục không đứt.

| Thứ tự | Nhóm | Vì sao ở đây |
|---|---|---|
| 1 | **F1** toàn bộ | Không phụ thuộc gì. Mở được `/groups` là có cái để demo và verify mọi task sau |
| 2 | **F2.1 → F2.4** cây, tạo/sửa | Port từ nhánh demo rồi rà theo PRD v0.7; nhẹ hơn dựng mới |
| 3 | **F2.6, F2.7, F2.9** thành viên, nhóm đồng bộ | Tiếp luồng chi tiết nhóm, không chặn |
| 4 | **F5.5, F5.6, F5.7** nhật ký, lưu trữ | Đọc dữ liệu đơn giản, hoàn thiện nốt chi tiết nhóm |
| 5 | **F3.1 → F3.5** quản lý, mentor trong module group | Phần trong `features/group`, tự làm được |
| 6 | **F4** giao nội dung | Độc lập, nằm gọn trong tab Nội dung |
| 7 | **F5.1 → F5.4** báo cáo | Nặng, nhưng không chặn ai |
| 8 | **F2.5** kéo-thả đổi nhóm cha | Nặng và dễ sinh lỗi; để sau khi cây đã ổn định qua nhiều đợt dùng |
| 9 | **F2.8** import theo tệp | Chờ BE #5 (`GROUP_MEMBER` + job import + file mẫu) |
| 10 | **F3.6, F3.7, F3.8** đụng `features/user`, `features/class-and-course` | Phải hẹn lịch với chủ module, dễ xung đột |
| 11 | **F6.4 → F6.6** US21 thông báo | Chờ PO trả lời câu hỏi mở #19, #15; và cần thiết kế FE v2.3 |
| 12 | **F6.1 → F6.3** `/my-team` | Chờ BE #3 (`isManager`) và #2 (quyền đọc theo quan hệ quản lý) |
| 13 | **F6.7** `lms-fe` US17 | Repo khác, làm cuối |

Mốc demo được: sau bước 1 (danh sách chạy), sau bước 3 (chi tiết nhóm đủ dùng), sau bước 6 (giao nội dung xong),
sau bước 8 (module group hoàn chỉnh trên mock).


## 4.1 Điểm trên Jira

**Từ 09/11/2026 điểm chỉ nằm ở story cha**, theo comment của PO (Bùi Đức Huy) so với baseline UPLND-404 = 3 điểm; một người làm trọn một story, không phân biệt BE hay FE, nên sub-task không chia điểm. Cột Điểm dưới đây là điểm sub-task ở Sprint 3 (đã làm xong, chỉ để tham khảo); sub-task Sprint 4 ghi "—".

| Task | Story | Nội dung | Điểm |
|---|---|---|---|
| UPLND-423 | UPLND-403 | Nền kỹ thuật, bỏ phòng ban | 0,5 |
| UPLND-424 | UPLND-402 | Port UI danh sách từ nhánh demo | 0,5 |
| UPLND-425 | UPLND-404 | Tab thành viên, nhập tệp, nhật ký | 0,5 |
| UPLND-426 | UPLND-405 | Thông báo theo nhóm | 0,5 |
| UPLND-427 | UPLND-406 | Giao nội dung, tự ghi danh | 1 |
| UPLND-428 | UPLND-407 | Kéo thả, lưu trữ, xoá | 1 |
| UPLND-429 | UPLND-408 | Nhóm đồng bộ chỉ đọc | — |
| UPLND-430 | UPLND-409 | Báo cáo hiện tại | — |
| UPLND-431 | UPLND-410 | Người phụ trách, kế thừa, chuyển | — |
| UPLND-432 | UPLND-411 | Mentor | — |
| UPLND-433 | UPLND-412 | Hồ sơ học viên trên Ops | — |
| UPLND-495 | UPLND-412 | Khối Quản lý của tôi trên LMS (tách từ UPLND-433) | — |
| UPLND-434 | UPLND-413 | `/my-team`, khung theo vai, 375 px: UI trên dữ liệu giả | — |
| UPLND-496 | UPLND-413 | `/my-team`: ghép API thật và cờ `isManager` (tách từ UPLND-434) | — |
| UPLND-435 | UPLND-420 | Mốc thời gian quá khứ | — |
| UPLND-494 | UPLND-472 | Phân quyền: sidebar, route guard, ẩn nút theo bốn quyền | — |

**Thang điểm Sprint 3 không còn là 1 điểm bằng 1 ngày.** Ngày công gốc của PO cho lane FE là 25 ngày; sau khi trừ phần UI demo đã dựng sẵn còn khoảng 18, rồi FE lead chốt gộp cả lane về 9 điểm (DEC-T5). Mục ƯỚC LƯỢNG trong mô tả từng task Jira vẫn ghi căn cứ ngày công gốc để đối chiếu.

**Cảnh báo rule Jira**: có automation đặt Story Points của story bằng tổng điểm các sub-task mỗi khi sub-task đổi điểm. Nó đã ghi đè điểm PO ở UPLND-404 (26/10) và 9 story Sprint 4 (09/11). Không đặt điểm cho sub-task; nếu lỡ đặt thì phải đặt lại điểm story theo comment của PO.

## 5. Sáu đợt làm

Thứ tự theo phụ thuộc kỹ thuật: nền tảng → cây và thành viên → quan hệ người → nội dung → đọc dữ liệu → phần chờ BE nhiều nhất.
Cột *Cỡ* là tương đối (S nhỏ, M vừa, L lớn) — **chưa có ước lượng ngày công**, FE lead điền khi phân owner.

### F1 — Nền tảng feature (U7) + khung danh sách (U1)

Mục tiêu: mở được `/groups`, thấy danh sách nhóm chạy bằng mock, đi lại được giữa danh sách và chi tiết.

| # | Task | US | Nơi làm | Cỡ |
|---|---|---|---|---|
| F1.1 | Dựng package `@ops/feature-group`: `package.json`, `tsconfig.json`, `src/index.ts` theo mẫu `features/class-and-course` | — | `features/group/` | S |
| F1.2 | Đăng ký feature vào app: route, DI container, sidebar bằng `ID_SIDE_BAR.GROUP` mới (**không** tái dùng `LIST_GROUP` của Recipients) | — | app + `libs/hooks/src/permission/useMenuData.tsx` | M |
| F1.3 | Khai `IGroupAPI` theo mục 4 của thiết kế FE; `group.service.ts` trả mock | — | `src/services/` | M |
| F1.4 | `mock-data.ts`: cây 4 cấp, đủ nguồn `Tự tạo`/`Đồng bộ`, trạng thái `Đang dùng`/`Lưu trữ`, có tài khoản kiểm thử và người nghỉ để thử luật lọc | — | `src/services/` | M |
| F1.5 | Route và guard `/groups`, `/groups/:id/*` | — | `src/routes.tsx`, `src/constants/routes.ts` | S |
| F1.6 | `GroupListPage` + `GroupListToolbar`: tìm kiếm, lọc nguồn/cấp/trạng thái/quản lý, công tắc *Hiện nhóm đã lưu trữ* mặc định tắt | US6 | `src/pages/groups/` | M |
| F1.7 | `GroupTableView`: antd Table, phân trang 20 dòng, lọc kết hợp, sắp xếp | US6 | `src/components/groups/` | M |
| F1.8 | Khung chi tiết nhóm: `GroupInfoCard` + khung tab (Thành viên · Người phụ trách · Nội dung · Báo cáo · Nhật ký) | US6 | `src/pages/groups/` | M |

**Xong khi**: `/groups` lên được từ menu, bảng hiển thị mock đúng `BR-6.2`, `BR-6.3`, `BR-6.5`, vào được chi tiết, `pnpm typecheck:ops-fe` sạch.

### F2 — Cây, tạo sửa, thành viên (U1 + U2)

| # | Task | US | Nơi làm | Cỡ |
|---|---|---|---|---|
| F2.1 | `GroupTreeChart` React Flow — **đã có ở nhánh demo**, chỉ port và rà theo PRD v0.7 | US6 | `src/components/groups/` | S |
| F2.2 | Nhớ lựa chọn Cây/Bảng gần nhất (`AC6.1`); `GroupPathBreadcrumb` khi tìm ra nhóm con (`BR-6.4`) | US6 | nt | S |
| F2.3 | Drawer xem nhanh khi bấm nhóm trên Cây: thông tin + tab *Managers* riêng (cạnh *Members*) với nút *Gán quản lý* + *Mở chi tiết* (mục 8.5) | US6 | nt | M |
| F2.4 | `GroupForm` + `GroupCreate` (Drawer) + `groupSchema` Zod — **đã có ở nhánh demo**, rà lại: khoá Mã nhóm khi sửa (`BR-1.1`), ô Nhóm cha chỉ nhóm Tự tạo + Đang dùng (`BR-1.2`), không render field nguồn/trạng thái (`BR-1.6`), **không giới hạn số cấp** (CR6) | US1 | nt | M |
| F2.5 | Kéo-thả đổi nhóm cha trên Cây + `MoveGroupConfirm`: viền xanh/đỏ, chặn thả vào chính nó/nhánh con (`BR-2.1`), nhóm đồng bộ không kéo (`BR-2.3`), hộp xác nhận nêu tên nhánh/số nhóm con/số người/cha cũ→mới (`AC2.1`) | US2 | nt | **L** |
| F2.6 | `MembersTab` + `AddMemberDialog`: tìm theo tên/mã NV/email, tối đa 20 kết quả cuộn tải thêm, người đã trong nhóm hiện mờ (`BR-3.1`), **không bao giờ hiện tài khoản kiểm thử** (`BR-3.2`) | US3 | nt | M |
| F2.7 | Gỡ thành viên: gọi `previewRemoveMembers` trước, cảnh báo người đang học dở (`BR-3.4`, `BR-3.7`) | US3 | nt | M |
| F2.8 | Nhập/gỡ theo tệp: `ModalImport` từ `@ops/ui` với `type='GROUP_MEMBER'`, bắt chọn Thêm/Gỡ trước khi tải (`AC4.1`), `TableImportLog` ba loại lỗi (`BR-4.3`), dòng hợp lệ vẫn chạy (`BR-4.2`) | US4 | nt | M |
| F2.9 | `SyncedGroupBanner` + ẩn nút theo `source === 'SYNCED'` (`BR-5.5`), vẫn render Giao nội dung/Gán quản lý/mentor (`BR-5.6`) | US5 | nt | S |

**Chặn**: F2.8 cần phụ thuộc BE #5 (`GROUP_MEMBER` vào union của `ModalImport` + job import + file mẫu) — phần FE của union có thể làm trước.

**F4.6 — thiếu sót của bản 0.1–0.4 (02/11/2026)**: `AC7.5` và `AC7.3` nằm ở tab `Students` của lớp,
không ở màn nhóm, nên bốn bản trước **bỏ quên** khi chia F4. Lộ ra khi BE giao `f6943d1`:
`GET /classes/:id/students` nay trả `meta.capacity`, `meta.current_count`, `meta.is_over_capacity` và
`source_groups` cho từng học viên. Hai trường thêm vào là cộng thêm nên không làm hỏng màn đang chạy,
nhưng **chưa ai đọc**.

**Không xếp cùng F3.8.** Mô tả `UPLND-427` đã ghi *"Dòng cảnh báo khi vượt sức chứa lớp"* trong mục
PHẠM VI, nên đây là việc của chính task đang `Doing`, không phải việc phải hẹn chủ module. Nửa còn
lại (`AC7.3` cột nguồn ghi danh) không được liệt kê tường minh ở `UPLND-427` — hỏi PO xem gộp vào đó
hay tách sub-task mới. Phía BE là `UPLND-458`, đã `IN STAGING`.

**F2.6 — phần `Already in group` (02/11/2026)**: trước `e32176a`, BE loại hẳn người đã ở trong
nhóm khỏi `candidates`, nên `AC3.1` *"hiện mờ kèm nhãn `Already in group`"* không dựng được —
họ không có trong kết quả. BE nay trả cả họ kèm `is_member` và `related_groups`, và
`PeoplePickerModal` khoá ô chọn (`getCheckboxProps`) kèm lý do ngay dưới tên.

`related_groups` là phần BE cho thêm ngoài yêu cầu: người đang là thành viên của nhóm tổ tiên
hoặc hậu duệ thì BE **cũng bỏ qua** khi thêm. PRD không nêu nhãn cho trường hợp này, nhưng để
chọn được rồi báo `skipped` sau là lỗi, nên chặn cùng cách và ghi rõ vướng nhóm nào. Thuộc
quyền FE tự quyết giao diện Ops mà PO đã giao.

### F3 — Quan hệ người (U4)

| # | Task | US | Nơi làm | Cỡ |
|---|---|---|---|---|
| F3.1 | `SupervisorsTab` (tab Người phụ trách) + `AssignSupervisorModal` dùng chung cho quản lý và mentor | US9, US12 | `features/group` | M |
| F3.2 | Gán quản lý: chọn nhiều, chỉ nhân sự vận hành đang hoạt động, mỗi dòng hiện nguồn quan hệ (trực tiếp / kế thừa). Email do BE bắn, FE không gửi | US9 | nt | M |
| F3.3 | Khối kế thừa: hiện *Kế thừa từ nhóm `<cha>`* (`BR-10.1`), nút *Gán riêng cho nhóm này* làm khối biến mất (`BR-10.3`). Kế thừa do BE tính, FE chỉ render | US10 | nt | S |
| F3.4 | Gán mentor: không gửi email (`AC12.5`); **mentor vừa là thành viên cùng lớp tạm được tự chấm** (`BR-12.8`, CR6) | US12 | nt | S |
| F3.5 | Nhãn *Chưa có quản lý* ở danh sách (`BR-13.1`) + bộ lọc *Chỉ nhóm chưa có quản lý* | US13 | nt | S |
| F3.6 | **Phối hợp `features/user`**: khối Quản lý ở hồ sơ học viên — nút *Chỉ định / Thay quản lý chính* (`BR-11.1`), thứ tự chính → theo nhóm → kế thừa (`BR-11.2`), khối *Nhóm đang thuộc* | US11 | `features/user` | M |
| F3.7 | **Phối hợp `features/user`**: nút *Chuyển toàn bộ phụ trách* ở hồ sơ NV, có bước xem trước, không đụng quản lý chính (`AC13.3`, `BR-13.4`) | US13 | `features/user` | M |
| F3.8 | **Phối hợp `features/class-and-course`**: cột *Phụ trách nhóm* ở tab Mentor của lớp | US12 | `features/class-and-course` | S |

**Chặn**: phụ thuộc BE #2 (quyền `gr_*` cho gán quản lý/mentor). F3.6–F3.8 đụng module của người khác, cần hẹn lịch trước.

### F4 — Giao nội dung (U3)

| # | Task | US | Nơi làm | Cỡ |
|---|---|---|---|---|
| F4.1 | `AssignedContentTab`: bảng lớp đã giao, nút *Gỡ lớp* ẩn khi đã có người học (`BR-7.10`) | US7 | `features/group` | M |
| F4.2 | `AssignContentDialog`: chọn nhiều lớp, tìm theo tên lớp/khoá, chỉ lớp đang nhận học viên (`BR-7.2`); hai công tắc *Chảy xuống nhánh con* và *Tự ghi danh người vào sau*, cả hai mặc định tắt | US7 | nt | M |
| F4.3 | Khối xem trước: số sẽ vào / đã có / bị bỏ qua kèm lý do (`AC7.2`). FE **không** chạy luật đứng, chỉ gọi `assignContent` và đọc kết quả | US7 | nt | M |
| F4.4 | Công tắc tự ghi danh theo từng cặp nhóm–lớp (`BR-8.1`), lưu ngay khi đổi; bật khi còn N người chưa vào thì hỏi *Ghi danh luôn* / *Chỉ người vào sau* (`AC8.2`); tắt thì báo người đã vào vẫn học (`BR-8.2`) | US8 | nt | M |
| F4.5 | Giao nội dung cho nhóm lớn không chặn giao diện — chạy nền, báo khi xong (NFR của US7) | US7 | nt | S |
| F4.6 | **`UPLND-427`** · ở `SCR21` tab `Students` của lớp (`features/class-and-course`) — dòng *Lớp này giới hạn N học viên, hiện có M người* khi vượt sức chứa (`BR-7.6`, `AC7.5`), và cột nguồn của lượt ghi danh hiện các nhóm đã giao lớp đó (`BR-7.9`, `AC7.3`) | US7 | `features/class-and-course` | S |

### F5 — Đọc dữ liệu: báo cáo và nhật ký (U7)

| # | Task | US | Nơi làm | Cỡ |
|---|---|---|---|---|
| F5.1 | `GroupReportTab` + `useGroupReport`: ba danh sách theo thành viên / nhóm con / khoá (CR6 — tab trong chi tiết nhóm, **không phải dashboard**) | US18 | `features/group` | **L** |
| F5.2 | Ô chọn **Mốc thời gian** (Hiện tại / ngày quá khứ, sớm nhất = ngày bật tính năng `BR-18.7`) | US18 | nt | M |
| F5.3 | Luật hiển thị: tính theo thành viên tại mốc (`BR-18.1`), loại kiểm thử + nghỉ việc ở chế độ hiện tại (`BR-18.4`, `BR-18.5`), **gồm nhánh con, không có công tắc tắt** (`BR-18.3`), nhóm con chỉ liệt con trực tiếp nhưng cộng dồn cả nhánh (`BR-18.6`) | US18 | nt | M |
| F5.4 | Không chặn giao diện khi tính báo cáo khối lớn (NFR của US18) | US18 | nt | S |
| F5.5 | `GroupLogPage` + `useGroupLog`: bảng chỉ-đọc, cột Thời điểm · Người · Nhóm · Hành động · Lý do (5 giá trị) · Người thao tác (*Hệ thống* khi đồng bộ), mặc định mới nhất lên đầu | US15 | nt | M |
| F5.6 | Lối vào nhật ký từ chi tiết nhóm (lọc sẵn nhóm) và từ hồ sơ học viên (lọc sẵn người), truyền query param | US15 | nt | S |
| F5.7 | `ArchiveGroupConfirm` + ẩn nút theo lịch sử: Xoá chỉ khi chưa từng có thành viên và chưa từng giao nội dung (`BR-14.1`); lưu trữ nhóm cha báo rõ số nhóm con bị lưu trữ theo (`BR-14.6`); nút Khôi phục cho nhóm `Lưu trữ` | US14 | nt | M |

**Ghi chú**: `BR-18.8` — đợt này **không** làm bộ lọc nhóm trên dashboard.

### F6 — Phạm vi người dùng và thông báo (U5 + US21)

Đợt chờ BE nhiều nhất, để cuối.

| # | Task | US | Nơi làm | Cỡ |
|---|---|---|---|---|
| F6.1 | `MyTeamPage` + `useMyTeam` tại `/my-team`: cột Họ tên · Nhóm · **Số khoá quá hạn** · đang học · hoàn thành · lần học gần nhất; mặc định sắp theo quá hạn giảm dần (`BR-16.1`); lọc theo nhóm / có quá hạn; phân trang; loại kiểm thử + nghỉ việc (`BR-16.5`, `BR-16.6`); **không** hiện % tiến độ từng khoá | US16 | `features/group` | **L** |
| F6.2 | Menu và route guard `/my-team` theo cờ `isManager`; **tài khoản học viên được gán quản lý/mentor vào được UpLMS Ops và chỉ thấy màn của vai đó** (`BR-16.7`, CR6 — thiết kế FE mục 8.0) | US16 | app + `libs/hooks` | **L** |
| F6.3 | `SCR24`, `SCR25` dùng được ở 375 px (NFR của US16) | US16 | `features/group` | S |
| F6.4 | **XONG 02/11.** Gỡ nhóm người nhận cũ của thông báo (`BR-21.1`) — xem ghi chú dưới bảng | US21 | `features/notification`, `libs/hooks`, `libs/core` | M |
| F6.5 | **XONG 02/11.** Ô Nhóm người nhận ở màn tạo/sửa thông báo (`AC21.1`, `BR-21.4`, `BR-21.5`) — xem ghi chú dưới bảng | US21 | `features/notification` | M |
| F6.6 | **XONG 02/11.** Khối Nhóm đã chọn ở chi tiết + bộ lọc Nhóm ở danh sách (`AC21.4`) — xem ghi chú dưới bảng | US21 | nt | M |
| F6.7 | **Phối hợp `lms-fe`** (`UPLND-495`): khối *Quản lý của tôi*, dùng được ở 375 px | US17 | `lms-fe` | M |
| F6.8 | **`UPLND-494`** · phân quyền chức năng Nhóm (story `UPLND-472`, DEC156): mục sidebar và `PermissionRoute` theo quyền Xem nhóm; ẩn nút theo Quản lý nhóm, Gán người phụ trách, Xem nhật ký thành viên ở danh sách nhóm, chi tiết nhóm, hồ sơ học viên. PRD chưa có US cho bộ quyền này (chỉ tiền điều kiện và `BR-6.6`). Chặn bởi BE `UPLND-493` về tên khoá quyền; nút ở hồ sơ học viên nằm trong `features/user` | — | `features/group`, `libs/core`, `libs/hooks`, `features/user` | S |

**Chặn**: F6.1–F6.3 cần phụ thuộc BE #3 (cờ `isManager`) và #2 (quyền đọc theo quan hệ quản lý — Vấn đề tồn đọng #2 của PRD). **F6.5–F6.6** cần PO trả lời câu hỏi mở #19 (mã màn) và #15 (chức năng gửi thông báo đã bật chưa). **F6.4 không nằm trong diện chặn đó** — nó chỉ là xoá, `BR-21.1` đã chốt "bỏ hẳn, không chuyển đổi", không cần mã màn.

#### F6.5 và F6.6 — đã làm ngày 02/11 (UPLND-426, phần 2 và 3)

**Câu hỏi mở #19 được PO gỡ chặn bằng cách khác**: không cấp mã màn, giao FE tự
quyết giao diện rồi duyệt trực tiếp trên app. Nên hai task này chạy mà không cần
`ux-design.md` v2.3.

**Quyết định giao diện (FE tự chọn, PO duyệt trên app)**

- Giữ nguyên **tương tác cũ**: bấm ô *Send to* → modal toàn màn có bảng kèm ô
  tick. Người vận hành đã quen, không có lý do đổi.
- Cột trong bảng còn **hai**: `Group name` (tên ở dòng trên, **đường dẫn từ gốc**
  ở dòng dưới cỡ nhỏ màu xám) và `Recipients`. Nhóm gốc có `path` trùng tên nên
  bỏ dòng thứ hai.
- **Bỏ bốn bộ lọc cũ** (`type`, khoảng ngày, `sort_type`, `selectType`): chúng
  thuộc nhóm người nhận cũ. Nhóm học viên không có `type`, và lọc theo ngày tạo
  thì vô nghĩa khi đang chọn người nhận. Còn đúng một ô tìm theo tên hoặc mã.
- Ở chi tiết, mỗi chip nhóm mang thêm **nhãn trạng thái** (`Active` xanh lá /
  `Archived` xám), cùng bộ màu `badge badge-light-*` với `GroupBadges` của
  `features/group`.
- Nhãn trong bộ lọc ở danh sách dùng **đường dẫn đầy đủ**, để hai nhóm trùng tên
  ở hai nhánh vẫn phân biệt được.

**Nguồn dữ liệu — viết theo hình đích, đệm tách riêng.** PO chốt "làm chuẩn FE,
BE bổ sung sau", nên FE code đúng contract đích rồi bọc phần thiếu vào một chỗ
xoá được:

| Endpoint | tên | đường dẫn | số người nhận | tìm kiếm |
| --- | --- | --- | --- | --- |
| `GET groups/options?purpose=ANY` | ✓ | ✓ | **chưa có** | ✓ (`q`) |
| `GET groups?status=ACTIVE` | ✓ | ✗ | ✓ | ✗ |

`useRecipientGroups` gọi **một** endpoint (`options`), **phân trang phía máy
chủ**, đọc `g.member_count`. Vì BE chưa trả trường đó, hàm `fetchCountFallback`
đọc thêm danh sách một lượt rồi tra theo `id` — hàm này tự thoát ngay khi BE
bắt đầu trả số, và xoá cả hàm là xong. `ILearnerGroupPathItem.member_count` đã
khai sẵn (tuỳ chọn) làm contract đích.

`purpose: ANY` đã lọc sẵn `status = ACTIVE` ở BE nên `BR-21.4` thoả mà FE không
phải lọc gì.

**NĂM chỗ hỏng sẵn lộ ra**, bốn cái đầu do BE đã gộp nhóm người nhận vào nhóm
học viên mà FE chưa chạy theo:

1. **Bộ lọc Nhóm ở danh sách thông báo đứng im ở *No data***. Code đọc
   `res.data.groups`, nhưng `GET groups` nay trả **mảng phẳng ở `data`**.
2. **Bộ lọc Nhóm bản điện thoại hỏng y hệt** — `libs/ui/src/base/mobile/
   FilterMobile.tsx`. Đã sửa cùng kiểu, nhãn cũng dùng đường dẫn đầy đủ cho
   khớp desktop.
3. **Khối nhóm đã chọn ở chi tiết thông báo rỗng**. Code đọc `data.groups`,
   nhưng `GET notifications/:id` trả `notification_groups: [{ id, group }]`.
   Cẩn thận: `ng.id` là id dòng quan hệ, id nhóm nằm ở `ng.group.id`.
4. **Mở thẳng URL đã lọc thì ô lọc hiện UUID thô** thay vì tên nhóm: tuỳ chọn
   chỉ nạp khi `onFocus`, nên antd không tra được nhãn. Nay nạp sẵn một trang
   lúc vào màn nếu `filter_groups` có giá trị.
5. `getSelectionTable` mặc định khoá theo `key`; dữ liệu mới không có trường đó
   (bản cũ chạy nhờ `addKeyToData`) nên lựa chọn rơi hết. Phải truyền `'id'` và
   đặt `rowKey='id'` cho `Table`.

**Kiểu đã sửa cho đúng contract**: `INotification.groups: Group[]` (nhóm người
nhận **cũ**) đổi thành `notification_groups?: INotificationGroupRef[]`, thêm
cùng trường vào `INotificationRes`. Cột *Send to* của bảng danh sách viết sẵn
theo hình đích — BE trả là cột tự hiện, không phải sửa thêm.

**Đã đo trên app**

| Việc | Kết quả |
| --- | --- |
| `AC21.1` ô chọn | 5 nhóm, mỗi dòng có tên + đường dẫn + số người nhận |
| tìm kiếm | `q=con` ra đúng 2 nhóm |
| `BR-21.4` | lưu trữ `Khối A` → biến khỏi ô chọn (còn 4); khôi phục lại sau khi đo |
| chọn và lưu | 2 nhóm → `POST` 200 → DB `notification_groups` trỏ đúng 2 nhóm học viên |
| `AC21.4` chi tiết | chip hiện `Khối B con [Active]` · `Khối B [Active]` |
| `AC21.4` lọc | lọc `Khối C` (không gắn) → *No data*; lọc `Khối B` → đúng 1 thông báo |

**Còn thiếu ở BE**: xem `be-pending-fe.md` cùng thư mục — danh sách gom đủ 14
mục của cả nhóm học viên lẫn thông báo, kèm "xong thì xoá gì" ở FE.

**Chưa đo được**: `AC21.2` (người nhận gồm cả nhánh con, loại tài khoản kiểm thử
và đã khoá) và `AC21.3` (một người ở hai nhóm chỉ nhận một thông báo) là **luật
phía BE**, phải đọc hộp thư thật mới kiểm được.

#### F6.4 — đã làm ngày 02/11 (UPLND-426, phần 1/3)

Phạm vi thực tế **rộng hơn hai file bảng này ghi**. Nhóm người nhận cũ là một
CRUD đầy đủ, xoá cả cụm mới hết lối vào:

| Xoá | Vì sao |
| --- | --- |
| `components/recipients/CreateGroupComponent.tsx` | nêu trong task |
| `components/recipients/GroupReceiverTable.tsx` | chỉ `ListGroupReceiver` dùng |
| `components/recipients/AddMember.tsx` | chỉ `CreateGroupComponent` dùng |
| `components/recipients/TableMembers.tsx` | chỉ `AddMember` dùng |
| `pages/recipients/CreateAndUpdateGroup.tsx` | màn tạo/sửa của chính nhóm cũ |
| `pages/recipients/ListGroupReceiver.tsx` | nêu trong task |

Cùng với: 3 route (`CREATE_GROUP`, `GROUP_DETAIL`, `LIST_GROUP`) và 4 hằng số
trong `NOTIFICATION_ROUTES`; `ID_SIDE_BAR.LIST_GROUP` khỏi `sidebarIds` của
module, khỏi `checkShowParentMenu`, khỏi mục con *Recipients List* và khỏi nhánh
`switch` trong `useMenuData.tsx`; `PageLink.LIST_GROUP` khỏi `useMenuState.ts`.

**Orphan do chính thay đổi này sinh ra, đã dọn**: `ID_SIDE_BAR.LIST_GROUP` và
`ID_SIDE_BAR.CREATE_GROUP`; bốn cờ `allowRenderGroupList/CreateGroup/EditGroup/
RemoveGroup` trong `sidebar.ts`; năm method `NotificationAPI` không còn ai gọi
(`addNotificationGroup`, `updateNotificationGroup`, `deleteUserGroup`,
`detailNotificationGroup`, `addStudentGroup`) ở cả bản cài lẫn `INotificationAPI`.

**Giữ lại có chủ ý**: `getNotificationGroups` (bộ lọc nhóm ở danh sách thông báo
— việc của F6.6) và `deleteNotificationGroup` (còn một chỗ gọi, xem cảnh báo
dưới). `AddGroupToNoti.tsx` + `TableGroup.tsx` ở màn tạo thông báo **không
động tới**: F6.5 sẽ thay, không phải xoá.

**Đã đo**: `/list-group` và `/create-group` trả trang 404; menu *Notice & Email*
còn đúng ba mục (Notice List & Email List · Mail Logs · Blocked Mail), không còn
*Recipients List*; ba màn Thông báo, Mail Logs, Blocked Mail vẫn chạy, không có
lời gọi API nào ≥ 400.

**⚠ Hai việc phải xử lý trước khi F6.5/F6.6 xong**

1. **Đụng đường dẫn với learner-group.** Các API nhóm cũ gọi thẳng `groups`,
   `groups/:id`, `groups/users` — **đúng những đường dẫn learner-group mới đang
   dùng**. `getNotificationGroups` (còn sống, phục vụ bộ lọc ở danh sách thông
   báo và hai `FilterMobile.tsx`) sẽ nhận **đúng hình dữ liệu mới** ngay khi BE
   cắt sang contract learner-group trên staging, và vỡ. F6.6 không phải việc
   làm đẹp, nó là điều kiện để danh sách thông báo không hỏng.
2. **Còn một bản sao thứ hai của bảng nhóm cũ**, ở
   `features/class-and-course/src/components/courses/group-receiver/`. Nó export
   qua `courses/index.ts` nhưng **không nơi nào tiêu thụ** — code chết có sẵn,
   không phải do thay đổi này sinh ra nên để nguyên. Nó vẫn trỏ
   `PageLink.UPDATE_GROUP` (giờ là `undefined`) và vẫn gọi
   `deleteNotificationGroup` — đó là lý do method ấy chưa xoá được. Nên gộp vào
   F6.6 hoặc mở một task dọn riêng.

## 6. Không thuộc lane FE

| US | Vì sao |
|---|---|
| US19 tự gỡ khỏi khoá chưa học | Không có thao tác FE; kết quả thấy qua nhật ký US15 |
| US20 báo quản lý qua email | FE không gửi mail. Quản lý xử lý bằng chức năng Lớp có sẵn. Khối xem trước khi gỡ thành viên ở F2.7 là nơi FE cảnh báo trước |

## 7. Việc song song của người khác

Những việc này **không chặn F1**; FE cứ chạy trên mock.

| # | Việc | Ai |
|---|---|---|
| 1 | Trả lời 5 phụ thuộc ở mục 13 của thiết kế FE, trước hết là contract `IGroupAPI` | BE lead |
| 2 | Cập nhật `fe-technical-design.md` lên v2.3 phủ US21 (G1) | Tech PIC |
| 3 | Trả lời câu hỏi mở #19 và #15 của PRD | PO |
| 4 | Dựng `openspec/` schema `run` + `references` cho `ops-fe` để mở change theo Bolt | người giữ khung |

## 8. Lịch sử tài liệu

| Version | Ngày | Thay đổi |
|---|---|---|
| 0.4 | 2026-10-26 | Chốt thang điểm 9 cho cả lane FE (DEC-T5); thêm mục 4.1 bảng điểm trên Jira |
| 0.3 | 2026-10-26 | Dùng lại UI demo ở nhánh `feature/manager-group` thay vì dựng lại (DEC-T4); F2.1 và F2.4 hạ cỡ; UPLND-424 hạ từ 2,5 xuống 1,5 điểm |
| 0.2 | 2026-10-26 | Gán toàn bộ lane FE cho một người; thêm mục 4.0 thứ tự chạy nối tiếp, dồn việc chờ người khác về cuối |
| 0.30 | 2026-11-10 | Drawer xem nhanh (`F2.3`): khối *Managers* tách thành tab riêng cạnh *Members* thay vì nằm dưới tab Overview. Đổi ở `fe-technical-design` §8.5 và `design.md` của change `uplnd-group-sprint-4`; PRD và UX không tả drawer này nên không lệch |
| 0.29 | 2026-11-09 | Bỏ điểm của 10 sub-task FE Sprint 4 (429 đến 435, 494 đến 496): một người làm trọn story nên không chia điểm sub-task. Điểm nằm ở story theo comment của PO (408: 5, 409: 2, 410: 5, 411: 3, 412: 2, 413: 5, 414: 3, 420: 2, 472: 2). Mục 4.1 viết lại, ghi cảnh báo rule Jira cộng điểm sub-task lên story |
| 0.28 | 2026-11-09 | Quy tắc mới: task FE tối đa 1 điểm, task lớn hơn tách thành UI trên dữ liệu giả và ghép API. Chỉ `UPLND-434` (1,5 điểm) vượt ngưỡng: `UPLND-434` còn UI `/my-team`, khung theo vai, 375 px (1 điểm); `UPLND-496` ghép API và cờ `isManager` (0,5 điểm, làm sau 434, chờ BE `UPLND-486`, `UPLND-478`). Tổng lane FE vẫn 10 điểm |
| 0.27 | 2026-11-09 | Tách `UPLND-433` (chạm cả `ops-fe` và `lms-fe`) thành hai task theo repo: `UPLND-433` còn phần hồ sơ học viên trên Ops, `UPLND-495` là khối *Quản lý của tôi* trên `lms-fe` (F6.7). Mỗi task 0,5 điểm, tổng hai task vẫn 1, lane FE vẫn 10. Các task còn lại chỉ làm một repo nên giữ nguyên |
| 0.26 | 2026-11-09 | Kéo `po/main` (DEC156): thêm story phân quyền `UPLND-472` (ORD-15) và task FE `UPLND-494` (F6.8, 1 điểm; tổng lane 10). Rà PRD v0.11: CR9 chỉ đổi US2, US3, US6, US7, US14, US15 (đã làm ở Sprint 3), không đổi luật của các story Sprint 4. Phụ thuộc quyền trong `UPLND-431` đổi sang tham chiếu `UPLND-472` |
| 0.25 | 2026-11-04 | Hai ô chọn nhóm (`Parent group` ở form, `Group` ở nhật ký `SCR17`) phân trang theo cuộn và tìm qua BE: hook `useGroupPathSelect` (`GET /groups/options`, 20 nhóm mỗi trang, cuộn gần cuối thì tải tiếp, gõ từ khoá gọi lại với `q` sau 300ms, giá trị đã chọn ngoài các trang đã tải thì lấy riêng từ `GET /groups/:id`). Bỏ giới hạn 100 nhóm. Người dùng chốt |
| 0.24 | 2026-11-04 | Bảng nhóm `SCR1`: đổi thứ tự cột thành Group name · Members · Parent group · Code · Status · Last updated (hoán đổi Code và Members). Người dùng chốt |
| 0.23 | 2026-11-04 | Ô lọc `Group` ở nhật ký `SCR17` hiện tên + đường dẫn giống ô `Parent group`: dùng chung helper `shared/groupPathSelect.tsx` và hook `useGroupPathOptions` (`GET /groups/options`, `purpose=ANY` cho bộ lọc, `PARENT` cho nhóm cha). Tìm theo cả tên lẫn đường dẫn; bỏ tooltip mặc định của trình duyệt trên từng dòng. Giới hạn 100 nhóm đầu vì BE chặn `page_size` tối đa 100. Người dùng chốt |
| 0.22 | 2026-11-04 | Nhật ký `SCR17`: cột và ô lọc `Lý do`/`Reason` đổi tên thành `Leave type`. BE lưu cột `group_user_instances.reason` chỉ khi lượt thuộc nhóm kết thúc (dòng Joined để trống), nên đây là loại rời nhóm. Lệch PRD (PRD gọi `Lý do`, áp cả vào và rời nhóm). Người dùng chốt |
| 0.21 | 2026-11-04 | Header chi tiết nhóm (`SCR4`): hai chip trạng thái và nguồn đứng ngay sau tên nhóm thay vì ở hàng thông tin phụ; tên dài cắt ba chấm kèm tooltip. Người dùng chốt |
| 0.20 | 2026-11-04 | Màn `SCR1`: bỏ khối báo lỗi tự dựng `Could not load the group list` kèm nút `Retry` (khác design system của Ops). Lỗi API đã có toast chung của interceptor axios (trừ mã 422, 413); bảng/sơ đồ lúc lỗi hiện trạng thái rỗng. Lệch `ux-design.md` mục 2 (bảng State của từng màn đòi trạng thái lỗi riêng có Retry). Người dùng chốt |
| 0.19 | 2026-11-03 | Thống nhất dùng `Delete` thay `Remove` ở mọi nhãn thao tác gỡ trong feature Group (khớp quy ước các màn Ops khác, vd màn lớp): nút, hộp xác nhận, toast, tooltip của thành viên, lớp được giao, người phụ trách; tuỳ chọn Import `Delete from group`; nhãn lý do log `Deleted manually/by import/by HR sync`. Giữ nguyên các câu mô tả như `nobody is removed from the class`. Chữ "Remove" của PRD đổi theo quyết định người dùng. Người dùng chốt |
| 0.18 | 2026-11-03 | Giai đoạn 2 (tiếp): màn chi tiết nhóm, tab Overview: form full chiều ngang (bỏ khung 700px); tiêu đề `Group Information` đổi thành `Group Overview` (`Edit Group Overview` khi sửa), đồng thời màn lớp đổi `Class Information` thành `Class Overview`; drawer xem nhanh không có tiêu đề này; ô Parent group hiện tên nhóm cha, đường dẫn đầy đủ trong tooltip, danh sách thả xuống hiện tên đậm + đường dẫn xám; modal Add members bỏ Phone/Date, thêm cột `Current group` (nhóm đang thuộc trong nhánh, hoặc `This group`) thay dòng `Already in …` dưới tên, thiếu trạng thái tài khoản và ngày vào nhóm vì BE chưa trả (B21). Người dùng chốt |
| 0.17 | 2026-11-03 | Danh sách issue sau demo, giai đoạn 2 (một phần): tạo từ dấu `+` trên thẻ nhóm cha là tạo **nhóm con** (nhãn bước `Subgroup info`, mục `Create empty subgroup`, toast `Subgroup created`, ô Parent group khoá); bảng nhóm bỏ cột Source, badge nguồn đứng sau tên nhóm (cách 12px); `Enrolled via this group` đổi thành `Enrolled by group` kèm tooltip giải thích; `Already in class` đổi thành `Already enrolled in this class`. Người dùng chốt |
| 0.16 | 2026-11-03 | Nhật ký `SCR17`, cột và bộ lọc `Lý do`: làm theo BE thay vì năm giá trị của PRD. Hiện đúng 7 mã rời nhóm của BE (xoá tay, xoá bằng import, chuyển bộ phận từ HR, HR xoá, nghỉ việc, thu hồi vai, chuyển trách nhiệm), không gộp; dòng `Joined` hiện `—` vì BE chỉ ghi lý do khi rời nhóm (trước đó FE hiện sai thành `Manual`). Nhãn tiếng Anh do FE đặt tạm, chờ Design (PRD ghi bốn nhãn đầu do Design dịch). Lệch PRD (PRD: năm giá trị, áp cả vào và rời nhóm). Người dùng chốt |
| 0.15 | 2026-11-03 | Danh sách issue sau demo, giai đoạn 1: ô `Group code` ẩn khi tạo nhóm (BE `5b94c0e` tự sinh mã từ tên), vẫn hiện khoá khi sửa; bảng nhóm thêm cột `Parent group` (đọc `parent` của `GET /groups`, BE `37d18fe` trả ngày 03/11); tab `Info` đổi tên `Overview`; ô nhập ở drawer xem nhanh rộng hết bề ngang; Member list thay cột `Phòng ban` bằng `Subgroup` (từ `member_groups` của BE, lệch PRD); màn log bỏ cột `Performed by` (B20) và cột `Action` hiện chữ thay badge. Người dùng chốt |
| 0.14 | 2026-11-03 | Lối vào `Membership log` (`SCR17`): bỏ nút ở header chi tiết nhóm, thay bằng liên kết gạch chân ở chân bảng giống `Import Log` của lớp, ở danh sách nhóm và ở tab Members của chi tiết nhóm (chỉ khi nhóm có thành viên, vào log lọc sẵn nhóm theo `AC15.5`). Màn log bỏ cột số thứ tự. Lệch PRD (PRD đặt lối vào ở chi tiết nhóm), người dùng chốt |
| 0.13 | 2026-11-03 | Rời khỏi nhóm cha (đưa nhóm con lên làm nhóm gốc). Dạng Graph: kéo một nhóm Tự tạo, đang dùng và đang có cha thì hiện ô chữ nhật cam nhạt nét đứt cỡ một thẻ ở góc trên phải; thả con trỏ vào ô thì mở hộp `Move branch` với cha mới là `Top level` (`PUT /groups/:id` với `parent_id: null`, BE đã hỗ trợ, có ghi log đổi cha; `move-preview` bỏ trống đích). Form sửa (tab Info và drawer): thêm lựa chọn `No parent (make top-level group)` đầu danh sách Parent group, ngoài nút xoá sẵn có của ô. Lệch PRD: trước đây thả vào vùng trống không làm gì (cố ý, tránh trượt tay); nay chỉ thả đúng vào ô rời cha mới đưa lên cấp một. Người dùng chốt |
| 0.12 | 2026-11-03 | `SCR1`: nút đổi dạng xem đặt bên phải `Create group`, cao 40px bằng nút tạo. Trạng thái rỗng của Bảng và Cây dùng hình `Empty` mặc định của antd (giống màn danh sách class), vùng rỗng của Bảng cao bằng khung rỗng của Cây để đổi qua lại không nhảy. Thẻ nhóm ở dạng Cây bỏ hàng `Code` và thêm hàng `Sub-groups` = tổng số nhóm con ở mọi cấp (đếm đệ quy trên cây đã tải, không chỉ con trực tiếp; `NODE_H` giữ 132 vì thay một hàng bằng một hàng); bỏ số đếm cạnh nút mở rộng khi thu gọn hoặc khi ẩn theo zoom. Chip `Archived` chuyển lên header thẻ cạnh chip nguồn; tên nhóm dài cắt bằng dấu ba chấm kèm tooltip. Sửa lỗi nền: enum nguồn nhóm của FE là `SYNCED` còn BE là `HR_SYNC`, nên lọc Source=Synced ở Bảng bị 422 và nhóm đồng bộ hiện thành Manual; đổi `LearnerGroupSource.SYNCED` thành `HR_SYNC`. Lệch PRD, người dùng chốt |
| 0.11 | 2026-11-03 | Màn `SCR1`: vào mặc định bằng dạng Bảng (PRD `AC6.1` ghi Cây; đổi khoá lưu sang `group-list-view-mode-v2` để giá trị `tree` cũ không giữ người dùng ở Cây, vẫn nhớ lựa chọn từ nay). Nút đổi dạng xem chuyển sang cạnh nút `Create group`. Dạng Cây dùng chung bộ lọc Search, Source, Status với dạng Bảng: Source và Status lọc tại chỗ bằng `filterTree` trên cây đã tải (BE chỉ nhận `include_archived` ở endpoint cây), chọn `Archived` thì tải cây kèm nhóm lưu trữ rồi giữ đúng nhóm lưu trữ. Nút gửi của dạng Cây đổi từ `Search` thành `Apply` vì từ khoá ở Cây đưa tới nhóm chứ không lọc. Bỏ công tắc `Show archived` ở dạng Cây. Phát hiện: `GET /groups` của BE không có tham số tìm theo tên nên ô tìm của dạng Bảng không lọc gì (B18). Lệch PRD, người dùng chốt |
| 0.10 | 2026-11-03 | Bảng danh sách nhóm (`SCR1`): bỏ ô lọc `Level` (PRD ghi Nguồn · Cấp · Trạng thái · Quản lý) và bỏ công tắc `Show archived` vì `Status` đã có `Archived` (dạng Cây cũng bỏ từ 0.11). Sửa lỗi nền: hook bảng trước đây bỏ qua ô `Status`, chỉ đọc công tắc, nên ô này không có tác dụng; nay `Status` quyết định `status` gửi BE, không chọn thì `ACTIVE`. Đổi nhãn trạng thái tài khoản `Locked` thành `Inactive` cho khớp `INACTIVE` của BE. Icon mục Learner Groups ở sidebar thành ba người. Lệch PRD, người dùng chốt |
| 0.9 | 2026-11-03 | Bảng thành viên (`SCR6`) bỏ hai cột `Mã nhân viên` và `Phòng ban` (cột sau không có dữ liệu: BE không trả phòng ban, DB không còn cột `department`); hộp chọn người (`SCR7`) bỏ cột `Mã nhân viên`, ô tìm vẫn tìm theo mã. Bỏ công tắc `Show former employees`; ô `Account status` nay gửi `account_status` lên BE thay vì lọc tại chỗ, không chọn thì BE vẫn ẩn tài khoản `BLOCKED` như mặc định PRD. Đổi nhãn `Resigned` thành `Blocked` vì BE chỉ có một trạng thái `BLOCKED` cho cả nghỉ việc lẫn bị khoá (PRD dòng 239). Lệch PRD `SCR6`, người dùng chốt |
| 0.8 | 2026-11-03 | Ẩn hàng Manager ở thẻ cây, cột và ô lọc Manager ở bảng `SCR1` bằng cờ `SUPERVISORS_TAB`: PRD có nhắc nhưng thuộc `US9`/`US13` (`UPLND-431`, backlog), chưa gán được quản lý thì chỉ toàn `—` hoặc `No manager` trên mọi nhóm. Phát hiện BE: API cây không trả quản lý (B17). Modal *Assign classes* bỏ lớp đã giao khỏi danh sách (PRD không nói, theo quy ước hộp chọn mentor/học viên, B15). Modal *Add members* giữ đúng PRD: người đã trong nhóm hiện mờ kèm nhãn, phân trang 20 dòng |
| 0.7 | 2026-11-02 (chiều) | Tổng kết Sprint 3. Đo đầu-cuối giao lớp (`UPLND-427`): preview 3 số → cascade → `POST .../class-assignments` 201 → bảng cập nhật; dòng vượt sức chứa + cột *Nguồn* ở tab `Students` của lớp verify mắt. Drawer xem nhanh rework: nút Edit sticky góc đáy drawer qua portal vào `footerContent` của `BaseDrawer`, loading đổi sang `Skeleton`, menu `...` không còn Edit (dời sang form `GroupInfoFormCard` dùng chung với tab Info), cột action tab Members ẩn khi không có dòng thao tác. 10/11 task FE của Sơn ở sprint này **done hoặc IN REVIEW**; `UPLND-421` người dùng tự làm nhánh khác, không trong lane group. Phát hiện: `GET/PUT /groups/settings` BE đã có nhưng PRD `DEC121` cố ý không mở UI đợt này. Tick `6.5`, `10.1` trong openspec; `10.3` giữ `[ ]` vì supervisors + report mock ngoài sprint |
| 0.6 | 2026-11-02 | Drawer xem nhanh (`F2.3`) nay sửa inline bốn field thông tin nhóm, không phải nhảy sang màn chi tiết. Tách `GroupInfoFormCard` dùng chung với tab Info, nút Edit đặt dưới cùng form theo yêu cầu. Cột thao tác ở tab Members của drawer ẩn khi không có dòng nào gỡ được. BE giao `AC7.5` + `AC7.3` ở `f6943d1`: dòng vượt sức chứa và cột *Nguồn* ở tab `Students` của lớp — FE ghép xong, dòng cảnh báo giờ đọc số của BE chứ không tự suy ở client |
| 0.5 | 2026-11-02 | Thêm F4.6: `AC7.5` dòng vượt sức chứa và `AC7.3` cột nguồn ghi danh ở tab `Students` của lớp — bốn bản trước bỏ quên, BE đã giao ở `f6943d1`. BE giao B3 ở `e32176a`: `GET groups/:id/candidates` thôi loại người đã ở trong nhóm, mỗi dòng kèm `is_member`, `roles_in_group`, `related_groups`. Ghép xong phần `Already in group` của F2.6 (`AC3.1`, `EC-11`) và chặn luôn người ở nhóm tổ tiên, hậu duệ. 13 mục còn lại của `be-pending-fe.md` chưa đổi |
| 0.4 | 2026-11-02 | Theo chỉ đạo "làm chuẩn FE, BE bổ sung sau": `useRecipientGroups` chuyển sang một endpoint + phân trang máy chủ, phần đệm tách thành hàm xoá được; khai đúng contract `notification_groups` thay `groups`; sửa thêm bộ lọc bản điện thoại và nhãn UUID khi mở URL đã lọc. Lập `be-pending-fe.md` gom 14 mục BE còn thiếu |
| 0.3 | 2026-11-02 | F6.5 + F6.6 xong. PO gỡ chặn câu hỏi mở #19 bằng cách giao FE tự quyết giao diện và duyệt trên app. Ghi lại quyết định giao diện, việc phải gộp hai endpoint cho `BR-21.5`, ba chỗ hỏng sẵn do BE gộp bảng nhóm, và hai yêu cầu còn lại gửi BE |
| 0.2 | 2026-11-02 | F6.4 xong. Ghi lại phạm vi thật (6 file, không phải 2), phần orphan đã dọn, và hai cảnh báo: đụng đường dẫn `groups` với learner-group, và bản sao bảng nhóm cũ ở `features/class-and-course` |
| 0.1 | 2026-10-26 | Bản đầu. Dựng theo đường ngắn từ `fe-technical-design` v2.2 + PRD v0.7; bổ sung US21 và việc gỡ nhóm người nhận cũ mà thiết kế v2.2 chưa phủ |
