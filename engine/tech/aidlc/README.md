# AWS AI-DLC (bản chép nguyên văn)

Nguồn: `https://github.com/awslabs/aidlc-workflows`, commit `f646384` (11/10/2026), giấy phép MIT-0 (`LICENSE`).
**Không sửa file trong thư mục này.** Điều chỉnh cho khung này nằm ở command `engine/tech/stages/*.md` và `engine/tech/protocol/tech-protocol.md`.

| Thư mục | Nội dung |
|---|---|
| `stages/inception/` | 2.1 reverse-engineering · 2.6 domain-design · 2.7 units-generation · 2.8 contract-design · 2.9 delivery-planning |
| `stages/construction/` | 3.1 functional-design · 3.2 nfr-requirements · 3.3 nfr-design · 3.4 infrastructure-design · 3.5 code-generation · 3.6 build-and-test |
| `knowledge/` | Kiến thức vai: architect, architecture-reviewer, developer, delivery, quality |
| `agents/` | Định nghĩa agent gốc (tham khảo, không được Claude Code nạp) |

## Quy đổi engine → khung này

Stage file của AWS viết cho engine `aidlc`. Khung này không cài engine; đọc theo bảng dưới.

| AWS | Khung này |
|---|---|
| `<record>` | `intents/<slug>/` |
| `aidlc/spaces/<space>/codekb/<repo>/` | `domain/codekb/<repo>/` |
| `{{INVOKE}} engine orchestrate report …`, `directive`, `state-init` | Cập nhật `tech-state.md` của intent theo `tech-protocol.md` |
| Approval gate | Gate theo `engine/protocol/gate-protocol.md`, người duyệt theo `tech-protocol.md` |
| `reviewer: aidlc-architecture-reviewer-agent` | Agent `tech-reviewer` (persona + checklist lấy từ `agents/aidlc-architecture-reviewer-agent.md` + `knowledge/aidlc-architecture-reviewer-agent/`) |
| Sensor `required-sections`, `upstream-coverage`, `traceability` | `python engine/tech/scripts/tech-tools.py check` + tự kiểm theo mục Steps của stage |
| Sensor `linter`, `type-check` | Bỏ ở stage thiết kế; ở code chạy lint/typecheck của từng repo |
| `{{HARNESS_DIR}}/knowledge/...` | `engine/tech/aidlc/knowledge/...` (product: `engine/knowledge/`) |
| Bolt (2.9) → Construction per Unit | Cuốn chiếu theo Bolt; code ở repo dev qua OpenSpec (change Bolt ở `openspec/`, change `run` ở repo) |
| `aidlc-developer-agent` sinh code | Dev code (owner Bolt) chạy `/opsx:apply` ở repo dev |
| Scope `feature` / `mvp` / `bugfix`… | Profile S/M/L của intent PO; stage conditional theo điều kiện trong frontmatter |

Cập nhật bản chép: clone repo AWS, chép đè đúng các file trên, sửa commit ở đầu file này, đọc `CHANGELOG.md` của AWS xem stage nào đổi rồi rà command tương ứng.
