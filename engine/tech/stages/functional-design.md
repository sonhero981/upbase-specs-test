---
description: Stage 3.1 Functional Design (AWS AI-DLC, mỗi Unit). Entity, business rule, functional spec, frontend components — technology-agnostic. Chạy cho các Unit của Bolt sắp làm. Gọi qua /tech
argument-hint: <intent-slug> <unit-name | Bnn>
---
# 3.1 Functional Design (AWS AI-DLC)

| | |
|---|---|
| Nguồn chuẩn | `engine/tech/aidlc/stages/construction/functional-design.md` · corner checklist `domain/corner-checklist.md` (domain pack, manifest `domain/domain.md`) |
| Record | `intents/<slug>/construction/<unit-name>/functional-design/`: `entities.md`, `rules.md`, `functional-spec.md`, `frontend-components.md` (Unit có UI), `functional-design-questions.md`, `traceability.json` |
| Consumes | `inception/units-generation/` (Unit + story map), `inception/contract-design/contract-summary.md`, `inception/domain-design/components.md`, PRD (AC, BR), `requirements.md` |
| Phạm vi | Các Unit của Bolt kế tiếp trong `bolt-plan.md` (cuốn chiếu). Truyền `Bnn` để chạy hết Unit của Bolt |
| Người làm / Gate | Tech lead tác giả · FE lead + BE lead |
| Reviewer | `tech-reviewer` |
| Điều kiện | Có data model, business logic hoặc rule mới. Chỉ sửa logic đơn giản → `[S]` |

Chạy theo `engine/tech/protocol/tech-protocol.md`; làm đúng Steps và định dạng của file nguồn chuẩn.

## Điều chỉnh của sản phẩm

Điều chỉnh riêng của sản phẩm đang cài cho stage này: `domain/tech-adjustments.md` mục `functional-design`.

## Verify
`python engine/tech/scripts/tech-tools.py check intents/<slug> --stage=functional-design --unit=<unit-name>` (mọi AC của Unit có BR, không BR mồ côi) → review → gate.
Sau đó: 3.2/3.3/3.4 nếu điều kiện đúng, 3.41 nếu Unit có UI, rồi 3.5.
