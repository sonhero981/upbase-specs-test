# Solution Comparison — Gamification

> # ⚠️ CR-007 đã thay đổi phạm vi sau khi tài liệu này được duyệt
>
> Ngày 23/09/2026, PO chốt **bỏ hẳn chiến dịch, kỳ lịch và cơ chế chốt kỳ**, thay bằng **bộ chọn khoảng ngày tự do** trên bảng xếp hạng. Đồng thời **khoá mốc huy hiệu sau khi tạo**, nên huy hiệu đã nhận không bao giờ bị lấy lại.
>
> **Những mục sau trong tài liệu này KHÔNG còn hiệu lực:**
> - Mọi nội dung về **chiến dịch**: thực thể, vòng đời, chỉ số xếp hạng do vận hành cố định, luật cấm sửa khi đang chạy
> - Mọi nội dung về **kỳ lịch như một thực thể riêng**, **chốt kỳ**, **snapshot**, **đóng băng kết quả**
> - Mục tiêu **`O5`** (kết quả không đổi về sau) — đã bỏ, PO chấp nhận số liệu sống
> - Quyết định **gỡ huy hiệu khi nâng ngưỡng** — không còn, vì mốc nay khoá
>
> Trạng thái đúng nằm ở `working/raw-inputs/change-requests.md` mục **CR-007** và ở PRD.

---


| | |
| --- | --- |
| **Project** | Gamification |
| **Version** | v0.1 |
| **Ngày** | 23/09/2026 |
| **Nguồn input** | `brd-v0.6-20260923.md` v0.6.1 (Gate 1) · `impact-matrix-v0.2-20260923.md` v0.2.1 (Gate 2) · `project-decisions.md` |
| **Trạng thái** | `Pending Confirmation` — trình Gate 3 |

> Bản phân tích **nội bộ**. Sau khi Gate 3 duyệt, nội dung chảy vào PRD mục `Solution` và `TDD`.

---

## 1. Tình huống

| | |
| --- | --- |
| Đã có định hướng? | **Có — bốn quyết định ở Bước 7** |
| Định hướng ban đầu | 1. Điểm hiện với học viên **chấp nhận trễ vài phút**<br>2. Bảng xếp hạng **cập nhật theo chu kỳ**, hiện rõ lần cập nhật cuối<br>3. "Ngày có mặt" = **cứ vào hệ thống là tính**, kiểu check-in<br>4. **Mỗi chỗ tự tính** chỉ số; vận hành tự cấu hình tham số |

### Nhận xét định hướng

**Alignment với Objective:** ✅ Tốt, và quyết định số 3 đặc biệt đúng chỗ.

Số liệu General Launch cho thấy `Activation` chỉ **40.2%** — chỉ số hụt sâu nhất so với mục tiêu 80%. **Check-in là cơ chế duy nhất trong phạm vi tác động thẳng vào tầng vấn đề đó** (`O1`). Ba tầng vấn đề ở BRD §2.2 được phủ đủ:

| Tầng | Số đo | Cơ chế nhắm vào |
|---|---|---|
| Không mở ứng dụng | Activation 40.2% | Điểm check-in (`S3`) |
| Mở rồi không học | 45% người đăng nhập không bắt đầu | Điểm theo hoạt động · huy hiệu · hạng |
| Bắt đầu rồi bỏ dở | Completion 64.1% | Chiến dịch · bảng xếp hạng |

**Điểm mạnh:**

| # | |
|---|---|
| 1 | **Chấp nhận độ trễ = giữ được nguyên tắc "gamification chỉ đọc".** Không đặt gamification lên đường đi của việc học, nên lỗi ở gamification không làm hỏng việc học |
| 2 | **Một nhịp cho mọi thứ.** Điểm trễ vài phút + bảng xếp hạng theo chu kỳ → cùng một nhịp, dễ giải thích cho học viên bằng một nhãn *"cập nhật lúc HH:mm"* |
| 3 | **Bỏ `S23` đúng.** Huy hiệu và hạng đếm trọn đời, chiến dịch đếm trong khoảng ngày — gộp là gộp hai thứ khác bản chất |

**Gap — đối chiếu Impact Matrix:**

| # | Gap |
|---|---|
| **G1** | **Trễ vài phút va với `S10`.** Học viên hoàn thành hoạt động **cuối cùng** rồi đóng app ngay sẽ không nhận thông báo, vì `S10` chỉ đẩy khi đang online |
| **G2** | **Chốt kỳ không được theo nhịp hiển thị.** `S19` yêu cầu đóng băng đúng biên kỳ. Nếu dùng chung chu kỳ cập nhật thì kết quả cuối cùng lệch vài phút so với thời điểm đóng — với chiến dịch có trao thưởng thì đó là sai lệch thật |
| **G3** | **Check-in không quét được.** Mọi hành động khác đều để lại dấu vết trong bảng tiến độ / bài làm / chứng chỉ. **Riêng "có mặt" không để lại gì** nếu không ghi lúc nó xảy ra |

---

## 2. Các option

Định hướng của PO **ràng buộc nhưng chưa quyết hết** — vẫn còn ba hình dạng khả dĩ cho tầng bắt sự kiện.

| Option | Tên | Nguồn gốc | Mô tả ngắn |
| --- | --- | --- | --- |
| **A** | **Nghe sự kiện** | AI gợi ý | Luồng học phát tín hiệu khi có việc xảy ra → gamification nhận và xử lý ngay. Độ trễ tính bằng giây |
| **B** | **Quét định kỳ** ⭐ | AI gợi ý | Tác vụ nền chạy mỗi N phút, quét các bản ghi **vừa chuyển sang hoàn thành** kể từ lần quét trước. Độ trễ tối đa bằng N |
| **C** | **Tính trong luồng** | Cách hệ thống hay làm | Cộng điểm ngay trong chính thao tác hoàn thành hoạt động. Độ trễ bằng 0 |

> **Cả ba đều dùng chung:** cùng cách ghi check-in (xem §5), cùng cách tính sẵn bảng xếp hạng theo chu kỳ, cùng tác vụ riêng chốt kỳ đúng biên.

---

## 3. Bảng so sánh

| Tiêu chí | **A — Nghe sự kiện** | **B — Quét định kỳ** ⭐ | **C — Tính trong luồng** |
| --- | --- | --- | --- |
| **Business fit** | ✅ Đạt | ✅ Đạt | ✅ Đạt |
| **Độ trễ học viên thấy** | Vài giây | **Tối đa N phút** *(N do vận hành đặt)* | Tức thì |
| **`G1` — thông báo khi đang online** | 🟢 Tốt nhất — gần như luôn kịp lúc học viên còn ở trong app | 🟡 Kịp nếu học viên học tiếp; **lỡ nếu họ đóng app ngay** | 🟢 Luôn kịp |
| **Tác động người dùng & quy trình** | Không đổi thói quen | Không đổi thói quen. Cần nhãn *"cập nhật lúc HH:mm"* | Không đổi thói quen |
| **Tác động hệ thống** *(Impact Matrix)* | Luồng học phải **phát tín hiệu** → chạm vào đường đi của việc học | 🟢 **Chỉ đọc bảng tiến độ** — đúng nguyên tắc §6.1, không chạm luồng học | 🔴 **Gamification nằm trên đường đi của việc học** |
| **Effort** | **Trung bình** — cần dựng và vận hành hạ tầng sự kiện | **Thấp** — một tác vụ nền đọc theo dấu thời gian. `OQ-B2` đã xác nhận có dấu thời gian | **Thấp** nhưng nợ về sau |
| **Risk kỹ thuật** | 🟠 Tín hiệu mất thì **mất luôn điểm**, khó phát hiện. Cần cơ chế phát lại | 🟢 **Chạy lại được** — quét lại cùng khoảng thời gian cho kết quả y hệt. Tự phủ `CG-8` | 🔴 **Lỗi gamification làm hỏng thao tác học.** Chậm gamification làm chậm việc học |
| **Risk nghiệp vụ** | Thấp | 🟡 Quét hỏng âm thầm thì điểm ngừng chạy mà không ai biết → **cần theo dõi** | Cao — đúng thứ `O6` muốn tránh |
| **Dependency** | Hạ tầng sự kiện · đội nền tảng | 🟢 **Không phụ thuộc gì mới** | Không |
| **Nợ đóng cứng tenant** | Không phát sinh | Không phát sinh | Không phát sinh |

> Ba option **không khác nhau về business fit** — khác ở *độ trễ*, *mức độ chạm vào luồng học*, và *khả năng phục hồi khi lỗi*.

---

## 4. Pros / Cons

### Option A — Nghe sự kiện

| Pros | Cons |
| --- | --- |
| Độ trễ thấp nhất trong ba option không-inline | Phải dựng hạ tầng sự kiện — phụ thuộc đội khác |
| Giải `G1` tốt nhất | Tín hiệu mất là mất điểm, khó phát hiện và khó phát lại |
| Mở đường cho các tính năng theo sự kiện sau này | Luồng học phải sửa để phát tín hiệu — chạm vào thứ đang chạy ổn |

### Option B — Quét định kỳ ⭐

| Pros | Cons |
| --- | --- |
| **Không chạm luồng học** — đúng nguyên tắc "gamification chỉ đọc" | Độ trễ cao hơn A. `G1` không giải trọn |
| **Chạy lại được**, cho kết quả y hệt → tự phủ `CG-8` và `CG-7` | Quét hỏng âm thầm thì điểm ngừng chạy mà không ai biết |
| Không phụ thuộc hạ tầng mới, không phụ thuộc đội khác | Nếu N quá lớn thì học viên thấy chậm |
| Cùng nhịp với bảng xếp hạng → **một nhãn thời gian giải thích được mọi thứ** | |
| `OQ-B2` đã xác nhận bảng tiến độ có dấu thời gian → quét theo khoảng ngày là đường thẳng | |

### Option C — Tính trong luồng

| Pros | Cons |
| --- | --- |
| Tức thì, không cần giải thích độ trễ | **Gamification nằm trên đường đi của việc học** — đã bị PO loại bằng quyết định "trễ vài phút" |
| Ít thành phần | Lỗi hoặc chậm ở gamification làm hỏng trải nghiệm học |

---

## 5. Ba điều áp cho mọi option

| # | |
|---|---|
| **S-1** | **Check-in phải ghi ngay lúc xảy ra, không quét được** (`G3`). Mọi hành động khác để lại dấu trong bảng tiến độ / bài làm / chứng chỉ; riêng *"có mặt"* không để lại gì. Cần một thao tác ghi rất nhẹ: **lần đầu trong ngày học viên vào hệ thống thì ghi lại ngày đó** |
| **S-2** | **Chốt kỳ phải là tác vụ riêng, chạy đúng biên kỳ theo múi giờ tổ chức** (`C6`, `C9`) — **không đi theo chu kỳ hiển thị** (`G2`). Kết quả công bố và trao thưởng phải khớp đúng thời điểm đóng |
| **S-3** | **Bảng xếp hạng tính sẵn theo chu kỳ**, hiển thị nhãn *"cập nhật lúc HH:mm"*. Kỳ đã chốt đọc thẳng từ snapshot (`S19`) — không tính lại |

---

## 6. Recommendation

| | |
| --- | --- |
| **Option đề xuất** | **B — Quét định kỳ** |
| **Điều kiện** | Đúng khi **chấp nhận độ trễ tính bằng phút** (PO đã chốt) và khi **`N` đặt đủ nhỏ**, gợi ý 5–10 phút. Nếu sau này cần phản hồi tức thì cho một cơ chế khác thì mới cần tới A |
| **Risk phải chấp nhận** | 1. **`G1` không giải trọn** — học viên hoàn thành hoạt động cuối rồi đóng app ngay sẽ không nhận thông báo. Thành tích vẫn vào lịch sử, tra lại được<br>2. **Quét hỏng âm thầm** thì điểm ngừng chạy mà không ai biết → **phải có theo dõi và cảnh báo**, đây là điều kiện bắt buộc chứ không phải tuỳ chọn |
| **Cái gì sẽ đổi kết luận** | • Nếu **hệ thống đã sẵn hạ tầng sự kiện** đang dùng cho việc khác → A rẻ hơn hẳn và giải `G1` tốt hơn, nên chọn A<br>• Nếu PO đổi ý, muốn học viên **thấy điểm tức thì** → quay lại cân nhắc A<br>• Nếu số học viên lớn tới mức mỗi lượt quét quá nặng → cần chia nhỏ, nhưng không đổi option |

### Vì sao B chứ không phải A

Ba lý do, theo thứ tự quan trọng:

1. **B là option duy nhất không chạm vào luồng học.** A đòi luồng học phải phát tín hiệu — tức là sửa thứ đang chạy ổn, để phục vụ một tính năng phụ trợ. Nguyên tắc §6.1 của BRD nói rõ *"gamification chỉ đọc, không sửa dữ liệu học tập"*; B là option duy nhất giữ được đúng nghĩa đen của câu đó.
2. **B chạy lại được.** Quét lại cùng khoảng thời gian cho kết quả y hệt. Điều này tự phủ hai coverage gap (`CG-7` hai thiết bị cùng hoàn thành, `CG-8` job lỗi) mà A phải xử lý riêng từng cái.
3. **B không phụ thuộc đội khác.** Dependency là thứ đắt nhất trong một tính năng không nằm trên đường găng.

Đổi lại là `G1`. Nhưng `G1` chỉ ảnh hưởng **một nhóm nhỏ**: người hoàn thành hoạt động cuối cùng rồi rời đi ngay. Người học liên tục — nhóm mà gamification muốn tạo ra — vẫn còn trong app sau 5 phút.

---

## 7. Open Questions

| # | Câu hỏi | Vì sao quan trọng | Người trả lời | Chặn Gate 3? |
| --- | --- | --- | --- | --- |
| **OQ-D1** | **`N` bằng bao nhiêu?** Gợi ý 5–10 phút. Vận hành đặt được hay cố định? | Quyết định trực tiếp thứ học viên cảm nhận | PO | No — Field Intake |
| **OQ-D2** | **Hệ thống đã có hạ tầng sự kiện đang dùng cho việc khác chưa?** | Nếu có thì kết luận đổi sang A | Dev | **Yes** |
| `OQ-C5` | Chính sách lưu trữ sổ giao dịch điểm | `R7` | PO + Dev | No |
| `OQ-C7` | Có khoá bảng điểm khi đang có chiến dịch chạy không | `CG-11` | PO | No |
| `OQ-C8` | Cơ chế **dừng** chiến dịch đang chạy (`S17` cấm sửa, `CF-6` bắt phải dừng được) | `CG-10` | PO | No |
| `OQ-C9` | Huy hiệu áp cùng nguyên tắc `CF-3` chứ | `CF-4` | PO | No |
| `OQ-B11` | Múi giờ tổ chức khai ở đâu | `C6`, `C9`, `S-2` | PO + Dev | No |
| `OQ-B4a` | Mẫu số 132 và 145 là hai nhóm khác nhau? | `Analytics` của PRD | PO | No |

---

## 8. References

| Nguồn | |
|---|---|
| BRD | `docs/brd/brd-v0.6-20260923.md` (v0.6.1) — §2 Analytics · §6.1 nguyên tắc chỉ đọc · `C1`–`C10` |
| Impact Matrix | `working/impact-analysis/impact-matrix-v0.2-20260923.md` (v0.2.1) — §5 conflict · §8 coverage gap · §11.1 hiệu năng |
| Quyết định | `project-decisions.md` — Gate 1 · Gate 2 · Bước 7 |
| KB | `07-learning-experience.md` (nguồn sự kiện) · `03-assessment.md` (`BR-TEST`) · `06-user-account.md` §8b (`Test Account`) · `15-product-direction.md` §6 (đóng cứng tenant) |
| Số liệu | General Launch 8/9–21/9/2026 — PO cung cấp 23/09/2026 |

---

## 9. Quyết định

| | |
| --- | --- |
| **Option được chọn** | **C — Tính trong luồng** |
| **Lý do** | **Dev xác nhận làm được theo cách này**, và PO chọn C |
| **Người quyết** | PO + Dev |
| **Ngày** | 23/09/2026 |

### 9.1 🟢 C giải luôn `G1`

Độ trễ bằng 0 nghĩa là **học viên luôn còn trong hệ thống tại đúng thời điểm điểm được cộng**.

`G1` — *"hoàn thành hoạt động cuối rồi đóng app thì không nhận được thông báo"* — **không còn tồn tại**. `US2` (thông báo thành tích khi đang online) nay thực hiện trọn vẹn, không có nhóm học viên nào bị lỡ.

Đây là điểm mạnh mà cả A lẫn B đều không có.

### 9.2 ⚠️ Cái giá của C, và điều kiện bắt buộc đi kèm

C đặt phần cộng điểm **vào trong cùng một lượt thao tác** với việc hoàn thành hoạt động. Kéo theo một yêu cầu không thể bỏ:

> **`NFR-GAM-01` — Lỗi ở gamification KHÔNG được làm hỏng thao tác học.**
>
> Học viên bấm Hoàn thành thì thao tác đó **phải thành công**, kể cả khi phần cộng điểm gặp lỗi. Lỗi gamification phải được chặn lại tại chỗ, không lan ra ngoài.
>
> Tương tự với tốc độ: phần cộng điểm **không được làm chậm cảm nhận** của thao tác hoàn thành hoạt động.

**Hệ quả trực tiếp cần chọn tiếp:** nếu lỗi bị chặn lại để bảo vệ thao tác học, thì **điểm lần đó mất mà không ai biết**. Hai cách xử lý:

| | Cách | Đánh đổi |
|---|---|---|
| **C-1** | Chấp nhận mất âm thầm | Không tốn gì. Nhưng `O6` *(điểm đáng tin)* bị sứt — có trường hợp học viên học thật mà không có điểm, và không ai giải thích được |
| **C-2** ⭐ | **Ghi lại chỗ lỗi** để vận hành thấy và xử lý | Thêm một chỗ ghi nhật ký lỗi. Rẻ, và giữ được `O6` |

`Recommendation` — **C-2**. Đây **không phải "tính bù"** (dựng lại quá khứ) mà là **xử lý một lần ghi bị hỏng** — hai chuyện khác nhau. → `OQ-D3`

### 9.3 Hai coverage gap dịch chuyển

| # | Trước | Sau khi chọn C |
|---|---|---|
| `CG-7` | Hai thiết bị cùng hoàn thành một hoạt động gần như đồng thời | 🔺 **Quan trọng hơn** — hai lượt thao tác song song đều có thể cộng điểm. Phải chống trùng ngay tại chỗ ghi |
| `CG-8` | Tác vụ nền chạy lỗi | 🔻 **Thu hẹp** — không còn tác vụ quét điểm. Chỉ còn áp cho **tác vụ chốt kỳ** |

### 9.4 Ba điều ở §5 vẫn giữ nguyên

| # | |
|---|---|
| `S-1` | Check-in ghi ngay lúc học viên vào hệ thống — với C thì tự nhiên, cùng một cách làm |
| `S-2` | **Chốt kỳ vẫn là tác vụ riêng**, chạy đúng biên kỳ theo múi giờ tổ chức |
| `S-3` | **Bảng xếp hạng vẫn tính sẵn theo chu kỳ**, có nhãn *"cập nhật lúc HH:mm"* |

> ℹ️ **Điểm hiện ngay nhưng bảng xếp hạng cập nhật theo chu kỳ** — hai nhịp khác nhau, và điều đó không sao. Học viên thấy *"+10 điểm"* tức thì ở trang thành tích, còn thứ hạng thì đổi ở lần cập nhật tiếp theo. Cần nói rõ điều này trên giao diện để không gây thắc mắc.
