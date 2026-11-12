# Vào workflow

Hướng dẫn cho **người mới** và cho việc **thêm một repo** vào workflow. Làm theo A → E, khoảng 10 phút.

## A. Bạn là ai

| Bạn là | Làm các mục | Đọc tiếp |
|---|---|---|
| PO | A → D | [USER-GUIDE.md](USER-GUIDE.md), rồi `/po` |
| Tech lead (FE / BE) | A → D | [engine/tech/knowledge/workflow.md](engine/tech/knowledge/workflow.md), rồi `/tech` |
| QA | A → D | workflow.md mục 2 (stage 2.81, 3.6) |
| Dev code một repo | Không cần cài repo này. Làm trong repo của mình theo `openspec/` ở đó; repo `flow: comet` thì thêm mục G | workflow.md §4.2 |
| Người thêm sản phẩm mới | A → E | [DOMAIN-SETUP.md](DOMAIN-SETUP.md) |
| Người giữ khung | A → G | [CHANGELOG.md](CHANGELOG.md), mục "Sửa engine" trong [AGENTS.md](AGENTS.md) |

## B. Cần có trên máy

| Phần mềm | Bản | Kiểm | Cài |
|---|---|---|---|
| Git | bất kỳ bản mới | `git --version` | `winget install --id Git.Git -e` · macOS `xcode-select --install` |
| Python | ≥ 3.10 | `python --version` | `winget install --id Python.Python.3.12 -e` |
| Node.js | LTS | `node --version` | `winget install --id OpenJS.NodeJS.LTS -e` |
| OpenSpec CLI | đúng bản khóa trong `workspace.yaml` | `openspec --version` | `npm install -g @fission-ai/openspec@1.14.1` |
| Claude Code | bản mới | `claude --version` | [Hướng dẫn cài](https://docs.anthropic.com/en/docs/claude-code/setup) |

Khuyến nghị thêm: `pip install pyyaml` (sensor `tech-tools.py` cần).

Chỉ khi làm ở repo có `flow: comet` trong `workspace.yaml`: Node.js **≥ 22.16** (không phải LTS cũ) và Comet CLI, xem mục G.

## C. Cài — một lệnh

```bash
git clone <remote upbase-specs> E:/UP_BASE/upbase-specs
cd E:/UP_BASE/upbase-specs
python scripts/setup.py
```

Lệnh này làm bốn việc, chạy lại bao nhiêu lần cũng an toàn:

1. Kiểm phần mềm ở mục B; thiếu thì in đúng lệnh cài. **Script không tự cài phần mềm hệ thống.**
2. Đọc `workspace.yaml`, kiểm từng repo đã clone chưa.
3. Sinh `.claude/commands/`, `.claude/agents/` từ `engine/`, và sinh `.claude/settings.json` từ `scripts/settings.base.json`: quyền, luật chặn ghi (`intents/*/archive/**`, `.po/**`, `engine/tech/aidlc/**`), **4 hook của luồng PO** (`po-tools.py status` lúc mở phiên, `po-hook.py` ghi sổ lượt người), cộng `additionalDirectories` lấy từ `repos:`. Script **tự dò lệnh python chạy được** rồi ghi vào hook — trên Windows `python3` thường là alias Microsoft Store và chạy lỗi.
4. Tạo khung `domain/codekb/<repo>/` rỗng cho repo chưa có, rồi in `[ok]` / `[!]` / `[X]` từng mục.

Đăng ký store OpenSpec (một lần mỗi máy):

```bash
openspec store register E:/UP_BASE/upbase-specs
cd E:/UP_BASE/<một repo code> && openspec doctor      # phải thấy: upbase-specs: ok
```

## D. Mở Claude Code và tự kiểm

1. Mở Claude Code **tại thư mục gốc `upbase-specs`** (thư mục có `CLAUDE.md`). Mở ở chỗ khác thì command và quyền của khung không có.
2. Kiểm lại bất kỳ lúc nào: `python scripts/doctor.py`. Mọi mục phải `[ok]` hoặc `[-]`.
3. Gõ `/po` (PO) hoặc `/tech` (Tech lead). Cả hai đều mở menu trước, chưa quét gì.

## E. Thêm repo hoặc thêm người

**Thêm một repo code vào workflow** — sửa một chỗ duy nhất:

1. Thêm một mục vào `repos:` trong [workspace.yaml](workspace.yaml): `id`, `path`, `kind`, `owner`, `conventions`, `gate`.
2. `python scripts/setup.py` — script sinh lại `settings.json` và tạo khung `domain/codekb/<id>/`.
3. Chạy `/tech <intent> nhảy tới reverse-engineering` cho repo đó để điền codekb (stage 2.1).

**Thêm người**: sửa mục `people:` trong `workspace.yaml`; tên lead và owner dùng trong `tech-state.md` và `system-map.md`.

**Thêm sản phẩm mới**: đổi `domain/` theo [DOMAIN-SETUP.md](DOMAIN-SETUP.md) hoặc chạy `/new-domain`. `engine/` không phụ thuộc sản phẩm, giữ nguyên.

## F. Nhận bản mới từ PO

Khung này tách ra từ repo PO và vẫn chung gốc lịch sử, nên nhận được cập nhật của PO. Remote `po` đã cấu hình sẵn,
**chỉ nhận, không gửi** (`pushurl = no_push`):

```bash
git remote -v | grep '^po'
# po  https://github.com/buidhui/uplnd_po_workflow.git (fetch)
# po  no_push                                          (push)
```

Chia làm **hai đường riêng**, vì hai vùng có chủ khác nhau. Đừng merge cả repo một lần.

### F.1 Engine — gần như luôn sạch

`engine/` của khung này trùng từng byte với PO. Phần thêm của mình (`engine/tech/`, `engine/commands/new-domain.md`)
không nằm trong `MANIFEST.txt` của PO nên PO không bao giờ chạm tới.

```bash
git fetch po
git log --oneline HEAD..po/main              # PO có gì mới
git diff --stat HEAD po/main -- engine/      # engine đổi những gì
git checkout po/main -- engine/              # nhận
python engine/scripts/po-tools.py engine-check
python scripts/setup.py                      # sinh lại .claude/ từ engine mới
```

Hai điều phải biết về `git checkout <ref> -- <đường dẫn>`:

- Nó **giữ nguyên** file chỉ có ở bên mình. `engine/tech/` và `new-domain.md` an toàn.
- Nó **không xoá** file mà PO đã xoá — bản cũ nằm lại thành rác. Vì vậy luôn chạy `engine-check` ngay sau đó:
  mục *Mới, chưa có trong manifest* liệt kê file không có trong `MANIFEST.txt` của PO. Trừ phần thêm của mình, mỗi
  dòng còn lại là một file PO đã xoá — xoá tay rồi chạy `po-tools.py manifest --write`.

`engine-check` cũng là cách phát hiện ai đó đã sửa tay file engine trước khi nhận bản mới (mục *Bị sửa*).
Sửa engine thì sửa ở repo PO, đừng sửa ở đây.

### F.2 Domain, memory và intents — merge có chọn lọc

Ba vùng này **không được `checkout` cả cụm**, vì bên mình có nội dung PO không có:

| Vùng | Bên mình có thêm gì | Cách nhận |
|---|---|---|
| `domain/` | `system-map.md`, `tech-adjustments.md`, `templates/tech-design.md`, `codekb/`, và mục `### 2.43 Design Alignment` trong `domain.md` | Xem `git diff HEAD po/main -- domain/` rồi lấy từng file KB mà PO cập nhật. **Không** `checkout` cả `domain/` |
| `memory/team.md` | Có thể có bài học bên mình | **Gộp theo dòng, giữ bài học của cả hai bên**, không chép đè (quy tắc trong `CHANGELOG.md` của PO) |
| `memory/project.md` | Bài học của sản phẩm | Của mình, không nhận từ PO |
| `intents/` | Artifact Tech: `tech-state.md`, `inception/{domain-design,units-generation,contract-design,test-cases,delivery-planning}/`, `construction/`, và khối `DEC-T` trong `decisions.md` | Artifact của PO (PRD, requirements, impact-matrix, brd, ux/test-design, reviews, `state.md`) lấy bản của PO. `decisions.md` giữ cả hai: phần PO ở trên, khối `## Quyết định của phần Tech` ở dưới |

```bash
git diff --stat HEAD po/main -- domain/ intents/     # xem trước
git checkout po/main -- intents/<slug>/inception/prd/prd.md   # lấy từng file
```

`workspace.yaml`, `scripts/`, `openspec/`, `SETUP.md` và `.claude/` chỉ có ở khung này, PO không có — không bao giờ phải merge.

### F.3 Sau khi nhận

```bash
python scripts/setup.py                                  # .claude/ khớp engine mới
python engine/scripts/po-tools.py doctor                 # 0 Lỗi
python engine/tech/scripts/tech-tools.py check intents/<slug>
openspec validate --all --strict
```

Engine lên version mới thì đọc mục tương ứng trong [CHANGELOG.md](CHANGELOG.md): mỗi bản có dòng *Tương thích* nói
rõ chỉ cần chép engine, hay phải chạy migrate, hay phải sửa intent bằng tay.

## G. Comet cho repo code (chỉ repo `flow: comet`)

Repo code có `flow: comet` trong `workspace.yaml` chạy vòng đời change bằng Comet Classic (OpenSpec + Superpowers). Việc này làm **trong từng repo code**, không làm ở gốc repo khung hay gốc workspace (Comet ở đó không thấy `openspec/` của repo).

1. Máy có Node.js ≥ 22.16 (`node --version`), rồi `npm install -g @rpamis/comet` và kiểm `comet --version`.
2. Trong repo code, trên nhánh làm việc: `comet init --workflow classic --platform claude --scope project --skip-existing --codegraph skip --language en`.
3. Trong `.comet/config.yaml` của repo đặt `artifact_layout: legacy`, `auto_transition: false`, `memory.learning: false`.
4. Schema mặc định của repo phải là bản `*-comet` (`openspec/config.yaml`), xem `domain/tech-adjustments.md` mục `bolt`.
5. Hook cổng Tech và chính sách file có trong `.claude/hooks/` của repo và được nối ở `.claude/settings.json`. Mở Claude Code **trong repo** (hook không chạy khi mở ở nơi khác), rồi `/comet-open <tên change>`.
6. Kiểm: `comet doctor` ở repo không có dòng ✗.

Repo có file `*.lock` ở gốc (như `yarn.lock`) hiện không chạy được `comet state init` (lỗi của Comet 0.5.2), nên để `flow: opsx`.

## Khi gặp lỗi

| Lỗi | Cách sửa |
|---|---|
| `chưa cài OpenSpec CLI` | `npm install -g @fission-ai/openspec@<bản trong workspace.yaml>` |
| `OpenSpec trên máy là X, khung yêu cầu Y` | Cài lại đúng bản Y. Stores và custom schema đang beta, lệch bản là hỏng |
| `repo <id> chưa có ở <path>` | Clone repo về đúng chỗ, hoặc sửa `path` trong `workspace.yaml` |
| Command `/po`, `/tech` không hiện | Chạy `python scripts/setup.py`, rồi mở lại Claude Code tại gốc repo |
| Mở phiên không thấy bảng trạng thái intent, hoặc `po-tools.py approve` báo không tìm thấy lời PO trong sổ lượt | Hook không chạy. Chạy `python scripts/setup.py` rồi mở lại Claude Code; kiểm dòng `settings.json: … hook, lệnh python` trong kết quả |
| Muốn đổi quyền, luật chặn hay hook | Sửa `scripts/settings.base.json` rồi chạy `python scripts/setup.py`. Sửa thẳng `.claude/settings.json` sẽ mất ở lần chạy sau |
| `codekb <repo> còn rỗng` | Bình thường với repo mới. Chạy stage 2.1 Reverse Engineering |
| Windows chặn chạy script | Chạy một lần: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| `[cổng Tech] <change> chưa được đi tiếp` | Contract chưa `status: agreed` hoặc còn `NEEDS CLARIFICATION`. Chờ BE lead ký, hoặc owner repo tự tạo `<change>/.comet/tech-gate-waiver.md` ngoài Claude |
| `comet state init` báo "旧 Runtime 含锁…" | Repo có `*.lock` ở gốc (lỗi Comet 0.5.2). Để `flow: opsx` cho repo đó |
| `pnpm` hoặc `yarn` "command not found" sau khi đổi Node | `nvm` giữ gói global theo từng bản Node: cài lại `pnpm`, `yarn` cho bản Node đang dùng |
| `engine-check` báo mục *Bị sửa* | Có người sửa tay file engine. Sửa engine thì sửa ở repo PO; ở đây lấy lại bản gốc: `git checkout po/main -- <file>` |
| `engine-check` báo *Mới, chưa có trong manifest* | Trừ `engine/tech/` và `engine/commands/new-domain.md` là phần thêm của khung này, còn lại là file PO đã xoá: xoá tay rồi `po-tools.py manifest --write` |
| `git push po` báo lỗi | Đúng như thiết kế: remote `po` chỉ nhận, không gửi. Công việc của khung này push lên `origin` |

---
Quy tắc: PR nào thêm công cụ, đổi phiên bản hay thêm bước cài phải sửa file này, `workspace.yaml` và `scripts/setup.py` trong cùng PR.
Sửa `engine/` xong phải chạy `python scripts/setup.py` để `.claude/` khớp lại; `.claude/` là bản sinh ra, không sửa tay — quyền và hook sửa ở `scripts/settings.base.json`.
Đổi file nào thì cập nhật luôn mô tả luồng ở các `.md` liên quan trong cùng lần sửa: `SETUP.md`, `AGENTS.md`, `engine/tech/knowledge/workflow.md`, `CHANGELOG.md`.
Phần PO của `engine/` sửa ở repo PO rồi nhận về theo mục F, không sửa tại chỗ — sửa tại chỗ là tự tạo xung đột cho lần nhận sau.
