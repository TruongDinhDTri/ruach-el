# 🪶 Authorship Reclaim Playbook

### Từ “AI viết hết, tôi chả hiểu gì” → “Tôi là TÁC GIẢ thật của hệ thống này” ⚙️🔥

---

# 📍 Bộ tài liệu này & Khi nào dùng

> Đọc cái này TRƯỚC. Để biết mình đang cầm tài liệu gì, dành cho ai, và khi nào nên dùng cái nào.

### 🎯 Tài liệu này là gì?

Đây là **PHƯƠNG PHÁP NHẬN LẠI QUYỀN TÁC GIẢ** — dành cho khi một codebase được build phần lớn (hoặc toàn bộ) bởi AI agent, và bây giờ bạn cần **đứng ra nhận nó như chính tay mình quyết định**: bảo vệ được kiến trúc, lý giải được mọi lựa chọn công nghệ, trả lời được câu hỏi phỏng vấn xoáy nhất.

Đây là một **TEMPLATE general** — không gắn với dự án cụ thể nào. Bạn **clone** nó ra, rồi điền dữ liệu thật của từng dự án vào.

### 🧩 Nó khác `CodeBase Understanding` chỗ nào?

| | CodeBase Understanding | Authorship Reclaim (tài liệu này) |
| --- | --- | --- |
| Dạy bạn | **HIỂU** hệ thống chạy sao | **NHẬN LẠI** quyền tác giả + **bảo vệ** quyết định |
| Câu hỏi gốc | "Cái gì? Ở đâu? Chạy sao?" | "**VÌ SAO** chọn vậy? Đánh đổi gì? Nói sao cho thuyết phục?" |
| Điểm khó | Lần theo flow, đọc code | **Tái dựng lý do** mà AI không để lại + **luyện nói** dưới áp lực |

> Nói ngắn gọn: `CodeBase Understanding` xây cho bạn cái **mental model**. `Authorship Reclaim` lấy mental model đó, **gắn lý do vào từng quyết định**, rồi **biến nó thành lời bạn nói được trong phòng phỏng vấn**.

### 🔬 Phân chia cốt lõi (đọc kỹ — đây là chỗ dễ lẫn nhất)

Hai tài liệu KHÔNG trùng nhau, vì chúng khác nhau ở **hai trục**:

**Trục 1 — Method vs Artifact (cách-làm vs sản-phẩm):**

- `CodeBase Understanding` là **METHOD** — một how-to-think guide, đọc để biết *cách* tiếp cận. Không có ô để điền.
- `Authorship Reclaim` (tài liệu này + bản instance) là **ARTIFACT** — có ô trống để ĐIỀN, tạo ra một tài liệu cụ thể bạn cầm đi phỏng vấn.

**Trục 2 — HOW vs WHY (hoạt-động-ra-sao vs vì-sao-xây-vậy):**

- `CodeBase Understanding` trả lời **HOW**: feature *hoạt động* ra sao — trace luồng, quan sát, hiểu cơ chế.
- `Authorship Reclaim` trả lời **WHY + cách KỂ**: feature được xây *vì sao*, đánh đổi gì, vấp trap nào, và *nói* nó ra sao trong phỏng vấn.

> 🪞 Cùng một feature "chat":
> - **CodeBase Understanding** hỏi: *"Tin nhắn đi từ đâu tới đâu? Lưu ở bảng nào?"* (HOW)
> - **Authorship Reclaim** hỏi: *"Vì sao dedup thread theo {buyer, seller}? Đánh đổi gì? Lúc làm vấp bug gì? Kể lại sao cho thuyết phục?"* (WHY + kể)
>
> Bạn cần CẢ HAI: hiểu cơ chế (CodeBase Understanding) TRƯỚC → rồi gắn lý do + luyện kể ở ĐÂY (Authorship Reclaim) SAU.

### 👤 Dành cho ai?

- Người đã build sản phẩm bằng AI agent nhưng chưa nắm sâu "vì sao" của các quyết định.
- Người sắp phỏng vấn / demo / review một dự án mà mình là "chủ" nhưng AI làm phần lớn.
- Bất kỳ ai cần biến "code tôi không nhớ mình viết" thành "hệ thống tôi hiểu tới tận gốc".

### 🕐 Dùng khi nào?

**BƯỚC THỨ HAI** — *sau* khi đã dùng `CodeBase Understanding` để hiểu hệ thống chạy ra sao. Khi câu hỏi trong đầu bạn chuyển từ *"nó chạy sao?"* thành *"tôi sẽ bảo vệ nó thế nào?"*

---

### 🗺️ Bộ tài liệu 3 tầng — Bạn đang ở đâu?

| | **CodeBase Understanding** | **Authorship Reclaim Playbook** | **Bản instance** (vd Asset Platform) |
| --- | --- | --- | --- |
| **Là gì** | Phương pháp HỌC | Phương pháp NHẬN LẠI quyền tác giả + luyện nói | Sản phẩm điền đầy |
| **Trả lời câu** | "Hệ thống này hoạt động sao?" | "Làm sao bảo vệ nó như tác giả thật?" | "Dự án này CỤ THỂ ra sao" |
| **Dành cho ai** | Dev cần hiểu code lạ | Người build bằng AI, chưa nắm 'vì sao' | Người ôn phỏng vấn dự án đó |
| **Dùng khi nào** | Bước 1 — hiểu | Bước 2 — nhận tác giả + luyện | Bước 3 — ôn thi |
| **Loại** | Method | Method (xây TRÊN cái bên trái) | Instance (clone từ template này) |

> 📌 **YOU ARE HERE → Authorship Reclaim Playbook** (template general — clone tài liệu này ra để tạo bản cho từng dự án).
>
> Chưa hiểu hệ thống chạy sao? Quay lại **CodeBase Understanding** trước. Đã hiểu rồi? Tốt — clone template này, đặt tên theo dự án (vd `Asset-Platform-Decision-Map.md`), rồi điền 4 phần dưới đây.

---

# 🧭 Cách dùng template này (Quy trình clone)

```text
1. Copy file này → đổi tên theo dự án (vd: Asset-Platform-Decision-Map.md)
2. Đi từ trên xuống, điền 4 phần — KHÔNG bỏ qua phần nào
3. Mỗi chỗ ___ là chỗ bạn điền. Mỗi "📥 Nguồn để điền" chỉ bạn đào dữ liệu ở đâu
4. Điền xong → đọc to phần Talk Track, tự trả lời, ghi âm lại nghe thử
5. Phần nào trả lời còn lắp bắp → đào sâu lại phần đó
```

### 📥 Bốn mỏ vàng để đào "vì sao" (đọc kỹ trước khi điền)

Khi AI viết code, nó không để lại lý do trong đầu bạn — nhưng nó để lại **dấu vết** ở 4 nơi:

| Mỏ | Chứa gì | Cách lấy |
| --- | --- | --- |
| **Commit messages** | Đã làm gì, theo thứ tự nào, fix bug gì | `git log <branch> --oneline` rồi đọc body từng commit |
| **Issue tracker** (Paperclip/Jira/GitHub) | **VÌ SAO** làm — yêu cầu nghiệp vụ, bối cảnh | Đọc title + description + comment của từng issue |
| **Code thật** | Quyết định kỹ thuật cuối cùng đã chốt | Mở file theo phương pháp `CodeBase Understanding` |
| **Config / deps** | Stack, version, lý do bảo mật | `package.json`, `Dockerfile`, `.env.example`, lockfile |

> 💡 **Sự thật an ủi:** AI gần như luôn chọn phương án **kinh điển, mainstream** (Postgres, JWT, REST, layered...). Mà cái gì kinh điển thì lý do biện minh cho nó cũng kinh điển — và **học được**. Bạn không cần đọc tâm trí AI; bạn chỉ cần hiểu *vì sao lựa chọn đó là lựa chọn đúng*.

### 🔗 LIÊN KẾT với `CodeBase Understanding` — Đến đâu, nhảy đâu, hỏi gì

> **Sống ở file NÀY (artifact).** Vài ô cần với tay mở **dụng cụ** ra — vì cần hiểu code THẬT, không đoán. Còn lại điền thẳng.
>
> ⚠️ **LUẬT THỨ TỰ:** trước khi trace luồng (3B) hay mổ feature (5), **PHẢI map cấu trúc tổng trước** (BƯỚC 0) — không có bản đồ thì trace sẽ lạc. Đào chi tiết khi chưa orient = "mông lung".

| Khi điền ô... | → Mở dụng cụ | Câu hỏi MANG THEO khi đào code |
| --- | --- | --- |
| **BƯỚC 0 — Map cấu trúc trước** (3A + định vị code) | `Trace Any Codebase` (BƯỚC 1) **+** `CodeBase Understanding` **PHASE 1-3** | App làm gì? → Entry point ở đâu (`main`/`app.module`)? → Có những module/khối nào (`ls src/`)? → Nối nhau ra sao? |
| **3B Trace luồng** | `Trace Any Codebase` (6 bước) **+** `CodeBase Understanding` PHASE 4 | Gì kích hoạt? → API nào? → Validate đâu? → Business logic đâu? → Bảng nào? → Trả gì? |
| **3C Data model** | `CodeBase Understanding` PHASE 5 (Study DB Schema) | Entity chính? → Quan hệ? → Bảng quan trọng nhất? → Source of truth? |
| **5 Feature → dòng "Flow"** | `Trace Any Codebase` (6 bước) **+** PHASE 4 | (như 3B, cho riêng feature đó) |

> 🔁 **Quy trình:** BƯỚC 0 (map cấu trúc) → mở Phase/6-bước → đào code tới khi HIỂU → quay lại điền "Flow" → rồi gắn WHY/trap. HOW là nền, WHY xây trên nó.
> ✅ Ô khác (Soul, Stack, Decision Map, Limitations, Ownership, Talk Track) → điền từ đầu bạn + commit + issues, KHÔNG cần mở dụng cụ.

---

# 1️⃣ THE SOUL — Linh hồn sản phẩm

> *Trước khi nói về code, phải nói được sản phẩm này SỐNG vì điều gì.*
> Đây là phần dễ ghi điểm nhất trong phỏng vấn — và là phần AI KHÔNG thể làm thay bạn.

### Điền vào:

- **Sản phẩm này là gì (một câu):** ___
- **Nó giải quyết nỗi đau gì?** ___
- **Người dùng là ai? Họ đang ở chương nào của câu chuyện của họ?** ___
- **Luồng chính người dùng làm nhiều nhất:** ___ → ___ → ___
- **Sản phẩm tạo ra sự chuyển hoá gì cho họ?** ___

> 📥 **Nguồn để điền:** README, landing page, issue tracker (các epic gốc thường mô tả mục đích), tên project, mô tả trên store/demo.

---

# 2️⃣ STACK & ARCHITECTURE — Dùng gì + Tổ chức kiểu gì

> ⚠️ Đây là chỗ phân biệt junior với senior. Phải tách RÕ **hai tầng**:
> **WHAT** (công nghệ nào) ≠ **HOW** (hệ thống được tổ chức ra sao). — xem `CodeBase Understanding` STEP 2 & 3.

### 2A. Tech Stack — WHAT (công nghệ gì)

| Layer | Công nghệ | Vì sao chọn (1 dòng) |
| --- | --- | --- |
| Frontend (web) | ___ | ___ |
| Frontend (mobile) | ___ | ___ |
| Backend / API | ___ | ___ |
| Database | ___ | ___ |
| Auth | ___ | ___ |
| AI / 3rd-party | ___ | ___ |
| Infra / Deploy | ___ | ___ |

### 2B. Architecture Style — HOW (tổ chức ra sao)

- **System shape:** ___ *(monolith / modular monolith / microservices / monorepo / ...)*
- **Communication:** ___ *(REST / GraphQL / WebSocket / queue / ...)*
- **State / source of truth:** ___
- **Processing:** ___ *(sync / async / queue-based / event-driven / ...)*
- **Auth model:** ___ *(stateless JWT / session / cookie-based / ...)*

> 📥 **Nguồn để điền:** `package.json` / `Dockerfile` / `docker-compose.yml` / lockfile cho stack; cấu trúc thư mục (`apps/`, `services/`...) + import graph cho architecture style.

---

# 3️⃣ SYSTEM MAP & DATA FLOW — Bản đồ hệ thống & luồng dữ liệu

> Trả lời 2 câu kinh điển: **"Vẽ kiến trúc ra giấy đi"** và **"Trace 1 request từ đầu tới cuối"**.
> Không vẽ được hệ thống từ trí nhớ → chưa thật sự nắm.

### 3A. Sơ đồ kiến trúc (component diagram) — ⭐ BƯỚC 0, LÀM TRƯỚC TIÊN

> Vẽ các khối lớn + cách nối nhau. ASCII xấu cũng quý.
> 🧭 **Chưa có sơ đồ này? Dựng nó TRƯỚC khi trace 3B.** Cách dựng: `Trace Any Codebase` BƯỚC 1 (`ls src/` + `cat main`/`app.module`) **+** `CodeBase Understanding` PHASE 1-3. Có bản đồ rồi mới trace luồng khỏi lạc.

```
[Client(s)] → [API / Gateway] → [Service / Module layer] → [Database]
                                        ↓
                       [Cache]  [Queue/Cron]  [3rd-party]  [Storage]
```

___ *(thay bằng sơ đồ thật)*

### 3B. Trace 1-2 luồng quan trọng (request lifecycle)

> 🔗 **Cần đào code? → `CodeBase Understanding` PHASE 4.** Hỏi: gì kích hoạt → API nào → validate đâu → business logic đâu → bảng nào → trả gì?
> Trace: UI → API → validate → business/service → DB → async → response.

- **Luồng [tên]:** ___ → ___ → ___ → ___

### 3C. Data Model — entity & quan hệ

> 🔗 **Cần đào code? → `CodeBase Understanding` PHASE 5.** Hỏi: entity chính? → quan hệ? → bảng quan trọng nhất? → source of truth?
> "Bảng/entity chính là gì, quan hệ ra sao." DB lộ ra domain thật.

- **Entity chính:** ___
- **Quan hệ:** ___
- **Source of truth:** ___

> 📥 Nguồn: entry point (main/app), router, ORM models/migrations, docker-compose (thấy các service).

---

# 4️⃣ THE DECISION MAP ★ — Bản đồ quyết định (TRÁI TIM)

> Đây là phần chiếm ~70% phỏng vấn senior. Mỗi quyết định = một câu trả lời đã viết sẵn.
> Công thức mỗi dòng: **Quyết định → Vì sao → Đánh đổi (cái mình hy sinh) → Câu phỏng vấn nó trả lời.**

### Mẫu một quyết định (copy block này cho mỗi quyết định lớn):

```
### [Tên quyết định] — vd "Chọn PostgreSQL làm DB chính"
- **Quyết định:** ___
- **Vì sao (lý do kinh điển):** ___
- **Phương án đã loại & vì sao:** ___ (vd: "không chọn Mongo vì dữ liệu quan hệ mạnh, cần JOIN + ACID")
- **Đánh đổi mình chấp nhận:** ___
- **Trả lời được câu phỏng vấn:** "___?"
- **Bằng chứng (commit / issue):** ___
```

### Danh sách quyết định cần điền (gợi ý — thêm/bớt theo dự án):

- [ ] Vì sao chọn **database** này (vs lựa chọn khác)?
- [ ] Vì sao mô hình **auth** này (JWT/session/cookie)?
- [ ] Vì sao kiểu **API** này (REST/GraphQL/...)?
- [ ] Vì sao cấu trúc **repo/architecture** này (monorepo/microservices/...)?
- [ ] Quyết định về **xử lý dữ liệu nhạy cảm** (tiền tệ, PII, ...)?
- [ ] Quyết định về **bảo mật** (xử lý CVE, dependency, secret)?
- [ ] Quyết định về **tích hợp bên thứ 3** (AI, payment, push, ...)?
- [ ] Quyết định về **quy trình / CI-CD / branch strategy**?

> 📥 **Nguồn để điền:** đây là nơi commit messages + issues toả sáng nhất. Mỗi commit kiểu `fix(security): replace X with Y` hay issue mô tả yêu cầu = một quyết định có sẵn lý do. Lọc commit/issue theo từ khoá: `auth`, `security`, `db`, `migration`, `refactor`.

---

# 5️⃣ FEATURE DEEP-DIVES — Mổ xẻ từng feature

> Trả lời câu phỏng vấn nguy hiểm NGAY SAU "vì sao": **"Kể anh đã XÂY feature X như thế nào?"**
> System design là cái khung; **feature-development là máu thịt** — kinh nghiệm thật nằm ở từng decision point, từng trap, từng bottleneck đã giải khi làm feature. Đừng làm mọi feature — chọn **5-8 cái xương sống**.
> 🔗 **Mỗi feature:** dòng **"Flow"** → mở `CodeBase Understanding` PHASE 4 (trace tới khi HIỂU). Dòng **"vì sao / trap"** → từ commit/issues + đầu bạn.

### Block mẫu (copy cho mỗi feature):

```
### [Tên feature]
- Là gì + vì sao có:                 ___
- Flow end-to-end:                   ___ → ___ → ___
- Quyết định kiến trúc bên trong:    ___
- Vì sao cách này (vs cách khác):    ___
- ⭐ Trap / bottleneck đã gặp & giải: ___   ← phần VÀNG nhất
- Câu phỏng vấn nó trả lời:          "Kể anh làm [feature] thế nào?"
- Bằng chứng:                        commit ___ / issue ___
```

> 📥 **Nguồn để điền:** commit `feat(...)` của feature + issue mô tả nó + code module tương ứng. Đặc biệt soi các commit `fix(...)` QUANH feature đó — chúng chính là "trap đã giải", phần đắt giá nhất khi kể chuyện.

---

# 6️⃣ KNOWN LIMITATIONS & WHAT I'D DO DIFFERENTLY — Giới hạn & nếu làm lại

> Câu "nếu làm lại đổi gì / nợ kỹ thuật là gì?" — biết TRƯỚC = trông như senior + chặn câu gotcha.
> Thành thật về giới hạn cho thấy sự TRƯỞNG THÀNH, không phải điểm yếu.

- **Nợ kỹ thuật đã biết:** ___
- **Cái sẽ làm khác nếu có thời gian/nguồn lực:** ___
- **Đánh đổi đã chấp nhận (và vì sao chấp nhận được lúc đó):** ___
- **Bottleneck sẽ vỡ trước khi scale:** ___

> 📥 Nguồn: commit `TODO`/`FIXME`/`hack`, issue backlog/cancelled, các "gap" ghi trong docs/commit.

---

# 7️⃣ OWNERSHIP & MY CONTRIBUTION — Phần này là CỦA TÔI

> ⭐ Câu chí tử khi code do AI build nhiều: **"Phần nào ANH thật sự làm?"**
> Trả lời tệ = mất hết uy tín. Trả lời tốt = biến "AI làm hộ" thành "tôi chỉ huy & sửa chữa cỗ máy".
> Nguyên tắc: KHÔNG nói dối — nhưng kể đúng phần *judgment* & *quyết định* mình sở hữu.

- **AI / đồng đội xây phần khung nào:** ___
- **TÔI thật sự quyết định / sửa / bắt lỗi gì:** ___ *(judgment, không phải số dòng code)*
- **Bằng chứng quyền tác giả:** ___ *(git authorship, commit, quyết định kiến trúc)*
- **Cách tôi sẽ NÓI về việc dùng AI (trung thực + tự tin):** ___

> 💡 Khung trả lời an toàn: *"AI/team dựng scaffolding; phần tôi sở hữu là [judgment X, bắt bug Y, quyết định Z]. Giá trị tôi mang là biết CÁI GÌ đúng và VÌ SAO — kể cả khi AI làm sai, tôi là người phát hiện và sửa."*

---

# 8️⃣ THE TALK TRACK — Luyện nói (Bài tập cuối)

> Hiểu ≠ Nói được. Phỏng vấn là màn trình diễn dưới áp lực, không phải bài kiểm tra viết.
> Phần này: viết câu hỏi xoáy + tự trả lời thành lời. Đọc TO. Ghi âm. Nghe lại.

### Khung trả lời chuẩn (dùng cho mọi câu "vì sao"):

```
DECISION → TRADEOFF → RESULT
"Bọn em chọn [X] vì [lý do]. Em có cân nhắc [Y] nhưng [đánh đổi].
Kết quả là [điều đạt được / điều học được]."
```

### Ngân hàng câu hỏi (điền câu trả lời của bạn vào):

1. **"Kể về dự án này trong 60 giây."** → ___ *(dùng phần THE SOUL)*
2. **"Vì sao chọn [stack chính]?"** → ___
3. **"Phần khó nhất của hệ thống là gì? Xử lý sao?"** → ___
4. **"Nếu làm lại, anh đổi gì?"** → ___ *(câu tủ — cho thấy tư duy phản biện)*
5. **"Hệ thống scale thế nào khi 100x người dùng?"** → ___
6. **"Chỗ nào trong hệ thống dễ hỏng nhất?"** → ___
7. **"Anh đóng góp phần nào cụ thể?"** → ___ *(câu nhạy cảm — chuẩn bị kỹ: nói về quyết định & định hướng, không phải số dòng code)*

> 📥 **Nguồn để điền:** tổng hợp từ phần 1-3 ở trên. Câu 4 & 7 quan trọng nhất — luyện tới khi trôi chảy.

---

# ✅ Checklist "Tôi đã sẵn sàng nhận tác giả"

Bạn thật sự sở hữu hệ thống khi có thể:

- [ ] Kể được linh hồn sản phẩm trong 60 giây mà không nhìn note
- [ ] Vẽ được kiến trúc ra giấy từ trí nhớ
- [ ] Lý giải MỌI quyết định lớn bằng công thức Decision → Tradeoff → Result
- [ ] Trả lời "nếu làm lại đổi gì" một cách tự tin, có chiều sâu
- [ ] Không nói "tôi không biết vì sao chỗ này vậy" cho bất kỳ quyết định cốt lõi nào
- [ ] Lần theo được ít nhất 2 flow chính end-to-end bằng lời

---

> *"Commit your work to the Lord, and your plans will be established."* — Proverbs 16:3 ✨
>
> Bạn không gian lận khi dùng AI để build. Bạn chỉ chưa nhận lại quyền tác giả. Tài liệu này giúp bạn nhận lại nó — một quyết định một lúc. 🪶🔥
