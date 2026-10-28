---
intent: 260923-gamification
artifact: test-cases
stage: 2.81 test-cases
version: 1.0
status: approved
approved_at: 2026-10-13 ([GIẢ LẬP] QA lead, DEC-T9)
prd_version: 0.14 + 2.43 Q1–Q4 (DEC-T4)
hld_version: n/a (2.41 [S], intent v1)
scope: US14, US15
consumes: inception/prd/prd.md v0.14, inception/prd-readiness/prd-readiness-questions.md, inception/units-generation/unit-of-work-story-map.md v1.0, inception/contract-design/contract-summary.md v1.0 (Agreed), domain/corner-checklist.md
---
# Test Cases: Gamification, lát Nền tảng (US14 · US15)

Mỗi test case trỏ US và dòng AC (`USn-ACk`, dòng thứ k của bảng "UI / UX / Rule UX / Rule UI" của USn) hoặc BR. Một Unit U0 mang cả hai US. Mã lỗi, shape, quyền lấy đúng `contract-summary.md` (C-01…C-03). Kiểm chặn quyền chạy trên staging (dòng `p` không sinh ở `LOCAL`). Tài khoản: SA = superadmin; V = staff có role chỉ `gr_view_gamification_settings`; E = staff có role `gr_update_gamification_settings`; N = staff không có quyền gamification.

| TC | US | AC / BR | Tiền điều kiện + dữ liệu | Bước | Kết quả mong đợi | Loại | Ưu tiên |
|---|---|---|---|---|---|---|---|
| TC-1 | US14 | US14-AC1 · BR-14.1 · BR-14.6 | Tenant chưa có bản ghi `gamification_settings`; SA | Mở trang Gamification; `GET /gamification/settings` | 200, `is_enabled:false`, `is_visible:false`, `has_been_visible:false`, mốc `null` (C-01). Trang chỉ có công tắc `Gamification` tắt, không có `Visibility in UpLMS` | Happy | P0 |
| TC-2 | US14 | US14-AC1 · US14-AC8 · US14-AC9 · BR-14.1 · BR-14.10 · BR-14.5 | TC-1 xong | Bấm bật `Gamification` | Không popover. `PATCH {is_enabled:true}` 200, `first_enabled_at` = `last_enabled_at` = lúc bật. Báo `Saved` nhỏ, tự ẩn. Không nút lưu. `Visibility in UpLMS` xuất hiện, tắt (chạy ngầm) | Happy | P0 |
| TC-3 | US14 | US14-AC2 · US14-AC3 · BR-14.2 | `Gamification` bật | Quan sát khối chung | `Visibility in UpLMS` hiện, dòng giải thích đúng nguyên văn `Show points, badges and ranks to your users. While this is off, they still accrue but stay hidden.` Không nhãn trạng thái riêng | Happy | P1 |
| TC-4 | US14 | US14-AC6 · US14-AC7 · BR-14.13 | `Gamification` bật, `has_been_visible:false` | Bấm bật `Visibility in UpLMS` → `Show` | Popover nhỏ cạnh công tắc (không modal), tiêu đề `Show gamification to your users?`, nội dung đúng chuỗi PO (2.43). `Show` → `PATCH {is_visible:true}` 200, `has_been_visible:true`, `Saved` | Happy | P0 |
| TC-5 | US14 | US14-AC6 · BR-14.13 | `has_been_visible:true`, `Visibility` đang tắt | Bấm bật `Visibility in UpLMS` | Không popover, lưu ngay, `Saved` (2.43 Q2: chỉ hỏi một lần trong đời tổ chức) | Edge | P1 |
| TC-6 | US14 | US14-AC4 · BR-14.13 | `Gamification` bật | Bấm tắt `Gamification` → `Cancel` | Công tắc về bật, không có request `PATCH` (tab Network), không `Saved` | Negative | P0 |
| TC-7 | US14 | US14-AC4 · US14-AC5 · BR-14.2 · BR-14.5 | `Gamification` bật, `Visibility` bật | Bấm tắt `Gamification` → `Turn off` | Popover tiêu đề `Turn off gamification?`, nội dung đúng chuỗi PO, không có phần campaign (2.43 A4). `PATCH {is_enabled:false}` 200; `Visibility` biến mất khỏi màn; `GET` vẫn `is_visible:true` | Happy | P0 |
| TC-8 | US14 | US14-AC1 · BR-14.2 · BR-14.5 | TC-7 xong | Bật lại `Gamification` | Không popover. `Visibility` hiện lại, bật. `last_enabled_at` = lúc bật lại, `first_enabled_at` không đổi | Happy | P0 |
| TC-9 | US14 | BR-14.2 | (a) `is_enabled:false, is_visible:false`; (b) `is_enabled:false, is_visible:true` (sau TC-7) | `PATCH {is_visible:true}` và `PATCH {is_visible:false}` trực tiếp (curl) ở cả (a), (b) | Cả bốn: 400 `400\|700001`, message `Turn on Gamification before changing Visibility in UpLMS.`; bản ghi không đổi | Negative | P1 |
| TC-10 | US14 | BR-14.10 · BR-14.11 | SA | `PATCH` với `{}`, `{is_enabled:true,is_visible:true}`, `{is_enabled:"yes"}` | Cả ba 422 `422\|000405`; bản ghi không đổi | Negative | P2 |
| TC-11 | US14 | US14-AC9 · BR-14.12 | `Gamification` bật; giả lập 500 cho `PATCH` (DevTools block) | Bấm tắt `Visibility in UpLMS` | Công tắc về giá trị đã lưu, báo lỗi, không `Saved`. Rời trang không cảnh báo | Negative | P1 |
| TC-12 | US14 | BR-14.8 · BR-14.9 | Staging, sau TC-2 | Kiểm DB và Redis | Một dòng `gamification_settings` mỗi tenant, có `tenant_id`, RLS bật; `tenant.timezone = Asia/Ho_Chi_Minh`; key Redis có tiền tố `tenant:{id}:`. Trang không có ô múi giờ | Happy | P1 |
| TC-13 | US14 | BR-14.6 · BR-14.10 | SA, cache đã có (đã `GET`) | `PATCH {is_enabled:false}` rồi `GET` ngay | `GET` trả `is_enabled:false` ngay lần đầu (cache xoá trong cùng request, 2.43 Q3) | Edge | P0 |
| TC-14 | US14 | BR-14.6 | Hai request `GET` đồng thời khi tenant chưa có bản ghi | Gửi song song 2 `GET` | Cả hai 200 cùng giá trị mặc định; DB đúng một dòng | Edge | P2 |
| TC-15 | US15 | US15-AC1 · BR-15.1 · BR-15.5 | Staging sau deploy (Ops khởi động, quét quyền) | SA mở màn tạo / sửa role | Có nhóm `gamification` với `View gamification settings`, `Update gamification settings`; không có màn phân quyền riêng | Happy | P0 |
| TC-16 | US15 | US15-AC2 · BR-15.2 · BR-15.7 | Tài khoản V | Mở trang Gamification; bấm công tắc; `PATCH` bằng curl | Trang mở, thấy công tắc ở trạng thái chỉ xem, không bấm được; `GET` 200; `PATCH` 403 `403\|000000` | Negative | P0 |
| TC-17 | US15 | US15-AC3 · BR-15.7 | Tài khoản E | Bật tắt `Gamification` | Lưu được như TC-2; `GET`, `PATCH` 200 | Happy | P0 |
| TC-18 | US15 | US15-AC5 · BR-15.3 | Tài khoản N | Xem menu Ops; mở thẳng `/gamification`; `GET` bằng curl | Không có mục Gamification trong menu; đường dẫn ra màn 403 sẵn có của Ops; API 403 `403\|000000` | Negative | P0 |
| TC-19 | US15 | BR-15.6 | Tài khoản N, SA gán cho role của N quyền xem | N đăng nhập lại | Hiệu lực theo cơ chế hiện có: sau khi đăng nhập lại (tải `/me`), N thấy mục menu và mở được trang | Edge | P1 |
| TC-20 | US15 | BR-15.4 | Học viên bất kỳ trên UpLMS | Đăng nhập lms-pro | Không có thay đổi nào ở UpLMS do lát này (lms-fe không chạm, ADR-006) | Happy | P2 |
| TC-21 | REG | — | Staging | Mở màn role, màn cache settings, một trang Ops có quyền sẵn | Hoạt động như trước; các nhóm quyền cũ không đổi | Happy | P1 |

## BR hoãn sang Unit sau
| BR | Vì sao hoãn | Kiểm ở |
|---|---|---|
| BR-14.3 | Chạy ngầm ghi nhận điểm, huy hiệu, hạng: lát chưa có luồng ghi nhận | Unit Điểm |
| BR-14.7 | Khoá bốn công tắc US8–US11: lát chưa có các khối đó | Unit Điểm, Huy hiệu, Hạng, Bảng xếp hạng |
| BR-14.4 | Không thông báo hồi tố khi bật Visibility: lát chưa có thông báo (US2); popover chỉ nêu câu chữ (TC-4) | Unit Hiển thị cho học viên |
| BR-15.8 | Khối Campaign chỉ xem khi tắt `Gamification`: US20 ngoài lát | Unit Campaign |
| US15-AC4 | Quyền `Xem danh sách học viên và hạng` chỉ hiện khi có endpoint learners (ADR-002) | Unit Bảng xếp hạng |

## Nguồn thay thế đã dùng
- Không có HLD Brief mục 10 (2.41 `[S]`): dùng contract C-01…C-03 và corner checklist domain.
- PRD "6/ Conner case" của US14, US15 trống ("QA điền"): Edge lấy từ corner checklist (đồng thời, cache, tạo mặc định).

## Assumptions & Open Questions
| # | Nội dung | Loại | Chặn | Owner |
|---|---|---|---|---|
| A1 | Kết quả mong đợi dùng câu trả lời 2.43 Q1–Q4 khi PRD chưa lên version (DEC-T4); CR đổi khác thì mở lại TC liên quan | Assumption | Không | QA lead |

## Sign-off
| Vai trò | Tên | Trạng thái | Ngày |
|---|---|---|---|
| QA lead | [GIẢ LẬP] chưa có tên | Approve | 2026-10-13 |
