---
description: Stage 2.9 Delivery Planning (AWS AI-DLC). Bolt plan, phân người, lý do thứ tự, phụ thuộc ngoài. Mang đi họp. Always. Gọi qua /tech
argument-hint: <intent-slug>
---
# 2.9 Delivery Planning (AWS AI-DLC)

| | |
|---|---|
| Nguồn chuẩn | `engine/tech/aidlc/stages/inception/delivery-planning.md` · `engine/tech/aidlc/knowledge/aidlc-delivery-agent/` |
| Record | `intents/<slug>/inception/delivery-planning/`: `bolt-plan.md`, `team-allocation.md`, `risk-and-sequencing-rationale.md`, `external-dependency-map.md`, `delivery-planning-questions.md` |
| Consumes | `inception/units-generation/` (DAG, ngày công), `inception/contract-design/`, `inception/test-cases/` (nếu đã có), `tech-state.md` (dev code, phạm vi đợt) |
| Người làm / Gate | Tech lead tác giả · họp: FE lead, BE lead, PO, QA, owner các Bolt |

Chạy theo `engine/tech/protocol/tech-protocol.md`; làm đúng Steps và định dạng của file nguồn chuẩn.

## Điều chỉnh của sản phẩm

Điều chỉnh riêng của sản phẩm đang cài cho stage này: `domain/tech-adjustments.md` mục `delivery-planning`.

## Verify
`python engine/tech/scripts/tech-tools.py check intents/<slug>` (mặc định = đầy đủ: US → Unit → Bolt → TC) phải Đạt. Sau gate họp: version số nguyên kế tiếp, archive, `[x]`; điền bảng Bolts ở `tech-state.md`. Bolt đầu tiên vào Construction (3.1).
