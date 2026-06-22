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

# 3️⃣ THE DECISION MAP ★ — Bản đồ quyết định (TRÁI TIM)

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

# 4️⃣ THE TALK TRACK — Luyện nói (Bài tập cuối)

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
