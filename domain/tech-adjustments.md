# Điều chỉnh của sản phẩm cho từng stage Tech — UpLnD

Phần riêng của sản phẩm đang cài, tách khỏi `engine/` ngày 2026-10-26 để engine không phụ thuộc sản phẩm.
Mỗi stage Tech trong `engine/tech/stages/` trỏ về mục tương ứng ở đây. Tên repo, đường dẫn, convention và
gate của từng repo lấy từ [`workspace.yaml`](../workspace.yaml); file này chỉ ghi điều chỉnh nội dung stage.

Đổi sang sản phẩm khác: viết lại file này, không sửa `engine/`.


## build-and-test

- Build: lệnh build/lint/typecheck từng repo (lms-fe `pnpm --filter <app> check-types`, ops-fe `pnpm typecheck:ops-fe`, lms-be theo rule repo).
- Integration: chạy `x-curl` của mỗi contract trên local (lms-be `openspec/conventions/verification.md`: service do người dùng bật, thiếu env → BLOCKED). Pass thì contract chuyển **Final** kèm bằng chứng trong `contract-summary.md` (PR store).
- `test-results.md`: từng TC của Bolt Pass / Fail / Blocked, người chạy, môi trường. Fail → quay lại 3.5 Part 2 (đúng loop-back 3.6 → 3.5 của AWS).
- `cross-unit-traceability.md`: AC → BR → TC → PR cho mọi Unit của Bolt.


## contract-design

- Contract gồm mọi REST/socket/Kafka giữa lms-be và lms-fe / ops-fe, giữa các Unit, và API dùng ngoài hệ thống.
- Mỗi contract một khối ```yaml **OpenAPI 3** (REST) hoặc **AsyncAPI** (socket, Kafka); dữ liệu dùng chung → shared-schema block.
- Đủ checklist lms-be `openspec/conventions/backend.md` § 2 API, § 3 DTO/exception: quyền, validation, lỗi + exception code, Swagger `operationId`, tương thích ngược, `tags: []`; thêm `x-curl` (một lệnh curl đại diện, `<auth-value>`). Event đủ `openspec/conventions/backend.md` § 4 Kafka event và job, spec có scenario message trùng (rule `specs` trong `lms-be/openspec/config.yaml`): payload, version, message key, idempotency, failure path.
- Endpoint "có sẵn / sửa" kèm `file:line` DTO thật ở `origin/staging`.
- Trạng thái mỗi contract: **Draft** → **Agreed** (BE lead ký, được code) → **Final** (sau curl verify ở 3.6). Contract này thay `_API_CONTRACT_TEMPLATE.md` của lms-be cho feature đi qua store.
- Không điền "Approved by" trước khi review cuối READY.
- Bắt buộc mục `### Phủ cạnh DAG`: bảng `| Cạnh (A phụ thuộc B) | Contract | Ghi chú |`, mỗi cạnh của DAG 2.7 một dòng dạng `U3 → U1`; cạnh không cần contract ghi lý do ở cột Contract.
- AsyncAPI cho event chạy đồng bộ trong process: thêm `x-transport: in-process-sync`.
- Contract buộc chỉnh nhỏ artifact 2.6/2.7 đã duyệt: ghi thành điều kiện gate ở `decisions.md` (mã `DEC-T<n>`); chỉnh lớn (đổi Unit, DAG) thì mở lại stage đó `[R]`.


## delivery-planning

- **Chia đủ Bolt cho mọi Unit của phạm vi** (mặc định cả intent) để giao việc cho cả team ở buổi họp; không để Unit nào chưa thuộc Bolt.
- `team-allocation.md`: "mob" = dev code thật (owner Bolt), không phải agent. Một owner làm trọn mọi repo của Bolt (fullstack). Ghi năng lực từng người (người × ngày) và so với tổng ngày công; gán owner cho **từng** Bolt, cân tải, ưu tiên cho chạy song song các Bolt không phụ thuộc nhau (khác owner); vượt năng lực thì đề xuất cắt đợt, PO chốt ở họp.
- `bolt-plan.md` có lịch dự kiến theo người (Bolt nào ai làm, bắt đầu / kết thúc theo ngày công luỹ kế, Bolt song song) để làm đầu vào cho `/jira-tasks` và sprint.
- `bolt-plan.md` có bảng tóm tắt (script đọc): `| Bolt | Units | Owner | Repo | Ngày công | Phụ thuộc |` với `Units` ghi `U{n}`; mỗi Unit ở đúng một Bolt. Mỗi Bolt: Units, walking-skeleton marker, DoD, confidence hypothesis, demo, TC (`TC-n`).
- B01 = walking skeleton (Unit đầu DAG). Thứ tự phải theo DAG của 2.7; lệch thì giải thích ở `risk-and-sequencing-rationale.md`.
- `external-dependency-map.md`: phụ thuộc ngoài (PO trả lời câu hỏi, design Figma, BE lên staging, quyền BA điền `tags`, team khác).
- Ràng buộc release (Bolt phải lên production cùng nhau, cutover) ghi ở `risk-and-sequencing-rationale.md` mục riêng.
- Bảng tóm tắt là bảng ĐẦU TIÊN có header `| Bolt | Units | …`; bảng chi tiết từng Bolt không dùng header đó.
- Phase check Inception (Step 5 AWS, `verification/phase-check-inception.md` thuộc PO): ghi mục `## Phase boundary verification` trong `bolt-plan.md`.


## domain-design

- `components.md`: catalogue yaml đúng well-formedness của AWS; thêm trường `repo` cho mỗi component (lms-be / lms-fe / ops-fe / lms-package). Component "có sẵn" hay "sửa" kèm `file:line`.
- `decisions.md`: ADR theo template AWS. Intent v1 (không có HLD Brief) thì ghi hướng kỹ thuật ở đây. Quyết định dùng lại nhánh WIP hay không (từ codekb) là một ADR.
- Không viết request/response chi tiết (2.8), không entity chi tiết từng field (3.1).
- `traceability.json`: `upstream_ids` = FR/US của phạm vi đợt; AC chưa có mã thì `USn-ACk`.


## functional-design

- **Technology-agnostic đúng AWS**: không code, không SQL, không tên framework/component cụ thể. File, migration, component reuse thuộc 3.5 `code-generation-plan.md`.
- `rules.md`: giữ mã BR của PRD (`BR-5.2` → `id: BR5.2`); rule kỹ thuật mới đánh tiếp số trong nhóm.
- `entities.md`: entity "có sẵn" trong hệ thống ghi nguồn `file:line` (entity lms-be) để 3.5 biết sửa hay tạo.
- `traceability.json`: `upstream_ids` = dòng AC của US thuộc Unit (`USn-ACk` khi PRD chưa có mã AC); mỗi `OK` trỏ `BRx.y` có trong `rules.md`.
- Dựa vào câu hỏi PO chưa trả lời: thẻ `[giả định <stage> Qn]`.
- Thay đổi so với contract 2.8: dừng, sửa `contract-summary.md` (BE lead ký lại) trước.


## nfr-requirements

- Nguồn NFR: `requirements.md` của PO (mục NFR / Constraints), PRD, impact matrix. Ràng buộc chung luôn xét: đa tenant (RLS), múi giờ tenant, Test Account bị loại khỏi logic.
- `tech-stack-decisions.md`: stack có sẵn của repo (codekb `technology-stack.md`) là mặc định; đổi stack là ADR ở `inception/domain-design/decisions.md`.


## reverse-engineering

- **Repo chạm tới**: từ PRD + impact matrix, thường lms-be, lms-fe, ops-fe, lms-package. Mỗi repo một store `codekb/<repo>/`.
- **Đọc code theo `origin/staging`** (lms-package `origin/main`): `git -C <repo> fetch origin`; working tree ở nhánh khác thì đọc bằng `git -C <repo> show|grep origin/staging:…` (Git Bash thêm `MSYS_NO_PATHCONV=1`). Không checkout.
- **Freshness thay cho `codekb-scope-diff`**: `reverse-engineering-timestamp.md` mục `## Scope of Analysis` ghi `commit`, `analyzed.paths`. CURRENT khi `git -C <repo> log --oneline <commit>..origin/staging -- <analyzed.paths>` rỗng; còn lại STALE. CURRENT và đủ phủ → hỏi tech lead dùng lại (`[S]`); STALE hoặc thiếu phủ → quét lại phần thiếu (focused scan), giữ phần còn đúng.
- **Nhánh đang làm dở** chạm vùng (`git -C <repo> branch -r --sort=-committerdate`): ghi ở `reverse-engineering-timestamp.md` mục `## WIP branches`, không coi là code đã có.
- **Không chép convention** đã có ở repo (lms-fe/ops-fe `.claude/rules`, `.claude/inventory`; lms-be `openspec/conventions/*`): `architecture.md`, `code-structure.md` trỏ tới đó.
- Mọi khẳng định kèm `file:line`. Giới hạn hạ tầng (tenant, RLS, idempotency, transaction, mọi đường ghi vào bảng chính) ghi ở `architecture.md` mục riêng.
- Repo lớn: chia agent con theo repo / theo nhóm module, gọi **foreground**, chờ đủ kết quả rồi mới viết.
- Code lệch KB domain của PO hoặc impact matrix: một dòng vào "Ghi chú cho PO" ở `tech-state.md`.
- **Xuyên repo** (AWS không có chỗ, mỗi repo một store): phát hiện chạm nhiều repo (tenant, lỗi 403 / redirect, cache, auth) ghi thêm một dòng ở `codekb/README.md` mục "Bức tranh xuyên repo", trỏ về `architecture.md` của từng repo.
- Không có engine: `reverse-engineering-timestamp.md` ghi thêm dòng `commit:` (origin/staging) cạnh `fingerprint: unknown`; file quá lớn chỉ đọc một đoạn thì ghi `path#Lx-Ly` trong `analyzed.paths`. Focused scan: `component-inventory.md` ghi rõ "phạm vi: …", không cần đủ toàn repo.


## units-generation

- Unit: `U{n}` + thư mục `u{n}-<mô-tả>`, `kind` đúng AWS (`service` / `spec` / `ui` / `packaging` / `library`), cỡ S/M/L/XL, **thêm repo chạm** và **ngày công ước lượng**. Một Unit có thể xuyên repo (BE + FE) nếu xây và test được cùng nhau.
- Proto-Unit của PO là gợi ý ban đầu; ghi Unit nào lấy từ `PU` nào.
- **Walking skeleton bật mặc định** khi intent chạm ≥ 2 repo: Unit đầu DAG (`u0-walking-skeleton` hoặc Unit đầu tiên) là lát mỏng nhất qua mọi điểm tích hợp thật.
- Unit ≤ khoảng 5–6 nhóm AC **và** ≤ ~3 ngày công; vượt thì tách ngay ở đây.
- `unit-of-work-dependency.md` bắt buộc khối ```yaml `units:` (đúng format AWS) — script đọc khối này.
- `unit-of-work-story-map.md`: bảng `| US | Unit |` cho mọi US trong phạm vi đợt; mỗi US đúng một Unit.

## code-generation

Section repo trong `code-generation-plan.md`, thứ tự package → be → fe:

- lms-be: migration theo `openspec/conventions/database.md` § 1, § 3 (RLS), event theo `backend.md` § 4, curl verify theo `verification.md`. Task lms-be của Bolt chạy bằng change `--schema run` ở lms-be (README mục "Quy trình Bolt").
- lms-fe / ops-fe: reuse `.claude/inventory/*` trước khi tạo mới; màn UI theo `construction/<unit>/ui-map/ui-map.md` qua `/ui-gate`.
- Test strategy (thay Testing Contract của engine AWS): lms-be theo `openspec/conventions/verification.md` (curl bắt buộc, unit test khi plan yêu cầu); lms-fe, ops-fe chưa có test runner → Minimal, verify bằng `/ui-gate` + typecheck + TC chạy tay ở 3.6. Ngưỡng coverage của scope AWS không áp: ghi một dòng Accepted risk chuẩn ở `decisions.md` (mã `DEC-T<n>`), không cần bàn lại mỗi Bolt.
- `unit-test-instructions.md` viết ngay ở Part 1 (đúng thứ tự AWS), trước Plan approval.

## bolt

Ràng buộc riêng giữa các repo khi chạy `/bolt`:

- Thứ tự: **lms-package** (consumer cần version mới) và **lms-be** (contract) trước, **ops-fe / lms-fe** sau.
- FE dùng package mới bằng task "nâng `@upbase-tech/<pkg>` lên `<version>`", chỉ sau khi PR lms-package merge `main` và đã publish. Trước đó không link tay vào `node_modules`.
- lms-package sau merge: kiểm version mới có trên GitHub Packages rồi mới cho repo FE nâng version.

Branch và base:

| Repo | Branch | Base | PR |
|---|---|---|---|
| lms-be | theo `openspec/conventions/git.md` | theo dòng Branch trong `context.md` (có thể là branch cá nhân từ branch feature) | MR, mô tả theo `git.md` |
| lms-fe · ops-fe | theo `.claude/rules/02-git-conventions.md` | `staging` | mẫu `openspec/schemas/run/templates/pr.md` |
| lms-package | `feature/<slug>` | `main` | PR vào `main` (merge là publish); ghi package + version cũ → mới + consumer |

Verify và build khi kết thúc từng repo:

| Repo | Lệnh |
|---|---|
| lms-be | build + curl verify theo `openspec/conventions/verification.md` (service do người dùng chạy; thiếu thì BLOCKED) |
| lms-fe | `pnpm --filter <app> check-types` |
| ops-fe | `pnpm typecheck:ops-fe` |
| lms-package | `pnpm --filter <name> build` từng package đã sửa; bump version một lần mỗi package (breaking → major); không publish tay |

Đọc trước khi code, theo repo:

| Repo | Đọc |
|---|---|
| lms-be | `CLAUDE.md`, `openspec/README.md`, `openspec/conventions/*` (mục liên quan) |
| lms-fe · ops-fe | `.claude/CLAUDE.md`, `.claude/rules/01–08`, `.claude/inventory/*` liên quan |
| lms-package | `.claude/CLAUDE.md` (bump version semver, không publish tay, style shadow DOM nằm trong package) |

Việc nhỏ chỉ một repo, không có intent: repo FE dùng `/fix-bug` hoặc change `--schema spec-driven`; lms-be dùng `/opsx:new upbase-<ticket>-<slug>` (schema `be-feature`) hoặc `--schema be-bugfix`.

Comet theo repo (cột `flow` trong `workspace.yaml`):

| Repo | `flow` | Schema mặc định của repo | Ghi chú |
|---|---|---|---|
| ops-fe | `comet` | `fe-feature-comet`: bản của `fe-feature`, chỉ đổi `apply.requires` từ `assignment` sang `tasks` | Comet Classic chỉ nhận artifact `proposal`, `specs`, `design`, `tasks`; `assignment` nằm ngoài nên không đứng trong `apply.requires` được |
| lms-fe · lms-package | `comet` | `run-comet`: `proposal` (con trỏ + mục tiêu), `specs` (bắt buộc với change có intent: Requirement `US<n>` và Scenario `AC <id>` kèm BR, TC, lấy từ specs của Bolt ở store để đọc cùng PRD), `design` (con trỏ tới thiết kế Tech đã duyệt), `tasks` | Schema `run` có artifact `context`, không dùng được với Comet. Thư mục `run` vẫn giữ vì lệnh `/fe`, `/opsx:*` trỏ vào templates của nó |
| lms-be | `opsx`, `change_style: feature` | `be-feature` | Chưa dùng Comet: Comet 0.5.2 từ chối `comet state init` khi gốc repo có `yarn.lock`, và chủ repo chưa cần. Change theo feature, tên `upbase-<ticket>-<slug>`, người tạo bằng `/opsx:new`; không có schema `run`. `/bolt` chỉ tìm change giữ việc của Bolt (hoặc hỏi) và ghi vào cột "Change ở repo" của `handoff.md`, không tự tạo |

- Máy cần Node ≥ 22.16 và `npm i -g @rpamis/comet`. Cài từng repo: `comet init --workflow classic --platform claude --scope project --skip-existing --codegraph skip --language en`, rồi trong `.comet/config.yaml` đặt `artifact_layout: legacy`, `auto_transition: false`, `memory.learning: false`. Cài ở gốc workspace không có tác dụng (Comet ở đó chỉ thấy `docs/openspec/`).
- Cổng Tech là hook trong `.claude/hooks/` của từng repo `comet` (`comet-tech-gate.mjs`, `comet-file-policy.mjs`), nối qua `.claude/settings.json`. Hook chỉ chạy khi phiên Claude mở trong repo.
- Intent đi đường ngắn chưa có `contract-summary.md` (vd `261005-group`, DEC-T1): cổng Tech chặn cho tới khi có contract. Owner repo muốn miễn thì tự tạo `<change>/.comet/tech-gate-waiver.md` (đủ `Cổng bị miễn:`, `Người quyết:`, `Lý do:`) ngoài Claude, ghi điều kiện thu hồi.
- **Specs đọc cùng PRD** (yêu cầu của CTO): change có intent ở repo `comet` phải có `specs/<capability>/spec.md` theo định dạng specs của Bolt ở store (`### Requirement: US<n> …`, `#### Scenario: AC <id> … (BR-x.y)` WHEN/THEN, TC cuối dòng), không đặt `skip_specs: true`. Chỉ change không có intent (refactor, fix nhỏ) mới bỏ qua. Hook `comet-tech-gate` chặn rời pha Design nếu thiếu specs, còn `skip_specs`, hoặc file spec không có Scenario. Specs ở repo là bản lọc từ store nên có nguy cơ lệch khi store đổi: dựa vào "Store commit" ở `proposal.md` để phát hiện.
- **Gói bàn giao thành file** (học từ `.comet/batches/*.json` của `product-ups`): `/bolt` ghi `handoff.md` vào change Bolt ở store (mẫu `engine/tech/templates/handoff.md`) thay vì chỉ in ra terminal. Phiên `/comet` ở mỗi repo đọc mục của repo mình trước `/comet-open` (schema `*-comet` có dặn ở artifact `proposal`), nên ba repo dùng chung Store commit, đường dẫn cần đọc và "Quyết định chung". File ghi `store_dirty` khi cây làm việc của store có sửa chưa commit, và `/bolt` cập nhật cột Trạng thái khi repo xong. `openspec validate` và `tech-tools check` bỏ qua file này (đã thử).
- **Báo cáo verify theo mẫu** (học từ cách `product-ups` verify): mỗi schema `*-comet` có `templates/verify-report.md` và nhóm task kết thúc có một task báo cáo verify. Mẫu buộc: bảng đối chiếu từng Scenario của specs, cột baseline cho mỗi kiểm tra (chạy trên worktree tạm của nhánh nền để tách lỗi có sẵn khỏi lỗi do change), chứng minh hồi quy khi sửa lỗi (test thất bại trước khi sửa, hoàn tác thử thì thất bại lại), review độc lập có phân mức.
- **Chọn lệnh theo loại việc**: Bolt tính năng đi luồng đầy đủ (`/bolt` rồi `/comet-open`); sửa lỗi cục bộ dùng `/comet-hotfix`; chỉnh nhẹ dùng `/comet-tweak`. Ở `product-ups` (180 change đã đo) khoảng 56% là hotfix, 34% full, 10% tweak, nên đừng ép mọi việc qua Design.
- Pha Design của Comet chỉ nhận thiết kế Tech: `design.md` của change là con trỏ, không brainstorm lại (`rules.design` trong `openspec/config.yaml` của repo).
- Change đã tạo từ trước bằng luồng `opsx` giữ luồng đó cho tới khi xong, trừ khi owner chủ động chuyển sang Comet.

## ui-map

Wrapper và token của design system: `UpBase*` (lms-fe) và `@ops/ui` (ops-fe); token Tailwind ở lms-fe, SCSS ở ops-fe.
Mỗi section UI Map là một repo FE; reuse `.claude/inventory/*` của repo đó trước khi tạo component mới.
