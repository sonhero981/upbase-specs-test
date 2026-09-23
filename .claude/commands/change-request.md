# Change Request – Đổi yêu cầu giữa chừng

Dùng khi yêu cầu **thay đổi hoặc bổ sung sau khi đã có tài liệu** (BRD / Impact Matrix / Solution / PRD), cần cập nhật tài liệu cũ thay vì làm lại từ đầu.

**Tự kích hoạt** khi người dùng nói: *"tôi có thay đổi yêu cầu…"*, *"bổ sung yêu cầu…"*, *"đổi scope…"*, *"thêm một rule…"*, *"khách yêu cầu thêm…"*. Gõ `/change-request` cũng được.

Input: mô tả thay đổi — `$ARGUMENTS`

> **Xác định project:** ưu tiên `$ARGUMENTS`; không có → suy từ file đang mở; >1 khả dĩ → liệt kê cho chọn, **không đoán**. **Echo + confirm trước khi chạy** — đặc biệt quan trọng khi làm nhiều project song song.

---

## CR-1. Ghi nhận thay đổi

Ghi vào `working/raw-inputs/change-requests.md` (tạo nếu chưa có):

| CR ID | Ngày | Nội dung thay đổi | Lý do / Nguồn | Trạng thái |
| --- | --- | --- | --- | --- |
| CR-001 | YYYY-MM-DD | | | `Đang xử lý` / `Đã áp dụng` |

Mỗi thay đổi một dòng, đánh số CR-001, CR-002…

---

## CR-2. Đề xuất điểm re-entry

Map thay đổi vào bảng, lấy **tầng thấp nhất** nếu chạm nhiều tầng:

| Loại thay đổi | Re-entry từ | Cascade ảnh hưởng |
| --- | --- | --- |
| Vấn đề / mục tiêu / phạm vi / business rule mức nghiệp vụ | **BRD** (Bước 4) | Impact → Solution → PRD |
| Phát hiện ảnh hưởng mới, bổ sung context hệ thống | **Impact Matrix** (Bước 6) | Solution → PRD |
| Đổi hướng giải pháp, thêm option | **Solution** (Bước 8) | PRD |
| Đổi chi tiết chức năng (US / field / rule / màn) | **PRD** (Bước 9) | Chỉ phần bị chạm |
| Chỉ đổi User Guide | **User Guide** | — |

**Nguyên tắc chọn tầng:** hỏi *"thay đổi này làm sai lệch kết luận của tầng nào?"* — tầng đó là điểm re-entry.

*Ví dụ: "thêm rule học viên bị Block thì không nộp được bài" → chạm business rule → nhưng rule này có làm sai Impact Matrix không? Có, vì nó thêm một nhánh xử lý chưa được quét. → re-entry từ Impact Matrix, không phải chỉ sửa PRD.*

---

## CR-3. Confirm trước khi chạy — BẮT BUỘC

Trình bày:

- **Điểm re-entry đề xuất** + lý do
- **Danh sách tài liệu sẽ bị cập nhật** (impact preview)
- **Gate nào phải duyệt lại** — mọi Gate sau điểm re-entry

> **Không chạy lại khi người dùng chưa confirm điểm re-entry.** Muốn điểm khác → theo người dùng.

---

## CR-4. Chạy lại xuôi — Update mode

Với mỗi tài liệu từ điểm re-entry trở đi:

- **Chỉ sửa phần bị ảnh hưởng.** Phần không liên quan giữ nguyên — không regenerate toàn bộ
- **Bump MINOR:** `v0.X` → `v0.(X+1)` trên cùng file
- Thêm dòng vào **Document version** ở đầu tài liệu:

  | Version | Người cập nhật | Nội dung | Impact | Ngày cập nhật |
  | --- | --- | --- | --- | --- |
  | v0.2 | | *tóm tắt thay đổi* | `CR-001` | |

- **PRD:** chỉ chạm US bị ảnh hưởng. US khác không động vào. Cập nhật `Document version` và mục `Vấn đề tồn đọng` nếu có
- **Mọi Gate sau điểm re-entry** chuyển về trạng thái chờ duyệt lại

Lệnh tương ứng theo điểm re-entry:

| Re-entry | Lệnh |
|---|---|
| BRD | `/generate-brd` |
| Impact Matrix | `/impact-analysis` |
| Solution | `/compare-solutions` |
| PRD | `/generate-prd` |
| User Guide | `/generate-user-guide` |

---

## CR-5. Kiểm tra tác động ngược

Sau khi cập nhật, kiểm ba thứ hay bị bỏ sót:

| Kiểm | Vì sao |
|---|---|
| **Business rule bị mồ côi** | Rule cũ còn được US nào dùng không, hay đã thành rule chết |
| **Mã tham chiếu gãy** | `BR-2.3` bị xoá mà chỗ khác còn trỏ tới |
| **Out of scope lỗi thời** | Thứ từng ghi "không làm" nay đã làm, hoặc ngược lại |

---

## Output

Tóm tắt cho người dùng:

- **CR đã ghi nhận** — ID + nội dung
- **Điểm re-entry** đã chạy lại từ đâu
- **Tài liệu đã cập nhật** — file nào, bump lên version nào, đổi gì
- **Gate cần duyệt lại** trước khi chốt
- **Tác động ngược** phát hiện được (nếu có)

Tự kiểm theo `.claude/checklist/change-request.md` trước khi trình bày.
