# 09 — Notification & Email

| | |
|---|---|
| Hệ | UpLMS Ops (gửi) · UpLMS (học viên nhận) |
| Đường dẫn | Engagement & Support → Notice & Email / Mail Logs / Blocked Mail / Course Comment |
| Trạng thái | 🔴 **3/4 page đang `hidden`** — xem §1 |
| Nguồn UG | `uplms-ops/engagement-and-support/` (4 page) |

---

## 1. ⚠️ Cảnh báo trạng thái — đọc trước

| Page | Trạng thái |
|---|---|
| Email và Thông báo hệ thống (Notice List & Email List) | 🔴 **hidden** |
| Nhóm người dùng nhận Email (Recipients List) | 🔴 **hidden** |
| Lịch sử gửi Email & Email bị chặn (Mail Logs, Blocked Mail) | 🔴 **hidden** |
| Nhân sự hỗ trợ trả lời bình luận (Comment Replier) | 🟢 active |

**Phần đang ẩn là giao diện gửi thủ công** — soạn và gửi Notification/Email theo setting trên Ops.

> ✅ **Đã đính chính (23/09/2026).** Bản KB đầu tiên kết luận "module Email ẩn → các luồng nghiệp vụ đứt ở mắt xích thông báo" — **sai**.
>
> BA xác nhận: **hệ thống gửi mail tự động theo event vẫn chạy bình thường** với 30 mail template. Xem [13-mail-events.md](13-mail-events.md). Chỉ phần **gửi thủ công qua giao diện Ops** là đang ẩn.
>
> ⚠️ **Nhưng một phần cảnh báo vẫn đúng, với nguyên nhân khác:** BA xác nhận **8 mail thuộc luồng chấm điểm đang tạm ngưng kích hoạt** — không phải vì module ẩn, mà bị tắt có chủ đích. Luồng chấm điểm hiện không có thông báo tự động. Xem [05-grading.md](05-grading.md) §9.

---

## 2. Bốn loại thông báo

| Type | Gửi đi đâu |
|---|---|
| **Notification** | Trên hệ thống UpLMS (học viên) |
| **Email** | Vào email học viên |
| **Noti & Email** | Cả hai |
| **Pinned Notification** | **Ghim đầu trang UpLMS, hiển thị ở mọi màn hình** |

---

## 3. Trạng thái — hai bộ khác nhau

### Notification / Email / Noti & Email

| Status | Nghĩa |
|---|---|
| Hẹn giờ gửi | Đã cài thời gian, chưa tới giờ |
| Đã gửi | Đã gửi đi |
| Hủy | Hủy thông báo đang ở 'Hẹn giờ gửi' |
| **Thu hồi** | Thu hồi thông báo 'Đã gửi' — **chỉ Type = Notification** |

### Pinned Notification

| Status | Nghĩa |
|---|---|
| Hẹn giờ gửi | Đã cài thời gian hiển thị, chưa tới giờ |
| Đang hiển thị | Đang hiện trên UpLMS |
| Hủy | Hủy hiển thị khi đang 'Hẹn giờ gửi' |
| Thu hồi | Thu hồi khi đang 'Đang hiển thị' |
| Kết thúc | Đã hết thời gian hiển thị |

### Chuyển trạng thái hợp lệ

```
Notification/Email/Noti&Email:   Hẹn giờ gửi ──► Hủy
                                 Đã gửi ──────► Thu hồi   (CHỈ Type = Notification)
Pinned Notification:             Hẹn giờ gửi ──► Hủy
                                 Đang hiển thị ► Thu hồi
```
**Mọi chuyển đổi khác đều không được phép.**

---

## 4. Field — tạo thông báo

| Field | Bắt buộc | Ghi chú |
|---|---|---|
| Title | **Có** | |
| **Pinned Notification** | **Có** | `Yes` / `No` — **không sửa được sau khi tạo** |
| Type | **Có** | Chọn 1 hoặc nhiều; chỉ áp dụng khi Pinned = No |
| Send to | **Có** | Nhóm người nhận (từ Recipients List). **Pinned không có Send to** — mặc định gửi tất cả học viên |
| Action | **Có** | `Hẹn giờ gửi` (dd/mm/yyyy hh:mm) hoặc `Gửi ngay` |
| Nội dung thông báo | **Có** | |
| Tệp đính kèm | Không | Chỉ với Email. **Tối đa 500MB/file** |

### Ràng buộc định dạng thời gian — rất đặc thù

> **Phút chỉ nhận `mm = 00` hoặc `mm = 30`.** Không có mốc nào khác. Đây là ràng buộc hệ thống chạy job theo nửa tiếng. `[suy ra]`

Với Pinned Notification: `Hẹn giờ gửi` cần **cả thời gian bắt đầu và kết thúc**; `Gửi ngay` chỉ cần thời gian kết thúc.

---

## 5. Recipients List (Nhóm người nhận)

| Thuộc tính | Giá trị |
|---|---|
| Field bắt buộc | Tên Nhóm |
| Nguồn thành viên | **User Management** |
| Cấu trúc màn | Tab `Group Settings` (tên nhóm) + Tab `Add Member` (thành viên) |
| Thứ tự bắt buộc | **Phải Save tên Nhóm trước** mới thêm được thành viên |

> Xoá Nhóm → **các thông báo đã dùng Nhóm này vẫn giữ nguyên**, chỉ ảnh hưởng việc chọn Nhóm cho thông báo mới.
> Thêm/xoá thành viên **phải bấm Finish/Save**, rời màn hình mà không lưu thì mất thay đổi.

---

## 6. Mail Logs & Blocked Mail

### Mail Logs

Cột: `Title` · `Receiver` · `Status` (Đã gửi / Thất bại) · `Sent time`. Lọc theo Người nhận, Loại Mail, Status, khoảng ngày.

Thao tác: **Resend** — gửi lại email cho người nhận.

### Blocked Mail

Cột: `Địa chỉ email` · `Date` · `Reason` (lý do bị chặn). Thao tác: **Unblock**.

> **Hệ thống Email là hệ tích hợp ngoài** — UG khai báo rõ: *"Hệ thống Email (gửi email tới học viên và phản hồi trạng thái bị chặn)"*. Trạng thái blocked do hệ ngoài đẩy về.

---

## 7. Comment Replier (🟢 page duy nhất còn active)

Nhóm nhân sự trả lời bình luận của học viên trên UpLMS, dùng **Display Name và Avatar chung** thay vì danh tính cá nhân.

| Field | Ghi chú |
|---|---|
| Name | Tên gợi nhớ nội bộ |
| Display Name | Tên hiển thị cho học viên trên UpLMS |
| **Course Category** | Danh mục khoá học nhóm chịu trách nhiệm |
| Avatar | Hình đại diện hiển thị cho học viên |

### Cơ chế đặc biệt — cần chú ý

| Rule |
|---|
| Thành viên phải là **tài khoản học viên có `Test Account = Yes`** |
| Mỗi nhóm cấu hình theo **một Course Category**; **không được trùng Category** với nhóm đã tồn tại |
| Một tài khoản **không thuộc 2 nhóm cùng Course Category** |
| ⚠️ Thêm thành viên vào nhóm → **tự động thêm vào các lớp** có Danh mục gắn với nhóm (mỗi khoá chỉ thêm vào **1 lớp duy nhất**); thời hạn học **gia hạn liên tục mỗi năm một lần** |
| ⚠️ Xoá thành viên khỏi nhóm / xoá nhóm → thành viên **bị xoá khỏi các lớp** có khoá thuộc Category đã thêm |

> Đây là cơ chế **ghi dữ liệu tự động vào Class** từ một module tưởng như chỉ là cấu hình hiển thị. Rất dễ bỏ sót khi phân tích impact về Class hoặc Student.

---

## 8. Business Rule

| ID | Rule | Nguồn |
|---|---|---|
| KB-NOTI-01 | **Chỉ Type = Notification và Status = 'Đã gửi' mới Thu hồi được.** Email đã gửi **không thu hồi được**. | notice-list mục III |
| KB-NOTI-02 | Chỉ thông báo Status = 'Hẹn giờ gửi' mới **chỉnh sửa thông tin** được; các trạng thái khác chỉ đổi được Status. | notice-list mục III |
| KB-NOTI-03 | Trường **Pinned Notification không sửa được** sau khi tạo. | notice-list mục III |
| KB-NOTI-04 | Khoảng thời gian hiển thị của Pinned Notification mới **không được trùng** với Pinned đã tạo trước đó. | notice-list mục III |
| KB-NOTI-05 | Định dạng thời gian gửi/hiển thị: `dd/mm/yyyy hh:mm` với **phút = 00 hoặc 30**. | notice-list mục III |
| KB-NOTI-06 | Tệp đính kèm tối đa **500MB/file**. | notice-list mục III |
| KB-NOTI-07 | Pinned Notification hiển thị cho **tất cả học viên**, không có lựa chọn Send to. | notice-list mục II |
| KB-NOTI-08 | Xoá Nhóm người nhận → **thông báo đã dùng nhóm vẫn giữ nguyên**. | recipients-list mục III |
| KB-NOTI-09 | Phải **Save tên Nhóm trước** mới thêm được thành viên. | recipients-list mục IV |
| KB-NOTI-10 | Thêm/xoá thành viên phải bấm **Finish/Save**, không lưu thì mất thay đổi. | recipients-list mục III |
| KB-CR-01 | Thành viên Comment Replier phải là học viên có **`Test Account = Yes`**. | comment-replier mục I |
| KB-CR-02 | Mỗi nhóm Comment Replier gắn **một Course Category**, không trùng với nhóm khác. | comment-replier mục IV |
| KB-CR-03 | ⚠️ Thêm thành viên → **tự động thêm vào lớp** thuộc Category (mỗi khoá 1 lớp); thời hạn **gia hạn mỗi năm 1 lần**. | comment-replier mục III |
| KB-CR-04 | ⚠️ Xoá thành viên/xoá nhóm → **xoá khỏi các lớp** có khoá thuộc Category đã thêm. | comment-replier mục III |

---

## 9. Phụ thuộc

| Module | Quan hệ | Ghi chú |
|---|---|---|
| **Hệ thống Email ngoài** ⚠️ | Gửi mail, phản hồi trạng thái blocked | Tích hợp ngoài, UG khai báo rõ |
| **User Management** | Nguồn thành viên Recipients List | |
| **Grading** ⚠️ | 4 điểm gửi email trong luồng chấm | **Rủi ro cao** nếu module ẩn |
| **Student (UpLMS)** | Nhận Notification, Pinned Notification | |
| **Course Category** | Phân nhóm Comment Replier | |
| **Class** ⚠️ | Comment Replier **tự động ghi/xoá học viên trong lớp** | Quan hệ ẩn, dễ sót |
| **Discussion** | Comment Replier trả lời bình luận với danh tính nhóm | |

---

## 10. Điểm cần BA xác nhận

| # | Câu hỏi |
|---|---|
| Q1 | 🚨 **3 page đang ẩn — module Email/Notification có thực sự đang chạy không?** Nếu không, các luồng Grading / OTP / thông báo học viên đang xử lý ra sao? |
| Q2 | Hệ thống Email tích hợp là dịch vụ nào (SendGrid, SES, SMTP nội bộ...)? |
| Q3 | Email bị chặn (Blocked) do đâu — bounce, spam report, hay hệ thống tự chặn? |
| Q4 | KB-NOTI-05: ràng buộc phút = 00/30 là do job chạy theo nửa tiếng? Xác nhận giúp tôi. |
| Q5 | KB-CR-03: "thời hạn học gia hạn liên tục mỗi năm một lần" — cơ chế tự động hay thủ công? Ai chạy? |
| Q6 | "Thu hồi" Notification đã gửi nghĩa là gì phía học viên — biến mất khỏi danh sách, hay đánh dấu đã thu hồi? |
| Q7 | `Test Account` là trường của Student — nằm ở màn nào, ai set? (trùng với Q4 của [06-user-account.md](06-user-account.md)) |
