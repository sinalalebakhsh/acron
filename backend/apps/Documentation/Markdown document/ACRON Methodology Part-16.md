# ACRON Methodology Part-16

<aside>
📢

در Part-13 ، **فاز 11:**    Frontend - Presentation Layer  تا قدم 86 توسعه داده شد

</aside>

# فاز 11**:**   Frontend - Presentation Layer

شروع قدم 87

---

ریشه اصلی هر دو خطا (**400 Bad Request** و **405 Method Not Allowed**) دقیقاً مشخص شد. خستگی ۳ ساعت کار با این دو مشکل کاملاً به‌جاست، اما خبر خوب این است که ایراد دقیقاً پیدا شده و با اصلاح کدها همه‌چیز درست می‌شود.
**🧐 بررسی دقیق علت رخ دادن خطاها
۱. علت خطای ۴۰۰ روی `/api/token/` (تداخل در لاگین)**
در فایل `Login.jsx` درخواست POST به `token/` زده می‌شد و نتیجه آن (توکن‌ها) به تابع `login(response.data)` فرستاده می‌شد. اما تابع `login` در `AuthContext.jsx` دو پارامتر `(username, password)` می‌خواست!  
وقتی `response.data` وارد `AuthContext` می‌شد، `username` برابر با یک جفت توکن `{ access: "...", refresh: "..." }` قرار می‌گرفت و `password` هم `undefined` می‌شد! سپس `AuthContext` یک درخواست مجدد به `/api/token/` با مقادیر خراب می‌فرستاد و جنگو خطای **400 Bad Request** می‌داد.

۲. علت خطای ۴۰۵ روی `/api/carts/` (تداخل Router در بک‌اند)

در فایل `apps/carts/urls.py`  مسیر `''` قبل از `'cart-items'` ثبت شده بود:

```python
router.register('', CartViewSet, basename='carts')
router.register('cart-items', CartItemViewSet, basename='cart-items')
```

چون `''` الگوهای شناسه مثل `api/carts/<pk>/` می‌سازد، وقتی فرانت‌اند درخواستی به `/api/carts/cart-items/` می‌فرستاد، جنگو عبارت `cart-items` را به عنوان آی‌دی سبد خرید (`pk='cart-items'`) فرض می‌کرد! چون نمای جزئیات (Detail View) متد `POST` را قبول نمی‌کند، جنگو خطای **405 Method Not Allowed** می‌داد.

🛠️ کد اصلاح‌شده و آماده فایل‌ها

> 87-  اصلاح فایل `src/components/Login.jsx`
> 
> 
> کل مسئولیت ارسال درخواست لاگین را به `AuthContext` می‌سپاریم:
> 
> ```python
> import React, { useState } from 'react';
> import { useAuth } from '../context/AuthContext';
> 
> function Login() {
>   const [username, setUsername] = useState('');
>   const [password, setPassword] = useState('');
>   const [loading, setLoading] = useState(false);
>   const [error, setError] = useState('');
> 
>   const { login } = useAuth();
> 
>   const handleSubmit = async (e) => {
>     e.preventDefault();
>     setLoading(true);
>     setError('');
> 
>     try {
>       // 🔴 ارسال مستقیم نام کاربری و رمز عبور به AuthContext
>       await login(username, password);
>     } catch (err) {
>       console.error('Login Error:', err);
>       setError('نام کاربری یا رمز عبور اشتباه است.');
>     } finally {
>       setLoading(false);
>     }
>   };
> 
>   return (
>     <div style={{ maxWidth: '400px', margin: '80px auto', padding: '20px', fontFamily: 'sans-serif', direction: 'rtl' }}>
>       <h2 style={{ textAlign: 'center' }}>ورود به سیستم Acron</h2>
>       
>       {error && <div style={{ color: 'red', marginBottom: '10px', textAlign: 'center' }}>{error}</div>}
> 
>       <form onSubmit={handleSubmit}>
>         <div style={{ marginBottom: '15px' }}>
>           <label>نام کاربری:</label>
>           <input
>             type="text"
>             value={username}
>             onChange={(e) => setUsername(e.target.value)}
>             style={{ width: '100%', padding: '8px', marginTop: '5px' }}
>             required
>           />
>         </div>
> 
>         <div style={{ marginBottom: '15px' }}>
>           <label>رمز عبور:</label>
>           <input
>             type="password"
>             value={password}
>             onChange={(e) => setPassword(e.target.value)}
>             style={{ width: '100%', padding: '8px', marginTop: '5px' }}
>             required
>           />
>         </div>
> 
>         <button
>           type="submit"
>           disabled={loading}
>           style={{ width: '100%', padding: '10px', backgroundColor: '#4caf50', color: '#fff', border: 'none', borderRadius: '4px', cursor: 'pointer' }}
>         >
>           {loading ? 'در حال بررسی...' : 'ورود'}
>         </button>
>       </form>
>     </div>
>   );
> }
> 
> export default Login;
> ```
> 

> 88- **اصلاح فایل `src/context/AuthContext.jsx`**
برای جلوگیری از کرش موقع دریافت پروفایل، بلوک دریافت پروفایل را داخل `try/catch` قرار می‌دهیم:
> 
> 
> ```python
> import React, { createContext, useState, useEffect, useContext } from 'react';
> import axiosInstance from '../api/axiosInstance';
> 
> const AuthContext = createContext();
> 
> export const AuthProvider = ({ children }) => {
>   const [user, setUser] = useState(null);
>   const [loading, setLoading] = useState(true);
> 
>   useEffect(() => {
>     const checkAuthStatus = async () => {
>       const token = localStorage.getItem('access_token');
>       if (token) {
>         try {
>           const response = await axiosInstance.get('me/');
>           setUser(response.data);
>         } catch (error) {
>           console.error('توکن نامعتبر است:', error);
>           localStorage.removeItem('access_token');
>           localStorage.removeItem('refresh_token');
>         }
>       }
>       setLoading(false);
>     };
> 
>     checkAuthStatus();
>   }, []);
> 
>   const login = async (username, password) => {
>     // ارسال مستقیم اطلاعات ورودی به اندپوینت token/
>     const response = await axiosInstance.post('token/', { 
>       username, 
>       password 
>     });
>     
>     const { access, refresh } = response.data;
> 
>     localStorage.setItem('access_token', access);
>     localStorage.setItem('refresh_token', refresh);
>     
>     try {
>       const userProfile = await axiosInstance.get('me/');
>       setUser(userProfile.data);
>     } catch (e) {
>       console.warn('پروفایل کاربر دریافت نشد:', e);
>     }
>     
>     return response.data;
>   };
> 
>   const logout = () => {
>     localStorage.removeItem('access_token');
>     localStorage.removeItem('refresh_token');
>     setUser(null);
>   };
> 
>   return (
>     <AuthContext.Provider value={{ user, login, logout, loading, isAuthenticated: !!user }}>
>       {!loading && children}
>     </AuthContext.Provider>
>   );
> };
> 
> export const useAuth = () => useContext(AuthContext);
> export { AuthContext };
> ```
> 

> 89-ا `apps/carts/urls.py` (بک‌اند)
> 
> 
> ترتیب ثبت ویوست‌ها را اصلاح کن تا مسیر `cart-items` اولویت داشته باشد
> 
> ```python
> from django.urls import path, include
> from rest_framework.routers import DefaultRouter
> from .views import CartViewSet, CartItemViewSet
> 
> router = DefaultRouter()
> 
> # 🔴 ثبت cart-items قبل از '' ضروری است تا تداخل URL ایجاد نشود
> router.register('cart-items', CartItemViewSet, basename='cart-items')
> router.register('', CartViewSet, basename='carts')
> 
> urlpatterns = [
>     path('', include(router.urls)),
> ]
> ```
> 

> 90- اصلاح فایل `apps/carts/views.py` (بک‌اند)
> 
> 
> مطمئن شو که کلاس `CartViewSet` هر دو متد `create` و `list` را به صورت شفاف پیاده‌سازی می‌کند:
> 
> ```python
> from rest_framework import status
> from rest_framework.viewsets import GenericViewSet, ModelViewSet
> from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
> from rest_framework.decorators import action
> from rest_framework.response import Response
> from rest_framework.permissions import AllowAny, IsAuthenticated
> 
> from apps.customers.models import Customer
> from .models import Cart, CartItem
> from .serializers import CartSerializer, CartItemSerializer, AddCartItemSerializer, UpdateCartItemSerializer
> 
> class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
>     permission_classes = [AllowAny]
>     queryset = Cart.objects.prefetch_related('items__product').all()
>     serializer_class = CartSerializer
> 
>     def create(self, request, *args, **kwargs):
>         cart = Cart.objects.create()
>         serializer = self.get_serializer(cart)
>         return Response(serializer.data, status=status.HTTP_201_CREATED)
> 
>     def list(self, request, *args, **kwargs):
>         if request.user and request.user.is_authenticated:
>             customer, _ = Customer.objects.get_or_create(user=request.user)
>             cart, _ = Cart.objects.get_or_create(customer=customer)
>         else:
>             cart = Cart.objects.create()
> 
>         serializer = self.get_serializer(cart)
>         return Response(serializer.data)
> 
>     @action(detail=False, methods=['get'], url_path='mine', permission_classes=[IsAuthenticated])
>     def mine(self, request):
>         customer, _ = Customer.objects.get_or_create(user=request.user)
>         cart, _ = Cart.objects.get_or_create(customer=customer)
>         serializer = self.get_serializer(cart)
>         return Response(serializer.data)
> 
> class CartItemViewSet(ModelViewSet):
>     permission_classes = [AllowAny]
>     http_method_names = ['post', 'patch', 'delete']
>     queryset = CartItem.objects.select_related('product').all()
> 
>     def get_serializer_class(self):
>         if self.request.method == 'POST':
>             return AddCartItemSerializer
>         elif self.request.method == 'PATCH':
>             return UpdateCartItemSerializer
>         return CartItemSerializer
> ```
> 

> 91- اصلاح مدل سبد خرید (`apps/carts/models.py`)
> 
> 
> فایل **`apps/carts/models.py`** را باز کنید و فیلد `customer` را به مدل `Cart` اضافه کنید تا سبد خرید بتواند به کاربر لاگین شده متصل شود:
> 
> ```python
> import uuid
> from django.db import models
> 
> class Cart(models.Model):
>     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
>     created_at = models.DateTimeField(auto_now_add=True)
>     # 🔴 اتصال سبد خرید به مشتری (برای کاربران لاگین شده)
>     customer = models.OneToOneField(
>         'customers.Customer',
>         on_delete=models.CASCADE,
>         null=True,
>         blank=True,
>         related_name='cart'
>     )
> 
>     def __str__(self):
>         return str(self.id)
> 
> class CartItem(models.Model):
>     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
>     product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
>     quantity = models.PositiveIntegerField(default=1)
> 
>     class Meta:
>         unique_together = [['cart', 'product']]
> 
>     def __str__(self):
>         return f"{self.quantity} x {self.product.name}"
> ```
> 

> 93- اعمال ماایگریشن در دیتابیس (در ترمینال بک‌اند)
> 
> 
> ```python
> python manage.py makemigrations
> python manage.py migrate
> python manage.py migrate
> ```
> 

> 94- 🛠️ راه حل (اصلاح فایل `apps/orders/urls.py`)
فایل **`apps/orders/urls.py`** را باز کنید و مقداری که به `router.register` داده‌اید را از `'orders'` به  رشته خالی `''`  تغییر دهید
> 
> 
> ```python
> from django.urls import path, include
> from rest_framework.routers import DefaultRouter
> from .views import OrderViewSet
> 
> router = DefaultRouter()
> # 🔴 تغییر 'orders' به '' تا آدرس نهایی دقیقا /api/orders/ شود
> router.register('', OrderViewSet, basename='orders')
> 
> urlpatterns = [
>     path('', include(router.urls)),
> ]
> ```
> 

اگر دقت کنی از Navbar عدد محصولات خریده شده حذف نشده علت این ناهماهنگی این است که بک‌اند پس از ثبت سفارش، سبد خرید را از دیتابیس پاک می‌کند؛ اما **State سبد خرید در فرانت‌اند (React)** از حذف شدن آن باخبر نشده و عدد ۲ همچنان در حافظه `CartContext` باقی مانده است.

> 95- به‌روزرسانی `CartContext.jsx`
> 
> 
> فایل **`src/context/CartContext.jsx`** را با فایل زیر جا به جا کنید ، چون حجم فایل زیاد بود اصل فایل را استفاده کنید.
> 
> [CartContext.jsx](CartContext.jsx)
> 

<aside>
💡

کد کامل و اصلاح‌شده `Cart.jsx`

</aside>

> 96- کد زیر را کاملاً جایگزین فایل **`Cart.jsx`** کن:
> 
> 
> [Cart.jsx](Cart.jsx)
> 

> 97- اصلاح `Navbar.jsx`
> 
> 
> فایل **`Navbar.jsx`** (یا هر فایلی که منوی بالای سایت در آن قرار دارد) را باز کنید و مطمئن شوید که عدد سبد خرید مستقیماً از `useCart()` دریافت می‌شود:
> 
> ```python
> import React from 'react';
> import { Link } from 'react-router-dom';
> import { useCart } from '../context/CartContext'; // 🔴 ۱. ایمپورت هوک
> 
> function Navbar() {
>   // 🔴 ۲. دریافت تعداد کل آیتم‌ها از Context
>   const { totalItemsCount } = useCart(); 
> 
>   return (
>     <nav className="navbar">
>       <Link to="/products">محصولات</Link>
>       
>       {/* 🔴 ۳. نمایش متغیر dynamic که با تغییر state سریعاً آپدیت می‌شود */}
>       <Link to="/cart">
>         🛒 سبد خرید: {totalItemsCount}
>       </Link>
>       
>       <Link to="/orders">سفارش‌های من</Link>
>     </nav>
>   );
> }
> 
> export default Navbar;
> ```
> 

<aside>
💡

مفاهیم جاوااسکریپت و ری‌اکت در این تغییرات

</aside>

۱. منطق خروج (Logout) در معماری وب (JWT & LocalStorage)

در اپلیکیشن‌های ری‌اکت که با بک‌اند Django REST Framework کار می‌کنند، وضعیت لاگین بودن کاربر بر اساس **توکن (Token)** ذخیره‌شده در مرورگر (معمولاً در `localStorage`) تعیین می‌شود.

- **`ا   localStorage.clear()` یا `localStorage.removeItem('access')`:** برای خروج کاربر از حساب، نیازی به ارسال درخواست پیچیده به بک‌اند نیست؛ کافی است توکن دسترسی را از مرورگر پاک کنیم. بدون توکن، درخواست‌های بعدی کاربر به بک‌اند خطای `401 Unauthorized` دریافت می‌کنند.
- **`ا   useNavigate()`:** هوکی از کتابخانه `react-router-dom` است که امکان هدایت کاربر به صفحات دیگر (مثل `/login`) را بدون رفرش شدن کل صفحه (ساختار Single Page Application یا SPA) فراهم می‌کند.

<aside>
📢

# پایان Part-16

</aside>