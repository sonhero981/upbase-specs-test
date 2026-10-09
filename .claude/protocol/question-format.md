# Question Format

Cách hỏi và ghi câu trả lời của PO. Bám theo AWS AI-DLC `stage-protocol.md` mục 3. File câu hỏi là nguồn sự thật: mọi câu trả lời, dù PO nói trong chat hay sửa file, cuối cùng đều nằm trong file.

## File
`<thư mục stage>/<slug>-questions.md`, tạo từ `.claude/templates/questions.md`.

```markdown
# <Tên stage>, câu hỏi
Intent: <slug> · Cách trả lời: <Guide me | Edit file | Chat> · Đã trả lời: 2/6

## Q1. <Câu hỏi, một câu, tự giải thích>
Vì sao hỏi: <một dòng: cái gì phụ thuộc vào câu trả lời>
A. <lựa chọn>  [đề xuất, theo KB-11 §2]
B. <lựa chọn>
C. <lựa chọn>
X. Khác, xin nói rõ
Chặn: có | không
[Answer]:
```

## Quy tắc đặt câu hỏi
- Chỉ hỏi câu mà đáp án **làm đổi phạm vi, business rule, dữ liệu, luồng, hoặc quyền**. Không hỏi kỹ thuật cho Dev.
- Tra KB, Swagger, DB và `decisions.md` trước. Có đáp án rồi thì không hỏi. Còn mơ hồ thì hỏi hẹp, nêu đáp án cũ: "Trước đã chốt A ở DEC5, giờ có áp cho trường hợp B không?"
- Mỗi câu tự giải thích. Mã nào xuất hiện thì kèm nội dung: "yêu cầu xuất báo cáo theo nhóm (FR3)", không viết "FR3 còn đúng không?".
- Một dòng *Vì sao hỏi* khi lý do không hiển nhiên.
- Lựa chọn A đến E, tối đa năm, luôn có X. Khi không chắc có lựa chọn nào hợp, thêm "Chưa xác định" để PO không bị ép chọn bừa.
- `[đề xuất]` là đáp án AI thấy hợp lý nhất, kèm nguồn. PO chỉ cần nói "đồng ý hết trừ Q3".
- *Chặn: có* khi thiếu đáp án thì không viết được artifact đúng. Câu chặn còn trống thì stage không đi tiếp.
- Hỏi theo lô tối đa bốn câu. Câu chặn hỏi trước.
- Chọn nhiều được: ghi "chọn nhiều" trong câu hỏi, PO trả lời "A, C".

## Ba cách trả lời
| Cách | PO làm gì | AI làm gì |
|---|---|---|
| Guide me | Trả lời từng lô qua hộp chọn AskUserQuestion, mỗi câu có lối "Khác" để nói bằng lời | Ghi vào file ngay sau mỗi lô |
| Edit file | Mở file, điền `[Answer]:`, nói "xong" | Đọc file, liệt kê câu còn trống, hỏi tiếp |
| Chat | Nói tự nhiên, nhiều câu một lúc | Trích quyết định, ghi vào đúng câu, trình lại danh sách để PO xác nhận |

Hỏi cách trả lời một lần cho cả intent, ghi vào `state.md`. Stage sau nói một dòng: "Đang hỏi theo cách anh/chị chọn: Guide me. Muốn đổi thì nói." PO đổi giữa chừng thì ghi lại.

## Ghi câu trả lời
- Nguyên văn lời PO sau `[Answer]:`, kể cả khi chọn bằng chữ cái: `A, "tính theo lượt ghi danh như SIS đang làm"`.
- Diễn giải của AI, nếu cần, dòng dưới: `Hiểu là: ...`.
- PO uỷ quyền: `[Answer]: [uỷ quyền] "tuỳ anh", chọn A theo đề xuất`. Nói với PO một dòng: "Anh/chị để tôi chọn Q2, tôi chọn A. Muốn khác thì nói."
- Không bao giờ tự điền `[Answer]:` khi PO chưa nói.

## Soát sau khi có câu trả lời
- Từ mơ hồ: "tuỳ", "chắc là", "có thể", "cả hai". Hỏi lại cho tới khi rõ.
- Mâu thuẫn giữa các câu, hoặc với `decisions.md`: trình hai câu cạnh nhau, giải thích vì sao vênh, hỏi một câu chốt. Không tự chọn một bên.
- Thiếu dữ kiện để sinh artifact: hỏi tiếp, đánh số tiếp.
- Đáp án không khớp lựa chọn nào và không phải "Khác" có lời: hỏi PO muốn chọn gì.

## Xác nhận tóm tắt
Khi mọi câu đã trả lời và stage có summary confirmation:
- Thêm mục `## Consolidated Summary` vào cuối file: gạch đầu dòng, mỗi câu một dòng, nội dung đã chốt.
- Hỏi bằng hộp chọn: **Looks correct**, sinh artifact từ những điều này. **Request changes**, sửa một vài câu trước.
- Request changes: hỏi "sửa gì" nếu chưa nói, sửa file, xoá tóm tắt cũ, hỏi lại.
- Chỉ sinh artifact sau Looks correct.

## Thẻ nguồn trong artifact nội bộ
| Thẻ | Nghĩa |
|---|---|
| `[desc]` | Lời yêu cầu gốc trong `inputs/` |
| `[Q3]` | Câu trả lời số 3 của stage này. Stage khác ghi `[2.3 Q3]` |
| `[KB-04 §3]` | Nguồn trong KB |
| `[DEC5]` | Quyết định đã ghi |
| `[assumption]` | Giả định, chưa xác nhận |
| `[suy ra]` | AI suy luận từ nguồn, không phải câu chữ trực tiếp |

Mỗi khối khẳng định trong artifact nội bộ có ít nhất một thẻ. Nội dung không có nguồn thì bỏ, hoặc hỏi, hoặc đưa vào Assumptions & Open Questions với `[assumption]`. Không nâng assumption thành fact ở stage sau khi PO chưa xác nhận.
