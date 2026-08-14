# ACRON Methodology Part-19

<aside>
📢

در Part-18 ، **فاز 11:**    Frontend - Presentation Layer  تا قدم 139 توسعه داده شد

</aside>

# فاز 11**:**   Frontend - Presentation Layer

شروع قدم 140

---

<aside>
💡

#### قدم بعدی ما

</aside>

حالا Orders Page

فعلاً فقط **نمایش سفارش‌های قبلی** را پیاده می‌کنیم. Checkout را هنوز وارد این صفحه نمی‌کنیم.

فایل:

> 140- فایل
> 
> 
> ```python
> frontend/src/pages/Orders.jsx
> ```
> 
> را با این نسخه جایگزین کن:
> 
> ```python
> import { useEffect, useState } from "react";
> 
> import orderService from "../features/orders/services/orderService";
> 
> function Orders() {
>   const [orders, setOrders] = useState([]);
> 
>   const [loading, setLoading] = useState(true);
> 
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
>         const data =
>           await orderService.getOrders();
> 
>         if (isMounted) {
>           setOrders(data);
>         }
>       } catch (error) {
>         console.error(
>           "Failed to load orders:",
>           error
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
> 
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
> 
>         </div>
>       </main>
>     );
>   }
> 
>   if (error) {
>     return (
>       <main className="page">
>         <div className="page__container">
> 
>           <div className="page__header">
>             <span className="page__eyebrow">
>               ACRON STORE
>             </span>
> 
>             <h1>Your Orders</h1>
> 
>             <p>
>               {error}
>             </p>
>           </div>
> 
>         </div>
>       </main>
>     );
>   }
> 
>   if (orders.length === 0) {
>     return (
>       <main className="page">
>         <div className="page__container">
> 
>           <div className="page__header">
>             <span className="page__eyebrow">
>               ACRON STORE
>             </span>
> 
>             <h1>Your Orders</h1>
> 
>             <p>
>               You don't have any orders yet.
>             </p>
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
>         <section className="orders">
> 
>           {orders.map((order) => (
>             <article
>               key={order.id}
>               className="order"
>             >
> 
>               <div className="order__header">
> 
>                 <div>
>                   <span className="order__label">
>                     Order
>                   </span>
> 
>                   <strong className="order__id">
>                     {order.id}
>                   </strong>
>                 </div>
> 
>                 <span className="order__status">
>                   {order.status}
>                 </span>
> 
>               </div>
> 
>               <div className="order__date">
>                 {new Date(
>                   order.created_at
>                 ).toLocaleDateString()}
>               </div>
> 
>               <div className="order__items">
> 
>                 {order.items.map((item) => (
>                   <div
>                     key={item.id}
>                     className="order__item"
>                   >
> 
>                     <div>
>                       <strong>
>                         {item.product_name}
>                       </strong>
> 
>                       <span>
>                         Quantity: {item.quantity}
>                       </span>
>                     </div>
> 
>                     <div>
>                       {item.unit_price}
>                     </div>
> 
>                   </div>
>                 ))}
> 
>               </div>
> 
>               <div className="order__total">
> 
>                 <span>
>                   Total
>                 </span>
> 
>                 <strong>
>                   {order.total_price}
>                 </strong>
> 
>               </div>
> 
>             </article>
>           ))}
> 
>         </section>
> 
>       </div>
> 
>     </main>
>   );
> }
> 
> export default Orders;
> ```
> 

<aside>
💡

یک نکته درباره Status

</aside>

از Backend این مقادیر را می‌فرستد:

```python
P = Pending
C = Completed
X = Canceled
```

پس الان Frontend احتمالاً نشان می‌دهد:

```python
P
C
X
```

فعلاً این را تبدیل نمی‌کنیم.

در UI نهایی بهتر است چیزی شبیه:

```python
P → Pending Payment
C → Paid
X → Canceled
```

نمایش داده شود.

این هم جزو **UI Polish** است و بعداً انجامش می‌دهیم.

---

<aside>
💡

نکته مهم درباره Order Detail

</aside>

الان API شما این قابلیت را دارد:

```python
GET /api/orders/<id>/
```

ولی فعلاً صفحه‌ای برای آن نداریم.

من پیشنهاد می‌کنم **هنوز Order Detail را نسازیم**.

چرا؟

چون مرحله بعدی ما Checkout است و جریان طبیعی فروشگاه باید این باشد:

```python
Cart
 ↓
Checkout
 ↓
Create Order
 ↓
Order Detail
 ↓
Payment
 ↓
Orders
```

اگر الان Order Detail را کامل کنیم، احتمالاً بعداً بخشی از آن را هنگام Checkout دوباره تغییر خواهیم داد.

پس فعلاً فقط Order List را متصل می‌کنیم.

<aside>
💡

نکته بسیار مهم در Backend

</aside>

در مدل:

```python
class Order(models.Model):
```

داریم:

```python
customer = models.ForeignKey(
    Customer,
    on_delete=models.PROTECT,
    related_name='orders'
)
```

این درست است.

و ViewSet هم:

```python
def get_queryset(self):
    return Order.objects.filter(
        customer__user=self.request.user
    )
```

این قسمت **خوب و امن‌تر** طراحی شده.

یعنی کاربر:

```python
GET /api/orders/
```

باشد، User B نمی‌تواند با GET لیست سفارش‌ها Order 1 و 2 را ببیند.

این بخش را فعلاً دست نمی‌زنیم.

اما `place_order` یک مشکل جدی دارد

این قسمت:

```python
cart = Cart.objects.prefetch_related(
    'items__product'
).get(id=cart_id)
```

فقط می‌گوید:

> آیا چنین Cartای وجود دارد؟
> 

ولی نمی‌گوید:

> آیا این Cart متعلق به همین User است؟
> 

بنابراین در Security Hardening باید چیزی در این مفهوم داشته باشیم:

```python
Current User
      ↓
Customer
      ↓
Cart
      ↓
Order
```

نه اینکه:

```python
Current User
      ↓
هر cart_id دلخواه
      ↓
Order
```

فعلاً **این را تغییر نمی‌دهیم** چون در حال تکمیل مسیر معماری هستیم و خودت هم مشخص کردی که Security را بعداً یک‌جا بررسی کنیم.

این مورد را در Backlog شماره ۴ ثبت می‌کنیم.

<aside>
💡

یک مشکل دیگر که Checkout آن را حل می‌کند

</aside>

در Serializer:

```python
class OrderCreateInputSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()
    shipping_address = serializers.CharField(min_length=10)
```

اما در Service:

```python
shipping_address = ...
```

گرفته می‌شود و بعد استفاده نمی‌شود.

یعنی الان کاربر می‌تواند بفرستد:

```python
{
  "cart_id": "...",
  "shipping_address": "Tehran..."
}
```

ولی Order هیچ فیلدی برای ذخیره این Address ندارد.

این نشان می‌دهد که **Checkout هنوز نباید الان پیاده‌سازی شود**.

ابتدا باید Domain مربوط به Address/Customer را با جریان Checkout هماهنگ کنیم.

پس مسیر درست:

```python
Orders List          ← الان
       ↓
Checkout Architecture
       ↓
Shipping Address
       ↓
Create Order
       ↓
Payment
```

<aside>
💡

### **وضعیت فعلی پروژه**

</aside>

```python
CART
────────────────────────
Cart API             ✅
Cart Context         ✅
Add to Cart          ✅
Cart Page            ✅
Quantity             ✅
Remove Item          ✅
Cart Summary         ✅

ORDERS
────────────────────────
Backend Domain       ✅
Order Service        ✅
Order API            ✅
Order Service Client ✅
Orders Page          ✅
Order Detail         ⏳
Checkout             ⏳
Payment              ⏳
```

و Backlog ما همچنان:

```python
1. Authentication / Login
2. Product Images
3. Cart UI / Visual Design
4. Security Hardening
5. Bug & Edge Case Review
```

را نگه می‌داریم.

<aside>
💡

### قدم بعدی

</aside>

حالا **قبل از Checkout** باید Domain مربوط به Customer/Address را بررسی کنیم؛ چون Checkout قرار است آدرس ارسال را دریافت کند و Order فعلی هم `shipping_address` را به‌صورت ناقص دریافت می‌کند.

مسیر را این‌طور ادامه می‌دهیم:

```python
Cart
  ↓
Checkout Page
  ↓
Load Customer Addresses
  ↓
Select / Add Address
  ↓
Review Order
  ↓
Create Order
  ↓
Payment
  ↓
Order Detail
  ↓
Orders
```

و یک تصمیم معماری مهم هم از الان مشخص است:

آدرس را داخل Order به شکل متن خام ذخیره نمی‌کنیم

مدل فعلی:

```python
class Order(models.Model):
    ...
```

فعلاً هیچ `shipping_address` ندارد، در حالی که `OrderCreateInputSerializer` آن را دریافت می‌کند.

در مرحله Checkout باید این را اصولی حل کنیم؛ چون اگر کاربر بعداً آدرسش را تغییر دهد، **سفارش قدیمی نباید آدرس ارسال قدیمی خودش را از دست بدهد**.

بنابراین احتمالاً به یک Snapshot از اطلاعات آدرس در زمان ثبت سفارش نیاز خواهیم داشت، نه اینکه صرفاً Order را به Address فعلی متصل کنیم. این دقیقاً از همان مواردی است که باید قبل از نوشتن Checkout تصمیم بگیریم.

پس فعلاً **هیچ کدی از Orders یا Customers را تغییر نده**.

<aside>
💡

نکته مهم این است که `AddressViewSet` از قبل درست طراحی شده:

</aside>

```python
GET    /api/customers/addresses/
POST   /api/customers/addresses/
PATCH  /api/customers/addresses/<id>/
DELETE /api/customers/addresses/<id>/
POST   /api/customers/addresses/<id>/set-default/
```

باعث می‌شود کاربر فقط آدرس‌های خودش را ببیند. این قسمت را فعلاً تغییر نمی‌دهیم.

اما حالا به یک تصمیم معماری مهم می‌رسیم.

<aside>
💡

### مشکل `shipping_address` را قبل از Checkout حل کنیم

</aside>

در حال حاضر Order این را ندارد:

```python
shipping_address
```

ولی هنگام ساخت Order این مقدار را می‌گیریم:

```python
shipping_address = serializer.validated_data['shipping_address']
```

و سپس هیچ‌جا استفاده نمی‌شود.

این را نباید در Frontend دور بزنیم.

چرا؟

فرض کن کاربر امروز سفارش شماره 100 را در این آدرس ثبت کند:

```python
تهران
خیابان X
پلاک 10
```

و فردا Address خودش را تغییر دهد:

```python
تهران
خیابان Y
پلاک 20
```

در اصل ، Order شماره 100 باید همچنان آدرس زمان ثبت سفارش را داشته باشد.

بنابراین صرفاً این کار را هم نمی‌کنیم:

```python
shipping_address = models.ForeignKey(Address, ...)
```

چون Order باید **Snapshot آدرس در لحظه سفارش** را داشته باشد.

<aside>
💡

### طراحی پیشنهادی Order

</aside>

به جای ذخیره یک رشته، یک Snapshot واقعی از آدرس ایجاد می‌کنیم.

> 141- مدل Order را به این شکل توسعه می‌دهیم:
> 
> 
> ```python
> class Order(models.Model):
> 
>     class OrderStatus(models.TextChoices):
>         PENDING = 'P', 'در انتظار پرداخت'
>         COMPLETED = 'C', 'پرداخت موفق'
>         CANCELED = 'X', 'لغو شده'
> 
>     id = models.UUIDField(
>         primary_key=True,
>         default=uuid.uuid4,
>         editable=False
>     )
> 
>     customer = models.ForeignKey(
>         Customer,
>         on_delete=models.PROTECT,
>         related_name='orders'
>     )
> 
>     status = models.CharField(
>         max_length=1,
>         choices=OrderStatus.choices,
>         default=OrderStatus.PENDING
>     )
> 
>     shipping_receiver_name = models.CharField(
>         max_length=100
>     )
> 
>     shipping_phone_number = models.CharField(
>         max_length=15
>     )
> 
>     shipping_province = models.CharField(
>         max_length=50
>     )
> 
>     shipping_city = models.CharField(
>         max_length=50
>     )
> 
>     shipping_street = models.TextField()
> 
>     shipping_postal_code = models.CharField(
>         max_length=10
>     )
> 
>     created_at = models.DateTimeField(
>         auto_now_add=True
>     )
> 
>     def __str__(self):
>         return f"Order {self.id} - {self.customer.user.username}"
> ```
> 

در این طراحی دیگر نیازی به:

```python
shipping_address = serializers.CharField(...)
```

نداریم.

حالا ، Checkout فقط `address_id` را می‌فرستد.

<aside>
💡

### ورودی Create Order را تغییر می‌دهیم

</aside>

به جای:

```python
class OrderCreateInputSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()
    shipping_address = serializers.CharField(min_length=10)
```

داریم:

```python
class OrderCreateInputSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()
    address_id = serializers.IntegerField()
```

یعنی Frontend فقط می‌گوید:

```python
{
  "cart_id": "....",
  "address_id": 5
}
```

و Backend خودش Address شماره 5 را پیدا می‌کند.

این خیلی بهتر است چون Frontend نباید اطلاعات آدرس را دوباره برای Backend ارسال کند و Backend هم باید خودش مالکیت Address را بررسی کند.

<aside>
💡

### OrderService

</aside>

اینجا Checkout واقعاً شکل می‌گیرد.

منطق باید این باشد:

```python
User
 ↓
Customer
 ↓
Address متعلق به Customer؟
 ↓
Cart متعلق به Customer؟
 ↓
Cart خالی نیست؟
 ↓
Create Order
 ↓
Snapshot Address
 ↓
Create OrderItems
 ↓
Delete Cart
```

> 142- پس Service را باید به سمت این ساختار ببریم.
> 
> 
> نسخه پیشنهادی:
> 
> ```python
> from django.db import transaction
> from rest_framework.exceptions import ValidationError
> 
> from apps.carts.models import Cart
> from apps.customers.models import Customer, Address
> from apps.orders.models import Order, OrderItem
> 
> class OrderService:
> 
>     @classmethod
>     def place_order(
>         cls,
>         user,
>         cart_id: str,
>         address_id: int
>     ) -> Order:
> 
>         with transaction.atomic():
> 
>             customer = Customer.objects.filter(
>                 user=user
>             ).first()
> 
>             if not customer:
>                 raise ValidationError(
>                     "پروفایل مشتری برای این کاربر یافت نشد."
>                 )
> 
>             address = Address.objects.filter(
>                 id=address_id,
>                 customer=customer
>             ).first()
> 
>             if not address:
>                 raise ValidationError(
>                     "آدرس انتخاب‌شده معتبر نیست."
>                 )
> 
>             cart = (
>                 Cart.objects
>                 .prefetch_related('items__product')
>                 .filter(
>                     id=cart_id,
>                     customer=customer
>                 )
>                 .first()
>             )
> 
>             if not cart:
>                 raise ValidationError(
>                     "سبد خرید معتبر نیست."
>                 )
> 
>             cart_items = list(
>                 cart.items.all()
>             )
> 
>             if not cart_items:
>                 raise ValidationError(
>                     "سبد خرید شما خالی است."
>                 )
> 
>             order = Order.objects.create(
>                 customer=customer,
>                 status=Order.OrderStatus.PENDING,
> 
>                 shipping_receiver_name=(
>                     address.receiver_name
>                     or f"{customer.user.first_name} "
>                        f"{customer.user.last_name}"
>                 ),
> 
>                 shipping_phone_number=(
>                     address.phone_number
>                     or customer.phone_number
>                     or ""
>                 ),
> 
>                 shipping_province=address.province,
>                 shipping_city=address.city,
>                 shipping_street=address.street,
>                 shipping_postal_code=address.postal_code,
>             )
> 
>             for item in cart_items:
> 
>                 OrderItem.objects.create(
>                     order=order,
>                     product=item.product,
>                     quantity=item.quantity,
>                     unit_price=item.product.price,
>                 )
> 
>             cart.delete()
> 
>             return order
> ```
> 

یک نکته

در این مرحله ، **امنیت Cart را همزمان با Checkout** درست کردم:

```python
.filter(
    id=cart_id,
    customer=customer
)
```

یعنی دیگر نمی‌توانیم یک `cart_id` متعلق به کاربر دیگری را برای ایجاد Order استفاده کنیم.

این همان مشکلی بود که قبلاً در Backlog Security داشتیم.

اما این به معنی انجام کامل Security Hardening نیست؛ فقط یک گارد ضروری Checkout است. در مرحله Security دوباره کل سیستم را بررسی می‌کنیم.

> 143- حالا ، View را هم هماهنگ می‌کنیم
> 
> 
> در `OrderViewSet`:
> 
> ```python
> def create(self, request, *args, **kwargs):
> 
>     serializer = self.get_serializer(
>         data=request.data
>     )
> 
>     serializer.is_valid(
>         raise_exception=True
>     )
> 
>     order = OrderService.place_order(
>         user=request.user,
>         cart_id=serializer.validated_data['cart_id'],
>         address_id=serializer.validated_data['address_id'],
>     )
> 
>     output_serializer = OrderSerializer(order)
> 
>     return Response(
>         output_serializer.data,
>         status=status.HTTP_201_CREATED
>     )
> ```
> 

> 144- حالا ، OrderSerializer
> 
> 
> اطلاعات Snapshot آدرس را هم باید به خروجی Order اضافه کنیم:
> 
> ```python
> class OrderSerializer(serializers.ModelSerializer):
> 
>     items = OrderItemSerializer(
>         many=True,
>         read_only=True
>     )
> 
>     total_price = serializers.SerializerMethodField()
> 
>     class Meta:
>         model = Order
>         fields = [
>             'id',
>             'customer',
>             'status',
>             'created_at',
>             'shipping_receiver_name',
>             'shipping_phone_number',
>             'shipping_province',
>             'shipping_city',
>             'shipping_street',
>             'shipping_postal_code',
>             'items',
>             'total_price',
>         ]
> 
>     def get_total_price(self, obj):
>         return sum(
>             item.quantity * item.unit_price
>             for item in obj.items.all()
>         )
> ```
> 
> حالا Order واقعاً یک فاکتور مستقل است.
> 

<aside>
💡

### حالا Checkout در Frontend

</aside>

بعد از این تغییر Backend، ساختار Frontend ما خواهد شد:

```python
frontend/src/
│
├── features/
│   ├── products/
│   │
│   ├── orders/
│   │   ├── components/
│   │   └── services/
│   │       └── orderService.js
│   │
│   └── checkout/
│       ├── components/
│       └── services/
│
└── pages/
    ├── Cart.jsx
    ├── Checkout.jsx
    └── Orders.jsx
```

اما فعلاً لازم نیست Checkout را با ده‌ها component خرد کنیم.

اول جریان اصلی را برقرار می‌کنیم:

```python
Cart
 ↓
Proceed to Checkout
 ↓
Checkout
 ↓
Load Addresses
 ↓
Select Address
 ↓
Order Summary
 ↓
Place Order
 ↓
Order Created
 ↓
Payment
```

<aside>
💡

### یک تغییر کوچک در Cart لازم داریم

</aside>

در Cart فعلی پروژه ، دکمه: Proceed to Checkout داریم.

باید هدایت شود به:

```python
/checkout
```

> 145- در `App.jsx` هم Route جدید: اضافه خواهد شد.
> 
> 
> ```python
> import Checkout from "./pages/Checkout";
> 
> <Route
>   path="/checkout"
>   element={<Checkout />}
> />
> ```
> 

<aside>
💡

وضعیت معماری الان

</aside>

```python
                    ACRON
                      │
          ┌───────────┴───────────┐
          │                       │
        Cart                    Orders
          │                       │
          ▼                       ▼
     Cart Context           Order Service
          │                       │
          ▼                       ▼
       Cart API                Order API
                                  │
                                  ▼
                              Checkout
                                  │
                                  ▼
                              Address
                                  │
                                  ▼
                           Create Order
                                  │
                                  ▼
                              Payment
```

و پنج مورد باز قبلی همچنان وجود دارند:

```python
1. Login / Authentication
2. Product Images
3. Cart UI / Layout
4. Security Hardening
5. Bug / Edge Cases
```

فقط **Security مربوط به مالکیت Cart** را الان مجبور شدیم برای Checkout اصلاح کنیم، چون اگر آن را اصلاح نمی‌کردیم، خود Checkout از ابتدا مشکل امنیتی داشت.

قدم عملی بعدی

قبل از اینکه کد Frontend Checkout را بنویسیم، این تغییرات Backend باید اعمال شوند:

```python
Order model
      ↓
Migration
      ↓
Order Serializer
      ↓
OrderCreateInputSerializer
      ↓
OrderService
      ↓
OrderViewSet
      ↓
تست API
```

بعد از اینکه Migration و API بدون خطا بالا آمدند، می‌رویم سراغ `Checkout.jsx` و اتصال آن به `Address API` و `Order API`.

این مسیر با همان معماری Domain-based پروژه ACRON ادامه پیدا می‌کند و فعلاً وارد زیباسازی Cart، تصاویر یا Login نمی‌شویم.

این قسمت بعد از تغییرات نیاز به makemigrations و migrate خواهد داشت که احتمالا به ارور میخوریم.

اتفاقاً **قبل از اینکه آن تغییرات را روی `Order` اعمال کنیم، باید نحوه‌ی Migration را مشخص کنیم**. 

چون اگر دیتابیس پروژه ، الان `Order` داشته باشد، اضافه کردن چند فیلد `null=False` بدون مقدار پیش‌فرض، احتمالاً همان مشکلی را ایجاد می‌کند که قبلاً در `customers` با آن برخورد کردیم.

مشکل چیست؟

اگر این‌ها را اضافه کنیم:

```python
shipping_receiver_name = models.CharField(max_length=100)
shipping_phone_number = models.CharField(max_length=15)
shipping_province = models.CharField(max_length=50)
shipping_city = models.CharField(max_length=50)
shipping_street = models.TextField()
shipping_postal_code = models.CharField(max_length=10)
```

و قبلاً Orderهایی در دیتابیس وجود داشته باشند، Django هنگام:

```python
python manage.py makemigrations
```

می‌پرسد:

> برای رکوردهای قبلی چه مقداری قرار بدهم؟
> 

و اگر migration اشتباه ساخته شود، ممکن است هنگام `migrate` به مشکل بخوریم.

<aside>
💡

### اما یک نکته مهم‌تر

</aside>

پیشنهاد قبلی‌ام را کمی اصلاح می‌کنم.

**الان نباید عجولانه این ۶ فیلد را به `Order` اضافه کنیم.**

چون هنوز در مرحله طراحی Checkout هستیم و باید ابتدا مشخص کنیم:

> آیا واقعاً می‌خواهیم Snapshot آدرس را به صورت ۶ ستون در `Order` ذخیره کنیم؟
> 

<aside>
💡

### کاری که الان باید انجام دهیم

</aside>

اول وضعیت واقعی دیتابیس را بررسی کنیم.

> 146- در پروژه Backend این دستور را اجرا کن:
> 
> 
> ```python
> python manage.py showmigrations orders
> ```
> 

> 147- سپس
> 
> 
> ```python
> python manage.py makemigrations orders --dry-run
> ```
> 

> 148- اگر نسخه Django شما اجازه بدهد، این هم مفید است:
> 
> 
> ```python
> python manage.py makemigrations orders --dry-run --verbosity 3
> ```
> 

> 149- فعلاً `migrate` نزن.
> 
> 
> همچنین اگر در دیتابیس Order واقعی داری، تعدادشان را بررسی کن:
> 
> ```python
> python manage.py shell
> ```
> 

> 150- و داخل shell:
> 
> 
> ```python
> from apps.orders.models import Order
> 
> Order.objects.count()
> ```
> 

> 151- سپس
> 
> 
> ```python
> Order.objects.values(
>     "id",
>     "status",
>     "created_at"
> )[:5]
> ```
> 

<aside>
💡

### چرا این کار بهتر است؟

</aside>

ما نمی‌خواهیم مثل تجربه قبلی Migrationها را حدس بزنیم و بعد وسط کار با:

```python
You are trying to add a non-nullable field...
```

یا Migration خراب مواجه شویم.

ابتدا می‌فهمیم:

```python
Orders موجود؟
        ↓
تعداد رکورد؟
        ↓
Migration فعلی؟
        ↓
تغییر Model
        ↓
Migration امن
        ↓
migrate
```

و اگر Orderهای موجود داشته باشی، **migration را طوری طراحی می‌کنیم که اطلاعات قبلی آسیب نبیند**.

### پس فعلاً:

**هیچ تغییری در `models.py` نده.**

فقط خروجی این سه مورد را بررسی کن :

```python
python manage.py showmigrations orders
```

```python
python manage.py makemigrations orders --dry-run --verbosity 3
```

```python
Order.objects.count()
```

چیزی شبیه به این خواهد بود :

```python
$ python manage.py showmigrations orders
orders
 [X] 0001_initial
 $ python manage.py makemigrations orders --dry-run --verbosity 3
Migrations for 'orders':
  apps\orders\migrations\0002_order_shipping_city_order_shipping_phone_number_and_more.py
    + Add field shipping_city to order
    + Add field shipping_phone_number to order
    + Add field shipping_postal_code to order
    + Add field shipping_province to order
    + Add field shipping_receiver_name to order
    + Add field shipping_street to order
Full migrations file '0002_order_shipping_city_order_shipping_phone_number_and_more.py':
# Generated by Django 6.0.7 on 2026-08-07 22:12

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_city',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_phone_number',
            field=models.CharField(default=None, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_postal_code',
            field=models.CharField(default=None, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_province',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_receiver_name',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_street',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
    
$ python manage.py shell
26 objects imported automatically (use -v 2 for details).

Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> Order.objects.count()
16
>>>
```

<aside>
💡

### یک نکته مثبت:

</aside>

**فعلاً هیچ Migration جدیدی ساخته نشده** چون `--dry-run` استفاده کردیم. بنابراین وضعیت دیتابیس خراب نشده است.

وضعیت فعلی

دیتابیس:

```python
orders
 [X] 0001_initial
```

یعنی فقط Migration اولیه اعمال شده.

اما: ( این مورد تنها نمونه است ، چون قبلا محصول فرضی ساخته بودم.)

```python
Order.objects.count()
16
```

یعنی **۱۶ سفارش موجود در دیتابیس داریم.**

مشکل اینجاست که Migration پیشنهادی Django برای هر ۶ فیلد این کار را می‌کند:

```python
field=models.CharField(default=None, ...)
```

و بعد:

```python
preserve_default=False
```

این برای Migration فعلی مناسب نیست، چون فیلدها در مدل ما `null=False` هستند و رکوردهای قبلی باید مقداری داشته باشند.

<aside>
💡

### مهم‌تر: اطلاعات آدرس ۱۶ سفارش قدیمی را نداریم

</aside>

این موضوع معماری را مشخص می‌کند.

همچنین ، Orderهای قبلی پروژه در مدل فعلی فقط این اطلاعات را دارند:

```python
Order
├── customer
├── status
├── created_at
└── OrderItems
```

و آدرس هنگام ایجاد سفارش قبلاً ذخیره نشده است.

بنابراین نمی‌توانیم برای ۱۶ سفارش قدیمی بگوییم:

> آدرسشان را از Address فعلی کاربر بردار.
> 

چون ممکن است کاربر بعداً آدرسش را تغییر داده باشد.

مثلاً:

```python
Order #1
    زمان خرید:
    Tehran / Street A

Customer Address فعلی:
    Tehran / Street B
```

اگر الان Address فعلی را روی Order قدیمی کپی کنیم، **اطلاعات تاریخی سفارش را جعل کرده‌ایم.**

این کار را انجام نمی‌دهیم.

<aside>
💡

### راه درست برای پروژه فعلی

</aside>

> 152- من پیشنهاد می‌کنم فعلاً فیلدهای Snapshot را `nullable` کنیم:
در `backend/apps/orders/models.py` فقط ۶ فیلد را این‌طور اضافه/اصلاح کن:
> 
> 
> ```python
> # backend/apps/orders/models.py
> 
> shipping_receiver_name = models.CharField(
>     max_length=100,
>     null=True,
>     blank=True
> )
> 
> shipping_phone_number = models.CharField(
>     max_length=15,
>     null=True,
>     blank=True
> )
> 
> shipping_province = models.CharField(
>     max_length=50,
>     null=True,
>     blank=True
> )
> 
> shipping_city = models.CharField(
>     max_length=50,
>     null=True,
>     blank=True
> )
> 
> shipping_street = models.TextField(
>     null=True,
>     blank=True
> )
> 
> shipping_postal_code = models.CharField(
>     max_length=10,
>     null=True,
>     blank=True
> )
> ```
> 

چرا `null=True`؟

برای اینکه:

```python
Orders قدیمی
      ↓
shipping_* = NULL
```

و اطلاعات تاریخی جعلی تولید نمی‌کنیم.

اما:

```python
Orders جدید
      ↓
Checkout
      ↓
Address معتبر
      ↓
Snapshot
      ↓
تمام shipping_* ها مقدار واقعی دارند
```

یعنی `null=True` به این معنی نیست که Checkout اجازه دارد سفارش جدید بدون آدرس بسازد.

**همچنین ، Service این الزام را enforce می‌کند.**

<aside>
💡

### پس Migration کاملاً امن می‌شود

</aside>

> 153- بعد از تغییر Model، دوباره:
> 
> 
> ```python
> python manage.py makemigrations orders
> ```
> 

```python
$ python manage.py makemigrations orders
Migrations for 'orders':
  apps\orders\migrations\0002_order_shipping_city_order_shipping_phone_number_and_more.py
    + Add field shipping_city to order
    + Add field shipping_phone_number to order
    + Add field shipping_postal_code to order
    + Add field shipping_province to order
    + Add field shipping_receiver_name to order
    + Add field shipping_street to order
```

این خروجی **کاملاً طبیعی و درست** است.

نکته مهم این است که این بار Django دیگر برای فیلدهای جدید `default=None` نساخته، چون آن‌ها را `null=True` تعریف کردیم. بنابراین ۱۶ سفارش قبلی می‌توانند مقدار `NULL` داشته باشند و اطلاعاتشان دست‌نخورده باقی می‌ماند.

مرحله بعد

قبل از `migrate`، فایل Migration ساخته‌شده را بررسی کنیم.

این فایل را باز کن:

```python
backend/apps/orders/migrations/0002_order_shipping_city_order_shipping_phone_number_and_more.py
```

احتمالاً Migration چیزی شبیه این تولید خواهد کرد:

```python
migrations.AddField(
    model_name='order',
    name='shipping_city',
    field=models.CharField(
        max_length=50,
        null=True,
        blank=True
    ),
)
```

برای هر ۶ فیلد باید `null=True` وجود داشته باشد و **نباید** چیزی مثل این داشته باشیم:

```python
default=None
```

اگر همین وضعیت را دارد، مرحله بعد:

> 154- برای پر کردن ۱۶ رکورد قبلی نخواهد بود.
> 
> 
> بعد:
> 
> ```python
> python manage.py migrate orders
> ```
> 

باید بتواند بدون نیاز به مقدار برای Orders قبلی، ستون‌ها را اضافه کند.

اما یک نکته بسیار مهم

فعلاً **OrderService را تغییر نده.**

اول فقط Model را تغییر بده.

یعنی فعلاً:

```python
1. Order model
      ↓
2. makemigrations
      ↓
3. بررسی migration
      ↓
4. migrate
      ↓
5. بررسی دیتابیس
```

بعد می رویم سراغ: 

```python
1. Order model
      ↓
2. makemigrations
      ↓
3. بررسی migration
      ↓
4. migrate
      ↓
5. بررسی دیتابیس
```

> 155- بعد از اجرای موفق، این را بزن:
> 
> 
> ```python
> python manage.py showmigrations orders
> ```
> 

باید ببینیم:

```python
orders
 [X] 0001_initial
 [X] 0002_order_shipping_city_order_shipping_phone_number_and_more
```

> 156- و بعد برای اطمینان:
> 
> 
> ```python
> python manage.py shell
> ```
> 
> سپس
> 
> ```python
> from apps.orders.models import Order
> 
> Order.objects.count()
> ```
> 

باید همچنان:

```python
16
```

باشد.

بعد از Migration چه کار می‌کنیم؟

اگر Migration موفق بود، **هنوز سراغ Frontend نمی‌رویم**.

مسیر را این‌طور ادامه می‌دهیم:

```python
Order Model
     ↓
Migration ✅
     ↓
OrderService
     ↓
Checkout API
     ↓
Checkout Page
     ↓
انتخاب Address
     ↓
ثبت Order + Snapshot Address
     ↓
Orders API
     ↓
Orders Page
     ↓
Payment
```

و بعد از تکمیل این بخش‌ها، همان پنج موردی که گفتی را یک‌جا وارد فاز **Hardening / Debugging** می‌کنیم:

1. 🔐اول Login و `/me/`
2. 🖼️ تصاویر Product
3. 🎨 طراحی و Grid صفحه Cart
4. 🔒 موارد امنیتی
5. 🐛 باگ‌ها و مشکلات باقی‌مانده

پس فعلاً مسیر اصلی را قطع نمی‌کنیم و وارد ریزه‌کاری UI نمی‌شویم.

خروجی نهایی:

```python
$ python manage.py migrate orders
Operations to perform:
  Apply all migrations: orders
Running migrations:
  Applying orders.0002_order_shipping_city_order_shipping_phone_number_and_more... OK
  
$ python manage.py showmigrations orders
orders
 [X] 0001_initial
 [X] 0002_order_shipping_city_order_shipping_phone_number_and_more
 
$ python manage.py shell
26 objects imported automatically (use -v 2 for details).

Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from apps.orders.models import Order
>>> Order.objects.count()
16
>>> exit()
now exiting InteractiveConsole...

```

**با موفقیت و بدون هیچ آسیبی به ۱۶ سفارش قبلی** انجام شد. ✅

وضعیت فعلی:

```python
orders
 [X] 0001_initial
 [X] 0002_order_shipping_city_order_shipping_phone_number_and_more
```

و همچنین:

```python
Order.objects.count()
16
```

### پس مرحله‌ی Migration تمام شد و می‌توانیم وارد **Checkout Architecture** شویم.

<aside>
💡

### مرحله بعد: اصلاح OrderService

</aside>

الان یک مشکل مهم در کد فعلی داریم.

در `OrderCreateInputSerializer` نوشته‌ای:

```python
shipping_address = serializers.CharField(min_length=10)
```

یعنی Frontend فعلاً باید یک رشته‌ی آزاد بفرستد:

```python
{
  "cart_id": "...",
  "shipping_address": "Tehran, ..."
}
```

اما ما الان در `Order` شش فیلد مشخص برای Snapshot آدرس داریم.

بنابراین باید معماری را تبدیل کنیم به:

```python
Customer
   │
   ├── Address 1
   ├── Address 2
   └── Address 3
          │
          ↓
      Checkout
          │
          ↓
    selected address
          │
          ↓
      OrderService
          │
          ↓
       Order
          │
          ├── shipping_receiver_name
          ├── shipping_phone_number
          ├── shipping_province
          ├── shipping_city
          ├── shipping_street
          └── shipping_postal_code
```

این دقیقاً همان چیزی است که برای سفارش واقعی می‌خواهیم.

<aside>
💡

### یک نکته امنیتی مهم

</aside>

`cart_id` را از Frontend می‌گیریم، اما نباید صرفاً به این اعتماد کنیم که این Cart متعلق به کاربر است.

در کد فعلی:

```python
cart = Cart.objects.prefetch_related(
    'items__product'
).get(id=cart_id)
```

هیچ بررسی‌ای وجود ندارد که:

```python
این Cart
    ↓
متعلق به همین Customer است؟
```

چون **Checkout الان در حال توسعه است**، بهتر است از همین الان طراحی درستش کنیم و بعداً لازم نباشد معماری را دوباره بشکنیم.

<aside>
💡

### قدم بعدی ما

</aside>

قبل از تغییر `OrderService`، باید `OrderCreateInputSerializer` را اصلاح کنیم.

در:

```python
backend/apps/orders/serializers.py
```

این:

```python
class OrderCreateInputSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()
    shipping_address = serializers.CharField(min_length=10)
```

باید تبدیل شود به:

```python
class OrderCreateInputSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()
    address_id = serializers.IntegerField()
```

یعنی Checkout به جای ارسال متن آزاد آدرس، شناسه‌ی Address انتخاب‌شده را می‌فرستد:

```python
{
    "cart_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "address_id": 3
}
```

سپس Backend:

```python
address_id
    ↓
Address.objects.get(...)
    ↓
بررسی مالکیت
    ↓
کپی اطلاعات Address
    ↓
Order.shipping_*
```

چرا این بهتر است؟

فرض کنیم Customer این آدرس‌ها را دارد:

```python
1 → Home
2 → Office
3 → Parents
```

کاربر در Checkout می‌زند:

```python
Home
```

و در Frontend فقط می‌فرستد:

```python
{
    "cart_id": "...",
    "address_id": 1
}
```

ولی در Backend خودش اطلاعات واقعی را از دیتابیس می‌گیرد.

در نتیجه کاربر نمی‌تواند مثلاً در Request بنویسد:

```python
{
    "address_id": 1,
    "shipping_city": "London",
    "shipping_postal_code": "..."
}
```

و اطلاعات جعلی وارد Order کند.

بعد از این مرحله

ترتیب دقیق کارمان این خواهد بود:

### 1. Serializer

```
cart_id
address_id
```

### 2. OrderService

بررسی:

```python
Customer
   ↓
Cart
   ↓
Cart مالک همین Customer؟
   ↓
Address
   ↓
Address مالک همین Customer؟
   ↓
Cart خالی نیست؟
   ↓
Create Order
   ↓
Snapshot Address
   ↓
Create OrderItems
   ↓
Delete Cart
```

### 3. Orders API

API ثبت سفارش آماده می‌شود.

### 4. Checkout Frontend

صفحه Checkout را می‌سازیم.

### 5. Orders Page

صفحه‌ای که الان فقط:

```
Your Orders
Your orders will appear here.
```

است، به API واقعی وصل می‌شود.

> 157- فعلاً فقط یک تغییر بده در:
> 
> 
> ```python
> # backend/apps/orders/serializers.py
> ```
> 
> این کلاس را:
> 
> ```python
> class OrderCreateInputSerializer(serializers.Serializer):
>     cart_id = serializers.UUIDField()
>     shipping_address = serializers.CharField(min_length=10)
> ```
> 
> به این تبدیل کن:
> 
> ```python
> class OrderCreateInputSerializer(serializers.Serializer):
>     cart_id = serializers.UUIDField()
>     address_id = serializers.IntegerField()
> ```
> 

حالا می‌رویم سراغ **OrderService**؛ اینجا بخش مهم Checkout در Backend را اصولی می‌سازیم.

در وضعیت فعلی `OrderService` سه مشکل دارد:

1. هنوز `shipping_address` می‌گیرد.
2. مالکیت `Cart` را بررسی نمی‌کند.
3. مالکیت `Address` را بررسی نمی‌کند.

ما هر سه را هم‌زمان اصلاح می‌کنیم.

> 158- فایل: `backend/apps/orders/services.py`
> 
> 
> کل محتوای فعلی `OrderService` را با این نسخه جایگزین کن:
> 
> ```python
> from django.db import transaction
> from rest_framework.exceptions import ValidationError
> 
> from apps.carts.models import Cart
> from apps.customers.models import Customer, Address
> from apps.orders.models import Order, OrderItem
> 
> class OrderService:
>     """
>     سرویس اصلی ثبت سفارش در پروژه ACRON.
>     """
> 
>     @classmethod
>     @transaction.atomic
>     def place_order(
>         cls,
>         user,
>         cart_id: str,
>         address_id: int,
>     ) -> Order:
> 
>         # --------------------------------------------------
>         # 1. پیدا کردن Customer مربوط به کاربر جاری
>         # --------------------------------------------------
> 
>         try:
>             customer = Customer.objects.get(user=user)
>         except Customer.DoesNotExist:
>             raise ValidationError(
>                 "پروفایل مشتری برای این کاربر یافت نشد."
>             )
> 
>         # --------------------------------------------------
>         # 2. دریافت Cart
>         # --------------------------------------------------
> 
>         try:
>             cart = (
>                 Cart.objects
>                 .prefetch_related("items__product")
>                 .get(id=cart_id)
>             )
>         except Cart.DoesNotExist:
>             raise ValidationError(
>                 "سبد خرید معتبری یافت نشد."
>             )
> 
>         # --------------------------------------------------
>         # 3. بررسی مالکیت Cart
>         # --------------------------------------------------
> 
>         if cart.customer_id != customer.id:
>             raise ValidationError(
>                 "این سبد خرید متعلق به شما نیست."
>             )
> 
>         # --------------------------------------------------
>         # 4. بررسی خالی نبودن Cart
>         # --------------------------------------------------
> 
>         cart_items = list(cart.items.all())
> 
>         if not cart_items:
>             raise ValidationError(
>                 "سبد خرید شما خالی است و امکان ثبت سفارش وجود ندارد."
>             )
> 
>         # --------------------------------------------------
>         # 5. دریافت Address
>         # --------------------------------------------------
> 
>         try:
>             address = Address.objects.get(
>                 id=address_id,
>                 customer=customer,
>             )
>         except Address.DoesNotExist:
>             raise ValidationError(
>                 "آدرس انتخاب‌شده یافت نشد."
>             )
> 
>         # --------------------------------------------------
>         # 6. ایجاد Order
>         # --------------------------------------------------
> 
>         order = Order.objects.create(
>             customer=customer,
>             status=Order.OrderStatus.PENDING,
> 
>             # Snapshot آدرس در لحظه ثبت سفارش
>             shipping_receiver_name=address.receiver_name,
>             shipping_phone_number=address.phone_number,
>             shipping_province=address.province,
>             shipping_city=address.city,
>             shipping_street=address.street,
>             shipping_postal_code=address.postal_code,
>         )
> 
>         # --------------------------------------------------
>         # 7. انتقال محصولات به OrderItem
>         # --------------------------------------------------
> 
>         for item in cart_items:
> 
>             product = item.product
> 
>             OrderItem.objects.create(
>                 order=order,
>                 product=product,
>                 quantity=item.quantity,
>                 unit_price=product.price,
>             )
> 
>         # --------------------------------------------------
>         # 8. حذف Cart پس از ایجاد موفق Order
>         # --------------------------------------------------
> 
>         cart.delete()
> 
>         return order
> ```
> 

چرا این نسخه بهتر است؟

جریان حالا این است:

```python
Frontend
   │
   │ cart_id + address_id
   ↓
OrderCreateInputSerializer
   │
   ↓
OrderService
   │
   ├── Customer متعلق به user؟
   │
   ├── Cart وجود دارد؟
   │
   ├── Cart متعلق به Customer است؟
   │
   ├── Cart خالی است؟
   │
   ├── Address وجود دارد؟
   │
   ├── Address متعلق به Customer است؟
   │
   ↓
Create Order
   │
   ├── Snapshot Address
   │
   └── Freeze Product Prices
   │
   ↓
Create OrderItems
   │
   ↓
Delete Cart
```

یک نکته مهم امنیتی هم اینجاست:

```python
Address.objects.get(
    id=address_id,
    customer=customer,
)
```

یعنی کاربر نمی‌تواند `address_id` متعلق به کاربر دیگری را بفرستد و از آن استفاده کند.

همین منطق را برای Cart هم اعمال کردیم.

<aside>
💡

### یک نکته درباره `cart.customer`

</aside>

این بررسی:

```python
if cart.customer_id != customer.id:
```

برای **کاربر لاگین‌شده** کاملاً ضروری است.

چون در حال حاضر Backend اجازه دارد Cartهایی داشته باشد که:

```python
customer = NULL
```

این‌ها همان Cartهای مهمان هستند.

اما Checkout در معماری فعلی فقط برای:

```python
Authenticated User
```

است؛ بنابراین Cart باید حتماً متعلق به Customer باشد.

مرحله بعد **وصل کردن `OrderViewSet` به قرارداد جدید Checkout** است.

در حال حاضر `views.py` هنوز این را دارد:

```python
shipping_address=serializer.validated_data['shipping_address']
```

که دیگر با Serializer جدید سازگار نیست.

> 159- فایل `backend/apps/orders/views.py`
> 
> 
> این بخش متد `create` را:
> 
> ```python
> def create(self, request, *args, **kwargs):
>     serializer = self.get_serializer(data=request.data)
>     serializer.is_valid(raise_exception=True)
> 
>     cart_id = serializer.validated_data['cart_id']
>     address_id = serializer.validated_data['address_id']
> 
>     order = OrderService.place_order(
>         user=request.user,
>         cart_id=cart_id,
>         address_id=address_id,
>     )
> 
>     output_serializer = OrderSerializer(order)
> 
>     return Response(
>         output_serializer.data,
>         status=status.HTTP_201_CREATED
>     )
> ```
> 
> با این جایگزین کن:
> 
> ```
> def create(self, request, *args, **kwargs):
>     serializer = self.get_serializer(data=request.data)
>     serializer.is_valid(raise_exception=True)
> 
>     cart_id = serializer.validated_data['cart_id']
>     address_id = serializer.validated_data['address_id']
> 
>     order = OrderService.place_order(
>         user=request.user,
>         cart_id=cart_id,
>         address_id=address_id,
>     )
> 
>     output_serializer = OrderSerializer(order)
> 
>     return Response(
>         output_serializer.data,
>         status=status.HTTP_201_CREATED
>     )
> ```
> 

### تفاوت اصلی

قبلاً:

```
cart_id
shipping_address
```

الان:

```
cart_id
address_id
```

و Service خودش Address را پیدا می‌کند.

<aside>
💡

### یک اصلاح مهم در `OrderSerializer`

</aside>

الان Serializer سفارش این‌ها را برنمی‌گرداند:

```
shipping_receiver_name
shipping_phone_number
shipping_province
shipping_city
shipping_street
shipping_postal_code
```

ولی وقتی بعداً صفحه Orders و Checkout را می‌سازیم، به این اطلاعات نیاز داریم.

> 160- پس در:
> 
> 
> ```python
> backend/apps/orders/serializers.py
> ```
> 
> این قسمت را 
> 
> ```python
> fields = [
>     'id',
>     'customer',
>     'status',
>     'created_at',
>     'items',
>     'total_price'
> ]
> ```
> 
> را به این تبدیل کن:
> 
> ```python
> fields = [
>     'id',
>     'customer',
>     'status',
>     'created_at',
>     'items',
>     'total_price',
>     'shipping_receiver_name',
>     'shipping_phone_number',
>     'shipping_province',
>     'shipping_city',
>     'shipping_street',
>     'shipping_postal_code',
> ]
> ```
> 

<aside>
💡

### یک نکته مهم در `OrderService`

</aside>

ما الان این را داریم:

```
cart.delete()
```

و این تصمیم فعلاً درست است.

چون Cart فعلی یک Cart متعلق به Customer است:

```
Customer
   │
   └── Cart
```

بعد از ثبت سفارش:

```
Cart
 ↓
Order
 ↓
Cart حذف می‌شود
```

و سفارش مستقل می‌شود.

اما در مرحله بعد باید درباره یک موضوع مهم تصمیم بگیریم:

### آیا بعد از Checkout باید Cart جدید ساخته شود؟

برای معماری فعلی، بله، بهتر است.

مثلاً:

```
قبل Checkout:

Customer
   │
   └── Cart #A
        ├── Product A
        └── Product B

ثبت Order
     ↓

Cart #A → deleted

Order #1 → created

     ↓

Customer
   │
   └── Cart #B → empty
```

این موضوع را در مرحله Checkout/Cart به‌صورت تمیز حل می‌کنیم.

بعد از این دو تغییر، Backend قرارداد جدیدی دارد:

```
POST /api/orders/

{
    "cart_id": "...",
    "address_id": 1
}
```

و Backend خودش:

```
address_id
     ↓
Address
     ↓
مالکیت
     ↓
Snapshot
     ↓
Order
```

را انجام می‌دهد.

حالا Backend مربوط به **Order/Checkout** از نظر ساختار اصلی آماده است. قدم بعدی این است که قبل از رفتن به React، خود API را تست کنیم.

<aside>
💡

### مرحله بعد: تست واقعی Checkout API

</aside>

چون `OrderService` تغییر کرده، باید مطمئن شویم این زنجیره واقعاً درست کار می‌کند:

```
Authenticated User
       ↓
Customer
       ↓
Cart
       ↓
CartItem
       ↓
Address
       ↓
POST /api/orders/
       ↓
Order
       ↓
OrderItem
       ↓
Cart حذف می‌شود
```

### 1. اول وضعیت Migration را بررسی کن

> 161- این بار فقط برای اطمینان:
> 
> 
> ```python
> python manage.py showmigrations orders
> ```
> 

خروجی باید این باشد:

```python
orders
 [X] 0001_initial
 [X] 0002_order_shipping_city_order_shipping_phone_number_and_more
```

<aside>
💡

### یک نکته مهم قبل از تست

</aside>

در `OrderService` این شرط را اضافه کردیم:

```
if cart.customer_id != customer.id:
    raise ValidationError(
        "این سبد خرید متعلق به شما نیست."
    )
```

پس برای تست Checkout باید از **Cart متعلق به همان User لاگین‌شده** استفاده کنیم.

پس Cartهای قدیمی که به‌صورت Guest ساخته شده‌اند و:

```
customer = NULL
```

برای این تست مناسب نیستند.

<aside>
💡

### تست را فعلاً از Django Shell انجام بدهیم

</aside>

من ترجیح می‌دهم قبل از اینکه React Checkout را بسازیم، Backend را مستقیم تست کنیم. این کار باعث می‌شود اگر مشکلی وجود داشت، ندانیم مشکل از React است یا Django.

> 162- وارد Shell شو:
> 
> 
> ```python
> python manage.py shell
> ```
> 

> 163- سپس:
> 
> 
> ```python
> from django.contrib.auth import get_user_model
> from apps.customers.models import Customer, Address
> from apps.carts.models import Cart, CartItem
> from apps.products.models import Product
> from apps.orders.models import Order
> ```
> 

> 164- کاربر فعلی را پیدا کن
> 
> 
> ```python
> User = get_user_model()
> 
> User.objects.all()
> ```
> 

> 165- اگر مثلاً username کاربر تستی تو `sina` است:
اگر username متفاوت است، همان username خودت را بگذار.
> 
> 
> ```python
> user = User.objects.get(username="sina")
> ```
> 

> 166- سپس Customer را بررسی کن
> 
> 
> ```python
> customer, created = Customer.objects.get_or_create(
>     user=user
> )
> 
> customer
> ```
> 

> 167- سپس Cart را پیدا کن یا بساز:
اگر `None` برگشت، یعنی Product نداریم و باید ابتدا یک محصول تستی ایجاد کنیم.
> 
> 
> ```python
> cart, created = Cart.objects.get_or_create(
>     customer=customer
> )
> 
> cart
> ```
> 

> 168- اگر Cart خالی است، یک محصول اضافه کن
> 
> 
> ```python
> CartItem.objects.get_or_create(
>     cart=cart,
>     product=product,
>     defaults={
>         "quantity": 2
>     }
> )
> ```
> 

> 169- بعد:
> 
> 
> ```python
> cart.items.all()
> ```
> 

> 170- حالا Address بساز
> 
> 
> این قسمت برای تست Checkout بسیار مهم است.
> 
> ```python
> address = Address.objects.filter(
>     customer=customer
> ).first()
> ```
> 

> 171- اگر `None` بود:
> 
> 
> ```python
> address = Address.objects.create(
>     customer=customer,
>     title="Home",
>     receiver_name="Sina",
>     phone_number="09120000000",
>     province="Tehran",
>     city="Tehran",
>     street="Test Street",
>     postal_code="1234567890",
>     is_default=True,
> )
> ```
> 

> 172- بعد:
> 
> 
> ```python
> address
> ```
> 

> 173- حالا خود OrderService را مستقیماً تست کن
> 
> 
> ```python
> from apps.orders.services import OrderService
> ```
> 

> 174- سپس
> 
> 
> ```python
> order = OrderService.place_order(
>     user=user,
>     cart_id=cart.id,
>     address_id=address.id,
> )
> ```
> 

اگر همه چیز درست باشد، باید یک `Order` برگردد.

مثلاً:

```python
<Order: Order ...>
```

<aside>
💡

### سفارش را بررسی کن

</aside>

```
order.status
```

باید:

```
'P'
```

باشد.

یعنی:

```
PENDING
```

> 175- اقلام سفارش
> 
> 
> ```python
> order.items.all()
> ```
> 

باید محصولی که در Cart داشتیم، به `OrderItem` منتقل شده باشد.

مثلاً:

```
order.items.first().quantity
```

و:

```
order.items.first().unit_price
```

را بررسی کن.

<aside>
💡

### مهم‌ترین تست: قیمت Freeze شده

</aside>

فرض کنیم قیمت محصول قبل از سفارش:

```
product.price
```

مثلاً:

```
12.00
```

باشد.

بعد:

```
order_item = order.items.first()

order_item.unit_price
```

باید همان قیمت زمان ثبت سفارش باشد.

این بخش معماری بسیار مهمی است:

```
Product.price
      ↓
ثبت سفارش
      ↓
OrderItem.unit_price
```

بعداً اگر:

```
Product.price = 15
```

شود، سفارش قبلی نباید به 15 تغییر کند.

> 176- تست Snapshot آدرس
> 
> 
> این قسمت هم مهم است.
> 
> ```python
> order.shipping_city
> ```
> 

باید:

```
Tehran
```

باشد.

همچنین:

```
order.shipping_receiver_name
order.shipping_phone_number
order.shipping_province
order.shipping_street
order.shipping_postal_code
```

باید اطلاعات Address را داشته باشند.

یعنی:

```
Address
   │
   │ هنگام Checkout
   ↓
Order
   │
   ├── shipping_receiver_name
   ├── shipping_phone_number
   ├── shipping_province
   ├── shipping_city
   ├── shipping_street
   └── shipping_postal_code
```

این **Snapshot** است و برای سیستم فروشگاهی ضروری است.

اگر کاربر بعداً آدرسش را تغییر دهد، سفارش قبلی نباید تغییر کند.

> 177- تست حذف Cart
> 
> 
> بعد از:
> 
> ```python
> OrderService.place_order(...)
> ```
> 

باید Cart قبلی دیگر وجود نداشته باشد.

مثلاً:

```
Cart.objects.filter(id=cart.id).exists()
```

باید:

```
False
```

باشد.

و:

```
Order.objects.filter(id=order.id).exists()
```

باید:

```
True
```

باشد.

<aside>
💡

### یک نکته مهم

</aside>

اگر این تست موفق شود، ما **هنوز Checkout در React را نمی‌سازیم**.

مرحله منطقی بعدی:

```
Order Backend
      ↓
Orders API
      ↓
Frontend Orders Service
      ↓
Orders Page
      ↓
Checkout Page
      ↓
Address Selection
      ↓
Place Order
      ↓
Payment
```

یعنی ابتدا **Orders را در Frontend کامل می‌کنیم** و بعد وارد Checkout می‌شویم.

این با همان مسیر Domain-based که از ابتدا انتخاب کردیم سازگار است.

این خطا:

```
Cart.DoesNotExist
سبد خرید معتبری یافت نشد.
```

**باگ نیست.**

چون بعد از اولین Checkout عمداً این اتفاق افتاده:

```
Cart
 ↓
Order ساخته شد
 ↓
Cart حذف شد
```

بنابراین وقتی دوباره همان `cart.id` را به Service دادی، طبیعی است که Cart وجود نداشته باشد.

<aside>
💡

### وضعیت فعلی ACRON

</aside>

الان معماری ما تقریباً اینجا قرار دارد:

```
PRODUCT
   │
   ↓
CART DOMAIN
   │
   ├── Cart
   ├── CartItem
   ├── Add Item
   ├── Update Quantity
   └── Remove Item
          │
          ↓
ORDER DOMAIN
   │
   ├── Order
   ├── OrderItem
   ├── Frozen Price
   ├── Address Snapshot
   ├── Ownership Validation
   ├── Transaction
   └── Cart Cleanup
```

و حالا وقت آن است که **Orders را در Frontend پیاده کنیم.**

<aside>
💡

### مرحله بعد: Orders Frontend

</aside>

در حال حاضر:

```
frontend/src/pages/Orders.jsx
```

فقط یک Placeholder است:

```
Yourorderswillappearhere.
```

این را تبدیل می‌کنیم به صفحه واقعی سفارش‌ها.

اما مثل قبل، نمی‌خواهیم مستقیم همه چیز را داخل `Orders.jsx` بنویسیم.

ساختار را Domain-based نگه می‌داریم:

```
features/
   orders/
      components/
      services/
```

> 178- پس ابتدا این دو مسیر را ایجاد کن:
> 
> 
> ```python
> frontend/src/features/orders/components/
> frontend/src/features/orders/services/
> ```
> 

> 180- ساخت `orderService.js`
> 
> 
> فایل زیر را بساز:
> 
> ```
> frontend/src/features/orders/services/orderService.js
> ```
> 

> 181- محتوای فایل ساخته شده:
> 
> 
> ```python
> import axiosInstance from "../../../api/axiosInstance";
> 
> const orderService = {
>   getOrders: async () => {
>     const response = await axiosInstance.get("orders/");
>     return response.data;
>   },
> 
>   getOrder: async (orderId) => {
>     const response = await axiosInstance.get(
>       `orders/${orderId}/`
>     );
> 
>     return response.data;
>   },
> 
>   createOrder: async (cartId, addressId) => {
>     const response = await axiosInstance.post(
>       "orders/",
>       {
>         cart_id: cartId,
>         address_id: addressId,
>       }
>     );
> 
>     return response.data;
>   },
> 
>   payOrder: async (orderId) => {
>     const response = await axiosInstance.post(
>       `orders/${orderId}/pay/`
>     );
> 
>     return response.data;
>   },
> };
> 
> export default orderService;
> ```
> 

> 182- س
> 
> 
> ```python
> 
> ```
> 

> 183- س
> 
> 
> ```python
> 
> ```
> 

> 184- س
> 
> 
> ```python
> 
> ```
> 

<aside>
📢

# پایان Part-19

</aside>