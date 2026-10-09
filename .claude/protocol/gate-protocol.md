# Gate Protocol

Mọi stage kết thúc bằng một approval gate. Bám theo AWS AI-DLC `stage-protocol.md` mục 1 và 2. Gate để chặn sai sót ở từng tầng, không phải thủ tục.

## Trước khi mở gate
- Checklist của stage đã đạt mục blocking. Review độc lập đã xong nếu stage có.
- Câu hỏi learnings đã hỏi nếu profile bật.
- Đánh dấu stage `[?]` trong `state.md`.

## Thông điệp hoàn thành, năm phần, đúng thứ tự
1. Tiêu đề: `# <Tên stage> hoàn thành`.
2. Bảng artifact: tên file, nội dung tóm tắt bằng số (số FR, số US, số câu đã trả lời). Không có lời dặn kiểu "xin xem lại".
3. Kết quả review nếu có: READY hoặc NOT-READY, rồi từng finding còn mở: mã, mức, vị trí, vấn đề, hành động. Mã finding ổn định qua các lần review.
4. Đường dẫn để mở: thư mục của stage.
5. Câu hỏi duyệt bằng hộp chọn AskUserQuestion. Mỗi lựa chọn ghi rõ hệ quả. Lựa chọn Approve nêu tên stage kế tiếp.

Lần đầu trong intent, thêm một dòng: profile, depth, cách trả lời đang dùng, và cách đổi.

## Lựa chọn tại gate
| Lựa chọn | Khi nào có | Hệ quả |
|---|---|---|
| **Approve** | Luôn | Ghi DEC. Finding còn mở ghi *Accepted risk*. Chụp bản duyệt. `[x]`. Sang stage kế |
| **Request Changes** | Luôn | `[R]`. Lời PO là phản hồi. Sửa, chạy lại review nếu artifact đổi, trình lại gate. Đếm số lần |
| **Accept as-is** | Từ lần Request Changes thứ ba. Báo trước từ lần thứ hai | Như Approve, ghi "chấp nhận có điều kiện" và điều kiện |
| **Add [stage]** | Ideation và Inception, khi có stage bị bỏ qua mà stage hiện tại thấy cần | Thêm stage vào `state.md`, nói một dòng, tiếp tục |
| **Reject Initiative** | Chỉ ở 1.7 | Kết thúc intent, ghi lý do, `state.md` chuyển Archived |

Stage 2.41 HLD Brief là **Alignment gate**: Approve chỉ khi bảng sign-off mục 12 của file trong repo có Design, Dev, QA ghi "Đồng ý" hoặc "Có ý kiến"; lead tự ghi, hoặc PO ghi theo tin nhắn xác nhận lưu trong `decisions.md`. Một lead ghi "Yêu cầu sửa" là Request Changes. Thiếu chữ ký thì PO chọn Accept as-is kèm lý do, hoặc chờ. Publish Lark chỉ sau Approve.

Profile M: stage 1.1 và 1.4 duyệt chung một gate. Thông điệp hoàn thành gộp hai artifact. Request Changes nêu rõ sửa artifact nào.

## Đọc câu trả lời của PO
- Một lựa chọn rõ ("1", "approve", "duyệt", "ok"): ghi đúng lựa chọn đó.
- Duyệt kèm chỉ thị ("ok nhưng đổi tên trường X"): ghi Approve, làm việc được yêu cầu, nói một dòng đã làm gì. Không hỏi lại.
- Duyệt kèm dừng ("duyệt, hôm nay dừng"): ghi Approve, ghi *Parked* vào `state.md`, nói cách tiếp tục bằng `/po`.
- Yêu cầu sửa không kèm duyệt: ghi Request Changes, lời PO là phản hồi. Chỉ hỏi "sửa gì" khi PO chưa nói.
- Câu hỏi: trả lời rồi kết thúc lượt. Lượt kế tiếp mới là quyết định.
- Không rõ ("hmm", "để xem"): hỏi một câu ngắn. Không suy đoán là duyệt.
- Làm lại stage, nhảy stage, bắt đầu intent mới: không phải câu trả lời gate. Làm theo `/po`.

## Ghi chép sau Approve
1. `decisions.md`: một dòng DEC cho quyết định gate, cột *Nguyên văn* là lời PO không sửa chữ. Finding Accepted risk ghi vào bảng Accepted risks kèm lý do.
2. `archive/<slug>/<artifact>-v<N>-<YYYYMMDD>.md`: bản sao y nguyên artifact tại thời điểm duyệt, chép bằng `python3 .claude/scripts/po-tools.py archive <intent-dir> <slug> <artifact>`; script từ chối ghi đè. File trong archive không bao giờ sửa.
3. `state.md`: `[x]`, bảng Versions, stage kế tiếp, việc kế tiếp.
4. Frontmatter artifact: `status: approved`, `approved_at`, `version` thành số nguyên kế tiếp.
5. Dòng tiến độ: `Progress: <đã xong>/<tổng stage của profile> | <PHASE> <đã xong>/<tổng> · Next: <tên stage kế>`.

## Sau Request Changes
- Sửa đúng phần PO nêu, không viết lại toàn bộ. Nói đã đổi gì.
- Artifact đổi và stage có reviewer: chạy lại review trước khi trình lại.
- Trình lại gate với thông điệp hoàn thành mới.
- Không để stage ở `[R]` mà không trình lại gate.
