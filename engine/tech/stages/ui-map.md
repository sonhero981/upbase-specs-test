---
description: Stage 3.41 UI Map (plugin tech-workflow, mỗi Unit có UI). Map màn của Unit sang Figma, component reuse, token, asset theo /ui-gate của repo FE. Gọi qua /tech
argument-hint: <intent-slug> <unit-name>
---
# 3.41 UI Map (plugin `tech-workflow`)

| | |
|---|---|
| Record | `intents/<slug>/construction/<unit-name>/ui-map/ui-map.md` |
| Template | `engine/tech/templates/ui-map.md` |
| Consumes | `construction/<unit-name>/functional-design/frontend-components.md`, `design/` + Figma, `.claude/inventory/*` và `.claude/commands/ui-gate.md` của repo FE |
| Người làm / Gate | Tech lead tác giả · FE lead |
| Điều kiện | Unit có màn ở một repo `kind: frontend` trong `workspace.yaml`. Không có UI → `[S]` |

Chạy theo `engine/tech/protocol/tech-protocol.md`.

## Vì sao có stage này
AWS `frontend-components.md` (3.1) technology-agnostic. `/ui-gate` của repo FE cần bảng UI-1 → UI-9 gắn Figma node, wrapper
wrapper và token của design system sản phẩm (xem `domain/tech-adjustments.md` mục `ui-map`), asset — chi tiết kỹ thuật nên tách thành plugin stage, là input bắt buộc của `/ui-gate build`.

## Generate
- Một section mỗi repo FE mà Unit chạm (`## <repo id>` theo `workspace.yaml`), mỗi section đủ UI-1 → UI-9 theo `ui-gate.md` của repo đó.
- Trạng thái **Provisional** khi chưa có Figma node (`/ui-gate review` bỏ so pixel) → **Final** khi đủ node.
- Component reuse ghi path thật trong inventory; component mới ghi lý do wrapper có sẵn không đủ.
