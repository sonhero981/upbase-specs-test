# Checklist: Clarify Requirements

## Tách bạch
- [ ] **[BLOCK]** `Proposed solution` tách khỏi `Problem` — giải pháp stakeholder đưa ra là `Recommendation`, không phải yêu cầu đã chốt
- [ ] Mọi mệnh đề gắn nhãn: `Fact` (có nguồn) / `Assumption` / `Open Question` / `Recommendation`
- [ ] Input đã chuẩn hoá đủ 7 nhóm: request · problem · outcome · users · systems · constraints · proposed solution

## Requirement candidates
- [ ] Bảng đủ cột: ID · Requirement · Type · Source · Confidence · Notes
- [ ] `Type` chọn từ danh sách: Business / Process / Functional / Data / Screen-Report / API-Integration / Role-Permission / Business Rule / NFR
- [ ] `Confidence` có lý do: High = rõ + có nguồn, Medium = thiếu chi tiết, Low = suy luận
- [ ] `Source` trỏ được về input cụ thể, không ghi chung chung

## Đối chiếu KB
- [ ] **[BLOCK]** Mỗi candidate đã tra KB: tính năng này **đã có chưa**
- [ ] Đã kiểm tính năng có đang `hidden` không
- [ ] Đã kiểm mail event liên quan (KB `13`) — có cái nào **đang tắt** không
- [ ] Vùng nằm trong phần **KB chưa phủ** (KB `14` §1–2) → ghi `❓BA`, **không kết luận "chưa có"**
- [ ] Phát hiện yêu cầu **trùng với thứ đã có** → nêu ngay, không để tới Impact Analysis

## Scope
- [ ] Tách đủ In / Out / Potential
- [ ] `Out of scope` có nội dung thật, không bỏ trống

## Open Questions
- [ ] Bảng đủ cột: ID · Question · Why It Matters · Owner · Blocks Next Step?
- [ ] Câu hỏi **cụ thể và trả lời được**, không hỏi mở kiểu "anh muốn thế nào?"
- [ ] `Blocks = Yes` đúng tiêu chí: scope · business rule cốt lõi · user/role · dữ liệu bắt buộc · tích hợp · phân quyền

## Dừng
- [ ] **[BLOCK]** Còn blocking question → **không** sang `/generate-brd`
- [ ] Đã hỏi người dùng: còn gì cần làm rõ thêm không
