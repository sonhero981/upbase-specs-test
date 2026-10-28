---
description: Stage 2.6 Domain Design (AWS AI-DLC). Component catalogue (yaml + mermaid + bảng) và ADR cho intent. Conditional. Gọi qua /tech
argument-hint: <intent-slug>
---
# 2.6 Domain Design (AWS AI-DLC)

| | |
|---|---|
| Nguồn chuẩn | `engine/tech/aidlc/stages/inception/domain-design.md` · ADR template `engine/tech/aidlc/knowledge/aidlc-architect-agent/adr-template.md` · `architecture-guide.md`, `ddd-patterns.md` cùng thư mục |
| Record | `intents/<slug>/inception/domain-design/`: `components.md`, `decisions.md`, `domain-design-questions.md`, `traceability.json` |
| Consumes | PRD + `requirements.md` (PO), `inception/tech-design/tech-design.md` (mục 0 ĐỦ, mục 2 quyết định kỹ thuật sơ lược), codekb các repo chạm tới |
| Người làm / Gate | Tech lead tác giả · FE lead + BE lead |
| Reviewer | `tech-reviewer` (tối đa 2 vòng theo AWS, quá thì lead quyết) |
| Điều kiện | Cần component / building block mới. Chỉ sửa component có sẵn → `[S]` kèm lý do |

Chạy theo `engine/tech/protocol/tech-protocol.md`; làm đúng Steps và định dạng của file nguồn chuẩn.

## Điều chỉnh của sản phẩm

Điều chỉnh riêng của sản phẩm đang cài cho stage này: `domain/tech-adjustments.md` mục `domain-design`.

## Verify
`python engine/tech/scripts/tech-tools.py check intents/<slug> --stage=domain-design` → review → gate. Sau Approve: version số nguyên kế tiếp, archive, `[x]` ở `tech-state.md`.
