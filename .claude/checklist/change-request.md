# Checklist: Change Request

## Ghi nhận
- [ ] CR đã ghi vào `working/raw-inputs/change-requests.md` với ID (`CR-001`…)
- [ ] Ghi đủ: ngày · nội dung · lý do/nguồn · trạng thái

## Điểm re-entry
- [ ] **[BLOCK]** Đã xác định **tầng thấp nhất** bị ảnh hưởng, không chỉ sửa tầng dễ nhất
- [ ] Đã hỏi đúng câu: *"thay đổi này làm sai lệch kết luận của tầng nào?"*
- [ ] **[BLOCK]** Đã trình người dùng **confirm điểm re-entry** trước khi chạy lại
- [ ] Đã trình **impact preview**: tài liệu nào sẽ bị cập nhật
- [ ] Đã nêu **Gate nào phải duyệt lại**

## Update mode
- [ ] **[BLOCK]** Chỉ sửa phần bị ảnh hưởng — **không regenerate toàn bộ**
- [ ] Đã bump MINOR (`v0.X` → `v0.X+1`)
- [ ] Đã thêm dòng vào `Document version` với `Impact = CR-XXX`
- [ ] PRD: chỉ chạm US bị ảnh hưởng, US khác **không động vào**
- [ ] Mọi Gate sau điểm re-entry đã chuyển về **chờ duyệt lại**

## Tác động ngược
- [ ] Đã kiểm **business rule mồ côi** — rule cũ còn US nào dùng không
- [ ] Đã kiểm **mã tham chiếu gãy** — `BR-2.3` bị xoá mà chỗ khác còn trỏ tới
- [ ] Đã kiểm **Out of scope lỗi thời** — thứ từng ghi "không làm" nay đã làm

## Delivery
- [ ] Tóm tắt đủ: CR · điểm re-entry · tài liệu đã cập nhật · Gate cần duyệt lại · tác động ngược
