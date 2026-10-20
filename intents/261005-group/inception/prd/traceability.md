---
intent: 261005-group
artifact: traceability
version: 0.2
date: 2026-10-20
note: Bảng RC làm tay ở gate 2.4 ngày 12/10/2026, vì intent dùng họ mã v1 (RC thay FR). Bảng BR sang AC lấy từ po-tools.py trace ngày 20/10/2026, CR3
---
# Traceability: Nhóm học viên (Group)

Trạng thái: OK có đích · GAP chưa có · ORPHAN không truy về đâu · Deferred để đợt sau, ghi rõ · N/A không áp dụng, ghi lý do.

## FR sang US
Intent này dùng mã `RC` của bản làm rõ yêu cầu thay cho `FR`.

| RC | US | Trạng thái | Ghi chú |
|---|---|---|---|
| `RC-01` cây nhóm nhiều cấp, mã tên mô tả nhóm cha | `US1` | OK | `BR-1.1` đến `BR-1.6` |
| `RC-02` quan hệ nhiều-nhiều, nhiều cây gốc | `US1` · `US3` · `US19` | OK | Nhiều cây gốc ở `US1`; một người nhiều nhóm `BR-3.1`; nhiều nhóm cùng giao một lớp `BR-3.7` `BR-19.7` (CR2) |
| `RC-03` phân loại theo nguồn, nguồn quyết quyền sửa | `US5` | OK | `BR-5.5` |
| `RC-04` tạo, sửa, di chuyển; nhánh con đi theo; quản lý tính lại | `US1` · `US2` · `US10` | OK | Di chuyển `BR-2.4`; quản lý tính động `BR-10.5` |
| `RC-05` thêm gỡ thủ công có tìm kiếm | `US3` | OK | |
| `RC-06` thêm gỡ theo lô bằng tệp | `US4` | OK | |
| `RC-07` nhóm cha bao trùm nhánh con ở mọi màn đọc | `US5` · `US6` · `US9` · `US16` · `US18` | OK | Rule nền, phủ bằng `BR-5.3` · `BR-6.2` · `BR-9.3` · `BR-16.1` · `BR-18.3` |
| `RC-08` gán nội dung, chảy xuống nhánh con, mặc định tắt | `US7` | OK | |
| `RC-09` người vào sau tự nhận nội dung, toàn bộ hay chỉ còn hiệu lực | `US8` | OK | `BR-8.3` chọn ghi danh luôn người đang thiếu hay chỉ từ giờ |
| `RC-10` danh sách cây hoặc bảng, bộ lọc | `US6` | OK | |
| `RC-11` nhật ký dựng lại được quá khứ | `US15` · `US18` | OK | Nhật ký `US15`; báo cáo theo mốc `BR-18.1` |
| `RC-12` lưu trữ, xoá nhóm | `US14` | OK | Xoá chỉ với nhóm chưa có lịch sử, `BR-14.1` |
| `RC-13` một hoặc nhiều quản lý, là người dùng | `US9` | OK | |
| `RC-14` quản lý suy ra theo cây, tính động | `US10` | OK | |
| `RC-15` chỉ định đích danh trên hồ sơ, ghi đè kết quả suy ra | `US11` | OK, đổi nghĩa | PRD theo `F-07`: quản lý chính **đứng cao nhất**, không ghi đè và không đổi phạm vi dữ liệu, `BR-11.2` `BR-11.3` |
| `RC-16` quản lý đọc nhánh mình; chọn ở `ORG.ROL.04` | `US16` | OK, một phần Deferred | Đọc nhánh mình `BR-16.1` `BR-16.4`. Phạm vi nhiều mức của `ORG.ROL.04` đưa ra Out of scope theo `OQ-18` |
| `RC-17` trang người học hiện quản lý và liên hệ | `US17` | OK | |
| `RC-18` quản lý bị khoá hoặc rời thì cảnh báo, chuyển quan hệ | `US13` | OK | |
| `RC-19` loại quan hệ mentor, dùng chung cơ chế gán và phạm vi dữ liệu | `US12` | OK, đổi nghĩa | Theo `CF-6` mentor không có phạm vi dữ liệu riêng; đi theo nhóm vào lớp, `BR-12.1` đến `BR-12.6` |
| `RC-20` báo email người được gán quản lý | `US9` · `US11` · `US13` | OK | `BR-9.6` `BR-9.7` `BR-11.7` `BR-13.6` `BR-13.7`, mail `MAIL-GRP-02` |

Không có GAP: 20 trên 20 RC có US.

## US sang FR
| US | RC | Trạng thái |
|---|---|---|
| `US1` | `RC-01` · `RC-02` · `RC-04` | OK |
| `US2` | `RC-04` | OK |
| `US3` | `RC-02` · `RC-05` | OK |
| `US4` | `RC-06` | OK |
| `US5` | `RC-03` · `RC-07` | OK |
| `US6` | `RC-07` · `RC-10` | OK |
| `US7` | `RC-08` | OK |
| `US8` | `RC-09` | OK |
| `US9` | `RC-07` · `RC-13` · `RC-20` | OK |
| `US10` | `RC-04` · `RC-14` | OK |
| `US11` | `RC-15` · `RC-20` | OK |
| `US12` | `RC-19` | OK |
| `US13` | `RC-18` · `RC-20` | OK |
| `US14` | `RC-12` | OK |
| `US15` | `RC-11` | OK |
| `US16` | `RC-07` · `RC-16` | OK |
| `US17` | `RC-17` | OK |
| `US18` | `RC-07` · `RC-11` một phần | OK qua `O4` · `BA-05a`. Không có RC riêng cho báo cáo cộng dồn |
| `US19` | — | OK qua `OQ-22` · `OQ-23` · `OQ-37`. Không có RC |
| `US20` | — | OK qua `OQ-22` · `OQ-38` · `MAIL-GRP-01`. Không có RC |

Ba US cuối truy về objective và quyết định ở Bước 5, Bước 7 của v1, không truy về bảng RC vì bảng đó chỉ được bổ sung một lần ở CR1 (`RC-20`). Không phải ORPHAN về phạm vi; là chỗ bảng yêu cầu chưa theo kịp quyết định.

## BR sang US
Mã business rule mang số US (`BR-<US>.<n>`), nên gắn vào US theo mã. Kiểm bằng máy ngày 12/10/2026 sau CR2: 130 BR định nghĩa trong 20 US, mọi mã trỏ tới US có thật, không BR nào được nhắc mà không định nghĩa.

## BR sang AC
CR3 ngày 20/10/2026 thêm 104 tiêu chí chấp nhận cho 20 user story. Mỗi business rule có ít nhất một tiêu chí kiểm nó. Các tiêu chí không gắn business rule kiểm validate của bảng giao diện hoặc nội dung email, ví dụ `AC1.3` · `AC6.5` · `AC20.4`.

| BR | AC | Trạng thái |
|---|---|---|
| `BR-1.1` | `AC1.2` | OK |
| `BR-1.2` | `AC1.4` | OK |
| `BR-1.3` | `AC1.5` | OK |
| `BR-1.4` | `AC1.5` | OK |
| `BR-1.5` | `AC1.6` | OK |
| `BR-1.6` | `AC1.1` | OK |
| `BR-2.1` | `AC2.2` | OK |
| `BR-2.2` | `AC2.3` | OK |
| `BR-2.3` | `AC2.4` | OK |
| `BR-2.4` | `AC2.5` | OK |
| `BR-2.5` | `AC2.5` | OK |
| `BR-2.6` | `AC2.6` | OK |
| `BR-3.1` | `AC3.1` | OK |
| `BR-3.2` | `AC3.2` | OK |
| `BR-3.3` | `AC3.3` | OK |
| `BR-3.4` | `AC3.4` | OK |
| `BR-3.5` | `AC3.6` | OK |
| `BR-3.6` | `AC3.5` | OK |
| `BR-3.7` | `AC3.5` | OK |
| `BR-4.1` | `AC4.2` | OK |
| `BR-4.2` | `AC4.3` | OK |
| `BR-4.3` | `AC4.4` | OK |
| `BR-4.4` | `AC4.5` | OK |
| `BR-4.5` | `AC4.6` | OK |
| `BR-5.1` | `AC5.1` | OK |
| `BR-5.2` | `AC5.2` | OK |
| `BR-5.3` | `AC5.3` | OK |
| `BR-5.4` | `AC5.2` | OK |
| `BR-5.5` | `AC5.4` | OK |
| `BR-5.6` | `AC5.4` | OK |
| `BR-5.7` | `AC5.5` | OK |
| `BR-5.8` | `AC5.5` | OK |
| `BR-5.9` | `AC5.1` | OK |
| `BR-5.10` | `AC5.6` | OK |
| `BR-6.1` | `AC6.1` | OK |
| `BR-6.2` | `AC6.2` | OK |
| `BR-6.3` | `AC6.2` | OK |
| `BR-6.4` | `AC6.3` | OK |
| `BR-6.5` | `AC6.4` | OK |
| `BR-7.1` | `AC7.1` | OK |
| `BR-7.2` | `AC7.2` | OK |
| `BR-7.3` | `AC7.3` | OK |
| `BR-7.4` | `AC7.2` · `AC7.4` | OK |
| `BR-7.5` | `AC7.4` | OK |
| `BR-7.6` | `AC7.5` | OK |
| `BR-7.7` | `AC7.5` | OK |
| `BR-7.8` | `AC7.4` | OK |
| `BR-7.9` | `AC7.3` | OK |
| `BR-7.10` | `AC7.6` | OK |
| `BR-7.11` | `AC7.1` | OK |
| `BR-8.1` | `AC8.1` | OK |
| `BR-8.2` | `AC8.3` | OK |
| `BR-8.3` | `AC8.2` | OK |
| `BR-8.4` | `AC8.4` | OK |
| `BR-8.5` | `AC8.5` | OK |
| `BR-9.1` | `AC9.1` | OK |
| `BR-9.2` | `AC9.1` | OK |
| `BR-9.3` | `AC9.3` | OK |
| `BR-9.4` | `AC9.4` | OK |
| `BR-9.5` | `AC9.4` | OK |
| `BR-9.6` | `AC9.5` | OK |
| `BR-9.7` | `AC9.5` | OK |
| `BR-10.1` | `AC10.1` | OK |
| `BR-10.2` | `AC10.2` | OK |
| `BR-10.3` | `AC10.3` | OK |
| `BR-10.4` | `AC10.3` | OK |
| `BR-10.5` | `AC10.4` | OK |
| `BR-11.1` | `AC11.1` | OK |
| `BR-11.2` | `AC11.2` | OK |
| `BR-11.3` | `AC11.3` | OK |
| `BR-11.4` | `AC11.2` | OK |
| `BR-11.5` | `AC11.4` | OK |
| `BR-11.6` | `AC11.4` | OK |
| `BR-11.7` | `AC11.5` | OK |
| `BR-12.1` | `AC12.1` | OK |
| `BR-12.2` | `AC12.2` | OK |
| `BR-12.3` | `AC12.2` | OK |
| `BR-12.4` | `AC12.3` | OK |
| `BR-12.5` | `AC12.4` | OK |
| `BR-12.6` | `AC12.4` | OK |
| `BR-13.1` | `AC13.1` | OK |
| `BR-13.2` | `AC13.2` | OK |
| `BR-13.3` | `AC13.3` | OK |
| `BR-13.4` | `AC13.3` | OK |
| `BR-13.5` | `AC13.4` | OK |
| `BR-13.6` | `AC13.5` | OK |
| `BR-13.7` | `AC13.5` | OK |
| `BR-14.1` | `AC14.1` | OK |
| `BR-14.2` | `AC14.1` | OK |
| `BR-14.3` | `AC14.3` | OK |
| `BR-14.4` | `AC14.3` | OK |
| `BR-14.5` | `AC14.4` | OK |
| `BR-14.6` | `AC14.2` | OK |
| `BR-14.7` | `AC14.4` | OK |
| `BR-15.1` | `AC15.2` | OK |
| `BR-15.2` | `AC15.1` | OK |
| `BR-15.3` | `AC15.3` | OK |
| `BR-15.4` | `AC15.4` | OK |
| `BR-16.1` | `AC16.1` | OK |
| `BR-16.2` | `AC16.2` | OK |
| `BR-16.3` | `AC16.2` | OK |
| `BR-16.4` | `AC16.3` | OK |
| `BR-16.5` | `AC16.4` | OK |
| `BR-16.6` | `AC16.4` | OK |
| `BR-16.7` | `AC16.1` | OK |
| `BR-17.1` | `AC17.3` | OK |
| `BR-17.2` | `AC17.2` | OK |
| `BR-17.3` | `AC17.1` | OK |
| `BR-17.4` | `AC17.3` | OK |
| `BR-18.1` | `AC18.3` | OK |
| `BR-18.2` | `AC18.3` | OK |
| `BR-18.3` | `AC18.2` | OK |
| `BR-18.4` | `AC18.4` | OK |
| `BR-18.5` | `AC18.4` | OK |
| `BR-18.6` | `AC18.5` | OK |
| `BR-18.7` | `AC18.6` | OK |
| `BR-19.1` | `AC19.1` | OK |
| `BR-19.2` | `AC19.1` | OK |
| `BR-19.3` | `AC19.2` | OK |
| `BR-19.4` | `AC19.4` | OK |
| `BR-19.5` | `AC19.3` | OK |
| `BR-19.6` | `AC19.1` | OK |
| `BR-19.7` | `AC19.5` | OK |
| `BR-20.1` | `AC20.1` | OK |
| `BR-20.2` | `AC20.2` | OK |
| `BR-20.3` | `AC20.2` | OK |
| `BR-20.4` | `AC20.2` | OK |
| `BR-20.5` | `AC20.3` | OK |
| `BR-20.6` | `AC20.1` | OK |
| `BR-20.7` | `AC20.1` | OK |

## Kết luận
Đạt. 0 GAP, 0 ORPHAN ở cả lớp RC sang US và lớp BR sang AC (130 BR, 104 AC, kiểm lại ngày 20/10/2026). Ghi chú để xử lý ở CR kế tiếp, không chặn: thêm ba dòng RC cho báo cáo cộng dồn theo nhóm (`US18`), tự gỡ khoá chưa học khi rời nhóm (`US19`), báo quản lý khi rời nhóm còn nghĩa vụ học (`US20`) để bảng yêu cầu khớp với 20 US. Ngày kiểm: 12/10/2026.
