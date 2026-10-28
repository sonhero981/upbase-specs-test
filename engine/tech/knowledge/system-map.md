# System Map — ai ghi ở đâu

Phần dùng chung, không phụ thuộc sản phẩm. Danh sách repo, owner, convention và gate của sản phẩm đang cài nằm ở
[`workspace.yaml`](../../../workspace.yaml); chi tiết riêng của sản phẩm (phụ thuộc giữa repo, package dùng chung,
câu hỏi treo) nằm ở `domain/system-map.md`.

Repo khung là **nguồn tài liệu duy nhất**: intent của PO, artifact Tech theo stage AWS AI-DLC
(`inception/<stage>/`, `construction/<unit>/` trong intent) và store OpenSpec (`openspec/`, mỗi change là một Bolt).
Code nằm ở các repo khai trong `workspace.yaml`; mỗi repo chỉ giữ change cùng tên Bolt (schema `run`).
Luồng: [`workflow.md`](workflow.md).

## Vùng và quyền ghi

| Phần | Path | Owner | Quyền của Tech |
|---|---|---|---|
| Intent của PO (requirement, PRD, Decision Brief) | `intents/<slug>/` | PO | Chỉ đọc theo `origin/main` — xem `intent-handoff.md` |
| Tech Design 1 | `intents/<slug>/inception/tech-design/tech-design.md` | Tech PIC | Ghi ở stage 2.43 của PO, trước khi phần Tech khởi động |
| Artifact Tech + QA | `intents/<slug>/tech-state.md`, dòng `DEC-T<n>` trong `decisions.md`, `inception/{domain-design,units-generation,contract-design,test-cases,delivery-planning}/`, `construction/` | FE lead + BE lead · QA lead (`test-cases/`) | Ghi qua PR |
| Chuẩn AWS AI-DLC (chép nguyên văn) | `engine/tech/aidlc/` | — | Không sửa; cập nhật theo `engine/tech/aidlc/README.md` |
| Knowledge domain | `domain/` | PO | Đọc; sai thì báo PO |
| Store OpenSpec | `openspec/` | Tech | Ghi qua PR |
| Knowledge tech | `engine/tech/knowledge/` | Tech | Ghi qua PR |
| Khai báo repo và người | `workspace.yaml` | Người giữ khung | Sửa rồi chạy `python scripts/setup.py` |

## Phụ thuộc giữa các tầng

```
intent PO ──PRD + Tech Design 1──> inception/<stage> (Tech, QA)
          ──bolt-plan──> construction/<unit>
          ──3.5 plan──> openspec/changes (Bolt)
          ──change cùng tên, schema run──> từng repo trong workspace.yaml
```

Thứ tự implement một change chạm nhiều repo: theo `build_order` trong `workspace.yaml`.
Phụ thuộc cụ thể giữa các repo của sản phẩm đang cài: `domain/system-map.md`.
