# <Tên tính năng>

> **Template User Guide — chuẩn GitBook UpLnD.** Theo đúng cấu trúc 57 page hiện có ở `LMS/User Guide/uplms/` và `uplms-ops/`.
>
> Tính năng chạm cả hai hệ → **viết hai bài riêng**, không gộp. Học viên và vận hành cần thông tin khác nhau.

## I. Thông tin chung

{% hint style="info" %}
**Dành cho:** *Học viên / UpLMS Operator / Mentor / L&D*

**Đường dẫn:** *Menu → Submenu → Màn hình*

#### Phạm vi & Module liên quan

* **Module chính:** *tên module*
* **Chức năng chính:** *tên chức năng*
* **Module liên quan:** *các module bị chạm*
{% endhint %}

{% hint style="warning" %}
#### Điều kiện tiên quyết

* *Quyền cần có*
* *Dữ liệu cần có trước*
* *Trạng thái cần đạt*
{% endhint %}

> ⚠️ **Mục `Phạm vi & Module liên quan` là bắt buộc.** 13 page UG hiện tại thiếu khai báo này, và thiếu theo cụm — cả nhóm Chấm điểm (4/4 page) và cả nhóm Hoạt động kiểm tra (3/3 page) đều trống. Hệ quả: KB không dựng được quan hệ chéo, và Impact Analysis bỏ sót đúng chỗ dày quan hệ nhất.

---

## II. Hướng dẫn chi tiết

<details>

<summary><Tên thao tác 1></summary>

{% stepper %}
{% step %}
**<Bước 1>**

*Mô tả thao tác*

<!-- ẢNH: mô tả cảnh cần chụp -->
{% endstep %}

{% step %}
**<Bước 2>**

*Mô tả*

<!-- ẢNH: mô tả cảnh cần chụp -->
{% endstep %}
{% endstepper %}

</details>

<details>

<summary><Tên thao tác 2></summary>

*…*

</details>

---

## III. Lưu ý & Quy tắc nghiệp vụ

{% hint style="warning" %}
### Lưu ý quan trọng

1. *Ràng buộc người dùng phải biết để không làm sai*
2. *Hành vi hệ thống dễ gây bất ngờ*
{% endhint %}

{% hint style="info" %}
### Mẹo sử dụng

1. *Cách dùng nhanh hơn*
{% endhint %}

---

## IV. Các lỗi thường gặp & Hướng dẫn xử lý

| Lỗi / Tình huống | Nguyên nhân | Cách xử lý |
| --- | --- | --- |
| | | |

---

## Chuyển từ PRD sang User Guide

| PRD | User Guide |
| --- | --- |
| `Scenario` | §II — các bước thao tác |
| `Pre-Condition` | §I — Điều kiện tiên quyết |
| `Business rule` | §III — Lưu ý & Quy tắc nghiệp vụ |
| Bảng UI → `validate`, `disable`, `tooltip` | §IV — Lỗi thường gặp |
| `Out of scope` | **Không đưa vào** — người dùng cuối không cần biết |
| `Conner case` (QA điền) | §IV, nếu là tình huống người dùng gặp thật |

### Đổi giọng văn

PRD viết cho Dev và QA. User Guide viết cho người dùng cuối.

| PRD viết | User Guide viết |
| --- | --- |
| *"Field `status` disable khi `class.type = Foundation`"* | *"Không đổi được trạng thái với lớp Foundation"* |
| *"Validate: tổng điểm thành phần = 100"* | *"Tổng điểm các thành phần phải bằng 100, nếu không hệ thống sẽ báo lỗi"* |
| *"`BR-EDIT-06`: không xoá Test đã có attempt"* | *"Không xoá được bài kiểm tra đã có học viên làm"* |

**Bỏ hết thuật ngữ nội bộ:** tên bảng · tên field kỹ thuật · tên endpoint · mã rule.

### Quy ước ảnh

| | |
| --- | --- |
| Viewport | **1920×1080**, headless |
| Tên file | `NN-<role>-<mô-tả-ngắn>.png` — ví dụ `01-ops-exam-list.png` |
| Thư mục | `docs/user-guide/screenshots/` |
| Kiểm trước khi dùng | Ảnh đạt ~1920px, layout giống desktop thật. Thu gọn hoặc sidebar phình → viewport sai, chụp lại |

Không chụp được → để `<!-- ẢNH: … -->` và liệt kê vào `docs/user-guide/pending-screenshots.md`.
