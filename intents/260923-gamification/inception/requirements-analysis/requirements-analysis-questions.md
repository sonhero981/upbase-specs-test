# Open Questions — Gamification

| | |
|---|---|
| Project | Gamification |
| Cập nhật | **v0.2 — 23/09/2026** |
| Nguồn | `working/ai-drafts/clarified-requirements-20260923.md` |
| Tổng | 16 câu — **8 đã chốt** · **2 đang chờ** · 6 không chặn |

---

## ✅ Đã chốt — PO trả lời 23/09/2026

Mọi quyết định đã ghi vào `project-decisions.md`. **Không hỏi lại.**

| ID | Câu hỏi | Đáp án của PO | Hệ quả |
|---|---|---|---|
| **OQ-01** | Có làm bảng xếp hạng không? | **Làm sau** | RC-12 → `Potential scope`. Nhưng RC-06 (điểm theo kỳ) **vẫn làm** vì là nền dữ liệu |
| **OQ-02** | "Lộ trình" là gì? | **Nội dung học tương tự khoá học, làm sau** | Bỏ hành động "hoàn thành lộ trình" → `Out of scope`. Còn 4/6 hành động |
| **OQ-03** | Lấy dữ liệu đăng nhập ở đâu? | **Keycloak.** Chuỗi ngày tính **từ ngày go-live**, không hồi tố | Giữ hành động "đăng nhập liên tiếp" và điều kiện huy hiệu "chuỗi ngày". Phát sinh phụ thuộc kỹ thuật → `OQ-17` |
| **OQ-04** | "Kỳ" là gì? | **Kỳ = chiến dịch.** Hết kỳ thì **lưu lại**, không xoá. Sau này dùng cho leaderboard | RC-06 giữ nguyên. Cần bảng lưu lịch sử kỳ |
| **OQ-06** | "Kỹ năng" là gì? | **Skills, thuộc tính năng Khung năng lực — làm sau** | Bỏ điều kiện huy hiệu "đạt kỹ năng" → `Out of scope`. Còn 4/5 loại điều kiện |
| **OQ-08** | Ai cấu hình? Đổi cách tính có hồi tố? | **Nhân sự vận hành có quyền tương ứng, trên Ops.** Đổi cách tính **áp dụng từ lúc đổi**, không tính lại lịch sử | Cần resource phân quyền mới trong Casbin |
| **OQ-09** | Vấn đề thật là gì? | **Học viên không chủ động vào học.** Gamification để duy trì động lực, làm nền cho leaderboard sau, **để đội truyền thông nội bộ chạy chiến dịch** thúc đẩy tinh thần học | `Problem` đã có. Phát hiện stakeholder mới: **Đội truyền thông nội bộ** |
| **OQ-10** | Có sửa logic hoàn thành Activity không? | **Không sửa, giữ nguyên.** Riêng Video **đã được cập nhật thành xem ≥80% thời lượng** | Đã cập nhật KB `07` → `KB-LX-03a`, `KB-LX-03b`. Phát sinh `OQ-16` |

---

## ⏳ Đang chờ PO

| ID | Câu hỏi | Trạng thái | Blocks |
|---|---|---|---|
| **OQ-07** | **Tắt gamification nghĩa là gì?** | ✅ **Đã phân tích** — xem §13 của bản làm rõ.<br>`Recommendation`: **hai công tắc** (`ghi nhận` + `hiển thị cho học viên`) cho ba trạng thái: *Tắt hẳn* · *Chạy ngầm* · *Bật đầy đủ*.<br>Lý do chính cho công tắc thứ hai: số điểm đặt lần đầu gần như chắc chắn sai; chạy ngầm 2–4 tuần để xem phân bố thật trước khi mở cho học viên. Chi phí gần bằng 0.<br>**Chờ PO chọn** | **Yes** |
| **OQ-16** | **Chống cày điểm với Activity dạng Text/Ảnh.** `KB-LX-03b`: loại này vẫn hoàn thành ngay khi mở hiển thị. Cơ chế *"không cộng điểm cho hoạt động bỏ qua quá nhanh"* trong RC-07 **không áp dụng được** nếu không đo thời gian — mà đo thời gian là sửa logic hoàn thành, điều PO đã chốt không làm.<br>Hai hướng: (a) chấp nhận chỉ dựa vào **trần điểm/ngày** + **chống cộng trùng nội dung đã học**; (b) gamification **tự đo thời gian riêng cho việc cộng điểm**, không đụng tới trạng thái hoàn thành của Activity | Mới phát sinh từ OQ-10 | **Yes** |

---

## Không chặn — xử lý ở Gate sau

| ID | Câu hỏi | Xử lý ở |
|---|---|---|
| OQ-05 | "Đạt bài kiểm tra" và "đạt điểm cao" là ngưỡng nào? Có dùng `Pass Point` sẵn có không? Cùng xảy ra thì cộng dồn? | Field Intake (9B) |
| OQ-11 | Thông báo thành tích cần tức thời tới mức nào? Hệ thống hiện gửi theo job nửa tiếng (`KB-NOTI-05`) và không có API sinh thông báo theo sự kiện cho từng người | Gate 2 / Gate 3 |
| OQ-12 | Chống cộng trùng "học lại" theo `(user_id, course_section_id)` cắt ngang lớp? Mọi bảng tiến độ treo vào `class_user_instances`, không treo vào `users` | Gate 2 |
| OQ-13 | Chốt từ vựng: "Point" đã là `Pass Point`, "Level" đã là `Course Level` và `Staff Level`. Gợi ý **Reward Point**/**XP** và **Rank**/**Tier** | Trước khi viết PRD |
| OQ-14 | Hoàn thành khoá đã có mail #10 và #29 đang chạy — gộp điểm vào mail sẵn có hay tách kênh riêng? | Gate 2 |
| OQ-15 | Luồng chấm điểm đang tắt hết thông báo (8 mail, gồm #19). Học viên sẽ biết được điểm thưởng trước khi biết bài đã chấm. Có bật lại mail #19 không? *(quyết định của luồng Grading, không thuộc gamification)* | Nêu để PO biết |
| **OQ-17** | **Keycloak có lưu sự kiện đăng nhập không, giữ bao lâu?** PO đã chốt nguồn là Keycloak, nhưng Keycloak mặc định **tắt** event logging và có hạn lưu trữ riêng. Cần Dev xác nhận đã bật chưa, giữ bao nhiêu ngày, và lấy ra bằng cách nào (Admin REST API hay đẩy sang bảng riêng) | Gate 2 — Dev |
| **OQ-18** | **Bảng tiến độ có `created_at`/`updated_at` không?** Cần cho khả năng tính bù điểm (§13.2) và cho việc chống cộng trùng theo thời gian. Swagger không khai DTO của bảng tiến độ; sơ đồ DB chỉ có PK/FK | Gate 2 — Dev |

---

## Trạng thái

- [x] OQ-01 · [x] OQ-02 · [x] OQ-03 · [x] OQ-04 · [x] OQ-06 · [x] OQ-08 · [x] OQ-09 · [x] OQ-10 — **đã chốt**
- [ ] **OQ-07** · [ ] **OQ-16** — **blocking, đang chờ**
- [ ] OQ-05 · [ ] OQ-11 · [ ] OQ-12 · [ ] OQ-13 · [ ] OQ-14 · [ ] OQ-15 · [ ] OQ-17 · [ ] OQ-18 — không chặn

**Chốt xong OQ-07 và OQ-16 là chạy `/generate-brd`.**
