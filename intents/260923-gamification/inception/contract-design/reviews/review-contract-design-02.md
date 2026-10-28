Kết luận: READY

Reviewer: aidlc-architecture-reviewer-agent · Stage 2.8 contract-design v1.1 · Vòng 2 · Đã tự kiểm lại từng sửa đổi trong `contract-summary.md` (script riêng cho YAML, quyền, cạnh DAG; đối chiếu code `origin/feature/gamification`).

**Tình trạng finding vòng 1**

| Mã | Mức trước | Giờ | Ghi chú đã kiểm |
|---|---|---|---|
| R-01 | Chặn | Đã sửa | Script đọc `x-permission.tags` của mọi operation Ops: GET `point-rules`, `badges`, `levels`, `leaderboard-settings`, `leaderboard-preview` chỉ còn `view_settings`, `update_settings`; C-01 và GET campaign (list, chi tiết) giữ ba mã; C-09, C-10, C-12 chỉ `view_learners`; mọi ghi chỉ `update_settings`. Khớp BR-15.7 và ADR-002. |
| R-02 | Nên sửa | Đã sửa | C-05 ghi "Không trả 630011"; mục "Lệch … WP3" ở đầu file ghi bỏ `630011` và bỏ việc WP3 tự tắt tiêu chí BADGES; C-06 giữ 630007 chỉ cho tắt trực tiếp tiêu chí đang chạy cuối. Khớp BR-10.7, BR-10.8. |
| R-03 | Nên sửa | Đã sửa | C-13 `GamificationMe` có `boards` (bảng đang chạy, theo thứ tự) và `default_board`; mã mới `404\|630016` cho bảng tắt/khoá, khác `630012`; bảng mã lỗi và C-19 mô tả khớp. |
| R-04 | Nên sửa | Đã sửa | `metadata: PaginationMeta` có trong `Board` (C-19, C-21 dùng lại) và `CampaignResult` (C-12); `next_page` kiểu boolean đúng `response.dto.ts:12-18`; bằng chứng Q4 ghi đúng khoá thực tế `caching_setttings` và nói gamification chốt `items`. |
| R-05 | Nên sửa | Đã sửa | S-03 (`x-transport: in-process-sync`) có `engine.record` (trích `gamification-engine.service.ts:44-47`, `gamification-record.types.ts` với bốn trạng thái RECORDED, SKIPPED, DUPLICATE, FAILED: đúng code), `awardBackfill`, `AchievementNotifier.notify` (adapter no-op ở U1, thay ở U6), `computeRange`, `writeSnapshot`/`switchVersion`. "Phủ cạnh DAG" vẫn 28/28, cạnh in-process trỏ S-03. |
| R-06 | Nên sửa | Đã sửa | `gamification_failed_events` thêm cột `kind` (RECORD, CHECKIN, BADGE_BACKFILL, BADGE_BACKFILL_JOB, mặc định RECORD cho dòng WP1); S-03 có bảng định tuyến chạy lại từng loại; A-01, A-02, A-04, C-16 và S-02 (điều kiện đóng băng chỉ tính RECORD, CHECKIN) cập nhật nhất quán. |
| R-07 | Ghi nhận | Đã sửa | POST, PUT, DELETE campaign cùng trả `630001` khi Gamification tắt; `630015` chỉ cho khoá theo trạng thái. |
| R-08 | Ghi nhận | Đã sửa | `details` và `current_points` có thuộc tính. |
| R-09 | Ghi nhận | Đã sửa | Ghi hai mã 404 cần exception mới; dẫn chứng đã đúng `libs/modules/src/lib/kafka/kafka.service.ts:81-88`. |

**Finding mới (không chặn)**

| Mã | Mức (Chặn/Nên sửa/Ghi nhận) | Vị trí | Vấn đề | Hành động |
|---|---|---|---|---|
| R-10 | Ghi nhận | C-20, C-21 (mô tả/response 404); S-03 `writeSnapshot` | Mã `630016` chỉ nêu ở bảng mã lỗi và mô tả C-19; C-20 và C-21 chưa ghi trong phần `responses` 404 nó áp cho trường hợp nào (và C-21 `/campaigns` ghi "Leaderboard tắt → 404" chưa nói 630012 hay 630016). `writeSnapshot(version, rows, scope)` chưa kiểu hoá `rows`. | Ghi mã cụ thể trong 404 của C-20, C-21; kiểu hoá `rows` bằng `LeaderboardRow` (3.1 có thể làm). |

**Công cụ**

| Hạng mục | Kết quả |
|---|---|
| Sensor `tech-tools.py check --stage=contract-design` | Đạt. |
| Script riêng | 28 khối `yaml` (S-01, C-01…C-21, A-01…A-04, S-02, S-03) parse được; mọi operation REST có `operationId`, `x-curl`, `responses`; "Phủ cạnh DAG" khớp 28/28 cạnh của khối `units:` 2.7. |

**Tóm tắt:** Chặn về quyền đã sửa đúng theo BR-15.7 và ADR-002; các luật WP3 trái BR-10.8, danh sách bảng cho lms-fe, metadata phân trang, contract in-process (S-03) và định tuyến chạy lại theo `kind` đều đã vào contract và nhất quán với nhau. Còn một ghi nhận nhỏ (R-10). Contract đủ để BE lead ký "Approved by".
