# Checklist: 2.31 Impact Analysis

## Related Features Map
- [ ] **[BLOCK]** PO đã chốt bản đồ: đủ, sót, không liên quan. `❓BA` đã xử lý, không trôi vào matrix
- [ ] Field, màn Existing được nhận diện ở đây, không bị coi là mới ở stage sau

## Nguồn
- [ ] KB 01 đến 11, 12, 13, 14 §1 và §2, 15 §6 đã tra
- [ ] **[BLOCK]** Chạm dữ liệu: schema gốc trên Lark đã đọc lại, không dựa bản chép
- [ ] Swagger `components.schemas` đã tra cho field

## Framework
- [ ] **[BLOCK]** Đủ 5 bước đúng thứ tự
- [ ] **[BLOCK]** Đủ 12 vùng. Vùng không ảnh hưởng có lý do
- [ ] Hidden được xét
- [ ] Conflict 4 chiều, **[BLOCK]** được escalate, không tự resolve
- [ ] Bidirectional có cả chiều Old sang New
- [ ] Coverage đủ boundary, exception, shared entity, side effect. Shared entity `course_categories` và Question Bank đã kiểm
- [ ] Transition đủ Data, Compatibility, Cutover
- [ ] Tenant đủ 4 câu

## Giao
- [ ] Mỗi dòng matrix có severity và nguồn
- [ ] FR, NFR phát sinh đã bổ sung vào requirements với thẻ `[2.31]`, version tăng, DEC ghi
- [ ] **[BLOCK]** Phụ lục nguồn đã đọc, kể cả chưa tra được
