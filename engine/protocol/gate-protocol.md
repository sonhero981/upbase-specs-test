# Gate Protocol

Mọi stage kết thúc bằng một approval gate. Bám theo AWS AI-DLC `stage-protocol.md` mục 1 và 2. Gate để chặn sai sót ở từng tầng, không phải thủ tục.

## Trước khi mở gate
- `po-tools.py check` không còn cảnh báo, hoặc cảnh báo còn lại đã có lý do. Checklist của stage đã đạt mục blocking. Review độc lập đã xong nếu stage có.
- Đánh dấu stage `[?]` trong `state.md`.

## Thứ tự tại gate
1. Thông điệp hoàn thành.
2. Câu hỏi bài học, nếu profile bật learnings, hỏi thành một lượt riêng.
3. Câu hỏi duyệt.

PO cần đọc kết quả trước rồi mới biết điều gì đáng nhớ. Hỏi bài học trước thông điệp hoàn thành là hỏi khi PO chưa thấy stage làm ra gì.

## Thông điệp hoàn thành, năm phần, đúng thứ tự
1. Tiêu đề: `# <Tên stage> hoàn thành`.
2. Bảng artifact: tên file, nội dung tóm tắt bằng số (số FR, số US, số câu đã trả lời). Số lấy từ script khi có, không tự đếm. Không có lời dặn kiểu "xin xem lại".
3. Kết quả review nếu có: READY hoặc NOT-READY, rồi từng finding còn mở trong sổ finding: mã, mức, vị trí, vấn đề, hành động.
4. Đường dẫn để mở: thư mục của stage.
5. Một câu nói duyệt xong thì sao: stage kế là gì, ai làm gì tiếp.

Lần đầu trong intent, thêm một dòng: profile, depth, cách trả lời đang dùng, và cách đổi.

## Câu hỏi bài học
Đưa các dòng mới của stage trong `memory.md` thành danh sách chọn, hỏi "Có gì cần nhớ cho lần sau không?" với hai lựa chọn Không có, Thêm ghi chú. Hỏi kể cả khi danh sách rỗng. Dòng được giữ ghi theo `stage-protocol.md` bước 6.

## Câu hỏi duyệt
Hộp chọn AskUserQuestion. Mỗi lựa chọn ghi rõ hệ quả. Lựa chọn khuyến nghị đứng đầu. Approve nêu tên stage kế tiếp.

| Lựa chọn | Khi nào có | Hệ quả |
|---|---|---|
| **Approve** | Luôn | Ghi chép sau Approve bên dưới. Finding còn mở ghi *Accepted risk*. Sang stage kế |
| **Request Changes** | Luôn | `[R]`. Lời PO là phản hồi. Sửa, chạy lại review nếu artifact đổi, trình lại gate. Đếm số lần |
| **Accept as-is** | Từ lần Request Changes thứ ba. Báo trước từ lần thứ hai | Như Approve, ghi "chấp nhận có điều kiện" và điều kiện |
| **Add [stage]** | Ideation và Inception, khi có stage bị bỏ qua mà stage hiện tại thấy cần | Thêm stage vào `state.md`, nói một dòng, tiếp tục |
| **Reject Initiative** | Chỉ ở 1.7 | Kết thúc intent, ghi lý do, `state.md` chuyển Archived |

Stage 2.41 HLD Brief là **Alignment gate**: Approve chỉ khi bảng sign-off mục 12 của file trong repo có Design PIC, Tech PIC, QA PIC ghi "Đồng ý" hoặc "Có ý kiến"; PIC tự ghi, hoặc PO ghi theo tin nhắn xác nhận lưu trong `decisions.md`. Một PIC ghi "Yêu cầu sửa" là Request Changes. Thiếu chữ ký thì PO chọn Accept as-is kèm lý do, hoặc chờ. Publish Lark chỉ sau Approve.

Profile M: stage 1.1 và 1.4 duyệt chung một gate. Thông điệp hoàn thành gộp hai artifact. Request Changes nêu rõ sửa artifact nào. Profile M không chạy 1.7, nên phase check Ideation chạy ở gate chung này: năm điều kiện Ideation trong `engine/templates/phase-check.md`, ghi `verification/phase-check-ideation.md`.

## Đọc câu trả lời của PO
- Một lựa chọn rõ ("1", "approve", "duyệt", "ok"): ghi đúng lựa chọn đó.
- Duyệt kèm chỉ thị ("ok nhưng đổi tên trường X"): ghi Approve, làm việc được yêu cầu, nói một dòng đã làm gì. Không hỏi lại.
- Duyệt kèm dừng ("duyệt, hôm nay dừng"): ghi Approve, ghi *Parked* vào `state.md`, nói cách tiếp tục bằng `/po`.
- Yêu cầu sửa không kèm duyệt: ghi Request Changes, lời PO là phản hồi. Chỉ hỏi "sửa gì" khi PO chưa nói.
- Nhờ một việc mà không duyệt ("thêm giúp một dòng ví dụ"): làm việc đó, giữ gate mở, trình lại. Không ghi Approve.
- Chọn ô "Khác" mà không viết gì: không ghi nhận, hỏi lại một câu.
- Câu hỏi: trả lời rồi kết thúc lượt. Lượt kế tiếp mới là quyết định.
- Không rõ ("hmm", "để xem"): hỏi một câu ngắn. Không suy đoán là duyệt.
- Làm lại stage, nhảy stage, bắt đầu intent mới: không phải câu trả lời gate. Làm theo `/po`.

## Ghi chép sau Approve
Chạy một lệnh, làm trọn mọi việc ghi chép:

```
python3 engine/scripts/po-tools.py approve intents/<slug> <slug-stage> --words "<lời PO nguyên văn>"
```

Script làm theo thứ tự, và từ chối nếu stage không ở `[?]`:
1. Frontmatter artifact: `version` theo quy tắc phiên bản dưới đây, `status: approved`, `approved_at`.
2. Chụp bản duyệt vào `archive/<slug>/<artifact>-v<version>-<YYYYMMDD>.md`. Từ chối ghi đè. File trong archive không bao giờ sửa.
3. `decisions.md`: một dòng DEC, cột *Nguyên văn* là lời PO không sửa chữ, cột *Người quyết* là tên trong `git config user.name`, kèm giờ.
4. `state.md`: `[x]`, bảng Versions, dòng Log có giờ và tên, stage kế và việc kế tiếp.
5. In dòng tiến độ: `Progress: <đã xong>/<tổng stage của profile> | <PHASE> <đã xong>/<tổng> · Next: <tên stage kế>`.

Sau script, AI tự làm hai việc: finding Accepted risk ghi vào bảng Accepted risks của `decisions.md` kèm lý do; sổ finding của stage chuyển các finding còn mở sang Accepted risk. Không chạy được python thì làm tay đủ năm việc trên.

### Quy tắc phiên bản
- Bản nháp là 0.x. Mỗi lần PO trả lời xong một đợt câu hỏi hoặc yêu cầu sửa thì tăng số phụ: 0.1, 0.2.
- Lần duyệt đầu tiên của một artifact: 1.0.
- Mỗi lần duyệt lại sau đó, do Request Changes sau duyệt hay change request: tăng số phụ, 1.0 thành 1.1.
- Intent cũ đã duyệt ở 0.x trước quy tắc này giữ nhánh 0.x và tăng số phụ.

### Gắn tag cho bản bàn giao
Duyệt `hld-brief` hoặc `prd`: script in tên tag gợi ý dạng `<intent>/prd-v1.0`. Sau khi commit, gắn tag và push tag. Agent của Dev đọc PRD theo tag nên luôn lấy đúng bản đã duyệt, xem mục "Bàn giao cho Design, Tech, QA" trong README. Duyệt `prd` xong thì chạy `/po-stories` để sinh Story List cho Jira.

## Sửa lựa chọn bị ghi nhầm
PO nói vừa rồi chọn nhầm:
- Ghi nhầm Request Changes: trình lại gate, không đổi file.
- Ghi nhầm Approve: thêm một dòng DEC đính chính trỏ về DEC cũ, đưa stage từ `[x]` về `[?]`, trình lại gate. Bản chụp trong `archive/` giữ nguyên làm lịch sử; lần duyệt sau dùng nhãn khác.

## Sau Request Changes
- Sửa đúng phần PO nêu, không viết lại toàn bộ. Nói đã đổi gì.
- Artifact đổi và stage có reviewer: chạy lại review trước khi trình lại.
- Trình lại gate với thông điệp hoàn thành mới.
- Không để stage ở `[R]` mà không trình lại gate.
