# Checklist: Generate User Guide

## Tiền điều kiện
- [ ] **[BLOCK]** PRD đã qua Gate 4
- [ ] **[BLOCK]** Tính năng **đã dev xong** — User Guide mô tả cái đang chạy, không mô tả cái sắp có

## Phân bài
- [ ] Chạm cả hai hệ → **viết hai bài riêng** (`-student` và `-ops`), không gộp
- [ ] Đặt đúng repo: `uplms/` cho học viên · `uplms-ops/` cho vận hành

## Cấu trúc
- [ ] Đủ 4 mục: I. Thông tin chung · II. Hướng dẫn chi tiết · III. Lưu ý & Quy tắc nghiệp vụ · IV. Lỗi thường gặp
- [ ] **[BLOCK]** Có khai báo **`Phạm vi & Module liên quan`**: Module chính · Chức năng chính · Module liên quan
- [ ] Có `Điều kiện tiên quyết`: quyền · dữ liệu cần có trước
- [ ] Dùng đúng cú pháp GitBook: `{% hint %}`, `<details>`, `{% stepper %}`

## Giọng văn
- [ ] **[BLOCK]** Bỏ hết thuật ngữ nội bộ: tên bảng · tên field kỹ thuật · tên endpoint · mã rule
- [ ] Business rule đã dịch sang ngôn ngữ người dùng cuối
- [ ] `Out of scope` của PRD **không** đưa vào User Guide

## Nội dung
- [ ] Business rule trong guide **khớp với PRD**, không mâu thuẫn
- [ ] Mục IV có lỗi thật, lấy từ `validate` / `disable` / `tooltip` trong bảng UI của PRD

## Ảnh
- [ ] Viewport 1920×1080, headless
- [ ] Tên file đúng quy ước `NN-<role>-<mô-tả>.png`
- [ ] Ảnh đã copy về `docs/user-guide/screenshots/`, **không để trong thư mục tạm Playwright**
- [ ] Đã kiểm ảnh đạt ~1920px, layout giống desktop thật
- [ ] Không chụp được → có `<!-- ẢNH: … -->` + liệt kê vào `pending-screenshots.md`

## Sau khi viết
- [ ] Đã trình người dùng review
- [ ] **[BLOCK]** Đã **cập nhật ngược KB**: business rule mới · field đổi · quan hệ module mới, đánh mã `KB-*` và ghi nguồn là PRD nào
