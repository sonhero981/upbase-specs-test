# Tech Protocol (AWS AI-DLC + plugin `tech-workflow`)

Phần Tech của intent chạy **đúng stage và artifact của AWS AI-DLC** (bản chép nguyên văn ở `engine/tech/aidlc/`, đọc
`engine/tech/aidlc/README.md` để quy đổi engine). Plugin `tech-workflow` chỉ thêm stage AWS không có (số thập phân, như plugin
`po-workflow` của PO). Nghi thức chung dùng `stage-protocol.md`, `gate-protocol.md`, `question-format.md` của repo; file này ghi chỗ khác.

## Stage

| Mã | Slug | Nguồn | Artifact (trong `intents/<slug>/`) | Người làm | Gate |
|---|---|---|---|---|---|
| 2.1 | reverse-engineering | AWS | `domain/codekb/<repo>/` (9 file AWS) | Tech lead tác giả | — (conditional) |
| 2.6 | domain-design | AWS | `inception/domain-design/components.md`, `decisions.md` | Tech lead tác giả | FE + BE lead |
| 2.7 | units-generation | AWS | `inception/units-generation/unit-of-work.md`, `unit-of-work-dependency.md`, `unit-of-work-story-map.md` | Tech lead tác giả | FE + BE lead |
| 2.8 | contract-design | AWS | `inception/contract-design/contract-summary.md` (OpenAPI / AsyncAPI) | Tech lead tác giả | BE lead ký "Approved by" |
| 2.81 | test-cases | plugin | `inception/test-cases/test-cases.md` | QA | QA lead |
| 2.9 | delivery-planning | AWS | `inception/delivery-planning/bolt-plan.md`, `team-allocation.md`, `risk-and-sequencing-rationale.md`, `external-dependency-map.md` | Tech lead tác giả | Họp: FE, BE, PO, QA, owner Bolt |
| 3.1 | functional-design | AWS, mỗi Unit | `construction/<unit>/functional-design/entities.md`, `rules.md`, `functional-spec.md`, `frontend-components.md` | Tech lead tác giả | FE + BE lead |
| 3.2 | nfr-requirements | AWS, mỗi Unit, conditional | `construction/<unit>/nfr-requirements/` | Tech lead tác giả | FE + BE lead |
| 3.3 | nfr-design | AWS, mỗi Unit, conditional | `construction/<unit>/nfr-design/` | Tech lead tác giả | FE + BE lead |
| 3.4 | infrastructure-design | AWS, mỗi Unit, conditional | `construction/<unit>/infrastructure-design/` | BE lead | BE lead |
| 3.41 | ui-map | plugin, Unit có UI | `construction/<unit>/ui-map/ui-map.md` | Tech lead tác giả | FE lead |
| 3.5 | code-generation | AWS, mỗi Bolt | Plan: `construction/<unit>/code-generation/code-generation-plan.md` + change Bolt ở `openspec/` + change `run` ở repo dev. Code: repo dev | Plan: tech lead · Code: owner Bolt | Plan: FE + BE lead · Code: review PR |
| 3.6 | build-and-test | AWS, mỗi Bolt | `construction/build-and-test/<bnn>/` | Owner Bolt + QA | QA lead |

**Thứ tự.** Inception chạy một lần: 2.1 → 2.6 → 2.7 → 2.8 → (2.81 ∥ 2.9). Điều kiện vào: PO đã duyệt gate 2.43 Design Alignment, nghĩa là `tech-design.md` của Tech PIC và Decision Brief đã ký. Construction **cuốn chiếu theo Bolt**
trong `bolt-plan.md`: với mỗi Bolt, chạy 3.1 → 3.2/3.3/3.4 (nếu điều kiện) → 3.41 cho các Unit của Bolt, rồi 3.5 → 3.6.
Bolt bắt đầu thiết kế khi **mọi Bolt nó phụ thuộc** (cột Phụ thuộc trong `bolt-plan.md`) đã qua gate 3.5 plan (không cần chờ code xong). Bolt không phụ thuộc nhau thiết kế và code **song song** (mỗi owner / lead một Bolt); Construction vẫn đi cuốn chiếu trong chuỗi phụ thuộc.

**Đọc trước mỗi stage AWS:** `engine/tech/aidlc/stages/<phase>/<slug>.md` (frontmatter: điều kiện, consumes, produces; mục
Steps; mục Sensors). Làm đúng Steps và định dạng artifact ở đó, với các điều chỉnh dưới đây.

## Vai trò

- **Tech lead tác giả**: FE lead hoặc BE lead nhận intent, viết Inception và thiết kế Construction. Ghi tên ở `tech-state.md`.
- **Lead còn lại**: soi chéo khi duyệt; BE lead luôn ký contract.
- **Owner Bolt**: dev code Bolt, có thể không tham gia viết tài liệu. Artifact phải tự đủ cho người không viết nó.

Owner, tên lead: `engine/tech/knowledge/system-map.md`.

## Điều chỉnh của sản phẩm cho stage AWS

| Mục | Điều chỉnh |
|---|---|
| Ngôn ngữ | Viết tiếng Việt, giữ thuật ngữ và tên artifact/heading tiếng Anh của AWS |
| Multi-repo | Một intent chạm nhiều repo trong `workspace.yaml`. Unit có thể xuyên repo; `unit-of-work.md` ghi repo chạm. Contract inter-unit gồm cả giao tiếp giữa repo backend và các app FE |
| Unit kind | Dùng đúng `service` / `spec` / `ui` / `packaging` / `library`; thêm cột repo |
| Walking skeleton | Bật mặc định khi intent chạm từ 2 repo trở lên: Unit đầu DAG (`u0-walking-skeleton`) là lát mỏng nhất qua mọi điểm tích hợp thật. U0 được phép **không mang US** (luật "mỗi US đúng một Unit" áp cho US, không bắt mọi Unit có US); component U0 dựng được Unit sau làm tiếp, ghi ở `unit-of-work.md` |
| Technology-agnostic | 3.1 không code, không SQL, không framework (đúng AWS). Chi tiết kỹ thuật (file, framework, component, migration SQL) nằm ở 3.5 `code-generation-plan.md` |
| Rule repo | Theo cột `conventions` của repo trong `workspace.yaml`; mục nào của convention áp cho stage nào ghi ở `domain/tech-adjustments.md` |
| Mọi câu "có sẵn / sửa / dùng lại" | Kèm `file:line` đã kiểm ở `origin/staging` |
| Mã | Theo AWS: `U{n}` + tên thư mục `u{n}-<mô-tả>`, `BRx.y`, `ADR-NNN`. Bolt `B01`. TC `TC-n`. Review `R-01` |
| AC | PRD chưa có mã AC: dùng `USn-ACk` (dòng thứ k các bảng AC của USn) thay cho `AC{x.y.z}` trong `traceability.json`. AC nằm ngoài lát đợt này: status `excluded` kèm lý do (ngoài OK/GAP của AWS). U0 không mang US: upstream id là ràng buộc tích hợp của skeleton (`U0-IC<n>`), release (`U0-REL`), contract (`U0-CR<n>`) |
| Reviewer | `reviewer: aidlc-architecture-reviewer-agent` → agent `tech-reviewer`. Không gọi được (phiên không mở ở gốc store): subagent general-purpose, prompt = nội dung `engine/tech/agents/tech-reviewer.md` + đường dẫn. Chạy foreground |
| Review và gate | Viết → review → sửa → re-review (tối đa theo `reviewer_max_iterations`, quá thì lead quyết) → READY mới mở gate. Không điền sign-off / "Approved by" trước đó |
| Sensor | `python engine/tech/scripts/tech-tools.py check intents/<slug> --stage=<slug>` (heading bắt buộc, DAG không vòng, coverage). Không thay cho Steps |
| State | `tech-state.md` ở gốc intent (template `engine/tech/templates/state.md`). Không sửa `state.md` của PO |
| Quyết định | Một sổ duy nhất cho cả intent: `decisions.md` ở gốc intent, mã `DEC-T<n>` cho quyết định của Tech, cột *Read when* ghi stage Tech. Không mở sổ riêng |
| Load | `git fetch` + rebase lên `origin/main` trước khi đọc artifact PO; chỉ dùng stage PO `[x]` |
| Learn | Như PO; bài học giữ lại ghi `memory/team.md` mục `## Tech` |
| Archive | `python engine/scripts/po-tools.py archive intents/<slug> <stage-slug> <đường dẫn artifact>` |
| Phạm vi đợt | Dòng "Phạm vi đợt này" trong `tech-state.md`. **Mặc định cả intent** để 2.9 chia đủ Bolt cho team. Lát nhỏ chỉ khi chạy thử / PO tách đợt release (DEC-T ghi lý do); phụ thuộc ra ngoài lát ghi ở mục 8 của `tech-design.md`. Mở rộng phạm vi sau: sửa dòng này → router mở lại `[R]` 2.6, 2.7, 2.8, 2.81, 2.9; Bolt đã qua 3.5 giữ nguyên |
| Chạy song song | Hai stage song song không ghi chung file; `tech-state.md` và `decisions.md` do người điều phối ghi |
| Agent con | Chia việc đọc cho agent con thì gọi foreground, chờ đủ kết quả rồi mới viết |

## Intent chuyển từ luồng v1

Thiếu `stories.md`, `tech-design.md`, hoặc họ mã cũ: lấy US, Proto-Unit từ PRD (`## USn:`, `# Unit — nhóm bàn giao`), mapping mã
theo `intent.md`; mã Unit cũ của PRD (`U1`…) đổi thành `PU1`… khi trích. NFR lấy từ Constraints, PRD, impact matrix. Không có `tech-design.md`:
tech lead ghi hướng kỹ thuật ở `inception/domain-design/decisions.md`. Mỗi artifact ghi nguồn thay thế đã dùng.

## Ranh giới và thay đổi

| Tình huống | Đường đi |
|---|---|
| Tech ghi ở đâu | `tech-state.md`, dòng `DEC-T<n>` trong `decisions.md`, `inception/{domain-design,units-generation,contract-design,test-cases,delivery-planning}/`, `construction/`, `archive/`; `engine/tech/knowledge/`; `openspec/`. Ngoài ra chỉ `inception/tech-design/tech-design.md` của Tech PIC |
| PRD sai, thấy trước khi thiết kế | Mục 0 và mục 7 của `tech-design.md`, chốt ở buổi họp 2.43; PO đi `/change-request` |
| PRD sai, thấy giữa stage Tech | Chặn → dừng stage, báo PO `/change-request`; không chặn → "Ghi chú cho PO" ở `tech-state.md` |
| PRD đổi qua CR | Mở lại stage Tech bị ảnh hưởng `[R]`; Bolt đang làm → `/opsx:update` |
| Code thấy thiết kế / contract sai | Dừng, sửa artifact ở store qua PR, lead ký lại; repo dev ghi `progress.md` |
| Đổi Bolt | Sửa `bolt-plan.md` (+ 3 file 2.9), FE lead duyệt, cập nhật change Bolt |
