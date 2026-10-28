---
intent: 260923-gamification
artifact: unit-of-work-dependency
stage: 2.7 units-generation
version: 1.0
status: approved
approved_at: 2026-10-13 ([GIẢ LẬP] BE lead, DEC-T7)
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
---
# Unit of Work Dependency: Gamification, lát Nền tảng

Một Unit, không có cạnh giữa Unit. Contract của lát là REST giữa ops-fe và lms-be bên trong U0 (2.8).

```yaml
units:
  - name: u0-foundation
    kind: service
    depends_on: []
```

## Dependency DAG

```mermaid
flowchart LR
  U0["U0 u0-foundation · US14, US15"]
```

| Unit | Phụ thuộc | Vì sao |
|---|---|---|
| U0 | — | Chỉ dựa vào code có sẵn trên `staging` (Casbin, Redis, tenant) |

Unit của các lát sau (Điểm, Hiển thị cho học viên…) sẽ phụ thuộc U0; thêm vào DAG khi tech-state mở rộng phạm vi.
