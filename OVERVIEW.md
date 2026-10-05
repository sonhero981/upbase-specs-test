# PO Workflow — tổng quan phương pháp

Quy trình làm việc giữa PO/BA và AI để biến một yêu cầu thô thành PRD đủ chi tiết cho Dev, QA và Design dùng ngay.

Tài liệu này mô tả **phương pháp**. Muốn biết cài đặt và chạy lệnh thì đọc [HUONG-DAN-SU-DUNG.md](HUONG-DAN-SU-DUNG.md).

---

## Nguyên tắc nền

**AI đề xuất, người quyết.** AI đọc knowledge base, tra Swagger, dựng bản nháp, chỉ ra chỗ mâu thuẫn. PO chốt mọi quyết định về phạm vi, nghiệp vụ và ưu tiên. Không có quyết định nào AI tự chốt thay.

Ba nguyên tắc đi kèm:

**Không bịa.** Thiếu thông tin nhẹ thì ghi `Assumption`. Thiếu tới mức ảnh hưởng phạm vi, business rule, dữ liệu hay luồng thì ghi `Open Question` và dừng hỏi. Ô không suy được đánh dấu `❓BA`, không điền bừa cho đủ chỗ.

**Dừng ở mức phân tích.** Cần biết một cơ chế kỹ thuật có tồn tại không thì hỏi PO, không tự đào Swagger rồi kết luận. Có endpoint không có nghĩa là có tính năng.

**Knowledge base là bản chụp, không phải chân lý.** Schema DB, Swagger và User Guide là nguồn sống. Yêu cầu chạm tới vùng nào thì đọc lại nguồn vùng đó, quá một tháng kể từ lần đối chiếu cuối cũng phải đọc lại.

---

## Năm giai đoạn

| Giai đoạn | Bước | Kết quả | Gate |
|---|---|---|---|
| Làm rõ yêu cầu | 1–3 | Bản yêu cầu đã làm rõ, danh sách câu hỏi mở | — |
| BRD | 4 | Business Requirement Document | Gate 1 |
| Phân tích ảnh hưởng | 5–6 | Related Map, Impact Matrix | Gate 2 |
| Solution | 7–8 | So sánh phương án, quyết định kỹ thuật | Gate 3 |
| PRD | 9 | PRD theo template công ty | Gate 4 |

Sau Gate 4: publish lên Lark, và viết User Guide khi Dev làm xong.

Bước 9 chia bốn chặng nhỏ, mỗi chặng có việc riêng:

```
9A   Khung PRD + danh sách US        → dừng, PO confirm danh sách
9A+  Chia Unit, nhóm bàn giao
9B   Field Intake                     → dừng, PO trả lời bảng field
9C   Viết chi tiết từng US
```

---

## Khái niệm riêng

| Khái niệm | Nghĩa |
|---|---|
| **Gate** | Điểm PO duyệt một artifact. Ba trạng thái: `Approved` · `Approved with Notes` · `Need Revision`. Trượt thì quay về **đúng bước cụ thể**, không làm lại từ đầu |
| **Điểm dừng** | Chỗ AI phải hỏi trước khi đi tiếp, nhưng không phải duyệt artifact. Có ba điểm dừng: chốt phạm vi liên quan, confirm danh sách US, trả lời bảng field |
| **Cỡ yêu cầu** | `S` · `M` · `L`. Quyết định đi mấy bước và qua mấy Gate |
| **Unit** | Nhóm US làm độc lập được. Trả lời câu hỏi Dev hỏi đầu tiên: làm cái nào trước |
| **Change request** | Yêu cầu đổi giữa chừng. Mỗi CR ghi rõ điểm re-entry: quay về bước nào, artifact nào phải sửa, Gate nào duyệt lại |
| `❓BA` | Ô chưa rõ, có người chịu trách nhiệm điền. Không dùng làm dữ kiện |
| `[suy ra]` | AI suy luận, không phải câu chữ trực tiếp từ nguồn |

---

## Phân cỡ để không bắt yêu cầu nhỏ chạy đủ chín bước

Một yêu cầu sửa nhãn trên một màn mà phải qua BRD, Impact Matrix, Solution Comparison rồi mới tới PRD là cách chắc chắn khiến người dùng bỏ quy trình và viết tay cho nhanh.

Sau Bước 2, AI quét nhanh knowledge base, DB và Swagger rồi phân cỡ:

| Cỡ | Dấu hiệu, phải đúng tất cả | Đường đi | Gate |
|---|---|---|---|
| **S** | Chạm 1 màn · không đổi data model · không đổi business rule hiện có · không chạm module khác | Bước 1–3 → PRD rút gọn 1 US | Gate 4 |
| **M** | Chạm tối đa 2 module · thêm field nhưng không đổi quan hệ bảng · không có conflict · đã rõ hướng giải | Bước 1–6 → Bước 9 | Gate 1, 2, 4 |
| **L** | Chạm từ 3 module trở lên, hoặc đổi data model, hoặc có conflict, hoặc có nhiều hướng giải | Đủ 9 bước | Đủ 4 Gate |

Ba quy tắc bắt buộc:

1. Nghi ngờ thì lên cỡ. Không chắc `S` hay `M` thì chọn `M`
2. Phát hiện giữa chừng thì nâng cỡ ngay, không đi tiếp đường cũ
3. Echo phân cỡ kèm lý do trước khi chạy. PO có quyền đổi cỡ

---

## Artifact sinh ra

```
.claude/projects/<tên project>/
├── project-context.md          bối cảnh, phạm vi, ràng buộc, mapping Lark
├── project-decisions.md        nhật ký mọi quyết định đã chốt
├── docs/
│   ├── brd/                    BRD theo version
│   ├── prd/                    PRD theo version
│   └── user-guide/             viết sau khi Dev xong
├── design/                     ảnh màn đã chốt + order.txt
└── working/
    ├── raw-inputs/             yêu cầu gốc, change-requests.md
    ├── ai-drafts/              bản làm rõ yêu cầu
    ├── open-questions/         câu hỏi mở theo nhóm
    ├── impact-analysis/        related map, impact matrix
    └── solution-options/       so sánh phương án
```

`project-decisions.md` là bộ nhớ của dự án. AI tra file này để không hỏi lại câu đã có đáp án.

---

## Cơ chế giữ chất lượng

**Bốn Gate cộng ba điểm dừng.** Ở cỡ `L` là bảy chỗ PO phải trả lời trước khi AI đi tiếp.

**Trạng thái Gate có ba mức, không phải hai.** `Approved with Notes` cho phép đi tiếp kèm danh sách việc còn treo, thay vì bắt chọn giữa duyệt sạch và làm lại.

**Điểm re-entry khi có change request.** Yêu cầu đổi ở Bước 9 không có nghĩa là làm lại từ Bước 1. CR ghi rõ artifact nào hết hiệu lực, Gate nào duyệt lại.

**Đối chiếu sau khi publish.** API trả `200` không có nghĩa nội dung vào đúng chỗ. Sau mỗi lần đẩy lên Lark, đếm lại số heading, số bảng, số sơ đồ, số ảnh và so với file nguồn.

**Dọn dấu vết quy trình trước khi bàn giao.** Ký hiệu nội bộ như `9A`, `Gate 3`, nhãn chờ, ghi chú thay đổi giữa chừng đều là giàn giáo. Dev và QA không tra được chúng. Trạng thái duyệt ghi ai duyệt, không ghi Gate mấy.

---

## Knowledge base

15 file, chia ba nhóm:

| Nhóm | File | Nội dung |
|---|---|---|
| Nghiệp vụ | `01`–`11` | Course · Question Bank · Assessment · Class · Grading · User · Learning Experience · Certificate · Notification · Storyline · Dashboard |
| Kỹ thuật | `12`–`14` | Data Model 85 bảng · Mail Events 30 mail · API Surface 708 operation |
| Định hướng | `15` | UpLnD Platform, bốn portal, chỗ đóng cứng |

Knowledge base phủ khoảng một nửa hệ thống. Ops có 25 nhóm API và LMS có 8 nhóm không nằm trong User Guide. Yêu cầu chạm vùng chưa phủ thì ghi `❓BA`, không kết luận.

---

## Quy trình này hợp với ai

Hợp khi:

- Bạn là PO hoặc BA, viết tài liệu cho một hệ thống đã chạy, có người dùng thật và dữ liệu cũ
- Yêu cầu chạm nhiều module và cần biết trước nó phá cái gì
- Tài liệu phải theo template có sẵn của công ty
- Cần truy được vì sao một quyết định được chốt, sau vài tháng vẫn tra lại được

Chưa hợp khi:

- Dựng sản phẩm mới hoàn toàn, chưa có hệ thống để phân tích ảnh hưởng
- Chỉ cần bản nháp nhanh để thảo luận, không cần bàn giao
- Quy trình công ty không có bước duyệt tài liệu

---

## So với các phương pháp khác

| | PO Workflow | AI-DLC | Spec generation |
|---|---|---|---|
| Phủ tới đâu | Yêu cầu → PRD → User Guide | Inception → Construction → Operations | Yêu cầu → spec |
| Người dùng | PO hoặc BA | Cả team, có dev | Bất kỳ ai |
| Phân tích ảnh hưởng tới module khác | Có, là một giai đoạn riêng | Không có | Không có |
| So sánh phương án trước khi chốt | Có, là một giai đoạn riêng | Không có | Không có |
| Checkpoint | 4 Gate, co giãn theo cỡ yêu cầu | Cố định cho mọi đơn vị công việc | 3 phase gate |
| Xử lý khi thiếu thông tin | `❓BA` · `Assumption` · `Open Question` | Không có cơ chế riêng | Không có cơ chế riêng |
| Template đầu ra | Template PRD của công ty | Chuẩn riêng | Chuẩn riêng |

Điểm mạnh của quy trình này nằm ở hai giai đoạn mà các phương pháp kia không có: phân tích ảnh hưởng và so sánh phương án. Cả hai chỉ có nghĩa khi hệ thống đã chạy và việc thêm một tính năng có thể phá thứ đang hoạt động.

Đổi lại, nó không nói gì về việc viết code, chạy test hay triển khai. Phần đó thuộc về Dev.

---

## Đầu ra thực tế

Dự án Gamification cho UpLMS, cỡ `L`, chạy đủ chín bước và bốn Gate:

| | |
|---|---|
| Thời gian | 23/09/2026 đến 05/10/2026 |
| Change request | 10 |
| Phiên bản BRD | 6 |
| Phiên bản PRD | 8 |
| US trong PRD | 15, chia 5 Unit |
| Business rule | 137 |
| Sơ đồ | 5, viết bằng Mermaid trong chính file nguồn |
| Ảnh design | 7 |

PRD cuối cùng: 139 heading, 90 bảng, publish lên Lark với đầy đủ sơ đồ và ảnh.
