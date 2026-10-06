# Checklist: Impact Analysis

## Tiền điều kiện
- [ ] **[BLOCK]** BRD đã qua Gate 1
- [ ] **[BLOCK]** Phạm vi liên quan (Bước 5) đã được người dùng chốt trước khi dựng matrix
- [ ] Mục `❓BA` trong Related Map đã được chốt, không để trôi vào matrix

## Nguồn đã tra
- [ ] KB `01`–`11` — business rule, luồng nghiệp vụ
- [ ] KB `12` — bảng, khoá ngoại
- [ ] **[BLOCK]** Yêu cầu **chạm tới dữ liệu** → đã đọc lại schema gốc trên [Lark `Data Architecture`](https://upbasevn.sg.larksuite.com/wiki/MaFpweI68iKNMvkTioLlJ1uJgQd), không dựa vào bản chép trong KB
- [ ] Bản KB `12` quá **1 tháng** kể từ "Đối chiếu lần cuối" → đã đọc lại nguồn và cập nhật ngày
- [ ] **Swagger `components.schemas`** — field, kiểu, required, enum
- [ ] KB `13` — mail event bị chạm, có cái nào **đang tắt**
- [ ] **[BLOCK]** KB `14` §1–2 — đã kiểm vùng nào **KB chưa phủ** trước khi kết luận "không ảnh hưởng"
- [ ] KB `15` §6 — chỗ đóng cứng UpBase

## Framework
- [ ] **[BLOCK]** Đủ 5 STEP, đúng thứ tự
- [ ] STEP 1 đọc để tìm **dependency**, không phải để hiểu feature
- [ ] **[BLOCK]** Quét đủ **12 vùng**. Vùng không ảnh hưởng vẫn ghi **lý do**, không bỏ trống
- [ ] **Tính năng `hidden` được xét** — không bỏ qua vì "đang ẩn"
- [ ] 3a Conflict: đủ 4 chiều (rule · process · data · permission)
- [ ] **[BLOCK]** Conflict được **escalate**, AI **không tự resolve**
- [ ] 3b Bidirectional: có **cả chiều Old→New** — chiều này hay bị bỏ
- [ ] 3c Coverage: đủ 4 loại (boundary · exception · shared entity · side effect)
- [ ] **Shared entity** đã kiểm: `course_categories` (FK của 6 bảng) · Question Bank (4 nơi tiêu thụ)
- [ ] STEP 4 Transition: đủ Data / Compatibility / Cutover
- [ ] STEP 5 Tenant: đã trả lời đủ 4 câu hỏi

## Chất lượng
- [ ] Mỗi dòng matrix có **severity** và **nguồn**
- [ ] Thiếu context → `Open Question`, **không giả định**
- [ ] FR/NFR phát sinh đã đánh dấu **feed ngược vào BRD**

## Delivery
- [ ] **[BLOCK]** Có **Phụ lục nguồn đã đọc**, ghi cả phần **"chưa tra được"**
- [ ] **[BLOCK]** Người dùng **đã xem bản trước chưa?** Rồi → **tạo file version mới**, giữ nguyên bản cũ, thêm mục **Lịch sử thay đổi**. Chưa → sửa tại chỗ được.
      > Mốc tăng version là **mỗi lần qua Gate** hoặc mỗi đợt người dùng trả lời một loạt câu hỏi. Làm liên tục trong một phiên thì rất dễ quên — xem `CLAUDE.md` mục *Cách làm việc*.
- [ ] Đúng thư mục `working/impact-analysis/`, đúng version
- [ ] Đã chuẩn bị nội dung trình Gate 2
