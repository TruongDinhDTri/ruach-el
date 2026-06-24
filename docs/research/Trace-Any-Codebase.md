# 🧭 Trace Any Codebase — Field Manual

### Sổ tay thực chiến: trace BẤT KỲ luồng nào, trong BẤT KỲ codebase nào — kể cả code chưa từng nhìn thấy ⚙️🔥

> *"Get wisdom, get understanding; do not forget my words." — Proverbs 4:5*

---

## 📍 Bộ tài liệu này & Khi nào dùng

| | **Trace Any Codebase** (file này) | `CodeBase Understanding` | `Authorship Reclaim` |
| --- | --- | --- | --- |
| Là gì | **Sổ tay THỰC CHIẾN** — 6 bước chạy lệnh thật | Phương pháp đầy đủ (11 phase) | Cách nhận quyền tác giả + luyện nói |
| Trả lời | *"Tay tôi gõ gì để hiểu code này?"* | *"Hệ thống này hoạt động sao?"* | *"Bảo vệ nó như tác giả thật sao?"* |
| Dùng khi | Ngồi xuống trước repo lạ, cần trace NGAY | Muốn hiểu sâu, có hệ thống | Ôn phỏng vấn / nhận tác giả |
| 👉 You are here | **★ BẠN ĐANG Ở ĐÂY** | (tham chiếu đầy đủ) | (đích đến để ghi lại) |

> 💡 File này là bản **distilled** (cô đặc) của `CodeBase Understanding` PHASE 1-4. Nó không thay thế — nó là **bản cầm-tay-làm-ngay**. Cần đào sâu hơn → mở `CodeBase Understanding`.

---

## 🕊️ Linh hồn — Vì sao file này tồn tại

Bạn KHÔNG bao giờ **học thuộc** một codebase. Codebase lớn quá, đổi liên tục — học thuộc là vô vọng.

Thứ một engineer thật sự làm: **lặp đi lặp lại 6 động tác.** Như một bác sĩ không thuộc lòng từng bệnh nhân — họ thuộc **quy trình khám.** Như một nhạc công không nhớ từng nốt của mọi bản — họ đọc được **bản nhạc.**

> **Codebase là bản nhạc. 6 bước này là cách bạn đọc nó.** 🎼
>
> Học 6 bước này = bạn **không còn sợ** bất kỳ codebase nào. Mở ra, áp 6 bước, là thấy đường. Kể cả code bạn chưa từng viết. Kể cả code AI viết. Kể cả code người lạ viết 5 năm trước.

Đó gọi là **gain control back** — giành lại quyền kiểm soát. 💪

---

## ⚖️ Luật vàng (đọc trước khi làm bất cứ gì)

> **❌ ĐỪNG đọc file ngẫu nhiên. ✅ Chọn 1 LUỒNG, đi HẾT nó.**

Mở repo lạ rồi đọc lung tung từng file = lạc trong rừng, càng đọc càng "mông lung". Thay vào đó: chọn **một việc người dùng làm** (login, upload ảnh, thanh toán, gửi tin nhắn) → bám theo nó **từ đầu đến cuối**. Cách này tạo ra **hiểu biết CÓ KẾT NỐI** — vì code thật chạy theo luồng, không theo thứ tự file.

---

# 🪜 6 BƯỚC THỰC CHIẾN — Trái tim của file này

> Mỗi bước có: **(a) Làm gì → (b) Vì sao → (c) Lệnh thật → (d) Nhìn cái gì → (e) Ví dụ Asset Platform.**
> Ví dụ xuyên suốt: trace luồng **AI Capture** (chụp ảnh → nhận diện → vào kho) của Asset Platform.

### 👀 Tổng quan — 6 bước là gì (đọc bảng này TRƯỚC)

> Đây là cả "bộ phim" trong 1 màn hình. Đọc xong bảng này là anh đã nắm cái xương — phần dưới chỉ là chi tiết từng bước.

| Bước | Tên gọi | Làm gì (một câu) | Trả lời câu hỏi |
| :--: | --- | --- | :--: |
| 1️⃣ | **ĐỊNH HƯỚNG** | `ls src/` → đọc tên folder → đoán **domain** nằm đâu | #1 |
| 2️⃣ | **KHOANH VÙNG** | `grep` từ khoá URL → **lọc** kết quả → còn đúng 1 file | #2 |
| 3️⃣ | **TÌM CỬA VÀO** | mở **controller** → thấy route `@Post/@Get` (điểm request đập vào) | #1, #2 |
| 4️⃣ | **VÀO BỘ NÃO** | controller gọi **service** → đọc business logic thật | #3, #4, #5 |
| 5️⃣ | **CHẠM DỮ LIỆU** | service đọc/ghi **DB** → biết đụng **bảng** nào | #6 |
| 6️⃣ | **SOI ĐUÔI** | xem **return** + việc chạy **ngầm** (job/cron/event) | #7, #8 |

> 🧠 **Mạch logic xuyên suốt:** đi từ NGOÀI VÀO TRONG — *ngoài cùng là nơi user gõ (cửa vào) → vào trong là nơi suy nghĩ (logic) → tận đáy là nơi cất giữ (DB) → rồi quay ra (response).* Cứ men theo **lời gọi hàm** mà đi, như lần theo sợi chỉ.

```
  1️⃣ ĐỊNH HƯỚNG   2️⃣ KHOANH VÙNG   3️⃣ TÌM CỬA VÀO   4️⃣ VÀO BỘ NÃO   5️⃣ CHẠM DỮ LIỆU   6️⃣ SOI ĐUÔI
    ls src/     →   grep + lọc    →   mở CONTROLLER  →    SERVICE    →     DB/REPO     →  RETURN + ngầm
  (đoán domain)   (xác nhận file)   (route vào)       (logic)         (đụng bảng)      (response+job)
       │               │                 │               │                │               │
    PHASE 1&3      lọc kết quả         PHASE 2     ──────────── men theo dòng gọi hàm ────────────
```

---

## 🟦 BƯỚC 1 — ĐỊNH HƯỚNG · `ls src/` → đọc tên folder → đoán domain

**(a) Làm gì:** Liệt kê thư mục gốc của source. Đọc **tên folder** như đọc mục lục một cuốn sách.

**(b) Vì sao:** Backend/frontend tốt tổ chức theo **feature/domain** — mỗi nghiệp vụ một folder, **đặt tên theo nghiệp vụ.** Tên folder = bản đồ thô. Đây là khởi đầu của *"map cấu trúc TRƯỚC khi đọc chi tiết."*

**(c) Lệnh thật:**
```bash
ls apps/api/src/            # backend
ls apps/web/src/ apps/web/app/   # frontend
```

**(d) Nhìn cái gì:** Tên folder nào nói lên domain? `payments/` = tiền. `auth/` = đăng nhập. `chat/` = tin nhắn. Folder lạ (`common/`, `shared/`, `config/`) = hạ tầng, để sau.

**(e) Ví dụ Asset Platform:**
```bash
$ ls apps/api/src/
admin   ai   auth   chat   common   config   database   items
mail    marketplace   notifications   payments   reminders   reports
reviews   shared   sharing   storage   transactions   types   users
```
→ Muốn trace AI Capture? Mắt dừng ngay ở **`ai/`** và **`items/`**. Chưa cần mở file nào — tên folder đã chỉ đường. 🎯

> 🔗 *Tương ứng `CodeBase Understanding` PHASE 1 (Orient) + PHASE 3 (Map Architecture).*

---

## 🟩 BƯỚC 2 — KHOANH VÙNG · `grep` từ khoá → xác nhận file (+ lọc kết quả)

**(a) Làm gì:** Đừng đoán mò. Lấy **từ khoá từ URL hoặc tên tính năng** rồi search toàn repo.

**(b) Vì sao:** Route, tên hàm, tên biến **nằm ngay trong code** — search ra là thấy. Frontend gọi `/api/ai/recognize`? → search `recognize`.

**(c) Lệnh thật:**
```bash
grep -rn "recognize" apps/api/src/ --include=*.ts
# hoặc dùng ripgrep (nhanh hơn):  rg "recognize" apps/api/src
```

**(d) Nhìn cái gì — ⚠️ ĐÂY LÀ CHỖ DỄ NGỘP:** Search ra **58 kết quả / 23 file** thì biết chọn cái nào? → **Lọc theo VAI TRÒ của file** (xem bảng ngay dưới). Bạn đang tìm **cửa vào** → chỉ quan tâm `*.controller.*`.

**(e) Ví dụ Asset Platform:** search `recognize` ra 58 kết quả, gồm:
- `ai.controller.ts` ← 🚪 **CỬA VÀO — cái cần tìm**
- `ai.controller.spec.ts` ← test, BỎ QUA
- `vision-recognition.service.ts` ← logic, để BƯỚC 4
- `recognize-asset.dto.ts` ← validate, để BƯỚC 4
- `README.md` ← docs, chỉ để xác nhận
→ Lọc xong, từ 58 còn **1 file** cần mở: `ai.controller.ts`. 😮‍💨

### 🔍 Bảng lọc kết quả search — phân loại theo VAI TRÒ file

| Đuôi / tên file | Vai trò | Khi tìm luồng |
| --- | --- | --- |
| `*.controller.*`, `routes/*`, `*.view.*`, `urls.py` | 🚪 **Cửa vào** (route) | ✅ **CÁI CẦN TÌM** |
| `*.service.*`, `*.usecase.*`, `*.handler.*` | 🧠 Business logic | ✅ đi tới ở BƯỚC 4 |
| `*.dto.*`, `*.schema.*`, `*.validator.*` | 🛂 Validate input | ✅ xem ở BƯỚC 4 |
| `*.entity.*`, `*.model.*`, `*.repository.*` | 🗄️ Hình dạng & truy cập DB | ✅ xem ở BƯỚC 5 |
| `*.spec.*`, `*.test.*`, `__tests__/*` | 🧪 Test | ⏭️ **BỎ QUA** (lúc tìm luồng) |
| `*.md`, `README`, `docs/*` | 📖 Tài liệu | 👀 xác nhận, không phải code |
| `*.module.*`, `*.config.*`, `*.providers.*` | 🔌 Lắp ráp / cấu hình | 🔧 xem khi cần hiểu wiring |

> 💎 **Mẹo:** muốn bớt nhiễu ngay từ đầu, grep kèm pattern file: `grep -rn "recognize" --include=*.controller.ts` → chỉ tìm trong cửa vào.

---

## 🟨 BƯỚC 3 — TÌM CỬA VÀO · mở CONTROLLER → `@Post/@Get`

**(a) Làm gì:** Mở file controller. Tìm **route decorator/khai báo** — đó là điểm request HTTP đập vào đầu tiên. Trả lời được **câu 1 & 2** (cái gì kích hoạt + API nào).

**(b) Vì sao:** Cửa vào là **mỏ neo điều hướng.** Từ đây mọi thứ tỏa ra. Tìm được cửa = tìm được sợi chỉ để kéo cả cuộn.

**(c) Lệnh thật:**
```bash
grep -n "@Post\|@Get\|@Patch\|@Delete\|@Controller" apps/api/src/ai/ai.controller.ts
```

**(d) Nhìn cái gì:** route path, HTTP method, **guard** (ai được vào?), **validation pipe**, và **controller gọi service nào** (đây là cây cầu sang BƯỚC 4).

**(e) Ví dụ Asset Platform** — `apps/api/src/ai/ai.controller.ts:37`:
```ts
@Controller('ai')              // → mọi route bắt đầu bằng /api/ai
@UseGuards(JwtAuthGuard)       // 🛡️ phải đăng nhập
export class AiController {
  @Post('recognize')                          // 🚪 CỬA VÀO: POST /api/ai/recognize
  @Throttle({ default: { ttl: 60_000, limit: 20 } })  // 🛡️ tối đa 20 lần/phút
  async recognize(@Body() dto: RecognizeAssetDto) {    // 🛂 validate bằng DTO
    return this.visionRecognitionService.recognizeFromBase64(...);  // ➡️ sang BƯỚC 4
  }
}
```
→ Một file controller đã trả lời: API nào (`POST /api/ai/recognize`), ai vào được (đã login), giới hạn (20/phút), và **nó gọi `visionRecognitionService`** — đi tiếp!

> 🔗 *Tương ứng `CodeBase Understanding` PHASE 2 (Find Entry Points).*

---

## 🟧 BƯỚC 4 — VÀO BỘ NÃO · Controller → SERVICE (business logic)

**(a) Làm gì:** Đi theo lời gọi từ controller xuống **service** — nơi nghiệp vụ thật sự xảy ra. Trả lời **câu 3, 4, 5** (validate ở đâu, logic ở đâu, state đổi ở đâu).

**(b) Vì sao:** Controller chỉ là người gác cổng — nó **mỏng**. Mọi quyết định, tính toán, gọi bên thứ ba đều nằm trong service. **Đây là nơi "đọc hiểu" thật sự.**

**(c) Lệnh thật:**
```bash
grep -n "async \|return\|this\.\|await" apps/api/src/ai/vision-recognition.service.ts | head -30
```

**(d) Nhìn cái gì:** điều kiện rẽ nhánh (if/else), gọi API ngoài (OpenAI, Stripe...), biến đổi dữ liệu, và **nó gọi repository/DB nào** (cầu sang BƯỚC 5).

**(e) Ví dụ Asset Platform** — `vision-recognition.service.ts:32` `recognizeFromBase64()`:
- nếu `OPENAI_LOCAL_MODE` → trả **mock** (khỏi tốn tiền);
- `detectImageMime()` tin bytes thật hơn client (tránh OpenAI reject);
- gọi **OpenAI gpt-4o-mini** với prompt tiếng Việt + ép **JSON schema strict** → trả `{name, brand, model, category, confidence}`.
→ Đây là toàn bộ "bộ não" của tính năng. Controller chỉ 3 dòng — service mới là 100 dòng.

---

## 🟥 BƯỚC 5 — CHẠM DỮ LIỆU · Service → DB/REPOSITORY (đụng bảng nào)

**(a) Làm gì:** Tìm nơi dữ liệu được **đọc/ghi xuống database.** Trả lời **câu 6** (đụng bảng DB nào).

**(b) Vì sao:** Cuối cùng mọi hệ thống đều là **biến đổi dữ liệu rồi lưu lại.** Biết nó ghi vào bảng nào = biết "sự thật" của hệ thống nằm ở đâu (source of truth).

**(c) Lệnh thật:**
```bash
grep -n "Repository\|\.save\|\.create\|\.find\|INSERT\|UPDATE" apps/api/src/items/items.service.ts
ls apps/api/src/items/entities/      # xem entity = hình dạng bảng
```

**(d) Nhìn cái gì:** repository nào được inject, gọi `.save()/.create()/.update()` lên entity nào, có gắn `userId` (ownership) không, có transaction/lock không (quan trọng với tiền).

**(e) Ví dụ Asset Platform** — `items.service.ts` `create()`:
```ts
const item = this.itemsRepository.create({ ...dto, userId });  // gắn chủ sở hữu
const saved = await this.itemsRepository.save(item);            // 🗄️ ghi vào bảng items
```
→ Bảng bị đụng: **`items`**. Source of truth của tài sản nằm ở đây.

> 🔗 *Tương ứng `CodeBase Understanding` PHASE 5 (Data Model).*

---

## 🟪 BƯỚC 6 — SOI ĐUÔI · RETURN + side-effect (response + job ngầm)

**(a) Làm gì:** Nhìn **cái gì trả về cho client** và **việc gì chạy NGẦM** sau đó. Trả lời **câu 7 & 8** (background job + response).

**(b) Vì sao:** Nhiều bug & nhiều "điểm vàng phỏng vấn" nằm ở đây: fire-and-forget, cron, event, webhook. Đây là phần người mới hay bỏ sót.

**(c) Lệnh thật:**
```bash
grep -n "return\|void \|emit\|enqueue\|@Cron\|setTimeout\|fireAndForget\|\.then(" apps/api/src/items/items.service.ts
```

**(d) Nhìn cái gì:** shape của response trả về; lời gọi **không `await`** (chạy ngầm); event được `emit`; cron/queue được đẩy.

**(e) Ví dụ Asset Platform** — sau khi `save()`:
```ts
this.triggerConditionAssessment(saved.id, saved.photos);   // chạy ngầm, không await
void this.priceHistoryService.recordSnapshot(saved, ...);  // best-effort, never throws
return saved;                                              // response: Item vừa lưu
```
→ Response = Item. Job ngầm = đánh giá tình trạng + chụp snapshot giá. Không chặn lúc lưu. 💎

---

# 🚪 KỸ NĂNG RIÊNG: Tìm "CỬA VÀO" của BẤT KỲ module nào

Câu hỏi muôn thuở: *"File nào là cửa vào?"* — Tùy framework, nhưng luôn có **một quy ước.** Học bảng này = mở repo bất kỳ stack nào cũng tìm được cửa trong 10 giây:

| Stack / Framework | Cửa vào (route) nằm ở | Dấu hiệu nhận biết |
| --- | --- | --- |
| **NestJS** (Asset Platform) | `*.controller.ts` | `@Controller()`, `@Get/@Post()` |
| **Express / Fastify** | `routes/`, `*.routes.js`, `app.js` | `router.get('/...', handler)` |
| **Next.js (App Router)** | `app/api/**/route.ts` | `export async function GET/POST()` |
| **Django** | `urls.py` → `views.py` | `path('...', view)` |
| **Flask / FastAPI** | file có `@app.route` / `@router.get` | decorator route |
| **Spring Boot** | `*Controller.java` | `@RestController`, `@GetMapping` |
| **Rails** | `config/routes.rb` → `app/controllers/` | `resources :x` |
| **Go (net/http)** | `main.go`, `routes.go` | `mux.HandleFunc("/...")` |

### 📖 "Mục lục" & "công tắc khởi động" của backend

Hai file luôn đáng đọc đầu tiên trong mọi backend:

```bash
cat apps/api/src/main.ts        # 🔌 CÔNG TẮC: app khởi động thế nào
cat apps/api/src/app.module.ts  # 📖 MỤC LỤC: nạp những module/phòng ban nào
```

**Ví dụ Asset Platform:**
- `main.ts` → `bootstrap()`: `cookieParser` → `enableCors` → `useGlobalPipes` (validate toàn cục) → `setGlobalPrefix('api')` → `listen(port)`. *Đọc 1 file = hiểu cách app dựng lên.*
- `app.module.ts` → import `AiModule, AuthModule, ItemsModule, ChatModule, PaymentGatewayModule, TransactionsModule...` + `ThrottlerModule` (rate-limit) + `ScheduleModule` (cron) + `TypeOrmModule` (DB). *Đọc 1 file = thấy TOÀN BỘ "phòng ban".*

> 💡 Lạc trong repo lạ? Về `main` → `app.module` (hoặc tương đương). Đó là **đỉnh núi để nhìn toàn cảnh.**

---

# 🎬 KỸ NĂNG RIÊNG: TRACE FRONTEND & "ĐỔI SÂN" khi dấu vết nguội

> Đọc mục này khi: trace tới backend thì hàm kết thúc bằng `return` cho client, mà luồng **vẫn chưa xong** (vd: nhận diện xong rồi mới *lưu*). Đây là lúc dấu vết "nguội".

## ❄️ Vấn đề: luồng "đứt" ở chữ `return`

Một endpoint backend chạy xong, `return` kết quả về cho client, rồi **ngủ.** Nếu bạn cứ ngồi trong backend tìm "bước tiếp theo" → **không thấy đâu cả** — và đó **không phải lỗi của bạn.**

> 🔑 **Nguyên lý vàng:** *Một HTTP request = MỘT nửa của luồng. Backend KHÔNG tự nối các nửa — **frontend (hoặc hành vi user) mới là thứ khâu chúng lại**, bằng điều hướng màn hình (router) hoặc bằng một request MỚI khi user bấm nút.*

→ Vậy khi dấu vết nguội ở `return`: **ĐỪNG tìm trong backend nữa. ĐỔI SÂN sang frontend.**

## 🎬 Kỹ thuật "ĐỔI SÂN" — 3 nước

1. **Search LẠI cùng từ khoá**, nhưng trong folder frontend (`apps/web`, `apps/mobile`...). ⚠️ **Exclude** `node_modules` + thư mục build/log (`.next`, `.expo`, `.turbo`, `*.log`) — không thì rác chôn mất file thật.
2. **Đoán web hay mobile:** tính năng cần camera/GPS/push → thường là **mobile**; search ra toàn `node_modules` → không nằm ở sân đó.
3. **Lọc theo folder convention của frontend** (bảng dưới — khác backend).

| Folder / đuôi | Vai trò |
| --- | --- |
| `services/`, `api/`, `lib/` | 📡 Lớp gọi API — **URL nằm Ở ĐÂY** |
| `app/`, `pages/`, `screens/`, `routes/` | 🖼️ Màn hình (user nhìn & bấm) |
| `components/` | 🧩 UI tái dùng |
| `hooks/`, `store/`, `context/` | 🧠 State / logic dùng chung |
| `*.tsx` = có UI · `*.ts` = logic thuần | |

## ⚠️ BẪY 3 LỚP: màn hình thường KHÔNG chứa URL

Frontend tốt **tách lớp**: *màn hình gọi HÀM → lớp service mới gửi HTTP.* Đừng trông chờ thấy `/api/...` ngay trong file màn hình — mở lớp `services/api` mới thấy URL. *(Vì sao? đổi endpoint sửa 1 chỗ, mọi màn hình hưởng theo.)*

```
🖼️ Màn hình  ─gọi HÀM─▶  📡 Lớp service FE  ─gửi HTTP─▶  🚪 API/controller ─▶ 🧠 service ─▶ 🗄️ DB
(BƯỚC 1·ngoài)            ⚠️ CHẶNG ẨN (giữ URL)            (BƯỚC 3·cửa vào)    (BƯỚC 4·logic)  (BƯỚC 5)
└──────────────────────────── đi từ NGOÀI VÀO TRONG ──────────────────────────────────────────▶ (đáy)
```

> 🧪 *Ví dụ ngắn (Asset Platform):* màn hình chỉ gọi `aiApi.recognizeAsset()`; URL thật `/ai/recognize` nằm trong file `aiApi.ts`. Nút bấm không lưu ngay — nó **điều hướng** (`router`) sang màn hình khác, nơi đó mới gọi API lưu → 2 nửa backend được khâu bằng frontend.

> 🔑 **Mang theo cả đời:** backend `return` mà luồng chưa xong → ĐỔI SÂN sang frontend; search cùng từ khoá (exclude node_modules/build); URL ở lớp `services/api`, không ở màn hình; các nửa nối nhau bằng điều hướng (router) hoặc request mới do user kích hoạt.

---

# 🧠 8 CÂU HỎI XƯƠNG SỐNG — checklist mà 6 bước trả lời

Trace xong 1 luồng = trả lời được 8 câu này. In ra, đánh dấu từng câu:

```
[ ] 1. Cái gì KÍCH HOẠT luồng này?     → BƯỚC 1-3 (user action → route)
[ ] 2. API nào được gọi?               → BƯỚC 3 (@Post/@Get)
[ ] 3. Validate ở đâu?                 → BƯỚC 3-4 (DTO/pipe)
[ ] 4. Business logic ở đâu?           → BƯỚC 4 (service)
[ ] 5. State cập nhật ở đâu?           → BƯỚC 5 (repository.save)
[ ] 6. Đụng bảng DB nào?               → BƯỚC 5 (entity)
[ ] 7. Background job nào chạy?        → BƯỚC 6 (không-await/cron/event)
[ ] 8. Response trả về cái gì?         → BƯỚC 6 (return)
```

---

# 🃏 CHEAT CARD — dán cạnh máy

```
┌─ TRACE ANY CODEBASE — 6 BƯỚC ───────────────────────────────
│ Luật vàng: chọn 1 LUỒNG, đi HẾT. Đừng đọc file ngẫu nhiên.
│
│ 1. ĐỊNH HƯỚNG    ls src/           → folder = domain    (câu 1)
│ 2. KHOANH VÙNG   grep + lọc        → còn 1 file         (câu 2)
│ 3. TÌM CỬA VÀO   mở *.controller   → @Post/@Get         (câu 1,2)
│ 4. VÀO BỘ NÃO    → service         → business logic     (câu 3,4,5)
│ 5. CHẠM DỮ LIỆU  → repository/DB   → đụng bảng nào       (câu 6)
│ 6. SOI ĐUÔI      return + ngầm     → response + job ngầm (câu 7,8)
│
│ Lạc? → cat main.ts (công tắc) + app.module.ts (mục lục)
│ Lọc search: controller=cửa · service=logic · .spec=BỎ QUA
│ Backend `return` rồi mà chưa xong? → ĐỔI SÂN sang frontend,
│   search cùng từ khoá (exclude node_modules). URL ở services/api.
│
│ ── 4 THẾ KIẾM (chi tiết ở chương mở rộng cuối file) ────────
│ ① XUÔI    user làm X → gì xảy ra        (chính 6 bước trên)
│ ② NGƯỢC   giá trị SAI → grep nó → lần NGƯỢC lên nguồn (debug)
│ ③ KO-REQUEST  @Cron · emit/@OnEvent · webhook/IPN  (ai đánh thức?)
│ ④ DỮ LIỆU  theo 1 field: grep "x =" (ghi) vs "x" (đọc)
│ Đọc TĨNH chết? → ĐỔI NHẠC CỤ: log · breakpoint · git log -S
└──────────────────────────────────────────────────────────────
```

---

# ⚔️ CHƯƠNG MỞ RỘNG: 4 THẾ KIẾM — trace ANY thing

> 6 bước ở trên dạy anh **THẾ XUÔI**: *user bấm nút → request → controller → service → DB → return.* Đẹp, sắc — nhưng đó là **1 trong 4 thế** của cùng thanh kiếm.
>
> Vì "trace any **flow**, any **data**, any **thing**" đòi hỏi vung gươm theo **mọi hướng**. Cả 4 thế dùng chung một xương sống (`trigger → cửa vào → logic → data → lối ra`); cái thay đổi là **anh bắt đầu từ đâu, cái gì kích hoạt, anh đi theo cái gì.**

| Thế | Câu hỏi mở màn | Đi theo | Dùng khi |
| :--: | --- | --- | --- |
| ① **XUÔI** | *"User làm X → gì xảy ra?"* | hành động, theo thời gian | hiểu feature, onboard |
| ② **NGƯỢC** | *"Giá trị này SAI/lạ → từ đâu ra?"* | mũi tên đảo chiều | **debug**, data lineage |
| ③ **KHÔNG-REQUEST** | *"Không ai bấm — sao nó chạy?"* | trigger phi-HTTP | cron, event, webhook |
| ④ **DỮ LIỆU** | *"Field này: ai ghi, ai đọc?"* | một danh từ, theo không gian | hiểu một dữ liệu xuyên hệ thống |

> 🧠 **Mấu chốt:** Thế ① đi theo **VERB** (động từ, qua thời gian). Thế ④ đi theo **NOUN** (danh từ, qua các file). Thế ② **đảo chiều mũi tên**. Thế ③ đổi câu hỏi *"user làm gì"* thành *"ai/cái gì đánh thức code này dậy?"*

---

## 🧭 LA BÀN CHỌN THẾ — *khi nào rút thế nào* (đọc TRƯỚC khi vung)

> Phần khó nhất của trace KHÔNG phải *"trace sao"* — mà là ***"tình huống này, nên trace KIỂU gì?"*** Rút nhầm thế = đào sai hướng, càng đào càng *mông lung*. La bàn này chữa đúng chỗ đó.

**🔑 Nguyên lý vàng:** Đừng hỏi *"tôi biết thế nào?"* — hỏi **"NGAY BÂY GIỜ trong đầu tôi đang cầm CÁI GÌ?"** Điểm xuất phát quyết định thế kiếm:

| Trong đầu anh đang cầm... | Mục tiêu — muốn cầm được... | → RÚT THẾ |
| --- | --- | :--: |
| Một **HÀNH ĐỘNG** user ("khi bấm Lưu…") — muốn hiểu nó chạy sao | bản đồ luồng đầy đủ + 8 câu xương sống | **① XUÔI** |
| Một **TRIỆU CHỨNG SAI** (số lạ, lỗi, output vô lý) — chưa biết vì sao | đúng dòng code bẻ gãy + lý do | **② NGƯỢC** |
| Một **HIỆN TƯỢNG TỰ XẢY RA** (không ai bấm) *hoặc* tìm controller mà **không thấy** | cái gì đánh thức nó + việc ngầm | **③ KHÔNG-REQUEST** |
| Một **CÁI TÊN dữ liệu** (field/cột/biến) — muốn biết nó sống sao | nơi sinh–biến đổi–hiện của field | **④ DỮ LIỆU** |
| (đang dùng thế nào đó) mà **đọc code TẮC**, lần không tiếp được | đường đi THẬT lúc chạy | **🎛️ ĐỔI NHẠC CỤ** |

**🔮 Câu thần chú nhận diện** — nghe thấy mình lẩm bẩm câu nào, rút thế đó:

- *"Tính năng này chạy thế nào?"* → **① XUÔI**
- *"Ơ sao nó ra số này / sao lỗi này?"* → **② NGƯỢC**
- *"Ủa không ai làm gì mà sao nó vẫn…?"* → **③ KHÔNG-REQUEST**
- *"Cái `xyz` này từ đâu ra / ai đụng tới nó?"* → **④ DỮ LIỆU**
- *"Đọc hoài không thấy ai gọi hàm này…"* → **🎛️ ĐỔI NHẠC CỤ**

### ⚖️ SO SÁNH — cùng MỘT chủ thể, 4 câu hỏi, 4 thế

> Để thấy 4 thế là **4 ỐNG KÍNH khác nhau** (KHÔNG phải 4 bước nối tiếp): cùng soi vào **"giá của một món đồ"** trong Asset Platform —

| Cùng hỏi về *giá*, nhưng… | Thế | Đào ra |
| --- | :--: | --- |
| "User chụp ảnh → lưu món, luồng chạy sao?" | ① | AI Capture: review → `/items` → service → bảng `items` |
| "Sao món **9.87M₫** lại gợi ý **246 TỶ**?" | ② | `toValuationRequest()` nhân nhầm FX — điểm bẻ gãy |
| "Sao **khấu hao** tự đổi mỗi đêm dù không ai sửa?" | ③ | cron *nightly valuation* — time-triggered, không request |
| "`purchasePrice` lưu đơn vị gì, ai ghi, ai đọc?" | ④ | VND-canonical; ghi lúc `create`, đọc ở valuation + UI |

> 💡 **Cùng một miền (giá tiền), 4 cuộc điều tra hoàn toàn khác nhau.** Chọn sai ống kính = soi nhầm chỗ, mất buổi chiều.

### 🔗 GHÉP THẾ — điều tra thật thường XÍCH nhiều thế

Thực chiến hiếm khi xài đúng 1 thế. Ba chuỗi hay gặp:

- **② → ④** (debug → đo blast radius): bắt bug (NGƯỢC) thấy 1 field hỏng → trace chính field đó (DỮ LIỆU) xem nó còn vấy bẩn chỗ nào trước khi fix. *(Đúng bug 246 tỷ: NGƯỢC tìm ra → DỮ LIỆU lộ nó lan cả admin escrow.)*
- **① → 🎛️** (hiểu → tắc → đổi nhạc cụ): trace xuôi tới chỗ DI/reflection, đọc tĩnh chết → đặt breakpoint xem call stack thật.
- **① → ③** (hiểu → gặp việc ngầm): trace feature xuôi tới `return`/`save`, thấy lời gọi **không-await** → chuyển thế ③ truy việc ngầm (cron/emitter).

---

## 🔄 THẾ ② — TRACE NGƯỢC · từ TRIỆU CHỨNG về NGUỒN

**(a) Làm gì:** Bắt đầu ở **LỐI RA** (con số sai trên UI, dòng lỗi trong log, ô DB bất thường) rồi đi **NGƯỢC** lên cửa vào — ngược chiều 6 bước.

**(b) Vì sao:** Khi debug, anh không có "user action" để bắt đầu — anh chỉ có **một triệu chứng.** Đọc xuôi cả codebase tìm bug = mò kim đáy bể. Đọc ngược từ triệu chứng = lần sợi chỉ về đúng ổ.

**(c) 5 nước đi ngược:**
```
1. CHỘP triệu chứng chính xác   → con số "246000000000", message lỗi, tên field
2. grep CHÍNH triệu chứng đó     → grep -rn "USD_TO_VND_RATE\|vndToUsd\|valuation"
3. Tìm nơi GHI/ĐỊNH DẠNG ra nó   → write-site, KHÔNG phải read-site
4. Lần NGƯỢC từng lớp gọi        → "ai đưa value này vào?" (Find usages / grep tên biến)
5. Dừng ở ĐIỂM BẺ GÃY            → chỗ value đúng hoá thành sai
```

**(d) Nhìn cái gì:** phép biến đổi đáng ngờ (×, ÷, parse, cast, format), ranh giới đơn vị (USD↔VND, ms↔s), nơi dữ liệu đổi tay giữa 2 module.

**(e) Ví dụ Asset Platform — bug "246 TỶ ₫" (`a1c2ebc`):**
> Triệu chứng: món **9.87M₫** gợi ý giá **246 tỷ ₫** (tràn cả cột DB). → grep `valuation` + `vndToUsd` → tìm ra `toValuationRequest()` chạy `vndToUsd()` trên giá vốn **đã là VND** → nhân nhầm ~25.000× → điểm bẻ gãy: **invariant tiền tệ sai.** Anh KHÔNG đọc xuôi — anh thấy *output vô lý* rồi lần ngược về phép nhân. **Đó là Thế ②.**

> 💎 Đây chính là câu chuyện phỏng vấn vàng của anh (Decision Map §J1). Reverse-trace **là** kỹ năng đã bắt được nó.

---

## ⏰ THẾ ③ — KHI TRIGGER KHÔNG PHẢI REQUEST

**(a) Làm gì:** Tìm cửa vào cho luồng **không do user gõ.** Câu hỏi đổi từ *"API nào?"* sang ***"AI/CÁI GÌ đánh thức code này dậy?"***

**(b) Vì sao:** Rất nhiều "sự sống" của hệ thống chạy ngầm — không request, không màn hình. Nếu chỉ biết tìm controller, anh **mù** với nửa hệ thống này.

**(c) Bảng cửa vào theo loại trigger:**

| Trigger | "Ai đánh thức?" | grep dấu hiệu | Ví dụ Asset Platform |
| --- | --- | --- | --- |
| ⏰ **Cron / lịch** | **Thời gian** | `@Cron`, `@Interval`, `CronJob`, `@nestjs/schedule` | escrow **auto-release 72h**, nightly valuation |
| 🔔 **Event / emitter** | **Sự kiện nội bộ** | `emit(`, `@OnEvent`, `EventEmitter`, `.on(` | **Notification emitter**: `transition()` → `notificationsService.create()` |
| 💸 **Webhook / IPN** | **Hệ thống NGOÀI gọi vào** | `webhook`, `ipn`, `callback`, `verify`, `hmac` | **MoMo IPN** `@Post` + verify HMAC-SHA256 |
| 📨 **Queue / worker** | **Message trong hàng đợi** | `@Process`, `Queue`, `consume`, `worker` | (Redis sẵn — đường mở rộng tương lai) |

**(d) Nhìn cái gì:** với **cron** → cửa vào là **method gắn `@Cron`** (không URL!), từ đó trace xuôi tiếp bước 4-6. Với **webhook** → *trông* giống Thế ① (cũng là controller) nhưng mối lo cốt lõi là **verify chữ ký + idempotency** (vì attacker có thể giả request). Với **emitter** → để tìm "notification sinh ra sao", grep **`notificationsService.create(`** rồi tìm **mọi nơi gọi nó.**

**(e) Ví dụ Asset Platform:**
- ⏰ **Escrow auto-release:** không ai bấm — cron `@nestjs/schedule` thức dậy sau 72h → gated bằng `pg_try_advisory_lock` (chống 2 instance đua) → release tiền. Cửa vào = method `@Cron`.
- 🔔 **Notification:** producer (escrow `transition()`, chat mới, sharing invite, warranty cron) gọi `NotificationsService.create()`, **bọc try/catch** để lỗi notification KHÔNG phá FSM escrow (`1fecb53`). Trace ngược từ `.create()` ra mọi producer = thấy toàn bộ "ai sinh thông báo".
- 💸 **MoMo IPN** (`e8b0b25`): MoMo (ngoài) POST vào webhook → `crypto.timingSafeEqual` so HMAC → row-lock `SELECT...FOR UPDATE` + idempotency key → ghi `payment_events` (append-only ledger).

---

## 🏷️ THẾ ④ — TRACE MỘT DỮ LIỆU (data lineage)

**(a) Làm gì:** Không theo *một hành động*, mà theo **một FIELD** xuyên suốt codebase: nó **SINH ra** ở đâu → **BIẾN ĐỔI** ở đâu → **HIỆN / CHẾT** ở đâu.

**(b) Vì sao:** Nhiều câu hỏi không phải "luồng nào" mà là *"giá trị `depreciatedValue` này từ đâu mà có, và ai dựa vào nó?"* Đây là đi theo **danh từ qua không gian**, không phải động từ qua thời gian.

**(c) Hai cú grep cốt tử:**
```bash
# Nơi GHI (write-site): tìm phép gán + lưu
grep -rn "depreciatedValue\s*=\|\.depreciatedValue\s*=" apps/api/src/

# Nơi ĐỌC (read-site): tìm mọi nơi tiêu thụ
grep -rn "depreciatedValue" apps/api/src/ apps/web/ apps/mobile/
```

**(d) Nhìn cái gì:** **ENTRY** (input thô từ đâu: DTO? AI response? form?) → **TRANSFORM** (công thức nào chạm vào) → **STORE** (cột entity/migration nào) → **EXIT** (shape response API + nơi UI render). Xếp các điểm chạm thành **"bản đồ đời của dữ liệu".**

**(e) Ví dụ Asset Platform — `sellerPayoutVND` (`74e5aa4`):**
> SINH: tính lúc escrow release = `priceVND − commissionVND` (`PLATFORM_COMMISSION_RATE` 2%). LƯU: cột trên transaction. ĐỌC: payout cho seller + hiện ở admin panel. → một field, ba điểm chạm, một bản đồ rõ. *(Cùng họ với bug tiền tệ: `depreciatedValue`/giá lưu **VND-canonical**, engine định giá chuyển USD ở **biên** — Decision Map §J1.)*

---

## 🎛️ KỸ NĂNG VẮT NGANG — ĐỔI NHẠC CỤ khi đọc TĨNH chết

> Cả 4 thế trên đều là **đọc tĩnh** (đọc code đứng yên). Đôi khi đọc tĩnh **chết** — DI/reflection, dynamic dispatch, config-driven, code generate, "không thấy ai gọi hàm này". Lúc đó: **đừng đọc nữa — ĐỔI DỤNG CỤ QUAN SÁT.**

| Nhạc cụ | Khi nào | Cho anh thấy |
| --- | --- | --- |
| 🪵 **Log tạm** | nghi luồng đi đường nào | thứ tự chạy THẬT, giá trị THẬT |
| 🔴 **Breakpoint + debugger** | "ai gọi tới đây?" | **call stack thật** = Thế ② do máy làm hộ (cả chuỗi gọi hiện ngay) |
| 📜 **Log hệ thống đang chạy** | bug chỉ xảy ra lúc chạy | lỗi thật, request thật |
| ⏳ **`git log -S"chuỗi"` + `git blame`** | "vì sao dòng này tồn tại?" | commit thêm/sửa nó → **đọc commit message = đọc Ý ĐỊNH** |

> 🔑 **"Đổi sân sang frontend"** (mục trên) chỉ là **MỘT ca đặc biệt** của nguyên lý này: trail nguội ở backend `return` → đổi *sân quan sát* (backend→frontend). Nguyên lý lớn: **trail nguội → đổi nhạc cụ** (tĩnh→động, code→lịch-sử-git, backend→frontend).
>
> 💡 *Mẹo vàng:* một breakpoint trả lời "ai gọi hàm này?" nhanh hơn cả giờ đọc code — vì **call stack chính là đường đi ngược** mà Thế ② phải lần thủ công.

---

# 🔗 Cầu nối — Đi đâu tiếp

| Khi bạn... | Nhảy sang | Để làm gì |
| --- | --- | --- |
| Cần phương pháp đầy đủ, sâu hơn | `CodeBase Understanding` PHASE 1-11 | Hiểu có hệ thống (orient → entry → map → trace → data → run → fail → boundaries → tests → ops → tự vẽ map) |
| Đã trace xong 1 luồng, muốn GHI LẠI | `Authorship Reclaim` ô **3B** / **Feature Deep-Dive** | Gắn WHY + trade-off + luyện kể phỏng vấn |
| Cần dựng sơ đồ kiến trúc tổng | `CodeBase Understanding` PHASE 3 (STEP 4) | Vẽ component map trước khi trace chi tiết |

> **HOW (file này) là nền. WHY (Authorship Reclaim) xây trên nó.** Trace để HIỂU cách nó chạy → rồi mới hỏi được "vì sao chọn vậy".

---

> *"Commit your work to the Lord, and your plans will be established." — Proverbs 16:3*
>
> Mở repo lạ ra. Đừng sợ. Áp 6 bước. Bạn sẽ thấy đường. ⚙️🔥
