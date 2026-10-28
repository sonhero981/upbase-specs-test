---
intent: 261005-group
artifact: fe-task-plan
feature: LMS-F002
version: 0.4
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

Mỗi story của PO có đúng một task FE, gán Nguyễn Hùng Sơn. **Tổng 9 điểm** cho cả lane FE
(8,5 trong Sprint 3/Q4/2026; UPLND-435 ở backlog).

| Task | Story | Nội dung | Điểm |
|---|---|---|---|
| UPLND-423 | UPLND-403 | Nền kỹ thuật, bỏ phòng ban | 0,5 |
| UPLND-424 | UPLND-402 | Port UI danh sách từ nhánh demo | 0,5 |
| UPLND-425 | UPLND-404 | Tab thành viên, nhập tệp, nhật ký | 0,5 |
| UPLND-426 | UPLND-405 | Thông báo theo nhóm | 0,5 |
| UPLND-427 | UPLND-406 | Giao nội dung, tự ghi danh | 1 |
| UPLND-428 | UPLND-407 | Kéo thả, lưu trữ, xoá | 1 |
| UPLND-429 | UPLND-408 | Nhóm đồng bộ chỉ đọc | 0,5 |
| UPLND-430 | UPLND-409 | Báo cáo hiện tại | 0,5 |
| UPLND-431 | UPLND-410 | Người phụ trách, kế thừa, chuyển | 0,5 |
| UPLND-432 | UPLND-411 | Mentor | 0,5 |
| UPLND-433 | UPLND-412 | Hồ sơ học viên Ops và LMS | 1 |
| UPLND-434 | UPLND-413 | `/my-team`, khung theo vai | 1,5 |
| UPLND-435 | UPLND-420 | Mốc thời gian quá khứ | 0,5 |

**Thang điểm này không còn là 1 điểm bằng 1 ngày.** Ngày công gốc của PO cho lane FE là 25 ngày;
sau khi trừ phần UI demo đã dựng sẵn còn khoảng 18, rồi FE lead chốt gộp cả lane về 9 điểm
(DEC-T5). Mục ƯỚC LƯỢNG trong mô tả từng task Jira vẫn ghi căn cứ ngày công gốc để đối chiếu,
nên con số ở đó lớn hơn trường Story Points. Dùng trường Story Points khi tính sprint.

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
| F2.3 | Drawer xem nhanh khi bấm nhóm trên Cây: thông tin + quản lý + nút *Gán quản lý* + *Mở chi tiết* (mục 8.5) | US6 | nt | M |
| F2.4 | `GroupForm` + `GroupCreate` (Drawer) + `groupSchema` Zod — **đã có ở nhánh demo**, rà lại: khoá Mã nhóm khi sửa (`BR-1.1`), ô Nhóm cha chỉ nhóm Tự tạo + Đang dùng (`BR-1.2`), không render field nguồn/trạng thái (`BR-1.6`), **không giới hạn số cấp** (CR6) | US1 | nt | M |
| F2.5 | Kéo-thả đổi nhóm cha trên Cây + `MoveGroupConfirm`: viền xanh/đỏ, chặn thả vào chính nó/nhánh con (`BR-2.1`), nhóm đồng bộ không kéo (`BR-2.3`), hộp xác nhận nêu tên nhánh/số nhóm con/số người/cha cũ→mới (`AC2.1`) | US2 | nt | **L** |
| F2.6 | `MembersTab` + `AddMemberDialog`: tìm theo tên/mã NV/email, tối đa 20 kết quả cuộn tải thêm, người đã trong nhóm hiện mờ (`BR-3.1`), **không bao giờ hiện tài khoản kiểm thử** (`BR-3.2`) | US3 | nt | M |
| F2.7 | Gỡ thành viên: gọi `previewRemoveMembers` trước, cảnh báo người đang học dở (`BR-3.4`, `BR-3.7`) | US3 | nt | M |
| F2.8 | Nhập/gỡ theo tệp: `ModalImport` từ `@ops/ui` với `type='GROUP_MEMBER'`, bắt chọn Thêm/Gỡ trước khi tải (`AC4.1`), `TableImportLog` ba loại lỗi (`BR-4.3`), dòng hợp lệ vẫn chạy (`BR-4.2`) | US4 | nt | M |
| F2.9 | `SyncedGroupBanner` + ẩn nút theo `source === 'SYNCED'` (`BR-5.5`), vẫn render Giao nội dung/Gán quản lý/mentor (`BR-5.6`) | US5 | nt | S |

**Chặn**: F2.8 cần phụ thuộc BE #5 (`GROUP_MEMBER` vào union của `ModalImport` + job import + file mẫu) — phần FE của union có thể làm trước.

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
| F6.4 | **Gỡ nhóm người nhận cũ của thông báo** (`BR-21.1`): xoá `components/recipients/CreateGroupComponent.tsx`, `pages/recipients/ListGroupReceiver.tsx`, route và hằng số liên quan, gỡ `ID_SIDE_BAR.LIST_GROUP` khỏi menu Thông báo | US21 | `features/notification`, `libs/hooks`, `libs/core` | M |
| F6.5 | Ô **Nhóm người nhận** ở màn tạo/sửa thông báo: chọn nhiều, chỉ nhóm `Đang dùng`, mỗi dòng có đường dẫn từ gốc + số người nhận tính cả nhánh con, có tìm kiếm (`AC21.1`, `BR-21.4`, `BR-21.5`) | US21 | `features/notification` | M |
| F6.6 | Khối **Nhóm đã chọn** ở chi tiết thông báo + bộ lọc **Nhóm** ở danh sách thông báo (`AC21.4`) | US21 | nt | M |
| F6.7 | **Phối hợp `lms-fe`**: khối *Quản lý của tôi*, dùng được ở 375 px | US17 | `lms-fe` | M |

**Chặn**: F6.1–F6.3 cần phụ thuộc BE #3 (cờ `isManager`) và #2 (quyền đọc theo quan hệ quản lý — Vấn đề tồn đọng #2 của PRD). F6.4–F6.6 cần PO trả lời câu hỏi mở #19 (mã màn) và #15 (chức năng gửi thông báo đã bật chưa).

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
| 0.1 | 2026-10-26 | Bản đầu. Dựng theo đường ngắn từ `fe-technical-design` v2.2 + PRD v0.7; bổ sung US21 và việc gỡ nhóm người nhận cũ mà thiết kế v2.2 chưa phủ |
