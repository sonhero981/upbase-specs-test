# Checklist: Generate BRD

## Tiền điều kiện
- [ ] **[BLOCK]** Không còn blocking question trong `open-questions-*.md`
- [ ] Đã đọc clarified requirements bản mới nhất

## Ranh giới nội dung
- [ ] **[BLOCK]** KHÔNG chứa: chi tiết màn hình · danh sách field · validate · expected behavior từng thao tác · state machine · API flow · cấu trúc bảng
- [ ] **[BLOCK]** Thông tin chưa rõ → `Open Question`. **Không** viết placeholder vào nội dung
- [ ] Nguyên tắc "cái gì phải đúng, không phải làm thế nào" được giữ

## Nội dung
- [ ] `Problem` viết theo góc nhìn người dùng: ai gặp · khi nào · hậu quả gì
- [ ] `Problem` **không** mô tả giải pháp
- [ ] `Analytics` có dữ liệu, **hoặc** ghi rõ `Chưa có dữ liệu định lượng` + căn cứ định tính — không bỏ trống
- [ ] `Objective` là **kết quả**, không phải danh sách việc làm
- [ ] Scope tách đủ In / Out / Potential
- [ ] `Solution (khung)` chưa đi vào màn hình/field
- [ ] Nhiều hướng → nêu đánh đổi, ghi `Recommendation`, **không tự chốt**

## Danh sách US
- [ ] Mỗi US = **một mục tiêu hoàn chỉnh của người dùng**
- [ ] Không chia US theo màn hình, không chia theo business rule
- [ ] Đánh số `US1`, `US2`… liên tục
- [ ] Mỗi US ghi **nguồn** — yêu cầu nào sinh ra nó

## Phần còn lại
- [ ] `Tác động tới hệ thống` — chưa chạy Impact Analysis thì ghi `Chưa phân tích`, **không đoán**
- [ ] `Assumptions` mỗi dòng kiểm chứng được
- [ ] `Open Questions` có owner + cờ blocking
- [ ] `References` ghi rõ **file KB nào** đã đọc

## Delivery
- [ ] **[BLOCK]** Người dùng **đã xem bản trước chưa?** Rồi → **tạo file version mới**, giữ nguyên bản cũ, thêm mục **Lịch sử thay đổi**. Chưa → sửa tại chỗ được.
      > Mốc tăng version là **mỗi lần qua Gate** hoặc mỗi đợt người dùng trả lời một loạt câu hỏi. Làm liên tục trong một phiên thì rất dễ quên — xem `CLAUDE.md` mục *Cách làm việc*.
- [ ] Đúng thư mục `docs/brd/`, đúng version
- [ ] Còn assumption lớn → đánh dấu `Draft - Pending Confirmation`
- [ ] Đã chuẩn bị nội dung trình Gate 1

## Danh sách US
- [ ] **Define hết US**, kể cả cái chưa làm ngay — không tự giới hạn theo sức một đợt
- [ ] US chưa làm → vẫn viết đủ, ghi rõ trong tiêu đề (`US5: … — chưa làm`)
