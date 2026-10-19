---
intent: 261005-group
artifact: traceability
version: 0.1
date: 2026-10-12
note: Làm tay ở gate 2.4 ngày 12/10/2026. Intent dùng họ mã v1 (RC thay FR), script po-tools.py trace không áp dụng
---
# Traceability: Nhóm học viên (Group)

Trạng thái: OK có đích · GAP chưa có · ORPHAN không truy về đâu · Deferred để đợt sau, ghi rõ · N/A không áp dụng, ghi lý do.

## RC sang US
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

## US sang RC
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

## Kết luận
Đạt. 0 GAP, 0 ORPHAN. Ghi chú để xử lý ở CR kế tiếp, không chặn: thêm ba dòng RC cho báo cáo cộng dồn theo nhóm (`US18`), tự gỡ khoá chưa học khi rời nhóm (`US19`), báo quản lý khi rời nhóm còn nghĩa vụ học (`US20`) để bảng yêu cầu khớp với 20 US. Ngày kiểm: 12/10/2026.
