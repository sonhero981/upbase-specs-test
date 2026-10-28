---
description: Stage 2.8 Contract Design (AWS AI-DLC). Mọi contract giữa Unit và API public dạng OpenAPI / AsyncAPI trong contract-summary.md. Conditional. Gọi qua /tech
argument-hint: <intent-slug>
---
# 2.8 Contract Design (AWS AI-DLC)

| | |
|---|---|
| Nguồn chuẩn | `engine/tech/aidlc/stages/inception/contract-design.md` |
| Record | `intents/<slug>/inception/contract-design/contract-summary.md` (+ `contract-design-questions.md`) |
| Consumes | `inception/units-generation/` (DAG: mỗi cạnh là một contract ứng viên), `inception/domain-design/components.md`, `requirements.md` |
| Người làm / Gate | Tech lead tác giả · **BE lead ký "Approved by"** + FE lead |
| Reviewer | `tech-reviewer` |

Chạy theo `engine/tech/protocol/tech-protocol.md`; làm đúng Steps và định dạng của file nguồn chuẩn.

## Điều chỉnh của sản phẩm

Điều chỉnh riêng của sản phẩm đang cài cho stage này: `domain/tech-adjustments.md` mục `contract-design`.

## Verify
`python engine/tech/scripts/tech-tools.py check intents/<slug> --stage=contract-design` (mỗi cạnh DAG có contract hoặc ghi lý do không cần; YAML parse được) → review → gate.
