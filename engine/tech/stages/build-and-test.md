---
description: Stage 3.6 Build and Test (AWS AI-DLC, mỗi Bolt). Build, integration/curl, TC của Bolt, kết quả, cross-unit traceability; contract lên Final; archive Bolt. Gọi qua /tech
argument-hint: <intent-slug> <Bnn>
---
# 3.6 Build and Test (AWS AI-DLC)

| | |
|---|---|
| Nguồn chuẩn | `engine/tech/aidlc/stages/construction/build-and-test.md` · `engine/tech/aidlc/knowledge/aidlc-quality-agent/` |
| Record | `intents/<slug>/construction/build-and-test/<bnn>/`: `build-instructions.md`, `integration-test-instructions.md`, `performance-test-instructions.md` (nếu có NFR), `security-test-instructions.md` (nếu có NFR), `build-and-test-summary.md`, `test-results.md`, `cross-unit-traceability.md` |
| Consumes | `code-summary.md` của các Unit, `contract-summary.md` (`x-curl`), `inception/test-cases/` (TC của Bolt), `progress.md` ở repo dev |
| Người làm / Gate | Owner Bolt + QA · QA lead, sau đó demo theo DoD |

Chạy theo `engine/tech/protocol/tech-protocol.md`; làm đúng Steps của nguồn chuẩn.

## Điều chỉnh của sản phẩm

Điều chỉnh riêng của sản phẩm đang cài cho stage này: `domain/tech-adjustments.md` mục `build-and-test`.

## Gate và đóng Bolt
QA lead duyệt + demo đạt DoD → `/opsx:archive` ở từng repo dev và change Bolt ở store, bảng Bolts trong `tech-state.md` sang "Xong". Bolt kế tiếp vào 3.1.
