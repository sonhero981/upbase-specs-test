# Review: prd.md · 2.42 PRD Generation · lần 03
**Verdict:** READY
**Verdict Dictated:** no
**Reviewer:** ai-reviewer · **Date:** 2026-10-20

## Prior findings
| ID | Severity | Now | Note |
|---|---|---|---|
| R-05 | Major | Fixed | `AC5.1` đã thêm câu "Khi một lần đồng bộ lỗi giữa chừng, lần chạy kế tiếp tự sửa chênh lệch... không cần ai dọn tay". Dòng Document version v0.4 không còn khẳng định sai "mọi US có AC nhánh lỗi"; câu đúng lại thành "ở mọi user story mà PRD đã định nghĩa nhánh đó", và Vấn đề tồn đọng #8 liệt đúng 8 US còn thiếu (`US6` `US8` `US9` `US10` `US12` `US13` `US19` `US20`), khớp số liệu sau khi `US5` đã có AC |
| R-06 | Major | Fixed | Vấn đề tồn đọng #3 và #4 đã gạch ngang câu hỏi cũ, ghi "Đã quyết 12/10/2026" kèm nội dung quyết định đúng theo `DEC84` (loại quan hệ cố định) và `DEC85` (tài khoản kiểm thử, Comment Replier tạo trong Ops), không còn ở dạng câu hỏi mở |

## New findings
| Severity | Location | Finding | Required action |
|---|---|---|---|
| Major | prd.md > US15 > 1/ User story | 19 trên 20 US có dòng `**Ưu tiên:**` sau CR3, riêng `US15` không có, dù dòng Document version v0.4 ghi đã "Thêm dòng Ưu tiên cho từng user story" cho cả 20 US. Thiếu dòng này thì script sinh Story List cho Jira không có giá trị Priority để điền cho story US15 | Thêm dòng `**Ưu tiên:** Must` hoặc `Should`/`Could` ngay dưới câu User story của `US15`, đúng vị trí như 19 US còn lại |
| Minor | prd.md > mục Preferences | Mục này đổi tên từ "References" — tên mục do repo quyết, không được đổi theo `engine/stages/prd-generation.md` — và viết theo bảng (Figma, Tài khoản staging, BRD, Dữ liệu cơ cấu tham chiếu) thay vì năm gạch đầu dòng chuẩn của template (UX, tài liệu kỹ thuật bên thứ ba, API tham chiếu, tài khoản staging, tài liệu nền khác). Dev và QA quen tìm link theo đúng tên và cấu trúc mục References dễ bỏ sót mục này | Đổi lại tiêu đề thành "References" và trình bày theo cấu trúc gạch đầu dòng của `domain/templates/prd.md`; mục nào không áp dụng thì xoá hẳn thay vì gộp vào bảng khác |
| Minor | prd.md > bảng đầu tài liệu | Bảng mô tả đầu PRD thiếu hàng "Mã tính năng" mà `engine/stages/prd-generation.md` yêu cầu ("hàng Mã tính năng ở bảng đầu PRD, lấy từ intent.md"). Mã `LMS-F002` hiện chỉ có trong frontmatter, không hiện trên bản xem thường kể cả khi publish lên Lark | Thêm hàng `**Mã tính năng** | LMS-F002` vào đầu bảng metadata, trước hàng Target release |
| Minor | prd.md > Solution > TDD — ràng buộc nghiệp vụ cho thiết kế kỹ thuật | Tiêu đề dùng chữ viết tắt "TDD" không giải nghĩa, trong khi stage yêu cầu "không viết tắt". "TDD" dễ bị Tech PIC đọc lướt hiểu nhầm thành Test-Driven Development thay vì nội dung thật là ràng buộc nghiệp vụ cho thiết kế kỹ thuật | Đổi tiêu đề về đúng tên mục cố định "Technical Direction" theo `domain/templates/prd.md`, bỏ chữ viết tắt "TDD" |

## Summary
Hai Major Open từ lần 02 (`R-05`, `R-06`) đã sửa đúng theo `DEC93` và kiểm chứng được trong nội dung v0.4. Bốn điểm mới đều không chặn Dev bắt đầu từ bản này — 130 BR và 104 AC đã khớp 0 GAP, 0 ORPHAN theo kiểm bằng máy — nhưng `US15` thiếu dòng Ưu tiên là lỗi thực tế cần sửa trước khi sinh Story List.
