---
description: Stage 2.1 Reverse Engineering (AWS AI-DLC). Quét code từng repo chạm tới, ghi codekb 9 file theo chuẩn AWS, dùng lại cho mọi intent. Conditional. Gọi qua /tech
argument-hint: <intent-slug> [repo]
---
# 2.1 Reverse Engineering (AWS AI-DLC)

| | |
|---|---|
| Nguồn chuẩn | `engine/tech/aidlc/stages/inception/reverse-engineering.md` · template artifact `engine/tech/aidlc/knowledge/aidlc-developer-agent/re-artifacts.md` · cách quét `code-analysis-guide.md` cùng thư mục |
| Record | `domain/codekb/<repo>/` — 9 file: `business-overview`, `architecture`, `code-structure`, `api-documentation`, `component-inventory`, `technology-stack`, `dependencies`, `code-quality-assessment`, `reverse-engineering-timestamp` |
| Đào sâu (tuỳ chọn) | `domain/codekb/<repo>/areas/<area>.md` — vùng nghiệp vụ cụ thể của intent |
| Người làm | Tech lead tác giả. Không gate (báo một dòng) |
| Điều kiện | Repo chạm tới chưa có codekb, hoặc codekb STALE |

Chạy theo `engine/tech/protocol/tech-protocol.md`; làm đúng Steps của file nguồn chuẩn, quy đổi engine theo `engine/tech/aidlc/README.md`.

## Điều chỉnh của sản phẩm

Điều chỉnh riêng của sản phẩm đang cài cho stage này: `domain/tech-adjustments.md` mục `reverse-engineering`.

## Verify
`python engine/tech/scripts/tech-tools.py check intents/<slug> --stage=reverse-engineering` (đủ 9 file mỗi repo, có `## Scope of Analysis`).
Cập nhật bảng ở `domain/codekb/README.md`. Không commit lẻ; đi cùng PR của nhánh Tech.
