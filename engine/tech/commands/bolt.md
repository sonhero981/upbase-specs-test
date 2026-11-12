---
description: "Chạy một Bolt từ store - kiểm cổng, mở change ở mọi repo; repo flow opsx code bằng subagent, repo flow comet thì bàn giao cho phiên /comet mở trong repo đó"
argument-hint: "[tên change Bolt, vd 260923-gamification-b01-foundation]"
---

# /bolt — chạy cả Bolt ở một chỗ

Mở Claude ở gốc repo khung. Danh sách repo, đường dẫn, owner, convention, gate và `flow` của từng repo lấy từ `repos:` trong `workspace.yaml`; `.claude/settings.json` (do `scripts/setup.py` sinh từ chính danh sách đó) cho phép sửa các repo ấy. Repo của Bolt lấy theo dòng Repo của Bolt và phải nằm trong danh sách. Mỗi repo có change riêng vì mỗi repo là một PR; `/bolt` chỉ gom thao tác về một chỗ. `/fe`, `/be` ở từng repo vẫn dùng được (khi chỉ làm một phía, hoặc người khác cầm phần đó).

## Hai luồng theo repo

Cột `flow` của repo trong `workspace.yaml`:

| `flow` | Ai code | Change ở repo |
|---|---|---|
| `opsx` (mặc định khi không khai) | Subagent do `/bolt` chạy, đọc `opsx/apply.md` của repo | Theo cột `change_style` (bảng kế) |
| `comet` | Phiên Claude mở **trong repo đó**, chạy `/comet` | `/comet-open` tự tạo change và khởi tạo state; `/bolt` **không tạo** (Comet cấm `openspec new change` trực tiếp) |

Repo `opsx` còn một cột nữa, `change_style`, vì không phải repo nào cũng tổ chức change theo Bolt:

| `change_style` | Change ở repo | Ai tạo |
|---|---|---|
| `bolt` (mặc định khi không khai) | Một change cho mỗi Bolt, tên giống tên change Bolt, schema `run` (con trỏ về store, ghi Store commit) | `/bolt` tạo ở bước 3 |
| `feature` | Một change cho mỗi feature, tên theo ticket (quy ước của repo), schema `*-feature`, PRD đến từ BA ngoài store, việc chia Work Package và giao owner | Người tạo bằng `/opsx:new`; `/bolt` **không tạo**, chỉ tìm và ghi lại change nào đang giữ việc của Bolt |

Vì sao repo `comet` không chạy bằng subagent: Comet có nhiều điểm dừng chờ người (xác nhận Open, duyệt Design, chọn cấu hình Build, chọn cách giao ở Archive) và hook cổng Tech nằm trong cấu hình của chính repo, chỉ chạy khi phiên Claude mở trong repo. Subagent foreground của `/bolt` không hỏi người được, nên `/bolt` bàn giao rồi dừng.

Luật:
- **Menu trước, quét sau** (như `/fe`).
- Repo `opsx`: mỗi repo bằng **một subagent foreground** (context sạch, đúng rule repo đó); repo này xong mới sang repo kế.
- Command riêng của repo (`/opsx:apply`, `/ui-gate`, `/fe:review`, `/be:review`, `/opsx:verify`, `/opsx:archive`) không gọi được từ store: subagent **đọc file command trong repo đó và làm theo**.
- Repo `comet`: `/bolt` không chạy pha nào của Comet, không viết `proposal.md`, `design.md`, `tasks.md` thay Comet.
- Không tự commit / push / tạo PR, không tạo branch khi chưa hỏi. Typecheck một lần cuối mỗi repo `opsx`. Repo `comet` commit/push/PR do pha Archive của Comet làm sau khi người chọn cách giao.
- Change có banner `[DEMO` / `[TEST]` là mẫu, bỏ qua.

## Bước 1 — Chọn Bolt

- Có `$ARGUMENTS`: dùng tên đó, sang bước 2.
- Không có: AskUserQuestion **ngay** (chưa quét), 3 lựa chọn: **Bolt đang làm dở** (tìm Bolt đã có change ở repo) · **Bolt mới** (tìm Bolt chưa mở ở repo nào) · **Tất cả Bolt**. Chọn xong mới quét:
  - `git pull --ff-only` (store); mỗi `openspec/changes/*` (bỏ `archive/`, mẫu): bảng đầu `proposal.md` (Repo, Owner, Intent, Phụ thuộc, Ước lượng).
  - Mỗi repo trong dòng Repo: có `<path repo>/openspec/changes/<tên>` chưa (repo `opsx` kiểu `change_style: feature`: lấy tên change từ cột "Change ở repo" của `handoff.md`, chưa ghi thì coi là chưa mở). Repo `opsx`: task xong / tổng. Repo `comet`: đọc pha bằng `comet status <path repo>` (chỉ đọc).
  - Hỏi danh sách (tối đa 3 + "Bolt khác"); description `owner · repo: <id> <xong>/<tổng>, … · ước lượng`.

## Bước 2 — Kiểm cổng (không đạt thì dừng, nói ai cần làm gì)

- Contract của intent (`intents/<slug>/inception/contract-design/contract-summary.md`) có `Approved by -`.
- `grep -rn "NEEDS CLARIFICATION" openspec/changes/<tên>` rỗng.
- `python engine/tech/scripts/tech-tools.py check intents/<slug> --stage=code-generation --bolt=<Bnn>` đạt.
- Bolt trong dòng "Phụ thuộc" của proposal: task merge ở change Bolt store đã tick (chưa thì cảnh báo, hỏi có làm tiếp không).

Repo `comet` còn một lớp nữa ngoài `/bolt`: hook `comet-tech-gate` của repo chặn Comet rời pha Design (hoặc hoàn tất pha Open của preset hotfix/tweak) khi contract chưa `status: agreed` hoặc còn `NEEDS CLARIFICATION`. Miễn cổng cho một change phải do **người** tạo `<change>/.comet/tech-gate-waiver.md` ngoài Claude; agent không được ghi file này.

## Bước 3 — Mở change ở mọi repo của Bolt

Với từng repo trong dòng Repo (theo thứ tự section trong `code-generation-plan.md`):

**Repo `opsx`, `change_style: bolt` (mặc định):**
- Chưa có change: `cd <path repo> && openspec new change <tên> --schema run`; lấy `openspec instructions context --change <tên>` và `... tasks ...` (chạy trong repo đó để dùng rules `openspec/config.yaml` của repo) rồi viết `context.md` (Store commit = `git rev-parse --short HEAD` của store) và `tasks.md` = section `## <repo>` của plan.
- Đã có: giữ nguyên; so "Store commit" với store trên các path "Đọc trước khi code" — đổi thì tóm tắt, hỏi cập nhật `tasks.md` (theo `opsx/update.md` của repo).

**Repo `opsx`, `change_style: feature`:** không tạo change và không đặt tên ticket thay người.
- Tìm change của Bolt ở repo theo thứ tự: (1) cột "Change ở repo" của `handoff.md` nếu đã ghi; (2) chưa có thì AskUserQuestion, liệt kê change chưa archive của repo (`openspec list --json` chạy trong repo; description `schema · task xong / tổng`) cộng lựa chọn "Chưa có change cho Bolt này". Có thể gợi ý theo intent hoặc ticket nhưng không tự chọn thay người. Một change đã xong hết task từ trước khi Bolt được lên kế hoạch thường không chứa việc của Bolt này: hỏi lại, không ghép.
- Người chọn một change: so nhóm task thô của repo trong change Bolt với `tasks.md` của change đó (theo tên việc và mã plan). Không phủ hết thì liệt kê phần thiếu và hỏi: bổ sung vào change bằng `/opsx:update` của repo, hoặc mở change mới.
- Chưa có change: dừng ở repo này và nói rõ owner repo cần làm gì: mở change theo quy ước của repo (`/opsx:new <tên theo ticket> --schema <schema của repo>` rồi `/opsx:propose`, nguồn là PRD, thiết kế và plan ở store), rồi chạy lại `/bolt`.
- Ghi change đã chọn vào cột "Change ở repo" của `handoff.md` (tạo file theo mẫu nếu chưa có, như ở repo `comet`).

**Repo `comet`:** không tạo change.
- Kiểm repo đã cài Comet: có `<path repo>/.comet/config.yaml`. Thiếu thì dừng, chỉ `SETUP.md` mục Comet.
- Change `<tên>` đã có ở repo: in pha hiện tại từ `comet status <path repo>`, không soạn lại.
- Chưa có: ghi **gói bàn giao** vào `openspec/changes/<tên>/handoff.md` ở store, theo `engine/tech/templates/handoff.md` (file này không phải artifact của schema `bolt`, `openspec validate` bỏ qua). Điền: tên change (đúng tên change Bolt), intent, owner, Jira, version PRD / contract, `store_commit` (`git -C <store> rev-parse --short HEAD`) và `store_dirty` (`git -C <store> status --porcelain -- intents/<slug> openspec/changes/<tên>` khác rỗng thì `true`, kèm tệp chưa commit ở mục "Quyết định chung"), mục riêng cho từng repo `comet` (đường dẫn store cần đọc: section `## <repo>` của plan, contract, ui-map, test case, `specs/` của Bolt; nhóm task thô của repo trong `tasks.md` của change Bolt), và bảng tiến độ. Đã có `handoff.md`: giữ nguyên "Quyết định chung" (người sửa tay), chỉ cập nhật `store_commit`, `store_dirty`, `written_at` và cột Trạng thái; `store_commit` đổi so với lần ghi trước thì tóm tắt tài liệu nào đổi và hỏi có cập nhật mục repo không. Không tự commit file này.

In bảng: `repo · flow · change · task xong / tổng hoặc pha Comet · branch hiện tại · Pause`.

## Bước 4 — Jira

Bolt chưa có subtask: đọc ``.claude/commands/jira-tasks.md` của repo FE` và làm theo, nguồn là `bolt-plan.md` + `tasks.md` của mọi repo (một ticket Bolt, subtask theo nhóm task từng repo). Repo `comet` chưa có `tasks.md` trước khi `/comet-open` xong: dùng nhóm task thô trong change Bolt ở store, và chạy lại bước này sau khi Open xong nếu `tasks.md` chi tiết đổi nhóm. Không có MCP Atlassian: bỏ qua, ghi chú.

## Bước 5 — Branch

Mỗi repo: hỏi rồi mới tạo.
- Repo FE: `.claude/rules/02-git-conventions.md` của repo (base `staging`).
- Repo khác: quy ước branch của repo đó; base theo dòng Branch trong `context.md` (repo `opsx` kiểu `bolt`), theo quy ước branch của repo cho feature nhiều dev (repo `opsx` kiểu `feature`), hoặc trong gói bàn giao (repo `comet`).
Quy ước branch và base của từng repo trong sản phẩm đang cài: `domain/tech-adjustments.md` mục `bolt`.
Repo `opsx`: ghi branch vào bảng `context.md` của repo. Repo `comet`: **tạo branch trước khi chạy `/comet-open`**, vì Comet gắn change với branch hiện tại (`isolation: current`); ghi branch vào bảng "Tiến độ theo repo" của `handoff.md`.

## Bước 6 — Code từng repo

Thứ tự repo theo mục "Cách đọc" của plan; không có thì theo `build_order` trong `workspace.yaml` (mặc định `library` → `backend` → `frontend`). FE mock theo contract tới khi BE lên môi trường chung. Ràng buộc riêng giữa các repo của sản phẩm đang cài: `domain/tech-adjustments.md` mục `bolt`. Bỏ qua repo đã hết task trước nhóm Kết thúc (repo `comet`: đã archive).

### Repo `opsx` — subagent

Prompt subagent (Agent, `general-purpose`, foreground), điền giá trị thật:
```
Bạn là owner Bolt, code phần <repo> của change <change ở repo> (kiểu `bolt`: <tên>; kiểu `feature`: change ghi ở cột "Change ở repo" của handoff.md). Làm việc trong <path repo> theo `workspace.yaml` (chạy lệnh bằng cd vào repo).
Đọc trước, theo đúng repo:
- Convention của repo: cột `conventions` của repo đó trong workspace.yaml, đọc các mục liên quan tới task.
- openspec/config.yaml (rules, guidance apply) và file <path repo>/.claude/commands\opsx\apply.md.
Lấy hướng dẫn: `cd <path repo> && openspec instructions apply --change <change ở repo> --json`; làm đúng instruction + guidance của repo: đọc progress.md, context.md (nếu có), kiểm Store commit (nếu có), Pause. Change kiểu `feature`: chỉ làm Work Package có owner trùng `git config user.email`, theo đúng hướng dẫn apply của repo.
Task UI (repo FE): trước khi code đọc và làm theo .claude/commands/ui-gate/build.md; trước khi tick đọc và làm theo .claude/commands/ui-gate/review.md.
Cách verify và cách build của repo này: cột `gate` trong workspace.yaml, chi tiết ở domain/tech-adjustments.md mục bolt. Thiếu thứ cần để verify thì ghi BLOCKED, không bỏ qua.
Làm task chưa tick trong tasks.md theo thứ tự, DỪNG trước nhóm "Kết thúc"; tick ngay khi verify đạt; cuối lượt ghi một khối progress.md.
Không git commit / push; không typecheck giữa chừng; thiết kế / contract sai thì dừng, ghi progress.md, báo lại.
Trả về: task đã xong, task còn lại, blocker, file đã sửa, kết quả verify.
```
Sau mỗi subagent: in tóm tắt. Có blocker → hỏi (Pause theo schema / sửa ở store / bỏ qua sang repo kế). Còn task → hỏi chạy tiếp lượt nữa.

### Repo `comet` — bàn giao rồi dừng

Chỉ in bàn giao cho **repo đến lượt** (theo thứ tự trên); repo kế chỉ in khi repo này đã xong. In:
```
Repo <id> — mở Claude Code TRONG <path repo>, nhánh <branch>, chạy:
  /comet-open <tên change>
rồi bảo Claude đọc `<store>/openspec/changes/<tên>/handoff.md` mục "Repo <id>" trước khi tạo artifact (không cần dán gì).
Trong pha Design: design.md là con trỏ tới thiết kế Tech đã duyệt ở store, không brainstorm lại.
Mỗi pha do bạn gọi tiếp (auto_transition = false). Cổng Tech là hook của repo.
Xong khi: change đã archive (có trong <path repo>/openspec/changes/archive/) và PR đã merge.
Quay lại: /bolt <tên> để lấy repo kế.
```
Rồi dừng, không chạy tiếp. Không dùng Agent để chạy `/comet-*`.

## Bước 7 — Kết thúc từng repo

### Repo `opsx`

Khi repo chỉ còn nhóm Kết thúc:
1. Typecheck + lint theo cột `gate` của repo trong `workspace.yaml` và `openspec/config.yaml` của repo.
2. **Review độc lập**: subagent mới, đọc và làm theo lệnh review của chính repo đó (`.claude/commands/fe/review.md` với repo `kind: frontend` và `library`, `be/review.md` với `kind: backend`). Còn lỗi Chặn → quay lại bước 6 cho repo đó.
3. FE: `CLAUDE.md` feature theo `openspec/schemas/run/templates/feature-claude.md`.
4. Verify: đọc và làm theo `<path repo>/.claude/commands\opsx/verify.md`.
5. Hỏi xác nhận rồi commit + push; in link PR theo mẫu PR của repo đó.

### Repo `comet`

Typecheck, review độc lập, verify, commit, push, PR đều nằm trong pha Verify và Archive của Comet; `/bolt` không lặp lại. Khi người quay lại `/bolt <tên>` và repo đã archive + PR đã merge, cập nhật cột Trạng thái của repo đó trong `handoff.md` (`Đã archive` hoặc `PR đã merge`, kèm ngày và link PR), rồi làm tiếp mục chung dưới đây.

### Chung cho mọi repo

- Repo `kind: library` sau merge: publish xong thì ghi version mới vào mục `## <repo id>` của `code-generation-plan.md` ở store; repo nào còn task nâng version thì quay lại bước 6 cho repo đó.
- Store: tick task tương ứng trong `openspec/changes/<tên>/tasks.md`; cập nhật bảng Construction trong `tech-state.md` (Bolt "Đang code" / "Chờ demo").

## Bước 8 — Sau merge

- QA chạy 3.6: `/tech <slug> bolt <Bnn>`.
- Archive: repo `opsx` đọc `opsx/archive.md` của repo; repo `comet` đã archive ở pha Archive của Comet. Sau đó archive change Bolt ở store.

## Làm tiếp hôm sau

`/bolt <tên>` → bước 3 thấy change đã có: repo `opsx` in bảng tiến độ, repo `comet` in pha từ `comet status` → bước 6 bắt đầu từ repo còn việc.
