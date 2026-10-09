# Knowledge pack vai PO

Kiến thức chung cho vai Product, không phụ thuộc sản phẩm, chép từ AWS AI-DLC Workflows v2.10 (`core/knowledge/aidlc-product-agent/`, giấy phép MIT-0). Khác với `../domain/`, là domain pack của sản phẩm đang cài. Command của stage ghi file nào cần đọc.

| File | Nội dung | Stage đọc | Tình trạng |
|---|---|---|---|
| `corner-checklist-aws.md` | Góc hay sót, quét từng thành phần qua danh sách cố định. Bản gốc chung; mỗi domain viết lại thành `domain/corner-checklist.md` | 2.3, 2.42 qua bản của domain | Nguyên văn AWS |
| `requirements-guide.md` | FR, NFR, constraint, assumption; mẫu acceptance criteria; completeness checklist; ma trận truy vết | 2.3 | Nguyên văn AWS |
| `requirements-elicitation.md` | Phỏng vấn, workshop, quan sát, phân tích tài liệu, prototype; validation checklist | 1.1, 2.3 | Nguyên văn AWS |
| `user-story-patterns.md` | INVEST, cách tách story, Given/When/Then, anti-pattern, Definition of Ready | 2.4, 2.42 | Nguyên văn AWS |
| `prioritization-frameworks.md` | MoSCoW, WSJF, RICE, Kano; xử lý hoà và bất đồng | 1.4, 2.4 | Nguyên văn AWS |
| `product-guide.md` | Persona, MVP, story mapping, workflow planning | 1.1, 1.4, 2.4 | Nguyên văn AWS |
| `market-research-methods.md` | Competitive analysis, SWOT, build vs buy, market sizing | 1.2 | Nguyên văn AWS |

File chép nguyên văn giữ tiếng Anh, có dòng nguồn ở đầu. Cập nhật từ AWS: `git clone --depth 1 https://github.com/awslabs/aidlc-workflows`, so với bản trong repo, giữ dòng nguồn. Không chép `functional-design-guide.md`: thiết kế thực thể và state machine là việc của Dev, ngoài phạm vi PO.
