---
intent: 260923-gamification
artifact: unit-of-work
stage: 2.7 units-generation
version: 2.0
status: approved
approved_at: 2026-10-13 (FE lead + [GIẢ LẬP] BE lead, DEC-T20)
author: FE lead Nguyễn Hùng Sơn (tech lead tác giả)
scope: cả intent, 19 US (DEC-T15)
consumes: inception/domain-design/components.md v2.0, decisions.md v2.0 (DEC-T19)
supersedes: v1.0 (U0 cho US14, US15, DEC-T7)
---

# Unit of Work: Gamification, cả intent (19 US)

18 Unit, tổng ước lượng 50.5 ngày công. Chia theo **lát dọc mỗi US** (một US đúng một Unit, BE + FE cùng Unit khi xây và test được cùng nhau), cắt nhỏ hơn Proto-Unit của PRD để mỗi Unit ≤ ~3 ngày công (`units-generation-questions.md` Q1, Q2). U0 giữ nguyên Unit đã có thiết kế. Thứ tự làm và người làm thuộc 2.9.

## Units

| Unit ID | Directory | Kind | US | Repo chạm | Cỡ | Ngày công | Nhóm AC | Deployment | Proto-Unit |
|---|---|---|---|---|---|---|---|---|---|
| U0 | `u0-foundation` | service | US14, US15 | lms-be, ops-fe | M | 3 | 7 | embedded | PU1 Nền tảng |
| U1 | `u1-recording-engine` | service | US13 | lms-be | L | 3,5 | 1 | embedded | PU2 Điểm |
| U2 | `u2-daily-checkin` | service | US5 | lms-be, lms-fe | M | 3 | 4 | embedded | PU2 Điểm |
| U3 | `u3-points-config` | service | US8 | lms-be, ops-fe | M | 2,5 | 2 | embedded | PU2 Điểm |
| U4 | `u4-ops-achievement-log` | service | US22 | lms-be, ops-fe | M | 3 | 2 | embedded | PU2 Điểm |
| U5 | `u5-learner-home` | service | US1 | lms-be, lms-fe | M | 3 | 7 | embedded | PU5 Hiển thị cho học viên |
| U6 | `u6-achievement-realtime` | service | US2 | lms-be, lms-fe | M | 3 | 2 | embedded | PU5 Hiển thị cho học viên |
| U7 | `u7-achievement-history` | service | US3 | lms-be, lms-fe | S | 2 | 4 | embedded | PU5 Hiển thị cho học viên |
| U8 | `u8-badges-config` | service | US9 | lms-be, ops-fe | M | 3 | 3 | embedded | PU3 Huy hiệu |
| U9 | `u9-badge-gallery` | service | US4 | lms-be, lms-fe | S | 1,5 | 2 | embedded | PU3 Huy hiệu |
| U10 | `u10-levels-config` | service | US10 | lms-be, ops-fe | M | 2,5 | 4 | embedded | PU4 Hạng |
| U11 | `u11-leaderboard` | service | US6 | lms-be, lms-fe | L | 4,5 | 4 | embedded | PU6 Bảng xếp hạng |
| U12 | `u12-my-position` | service | US7 | lms-be, lms-fe | S | 2 | 1 | embedded | PU6 Bảng xếp hạng |
| U13 | `u13-leaderboard-config` | service | US11 | lms-be, ops-fe | S | 2 | 3 | embedded | PU6 Bảng xếp hạng |
| U14 | `u14-ops-learner-list` | service | US12 | lms-be, ops-fe | M | 3 | 1 | embedded | PU6 Bảng xếp hạng |
| U15 | `u15-campaign-admin` | service | US20 | lms-be, ops-fe | M | 3 | 3 | embedded | PU7 Campaign |
| U16 | `u16-campaign-board` | service | US19 | lms-be, lms-fe | M | 3 | 1 | embedded | PU7 Campaign |
| U17 | `u17-campaign-results` | service | US21 | lms-be, ops-fe, lms-fe | M | 3 | 2 | embedded | PU7 Campaign |

- **Kind `service`** cho mọi Unit: mỗi Unit có phần lms-be chạy được (endpoint, consumer, cron hoặc hook) kèm hoặc không kèm UI → áp 3.1, 3.41 khi có màn, 3.5. Không có Unit `spec` riêng: contract nằm ở 2.8, dùng chung.
- **Deployment `embedded`** cho mọi Unit: không có deployable mới. Code lms-be nằm trong app có sẵn (`lms`, `ops`, `mock-test-service`, `event-processor-service`, `background-job-service`) + `libs/*`; FE là feature module có sẵn (`@ops/feature-gamification`, `@lms/feature-gamification`). Phát hành an toàn vì mọi công tắc mặc định tắt (BR-14.6, 2.43 Q4).
- **Ngày công**: một dev làm trọn Unit, gồm test tay; đã trừ phần có sẵn ở WP0, WP1, WP3 (lms-be) và nhánh WIP lms-fe (ADR-015). Ước lượng thô, 3.1 xem lại. U1 (3,5) và U11 (4,5) vượt trần ~3 ngày, có ký (Q6).
- **Cỡ**: S ≤ 2 ngày, M 2,5–3 ngày, L > 3 ngày.
- **Nhóm AC** (Q6): số bảng markdown trong mục `4/ Acceptance criteria` của từng US trong PRD v0.14 (đếm dòng phân cách `|---|`, tái lập bằng script). U0 (7) và U5 (7) vượt trần 6, nằm trong ngoại lệ có ký cùng U1, U11 (Q6): story không chia được, U0 đã có thiết kế. Ước lượng U5 và U17 có thể lạc quan (đưa nhánh WIP vào; thêm phần học viên ở U17): 3.1 của hai Unit này xem lại ngày công.
- **Proto-Unit của PRD** (`# Unit — nhóm bàn giao`): PU1 Nền tảng, PU2 Điểm, PU3 Huy hiệu, PU4 Hạng, PU5 Hiển thị cho học viên, PU6 Bảng xếp hạng, PU7 Campaign. Mỗi PU tách thành một hoặc nhiều Unit để giữ trần 3 ngày.

## U0 — `u0-foundation`
**Mô tả.** Vận hành có quyền mở trang Gamification bên Ops, bật tắt hai công tắc chung; quyền gamification gắn đúng mọi endpoint cấu hình.

| | |
|---|---|
| US | US14, US15 |
| Component (`components.md` v2.0) | GamificationConfig (khối chung), GamificationSettingsOpsApi (sửa WP3: PATCH khối chung, tên quyền + tags cho mọi endpoint, ADR-016), OpsAccessControl, TenantProfile; ops-fe OpsGamificationModule, OpsSettingsPage (khối chung), OpsGamificationApiClient, OpsPermissionCatalog, RolePermissionScreen |
| Phụ thuộc Unit | — |
| Điểm tích hợp | U0-IC1 ops-fe → lms-be qua guard Ops thật · U0-IC2 PostgreSQL RLS · U0-IC3 Redis cache tenant · U0-IC4 Casbin + màn role |
| Ghi chú | Đã có thiết kế Construction (3.1, 3.41; plan 3.5 đang `[R]` theo ADR-016). Giữ số, giữ thư mục. |

## U1 — `u1-recording-engine`
**Mô tả.** Hoàn thành hoạt động, khoá, bài Test ở mọi luồng học sinh ra một lần ghi nhận đúng (chống trùng, chỉ lúc chuyển trạng thái, dòng 0 điểm, loại Test Account); lỗi không làm hỏng thao tác học và được tự chạy lại.

| | |
|---|---|
| US | US13 |
| Component (`components.md` v2.0) | LearningFlowHooks (5 điểm hook + updateUserCourseSectionProgress), GamificationRecordPublisher (WP1), GamificationEngine (WP1: Point/Badge/Level handler; bổ sung object_name_snapshot, dòng 0 điểm theo công tắc), FailedEventStore, FailedEventRetry, LearnerDirectory |
| Phụ thuộc Unit | U0 `u0-foundation` |
| Điểm tích hợp | Kafka process_gamification_record lms/mock-test/ops → event-processor · cron background-job |
| Ghi chú | WP1 đã có engine + publisher + consumer. Ngày công: hook lms 1 + hook mock-test/ops 1,5 (≈ WP7) + cron retry 0,5 + rà BR-13.* 0,5 = 3,5, vượt trần có ký (Q6). Không có UI: kiểm bằng dữ liệu ledger. AchievementNotifier chưa có thì engine dùng adapter no-op, Unit của US2 thay bằng bản thật. |

## U2 — `u2-daily-checkin`
**Mô tả.** Học viên mở UpLMS lần đầu trong ngày (thao tác thật) được ghi ngày có mặt, chuỗi và điểm theo chuỗi; tab treo, request nền không tính.

| | |
|---|---|
| US | US5 |
| Component (`components.md` v2.0) | CheckinService (endpoint + consumer, chuỗi BR-5.4…5.15), LmsCheckinTrigger, LmsGamificationApiClient (thêm hàm check-in), LmsAppShellIntegration (gắn trigger) |
| Phụ thuộc Unit | U1 `u1-recording-engine`, U5 `u5-learner-home` |
| Điểm tích hợp | lms-fe → lms-be endpoint check-in · Kafka process_gamification_checkin → event-processor |
| Ghi chú | Phụ thuộc U5: dùng LmsGamificationApiClient và múi giờ từ thông tin của tôi do U5 dựng, gắn trigger vào app shell của U5. Thông báo của check-in thuộc U6. |

## U3 — `u3-points-config`
**Mô tả.** Vận hành bật tắt Points và từng hành động, khai điểm, điểm nền check-in; tự lưu từng ô; giá trị mặc định theo design.

| | |
|---|---|
| US | US8 |
| Component (`components.md` v2.0) | GamificationConfig (khối Points, rule chéo khoá tiêu chí hạng), GamificationSettingsOpsApi (point-rules PATCH), OpsSettingsPage (khối Points) |
| Phụ thuộc Unit | U0 `u0-foundation` |
| Điểm tích hợp | ops-fe → lms-be PATCH point-rules |
| Ghi chú | Rule khoá tiêu chí hạng (BR-10.7) lưu ở U3 nhưng chỉ kiểm được khi có khối Levels: nghiệm thu BR-10.7 ở U10. |

## U4 — `u4-ops-achievement-log`
**Mô tả.** Vận hành tra mọi lần ghi nhận của cả tổ chức, lọc học viên, loại sự kiện, khoảng ngày; thấy dòng 0 điểm; kể cả khi chưa hiển thị cho học viên.

| | |
|---|---|
| US | US22 |
| Component (`components.md` v2.0) | GamificationOpsDataApi (nhật ký), OpsAchievementLogPage, OpsGamificationModule (mục menu), OpsPermissionCatalog (quyền xem học viên) |
| Phụ thuộc Unit | U1 `u1-recording-engine` |
| Điểm tích hợp | ops-fe → lms-be GET nhật ký |
| Ghi chú | Chủ của GamificationOpsDataApi (Unit khác mở rộng). Mục menu thứ hai của nhóm Gamification; quyền `gr_view_gamification_learners` có endpoint đầu tiên ở đây (US15-AC4 nghiệm thu ở U4). |

## U5 — `u5-learner-home`
**Mô tả.** Học viên vào màn Gamification (menu, dải tóm tắt, hai panel How to…, khối My Learning); mọi thành phần ẩn hiện theo công tắc (BR-1.8); tắt thì không truy cập được.

| | |
|---|---|
| US | US1 |
| Component (`components.md` v2.0) | LearnerGamificationApi (thông tin của tôi + cờ, quy tắc, field My Learning), LmsGamificationFeature (màn, dải, panel, banner), LmsAppShellIntegration (menu, route, My Learning), LmsGamificationVisibility, LmsGamificationApiClient |
| Phụ thuộc Unit | U1 `u1-recording-engine` |
| Điểm tích hợp | lms-fe → lms-be GET thông tin của tôi, quy tắc, my-learnings |
| Ghi chú | Chủ của LearnerGamificationApi, LmsGamificationFeature, LmsAppShellIntegration, LmsGamificationVisibility, LmsGamificationApiClient (Unit khác mở rộng). Nhận việc đưa nhánh WIP lms-fe vào (rebase lên staging, phần UI của Unit khác giữ sau cờ ẩn tới Unit đó) (ADR-015). Ngày công: đưa WIP vào 0,5 + API thông tin của tôi, quy tắc, field My Learning 1 + nối API FE 1 + rà BR-1.8 0,5 = 3. Đi trọn lms-fe → lms-be → dữ liệu engine thật. |

## U6 — `u6-achievement-realtime`
**Mô tả.** Học viên đang online thấy thẻ thông báo ngay khi nhận điểm, huy hiệu, lên hạng; không gộp; offline thì không xếp hàng.

| | |
|---|---|
| US | US2 |
| Component (`components.md` v2.0) | AchievementNotifier (gateway socket.io mới + redis-adapter/emitter, thay adapter no-op), GamificationEngine (emit sau commit), LmsAchievementRealtime, LmsAppShellIntegration (gắn realtime) |
| Phụ thuộc Unit | U5 `u5-learner-home` |
| Điểm tích hợp | socket.io lms-fe ↔ lms gateway · redis-emitter từ event-processor |
| Ghi chú | Hạ tầng mới (ADR-008, R-14): dependency mới, cấu hình nhiều instance. |

## U7 — `u7-achievement-history`
**Mô tả.** Học viên mở lịch sử ghi nhận từ panel, tải 20 mục mỗi lần, dòng ẩn theo chức năng, dòng 0 điểm không hiện.

| | |
|---|---|
| US | US3 |
| Component (`components.md` v2.0) | LearnerGamificationApi (lịch sử), LmsGamificationFeature (panel lịch sử) |
| Phụ thuộc Unit | U5 `u5-learner-home` |
| Điểm tích hợp | lms-fe → lms-be GET lịch sử |
| Ghi chú | Panel đã có ở nhánh WIP. |

## U8 — `u8-badges-config`
**Mô tả.** Vận hành bật tắt Badges, từng loại, đặt tên, mô tả, hình từng mốc (mốc chỉ đọc); bật thì trao bù không thông báo.

| | |
|---|---|
| US | US9 |
| Component (`components.md` v2.0) | GamificationConfig (khối Badges), GamificationSettingsOpsApi (badges PATCH), BadgeBackfill, GamificationEngine (awardBackfill), ResourceLibrary, OpsSettingsPage (khối Badges, chọn ảnh) |
| Phụ thuộc Unit | U0 `u0-foundation`, U1 `u1-recording-engine` |
| Điểm tích hợp | ops-fe → lms-be PATCH badges · Kafka việc trao bù |
| Ghi chú | Xét huy hiệu khi ghi nhận đã có ở WP1; Unit này lo cấu hình và trao bù. |

## U9 — `u9-badge-gallery`
**Mô tả.** Học viên xem tab Badges trong My Profile: mọi mốc của loại đang bật, đã đạt màu, chưa đạt xám, trỏ vào thấy mốc.

| | |
|---|---|
| US | US4 |
| Component (`components.md` v2.0) | LearnerGamificationApi (huy hiệu), LmsGamificationFeature (gallery), LmsAppShellIntegration (tab Badges desktop + mobile) |
| Phụ thuộc Unit | U5 `u5-learner-home`, U8 `u8-badges-config` |
| Điểm tích hợp | lms-fe → lms-be GET huy hiệu |
| Ghi chú | Tab đã có ở nhánh WIP. |

## U10 — `u10-levels-config`
**Mô tả.** Vận hành đặt bội số ba tiêu chí, trần hạng; tiêu chí khoá theo Points/Badges; không tắt được tiêu chí cuối; hạng chỉ tính mốc mới vượt.

| | |
|---|---|
| US | US10 |
| Component (`components.md` v2.0) | GamificationConfig (khối Levels, rule BR-10.7, BR-10.8), GamificationSettingsOpsApi (levels PATCH), GamificationEngine (LevelHandler đọc total_badges_acquired, ADR-011), OpsSettingsPage (khối Levels) |
| Phụ thuộc Unit | U3 `u3-points-config`, U8 `u8-badges-config` |
| Điểm tích hợp | ops-fe → lms-be PATCH levels |
| Ghi chú | Phụ thuộc U3, U8 vì khoá tiêu chí theo hai khối đó. |

## U11 — `u11-leaderboard`
**Mô tả.** Học viên xem năm bảng theo năm khung cố định, tính sẵn 8 tiếng, top 3, Show All, nhãn Last updated.

| | |
|---|---|
| US | US6 |
| Component (`components.md` v2.0) | LeaderboardComputation (computeRange, snapshot, con trỏ ADR-018), LeaderboardService (cron + đọc), LearnerGamificationApi (bảng), LmsGamificationFeature (bảng, khung) |
| Phụ thuộc Unit | U1 `u1-recording-engine`, U5 `u5-learner-home` |
| Điểm tích hợp | cron background-job → snapshot · lms-fe → lms-be GET bảng |
| Ghi chú | Chủ của LeaderboardComputation. Ngày công: computeRange + snapshot + con trỏ 2 (≈ WP2) + cron 1 + API 0,5 + nối FE 0,5 (UI có ở WIP) + rà BR-6.* 0,5 = 4,5, vượt trần có ký (Q6): US6 không chia được; phần BE và FE làm song song được trong cùng Unit. |

## U12 — `u12-my-position`
**Mô tả.** Học viên luôn thấy dòng của mình, một người dưới, khoảng cách tới người trên, kể cả khi chưa có chỉ số.

| | |
|---|---|
| US | US7 |
| Component (`components.md` v2.0) | LeaderboardService (vị trí của tôi), LearnerGamificationApi, LmsGamificationFeature (MyPosition) |
| Phụ thuộc Unit | U11 `u11-leaderboard` |
| Điểm tích hợp | lms-fe → lms-be GET vị trí của tôi |

## U13 — `u13-leaderboard-config`
**Mô tả.** Vận hành bật tắt Leaderboard và năm bảng, bảng khoá theo chức năng nguồn, không tắt được bảng cuối; xem trước All time.

| | |
|---|---|
| US | US11 |
| Component (`components.md` v2.0) | GamificationConfig (khối Leaderboard, BR-11.4, BR-11.5), GamificationSettingsOpsApi (leaderboard-settings PATCH), GamificationOpsDataApi (xem trước), OpsSettingsPage (khối Leaderboard + xem trước) |
| Phụ thuộc Unit | U3 `u3-points-config`, U4 `u4-ops-achievement-log`, U11 `u11-leaderboard` |
| Điểm tích hợp | ops-fe → lms-be PATCH leaderboard-settings, GET xem trước |
| Ghi chú | Thêm endpoint xem trước vào GamificationOpsDataApi của U4. |

## U14 — `u14-ops-learner-list`
**Mô tả.** Vận hành xem danh sách học viên với hạng, điểm, huy hiệu, hoạt động, khoá; khoảng ngày tự do + nút nhanh; sắp xếp, tìm, xuất Excel.

| | |
|---|---|
| US | US12 |
| Component (`components.md` v2.0) | GamificationOpsDataApi (danh sách + export), LeaderboardComputation (computeRange), OpsLearnerListPage, OpsGamificationModule (mục menu) |
| Phụ thuộc Unit | U4 `u4-ops-achievement-log`, U11 `u11-leaderboard` |
| Điểm tích hợp | ops-fe → lms-be GET danh sách, export |
| Ghi chú | Phụ thuộc U4 vì bấm tên mở nhật ký đã lọc và dùng chung nhóm menu. |

## U15 — `u15-campaign-admin`
**Mô tả.** Vận hành tạo, sửa, xoá campaign theo luật trạng thái ở khối Campaign trang cấu hình; quyền xem học viên chỉ xem.

| | |
|---|---|
| US | US20 |
| Component (`components.md` v2.0) | CampaignService, CampaignOpsApi, OpsCampaignPanels (danh sách, Campaign Settings), OpsSettingsPage (khối Campaign), GamificationConfig (popover tắt nêu số campaign, 2.43 Q7) |
| Phụ thuộc Unit | U0 `u0-foundation` |
| Điểm tích hợp | ops-fe → lms-be CRUD campaign |

## U16 — `u16-campaign-board`
**Mô tả.** Học viên thấy lối vào campaign cạnh khung cố định, xem bảng tạm tính của campaign đang chạy và kết quả đã kết thúc.

| | |
|---|---|
| US | US19 |
| Component (`components.md` v2.0) | CampaignLeaderboard (tạm tính cùng lượt cron), LeaderboardService, LearnerGamificationApi (campaign), LmsGamificationFeature (lối vào + màn campaign) |
| Phụ thuộc Unit | U11 `u11-leaderboard`, U12 `u12-my-position`, U15 `u15-campaign-admin` |
| Điểm tích hợp | lms-fe → lms-be GET campaign, bảng campaign |
| Ghi chú | Chưa có design (OQ-45): ui-map Provisional. Phần học viên xem kết quả đã đóng băng (BR-19.6) nghiệm thu ở U17. |

## U17 — `u17-campaign-results`
**Mô tả.** Campaign kết thúc: chốt người tham gia ở biên, đóng băng sau 24 giờ khi hết lỗi chờ; vận hành xem kết quả ba tab và xuất Excel.

| | |
|---|---|
| US | US21 |
| Component (`components.md` v2.0) | CampaignLeaderboard (CampaignParticipant, đóng băng, ADR-013, ADR-017), GamificationOpsDataApi (kết quả + export), OpsCampaignPanels (panel kết quả), LearnerGamificationApi + LmsGamificationFeature (học viên đọc kết quả đã đóng băng, BR-19.6) |
| Phụ thuộc Unit | U4 `u4-ops-achievement-log`, U16 `u16-campaign-board` |
| Điểm tích hợp | job 15 phút background-job · ops-fe → lms-be GET kết quả, export · lms-fe → lms-be đọc version 0 |
| Ghi chú | Gồm phần nhỏ của story Campaign phía học viên (BR-19.6) vì chỉ kiểm được khi đã có đóng băng. |

## Chủ component dùng chung
Component do nhiều Unit chạm: Unit chủ dựng khung, Unit khác thêm phần của mình và phải có đường phụ thuộc tới Unit chủ.

| Component | Unit chủ | Unit mở rộng |
|---|---|---|
| GamificationConfig, GamificationSettingsOpsApi, OpsSettingsPage, OpsGamificationModule, OpsGamificationApiClient, OpsPermissionCatalog | U0 | U3, U4, U8, U10, U13, U14, U15 |
| GamificationEngine, LearnerDirectory | U1 | U6, U8, U10 |
| GamificationOpsDataApi | U4 | U13, U14, U17 |
| LearnerGamificationApi, LmsGamificationFeature, LmsAppShellIntegration, LmsGamificationVisibility, LmsGamificationApiClient | U5 | U2, U6, U7, U9, U11, U12, U16, U17 |
| LeaderboardComputation, LeaderboardService | U11 | U12, U14, U16, U17 |
| CampaignLeaderboard | U16 | U17 |

## AC nghiệm thu ở Unit khác
| AC / BR | Thuộc story | Nghiệm thu ở | Vì sao |
|---|---|---|---|
| BR-14.13 phần số campaign đang chạy trong popover tắt | Hai công tắc | U15 | Cần dữ liệu campaign |
| Quyền "Xem danh sách học viên và hạng" hiện trên màn role | Phân quyền | U4 | Quyền chỉ xuất hiện khi có endpoint đầu tiên dùng nó (ADR-002) |
| BR-19.6 học viên xem kết quả đã đóng băng | Campaign phía học viên | U17 | Cần đóng băng |
| BR-10.7 khoá tiêu chí hạng khi tắt Points | Cấu hình điểm | U10 | Cần khối Levels |

## Walking skeleton (ngoại lệ có ký, Q3)
Intent chạm ba repo (lms-be, ops-fe, lms-fe) và năm app lms-be. Theo quy tắc, Unit gốc phải là lát mỏng qua mọi điểm tích hợp; ở đây là **ngoại lệ có ký** (Q3, BE lead): U0 là lát skeleton của nhánh Ops (ops-fe → lms-be → PostgreSQL/Redis/Casbin) và đã có thiết kế Construction, nên giữ thay vì dựng Unit gốc mới. Mỗi điểm tích hợp còn lại có một Unit gần gốc nhất trong DAG (ít Unit tổ tiên nhất) chạy thật đầu-cuối, không mock; đây là topo, không phải thứ tự làm:

| Điểm tích hợp | Unit đầu tiên chạy thật |
|---|---|
| ops-fe → lms-be, guard + Casbin | U0 |
| Hook luồng học → Kafka → event-processor → ledger | U1 |
| lms-fe → lms-be, đọc dữ liệu engine thật | U5 |
| lms-fe → lms-be check-in → Kafka | U2 |
| socket.io gateway + redis-emitter | U6 |
| cron background-job (chạy lại lỗi) | U1 |
| cron background-job → snapshot | U11 |
| job đóng băng | U17 |

## Code Organization (brownfield)
- lms-be: `openspec/conventions/backend.md` § 1, `database.md`; dựng trên nhánh `feature/gamification` (ADR-008); mỗi Bolt một change `run`.
- ops-fe: `.claude/rules/01-code-placement.md` (feature `features/gamification/`, API `apps/ops-fe/src/apis/gamification/`).
- lms-fe: `.claude/rules/01-code-placement.md` (feature `features/gamification/`, `@lms/feature-gamification`), cắt từ nhánh WIP (ADR-015).
