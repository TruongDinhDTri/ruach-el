# 🔵 NestJS Routing — Field Manual

### Route của backend NestJS: "DÁN NHÃN ĐỊA CHỈ lên hàm" ⚙️

> *"By wisdom a house is built." — Proverbs 24:3*

---

## 🕊️ Triết lý một câu

> **Route NestJS = DECORATOR anh GÕ ra.** Không phải vị trí file — mà là cái nhãn `@Get/@Post` anh dán lên trên một hàm. Đọc route = đọc decorator.

Đối lập hoàn toàn với frontend (Next/Expo) — nơi *vị trí file* mới là URL. Xem `Routing-NextJS.md`.

---

## ⚠️ BẪY TINH VI: ở NestJS, FOLDER ≠ URL

Dễ lẫn nhất. Có **3 ý riêng biệt** — đừng gộp:

| # | Ý | Của ai? | Vai trò |
| :-: | --- | --- | --- |
| 1️⃣ | **Folder = domain** (`items/`, `users/`) | 🔵🟢 **CẢ HAI** | sắp xếp code cho **người DỄ TÌM** — KHÔNG liên quan URL |
| 2️⃣ | **Đường dẫn file = URL** | 🟢 **chỉ Next/Expo** | routing: vị trí file **đẻ ra** URL |
| 3️⃣ | **Decorator `@Post()` = route** | 🔵 **chỉ NestJS** | routing: anh **gõ** route lên hàm |

> 🔬 **Bằng chứng folder KHÔNG đẻ URL ở NestJS:** đổi tên folder `items/` → `stuff/` nhưng giữ `@Controller('items')` → URL **vẫn là `/api/items`**. Folder đổi, URL không đổi. → Ở NestJS: **folder chỉ để con người tìm code; DECORATOR mới quyết URL.**
>
> 🪞 Còn Next/Expo ngược lại: đổi tên file = đổi URL liền (file path CHÍNH LÀ route).

> 🧠 **Nhớ đời:** 🔵 NestJS → folder = *"tủ hồ sơ cho người"*, URL = *decorator anh gõ*. Khi mình grep `apps/api/src/items/` là đang dùng folder để **TÌM CODE** (ý 1️⃣), KHÔNG phải đọc URL từ folder.

---

## 🧩 LUẬT VÀNG — Route = phép CỘNG 3 mảnh

URL đầy đủ KHÔNG nằm một chỗ. Nó **cộng dồn** từ 3 tầng:

```
  setGlobalPrefix('api')   (main.ts, 1 lần cho cả app)   →  /api
+ @Controller('items')     (đầu class controller)         →  /api/items
+ @Post()  /  @Get(':id')  (trên từng hàm)                →  POST /api/items
─────────────────────────────────────────────────────────────────────────
= URL THẬT mà client gọi
```

> 🔑 Thấy `@Post()` **rỗng** (không chữ trong ngoặc)? Nó KHÔNG thiếu — nó **kế thừa** path của `@Controller`. Rỗng = "ngay tại địa chỉ gốc của controller."

---

## 🗺️ Bản đồ decorator — đọc một controller

| Decorator | Nghĩa | Cho anh biết |
| --- | --- | --- |
| `@Controller('items')` | base path của cả class | mọi route trong đây bắt đầu bằng `/items` |
| `@Get()` `@Post()` `@Patch(':id')` `@Delete(':id')` | route + HTTP method | **CỬA VÀO** — request đập vào đây |
| `@UseGuards(JwtAuthGuard)` | chốt chặn trước khi vào | *ai* được vào (phải login?) |
| `@Throttle({...})` | rate-limit | tối đa bao nhiêu lần/phút |
| `@Body() dto: XxxDto` | thân request + validate | input được kiểm bằng DTO nào |
| `@CurrentUser()` `@Param()` `@Query()` | trích dữ liệu từ request | user (từ JWT), id trên URL, query string |

> 💎 **`:id` = tham số động.** `@Get(':id')` → `/api/items/abc-123` → `id = "abc-123"`. Dấu hai chấm = "chỗ này điền gì cũng được."

---

## 🔬 Ví dụ THẬT — Asset Platform (`items.controller.ts`, đã tự trace)

```ts
@Controller('items')                       // :57  → base = /api/items
export class ItemsController {

  @Post('photos/upload')                   // :67  → POST /api/items/photos/upload
  async uploadPhoto(...) { ... }

  @Post()                                  // :126 → POST /api/items  (rỗng = gốc controller)
  @HttpCode(HttpStatus.CREATED)            // :127 ┐
  @ApiOperation({ summary: '...' })        //      │ decorator MÔ TẢ (Swagger/status)
  @ApiResponse({ status: 201, ... })       //      ┘ — KHÔNG phải route
  async createItem(                        // :136 ← HÀM thật, cách @Post 10 dòng!
    @CurrentUser() user: any,              //       user lấy từ JWT guard (KHÔNG từ body)
    @Body() dto: CreateItemDto,            //       body validate bằng CreateItemDto
  ): Promise<ItemResponseDto> {
    return this.itemsService.create(dto, user.id);   // :137 → đẩy xuống SERVICE (controller mỏng)
  }
}
```

> ⚠️ **Bẫy hay vấp:** `@Post()` ở dòng 126 và hàm `createItem` ở dòng 136 **cách nhau 10 dòng** vì có 4 decorator mô tả chen giữa. Route (`@Post`) và việc làm (`createItem`) là 2 thứ DÁN vào nhau — đừng tưởng dòng `@Post` chính là hàm.

---

## 🪜 Cách TRACE một route NestJS (gắn với `Trace-Any-Codebase` BƯỚC 3)

```
1. Có URL (vd /items, method POST)
2. grep cửa vào:  grep -rn "@Controller('items')\|@Post(" apps/api/src/items/
3. Ráp 3 mảnh:    globalPrefix + @Controller(path) + @Post(path) = URL thật
4. Tìm hàm NGAY DƯỚI decorator (có thể cách vài dòng vì decorator mô tả)
5. Hàm đó gọi service nào → đó là cầu sang BƯỚC 4 (business logic)
```

---

## 🃏 CHEAT CARD

```
┌─ NESTJS ROUTING ────────────────────────────────────────────
│ Route = DECORATOR (gõ ra), KHÔNG phải vị trí file.
│ URL = setGlobalPrefix + @Controller(path) + @Method(path)
│ @Post() rỗng = gốc controller. @Get(':id') = param động.
│ Cửa vào = file *.controller.ts, grep "@Controller\|@Post\|@Get"
│ Controller MỎNG → đọc nó để tìm service nó gọi (→ BƯỚC 4).
│ Hàm có thể cách decorator vài dòng (decorator mô tả chen giữa).
└──────────────────────────────────────────────────────────────
```

---

## 🔗 Anh em

- **`Routing-NextJS.md`** — mặt ngược lại: route = VỊ TRÍ FILE (frontend).
- **`Trace-Any-Codebase.md`** — file này phục vụ BƯỚC 3 (tìm cửa vào) của 6 bước.

> *"Commit your work to the Lord, and your plans will be established." — Proverbs 16:3* ⚙️🔥
