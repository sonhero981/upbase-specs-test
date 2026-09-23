# Checklist: PO Workflow

Tự kiểm khi điều phối toàn luồng. `[BLOCK]` = không đi tiếp cho đến khi đạt.

## Xác định project
- [ ] **[BLOCK]** Đã echo + confirm project trước khi chạy
- [ ] Nhiều project khả dĩ → **liệt kê cho chọn**, không tự đoán
- [ ] Đã đọc `project-context.md` và `project-decisions.md`
- [ ] Đã tra `project-decisions.md` để **không hỏi lại câu đã có đáp án**

## Trình tự
- [ ] **[BLOCK]** Không nhảy Gate. Mỗi Gate phải có quyết định rõ ràng trước khi sang giai đoạn sau
- [ ] **[BLOCK]** Trả lời Gate không rõ → **hỏi lại**, không suy đoán là duyệt
- [ ] Ba điểm dừng nhỏ đã thực hiện: chốt phạm vi (B5) · confirm danh sách US (9A) · Field Intake (9B)
- [ ] Đã chạy `/compact` trước Bước 6 và Bước 9

## Artifact
- [ ] Mỗi artifact lưu đúng chỗ: BRD → `docs/brd/` · Impact → `working/impact-analysis/` · Solution → `working/solution-options/` · PRD → `docs/prd/`
- [ ] Không ghi đè bản cũ — dùng version mới
- [ ] Mỗi artifact ghi rõ nguồn input

## Chất lượng chung
- [ ] **[BLOCK]** Không bịa. Thiếu nhẹ → `Assumption`; thiếu ảnh hưởng scope/rule/data/flow → `Open Question`
- [ ] Tách rõ `Fact` / `Assumption` / `Open Question` / `Recommendation`
- [ ] Không tự chốt quyết định thay người dùng
- [ ] Quyết định đã chốt được ghi vào `project-decisions.md`

## Sau khi xong
- [ ] Đã gợi ý bước tiếp theo (`/review-output`, `/publish-lark`, `/change-request`)
- [ ] Publish Lark: **hỏi trước**, người dùng có thể skip

## Phân loại cỡ yêu cầu
- [ ] **[BLOCK]** Đã phân loại S / M / L sau Bước 2, dựa trên quét nhanh KB + DB + Swagger
- [ ] **[BLOCK]** Đã echo phân loại **kèm lý do** và được người dùng đồng ý
- [ ] Nghi ngờ giữa hai cỡ → **chọn cỡ lớn hơn**
- [ ] Phát hiện giữa chừng vượt cỡ (chạm rule hiện có, `❓BA` về dữ liệu cũ) → **dừng, báo, nâng cỡ**
- [ ] Cỡ S: vẫn chạy **Field Intake** (9B), không bỏ qua
- [ ] Người dùng muốn đổi cỡ → theo người dùng
