# 🟢 Next.js / Expo Router — Field Manual

### Route của frontend: "ĐỂ ĐỒ ĐÚNG KỆ — KỆ chính là ĐỊA CHỈ" 🗂️

> *"Let your light shine before others." — Matthew 5:16*

---

## 🕊️ Triết lý một câu

> **Route frontend = VỊ TRÍ FILE.** Không có decorator nào cả. Anh để file đúng thư mục → thư mục đó CHÍNH LÀ URL. Đọc route = đọc đường dẫn file.

Đối lập hoàn toàn với backend NestJS — nơi *decorator anh gõ* mới là route. Xem `Routing-NestJS.md`.

> 💡 **Next.js** (web) và **Expo Router** (mobile) cùng MỘT triết lý: file-based. Asset Platform xài cả hai → nắm 1 cái là hiểu cái kia.

---

## ⚠️ ĐỪNG LẪN với NestJS: ở đây FILE = URL (THẬT SỰ)

Có **3 ý riêng biệt** — chỗ này hay lẫn:

| # | Ý | Của ai? | Vai trò |
| :-: | --- | --- | --- |
| 1️⃣ | **Folder = domain** (gom code theo tính năng) | 🔵🟢 **CẢ HAI** | sắp xếp code cho **người DỄ TÌM** |
| 2️⃣ | **Đường dẫn file = URL** | 🟢 **chỉ Next/Expo (file này)** | vị trí file **đẻ ra** URL |
| 3️⃣ | **Decorator `@Post()` = route** | 🔵 **chỉ NestJS** | gõ route lên hàm — xem `Routing-NestJS.md` |

> 🔬 **Bằng chứng file ĐẺ RA URL ở Next/Expo:** đổi tên `add-item.tsx` → `new-item.tsx` → route **đổi liền** `/add-item` → `/new-item`. File path CHÍNH LÀ route. (Ngược với NestJS: đổi folder, URL không đổi — vì URL ở decorator.)

> 🧠 **Nhớ đời:** 🟢 Next/Expo → folder/file = *vừa là tủ hồ sơ, VỪA LÀ địa chỉ URL luôn*. 🔵 NestJS → folder chỉ là tủ hồ sơ, URL nằm ở decorator.

---

## 🧩 LUẬT VÀNG — Đường dẫn file = URL

```
  app/dashboard/page.tsx          →  /dashboard
  app/items/[id]/page.tsx         →  /items/:id        ([id] = param động)
  app/(app)/add-item.tsx          →  /add-item         ((app) = nhóm, KHÔNG vào URL)
  app/api/items/route.ts          →  /api/items        (API route — backend-trong-Next)
```

> 🔑 **KHÔNG cần khai báo route ở đâu cả.** Tạo file đúng chỗ = route tự sinh. Xoá file = route biến mất.

---

## 🗺️ Bảng quy ước file/folder — đọc một route

| Ký hiệu | Nghĩa | Ví dụ |
| --- | --- | --- |
| `page.tsx` (Next) / `*.tsx` (Expo) | màn hình tại route đó | `app/items/page.tsx` → `/items` |
| `layout.tsx` | khung bọc chung (nav, header) | bọc mọi route con bên trong |
| `[id]` `[slug]` | **param động** (1 đoạn) | `items/[id]` → `/items/abc-123` |
| `[...slug]` | catch-all (nhiều đoạn) | bắt mọi path con |
| `(group)` | **nhóm route** — ngoặc tròn KHÔNG vào URL | `(app)`, `(auth)` để gom màn, không đổi địa chỉ |
| `app/api/.../route.ts` | **API route** (server, chỉ Next web) | backend nhẹ ngay trong Next |

> 💎 **`(app)` vs `[id]` — đừng lẫn:**
> - `(ngoặc tròn)` = nhóm tổ chức, **tàng hình** với URL.
> - `[ngoặc vuông]` = param động, **hiện** trong URL.

---

## 🔬 Ví dụ THẬT — Asset Platform mobile (đã tự trace)

```
apps/mobile/app/(app)/add-item.tsx
                └(app)┘ = nhóm route (tàng hình)   →  màn hình ở route /add-item
                       └ add-item ┘                →  tên file = đoạn URL
```

Luồng AI Capture đã trace — 2 màn nối nhau bằng **điều hướng file-based**:

```
review.tsx  ──router.replace('/(app)/add-item', {data})──▶  add-item.tsx
(màn nhận diện)         🧵 frontend KHÂU 2 nửa            (màn lưu kho)
```

> ⚠️ **BẪY 3 LỚP (quan trọng nhất):** màn hình `*.tsx` **KHÔNG giữ URL của API backend.** Nó chỉ gọi HÀM. URL `/items` thật nằm ở **lớp service** (`services/itemsApi.ts`), KHÔNG ở màn hình. → Tìm URL backend? Đừng đọc màn hình — mở `services/`.

```
🖼️ add-item.tsx ──gọi hàm── 📡 services/itemsApi.ts ──giữ URL /items── HTTP ──▶ backend
   (route file-based)         (lớp service, nơi có URL)
```

---

## 🪜 Cách TRACE một route frontend (gắn với `Trace-Any-Codebase`)

```
1. Muốn tìm MÀN HÌNH:  nhìn ĐƯỜNG DẪN FILE trong app/ (không grep decorator)
2. Muốn tìm URL API:   ĐỪNG đọc màn hình → mở services/ | api/ | lib/  (chặng ẩn)
3. Điều hướng giữa màn: tìm router.push/replace('/...') → đích là 1 file route khác
4. Param động:         thấy [id] trong path → đọc useLocalSearchParams()/useParams()
```

---

## 🃏 CHEAT CARD

```
┌─ NEXT.JS / EXPO ROUTING ────────────────────────────────────
│ Route = VỊ TRÍ FILE (không decorator, không khai báo).
│ đường-dẫn-file = URL.   page.tsx (Next) / *.tsx (Expo) = màn.
│ [id] = param ĐỘNG (hiện URL).  (group) = nhóm (TÀNG HÌNH).
│ app/api/.../route.ts = API route (server, chỉ Next web).
│ ⚠️ Màn hình KHÔNG giữ URL API → URL ở lớp services/api.
│ Điều hướng = router.push/replace('/path') → file route khác.
└──────────────────────────────────────────────────────────────
```

---

## 🔗 Anh em

- **`Routing-NestJS.md`** — mặt ngược lại: route = DECORATOR (backend).
- **`Trace-Any-Codebase.md`** — phục vụ "đổi sân sang frontend" + BẪY 3 LỚP.

> *"See, I am doing a new thing!" — Isaiah 43:19* 🟢🔥
