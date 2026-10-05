# Các LMS khác làm chức năng Nhóm thế nào

**Ngày:** 05/10/2026
**Mục đích:** đối chiếu yêu cầu của UpLnD với cách làm phổ biến, để biết chỗ nào đang theo mẫu chung và chỗ nào đang thiếu

> ⚠️ **Đây là tài liệu tham khảo, không phải đề xuất giải pháp.** Không dòng nào ở đây là quyết định. Bước 7 và 8 mới là chỗ so sánh phương án và chọn.

---

## 1. Mẫu chung: hầu hết đều tách hai loại nhóm

Ba nền tảng lớn đều có **hai khái niệm riêng biệt**, không gộp làm một:

| Nền tảng | Loại theo cơ cấu | Loại tuỳ ý |
|---|---|---|
| **TalentLMS** | `Branch` — sub-portal độc lập, có quản trị riêng, thương hiệu riêng, bộ quy tắc riêng | `Group` — gom learner cần cùng một bộ training, kèm báo cáo nhóm |
| **Docebo** | `Branch` — mô phỏng cơ cấu công ty, người trong cùng nhánh thấy nhau | `Group` — gom kiểu không chính thức, **có thể cắt ngang nhiều nhánh** |
| **Moodle** | `Cohort` — phạm vi toàn site hoặc toàn danh mục khoá | `Group` — nằm trong **một khoá** cụ thể |

Điểm chung: **cơ cấu tổ chức là một loại nhóm, không phải toàn bộ khái niệm nhóm.** Docebo nói thẳng rằng group dùng để gom những tập hợp *"có thể là tập con bên trong cơ cấu, hoặc cắt ngang nhiều phần của cơ cấu"*.

Điều này khớp với cách PO đóng khung bài toán ngày 05/10: cây tổ chức đồng bộ từ HRM chỉ là **một nguồn** tạo nhóm, không phải bản chất của chức năng.

---

## 2. Cohort của Moodle hoạt động đúng như "luật đứng"

Tài liệu Moodle mô tả: *thêm hoặc bớt người khỏi một cohort thì họ tự động được ghi danh hoặc gỡ ghi danh khỏi những khoá gắn với cohort đó.*

Đây chính là cơ chế PO mô tả: gán nội dung cho nhóm là **một luật đứng**, không phải sao chép thành viên một lần. Cách hiểu của UpLnD trùng với một hệ đã chạy nhiều năm.

Khác biệt đáng chú ý: Moodle **gỡ ghi danh** khi người rời cohort. Yêu cầu của UpLnD chưa nói rõ chuyện này — `OQ-07` mới chỉ bàn trường hợp xoá cả nhóm, chưa bàn trường hợp một người rời nhóm.

---

## 3. Khái niệm yêu cầu hiện chưa có: nhóm động

Moodle có `Dynamic Cohorts`, cho phép thành viên vào ra **tự động theo điều kiện** thay vì gán tay:

- Nhiều điều kiện trong một luật, ghép bằng `AND` hoặc `OR`
- Điều kiện dựa trên: trường hồ sơ chuẩn, trường hồ sơ tuỳ chỉnh, trạng thái ghi danh, lần đăng nhập cuối, vai trò trong một ngữ cảnh

Yêu cầu 19 hạng mục của UpLnD hiện có **hai cách vào nhóm**: đồng bộ từ HRM, và gán tay. Không có cách thứ ba là *theo điều kiện*.

Ví dụ thứ mà nhóm động làm được còn hai cách kia thì không: *"mọi người có chức danh chứa chữ Trưởng nhóm, ở bất kỳ phòng ban nào"*. Cây tổ chức không gom được nhóm này vì họ nằm rải rác, mà gán tay thì phải cập nhật mỗi lần có người lên chức.

**Không đề xuất làm.** Chỉ nêu để PO biết có khoảng trống đó, và quyết ở Bước 7 xem có đưa vào phạm vi không.

---

## 4. Đồng bộ HRIS: ba tầng dữ liệu

Tài liệu về tích hợp HRIS với LMS mô tả ba tầng, và hệ nào cũng phải quyết riêng từng tầng:

| Tầng | Dữ liệu | UpLnD hiện ở đâu |
|---|---|---|
| 1 | Người dùng: tên, email, mã nhân viên, trạng thái | ✅ Đã đồng bộ được từ Lark |
| 2 | **Cơ cấu: phòng ban, quản lý, địa điểm, chức danh** | ❌ Chưa. Đây là phần dự án này làm |
| 3 | Sự kiện vòng đời: tuyển mới, điều chuyển, nghỉ việc | ❓ Chưa rõ |

Nguyên tắc chung: **HRIS luôn là hệ gốc**, LMS đọc từ đó và ghi ngược lại kết quả học.

Tầng 3 đáng chú ý vì yêu cầu hiện tại chưa nhắc tới. `RC-18` có nói trường hợp quản lý rời vị trí, nhưng chưa nói trường hợp **một học viên bị điều chuyển sang phòng ban khác** — khi đó nghĩa vụ học đã gán qua nhóm cũ xử lý ra sao.

---

## 5. Lỗi hay gặp nhất khi đồng bộ cơ cấu

Một tài liệu về thất bại khi tích hợp HRIS ghi: *phần lớn các lần đồng bộ HRIS sang LMS hỏng vì nhóm lồng nhau. Nếu HRIS không làm phẳng cơ cấu trước khi đẩy qua API, LMS nhiều khả năng sẽ tạo ra hồ sơ người dùng trùng.*

Đúng tình huống UpLnD sắp gặp: cây Lark có 4 cấp, 53 phòng ban, và yêu cầu `RC-07` nói **nhóm cha bao trùm toàn bộ nhánh con**.

Câu hỏi nảy ra từ đây: khi đồng bộ, một người ở `ECOM / Trung tâm vận hành 1 / Growth 1 / Sub-Growth 1` được ghi là thành viên của **một nhóm sâu nhất**, hay của **cả bốn nhóm trên đường đi**? Hai cách cho hai kết quả khác hẳn nhau ở báo cáo và ở phạm vi quản lý.

→ Thành `OQ-21`.

---

## 6. Nhịp đồng bộ

Tài liệu tích hợp phân biệt hai nhịp theo loại sự kiện:

| Loại | Nhịp phù hợp |
|---|---|
| Ghi danh, nghỉ việc | Gần thời gian thực, qua webhook |
| Thay đổi cơ cấu tổ chức | Theo lô, mỗi ngày hoặc mỗi tuần là đủ |

Cơ cấu tổ chức đổi vài lần một năm, nên đồng bộ theo lô là đủ. Nhưng **nghỉ việc thì khác** — người đã rời công ty mà vẫn còn trong nhóm và vẫn nhận nội dung mới là một vấn đề thật.

---

## 7. Tóm tắt: ba chỗ yêu cầu đang thiếu so với mẫu chung

| | Khoảng trống | Hệ nào có |
|---|---|---|
| 1 | **Nhóm động theo điều kiện** — ngoài đồng bộ và gán tay | Moodle `Dynamic Cohorts` |
| 2 | **Người rời nhóm thì nghĩa vụ học xử lý thế nào** — yêu cầu mới bàn trường hợp xoá cả nhóm | Moodle gỡ ghi danh |
| 3 | **Sự kiện vòng đời nhân sự** — điều chuyển, nghỉ việc | Tầng 3 của mô hình tích hợp HRIS |

Và một chỗ yêu cầu **chặt hơn** mẫu chung: `RC-11` đòi dựng lại được ai thuộc nhóm nào tại một thời điểm quá khứ. Không nguồn nào trong ba nền tảng trên nhắc tới việc này như một tính năng sẵn có.

---

## Nguồn

- [What is the difference between groups and branches in TalentLMS](https://help.talentlms.com/hc/en-us/articles/9651522351260-What-is-the-difference-between-groups-and-branches-in-TalentLMS)
- [Best Practices for Setting up Branches and Groups — Docebo Community](https://community.docebo.com/product-q-a-7/best-practices-for-setting-up-branches-and-groups-505)
- [Groups and cohorts — MoodleDocs](https://docs.moodle.org/502/en/Groups_and_cohorts)
- [Dynamic cohorts — Moodle Marketplace](https://marketplace.moodle.com/plugins/tool_dynamic_cohorts)
- [HRIS Integration in LMS: Failures, Sync Issues & Models](https://lmspedia.org/hris-integration-in-lms-why-it-breaks-where-it-works-and-how-different-approaches-compare/)
- [TalentLMS Features For Organizational Mapping — eLearning Industry](https://elearningindustry.com/talentlms-features-organizational-mapping)
