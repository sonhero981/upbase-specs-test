# Sổ finding: prd-generation
| ID | Lần | Mức | Vị trí | Finding | Trạng thái | Quyết định của PO |
|---|---|---|---|---|---|---|
| R-01 | 01 | Major | prd.md > US9 > Nội dung email MAIL-GRP-02 · US11 | Gán quản lý chính qua US11 chưa nói có gửi MAIL-GRP-02 hay không | Fixed | Sửa theo DEC76 ngày 09/10/2026: thêm BR-11.7 |
| R-02 | 01 | Major | prd.md > US13 > BR-13.6 | Email gộp khi chuyển phụ trách chưa nói có loại nhóm người nhận đã quản lý sẵn không | Fixed | Sửa theo DEC76: BR-13.6 chỉ liệt nhóm mới, không còn nhóm mới thì không gửi |
| R-03 | 01 | Minor | prd.md > BR-9.7 · BR-13.6 | Thiếu câu nối hai trục số người nhận và số nhóm | Fixed | Sửa theo DEC76 |
| R-04 | 01 | Minor | prd.md > BR-13.3 · MAIL-GRP-02 | Phần mentor được chuyển có được báo không | Fixed | Sửa theo DEC76: thêm BR-13.7 |
| R-05 | 02 | Major | prd.md > Document version v0.4 · US5 US6 US8 US9 US10 US12 US13 US19 US20 > Tiêu chí chấp nhận | Dòng v0.4 khẳng định mỗi US có AC nhánh bị từ chối hoặc lỗi, nhưng 9 US chưa có AC như vậy | Fixed | Request Changes, sửa theo DEC93: AC5.1 thêm luật đồng bộ lỗi; dòng v0.4 sửa; 8 US ghi tồn đọng #8 |
| R-06 | 02 | Major | prd.md > Vấn đề tồn đọng #3 · #4 | Hai câu đã được PO chốt ở DEC84, DEC85 nhưng bảng vẫn ghi là câu hỏi mở | Fixed | Request Changes, sửa theo DEC93: tồn đọng #3 #4 ghi đã quyết |
| R-07 | 03 | Major | prd.md > US15 > 1/ User story | US15 thiếu dòng Ưu tiên | Rejected | Rejected: "Approve: bác R-07, chấp nhận R-08 R-09 R-10 (Recommended)". US15 có dòng **Ưu tiên:** Should; file có đủ 20 dòng Ưu tiên |
| R-08 | 03 | Minor | prd.md > Preferences | Tên mục khác template (References) và không theo cấu trúc gạch đầu dòng | Accepted risk | "Approve: bác R-07, chấp nhận R-08 R-09 R-10 (Recommended)". Tên mục cũ của PRD đã publish; đổi tên chờ chủ template xác nhận |
| R-09 | 03 | Minor | prd.md > bảng đầu tài liệu | Thiếu hàng Mã tính năng LMS-F002 | Accepted risk | "Approve: bác R-07, chấp nhận R-08 R-09 R-10 (Recommended)". Mã có trong frontmatter, Story List lấy mã từ đó; bổ sung ở lần sửa PRD sau |
| R-10 | 03 | Minor | prd.md > Solution > TDD | Tiêu đề viết tắt TDD, template gọi là Technical Direction | Accepted risk | "Approve: bác R-07, chấp nhận R-08 R-09 R-10 (Recommended)". Cùng lý do R-08 |
