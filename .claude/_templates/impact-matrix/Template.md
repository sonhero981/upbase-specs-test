# Impact Matrix — <Tên tính năng>

| | |
| --- | --- |
| **Project** | |
| **Version** | v0.1 |
| **Ngày** | |
| **Nguồn input** | `brd-v*.md` (Gate 1) · KB · DB Diagram · Swagger |
| **Trạng thái** | `Draft` / `Pending Confirmation` / `Approved` |

> Bản phân tích **nội bộ**, không phải mục trong PRD. Kết quả chảy vào PRD ở: `Solution` · `Database` · `API` · `Acceptance criteria → Data Field` · `Out of scope`.

---

## 1. Summary

*3–5 dòng: thay đổi này chạm vào đâu, chỗ nào nguy hiểm nhất, có conflict nào phải quyết không.*

| | Số lượng |
| --- | --- |
| Vùng bị ảnh hưởng (High / Medium / Low) | / / |
| Conflict cần escalate | |
| FR/NFR bổ sung phát hiện được | |
| Coverage gap | |
| Chỗ đóng cứng tenant tăng thêm | |

---

## 2. Current Situation — Dependency Map *(STEP 1)*

*Đọc để tìm **dependency**, không phải để hiểu feature.*

| Loại | Mục | Nguồn | Ghi chú |
| --- | --- | --- | --- |
| Module / Feature | | KB `0X §Y` | |
| Data / Entity / Field | | KB `12` · bảng `<tên>` | |
| Business Rule | | `BR-XXX-01` / `KB-XXX-01` | |
| Process / Workflow | | | |
| Permission | | KB `06 §9` · `casbin_rule` | |
| Integration / Consumer | | KB `14` | |
| **Mail event liên quan** | | KB `13` — mail #N | Đang bật / **đang tắt** |
| **Tính năng ẩn bị chạm** | | KB `00-index` | `hidden: true` |

> ⚠️ Tính năng `hidden` vẫn phải xét — đã có code, chỉ tạm ẩn.

---

## 3. Desired Situation *(STEP 2)*

*Từ BRD: tính năng mới làm gì · process mới ra sao · FR/NFR đã có.*

---

## 4. Impact Matrix — 12 vùng *(STEP 3.0)*

### Severity

| Mức | Nghĩa |
| --- | --- |
| **High** | Đổi hành vi hiện tại, hoặc hỏng dữ liệu/luồng nếu làm sai |
| **Medium** | Phải sửa nhưng không đổi hành vi hiện tại |
| **Low** | Chỉ thêm mới, không chạm cái cũ |

### Bảng

| # | Vùng | Bị ảnh hưởng? | Mô tả | Severity | Nguồn |
| --- | --- | --- | --- | --- | --- |
| 1 | Business process | | | | |
| 2 | Module / function | | | | |
| 3 | Screen / report | | | | |
| 4 | Data | | | | |
| 5 | API | | | | |
| 6 | Role / permission | | | | |
| 7 | Business rule | | | | |
| 8 | NFR | | | | |
| 9 | Notification / Email | | | | KB `13` |
| 10 | Reporting | | | | |
| 11 | Test | | | | |
| 12 | Release | | | | |

> Vùng **không** bị ảnh hưởng vẫn phải ghi **lý do**. Bỏ trống nghĩa là chưa xét.
>
> Vùng nằm trong phần **KB chưa phủ** (lịch dạy · phòng học · thi cử · phòng ban · phân quyền — xem KB `14` §1–2) → ghi `❓BA`, **không kết luận "không ảnh hưởng"**.

---

## 5. Conflict Analysis *(STEP 3a)*

*Bốn chiều. Phát hiện conflict → **escalate, không tự resolve**.*

| Chiều | Nghĩa |
| --- | --- |
| **Business rule** | Rule mới mâu thuẫn rule hiện tại |
| **Process** | Quy trình mới phá quy trình đang chạy |
| **Data** | Ràng buộc dữ liệu xung đột |
| **Permission** | Ai được làm gì bị mâu thuẫn |

| # | Chiều | Conflict | Rule/luồng hiện tại | Rule/luồng mới | Ai quyết |
| --- | --- | --- | --- | --- | --- |

---

## 6. Bidirectional Impact — FR/NFR còn thiếu *(STEP 3b)*

| Chiều | Câu hỏi |
| --- | --- |
| **New → Old** | Tính năng mới làm hỏng gì ở cái đang chạy |
| **Old → New** | Cái đang chạy **ràng buộc gì** lên tính năng mới ← *chiều này hay bị bỏ* |

| # | Chiều | Phát hiện | FR/NFR bổ sung | Feed ngược vào BRD? |
| --- | --- | --- | --- | --- |

---

## 7. Coverage Gaps *(STEP 3c)*

| Loại | Kiểm gì |
| --- | --- |
| **Boundary** | Giá trị biên, rỗng, tối đa, trùng |
| **Exception** | Lỗi mạng, timeout, thao tác đồng thời, quyền bị thu hồi giữa chừng |
| **Shared entity** | Entity dùng chung bị chạm |
| **Side effect** | Hệ quả ngoài ý muốn ở chỗ khác |

> **Shared entity là chỗ dễ vỡ nhất của hệ này.** `course_categories` là FK của 6 bảng (`courses`, `users`, `staffs`, `quizzes`, `certificates`, `support-groups`). Question Bank được tiêu thụ bởi Test, Quiz, Case Study, Storyline. Chạm vào chúng là chạm nhiều nơi.

| # | Loại | Case chưa định nghĩa | FR bổ sung |
| --- | --- | --- | --- |

---

## 8. Transition Requirements *(STEP 4)*

| Loại | Nội dung |
| --- | --- |
| **Data** | Migration · backfill · dữ liệu cũ xử lý sao |
| **Compatibility** | Bản cũ và mới chạy song song được không |
| **Cutover** | Thứ tự bật · rollback · ẩn hay hiện khi golive |

---

## 9. Kiểm tra chiều tenant *(STEP 5)*

*Đối chiếu KB `15-product-direction.md` §6. Ràng buộc: tính năng làm cho UpBase, **dữ liệu và hạ tầng thiết kế cho đa tenant**.*

| Câu hỏi | Trả lời | Xử lý |
| --- | --- | --- |
| Có nhúng thêm logic riêng UpBase vào code không? | | Nếu có → đề xuất cách tách |
| Có hằng số cứng mới không? | | Khai báo: hardcode hay cấu hình được |
| Bảng mới có `tenant_id` không? | | Thiếu → rủi ro rò rỉ dữ liệu |
| Enum/danh mục mới: hệ thống định nghĩa hay tenant tự định nghĩa? | | |

---

## 10. Risk Summary

| # | Risk | Mức | Giảm nhẹ |
| --- | --- | --- | --- |

---

## 11. Open Questions

| # | Câu hỏi | Vì sao quan trọng | Người trả lời | Chặn Gate 3? |
| --- | --- | --- | --- | --- |

---

## 12. Phụ lục — Nguồn đã đọc

*Bắt buộc. Để người duyệt biết phân tích dựa trên gì và **thiếu gì**.*

| Nguồn | Cụ thể |
| --- | --- |
| KB | `01-course.md §5` · `12-data-model.md §2` · … |
| DB | Bảng `classes`, `class_user_instances` · FK `hybrid_class_id` |
| Swagger | `GET /api/v1/classes` · schema `ClassResponseDto` |
| Mail | KB `13` mail #17, #19 |
| **Chưa tra được** | *Vùng nào không có nguồn để tra — ghi rõ* |
