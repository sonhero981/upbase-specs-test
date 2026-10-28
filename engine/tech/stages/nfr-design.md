---
description: Stage 3.3 NFR Design (AWS AI-DLC, mỗi Unit, conditional). Thiết kế đáp ứng NFR và logical components. Chạy khi 3.2 đã chạy. Gọi qua /tech
argument-hint: <intent-slug> <unit-name>
---
# 3.3 NFR Design (AWS AI-DLC)

| | |
|---|---|
| Nguồn chuẩn | `engine/tech/aidlc/stages/construction/nfr-design.md` · `engine/tech/aidlc/knowledge/aidlc-architect-agent/nfr-design-guide.md`, `nfr-design-patterns.md` |
| Record | `intents/<slug>/construction/<unit-name>/nfr-design/` (6 file + `traceability.json` theo nguồn chuẩn) |
| Người làm / Gate | Tech lead tác giả · FE lead + BE lead · reviewer `tech-reviewer` |
| Điều kiện | 3.2 đã chạy cho Unit này; 3.2 `[S]` thì `[S]` |

Chạy theo `engine/tech/protocol/tech-protocol.md`; làm đúng Steps của nguồn chuẩn. Pattern có sẵn trong repo (cache Redis, RLS, queue Kafka, cron) ghi kèm `file:line`.
