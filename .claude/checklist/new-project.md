# Checklist: New Project

## Tên
- [ ] **Người dùng tự đặt tên** — không ép format, không hỏi năm/BU
- [ ] Chỉ chuẩn hoá thành dạng an toàn cho tên thư mục (bỏ dấu, gạch nối)
- [ ] Tên trùng project đã có → **đã báo và hỏi**, không tự ghi đè

## Cấu trúc
- [ ] Đủ `working/`: raw-inputs · ai-drafts · open-questions · meeting-notes · impact-analysis · solution-options
- [ ] Đủ `docs/`: brd · prd · user-guide
- [ ] Có `.gitkeep` trong thư mục rỗng

## File nền
- [ ] `project-context.md` có đủ mục: Background · Objectives · Scope · Stakeholders · **Phạm vi sản phẩm** (UpLMS/Ops) · Key References · **Lark** (space + parent node + bảng đã publish) · **Jira** (Epic/Story)
- [ ] `project-decisions.md` có bảng: Ngày · Quyết định · Lý do · Người quyết · Gate

## Báo cáo
- [ ] Đã nêu việc cần làm tiếp: điền `project-context.md` · đặt input vào `working/raw-inputs/`
- [ ] Đã nêu lệnh bắt đầu: `/po-workflow <tên-project>`
- [ ] Đã nhắc **không xoá `project-decisions.md`** — đây là bộ nhớ của dự án
