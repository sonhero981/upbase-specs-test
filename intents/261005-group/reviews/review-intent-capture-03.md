# Review: brd.md · 1.1 Intent Capture & Framing · 1.4 Scope Definition · 1.7 Approval & Handoff · lần 03
**Verdict:** READY
**Verdict Dictated:** no
**Reviewer:** ai-reviewer · **Date:** 2026-10-21

## Prior findings
| ID | Severity | Now | Note |
|---|---|---|---|
| R-01 | Critical | Fixed | Mentor ở §5 *Quan hệ mentor* và `US12` khớp `CF-6`: mentor của nhóm chính là mentor của lớp |
| R-02 | Critical | Fixed | §1 *Product boundary* đủ portal, tenant, tầng, hằng số, chỗ đóng cứng; `US16` đúng ở **UpLMS Ops** |
| R-03 | Critical | Fixed | `MAIL-GRP-02` có đủ ở §7, kèm điều kiện bắn và không bắn |
| R-04 | Major | Accepted risk | Giữ nguyên quyết định DEC78: bảng Unit đã có ở PRD, BRD không lặp lại |
| R-05 | Minor | Accepted risk | Giữ nguyên quyết định DEC78: PRD đã có Tiêu chí thành công cho từng objective |
| R-06 | Minor | Accepted risk | Giữ nguyên quyết định DEC78: stakeholder lấy từ yêu cầu gốc, PO là người quyết |
| R-07 | Minor | Fixed | §11 References trỏ đúng cấu trúc intent v2 (dù một số số phiên bản đã lỗi thời — xem New findings) |
| R-08 | Minor | Fixed | Dùng `❓PO` nhất quán ở §2, không còn `❓BA` |

## New findings
| Severity | Location | Finding | Required action |
|---|---|---|---|
| Major | brd.md §8 Tác động tới hệ thống hiện tại | Bảng module bị chạm không có **Chấm điểm**, dù `DEC103` (CR6) cho phép người vừa là mentor vừa là thành viên của cùng một lớp tự chấm bài của mình — đây là thay đổi hành vi trực tiếp của module chấm điểm, không chỉ là rủi ro chấp nhận ở §5. Người quét bảng này để biết việc chạm module nào sẽ bỏ sót nó | Thêm một dòng "Chấm điểm" vào bảng §8, ghi lý do chạm là `DEC103`; sửa câu dẫn đầu mục để nói rõ bảng đã cập nhật theo CR6, không chỉ CR1 |
| Minor | brd.md §5 In scope · Một người nhiều vai | Câu tóm tắt `DEC102` chỉ nói "lên quản lý của nhóm cha gần nhất", bỏ sót vế hết cây thì gửi quản trị viên hệ thống — vế này có đủ ở `decisions.md` DEC102 và `requirements.md` RC-22, nhưng không có trong brd.md. Người chỉ đọc BRD sẽ không biết trường hợp hết cây xử lý thế nào | Viết lại dòng này, thêm "hết cây thì gửi quản trị viên hệ thống", hoặc ít nhất dẫn rõ sang `RC-22` |
| Minor | brd.md §5 Out of scope | Không ghi nhận `DEC84` (chỉ đúng hai loại quan hệ cố định — quản lý và mentor; tổ chức không tự thêm loại mới), dù hạng mục 19 của yêu cầu gốc từng mô tả đây là cơ chế "dùng chung, mở rộng được" và PO đã chốt dứt điểm câu hỏi này ở stage 2.41. Thiếu dòng này, người đọc BRD có thể hiểu nhầm cơ chế quan hệ còn mở để thêm loại mới | Thêm một dòng Out of scope: "Thêm loại quan hệ người–nhóm mới ngoài quản lý và mentor", dẫn `DEC84` |
| Minor | brd.md §11 References | Bảng trỏ tới bản cũ: "`inception/prd/prd.md` v0.2 — 20 US, 128 business rule" (hiện là v0.6, 130+ business rule kèm AC), "`impact-matrix.md` v0.3" (hiện là v0.5 theo CR6 trong `decisions.md`), "`decisions.md` — DEC1 đến DEC78" (hiện tới DEC104) | Cập nhật ba dòng Phạm vi hiện hành chi tiết, Ảnh hưởng, Quyết định đã chốt ở §11 theo đúng phiên bản và mã DEC mới nhất sau CR6 |

## Summary
Ba finding Critical của lần 01 vẫn giữ Fixed sau CR6, không hồi lại. Các thay đổi của CR6 (DEC100–DEC104: bỏ giới hạn cấp, một tài khoản nhiều vai, thông báo quản lý cấp gần nhất, tạm cho tự chấm, báo cáo ở tab chi tiết nhóm) được phản ánh nhất quán ở §1, §5, §6, §9, §10 — không còn sót "6 cấp" hay "tài khoản nhân sự vận hành" từ bản cũ. Bốn finding mới đều là chỗ thiếu khi cập nhật theo CR6 (một module tác động bị bỏ sót, một quy tắc tóm tắt thiếu vế cuối, một quyết định phạm vi không được ghi lại, và các mục tham chiếu lỗi thời), không có Critical, chỉ một Major có cách sửa rõ ràng — đạt ngưỡng READY.
