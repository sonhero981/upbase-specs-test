---
description: "Chạy trọn một Bolt fullstack từ store - mở change run ở mọi repo, tạo task FE + BE, code lần lượt từng repo bằng subagent theo rule repo đó, review, verify, PR"
argument-hint: "[tên change Bolt, vd 260923-gamification-b01-foundation]"
---

# /bolt — chạy cả Bolt ở một chỗ

Mở Claude ở gốc repo khung. Danh sách repo, đường dẫn, owner, convention và gate của từng repo lấy từ `repos:` trong `workspace.yaml`; `.claude/settings.json` (do `scripts/setup.py` sinh từ chính danh sách đó) cho phép sửa các repo ấy. Repo của Bolt lấy theo dòng Repo của Bolt và phải nằm trong danh sách. Mỗi repo vẫn có change `run` riêng (`context.md`, `tasks.md`, `progress.md`) vì mỗi repo là một PR; `/bolt` chỉ gom thao tác về một chỗ. `/fe`, `/be` ở từng repo vẫn dùng được (khi chỉ làm một phía, hoặc người khác cầm phần đó).

Luật:
- **Menu trước, quét sau** (như `/fe`).
- Mỗi repo code bằng **một subagent foreground** (context sạch, đúng rule repo đó); repo này xong mới sang repo kế.
- Command riêng của repo (`/opsx:apply`, `/ui-gate`, `/fe:review`, `/be:review`, `/opsx:verify`, `/opsx:archive`) không gọi được từ store: subagent **đọc file command trong repo đó và làm theo**.
- Không tự commit / push / tạo PR, không tạo branch khi chưa hỏi. Typecheck một lần cuối mỗi repo.
- Change có banner `[DEMO` / `[TEST]` là mẫu, bỏ qua.

## Bước 1 — Chọn Bolt

- Có `$ARGUMENTS`: dùng tên đó, sang bước 2.
- Không có: AskUserQuestion **ngay** (chưa quét), 3 lựa chọn: **Bolt đang làm dở** (tìm Bolt đã có change ở repo) · **Bolt mới** (tìm Bolt chưa mở ở repo nào) · **Tất cả Bolt**. Chọn xong mới quét:
  - `git pull --ff-only` (store); mỗi `openspec/changes/*` (bỏ `archive/`, mẫu): bảng đầu `proposal.md` (Repo, Owner, Intent, Phụ thuộc, Ước lượng).
  - Mỗi repo trong dòng Repo: có `<path repo>/openspec/changes/<tên>` chưa, task xong / tổng.
  - Hỏi danh sách (tối đa 3 + "Bolt khác"); description `owner · repo: <id> <xong>/<tổng>, … · ước lượng`.

## Bước 2 — Kiểm cổng (không đạt thì dừng, nói ai cần làm gì)

- Contract của intent (`intents/<slug>/inception/contract-design/contract-summary.md`) có `Approved by -`.
- `grep -rn "NEEDS CLARIFICATION" openspec/changes/<tên>` rỗng.
- `python engine/tech/scripts/tech-tools.py check intents/<slug> --stage=code-generation --bolt=<Bnn>` đạt.
- Bolt trong dòng "Phụ thuộc" của proposal: task merge ở change Bolt store đã tick (chưa thì cảnh báo, hỏi có làm tiếp không).

## Bước 3 — Mở change `run` ở mọi repo của Bolt

Với từng repo trong dòng Repo (theo thứ tự section trong `code-generation-plan.md`):
- Chưa có change: `cd <path repo> && openspec new change <tên> --schema run`; lấy `openspec instructions context --change <tên>` và `... tasks ...` (chạy trong repo đó để dùng rules `openspec/config.yaml` của repo) rồi viết `context.md` (Store commit = `git rev-parse --short HEAD` của store) và `tasks.md` = section `## <repo>` của plan.
- Đã có: giữ nguyên; so "Store commit" với store trên các path "Đọc trước khi code" — đổi thì tóm tắt, hỏi cập nhật `tasks.md` (theo `opsx/update.md` của repo).
- In bảng: `repo · change · task xong / tổng · branch hiện tại · Pause`.

## Bước 4 — Jira

Bolt chưa có subtask: đọc ``.claude/commands/jira-tasks.md` của repo FE` và làm theo, nguồn là `bolt-plan.md` + `tasks.md` của mọi repo (một ticket Bolt, subtask theo nhóm task từng repo). Không có MCP Atlassian: bỏ qua, ghi chú.

## Bước 5 — Branch

Mỗi repo: hỏi rồi mới tạo.
- Repo FE: `.claude/rules/02-git-conventions.md` của repo (base `staging`).
- Repo khác: quy ước branch của repo đó; base theo dòng Branch trong `context.md`.
Quy ước branch và base của từng repo trong sản phẩm đang cài: `domain/tech-adjustments.md` mục `bolt`.
Ghi branch vào bảng `context.md` của repo.

## Bước 6 — Code từng repo (subagent)

Thứ tự repo theo mục "Cách đọc" của plan; không có thì theo `build_order` trong `workspace.yaml` (mặc định `library` → `backend` → `frontend`). FE mock theo contract tới khi BE lên môi trường chung. Ràng buộc riêng giữa các repo của sản phẩm đang cài: `domain/tech-adjustments.md` mục `bolt`. Bỏ qua repo đã hết task trước nhóm Kết thúc.

Prompt subagent (Agent, `general-purpose`, foreground), điền giá trị thật:
```
Bạn là owner Bolt, code phần <repo> của change <tên>. Làm việc trong <path repo> theo `workspace.yaml` (chạy lệnh bằng cd vào repo).
Đọc trước, theo đúng repo:
- Convention của repo: cột `conventions` của repo đó trong workspace.yaml, đọc các mục liên quan tới task.
- openspec/config.yaml (rules, guidance apply) và file <path repo>/.claude/commands\opsx\apply.md.
Lấy hướng dẫn: `cd <path repo> && openspec instructions apply --change <tên> --json`; làm đúng instruction + guidance: đọc progress.md, context.md, kiểm Store commit, Pause.
Task UI (repo FE): trước khi code đọc và làm theo .claude/commands/ui-gate/build.md; trước khi tick đọc và làm theo .claude/commands/ui-gate/review.md.
Cách verify và cách build của repo này: cột `gate` trong workspace.yaml, chi tiết ở domain/tech-adjustments.md mục bolt. Thiếu thứ cần để verify thì ghi BLOCKED, không bỏ qua.
Làm task chưa tick trong tasks.md theo thứ tự, DỪNG trước nhóm "Kết thúc"; tick ngay khi verify đạt; cuối lượt ghi một khối progress.md.
Không git commit / push; không typecheck giữa chừng; thiết kế / contract sai thì dừng, ghi progress.md, báo lại.
Trả về: task đã xong, task còn lại, blocker, file đã sửa, kết quả verify.
```
Sau mỗi subagent: in tóm tắt. Có blocker → hỏi (Pause theo schema / sửa ở store / bỏ qua sang repo kế). Còn task → hỏi chạy tiếp lượt nữa.

## Bước 7 — Kết thúc từng repo

Khi repo chỉ còn nhóm Kết thúc:
1. Typecheck + lint theo cột `gate` của repo trong `workspace.yaml` và `openspec/config.yaml` của repo.
2. **Review độc lập**: subagent mới, đọc và làm theo lệnh review của chính repo đó (`.claude/commands/fe/review.md` với repo `kind: frontend` và `library`, `be/review.md` với `kind: backend`). Còn lỗi Chặn → quay lại bước 6 cho repo đó.
3. FE: `CLAUDE.md` feature theo `openspec/schemas/run/templates/feature-claude.md`.
4. Verify: đọc và làm theo `<path repo>/.claude/commands\opsx/verify.md`.
5. Hỏi xác nhận rồi commit + push; in link PR theo mẫu PR của repo đó.
   Repo `kind: library` sau merge: publish xong thì ghi version mới vào mục `## <repo id>` của `code-generation-plan.md` ở store; repo nào còn task nâng version thì quay lại bước 6 cho repo đó.
6. Store: tick task tương ứng trong `openspec/changes/<tên>/tasks.md`; cập nhật bảng Construction trong `tech-state.md` (Bolt "Đang code" / "Chờ demo").

## Bước 8 — Sau merge

- QA chạy 3.6: `/tech <slug> bolt <Bnn>`.
- Archive từng repo (đọc `opsx/archive.md` của repo), rồi archive change Bolt ở store.

## Làm tiếp hôm sau

`/bolt <tên>` → bước 3 thấy change đã có, in bảng tiến độ → bước 6 bắt đầu từ repo còn task.
