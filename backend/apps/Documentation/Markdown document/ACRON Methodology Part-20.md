# ACRON Methodology Part-20

<aside>
📢

در Part-19 ، **فاز 11:**    Frontend - Presentation Layer  تا قدم 181 توسعه داده شد

</aside>

# فاز 11**:**   Frontend - Presentation Layer

شروع قدم 182

---

<aside>
💡

### چرا Service جدا؟

</aside>

چون نمی‌خواهیم `Orders.jsx` مستقیماً با Axios صحبت کند.

معماری:

```
Orders.jsx
    ↓
orderService.js
    ↓
axiosInstance
    ↓
Django API
```

این همان روشی است که برای Product هم استفاده کرده‌ایم.

<aside>
💡

### یک نکته مهم درباره `Orders API`

</aside>

Backend ما:

```
def get_queryset(self):
    return Order.objects.filter(
        customer__user=self.request.user
    )
```

دارد.

این خیلی مهم است.

یعنی Frontend فقط می‌تواند:

```
Orders
   ↓
Current User's Orders
```

را بگیرد.

ما نمی‌خواهیم Frontend بتواند مثلاً:

```
/api/orders/<someone-else-order-id>/
```

را بخواند.

حتی اگر UUID سفارش شخص دیگری را داشته باشد، `get_queryset()` جلوی آن را می‌گیرد.

این یکی از موارد امنیتی خوبی است که الان اصولی انجام داده‌ایم.

<aside>
💡

#### قدم بعدی ما

</aside>

> 182- حالا `Orders.jsx`
> 
> 
> فایل:
> 
> ```
> frontend/src/pages/Orders.jsx
> ```
> 
> را فعلاً با این نسخه جایگزین کن:
> 
> ```python
> import { useEffect, useState } from "react";
> 
> import orderService from "../features/orders/services/orderService";
> 
> function Orders() {
>   const [orders, setOrders] = useState([]);
>   const [loading, setLoading] = useState(true);
>   const [error, setError] = useState("");
> 
>   useEffect(() => {
>     let isMounted = true;
> 
>     async function loadOrders() {
>       setLoading(true);
>       setError("");
> 
>       try {
>         const data = await orderService.getOrders();
> 
>         if (isMounted) {
>           setOrders(data);
>         }
>       } catch (err) {
>         console.error(
>           "Failed to load orders:",
>           err
>         );
> 
>         if (isMounted) {
>           setError(
>             "Unable to load your orders."
>           );
>         }
>       } finally {
>         if (isMounted) {
>           setLoading(false);
>         }
>       }
>     }
> 
>     loadOrders();
> 
>     return () => {
>       isMounted = false;
>     };
>   }, []);
> 
>   if (loading) {
>     return (
>       <main className="page">
>         <div className="page__container">
>           <div className="page__header">
>             <span className="page__eyebrow">
>               ACRON STORE
>             </span>
> 
>             <h1>Your Orders</h1>
> 
>             <p>
>               Loading your orders...
>             </p>
>           </div>
>         </div>
>       </main>
>     );
>   }
> 
>   if (error) {
>     return (
>       <main className="page">
>         <div className="page__container">
>           <div className="page__header">
>             <span className="page__eyebrow">
>               ACRON STORE
>             </span>
> 
>             <h1>Your Orders</h1>
> 
>             <p>{error}</p>
>           </div>
>         </div>
>       </main>
>     );
>   }
> 
>   return (
>     <main className="page">
>       <div className="page__container">
> 
>         <div className="page__header">
>           <span className="page__eyebrow">
>             ACRON STORE
>           </span>
> 
>           <h1>Your Orders</h1>
> 
>           <p>
>             Review your previous orders.
>           </p>
>         </div>
> 
>         {orders.length === 0 ? (
>           <div className="orders-empty">
>             <h2>No orders yet.</h2>
> 
>             <p>
>               Your completed orders will
>               appear here.
>             </p>
>           </div>
>         ) : (
>           <div className="orders-list">
> 
>             {orders.map((order) => (
>               <article
>                 key={order.id}
>                 className="order-card"
>               >
> 
>                 <div className="order-card__header">
> 
>                   <div>
>                     <span>
>                       Order
>                     </span>
> 
>                     <h2>
>                       {order.id}
>                     </h2>
>                   </div>
> 
>                   <span>
>                     {order.status}
>                   </span>
> 
>                 </div>
> 
>                 <div className="order-card__date">
>                   {new Date(
>                     order.created_at
>                   ).toLocaleString()}
>                 </div>
> 
>                 <div className="order-card__items">
> 
>                   {order.items.map((item) => (
>                     <div
>                       key={item.id}
>                       className="order-card__item"
>                     >
> 
>                       <div>
>                         <strong>
>                           {item.product_name}
>                         </strong>
> 
>                         <span>
>                           Quantity: {item.quantity}
>                         </span>
>                       </div>
> 
>                       <span>
>                         {item.unit_price}
>                       </span>
> 
>                     </div>
>                   ))}
> 
>                 </div>
> 
>                 <div className="order-card__total">
> 
>                   <span>
>                     Total
>                   </span>
> 
>                   <strong>
>                     {order.total_price}
>                   </strong>
> 
>                 </div>
> 
>               </article>
>             ))}
> 
>           </div>
>         )}
> 
>       </div>
>     </main>
>   );
> }
> 
> export default Orders;
> ```
> 

فعلاً عمداً وارد CSS و طراحی دقیق نمی‌شویم.

همان تصمیمی که درباره Cart گرفتیم:

> **Architecture first → UI polish later**
> 

---

<aside>
💡

### اما یک موضوع مهم داریم

</aside>

قبل از اینکه Checkout را بسازیم، باید **Orders API را از داخل React تست کنیم.**

> 183- سرور Frontend را اجرا کن:
> 
> 
> ```python
> npm run dev
> ```
> 

<aside>
💡

### چیزی که انتظار داریم

</aside>

تقریباً:

```
Your Orders

Order
1bc01589-7012-4d51-a80e-143d06328183

P

Samsung S24
Quantity: 3
12.00

موبایل اپل 10 X
Quantity: 2
10.00

Total
56.00
```

البته ظاهر فعلاً ساده خواهد بود و **قرار نیست الان UI را نهایی کنیم.**

---

<aside>
💡

### بعد از این مرحله چه می‌شود؟

</aside>

اگر `/orders` درست کار کرد، مسیرمان می‌شود:

```
Cart
  ↓
Orders API ✓
  ↓
Orders Page ← الان اینجا هستیم
  ↓
Checkout Page
  ↓
Address API
  ↓
Address Selection
  ↓
Create Order
  ↓
Payment
  ↓
Order Detail
```

و بعد از تکمیل این بخش‌ها، برمی‌گردیم سراغ همان **پنج موردی که گفتی**:

1. 🔴 Login
2. 🔴 Product Images
3. 🔴 Cart UI / Grid / Layout
4. 🔴 Security hardening
5. 🔴 Bug fixing / edge cases

پس فعلاً هیچ‌کدام را فراموش نکرده‌ایم؛ عمداً در Backlog نگه داشته‌ایم تا وسط معماری Domain-based پراکنده نشویم.

**فعلاً دو فایل Orders را ایجاد/تغییر بده و `/orders` را تست کن.**

<aside>
💡

نتیجه اگر این بود :

</aside>

```
D:/Repo/Django/acron/frontend/src/App.jsx:15:21
```

```
7  |  import Cart from "./pages/Cart";
8  |  import Orders from "./pages/Orders";
9  |  import Checkout from "./pages/Checkout";
   |                        ^
10 |  var _jsxFileName = "D:/Repo/Django/acron/frontend/src/App.jsx";
11 |  import { jsxDEV as _jsxDEV } from "react/jsx-dev-runtime";
```

```
    at TransformPluginContext._formatLog (file:///D:/Repo/Django/acron/frontend/node_modules/vite/dist/node/chunks/node.js:30416:39)
    at TransformPluginContext.error (file:///D:/Repo/Django/acron/frontend/node_modules/vite/dist/node/chunks/node.js:30413:14)
    at normalizeUrl (file:///D:/Repo/Django/acron/frontend/node_modules/vite/dist/node/chunks/node.js:27438:18)
    at async file:///D:/Repo/Django/acron/frontend/node_modules/vite/dist/node/chunks/node.js:27506:30
    at async Promise.all (index 8)
    at async TransformPluginContext.transform (file:///D:/Repo/Django/acron/frontend/node_modules/vite/dist/node/chunks/node.js:27474:4)
    at async EnvironmentPluginContainer.transform (file:///D:/Repo/Django/acron/frontend/node_modules/vite/dist/node/chunks/node.js:30201:14)
    at async loadAndTransform (file:///D:/Repo/Django/acron/frontend/node_modules/vite/dist/node/chunks/node.js:20124:26)
    at async viteTransformMiddleware (file:///D:/Repo/Django/acro
```

این خطا **مستقیماً مربوط به مرحله‌ای است که الان انجام دادیم نیست**؛ Vite دارد می‌گوید در `App.jsx` یک `Checkout` import شده، اما فایلش هنوز وجود ندارد.

خطای اصلی دقیقاً این است:

```
Failed to resolve import "./pages/Checkout"
```

و این خط:

```
import Checkout from "./pages/Checkout";
```

در `App.jsx` اضافه شده، در حالی که هنوز `Checkout.jsx` را نساخته‌ایم.

<aside>
💡

### چرا این اتفاق افتاده؟

</aside>

احتمالاً `App.jsx` الان چیزی شبیه این دارد:

```
import Cart from "./pages/Cart";
import Orders from "./pages/Orders";
import Checkout from "./pages/Checkout";
```

در حالی که ساختار فعلی تو هنوز:

```
pages/
├── Cart.jsx
├── Orders.jsx
├── Home.jsx
├── Login.jsx
├── Products.jsx
└── ProductDetail.jsx
```

است.

پس Vite نمی‌تواند این را پیدا کند:

```
pages/Checkout.jsx
```

<aside>
💡

### فعلاً Checkout را اضافه نکن

</aside>

چون طبق مسیر توسعه‌ای که با هم تعیین کردیم، **هنوز به Checkout نرسیده‌ایم**.

ما الان اینجا هستیم:

```
Cart
  ↓
Cart API                 ✓
  ↓
Cart Context             ✓
  ↓
Add to Cart              ✓
  ↓
Cart Page                ✓
  ↓
Quantity                 ✓
  ↓
Remove Item              ✓
  ↓
Cart Summary             ✓
  ↓
Orders API               ✓ Backend
  ↓
Orders Page              ← الان این مرحله
  ↓
Checkout
```

بنابراین `Checkout` نباید فعلاً وارد `App.jsx` شده باشد.

<aside>
💡

### `App.jsx` را اصلاح کن

</aside>

این خط را حذف کن:

```
import Checkout from "./pages/Checkout";
```

و اگر پایین‌تر Route مربوط به Checkout هم اضافه شده، آن را هم حذف کن:

```
<Route
  path="/checkout"
  element={<Checkout />}
/>
```

فعلاً App باید چیزی در این محدوده داشته باشد:

```
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

import Navbar from "./components/layout/Navbar";

import Home from "./pages/Home";
import Login from "./pages/Login";
import Products from "./pages/Products";
import ProductDetail from "./pages/ProductDetail";
import Cart from "./pages/Cart";
import Orders from "./pages/Orders";

function App() {
  return (
    <BrowserRouter>

      <Navbar />

      <Routes>

        <Route
          path="/"
          element={<Home />}
        />

        <Route
          path="/login"
          element={<Login />}
        />

        <Route
          path="/products"
          element={<Products />}
        />

        <Route
          path="/products/:slug"
          element={<ProductDetail />}
        />

        <Route
          path="/cart"
          element={<Cart />}
        />

        <Route
          path="/orders"
          element={<Orders />}
        />

      </Routes>

    </BrowserRouter>
  );
}

export default App;
```

بعد Vite باید خودش HMR انجام دهد؛ اگر نکرد:

```
npm run dev
```

را دوباره اجرا کن.

---

### یک نکته مهم

این بار **Checkout.jsx را برای رفع خطا نساز**.

چون این کار فقط برای ساکت کردن Vite است و با مسیر معماری ما هماهنگ نیست.

ما اول باید مطمئن شویم:

```
/orders
```

واقعاً Order ایجادشده در Backend را نمایش می‌دهد.

بعد می‌رویم سراغ:

```
Orders
   ↓
Checkout
```

و Checkout را وقتی بسازیم که واقعاً وارد آن مرحله شده باشیم.

**پس فعلاً فقط import و Route مربوط به Checkout را از `App.jsx` حذف کن و `/orders` را باز کن.**

فعلا امکان تست نیست چون امکان لاگین نیست. یعنی زمانی که یوزر sinaa رو با پسووردش میزنم این ارور را در کنسول مرورگر میگیرم:

```python
Failed to load resource: the server responded with a status of 401 (Unauthorized)
Orders.jsx:24 Failed to load orders: AxiosError: Request failed with status code 401
at async Object.getOrders (orderService.js:5:22)
at async loadOrders (Orders.jsx:18:22)
loadOrders	@	Orders.jsx:24
127.0.0.1:8000/api/orders/:1
Failed to load resource: the server responded with a status of 401 (Unauthorized)
Orders.jsx:24 Failed to load orders: AxiosError: Request failed with status code 401
at async Object.getOrders (orderService.js:5:22)
at async loadOrders (Orders.jsx:18:22)
loadOrders	@	Orders.jsx:24
login:1 [DOM] Input elements should have autocomplete attributes (suggested: "current-password"): (More info: https://goo.gl/9p2vKq)
127.0.0.1:8000/api/me/:1
Failed to load resource: the server responded with a status of 404 (Not Found)
Login.jsx:28 AxiosError: Request failed with status code 404
at async login (AuthContext.jsx:59:26)
at async handleSubmit (Login.jsx:24:7)
(anonymous)	@	Login.jsx:28
AuthContext.jsx:59
GET http://127.0.0.1:8000/api/me/ 404 (Not Found)
Promise.then
(anonymous)	@	AuthContext.jsx:59
await in (anonymous)
(anonymous)	@	Login.jsx:24
Login.jsx:28 AxiosError: Request failed with status code 404
at async login (AuthContext.jsx:59:26)
at async handleSubmit (Login.jsx:24:7)
(anonymous)	@	Login.jsx:28
```

الان مشکل اصلی `/orders` نیست؛ **احراز هویت Frontend هنوز کامل نشده** و به همین دلیل تست Orders هم معتبر نیست.

از خطاها می‌شود با اطمینان دو مشکل مشخص را جدا کرد:

<aside>
💡

### 1. مشکل اصلی Login

</aside>

این خط مهم‌ترین خطاست:

```
GET http://127.0.0.1:8000/api/me/ 404
```

در `AuthContext.jsx` داریم:

```
const userResponse = await axiosInstance.get("me/");
```

پس Frontend انتظار دارد این endpoint وجود داشته باشد:

```
GET /api/me/
```

اما در Backend، طبق کدی که فرستادی، endpoint مربوط به کاربر این است:

```
class CustomerMeView(APIView):
```

<aside>
💡

### چرا `/orders/` خطای 401 می‌دهد؟

</aside>

این هم نتیجه همان مشکل است.

Orders با این permission کار می‌کند:

```
permission_classes = [permissions.IsAuthenticated]
```

بنابراین بدون Access Token معتبر:

```
GET /api/orders/
        ↓
401 Unauthorized
```

کاملاً طبیعی است.

یعنی فعلاً **Orders را دستکاری نمی‌کنیم**.

---

## الان مسیر درست توسعه

ما باید موقتاً یک مرحله به عقب برگردیم و Authentication را درست کنیم:

```
Authentication
    ↓
Login
    ↓
GET /api/me/
    ↓
User authenticated
    ↓
Orders
    ↓
Checkout
```

و بعد از آن دوباره به Orders برمی‌گردیم.

این دقیقاً با تصمیم قبلی ما هم هماهنگ است: **Login یکی از مواردی است که قرار بود اصولی اصلاح شود، نه اینکه با راه‌حل موقتی از کنارش رد شویم.**

**مشکل از `config/urls.py` نیست.**

مسیر `/api/me/` واقعاً در `apps/api/urls.py` تعریف شده:

```
path('me/', views.me),
```

و با توجه به این خط:

```
path('api/', include('apps.api.urls')),
```

باید این endpoint وجود داشته باشد:

```
GET /api/me/
```

پس اینکه مرورگر می‌گوید:

```
GET /api/me/ → 404
```

احتمالاً مشکل داخل خود `apps/api/views.py` است، نه routing.

### یک نکته دیگر که باید فعلاً دست نزنیم

در `apps/api/urls.py` این‌ها را هم داریم:

```
path('', include('apps.carts.urls')),
path('', include('apps.orders.urls')),
```

در حالی که در `config/urls.py` قبلاً به‌صورت اختصاصی داریم:

```
path('api/carts/', include('apps.carts.urls')),
path('api/orders/', include('apps.orders.urls')),
```

این **تکراری و از نظر معماری تمیز نیست** و بعداً باید پاک‌سازی شود؛ اما فعلاً علت مستقیم `/api/me/` نیست.

همچنین:

```
path('customers/', include('apps.customers.urls')),
path('products/', include('apps.products.urls')),
```

نیز با URLهای مستقیم `config/urls.py` تکراری هستند.

پس فعلاً هیچ‌کدام را تغییر نمی‌دهیم تا Authentication را سالم کنیم.

علت مشکل تقریباً مشخص است. `views.py` از نظر تعریف `me` درست به نظر می‌رسد:

```
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):
    serializer = serializers.UserSerializer(request.user)
    return Response(serializer.data)
```

بنابراین **404 شدن `/api/me/` به احتمال زیاد از خود `me()` نیست**؛ اگر View اجرا شود ولی احراز هویت مشکل داشته باشد، انتظار `401` داریم، نه `404`.

اما یک نکته بسیار مهم‌تر پیدا کردیم.

### مشکل اصلی ساختار URL

در `config/urls.py` این را داریم:

```
path('api/', include('apps.api.urls')),
```

و داخل `apps/api/urls.py`:

```
path('me/', views.me),
```

پس مسیر `/api/me/` از نظر تئوری کاملاً صحیح است.

اما در همان `apps/api/urls.py` چند URL دیگر را هم دوباره include کرده‌ای:

```
path('', include('apps.carts.urls')),
path('', include('apps.orders.urls')),
path('customers/', include('apps.customers.urls')),
path('products/', include('apps.products.urls')),
```

در حالی که قبلاً در `config/urls.py` همین‌ها را مستقیم تعریف کرده‌ای.

این ساختار باید بعداً تمیز شود.

<aside>
💡

### یک تست خیلی مهم انجام بده

</aside>

> 184- حالا Backend در حال اجرا باشد و این دستور را در مرورگر باز کن:
> 
> 
> ```python
> http://127.0.0.1:8000/api/me/
> ```
> 

اگر با مرورگر بازش کنی، چون Authorization header ندارد، انتظار داریم:

```
{
    "detail": "Authentication credentials were not provided."
}
```

با status:

```
401 Unauthorized
```

اگر این اتفاق افتاد، یعنی URL `/api/me/` **وجود دارد** و routing درست است.

اما اگر:

```
404 Page not found
```

گرفتی، آن وقت مشکل routing است.

> 185- یک تست حتی بهتر
> 
> 
> در ترمینال backend اجرا کن:
> 
> ```
> python manage.py shell
> ```
> 
> بعد:
> 
> ```
> from django.urls import resolve
> 
> resolve("/api/me/")
> ```
> 

اگر مسیر درست باشد، باید چیزی شبیه این ببینی:

```
ResolverMatch(
    func=apps.api.views.me,
    ...
)
```

این تست خیلی دقیق‌تر از مرورگر است.

<aside>
💡

### یک مشکل دیگر هم داریم

</aside>

در `AuthContext.jsx` این کد را داریم:

```
const userResponse = await axiosInstance.get("me/");
```

و `axiosInstance` این را دارد:

```
baseURL: "http://127.0.0.1:8000/api/",
```

بنابراین:

```
"me/"
   +
"http://127.0.0.1:8000/api/"
   ↓
http://127.0.0.1:8000/api/me/
```

پس **Frontend هم URL را درست می‌سازد.**

بنابراین فعلاً `AuthContext.jsx` را تغییر نده.

```python
$ python manage.py shell

26 objects imported automatically (use -v 2 for details).
Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32

Type "help", "copyright", "credits" or "license" for more information.

(InteractiveConsole)

from django.urls import resolve

resolve("/api/me/")

ResolverMatch(func=apps.carts.views.CartViewSet, args=(), kwargs={'pk': 'me'}, url_name='carts-detail', app_names=[], namespaces=[], route='api/(?P[^/.]+)/$', captured_kwargs={'pk': 'me'})
```

خروجی کاملاً قطعی است:

```
ResolverMatch(
    func=apps.carts.views.CartViewSet,
    ...
    route='api/(?P[^/.]+)/$',
    captured_kwargs={'pk': 'me'}
)
```

یعنی Django اصلاً به این خط نمی‌رسد:

```
path('me/', views.me)
```

چرا؟

چون در `apps/api/urls.py` این خط را **قبل از `me/`** داریم:

```
path('', include('apps.carts.urls')),
```

و `CartViewSet` یک route عمومی دارد که `me` را به‌عنوان `pk` قبول می‌کند.

در نتیجه:

```
/api/me/
      ↓
apps.carts.urls
      ↓
CartViewSet
      ↓
me = pk
      ↓
404
```

این دقیقاً علت خطای Login توست.

<aside>
💡

### راه‌حل اصولی

</aside>

ما قبلاً در `config/urls.py` این‌ها را داریم:

```
path('api/carts/', include('apps.carts.urls')),
path('api/customers/', include('apps.customers.urls')),
path('api/products/', include('apps.products.urls')),
path('api/orders/', include('apps.orders.urls')),
```

بنابراین این موارد در `apps/api/urls.py` **تکراری هستند** و باید حذف شوند.

> 186- فایل:
> 
> 
> ```
> backend/apps/api/urls.py
> ```
> 
> را به این شکل تغییر بده:
> 
> ```python
> from django.urls import include, path
> 
> from rest_framework_simplejwt.views import (
>     TokenObtainPairView,
>     TokenRefreshView,
> )
> 
> from . import views
> 
> urlpatterns = [
>     # JWT Authentication
>     path(
>         'token/',
>         TokenObtainPairView.as_view(),
>         name='token_obtain_pair',
>     ),
> 
>     path(
>         'token/refresh/',
>         TokenRefreshView.as_view(),
>         name='token_refresh',
>     ),
> 
>     # Current authenticated user
>     path(
>         'me/',
>         views.me,
>         name='me',
>     ),
> 
>     # Other API domains
>     path(
>         '',
>         include('apps.advisor.urls'),
>     ),
> 
>     path(
>         'payments/',
>         include('apps.payments.urls'),
>     ),
> 
>     path(
>         'shipments/',
>         include('apps.shipments.urls'),
>     ),
> ]
> ```
> 

### این‌ها را عمداً حذف کردیم:

```
path('', include('apps.carts.urls')),
path('', include('apps.orders.urls')),
path('customers/', include('apps.customers.urls')),
path('products/', include('apps.products.urls')),
```

چون قبلاً در `config/urls.py` ثبت شده‌اند.

<aside>
💡

### چرا این ساختار بهتر است؟

</aside>

الان routing ما واضح‌تر می‌شود:

```
config/urls.py
│
├── /admin/
│
├── /api/carts/
│   └── carts
│
├── /api/customers/
│   └── customers
│
├── /api/products/
│   └── products
│
├── /api/orders/
│   └── orders
│
└── /api/
    │
    ├── token/
    ├── token/refresh/
    ├── me/
    ├── advisor/
    ├── payments/
    └── shipments/
```

این خیلی تمیزتر از این است که یک Domain را هم در `config/urls.py` و هم در `apps/api/urls.py` register کنیم.

---

# بعد از تغییر، هنوز Login را تست نکن

اول routing را تست کنیم.

> 187- در همان shell:
> 
> 
> ```
> python manage.py shell
> ```
> 
> و:
> 
> ```
> from django.urls import resolve
> ```
> 
> بعد:
> 
> ```
> resolve("/api/me/")
> ```
> 

این بار باید چیزی شبیه این ببینی:

```
ResolverMatch(
    func=apps.api.views.me,
    ...
    url_name='me',
    route='api/me/'
)
```

**اگر این خروجی را گرفتی، یعنی مشکل 404 را اصولی حل کرده‌ایم.**

> 188- سپس یک تست دوم
> 
> 
> این را اجرا کن:
> 
> ```
> resolve("/api/carts/")
> ```
> 
> باید به `CartViewSet` برسد
> 

و:

```
resolve("/api/orders/")
```

باید به `OrderViewSet` برسد.

این تست مهم است چون مطمئن می‌شویم با اصلاح `api/urls.py` چیزی از Cart و Orders خراب نشده است.

<aside>
💡

### بعد از آن

</aside>

وقتی این سه تست صحیح بودند:

```
/api/me/       → apps.api.views.me       ✓
/api/carts/    → CartViewSet              ✓
/api/orders/   → OrderViewSet             ✓
```

آن‌وقت می‌رویم سراغ Login در مرورگر.

اگر Login درست شد، این خط:

```
GET /api/orders/ → 401
```

هم باید از بین برود، چون `AuthContext` بالاخره می‌تواند کاربر را authenticate کند.

> from django.urls import resolve

resolve("/api/me/")

ResolverMatch(func=apps.carts.views.CartViewSet, args=(), kwargs={'pk': 'me'}, url_name='carts-detail', app_names=[], namespaces=[], route='api/(?P[^/.]+)/$', captured_kwargs={'pk': 'me'})

resolve("/api/carts/")

ResolverMatch(func=apps.carts.views.CartViewSet, args=(), kwargs={}, url_name='carts-list', app_names=[], namespaces=[], route='api/carts/$')

resolve("/api/orders/")

ResolverMatch(func=apps.orders.views.OrderViewSet, args=(), kwargs={}, url_name='orders-list', app_names=[], namespaces=[], route='api/orders/$')
> 

دقیقاً؛ این خروجی خیلی مهم است و نشان می‌دهد **هنوز مشکل حل نشده**، اما الان کاملاً می‌دانیم چرا.

سه تست:

```
/api/me/       → CartViewSet   ❌
/api/carts/    → CartViewSet   ✓
/api/orders/   → OrderViewSet  ✓
```

مشکل فقط `/api/me/` است.

### چرا هنوز `/api/me/` به Cart می‌رود؟

این خروجی:

```
route='api/(?P[^/.]+)/$'
```

یعنی هنوز در URLهای Django یک route عمومی Cart قبل از `me/` قرار دارد.

بنابراین تقریباً قطعی است که این خط هنوز در `backend/apps/api/urls.py` وجود دارد:

```
path('', include('apps.carts.urls')),
```

و همین خط `me` را به‌عنوان `pk` سبد خرید تفسیر می‌کند.

> 189- فایل:
> 
> 
> ```
> backend/apps/api/urls.py
> ```
> 
> را **کامل** به این تبدیل کن:
> 
> ```python
> from django.urls import include, path
> 
> from rest_framework_simplejwt.views import (
>     TokenObtainPairView,
>     TokenRefreshView,
> )
> 
> from . import views
> 
> urlpatterns = [
>     # JWT Authentication
>     path(
>         'token/',
>         TokenObtainPairView.as_view(),
>         name='token_obtain_pair',
>     ),
> 
>     path(
>         'token/refresh/',
>         TokenRefreshView.as_view(),
>         name='token_refresh',
>     ),
> 
>     # Current authenticated user
>     path(
>         'me/',
>         views.me,
>         name='me',
>     ),
> 
>     # Other API domains
>     path(
>         '',
>         include('apps.advisor.urls'),
>     ),
> 
>     path(
>         'payments/',
>         include('apps.payments.urls'),
>     ),
> 
>     path(
>         'shipments/',
>         include('apps.shipments.urls'),
>     ),
> ]
> ```
> 

### حتماً این ۴ خط را از `apps/api/urls.py` حذف کن:

```
path('', include('apps.carts.urls')),
path('', include('apps.orders.urls')),
path('customers/', include('apps.customers.urls')),
path('products/', include('apps.products.urls')),
```

چون این‌ها همین الان در `config/urls.py` ثبت شده‌اند:

```
path('api/carts/', include('apps.carts.urls')),
path('api/customers/', include('apps.customers.urls')),
path('api/products/', include('apps.products.urls')),
path('api/orders/', include('apps.orders.urls')),
```

---

<aside>
💡

### سپس یک نکته خیلی مهم

</aside>

چون داری `python manage.py shell` استفاده می‌کنی، بعد از تغییر فایل، **Shell قبلی را ببند**:

```python
exit()
```

دوباره:

```python
python manage.py shell
```

و تست کن:

```python
from django.urls import resolve

resolve("/api/me/")
```

<aside>
💡

### نتیجه‌ای که می‌خواهیم:

</aside>

باید چیزی شبیه این باشد:

```
ResolverMatch(
    func=apps.api.views.me,
    ...
    url_name='me',
    ...
)
```

دیگر نباید این را ببینیم:

```
func=apps.carts.views.CartViewSet
```

<aside>
💡

### سپس این دو مورد را هم تست کن:

</aside>

```
resolve("/api/carts/")
```

باید:

```
func=apps.carts.views.CartViewSet
```

باشد.

و:

```
resolve("/api/orders/")
```

باید:

```
func=apps.orders.views.OrderViewSet
```

باشد.

---

<aside>
💡

### نکته مهم معماری

</aside>

این اصلاح **هیچ ارتباطی با Migration ندارد**.

ما فقط URL routing را اصلاح می‌کنیم:

```
Database        → بدون تغییر
Models          → بدون تغییر
Migrations      → بدون تغییر
Cart API        → بدون تغییر
Orders API      → بدون تغییر

URL Routing     → اصلاح
Authentication  → بعد از آن تست
```

پس **`makemigrations` و `migrate` اصلاً لازم نیست.**

بعد از اینکه `resolve("/api/me/")` به `apps.api.views.me` رسید، مرحله بعدی این است که Login واقعی `sinaa` را تست کنیم. اگر آنجا مشکل بعدی وجود داشته باشد، همان را جداگانه بررسی می‌کنیم؛ فعلاً هیچ چیز دیگری را تغییر نمی‌دهیم.

> 190- فایل زیر را بساز
> 
> 
> ```
> frontend/src/features/orders/services/orderService.js
> ```
> 
> محتوای کامل:
> 
> ```python
> import apiClient from "../../../services/apiClient";
> 
> const orderService = {
>   // دریافت سفارش‌های کاربر جاری
>   getOrders: async () => {
>     const response = await apiClient.get("/orders/");
> 
>     // Django REST Framework ممکن است پاسخ paginated برگرداند:
>     // {
>     //   count: ...,
>     //   next: ...,
>     //   previous: ...,
>     //   results: [...]
>     // }
>     //
>     // یا در صورت غیرفعال بودن pagination مستقیماً آرایه برگرداند.
>     if (Array.isArray(response.data)) {
>       return response.data;
>     }
> 
>     if (Array.isArray(response.data?.results)) {
>       return response.data.results;
>     }
> 
>     return [];
>   },
> 
>   // دریافت یک سفارش مشخص
>   getOrder: async (orderId) => {
>     const response = await apiClient.get(`/orders/${orderId}/`);
>     return response.data;
>   },
> 
>   // ایجاد سفارش از روی سبد خرید
>   createOrder: async (cartId, addressId) => {
>     const response = await apiClient.post("/orders/", {
>       cart_id: cartId,
>       address_id: addressId,
>     });
> 
>     return response.data;
>   },
> 
>   // پرداخت یک سفارش
>   payOrder: async (orderId) => {
>     const response = await apiClient.post(
>       `/orders/${orderId}/pay/`
>     );
> 
>     return response.data;
>   },
> };
> 
> export default orderService;
> ```
> 

این مشکل `orders.map` را هم حل می‌کند:

در `Orders.jsx` این قسمت را داریم:

```
const data = await orderService.getOrders();

setOrders(data);
```

و بعد:

```
orders.map(...)
```

بنابراین `getOrders()` **حتماً باید یک Array برگرداند**.

اگر Django پاسخ pagination بدهد:

```
{
    "count": 16,
    "next": null,
    "previous": null,
    "results": [...]
}
```

کد بالا فقط این قسمت را برمی‌گرداند:

```
response.data.results
```

در نتیجه:

```
orders
```

واقعاً آرایه خواهد بود و:

```
orders.map(...)
```

بدون خطا اجرا می‌شود.

<aside>
💡

### یک نکته مهم درباره Checkout

</aside>

من در `createOrder` عمداً این را گذاشتم:

```
{
  cart_id: cartId,
  address_id: addressId,
}
```

چون طبق تغییراتی که اخیراً روی `OrderService` انجام دادیم، ثبت سفارش دیگر نباید فقط یک `shipping_address` متنی دریافت کند؛ باید از **Address واقعی مشتری** استفاده کنیم و اطلاعات آدرس هنگام ایجاد Order در فیلدهای shipping سفارش Freeze شوند.

این با تستی که خودت انجام دادی هم هماهنگ است:

```
order.shipping_city
order.shipping_receiver_name
order.shipping_phone_number
order.shipping_province
order.shipping_street
order.shipping_postal_code
```

و همچنین:

```
OrderItem.unit_price
```

قیمت را در لحظه ثبت سفارش نگه می‌دارد.

> 191- بعد از ساخت `orderService.js`، سرور Vite را اگر لازم شد restart کن:
> 
> 
> ```
> npm run dev
> ```
> 
> سپس وارد:
> 
> ```
> http://localhost:5173/orders
> ```
> 
> شو.
> 

**الان Orders Domain در فرانت‌اند عملاً درست کار می‌کند.** ✅

- `GET /api/orders/` با موفقیت انجام شده.
- سفارش‌ها از Backend دریافت می‌شوند.
- `OrderItem`ها درست نمایش داده می‌شوند.
- `quantity` درست است.
- `unit_price` درست از سفارش خوانده می‌شود.
- `total_price` درست محاسبه شده؛ مثلاً:
    - `3 × 12 + 2 × 10 = 56`
    - `2 × 12 + 3 × 10 = 54`
- وضعیت‌های `P` و `C` هم از Backend دریافت می‌شوند.
- مشکل `orders.map is not a function` هم برطرف شده.

<aside>
💡

### وضعیت فعلی مسیر توسعه ACRON

</aside>

ما الان تقریباً این مرحله را داریم:

```
Cart Domain
    ↓
Cart API
    ↓
Cart Context
    ↓
Add to Cart
    ↓
Cart Page
    ↓
Quantity / Remove
    ↓
Orders Backend
    ↓
OrderService
    ↓
Address Snapshot
    ↓
Price Snapshot
    ↓
Orders API
    ↓
Orders Frontend   ✅
    ↓
Checkout          ← مرحله بعد
    ↓
Authentication Hardening
    ↓
Bug & Security Review
    ↓
UI / Images / Cart Design
```

بنابراین پیشنهاد من این است که **الان ظاهر Orders و Cart را هم دست نزنیم.** عملکرد و معماری مهم‌تر است و بعداً یک مرحله مشخص برای UI/UX انجام می‌دهیم.

### یک نکته مهم

کدهای فعلی نشان می‌دهند که بخش مهمی از منطق سفارش واقعاً درست طراحی شده:

**Cart حذف می‌شود، ولی Order باقی می‌ماند و قیمت و اطلاعات ارسال خودش را نگه می‌دارد.**

این دقیقاً همان رفتاری است که از یک سیستم فروشگاهی انتظار داریم.

پس مرحله بعدی را می‌بریم روی:

> **Checkout Domain → انتخاب آدرس → خلاصه سفارش → ایجاد Order → انتقال به Payment**
> 

و بعد از تکمیل آن، سراغ آن **۵ موردی که قرار گذاشتیم در پایان بررسی و اصلاح کنیم** می‌رویم.

الان وضعیت ما این است:

```
Cart                         ✅
Cart API / Context           ✅
Add / Update / Remove        ✅
Order Backend                ✅
OrderService                 ✅
Price Snapshot               ✅
Shipping Snapshot            ✅
Orders API                   ✅
Orders Frontend              ✅
────────────────────────────────
Checkout                     ← الان اینجا هستیم
Payment                      ← بعد از Checkout
Authentication Hardening
Security / Bug Review
UI / Images / Styling
```

مشکل Login که داشتیم را هم فعلاً **حل‌شده فرض نمی‌کنیم**؛ آن را در مرحله‌ی Authentication Hardening برمی‌گردانیم و اصولی اصلاح می‌کنیم. همین‌طور سه مشکل قبلی UI/تصاویر و موارد امنیتی را فعلاً دست نمی‌زنیم.

<aside>
💡

### قدم بعدی: Checkout

</aside>

در Checkout باید این جریان را بسازیم:

```
Cart
  ↓
Checkout
  ↓
دریافت Addressهای کاربر
  ↓
انتخاب Address
  ↓
نمایش محصولات و قیمت‌ها
  ↓
نمایش Total
  ↓
Confirm Order
  ↓
POST /api/orders/
  ↓
Order با وضعیت PENDING
  ↓
Payment
```

اما قبل از اینکه کد جدید بسازیم، یک نکته مهم داریم: **Backend فعلی Order را با `address_id` طراحی کرده‌ایم** و تست Shell تو هم نشان داد که Address به‌درستی داخل Order snapshot شده است.

پس Checkout باید دقیقاً بر اساس همین قرارداد Backend ساخته شود، نه اینکه دوباره `shipping_address` متنی بسازیم.

حالا Checkout را **مرحله‌به‌مرحله و Domain-based** می‌سازیم:

1. `checkoutService.js`
2. دریافت Addressها
3. ساخت `Checkout.jsx`
4. انتخاب آدرس
5. خلاصه Cart
6. ایجاد Order
7. هدایت به Payment

و هر مرحله را تست می‌کنیم و بعد می‌رویم مرحله بعد.

وضعیت کاملاً مشخص است. `Checkout` هنوز وارد Router نشده، که اتفاقاً خوب است؛ چون اول خود Checkout را می‌سازیم و بعد Route را فعال می‌کنیم.

از اینجا به بعد **مرحله Checkout Domain** را شروع می‌کنیم.

<aside>
💡

### مرحله 1 — ساخت Serviceهای Checkout

</aside>

برای Checkout دو API لازم داریم:

```
GET  /api/customers/addresses/
POST /api/orders/
```

یعنی:

```
Checkout
   │
   ├── Addresses → Customer API
   │
   └── Create Order → Orders API
```

> 192- این پوشه را بساز
> 
> 
> اگر وجود ندارد:
> 
> ```python
> frontend/src/features/checkout/
> ```
> 

> 193- داخل پوشه:
> 
> 
> ```python
> frontend/src/features/checkout/
> └── services/
>     └── checkoutService.js
> ```
> 

> 194- فایل `checkoutService.js` را بساز:
> 
> 
> ```python
> import apiClient from "../../../services/apiClient";
> 
> const checkoutService = {
>   // دریافت آدرس‌های مشتری جاری
>   getAddresses: async () => {
>     const response = await apiClient.get("/customers/addresses/");
> 
>     if (Array.isArray(response.data)) {
>       return response.data;
>     }
> 
>     if (Array.isArray(response.data?.results)) {
>       return response.data.results;
>     }
> 
>     return [];
>   },
> 
>   // ثبت سفارش جدید بر اساس سبد خرید و آدرس انتخاب‌شده
>   createOrder: async (cartId, addressId) => {
>     const response = await apiClient.post("/orders/", {
>       cart_id: cartId,
>       address_id: addressId,
>     });
> 
>     return response.data;
>   },
> };
> 
> export default checkoutService;
> ```
> 

<aside>
💡

### چرا این Service جداست؟

</aside>

نمی‌خواهیم `Checkout.jsx` مستقیماً با Axios صحبت کند.

ساختار ما همچنان Domain-based است:

```
Checkout.jsx
     │
     ↓
checkoutService.js
     │
     ↓
apiClient.js
     │
     ↓
Django API
```

این همان الگوی `Orders` است که الان با موفقیت کار می‌کند:

```
Orders.jsx
     ↓
orderService.js
     ↓
apiClient.js
     ↓
/api/orders/
```

<aside>
💡

### یک نکته مهم قبل از ساخت Checkout

</aside>

ما برای Checkout باید Cart فعلی را داشته باشیم.

`CartContext` که قبلاً ساختیم این اطلاعات را در اختیارمان می‌گذارد:

```
cart
loading
totalItemsCount
addToCart
updateQuantity
removeFromCart
refreshCart
```

بنابراین صفحه Checkout قرار نیست دوباره Cart را از Backend به شکل مستقل مدیریت کند.

ساختار نهایی:

```
                 Checkout
                    │
          ┌─────────┴─────────┐
          ↓                   ↓
      useCart()        checkoutService
          │                   │
          ↓             ┌─────┴─────┐
      Cart Data         ↓           ↓
                    Addresses    Create Order
                        │           │
                        └─────┬─────┘
                              ↓
                           Django
```

---

## اما یک نکته معماری مهم پیدا کردم

در `main.jsx` که قبلاً ساختیم ، فعلاً این را داریم:

```
<AuthProvider>
  <App />
</AuthProvider>
```

ولی `CartProvider` در `main.jsx` قرار ندارد.

یعنی:

```
AuthProvider
    └── App
```

داریم، اما:

```
CartProvider
```

در Provider tree دیده نمی‌شود.

در حالی که `Cart.jsx` و Checkout به `useCart()` نیاز دارند.

**قبل از ساخت Checkout باید این را درست کنیم**، وگرنه ممکن است با خطای:

```
useCart() ... null
```

یا رفتارهای عجیب Cart مواجه شویم.

فعلاً **صفحه‌آرایی، تصاویر و Login را دست نمی‌زنیم**.

### مرحله بعد: Checkout Domain

الان Backend ما برای ثبت سفارش آماده است و `OrderService.place_order()` عملاً این جریان را انجام می‌دهد:

**Cart → انتخاب Address → ساخت Order → انتقال CartItem به OrderItem → Freeze Price → حذف Cart**

بنابراین قدم بعدی در Frontend این است که صفحه Checkout را بسازیم.

اما یک نکته مهم: چون در `App.jsx` فعلاً Checkout را کامنت کرده‌ای، ابتدا خود فایل را می‌سازیم و **هنوز Route را فعال نمی‌کنیم**.

> 195- فایل زیر را بساز:
> 
> 
> `frontend/src/pages/Checkout.jsx`
> 
> ```python
> import { useEffect, useState } from "react";
> import { Link, useNavigate } from "react-router-dom";
> 
> import cartService from "../features/cart/services/cartService";
> import orderService from "../features/orders/services/orderService";
> 
> function Checkout() {
>   const navigate = useNavigate();
> 
>   const [cart, setCart] = useState(null);
>   const [addresses, setAddresses] = useState([]);
> 
>   const [selectedAddressId, setSelectedAddressId] = useState("");
> 
>   const [loading, setLoading] = useState(true);
>   const [submitting, setSubmitting] = useState(false);
> 
>   const [error, setError] = useState("");
> 
>   useEffect(() => {
>     let isMounted = true;
> 
>     async function loadCheckoutData() {
>       setLoading(true);
>       setError("");
> 
>       try {
>         const [cartData, addressData] = await Promise.all([
>           cartService.getCart(),
>           fetchAddresses(),
>         ]);
> 
>         if (!isMounted) {
>           return;
>         }
> 
>         setCart(cartData);
>         setAddresses(addressData);
> 
>         const defaultAddress = addressData.find(
>           (address) => address.is_default
>         );
> 
>         if (defaultAddress) {
>           setSelectedAddressId(
>             String(defaultAddress.id)
>           );
>         }
>       } catch (err) {
>         console.error(
>           "Failed to load checkout data:",
>           err
>         );
> 
>         if (isMounted) {
>           setError(
>             "Unable to load checkout information."
>           );
>         }
>       } finally {
>         if (isMounted) {
>           setLoading(false);
>         }
>       }
>     }
> 
>     async function fetchAddresses() {
>       const response = await fetch(
>         "http://127.0.0.1:8000/api/customers/addresses/",
>         {
>           headers: {
>             Authorization: `Bearer ${localStorage.getItem(
>               "access_token"
>             )}`,
>           },
>         }
>       );
> 
>       if (!response.ok) {
>         throw new Error(
>           "Failed to load addresses."
>         );
>       }
> 
>       return response.json();
>     }
> 
>     loadCheckoutData();
> 
>     return () => {
>       isMounted = false;
>     };
>   }, []);
> 
>   async function handlePlaceOrder() {
>     if (!selectedAddressId) {
>       setError(
>         "Please select a shipping address."
>       );
>       return;
>     }
> 
>     if (!cart?.id) {
>       setError(
>         "Your cart could not be found."
>       );
>       return;
>     }
> 
>     setSubmitting(true);
>     setError("");
> 
>     try {
>       const order = await orderService.createOrder({
>         cart_id: cart.id,
>         address_id: Number(selectedAddressId),
>       });
> 
>       navigate("/orders");
>     } catch (err) {
>       console.error(
>         "Failed to create order:",
>         err
>       );
> 
>       setError(
>         "Unable to place your order."
>       );
>     } finally {
>       setSubmitting(false);
>     }
>   }
> 
>   if (loading) {
>     return (
>       <main className="page">
>         <div className="page__container">
>           <div className="page__header">
>             <span className="page__eyebrow">
>               ACRON STORE
>             </span>
> 
>             <h1>Checkout</h1>
> 
>             <p>
>               Loading checkout information...
>             </p>
>           </div>
>         </div>
>       </main>
>     );
>   }
> 
>   if (error && !cart) {
>     return (
>       <main className="page">
>         <div className="page__container">
>           <div className="page__header">
>             <span className="page__eyebrow">
>               ACRON STORE
>             </span>
> 
>             <h1>Checkout</h1>
> 
>             <p>{error}</p>
> 
>             <Link to="/cart">
>               Back to cart
>             </Link>
>           </div>
>         </div>
>       </main>
>     );
>   }
> 
>   if (!cart?.items?.length) {
>     return (
>       <main className="page">
>         <div className="page__container">
>           <div className="page__header">
>             <span className="page__eyebrow">
>               ACRON STORE
>             </span>
> 
>             <h1>Your cart is empty</h1>
> 
>             <p>
>               Add products to your cart before
>               checking out.
>             </p>
> 
>             <Link to="/products">
>               Continue shopping
>             </Link>
>           </div>
>         </div>
>       </main>
>     );
>   }
> 
>   return (
>     <main className="page">
>       <div className="page__container">
> 
>         <div className="page__header">
>           <span className="page__eyebrow">
>             ACRON STORE
>           </span>
> 
>           <h1>Checkout</h1>
> 
>           <p>
>             Review your order and select a
>             shipping address.
>           </p>
>         </div>
> 
>         {error && (
>           <div className="checkout-error">
>             {error}
>           </div>
>         )}
> 
>         <section className="checkout">
> 
>           <div className="checkout__address">
> 
>             <h2>
>               Shipping address
>             </h2>
> 
>             {addresses.length === 0 ? (
>               <div className="checkout__no-address">
>                 <p>
>                   You do not have a shipping
>                   address yet.
>                 </p>
> 
>                 <Link to="/profile">
>                   Add an address
>                 </Link>
>               </div>
>             ) : (
>               <div className="checkout__addresses">
> 
>                 {addresses.map((address) => (
>                   <label
>                     key={address.id}
>                     className="checkout__address-card"
>                   >
>                     <input
>                       type="radio"
>                       name="shipping-address"
>                       value={address.id}
>                       checked={
>                         selectedAddressId ===
>                         String(address.id)
>                       }
>                       onChange={(event) =>
>                         setSelectedAddressId(
>                           event.target.value
>                         )
>                       }
>                     />
> 
>                     <div>
>                       <strong>
>                         {address.title ||
>                           "Address"}
>                       </strong>
> 
>                       <p>
>                         {address.receiver_name}
>                       </p>
> 
>                       <p>
>                         {address.province},{" "}
>                         {address.city}
>                       </p>
> 
>                       <p>
>                         {address.street}
>                       </p>
> 
>                       <p>
>                         {address.postal_code}
>                       </p>
>                     </div>
>                   </label>
>                 ))}
> 
>               </div>
>             )}
> 
>           </div>
> 
>           <div className="checkout__summary">
> 
>             <h2>
>               Order summary
>             </h2>
> 
>             <div className="checkout__items">
> 
>               {cart.items.map((item) => (
>                 <div
>                   key={item.id}
>                   className="checkout__item"
>                 >
>                   <div>
>                     <strong>
>                       {item.product_name}
>                     </strong>
> 
>                     <span>
>                       Quantity: {item.quantity}
>                     </span>
>                   </div>
> 
>                   <span>
>                     {item.subtotal}
>                   </span>
>                 </div>
>               ))}
> 
>             </div>
> 
>             <div className="checkout__total">
>               <span>
>                 Total
>               </span>
> 
>               <strong>
>                 {cart.total_price}
>               </strong>
>             </div>
> 
>             <button
>               type="button"
>               className="checkout__button"
>               disabled={
>                 submitting ||
>                 !selectedAddressId ||
>                 addresses.length === 0
>               }
>               onClick={handlePlaceOrder}
>             >
>               {submitting
>                 ? "Placing order..."
>                 : "Place order"}
>             </button>
> 
>           </div>
> 
>         </section>
> 
>       </div>
>     </main>
>   );
> }
> 
> export default Checkout;
> ```
> 

این مرحله مهم است چون می‌خواهیم زنجیره زیر کاملاً تمیز و قابل تست باشد:

```
Cart
  ↓
Checkout
  ↓
Address
  ↓
POST /api/orders/
  ↓
OrderViewSet
  ↓
OrderService
  ↓
Order + OrderItem
  ↓
Cart حذف می‌شود
  ↓
Orders
```

قرارداد فعلی دقیقاً این است:

```
POST /api/orders/
```

با Body:

```
{
  "cart_id": "UUID",
  "address_id": 3
}
```

و Backend خودش:

- مالکیت Cart را بررسی می‌کند.
- خالی نبودن Cart را بررسی می‌کند.
- مالکیت Address را بررسی می‌کند.
- اطلاعات Address را داخل Order به‌صورت Snapshot ذخیره می‌کند.
- قیمت محصول را داخل `OrderItem.unit_price` Freeze می‌کند.
- Cart را بعد از موفقیت حذف می‌کند.

این قسمت از معماری خوب است. **دستش نمی‌زنیم.**

### حالا قدم بعدی

قبل از ساخت Checkout باید Frontend Service را با این قرارداد هماهنگ کنیم.

الان وضعیت ما این است:

- `OrderSerializer` اطلاعات Snapshot آدرس را برمی‌گرداند.
- `OrderService.place_order()` مالکیت Cart و Address را بررسی می‌کند.
- `orderService.js` برای ساخت Order، `cart_id` و `address_id` می‌فرستد.
- صفحه `Orders.jsx` سفارش‌ها را دریافت و نمایش می‌دهد.
- مسیر `/orders/` هم در Backend درست resolve می‌شود.

### قدم بعدی

الان منطقی‌ترین مرحله در همان مسیر Domain-based، رفتن به **Checkout** است؛ چون Backend برای ایجاد سفارش آماده است ولی Frontend هنوز صفحه Checkout را ندارد.

جریان موردنظرمان:

```
Cart
  ↓
Checkout
  ↓
Select Address
  ↓
Create Order
  ↓
Order Detail / Orders
  ↓
Pay
```

اما قبل از اینکه Checkout را بسازیم، یک نکته مهم وجود دارد: **احراز هویت هنوز کاملاً سالم نیست** و قبلاً `/api/me/` باعث `404` می‌شد. ما نباید این مشکل را با یک راه‌حل موقتی دور بزنیم.

بنابراین من پیشنهاد می‌کنم دقیقاً این ترتیب را ادامه بدهیم:

1. **Authentication / `/api/me/` را اصولی اصلاح کنیم**
2. تست Login با `sinaa`
3. تست دریافت Cart
4. ساخت Checkout
5. انتخاب Address
6. ارسال `cart_id + address_id`
7. ایجاد Order
8. نمایش Order ایجادشده
9. اتصال Payment
10. سپس برگردیم سراغ آن **۵ موردی که عمداً عقب انداختیم**:
- Login / Authentication
- تصاویر محصولات
- UI و Grid صفحات
- امنیت
- Bug fixing / hardening

نکته مهم این است که **الان نباید وارد CSS و زیباسازی شویم**؛ چون خودمان تصمیم گرفتیم ابتدا جریان اصلی فروشگاه را کامل کنیم.

پس قدم بعدی: **رفع اصولی مشکل `/api/me/` و Authentication** است، نه ساخت Checkout هنوز.

الان اول باید مشکل `401 / 404` احراز هویت را کامل کنیم، چون تا Authentication درست نباشد Checkout را تست‌کردن معنی ندارد.

<aside>
💡

### مرحله ۱ — پیدا کردن علت `/api/me/`

</aside>

ما قبلاً این را داشتیم:

```
GET /api/me/
404 Not Found
```

و با `resolve()` مشخص شد:

```
resolve("/api/me/")
→ apps.carts.views.CartViewSet
→ kwargs={'pk': 'me'}
→ route='api/(?P<...>[^/.]+)/$'
```

یعنی `/api/me/` **قبل از رسیدن به `apps.api.urls` توسط مسیر Cart گرفته می‌شود.**

علت اصلی همین ساختار در `backend/apps/api/urls.py` است:

```
path('', include('apps.carts.urls')),
```

و احتمالاً همین includeهای قدیمی باعث شده‌اند مسیرهای عمومی داخل `api/` با مسیرهای جدید تداخل داشته باشند.

ما در `config/urls.py` مسیرهای اختصاصی را جدا کرده‌ایم:

```
path('api/carts/', include('apps.carts.urls')),
path('api/customers/', include('apps.customers.urls')),
path('api/products/', include('apps.products.urls')),
path('api/orders/', include('apps.orders.urls')),
```

بنابراین دیگر نباید دوباره `carts` و `orders` را از داخل `apps.api.urls` وارد کنیم.

> 196- فایل`apps/api/urls.py` را اصلاح کن:
> 
> 
> ```
> backend/apps/api/urls.py
> ```
> 
> را به این شکل دربیاور:
> 
> ```python
> from django.urls import include, path
> 
> from rest_framework_simplejwt.views import (
>     TokenObtainPairView,
>     TokenRefreshView,
> )
> 
> from . import views
> 
> urlpatterns = [
>     # JWT Authentication
>     path(
>         "token/",
>         TokenObtainPairView.as_view(),
>         name="token_obtain_pair",
>     ),
> 
>     path(
>         "token/refresh/",
>         TokenRefreshView.as_view(),
>         name="token_refresh",
>     ),
> 
>     # Protected current-user endpoint
>     path(
>         "me/",
>         views.me,
>         name="api-me",
>     ),
> 
>     # Other API domains
>     path(
>         "payments/",
>         include("apps.payments.urls"),
>     ),
> 
>     path(
>         "shipments/",
>         include("apps.shipments.urls"),
>     ),
> 
>     path(
>         "advisor/",
>         include("apps.advisor.urls"),
>     ),
> ]
> ```
> 

این قسمت‌ها را عمداً حذف کردیم:

```
path('', include('apps.carts.urls')),
path('', include('apps.orders.urls')),
path('customers/', include('apps.customers.urls')),
path('products/', include('apps.products.urls')),
```

چون الان این Domainها در `config/urls.py` به‌صورت مستقیم ثبت شده‌اند.

یعنی معماری URL ما می‌شود:

```
/api/
│
├── token/
├── token/refresh/
├── me/
│
├── carts/
├── customers/
├── products/
├── orders/
│
├── payments/
├── shipments/
└── advisor/
```

این ساختار خیلی تمیزتر است.

> 197- فایل `config/urls.py`
> 
> 
> ```
> backend/config/urls.py
> ```
> 
> باید تقریباً این ساختار را داشته باشد:
> 
> ```python
> from django.contrib import admin
> from django.urls import include, path
> 
> from drf_spectacular.views import (
>     SpectacularAPIView,
>     SpectacularSwaggerView,
>     SpectacularRedocView,
> )
> 
> from django.conf import settings
> 
> urlpatterns = [
>     path("admin/", admin.site.urls),
> 
>     # -------------------------
>     # Domain APIs
>     # -------------------------
> 
>     path(
>         "api/carts/",
>         include("apps.carts.urls"),
>     ),
> 
>     path(
>         "api/customers/",
>         include("apps.customers.urls"),
>     ),
> 
>     path(
>         "api/products/",
>         include("apps.products.urls"),
>     ),
> 
>     path(
>         "api/orders/",
>         include("apps.orders.urls"),
>     ),
> 
>     # -------------------------
>     # General API
>     # -------------------------
> 
>     path(
>         "api/",
>         include("apps.api.urls"),
>     ),
> 
>     # -------------------------
>     # API Documentation
>     # -------------------------
> 
>     path(
>         "api/schema/",
>         SpectacularAPIView.as_view(),
>         name="schema",
>     ),
> 
>     path(
>         "api/docs/",
>         SpectacularSwaggerView.as_view(
>             url_name="schema"
>         ),
>         name="swagger-ui",
>     ),
> 
>     path(
>         "api/redoc/",
>         SpectacularRedocView.as_view(
>             url_name="schema"
>         ),
>         name="redoc",
>     ),
> ]
> 
> if not settings.TESTING:
>     from debug_toolbar.toolbar import debug_toolbar_urls
> 
>     urlpatterns = [
>         *urlpatterns,
>     ] + debug_toolbar_urls()
> ```
> 

<aside>
💡

### یک نکته مهم درباره ترتیب URLها

</aside>

در Django ترتیب `urlpatterns` اهمیت دارد.

الان:

```
api/carts/
api/customers/
api/products/
api/orders/
api/
```

داریم.

پس وقتی Django می‌بیند:

```
/api/me/
```

دیگر با:

```
api/carts/
```

match نمی‌شود.

بعد می‌رود سراغ:

```
api/
```

و وارد:

```
apps.api.urls
```

می‌شود.

آنجا:

```
path("me/", views.me)
```

آن را می‌گیرد.

بنابراین:

```
/api/me/
        ↓
config/urls.py
        ↓
api/
        ↓
apps.api.urls
        ↓
me/
        ↓
views.me
```

و دیگر نباید به `CartViewSet` برسد.

> 198- سرور Django را restart کن
> 
> 
> سرور را متوقف کن:
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

> 199- بعد وارد shell شو:
> 
> 
> ```
> python manage.py shell
> ```
> 
> و این تست را انجام بده:
> 
> ```
> from django.urls import resolve
> 
> resolve("/api/me/")
> ```
> 

<aside>
💡

### نتیجه‌ای که می‌خواهیم ببینیم

</aside>

باید چیزی شبیه این باشد:

```
ResolverMatch(
    func=apps.api.views.me,
    ...
    route='api/me/'
)
```

و **دیگر نباید** این را ببینیم:

```
apps.carts.views.CartViewSet
```

این نتیجه **دقیقاً همان چیزی است که می‌خواستیم**:

```
ResolverMatch(
    func=apps.api.views.me,
    ...
    route='api/me/'
)
```

پس مشکل قبلی Route Conflict کاملاً برطرف شده است. `/api/me/` دیگر به `CartViewSet` نمی‌رود و مستقیماً به `apps.api.views.me` می‌رسد.

<aside>
💡

### مرحله بعد: تست خود Authentication

</aside>

حالا هنوز Frontend را تغییر نمی‌دهیم. اول Backend را مستقل تست می‌کنیم تا مشخص شود مشکل Login واقعاً کجاست.

> 200- در همان Django shell این‌ها را اجرا کن:
> 
> 
> ```python
> from django.contrib.auth import get_user_model
> 
> User = get_user_model()
> 
> user = User.objects.get(username="sinaa")
> 
> user.check_password("PASSWORD")
> ```
> 

به جای:

```
PASSWORD
```

**پسورد واقعی `sinaa`** را وارد کن.

اگر نتیجه:

```
True
```

بود، یعنی username/password درست است.

اگر:

```
False
```

بود، یعنی مشکل از credential است و فعلاً سراغ Frontend نمی‌رویم.

### بعد از آن، Token endpoint را تست می‌کنیم

اگر `check_password()` برابر `True` شد،

> 201- در مرورگر یا Postman/Thunder Client این endpoint را تست کن:
> 
> 
> ```
> POST http://127.0.0.1:8000/api/token/
> ```
> 
> Body:
> 
> ```
> {
>     "username": "sinaa",
>     "password": "PASSWORD"
> }
> ```
> 

باید چیزی شبیه این بگیری:

```
{
    "refresh": "...",
    "access": "..."
}
```

اگر این مرحله موفق شد، یعنی:

```
User
 ↓
Password
 ↓
JWT
```

کاملاً سالم است.

بعد با `access` token، endpoint زیر را تست می‌کنیم:

```
GET http://127.0.0.1:8000/api/me/
```

با Header:

```
Authorization: Bearer YOUR_ACCESS_TOKEN
```

و باید اطلاعات کاربر برگردد.

---

<aside>
💡

### چرا این ترتیب مهم است؟

</aside>

چون الان نمی‌خواهیم دوباره حدس بزنیم که مشکل از React است یا Axios یا JWT یا Django.

مرحله‌به‌مرحله مشخص می‌کنیم:

```
1. Password      ← الان
2. /api/token/   ← بعد
3. /api/me/      ← بعد
4. AuthContext   ← بعد
5. Login.jsx     ← بعد
6. Orders        ← بعد
7. Checkout      ← بعد
```

یک نکته مهم داریم که باید قبل از ادامه اصلاحش کنیم.

<aside>
💡

### چیزی که الان درست است

</aside>

درخواست‌ها از این مسیر می‌روند:

```
Login
  ↓
access_token در localStorage
  ↓
apiClient
  ↓
Request Interceptor
  ↓
Authorization: Bearer <access_token>
  ↓
Django
```

و Refresh Token هم به شکل مناسبی جداگانه با `axios.post()` درخواست می‌شود.

### اما یک مشکل معماری داریم

این قسمت:

```
const accessToken = localStorage.getItem("access_token");
```

خودش مشکلی ندارد، اما باید ببینیم **Login واقعاً توکن‌ها را با همین نام‌ها ذخیره می‌کند یا نه**.

چون `apiClient` انتظار دارد دقیقاً این دو کلید وجود داشته باشند:

```
access_token
refresh_token
```

اگر `AuthContext.jsx` مثلاً از نام دیگری استفاده کند، درخواست `/api/me/` بدون Authorization ارسال می‌شود و نتیجه همان `401` خواهد بود.

فایل AuthContext.jsx از این استفاده می‌کند:

```
import axiosInstance from "../api/axiosInstance";
```

اما فایلی که قبل‌تر بررسی کردیم یعنی:

```
frontend/src/services/apiClient.js
```

اصلاً در `AuthContext` استفاده نمی‌شود.

یعنی الان پروژه **دو Axios instance جداگانه** دارد:

```
AuthContext
    ↓
api/axiosInstance.js
```

ولی بقیه بخش‌های پروژه مثل Orders:

```
orderService
    ↓
services/apiClient.js
```

این معماری می‌تواند دقیقاً باعث شود Authentication بین قسمت‌های مختلف پروژه یکسان رفتار نکند.

### یک نکته دیگر

در `AuthContext` این درخواست‌ها:

```
axiosInstance.post("token/")
axiosInstance.get("me/")
```

باید ببینید `axiosInstance` چه `baseURL` و چه interceptorهایی دارد.

در حالی که `apiClient.js` ما این‌ها را دارد:

```
/api
Request Interceptor
Authorization Bearer
Refresh Token
401 handling
```

پس قبل از اینکه چیزی را تغییر دهیم، باید `axiosInstance` را بررسی کنیم.

**مشکل معماری Authentication را دقیقاً پیدا کردیم.**

ما دو Axios instance داریم که تقریباً یک کار را انجام می‌دهند:

```
frontend/src/api/axiosInstance.js
frontend/src/services/apiClient.js
```

و هر دو JWT، refresh token و interceptor دارند. این کار لازم نیست و در ادامه می‌تواند باعث رفتارهای متفاوت و باگ‌های سخت‌تری شود.

### تصمیم معماری

از اینجا به بعد فقط **یک HTTP client مرکزی** داشته باشیم:

```
frontend/src/services/apiClient.js
```

و تمام Domainها از آن استفاده کنند:

```
AuthContext
Products
Cart
Orders
Checkout
Payments
...
       ↓
apiClient.js
       ↓
Django API
```

این با همان Domain-based architecture که داریم جلو می‌رویم سازگارتر است.

<aside>
💡

### اما هنوز فایل را حذف نکن

</aside>

> 202- اول `AuthContext.jsx` را به `apiClient` منتقل می‌کنیم.
> 
> 
> در:
> 
> ```
> frontend/src/context/AuthContext.jsx
> ```
> 
> این:
> 
> ```
> import axiosInstance from "../api/axiosInstance";
> ```
> 
> را تبدیل کن به:
> 
> ```
> import apiClient from "../services/apiClient";
> ```
> 

> 203- سپس تمام استفاده‌های:
> 
> 
> ```
> axiosInstance
> ```
> 
> را به:
> 
> ```
> apiClient
> ```
> 
> تغییر بده.
> 

عنی این بخش‌ها:

```
await axiosInstance.get("me/");
```

و:

```
await axiosInstance.post(
  "token/",
  {
    username,
    password,
  }
);
```

باید بشوند:

```
await apiClient.get("/me/");
```

و:

```
await apiClient.post("/token/", {
  username,
  password,
});
```

### چرا `/` را اضافه کردم؟

`apiClient` این را دارد:

```
baseURL = "http://127.0.0.1:8000/api"
```

بنابراین:

```
apiClient.get("/me/")
```

درخواست را به اینجا می‌فرستد:

```
http://127.0.0.1:8000/api/me/
```

و:

```
apiClient.post("/token/")
```

می‌شود:

```
http://127.0.0.1:8000/api/token/
```

---

### فعلاً `axiosInstance.js` را حذف نکن

بعد از این تغییر، پروژه را اجرا می‌کنیم و Login را تست می‌کنیم.

اگر همه‌چیز درست شد، آن‌وقت:

```
frontend/src/api/axiosInstance.js
```

دیگر استفاده‌ای نخواهد داشت و حذفش می‌کنیم.

<aside>
💡

### این ترتیب مهم است؛ نمی‌خواهم همزمان چند تغییر انجام دهیم و اگر چیزی خراب شد، ندانیم علتش کدام تغییر بوده.

</aside>

```python

$ python manage.py runserver

Watching for file changes with StatReloader

Performing system checks...

System check identified no issues (0 silenced).

August 11, 2026 - 19:22:21

Django version 6.0.7, using settings 'config.settings'

Starting development server at http://127.0.0.1:8000/

Quit the server with CTRL-BREAK.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.

For more information on production servers see: https://docs.djangoproject.com/en/6.0/howto/deployment/

[11/Aug/2026 19:22:46] "POST /api/carts/ HTTP/1.1" 201 72

[11/Aug/2026 19:22:46] "POST /api/carts/ HTTP/1.1" 201 72

[11/Aug/2026 19:23:05] "OPTIONS /api/token/ HTTP/1.1" 200 0

[11/Aug/2026 19:23:08] "POST /api/token/ HTTP/1.1" 200 489

[11/Aug/2026 19:23:08] "OPTIONS /api/me/ HTTP/1.1" 200 0

[11/Aug/2026 19:23:08] "GET /api/me/ HTTP/1.1" 200 96

[11/Aug/2026 19:23:08] "OPTIONS /api/carts/mine/ HTTP/1.1" 200 0

[11/Aug/2026 19:23:08] "GET /api/carts/mine/ HTTP/1.1" 200 72

[11/Aug/2026 19:23:14] "OPTIONS /api/orders/ HTTP/1.1" 200 0

[11/Aug/2026 19:23:14] "OPTIONS /api/orders/ HTTP/1.1" 200 0

[11/Aug/2026 19:23:15] "GET /api/orders/ HTTP/1.1" 200 4934

[11/Aug/2026 19:23:15] "GET /api/orders/ HTTP/1.1" 200 4934

[11/Aug/2026 19:23:19] "OPTIONS /api/products/?page=1 HTTP/1.1" 200 0

[11/Aug/2026 19:23:19] "OPTIONS /api/products/?page=1 HTTP/1.1" 200 0

C:\Users\sina.virtualenvs\backend-TBakwqam\Lib\site-packages\rest_framework\pagination.py:198: UnorderedObjectListWarning: Pagination may yield inconsistent results with an unordered object_list: <class 'apps.products.models.Product'> QuerySet.

paginator = self.django_paginator_class(queryset, page_size)

[11/Aug/2026 19:23:19] "GET /api/products/?page=1 HTTP/1.1" 200 2439

[11/Aug/2026 19:23:19] "GET /api/products/?page=1 HTTP/1.1" 200 2439

Not Found: /products/main/2026/07/apple-10-x-jpg.jpg

[11/Aug/2026 19:23:19] "GET /products/main/2026/07/apple-10-x-jpg.jpg HTTP/1.1" 404 18008

Not Found: /products/main/2026/07/Samsung-S24_-2.jpg

[11/Aug/2026 19:23:19] "GET /products/main/2026/07/Samsung-S24_-2.jpg HTTP/1.1" 404 18008
```

**الان وضعیت پروژه کاملاً روشن است و می‌توانیم دقیقاً از همان مسیر Domain-based ادامه بدهیم.**

لاگ‌ها نشان می‌دهند بخش‌های اصلی که روی آن‌ها کار کردیم فعلاً درست کار می‌کنند:

- JWT Login → `200`
- `/api/me/` → `200`
- Cart → `200`
- Orders → `200`
- Products → `200`
- سفارش‌ها در Frontend نمایش داده می‌شوند.
- مشکل قبلی `401` و `404 /api/me/` حل شده است.

دو موردی که عمداً فعلاً دست نمی‌زنیم:

1. ❗ تصاویر محصولات → `404`
2. ⚠️ هشدار Pagination برای `Product.objects` که `order_by()` ندارد.

این‌ها همان مواردی هستند که بعداً در مرحله‌ی **Bug Fix / Hardening** برمی‌گردیم.

<aside>
💡

### قدم بعدی: Checkout Domain

</aside>

الان از نظر مسیر منطقی پروژه اینجا هستیم:

```
Cart
  ↓
Cart API
  ↓
Cart Context
  ↓
Add to Cart
  ↓
Cart Page
  ↓
Quantity / Remove
  ↓
Order API
  ↓
Order Service
  ↓
Order Snapshot
  ↓
Orders Page
  ↓
>>> Checkout
  ↓
Payment
  ↓
Authentication Hardening
  ↓
Image Fix
  ↓
UI / Layout
  ↓
Security & Bug Fix
```

و Backend ما برای Checkout تقریباً آماده است، چون `OrderService.place_order()` اکنون این کارها را انجام می‌دهد:

- بررسی Customer
- بررسی Cart
- بررسی مالکیت Cart
- بررسی خالی نبودن Cart
- بررسی مالکیت Address
- Snapshot کردن آدرس
- Freeze کردن قیمت محصول
- ساخت `OrderItem`
- حذف Cart
- ساخت Order با وضعیت `PENDING`

بنابراین **نباید دوباره منطق سفارش را در Frontend بنویسیم.**

قدم بعدی این است که Checkout را به این جریان وصل کنیم:

```
Cart Page
   ↓
Proceed to Checkout
   ↓
Checkout Page
   ↓
Load user's addresses
   ↓
Select address
   ↓
Review cart/order
   ↓
Place Order
   ↓
POST /api/orders/
   ↓
Order created
   ↓
Order Detail / Orders
```

**فعلاً ظاهر Checkout را ساده نگه می‌داریم.** هدف این مرحله اتصال صحیح:

`Cart → Address → Create Order → Orders`

است، نه صفحه‌آرایی نهایی.

<aside>
💡

### مرحله ۱ — ساخت Customer Service

</aside>

> 204- این فایل را بساز:
> 
> 
> `frontend/src/features/customers/services/customerService.js`
> 
> ```python
> import apiClient from "../../../services/apiClient";
> 
> const customerService = {
>   // دریافت آدرس‌های کاربر جاری
>   getAddresses: async () => {
>     const response = await apiClient.get("/customers/addresses/");
> 
>     if (Array.isArray(response.data)) {
>       return response.data;
>     }
> 
>     if (Array.isArray(response.data?.results)) {
>       return response.data.results;
>     }
> 
>     return [];
>   },
> };
> 
> export default customerService;
> ```
> 

ساختار دایرکتوری هم این می‌شود:

```
frontend/src/features/
├── cart/
├── orders/
├── products/
└── customers/
    └── services/
        └── customerService.js
```

<aside>
💡

### مرحله ۲ — ساخت Checkout

</aside>

> 205- حالا این فایل را بساز:
> 
> 
> `frontend/src/pages/Checkout.jsx`
> 
> ```python
> import { useEffect, useState } from "react";
> import { Link, useNavigate } from "react-router-dom";
> 
> import { useCart } from "../context/CartContext";
> import customerService from "../features/customers/services/customerService";
> import orderService from "../features/orders/services/orderService";
> 
> function Checkout() {
>   const navigate = useNavigate();
> 
>   const { cart, loading: cartLoading } = useCart();
> 
>   const [addresses, setAddresses] = useState([]);
>   const [selectedAddressId, setSelectedAddressId] = useState("");
> 
>   const [loadingAddresses, setLoadingAddresses] = useState(true);
>   const [submitting, setSubmitting] = useState(false);
> 
>   const [error, setError] = useState("");
> 
>   useEffect(() => {
>     let isMounted = true;
> 
>     async function loadAddresses() {
>       setLoadingAddresses(true);
>       setError("");
> 
>       try {
>         const data = await customerService.getAddresses();
> 
>         if (!isMounted) {
>           return;
>         }
> 
>         setAddresses(data);
> 
>         // اگر آدرس پیش‌فرض وجود داشته باشد،
>         // به صورت خودکار انتخاب می‌شود.
>         const defaultAddress = data.find(
>           (address) => address.is_default
>         );
> 
>         if (defaultAddress) {
>           setSelectedAddressId(
>             String(defaultAddress.id)
>           );
>         } else if (data.length > 0) {
>           setSelectedAddressId(
>             String(data[0].id)
>           );
>         }
>       } catch (err) {
>         console.error(
>           "Failed to load addresses:",
>           err
>         );
> 
>         if (isMounted) {
>           setError(
>             "Unable to load your addresses."
>           );
>         }
>       } finally {
>         if (isMounted) {
>           setLoadingAddresses(false);
>         }
>       }
>     }
> 
>     loadAddresses();
> 
>     return () => {
>       isMounted = false;
>     };
>   }, []);
> 
>   if (cartLoading) {
>     return (
>       <main className="page">
>         <div className="page__container">
>           <div className="page__header">
>             <span className="page__eyebrow">
>               ACRON STORE
>             </span>
> 
>             <h1>Checkout</h1>
> 
>             <p>
>               Loading your cart...
>             </p>
>           </div>
>         </div>
>       </main>
>     );
>   }
> 
>   const items = cart?.items || [];
> 
>   if (items.length === 0) {
>     return (
>       <main className="page">
>         <div className="page__container">
>           <div className="page__header">
>             <span className="page__eyebrow">
>               ACRON STORE
>             </span>
> 
>             <h1>Checkout</h1>
> 
>             <p>
>               Your cart is empty.
>             </p>
>           </div>
> 
>           <Link to="/products">
>             Continue Shopping
>           </Link>
>         </div>
>       </main>
>     );
>   }
> 
>   const handlePlaceOrder = async () => {
>     if (!selectedAddressId) {
>       setError(
>         "Please select a shipping address."
>       );
>       return;
>     }
> 
>     if (!cart?.id) {
>       setError(
>         "Your cart could not be identified."
>       );
>       return;
>     }
> 
>     setSubmitting(true);
>     setError("");
> 
>     try {
>       const order = await orderService.createOrder(
>         cart.id,
>         Number(selectedAddressId)
>       );
> 
>       navigate(`/orders/${order.id}`);
>     } catch (err) {
>       console.error(
>         "Failed to create order:",
>         err
>       );
> 
>       setError(
>         err.response?.data?.detail ||
>           "Unable to create your order."
>       );
>     } finally {
>       setSubmitting(false);
>     }
>   };
> 
>   return (
>     <main className="page">
>       <div className="page__container">
> 
>         <div className="page__header">
>           <span className="page__eyebrow">
>             ACRON STORE
>           </span>
> 
>           <h1>Checkout</h1>
> 
>           <p>
>             Select your shipping address and
>             review your order.
>           </p>
>         </div>
> 
>         {error && (
>           <div className="checkout__error">
>             {error}
>           </div>
>         )}
> 
>         <section className="checkout">
> 
>           <div className="checkout__addresses">
> 
>             <h2>
>               Shipping Address
>             </h2>
> 
>             {loadingAddresses ? (
>               <p>
>                 Loading addresses...
>               </p>
>             ) : addresses.length === 0 ? (
>               <div>
>                 <p>
>                   You don't have any shipping
>                   addresses yet.
>                 </p>
> 
>                 <p>
>                   Please add an address before
>                   placing your order.
>                 </p>
>               </div>
>             ) : (
>               <div>
>                 {addresses.map((address) => (
>                   <label
>                     key={address.id}
>                     className="checkout__address"
>                   >
>                     <input
>                       type="radio"
>                       name="shipping_address"
>                       value={address.id}
>                       checked={
>                         selectedAddressId ===
>                         String(address.id)
>                       }
>                       onChange={(event) =>
>                         setSelectedAddressId(
>                           event.target.value
>                         )
>                       }
>                     />
> 
>                     <div>
>                       <strong>
>                         {address.title ||
>                           "Address"}
>                       </strong>
> 
>                       <p>
>                         {address.receiver_name}
>                       </p>
> 
>                       <p>
>                         {address.province},{" "}
>                         {address.city}
>                       </p>
> 
>                       <p>
>                         {address.street}
>                       </p>
> 
>                       <p>
>                         {address.postal_code}
>                       </p>
> 
>                       <p>
>                         {address.phone_number}
>                       </p>
> 
>                       {address.is_default && (
>                         <span>
>                           Default address
>                         </span>
>                       )}
>                     </div>
>                   </label>
>                 ))}
>               </div>
>             )}
> 
>           </div>
> 
>           <aside className="checkout__summary">
> 
>             <h2>
>               Order Summary
>             </h2>
> 
>             <div className="checkout__items">
> 
>               {items.map((item) => (
>                 <div
>                   key={item.id}
>                   className="checkout__item"
>                 >
>                   <div>
>                     <strong>
>                       {item.product?.name}
>                     </strong>
> 
>                     <span>
>                       Quantity: {item.quantity}
>                     </span>
>                   </div>
> 
>                   <span>
>                     {item.total_price}
>                   </span>
>                 </div>
>               ))}
> 
>             </div>
> 
>             <div className="checkout__total">
>               <span>
>                 Total
>               </span>
> 
>               <strong>
>                 {cart.total_price}
>               </strong>
>             </div>
> 
>             <button
>               type="button"
>               className="checkout__place-order"
>               onClick={handlePlaceOrder}
>               disabled={
>                 submitting ||
>                 loadingAddresses ||
>                 addresses.length === 0 ||
>                 !selectedAddressId
>               }
>             >
>               {submitting
>                 ? "Placing Order..."
>                 : "Place Order"}
>             </button>
> 
>             <Link to="/cart">
>               Back to Cart
>             </Link>
> 
>           </aside>
> 
>         </section>
> 
>       </div>
>     </main>
>   );
> }
> 
> export default Checkout;
> ```
> 

<aside>
💡

### **مرحله ۳ — اتصال Cart به Checkout**

</aside>

> 206- در `Cart.jsx` فقط دکمه فعلی را تغییر می‌دهیم.
> 
> 
> الان این قسمت را داری:
> 
> ```
> <button
>   type="button"
>   className="cart__checkout-button"
> >
>   Proceed to Checkout
> </button>
> ```
> 
> آن را با این جایگزین کن:
> 
> ```
> <Link
>   to="/checkout"
>   className="cart__checkout-button"
> >
>   Proceed to Checkout
> </Link>
> ```
> 

دلیلش ساده است: Checkout یک **Route** مستقل است و با `Link` وارد آن می‌شویم. فعلاً لازم نیست برای این کار Context یا state جدیدی ایجاد کنیم.

<aside>
💡

### مرحله ۴ — اضافه کردن Route

</aside>

> 207- حالا در `App.jsx` کامنت Checkout را بردار و import را فعال کن:
> 
> 
> ```
> import Checkout from "./pages/Checkout";
> ```
> 
> و بعد از Route مربوط به Cart این Route را اضافه کن:
> 
> ```
> <Route
>   path="/checkout"
>   element={<Checkout />}
> />
> ```
> 

در نتیجه بخش مربوط به مسیرها باید تقریباً این شکلی باشد:

```
<Route
  path="/cart"
  element={<Cart />}
/>

<Route
  path="/checkout"
  element={<Checkout />}
/>

<Route
  path="/orders"
  element={<Orders />}
/>
```

---

<aside>
💡

### یک نکته بسیار مهم در مورد `navigate`

</aside>

من در Checkout بعد از ایجاد سفارش این را گذاشتم:

```
navigate(`/orders/${order.id}`);
```

اما **ما هنوز صفحه Order Detail را نساخته‌ایم**.

> 208- پس فعلاً این قسمت را به:
> 
> 
> ```
> navigate("/orders");
> ```
> 
> تغییر بده.
> 
> یعنی بعد از ثبت موفق سفارش:
> 
> ```
> const order = await orderService.createOrder(
>   cart.id,
>   Number(selectedAddressId)
> );
> 
> navigate("/orders");
> ```
> 

> 209- این نسخه با `apiClient.js`، `orderService.js` و `CartContext` فعلی پروژه هماهنگ است.
> 
> 
> ```python
> import { useEffect, useState } from "react";
> import { Link, useNavigate } from "react-router-dom";
> 
> import { useCart } from "../context/CartContext";
> import customerService from "../features/customers/services/customerService";
> import orderService from "../features/orders/services/orderService";
> 
> function Checkout() {
>   const navigate = useNavigate();
> 
>   const {
>     cart,
>     loading: cartLoading,
>   } = useCart();
> 
>   const [addresses, setAddresses] = useState([]);
>   const [selectedAddressId, setSelectedAddressId] =
>     useState("");
> 
>   const [loadingAddresses, setLoadingAddresses] =
>     useState(true);
> 
>   const [submitting, setSubmitting] =
>     useState(false);
> 
>   const [error, setError] = useState("");
> 
>   useEffect(() => {
>     let isMounted = true;
> 
>     async function loadAddresses() {
>       setLoadingAddresses(true);
>       setError("");
> 
>       try {
>         const data =
>           await customerService.getAddresses();
> 
>         if (!isMounted) {
>           return;
>         }
> 
>         setAddresses(data);
> 
>         const defaultAddress = data.find(
>           (address) => address.is_default
>         );
> 
>         if (defaultAddress) {
>           setSelectedAddressId(
>             String(defaultAddress.id)
>           );
>         } else if (data.length > 0) {
>           setSelectedAddressId(
>             String(data[0].id)
>           );
>         }
>       } catch (err) {
>         console.error(
>           "Failed to load addresses:",
>           err
>         );
> 
>         if (isMounted) {
>           setError(
>             "Unable to load your addresses."
>           );
>         }
>       } finally {
>         if (isMounted) {
>           setLoadingAddresses(false);
>         }
>       }
>     }
> 
>     loadAddresses();
> 
>     return () => {
>       isMounted = false;
>     };
>   }, []);
> 
>   const handlePlaceOrder = async () => {
>     if (!selectedAddressId) {
>       setError(
>         "Please select a shipping address."
>       );
>       return;
>     }
> 
>     if (!cart?.id) {
>       setError(
>         "Your cart could not be identified."
>       );
>       return;
>     }
> 
>     setSubmitting(true);
>     setError("");
> 
>     try {
>       const order =
>         await orderService.createOrder(
>           cart.id,
>           Number(selectedAddressId)
>         );
> 
>       console.log(
>         "Order created successfully:",
>         order
>       );
> 
>       navigate("/orders");
>     } catch (err) {
>       console.error(
>         "Failed to create order:",
>         err
>       );
> 
>       setError(
>         err.response?.data?.detail ||
>           "Unable to place your order."
>       );
>     } finally {
>       setSubmitting(false);
>     }
>   };
> 
>   if (cartLoading || loadingAddresses) {
>     return (
>       <main className="page">
>         <div className="page__container">
> 
>           <div className="page__header">
> 
>             <span className="page__eyebrow">
>               ACRON STORE
>             </span>
> 
>             <h1>
>               Checkout
>             </h1>
> 
>             <p>
>               Loading checkout information...
>             </p>
> 
>           </div>
> 
>         </div>
>       </main>
>     );
>   }
> 
>   const items = cart?.items || [];
> 
>   if (items.length === 0) {
>     return (
>       <main className="page">
>         <div className="page__container">
> 
>           <div className="page__header">
> 
>             <span className="page__eyebrow">
>               ACRON STORE
>             </span>
> 
>             <h1>
>               Your cart is empty
>             </h1>
> 
>             <p>
>               Add products to your cart
>               before checking out.
>             </p>
> 
>             <Link to="/products">
>               Continue shopping
>             </Link>
> 
>           </div>
> 
>         </div>
>       </main>
>     );
>   }
> 
>   return (
>     <main className="page">
> 
>       <div className="page__container">
> 
>         <div className="page__header">
> 
>           <span className="page__eyebrow">
>             ACRON STORE
>           </span>
> 
>           <h1>
>             Checkout
>           </h1>
> 
>           <p>
>             Review your order and select
>             a shipping address.
>           </p>
> 
>         </div>
> 
>         {error && (
>           <div className="checkout-error">
>             {error}
>           </div>
>         )}
> 
>         <section className="checkout">
> 
>           <div className="checkout__address">
> 
>             <h2>
>               Shipping address
>             </h2>
> 
>             {addresses.length === 0 ? (
>               <div className="checkout__no-address">
> 
>                 <p>
>                   You do not have a shipping
>                   address yet.
>                 </p>
> 
>                 <p>
>                   Please add an address before
>                   placing your order.
>                 </p>
> 
>               </div>
>             ) : (
>               <div className="checkout__addresses">
> 
>                 {addresses.map((address) => (
>                   <label
>                     key={address.id}
>                     className="checkout__address-card"
>                   >
> 
>                     <input
>                       type="radio"
>                       name="shipping-address"
>                       value={address.id}
>                       checked={
>                         selectedAddressId ===
>                         String(address.id)
>                       }
>                       onChange={(event) =>
>                         setSelectedAddressId(
>                           event.target.value
>                         )
>                       }
>                     />
> 
>                     <div>
> 
>                       <strong>
>                         {address.title ||
>                           "Address"}
>                       </strong>
> 
>                       <p>
>                         {address.receiver_name}
>                       </p>
> 
>                       <p>
>                         {address.province},{" "}
>                         {address.city}
>                       </p>
> 
>                       <p>
>                         {address.street}
>                       </p>
> 
>                       <p>
>                         {address.postal_code}
>                       </p>
> 
>                       <p>
>                         {address.phone_number}
>                       </p>
> 
>                       {address.is_default && (
>                         <span>
>                           Default address
>                         </span>
>                       )}
> 
>                     </div>
> 
>                   </label>
>                 ))}
> 
>               </div>
>             )}
> 
>           </div>
> 
>           <div className="checkout__summary">
> 
>             <h2>
>               Order summary
>             </h2>
> 
>             <div className="checkout__items">
> 
>               {items.map((item) => (
>                 <div
>                   key={item.id}
>                   className="checkout__item"
>                 >
> 
>                   <div>
> 
>                     <strong>
>                       {item.product?.name ||
>                         item.product_name}
>                     </strong>
> 
>                     <span>
>                       Quantity: {item.quantity}
>                     </span>
> 
>                   </div>
> 
>                   <span>
>                     {item.total_price ||
>                       item.subtotal}
>                   </span>
> 
>                 </div>
>               ))}
> 
>             </div>
> 
>             <div className="checkout__total">
> 
>               <span>
>                 Total
>               </span>
> 
>               <strong>
>                 {cart.total_price}
>               </strong>
> 
>             </div>
> 
>             <button
>               type="button"
>               className="checkout__button"
>               disabled={
>                 submitting ||
>                 !selectedAddressId ||
>                 addresses.length === 0
>               }
>               onClick={handlePlaceOrder}
>             >
>               {submitting
>                 ? "Placing order..."
>                 : "Place order"}
>             </button>
> 
>             <Link to="/cart">
>               Back to cart
>             </Link>
> 
>           </div>
> 
>         </section>
> 
>       </div>
> 
>     </main>
>   );
> }
> 
> export default Checkout;
> ```
> 

<aside>
💡

### یک فایل جدید هم لازم است

</aside>

> 210-  این فایل را ایجاد کن:
> 
> 
> `frontend/src/features/customers/services/customerService.js`
> 
> ```python
> import apiClient from "../../../services/apiClient";
> 
> const customerService = {
>   getAddresses: async () => {
>     const response = await apiClient.get(
>       "/customers/addresses/"
>     );
> 
>     if (Array.isArray(response.data)) {
>       return response.data;
>     }
> 
>     if (Array.isArray(response.data?.results)) {
>       return response.data.results;
>     }
> 
>     return [];
>   },
> };
> 
> export default customerService;
> ```
> 

این انتخاب فعلاً درست‌تر است، چون `Orders.jsx` موجود است و سفارش جدید را نمایش خواهد داد.

---

<aside>
💡

### حالا چه چیزی ساخته‌ایم؟

</aside>

مسیر توسعه فعلی ACRON تبدیل شده به:

```
Products
   ↓
Add to Cart
   ↓
Cart
   ↓
Proceed to Checkout
   ↓
Checkout
   ├── Load Addresses
   ├── Select Address
   ├── Review Order
   └── Place Order
           ↓
       POST /api/orders/
           ↓
      OrderService
           ↓
       Order Created
           ↓
       Cart Deleted
           ↓
      /orders
```

و این دقیقاً با Backend فعلی تو هماهنگ است:

```
POST /api/orders/

{
    "cart_id": "...",
    "address_id": 3
}
```

Backend هم خودش مالکیت Cart و Address را بررسی می‌کند و Snapshot آدرس و قیمت را انجام می‌دهد.

بعد از ساخت این سه بخش، فقط تست می‌کنیم:

1. Login
2. Cart دارای محصول
3. `/checkout`
4. نمایش Address
5. انتخاب Address
6. `Place Order`
7. ایجاد Order
8. حذف Cart
9. نمایش Order جدید در `/orders`

اگر این تست موفق شد، **Checkout Domain را تمام‌شده در نظر می‌گیریم و می‌رویم سراغ Payment Domain**؛ نه اینکه فعلاً CSS، تصویر یا مشکلات امنیتی قبلی را وسط کار وارد کنیم.

در `Checkout.jsx` این را نوشته‌ای:

```
const order = await orderService.createOrder({
  cart_id: cart.id,
  address_id: Number(selectedAddressId),
});
```

در حالی که `orderService.js` فعلی تو این تابع را این‌طور تعریف کرده:

```
createOrder: async (cartId, addressId) => {
```

بنابراین این دو با هم **هماهنگ نیستند**.

یعنی باید اول این اختلاف را اصلاح کنیم، بعد Checkout را تست کنیم.

> 211- قدم بعدی
> 
> 
> در `Checkout.jsx` فقط این قسمت:
> 
> ```
> const order = await orderService.createOrder({
>   cart_id: cart.id,
>   address_id: Number(selectedAddressId),
> });
> ```
> 
> را به این تبدیل کن:
> 
> ```
> await orderService.createOrder(
>   cart.id,
>   Number(selectedAddressId)
> );
> ```
> 
> بعد:
> 
> ```
> navigate("/orders");
> ```
> 
> همان‌طور باقی بماند.
> 

**فعلاً هیچ فایل دیگری را تغییر نده.**

بعد از این تغییر، چون مسیر اصلی ما این است:

**Cart → Checkout → Address → Create Order → Orders**

می‌رویم سراغ تست واقعی Checkout و اگر خطایی آمد، همان خطا را مرحله‌به‌مرحله برطرف می‌کنیم.

الان بهترین کار این است که **سرور Django و React را اجرا کنیم و Checkout را به‌صورت واقعی تست کنیم**. چون Backend سفارش و Orders قبلاً با موفقیت تست شده و Login هم الان کار می‌کند، دیگر نباید حدسی کد بزنیم.

مسیر توسعه فعلی ما این است:

**Cart → Checkout → انتخاب Address → ایجاد Order → خالی‌شدن Cart → Orders**

<aside>
💡

### **مرحله ۱ — اصلاح `Checkout.jsx`**

</aside>

> 212- اول همان اصلاحی که گفتم انجام بده:
> 
> 
> ```
> await orderService.createOrder(
>   cart.id,
>   Number(selectedAddressId)
> );
> ```
> 
> به‌جای:
> 
> ```
> await orderService.createOrder({
>   cart_id: cart.id,
>   address_id: Number(selectedAddressId),
> });
> ```
> 

<aside>
💡

### مرحله ۲ — سرور Django را اجرا کن

</aside>

> 213- در Terminal مربوط به Backend:
> 
> 
> ```
> cd D:/Repo/Django/acron/backend
> python manage.py runserver
> ```
> 
> باید چیزی شبیه این ببینی:
> 
> ```
> Starting development server at http://127.0.0.1:8000/
> ```
> 

<aside>
💡

### مرحله ۳ — سرور React را اجرا کن

</aside>

> 214- در یک Terminal جدا:
> 
> 
> ```
> cd D:/Repo/Django/acron/frontend
> npm run dev
> ```
> 
> بعد وارد:
> 
> ```
> http://localhost:5173/
> ```
> 
> شو.
> 
> ---
> 

<aside>
📢

# پایان Part-20

</aside>