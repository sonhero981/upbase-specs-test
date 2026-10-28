---
intent: 260923-gamification
unit: u1-recording-engine
artifact: rules
stage: 3.1 functional-design
bolt: B02
version: 1.2
status: draft
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
---
# Business Rules: U1 `u1-recording-engine`

Mã `BR13.x` (x ≤ 13) = `BR-13.x` của PRD v0.14. Ba rule nền của PRD (`BR-TEST`, `BR-REGRADE`, `BR-SKIP`) và rule kỹ thuật mới đánh tiếp từ `BR13.14`. Thẻ `[Qn]` = `functional-design-questions.md`; `[2.43 Qn]`, `[ADR-n]`, `[A-01]`/`[S-03]` = nguồn upstream.

```yaml
rules:
  # ---- Ba cửa trước khi ghi ----
  - id: BR13.1
    statement: "Mỗi nội dung chỉ trả điểm một lần trong một lượt ghi danh."
    category: constraint
    applies_to: AchievementHistory (POINT)
    trigger: "Engine ghi dòng POINT"
    logic: "IF đã có dòng POINT cùng (lượt ghi danh, hành động, nội dung) THEN dừng, kết quả DUPLICATE"
    violation: "Không ghi gì thêm, không đổi UserStats, không thông báo, không phải lỗi"
    source: "PRD BR-13.1, C5"
  - id: BR13.2
    statement: "Điểm chỉ sinh khi bản ghi tiến độ vừa chuyển từ chưa hoàn thành sang hoàn thành, và chỉ các lần chuyển từ lúc bật trở đi."
    category: policy
    applies_to: LearningFlowHooks
    trigger: "Luồng học lưu tiến độ"
    logic: "IF trạng thái trước lần lưu là chưa hoàn thành AND sau lần lưu là hoàn thành THEN phát CompletionFact; ELSE không phát. Thời điểm bật xét ở BR13.18"
    violation: "Không phát"
    source: "PRD BR-13.2, C5"
  - id: BR13.4
    statement: "Test Account không phát sinh gì, lọc ngay từ tầng ghi nhận."
    category: authorization
    applies_to: LearningFlowHooks, GamificationEngine
    trigger: "Trước khi phát và trước khi ghi"
    logic: "IF học viên là Test Account THEN không ghi dòng nào (kể cả dòng 0 điểm), không FailedEvent, không thông báo"
    violation: "Kết quả SKIPPED"
    source: "PRD BR-13.4, C10"
  # ---- Song song ----
  - id: BR13.5
    statement: "Hai lần hoàn thành cùng nội dung gần như đồng thời chỉ cộng một lần; kiểm và ghi là một thao tác không tách rời."
    category: constraint
    applies_to: GamificationEngine
    trigger: "Hai CompletionFact cùng khoá chống trùng"
    logic: "Kiểm trùng nằm trong chính lần ghi (ràng buộc duy nhất của sổ), không đọc rồi ghi; UserStats của học viên khoá trong lần ghi; sự kiện của một học viên xử lý theo thứ tự (khoá phân vùng = học viên)"
    violation: "Lần sau DUPLICATE"
    source: "PRD BR-13.5, A-01 x-idempotency"
  - id: BR13.6
    statement: "Check-in: một học viên một ngày một bản ghi đã tự chặn trùng."
    category: constraint
    applies_to: CheckinService (U2)
    trigger: "—"
    logic: "U1 không làm gì thêm; nghiệm thu ở U2"
    violation: "—"
    source: "PRD BR-13.6"
  # ---- Lỗi ----
  - id: BR13.7
    statement: "Lỗi ở phần ghi nhận không làm hỏng, không làm chậm thao tác học."
    category: policy
    applies_to: LearningFlowHooks, GamificationRecordPublisher
    trigger: "Mọi lỗi sau khi luồng học đã lưu"
    logic: "Điểm gắn chạy sau khi tiến độ đã lưu xong; mọi lỗi của điểm gắn và của việc phát bị chặn lại, không đổi kết quả trả cho học viên; thời gian thêm vào thao tác hoàn thành ≤ 200 ms p95 [2.43 Q14]. Việc phát có hạn chờ ≤ 100 ms: quá hạn coi như phát lỗi (lưu FailedEvent); nếu message thực ra đã tới thì lần chạy lại thành DUPLICATE (BR13.1), không cộng hai lần. (Con số 100 ms để lại biên 100 ms cho phần còn lại của hook; NFR cụ thể do 3.2 chốt, nhưng hạn phát phải < 200 ms)"
    violation: "Ghi FailedEvent (BR13.8)"
    source: "PRD BR-13.7, NFR-GAM-01, 2.43 Q14"
  - id: BR13.8
    statement: "Lần lỗi được ghi lại và tự chạy lại; lần chạy lại mang thời điểm gốc và không thông báo."
    category: policy
    applies_to: FailedEventStore, FailedEventRetry, GamificationEngine
    trigger: "Phát lỗi hoặc engine lỗi"
    logic: "Phát lỗi hoặc engine lỗi (không phải lần chạy lại) THEN lưu FailedEvent RECORD, PENDING, giữ payload gốc. Lần chạy lại dùng occurredAt của payload, không gọi cổng thông báo. Vận hành không cộng bù tay, không có màn Ops [ADR-012, 2.43 Q9]"
    violation: "—"
    source: "PRD BR-13.8, ADR-012"
  # ---- Không chặn, có chủ đích ----
  - id: BR13.9
    statement: "Learning Activity chỉ có Text hoặc Ảnh được tính khi mở; không có cơ chế chống cày riêng."
    category: policy
    applies_to: LearningFlowHooks
    trigger: "Hoàn thành Learning Activity"
    logic: "Không đo thời gian; điểm gắn tin trạng thái hoàn thành của luồng học hiện có (mốc video 80% do client quyết, backend không đổi)"
    violation: "—"
    source: "PRD BR-13.9"
  - id: BR13.10
    statement: "Bị xoá khỏi lớp rồi thêm lại là lượt ghi danh mới, điểm tính lại từ đầu."
    category: policy
    applies_to: GamificationEngine
    trigger: "Học viên học trong lượt ghi danh mới"
    logic: "Khoá chống trùng gồm lượt ghi danh nên lượt mới không trùng lượt cũ. Đường vận hành đặt thẳng trạng thái hoàn thành không phải điểm gắn nên không sinh điểm"
    violation: "—"
    source: "PRD BR-13.10, C5"
  - id: BR13.11
    statement: "Học viên không tự huỷ ghi danh được sau khi đã học; U1 không làm gì thêm."
    category: policy
    applies_to: hệ thống hiện có
    trigger: "—"
    logic: "Dựa vào chặn sẵn của hệ thống (KB-LX-08)"
    violation: "—"
    source: "PRD BR-13.11"
  - id: BR13.12
    statement: "Số khoá hoàn thành đếm lượt hoàn thành, không đếm chứng chỉ."
    category: calculation
    applies_to: UserStats.totalCoursesCompleted
    trigger: "Ghi COURSE_COMPLETED"
    logic: "Mỗi COURSE_COMPLETED được ghi (kể cả 0 điểm) tăng 1; không đọc chứng chỉ"
    violation: "—"
    source: "PRD BR-13.12"
  - id: BR13.13
    statement: "Points hoặc hành động đang tắt vẫn ghi nhận với 0 điểm để chỉ số đếm chạy tiếp."
    category: calculation
    applies_to: GamificationEngine
    trigger: "Qua ba cửa"
    logic: "IF Points tắt OR hành động tắt THEN điểm = 0 ELSE điểm = điểm cấu hình của hành động đọc lúc ghi (C4). Dòng 0 điểm vẫn tăng chỉ số đếm, vẫn xét huy hiệu và hạng; không tăng tổng điểm"
    violation: "—"
    source: "PRD BR-13.13, Định nghĩa chỉ số"
  # ---- Ba rule nền của PRD ----
  - id: BR13.14
    statement: "Bài Test tính TEST_PASSED: Graded = Yes khi đạt ngưỡng, Graded = No khi hoàn thành; Quiz, Case Study, Storyline không phải bài Test."
    category: calculation
    applies_to: LearningFlowHooks
    trigger: "Nộp bài Test, hoặc chấm tay lần đầu"
    logic: "Bài Test = bài trong khoá kiểu giữa kỳ, cuối kỳ, thi thử, kiểm tra chủ đề, kiểm tra chương, làm trong một lượt ghi danh; lượt làm không gắn lượt ghi danh thì không phát [Q3]. Với TEST_PASSED, 'chuyển trạng thái' của BR13.2 là 'lượt này đạt', không phải tiến độ bài (tiến độ bài đã có từ lượt nộp đầu, kể cả trượt). Graded = Yes: đạt khi phần trăm điểm tổng của lượt (hệ thống đã quy đổi) ≥ ngưỡng phần trăm của chính bài; bài không khai ngưỡng thì đạt khi hoàn thành; ngưỡng theo từng phần của bài không dùng [Q2]. Graded = No: phát khi nộp (hoàn thành), không chờ chấm. Graded = Yes xét lúc nộp nếu lượt có điểm ngay (tự chấm, hoặc bài chấm tay chỉ có trắc nghiệm nên không tạo bản chấm); ngược lại xét ở lần chấm đầu tiên kết thúc (BR13.15). Lượt không đạt không phát; lượt sau đạt thì phát (chống trùng giữ một lần mỗi lượt ghi danh)"
    violation: "Không phát"
    source: "PRD BR-TEST, Q2, Q3"
  - id: BR13.15
    statement: "Chấm lại không cộng thêm và không biến trượt thành điểm."
    category: policy
    applies_to: LearningFlowHooks (chấm tay)
    trigger: "Kết thúc chấm"
    logic: "Lần chấm đầu tiên = lần đầu một bản chấm của lượt làm đi tới kết thúc, xét theo lịch sử chấm của lượt (không theo trạng thái hiện tại). Bản chấm bị trả về từ bước duyệt để chấm lại khi chưa kết thúc lần nào thì lần kết thúc sau đó vẫn là lần đầu. IF lượt đã từng có bản chấm kết thúc THEN không phát, kể cả khi đổi từ trượt sang đạt"
    violation: "—"
    source: "PRD BR-REGRADE [suy ra từ luồng chấm → duyệt → chấm lại, review R-02]"
  - id: BR13.16
    statement: "Khoá bỏ qua không tính là hoàn thành."
    category: policy
    applies_to: LearningFlowHooks
    trigger: "Lượt ghi danh chuyển sang hoàn thành"
    logic: |
      Không lọc thêm; cách mỗi loại 'bỏ qua' ra khỏi hook tự nhiên:
      - PASS_BY_ADMIN / PASS_BY_OTHER_CLASS: vận hành đặt thẳng COMPLETED (class.service.ts:8909; grade.service.ts:771), không đi qua hook học, nên không có COURSE_COMPLETED.
      - SKIP_FOUNDATION: học viên tự bỏ qua Foundation để vào khoá chính (class.service.ts:17170-17177); lượt ghi danh Foundation giữ nguyên chưa hoàn thành. Nếu học viên sau đó học nốt Foundation thì H1 phát COURSE_COMPLETED như bình thường — đây là edge case cần PO xác nhận; tạm chấp nhận phát (không có cờ lọc trên lượt ghi danh Foundation, xem Ghi chú cho PO). Khoá chính tính bình thường [Q4b].
    violation: "—"
    source: "PRD BR-SKIP, Q4b"
  # ---- Rule kỹ thuật mới của U1 ----
  - id: BR13.17
    statement: "Hoạt động là Learning Activity; Learning Activity chứa Quiz tính khi Quiz làm xong."
    category: validation
    applies_to: LearningFlowHooks
    trigger: "Section chuyển hoàn thành"
    logic: "Chỉ section kiểu Learning Activity phát ACTIVITY_COMPLETED, ở cả đường mở nội dung và đường nộp Quiz trong hoạt động; bài Test, Case Study, Storyline, chương, phần không phát ACTIVITY_COMPLETED"
    violation: "Không phát"
    source: "PRD Định nghĩa chỉ số (PO chốt 12/10)"
  - id: BR13.18
    statement: "Cửa thời điểm: chỉ ghi khi lúc xử lý Gamification đang bật và thời điểm gốc không sớm hơn lần bật gần nhất."
    category: policy
    applies_to: GamificationEngine
    trigger: "Mọi lần ghi, kể cả chạy lại"
    logic: "IF Gamification tắt OR occurredAt < lastEnabledAt THEN SKIPPED (không ghi, kể cả dòng 0 điểm). Lần chạy lại vượt qua một vòng tắt/bật sẽ bị bỏ, có log. Đang bật mà lastEnabledAt rỗng (dữ liệu cũ) thì không áp vế thời điểm"
    violation: "SKIPPED"
    source: "Q1, PRD BR-14.5, BR-13.2"
  - id: BR13.19
    statement: "Điểm gắn lọc sớm: Gamification tắt hoặc Test Account thì không phát; đọc lỗi thì vẫn phát."
    category: policy
    applies_to: LearningFlowHooks
    trigger: "Trước khi phát"
    logic: "Đọc công tắc từ cấu hình đã lưu đệm và cờ Test Account; IF tắt OR Test Account THEN không phát; IF đọc lỗi THEN phát. Engine vẫn kiểm lại (BR13.4, BR13.18)"
    violation: "—"
    source: "Q5, PRD BR-13.4"
  - id: BR13.20
    statement: "Điểm gắn chỉ phát sau khi tiến độ đã lưu bền, và xét chuyển trạng thái so với trạng thái đọc trước lần lưu."
    category: constraint
    applies_to: LearningFlowHooks
    trigger: "Luồng học có giao dịch hoặc không"
    logic: "Ghi nhận trạng thái lượt ghi danh và section TRƯỚC lần lưu; phát sau khi lưu xong (sau khi giao dịch của luồng học kết thúc). Lượt ghi danh đã hoàn thành từ trước mà luồng đặt lại hoàn thành thì không phát COURSE_COMPLETED"
    violation: "Không phát"
    source: "BR13.2 [suy ra từ code: class.service.ts:10271 đặt lại COMPLETED mỗi lần gọi]"
  - id: BR13.21
    statement: "Chạy lại mỗi 15 phút, tối đa 5 lần, rồi bỏ cuộc có cảnh báo."
    category: policy
    applies_to: FailedEventRetry
    trigger: "Mỗi 15 phút, từng tổ chức"
    logic: "Lấy FailedEvent PENDING, cũ trước; mỗi sự kiện chỉ một bộ chạy xử lý cùng lúc. Kết quả ghi được hoặc DUPLICATE hoặc SKIPPED → RESOLVED. Lỗi → retryCount + 1; retryCount = 5 → GAVE_UP và log mã GAMIFICATION_RECORD_GAVE_UP"
    violation: "—"
    source: "ADR-012, S-03"
  - id: BR13.22
    statement: "Chạy lại theo loại; loại chưa có Unit xử lý thì giữ PENDING."
    category: policy
    applies_to: FailedEventRetry
    trigger: "Chạy lại một FailedEvent"
    logic: "RECORD → engine ghi lại (chế độ chạy lại). CHECKIN, BADGE_BACKFILL, BADGE_BACKFILL_JOB đăng ký bởi U2, U8; chưa đăng ký thì bỏ qua lần này, không tăng retryCount, có log. Dòng lỗi cũ chưa có loại coi là RECORD"
    violation: "—"
    source: "S-03 FailedEventStore.save / retry routing"
  - id: BR13.23
    statement: "Dòng sổ giao dịch giữ tên nội dung tại lúc ghi."
    category: calculation
    applies_to: AchievementHistory.objectNameSnapshot
    trigger: "Ghi dòng POINT"
    logic: "Lấy tên từ CompletionFact; thiếu thì tra tên hiện tại của nội dung; tra không được thì để trống. Đổi tên hay xoá nội dung sau đó không đổi dòng"
    violation: "—"
    source: "PRD BR-3.11, A-01, S-02"
  - id: BR13.24
    statement: "Sau khi ghi xong, engine báo thành tích qua cổng thông báo; U1 dùng bản không làm gì."
    category: policy
    applies_to: GamificationEngine, AchievementNotifier
    trigger: "Lần ghi RECORDED đã lưu bền, không phải chạy lại"
    logic: "Engine lọc trước khi gọi (theo components.md GamificationEngine): chỉ khi Visibility đang bật, không phải chạy lại, không phải trao bù; các mục gửi là dòng POINT có điểm > 0 và dòng BADGE, LEVEL vừa ghi (dòng 0 điểm không gửi, BR-2.10) [suy ra: BADGE/LEVEL từ dòng 0 điểm vẫn gửi, U6 xác nhận]. Gọi sau khi lưu bền, mỗi thành tích một mục theo thứ tự phát sinh; lỗi của cổng bị nuốt và log, không đổi kết quả ghi. Gửi tới ai đang online và hiển thị thế nào thuộc cổng thật của U6"
    violation: "—"
    source: "S-03 AchievementNotifier.notify, NFR-GAM-01"
  - id: BR13.25
    statement: "Dữ kiện hỏng bỏ cuộc ngay, không chạy lại."
    category: validation
    applies_to: GamificationEngine
    trigger: "Kiểm dữ kiện đầu lần ghi"
    logic: "IF CompletionFact thiếu trường bắt buộc hoặc sai loại THEN lưu FailedEvent GAVE_UP, log GAMIFICATION_RECORD_FAILED"
    violation: "FAILED"
    source: "A-01 x-failure-path"
  - id: BR13.26
    statement: "Mọi lần ghi cho đúng một kết quả: RECORDED, SKIPPED, DUPLICATE hoặc FAILED; engine không ném lỗi ra ngoài."
    category: constraint
    applies_to: GamificationEngine
    trigger: "Kết thúc lần ghi"
    logic: "DUPLICATE và SKIPPED không phải lỗi; FAILED đã được lưu theo BR13.8 / BR13.25 (trừ khi đang chạy lại)"
    violation: "—"
    source: "S-03 GamificationEngine.record"
```

## Tóm tắt

| ID | Rule | Loại | Thuộc |
|---|---|---|---|
| BR13.1 | Một lần mỗi nội dung mỗi lượt ghi danh | constraint | Engine |
| BR13.2 | Chỉ lúc chuyển trạng thái, từ lúc bật | policy | Hook |
| BR13.4 | Loại Test Account từ tầng ghi nhận | authorization | Hook + Engine |
| BR13.5 | Song song chỉ một lần | constraint | Engine |
| BR13.6 | Check-in tự chặn trùng | constraint | U2 |
| BR13.7 | Lỗi không làm hỏng, không làm chậm (≤ 200 ms) | policy | Hook + Publisher |
| BR13.8 | Ghi lại lỗi, chạy lại mang thời điểm gốc, không thông báo | policy | Store + Retry |
| BR13.9 | Text/Ảnh tính khi mở, không chống cày | policy | Hook |
| BR13.10 | Lượt ghi danh mới tính lại | policy | Engine |
| BR13.11 | Không tự huỷ ghi danh (có sẵn) | policy | Hệ thống |
| BR13.12 | Đếm lượt hoàn thành khoá | calculation | Engine |
| BR13.13 | Tắt điểm vẫn ghi 0 điểm | calculation | Engine |
| BR13.14 | Bài Test và ngưỡng đạt | calculation | Hook |
| BR13.15 | Chấm lại không cộng | policy | Hook |
| BR13.16 | Khoá bỏ qua không tính | policy | Hook |
| BR13.17 | Hoạt động = Learning Activity | validation | Hook |
| BR13.18 | Cửa thời điểm bật | policy | Engine |
| BR13.19 | Lọc sớm ở điểm gắn | policy | Hook |
| BR13.20 | Phát sau lưu bền, so trạng thái trước | constraint | Hook |
| BR13.21 | Chạy lại 15 phút, 5 lần, GAVE_UP | policy | Retry |
| BR13.22 | Chạy lại theo loại | policy | Retry |
| BR13.23 | Giữ tên nội dung lúc ghi | calculation | Engine |
| BR13.24 | Cổng thông báo sau lưu bền (no-op ở U1) | policy | Engine |
| BR13.25 | Dữ kiện hỏng bỏ cuộc ngay | validation | Engine |
| BR13.26 | Bốn kết quả, không ném lỗi | constraint | Engine |
