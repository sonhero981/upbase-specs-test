# New Project – Khởi tạo project mới

Tạo cấu trúc thư mục và file nền cho một project mới.

---

## Đầu vào

Tên project: `$ARGUMENTS`

**Người dùng tự đặt tên.** Không ép format, không hỏi năm/BU/viết tắt. Nhận tên sao dùng vậy — chỉ chuẩn hoá thành dạng an toàn cho tên thư mục (bỏ dấu, thay khoảng trắng bằng gạch nối).

Không có tên → hỏi một câu: *"Đặt tên project là gì?"*

Tên trùng với project đã có → báo và hỏi: dùng tiếp project cũ, hay đặt tên khác.

---

## Cách làm

### 1. Tạo thư mục

```
.claude/projects/<tên-project>/
├── project-context.md
├── project-decisions.md
├── working/
│   ├── raw-inputs/
│   ├── ai-drafts/
│   ├── open-questions/
│   ├── meeting-notes/
│   ├── impact-analysis/
│   └── solution-options/
└── docs/
    ├── brd/
    ├── prd/
    └── user-guide/
```

> `working/` chứa **bản phân tích nội bộ** — Impact Matrix, Solution Comparison, bản nháp.
> `docs/` chứa **artifact chính thức** — BRD (bản chốt hướng) và PRD (tài liệu bàn giao).

### 2. Tạo `project-context.md`

```markdown
# Project Context

## Background

<!-- Bối cảnh: vì sao có yêu cầu này, đang xảy ra chuyện gì -->

## Objectives

<!-- Mục tiêu cần đạt -->

## Scope

<!-- Phạm vi sơ bộ, có thể chưa chắc -->

## Stakeholders

| Vai trò | Người | Ghi chú |
| --- | --- | --- |

## Phạm vi sản phẩm

<!-- Portal nào bị chạm: UpLMS (người học) / UpLMS Ops (vận hành) / cả hai -->

## Key References

<!-- Link Figma, tài liệu nền, PRD liên quan, KB cần đọc -->

## Lark

- **Wiki space:** <!-- space chứa tài liệu của project này -->
- **Parent node:** <!-- node cha để đặt PRD -->

### Đã publish

| Artifact | Node token | URL | Lần publish gần nhất |
| --- | --- | --- | --- |

## Jira

- **Epic:** <!-- link -->
- **Story:** <!-- link -->
```

### 3. Tạo `project-decisions.md`

```markdown
# Project Decisions

Nơi ghi mọi quyết định đã chốt. AI tra file này để **không hỏi lại câu đã có đáp án**.

| Ngày | Quyết định | Lý do | Người quyết | Gate |
| --- | --- | --- | --- | --- |
```

### 4. Tạo `.gitkeep` trong các thư mục rỗng

Để thư mục tồn tại khi commit.

---

## Sau khi tạo

Tự kiểm theo `.claude/checklist/new-project.md`.

Báo người dùng:

1. Cấu trúc đã tạo tại `.claude/projects/<tên-project>/`
2. **Việc cần làm tiếp:**
   - Điền `project-context.md` — càng đầy đủ thì AI càng ít phải hỏi lại
   - Đặt tài liệu đầu vào (email, meeting note, mô tả yêu cầu) vào `working/raw-inputs/`
3. **Bắt đầu:** `/po-workflow <tên-project>` — hoặc vào thẳng một bước cụ thể: `/clarify-requirements`, `/generate-brd`…

> Nhắc: `project-decisions.md` là bộ nhớ của dự án. Đừng xoá trong quá trình làm việc.
