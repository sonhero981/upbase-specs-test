---
intent: 260923-gamification
unit: u1-recording-engine
artifact: functional-design-questions
stage: 3.1 functional-design
bolt: B02
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
answerer: BE lead Đoàn Quang Cường
---
# 3.1 Functional Design U1 `u1-recording-engine`, câu hỏi
Intent: 260923-gamification · Cách trả lời: Guide me · Đã trả lời: 6/6 (Q4 thay bằng Q4b)

Bằng chứng: lms-be `origin/feature/gamification` @9006b80. Đã có đáp án ở PRD, 2.43, ADR, contract thì không hỏi lại (xem cuối file).

## Lô 1 (chặn)

## Q1. Công tắc `Gamification` được xét theo thời điểm nào khi engine xử lý một sự kiện?
Vì sao hỏi: Engine chạy sau Kafka (ADR-009) và chạy lại sau tối đa ~75 phút (ADR-012). Code WP1 chỉ xét công tắc lúc xử lý (`eligibility.handler.ts:30-31`), nên sự kiện xảy ra lúc tắt mà xử lý sau khi bật vẫn được ghi, trái BR-13.2 / BR-14.5 ("chỉ tính từ thời điểm bật").
A. Ghi khi lúc xử lý `Gamification` đang bật **và** thời điểm gốc ≥ lần bật gần nhất (`lastEnabledAt`). Sự kiện xảy ra trong một lượt bật trước, chạy lại sau một vòng tắt/bật, sẽ mất (hiếm, có log)  [đề xuất, đúng BR-14.5, không cần lưu lịch sử bật/tắt]
B. Chỉ xét công tắc lúc xử lý (giữ code WP1)
C. Lưu lịch sử các khoảng bật, ghi khi thời điểm gốc nằm trong một khoảng bật (kể cả đang tắt lúc xử lý)
X. Khác, xin nói rõ
Chặn: có
[Answer]: A (chọn trong phiên 2026-10-14 thay BE lead, chờ BE lead xác nhận)

## Q2. Một bài Test `Graded Assignment = Yes` "đạt Pass Point" (BR-TEST) so với ngưỡng nào?
Vì sao hỏi: Có ba ngưỡng trong code: ngưỡng phần trăm của bài (`quiz.entity.ts:117-118` `required_percent_score`, hiện dùng cho bài cuối Foundation `libs/modules/src/lib/quiz-attempt/quiz-attempt.service.ts:406-407` và thủ tục tính điểm lớp `libs/database/migrations-stored-procedure/1721890762428-update-function-get-class-user-instance-to-score.ts:188`; ngưỡng theo phần `quiz-section.entity.ts:29`, `quiz-section-category-setting.entity.ts:31` `pass_point` không phải ngưỡng của cả bài), điểm đạt của khoá (`course.entity.ts:53` `pass_point`), kết quả đạt khoá (`user-scores.entity.ts:47` `is_passed`). `finishGrading` không xét đạt (`quiz-attempt-grading.service.ts:3105-3115`).
A. Phần trăm điểm của lượt ≥ ngưỡng phần trăm của chính bài Test; bài không khai ngưỡng thì coi như đạt khi hoàn thành  [đề xuất, BR-TEST nói "Pass Point" của bài Test]
B. Phần trăm điểm của lượt ≥ điểm đạt của khoá
C. Theo kết quả đạt khoá
X. Khác, xin nói rõ
Chặn: có
[Answer]: A (chọn trong phiên 2026-10-14 thay BE lead, chờ BE lead xác nhận)

## Q3. Loại bài nào là "bài Test" (điểm TEST_PASSED, đếm số bài Test)?
Vì sao hỏi: `QUIZ_TYPE` (`quiz.constants.ts:33-43`) có QUIZ, MID_TERM_TEST, FINAL_TEST, MOCK_TEST, ENTRANCE_TEST, STORY, TOPIC_TEST, CHAPTER_TEST, EVENT_TEST. PRD loại Quiz, Case Study (STORY), Storyline nhưng không nói ENTRANCE_TEST, EVENT_TEST.
A. Bài Test là bài nằm trong khoá, kiểu MID_TERM_TEST, FINAL_TEST, MOCK_TEST, TOPIC_TEST, CHAPTER_TEST. ENTRANCE_TEST, EVENT_TEST không tính  [đề xuất, PRD nói "bài Test trong khoá"; hai loại kia không nằm trong lượt ghi danh nên không chống trùng được theo C5]
B. Mọi kiểu trừ QUIZ, STORY
X. Khác, xin nói rõ
Chặn: có
[Answer]: A (chọn trong phiên 2026-10-14 thay BE lead, chờ BE lead xác nhận)

## Q4. "Khoá được đánh dấu bỏ qua" (BR-SKIP) ứng với trạng thái nào trong hệ thống?
Vì sao hỏi: Không có cờ bỏ qua khoá. Gần nhất là `class_user_instances.foundation_status` (`class-user-instances.entity.ts:95-101`, giá trị `class.constants.ts:124-130`): SKIP_FOUNDATION (học viên tự bỏ qua, `class.service.ts:17171`), PASS_BY_ADMIN (vận hành cho qua, đặt thẳng COMPLETED `:8909`), PASS_BY_OTHER_CLASS (`grade.service.ts:771`).
A. Lượt ghi danh có `foundation_status` là SKIP_FOUNDATION, PASS_BY_ADMIN hoặc PASS_BY_OTHER_CLASS thì không phát COURSE_COMPLETED; hoạt động, bài Test học thật vẫn tính  [đề xuất, khớp TC-124]
B. Chỉ SKIP_FOUNDATION
X. Khác, xin nói rõ
Chặn: có
[Answer]: A (chọn trong phiên 2026-10-14 thay BE lead, chờ BE lead xác nhận)
Đính chính (review R-01, 2026-10-14): `foundation_status` nằm trên lượt ghi danh khoá CHÍNH (lớp LESSON, `class.service.ts:8888`, `:17141-17171`), ghi việc Foundation đã qua/bỏ qua; đáp án A sẽ chặn COURSE_COMPLETED của khoá chính. Hỏi lại thành Q4b.

## Q4b. BR-SKIP xử lý thế nào khi không có cờ "khoá bỏ qua"?
Vì sao hỏi: Không có cờ bỏ qua trực tiếp trên lượt ghi danh. Ba tình huống:
- PASS_BY_ADMIN (`class.service.ts:8909`): vận hành đặt thẳng COMPLETED không qua hook → tự không có COURSE_COMPLETED.
- PASS_BY_OTHER_CLASS (`grade.service.ts:771`): tương tự.
- SKIP_FOUNDATION (`class.service.ts:17170-17177`): chỉ gắn cờ trên lượt ghi danh khoá CHÍNH và mở khoá chính; lượt ghi danh Foundation vẫn ở trạng thái chưa hoàn thành. Nếu học viên sau đó học nốt Foundation thật, H1 sẽ phát COURSE_COMPLETED cho Foundation như bình thường.
A. Không lọc thêm: PASS_BY_ADMIN/PASS_BY_OTHER_CLASS tự không có COURSE_COMPLETED vì không qua hook. SKIP_FOUNDATION rồi học nốt thì phát — edge case này chờ PO xác nhận (xem Ghi chú cho PO trong functional-spec.md); khoá chính tính bình thường; không đọc `foundation_status`  [đề xuất, tạm chấp nhận]
B. Coi là câu hỏi mở cho PO, tạm dùng A
X. Khác, xin nói rõ
Chặn: có
[Answer]: A (chọn trong phiên 2026-10-14 thay BE lead, chờ BE lead xác nhận). Thay Q4. Edge case SKIP_FOUNDATION bổ sung 2026-10-15 (review R-14).

## Lô 2 (không chặn)

## Q5. Điểm gắn trong luồng học có đọc công tắc trước khi phát sự kiện không?
Vì sao hỏi: Mọi tổ chức mặc định tắt (BR-14.6). Phát mọi lần hoàn thành của mọi tổ chức thì event-processor nhận nhiều sự kiện chỉ để bỏ qua.
A. Có: điểm gắn đọc `Gamification` bật/tắt và Test Account từ dữ liệu đã có (cache cấu hình), tắt hoặc Test Account thì không phát; đọc lỗi thì vẫn phát. Engine vẫn kiểm lại (cửa chính)  [đề xuất, BR-13.4 "lọc ngay từ tầng ghi nhận", NFR ≤ 200 ms]
B. Không: luôn phát, engine quyết
X. Khác, xin nói rõ
Chặn: không
[Answer]: A (chọn trong phiên 2026-10-14 thay BE lead, chờ BE lead xác nhận)

## Đã có đáp án, không hỏi
- Qua Kafka, key = học viên: ADR-009, A-01.
- Chạy lại 15 phút, tối đa 5 lần, GAVE_UP + log, không màn Ops: ADR-012, 2.43 Q9.
- Lần chạy lại mang thời điểm gốc, không thông báo: BR-13.8, S-03.
- Chạy lại tới sau đóng băng campaign: không đổi kết quả campaign (2.43 Q8, ADR-013); U1 chỉ cần giữ thời điểm gốc của sự kiện lỗi đọc được.
- Thông báo: U1 khai cổng thông báo + bản không làm gì; U6 thay (S-03).
- Phương án "ghi nhận đã xong khoá" khi thêm lại học viên (BR-13.10) không có trong code (`class.service.ts:7767` luôn tạo lượt mới chưa học). Mọi đường vận hành đặt thẳng hoàn thành (`:2795`, `:4079`, `:8909`, `:10552`, `:16110`) không phải đường gắn, nên không sinh điểm. Ghi chú cho PO, không hỏi.

## Consolidated Summary
- Q1: ghi khi lúc xử lý `Gamification` bật và thời điểm gốc ≥ lần bật gần nhất; chạy lại qua một vòng tắt/bật thì bỏ, có log.
- Q2: bài Test chấm điểm đạt khi phần trăm điểm của lượt ≥ ngưỡng phần trăm của chính bài; không khai ngưỡng thì đạt khi hoàn thành. Xét lúc nộp, hoặc lúc chấm tay lần đầu.
- Q3: bài Test = MID_TERM_TEST, FINAL_TEST, MOCK_TEST, TOPIC_TEST, CHAPTER_TEST nằm trong khoá.
- Q4 (thay bằng Q4b): PASS_BY_ADMIN/PASS_BY_OTHER_CLASS đi đường vận hành không gắn nên không có COURSE_COMPLETED; SKIP_FOUNDATION rồi học nốt Foundation thật thì phát COURSE_COMPLETED — edge case cần PO xác nhận; không đọc foundation_status.
- Q5: điểm gắn đọc công tắc + Test Account trước khi phát; đọc lỗi vẫn phát; engine kiểm lại.

Xác nhận: Looks correct (2026-10-14, chọn trong phiên thay BE lead).
