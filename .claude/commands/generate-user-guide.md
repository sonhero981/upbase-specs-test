# Generate User Guide – Viết hướng dẫn cho người dùng cuối

Dùng **sau khi tính năng đã phát triển xong**, viết hướng dẫn sử dụng từ PRD đã duyệt + sản phẩm thật.

Đây là mắt xích cuối của workflow: `Yêu cầu → PRD → (dev) → User Guide`.

---

## Đầu vào

`$ARGUMENTS` — tên project hoặc tính năng.

> **Xác định project:** ưu tiên `$ARGUMENTS`; không có → suy từ file đang mở; >1 khả dĩ → liệt kê cho chọn. **Echo + confirm trước khi chạy.**

Đọc theo thứ tự:

1. `docs/prd/prd-*.md` — bản đã qua Gate 4
2. `.claude/_shared-knowledge-base/` — cách các module liên quan đang được mô tả
3. `.claude/_templates/user-guide/Template.md`

**Tính năng chưa dev xong → dừng.** User Guide mô tả cái đang chạy, không mô tả cái sắp có.

---

## Nơi User Guide sống

Hai GitBook repo, tách theo đối tượng:

| Repo | Đối tượng | Đường dẫn |
|---|---|---|
| `uplms` | Học viên | `LMS/User Guide/uplms/` |
| `uplms-ops` | Vận hành | `LMS/User Guide/uplms-ops/` |

Tính năng chạm cả hai → **viết hai bài riêng**, không gộp. Học viên và vận hành cần thông tin khác nhau.

---

## Cấu trúc bài viết

Theo đúng chuẩn 57 page hiện có:

```markdown
# <Tên tính năng>

## I. Thông tin chung

{% hint style="info" %}
**Dành cho:** <vai trò>

**Đường dẫn:** <menu → submenu → màn>

#### Phạm vi & Module liên quan

* **Module chính:** <tên module>
* **Chức năng chính:** <tên chức năng>
* **Module liên quan:** <các module bị chạm>
{% endhint %}

{% hint style="warning" %}
#### Điều kiện tiên quyết

* <quyền cần có>
* <dữ liệu cần có trước>
{% endhint %}

## II. Hướng dẫn chi tiết

<details>
<summary><Tên thao tác></summary>

{% stepper %}
{% step %}
**<Bước 1>**

<mô tả + ảnh>
{% endstep %}
{% endstepper %}

</details>

## III. Lưu ý & Quy tắc nghiệp vụ

{% hint style="warning" %}
### Lưu ý quan trọng
1. …
{% endhint %}

{% hint style="info" %}
### Mẹo sử dụng
1. …
{% endhint %}

## IV. Các lỗi thường gặp & Hướng dẫn xử lý

| Lỗi / Tình huống | Nguyên nhân | Cách xử lý |
| --- | --- | --- |
```

> ⚠️ **Mục `Phạm vi & Module liên quan` là bắt buộc.** 13 page UG hiện tại thiếu khai báo này, và chúng thiếu theo cụm — cả nhóm Chấm điểm và cả nhóm Hoạt động kiểm tra đều trống. Hệ quả: KB không dựng được quan hệ chéo, Impact Analysis bỏ sót đúng chỗ dày quan hệ nhất.

---

## Chuyển PRD → User Guide

| PRD | User Guide |
|---|---|
| `Scenario` | §II Hướng dẫn chi tiết — các bước thao tác |
| `Pre-Condition` | §I Điều kiện tiên quyết |
| `Business rule` | §III Lưu ý & Quy tắc nghiệp vụ |
| Bảng UI → `validate`, `disable`, `tooltip` | §IV Lỗi thường gặp |
| `Out of scope` | Không đưa vào — người dùng cuối không cần biết |
| `Conner case` (QA điền) | §IV Lỗi thường gặp, nếu là tình huống người dùng gặp thật |

**Đổi giọng văn:** PRD viết cho Dev và QA, User Guide viết cho người dùng cuối.

| PRD viết | User Guide viết |
|---|---|
| *"Field `status` disable khi `class.type = Foundation`"* | *"Không đổi được trạng thái với lớp Foundation"* |
| *"Validate: tổng điểm thành phần = 100"* | *"Tổng điểm các thành phần phải bằng 100, nếu không hệ thống sẽ báo lỗi"* |

Bỏ hết thuật ngữ nội bộ: tên bảng, tên field kỹ thuật, tên endpoint, mã rule.

---

## Ảnh màn hình

### Có Playwright MCP

1. Chạy **headless**, viewport **1920×1080**
2. Đăng nhập bằng tài khoản test người dùng cung cấp
3. Chụp theo từng bước trong §II
4. Lưu về `docs/user-guide/screenshots/` với tên `NN-<role>-<mô-tả-ngắn>.png`
5. **Kiểm ảnh đạt ~1920px và layout giống desktop thật** — thu gọn hoặc sidebar phình nghĩa là viewport sai, chụp lại

> Ảnh trong thư mục tạm của Playwright **không phải output**. Phải copy về `screenshots/`.

### Không có Playwright, hoặc người dùng gõ `skip-screenshot`

Chèn placeholder `<!-- ẢNH: mô tả cảnh cần chụp -->` và **liệt kê danh sách ảnh còn thiếu** ở cuối, lưu vào `docs/user-guide/pending-screenshots.md`.

---

## Output

`docs/user-guide/<slug>-<role>.md`

Tính năng chạm cả hai hệ → hai file, hậu tố `-student` và `-ops`.

Tự kiểm theo `.claude/checklist/generate-user-guide.md` trước khi trình bày.

---

## Sau khi viết xong

1. Trình người dùng review
2. Duyệt xong → hỏi có đưa vào GitBook repo tương ứng không
3. **Cập nhật ngược KB:** tính năng mới làm KB thay đổi gì — thêm business rule, đổi field, thêm quan hệ module. Ghi vào file KB tương ứng với mã `KB-*` và đánh dấu nguồn là PRD nào

> Bước 3 là cách KB giàu lên. Không làm thì KB đứng yên trong khi sản phẩm chạy tiếp, và lần Impact Analysis sau sẽ phân tích trên dữ liệu cũ.
