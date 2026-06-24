# 🏛️ Asset Platform — Decision Map

> **Instance** clone từ `Authorship-Reclaim-Playbook.md`. Đây là tài liệu ÔN PHỎNG VẤN của Wiganz cho dự án Asset Platform.
> Trạng thái: 🚧 ĐANG ĐIỀN — mình điền chung, từng quyết định một (kiểu Socratic).
>
> 📌 Phần 1-8: điền tay, có suy nghĩ. Phần dưới (📚 Appendix): nguyên liệu thô đã đào sẵn từ 246 commit + 300 issues.

---

## 🔗 LIÊN KẾT 2 FILE — Đến đâu, nhảy đâu, hỏi gì

> **Sống ở file NÀY (Decision Map).** Vài ô cần với tay mở **dụng cụ** ra — vì cần hiểu code THẬT, không đoán mò. Còn lại điền thẳng.
>
> ⚠️ **LUẬT THỨ TỰ:** trước khi trace luồng (3B) hay mổ feature (5), **PHẢI map cấu trúc tổng trước** (BƯỚC 0). Không có bản đồ thì đào code sẽ lạc → "mông lung".

| Khi điền ô...                                                    | → Mở dụng cụ                                                                             | Câu hỏi MANG THEO khi đào code                                                                                                             |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **BƯỚC 0 — Map cấu trúc trước** (3A + định vị code) | `Trace Any Codebase` (BƯỚC 1) **+** `CodeBase Understanding` **PHASE 1-3** | App làm gì? → Entry point đâu (`apps/api/src/main.ts`, `app.module.ts`)? → Có module nào (`ls apps/api/src/`)? → Nối nhau sao? |
| **3B Trace luồng**                                           | `Trace Any Codebase` (6 bước) **+** PHASE 4                                        | Gì kích hoạt? → API nào? → Validate đâu? → Business logic đâu? → Bảng nào? → Trả gì?                                          |
| **3C Data model**                                             | `CodeBase Understanding` PHASE 5 (Study DB Schema)                                         | Entity chính? → Quan hệ? → Bảng nào quan trọng nhất? → Source of truth?                                                               |
| **5 Feature → dòng "Flow"**                                 | `Trace Any Codebase` (6 bước) **+** PHASE 4                                        | (như 3B, nhưng cho riêng feature đó)                                                                                                      |

> 🔁 **Quy trình:** BƯỚC 0 (map cấu trúc) → mở 6-bước/Phase → đào code tới khi HIỂU → quay lại đây điền dòng "Flow" → rồi gắn WHY/trap (phần của file NÀY). HOW là nền, WHY xây trên nó.
> ✅ Mọi ô khác (Soul, Stack, Decision Map, Limitations, Ownership, Talk Track) → điền từ đầu anh + commit + issues, **KHÔNG cần** mở dụng cụ.

---

# 1️⃣ THE SOUL — Linh hồn sản phẩm

> ✍️ *Điền chung — bắt đầu từ đây.*

- **Sản phẩm này là gì (một câu):** Asset Platform là nền tảng giúp người dùng quản lý tài sản/đồ đạc trong nhà — lưu lại những món đã mua để khỏi quên mình sở hữu gì, theo dõi thông tin quan trọng (bảo hành, khấu hao giá trị), và khi muốn, bán lại chúng trên một chợ C2C tích hợp.
- **Nó giải quyết nỗi đau gì?** Người ta tích góp đồ đạc qua năm tháng nhưng KHÔNG có hệ thống nhớ giùm — dẫn tới: (1) quên mình sở hữu gì và để ở đâu, mất thời gian đi tìm; (2) mua trùng món đã có; (3) bỏ lỡ hạn bảo hành vì không ai nhắc. Asset Platform là **"bộ nhớ ngoài" cho tài sản của bạn.**
- **Người dùng là ai?** **Primary:** cá nhân người Việt có **nhiều tài sản/đồ đạc** cần quản lý (người càng nhiều đồ càng đau). **Secondary:** hộ gia đình — qua tính năng **chia sẻ inventory** cho thành viên. **Thị trường:** Việt Nam — bằng chứng nằm trong chính các quyết định kỹ thuật: VND-canonical, OCR hoá đơn tiếng Việt, thanh toán MoMo, chat kiểu "Chợ Tốt".
- **Luồng chính người dùng làm nhiều nhất:** "Thêm tài sản vào kho" — thiết kế quanh AI để giảm ma sát. **Cách chính (AI):** chụp/quét camera → AI nhận diện (tên, model, ghi chú) → "Tiếp tục" → trang chi tiết → điền nốt (ngày mua, giá, khấu hao, vị trí). **Cách dự phòng (thủ công):** bấm "Thêm tài sản" → upload ảnh → AI tự đánh giá "độ mới" + fill trước vài field → điền phần còn lại. Cả hai **hội tụ về cùng một trang chi tiết** — triết lý: *để AI gõ thay, người dùng chỉ xác nhận.* (DXS-10, DXS-12 "fallback khi AI không nhận ra", DXS-17)
- **Sự chuyển hoá nó tạo ra:** Từ **MÙ MỜ → NẮM QUYỀN** với tài sản của mình.
  - **Trước:** quên đã mua gì, mua bao nhiêu, để ở đâu, còn bảo hành không, đã khấu hao bao nhiêu, bán lại giờ được bao nhiêu — *không biết gì cả.*
  - **Sau:** có một **bản quản lý số hoá** — biết mình đang còn món gì, đã mua bao nhiêu, **giá trị thị trường hiện tại** còn bao nhiêu, và món đó **đang ở đâu.**
  - 🎯 Một câu chốt: *Asset Platform biến người sở hữu đồ một cách mù mờ thành người **nắm quyền kiểm soát** tài sản của mình — số hoá, có ý thức, sẵn sàng (cho bảo hiểm, cho việc bán lại).*

---

# 2️⃣ STACK & ARCHITECTURE

> ✍️ *Sẽ điền sau THE SOUL.*

### 2A. Tech Stack — WHAT

| Layer          | Công nghệ                                                                                                                                                                                                   | Vì sao chọn                                                                                                                                                                                                                                                                                                                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Web            | **Next.js** (trên React) — React 18.2 / Next 14.2                                                                                                                                                     | SSR + routing + build tối ưu +`next/image` cho app **nhiều ảnh**; SSR giúp **trang listing công khai lên Google** (SEO)                                                                                                                                                                                                               |
| Mobile         | **React Native + Expo** (Expo Go)                                                                                                                                                                       | 1 codebase JS/React → chạy**cả iOS + Android**; Expo lo sẵn build/OTA/native API (đặc biệt **camera** — trái tim của luồng AI capture)                                                                                                                                                                                              |
| Backend        | **NestJS v11** (Node.js + TypeScript, trên Express)                                                                                                                                                    | Cấu trúc**module/controller/service + DI + guards/pipes** sẵn → hợp app **nhiều domain** (Items, Marketplace, Chat, AI...); ngăn nắp, dễ test                                                                                                                                                                                         |
| Database       | **PostgreSQL 16** + **PostGIS** + **pgvector**                                                                                                                                              | Quan hệ mạnh +**ACID** (bắt buộc cho escrow/tiền); **1 DB lo cả 3**: relational + geo (PostGIS, tìm-quanh-đây) + AI embeddings (pgvector) → khỏi thêm DB riêng. *Lý do tái dựng — commit chỉ nói WHAT, không nói WHY.* Evidence: DXS-3, DXS-298/`34968af`, DXS-62                                                     |
| Auth           | **JWT** (access + refresh, HS256, TTL 15m) + bcrypt. **Web:** httpOnly cookie + CSRF double-submit. **Mobile:** Bearer token (SecureStore). +Google OAuth, phone OTP (Twilio)               | httpOnly chống XSS trộm token (web); Bearer hợp mobile (không browser);**CSRF guard tự bỏ qua khi có header `Bearer`** (attacker không set được header). Evidence: DXS-8/59/60, `6ad97b0`, `19b406a`; ⭐ **anh tự fix** cookie footgun `858cdee`/`30114b9`                                                               |
| AI / 3rd-party | **OpenAI** (vision nhận diện + OCR hoá đơn + định giá), **MoMo** (escrow, HMAC-SHA256 IPN), **Expo Push + FCM** (thông báo), **AWS S3 + CloudFront** (ảnh, fallback local) | OpenAI có**`OPENAI_LOCAL_MODE` mock** → dev/test không tốn tiền, không lệ thuộc; **rate-limit `/ai/*`** chống đốt budget; **MoMo** = ví VN hợp thị trường (buộc về THE SOUL). Evidence: DXS-17/18/62, `5ee39ae`, DXS-157, `e8b0b25`                                                                            |
| Infra          | **Docker Compose** (local/stg/prod) trên **server vật lý công ty**, sau **Nginx Proxy Manager**, deploy qua SSH                                                                         | ⭐**Pivot** bỏ AWS EB / Vercel / Supabase → self-host. Lý do: directive **3-môi-trường "local-first"** (DXS-39) — cùng code chạy mọi env qua Docker + env vars; đỡ lệ thuộc/chi phí cloud. Đánh đổi: tự lo ops nhiều hơn, đổi lại kiểm soát + parity. Evidence: `41f0ee4`, `1dcb7e6` (revert Vercel), DXS-28/29 |

> 🛡️ **Câu thoát hiểm (Frontend — khi bị dồn về Next.js / React Native):** *"Phần scaffold frontend có sự hỗ trợ của tooling/agent; em nắm LÝ DO chọn (SSR + image-opt + routing cho web; 1 codebase đa nền cho mobile) và biết nó hợp với app nhiều ảnh + có listing công khai — nhưng em chưa dùng hết các tính năng nâng cao."* → trung thực, vẫn vững.

### 2B. Architecture Style — HOW

- **System shape:** **Monorepo** (Turborepo + npm workspaces) chứa `apps/web` + `apps/mobile` + `apps/api` + packages chung (`@dx-aiot/contracts` Zod = single source of truth validation/DTO, `@dx-aiot/shared`). Backend = **modular monolith** (1 API, chia module: Items, Marketplace, Transactions, Chat, AI, Notifications...) — **KHÔNG microservices**.
  - ⚠️ **Monorepo ≠ Monolith — 2 TRỤC KHÁC NHAU:**
    - **Monorepo** = chuyện *tổ chức source code lúc VIẾT* (mấy repo?). Đối thủ: polyrepo. Phạm vi: cả web+mobile+api.
    - **Modular Monolith** = chuyện *backend CHẠY lúc DEPLOY* (mấy tiến trình?). Đối thủ: microservices. Phạm vi: chỉ `apps/api`.
    - → Biết 1 cái KHÔNG suy ra cái kia. Asset Platform = monorepo **+** modular monolith.
  - 🏛️ **Modular Monolith vs Microservices** (cùng trục runtime):
    - **Modular Monolith** (← của mình): tất cả module (Items, Chat, Payments, AI...) chạy chung **1 tiến trình NestJS, deploy 1 lần**, nhưng bên trong **chia ngăn rõ theo domain**. Metaphor: 1 căn nhà liền khối nhưng chia phòng sạch sẽ.
    - **Microservices**: mỗi domain là **1 service riêng, deploy riêng, gọi nhau qua mạng** (HTTP/queue). Metaphor: 5 căn nhà riêng nối bằng dây điện thoại. Mạnh ở scale từng phần độc lập — nhưng trả giá bằng **độ phức tạp vận hành** (network, distributed transaction, observability...).
  - 💎 **Vì sao monorepo:** chia sẻ contracts FE↔BE → diệt lớp bug "validate lệch nhau" (DXS-218). **Vì sao modular monolith (không microservices):** team nhỏ, 1 deploy đơn giản, escrow cần transaction trong 1 DB (microservices làm distributed transaction phức tạp), chưa có nhu cầu scale riêng từng phần → microservices lúc này là **over-engineering**.
- **Communication:** **REST** (NestJS controllers, prefix `/api`, `/marketplace/*`, `/chat/*`, `/ai/*`).
- **State / source of truth:** **PostgreSQL** (+ Redis cache). `payment_events` = ledger append-only cho escrow.
- **Processing:** **sync REST** + **async cron** (`@nestjs/schedule`) cho escrow auto-release / nightly valuation; **push** cho thông báo; **chat polling 7s** (chưa websocket — nợ kỹ thuật, xem mục 6).
- **Auth model:** **stateless JWT** (cookie httpOnly cho web, Bearer cho mobile) — xem 2A.

---

# 3️⃣ SYSTEM MAP & DATA FLOW

> ✍️ *Sơ đồ + entity em seed sẵn từ code (factual). Luồng trace để trống — mình vẽ chung.*

### 3A. Sơ đồ kiến trúc (từ code thật) — ⭐ BƯỚC 0, đọc TRƯỚC khi trace 3B

> 🧭 Sơ đồ này được dựng bằng `Trace Any Codebase` BƯỚC 1 (`ls apps/api/src/` + `cat main.ts`/`app.module.ts`) + PHASE 1-3. Đây là bản đồ — có nó rồi mới trace luồng 3B khỏi lạc.

```
   [Mobile (Expo/RN)]        [Web (Next.js)]
            \                     /
             ──→  [API: NestJS  /api]  ←──
                          │  (modular: Items, Marketplace,
                          │   Transactions, Chat, AI, Storage...)
        ┌─────────────┬───┴────────────┬───────────────┐
   [PostgreSQL]    [Redis]      [Cron/Scheduler]    [3rd-party]
   + PostGIS       cache        escrow auto-release   OpenAI (vision/OCR/valuation)
   + pgvector                   nightly valuation     MoMo (escrow IPN)
                                                      S3/CloudFront (+ local fallback)
                                                      Expo Push + FCM
```

### 3B. Trace luồng quan trọng (điền chung)

> 🔗 **Cần đào code? → `CodeBase Understanding` PHASE 4 (Trace Real Flows).** Hỏi khi trace: gì kích hoạt → API nào → validate đâu → business logic đâu → bảng nào → trả gì?

- **Luồng AI Capture** *(trace cùng Ruach-El bằng `Trace Any Codebase` — tới đây là phần đã đi):*
  - **NỬA 1 — Nhận diện (đã trace xong, stateless, KHÔNG lưu DB):**
    1. 📱 `apps/mobile/app/(app)/review.tsx` (màn hình) → gọi hàm `aiApi.recognizeAsset(imageUri)`.
    2. 📡 `apps/mobile/services/aiApi.ts` (lớp service, **giữ URL**) → `api.post('/ai/recognize', ...)`.
    3. 🚪 `apps/api/src/ai/ai.controller.ts:37` `@Post('recognize')` — có `JwtAuthGuard` (phải login) + `@Throttle 20/phút` (💎 chặn đốt budget OpenAI) + validate `RecognizeAssetDto`.
    4. 🧠 `vision-recognition.service.ts:32` `recognizeFromBase64()`: 💎 `OPENAI_LOCAL_MODE` → trả mock (khỏi tốn tiền/CI chạy được); 💎 `detectImageMime()` tin bytes thật hơn client (fix bug client gắn sai MIME → OpenAI reject); gọi **GPT-4o-mini** (prompt tiếng Việt) + ép **`json_schema strict`**.
    5. 📦 `return` mỗi field kèm **`confidence` 0..1** + `fallbackSuggested` + `latencyMs` → user XEM & SỬA (💎 human-in-the-loop; confidence thấp → UI cảnh báo check lại). **KHÔNG đụng database.**
  - **🧵 Mắt nối 2 nửa (frontend khâu):** nút "Tiếp tục" ở `review.tsx` → `router.replace('/(app)/add-item', {data AI đoán})`. → 2 nửa backend (`/ai/recognize` và `/api/items`) **không biết nhau**; frontend nối bằng **điều hướng**, không bằng lời gọi hàm.
  - **NỬA 2 — Lưu vào kho (🚧 ĐANG trace — Wiganz tự đào, branch `dev`, 2026-06-23, thế ① XUÔI):**
    - **✅ ĐÃ tự trace (FRONTEND — tới `POST /items`):**
      1. 🖼️ `apps/mobile/app/(app)/add-item.tsx:755` — nút `saveButton` `onPress={handleSubmit}` (hàm khai báo `:416`). *(Bẫy 3 lớp: màn hình KHÔNG giữ URL — chỉ gọi hàm.)*
      2. 🔀 Trong `handleSubmit`: **nhánh `if (itemId)`** → `itemsApi.update(itemId,…)` (`:454`); **else** → `itemsApi.create(…)` (`:456`). 💎 *Một màn `add-item` GÁNH 2 VAI: `itemId` (route param) CÓ = sửa, RỖNG = tạo mới.*
      3. 📤 Thứ tự bắt buộc: `itemsApi.uploadLocalPhotos(photos)` (`:429`) chạy **TRƯỚC** + `await` → trả về **URL** → `itemData` ôm URL → rồi mới `create`. 💎 *DB lưu **link ảnh (URL)**, KHÔNG lưu blob ảnh (ảnh nằm ở S3/CloudFront) → phụ thuộc dữ liệu: phải có URL trước khi save.*
      4. 📡 `apps/mobile/services/itemsApi.ts:54` (lớp service giữ URL) → `api.post('/items', data)`.
    - **✅ ĐÃ tự trace tiếp (BACKEND — `POST /api/items` → DB), Wiganz tự đào 2026-06-23:**
      5. 🚪 `apps/api/src/items/items.controller.ts` — `@Post()` (`:126`, route = `setGlobalPrefix('api')` + `@Controller('items')` + `@Post()` rỗng = `POST /api/items`). Hàm `createItem()` (`:136`, cách decorator 10 dòng vì `@HttpCode`/`@ApiOperation`/`@ApiResponse` chen giữa). Nhận `@CurrentUser() user` + `@Body() dto: CreateItemDto`. 💎 **`user.id` lấy từ `@CurrentUser` (JWT token), KHÔNG từ `@Body`** → client không tự xưng được là ai (chặn giả mạo chủ sở hữu). Controller MỎNG → `return this.itemsService.create(dto, user.id)`.
      6. 🧠 `apps/api/src/items/items.service.ts:38` `create(dto, userId)` — BỘ NÃO. *(grep tìm: `grep -rn "async create" --include="*.service.ts" apps/api/` → lọc theo domain `items/`.)*
      7. 🗄️ **2 chữ "create" KHÁC NHAU:** `itemsRepository.create({...dto, photos: dto.photos ?? [], userId})` = chỉ **dựng object trong RAM** (chưa đụng DB). `await itemsRepository.save(item)` = **mới THẬT SỰ ghi xuống** bảng **`items`**. 💎 *`repository.create` ≠ ghi DB; `repository.save` mới ghi.* `userId` gắn vào lúc dựng object → dấu ấn chủ sở hữu.
      8. 🔭 **SOI ĐUÔI — 2 việc ngầm (KHÔNG `return`/`await` → chạy sau lưng, user không chờ):** `triggerConditionAssessment(...)` (đánh giá độ mới) + `void priceHistoryService.recordSnapshot(...)` (chụp snapshot giá). 💎 *Chữ `void` = tuyên bố CHỦ Ý không-await.* → cửa sang **thế ③** (trace tiếp `conditionAssessment` = luồng riêng).
      9. 📦 `return saved` → trả **object vừa lưu** về client → app báo "đã thêm vào kho ✅".
    - **🪜 ĐƯỜNG ĐI NGOÀI→TRONG (2 nửa AI Capture KHÉP KÍN ✅):** `add-item.tsx (BƯỚC 1)` → `itemsApi service FE — chặng ẩn` → `items.controller @Post (BƯỚC 3)` → `service.create (BƯỚC 4)` → `repo.save → bảng items (BƯỚC 5)` → `2 job ngầm + return saved (BƯỚC 6)`.
- **Luồng Escrow auto-release** *(trace cùng Ruach-El, branch `dev`, 2026-06-23 — **thế ③ KHÔNG-REQUEST**: không ai bấm, **THỜI GIAN** đánh thức):*
  - **Bối cảnh nghiệp vụ:** người mua trả tiền → tiền nằm trong "két" platform (`ESCROW_HELD`), **CHƯA** tới người bán. Quá hạn 72h mà người mua không bấm "đã nhận" → hệ thống **tự thả** tiền cho người bán. Không cú bấm nào → **cron** đánh thức.
  - **CỬA VÀO (khác AI Capture — KHÔNG phải `@Post`):** `apps/api/src/transactions/escrow-release.service.ts` — **2 con `@Cron`** *(cửa vào của thế ③ = method gắn `@Cron`, không có URL; grep `"@Cron"` thay vì grep URL):*
    1. ⏰ `@Cron('0/15 * * * *')` `releaseExpiredEscrows()` — mỗi 15': việc **CHÍNH** (thả đứa tới hạn).
    2. ⏰ `@Cron('* * * * *')` `processReleaseRetries()` — mỗi phút: **LƯỚI AN TOÀN** (thử lại đứa từng fail). 💎 *Tách 2 cron → happy-path & retry không giẫm chân nhau.*
  - **Cửa vào MỎNG** → đẩy thẳng xuống `transactionsService` *(giống controller mỏng ở AI Capture — bộ não thật luôn ở service).*
  - **🧠 BỘ NÃO #1 — `releaseExpiredEscrows()` (điều phối, ai được thả):**
    - 🔑 bọc trong `withSchedulerLock(...)` = **advisory lock** (`pg_try_advisory_lock`). 💎 *Chỉ 1 cron/instance chạy vòng quét — chống 2 server đua. `try_` = giành không được thì **BỎ QUA**, không đứng chờ. Dùng query-runner **đường-dây-riêng** vì advisory lock dính chặt 1 connection (khoá & mở phải cùng 1 dây).*
    - 🔍 hỏi DB: `status=ESCROW_HELD` + `releaseAfter ≤ now` (đã quá 72h) + `nextReleaseAttemptAt IS NULL` (chưa xếp lịch retry).
    - 🛡️ **loại trừ tranh chấp:** giao dịch có `DisputeStatus.OPEN` → **GIỮ tiền**, không thả. 💎 *Tới hạn ≠ được thả nếu đang cãi nhau.*
    - 🔁 loop → mỗi giao dịch gọi `attemptGatewayRelease(txId, actor=SYSTEM)`. 💎 *actor `SYSTEM` (`id=null`) = **bằng chứng sống của thế ③**: không user nào ra lệnh.*
  - **🧠 BỘ NÃO #2 — `attemptGatewayRelease()` (ra tay thả tiền) — 5 viên ngọc:**
    - 🔒 **Ngọc 1 — khoá tầng 2:** cả hàm trong `dataSource.transaction(...)` + `findOne({ lock: pessimistic_write })` = **ROW LOCK** (`SELECT…FOR UPDATE`). 💎 *advisory lock khoá **cả ca cron**; row lock khoá **đúng 1 hàng** — chặn cron & "người mua bấm tay" cùng đụng 1 giao dịch.*
    - ♻️ **Ngọc 2 — idempotency (phía DB):** giành khoá xong **check lại** `if (status !== ESCROW_HELD) return` → đã thả rồi thì thôi. 💎 *Khoá bắt đứa thứ 2 đợi; check này chặn nó thả lần 2 sau khi đợi xong.*
    - 🧾 **Ngọc 3 — idempotency (phía gateway):** gửi `requestId = REL-{txId}-{releaseAttempts}` xác định cho MoMo → mạng chập chờn gọi lại cùng `requestId` → MoMo chỉ trả **1 lần**. 💎 *Phòng thủ 2 đầu: DB mình + gateway MoMo.*
    - ✅ **Ngọc 4 — happy path (đều `await`, trong 1 transaction):** `transition(RELEASED_TO_SELLER)` → `save` → `recordEvent` (ghi `payment_events` — **sổ cái append-only**) → `listing = SOLD`. 💎 *Việc TIỀN → `await` **từng bước**; nổ giữa chừng → **rollback hết**. Hoặc xong hết, hoặc không gì cả. (≠ AI Capture: việc thường thì fire-and-forget `void`.)*
    - 🔁 **Ngọc 5 — catch retry (tự lành):** fail → `releaseAttempts++`; còn cửa → set `nextReleaseAttemptAt = now + delayMs` (**backoff tăng dần** `RELEASE_RETRY_DELAYS_MS`); hết cửa → `RELEASE_FAILED` + log `OPS_ALERT` (người vào tay). 💎 *`catch` chính là nơi set `nextReleaseAttemptAt` → **đóng vòng** với cron-mỗi-phút: **2 cron + 1 field = máy retry hoàn chỉnh.** Câu chuyện phỏng vấn đắt nhất.*
  - **🪜 ĐƯỜNG ĐI (thế ③, khép kín):** `⏰ @Cron 15'` → `releaseExpiredEscrows` → `🔑 advisory lock` → `DB: ESCROW_HELD + >72h + ko dispute` → loop → `attemptGatewayRelease` → `🔒 row lock + transaction` → `MoMo release(requestId)` → `RELEASED_TO_SELLER + ghi payment_events + listing SOLD` → `fail? backoff (nextReleaseAttemptAt) ↔ @Cron 1'` → `hết cửa: RELEASE_FAILED + OPS_ALERT`.
  - **🗄️ Bảng DB đụng:** `transactions` (FSM `status`, `releaseAfter`, `releaseAttempts`, `nextReleaseAttemptAt`), `disputes` (loại trừ), `payment_events` (sổ cái), `listings` (→ `SOLD`).
  - **🕵️ Tác quyền (ĐỔI NHẠC CỤ):** `git blame` hiện `QADevOps Bot` (CI commit) — **không phải tên người.** → tác quyền thật = **khả năng giải thích**, không phải dòng `Author:`. *(Authorship Reclaim)*

### 3C. Data Model — entity chính (từ code)

> 🔗 **Cần đào code? → `CodeBase Understanding` PHASE 5 (Study DB Schema).** Hỏi: entity chính? → quan hệ? → bảng quan trọng nhất? → source of truth?

- **Core:** `User`, `Item` (brand / model / serial / purchasePrice / warranty / location / depreciatedValue)
- **Marketplace:** `Listing`, `Transaction` (FSM), `ChatThread` + `ChatMessage`, `Review`
- **Khác:** `Notification`, `Sharing` (family), `payment_events` (ledger append-only)
- **Quan hệ (điền chung):** ___
- **Source of truth:** ___

> 📥 Nguồn: `apps/api/src/**/entities`, migrations, `docker-compose.yml`.

---

# 4️⃣ THE DECISION MAP ★ (TRÁI TIM)

> ✍️ *Điền từng quyết định một. Mỗi cái: hỏi "anh nghĩ vì sao?" trước, rồi bổ sung.*

Hàng đợi quyết định cần điền (từ Appendix):

- [ ] Database: PostgreSQL + PostGIS (và câu chuyện gỡ pgvector)
- [ ] Auth: httpOnly cookie (web) + Bearer (mobile) + CSRF double-submit
- [ ] JWT hardening (HS256, TTL 15m)
- [ ] Currency: USD-canonical lưu trữ, VND hiển thị (+ bug 0₫)
- [ ] Escrow idempotency (row-lock + advisory lock)
- [ ] AI pipeline: OpenAI Vision + OCR + graceful degradation
- [ ] Image upload hardening (magic-bytes)
- [ ] Monorepo + shared contracts (Zod)
- [ ] Security: xlsx→exceljs, Expo SDK 50→56, Dependabot sweep
- [ ] Process: never-merge-to-main, 3-environment strategy

*(điền block chi tiết cho từng cái khi tới lượt)*

---

# 5️⃣ FEATURE DEEP-DIVES — Mổ xẻ từng feature

> ✍️ *Điền từng feature một, kiểu Socratic. Em hỏi "anh làm cái này sao?" trước, rồi bổ sung từ Appendix.*
> Trả lời câu "Kể anh làm feature X thế nào?" — phần máu thịt; trap/bottleneck = câu chuyện vàng.
> 🔗 **Mỗi feature:** dòng **"Flow"** → mở `CodeBase Understanding` PHASE 4 (trace code feature đó tới khi HIỂU). Dòng **"vì sao / trap"** → từ commit/issues + đầu anh.

### 📸 1. AI Capture (ảnh → nhận diện → review → vào kho)

- **Flow end-to-end:** ___
- **Kiến trúc + vì sao:** ___
- ⭐ **Trap đã giải:** ___
- **Bằng chứng:** DXS-10, DXS-17; magic-bytes `cd7993e`/`d62d9af`

### 🧾 2. OCR hoá đơn (ảnh receipt → trích ngày/giá/bảo hành)

- **Flow:** ___ | **Kiến trúc + vì sao:** ___ | ⭐ **Trap:** ___
- **Bằng chứng:** DXS-18; `cad8075`; OCR JSON-fence fix DXS-272/`5ee39ae`

### 💰 3. AI Valuation + Currency (định giá + toggle ₫/$)

- **Flow:** ___ | **Kiến trúc + vì sao:** ___ | ⭐ **Trap:** ___
- **Bằng chứng:** DXS-62; ⭐ story 246 tỷ `a1c2ebc`/`abf7fce` vs `da33309`

### 💬 4. Chat per-person (kiểu Chợ Tốt/Messenger)

- **Flow:** ___ | **Kiến trúc + vì sao:** ___ | ⭐ **Trap:** ___
- **Bằng chứng:** `edd71dd`; DXS-89

### 🔔 5. Notifications + Push (emitter pattern, Expo+FCM)

- **Flow:** ___ | **Kiến trúc + vì sao:** ___ | ⭐ **Trap:** ___
- **Bằng chứng:** `1fecb53`/`c17ec9d`; DXS-63

### 🛒 6. Marketplace / Sale + Escrow (MoMo, FSM, idempotency)

- **Flow:** ___ | **Kiến trúc + vì sao:** ___ | ⭐ **Trap:** ___
- **Bằng chứng:** DXS-143/157; FSM `a3fe8ec`; ⭐ idempotency `e8b0b25`

### 🤝 7. Family Sharing (chia sẻ inventory hộ gia đình)

- **Flow:** ___ | **Kiến trúc + vì sao:** ___ | ⭐ **Trap:** ___
- **Bằng chứng:** DXS-66; permission enforce DXS-279/280

### 🔐 8. Auth (cookie web + Bearer mobile + CSRF)

- **Flow:** ___ | **Kiến trúc + vì sao:** ___ | ⭐ **Trap:** ___
- **Bằng chứng:** DXS-8/59/60; `6ad97b0`, `19b406a`, ⭐ cookie footgun `858cdee`/`30114b9`

---

# 6️⃣ KNOWN LIMITATIONS & WHAT I'D DO DIFFERENTLY

> ✍️ *Em seed nợ kỹ thuật thật từ commit/issue. Mình bàn cách KỂ cho khéo.*

- FX rate **hardcode `25000`** (`DEFAULT_USD_TO_VND_RATE`) — chưa có forex live (BE gap, ghi ở `abf7fce`/`c29d678`)
- Chat dùng **polling 7s**, chưa websocket (`dff4c27`) — sẽ vỡ khi nhiều người dùng
- Chưa deploy **staging thật** (Sprint 6 DXS-175 cancelled) — giữ local-first
- Test chủ yếu **mock** (`OPENAI_LOCAL_MODE`/`MOMO_LOCAL_MODE`), chưa E2E thiết bị thật
- **39 commit suiren** (việc mới & quan trọng nhất) **chưa merge vào dev**
- **Cái sẽ làm khác:** ___ *(điền chung)*
- **Bottleneck vỡ trước:** ___ *(điền chung — gợi ý: OpenAI cost/rate-limit, chat polling, escrow concurrency)*

---

# 7️⃣ OWNERSHIP & MY CONTRIBUTION — Phần này là CỦA WIGANZ

> ⭐ Câu chí tử: "Phần nào ANH thật sự làm?" — phần QUAN TRỌNG NHẤT của tài liệu này.
> ✍️ *Em seed sự thật từ git authorship. Mình craft cách NÓI chung.*

- **AI/bot (QADevOps, Paperclip) xây:** toàn bộ nền móng branch `dev` (246 commit) — scaffolding module, CRUD, pipeline.
- **WIGANZ tự làm** (branch `refactor/suiren-ui-redesign`, 39 commit, git author = `AiOT-TriTDD`):
  - ⭐ Bắt + sửa bug định giá "246 tỷ ₫" → **đảo ngược quyết định USD→VND canonical** (`a1c2ebc`) — judgment kiến trúc thật
  - Audit gỡ data BỊA của UI bot → biến demo-ware thành sản phẩm thật (`9bb1879`)
  - Dựng **Notification system** (emitter pattern) + **chat per-person** + OS push (Expo+FCM)
  - Sửa **footgun load-env** (cookie chết 15m trong khi token sống 7d) (`30114b9`)
  - Toàn bộ **Suiren UI redesign** (web + mobile)
- **Cách tôi sẽ nói (craft chung):** ___
- **Bằng chứng quyền tác giả:** `git log refactor/suiren-ui-redesign --author=AiOT-TriTDD`

> 💡 Khung an toàn (bàn chung sau): *"Nền móng có sự hỗ trợ của tooling/agent; phần tôi sở hữu là engineering judgment — tôi là người phát hiện AI suy SAI invariant tiền tệ, đảo ngược nó, và biến scaffolding thành sản phẩm thật."*

---

# 8️⃣ THE TALK TRACK — Luyện nói

> ✍️ *Điền cuối cùng, sau khi xong 1-7.*

1. "Kể về dự án trong 60 giây." → ___
2. "Vì sao chọn stack này?" → ___
3. "Phần khó nhất? Xử lý sao?" → ___
4. "Nếu làm lại đổi gì?" → ___
5. "Scale 100x thế nào?" → ___
6. "Chỗ nào dễ hỏng nhất?" → ___
7. "Anh đóng góp phần nào?" → ___

---

---

# 📚 APPENDIX — Nguyên liệu thô (đã đào từ commit + issues)

> Đây là bằng chứng. Mọi thứ ở trên rút ra từ đây. Giữ nguyên để verify được.
> Nguồn: branch `origin/dev` (246 commit, 2026-05-28 → 06-12) + **Paperclip: 300 issues** trong project Asset_Platform. Repo `DX-AIoT/Asset_Platform`. Codename "monomana", deploy `monomana.aiotso.net`. Khách hàng: anh Hùng, CEO AIoT.
>
> 🔄 **ĐỐI CHIẾU LIVE — snapshot 2026-06-23, kéo trực tiếp từ `paperclip.aiotso.net`** (company `ec272d4a…`, project `c008a6be…`):
>
> - **300 issue** trong project (company có **309** tổng) — *con số "309" trong bản cũ thực ra là tổng-issue-của-company, KHÔNG phải số DXS; "168 issues" là snapshot phiên trước, dự án đã đi tiếp.*
> - **Trạng thái:** 🟢 **275 done · ⛔ 19 cancelled · 📋 5 backlog · 🚨 1 BLOCKED**.
> - **Đánh số:** issue có `DXS-` chạy dải **DXS-14..294**, nhưng phần lớn title là **mô tả tự do** (≈6 issue khởi đầu bằng `DXS-`, ≈6 bằng `AIO-`). → `DXS-NN` là **số THAM CHIẾU để truy vết**, không phải prefix nghiêm ngặt. Các trích dẫn `DXS-x` ở trên vẫn tra cứu được.

## A. THE SOUL (từ issues)

Một **app theo dõi tài sản/đồ đạc cá nhân** ĐÃ TIẾN HOÁ thành **chợ C2C (mua bán lại) có escrow**.

- **Vòng lặp cốt lõi:** chụp ảnh → AI nhận diện món đồ → xác nhận → vào kho cá nhân (DXS-10, DXS-17). DB model `Item`: brand, model, serial, ngày/giá mua, tình trạng, bảo hành, vị trí, `depreciatedValue` (DXS-3).
- **Đau gốc:** nhập kho thủ công quá cực → AI làm thay (Vision DXS-17, OCR hoá đơn DXS-18, auto-category DXS-19, barcode DXS-20). Tinh chỉnh cho **thị trường VN** (đồ gia dụng VN, hoá đơn tiếng Việt, VND).
- **Người dùng:** cá nhân/hộ gia đình VN muốn quản lý đồ đạc, sẵn sàng cho bảo hiểm, và sau cùng là bán lại kiếm thanh khoản. Hai phía khi có marketplace: người bán (chủ kho) + người mua địa phương.

## B. PRODUCT EVOLUTION (sprint arc)

| Phase/Sprint | Theme                                                                                                                              | Evidence               |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| Sprint 1     | Inventory MVP: auth, mobile AI-capture, web dashboard, Vision+OCR. Gate demo CEO 7 tiêu chí                                      | DXS-3..22, demo DXS-22 |
| Sprint 2     | Security hardening (carry-over) + tài chính: market valuation, depreciation, insurance PDF, maintenance reminder, family sharing | DXS-57..66             |
| Sprint 3     | Local-first delivery, documentation, full-stack local E2E, + nền tảng Phase 3                                                    | DXS-83                 |
| Sprint 4     | **C2C Marketplace MVP** — listing CRUD, browse/search, AI suggested price (chưa payment)                                   | DXS-143..148           |
| Sprint 5     | Payments & escrow qua MoMo (hold/release, 72h auto-release, dispute, IPN)                                                          | DXS-157..170           |
| Sprint 6     | Staging deploy, S3/CloudFront, admin panel, rate limit, CI gate —**CANCELLED** (code ship, deploy bỏ)                      | DXS-175                |
| 2026-06-09   | QA bug batch cross-cutting                                                                                                         | DXS-276+               |
| Latest       | 79 Dependabot CVEs, phone OTP, PostGIS geo, security baseline, CI orchestrate                                                      | DXS-289, 296-304       |

**Một dòng:** Inventory tracker → lớp tài chính/bảo hiểm → marketplace MVP → payments/escrow → hardening & ops.

## C. TECH STACK (từ commit, có evidence)

- **Backend:** NestJS v11 (nâng từ v10, `9767d39`), TypeScript, TypeORM 0.3.x — `apps/api/package.json`
- **Web:** Next.js 14.2 (standalone), React 18.2, TanStack Table, Tailwind — `apps/web/package.json`
- **Mobile:** Expo SDK 56 / RN 0.85 / React 19, expo-router, SecureStore — `apps/mobile/package.json`
- **DB:** PostgreSQL + **PostGIS** (geography Point 4326, GiST index cho ST_DWithin) — `34968af`; image `postgis/postgis:16-3.4`
- **Cache/queue:** Redis (ioredis)
- **Auth:** JWT (httpOnly cookie web + Bearer mobile), passport-jwt, google-oauth20, phone OTP qua **Twilio** `3cced4e`, bcrypt
- **AI/3rd-party:** **OpenAI** v4 (vision, OCR gpt-4.1-mini, valuation, autofill) + `OPENAI_LOCAL_MODE` mock `5ee39ae`; **MoMo** (HMAC-SHA256 IPN); **Firebase Admin** + expo-server-sdk push
- **Storage:** AWS S3 + CloudFront, fallback local disk (`S3_LOCAL_MODE`) `2a9fbef`; `sharp` re-encode, `file-type` magic-byte
- **Infra:** Docker Compose (local/stg/prod), **Nginx Proxy Manager**, server vật lý tự host — `f17c065`

## D. ARCHITECTURE STYLE

- **Monorepo** npm workspaces + Turborepo. Apps: api/web/mobile; packages: `@dx-aiot/contracts` (Zod, single source of truth), `@dx-aiot/shared` (currency utils).
- **REST** (NestJS controllers, prefix `/api`, `/marketplace/*`, `/chat/*`, `/ai/*`).
- **Modular NestJS** (Items, Marketplace, Transactions, Chat, Reviews, Sharing, Admin, AI, Storage), `autoLoadEntities:true`.
- **Processing:** sync REST + **async cron** (`@nestjs/schedule`) cho escrow auto-release, retry, nightly valuation; **push** cho reminder; chat dùng **polling 7s** (không websocket) `dff4c27`.
- **Transaction = FSM rõ ràng:** `PENDING_PAYMENT → ESCROW_HELD → RELEASED_TO_SELLER | BUYER_REFUNDED | RELEASE_FAILED | DISPUTED` — `a3fe8ec`.

## E. KEY ENGINEERING DECISIONS (commit evidence)

- **PostGIS thay pgvector** → marketplace cần geo radius search, không cần vector; pgvector bỏ không dùng. Đổi docker image, backfill `geom`, GiST index — `34968af`
- **Pricing: purchasePrice lưu USD-canonical, valuation USD, hiển thị VND** qua `USD_TO_VND_RATE` (default 25000). Gộp formatter, xoá 9 bản trùng — `da33309`
- **Auth: httpOnly cookie (web) + CSRF double-submit; Bearer (mobile)** → JWT off localStorage `18b011c`/`76d6b2c`; mobile SecureStore `268aeec`; CSRF guard skip khi có header `Authorization: Bearer` — `6ad97b0`
- **JWT hardening** → ghim HS256 (chặn alg-confusion/`alg:none`), bắt buộc iss/aud, claim `type:access|refresh`, validate secret lúc boot (≥32 ký tự), TTL 7d→15m, bcrypt cost→12 — `19b406a` (AIO-47)
- **Image upload hardening** → MIME thật từ magic-bytes (`file-type`), không tin Content-Type; sharp re-encode strip EXIF/GPS; serve `Content-Disposition: attachment` + `nosniff` + CSP — `6b1a9fc` (AIO-48)
- **Escrow idempotency** → `SELECT...FOR UPDATE` row-lock + status claim check (3 caller đua: auto-release cron, retry cron, buyer confirm); deterministic requestId làm idempotency key; scheduler gated bằng `pg_try_advisory_lock`; ledger append-only `payment_events`; HMAC compare `crypto.timingSafeEqual` — `e8b0b25` (AIO-46, CRITICAL)
- **Shared contracts (Zod)** → diệt defect class #1 (FE/BE validate độc lập); CI gate `contract-tests` — `3b2aef8` (DXS-218)
- **Platform commission** → `PLATFORM_COMMISSION_RATE` default 2%, cột `commissionVND`/`sellerPayoutVND` — `74e5aa4`
- **AI graceful degradation** → `OPENAI_LOCAL_MODE`/thiếu key → mock; OCR ghim `json_schema` strict — `5ee39ae`, `cad8075`

## F. SECURITY DECISIONS

- **xlsx → exceljs** → diệt GHSA-4r6h (Prototype Pollution) + GHSA-5pgg (ReDoS) — `1a83a30` (DXS-293)
- **Expo SDK 50→56** → diệt 11 HIGH CVE — `146f988` (DXS-292)
- **Dependabot sweep** → 66→50 vulns, 3 critical về 0; NestJS 10→11, Next 14.1→14.2, bcrypt 5→6 — `9767d39` (DXS-289)
- **Secret purge** → gỡ QA session cookie committed; chọn KHÔNG rewrite history (blast radius dev-only, free plan) — `9014258` (DXS-305)
- **Security CI baseline** → CodeQL + dependency-review + npm audit + gitleaks `6657238`; adapt free plan sau khi board từ chối GitHub trả phí — `b7cf31d` (DXS-304)
- **RBAC** → RolesGuard fail-closed, super_admin hierarchy, mass-assignment defense; `@Unique` + 23505→ConflictException chặn TOCTOU — `c86df6a`, `21f7ba3`
- **Rate limiting** → throttler: auth 10/min, AI 20/min, payments 30/min — `a8b4b30` (DXS-176)
- **`/ai/*` từng KHÔNG auth** → thêm JwtAuthGuard class-level; owner-scoping cross-user → 404 — `8bca3a0` (DXS-278)

## G. PROCESS / CI-CD

- **Never-merge-to-main / board-only promotion** → mọi branch chỉ merge vào `dev` (PR + green CI); chỉ board promote `dev→main`. Khởi từ PR #48 bypass dev làm main tụt 22 patch (gồm 2 security fix) — `d54ebe9`/`5886233` (DXS-303)
- **3-Environment Strategy (LOCAL→STAGING→PROD)** directive (DXS-39): "tất cả code phải chạy local trước"; không block chờ cloud creds; không hardcode cloud URL.
- **CI gates** → `ci.yml` (typecheck/test/build/lint), `local-first-gate.yml` (compose boot + `/api/health`), `contract-tests`, prettier `format:check`. Test chạy với `OPENAI_LOCAL_MODE`/`MOMO_LOCAL_MODE`.
- **Deploy** → pivot bỏ AWS EB + Vercel sang Docker-Compose-over-SSH sau Nginx Proxy Manager — `41f0ee4`, `1dcb7e6` (revert Vercel), `2eb958b`

## H. NHỮNG BUG LỘ RA THIẾT KẾ (vàng cho phỏng vấn)

- **AI gợi ý 0₫** `98af30d` → lộ rule purchasePrice USD-canonical: `toValuationRequest()` chạy nhầm `vndToUsd()` trên giá vốn đã USD → chia 25000 → làm tròn 0. Món có comparable (iPhone) thoát bug nên unit test không bắt được.
- **Mobile bị 403 "CSRF token missing" hết** `6ad97b0` → lộ web & mobile DÙNG CHUNG login endpoint; fix: key CSRF-skip vào header Bearer.
- **Marketplace route 404 im lặng** `c109a8f` (DXS-171) → lộ trùng tên entity: 2 class `Transaction` dưới `autoLoadEntities` gây nhập nhằng metadata → MarketplaceModule không init.
- **API crash `Cannot access ChatThread before initialization`** `aff2a7e` → lộ circular entity import (ChatThread↔ChatMessage); fix bằng `Relation<>` / `import type`.
- **GET /items/export 500, DELETE 404 trên build mới** `bdfcc1e` → `dist/` cũ của tsc lọt vào Docker image đè SWC output; fix thêm `**/dist` vào `.dockerignore`.

## I. CANCELLED / BACKLOG (và lý do — chủ đề chung)

- **DXS-175 Sprint 6 staging deploy** CANCELLED — code ship (DXS-176..181) nhưng deploy thật (DXS-182/183) bỏ; giữ local-first.
- **DXS-51/52/47** Docker-out-of-Docker cho QA agent — bỏ, thay bằng mock integration test (DXS-139/140).
- **DXS-283/288** iOS camera crash + simulator verify — bỏ (không có iOS simulator cho agent).
- **Backlog (5):** device push E2E (DXS-99/104/107), S3/CDN infra (DXS-100) — block vì thiếu real device/cloud; bản code làm bằng mock/local-mode.

> 🔑 **Chủ đề chung của mọi thứ bị cancel:** đều block vì *hạ tầng thật mà sandbox của agent không có* (Docker socket, iOS sim, cloud/staging, MoMo sandbox thật, real device). Quyết định nhất quán: **thay bằng mock/local-mode, giữ local-first** — hệ quả trực tiếp của directive DXS-39.

> ✅ **LIVE (2026-06-23) XÁC NHẬN luận điểm trên.** 19 issue `cancelled` thật, phân loại: **Docker/DooD runtime (7)** · **staging/cloud deploy (6:** Sprint 6, AWS IAM/S3/EB/CloudFront, Vercel, Supabase staging**)** · **MoMo STG sandbox (1)** · **iOS simulator/camera MOB-04 (3)** · **real OpenAI key (1)**. → 100% bị bỏ vì *thiếu hạ tầng thật trong sandbox agent* — đúng y luận điểm. 5 backlog cùng họ (push E2E `DXS-104`/`DXS-109`, S3/CloudFront CDN).
>
> 🚨 **MỚI — chưa có ở snapshot cũ:** issue đang `BLOCKED` NGAY LÚC NÀY = **`[BLOCKER] GitHub Actions billing/spending-limit failure — all CI red, merges blocked`**. Cùng arc gần nhất: board merge-policy PR #50 land vào dev · gitleaks purge QA cookies · security CI free-plan-compatible · `[AIO-114]` TRIAGE reconcile-to-main (129 files). → **Trạng thái sống của dự án:** CI đỏ vì hết hạn mức GitHub Actions → mọi merge bị chặn. *(Đây là chương tiếp theo của arc "never-merge-to-main / board-only promotion" ở mục G + bug GHA billing — đáng thành một dòng trong mục 6 Limitations nếu mình muốn kể.)*

---

## J. ⭐ SUIREN BRANCH DELTA — 39 commit CHƯA merge vào dev (VIỆC CỦA CHÍNH WIGANZ)

> 🔥 **QUAN TRỌNG NHẤT:** Branch `refactor/suiren-ui-redesign` (39 commit, 2026-06-14→19) do **AiOT-TriTDD = chính Wiganz** viết — KHÁC với dev (do bot QADevOps/Paperclip viết). Đây là phần **engineering judgment THẬT của anh**, ngồi trên nền móng bot tạo ra. Đây là bằng chứng quyền tác giả mạnh nhất.

### J1. ★ ĐẢO NGƯỢC QUYẾT ĐỊNH TIỀN TỆ: USD-canonical → VND-canonical (commit `a1c2ebc`, `abf7fce`)

- **Quy ước cũ (dev, bot, `da33309`):** giá tài sản lưu **USD**. Bot suy ra rule này từ đọc code formatter — nhưng SAI: data & UX thật ra là VND.
- **Bug "ngáo giá":** pipeline tin "lưu USD" → nhân FX ~25.000× → món 9.87M₫ gợi ý giá **246 TỶ ₫** (tràn cả cột DB). Có lúc còn lật ngược: bỏ `vndToUsd()` → chia 25.000 → món không có comparable về **0₫**. Cùng một giá trị: lúc phồng 25.000×, lúc chia 25.000×.
- **Fix của Wiganz (`a1c2ebc`):** VND-canonical end-to-end. Storage = VND. Engine định giá vẫn chạy USD nội bộ (corpus comparable là USD) → **chuyển đổi dời về BIÊN của engine**: `vndToUsd()` trước khi vào engine, `usdToVnd()` khi ra. FX = hằng số `DEFAULT_USD_TO_VND_RATE=25000` (env override, KHÔNG phải forex live — đây là BE gap đã ghi nhận). Kèm migration 1 lần: `UPDATE items SET purchasePrice*25000 WHERE purchasePrice<100000`.
- **Verify:** iPhone 29.97M→11.26M₫, "other" 12.34M→9.87M₫ (hợp lý).
- 💎 **Story phỏng vấn:** "AI suy ra invariant SAI từ code formatter; tôi bắt được từ output vô lý (246 tỷ) + tràn cột DB; fix không chỉ đổi hằng số mà *dời điểm chuyển đổi về biên engine* để corpus USD và sản phẩm VND chung sống sạch."

### J2. Tính năng mới (chưa có trên dev)

| Feature                                 | Gì + Vì sao                                                                                                                                                                                                                                                                                                                                                     | Commit                                             |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **Notification system (Phase 3)** | `NotificationsModule` — feed thật: `GET /notifications` (cursor), unread-count, mark-read. **Emitter pattern**: producer gọi `NotificationsService.create()` khi có event (chat mới, escrow đổi state, sharing invite, warranty cron). `transition()` đổi thành async, emit bọc try/catch để lỗi notification KHÔNG phá FSM escrow. | `1fecb53`, `8a72bc2`, `c95be88`              |
| **OS push mọi notification**     | Expo trước (decrypt `pushToken`), **FCM fallback**. Push lỗi chỉ log, không ảnh hưởng feed/transaction.                                                                                                                                                                                                                                           | `c17ec9d`                                        |
| **Chat per-person**               | `getOrCreateThread` dedup theo `{buyerId, sellerId}` (bỏ `listingId`) → 1 hội thoại/người kiểu Chợ Tốt/Messenger. Không mutate `listingId` cũ (đụng unique index).                                                                                                                                                                           | `edd71dd`                                        |
| **Suiren UI redesign**            | Design tokens (web `globals.css` + mobile `theme/suiren.ts`), ~20 route, Ghibli background, AppNav responsive (⌘K search), trang `/search` global, mobile home redesign.                                                                                                                                                                                   | `de57673`, `95a8a18`, `96391ad`, `7708e19` |
| **Currency toggle ₫/$**          | `CurrencyContext` + `useCurrency()`, persist localStorage, default VND. Checkout MoMo & admin để cố định VND.                                                                                                                                                                                                                                            | `c29d678`                                        |

### J3. Fix lộ ra thiết kế (env footgun + currency lan rộng)

- **CSRF cookie maxAge 30d** (`858cdee`) → csrf là session cookie (mất khi đóng browser) trong khi access/refresh token sống lâu → user "như đang login" nhưng mọi POST 403. Lộ ra: scheme **double-submit-cookie CSRF**, tuổi thọ 3 cookie phải khớp.
- **access_token cookie 7d** (`30114b9`) → `ACCESS_TTL_MS` đọc env lúc **import module** (trước khi dotenv load) → default 15m; token ký lúc runtime nên `exp`=7d nhưng *cookie* chết ở 15m. Lộ ra: **footgun thứ tự load env / evaluate lúc import**. Fix: tính maxAge lúc runtime.
- **Magic-bytes trong AI flow** (`d62d9af`, `cd7993e`) → vision hardcode `image/jpeg` → PNG bị OpenAI 400. Đọc magic bytes (PNG `iVBORw`, JPEG `/9j/`...) để gán đúng MIME. ⚠️ **KHÁC dev `6b1a9fc`**: cái kia magic-byte để *từ chối* upload giả mạo (bảo mật); cái này để *gán đúng* nhãn cho OpenAI (đúng đắn). Cùng kỹ thuật, ngược mục đích.
- **PostGIS vào postgres image** (`5706ebe` stg, `63e09e2` prod) → image `pgvector/pgvector:pg16` thiếu PostGIS → `synchronize` crash tạo cột `geography` → API loop 502. Fix: Dockerfile `FROM pgvector + postgresql-16-postgis-3`. Lộ ra: hệ thống cần **CẢ pgvector (AI search) VÀ PostGIS (geo listing)** trong 1 image.
- **Audit 21 bug "make it real"** (`9bb1879`, `56d14c9`, `ceb02a5`) → gỡ data BỊA của UI bot tạo: fake category `[38,31,16,9,6]`, fake specs (256GB/91% pin), fake view count (`charCodeAt`), fake trend +4.2%, fake badge. CRITICAL: admin escrow hiện USD lệch 25.000× (cùng họ bug tiền tệ). Lộ ra: UI bot trông xong nhưng là **demo-ware bịa số**; Wiganz biến nó thành sản phẩm thật.

### J4. 💎 Mâu thuẫn dev↔suiren (vàng để kể chuyện phỏng vấn)

1. **USD→VND canonical** (J1) — bot suy invariant sai từ formatter; người bắt từ output vô lý.
2. **Flip-flop USD giữa chừng** — cùng giá trị lúc ×25.000 (246 tỷ), lúc ÷25.000 (0₫). "Bug có hai mặt"; fix thật = chọn 1 đơn vị canonical, chuyển đổi ở 1 biên duy nhất.
3. **Magic-byte 2 mục đích** — dev: từ chối (security); suiren: gán đúng (correctness). Đừng lẫn.
4. **UI bịa số → UI số thật** — scaffolding bot trông xong nhưng là demo-ware; pass audit của người làm nó thành thật.
5. **Bug tiền tệ lan nhiều bề mặt** (cả admin escrow) → chứng minh vì sao cần MỘT rule canonical duy nhất.

> ⚠️ **Lưu ý git:** 39 commit này CHƯA ở dev. Bản đồ quyết định phản ánh chúng vì là việc mới & thật nhất. Merge là quyết định production riêng (CI xanh + review), không phải vì tài liệu cần.
