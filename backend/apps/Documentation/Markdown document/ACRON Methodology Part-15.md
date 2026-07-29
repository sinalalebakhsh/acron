# ACRON Methodology Part-15

<aside>
📢

در Part-13 ، **فاز 11:**    Frontend - Presentation Layer  تا قدم 47 توسعه داده شد

</aside>

# فاز 11**:**   Frontend - Presentation Layer

شروع قدم 48

---

<aside>
💡

📚 آموزش مفاهیم فاز بعدی: تبدیل سبد خرید به سفارش (Orders)

</aside>

1. **الگوی فریز/عکس‌برداری داده‌ها (Snapshot Pattern in Orders):**
سبد خرید یک موجودیت پویا (Dynamic) است؛ اما وقتی کاربر دکمه «ثبت سفارش» را می‌زند، سیستم باید قیمت‌ها و عناوین محصولات را در آن لحظه دقیقاً فریز کند و در جدول `Order` ثبت نماید. این کار باعث می‌شود اگر فردا قیمت یک محصول در دیتابیس تغییر کرد، فاکتورهای خرید قبلی کاربر دچار تغییر یا خطای مالی نشوند.
2. **ریست شدن چرخه حیات سبد خرید (Cart Reset):**
پس از اینکه درخواست ساخت سفارش به API ارسال شد و کد وضعیت `201 Created` دریافت کردیم، شناسه `cart_id` قبلی از `localStorage` پاک می‌شود تا سبد خرید کاربر برای خریدهای بعدی خالی و آماده شود.

<aside>
💡

🛣️ مسیر گام بعدی

</aside>

اکنون زمان آن رسیده که **فرآیند نهایی‌سازی خرید و ثبت سفارش (`apps.orders`)** را پیاده‌سازی کنیم.

برای این کار:

1. ابتدا آدرس دقیق API مربوط به سفارشات را در بک‌اند (از طریق Swagger یا فایل `apps/orders/urls.py`) چک می‌کنیم.
2. دکمه **«ادامه جهت ثبت سفارش»** را به فرم ثبت آدرس/ارسال درخواست سفارش متصل می‌کنیم.

<aside>
💡

🔍 تحلیل و بررسی معماری بک‌اند سفارشات orders APP

</aside>

1. **معماری تمیز (Clean Architecture / Service Layer):**
تمام منطق تجاری پیچیده دیتابیس در `OrderService.place_order` قرار گرفته و `OrderViewSet` کاملاً خلوت و خوانا نگه داشته شده است.
2. **تراکنش اتمیک (`transaction.atomic`):**
اگر در حین کسر موجودی انبار یا ایجاد آیتم‌های سفارش هرگونه خطایی رخ دهد، کل عملیات برگشت (`Rollback`) داده می‌شود تا دیتابیس دچار داده‌های ناهمگام نشود.
3. **فریز کردن قیمت کالا (`unit_price` / `price`):**
قیمت کالا در لحظه خرید روی `OrderItem` ذخیره می‌شود تا تغییرات قیمت در آینده روی فاکتورهای قبلی کاربر تاثیری نگذارد.
4. **کنترل موجودی انبار و غیرفعال‌سازی سبد خرید:**
موجودی محصولات کسر شده و وضعیت سبد خرید پس از ثبت سفارش برابر `is_active = False` قرار می‌گیرد.

<aside>
💡

📋 قرارداد ارتباطی (API Contract) برای فرانت‌اند

</aside>

طبق کد `OrderCreateInputSerializer` و `OrderViewSet`:  
• **آدرس درخواست:** `POST /api/orders/`
  
• **سطح دسترسی:** فقط کاربر لاگین شده (`IsAuthenticated`)  
• **ورودی‌های مورد نیاز (Request Body):**

```python
{
  "cart_id": "شناسه UUID سبد خرید فعلی",
  "shipping_address": "آدرس کامل جهت ارسال سفارش (حداقل ۱۰ کاراکتر)"
}
```

<aside>
💡

🛠️ پیاده‌سازی ثبت سفارش در فرانت‌اند

</aside>

برای وصل کردن دکمه **«ادامه جهت ثبت سفارش»**، یک مودال (پنجره شناور) دریافت آدرس در صفحه `/cart` ایجاد می‌کنیم تا کاربر آدرس خود را وارد کرده و سفارش نهایی ثبت شود.

> 48- به‌روزرسانی `src/components/Cart.jsx`
> 
> 
> کد زیر را جایگزین فایل `src/components/Cart.jsx` کن تا فرم دریافت آدرس و ارسال درخواست به `/api/orders/` اضافه شود:
> 
> ```jsx
> import React, { useState } from 'react';
> import { useCart } from '../context/CartContext';
> import { Link, useNavigate } from 'react-router-dom';
> import axiosInstance from '../api/axiosInstance';
> 
> function Cart() {
>   const { cart, cartCount, refreshCart } = useCart();
>   const navigate = useNavigate();
> 
>   // وضعیت‌های مربوط به پنجره دریافت آدرس و ثبت سفارش
>   const [showAddressModal, setShowAddressModal] = useState(false);
>   const [shippingAddress, setShippingAddress] = useState('');
>   const [loading, setLoading] = useState(false);
>   const [errorMessage, setErrorMessage] = useState('');
> 
>   if (!cart || !cart.items || cart.items.length === 0) {
>     return (
>       <div style={{ textAlign: 'center', marginTop: '60px', fontFamily: 'sans-serif', direction: 'rtl' }}>
>         <h2>سبد خرید شما خالی است 🛒</h2>
>         <p style={{ color: '#64748b', marginTop: '10px' }}>می‌توانید محصولات را از کاتالوگ انتخاب کنید.</p>
>         <Link to="/products" style={{
>           display: 'inline-block',
>           marginTop: '15px',
>           padding: '10px 20px',
>           backgroundColor: '#2563eb',
>           color: 'white',
>           textDecoration: 'none',
>           borderRadius: '6px'
>         }}>
>           مشاهده کاتالوگ محصولات
>         </Link>
>       </div>
>     );
>   }
> 
>   const calculateTotalPrice = () => {
>     return cart.items.reduce((sum, item) => {
>       const price = item.total_price || (item.product?.price ? Number(item.product.price) * item.quantity : 0);
>       return sum + price;
>     }, 0);
>   };
> 
>   // تابع ارسال درخواست ثبت سفارش به بک‌اند
>   const handlePlaceOrder = async (e) => {
>     e.preventDefault();
>     setErrorMessage('');
> 
>     if (shippingAddress.trim().length < 10) {
>       setErrorMessage('آدرس ارسال باید حداقل ۱۰ کاراکتر باشد.');
>       return;
>     }
> 
>     setLoading(true);
>     try {
>       const cartId = localStorage.getItem('cart_id');
>       
>       // ۱. ارسال درخواست به بک‌اند
>       await axiosInstance.post('orders/', {
>         cart_id: cartId,
>         shipping_address: shippingAddress
>       });
> 
>       // ۲. پاکسازی سبد خرید از حافظه مرورگر پس از ثبت موفق سفارش
>       localStorage.removeItem('cart_id');
>       await refreshCart();
> 
>       alert('🎉 سفارش شما با موفقیت ثبت شد!');
>       setShowAddressModal(false);
>       
>       // انتقال کاربر به صفحه داشبورد یا لیست سفارشات
>       navigate('/');
>     } catch (error) {
>       console.error('خطا در ثبت سفارش:', error.response?.data);
>       const backendError = error.response?.data?.non_field_errors?.[0] 
>         || error.response?.data?.shipping_address?.[0]
>         || error.response?.data?.detail 
>         || 'خطایی در ثبت سفارش رخ داد.';
>       setErrorMessage(backendError);
>     } finally {
>       setLoading(false);
>     }
>   };
> 
>   return (
>     <div style={{ padding: '30px', maxWidth: '850px', margin: '0 auto', fontFamily: 'sans-serif', direction: 'rtl' }}>
>       <h2 style={{ marginBottom: '20px', color: '#0f172a' }}>سبد خرید شما ({cartCount} آیتم)</h2>
>       
>       <div style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
>         {cart.items.map((item) => (
>           <div key={item.id} style={{
>             display: 'flex',
>             justifyContent: 'space-between',
>             alignItems: 'center',
>             padding: '15px 20px',
>             border: '1px solid #e2e8f0',
>             borderRadius: '8px',
>             backgroundColor: '#fff'
>           }}>
>             <div style={{ flex: 1 }}>
>               <h3 style={{ margin: '0 0 5px 0', fontSize: '18px' }}>
>                 {item.product?.name || `محصول کد ${item.product_id}`}
>               </h3>
>               <span style={{ color: '#059669', fontWeight: 'bold' }}>
>                 تعداد: {item.quantity}
>               </span>
>             </div>
>             <div style={{ fontWeight: 'bold', fontSize: '16px' }}>
>               {(item.total_price 
>                 ? Number(item.total_price) 
>                 : (Number(item.product?.price || 0) * item.quantity)
>               ).toLocaleString()} تومان
>             </div>
>           </div>
>         ))}
>       </div>
> 
>       {/* خلاصه فاکتور */}
>       <div style={{
>         marginTop: '30px',
>         padding: '20px',
>         backgroundColor: '#f8fafc',
>         border: '1px solid #cbd5e1',
>         borderRadius: '8px',
>         display: 'flex',
>         justifyContent: 'space-between',
>         alignItems: 'center'
>       }}>
>         <div>
>           <span style={{ fontSize: '16px', color: '#475569' }}>مجموع قابل پرداخت:</span>
>           <h2 style={{ margin: '5px 0 0 0', color: '#059669' }}>
>             {calculateTotalPrice().toLocaleString()} تومان
>           </h2>
>         </div>
> 
>         <button 
>           onClick={() => setShowAddressModal(true)}
>           style={{
>             padding: '12px 24px',
>             backgroundColor: '#16a34a',
>             color: 'white',
>             border: 'none',
>             borderRadius: '6px',
>             fontSize: '16px',
>             fontWeight: 'bold',
>             cursor: 'pointer'
>           }}
>         >
>           ادامه جهت ثبت سفارش ➔
>         </button>
>       </div>
> 
>       {/* پنجره مودال دریافت آدرس */}
>       {showAddressModal && (
>         <div style={{
>           position: 'fixed',
>           top: 0,
>           left: 0,
>           right: 0,
>           bottom: 0,
>           backgroundColor: 'rgba(0,0,0,0.5)',
>           display: 'flex',
>           justifyContent: 'center',
>           alignItems: 'center',
>           zIndex: 1000
>         }}>
>           <div style={{
>             backgroundColor: '#fff',
>             padding: '30px',
>             borderRadius: '10px',
>             width: '90%',
>             maxWidth: '500px',
>             direction: 'rtl'
>           }}>
>             <h3 style={{ marginTop: 0 }}>تکمیل آدرس ارسال سفارش</h3>
>             <form onSubmit={handlePlaceOrder}>
>               <div style={{ marginBottom: '15px' }}>
>                 <label style={{ display: 'block', marginBottom: '8px', fontWeight: 'bold' }}>
>                   آدرس دقیق پستی:
>                 </label>
>                 <textarea 
>                   rows="4"
>                   value={shippingAddress}
>                   onChange={(e) => setShippingAddress(e.target.value)}
>                   placeholder="مثال: تهران، خیابان آزادی، پلاک ۱۲، واحد ۴ (حداقل ۱۰ کاراکتر)"
>                   style={{
>                     width: '100%',
>                     padding: '10px',
>                     borderRadius: '6px',
>                     border: '1px solid #cbd5e1',
>                     boxSizing: 'border-box'
>                   }}
>                   required
>                 />
>               </div>
> 
>               {errorMessage && (
>                 <div style={{ color: '#dc2626', marginBottom: '15px', fontSize: '14px' }}>
>                   {errorMessage}
>                 </div>
>               )}
> 
>               <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px' }}>
>                 <button
>                   type="button"
>                   onClick={() => setShowAddressModal(false)}
>                   disabled={loading}
>                   style={{
>                     padding: '10px 18px',
>                     backgroundColor: '#e2e8f0',
>                     border: 'none',
>                     borderRadius: '6px',
>                     cursor: 'pointer'
>                   }}
>                 >
>                   انصراف
>                 </button>
>                 <button
>                   type="submit"
>                   disabled={loading}
>                   style={{
>                     padding: '10px 20px',
>                     backgroundColor: '#16a34a',
>                     color: '#fff',
>                     border: 'none',
>                     borderRadius: '6px',
>                     fontWeight: 'bold',
>                     cursor: loading ? 'not-allowed' : 'pointer'
>                   }}
>                 >
>                   {loading ? 'در حال ثبت...' : 'تایید و ثبت سفارش نهایی'}
>                 </button>
>               </div>
>             </form>
>           </div>
>         </div>
>       )}
>     </div>
>   );
> }
> 
> export default Cart;
> ```
> 

<aside>
💡

🧪 نحوه تست در محیط واقعی

</aside>

1. فایل فوق را ذخیره کن و وارد مسیر `/cart` شو.
2. روی **«ادامه جهت ثبت سفارش»** کلیک کن.
3. یک آدرس پستی (بیشتر از ۱۰ حرف) وارد کن و **تایید و ثبت سفارش نهایی** را بزن.
4. اگر سفارش با موفقیت ثبت شود:
    ◦ پیغام موفقیت نمایش داده می‌شود.
    ◦ سبد خرید قدیمی غیرفعال شده و از `localStorage` پاک می‌شود.  
    ◦ نشانگر سبد خرید روی `Navbar` مجدداً **`۰`** خواهد شد.

<aside>
💡

حل ارور 500 سمت سرور

</aside>

در فایل `apps/orders/services.py` در خط ۳۱ و ۷۸، سیستم سعی می‌کند فیلد `is_active` را روی مدل `Cart` فیلتر و مقداردهی کند. اما طبق پیغام دقیق خطا:  `django.core.exceptions.FieldError: Cannot resolve keyword 'is_active' into field. Choices are: created_at, id, items`
در مدل `Cart` شما، فیلدی به نام `is_active` وجود ندارد و تنها فیلدهای موجود `id` و `created_at` و `items` هستند.

<aside>
💡

🛠️ راه حل سریع و تمیز (اصلاح `apps/orders/services.py`)

</aside>

برای حل این مشکل، به‌جای استفاده از فیلد غیرموجود `is_active`، فرآیند را طوری تنظیم می‌کنیم که پس از ثبت موفق سفارش، سبد خرید با دستور `cart.delete()` کلاً پاک شود (یا آیتم‌های آن حذف شوند).

> 49- کد زیر را در فایل **`apps/orders/services.py`** جایگزین کن:
> 
> 
> ```jsx
> # apps/orders/services.py
> 
> from django.db import transaction
> from rest_framework.exceptions import ValidationError
> from apps.carts.models import Cart
> from apps.orders.models import Order, OrderItem
> from apps.products.models import Product
> 
> class OrderService:
>     """
>     سرویس ارشد مدیریت و پردازش فرآیند ثبت سفارش در پروژه ACRON.
>     """
> 
>     @classmethod
>     def place_order(cls, user, cart_id: str, shipping_address: str) -> Order:
>         
>         with transaction.atomic():
>             
>             # ۱. واکشی سبد خرید به همراه اقلام آن (بدون فیلتر is_active)
>             try:
>                 cart = Cart.objects.prefetch_related('items__product').get(id=cart_id)
>             except Cart.DoesNotExist:
>                 raise ValidationError("سبد خرید معتبری یافت نشد.")
> 
>             # ۲. بررسی اینکه آیا سبد خرید اصلاً قلم کالا دارد یا خیر
>             cart_items = cart.items.all()
>             if not cart_items:
>                 raise ValidationError("سبد خرید شما خالی است و امکان ثبت سفارش وجود ندارد.")
> 
>             # ۳. محاسبه کل مبلغ سفارش و بررسی موجودی انبار
>             total_price = 0
>             for item in cart_items:
>                 product = item.product
>                 
>                 if product.stock < item.quantity:
>                     raise ValidationError(
>                         f"موجودی کالا '{product.name}' کافی نیست. موجودی فعلی: {product.stock}"
>                     )
>                 
>                 total_price += product.price * item.quantity
> 
>             # ۴. ایجاد رکورد اصلی سفارش در دیتابیس
>             order = Order.objects.create(
>                 user=user,
>                 total_price=total_price,
>                 shipping_address=shipping_address,
>                 status='PENDING'
>             )
> 
>             # ۵. انتقال اقلام به سفارش + فریز کردن قیمت‌ها + کسر از انبار
>             for item in cart_items:
>                 product = item.product
>                 
>                 OrderItem.objects.create(
>                     order=order,
>                     product=product,
>                     quantity=item.quantity,
>                     price=product.price
>                 )
> 
>                 product.stock -= item.quantity
>                 product.save(update_fields=['stock'])
> 
>             # ۶. حذف سبد خرید پس از تکمیل موفق ثبت سفارش (به‌جای is_active = False)
>             cart.delete()
> 
>             return order
>             
>             
>   
> ```
> 

<aside>
💡

AttributeError: 'Product' object has no attribute 'stock' 

</aside>

علت این خطا این است که مدل `Product` در حال حاضر فیلدی به نام `stock` (موجودی انبار) ندارد و تلاش برای خواندن `product.stock` باعث بروز `AttributeError` شده است.
علاوه بر این، اگر فایل `models.py` اپلیکیشن `orders` را بررسی کنیم، چند مغایرت دیگر هم بین کد قبلی `services.py` و ساختار واقعی مدل‌های دیتابیس وجود دارد که در صورت عدم اصلاح، بلافاصله خطاهای بعدی را ایجاد می‌کردند:  

1. **مدل `Order`:** به کلید خارجی `customer` (شیء `Customer`) متصل است نه مستقیماً `user`. همچنین فیلدهای `total_price` و `shipping_address` روی مدل `Order` تعریف نشده‌اند.  
2. **وضعیت سفارش (`status`):** مقدار در انتظار پرداخت در این مدل برابر `'P'` است (`Order.OrderStatus.PENDING`).  
3. **مدل `OrderItem`:** اسم فیلد قیمت فریز شده `unit_price` است، نه `price`.  

<aside>
💡

🛠️ کد اصلاح‌شده و نهایی `apps/orders/services.py`

</aside>

> 50- فایل **`apps/orders/services.py`** را با کد زیر کاملاً جایگزین کن تا ۱۰۰٪ با مدل‌های دیتابیس فعلی‌ات هماهنگ شود:
> 
> 
> ```jsx
> # apps/orders/services.py
> 
> from django.db import transaction
> from rest_framework.exceptions import ValidationError
> from apps.carts.models import Cart
> from apps.orders.models import Order, OrderItem
> from apps.customers.models import Customer
> 
> class OrderService:
>     """
>     سرویس ارشد مدیریت و پردازش فرآیند ثبت سفارش در پروژه ACRON.
>     """
> 
>     @classmethod
>     def place_order(cls, user, cart_id: str, shipping_address: str) -> Order:
>         """
>         متد ثبت سفارش با رعایت کامل ساختار مدل‌های Order و OrderItem.
>         """
>         
>         with transaction.atomic():
>             
>             # ۱. یافتن پروفایل مشتری (Customer) متصل به کاربر جاری
>             try:
>                 customer = Customer.objects.get(user=user)
>             except Customer.DoesNotExist:
>                 raise ValidationError("پروفایل مشتری برای این کاربر یافت نشد.")
> 
>             # ۲. واکشی سبد خرید به همراه اقلام آن
>             try:
>                 cart = Cart.objects.prefetch_related('items__product').get(id=cart_id)
>             except Cart.DoesNotExist:
>                 raise ValidationError("سبد خرید معتبری یافت نشد.")
> 
>             # ۳. بررسی خالی نبودن سبد خرید
>             cart_items = cart.items.all()
>             if not cart_items:
>                 raise ValidationError("سبد خرید شما خالی است و امکان ثبت سفارش وجود ندارد.")
> 
>             # ۴. ایجاد رکورد اصلی سفارش در دیتابیس (مطابق با مدل Order)
>             order = Order.objects.create(
>                 customer=customer,
>                 status=Order.OrderStatus.PENDING  # مقدار 'P'
>             )
> 
>             # ۵. انتقال اقلام به سفارش و فریز کردن قیمت در فیلد unit_price
>             for item in cart_items:
>                 product = item.product
>                 
>                 OrderItem.objects.create(
>                     order=order,
>                     product=product,
>                     quantity=item.quantity,
>                     unit_price=product.price  # ذخیره قیمت فریز شده کالا
>                 )
> 
>             # ۶. پاکسازی سبد خرید پس از ثبت موفق سفارش
>             cart.delete()
> 
>             return order
> ```
> 

<aside>
💡

🧪 تست مجدد

</aside>

اکنون کافی است مجدداً در فرانت‌اند روی **تایید و ثبت سفارش نهایی** کلیک کنی. سفارش بدون هیچ خطایی ثبت شده و سبد خرید پاکسازی خواهد شد.

![image.png](image.png)

هدایت کاربر به **صفحه فاکتور یا لیست سفارشات (`/orders`)** استانداردترین و حرفه‌ای‌ترین گام بعدی است.

<aside>
💡

📚 مفهوم این گام (چرخه هدایت کاربر پس از خرید)

</aside>

1. **استفاده از خروجی API ثبت سفارش:**
وقتی درخواست `POST /api/orders/` موفقیت‌آمیز باشد، بک‌اند شیء سفارشِ ساخته‌شده را همراه با شناسه `id` برمی‌گرداند.
2. **بهبود تجریه کاربری (UX):**
به‌جای اینکه کاربر را به صفحه اصلی (`/`) منتقل کنیم، بهتر است او را مستقیماً به صفحه **«سفارش‌های من»** یا **«فاکتور سفارش»** هدایت کنیم تا وضعیت سفارش (در انتظار پرداخت، اقلام خریده‌شده و آدرس) را مشاهده کند.

<aside>
💡

🛣️ نقشه راه تکمیل بخش سفارشات

</aside>

برای کامل شدن این بخش، ۳ گام ساده پیش‌رو داریم:
1. **ساخت کامپوننت `Orders.jsx`:** برای دریافت لیست سفارشات کاربر از `GET /api/orders/` و نمایش فاکتورها.  
2. **افزودن روت جدید در `App.jsx`:** اضافه کردن مسیر `/orders`.
3. **افزودن لینک به Navbar:** ایجاد دکمه **«سفارش‌های من»** در نوار بالای سایت.

<aside>
💡

📚 مفاهیم آموزشی این گام

</aside>

1. **نگاشت وضعیت‌ها (Status Mapping):**
در دیتابیس، وضعیت سفارشات با کدهای تک‌حرفی مانند `'P'` (در انتظار پرداخت)، `'C'` (پرداخت موفق) و `'X'` (لغو شده) ذخیره می‌شود. در فرانت‌اند با یک شیء نگاشت (Map) این کدها را به برچسب‌های فارسی و رنگ‌های مناسب وضعیت (سبز، زرد، قرمز) تبدیل می‌کنیم.
2. **جداسازی صفحات و بهبود جریان کاربری (User Flow):**
    
    پس از ارسال موفقیت‌آمیز سفارش در `/cart`، کاربر نباید در صفحه خالی سبد خرید بماند یا به صفحه اصلی پرت شود؛ هدایت خودکار به `/orders` شفاف‌ترین تجربه کاربری را رقم می‌زند.
    
    <aside>
    💡
    
    🛠️ اجرای گام به گام توسعه
    
    </aside>
    

> 51- ساخت کامپوننت `src/components/Orders.jsx`
> 
> 
> این کامپوننت هنگام لود شدن، درخواست `GET /api/orders/` را به بک‌اند می‌فرستد و کارت‌های سفارش را همراه با اقلام داخلی نمایش می‌دهد:
> 
> ```jsx
> import React, { useEffect, useState } from 'react';
> import axiosInstance from '../api/axiosInstance';
> import { Link } from 'react-router-dom';
> 
> function Orders() {
>   const [orders, setOrders] = useState([]);
>   const [loading, setLoading] = useState(true);
>   const [error, setError] = useState('');
> 
>   // فرهنگ‌لغت نگاشت وضعیت‌های بک‌اند به عنوان و رنگ
>   const statusConfig = {
>     P: { label: 'در انتظار پرداخت', color: '#d97706', bgColor: '#fef3c7' },
>     C: { label: 'پرداخت موفق', color: '#16a34a', bgColor: '#dcfce7' },
>     X: { label: 'لغو شده', color: '#dc2626', bgColor: '#fee2e2' },
>   };
> 
>   useEffect(() => {
>     const fetchOrders = async () => {
>       try {
>         const response = await axiosInstance.get('orders/');
>         setOrders(response.data);
>       } catch (err) {
>         console.error('خطا در دریافت سفارشات:', err);
>         setError('خطا در دریافت لیست سفارش‌ها. لطفاً مجدداً تلاش کنید.');
>       } finally {
>         setLoading(false);
>       }
>     };
> 
>     fetchOrders();
>   }, []);
> 
>   if (loading) {
>     return (
>       <div style={{ textAlign: 'center', marginTop: '50px', fontFamily: 'sans-serif', direction: 'rtl' }}>
>         در حال دریافت تاریخچه سفارشات... 🔄
>       </div>
>     );
>   }
> 
>   if (error) {
>     return (
>       <div style={{ textAlign: 'center', marginTop: '50px', color: '#dc2626', fontFamily: 'sans-serif', direction: 'rtl' }}>
>         {error}
>       </div>
>     );
>   }
> 
>   if (orders.length === 0) {
>     return (
>       <div style={{ textAlign: 'center', marginTop: '60px', fontFamily: 'sans-serif', direction: 'rtl' }}>
>         <h2>هنوز هیچ سفارشی ثبت نکرده‌اید 📦</h2>
>         <p style={{ color: '#64748b', marginTop: '10px' }}>محصولات مورد علاقه خود را انتخاب و سفارش دهید.</p>
>         <Link to="/products" style={{
>           display: 'inline-block',
>           marginTop: '15px',
>           padding: '10px 20px',
>           backgroundColor: '#2563eb',
>           color: 'white',
>           textDecoration: 'none',
>           borderRadius: '6px'
>         }}>
>           مشاهده کاتالوگ محصولات
>         </Link>
>       </div>
>     );
>   }
> 
>   return (
>     <div style={{ padding: '30px', maxWidth: '850px', margin: '0 auto', fontFamily: 'sans-serif', direction: 'rtl' }}>
>       <h2 style={{ marginBottom: '20px', color: '#0f172a' }}>سفارش‌های من ({orders.length})</h2>
> 
>       <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
>         {orders.map((order) => {
>           const status = statusConfig[order.status] || { label: order.status, color: '#475569', bgColor: '#f1f5f9' };
>           const formattedDate = new Date(order.created_at).toLocaleDateString('fa-IR');
> 
>           return (
>             <div key={order.id} style={{
>               border: '1px solid #e2e8f0',
>               borderRadius: '10px',
>               backgroundColor: '#fff',
>               overflow: 'hidden',
>               boxShadow: '0 2px 4px rgba(0,0,0,0.04)'
>             }}>
>               {/* سربرگ کارت سفارش */}
>               <div style={{
>                 padding: '15px 20px',
>                 backgroundColor: '#f8fafc',
>                 borderBottom: '1px solid #e2e8f0',
>                 display: 'flex',
>                 justifyContent: 'space-between',
>                 alignItems: 'center'
>               }}>
>                 <div>
>                   <span style={{ fontSize: '13px', color: '#64748b' }}>شناسه سفارش: </span>
>                   <strong style={{ fontSize: '14px', color: '#1e293b' }}>{order.id.substring(0, 8)}...</strong>
>                   <span style={{ margin: '0 10px', color: '#cbd5e1' }}>|</span>
>                   <span style={{ fontSize: '13px', color: '#64748b' }}>تاریخ: {formattedDate}</span>
>                 </div>
> 
>                 <span style={{
>                   padding: '4px 12px',
>                   borderRadius: '20px',
>                   fontSize: '13px',
>                   fontWeight: 'bold',
>                   color: status.color,
>                   backgroundColor: status.bgColor
>                 }}>
>                   {status.label}
>                 </span>
>               </div>
> 
>               {/* اقلام داخلی سفارش */}
>               <div style={{ padding: '20px' }}>
>                 <h4 style={{ margin: '0 0 12px 0', fontSize: '15px', color: '#334155' }}>اقلام سفارش:</h4>
>                 <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
>                   {order.items?.map((item) => (
>                     <li key={item.id} style={{
>                       padding: '8px 0',
>                       borderBottom: '1px dashed #f1f5f9',
>                       display: 'flex',
>                       justifyContent: 'space-between',
>                       alignItems: 'center'
>                     }}>
>                       <span style={{ color: '#0f172a' }}>{item.product_name}</span>
>                       <span style={{ fontSize: '14px', color: '#64748b' }}>تعداد: {item.quantity}</span>
>                     </li>
>                   ))}
>                 </ul>
>               </div>
>             </div>
>           );
>         })}
>       </div>
>     </div>
>   );
> }
> 
> export default Orders;
> 
> ```
> 

> 52- اضافه کردن مسیر جدید در `src/App.jsx`
> 
> 
> کامپوننت `Orders` را وارد کرده و مسیریابی `/orders` را اضافه می‌کنیم:
> 
> ```jsx
> import React from 'react';
> import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
> import Navbar from './components/Navbar';
> import Dashboard from './components/Dashboard';
> import Products from './components/Products';
> import Cart from './components/Cart';
> import Orders from './components/Orders'; // 👈 اضافه شد
> import Login from './components/Login';
> import { CartProvider } from './context/CartContext';
> 
> function App() {
>   return (
>     <Router>
>       <CartProvider>
>         <Navbar />
>         <Routes>
>           <Route path="/" element={<Dashboard />} />
>           <Route path="/products" element={<Products />} />
>           <Route path="/cart" element={<Cart />} />
>           <Route path="/orders" element={<Orders />} /> {/* 👈 مسیر جدید */}
>           <Route path="/login" element={<Login />} />
>         </Routes>
>       </CartProvider>
>     </Router>
>   );
> }
> 
> export default App;
> ```
> 

> 53- به‌روزرسانی `Navbar.jsx` و انحراف مسیر خرید در `Cart.jsx`
> 
> 1. **در فایل `src/components/Navbar.jsx`:** منوی جدید **«سفارش‌های من»** را اضافه کن:
> 
> ```jsx
> // در داخل JSX مربوط به Navbar در کنار بقیه لینک‌ها:
> <Link to="/orders" style={{ color: 'white', textDecoration: 'none', marginLeft: '15px' }}>
>   سفارش‌های من
> </Link>
> ```
> 

> 54- **در فایل `src/components/Cart.jsx`:** مسیر انتقال پس از ثبت موفق سفارش را از `/` به `/orders` تغییر بده:
> 
> 
> ```jsx
> // در تابع handlePlaceOrder داخل Cart.jsx:
> alert('🎉 سفارش شما با موفقیت ثبت شد!');
> setShowAddressModal(false);
> 
> // انتقال مستقیم کاربر به صفحه لیست سفارش‌ها
> navigate('/orders'); // 👈 جایگزین navigate('/') شد
> ```
> 

![image.png](image%201.png)

فایل `Cart.jsx` کاملاً درست پیاده‌سازی شده و انتقال به صفحه `/orders` بدون مشکل انجام می‌شود.

خطای قرمز‌رنگی که در تصویر صفحه `/orders` می‌بینی (`خطا در دریافت لیست سفارش‌ها...`) مربوط به سمت فرانت‌اند نیست؛ بلکه هنگام ارسال درخواست `GET /api/orders/` سمت بک‌اند رخ داده است.

دلیل اصلی این است که در `OrderViewSet` سمت Django، کوئری دریافت سفارشات احتمالاً سعی می‌کند بر اساس `user=request.user` فیلتر کند یا از سریالایزری استفاده می‌کند که فیلدهایش با مدل `Order` و `Customer` همخوانی ندارند.

<aside>
💡

🛠️ اصلاح بک‌اند (برطرف کردن خطای `GET /api/orders/`)

</aside>

برای اینکه لیست سفارشات کاربر بدون خطا و همراه با جزییات کامل خروجی داده شود، دو فایل زیر را در اپلیکیشن `orders` به‌روزرسانی کن:

> 55- اصلاح `apps/orders/serializers.py`
> 
> 
> این فایل را تنظیم می‌کنیم تا اقلام سفارش (`items`) و مجموع قیمت (`total_price`) را محاسبه کرده و برگرداند:
> 
> ```jsx
> # apps/orders/serializers.py
> 
> from rest_framework import serializers
> from .models import Order, OrderItem
> 
> class OrderItemSerializer(serializers.ModelSerializer):
>     product_name = serializers.CharField(source='product.name', read_only=True)
> 
>     class Meta:
>         model = OrderItem
>         fields = ['id', 'product', 'product_name', 'quantity', 'unit_price']
> 
> class OrderSerializer(serializers.ModelSerializer):
>     items = OrderItemSerializer(many=True, read_only=True)
>     total_price = serializers.SerializerMethodField()
> 
>     class Meta:
>         model = Order
>         fields = ['id', 'customer', 'status', 'created_at', 'items', 'total_price']
> 
>     def get_total_price(self, obj):
>         # محاسبه مجموع قیمت فاکتور بر اساس اقلام
>         return sum(item.quantity * item.unit_price for item in obj.items.all())
> 
> class OrderCreateInputSerializer(serializers.Serializer):
>     cart_id = serializers.UUIDField()
>     shipping_address = serializers.CharField(min_length=10)
> ```
> 

> 56- اصلاح `apps/orders/views.py`
> 
> 
> در `get_queryset` کوئری را متصل به رابطه `customer__user` می‌کنیم تا فقط سفارشات خود کاربر جاری دریافت شوند:
> 
> ```jsx
> # apps/orders/views.py
> 
> from rest_framework import viewsets, permissions, status
> from rest_framework.response import Response
> from .models import Order
> from .serializers import OrderSerializer, OrderCreateInputSerializer
> from .services import OrderService
> 
> class OrderViewSet(viewsets.ModelViewSet):
>     permission_classes = [permissions.IsAuthenticated]
> 
>     def get_queryset(self):
>         # فیلتر سفارشات بر اساس کاربر جاری از طریق رابط Customer
>         return Order.objects.filter(
>             customer__user=self.request.user
>         ).prefetch_related('items__product').order_by('-created_at')
> 
>     def get_serializer_class(self):
>         if self.action == 'create':
>             return OrderCreateInputSerializer
>         return OrderSerializer
> 
>     def create(self, request, *args, **kwargs):
>         serializer = self.get_serializer(data=request.data)
>         serializer.is_valid(raise_exception=True)
> 
>         cart_id = serializer.validated_data['cart_id']
>         shipping_address = serializer.validated_data['shipping_address']
> 
>         order = OrderService.place_order(
>             user=request.user,
>             cart_id=cart_id,
>             shipping_address=shipping_address
>         )
> 
>         output_serializer = OrderSerializer(order)
>         return Response(output_serializer.data, status=status.HTTP_201_CREATED)
> ```
> 

🧪 تست مجدد

با ذخیره این دو فایل در بک‌اند، صفحه `/orders` را رفرش کن. حالا فاکتور سفارشی که ثبت کرده بودی با تمام جزئیات نمایش داده خواهد شد.

![image.png](image%202.png)

کد وضعیت **`200`** و حجم ۲۰۹۰ بایت در لاگ سرور نشان می‌دهد که بک‌اند اطلاعات سفارشات را با موفقیت تولید و ارسال کرده است. سفید شدن کامل صفحه در فرانت‌اند به این معنی است که کامپوننت ری‌اکت هنگام رندر کردن دیتای دریافتی دچار خطای جاوااسکریپت شده و اصطلاحاً Crash کرده است.

اصلی‌ترین علت این اتفاق در DRF این است که اگر **پجینیشن (Pagination)** در بک‌اند فعال باشد، دیتای خروجی به‌جای یک آرایه مستقیم (`[...]`)، به صورت یک شیء حاوی کلید `results` (یعنی `{ count: 1, results: [...] }`) ارسال می‌شود. در این حالت فراخوانی متد `orders.map` باعث خطای runtime شده و کل صفحه سفید می‌شود.

<aside>
💡

🛠️ کد دفاعی و امن `src/components/Orders.jsx`

</aside>

> 57- کد زیر را کاملاً جایگزین فایل **`src/components/Orders.jsx`** کن. این نسخه طوری طراحی شده که هم فرمت صفحه‌بندی‌شده DRF و هم فرمت آرایه ساده را پشتیبانی می‌کند و با برقراری گارد روی فیلدها، مانع سفید شدن صفحه می‌شود:
> 
> 
> ```jsx
> import React, { useEffect, useState } from 'react';
> import axiosInstance from '../api/axiosInstance';
> import { Link } from 'react-router-dom';
> 
> function Orders() {
>   const [orders, setOrders] = useState([]);
>   const [loading, setLoading] = useState(true);
>   const [error, setError] = useState('');
> 
>   // فرهنگ‌لغت نگاشت وضعیت‌های بک‌اند به عنوان و رنگ
>   const statusConfig = {
>     P: { label: 'در انتظار پرداخت', color: '#d97706', bgColor: '#fef3c7' },
>     C: { label: 'پرداخت موفق', color: '#16a34a', bgColor: '#dcfce7' },
>     X: { label: 'لغو شده', color: '#dc2626', bgColor: '#fee2e2' },
>   };
> 
>   useEffect(() => {
>     const fetchOrders = async () => {
>       try {
>         const response = await axiosInstance.get('orders/');
>         
>         // گارد امنیتی: استخراج آرایه سفارشات چه با پجینیشن چه بدون آن
>         const rawData = response.data;
>         const ordersArray = Array.isArray(rawData) 
>           ? rawData 
>           : (rawData?.results || []);
> 
>         setOrders(ordersArray);
>       } catch (err) {
>         console.error('خطا در دریافت سفارشات:', err);
>         setError('خطا در دریافت لیست سفارش‌ها. لطفاً مجدداً تلاش کنید.');
>       } finally {
>         setLoading(false);
>       }
>     };
> 
>     fetchOrders();
>   }, []);
> 
>   if (loading) {
>     return (
>       <div style={{ textAlign: 'center', marginTop: '50px', fontFamily: 'sans-serif', direction: 'rtl' }}>
>         در حال دریافت تاریخچه سفارشات... 🔄
>       </div>
>     );
>   }
> 
>   if (error) {
>     return (
>       <div style={{ textAlign: 'center', marginTop: '50px', color: '#dc2626', fontFamily: 'sans-serif', direction: 'rtl' }}>
>         {error}
>       </div>
>     );
>   }
> 
>   if (orders.length === 0) {
>     return (
>       <div style={{ textAlign: 'center', marginTop: '60px', fontFamily: 'sans-serif', direction: 'rtl' }}>
>         <h2>هنوز هیچ سفارشی ثبت نکرده‌اید 📦</h2>
>         <p style={{ color: '#64748b', marginTop: '10px' }}>محصولات مورد علاقه خود را انتخاب و سفارش دهید.</p>
>         <Link to="/products" style={{
>           display: 'inline-block',
>           marginTop: '15px',
>           padding: '10px 20px',
>           backgroundColor: '#2563eb',
>           color: 'white',
>           textDecoration: 'none',
>           borderRadius: '6px'
>         }}>
>           مشاهده کاتالوگ محصولات
>         </Link>
>       </div>
>     );
>   }
> 
>   return (
>     <div style={{ padding: '30px', maxWidth: '850px', margin: '0 auto', fontFamily: 'sans-serif', direction: 'rtl' }}>
>       <h2 style={{ marginBottom: '20px', color: '#0f172a' }}>سفارش‌های من ({orders.length})</h2>
> 
>       <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
>         {orders.map((order) => {
>           const status = statusConfig[order.status] || { label: order.status || 'نامشخص', color: '#475569', bgColor: '#f1f5f9' };
>           
>           let formattedDate = '---';
>           if (order.created_at) {
>             try {
>               formattedDate = new Date(order.created_at).toLocaleDateString('fa-IR');
>             } catch {
>               formattedDate = order.created_at;
>             }
>           }
> 
>           return (
>             <div key={order.id} style={{
>               border: '1px solid #e2e8f0',
>               borderRadius: '10px',
>               backgroundColor: '#fff',
>               overflow: 'hidden',
>               boxShadow: '0 2px 4px rgba(0,0,0,0.04)'
>             }}>
>               {/* سربرگ کارت سفارش */}
>               <div style={{
>                 padding: '15px 20px',
>                 backgroundColor: '#f8fafc',
>                 borderBottom: '1px solid #e2e8f0',
>                 display: 'flex',
>                 justifyContent: 'space-between',
>                 alignItems: 'center'
>               }}>
>                 <div>
>                   <span style={{ fontSize: '13px', color: '#64748b' }}>شناسه سفارش: </span>
>                   <strong style={{ fontSize: '14px', color: '#1e293b' }}>
>                     {order.id ? String(order.id).substring(0, 8) : '---'}...
>                   </strong>
>                   <span style={{ margin: '0 10px', color: '#cbd5e1' }}>|</span>
>                   <span style={{ fontSize: '13px', color: '#64748b' }}>تاریخ: {formattedDate}</span>
>                 </div>
> 
>                 <span style={{
>                   padding: '4px 12px',
>                   borderRadius: '20px',
>                   fontSize: '13px',
>                   fontWeight: 'bold',
>                   color: status.color,
>                   backgroundColor: status.bgColor
>                 }}>
>                   {status.label}
>                 </span>
>               </div>
> 
>               {/* اقلام داخلی سفارش */}
>               <div style={{ padding: '20px' }}>
>                 <h4 style={{ margin: '0 0 12px 0', fontSize: '15px', color: '#334155' }}>اقلام سفارش:</h4>
>                 <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
>                   {order.items && order.items.map((item) => (
>                     <li key={item.id} style={{
>                       padding: '8px 0',
>                       borderBottom: '1px dashed #f1f5f9',
>                       display: 'flex',
>                       justifyContent: 'space-between',
>                       alignItems: 'center'
>                     }}>
>                       <span style={{ color: '#0f172a' }}>
>                         {item.product_name || `محصول کد ${item.product}`}
>                       </span>
>                       <div style={{ fontSize: '14px', color: '#64748b' }}>
>                         <span style={{ marginLeft: '15px' }}>تعداد: {item.quantity}</span>
>                         {item.unit_price && (
>                           <span style={{ fontWeight: 'bold', color: '#0f172a' }}>
>                             {Number(item.unit_price).toLocaleString()} تومان
>                           </span>
>                         )}
>                       </div>
>                     </li>
>                   ))}
>                 </ul>
> 
>                 {/* مجموع کل فاکتور */}
>                 {order.total_price !== undefined && (
>                   <div style={{
>                     marginTop: '15px',
>                     paddingTop: '12px',
>                     borderTop: '1px solid #e2e8f0',
>                     textAlign: 'left',
>                     fontWeight: 'bold',
>                     color: '#059669'
>                   }}>
>                     مجموع فاکتور: {Number(order.total_price).toLocaleString()} تومان
>                   </div>
>                 )}
>               </div>
>             </div>
>           );
>         })}
>       </div>
>     </div>
>   );
> }
> 
> export default Orders;
> 
> ```
> 

🔍 نحوه چک کردن در مرورگر

پس از ذخیره فایل، صفحه را رفرش کن. اگر کماکان مشکلی وجود داشت، کافی است روی صفحه راست کلیک کرده، گزینه **Inspect** را بزنی و وارد تب **Console** شوی؛ متن دقیق ارور مشخص خواهد شد.

ارتباط فرانت‌اند و بک‌اند کاملاً برقرار شده و هر ۷ سفارش به‌خوبی دریافت شده و روی صفحه نمایش داده می‌شوند.

![image.png](image%203.png)

با بررسی تصاویر، **دو نکته مهم** وجود دارد که باید در این مرحله آن‌ها را بهبود دهیم:

1. **چسبیدن اعداد (تعداد و قیمت واحد):** اگر به تصویر دقت کنی، مثلاً برای ۱ عدد محصول ۱۲ تومانی، عبارت به صورت «تعداد: 112 تومان» دیده می‌شود! در واقع عدد `1` (تعداد) و `12` (قیمت واحد) به دلیل چیدمان متن کنار هم چسبیده‌اند.
2. **امکان پرداخت برای سفارش‌های معوقه:** سفارش‌هایی که وضعیت آن‌ها **«در انتظار پرداخت»** است، باید دکمه‌ای برای «پرداخت فاکتور» داشته باشند تا کاربر بتواند فرایند خرید را تکمیل کند

<aside>
💡

🛠️ کد به‌روزرسانی‌شده `src/components/Orders.jsx`

</aside>

کد زیر ظاهر کارت‌ها را مرتب کرده، اعداد تعداد و قیمت را از هم تفکیک می‌کند و دکمه **«پرداخت آنلاین»** را به سفارش‌های در انتظار پرداخت اضافه می‌کند:

> 58- 🛠️ کد به‌روزرسانی‌شده `src/components/Orders.jsx`
> 
> 
> ```jsx
> import React, { useEffect, useState } from 'react';
> import axiosInstance from '../api/axiosInstance';
> import { Link } from 'react-router-dom';
> 
> function Orders() {
>   const [orders, setOrders] = useState([]);
>   const [loading, setLoading] = useState(true);
>   const [error, setError] = useState('');
>   const [payingOrderId, setPayingOrderId] = useState(null);
> 
>   // وضعیت‌های سفارش
>   const statusConfig = {
>     P: { label: 'در انتظار پرداخت', color: '#d97706', bgColor: '#fef3c7' },
>     C: { label: 'پرداخت موفق', color: '#16a34a', bgColor: '#dcfce7' },
>     X: { label: 'لغو شده', color: '#dc2626', bgColor: '#fee2e2' },
>   };
> 
>   const fetchOrders = async () => {
>     try {
>       const response = await axiosInstance.get('orders/');
>       const rawData = response.data;
>       const ordersArray = Array.isArray(rawData) 
>         ? rawData 
>         : (rawData?.results || []);
> 
>       setOrders(ordersArray);
>     } catch (err) {
>       console.error('خطا در دریافت سفارشات:', err);
>       setError('خطا در دریافت لیست سفارش‌ها. لطفاً مجدداً تلاش کنید.');
>     } finally {
>       setLoading(false);
>     }
>   };
> 
>   useEffect(() => {
>     fetchOrders();
>   }, []);
> 
>   // شبیه‌سازی / اجرای پرداخت فاکتور
>   const handlePayment = async (orderId) => {
>     setPayingOrderId(orderId);
>     try {
>       // در مرحله بعد می‌توان این درخواست را به درگاه پرداخت یا اندپوینت مربوطه متصل کرد
>       alert(`در حال انتقال به درگاه پرداخت برای سفارش ${orderId.substring(0, 8)}...`);
>       // فراخوانی مجدد برای به‌روزرسانی وضعیت
>       await fetchOrders();
>     } catch (err) {
>       alert('خطا در پردازش پرداخت');
>     } finally {
>       setPayingOrderId(null);
>     }
>   };
> 
>   if (loading) {
>     return (
>       <div style={{ textAlign: 'center', marginTop: '50px', fontFamily: 'sans-serif', direction: 'rtl' }}>
>         در حال دریافت تاریخچه سفارشات... 🔄
>       </div>
>     );
>   }
> 
>   if (error) {
>     return (
>       <div style={{ textAlign: 'center', marginTop: '50px', color: '#dc2626', fontFamily: 'sans-serif', direction: 'rtl' }}>
>         {error}
>       </div>
>     );
>   }
> 
>   if (orders.length === 0) {
>     return (
>       <div style={{ textAlign: 'center', marginTop: '60px', fontFamily: 'sans-serif', direction: 'rtl' }}>
>         <h2>هنوز هیچ سفارشی ثبت نکرده‌اید 📦</h2>
>         <p style={{ color: '#64748b', marginTop: '10px' }}>محصولات مورد علاقه خود را انتخاب و سفارش دهید.</p>
>         <Link to="/products" style={{
>           display: 'inline-block',
>           marginTop: '15px',
>           padding: '10px 20px',
>           backgroundColor: '#2563eb',
>           color: 'white',
>           textDecoration: 'none',
>           borderRadius: '6px'
>         }}>
>           مشاهده کاتالوگ محصولات
>         </Link>
>       </div>
>     );
>   }
> 
>   return (
>     <div style={{ padding: '30px', maxWidth: '850px', margin: '0 auto', fontFamily: 'sans-serif', direction: 'rtl' }}>
>       <h2 style={{ marginBottom: '20px', color: '#0f172a' }}>سفارش‌های من ({orders.length})</h2>
> 
>       <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
>         {orders.map((order) => {
>           const status = statusConfig[order.status] || { label: order.status || 'نامشخص', color: '#475569', bgColor: '#f1f5f9' };
>           
>           let formattedDate = '---';
>           if (order.created_at) {
>             try {
>               formattedDate = new Date(order.created_at).toLocaleDateString('fa-IR');
>             } catch {
>               formattedDate = order.created_at;
>             }
>           }
> 
>           return (
>             <div key={order.id} style={{
>               border: '1px solid #e2e8f0',
>               borderRadius: '10px',
>               backgroundColor: '#fff',
>               overflow: 'hidden',
>               boxShadow: '0 2px 4px rgba(0,0,0,0.04)'
>             }}>
>               {/* سربرگ کارت */}
>               <div style={{
>                 padding: '15px 20px',
>                 backgroundColor: '#f8fafc',
>                 borderBottom: '1px solid #e2e8f0',
>                 display: 'flex',
>                 justifyContent: 'space-between',
>                 alignItems: 'center'
>               }}>
>                 <div>
>                   <span style={{ fontSize: '13px', color: '#64748b' }}>شناسه سفارش: </span>
>                   <strong style={{ fontSize: '14px', color: '#1e293b' }}>
>                     {order.id ? String(order.id).substring(0, 8) : '---'}...
>                   </strong>
>                   <span style={{ margin: '0 10px', color: '#cbd5e1' }}>|</span>
>                   <span style={{ fontSize: '13px', color: '#64748b' }}>تاریخ: {formattedDate}</span>
>                 </div>
> 
>                 <span style={{
>                   padding: '4px 12px',
>                   borderRadius: '20px',
>                   fontSize: '13px',
>                   fontWeight: 'bold',
>                   color: status.color,
>                   backgroundColor: status.bgColor
>                 }}>
>                   {status.label}
>                 </span>
>               </div>
> 
>               {/* لیست اقلام */}
>               <div style={{ padding: '20px' }}>
>                 <h4 style={{ margin: '0 0 12px 0', fontSize: '15px', color: '#334155' }}>اقلام سفارش:</h4>
>                 <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
>                   {order.items && order.items.map((item) => (
>                     <li key={item.id} style={{
>                       padding: '10px 0',
>                       borderBottom: '1px dashed #f1f5f9',
>                       display: 'flex',
>                       justifyContent: 'space-between',
>                       alignItems: 'center'
>                     }}>
>                       <span style={{ fontWeight: '500', color: '#0f172a' }}>
>                         {item.product_name || `محصول کد ${item.product}`}
>                       </span>
> 
>                       {/* تفکیک شفاف تعداد و قیمت */}
>                       <div style={{ display: 'flex', gap: '15px', alignItems: 'center', fontSize: '14px' }}>
>                         <span style={{
>                           backgroundColor: '#f1f5f9',
>                           padding: '3px 8px',
>                           borderRadius: '5px',
>                           color: '#475569',
>                           fontSize: '13px'
>                         }}>
>                           تعداد: <strong>{item.quantity}</strong>
>                         </span>
> 
>                         {item.unit_price && (
>                           <span style={{ color: '#0f172a' }}>
>                             قیمت واحد: <strong>{Number(item.unit_price).toLocaleString()}</strong> تومان
>                           </span>
>                         )}
>                       </div>
>                     </li>
>                   ))}
>                 </ul>
> 
>                 {/* بخش جمع کل و دکمه اقدام */}
>                 <div style={{
>                   marginTop: '15px',
>                   paddingTop: '15px',
>                   borderTop: '1px solid #e2e8f0',
>                   display: 'flex',
>                   justifyContent: 'space-between',
>                   alignItems: 'center'
>                 }}>
>                   {order.total_price !== undefined && (
>                     <div style={{ fontWeight: 'bold', color: '#059669', fontSize: '15px' }}>
>                       مجموع فاکتور: {Number(order.total_price).toLocaleString()} تومان
>                     </div>
>                   )}
> 
>                   {/* دکمه پرداخت فقط برای سفارش‌های در انتظار پرداخت */}
>                   {order.status === 'P' && (
>                     <button
>                       onClick={() => handlePayment(order.id)}
>                       disabled={payingOrderId === order.id}
>                       style={{
>                         backgroundColor: '#16a34a',
>                         color: 'white',
>                         border: 'none',
>                         padding: '8px 18px',
>                         borderRadius: '6px',
>                         cursor: 'pointer',
>                         fontSize: '14px',
>                         fontWeight: 'bold',
>                         transition: 'background-color 0.2s'
>                       }}
>                     >
>                       {payingOrderId === order.id ? 'در حال اتصال...' : 'پرداخت فاکتور 💳'}
>                     </button>
>                   )}
>                 </div>
>               </div>
>             </div>
>           );
>         })}
>       </div>
>     </div>
>   );
> }
> 
> export default Orders;
> 
> ```
> 

![image.png](image%204.png)

<aside>
💡

#### حالا که چرخه کامل **سبد خرید ➔ ثبت سفارش ➔ مشاهده فاکتورها** به درستی کار می‌کند، گام منطقی بعدی پیاده‌سازی **فرایند پرداخت (شبیه‌سازی درگاه پرداخت)** است؛ تا کاربر با کلیک روی «پرداخت فاکتور»، وضعیت سفارش از **«در انتظار پرداخت»** به **«پرداخت موفق»** تغییر کند و موجودی محصولات یا سبد خرید به‌روزرسانی شود.

</aside>

شبیه‌سازی درگاه پرداخت را در دو گام شفاف (بک‌اند و فرانت‌اند) پیاده‌سازی می‌کنیم.

در این سناریو، یک اکشن (Action) اختصاصی در DRF ایجاد می‌کنیم تا درخواست پرداخت را دریافت کند، وضعیت سفارش را از **`P` (در انتظار پرداخت)** به **`C` (پرداخت موفق)** تغییر دهد و در فرانت‌اند با کلیک روی دکمه پرداخت، این اندپوینت صدا زده شود.

<aside>
💡

🛠️ گام اول: افزودن اندپوینت پرداخت در بک‌اند

</aside>

در فریم‌ورک Django REST Framework، وقتی از `ModelViewSet` استفاده می‌کنیم، می‌توانیم با دکوراتور `@action` اندپوینت‌های سفارشی ایجاد کنیم.

> 59- فایل **`apps/orders/views.py`** را باز کرده و اکشن `pay` را به `OrderViewSet` اضافه کن:
> 
> 
> ```python
> # apps/orders/views.py
> 
> from rest_framework import viewsets, permissions, status
> from rest_framework.decorators import action
> from rest_framework.response import Response
> from .models import Order
> from .serializers import OrderSerializer, OrderCreateInputSerializer
> from .services import OrderService
> 
> class OrderViewSet(viewsets.ModelViewSet):
>     permission_classes = [permissions.IsAuthenticated]
> 
>     def get_queryset(self):
>         return Order.objects.filter(
>             customer__user=self.request.user
>         ).prefetch_related('items__product').order_by('-created_at')
> 
>     def get_serializer_class(self):
>         if self.action == 'create':
>             return OrderCreateInputSerializer
>         return OrderSerializer
> 
>     def create(self, request, *args, **kwargs):
>         serializer = self.get_serializer(data=request.data)
>         serializer.is_valid(raise_exception=True)
> 
>         cart_id = serializer.validated_data['cart_id']
>         shipping_address = serializer.validated_data['shipping_address']
> 
>         order = OrderService.place_order(
>             user=request.user,
>             cart_id=cart_id,
>             shipping_address=shipping_address
>         )
> 
>         output_serializer = OrderSerializer(order)
>         return Response(output_serializer.data, status=status.HTTP_201_CREATED)
> 
>     # ----------------------------------------------------
>     # اندپوینت سفارشی: POST /api/orders/{id}/pay/
>     # ----------------------------------------------------
>     @action(detail=True, methods=['post'], url_path='pay')
>     def pay(self, request, pk=None):
>         """
>         شبیه‌سازی تایید پرداخت درگاه آنلاین برای یک سفارش مشخص
>         """
>         order = self.get_object()
> 
>         # گارد: اگر سفارش قبلاً پرداخت شده یا لغو شده باشد
>         if order.status != 'P':
>             return Response(
>                 {"detail": "این سفارش در وضعیت «در انتظار پرداخت» نیست."},
>                 status=status.HTTP_400_BAD_REQUEST
>             )
> 
>         # تغییر وضعیت سفارش به پرداخت موفق
>         order.status = 'C'
>         order.save()
> 
>         return Response(
>             {
>                 "detail": "پرداخت با موفقیت انجام شد.",
>                 "order": OrderSerializer(order).data
>             },
>             status=status.HTTP_200_OK
>         )
> ```
> 

<aside>
💡

💡 دکوراتور `@action` چطور کار می‌کند؟

</aside>

- ا    **`detail=True`**: مشخص می‌کند این اندپوینت روی یک نمونه خاص کار می‌کند (`/api/orders/{id}/pay/`).
- ا   **`methods=['post']`**: فقط درخواست‌های HTTP POST را می‌پذیرد.
- ا   **`url_path='pay'`**: مسیر URL را برابر `pay` قرار می‌دهد.

<aside>
💡

🛠️ گام دوم: اتصال فرانت‌اند به اندپوینت پرداخت

</aside>

حالا تابع `handlePayment` در فایل **`src/components/Orders.jsx`** را به‌روزرسانی می‌کنیم تا درخواست واقعی به `POST /api/orders/{orderId}/pay/` ارسال شود.

> 60- فایل **`src/components/Orders.jsx`** را به شکل زیر به‌روزرسانی کن:
> 
> 
> ```jsx
> import React, { useEffect, useState } from 'react';
> import axiosInstance from '../api/axiosInstance';
> import { Link } from 'react-router-dom';
> 
> function Orders() {
>   const [orders, setOrders] = useState([]);
>   const [loading, setLoading] = useState(true);
>   const [error, setError] = useState('');
>   const [payingOrderId, setPayingOrderId] = useState(null);
> 
>   const statusConfig = {
>     P: { label: 'در انتظار پرداخت', color: '#d97706', bgColor: '#fef3c7' },
>     C: { label: 'پرداخت موفق', color: '#16a34a', bgColor: '#dcfce7' },
>     X: { label: 'لغو شده', color: '#dc2626', bgColor: '#fee2e2' },
>   };
> 
>   const fetchOrders = async () => {
>     try {
>       const response = await axiosInstance.get('orders/');
>       const rawData = response.data;
>       const ordersArray = Array.isArray(rawData) 
>         ? rawData 
>         : (rawData?.results || []);
> 
>       setOrders(ordersArray);
>     } catch (err) {
>       console.error('خطا در دریافت سفارشات:', err);
>       setError('خطا در دریافت لیست سفارش‌ها. لطفاً مجدداً تلاش کنید.');
>     } finally {
>       setLoading(false);
>     }
>   };
> 
>   useEffect(() => {
>     fetchOrders();
>   }, []);
> 
>   // ارسال درخواست پردازش پرداخت به بک‌اند
>   const handlePayment = async (orderId) => {
>     setPayingOrderId(orderId);
>     try {
>       await axiosInstance.post(`orders/${orderId}/pay/`);
>       
>       alert('پرداخت با موفقیت انجام شد! 💳✨');
>       
>       // دریافت مجدد اطلاعات سفارشات برای به‌روزرسانی وضعیت روی صفحه
>       await fetchOrders();
>     } catch (err) {
>       console.error('خطا در پرداخت:', err);
>       const serverMessage = err.response?.data?.detail || 'خطایی در پردازش پرداخت رخ داد.';
>       alert(serverMessage);
>     } finally {
>       setPayingOrderId(null);
>     }
>   };
> 
>   if (loading) {
>     return (
>       <div style={{ textAlign: 'center', marginTop: '50px', fontFamily: 'sans-serif', direction: 'rtl' }}>
>         در حال دریافت تاریخچه سفارشات... 🔄
>       </div>
>     );
>   }
> 
>   if (error) {
>     return (
>       <div style={{ textAlign: 'center', marginTop: '50px', color: '#dc2626', fontFamily: 'sans-serif', direction: 'rtl' }}>
>         {error}
>       </div>
>     );
>   }
> 
>   if (orders.length === 0) {
>     return (
>       <div style={{ textAlign: 'center', marginTop: '60px', fontFamily: 'sans-serif', direction: 'rtl' }}>
>         <h2>هنوز هیچ سفارشی ثبت نکرده‌اید 📦</h2>
>         <p style={{ color: '#64748b', marginTop: '10px' }}>محصولات مورد علاقه خود را انتخاب و سفارش دهید.</p>
>         <Link to="/products" style={{
>           display: 'inline-block',
>           marginTop: '15px',
>           padding: '10px 20px',
>           backgroundColor: '#2563eb',
>           color: 'white',
>           textDecoration: 'none',
>           borderRadius: '6px'
>         }}>
>           مشاهده کاتالوگ محصولات
>         </Link>
>       </div>
>     );
>   }
> 
>   return (
>     <div style={{ padding: '30px', maxWidth: '850px', margin: '0 auto', fontFamily: 'sans-serif', direction: 'rtl' }}>
>       <h2 style={{ marginBottom: '20px', color: '#0f172a' }}>سفارش‌های من ({orders.length})</h2>
> 
>       <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
>         {orders.map((order) => {
>           const status = statusConfig[order.status] || { label: order.status || 'نامشخص', color: '#475569', bgColor: '#f1f5f9' };
>           
>           let formattedDate = '---';
>           if (order.created_at) {
>             try {
>               formattedDate = new Date(order.created_at).toLocaleDateString('fa-IR');
>             } catch {
>               formattedDate = order.created_at;
>             }
>           }
> 
>           return (
>             <div key={order.id} style={{
>               border: '1px solid #e2e8f0',
>               borderRadius: '10px',
>               backgroundColor: '#fff',
>               overflow: 'hidden',
>               boxShadow: '0 2px 4px rgba(0,0,0,0.04)'
>             }}>
>               {/* سربرگ کارت */}
>               <div style={{
>                 padding: '15px 20px',
>                 backgroundColor: '#f8fafc',
>                 borderBottom: '1px solid #e2e8f0',
>                 display: 'flex',
>                 justifyContent: 'space-between',
>                 alignItems: 'center'
>               }}>
>                 <div>
>                   <span style={{ fontSize: '13px', color: '#64748b' }}>شناسه سفارش: </span>
>                   <strong style={{ fontSize: '14px', color: '#1e293b' }}>
>                     {order.id ? String(order.id).substring(0, 8) : '---'}...
>                   </strong>
>                   <span style={{ margin: '0 10px', color: '#cbd5e1' }}>|</span>
>                   <span style={{ fontSize: '13px', color: '#64748b' }}>تاریخ: {formattedDate}</span>
>                 </div>
> 
>                 <span style={{
>                   padding: '4px 12px',
>                   borderRadius: '20px',
>                   fontSize: '13px',
>                   fontWeight: 'bold',
>                   color: status.color,
>                   backgroundColor: status.bgColor
>                 }}>
>                   {status.label}
>                 </span>
>               </div>
> 
>               {/* لیست اقلام */}
>               <div style={{ padding: '20px' }}>
>                 <h4 style={{ margin: '0 0 12px 0', fontSize: '15px', color: '#334155' }}>اقلام سفارش:</h4>
>                 <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
>                   {order.items && order.items.map((item) => (
>                     <li key={item.id} style={{
>                       padding: '10px 0',
>                       borderBottom: '1px dashed #f1f5f9',
>                       display: 'flex',
>                       justifyContent: 'space-between',
>                       alignItems: 'center'
>                     }}>
>                       <span style={{ fontWeight: '500', color: '#0f172a' }}>
>                         {item.product_name || `محصول کد ${item.product}`}
>                       </span>
> 
>                       <div style={{ display: 'flex', gap: '15px', alignItems: 'center', fontSize: '14px' }}>
>                         <span style={{
>                           backgroundColor: '#f1f5f9',
>                           padding: '3px 8px',
>                           borderRadius: '5px',
>                           color: '#475569',
>                           fontSize: '13px'
>                         }}>
>                           تعداد: <strong>{item.quantity}</strong>
>                         </span>
> 
>                         {item.unit_price && (
>                           <span style={{ color: '#0f172a' }}>
>                             قیمت واحد: <strong>{Number(item.unit_price).toLocaleString()}</strong> تومان
>                           </span>
>                         )}
>                       </div>
>                     </li>
>                   ))}
>                 </ul>
> 
>                 {/* جمع کل و دکمه پرداخت */}
>                 <div style={{
>                   marginTop: '15px',
>                   paddingTop: '15px',
>                   borderTop: '1px solid #e2e8f0',
>                   display: 'flex',
>                   justifyContent: 'space-between',
>                   alignItems: 'center'
>                 }}>
>                   {order.total_price !== undefined && (
>                     <div style={{ fontWeight: 'bold', color: '#059669', fontSize: '15px' }}>
>                       مجموع فاکتور: {Number(order.total_price).toLocaleString()} تومان
>                     </div>
>                   )}
> 
>                   {order.status === 'P' && (
>                     <button
>                       onClick={() => handlePayment(order.id)}
>                       disabled={payingOrderId === order.id}
>                       style={{
>                         backgroundColor: payingOrderId === order.id ? '#94a3b8' : '#16a34a',
>                         color: 'white',
>                         border: 'none',
>                         padding: '8px 18px',
>                         borderRadius: '6px',
>                         cursor: payingOrderId === order.id ? 'not-allowed' : 'pointer',
>                         fontSize: '14px',
>                         fontWeight: 'bold',
>                         transition: 'background-color 0.2s'
>                       }}
>                     >
>                       {payingOrderId === order.id ? 'در حال پرداخت...' : 'پرداخت فاکتور 💳'}
>                     </button>
>                   )}
>                 </div>
>               </div>
>             </div>
>           );
>         })}
>       </div>
>     </div>
>   );
> }
> 
> export default Orders;
> 
> ```
> 

🧪 نحوه تست

- روی دکمه **«پرداخت فاکتور 💳»** یکی از سفارش‌های در انتظار پرداخت کلیک کن.
- پیام «پرداخت با موفقیت انجام شد!» نمایش داده می‌شود.
- بلافاصله بدون نیاز به رفرش دستی، لیبل وضعیت سفارش به **«پرداخت موفق»** (سبزرنگ) تغییر یافته و دکمه پرداخت از روی آن فاکتور ناپدید می‌شود.

![image.png](image%205.png)

<aside>
💡

🧠 اصول S.O.L.I.D به زبان ساده و کاربردی

</aside>

پنج اصل S.O.L.I.D راهنمای ما برای نوشتن کدهای تمیز (Clean Code) در برنامه‌نویسی شیءگرا هستند:

<aside>
💡

1- ا Single Responsibility Principle (SRP) - اصل تک‌مسئولیتی

</aside>

- **مفهوم:** هر کلاس، کامپوننت یا ماژول فقط باید **یک دلیل برای تغییر** داشته باشد (فقط یک وظیفه مشخص).
- **کاربرد در پروژه:**
    - **در بک‌اند:** ViewSet نباید خودش الگوریتم‌های پیچیده مالی یا انبارداری را محاسبه کند؛ این کار به `Service`ها منتقل می‌شود.
    - **در فرانت‌اند:** کامپوننت `AddressCard` فقط مسئول نمایش کارت آدرس است و نباید فرم ویرایش یا منطق API را داخل خودش جا دهد.

<aside>
💡

2-ا Open/Closed Principle (OCP) - اصل باز/بسته

</aside>

- **مفهوم:** کدهای ما باید برای **توسعه باز** (Open for extension) اما برای **تغییر بسته** (Closed for modification) باشند.
- **کاربرد در پروژه:** وقتی می‌خواهیم قابلیت جدیدی (مثل روش‌های جدید محاسبه هزینه پست) اضافه کنیم، نباید کدهای قبلی را با دست‌کاری و شرط‌های `if/else` فراوان خراب کنیم؛ بلکه با الگوهای طراحی کلاس جدیدی اضافه می‌کنیم که از ساختار قبلی پیروی می‌کند.

<aside>
💡

3-ا Liskov Substitution Principle (LSP) - اصل جانشینی لیسکوف

</aside>

- **مفهوم:** کلاس‌های فرزند باید بتوانند بدون ایجاد خطا یا تغییر رفتار نادرست در برنامه، جایگزین کلاس والد (پدر) خود شوند.
- **کاربرد در پروژه:** در Django اگر یک `CustomUser` از `AbstractUser` ارث‌بری می‌کند، باید دقیقاً تمام رفتارهای استاندارد کاربر جنگو را پشتیبانی کند تا سیستم احراز هویت دچار مشکل نشود.

<aside>
💡

4-ا Interface Segregation Principle (ISP) - اصل تفکیک رابط‌ها

</aside>

- **مفهوم:** کلاینت‌ها (یا کامپوننت‌ها) نباید مجبور شوند به متدها یا دیتاهایی وابسته شوند که به آن‌ها نیازی ندارند.
- **کاربرد در پروژه:** در فرانت‌اند، به جای فرستادن کل کلیدهای شیء بزرگ `User` به کامپوننتی که فقط به اسم و عکس نیاز دارد، فقط همان مقادیر مورد نیاز را به عنوان `props` می‌فرستیم.

<aside>
💡

5-ا Dependency Inversion Principle (DIP) - اصل وارونگی وابستگی

</aside>

- **مفهوم:** ماژول‌های سطح بالا (های‌لِوِل) نباید به ماژول‌های سطح پایین وابسته باشند؛ هر دو باید به یک «انتزاع» (Abstraction) وابسته باشند.
- **کاربرد در پروژه:** در فرانت‌اند به جای درخواست مستقیم `fetch()` در هر فایل، یک ماژول متمرکز `axiosInstance` ساختیم تا کل فرانت به آن وابسته باشد. اگر فردا بخواهیم توکن را عوض کنیم، فقط یک جا تغییر داده می‌شود.

<aside>
💡

**🛠️ گام اول: پیاده‌سازی مدیریت آدرس‌ها در بک‌اند (Django REST Framework)**

</aside>

> 61- این فایل را بر اساس کد زیر جایگزین کنید:
> 
> 
> ```python
> # acron/backend/apps/customers/models.py
> 
> from django.db import models
> from django.conf import settings
> 
> class Customer(models.Model):
>     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
>     phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
>     birth_date = models.DateField(null=True, blank=True)
> 
>     def __str__(self):
>         return f"{self.user.first_name} {self.user.last_name}"
> 
> class Address(models.Model):
>     customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='addresses')
>     title = models.CharField(max_length=50,help_text="مثال: خانه، محل کار",null=True,blank=True)
>     receiver_name = models.CharField(max_length=100,null=True,blank=True)
>     phone_number = models.CharField(max_length=15,null=True,blank=True)
>     province = models.CharField(max_length=50)
>     city = models.CharField(max_length=50)
>     street = models.TextField()
>     postal_code = models.CharField(max_length=10)
>     is_default = models.BooleanField(default=False)
>     created_at = models.DateTimeField(auto_now_add=True)
>     
>     
>     
>     
>     
>     
> ```
> 
> درترمینال بنویسید: دقت کنید عدد 1 را وارد کنید سپس
> timezone.now()
> را بنویسید و Enter بزنید
> 
> ```python
> $python manage.py makemigrations customers
> It is impossible to add the field 'created_at' with 'auto_now_add=True' to address without providing a default. This is because the database needs something to populate existing rows.
>  1) Provide a one-off default now which will be set on all existing rows
>  2) Quit and manually define a default value in models.py.
> Select an option: 1
> Please enter the default value as valid Python.
> Accept the default 'timezone.now' by pressing 'Enter' or provide another value.
> The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
> Type 'exit' to exit this prompt
> [default: timezone.now] >>> timezone.now()
> Migrations for 'customers':
>   apps\customers\migrations\0004_address_created_at_address_is_default_and_more.py
>     + Add field created_at to address
>     + Add field is_default to address
>     + Add field phone_number to address
>     + Add field receiver_name to address
>     + Add field title to address
>     ~ Alter field city on address
>     ~ Alter field postal_code on address
>     ~ Alter field province on address
>     ~ Alter field street on address
> 
> ```
> 
> سپس بنویسید:
> 
> ```python
> python manage.py migrate
> ```
> 
> انتظار می رود نتیجه مشابه زیر باشد:
> 
> ```python
> $ python manage.py migrate
> Operations to perform:
>   Apply all migrations: accounts, admin, advisor, auth, carts, contenttypes, customers, orders, payments, products, sessions, shipments
> Running migrations:
>   Applying customers.0004_address_created_at_address_is_default_and_more... OK
> 
> ```
> 

با داشتن رابطه بین `User` و `Customer` و متصل بودن `Address` به `Customer` (ارتباط یک به چند)، دقیقاً بر اساس همین ساختار کدمان را تنظیم می‌کنیم تا اصل **DRY (Don't Repeat Yourself)** و **SRP** رعایت شود و نیازی به دوباره‌کاری یا تغییر مدل‌های فعلی دیتابیس نباشد.

نکته‌ای که در مدل شما وجود دارد این است که نام فیلد آدرس متنی **`street`** است (نه `full_address`). تمام لایه‌ها را بر همین اساس پیاده‌سازی می‌کنیم.

برای رعایت **SRP**، مدل آدرس‌ها و سرویس‌های مرتبط با پروفایل کاربر را در اپلیکیشن مربوط به کاربران/پروفایل قرار می‌دهیم.

ارتباط دادن `Address` به مدل `Customer` (به‌جای ارتباط مستقیم با User) چند مزیت بزرگ دارد:

1. **رعایت اصل SRP:** مدل User جنگو فقط مسئول هویت و احراز هویت باقی می‌ماند و تمام اطلاعات مربوط به مشتری فروشگاه (تلفن، تاریخ تولد، آدرس‌ها) در مدل `Customer` کپسوله می‌شود.
2. **یکپارچگی با بخش سفارشات:** در بخش‌های قبلی (مثل `OrderViewSet`) هم از رابطه `customer__user` استفاده کرده بودیم، بنابراین کدی که نوشتی کاملاً هم‌راستا با ساختار قبلی دیتابیس است.

نیازی به تغییر در `models.py` نداری. فقط بقیه لایه‌ها (سرویس، سریالایزر و ویوها) را متناسب با مدل خودت تنظیم می‌کنیم.

<aside>
💡

🛠️ پیاده‌سازی لایه‌های DRF روی ساختار موجود `apps/customers`

</aside>

فایل‌های زیر را در همان اپلیکیشن `apps/customers` قرار بده یا ویرایش کن:

> 62- لایه منطق کسب‌وکار (`apps/customers/services.py`)
> 
> 
> فایل **`apps/customers/services.py`** را ایجاد یا به‌روزرسانی کن:
> 
> ```jsx
> from django.db import transaction
> from .models import Customer, Address
> 
> class AddressService:
>     @staticmethod
>     @transaction.atomic
>     def set_default_address(user, address_id):
>         """
>         تنظیم آدرس پیش‌فرض برای کاربر و غیرفعال کردن بقیه آدرس‌ها
>         """
>         customer = Customer.objects.get(user=user)
>         
>         # تمام آدرس‌های فعلی کاربر از حالت پیش‌فرض خارج می‌شوند
>         Address.objects.filter(customer=customer, is_default=True).update(is_default=False)
>         
>         # آدرس انتخابی پیش‌فرض می‌شود
>         address = Address.objects.get(id=address_id, customer=customer)
>         address.is_default = True
>         address.save()
>         return address
>         
>         
>   
> ```
> 

> 63- لایه تبدیل داده‌ها (`apps/customers/serializers.py`)
> 
> 
> فایل **`apps/customers/serializers.py`** را به شکل زیر تنظیم کن:
> 
> ```jsx
> 
> class AddressSerializer(serializers.ModelSerializer):
>     class Meta:
>         model = Address
>         fields = [
>             'id', 'title', 'receiver_name', 'phone_number',
>             'province', 'city', 'street', 'postal_code',
>             'is_default', 'created_at'
>         ]
>         read_only_fields = ['id', 'created_at']
> 
> class ProfileSerializer(serializers.ModelSerializer):
>     addresses = serializers.SerializerMethodField()
>     customer_phone = serializers.CharField(source='customer.phone_number', read_only=True)
>     birth_date = serializers.DateField(source='customer.birth_date', read_only=True)
> 
>     class Meta:
>         model = User
>         fields = [
>             'id', 'username', 'email', 'first_name', 
>             'last_name', 'customer_phone', 'birth_date', 'addresses'
>         ]
> 
>     def get_addresses(self, obj):
>         # دریافت لیست آدرس‌ها از طریق رابطه Customer
>         if hasattr(obj, 'customer'):
>             addresses = obj.customer.addresses.all()
>             return AddressSerializer(addresses, many=True).data
>         return []
> ```
> 

برای تکمیل آن و اضافه کردن قابلیت **تنظیم آدرس پیش‌فرض** (با حفظ تمام ویوهای قبلی مثل `CustomerMeView` و `CustomerProfileView`)، تنها کافی است موارد زیر به `AddressViewSet` اضافه شوند:

1. وارد کردن `status` و دکوراتور `action` از DRF.
2. وارد کردن `AddressService` از فایل `services.py`.
3. افزودن متد `@action` به `AddressViewSet` برای تغییر آدرس پیش‌فرض.
4. به‌روزرسانی متد `perform_create` در `AddressViewSet` تا اگر اولین آدرس کاربر ساخته می‌شود، خودکار پیش‌فرض شود.

> 64- لایه کنترلر (`apps/customers/views.py`)
> 
> 
> فایل **`apps/customers/views.py`** را ویرایش کن:
> 
> ```jsx
> from rest_framework import status
> from rest_framework.response import Response
> from rest_framework.views import APIView
> from rest_framework.permissions import IsAuthenticated
> from rest_framework.viewsets import ModelViewSet
> from rest_framework.generics import RetrieveUpdateAPIView
> from rest_framework.decorators import action
> 
> from .models import Customer, Address
> from .serializers import CustomerProfileSerializer, AddressSerializer, CustomerSerializer
> from .services import AddressService
> 
> class CustomerMeView(APIView):
>     permission_classes = [IsAuthenticated]
> 
>     def get(self, request):
>         customer, _ = Customer.objects.get_or_create(user=request.user)
>         serializer = CustomerSerializer(customer)
>         return Response(serializer.data)
> 
>     def patch(self, request):
>         customer, _ = Customer.objects.get_or_create(user=request.user)
>         serializer = CustomerSerializer(customer, data=request.data, partial=True)
>         serializer.is_valid(raise_exception=True)
>         serializer.save()
>         return Response(serializer.data)
> 
> class CustomerProfileView(RetrieveUpdateAPIView):
>     """
>     این ویو برای مشاهده و ویرایش پروفایل کاربری خود شخص است.
>     """
>     serializer_class = CustomerProfileSerializer
>     permission_classes = [IsAuthenticated]
> 
>     def get_object(self):
>         # این متد باعث می‌شود نیازی به ارسال ID در URL نباشد.
>         # کاربر بر اساس توکنی که می‌فرستد، فقط پروفایل خودش را دریافت می‌کند.
>         customer, created = Customer.objects.get_or_create(user=self.request.user)
>         return customer
> 
> class AddressViewSet(ModelViewSet):
>     """
>     مدیریت آدرس‌های پستی کاربر
>     """
>     serializer_class = AddressSerializer
>     permission_classes = [IsAuthenticated]
> 
>     def get_queryset(self):
>         # هر کاربر فقط آدرس‌های خودش را می‌بیند
>         return Address.objects.filter(customer__user=self.request.user)
> 
>     def perform_create(self, serializer):
>         customer, _ = Customer.objects.get_or_create(user=self.request.user)
>         
>         # اگر این اولین آدرس کاربر باشد، به صورت خودکار پیش‌فرض می‌شود
>         is_first = not Address.objects.filter(customer=customer).exists()
>         
>         # اگر کاربر آدرس جدید را پیش‌فرض انتخاب کرده یا اولین آدرسش است
>         if serializer.validated_data.get('is_default', False) or is_first:
>             Address.objects.filter(customer=customer, is_default=True).update(is_default=False)
>             serializer.save(customer=customer, is_default=True)
>         else:
>             serializer.save(customer=customer)
> 
>     @action(detail=True, methods=['post'], url_path='set-default')
>     def set_default(self, request, pk=None):
>         """
>         اکشن اختصاصی برای انتخاب آدرس پیش‌فرض:
>         POST /api/customers/addresses/{id}/set-default/
>         """
>         try:
>             address = AddressService.set_default_address(request.user, pk)
>             return Response(
>                 {
>                     "detail": "آدرس پیش‌فرض با موفقیت تغییر کرد.",
>                     "address": AddressSerializer(address).data
>                 },
>                 status=status.HTTP_200_OK
>             )
>         except (Address.DoesNotExist, Customer.DoesNotExist):
>             return Response(
>                 {"detail": "آدرس یا مشتری یافت نشد."},
>                 status=status.HTTP_404_NOT_FOUND
>             )
>     
>     
>     
> ```
> 

> 65- تنظیم مسیرها (`apps/customers/urls.py`)
> 
> 
> فایل **`apps/customers/urls.py`** را باز کرده و روتر را پیکربندی کن:
> 
> ```jsx
> from django.urls import path, include
> from rest_framework.routers import DefaultRouter
> from .views import AddressViewSet, UserProfileView
> 
> router = DefaultRouter()
> router.register(r'addresses', AddressViewSet, basename='address')
> 
> urlpatterns = [
>     path('profile/', UserProfileView.as_view(), name='user-profile'),
>     path('', include(router.urls)),
> ]
> 
> ```
> 

*(مطمئن شو مسیر `apps.customers.urls` در `urls.py` اصلی پروژه با پیشوند مناسب مثل `api/` یا `api/customers/` اضافه شده باشد).*

💡 چه تغییراتی اعمال شد؟

1. **تضمین وجود Customer**: در `CustomerMeView` از `get_or_create` استفاده شد تا اگر کاربری پروفایل `Customer` نداشت، خطای `RelatedObjectDoesNotExist` رخ ندهد.
2. **رعایت SRP در اکشن `set_default`**: منطق تغییر آدرس‌های پیش‌فرض قبلی به سرویس `AddressService` سپرده شده تا `ViewSet` شلوغ نشود.
3. **هوشمندسازی ساخت آدرس**: موقع ساخت آدرس جدید، اگر کاربر هنوز هیچ آدرسی ندارد، اولین آدرس به‌صورت خودکار `is_default=True` می‌شود.

<aside>
💡

نقشه راه ادامه توسعه در این مرحله به صورت زیر است:

</aside>

- **ساخت کامپوننت `Profile.jsx`:** صفحه‌ای برای نمایش اطلاعات کاربر + فرم ثبت و لیست آدرس‌ها.
- **افزودن مسیر در `App.jsx` و `Navbar.jsx`:** ایجاد مسیر `/profile` و اضافه کردن دکمه آن در منوی بالای صفحه.
- **ارتقای فرایند ثبت سفارش در سبد خرید:** استفاده از آدرس‌های ذخیره‌شده کاربر به‌جای تایپ دستی آدرس.

<aside>
💡

🛠️ گام اول فرانت‌اند: ساخت کامپوننت `src/components/Profile.jsx`

</aside>

با رعایت اصل **SRP (تک‌مسئولیتی)**، این کامپوننت مسئول دریافت اطلاعات پروفایل، نمایش آدرس‌ها، ساخت آدرس جدید و تغییر آدرس پیش‌فرض است.

> 66- یک فایل جدید به نام **`src/components/Profile.jsx`** ایجاد کرده و کد زیر را در آن قرار بده:
> 
> 
> ```jsx
> import React, { useEffect, useState } from 'react';
> import axiosInstance from '../api/axiosInstance';
> 
> function Profile() {
>   const [profile, setProfile] = useState(null);
>   const [addresses, setAddresses] = useState([]);
>   const [loading, setLoading] = useState(true);
>   const [error, setError] = useState('');
> 
>   // وضعیت فرم آدرس جدید
>   const [showAddForm, setShowAddForm] = useState(false);
>   const [newAddress, setNewAddress] = useState({
>     title: '',
>     receiver_name: '',
>     phone_number: '',
>     province: '',
>     city: '',
>     street: '',
>     postal_code: '',
>   });
>   const [submitting, setSubmitting] = useState(false);
> 
>   // دریافت اطلاعات پروفایل و آدرس‌ها
>   const fetchProfileData = async () => {
>     try {
>       const response = await axiosInstance.get('customers/profile/');
>       setProfile(response.data);
>       setAddresses(response.data.addresses || []);
>     } catch (err) {
>       console.error('خطا در دریافت پروفایل:', err);
>       setError('خطا در دریافت اطلاعات پروفایل.');
>     } finally {
>       setLoading(false);
>     }
>   };
> 
>   useEffect(() => {
>     fetchProfileData();
>   }, []);
> 
>   // تغییر آدرس پیش‌فرض
>   const handleSetDefault = async (addressId) => {
>     try {
>       await axiosInstance.post(`customers/addresses/${addressId}/set-default/`);
>       fetchProfileData(); // به‌روزرسانی لیست
>     } catch (err) {
>       alert('خطا در تغییر آدرس پیش‌فرض');
>     }
>   };
> 
>   // ثبت آدرس جدید
>   const handleAddAddress = async (e) => {
>     e.preventDefault();
>     setSubmitting(true);
>     try {
>       await axiosInstance.post('customers/addresses/', newAddress);
>       setShowAddForm(false);
>       setNewAddress({
>         title: '',
>         receiver_name: '',
>         phone_number: '',
>         province: '',
>         city: '',
>         street: '',
>         postal_code: '',
>       });
>       fetchProfileData();
>     } catch (err) {
>       alert('خطا در ثبت آدرس جدید. لطفاً ورودی‌ها را بررسی کنید.');
>     } finally {
>       setSubmitting(false);
>     }
>   };
> 
>   // حذف آدرس
>   const handleDeleteAddress = async (addressId) => {
>     if (!window.confirm('آیا از حذف این آدرس اطمینان دارید؟')) return;
>     try {
>       await axiosInstance.delete(`customers/addresses/${addressId}/`);
>       fetchProfileData();
>     } catch (err) {
>       alert('خطا در حذف آدرس');
>     }
>   };
> 
>   if (loading) {
>     return <div style={{ textAlign: 'center', marginTop: '50px', direction: 'rtl' }}>در حال دریافت اطلاعات کاربر... 🔄</div>;
>   }
> 
>   if (error) {
>     return <div style={{ textAlign: 'center', marginTop: '50px', color: '#dc2626', direction: 'rtl' }}>{error}</div>;
>   }
> 
>   return (
>     <div style={{ padding: '30px', maxWidth: '850px', margin: '0 auto', fontFamily: 'sans-serif', direction: 'rtl' }}>
>       
>       {/* کارت اطلاعات کاربر */}
>       <div style={{
>         backgroundColor: '#fff',
>         border: '1px solid #e2e8f0',
>         borderRadius: '10px',
>         padding: '20px',
>         marginBottom: '25px',
>         boxShadow: '0 2px 4px rgba(0,0,0,0.03)'
>       }}>
>         <h2 style={{ margin: '0 0 15px 0', color: '#0f172a' }}>پروفایل کاربری 👤</h2>
>         <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px', color: '#334155' }}>
>           <div><strong>نام کاربری:</strong> {profile?.username}</div>
>           <div><strong>ایمیل:</strong> {profile?.email || 'ثبت نشده'}</div>
>           <div><strong>نام و نام خانوادگی:</strong> {profile?.first_name} {profile?.last_name}</div>
>           <div><strong>شماره تماس:</strong> {profile?.customer_phone || 'ثبت نشده'}</div>
>         </div>
>       </div>
> 
>       {/* بخش آدرس‌ها */}
>       <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '15px' }}>
>         <h3 style={{ margin: 0, color: '#0f172a' }}>آدرس‌های پستی من ({addresses.length}) 📍</h3>
>         <button
>           onClick={() => setShowAddForm(!showAddForm)}
>           style={{
>             backgroundColor: showAddForm ? '#64748b' : '#2563eb',
>             color: '#fff',
>             border: 'none',
>             padding: '8px 16px',
>             borderRadius: '6px',
>             cursor: 'pointer',
>             fontWeight: 'bold'
>           }}
>         >
>           {showAddForm ? 'انصراف' : '+ افزودن آدرس جدید'}
>         </button>
>       </div>
> 
>       {/* فرم افزودن آدرس جدید */}
>       {showAddForm && (
>         <form onSubmit={handleAddAddress} style={{
>           backgroundColor: '#f8fafc',
>           border: '1px solid #cbd5e1',
>           borderRadius: '10px',
>           padding: '20px',
>           marginBottom: '25px'
>         }}>
>           <h4 style={{ marginTop: 0, color: '#1e293b' }}>افزودن آدرس پستی جدید</h4>
>           
>           <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px', marginBottom: '12px' }}>
>             <input
>               type="text"
>               placeholder="عنوان (مثلاً خانه، محل کار)"
>               value={newAddress.title}
>               onChange={(e) => setNewAddress({ ...newAddress, title: e.target.value })}
>               required
>               style={inputStyle}
>             />
>             <input
>               type="text"
>               placeholder="نام گیرنده"
>               value={newAddress.receiver_name}
>               onChange={(e) => setNewAddress({ ...newAddress, receiver_name: e.target.value })}
>               required
>               style={inputStyle}
>             />
>             <input
>               type="text"
>               placeholder="شماره تماس گیرنده"
>               value={newAddress.phone_number}
>               onChange={(e) => setNewAddress({ ...newAddress, phone_number: e.target.value })}
>               required
>               style={inputStyle}
>             />
>             <input
>               type="text"
>               placeholder="کد پستی (۱۰ رقمی)"
>               value={newAddress.postal_code}
>               onChange={(e) => setNewAddress({ ...newAddress, postal_code: e.target.value })}
>               required
>               style={inputStyle}
>             />
>             <input
>               type="text"
>               placeholder="استان"
>               value={newAddress.province}
>               onChange={(e) => setNewAddress({ ...newAddress, province: e.target.value })}
>               required
>               style={inputStyle}
>             />
>             <input
>               type="text"
>               placeholder="شهر"
>               value={newAddress.city}
>               onChange={(e) => setNewAddress({ ...newAddress, city: e.target.value })}
>               required
>               style={inputStyle}
>             />
>           </div>
> 
>           <textarea
>             placeholder="آدرس دقیق پستی (خیابان، کوچه، پلاک، واحد)"
>             value={newAddress.street}
>             onChange={(e) => setNewAddress({ ...newAddress, street: e.target.value })}
>             required
>             rows="3"
>             style={{ ...inputStyle, width: '100%', marginBottom: '15px' }}
>           />
> 
>           <button
>             type="submit"
>             disabled={submitting}
>             style={{
>               backgroundColor: '#16a34a',
>               color: '#fff',
>               border: 'none',
>               padding: '10px 20px',
>               borderRadius: '6px',
>               cursor: 'pointer',
>               fontWeight: 'bold'
>             }}
>           >
>             {submitting ? 'در حال ثبت...' : 'ذخیره آدرس'}
>           </button>
>         </form>
>       )}
> 
>       {/* لیست آدرس‌ها */}
>       {addresses.length === 0 ? (
>         <p style={{ color: '#64748b' }}>هیچ آدرسی ثبت نکرده‌اید.</p>
>       ) : (
>         <div style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
>           {addresses.map((addr) => (
>             <div key={addr.id} style={{
>               border: addr.is_default ? '2px solid #2563eb' : '1px solid #e2e8f0',
>               backgroundColor: addr.is_default ? '#eff6ff' : '#fff',
>               borderRadius: '8px',
>               padding: '15px 20px',
>               position: 'relative'
>             }}>
>               <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
>                 <strong style={{ fontSize: '16px', color: '#0f172a' }}>
>                   {addr.title || 'آدرس بدون عنوان'}
>                 </strong>
>                 {addr.is_default ? (
>                   <span style={{ backgroundColor: '#2563eb', color: '#fff', fontSize: '12px', padding: '2px 8px', borderRadius: '12px' }}>
>                     آدرس پیش‌فرض
>                   </span>
>                 ) : (
>                   <button
>                     onClick={() => handleSetDefault(addr.id)}
>                     style={{ background: 'none', border: 'none', color: '#2563eb', cursor: 'pointer', fontSize: '13px' }}
>                   >
>                     انتخاب به‌عنوان پیش‌فرض
>                   </button>
>                 )}
>               </div>
> 
>               <p style={{ margin: '5px 0', color: '#334155', fontSize: '14px' }}>
>                 {addr.province}، {addr.city}، {addr.street}
>               </p>
>               
>               <div style={{ fontSize: '13px', color: '#64748b', marginTop: '8px', display: 'flex', gap: '20px' }}>
>                 <span>گیرنده: {addr.receiver_name}</span>
>                 <span>تلفن: {addr.phone_number}</span>
>                 <span>کد پستی: {addr.postal_code}</span>
>               </div>
> 
>               <button
>                 onClick={() => handleDeleteAddress(addr.id)}
>                 style={{
>                   position: 'absolute',
>                   top: '15px',
>                   left: '15px',
>                   background: 'none',
>                   border: 'none',
>                   color: '#dc2626',
>                   cursor: 'pointer',
>                   fontSize: '13px'
>                 }}
>               >
>                 حذف
>               </button>
>             </div>
>           ))}
>         </div>
>       )}
>     </div>
>   );
> }
> 
> const inputStyle = {
>   padding: '8px 12px',
>   borderRadius: '6px',
>   border: '1px solid #cbd5e1',
>   fontSize: '14px',
>   boxSizing: 'border-box'
> };
> 
> export default Profile;
> 
> ```
> 

حالا دو گام باقی‌مانده را انجام می‌دهیم: ابتدا روت `/profile` و لینک آن را در Navbar قرار می‌دهیم، و سپس فرم ثبت سفارش در سبد خرید (`Cart.jsx`) را ارتقا می‌دهیم تا کاربر آدرس خود را از لیست آدرس‌های ذخیره‌شده انتخاب کند.

<aside>
💡

🛠️ گام اول: افزودن روت به `src/App.jsx`

</aside>

> 67- فایل **`src/App.jsx`** را باز کن، کامپوننت `Profile` را ایمپورت کرده و مسیر `/profile` را به لیست روت‌ها اضافه کن:
> 
> 
> ```jsx
> // در بالای فایل:
> import Profile from './components/Profile';
> 
> // در داخل بخش <Routes>:
> <Route path="/profile" element={<Profile />} />
> ```
> 

<aside>
💡

🛠️ گام دوم: افزودن لینک پروفایل به `src/components/Navbar.jsx`

</aside>

> 68- فایل **`src/components/Navbar.jsx`** را باز کرده و لینک صفحه پروفایل را در کنار نام کاربر یا منوی بالای صفحه قرار بده:
> 
> 
> ```jsx
> import React from 'react';
> import { Link } from 'react-router-dom';
> 
> function Navbar({ user, onLogout }) {
>   return (
>     <nav style={{
>       display: 'flex',
>       justifyContent: 'space-between',
>       alignItems: 'center',
>       padding: '15px 30px',
>       backgroundColor: '#0f172a',
>       color: '#fff',
>       direction: 'rtl',
>       fontFamily: 'sans-serif'
>     }}>
>       <div style={{ display: 'flex', alignItems: 'center', gap: '20px' }}>
>         <Link to="/products" style={{ color: '#fff', textDecoration: 'none', fontWeight: 'bold', fontSize: '20px' }}>
>           ACRON
>         </Link>
>         <Link to="/products" style={{ color: '#94a3b8', textDecoration: 'none' }}>
>           محصولات
>         </Link>
>         <Link to="/orders" style={{ color: '#94a3b8', textDecoration: 'none' }}>
>           سفارش‌های من
>         </Link>
>       </div>
> 
>       <div style={{ display: 'flex', alignItems: 'center', gap: '15px' }}>
>         {user ? (
>           <>
>             {/* لینک به صفحه پروفایل کاربر */}
>             <Link to="/profile" style={{
>               color: '#38bdf8',
>               textDecoration: 'none',
>               fontWeight: 'bold',
>               backgroundColor: '#1e293b',
>               padding: '6px 12px',
>               borderRadius: '6px'
>             }}>
>               پروفایل {user.username || user} 👤
>             </Link>
> 
>             <button
>               onClick={onLogout}
>               style={{
>                 backgroundColor: '#dc2626',
>                 color: '#fff',
>                 border: 'none',
>                 padding: '6px 12px',
>                 borderRadius: '6px',
>                 cursor: 'pointer'
>               }}
>             >
>               خروج
>             </button>
>           </>
>         ) : (
>           <Link to="/login" style={{ color: '#fff', textDecoration: 'none' }}>
>             ورود / ثبت‌نام
>           </Link>
>         )}
>       </div>
>     </nav>
>   );
> }
> 
> export default Navbar;
> 
> ```
> 

<aside>
💡

🛠️ گام سوم: به‌روزرسانی `src/components/Cart.jsx` (انتخاب سریع آدرس)

</aside>

حالا به هدف اصلی یعنی **عدم نیاز به تایپ دستی آدرس موقع خرید** می‌رسیم. در این مرحله کامپوننت سبد خرید را به‌گونه‌ای تغییر می‌دهیم که:

1. لیست آدرس‌های کاربر را از `GET customers/addresses/` دریافت کند.
2. به صورت خودکار آدرس پیش‌فرض (`is_default: true`) را انتخاب کند.
3. یک منوی کشویی (`<select>`) برای انتخاب بین آدرس‌ها یا دکمه‌ای برای هدایت به صفحه پروفایل (در صورت عدم وجود آدرس) نمایش دهد.

> 69- فایل **`src/components/Cart.jsx`** را به شکل زیر به‌روزرسانی کن:
> 
> 
> ```jsx
> import React, { useEffect, useState } from 'react';
> import axiosInstance from '../api/axiosInstance';
> import { useNavigate, Link } from 'react-router-dom';
> 
> function Cart() {
>   const [cart, setCart] = useState(null);
>   const [addresses, setAddresses] = useState([]);
>   const [selectedAddressId, setSelectedAddressId] = useState('');
>   const [loading, setLoading] = useState(true);
>   const [submitting, setSubmitting] = useState(false);
>   const [error, setError] = useState('');
>   const navigate = useNavigate();
> 
>   const fetchCartAndAddresses = async () => {
>     try {
>       // 1. دریافت اطلاعات سبد خرید
>       const cartRes = await axiosInstance.get('carts/mine/');
>       setCart(cartRes.data);
> 
>       // 2. دریافت لیست آدرس‌های ذخیره‌شده کاربر
>       const addrRes = await axiosInstance.get('customers/addresses/');
>       const addrList = Array.isArray(addrRes.data) ? addrRes.data : (addrRes.data?.results || []);
>       setAddresses(addrList);
> 
>       // انتخاب خودکار آدرس پیش‌فرض در صورت وجود
>       const defaultAddr = addrList.find(a => a.is_default);
>       if (defaultAddr) {
>         setSelectedAddressId(defaultAddr.id);
>       } else if (addrList.length > 0) {
>         setSelectedAddressId(addrList[0].id);
>       }
>     } catch (err) {
>       console.error('خطا در دریافت اطلاعات:', err);
>       setError('خطا در بارگذاری اطلاعات سبد خرید یا آدرس‌ها.');
>     } finally {
>       setLoading(false);
>     }
>   };
> 
>   useEffect(() => {
>     fetchCartAndAddresses();
>   }, []);
> 
>   // نهایی کردن و ثبت سفارش
>   const handlePlaceOrder = async (e) => {
>     e.preventDefault();
>     if (!selectedAddressId) {
>       alert('لطفاً یک آدرس برای ارسال انتخاب کنید.');
>       return;
>     }
> 
>     const selectedAddrObj = addresses.find(a => String(a.id) === String(selectedAddressId));
>     if (!selectedAddrObj) {
>       alert('آدرس انتخابی معتبر نیست.');
>       return;
>     }
> 
>     // ساخت رشته کامل آدرس جهت ثبت در سفارش
>     const formattedAddress = `${selectedAddrObj.province}، ${selectedAddrObj.city}، ${selectedAddrObj.street} - گیرنده: ${selectedAddrObj.receiver_name} (${selectedAddrObj.phone_number})`;
> 
>     setSubmitting(true);
>     try {
>       await axiosInstance.post('orders/', {
>         cart_id: cart.id,
>         shipping_address: formattedAddress,
>       });
> 
>       alert('سفارش شما با موفقیت ثبت شد! 🎉');
>       navigate('/orders');
>     } catch (err) {
>       console.error('خطا در ثبت سفارش:', err);
>       alert('خطا در ثبت سفارش. لطفاً مجدداً تلاش کنید.');
>     } finally {
>       setSubmitting(false);
>     }
>   };
> 
>   if (loading) {
>     return <div style={{ textAlign: 'center', marginTop: '50px', direction: 'rtl' }}>در حال بارگذاری سبد خرید... 🔄</div>;
>   }
> 
>   if (error) {
>     return <div style={{ textAlign: 'center', marginTop: '50px', color: '#dc2626', direction: 'rtl' }}>{error}</div>;
>   }
> 
>   if (!cart || !cart.items || cart.items.length === 0) {
>     return (
>       <div style={{ textAlign: 'center', marginTop: '60px', direction: 'rtl', fontFamily: 'sans-serif' }}>
>         <h2>سبد خرید شما خالی است 🛒</h2>
>         <Link to="/products" style={{ display: 'inline-block', marginTop: '15px', color: '#2563eb' }}>
>           مشاهده کاتالوگ محصولات
>         </Link>
>       </div>
>     );
>   }
> 
>   return (
>     <div style={{ padding: '30px', maxWidth: '800px', margin: '0 auto', fontFamily: 'sans-serif', direction: 'rtl' }}>
>       <h2 style={{ marginBottom: '20px', color: '#0f172a' }}>سبد خرید من 🛒</h2>
> 
>       {/* اقلام سبد خرید */}
>       <div style={{ border: '1px solid #e2e8f0', borderRadius: '8px', padding: '15px', marginBottom: '20px', backgroundColor: '#fff' }}>
>         {cart.items.map((item) => (
>           <div key={item.id} style={{ display: 'flex', justifyContent: 'space-between', padding: '10px 0', borderBottom: '1px dashed #f1f5f9' }}>
>             <div>
>               <strong>{item.product?.name || `محصول ${item.product}`}</strong>
>               <div style={{ fontSize: '13px', color: '#64748b' }}>تعداد: {item.quantity}</div>
>             </div>
>             <div>{Number(item.total_price || 0).toLocaleString()} تومان</div>
>           </div>
>         ))}
>         <div style={{ marginTop: '15px', textAlign: 'left', fontWeight: 'bold', fontSize: '16px', color: '#059669' }}>
>           جمع کل: {Number(cart.total_price || 0).toLocaleString()} تومان
>         </div>
>       </div>
> 
>       {/* بخش انتخاب آدرس ارسال */}
>       <div style={{ border: '1px solid #e2e8f0', borderRadius: '8px', padding: '20px', backgroundColor: '#f8fafc' }}>
>         <h3 style={{ marginTop: 0, color: '#1e293b' }}>آدرس تحویل سفارش 📍</h3>
> 
>         {addresses.length === 0 ? (
>           <div style={{ color: '#dc2626', marginBottom: '15px' }}>
>             شما هنوز هیچ آدرسی ثبت نکرده‌اید! 
>             <br />
>             <Link to="/profile" style={{ color: '#2563eb', fontWeight: 'bold', display: 'inline-block', marginTop: '8px' }}>
>               + افزودن آدرس در صفحه پروفایل
>             </Link>
>           </div>
>         ) : (
>           <div style={{ marginBottom: '15px' }}>
>             <label style={{ display: 'block', marginBottom: '8px', fontWeight: 'bold', color: '#334155' }}>
>               انتخاب از آدرس‌های ذخیره‌شده:
>             </label>
>             <select
>               value={selectedAddressId}
>               onChange={(e) => setSelectedAddressId(e.target.value)}
>               style={{
>                 width: '100%',
>                 padding: '10px',
>                 borderRadius: '6px',
>                 border: '1px solid #cbd5e1',
>                 fontSize: '14px',
>                 backgroundColor: '#fff'
>               }}
>             >
>               {addresses.map((addr) => (
>                 <option key={addr.id} value={addr.id}>
>                   {addr.title ? `[${addr.title}] ` : ''}{addr.province}، {addr.city}، {addr.street} ({addr.receiver_name}) {addr.is_default ? '⭐ پیش‌فرض' : ''}
>                 </option>
>               ))}
>             </select>
>             
>             <Link to="/profile" style={{ fontSize: '12px', color: '#2563eb', display: 'inline-block', marginTop: '8px' }}>
>               مدیریت آدرس‌ها / افزودن آدرس جدید
>             </Link>
>           </div>
>         )}
> 
>         <button
>           onClick={handlePlaceOrder}
>           disabled={submitting || addresses.length === 0}
>           style={{
>             width: '100%',
>             padding: '12px',
>             backgroundColor: addresses.length === 0 ? '#94a3b8' : '#16a34a',
>             color: '#fff',
>             border: 'none',
>             borderRadius: '6px',
>             fontSize: '16px',
>             fontWeight: 'bold',
>             cursor: addresses.length === 0 ? 'not-allowed' : 'pointer'
>           }}
>         >
>           {submitting ? 'در حال ثبت سفارش...' : 'تکمیل و ثبت سفارش 📦'}
>         </button>
>       </div>
>     </div>
>   );
> }
> 
> export default Cart;
> ```
> 

> 70- اصلاح فایل `apps/customers/serializers.py`
> 
> 
> کد این فایل را کاملاً با کد زیر جایگزین کن. در این کد، فیلدهای مربوط به کاربر (`User`) با `source='user.xxx'` به سریالایزر متصل شده‌اند و لیست آدرس‌ها نیز به صورت ساختار یافته بازگردانده می‌شود:
> 
> ```jsx
> from rest_framework import serializers
> from .models import Customer, Address
> 
> class AddressSerializer(serializers.ModelSerializer):
>     """
>     سریالایزر برای تبدیل مدل آدرس به JSON و برعکس
>     """
>     class Meta:
>         model = Address
>         fields = [
>             'id', 
>             'title', 
>             'receiver_name', 
>             'phone_number', 
>             'province', 
>             'city', 
>             'street', 
>             'postal_code', 
>             'is_default'
>         ]
>         read_only_fields = ['id']
> 
> class CustomerSerializer(serializers.ModelSerializer):
>     """
>     سریالایزر ساده برای اطلاعات کلی مشتری
>     """
>     username = serializers.CharField(source='user.username', read_only=True)
>     email = serializers.CharField(source='user.email', read_only=True)
> 
>     class Meta:
>         model = Customer
>         fields = ['id', 'username', 'email', 'phone_number']
> 
> class CustomerProfileSerializer(serializers.ModelSerializer):
>     """
>     سریالایزر کامل برای صفحه پروفایل (شامل اطلاعات کاربری و لیست آدرس‌ها)
>     """
>     # خواندن فیلدهای مرتبط از مدل User از طریق رابطه OneToOne
>     username = serializers.CharField(source='user.username', read_only=True)
>     email = serializers.CharField(source='user.email', read_only=True)
>     first_name = serializers.CharField(source='user.first_name', read_only=True)
>     last_name = serializers.CharField(source='user.last_name', read_only=True)
>     customer_phone = serializers.CharField(source='phone_number', read_only=True)
>     
>     # دریافت آدرس‌های مرتبط با این مشتری (سریالایزر چندتایی)
>     addresses = AddressSerializer(many=True, read_only=True)
> 
>     class Meta:
>         model = Customer
>         fields = [
>             'id', 
>             'username', 
>             'email', 
>             'first_name', 
>             'last_name', 
>             'customer_phone', 
>             'addresses'
>         ]
> ```
> 

> 71- ررسی فایل `apps/customers/models.py`
> 
> 
> مطمئن شو که در مدل `Address` فیلد کلید خارجی `customer` حتما دارای `related_name='addresses'` باشد تا جنگو بتواند لیست آدرس‌ها را به `CustomerProfileSerializer` متصل کند:
> 
> ```jsx
> from django.db import models
> from django.conf import settings
> 
> class Customer(models.Model):
>     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='customer')
>     phone_number = models.CharField(max_length=15, blank=True, null=True)
> 
>     def __str__(self):
>         return self.user.username
> 
> class Address(models.Model):
>     # 🔴 حتما بررسی کن که related_name='addresses' قرار داشته باشد
>     customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='addresses')
>     title = models.CharField(max_length=50, blank=True)
>     receiver_name = models.CharField(max_length=100)
>     phone_number = models.CharField(max_length=15)
>     province = models.CharField(max_length=50)
>     city = models.CharField(max_length=50)
>     street = models.TextField()
>     postal_code = models.CharField(max_length=10)
>     is_default = models.BooleanField(default=False)
> 
>     def __str__(self):
>         return f"{self.customer.user.username} - {self.title or self.city}"
> ```
> 

> 72- بررسی یا اصلاح `apps/carts/views.py`
> 
> 
> در فایل **`apps/carts/views.py`**، باید متد یا اکشنی داشته باشیم که سبد خرید کاربر فعلی را برگرداند. مطمئن شو که اکشن `@action` با `url_path='mine'` تعریف شده است:
> 
> ```jsx
> from rest_framework import status, viewsets
> from rest_framework.decorators import action
> from rest_framework.response import Response
> from rest_framework.permissions import IsAuthenticated
> 
> from .models import Cart
> from .serializers import CartSerializer
> 
> class CartViewSet(viewsets.ModelViewSet):
>     permission_classes = [IsAuthenticated]
>     serializer_class = CartSerializer
> 
>     def get_queryset(self):
>         return Cart.objects.filter(customer__user=self.request.user)
> 
>     @action(detail=False, methods=['get'], url_path='mine')
>     def mine(self, request):
>         """
>         اندپوینت اختصاصی برای دریافت سبد خرید کاربر جاری:
>         GET /api/carts/mine/
>         """
>         cart, _ = Cart.objects.get_or_create(customer__user=request.user)
>         serializer = self.get_serializer(cart)
>         return Response(serializer.data)
> ```
> 

> 73- بررسی یا اصلاح `apps/carts/urls.py`
> 
> 
> فایل **`apps/carts/urls.py`** را به صورت زیر تنظیم کن تا تمام اندپوینت‌های مربوط به سبد خرید (از جمله `/mine/`) به درست ثبت شوند:
> 
> ```jsx
> from django.urls import path, include
> from rest_framework.routers import DefaultRouter
> from .views import CartViewSet
> 
> router = DefaultRouter()
> router.register(r'', CartViewSet, basename='cart')
> 
> urlpatterns = [
>     path('', include(router.urls)),
> ]
> ```
> 

> 73- بررسی `config/urls.py` (یا `backend/urls.py` اصلی)
> 
> 
> مطمئن شو که مسیر کلی اپلیکیشن `carts` در URL اصلی پروژه با پیشوند `api/carts/` ست شده باشد:
> 
> ```jsx
> # در فایل urls.py اصلی پروژه:
> urlpatterns = [
>     # ...
>     path('api/carts/', include('apps.carts.urls')),
>     # ...
> ]
> ```
> 

🧪 تست و نتیجه

پس از ذخیره تغییرات بالا، نیازی به ریستارت کردن سرور نیست (جنگو خودکار Reload می‌شود). حالا کافیست صفحه سبد خرید (`http://localhost:5173/cart`) را رفرش کنی تا لیست آدرس‌های ذخیره‌شده و محصولات سبد خریدت بدون هیچ خطایی نمایش داده شوند.

اصلاح فایل `apps/carts/urls.py`

> 74- مقدار اول `router.register` را به رشته خالی `''` تغییر بده تا کلمه `carts` دوبار در URL تکرار نشود:
> 
> 
> ```jsx
> from django.urls import path, include
> from rest_framework.routers import DefaultRouter
> from .views import CartViewSet, CartItemViewSet
> 
> router = DefaultRouter()
> 
> # 🔴 تغییر بزرگ: 'carts' به '' تغییر یافت تا URL دوبله نشود
> router.register('', CartViewSet, basename='carts')
> router.register('cart-items', CartItemViewSet, basename='cart-items')
> 
> urlpatterns = [
>     path('', include(router.urls)),
> ]
> ```
> 

اصلاح فایل `apps/carts/views.py`

دو مشکل در این فایل وجود داشت:

1. عدم ایمپورت `Response` که موقع فراخوانی `mine` خطای ۵۰۰ می‌داد.
2. متد `get_or_create` نمی‌تواند با شرط `customer__user` به شکل مستقیم رکورد جدید بسازد، باید ابتدا شیء `Customer` دریافت شود.

> 75- ک
> 
> 
> ```jsx
> from rest_framework.viewsets import ModelViewSet, GenericViewSet
> from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
> from rest_framework.decorators import action
> from rest_framework.response import Response  # 🔴 ۱. اضافه شدن ایمپورت Response
> from rest_framework.permissions import IsAuthenticated
> from drf_spectacular.utils import extend_schema_view, extend_schema
> 
> from apps.customers.models import Customer  # 🔴 ۲. ایمپورت مدل Customer
> from .models import Cart, CartItem
> from .serializers import CartSerializer, CartItemSerializer, AddCartItemSerializer, UpdateCartItemSerializer
> 
> @extend_schema_view(
>     create=extend_schema(summary="ساخت سبد خرید جدید", tags=['Carts']),
>     retrieve=extend_schema(summary="دریافت محتویات سبد خرید", tags=['Carts']),
>     destroy=extend_schema(summary="حذف کامل سبد خرید", tags=['Carts']),
> )
> class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
>     permission_classes = [IsAuthenticated]
>     queryset = Cart.objects.prefetch_related('items__product').all()
>     serializer_class = CartSerializer
> 
>     @action(detail=False, methods=['get'], url_path='mine')
>     def mine(self, request):
>         """
>         اندپوینت اختصاصی برای دریافت سبد خرید کاربر جاری:
>         GET /api/carts/mine/
>         """
>         # 🔴 اصلاح نحوه get_or_create برای جلوگیری از خطای دیتابیس
>         customer, _ = Customer.objects.get_or_create(user=request.user)
>         cart, _ = Cart.objects.get_or_create(customer=customer)
>         
>         serializer = self.get_serializer(cart)
>         return Response(serializer.data)
> 
> @extend_schema_view(
>     create=extend_schema(summary="افزودن محصول به سبد خرید", tags=['Cart Items']),
>     partial_update=extend_schema(summary="تغییر تعداد یک محصول در سبد", tags=['Cart Items']),
>     destroy=extend_schema(summary="حذف یک محصول از سبد خرید", tags=['Cart Items']),
> )
> class CartItemViewSet(ModelViewSet):
>     permission_classes = [IsAuthenticated]
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

اصلاح فایل `apps/carts/serializers.py`

> 76- در فرانت‌اند (`Cart.jsx`) نام فیلد قیمت کل `cart.total_price` خوانده می‌شود، اما در سریالایزر اسم آن `grand_total` گذاشته شده بود. نام فیلد را هم‌گام می‌کنیم:
> 
> 
> ```jsx
> from rest_framework import serializers
> from .models import Cart, CartItem
> from apps.products.models import Product
> 
> class SimpleProductSerializer(serializers.ModelSerializer):
>     class Meta:
>         model = Product
>         fields = ['id', 'name', 'price', 'main_image']
> 
> class CartItemSerializer(serializers.ModelSerializer):
>     product = SimpleProductSerializer(read_only=True)
>     total_price = serializers.SerializerMethodField()
> 
>     class Meta:
>         model = CartItem
>         fields = ['id', 'product', 'quantity', 'total_price']
> 
>     def get_total_price(self, cart_item: CartItem):
>         return cart_item.quantity * cart_item.product.price
> 
> class CartSerializer(serializers.ModelSerializer):
>     id = serializers.UUIDField(read_only=True)
>     items = CartItemSerializer(many=True, read_only=True)
>     # 🔴 تغییر نام به total_price جهت هماهنگی کامل با Cart.jsx
>     total_price = serializers.SerializerMethodField()
> 
>     class Meta:
>         model = Cart
>         fields = ['id', 'items', 'total_price']
> 
>     def get_total_price(self, cart: Cart):
>         return sum([item.quantity * item.product.price for item in cart.items.all()])
> 
> class AddCartItemSerializer(serializers.ModelSerializer):
>     product_id = serializers.IntegerField()
>     cart_id = serializers.UUIDField()
> 
>     class Meta:
>         model = CartItem
>         fields = ['id', 'cart_id', 'product_id', 'quantity']
> 
>     def validate_product_id(self, value):
>         if not Product.objects.filter(id=value).exists():
>             raise serializers.ValidationError("محصولی با این شناسه یافت نشد.")
>         return value
> 
>     def validate_cart_id(self, value):
>         if not Cart.objects.filter(id=value).exists():
>             raise serializers.ValidationError("سبد خریدی با این شناسه یافت نشد.")
>         return value
> 
>     def save(self, **kwargs):
>         cart_id = self.validated_data['cart_id']
>         product_id = self.validated_data['product_id']
>         quantity = self.validated_data['quantity']
> 
>         try:
>             cart_item = CartItem.objects.get(cart_id=cart_id, product_id=product_id)
>             cart_item.quantity += quantity
>             cart_item.save()
>             self.instance = cart_item
>         except CartItem.DoesNotExist:
>             self.instance = CartItem.objects.create(
>                 cart_id=cart_id, 
>                 product_id=product_id, 
>                 quantity=quantity
>             )
> 
>         return self.instance
> 
> class UpdateCartItemSerializer(serializers.ModelSerializer):
>     class Meta:
>         model = CartItem
>         fields = ['quantity']
> ```
> 

🧐 علت افتادن سرور روی لوپ بی‌نهایت چیست؟

همان‌طور که در لاگ ترمینال مشخص است، درخواست‌های متوالی زیر در حال ارسال هستند:
`POST /api/carts/ HTTP/1.1 401 58`

دلیلش این است که وقتی دسترسی کل `CartViewSet` روی `IsAuthenticated` قرار گرفت، فرانت‌اند (احتمالاً موقع لود شدن سایت یا کاتالوگ محصولات) سعی می‌کند یک سبد خرید جدید بسازد (`POST /api/carts/`). چون کاربر هنوز توکن ارسال نکرده یا لاگین نبوده، جنگو خطای **`401 Unauthorized`** برمی‌گرداند.

کد فرانت‌اند (در `useEffect` یا Interceptor) با گرفتن خطای ۴۰۱ دوباره تلاش می‌کند همان درخواست را بفرستد و این چرخه بی‌نهایت ادامه پیدا می‌کند!

<aside>
💡

🛠️ راه حل رفع مشکل

</aside>

برای حل این مشکل باید اجازه دهیم ساخت سبد خرید عمومی (`POST /api/carts/`) بدون نیاز به توکن (با `AllowAny`) انجام شود، اما اندپوینت سبد خریدِ کاربر جاری (`/api/carts/mine/`) همچنان نیازمند لاگین (`IsAuthenticated`) باشد.

> 77- فایل **`apps/carts/views.py`** را به صورت زیر جایگزین کن:
> 
> 
> ```jsx
> from rest_framework.viewsets import ModelViewSet, GenericViewSet
> from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
> from rest_framework.decorators import action
> from rest_framework.response import Response
> from rest_framework.permissions import AllowAny, IsAuthenticated  # 🔴 اضافه شدن IsAuthenticated و AllowAny
> from drf_spectacular.utils import extend_schema_view, extend_schema
> 
> from apps.customers.models import Customer
> from .models import Cart, CartItem
> from .serializers import CartSerializer, CartItemSerializer, AddCartItemSerializer, UpdateCartItemSerializer
> 
> @extend_schema_view(
>     create=extend_schema(summary="ساخت سبد خرید جدید", tags=['Carts']),
>     retrieve=extend_schema(summary="دریافت محتویات سبد خرید", tags=['Carts']),
>     destroy=extend_schema(summary="حذف کامل سبد خرید", tags=['Carts']),
> )
> class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
>     # 🔴 اجازه دسترسی عمومی برای ساخت سبد خرید کلی (جلوگیری از خطای 401 و لوپ)
>     permission_classes = [AllowAny]
>     
>     queryset = Cart.objects.prefetch_related('items__product').all()
>     serializer_class = CartSerializer
> 
>     # 🔴 فقط این متد نیاز به لاگین بودن کاربر دارد
>     @action(detail=False, methods=['get'], url_path='mine', permission_classes=[IsAuthenticated])
>     def mine(self, request):
>         """
>         اندپوینت اختصاصی برای دریافت سبد خرید کاربر جاری:
>         GET /api/carts/mine/
>         """
>         customer, _ = Customer.objects.get_or_create(user=request.user)
>         cart, _ = Cart.objects.get_or_create(customer=customer)
>         serializer = self.get_serializer(cart)
>         return Response(serializer.data)
> 
> @extend_schema_view(
>     create=extend_schema(summary="افزودن محصول به سبد خرید", tags=['Cart Items']),
>     partial_update=extend_schema(summary="تغییر تعداد یک محصول در سبد", tags=['Cart Items']),
>     destroy=extend_schema(summary="حذف یک محصول از سبد خرید", tags=['Cart Items']),
> )
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

دلیل اصلی گیر کردن صفحه روی «در حال بررسی...» و دریافت خطای **405 Method Not Allowed**، **عدم وجود اسلش پایانی (`/`) در انتهای آدرس‌های ارسال‌شده از فرانت‌اند** به همراه **عدم مدیریت وضعیت Loading در صورت بروز خطا** در فایل `Login.jsx` است.

🧐 علت دقیق خطای 405 چیست؟

1. **تبدیل درخواست POST به GET توسط مرورگر (مشکل Trailing Slash):**
وقتی فرانت‌اند درخواستی مثل `POST /api/token` (بدون اسلش آخر) می‌فرستد، جنگو طبق تنظیمات خود یک تغییر مسیر (301 Redirect) به `/api/token/` (با اسلش) برمی‌گرداند. مرورگرها موقع فالو کردن این دایرکت، متد `POST` را خودکار به `GET` تبدیل می‌کنند! چون اندپوینت دریافت توکن و سبد خرید متد `GET` را قبول نمی‌کنند، جنگو خطای **405 Method Not Allowed** می‌دهد.
2. **قفل شدن دکمه ورود:**
در کد `Login.jsx` موقع کلیک روی دکمه ورود، متغیر حالتِ loading مقدار `true` می‌گیرد. وقتی درخواست با خطای ۴۰۵ شکست می‌خورد، بخش `catch` یا `finally` وجود ندارد که این حالت را دوباره `false` کند؛ بنابراین دکمه روی «در حال بررسی...» قفل می‌شود.

> 78- اصلاح کد `Login.jsx` در فرانت‌اند
> 
> 
> فایل `Login.jsx` را طوری تغییر بده که حتماً به `/api/token/` (با اسلش آخر) درخواست بزند و در بلوک `finally` حالت loading را ریست کند:
> 
> ```jsx
> import React, { useState, useContext } from 'react';
> import axiosInstance from '../api/axiosInstance';
> import { AuthContext } from '../context/AuthContext';
> 
> function Login() {
>   const [username, setUsername] = useState('');
>   const [password, setPassword] = useState('');
>   const [loading, setLoading] = useState(false);
>   const [error, setError] = useState('');
>   
>   const { login } = useContext(AuthContext); // یا استفاده از useAuth
> 
>   const handleSubmit = async (e) => {
>     e.preventDefault();
>     setLoading(true);
>     setError('');
> 
>     try {
>       // 🔴 حتما اسلش انتهای آدرس token/ قرار داشته باشد
>       const response = await axiosInstance.post('token/', {
>         username,
>         password,
>       });
> 
>       // ذخیره توکن‌ها و ورود به سیستم
>       login(response.data);
>     } catch (err) {
>       console.error('Login Error:', err);
>       setError('نام کاربری یا رمز عبور اشتباه است.');
>     } finally {
>       // 🔴 این بخش باعث می‌شود دکمه از حالت "در حال بررسی..." خارج شود
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

بررسی مسیر توکن در `config/urls.py` (بک‌اند)

> 79- در فایل اصلی `urls.py` پروژه بک‌اند، مطمئن شو اندپوینت توکن به شکل زیر با SimpleJWT ست شده باشد:
> 
> 
> ```jsx
> from django.contrib import admin
> from django.urls import path, include
> from rest_framework_simplejwt.views import (
>     TokenObtainPairView,
>     TokenRefreshView,
> )
> 
> urlpatterns = [
>     path('admin/', admin.site.urls),
>     
>     # 🔴 اندپوینت‌های توکن با اسلش پایانی
>     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
>     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
>     
>     path('api/carts/', include('apps.carts.urls')),
>     path('api/customers/', include('apps.customers.urls')),
>     # سایر مسیرها...
> ]
> ```
> 

> 80- اصلاح فایل `apps/carts/urls.py`
> 
> 
> در فایل `apps/carts/urls.py` نیز جهت جلوگیری از خطای ۴۰۵ موقع ساخت یا دریافت سبد، روت‌ها را به شکل استاندارد زیر تعریف کن:
> 
> ```jsx
> from django.urls import path, include
> from rest_framework.routers import DefaultRouter
> from .views import CartViewSet, CartItemViewSet
> 
> router = DefaultRouter()
> # ثبت ویوست‌ها
> router.register('items', CartItemViewSet, basename='cart-items')
> router.register('', CartViewSet, basename='carts')
> 
> urlpatterns = [
>     path('', include(router.urls)),
> ]
> ```
> 

💡 نکته طلایی برای تمام درخواست‌های Axios

در فایل `api/axiosInstance.js` مطمئن شو که `baseURL` به صورت `[http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)` (با اسلش در آخر) تعریف شده باشد و تمام آدرس‌هایی که در فرانت‌اند صدا می‌زنی (مثل `token/`, `carts/mine/`, `customers/profile/`) **حتماً در انتها اسلش `/` داشته باشند**.

دلیل اصلی رخ دادن خطای **405 Method Not Allowed** در این دو فایل (`CartContext.jsx` و `Login.jsx`) دو موضوع کاملاً مشخص است:

1. **در مورد سبد خرید (`/api/carts/`):** فایل `CartContext.jsx` موقع بالا آمدن برنامه (حتی روی صفحه لاگین) یک درخواست `GET` به آدرس `carts/` یا `/api/carts/` می‌فرستد. چون در بک‌اند برای `CartViewSet` متد لیست (`ListModelMixin`) را تعریف نکرده‌ایم، جنگو درخواست `GET` روی این آدرس را غیرمجاز دانسته و خطای **405** می‌دهد.
2. **در مورد توکن لاگین (`/api/token/`) و Axios:** اگر در درخواست‌های Axios قبل از اسم آدرس **اسلش اول `/`** بگذاری (مثلاً `axiosInstance.post('/token/')` به جای `token/`)، Axios بخش `api/` را از `baseURL` حذف کرده و درخواست را به `[http://127.0.0.1:8000/token/](http://127.0.0.1:8000/token/)` می‌فرستد که باعث خطای ۴۰۵ یا ۴۰۴ می‌شود.

برای حل کامل این موضوع، مراحل زیر را در فرانت‌اند اعمال کن:

> 81- اصلاح فایل `src/context/CartContext.jsx`
> 
> 
> در این فایل آدرس درخواست دریافت سبد خرید را از `carts/` به **`carts/mine/`** تغییر بده و بررسی کن که کاربر حتما توکن داشته باشد تا موقع لاگین نبودن درخواست بیهوده به سرور ارسال نشود:
> 
> ```jsx
> import React, { createContext, useState, useEffect } from 'react';
> import axiosInstance from '../api/axiosInstance';
> 
> export const CartContext = createContext();
> 
> export const CartProvider = ({ children }) => {
>   const [cart, setCart] = useState(null);
>   const [loading, setLoading] = useState(false);
> 
>   const fetchCart = async () => {
>     // اگر توکن وجود ندارد، اصلاً به سرور درخواست نزن
>     const token = localStorage.getItem('access_token'); 
>     if (!token) return;
> 
>     try {
>       setLoading(true);
>       // 🔴 آدرس درست: carts/mine/ (بدون اسلش در ابتدای کلمه)
>       const response = await axiosInstance.get('carts/mine/');
>       setCart(response.data);
>     } catch (error) {
>       console.error('خطا در دریافت سبد خرید:', error);
>     } finally {
>       setLoading(false);
>     }
>   };
> 
>   useEffect(() => {
>     fetchCart();
>   }, []);
> 
>   return (
>     <CartContext.Provider value={{ cart, setCart, fetchCart, loading }}>
>       {children}
>     </CartContext.Provider>
>   );
> };
> ```
> 

> 82- کد زیر را به‌طور کامل جایگزین محتوای فایل **`src/context/CartContext.jsx`** کن:
> 
> 
> ```jsx
> import React, { createContext, useState, useEffect, useContext } from 'react';
> import axiosInstance from '../api/axiosInstance';
> 
> const CartContext = createContext();
> 
> export const CartProvider = ({ children }) => {
>   const [cart, setCart] = useState(null);
>   const [cartCount, setCartCount] = useState(0);
> 
>   // ۱. دریافت یا ایجاد سبد خرید (پشتیبانی هوشمند از کاربر لاگین‌شده و مهمان)
>   const fetchOrCreateCart = async () => {
>     const token = localStorage.getItem('access_token');
> 
>     try {
>       // سناریو اول: کاربر لاگین است -> دریافت سبد خرید اختصاصی کاربر از جنگو
>       if (token) {
>         const response = await axiosInstance.get('carts/mine/');
>         setCart(response.data);
>         if (response.data?.id) {
>           localStorage.setItem('cart_id', response.data.id);
>         }
>         const totalItems = response.data.items?.reduce((sum, item) => sum + item.quantity, 0) || 0;
>         setCartCount(totalItems);
>         return;
>       }
> 
>       // سناریو دوم: کاربر مهمان است -> استفاده از UUID ذخیره‌شده در localStorage
>       let cartId = localStorage.getItem('cart_id');
> 
>       // اگر کاربر مهمان هنوز آی‌دی سبد ندارد، یک سبد جدید در بک‌اند می‌سازیم
>       if (!cartId) {
>         const response = await axiosInstance.post('carts/');
>         cartId = response.data.id;
>         localStorage.setItem('cart_id', cartId);
>       }
> 
>       const response = await axiosInstance.get(`carts/${cartId}/`);
>       setCart(response.data);
> 
>       const totalItems = response.data.items?.reduce((sum, item) => sum + item.quantity, 0) || 0;
>       setCartCount(totalItems);
>     } catch (error) {
>       console.error('خطا در دریافت سبد خرید:', error);
>       // اگر سبد خرید در دیتابیس یافت نشد (مثلاً پاک شده بود)، آی‌دی محلی را حذف کن
>       if (error.response?.status === 404) {
>         localStorage.removeItem('cart_id');
>       }
>     }
>   };
> 
>   useEffect(() => {
>     fetchOrCreateCart();
>   }, []);
> 
>   // ۲. افزودن محصول به سبد خرید
>   const addToCart = async (productId) => {
>     try {
>       let cartId = cart?.id || localStorage.getItem('cart_id');
> 
>       // اگر آی‌دی سبد خرید وجود نداشت، ابتدا یک سبد می‌سازیم
>       if (!cartId) {
>         const newCartResponse = await axiosInstance.post('carts/');
>         cartId = newCartResponse.data.id;
>         localStorage.setItem('cart_id', cartId);
>       }
> 
>       // ارسال درخواست افزودن آیتم به اندپوینت درست در جنگو
>       await axiosInstance.post('carts/cart-items/', {
>         cart_id: cartId,
>         product_id: productId,
>         quantity: 1,
>       });
> 
>       // به‌روزرسانی وضعیت سبد خرید
>       await fetchOrCreateCart();
>     } catch (error) {
>       console.error('خطا در افزودن به سبد خرید:', error.response?.data || error);
>     }
>   };
> 
>   // ۳. تغییر تعداد محصول در سبد خرید (با استفاده از PATCH)
>   const updateQuantity = async (itemId, newQuantity) => {
>     if (newQuantity < 1) return;
>     try {
>       await axiosInstance.patch(`carts/cart-items/${itemId}/`, {
>         quantity: newQuantity,
>       });
>       await fetchOrCreateCart();
>     } catch (error) {
>       console.error('خطا در به‌روزرسانی تعداد:', error.response?.data || error);
>     }
>   };
> 
>   // ۴. حذف کامل محصول از سبد خرید (با استفاده از DELETE)
>   const removeFromCart = async (itemId) => {
>     try {
>       await axiosInstance.delete(`carts/cart-items/${itemId}/`);
>       await fetchOrCreateCart();
>     } catch (error) {
>       console.error('خطا در حذف آیتم از سبد خرید:', error.response?.data || error);
>     }
>   };
> 
>   return (
>     <CartContext.Provider
>       value={{
>         cart,
>         cartCount,
>         addToCart,
>         updateQuantity,
>         removeFromCart,
>         refreshCart: fetchOrCreateCart,
>       }}
>     >
>       {children}
>     </CartContext.Provider>
>   );
> };
> 
> export const useCart = () => useContext(CartContext);
> ```
> 

علت ریشه‌ای رخ دادن خطای **405 Method Not Allowed** مشخص شده است. دو دلیل تداخل در مسیریابی (Routing) جنگو باعث این اتفاق شده‌اند:

1. **تداخل آدرس `/api/token/` با سبد خرید:**
وقتی در `apps/carts/urls.py` از `router.register('', CartViewSet)` استفاده می‌کنیم، یک الگوی متغیر مثل `api/<pk>/` ساخته می‌شود. اگر در `config/urls.py` مسیر `api/` به اپلیکیشن `carts` متصل شده باشد، جنگو درخواست `POST /api/token/` را به اشتباه به عنوان شناسه سبد خرید (`pk='token'`) می‌شناسد! چون نمایش تکی سبد خرید اجازه درخواست `POST` ندارد، جنگو خطای **405** صادر می‌کند.
2. **عدم وجود متد دریافت لیست (`GET`) در `CartViewSet`:**
کلاس `CartViewSet` فاقد متد `list` یا `ListModelMixin` بود؛ بنابراین وقتی فرانت‌اند درخواست `GET` به `/api/carts/` می‌فرستاد، جنگو این متد را غیرمجاز دانسته و خطای **405** برمی‌گرداند.

برای حل ریشه‌ای و کامل این دو مشکل، ۳ فایل زیر را اصلاح کن:

> 83- اصلاح فایل اصلی مسیریابی پروژه‌ بک‌اند (`config/urls.py` یا `backend/urls.py`)
> 
> 
> در فایل اصلی `urls.py` پروژه، مطمئن شو که آدرس‌های توکن **قبل** از سایر اپلیکیشن‌ها قرار دارند و اپلیکیشن `carts` حتماً پیشوند اختصاصی `api/carts/` دارد:
> 
> ```jsx
> from django.contrib import admin
> from django.urls import path, include
> from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
> 
> urlpatterns = [
>     path('admin/', admin.site.urls),
>     
>     # 🔴 ۱. مسیرهای توکن حتماً باید بالا و مستقل از بقیه اپ‌ها باشند
>     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
>     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
>     
>     # 🔴 ۲. مسیرهای اختصاصی اپلیکیشن‌ها
>     path('api/carts/', include('apps.carts.urls')),
>     path('api/customers/', include('apps.customers.urls')),
>     path('api/products/', include('apps.products.urls')),
> ]
> ```
> 

> 84- اصلاح فایل `apps/carts/views.py`
> 
> 
> متد `list` را به `CartViewSet` اضافه می‌کنیم تا اگر فرانت‌اند به `/api/carts/` درخواست `GET` فرستاد، به‌جای خطای ۴۰۵، سبد خرید کاربر را برگرداند:
> 
> ```jsx
> from rest_framework.viewsets import GenericViewSet
> from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
> from rest_framework.decorators import action
> from rest_framework.response import Response
> from rest_framework.permissions import AllowAny, IsAuthenticated
> from drf_spectacular.utils import extend_schema_view, extend_schema
> 
> from apps.customers.models import Customer
> from .models import Cart, CartItem
> from .serializers import CartSerializer, CartItemSerializer, AddCartItemSerializer, UpdateCartItemSerializer
> 
> @extend_schema_view(
>     create=extend_schema(summary="ساخت سبد خرید جدید", tags=['Carts']),
>     retrieve=extend_schema(summary="دریافت محتویات سبد خرید", tags=['Carts']),
>     destroy=extend_schema(summary="حذف کامل سبد خرید", tags=['Carts']),
> )
> class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
>     permission_classes = [AllowAny]
>     queryset = Cart.objects.prefetch_related('items__product').all()
>     serializer_class = CartSerializer
> 
>     # 🔴 جادوی حل خطای 405: افزودن پاسخ به درخواست GET /api/carts/
>     def list(self, request, *args, **kwargs):
>         if request.user and request.user.is_authenticated:
>             customer, _ = Customer.objects.get_or_create(user=request.user)
>             cart, _ = Cart.objects.get_or_create(customer=customer)
>         else:
>             cart_id = request.headers.get('X-Cart-ID')
>             cart = Cart.objects.filter(id=cart_id).first() if cart_id else None
>             if not cart:
>                 cart = Cart.objects.create()
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
> @extend_schema_view(
>     create=extend_schema(summary="افزودن محصول به سبد خرید", tags=['Cart Items']),
>     partial_update=extend_schema(summary="تغییر تعداد یک محصول در سبد", tags=['Cart Items']),
>     destroy=extend_schema(summary="حذف یک محصول از سبد خرید", tags=['Cart Items']),
> )
> class CartItemViewSet(GenericViewSet, CreateModelMixin, DestroyModelMixin):
>     permission_classes = [AllowAny]
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

> 85- اصلاح فایل `apps/carts/urls.py`
> 
> 
> فایل آدرس‌های مربوط به سبد خرید را به این صورت تنظیم کن:
> 
> ```jsx
> from django.urls import path, include
> from rest_framework.routers import DefaultRouter
> from .views import CartViewSet, CartItemViewSet
> 
> router = DefaultRouter()
> 
> # 🔴 آیتم‌های سبد در روت items ثبت می‌شوند
> router.register('items', CartItemViewSet, basename='cart-items')
> router.register('', CartViewSet, basename='carts')
> 
> urlpatterns = [
>     path('', include(router.urls)),
> ]
> ```
> 

### 🧪 تست نهایی

پس از ذخیره تغییرات این فایل‌ها:

1. ترمینال فرانت‌اند و بک‌اند را یک‌بار متوقف و مجدداً اجرا کن.
2. فرم لاگین را تست کن؛ بدون هیچ مشکلی توکن دریافت شده و لاگین انجام خواهد شد.

```python
$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
July 28, 2026 - 13:04:55
Django version 6.0.7, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
For more information on production servers see: https://docs.djangoproject.com/en/6.0/howto/deployment/
Method Not Allowed: /api/carts/
Method Not Allowed: /api/carts/
[28/Jul/2026 13:05:12] "POST /api/carts/ HTTP/1.1" 405 41
[28/Jul/2026 13:05:12] "POST /api/carts/ HTTP/1.1" 405 41
[28/Jul/2026 13:05:31] "POST /api/token/ HTTP/1.1" 200 489
Bad Request: /api/token/
[28/Jul/2026 13:05:31] "POST /api/token/ HTTP/1.1" 400 75
[28/Jul/2026 13:05:51] "POST /api/token/ HTTP/1.1" 200 489
Bad Request: /api/token/
[28/Jul/2026 13:05:51] "POST /api/token/ HTTP/1.1" 400 75

```

همان‌طور که در لاگ می‌بینی، درخواست `POST /api/token/` وضعیت **200 OK** گرفته (و موقع ارسال رمز اشتباه، وضعیت استاندارد **400 Bad Request** داده)؛ این یعنی اندپوینت‌های احراز هویت بدون هیچ مشکلی کار می‌کنند.

حالا تنها ایراد باقی‌مانده خطای **405** روی **`POST /api/carts/`** است. این خطا به این دلیل رخ می‌دهد که متد `create` در `CartViewSet` به صورت صریح تعریف نشده تا متد `POST` را روی روت اصلی سبد خرید بپذیرد.

> 86- برای رفع این آخرین قطعه از پازل، فایل **`apps/carts/views.py`** را کاملاً با کد زیر جایگزین کن:
> 
> 
> ```jsx
> from rest_framework import status
> from rest_framework.viewsets import GenericViewSet, ModelViewSet
> from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
> from rest_framework.decorators import action
> from rest_framework.response import Response
> from rest_framework.permissions import AllowAny, IsAuthenticated
> from drf_spectacular.utils import extend_schema_view, extend_schema
> 
> from apps.customers.models import Customer
> from .models import Cart, CartItem
> from .serializers import CartSerializer, CartItemSerializer, AddCartItemSerializer, UpdateCartItemSerializer
> 
> @extend_schema_view(
>     create=extend_schema(summary="ساخت سبد خرید جدید", tags=['Carts']),
>     retrieve=extend_schema(summary="دریافت محتویات سبد خرید", tags=['Carts']),
>     destroy=extend_schema(summary="حذف کامل سبد خرید", tags=['Carts']),
> )
> class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
>     permission_classes = [AllowAny]
>     queryset = Cart.objects.prefetch_related('items__product').all()
>     serializer_class = CartSerializer
> 
>     def create(self, request, *args, **kwargs):
>         """
>         ساخت صریح سبد خرید جدید برای درخواست‌های POST /api/carts/
>         """
>         cart = Cart.objects.create()
>         serializer = self.get_serializer(cart)
>         return Response(serializer.data, status=status.HTTP_201_CREATED)
> 
>     def list(self, request, *args, **kwargs):
>         """
>         پاسخ به درخواست‌های GET /api/carts/
>         """
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
>         """
>         دریافت سبد خرید اختصاصی کاربر لاگین شده
>         GET /api/carts/mine/
>         """
>         customer, _ = Customer.objects.get_or_create(user=request.user)
>         cart, _ = Cart.objects.get_or_create(customer=customer)
>         serializer = self.get_serializer(cart)
>         return Response(serializer.data)
> 
> @extend_schema_view(
>     create=extend_schema(summary="افزودن محصول به سبد خرید", tags=['Cart Items']),
>     partial_update=extend_schema(summary="تغییر تعداد یک محصول در سبد", tags=['Cart Items']),
>     destroy=extend_schema(summary="حذف یک محصول از سبد خرید", tags=['Cart Items']),
> )
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

<aside>
📢

# پایان Part-15

</aside>