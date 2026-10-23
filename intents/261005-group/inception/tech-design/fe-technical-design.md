---
intent: 261005-group
artifact: technical-design-fe
feature: LMS-F002
version: 2.1
status: draft
created: 2026-10-21
updated: 2026-10-23
based-on: prd.md v0.6
---
# Technical Design — Frontend: Nhóm học viên (Group)

> **Trạng thái: draft, đã soi codebase thật.** Bản này viết theo cấu trúc hiện có của `ops-fe` và `lms-fe` (đã khảo sát 2026-10-23), nên mọi path, package, và pattern dưới đây là thật, dùng được ngay để dựng khung. Phần còn **chờ BE** là **API contract** (endpoint + shape response) — đánh dấu `⚠️ BE` tại chỗ.

> **Cập nhật v2.1 theo PRD v0.6 (CR6 ngày 2026-10-21):**
> - **Bỏ giới hạn số cấp** của cây nhóm — không còn `BR-1.3`, `BR-1.4`, `BR-2.2`
> - **US18** thay đổi: từ dashboard thành **tab Báo cáo trong chi tiết nhóm** (`BR-18.8`)
> - **Một người nhiều vai** trong một nhóm: quản lý/mentor/thành viên dùng **một tài khoản học viên**, tài khoản đó vào UpLMS Ops chỉ thấy màn theo vai (`BR-16.7`)
> - **Thông báo không gửi cho chính người** mà thông báo nói tới (`BR-20.8`)
> - **Mentor vừa là thành viên** tạm được tự chấm bài của mình (`BR-12.8` — rủi ro đã chấp nhận)

## Mục lục

- [1. Tổng quan](#1-tổng-quan)
- [2. Đăng ký feature vào ops-fe](#2-đăng-ký-feature-vào-ops-fe)
- [3. Cấu trúc module `features/group`](#3-cấu-trúc-module-featuresgroup)
- [4. Tầng API và Dependency Injection](#4-tầng-api-và-dependency-injection)
- [5. Routing, quyền và menu](#5-routing-quyền-và-menu)
- [6. State và data fetching](#6-state-và-data-fetching)
- [7. Thiết kế màn theo US](#7-thiết-kế-màn-theo-us)
- [8. Các tương tác khó](#8-các-tương-tác-khó)
- [9. Validation](#9-validation)
- [10. Xử lý lỗi](#10-xử-lý-lỗi)
- [11. Hiệu năng](#11-hiệu-năng)
- [12. lms-fe — màn học viên và quản lý](#12-lms-fe--màn-học-viên-và-quản-lý)
- [13. Phụ thuộc BE và câu hỏi cần chốt](#13-phụ-thuộc-be-và-câu-hỏi-cần-chốt)
- [14. Lịch sử tài liệu](#14-lịch-sử-tài-liệu)

---

## 1. Tổng quan

### 1.1 App và màn

| App | Màn / Khối | US |
|---|---|---|
| **ops-fe** (Admin Portal) | Danh sách nhóm — dạng Cây + dạng Bảng | US1, US6, US13 |
| ops-fe | Form tạo/sửa nhóm | US1, US2 |
| ops-fe | Chi tiết nhóm — tab Thành viên | US3, US4 |
| ops-fe | Chi tiết nhóm — tab Nội dung được giao | US7, US8 |
| ops-fe | Chi tiết nhóm — tab Người phụ trách | US9, US10, US12 |
| ops-fe | Chi tiết nhóm — **tab Báo cáo** (CR6) | US18 |
| ops-fe | Nhóm đồng bộ — chế độ chỉ đọc | US5 |
| ops-fe | Lưu trữ / khôi phục / xoá nhóm | US14 |
| ops-fe | Nhật ký thay đổi thành viên | US15 |
| ops-fe | Màn theo dõi nhánh (cho Quản lý) | US16 |
| ops-fe | Hồ sơ học viên — khối Quản lý (chỉ định quản lý chính) | US11 |
| ops-fe | Hồ sơ nhân sự vận hành — Chuyển toàn bộ phụ trách | US13 |
| **lms-fe** (Learner) | Hồ sơ học viên — khối "Quản lý của tôi" | US17 |

**Chủ yếu là backend, FE chỉ hiển thị/kích hoạt rồi đọc kết quả:** luật đứng tự ghi danh (US7, US8), tự gỡ khỏi khoá chưa học (US19), mail event `MAIL-GRP-01`/`MAIL-GRP-02` (US20, US9/US11/US13). FE **không** thực thi các luật này; FE gọi API, hiển thị khối xem trước và trạng thái, và đọc lại kết quả.

> **Lưu ý quan trọng về email (CR6):** Thông báo gửi quản lý **không bao giờ gửi cho chính người mà thông báo nói tới**. BE xử lý logic này (`BR-20.8`); nếu không còn ai thì gửi quản lý của nhóm cha gần nhất có quản lý, hết cây thì gửi quản trị viên. FE không can thiệp.

### 1.2 Tech stack thật (đã xác nhận trong repo)

**ops-fe** — pnpm workspaces (`apps/*`, `libs/*`, `features/*`), không nx/turbo.

| Thứ | Phiên bản / cách dùng |
|---|---|
| React | 18 |
| Router | `react-router-dom` ^6.11.2 — mỗi feature export một `AppModule`, gộp ở `module-registry.ts` |
| Data fetching | **`react-query` v3 (3.38.0)** — `import { useQuery, useMutation, useInfiniteQuery } from 'react-query'`. **Không** phải `@tanstack/react-query` |
| UI | **Ant Design v5** (^5.24.3) + Metronic (`@ops/_metronic`, bootstrap 5) cho layout |
| Form | `react-hook-form` ^7.55.0 + `zod` ^3.24.2 + `@hookform/resolvers/zod` ^5.0.1 |
| Toast | **`react-hot-toast`** ^2.6.0 (`toast.success/error`). Không dùng antd `message` |
| Excel | `exceljs` ^4.4.0 (client-side khi cần) |
| Auth | Keycloak (không có route login) |
| i18n | **Không có i18n runtime.** Chuỗi để ở `constants/messages.ts` + `LANG_*` trong `@ops/core` |

**lms-fe** — pnpm + Turbo, **Next.js 14 App Router**, react-query v3 (3.39.3), antd v5 + Tailwind, scope `@lms/*`.

### 1.3 Scaffolding Group đã có sẵn trong ops-fe

Không cần dựng lại — tái sử dụng:

- **Quyền:** `TITLE_GROUPS_GR` trong `libs/core/src/constants/permission.ts`
  ```ts
  export const TITLE_GROUPS_GR = {
    VIEW_GROUP:   "gr_get_groups",
    CREATE_GROUP: "gr_create_group",
    EDIT_GROUP:   "gr_edit_group",
    REMOVE_GROUP: "gr_remove_group",
  };
  ```
- **Sidebar id:** `ID_SIDE_BAR.LIST_GROUP = "list-group"`, `ID_SIDE_BAR.CREATE_GROUP = "create-group"`.
- **permissionsToCheck** (`apps/ops-fe/src/constants/sidebar.ts`): `allowRenderGroupList`, `allowRenderCreateGroup`, `allowRenderEditGroup`, `allowRenderRemoveGroup`.

> ⚠️ Bộ quyền hiện có **4 quyền** (view/create/edit/remove) là cho CRUD nhóm. PRD cần thêm trục quyền cho: xem nhật ký (US15), màn theo dõi nhánh của quản lý (US16 — đọc theo **quan hệ quản lý**, không theo vai trò hệ thống, xem `BR-16.4`), giao nội dung, gán quản lý/mentor. **Chốt với BE danh sách quyền `gr_*` đầy đủ** trước khi làm U4/U5 (Vấn đề tồn đọng #2 trong PRD).

---

## 2. Đăng ký feature vào ops-fe

Theo đúng pattern của `gamification` / `department`. Năm việc:

1. **Tạo package** `features/group` (`@ops/feature-group`, `"main": "src/index.ts"`), `peerDependencies` pin runtime chung (react-query 3.38.0, antd ^5.24.3, react-hook-form, zod, @hookform/resolvers, react-hot-toast, exceljs), deps `@ops/*` là `workspace:*`.
2. **Export `groupModule: AppModule`** từ `features/group/src/index.ts`.
3. **Đăng ký** trong `apps/ops-fe/src/module-registry.ts` (thêm `groupModule` vào mảng `modules`) và thêm `@ops/feature-group` vào `apps/ops-fe/package.json`.
4. **generate-customer:** thêm `group` vào `FEATURE_MODULE_MAP`, `FEATURE_FOLDER_MAP` (và `REQUIRED_FEATURES` nếu luôn bật) trong `scripts/generate-customer.js`, và vào `"features"` của các file `configs/<customer>.json` muốn bật.
5. **Wire API** (xem §4).

```ts
// features/group/src/index.ts
import type { AppModule } from '@ops/core';
import { groupRoutes } from './routes';
import { GROUP_ROUTES } from './constants/routes';
import { ID_SIDE_BAR } from '@ops/core';

export const groupModule: AppModule = {
  name: 'group',
  routes: groupRoutes,
  pageLink: GROUP_ROUTES,
  sidebarIds: [ID_SIDE_BAR.LIST_GROUP, ID_SIDE_BAR.CREATE_GROUP],
};
```

---

## 3. Cấu trúc module `features/group`

Mô phỏng `features/gamification` (mới nhất, sạch nhất) và `features/department` (analog gần nhất — phân cấp + import nhân sự).

```
features/group/src/
  index.ts                      # export groupModule
  routes.tsx                    # RouteObject[] + PermissionRoute + withAuthComponents
  constants/
    routes.ts                   # GROUP_ROUTES (path constants)
    group.constants.ts          # enum GroupSource, GroupStatus, MemberChangeReason...
    messages.ts                 # chuỗi VN (validate, confirm, empty state)
  types/
    group.types.ts              # IGroup, IGroupTreeNode, IGroupMember... ⚠️ khớp BE
    api.types.ts                # params + response shapes ⚠️ khớp BE
  schema/
    groupSchema.ts              # Zod: createGroupSchema, moveGroupSchema
  hooks/
    useGroupQueries.ts          # useGroupList, useGroupTree (infinite theo nhánh), useGroupDetail
    useGroupMutations.ts        # create/update/move/archive/restore/delete (useAppMutation)
    useGroupMembers.ts          # list + add/remove + import
    useGroupContent.ts          # assign class, toggle auto-enroll
    useGroupStakeholders.ts     # managers, mentors, inherited managers
    useGroupLog.ts              # nhật ký (US15)
    useMyTeam.ts                # màn theo dõi nhánh (US16)
    useGroupReport.ts           # tab báo cáo (US18)
  pages/
    list/GroupListPage.tsx
    detail/[id].tsx             # chi tiết nhóm (naming [id].tsx như department)
    create/CreateGroupPage.tsx
    edit/[id].tsx
    my-team/MyTeamPage.tsx      # US16
    log/GroupLogPage.tsx        # US15 (hoặc nhúng trong detail)
  components/
    list/
      GroupTreeView.tsx         # dạng cây, lazy-load nhánh, kéo thả (US2, US6)
      GroupTableView.tsx        # dạng bảng, lọc/sắp xếp/phân trang (US6)
      GroupListToolbar.tsx      # công tắc Cây/Bảng, tìm kiếm, bộ lọc, công tắc "Hiện lưu trữ"
      GroupViewSwitch.tsx       # nhớ lựa chọn gần nhất (localStorage)
    detail/
      GroupDetailLayout.tsx     # antd Tabs + GroupInfoCard + action buttons
      GroupInfoCard.tsx         # thông tin + nút Sửa/Lưu trữ/Xoá/Khôi phục (ẩn theo nguồn/trạng thái)
      SyncedGroupBanner.tsx     # dòng giải thích nhóm đồng bộ (US5)
      tabs/
        MembersTab.tsx          # US3, US4
        AssignedContentTab.tsx  # US7, US8
        StakeholdersTab.tsx     # US9, US10, US12
        ReportTab.tsx           # US18 — tab Báo cáo trong chi tiết nhóm (CR6)
      dialogs/
        GroupFormModal.tsx      # tạo/sửa (US1)
        MoveGroupConfirm.tsx    # xác nhận di chuyển nhánh (US2)
        AddMemberDialog.tsx     # tìm + chọn người (US3)
        AssignContentDialog.tsx # chọn lớp + 2 công tắc + xem trước (US7)
        AutoEnrollConfirm.tsx   # hộp xác nhận bật/tắt tự ghi danh (US8)
        AssignManagerDialog.tsx # US9
        AssignMentorDialog.tsx  # US12
        ArchiveGroupConfirm.tsx # US14
    report/
      GroupReportView.tsx       # US18 — view trong tab Báo cáo, ba danh sách
    shared/
      GroupStatusBadge.tsx      # antd Tag: Đang dùng / Lưu trữ
      GroupSourceBadge.tsx      # Đồng bộ / (ẩn với Tự tạo)
      NoManagerBadge.tsx        # "Chưa có quản lý" (US13)
      GroupPathBreadcrumb.tsx   # đường dẫn đầy đủ từ gốc "ECOM / ... / Growth 1" (US6)
  utils/
    treeHelpers.ts              # build/flatten cây, kiểm vòng, tính độ sâu
    groupMappers.ts             # map response BE -> view model
    export.ts                   # tải nhật ký/thành viên (nếu cần)
```

**Dùng lại từ libs (không viết mới):**

| Việc | Dùng |
|---|---|
| Import file thành viên | `ModalImport` từ `@ops/ui` (`libs/ui/src/base/upload-file/ModalImport.tsx`) |
| Log lỗi import | `TableImportLog` từ `@ops/ui` + `ImportLogAPI` |
| Mutation có toast + invalidate | `useAppMutation` từ `@ops/hooks` |
| Kiểm quyền | `useHasPermission` / `usePermissions` từ `@ops/hooks` |
| Guard route | `PermissionRoute` (`@ops/ui`) + `withAuthComponents` (`@ops/hoc`) |
| Badge/Tag, Modal | Ant Design v5 + `@ops/ui` |
| Kiểm vòng khi kéo thả | Helper `isDescendant` trong `utils/treeHelpers.ts` — **không** kiểm độ sâu (CR6) |

---

## 4. Tầng API và Dependency Injection

**Quy tắc then chốt của repo:** feature **không** import API trực tiếp. API là **interface** ở `@ops/core`, inject qua `FeatureContext`, implement ở `apps/ops-fe`. Feature gọi `const { GroupAPI } = useFeature()`.

Bốn việc để nối API:

**1) Khai interface** — `libs/core/src/types/` (vd `IGroupAPI.ts`):
```ts
export interface IGroupAPI {
  getGroups(params: IGroupListParams): Promise<IPaged<IGroup>>;
  getGroupTree(parentId?: string, showArchived?: boolean): Promise<IGroupTreeNode[]>;
  getGroupDetail(id: string): Promise<IGroupDetail>;
  createGroup(data: ICreateGroupReq): Promise<IGroup>;
  updateGroup(id: string, data: IUpdateGroupReq): Promise<IGroup>;
  moveGroup(id: string, newParentId: string | null): Promise<void>;
  archiveGroup(id: string): Promise<void>;
  restoreGroup(id: string): Promise<void>;
  deleteGroup(id: string): Promise<void>;
  // members
  getMembers(id: string, params: IMemberParams): Promise<IPaged<IGroupMember>>;
  addMembers(id: string, userIds: string[]): Promise<void>;
  removeMembers(id: string, userIds: string[]): Promise<IRemoveMemberResult>; // chứa cảnh báo học dở
  previewRemoveMembers(id: string, userIds: string[]): Promise<IRemovePreview>;
  // content
  getAssignedContent(id: string): Promise<IAssignedClass[]>;
  previewAssignContent(id: string, classIds: string[], cascade: boolean): Promise<IAssignPreview>;
  assignContent(id: string, req: IAssignContentReq): Promise<void>;
  setAutoEnroll(id: string, classId: string, enabled: boolean, enrollExisting: boolean): Promise<void>;
  // stakeholders
  getStakeholders(id: string): Promise<IStakeholders>; // managers (direct+inherited), mentors
  setManagers(id: string, userIds: string[]): Promise<void>;
  setMentors(id: string, userIds: string[]): Promise<void>;
  transferResponsibility(fromUserId: string, toUserId: string): Promise<ITransferResult>;
  // log, report, my-team
  getMemberLog(params: ILogParams): Promise<IPaged<ILogEntry>>;
  getMyTeam(params: IMyTeamParams): Promise<IPaged<ILearnerProgress>>;
  getGroupReport(groupId: string, params: IReportParams): Promise<IGroupReport>; // US18 — báo cáo của một nhóm cụ thể
}
```

**2) Thêm vào context** — `libs/state/src/context/FeatureContext.tsx`: thêm `GroupAPI: IGroupAPI` vào `FeatureContextProps`.

**3) Implement** — `apps/ops-fe/src/apis/group/index.ts` (static class + `fetcher` + `unwrap`, như `GamificationAPI`):
```ts
import { fetcher } from '@ops/service';
const BASE = '/groups';                                  // ⚠️ BE chốt prefix
const unwrap = <T>(p: Promise<{ data: T }>) => p.then((r) => r.data);

export class GroupAPI {
  static getGroups(params: IGroupListParams) {
    return unwrap<IPaged<IGroup>>(fetcher(BASE, { params }));
  }
  static getGroupTree(parentId?: string, showArchived = false) {
    return unwrap<IGroupTreeNode[]>(fetcher(`${BASE}/tree`, { params: { parentId, showArchived } }));
  }
  // ... phần còn lại
}
```

**4) Wire** — `apps/ops-fe/src/index.tsx`: import `GroupAPI`, truyền vào `<FeatureProvider value={{ ..., GroupAPI }}>`.

**Query key factory** — `libs/core/src/constants/queryKeyFactory/groupKeys.ts`:
```ts
export const groupKeys = {
  all: ['group'] as const,
  listPrefix: () => [...groupKeys.all, 'list'] as const,
  list: (params: object) => [...groupKeys.listPrefix(), params] as const,
  tree: (parentId: string | 'root', showArchived: boolean) =>
    [...groupKeys.all, 'tree', parentId, showArchived] as const,
  detail: (id: string) => [...groupKeys.all, 'detail', id] as const,
  members: (id: string, params: object) => [...groupKeys.detail(id), 'members', params] as const,
  content: (id: string) => [...groupKeys.detail(id), 'content'] as const,
  stakeholders: (id: string) => [...groupKeys.detail(id), 'stakeholders'] as const,
  log: (params: object) => [...groupKeys.all, 'log', params] as const,
  myTeam: (params: object) => [...groupKeys.all, 'my-team', params] as const,
  report: (id: string, params: object) => [...groupKeys.detail(id), 'report', params] as const, // US18 — báo cáo của một nhóm
};
```

---

## 5. Routing, quyền và menu

### 5.1 Route constants — `features/group/src/constants/routes.ts`

```ts
export const GROUP_ROUTES = {
  GROUP_LIST:   '/groups',
  GROUP_CREATE: '/groups/create',
  GROUP_DETAIL: '/groups/:id',
  GROUP_EDIT:   '/groups/:id/edit',
  GROUP_LOG:    '/groups/log',        // US15 (hoặc tab trong detail)
  MY_TEAM:      '/my-team',           // US16
  // US18 là tab trong GROUP_DETAIL, không có route riêng (CR6)
};
```

### 5.2 Guard — `features/group/src/routes.tsx`

```tsx
const GuardedList = withAuthComponents(() => (
  <PermissionRoute permissions={[TITLE_GROUPS_GR.VIEW_GROUP]}>
    <GroupListPage />
  </PermissionRoute>
));
// MY_TEAM dùng guard theo quan hệ quản lý, KHÔNG theo TITLE_GROUPS_GR (BR-16.4) ⚠️ cần quyền gr_* riêng
export const groupRoutes: RouteObject[] = [
  { path: GROUP_ROUTES.GROUP_LIST,   element: <GuardedList /> },
  { path: GROUP_ROUTES.GROUP_CREATE, element: <GuardedCreate /> },
  { path: GROUP_ROUTES.GROUP_DETAIL, element: <GuardedDetail /> },
  { path: GROUP_ROUTES.GROUP_EDIT,   element: <GuardedEdit /> },
  { path: GROUP_ROUTES.MY_TEAM,      element: <GuardedMyTeam /> },
];
```

| Route | Quyền |
|---|---|
| `/groups`, `/groups/:id` | `gr_get_groups` |
| `/groups/create` | `gr_create_group` |
| `/groups/:id/edit` | `gr_edit_group` |
| `/my-team` (US16) | ⚠️ quyền mới, đọc theo quan hệ quản lý (`BR-16.4`, `BR-16.7`); tài khoản học viên được gán quản lý vào UpLMS Ops |

### 5.3 Menu — `libs/hooks/src/permission/useMenuData.tsx`

Thêm item dưới nhóm "Quản lý tổ chức", key theo `ID_SIDE_BAR.LIST_GROUP`, gate bằng `allowRender.allowRenderGroupList`, label ở `LANG_SIDEBAR`, icon `ki-outline ki-abstract-...`. `/my-team` là item riêng, chỉ hiện khi người dùng là quản lý — **tài khoản học viên được gán quản lý có cờ từ profile** (⚠️ BE cấp cờ `isManager` hoặc kiểm bằng API).

---

## 6. State và data fetching

**Nguyên tắc:** cache của react-query là source of truth cho server data; chỉ UI state (dạng xem, filter đang chọn, node đang mở) để ở context/local.

### 6.1 Query — ví dụ cây lazy-load (US6, `BR-6.1`)

Cây tải dần theo nhánh. Mỗi node mở ra là một query riêng theo `parentId`:
```ts
// useGroupQueries.ts
export const useGroupChildren = (parentId: string | 'root', showArchived: boolean) => {
  const { GroupAPI } = useFeature();
  return useQuery(
    groupKeys.tree(parentId, showArchived),
    () => GroupAPI.getGroupTree(parentId === 'root' ? undefined : parentId, showArchived),
    { staleTime: 60_000, refetchOnWindowFocus: false },
  );
};
```
Dạng bảng dùng `useQuery(groupKeys.list(params), ..., { keepPreviousData: true })` cho phân trang mượt (`AC6.5`).

### 6.2 Mutation — dùng `useAppMutation` (auto toast + invalidate)

```ts
// useGroupMutations.ts
export const useGroupMutations = () => {
  const { GroupAPI } = useFeature();
  const create = useAppMutation({
    mutationFn: (d: ICreateGroupReq) => GroupAPI.createGroup(d),
    successMessage: GROUP_MSG.CREATE_SUCCESS,
    queryKeyPrefix: groupKeys.all,
  });
  const move = useAppMutation({
    mutationFn: ({ id, parentId }: IMoveArgs) => GroupAPI.moveGroup(id, parentId),
    successMessage: GROUP_MSG.MOVE_SUCCESS,
    queryKeyPrefix: groupKeys.all,
  });
  // update, archive, restore, delete ...
  return { create, move /* ... */ };
};
```

### 6.3 UI state context — `features/group/src/context` (chỉ UI)

```ts
interface GroupUIState {
  listView: 'TREE' | 'TABLE';          // nhớ qua localStorage (AC6.1)
  filters: IGroupListParams;
  expandedIds: Set<string>;
  showArchived: boolean;               // mặc định false (BR-6.5)
}
```

---

## 7. Thiết kế màn theo US

> Mỗi dòng dưới đây là ánh xạ US → component → điểm FE cần chú ý. Chi tiết luật nằm trong PRD; đây là cách hiện thực ở FE.

### U1 — Khung nhóm

| US | Component | Điểm FE |
|---|---|---|
| **US1** Tạo/sửa nhóm | `GroupFormModal` + `groupSchema` | Nguồn `Tự tạo`/trạng thái `Đang dùng` do hệ thống đặt, **không render field chọn** (`BR-1.6`). Ô **Nhóm cha** chỉ liệt nhóm `Tự tạo` + `Đang dùng` (`BR-1.2`); sửa thì khoá ô **Mã nhóm** (`BR-1.1`). **Không giới hạn số cấp** của cây — cây thật 4 cấp, không có ràng buộc tối đa. |
| **US2** Di chuyển nhánh | `GroupTreeView` (kéo thả) + `MoveGroupConfirm` | Xem [§8.1](#81-cây-kéo-thả-us2-us6). Viền xanh/đỏ khi thả; hộp xác nhận hiện tên nhánh, số nhóm con, số người ảnh hưởng, cha cũ→mới (`AC2.1`). Chặn thả vào chính nó/nhánh con (`BR-2.1`). Nhóm đồng bộ không kéo được (`BR-2.3`). |
| **US3** Thêm/gỡ thành viên | `MembersTab` + `AddMemberDialog` | Tìm theo tên/mã NV/email, tối đa 20 kết quả, cuộn tải thêm. Người đã trong nhóm hiện mờ + nhãn *Đã trong nhóm* (`BR-3.1`). **Không bao giờ hiện tài khoản kiểm thử** (`BR-3.2`). Gỡ → gọi `previewRemoveMembers` trước; nếu có người học dở, hộp xác nhận cảnh báo (`BR-3.4`, `BR-3.7`). |
| **US4** Thêm/gỡ theo lô | `ModalImport` (từ `@ops/ui`) | `type='GROUP_MEMBER'` ⚠️ (thêm vào union của ModalImport + BE import job), `templateFile`, `uploadUrl`. Chọn hành động *Thêm*/*Gỡ* bắt buộc trước khi tải (`AC4.1`). Log lỗi qua `TableImportLog`: không tìm thấy / đã trong nhóm / tài khoản kiểm thử (`BR-4.3`). Dòng hợp lệ vẫn chạy khi có dòng lỗi (`BR-4.2`). |
| **US6** Danh sách nhóm | `GroupListPage` + `GroupTreeView`/`GroupTableView` + `GroupListToolbar` | Mặc định **Cây**, nhớ lựa chọn gần nhất (`AC6.1`). Số thành viên **gồm nhánh con**, loại kiểm thử + nghỉ việc (`BR-6.2`, `BR-6.3`). Tìm kiếm trả nhóm con → `GroupPathBreadcrumb` đường dẫn từ gốc (`BR-6.4`). Công tắc *Hiện nhóm đã lưu trữ* mặc định tắt (`BR-6.5`). Bảng: phân trang 20 dòng, lọc kết hợp, sắp xếp (`AC6.5`). |

### U2 — Đồng bộ cơ cấu

| US | Component | Điểm FE |
|---|---|---|
| **US5** Nhóm đồng bộ | `SyncedGroupBanner` + ẩn nút theo `source` | Nếu `source === 'SYNCED'`: ẩn **Sửa / Thêm-Gỡ thành viên / Di chuyển / Xoá**, thay bằng dòng giải thích (`BR-5.5`). **Vẫn render** Giao nội dung / Gán quản lý / Gán mentor (`BR-5.6`). `GroupInfoCard` hiện nguồn + lần đồng bộ gần nhất + số thành viên lần đó. Đây là màn chỉ-đọc, không có mutation cơ cấu. |

### U3 — Giao nội dung

| US | Component | Điểm FE |
|---|---|---|
| **US7** Giao nội dung | `AssignedContentTab` + `AssignContentDialog` | Xem [§8.2](#82-giao-nội-dung--xem-trước-us7). Ô chọn **lớp** (nhiều, tìm theo tên lớp/khoá), chỉ lớp đang nhận học viên (`BR-7.2`). Hai công tắc: *Chảy xuống nhánh con* (mặc định tắt), *Tự ghi danh người vào sau* (mặc định tắt). Khối xem trước: số sẽ vào / đã có / bị bỏ qua + lý do (`AC7.2`). Nút *Gỡ lớp* ẩn khi đã có người học (`BR-7.10`). FE **không** chạy luật đứng — chỉ gọi `assignContent` và đọc kết quả. |
| **US8** Bật/tắt tự ghi danh | Công tắc trên từng dòng lớp + `AutoEnrollConfirm` | Công tắc theo **từng cặp nhóm–lớp** (`BR-8.1`), lưu ngay khi đổi. Bật khi còn N người chưa vào → hỏi *Ghi danh luôn?* / *Chỉ áp dụng người vào sau* (`AC8.2`). Tắt → hộp xác nhận báo người đã vào vẫn học (`BR-8.2`). |

### U4 — Quan hệ người

| US | Component | Điểm FE |
|---|---|---|
| **US9** Gán quản lý | `StakeholdersTab` + `AssignManagerDialog` | Chọn nhiều, chỉ tài khoản nhân sự vận hành đang hoạt động. Mỗi dòng hiện **nguồn quan hệ** (gán trực tiếp / kế thừa). Email `MAIL-GRP-02` do BE bắn — FE không gửi. **Một người có thể vừa là quản lý vừa là mentor vừa là thành viên của cùng một nhóm bằng một tài khoản học viên** (CR6). |
| **US10** Suy ra quản lý theo cây | Khối kế thừa trong `StakeholdersTab` | Không có thao tác; hiển thị quản lý kế thừa + *Kế thừa từ nhóm `<cha>`* (`BR-10.1`). Nút *Gán riêng cho nhóm này* → ngừng kế thừa, khối biến mất (`BR-10.3`). Kế thừa **tính runtime từ BE**, FE chỉ render. |
| **US11** Quản lý chính trên hồ sơ | Khối Quản lý ở **Hồ sơ học viên** (màn user hiện có) | Nút *Chỉ định quản lý chính*; đã có thì đổi thành *Thay quản lý chính* (`BR-11.1`). Xếp: chính → theo nhóm → kế thừa (`BR-11.2`). Khối *Nhóm đang thuộc* hiện đường dẫn từ gốc hoặc *Chưa thuộc nhóm nào*. Màn này nằm trong `features/user`, cần phối hợp. |
| **US12** Gán mentor | `AssignMentorDialog` trong `StakeholdersTab` | Chọn nhiều, chỉ nhân sự vận hành. Gán mentor **không gửi email** (`AC12.5`). Hiển thị cột *Phụ trách nhóm* ở tab Mentor của **lớp** (màn class hiện có — phối hợp `features/class-and-course`). **Mentor vừa là thành viên của cùng lớp tạm được tự chấm bài của mình** (`BR-12.8`, CR6 — rủi ro đã chấp nhận). |
| **US13** Cảnh báo nhóm trống quản lý + chuyển phụ trách | `NoManagerBadge` + bộ lọc + nút *Chuyển toàn bộ phụ trách* ở hồ sơ NV | Nhãn *Chưa có quản lý* ở danh sách (`BR-13.1`), bộ lọc *Chỉ nhóm chưa có quản lý*. Chuyển: hộp xác nhận hiện số nhóm / số người / người nhận, có bước xem trước (`AC13.3`). Không đụng quản lý chính (`BR-13.4`). |

### U5 — Phạm vi và hiển thị

| US | Component | Điểm FE |
|---|---|---|
| **US16** Theo dõi nhánh | `MyTeamPage` + `useMyTeam` | Bảng cột: Họ tên · Nhóm · **Số khoá quá hạn** · đang học · hoàn thành · lần học gần nhất. Mặc định sắp theo quá hạn giảm dần (`BR-16.1`). Lọc theo nhóm / có quá hạn; phân trang (NFR hàng trăm người). Loại kiểm thử + nghỉ việc (`BR-16.5`, `BR-16.6`). **Không** hiện % tiến độ từng khoá (chủ ý PRD). Đọc theo quan hệ quản lý (`BR-16.4`). **Tài khoản học viên được gán quản lý hoặc mentor vào UpLMS Ops và chỉ thấy màn của vai đó** (`BR-16.7`, CR6). Bấm 1 người → mở hồ sơ học viên. |
| **US17** → xem [§12](#12-lms-fe--màn-học-viên-và-quản-lý) (lms-fe) | | |

### U7 — Nền tảng

| US | Component | Điểm FE |
|---|---|---|
| **US14** Lưu trữ nhóm | `ArchiveGroupConfirm` + logic ẩn nút ở `GroupInfoCard` | Nút **Xoá** chỉ hiện khi nhóm chưa từng có thành viên & chưa từng giao nội dung (`BR-14.1`); còn lại hiện *Nhóm đã có lịch sử, chỉ lưu trữ được*. Lưu trữ nhóm cha → hộp xác nhận nói rõ số nhóm con bị lưu trữ theo (`BR-14.6`). Nút **Khôi phục** cho nhóm `Lưu trữ`. |
| **US15** Nhật ký thành viên | `GroupLogPage` + `useGroupLog` | Bảng chỉ-đọc, cột: Thời điểm · Người · Nhóm · Hành động (`Vào`/`Rời`) · Lý do (5 giá trị) · Người thao tác (*Hệ thống* khi đồng bộ). Lọc theo khoảng thời gian / nhóm / người / lý do. Mặc định mới nhất lên đầu. Lối vào: từ chi tiết nhóm (lọc sẵn nhóm) và từ hồ sơ học viên (lọc sẵn người) — truyền query param. |
| **US18** Báo cáo cộng dồn | `GroupReportTab` + `useGroupReport` | **Tab Báo cáo trong chi tiết nhóm** (CR6), gồm ba danh sách: theo thành viên, theo nhóm con, theo khoá. Ô chọn **Mốc thời gian** (Hiện tại / ngày quá khứ, sớm nhất = ngày bật tính năng `BR-18.7`). Báo cáo tính theo thành viên tại mốc (`BR-18.1`), loại kiểm thử + nghỉ việc ở chế độ hiện tại (`BR-18.4`, `BR-18.5`), **gồm nhánh con** không có công tắc tắt (`BR-18.3`). Nhóm con chỉ liệt con trực tiếp, mỗi dòng cộng dồn cả nhánh (`BR-18.6`). Toàn bộ tính toán ở BE; FE gửi params, render. **Đợt này không có bộ lọc nhóm trên dashboard** (`BR-18.8`). |

### U6 — Vòng đời nhân sự (hầu hết BE)

| US | FE phần nào |
|---|---|
| **US19** tự gỡ khỏi khoá chưa học | **Không có FE thao tác.** Kết quả thấy qua nhật ký (US15) và trạng thái thành viên. |
| **US20** báo quản lý qua email | **Không có FE gửi mail.** Quản lý xử lý thủ công bằng chức năng **Lớp** hiện có (giữ nguyên / gỡ khỏi lớp) — ngoài phạm vi module group. Khối xem trước khi gỡ thành viên (US3/US4) là nơi FE cảnh báo trước. Email không gửi cho chính người bị rời nhóm (CR6, `BR-20.8`). |

---

## 8. Các tương tác khó

### 8.0 Một người nhiều vai — quyền vào UpLMS Ops (CR6)

**Thách thức:** Tài khoản học viên được gán quản lý hoặc mentor phải vào được UpLMS Ops và chỉ thấy màn của vai đó (`BR-16.7`).

**Giải pháp:**
- **Auth/Guard:** Kiểm tra cờ `isManager` hoặc `isMentor` từ profile/token — ⚠️ **BE cấp**
- **Menu:** `/my-team` chỉ hiện khi `isManager === true`; màn chấm bài (hiện có) chỉ hiện khi `isMentor === true`
- **Phân quyền:** Guard các route theo vai trò này, **không** theo `TITLE_GROUPS_GR` vì quản lý không phải nhân sự vận hành
- **Data:** Màn theo dõi nhánh đọc theo **quan hệ quản lý**, không theo vai trò hệ thống (`BR-16.4`)

> Vấn đề tồn đọng: Cần BE chốt cách nhận diện tài khoản học viên có quyền vào UpLMS Ops — cờ trong profile, claim trong token, hoặc API riêng.

### 8.1 Cây kéo thả (US2, US6)

Dùng antd v5 `<Tree draggable onDrop allowDrop>` — nhẹ, nhất quán với UI lib. `allowDrop` chặn thả vào chính nó / nhánh con (dựng từ `treeHelpers.isDescendant`) và chặn nhóm đồng bộ (`draggable: node.source !== 'SYNCED'`). **Không kiểm độ sâu** (CR6 bỏ giới hạn số cấp). Pattern này **chưa có** trong repo (sẽ là tiền lệ mới) nhưng antd v5 đã là chuẩn.

Hiển thị cây phân cấp chỉ-đọc có thể theo tiền lệ **department**: antd `<Table>` với `children` lồng (tree-table) thay vì `<Tree>`. Group nên dùng `<Tree draggable>` vì cần kéo thả.

### 8.2 Giao nội dung — xem trước (US7)

Flow: chọn lớp → đặt 2 công tắc → gọi `previewAssignContent(id, classIds, cascade)` → hiển thị khối xem trước (số sẽ vào / đã có / bỏ qua + lý do) → xác nhận → `assignContent`. Preview là **read-only call tới BE**, không tạo dữ liệu. FE không tự tính ai vào lớp.

### 8.3 Import thành viên (US4)

Dùng thẳng `ModalImport` từ `@ops/ui`, theo `ModalImportStaff.tsx`:
```tsx
<ModalImport
  open={open} setOpen={setOpen}
  title="Nhập thành viên theo tệp"
  templateFile="./IMPORT_GROUP_MEMBER_TEMPLATE.xlsx"
  templateFileName="mau-nhap-thanh-vien.xlsx"
  uploadUrl={`groups/${groupId}/members/import`}   /* ⚠️ BE chốt */
  type="GROUP_MEMBER"                                /* ⚠️ thêm vào union + BE job */
  beforeUpload={beforeUpload}                        /* .xlsx/.csv, cap 5MB */
  refetch={refetchMembers}
/>
```
`ModalImport` đã lo Dragger + Progress + poll job + `ModalImportComplete(errorRows/totalRows)`. Chỉ cần thêm `type` mới và chuẩn bị file mẫu.

### 8.4 Ẩn/hiện nút theo nguồn & trạng thái

Một bảng quyết định ở `GroupInfoCard` / tabs, tránh rải điều kiện khắp nơi:

| Hành động | Hiện khi |
|---|---|
| Sửa thông tin | `source==='SELF'` |
| Thêm/Gỡ thành viên | `source==='SELF' && status==='ACTIVE'` |
| Di chuyển (kéo thả) | `source==='SELF'` |
| Xoá | `source==='SELF' && !hasEverHadMembers && !hasEverAssignedContent` |
| Lưu trữ | `status==='ACTIVE'` |
| Khôi phục | `status==='ARCHIVED'` |
| Giao nội dung / Gán quản lý / Gán mentor | luôn (cả nhóm đồng bộ), nếu `status==='ACTIVE'` |

---

## 9. Validation

Zod + `zodResolver`, theo tiền lệ `features/department/.../schema.ts`.

```ts
// features/group/src/schema/groupSchema.ts
export const createGroupSchema = z.object({
  name: z.string().trim().min(1, GROUP_MSG.NAME_REQUIRED).max(255, GROUP_MSG.NAME_MAX),
  code: z.string().trim().min(1).max(/* ⚠️ BE */ 50),
  description: z.string().max(1000, GROUP_MSG.DESC_MAX).optional(),
  parentId: z.string().nullable().optional(),
});
```

- Trùng mã (`BR-1.1`) **kiểm cuối ở BE** → bắt lỗi qua error code (xem §10); FE chỉ chặn sớm những gì biết được client-side (độ dài, nhánh con/vòng khi kéo thả).
- `moveGroupSchema` / helper `validateGroupMove()` ở `utils/treeHelpers.ts`: kiểm vòng trước khi gọi API. **Không kiểm độ sâu** (CR6 bỏ giới hạn số cấp).

---

## 10. Xử lý lỗi

- **Toast tự động:** interceptor axios trong `@ops/service` và `useAppMutation` đã tự `toast.error` theo error code BE (có `toastExceptions` allowlist). FE **không** lặp lại toast cho các lỗi đó.
- **Lỗi validate field** → inline trong form (RHF).
- **Error code cần map riêng** (hiển thị đúng câu trong PRD thay vì toast chung) — khai enum, dùng `toastExceptions` để tự xử:
  ```ts
  export enum GroupErrorCode {
    DUPLICATE_CODE     = 'GROUP_DUPLICATE_CODE',      // "Mã nhóm đã tồn tại"
    MOVE_INTO_SELF     = 'GROUP_MOVE_INTO_SELF',      // "Không thể di chuyển nhóm vào chính nó hoặc nhánh con"
    HAS_HISTORY        = 'GROUP_HAS_HISTORY',         // không xoá được
    CLASS_ENDED        = 'GROUP_CLASS_ENDED',         // luật đứng dừng im lặng (chỉ log, không toast)
  }
  ```
  ⚠️ **Chốt danh sách error code với BE.** Bỏ `MAX_DEPTH_EXCEEDED` (CR6 bỏ giới hạn số cấp).

---

## 11. Hiệu năng

- **Cây lazy-load theo nhánh** (`BR-6.1`): mỗi `parentId` một query, `staleTime` 60s.
- **Phân trang** bảng danh sách (20/trang), màn theo dõi nhánh, nhật ký (`keepPreviousData`).
- **Debounce** ô tìm kiếm 300ms.
- **Việc nền chạy ở BE** (đồng bộ 53 nhóm/384 người, giao nội dung nhóm 55 người, import): FE hiển thị trạng thái qua job/poll (`ModalImport`) hoặc optimistic + invalidate, **không chặn giao diện** (NFR US5/US7).
- **Virtualize** danh sách rất dài nếu cần (`react-virtualized` đã có trong repo qua tree-course).

---

## 12. lms-fe — màn học viên và quản lý

**US17 — khối "Quản lý của tôi"** trên hồ sơ học viên (Next.js App Router, `@lms/*`):

- Đặt trong khu hồ sơ học viên hiện có; page `'use client'` bọc `withAuthorization`, có thể render qua `Slot` nếu khu đó dùng pattern slot.
- Hiển thị **nhiều** quản lý: ảnh · họ tên · email (**không** số điện thoại `BR-17.2`). Quản lý chính lên đầu, có nhãn (`BR-17.3`). Chỉ xem (`BR-17.1`). Không hiển thị học viên thuộc nhóm nào (`BR-17.4`). Trạng thái rỗng: *Chưa có thông tin quản lý. Liên hệ bộ phận vận hành nếu cần.*
- Data: react-query v3 + `@lms/api` (thêm `GroupAPI.getMyManagers()` trong `libs/api/api/group/` ⚠️ BE).

> **US16 KHÔNG ở lms-fe.** PRD `BR-16.7` chốt màn theo dõi nhánh nằm ở **UpLMS Ops** (ops-fe), quản lý đăng nhập bằng tài khoản học viên đã được gán làm quản lý ở `US9`, tài khoản đó vào UpLMS Ops chỉ thấy màn theo dõi nhánh (CR6). lms-fe chỉ có US17.

---

## 13. Phụ thuộc BE và câu hỏi cần chốt

| # | Nội dung | Chặn | Cần ai |
|---|---|---|---|
| 1 | **API contract đầy đủ** cho `IGroupAPI` (endpoint, params, shape response, phân trang) | Chặn code thật (khung dựng được trước) | BE |
| 2 | **Danh sách quyền `gr_*` đầy đủ** — hiện mới có view/create/edit/remove; cần quyền cho nhật ký, giao nội dung, gán quản lý/mentor, và màn theo dõi nhánh (đọc theo quan hệ quản lý — Vấn đề tồn đọng #2 của PRD) | Chặn U4/U5 | BE · PO |
| 3 | **Cờ `isManager`** trên profile để hiện menu `/my-team` và route guard US16 | Chặn US16 | BE |
| 4 | **Error code** cho các luật nghiệp vụ (trùng mã, vượt cấp, có lịch sử, lớp đã kết thúc…) để map câu thông báo đúng PRD | Chặn hoàn thiện UX lỗi | BE |
| 5 | **`type` import mới** `GROUP_MEMBER` trong `ModalImport` + job import phía BE + file mẫu `.xlsx` | Chặn US4 | BE · FE |
---

## 14. Lịch sử tài liệu

| Version | Ngày | Người | Thay đổi |
|---|---|---|---|
| 1.0 | 2026-10-21 | Tech Team | Bản draft đầu, path giả định |
| 2.0 | 2026-10-23 | Tech Team | Viết lại theo codebase thật (ops-fe pnpm workspaces, DI qua `useFeature`, react-query v3, antd v5, RHF+Zod). Ánh xạ đủ 20 US → component. Phát hiện scaffolding Group có sẵn (`TITLE_GROUPS_GR`, `ID_SIDE_BAR.LIST_GROUP`). Thêm hướng dẫn đăng ký feature, tầng API/DI, các tương tác khó, phụ thuộc BE |
| 2.1 | 2026-10-23 | Tech Team | Cập nhật theo PRD v0.6 (CR6): Bỏ giới hạn số cấp cây (`BR-1.3`, `BR-1.4`, `BR-2.2` không còn); US18 thay đổi từ dashboard thành **tab Báo cáo trong chi tiết nhóm**; một người nhiều vai (quản lý/mentor/thành viên) bằng một tài khoản học viên (`BR-16.7`, `BR-12.8`); thông báo không gửi cho chính người; mentor vừa là thành viên tạm được tự chấm. Sửa §1.1, §3, §7, §12 |

---

**Việc tiếp theo để chuẩn bị làm:**
1. Chốt API contract `IGroupAPI` với BE (mục #1, #2 §13) — đặc biệt `getGroupReport(groupId, params)` cho US18.
2. **Chốt cơ chế auth cho tài khoản học viên vào UpLMS Ops** (§8.0) — cờ `isManager`/`isMentor`, claim, hay API check.
3. Dựng khung `features/group` + đăng ký module (§2) + wire API rỗng (mock) để chạy được route.
4. Làm trước **U1** (US1, US3, US4, US6) — không phụ thuộc nguồn ngoài, mang giá trị thấy ngay; rồi **U3** (US7, US8).
5. Chuẩn bị file mẫu import và thêm `type='GROUP_MEMBER'`.
6. Phối hợp `features/user` để thêm khối Quản lý vào hồ sơ học viên (US11).

**Rủi ro chính:**
- Cơ chế auth cho quản lý/mentor vào UpLMS Ops chưa rõ (§8.0) — **chặn US16**.
- Ma trận quyền đầy đủ chưa có (mục #2 §13) — ảnh hưởng U4, U5.
- US18 là tab trong detail, không phải dashboard — kiến trúc query khác ban đầu tưởng.
