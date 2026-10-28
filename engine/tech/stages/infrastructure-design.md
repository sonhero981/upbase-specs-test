---
description: Stage 3.4 Infrastructure Design (AWS AI-DLC, mỗi Unit, conditional). Hạ tầng, monitoring, CI/CD khi Unit cần thay đổi hạ tầng. Gọi qua /tech
argument-hint: <intent-slug> <unit-name>
---
# 3.4 Infrastructure Design (AWS AI-DLC)

| | |
|---|---|
| Nguồn chuẩn | `engine/tech/aidlc/stages/construction/infrastructure-design.md` |
| Record | `intents/<slug>/construction/<unit-name>/infrastructure-design/`: `infrastructure-specification.md`, `monitoring-design.md`, `cicd-pipeline.md`, `traceability.json` |
| Người làm / Gate | BE lead · BE lead · reviewer `tech-reviewer` |
| Điều kiện | Unit cần service hạ tầng mới (queue, cron chạy riêng, bucket, biến môi trường mới), đổi deploy hoặc CI. Không đổi hạ tầng → `[S]` (thường gặp) |

Chạy theo `engine/tech/protocol/tech-protocol.md`; làm đúng Steps của nguồn chuẩn. Hạ tầng hiện tại: Docker + compose trên EC2, GitHub Actions (`deploy-staging.yml`, `deploy-production.yml`); không giả định AWS service khác khi chưa kiểm.
