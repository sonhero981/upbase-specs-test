---
intent: 261005-group
phase: ideation
date: 2026-10-12
result: Không đạt
---
# Phase check: IDEATION · 261005-group

Kiểm trên `ideation/brd.md` v0.2, artifact luồng v1 thay cho intent-statement, scope-document và initiative-brief. Chạy ngày 12/10/2026 khi trình lại gate 1.1 · 1.4 · 1.7 theo nghi thức v2. Proto-Unit lấy từ bảng Unit `U1` đến `U7` trong `inception/prd/prd.md`, vì BRD không có bảng này.

## Ideation sang Inception, kiểm ở 1.7
| # | Điều kiện | Kết quả | Chi tiết |
|---|---|---|---|
| 1 | Mọi objective trong intent-statement có ít nhất một hạng mục In scope phục vụ | Đạt | `O1` giao nội dung cho tập người ổn định → In scope *Gán nội dung*, `US7` · `O2` người mới tự nhận → *Công tắc tự ghi danh*, `US8` · `O3` quản lý xem người mình phụ trách → *Quan hệ quản lý*, *Phạm vi dữ liệu*, `US16` · `O4` cộng dồn theo cơ cấu → *Báo cáo theo nhóm*, `US18` · `O5` dựng lại quá khứ → *Thành viên theo thời gian*, `C3`, `US15` |
| 2 | Mọi Proto-Unit truy về một objective | Đạt có điều kiện | `U3` giao nội dung → `O1` `O2` · `U5` phạm vi và hiển thị → `O3` · `U7` nền tảng → `O4` `O5`. `U1` khung nhóm, `U2` đồng bộ, `U4` quan hệ người, `U6` vòng đời nhân sự là hạng mục nền, truy về objective qua Unit phụ thuộc chúng. Điều kiện: bảng Proto-Unit nằm ở PRD, không nằm ở BRD; BRD không có cột MoSCoW |
| 3 | Out of scope không mâu thuẫn In scope | Đạt | Bốn cặp dễ nhầm đã soát: *Nhóm chứa nội dung* (Out) với *Gán nội dung* (In): gán là luật đứng dẫn vào Lớp, nhóm không chứa gì · *Chia dữ liệu học theo nhánh* (Out) với *Phạm vi dữ liệu* (In): một bên chia dữ liệu của một người, một bên giới hạn tập người, hai trục khác nhau · *Xoá nhóm đã có lịch sử* (Out) với *Lưu trữ, chỉ xoá nhóm chưa có lịch sử* (In): nhất quán · *Nhóm động* (Out) với *Nguồn nhóm: đồng bộ và tự tạo* (In): nhất quán |
| 4 | Câu hỏi mở có cờ Chặn đã đóng, hoặc chuyển thành assumption có lý do | Đạt | §10: `OQ-21` đến `OQ-24` đóng 06/10; `OQ-07` `OQ-08` `OQ-09` đóng 05/10; `BA-01` đến `BA-07` đóng 05/10. `state.md`: 0 câu chặn, CR1 đóng 09/10 |
| 5 | Mọi khối khẳng định có thẻ nguồn | Không đạt | BRD v1 không dùng thẻ `[desc]` `[Qn]` `[KB-..]` `[assumption]`. Nguồn ghi theo cách v1: *"PO chốt ngày …"*, mã `OQ-xx` `BA-xx` `CF-x`, cột *Nguồn* ở §7 trỏ hạng mục yêu cầu gốc. Truy vết được về `decisions.md`, nhưng không theo định dạng v2 |

## Lệch so với phạm vi hiện tại, ngoài năm điều kiện trên
BRD v0.2 ngày 06/10 chưa được cập nhật sau CR1 ngày 09/10 (DEC73 đến DEC77), trong khi requirements, impact-matrix và prd đã cập nhật:
- §7 xếp `US16` màn theo dõi nhánh vào *Phía quản lý và học viên — UpLMS*. DEC73 chốt màn này ở **UpLMS Ops** (`BR-16.7`)
- §5 In scope ghi *"Một mail event mới"*. Từ DEC74 có hai: `MAIL-GRP-01` và `MAIL-GRP-02` (báo người được gán quản lý). `RC-20` không có trong BRD
- §8 mở đầu *"Chưa chạy Impact Analysis"*, trong khi impact-matrix đã v0.3
- §2, §10, §11 còn đường dẫn luồng v1 (`working/raw-inputs/…`, `project-decisions.md`, `.claude/projects/Gamification/`)

## Kết luận
Về nội dung, ranh giới Ideation sang Inception đã đủ: mọi objective có hạng mục, Out không đánh In, không còn câu chặn. Hai điều kiện không đạt là điều kiện **định dạng v2** áp lên một artifact v1 đã duyệt: thẻ nguồn và bảng Proto-Unit trong BRD. Sửa cho đạt đồng nghĩa viết lại BRD, điều PO đã không chọn khi chuyển luồng ngày 09/10.

Stage phải sửa nếu PO không chấp nhận rủi ro: 1.4 (thêm bảng Proto-Unit hoặc trỏ sang bảng Unit của PRD) và 1.1 · 1.4 (thẻ nguồn). Phần lệch sau CR1 sửa được tại chỗ ở 1.4 và 1.7 mà không viết lại: bốn chỗ nêu trên. Quyết định ở gate.
