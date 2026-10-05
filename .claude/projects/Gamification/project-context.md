# Project Context

**Project:** Gamification
**Ngày tạo:** 23/09/2026 · **Cập nhật:** 05/10/2026, sau khi học từ AI-DLC
**Trạng thái:** 🔄 **PRD v0.5** mang `CR-009`, `CR-010` và design đã chốt. Chờ PO review lại từ đầu
**Cỡ yêu cầu:** **L** — đủ 9 bước, đủ 4 Gate

> ⚠️ **File này đã được viết lại toàn bộ sau `CR-007`.** Bản trước viết ở Bước 2 và lệch khá xa sau bảy change request. Nếu thấy mâu thuẫn với tài liệu khác, tin file này và `change-requests.md`.

---

## Background

Hệ thống UpLnD đã có khoá học và học viên đang vận hành. Số liệu General Launch 8/9–21/9/2026 cho thấy vấn đề ở ba tầng:

| Tầng | Số đo | |
|---|---|---|
| Không mở ứng dụng | Activation **40.2%** (53/132) | tiêu chí 80% |
| Mở rồi không học | **45%** người đăng nhập vẫn không bắt đầu (53 vào, 29 bắt đầu) | — |
| Bắt đầu rồi bỏ dở | Completion **64.1%** (93/145) | tiêu chí 80% |

## Objectives

| # | |
|---|---|
| O1 | Học viên quay lại học đều đặn hơn, không cần vận hành nhắc thủ công |
| O2 | Nỗ lực học được ghi nhận ngay lúc nó xảy ra |
| O3 | Học viên có mốc ngắn hạn để nhắm tới |
| O4 | Đội truyền thông nội bộ chọn được khoảng ngày bất kỳ để lấy số liệu công bố |
| O5 | Điểm số đáng tin, mỗi con số truy được nguồn, không bị thổi lên bằng thao tác đối phó |

> ⚠️ **Mã mục tiêu đã đánh số lại 24/09.** `CR-007` bỏ mục tiêu *"kết quả mỗi kỳ không đổi về sau"* (mã cũ `O5`), nên *"điểm số đáng tin"* từ `O6` **đổi thành `O5`**. `project-decisions.md` giữ mã cũ vì là nhật ký lịch sử — đọc chéo hai file thì để ý chỗ này.

## Scope

### In scope — 15 US

| Nhóm | Nội dung |
|---|---|
| **Cơ chế điểm** | Khai hành động nào được bao nhiêu điểm, bật/tắt từng hành động |
| **Ba hành động học** | Hoàn thành hoạt động · hoàn thành khoá · hoàn thành bài Test theo `BR-TEST` |
| **Vào hệ thống hằng ngày** | Mỗi ngày vào hệ thống được điểm một lần. **Điểm tăng dần theo chuỗi ngày liên tiếp** (`CR-009`): điểm nền, bước tăng, trần. Bỏ trọn một ngày thì chuỗi về `0`, đếm mọi ngày dương lịch nên nghỉ cuối tuần cũng đứt |
| **Huy hiệu** | Bốn loại đo bằng chỉ số đếm: Tích cực (số ngày có mặt) · Học tập (số hoạt động) · Test (số bài Test) · Course (số khoá).<br>**Mốc khoá sau khi tạo. Không có thao tác xoá huy hiệu.** Huy hiệu đã nhận không bị lấy lại bởi việc đổi cấu hình |
| **Bật/tắt huy hiệu** | Tắt được **cả chức năng huy hiệu**, và tắt được **từng huy hiệu riêng**. Tắt thì không hiện nữa nhưng **dữ liệu giữ nguyên**, bật lại là hiện lại đầy đủ |
| **Hạng** | Ngưỡng theo ba chỉ số: điểm · huy hiệu · số khoá. **Mỗi mốc chạm được ở bất kỳ tiêu chí nào đều cho một hạng**, không phải lấy tiêu chí cao nhất. Hạng **không tụt** |
| **Chống cày điểm** | Chống cộng trùng nội dung đã hoàn thành trong một lượt ghi danh. **Không có trần điểm ngày** (`CR-010`) |
| **Lịch sử ghi nhận** | `Achievement history` — panel trượt từ phải. Ba loại sự kiện: điểm, huy hiệu, lên hạng. **Giữ toàn bộ, không dọn** |
| **Thông báo thành tích** | Chỉ đẩy trong hệ thống khi học viên đang online. Không gửi mail, không gộp |
| **Trang Thành tích của tôi** | Điểm · hạng · toàn bộ huy hiệu kèm mốc và tiến độ |
| **Bảng xếp hạng** | **Bộ chọn khoảng ngày tự do** · bốn chỉ số · top 3 nổi bật · danh sách đầy đủ · vị trí của tôi |
| **Tra cứu bên Ops** | Danh sách học viên kèm điểm, hạng, huy hiệu; chọn khoảng ngày rồi xuất Excel |
| **Hai công tắc** | `Gamification` và `Visibility in UpLMS` |
| **Múi giờ tổ chức** | Tham số mới trên bảng `tenant` |
| **Phân quyền** | Vai trò vận hành nào sửa được cấu hình |

### Out of scope

| | Vì sao |
|---|---|
| **Chiến dịch · kỳ lịch như thực thể riêng · chốt kỳ · snapshot** | Bỏ theo `CR-007`. Bộ chọn khoảng ngày bao trùm |
| **Bộ lọc bảng xếp hạng theo nhóm, lớp, phòng ban** | Chờ chức năng nhóm đồng bộ từ HRM |
| **Tính điểm từ Quiz, Case Study, Storyline** | PO chốt không tính |
| **Lộ trình học · Khung năng lực** | Tính năng riêng, làm sau |
| **Hành động "đạt điểm cao"** | PO chốt tạm thời không có rule |
| **Sửa logic hoàn thành Activity** | Giữ nguyên |
| **Phần thưởng vật chất** · **Gamification cho nhân sự Ops** · **Thi đua theo đội** | Chưa yêu cầu |

## Stakeholders

| Vai trò | Ghi chú |
|---|---|
| PO | Bùi Đức Huy — chủ tài liệu |
| **Học viên (UpLMS)** | Nhận điểm, huy hiệu, hạng; xem thành tích và bảng xếp hạng |
| **Nhân sự vận hành (Ops)** | Cấu hình bảng điểm, huy hiệu, ngưỡng hạng, bật/tắt |
| **Đội truyền thông nội bộ** | Chọn khoảng ngày lấy số liệu, công bố và trao thưởng ngoài hệ thống |
| **L&D** | Đánh giá mức độ tham gia ở quy mô tổ chức |
| **Quản lý trực tiếp** | ⚠️ **Chưa có công cụ riêng ở đợt này** — cần `US14` (hoãn) |
| Dev | Xác nhận `OQ-30` tải bảng xếp hạng · `OQ-21` endpoint đếm chứng chỉ |
| QA | Điền `Conner case` trong PRD |

## Phạm vi sản phẩm

- **UpLMS** — trang thành tích, lịch sử, bảng xếp hạng, thông báo. **My Learning bị sửa** để hiện điểm và hạng
- **UpLMS Ops** — cấu hình điểm, huy hiệu, hạng, hai công tắc, phân quyền

**Module bị chạm:** Learning Experience · Course · Assessment · Grading · Certificate · User · Class · Phân quyền · Tenant

## Ràng buộc

| # | Ràng buộc |
|---|---|
| `C1` | Cấu hình gắn `tenant_id`, không hardcode |
| `C2` | Mọi danh mục mở rộng được bằng cấu hình |
| `C3` | Lưu **từng lần cộng điểm kèm thời điểm**, không chỉ lưu tổng |
| `C4` | Đổi cấu hình → **áp dụng từ thời điểm đổi**, không tính lại quá khứ. Áp cho cả điểm, huy hiệu và hạng |
| `C5` | Chống cộng trùng trong phạm vi **một lượt ghi danh**. Chỉ cộng điểm khi bản ghi tiến độ **chuyển trạng thái** sang hoàn thành |
| `C6` · `C9` | Biên ngày và biên khoảng cắt theo **múi giờ tổ chức** |
| `C7` | Một lần cộng điểm thuộc **mọi khoảng ngày bao trùm nó** |
| `C8` | Mọi mốc dùng để xếp hạng phải lưu **thời điểm đạt** |
| `C10` | **`Test Account` bị loại khỏi toàn bộ logic gamification** |
| `NFR-GAM-01` | Lỗi ở gamification **không được làm hỏng thao tác học** |

> **Ba cơ chế cùng một luật:** điểm, huy hiệu và hạng đều chỉ áp thay đổi từ thời điểm đổi trở đi, và **không có gì bị lấy lại** khỏi học viên.
>
> Huy hiệu chỉ **không còn hiện** trong hai trường hợp, và cả hai đều không phải mất dữ liệu: vận hành tắt chức năng hoặc tắt riêng huy hiệu đó, và học viên rời tổ chức.

## Quyết định giải pháp

| | |
|---|---|
| Cách bắt sự kiện | **Tính trong luồng** — cộng điểm ngay trong thao tác hoàn thành, độ trễ bằng 0 |
| Bảng xếp hạng | Tính sẵn theo chu kỳ **8 tiếng**, ba lần một ngày |
| Check-in | Ghi ngay lúc học viên vào hệ thống lần đầu trong ngày |

## Key References

| Loại | Nguồn |
|---|---|
| Yêu cầu gốc | `working/raw-inputs/yeu-cau-goc-20260923.md` |
| **Change requests** | `working/raw-inputs/change-requests.md` — **CR-001 đến CR-010** |
| BRD | `docs/brd/brd-v0.6-20260923.md` — ⚠️ có dấu CR-007 ở đầu, một số mục hết hiệu lực |
| Impact Matrix | `working/impact-analysis/impact-matrix-v0.2-20260923.md` — ⚠️ tương tự |
| Solution | `working/solution-options/solution-comparison-v0.1-20260923.md` — ⚠️ tương tự |
| **PRD** | `docs/prd/prd-gamification-v0.8-20261005.md` — **trạng thái đúng nhất**, đang mang `CR-009` |
| Quyết định | `project-decisions.md` |
| KB chính | `03-assessment.md` (`BR-TEST`) · `06-user-account.md` §8b (`Test Account`) · `07-learning-experience.md` · `12-data-model.md` · `14-api-surface.md` · `15-product-direction.md` |
| Schema DB | [Lark → Data Architecture](https://upbasevn.sg.larksuite.com/wiki/MaFpweI68iKNMvkTioLlJ1uJgQd) |
| Swagger | `lms-be.staging.upbase.asia/api/v1/docs` · `ops-be.staging.upbase.asia/api/v1/docs` |
| Figma | *(chưa có)* |

## Lark

- **Wiki space:** `7660816820865093342`
- **Parent node:** [`02. Execution — Epics & Features`](https://upbasevn.sg.larksuite.com/wiki/X3hhwv2MxizpFgkVudVl7e52gUc) — `X3hhwv2MxizpFgkVudVl7e52gUc`
- **Node dự án:** [`Gamification`](https://upbasevn.sg.larksuite.com/wiki/LRVgwz5L9imG6WkQvJdllro5gNd) — `LRVgwz5L9imG6WkQvJdllro5gNd`

### Đã publish

| Artifact | Node token | URL | Ghi chú |
|---|---|---|---|
| `[PRD] Gamification v0.8` | *(xem wiki)* | https://upbasevn.sg.larksuite.com/docx/KeT8dkIStofZ0axlTW5l4S94gre | **Bản mới nhất** — 05/10/2026 |
| `[PRD] Gamification v0.2` | `J4NGwHIlmijgZBkqxpWlNS4qgxe` | https://upbasevn.sg.larksuite.com/wiki/J4NGwHIlmijgZBkqxpWlNS4qgxe | Bản duyệt Gate 4, giữ để đối chiếu |

> **Publish lại thì nhớ chèn lại ảnh** bằng `.claude/scripts/lark-insert-design-images.py` — ảnh không nằm trong `.md` nên import mới là mất.

> Publish lại thì **ghi đè vào đúng node trên**, đừng import file mới — import mới sinh node khác và người đọc sẽ giữ link cũ.
>
> **5 sơ đồ nằm trong chính file `.md`** dưới dạng khối ` ```mermaid `.
>
> Đẩy bằng `lark-cli docs +create --doc-format markdown` thì **Lark tự dựng mermaid thành bảng trắng**, không cần bước chuyển đổi. Cách import qua `drive/v1/import_tasks` thì không — nó ra code block `Plaintext` và phải chạy `.claude/scripts/lark-mermaid-to-whiteboard.py` để vá.
>
> Cách import: `drive/v1/files/upload_all` → `drive/v1/import_tasks` → chờ `job_status = 0` → `wiki/v2/spaces/{space}/nodes/move_docs_to_wiki`. Token user nằm ở scratchpad, hết hạn thì chạy `lark_refresh.py`.

## Jira

- **Epic:** *(chưa có)*
- **Story:** *(chưa có)*
