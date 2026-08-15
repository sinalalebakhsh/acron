# ACRON Methodology Part-21

<aside>
📢

در Part-19 ، **فاز 11:**    Frontend - Presentation Layer  تا قدم 213 توسعه داده شد

</aside>

# فاز 11**:**   Frontend - Presentation Layer

شروع قدم 214

---

<aside>
💡

### مرحله ۴ — با کاربر `sinaa` وارد شو

</aside>

> 214- اجرا ، Login را انجام بده.
> 
> 
> بعد بررسی کن:
> 
> **Products → اضافه کردن محصول به Cart → Cart**
> 
> باید محصول داخل Cart باشد.
> 

<aside>
💡

### مرحله ۵ — Checkout

</aside>

> 215- در Cart روی:
> 
> 
> **Proceed to Checkout**
> 
> کلیک کن.
> 
> اینجا سه چیز باید بررسی شود:
> 
> 1. آیا صفحه `/checkout` باز می‌شود؟
> 2. آیا Address مربوط به `sinaa` نمایش داده می‌شود؟
> 3. آیا Cart و محصولات داخل Order Summary نمایش داده می‌شوند؟

<aside>
💡

### مرحله ۶ — ایجاد سفارش

</aside>

> 216- یک Address را انتخاب کن و روی:
> 
> 
> **Place order**
> 
> بزن.
> 
> اگر همه چیز درست باشد:
> 
> ```
> POST /api/orders/
> ```
> 
> باید پاسخ موفق بگیرد و بعد React به:
> 
> ```
> /orders
> ```
> 
> منتقل شود.
> 

<aside>
💡

### مرحله ۷ — مهم‌ترین تست

</aside>

> 217- بعد از ایجاد سفارش، برو به:
> 
> 
> ```
> /orders
> ```
> 
> باید سفارش جدید را ببینی.
> 
> بعد Cart را بررسی کن.
> 
> باید Cart قبلی حذف شده باشد؛ چون در Backend خودمان این رفتار را داریم:
> 
> ```
> cart.delete()
> ```
> 

یعنی جریان باید این باشد:

```
Cart
  │
  ▼
Checkout
  │
  ├── Select Address
  │
  ▼
OrderService.place_order()
  │
  ├── Customer validation
  ├── Cart validation
  ├── Address validation
  ├── Create Order
  ├── Create OrderItems
  └── Delete Cart
       │
       ▼
     Orders
```

### بعد از موفقیت Checkout چه کار می‌کنیم؟

اگر Checkout بدون خطا کار کرد، توسعه را همین‌جا متوقف نمی‌کنیم. مرحله بعدی منطقی پروژه:

**Checkout → Order Detail → Payment**

خواهد بود.

یعنی ابتدا:

1. تکمیل و تست Checkout
2. ساخت صفحه `OrderDetail`
3. نمایش جزئیات سفارش و Address Snapshot
4. اتصال Order Detail به API
5. سپس Payment Domain
6. بعد Authentication hardening
7. بعد برطرف‌کردن مشکل تصاویر محصولات
8. سپس بهبود UI

این همان مسیر **Domain-based** پروژه ACRON است و قرار نیست تصادفی بین فایل‌ها جابه‌جا شویم.

**پس الان فقط مرحله Checkout را تست کن.**

```python
[12/Aug/2026 12:09:57] "GET /products/main/2026/07/Samsung-S24_-2.jpg HTTP/1.1" 404 18009
[12/Aug/2026 12:10:00] "OPTIONS /api/carts/cart-items/41/ HTTP/1.1" 200 0
[12/Aug/2026 12:10:00] "PATCH /api/carts/cart-items/41/ HTTP/1.1" 200 14
[12/Aug/2026 12:10:01] "GET /api/carts/mine/ HTTP/1.1" 200 508
Not Found: /products/main/2026/07/apple-10-x-jpg.jpg
Not Found: /products/main/2026/07/Samsung-S24_-2.jpg
[12/Aug/2026 12:10:01] "GET /products/main/2026/07/apple-10-x-jpg.jpg HTTP/1.1" 404 18009
[12/Aug/2026 12:10:01] "GET /products/main/2026/07/Samsung-S24_-2.jpg HTTP/1.1" 404 18009
[12/Aug/2026 12:10:04] "OPTIONS /api/customers/addresses/ HTTP/1.1" 200 0
[12/Aug/2026 12:10:04] "OPTIONS /api/customers/addresses/ HTTP/1.1" 200 0
C:\Users\sina\.virtualenvs\backend-TBakwqam\Lib\site-packages\rest_framework\pagination.py:198: UnorderedObjectListWarning: Pagination may yield inconsistent results with an unordered object_list: <class 'apps.customers.models.Address'> QuerySet.
  paginator = self.django_paginator_class(queryset, page_size)
[12/Aug/2026 12:10:04] "GET /api/customers/addresses/ HTTP/1.1" 200 1013
[12/Aug/2026 12:10:04] "GET /api/customers/addresses/ HTTP/1.1" 200 1013
[12/Aug/2026 12:10:29] "POST /api/orders/ HTTP/1.1" 201 716
[12/Aug/2026 12:10:29] "GET /api/orders/ HTTP/1.1" 200 5161
[12/Aug/2026 12:10:29] "GET /api/orders/ HTTP/1.1" 200 5161
Not Found: /products/main/2026/07/Samsung-S24_-2.jpg
Not Found: /products/main/2026/07/apple-10-x-jpg.jpg
[12/Aug/2026 12:10:37] "GET /products/main/2026/07/Samsung-S24_-2.jpg HTTP/1.1" 404 18008
[12/Aug/2026 12:10:37] "GET /products/main/2026/07/apple-10-x-jpg.jpg HTTP/1.1" 404 18009
[12/Aug/2026 12:10:55] "GET /api/orders/ HTTP/1.1" 200 5161
[12/Aug/2026 12:10:55] "GET /api/orders/ HTTP/1.1" 200 5161
Not Found: /products/main/2026/07/Samsung-S24_-2.jpg
Not Found: /products/main/2026/07/apple-10-x-jpg.jpg
[12/Aug/2026 12:11:01] "GET /products/main/2026/07/Samsung-S24_-2.jpg HTTP/1.1" 404 18008
[12/Aug/2026 12:11:01] "GET /products/main/2026/07/apple-10-x-jpg.jpg HTTP/1.1" 404 18009
[12/Aug/2026 12:11:02] "GET /api/orders/ HTTP/1.1" 200 5161
[12/Aug/2026 12:11:02] "GET /api/orders/ HTTP/1.1" 200 5161
Not Found: /products/main/2026/07/apple-10-x-jpg.jpg
Not Found: /products/main/2026/07/Samsung-S24_-2.jpg
[12/Aug/2026 12:11:05] "GET /products/main/2026/07/apple-10-x-jpg.jpg HTTP/1.1" 404 18008
[12/Aug/2026 12:11:05] "GET /products/main/2026/07/Samsung-S24_-2.jpg HTTP/1.1" 404 18008
[12/Aug/2026 12:11:45] "GET /api/products/?page=1 HTTP/1.1" 200 2439
[12/Aug/2026 12:11:45] "GET /api/products/?page=1 HTTP/1.1" 200 2439
Not Found: /products/main/2026/07/apple-10-x-jpg.jpg
[12/Aug/2026 12:11:45] "GET /products/main/2026/07/apple-10-x-jpg.jpg HTTP/1.1" 404 18009
Not Found: /products/main/2026/07/Samsung-S24_-2.jpg
[12/Aug/2026 12:11:45] "GET /products/main/2026/07/Samsung-S24_-2.jpg HTTP/1.1" 404 18009
Bad Request: /api/carts/cart-items/
[12/Aug/2026 12:11:49] "POST /api/carts/cart-items/ HTTP/1.1" 400 73
[12/Aug/2026 12:11:49] "OPTIONS /api/carts/ HTTP/1.1" 200 0
[12/Aug/2026 12:11:50] "POST /api/carts/ HTTP/1.1" 201 72
[12/Aug/2026 12:11:50] "POST /api/carts/cart-items/ HTTP/1.1" 201 86
[12/Aug/2026 12:11:50] "GET /api/carts/mine/ HTTP/1.1" 200 72
[12/Aug/2026 12:11:59] "GET /api/products/?page=1 HTTP/1.1" 200 2439
[12/Aug/2026 12:11:59] "GET /api/products/?page=1 HTTP/1.1" 200 2439
Not Found: /products/main/2026/07/Samsung-S24_-2.jpg
Not Found: /products/main/2026/07/apple-10-x-jpg.jpg
[12/Aug/2026 12:11:59] "GET /products/main/2026/07/Samsung-S24_-2.jpg HTTP/1.1" 404 18009
[12/Aug/2026 12:11:59] "GET /products/main/2026/07/apple-10-x-jpg.jpg HTTP/1.1" 404 18009
[12/Aug/2026 12:12:01] "POST /api/carts/cart-items/ HTTP/1.1" 201 86
[12/Aug/2026 12:12:01] "GET /api/carts/mine/ HTTP/1.1" 200 297
Not Found: /products/main/2026/07/apple-10-x-jpg.jpg
[12/Aug/2026 12:12:05] "GET /products/main/2026/07/apple-10-x-jpg.jpg HTTP/1.1" 404 18008
[12/Aug/2026 12:12:21] "OPTIONS /api/carts/cart-items/43/ HTTP/1.1" 200 0
[12/Aug/2026 12:12:21] "PATCH /api/carts/cart-items/43/ HTTP/1.1" 200 14
[12/Aug/2026 12:12:21] "GET /api/carts/mine/ HTTP/1.1" 200 297
Not Found: /products/main/2026/07/apple-10-x-jpg.jpg
[12/Aug/2026 12:12:21] "GET /products/main/2026/07/apple-10-x-jpg.jpg HTTP/1.1" 404 18008
[12/Aug/2026 12:12:33] "GET /api/orders/ HTTP/1.1" 200 5161
[12/Aug/2026 12:12:33] "GET /api/orders/ HTTP/1.1" 200 5161
Not Found: /products/main/2026/07/apple-10-x-jpg.jpg
[12/Aug/2026 12:12:49] "GET /products/main/2026/07/apple-10-x-jpg.jpg HTTP/1.1" 404 18008
[12/Aug/2026 12:12:52] "GET /api/customers/addresses/ HTTP/1.1" 200 1013
[12/Aug/2026 12:12:52] "GET /api/customers/addresses/ HTTP/1.1" 200 1013
[12/Aug/2026 12:13:25] "POST /api/orders/ HTTP/1.1" 201 624
[12/Aug/2026 12:13:25] "GET /api/orders/ HTTP/1.1" 200 5296
[12/Aug/2026 12:13:25] "GET /api/orders/ HTTP/1.1" 200 5296
Not Found: /products/main/2026/07/apple-10-x-jpg.jpg
[12/Aug/2026 12:13:43] "GET /products/main/2026/07/apple-10-x-jpg.jpg HTTP/1.1" 404 18008
[12/Aug/2026 12:13:47] "OPTIONS /api/carts/e0adc89f-2c68-4476-b98d-58a7cc290713/ HTTP/1.1" 200 0
[12/Aug/2026 12:13:47] "OPTIONS /api/carts/e0adc89f-2c68-4476-b98d-58a7cc290713/ HTTP/1.1" 200 0
[12/Aug/2026 12:13:47] "GET /api/me/ HTTP/1.1" 200 96
Not Found: /api/carts/e0adc89f-2c68-4476-b98d-58a7cc290713/
[12/Aug/2026 12:13:47] "GET /api/carts/e0adc89f-2c68-4476-b98d-58a7cc290713/ HTTP/1.1" 404 45
[12/Aug/2026 12:13:47] "GET /api/me/ HTTP/1.1" 200 96
Not Found: /api/carts/e0adc89f-2c68-4476-b98d-58a7cc290713/
[12/Aug/2026 12:13:47] "GET /api/carts/e0adc89f-2c68-4476-b98d-58a7cc290713/ HTTP/1.1" 404 45
[12/Aug/2026 12:13:47] "GET /api/carts/mine/ HTTP/1.1" 200 72
[12/Aug/2026 12:13:47] "POST /api/carts/ HTTP/1.1" 201 72
```

**هسته‌ی اصلی Checkout و Order کاملاً درست کار می‌کند** و الان چند مسئله‌ی جداگانه داریم که باید به‌ترتیب و بدون تغییرات تصادفی بررسی کنیم.

### 1. Checkout و Order موفق هستند ✅

این بخش بسیار مهم است:

```
POST /api/orders/ HTTP/1.1" 201
GET /api/orders/ HTTP/1.1" 200
```

یعنی:

**Cart → Checkout → Address → OrderService → Order → Orders**

با موفقیت کار کرده است.

حتی پاسخ `201` برای `POST /api/orders/` نشان می‌دهد سفارش واقعاً در Backend ساخته شده.

---

### 2. مشکل تصاویر هنوز باقی است ❌

چندین بار داریم:

```
Not Found: /products/main/2026/07/apple-10-x-jpg.jpg
404
```

و:

```
Not Found: /products/main/2026/07/Samsung-S24_-2.jpg
404
```

این همان مشکلی است که قبلاً مشخص کرده بودیم:

> Product images are not being served correctly.
> 

نکته مهم این است که **این مشکل فعلاً مربوط به React نیست**.

همچنین ، React آدرس تصویر را دریافت کرده و درخواست را ارسال می‌کند، اما Django در آن URL فایل را پیدا نمی‌کند.

پس فعلاً ProductCard یا Cart را دستکاری نمی‌کنیم.

<aside>
💡

### الان چه کار کنیم؟

</aside>

الان وضعیت پروژه کاملاً قابل تشخیص است و **نباید تصادفی فایل‌های مختلف را تغییر بدهیم**.

خبر خوب این است که بخش‌های اصلی ACRON الان کار می‌کنند:

- Login ✅
- `/api/me/` ✅
- Cart API ✅
- تغییر تعداد Cart Item ✅
- Address API ✅
- Checkout / ایجاد Order ✅
- Orders API و صفحه Orders ✅

<aside>
💡

### مشکل اصلی Cart: استفاده از `cart_id` قدیمی

</aside>

این بخش لاگ خیلی مهم است:

```
GET /api/carts/e0adc89f-2c68-4476-b98d-58a7cc290713/ HTTP/1.1" 404
```

در حالی که بلافاصله بعدش:

```
GET /api/carts/mine/ HTTP/1.1" 200
POST /api/carts/ HTTP/1.1" 201
POST /api/carts/ HTTP/1.1" 201
```

یعنی Frontend در یک نقطه هنوز دارد با این شناسه:

```
e0adc89f-2c68-4476-b98d-58a7cc290713
```

به:

```
/api/carts/<cart_id>/
```

درخواست می‌زند، در حالی که Cart دیگر وجود ندارد.

### چرا؟

در `CartContext.jsx` این منطق را داریم:

```
let cartId = localStorage.getItem("cart_id");
```

و برای کاربر مهمان:

```
const cartData = await cartService.getCart(cartId);
```

اما وقتی Cart تبدیل به Order می‌شود، در Backend این کار انجام می‌شود:

```
cart.delete()
```

بنابراین:

```
Cart
 ↓
Create Order
 ↓
Cart deleted
```

ولی `localStorage` هنوز ممکن است این را داشته باشد:

```
cart_id = e0adc89f-...
```

پس Frontend می‌گوید:

> من Cart با این ID را می‌خواهم.
> 

Django می‌گوید:

> چنین Cartی وجود ندارد.
> 

و نتیجه:

```
404
```

<aside>
💡

### یک مشکل معماری کوچک در `CartContext`

</aside>

الان منطق Cart برای **Guest** و **Authenticated User** با هم مخلوط شده است.

این قسمت:

```
if (isAuthenticated) {
    const cartData = await cartService.getMyCart();

    setCart(cartData);

    if (cartData?.id) {
        localStorage.setItem("cart_id", cartData.id);
    }

    return;
}
```

درست است.

اما وقتی کاربر Login می‌کند، بهتر است Cart قدیمی Guest را دیگر به عنوان Cart فعلی نگه نداریم.

یعنی هنگام ورود:

```
Guest Cart
    ↓
Login
    ↓
Authenticated Cart
```

باید وضعیت Cart کاملاً از Backend کاربر گرفته شود.

<aside>
💡

### چرا دو بار `POST /api/carts/` می‌بینیم؟

</aside>

این قسمت:

```
POST /api/carts/ HTTP/1.1" 201
POST /api/carts/ HTTP/1.1" 201
```

هم مهم است.

در Development Mode، اگر پروژه React با `StrictMode` اجرا شود، `useEffect` ممکن است برای پیدا کردن side-effectهای مشکل‌دار دوبار اجرا شود.

بنابراین این:

```
useEffect(() => {
    fetchOrCreateCart();
}, [isAuthenticated]);
```

می‌تواند در Development باعث اجرای دوباره‌ی منطق شود.

ولی یک نکته مهم‌تر وجود دارد:

### Backend نباید اجازه دهد `POST /api/carts/` برای یک کاربر authenticated بی‌جهت Cart جدید بسازد.

این یک مسئله Backend هم هست.

در معماری درست، باید تقریباً این رفتار را داشته باشیم:

```
GET /api/carts/mine/
        ↓
Cart موجود؟
   ↙          ↘
 Yes           No
 ↓              ↓
Return       Create
Cart         Cart
```

نه اینکه Frontend مرتب:

```
POST /api/carts/
POST /api/carts/
POST /api/carts/
```

انجام دهد.

<aside>
💡

### اصلاح `CartContext.jsx`

</aside>

نسخه فعلی شما این قسمت را دارد:

```python
if (isAuthenticated) {
    const cartData = await cartService.getMyCart();

    setCart(cartData);

    if (cartData?.id) {
        localStorage.setItem("cart_id", cartData.id);
    }

    return;
}
```

این قسمت را نگه می‌داریم، ولی **قبل از گرفتن Cart کاربر، Cart ID قدیمی Guest را پاک می‌کنیم.**

به این شکل:

```python
if (isAuthenticated) {
    localStorage.removeItem("cart_id");

    const cartData = await cartService.getMyCart();

    setCart(cartData);

    if (cartData?.id) {
        localStorage.setItem("cart_id", cartData.id);
    }

    return;
}
```

### چرا؟

چون بعد از Login دیگر نباید به Cart Guest قبلی وابسته باشیم.

<aside>
💡

### یک اصلاح مهم‌تر

</aside>

وقتی Order ساخته می‌شود، Backend Cart را حذف می‌کند:

```
cart.delete()
```

پس بعد از:

```
const order = await orderService.createOrder(...)
```

باید Cart Context هم بفهمد که Cart قبلی دیگر وجود ندارد.

در `Checkout.jsx` الان احتمالاً این کار را نداریم.

پس بعد از موفقیت Order باید Cart state پاک شود.

ولی قبل از اینکه این را تغییر بدهیم، می‌خواهم معماری را تمیز نگه داریم.

<aside>
💡

### مشکل تصاویر کاملاً جداست

</aside>

این خط‌ها:

```
Not Found: /products/main/2026/07/apple-10-x-jpg.jpg
```

هیچ ارتباطی با Login، Cart یا Orders ندارند.

API محصول درست است:

```
GET /api/products/?page=1
200
```

ولی Browser برای تصویر می‌رود:

```
/products/main/2026/07/apple-10-x-jpg.jpg
```

و Django:

```
404
```

یعنی:

> URL تصویر تولید شده، ولی Django نمی‌تواند فایل Media را از آن URL سرو کند.
> 

این همان یکی از مشکلاتی است که قبلاً هم داشتیم و قرار بود **بعد از تکمیل جریان Cart → Orders → Checkout → Authentication** اصولی اصلاحش کنیم.

الان دقیقاً به همان نقطه رسیده‌ایم.

<aside>
💡

### الان چه کار کنیم؟

</aside>

من پیشنهاد می‌کنم **فعلاً هیچ چیز دیگری را تغییر ندهیم**.

ترتیب ادامه توسعه ACRON این باشد:

```
                    ACRON
                      │
                      ▼
             Authentication ✅
                      │
                      ▼
                Product ✅
                      │
                      ▼
                  Cart ✅
                      │
                      ▼
                 Checkout ✅
                      │
                      ▼
                 Orders ✅
                      │
                      ▼
             Cart State Fix  ← الان اینجاییم
                      │
                      ▼
             Product Images
                      │
                      ▼
          Pagination / API Cleanup
                      │
                      ▼
          Authentication Hardening
                      │
                      ▼
              Payment Domain
```

---

پیشنهاد می‌کنم **اول Cart state را اصولی اصلاح کنیم**؛ نه اینکه صرفاً خطای 404 را مخفی کنیم.

برای این مرحله فقط یک فایل را تغییر می‌دهیم:

```
frontend/src/context/CartContext.jsx
```

و منطق آن را به این شکل تمیز می‌کنیم:

### Guest

```
localStorage cart_id
        ↓
Cart موجود؟
   ↓ No
Create Cart
```

### Authenticated

```
GET /api/carts/mine/
        ↓
Cart کاربر
        ↓
ذخیره ID فعلی
```

### بعد از Checkout

```
POST /api/orders/
        ↓
Order created
        ↓
Cart deleted by Backend
        ↓
Frontend Cart state cleared
        ↓
New Cart when needed
```

این روش از اینکه هر بار با `404` به Cart قدیمی برخورد کنیم جلوگیری می‌کند.

هدف این اصلاح:

1. بعد از Login، `cart_id` قدیمی Guest باقی نماند.
2. بعد از Checkout، Cart حذف‌شده باعث 404 نشود.
3. Cart کاربر authenticated همیشه از `/api/carts/mine/` گرفته شود.
4. منطق فعلی `addToCart`, `updateQuantity`, `removeFromCart` حفظ شود.
5. ساختار Domain-based پروژه را به‌هم نزنیم.

<aside>
💡

### فایل را جایگزین کن

</aside>

> 218- فایل:
> 
> 
> ```
> frontend/src/context/CartContext.jsx
> ```
> 
> کل محتوای فعلی را با این نسخه جایگزین کن:
> 
> ```python
> import {
>   createContext,
>   useContext,
>   useEffect,
>   useState,
> } from "react";
> 
> import { useAuth } from "./AuthContext";
> import cartService from "../services/cartService";
> 
> const CartContext = createContext(null);
> 
> export const CartProvider = ({ children }) => {
>   const { isAuthenticated } = useAuth();
> 
>   const [cart, setCart] = useState(null);
>   const [loading, setLoading] = useState(true);
> 
>   // --------------------------------------------------
>   // دریافت یا ایجاد Cart
>   // --------------------------------------------------
> 
>   const fetchOrCreateCart = async () => {
>     setLoading(true);
> 
>     try {
>       // ==================================================
>       // کاربر authenticated
>       // ==================================================
> 
>       if (isAuthenticated) {
>         // Cart مربوط به Guest دیگر نباید استفاده شود.
>         localStorage.removeItem("cart_id");
> 
>         const cartData = await cartService.getMyCart();
> 
>         setCart(cartData);
> 
>         if (cartData?.id) {
>           localStorage.setItem(
>             "cart_id",
>             cartData.id
>           );
>         }
> 
>         return;
>       }
> 
>       // ==================================================
>       // کاربر Guest
>       // ==================================================
> 
>       let cartId =
>         localStorage.getItem("cart_id");
> 
>       // اگر Guest هنوز Cart ندارد
>       if (!cartId) {
>         const newCart =
>           await cartService.createCart();
> 
>         cartId = newCart.id;
> 
>         localStorage.setItem(
>           "cart_id",
>           cartId
>         );
> 
>         setCart(newCart);
> 
>         return;
>       }
> 
>       // ==================================================
>       // تلاش برای دریافت Cart موجود
>       // ==================================================
> 
>       try {
>         const cartData =
>           await cartService.getCart(cartId);
> 
>         setCart(cartData);
>       } catch (error) {
>         // Cart قبلی دیگر وجود ندارد
>         if (error.response?.status === 404) {
>           localStorage.removeItem("cart_id");
> 
>           const newCart =
>             await cartService.createCart();
> 
>           localStorage.setItem(
>             "cart_id",
>             newCart.id
>           );
> 
>           setCart(newCart);
>         } else {
>           throw error;
>         }
>       }
>     } catch (error) {
>       console.error(
>         "Failed to fetch cart:",
>         error.response?.data || error
>       );
> 
>       setCart(null);
>     } finally {
>       setLoading(false);
>     }
>   };
> 
>   // --------------------------------------------------
>   // اجرای Cart loading هنگام تغییر وضعیت Authentication
>   // --------------------------------------------------
> 
>   useEffect(() => {
>     fetchOrCreateCart();
>   }, [isAuthenticated]);
> 
>   // --------------------------------------------------
>   // افزودن محصول به Cart
>   // --------------------------------------------------
> 
>   const addToCart = async (productId) => {
>     try {
>       let cartId =
>         cart?.id ||
>         localStorage.getItem("cart_id");
> 
>       // اگر Cart نداریم، یک Cart ایجاد می‌کنیم
>       if (!cartId) {
>         const newCart =
>           await cartService.createCart();
> 
>         cartId = newCart.id;
> 
>         localStorage.setItem(
>           "cart_id",
>           cartId
>         );
>       }
> 
>       try {
>         await cartService.addItem(
>           cartId,
>           productId,
>           1
>         );
>       } catch (error) {
>         /*
>          * ممکن است cart_id موجود در localStorage
>          * دیگر در Backend وجود نداشته باشد.
>          */
> 
>         const invalidCart =
>           error.response?.status === 400 &&
>           error.response?.data?.cart_id;
> 
>         if (!invalidCart) {
>           throw error;
>         }
> 
>         // Cart قدیمی را حذف می‌کنیم
>         localStorage.removeItem("cart_id");
> 
>         // Cart جدید ایجاد می‌کنیم
>         const newCart =
>           await cartService.createCart();
> 
>         cartId = newCart.id;
> 
>         localStorage.setItem(
>           "cart_id",
>           cartId
>         );
> 
>         // دوباره محصول را اضافه می‌کنیم
>         await cartService.addItem(
>           cartId,
>           productId,
>           1
>         );
>       }
> 
>       // دریافت وضعیت جدید Cart
>       await fetchOrCreateCart();
>     } catch (error) {
>       console.error(
>         "Failed to add item to cart:",
>         error.response?.data || error
>       );
> 
>       throw error;
>     }
>   };
> 
>   // --------------------------------------------------
>   // تغییر تعداد محصول
>   // --------------------------------------------------
> 
>   const updateQuantity = async (
>     itemId,
>     newQuantity
>   ) => {
>     if (newQuantity < 1) {
>       return;
>     }
> 
>     try {
>       await cartService.updateItem(
>         itemId,
>         newQuantity
>       );
> 
>       await fetchOrCreateCart();
>     } catch (error) {
>       console.error(
>         "Failed to update cart item:",
>         error.response?.data || error
>       );
> 
>       throw error;
>     }
>   };
> 
>   // --------------------------------------------------
>   // حذف محصول از Cart
>   // --------------------------------------------------
> 
>   const removeFromCart = async (itemId) => {
>     try {
>       await cartService.removeItem(itemId);
> 
>       await fetchOrCreateCart();
>     } catch (error) {
>       console.error(
>         "Failed to remove cart item:",
>         error.response?.data || error
>       );
> 
>       throw error;
>     }
>   };
> 
>   // --------------------------------------------------
>   // پاک کردن وضعیت Cart در Frontend
>   // --------------------------------------------------
> 
>   const clearCartState = () => {
>     setCart(null);
>     localStorage.removeItem("cart_id");
>   };
> 
>   // --------------------------------------------------
>   // تعداد کل محصولات Cart
>   // --------------------------------------------------
> 
>   const totalItemsCount =
>     cart?.items?.reduce(
>       (total, item) =>
>         total + item.quantity,
>       0
>     ) || 0;
> 
>   // --------------------------------------------------
>   // Context
>   // --------------------------------------------------
> 
>   return (
>     <CartContext.Provider
>       value={{
>         cart,
>         loading,
>         totalItemsCount,
>         addToCart,
>         updateQuantity,
>         removeFromCart,
>         clearCartState,
>         refreshCart: fetchOrCreateCart,
>       }}
>     >
>       {children}
>     </CartContext.Provider>
>   );
> };
> 
> export const useCart = () =>
>   useContext(CartContext);
> ```
> 

<aside>
💡

### چرا این نسخه بهتر است؟

</aside>

تغییر اصلی این قسمت است:

```
if (isAuthenticated) {
  localStorage.removeItem("cart_id");

  const cartData =
    await cartService.getMyCart();
```

یعنی وقتی کاربر Login شده است، دیگر نمی‌گوییم:

> Cart قبلی داخل `localStorage` را استفاده کن.
> 

بلکه می‌گوییم:

> Backend، Cart واقعی این کاربر را به من بده.
> 

<aside>
💡

### حالا سرورها را اجرا کن

</aside>

Django:

```
python manage.py runserver
```

و Frontend:

```
npm run dev
```

اگر هر دو از قبل اجرا هستند، **لازم نیست خاموش و روشنشان کنی**؛ Vite فایل را Hot Reload می‌کند.

<aside>
💡

### تستی که می‌خواهم انجام بدهی

</aside>

قبل از تست، در Browser:

**F12 → Application → Local Storage →**

برای:

```
http://localhost:5173
```

اگر این مقدار را دیدی:

```
cart_id
```

فعلاً حذفش کن.

بعد صفحه را Refresh کن.

<aside>
💡

### تست اول — Cart

</aside>

> 219- برو:
> 
> 
> ```
> /products
> ```
> 
> یک محصول را Add to Cart کن.
> 
> بعد:
> 
> ```
> /cart
> ```
> 
> باید محصول را ببینی.
> 
> تعداد را با `+` و `−` تغییر بده.
> 
> باید درخواست‌هایی شبیه این ببینیم:
> 
> ```
> PATCH /api/carts/cart-items/<id>/
> 200
> ```
> 

---

<aside>
💡

### تست دوم — Checkout

</aside>

> 220- از Cart برو:
> 
> 
> ```
> /checkout
> ```
> 
> آدرس را انتخاب کن.
> 
> روی:
> 
> ```
> Place order
> ```
> 
> بزن.
> 
> باید:
> 
> ```
> POST /api/orders/
> 201
> ```
> 
> و سپس:
> 
> ```
> GET /api/orders/
> 200
> ```
> 
> ببینیم.
> 

---

<aside>
💡

### تست سوم — Cart بعد از Order

</aside>

> 221- بعد از ایجاد سفارش، دوباره برو:
> 
> 
> ```
> /cart
> ```
> 
> اینجا نکته مهم است.
> 
> چون Backend در `OrderService` این کار را انجام می‌دهد:
> 
> ```
> cart.delete()
> ```
> 
> Cart قبلی دیگر وجود ندارد.
> 
> نباید دوباره درخواست problematic زیر را ببینیم:
> 
> ```
> GET /api/carts/e0adc89f-.../
> 404
> ```
> 
> و Frontend باید بتواند Cart جدید/وضعیت جدید را مدیریت کند.
> 

<aside>
💡

### یک نکته مهم درباره Checkout

</aside>

در مرحله بعد، باید `Checkout.jsx` را هم با `CartContext` هماهنگ کنیم.

الان Checkout خودش Cart را با:

```
cartService.getCart()
```

می‌گیرد.

در حالی که ما یک `CartContext` داریم که وظیفه‌اش مدیریت Cart است.

بنابراین معماری نهایی بهتر است:

```
                  CartContext
                      │
          ┌───────────┴───────────┐
          │                       │
       Cart.jsx              Checkout.jsx
          │                       │
          └───────────┬───────────┘
                      │
                cartService
                      │
                Django API
```

نه اینکه:

```
Cart.jsx ──────────┐
                   │
Checkout.jsx ──────┼──> cartService
                   │
CartContext ───────┘
```

این یکی از کارهایی است که در مرحله بعد انجام می‌دهیم.

<aside>
💡

### اما فعلاً سراغ Checkout نرو

</aside>

فعلاً فقط:

**`CartContext.jsx` را جایگزین کن و تست بالا را انجام بده.**

```python
$ python manage.py runserver

Watching for file changes with StatReloader

Performing system checks...

System check identified no issues (0 silenced).

August 13, 2026 - 00:39:38

Django version 6.0.7, using settings 'config.settings'

Starting development server at http://127.0.0.1:8000/

Quit the server with CTRL-BREAK.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.

For more information on production servers see: https://docs.djangoproject.com/en/6.0/howto/deployment/

[13/Aug/2026 00:39:56] "OPTIONS /api/carts/657e794a-6cfc-455f-b66c-36c3392cbd95/ HTTP/1.1" 200 0

[13/Aug/2026 00:39:56] "OPTIONS /api/carts/657e794a-6cfc-455f-b66c-36c3392cbd95/ HTTP/1.1" 200 0

[13/Aug/2026 00:39:56] "OPTIONS /api/me/ HTTP/1.1" 200 0

[13/Aug/2026 00:39:56] "OPTIONS /api/me/ HTTP/1.1" 200 0

Unauthorized: /api/me/

[13/Aug/2026 00:39:56] "GET /api/me/ HTTP/1.1" 401 172

Unauthorized: /api/carts/657e794a-6cfc-455f-b66c-36c3392cbd95/

[13/Aug/2026 00:39:56] "GET /api/carts/657e794a-6cfc-455f-b66c-36c3392cbd95/ HTTP/1.1" 401 172

[13/Aug/2026 00:39:56] "OPTIONS /api/token/refresh/ HTTP/1.1" 200 0

Unauthorized: /api/carts/657e794a-6cfc-455f-b66c-36c3392cbd95/

[13/Aug/2026 00:39:56] "GET /api/carts/657e794a-6cfc-455f-b66c-36c3392cbd95/ HTTP/1.1" 401 172

Unauthorized: /api/me/

[13/Aug/2026 00:39:57] "OPTIONS /api/token/refresh/ HTTP/1.1" 200 0

[13/Aug/2026 00:39:57] "GET /api/me/ HTTP/1.1" 401 172

[13/Aug/2026 00:39:58] "POST /api/token/refresh/ HTTP/1.1" 200 244

[13/Aug/2026 00:39:58] "POST /api/token/refresh/ HTTP/1.1" 200 244

[13/Aug/2026 00:39:58] "POST /api/token/refresh/ HTTP/1.1" 200 244

[13/Aug/2026 00:39:58] "POST /api/token/refresh/ HTTP/1.1" 200 244

[13/Aug/2026 00:39:58] "GET /api/me/ HTTP/1.1" 200 96

[13/Aug/2026 00:39:58] "GET /api/me/ HTTP/1.1" 200 96

[13/Aug/2026 00:39:58] "OPTIONS /api/carts/mine/ HTTP/1.1" 200 0

[13/Aug/2026 00:39:58] "GET /api/carts/657e794a-6cfc-455f-b66c-36c3392cbd95/ HTTP/1.1" 200 72

[13/Aug/2026 00:39:58] "GET /api/carts/657e794a-6cfc-455f-
```

<aside>
💡

### وضعیت فعلی

</aside>

از لاگ مشخص است:

- `POST /api/token/` → `200` ✅
- `GET /api/me/` → بعد از refresh → `200` ✅
- `GET /api/carts/mine/` → `200` ✅
- `GET /api/products/` → `200` ✅
- افزودن به Cart → `201` ✅
- تغییر تعداد → قبلاً `200` و الان هم مسیر Cart درست است ✅
- دریافت Address → `200` ✅
- ایجاد Order → `201` ✅
- دریافت Orders → `200` ✅

پس این بخش‌ها را **فعلاً دست نمی‌زنیم**.

> 222- در:
> 
> 
> ```
> backend/config/settings/base.py
> ```
> 
> کنار تنظیمات Static این قسمت را اضافه کن.
> 
> الان داری:
> 
> ```
> STATIC_URL = 'static/'
> ```
> 
> آن را به این تبدیل کن:
> 
> ```
> STATIC_URL = "static/"
> 
> MEDIA_URL = "media/"
> MEDIA_ROOT = BASE_DIR / "media"
> ```
> 
> یعنی:
> 
> ```
> # Static files
> STATIC_URL = "static/"
> 
> # Media files
> MEDIA_URL = "media/"
> MEDIA_ROOT = BASE_DIR / "media"
> ```
> 
> ```python
> 
> ```
> 

### چرا؟

`MEDIA_ROOT` می‌گوید:

> فایل‌های آپلودشده را روی دیسک کجا ذخیره کن.
> 

و:

`MEDIA_URL` می‌گوید:

> مرورگر با چه URLای به این فایل‌ها دسترسی داشته باشد.
> 

> 223- در `config/urls.py`
> 
> 
> بالای فایل، این import را اضافه کن:
> 
> ```
> from django.conf.urls.static import static
> ```
> 
> سپس **بعد از تعریف اصلی `urlpatterns`**، این را اضافه کن:
> 
> ```python
> if settings.DEBUG:
>     urlpatterns += static(
>         settings.MEDIA_URL,
>         document_root=settings.MEDIA_ROOT,
>     )
> ```
> 

### بنابراین انتهای `urls.py` باید تقریباً این شکلی شود

بخش فعلی تو:

```
if not settings.TESTING:
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns = [
        *urlpatterns,
    ] + debug_toolbar_urls()
```

را نگه دار.

و **بعد از آن**:

```
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
```

پس انتهای فایل:

```
if not settings.TESTING:
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns = [
        *urlpatterns,
    ] + debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
```

<aside>
💡

### یک نکته بسیار مهم

</aside>

بعد از این تغییر، Django باید فایل‌ها را واقعاً در:

```
backend/media/
```

داشته باشد.

یعنی بررسی کن آیا این مسیر وجود دارد:

```
backend/
├── apps/
├── config/
├── manage.py
├── media/
│   └── products/
│       └── main/
│           └── 2026/
│               └── 07/
│                   ...
```

### اگر `media/products/main/2026/07/` وجود ندارد

یعنی فایل‌هایی که در دیتابیس ثبت شده‌اند، احتمالاً روی Disk وجود ندارند.

در این حالت فقط تنظیم URL مشکل نیست؛ **خود فایل‌ها هم ممکن است گم شده باشند.**

> 224- سرور را Restart کن
> 
> 
> بعد از تغییرات:
> 
> ```
> CTRL + C
> ```
> 
> و دوباره:
> 
> ```
> python manage.py runserver
> ```
> 

<aside>
💡

### تست مستقیم

</aside>

> 226- بعد از اجرای Django، این URL را مستقیماً در مرورگر باز کن:
> 
> 
> ```
> http://127.0.0.1:8000/media/products/main/2026/07/apple-10-x-jpg.jpg
> ```
> 
> اگر تصویر باز شد:
> 
> **مشکل حل شده است.** ✅
> 

اگر دوباره `404` گرفتی، آن موقع مشخص می‌شود که فایل واقعاً در `MEDIA_ROOT` وجود ندارد.

1. اضافه کردن MEDIA_URL
↓
2. اضافه کردن MEDIA_ROOT
↓
3. اضافه کردن static(...) به [urls.py](http://urls.py/)
↓
4. Restart Django
↓
5. بررسی وجود فایل در backend/media/
↓
6. تست URL مستقیم تصویر
↓
7. تست Products در React

<aside>
💡

### چیزی که الان واقعاً داریم

</aside>

طبق مدل شما:

```
# Category
image = models.ImageField(
    upload_to='categories/%Y/%m/',
    blank=True,
    null=True
)

# Brand
image = models.ImageField(
    upload_to='brands/%Y/%m/',
    blank=True,
    null=True
)

# Product
main_image = models.ImageField(
    upload_to='products/main/%Y/%m/'
)
```

بنابراین Django کاملاً درست است که فایل‌ها را به شکل زیر ذخیره کند:

```
backend/
├── brands/
│   └── 2026/
│       └── 07/
│           ├── apple.png
│           ├── MicroSoft.png
│           └── Samsung.png
│
├── categories/
│   └── 2026/
│       └── 07/
│           ├── Digital_Products.jpg
│           └── surface.jpg
│
└── products/
    └── main/
        └── 2026/
            ├── 07/
            │   ├── apple-10-x-jpg.jpg
            │   └── Samsung-S24_-2.jpg
```

یعنی **سه مسیر مجزا** داریم و این کاملاً صحیح است:

```
brands/
categories/
products/
```

<aside>
💡

### اما خطای اصلی اینجاست

</aside>

لاگ Django می‌گوید:

```
Not Found: /products/main/2026/07/apple-10-x-jpg.jpg
```

و:

```
Not Found: /products/main/2026/07/Samsung-S24_-2.jpg
```

در حالی که `urls.py` فعلی شما فقط این مسیرها را دارد:

```
urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/carts/", ...),
    path("api/customers/", ...),
    path("api/products/", ...),
    path("api/orders/", ...),
    path("api/", ...),

    path("api/schema/", ...),
    path("api/docs/", ...),
    path("api/redoc/", ...),
]
```

**هیچ URLای برای Media File تعریف نشده است.**

پس Django وقتی مرورگر درخواست می‌کند:

```
/products/main/2026/07/apple-10-x-jpg.jpg
```

می‌گوید:

> من چنین URLای در `urlpatterns` ندارم.
> 

<aside>
💡

### تنظیم MEDIA_ROOT و MEDIA_URL

</aside>

> 227- در:
> 
> 
> ```
> backend/config/settings/base.py
> ```
> 
> بعد از:
> 
> ```
> STATIC_URL = 'static/'
> ```
> 
> این را اضافه کن:
> 
> ```
> # Media files
> MEDIA_URL = '/media/'
> MEDIA_ROOT = BASE_DIR
> ```
> 

### چرا `BASE_DIR`؟

ساختار فعلی پروژه‌ی تو نشان می‌دهد که فایل‌های آپلودی مستقیماً داخل `backend` قرار گرفته‌اند:

```
backend/
├── brands/
├── categories/
├── products/
├── apps/
├── config/
├── manage.py
└── ...
```

و:

```
BASE_DIR = Path(__file__).resolve().parent.parent.parent
```

در این پروژه همان مسیر `backend` است.

بنابراین:

```
MEDIA_ROOT = BASE_DIR
```

با ساختار فعلی تو سازگار است.

<aside>
💡

### قدم بعدی: بررسی خروجی API

</aside>

Backend را یک بار restart کن و این endpoint را باز کن:

```
http://127.0.0.1:8000/api/products/?page=1
```

در JSON مربوط به یکی از محصولات دنبال این قسمت بگرد:

```
{
    "id": 1,
    "name": "Apple ...",
    "main_image": "..."
}
```

### مقدار `main_image` باید چیزی شبیه این باشد:

```
http://127.0.0.1:8000/media/products/main/2026/07/apple-10-x-jpg.jpg
```

یا حداقل:

```
/media/products/main/2026/07/apple-10-x-jpg.jpg
```

**نباید** این باشد:

```
/products/main/2026/07/apple-10-x-jpg.jpg
```

---

## چرا این تست مهم است؟

لاگ قبلی ما نشان می‌داد مرورگر درخواست می‌فرستاده:

```
GET /products/main/2026/07/apple-10-x-jpg.jpg
```

در حالی که مسیر درست اکنون:

```
GET /media/products/main/2026/07/apple-10-x-jpg.jpg
```

است.

بنابراین الان باید ببینیم Backend بعد از اضافه کردن:

```
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR
```

چه URLای را داخل API تحویل React می‌دهد.

---

# اگر API مقدار درست را برگرداند

مثلاً:

```
"main_image": "http://127.0.0.1:8000/media/products/main/2026/07/apple-10-x-jpg.jpg"
```

آن وقت **هیچ تغییری در `ProductSerializer` لازم نیست.**

کد فعلی:

```
class ProductSerializer(serializers.ModelSerializer):
    ...
    main_image = ...
```

در واقع Django REST Framework خودش URL صحیح را تولید می‌کند.

و در React نیز:

```
<img
    src={product.main_image}
    alt={product.name}
/>
```

باید کار کند.

در این حالت مشکل احتمالاً browser cache یا frontend dev server است؛ یک Hard Refresh انجام می‌دهیم.

---

# اگر API هنوز این را برگرداند

```
/products/main/2026/07/apple-10-x-jpg.jpg
```

آن وقت مشکل در **Storage configuration** یا تنظیمات دیگری است و قبل از دست زدن به React آن را اصلاح می‌کنیم.

<aside>
📢

# پایان Part-21

</aside>