---
intent: 260923-gamification
unit: u0-foundation
artifact: rules
stage: 3.1 functional-design
version: 1.0
status: approved
approved_at: 2026-10-13 ([GIẢ LẬP] BE lead, DEC-T11)
---
# Business Rules: U0 `u0-foundation`

Mã `BRx.y` = `BR-x.y` của PRD v0.14. Nội dung viết lại cho lát; chỗ thêm từ câu trả lời 2.43 ghi `[2.43 Qn]`.

## Cấu hình chung (US14)
- **BR14.1** Hai công tắc tạo ba trạng thái: tắt hẳn, chạy ngầm, bật đầy đủ (bảng ở `entities.md`).
- **BR14.2** `Visibility in UpLMS` chỉ hiện và chỉ bật được khi `Gamification` đang bật. Tắt `Gamification` thì công tắc 2 ẩn, giá trị giữ nguyên. Yêu cầu đổi `Visibility` (bật hay tắt) khi `Gamification` tắt bị từ chối, kể cả khi giá trị bằng giá trị đang lưu.
- **BR14.5** Mỗi lần bật `Gamification` ghi thời điểm bật gần nhất; lần đầu ghi thêm thời điểm bật đầu tiên, không bao giờ đổi lại. Unit sau tính từ thời điểm bật, không tính bù.
- **BR14.6** Tổ chức chưa có cấu hình (mới hoặc có sẵn lúc lên bản) nhận cấu hình mặc định mọi công tắc tắt khi được đọc lần đầu [2.43 Q4]. Hai lần đọc đồng thời không tạo hai bản.
- **BR14.8** Cấu hình gắn với tổ chức; người của tổ chức này không đọc, không ghi được cấu hình tổ chức khác.
- **BR14.9** Múi giờ là thuộc tính của tổ chức, mặc định `Asia/Ho_Chi_Minh`; không có ô chọn trên màn Gamification, không ghi qua API cấu hình.
- **BR14.10** Bấm công tắc là lưu, không nút lưu; mỗi lần lưu chỉ đổi đúng một công tắc. Công tắc có hiệu lực ngay khi lưu xong: lần đọc ngay sau đó thấy giá trị mới [2.43 Q3].
- **BR14.11** Yêu cầu lưu không hợp lệ (không có công tắc nào, nhiều hơn một, giá trị không phải bật/tắt) bị từ chối, không đổi gì.
- **BR14.12** Lưu xong báo `Saved` nhỏ, tự ẩn. Lưu lỗi thì công tắc về giá trị đã lưu và báo lỗi. Không cảnh báo khi rời trang.
- **BR14.13** Hai thao tác hỏi lại bằng popover nhỏ cạnh công tắc trước khi lưu; Huỷ thì không lưu, công tắc về như cũ:
  - Tắt `Gamification`: `Turn off gamification?` · `Points, badges and levels stop being recorded and all four features are locked. Existing data is kept. Turning it back on starts recording from that moment, nothing is backfilled.` · `Turn off` / `Cancel`. Lát này không có phần campaign.
  - Bật `Visibility in UpLMS` khi tổ chức **chưa từng** bật [2.43 Q2]: `Show gamification to your users?` · `They will immediately see all points, badges and levels earned so far. No notifications are sent for past achievements.` · `Show` / `Cancel`. Đã từng bật thì không hỏi.
  Các thao tác khác không hỏi lại.

## Phân quyền (US15)
- **BR15.1** Quyền gamification là nhóm mới trong hệ phân quyền Ops hiện có, gán ở màn role hiện có; không màn riêng.
- **BR15.2** Tách quyền xem và quyền sửa.
- **BR15.3** Không có quyền nào trong nhóm Gamification: không thấy mục menu, mở thẳng đường dẫn ra màn không có quyền, API từ chối.
- **BR15.5** Mọi vai trò Ops (gồm L&D, Mentor, Giáo viên) chỉ thấy theo quyền được gán.
- **BR15.6** Đổi quyền có hiệu lực theo cơ chế hiện có (sau khi tải lại thông tin người dùng).
- **BR15.7** Lát này: xem cấu hình → thấy công tắc, không đổi được; sửa cấu hình → đổi được; chỉ có quyền xem danh sách học viên → vào được trang nhưng không thấy khối chung [2.43 Q1]. Superadmin luôn được.

## Ngoài lát
BR14.3, BR14.4, BR14.7, BR15.4, BR15.8 không thuộc U0; xem `inception/test-cases/test-cases.md` mục "BR hoãn" và TC-20 (BR15.4: học viên không bị ảnh hưởng).
