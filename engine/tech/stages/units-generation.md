---
description: Stage 2.7 Units Generation (AWS AI-DLC). Chia Unit of Work, DAG phụ thuộc (yaml), story map. Always. Gọi qua /tech
argument-hint: <intent-slug>
---
# 2.7 Units Generation (AWS AI-DLC)

| | |
|---|---|
| Nguồn chuẩn | `engine/tech/aidlc/stages/inception/units-generation.md` |
| Record | `intents/<slug>/inception/units-generation/`: `unit-of-work.md`, `unit-of-work-dependency.md`, `unit-of-work-story-map.md`, `units-generation-questions.md`, `traceability.json` |
| Consumes | `inception/domain-design/` (nếu có), PRD (US, Proto-Unit `PU`), `requirements.md` |
| Người làm / Gate | Tech lead tác giả · FE lead + BE lead |
| Reviewer | `tech-reviewer` |

Chạy theo `engine/tech/protocol/tech-protocol.md`; làm đúng Steps và định dạng của file nguồn chuẩn.

## Điều chỉnh của sản phẩm

Điều chỉnh riêng của sản phẩm đang cài cho stage này: `domain/tech-adjustments.md` mục `units-generation`.

## Verify
`python engine/tech/scripts/tech-tools.py check intents/<slug> --stage=units-generation` (DAG không vòng, mọi US đợt này có đúng một Unit) → review → gate.
