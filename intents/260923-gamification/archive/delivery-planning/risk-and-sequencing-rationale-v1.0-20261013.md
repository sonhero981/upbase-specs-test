---
intent: 260923-gamification
artifact: risk-and-sequencing-rationale
stage: 2.9 delivery-planning
version: 1.0
status: approved
approved_at: 2026-10-13 ([GIẢ LẬP] họp, DEC-T10)
---
# Risk and Sequencing Rationale: Gamification, lát Nền tảng

## Thứ tự
Một Bolt. Trong B01: lms-be trước (migration → entity → service → controller → curl), ops-fe sau (types → API → module → menu → trang). ops-fe mock theo C-01, C-02 (`// TODO(api)`) tới khi lms-be lên staging.

## Rủi ro
| # | Rủi ro | Khả năng | Ảnh hưởng | Giảm thiểu |
|---|---|---|---|---|
| R1 | Path controller sai làm dòng `p` không khớp route → endpoint mở | Trung bình | Cao | `@Controller('gamification')` một đoạn (contract ràng buộc 3.5); TC-18 trên staging |
| R2 | Không test được chặn quyền ở local (`NODE_ENV=LOCAL` bỏ quét) | Chắc chắn | Trung bình | Kiểm TC-15…TC-19 trên staging trước khi đóng Bolt |
| R3 | `backend.md` § 2 chưa ghi ngoại lệ → reviewer MR từ chối `tags` có mã | Trung bình | Thấp | BE lead ghi ngoại lệ trước khi review MR (team-allocation) |
| R4 | Design gốc `upbase-221099` chưa cập nhật theo ADR-002…005 → dev BE khác làm Unit sau theo bản cũ | Trung bình | Trung bình | BE lead cập nhật design gốc trong B01 |
| R5 | PRD chưa lên version với câu trả lời 2.43 | Thấp | Thấp | DEC-T4; PO chạy `/change-request` |

## Release constraints
- Không bật Gamification trên production trong B01 (chưa có gì để ghi nhận); bật trên staging để test.
- MR lms-be theo `openspec/conventions/git.md` (nhánh sprint rồi `staging`), PR ops-fe vào `staging`.
