---
description: Stage 3.5 Code Generation (AWS AI-DLC, mỗi Bolt). Part 1 - plan theo Unit + mở Bolt (change ở store, change run ở repo dev). Part 2 - owner Bolt code bằng /opsx:apply ở từng repo. Gọi qua /tech
argument-hint: <intent-slug> <Bnn>
---
# 3.5 Code Generation (AWS AI-DLC)

| | |
|---|---|
| Nguồn chuẩn | `engine/tech/aidlc/stages/construction/code-generation.md` · `engine/tech/aidlc/knowledge/aidlc-developer-agent/` |
| Record | `intents/<slug>/construction/<unit-name>/code-generation/`: `code-generation-plan.md`, `code-generation-questions.md`, `unit-test-instructions.md`, `code-summary.md`, `traceability.json` · change Bolt `openspec/changes/<slug>-<bnn>-<tên>/` · change `run` cùng tên ở mỗi repo dev |
| Consumes | Mọi artifact 3.1–3.41 của các Unit trong Bolt, `contract-summary.md` (Agreed), `inception/test-cases/`, codekb, rule từng repo |
| Người làm / Gate | Part 1: tech lead tác giả, gate FE lead + BE lead (Plan approval của AWS). Part 2: owner Bolt, gate = review PR từng repo |
| Reviewer | `tech-reviewer` cho `code-generation-plan.md` |
| Requires | Unit của Bolt đã qua 3.1 (và 3.2–3.41 nếu chạy); contract Agreed; Bolt phụ thuộc đã merge |

Chạy theo `engine/tech/protocol/tech-protocol.md`; Part 1 / Part 2 đúng nguồn chuẩn, quy đổi engine theo `engine/tech/aidlc/README.md`.

## Part 1 — Planning (ở store)
1. `code-generation-plan.md` mỗi Unit, **một section mỗi repo** theo `build_order` trong `workspace.yaml`.
   Mỗi section: checklist theo các lớp của nguồn chuẩn (business logic, API, data access, migration, test, config)
   và **file tạo / sửa** theo convention của repo đó (cột `conventions` trong `workspace.yaml`), file "sửa" kèm `file:line`.
   Quy ước riêng từng repo và test strategy: `domain/tech-adjustments.md` mục `code-generation`.
2. Review `tech-reviewer` → gate Plan approval (FE lead + BE lead).
3. Mở Bolt ở store: `openspec new change <slug>-<bnn>-<tên> --schema bolt`; `proposal.md` trỏ tới `construction/<unit>/…` và contract, không chép; `specs/` = Scenario của Bolt (từ `rules.md`, `functional-spec.md`); `tasks.md` task thô theo repo. `openspec validate --strict` + `grep -rn "NEEDS CLARIFICATION"` rỗng. PR vào `main`.
4. **Sau khi PR store merge `main`**, mỗi repo dev: `openspec new change <cùng tên> --schema run`; `context.md` trỏ `code-generation-plan.md` section repo đó + contract + TC; `tasks.md` = checklist section repo đó của plan (đây là bản thực thi, plan ở store là bản gốc).

## Part 2 — Generation (ở repo dev, owner Bolt)
Theo thứ tự package → be → fe, mỗi repo: `/jira-tasks` → `/opsx:apply` (gate repo: `/ui-gate`, curl, typecheck) → `/opsx:verify` → PR. Lệch plan: dừng, sửa plan ở store (lead duyệt), ghi `progress.md`.
Xong mọi repo: ghi `code-summary.md` (PR từng repo, file đã đổi, lệch plan) ở store, cập nhật `unit-test-instructions.md` nếu lệch; tick task thô ở change Bolt.

## Verify
`python engine/tech/scripts/tech-tools.py check intents/<slug> --stage=code-generation --bolt=<Bnn>` (mỗi Unit của Bolt có plan, change Bolt tồn tại). Sang 3.6.
