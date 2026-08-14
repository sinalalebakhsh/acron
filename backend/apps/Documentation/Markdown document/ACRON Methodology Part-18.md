# ACRON Methodology Part-18

<aside>
📢

در Part-17 ، **فاز 11:**    Frontend - Presentation Layer  تا قدم 107 توسعه داده شد

</aside>

# فاز 11**:**   Frontend - Presentation Layer

شروع قدم 108

---

<aside>
💡

#### قدم بعدی ما

</aside>

بعد از اینکه این Foundation را اجرا کردیم، می‌رویم سراغ: 
**`Products Domain → Product List → Product Card → Product Detail → API → Pagination → Add to Cart`**

و در آن مرحله، به جای Componentهای بزرگ قبلی، ساختار را به صورت زیر پیش می‌بریم؛ این با ایده اصلی ACRON که Frontend هم Domainهای Backend مثل `products`، `carts` و `orders` را آینه کند، هماهنگ‌تر است. 

```powershell
features/
└── products/
    ├── components/
    │   ├── ProductCard.jsx
    │   ├── ProductGrid.jsx
    │   └── ProductSkeleton.jsx
    │
    ├── pages/
    │   ├── ProductsPage.jsx
    │   └── ProductDetailPage.jsx
    │
    └── services/
        └── productService.js
```

> 108- ساخت صفحات اولیه داخل :
> 
> 
> ```python
> src/pages/
> ```
> 
> این سه فایل را بساز:
> این صفحات موقتی نیستند به معنای «دور ریختنی»؛ ما آنها را به عنوان **Page Shell** می‌سازیم و بعد داخلشان Featureهای واقعی را قرار می‌دهیم.
> 
> ```python
> Products.jsx
> Cart.jsx
> Orders.jsx
> ```
> 

> 109- فعلاً: `Products.jsx`
> 
> 
> ```python
> function Products() {
>   return (
>     <main className="page">
>       <div className="page__container">
>         <div className="page__header">
>           <span className="page__eyebrow">
>             ACRON STORE
>           </span>
> 
>           <h1>Products</h1>
> 
>           <p>
>             Explore our products.
>           </p>
>         </div>
> 
>         <div className="products-grid">
>           <div className="product-placeholder">
>             Products will appear here.
>           </div>
>         </div>
>       </div>
>     </main>
>   );
> }
> 
> export default Products;
> ```
> 

> 110- فایل `Cart.jsx`
> 
> 
> ```python
> function Cart() {
>   return (
>     <main className="page">
>       <div className="page__container">
>         <div className="page__header">
>           <span className="page__eyebrow">
>             ACRON STORE
>           </span>
> 
>           <h1>Your Cart</h1>
> 
>           <p>
>             Your selected products will appear here.
>           </p>
>         </div>
>       </div>
>     </main>
>   );
> }
> 
> export default Cart;
> ```
> 

> 111- فایل `Orders.jsx`
> 
> 
> ```python
> function Orders() {
>   return (
>     <main className="page">
>       <div className="page__container">
>         <div className="page__header">
>           <span className="page__eyebrow">
>             ACRON STORE
>           </span>
> 
>           <h1>Your Orders</h1>
> 
>           <p>
>             Your orders will appear here.
>           </p>
>         </div>
>       </div>
>     </main>
>   );
> }
> 
> export default Orders;
> ```
> 

> 112- فایل  `App.jsx` را توسعه بده
> 
> 
> ```python
> import {
>   BrowserRouter,
>   Routes,
>   Route,
> } from "react-router-dom";
> 
> import Navbar from "./components/layout/Navbar";
> 
> import Home from "./pages/Home";
> import Login from "./pages/Login";
> import Products from "./pages/Products";
> import Cart from "./pages/Cart";
> import Orders from "./pages/Orders";
> 
> function App() {
>   return (
>     <BrowserRouter>
> 
>       <Navbar />
> 
>       <Routes>
> 
>         <Route
>           path="/"
>           element={<Home />}
>         />
> 
>         <Route
>           path="/login"
>           element={<Login />}
>         />
> 
>         <Route
>           path="/products"
>           element={<Products />}
>         />
> 
>         <Route
>           path="/cart"
>           element={<Cart />}
>         />
> 
>         <Route
>           path="/orders"
>           element={<Orders />}
>         />
> 
>       </Routes>
> 
>     </BrowserRouter>
>   );
> }
> 
> export default App;
> ```
> 

> 113- استایل Pageها
> 
> 
> به انتهای `index.css` اضافه کن:
> 
> [index.css](index.css)
> 

<aside>
💡

حالا می‌رسیم به بخش مهم‌تر: Products

</aside>

  در Backend فعلی ACRON endpoint زیر را دارد:

```powershell
GET /api/products/
```

و مستندات پروژه نیز همین endpoint را برای دریافت لیست محصولات مشخص کرده‌اند.

پس ساختار Frontend را از اینجا به بعد به شکل Domain-based می‌بریم:

```powershell
src/
│
├── api/
│   └── axiosInstance.js
│
├── components/
│   └── layout/
│       └── Navbar.jsx
│
├── context/
│   └── AuthContext.jsx
│
├── pages/
│   ├── Home.jsx
│   ├── Login.jsx
│   ├── Products.jsx
│   ├── Cart.jsx
│   └── Orders.jsx
│
└── features/
    │
    └── products/
        │
        ├── components/
        │   ├── ProductCard.jsx
        │   ├── ProductGrid.jsx
        │   └── ProductSkeleton.jsx
        │
        └── services/
            └── productService.js
```

این قسمت برای من خیلی مهم است.

دیگر نمی‌خواهم برگردیم به ساختار قبلی مثل:

```powershell
components/
    Products.jsx
    Cart.jsx
    Orders.jsx
    Login.jsx
    ...
```

چون خود مستندات معماری ACRON هم Frontend را به شکل `features` و Domainهای هم‌راستا با Backend پیشنهاد کرده‌اند. 

> 114- شروع Product Service
> 
> 
> فایل زیر را بساز:
> 
> ```python
> src/features/products/services/productService.js
> ```
> 

> 115- داخل فایل قدم قبلی این رو اضافه کن
> 
> 
> ```python
> import axiosInstance from "../../../api/axiosInstance";
> 
> export async function getProducts() {
>   const response = await axiosInstance.get("products/");
> 
>   return response.data;
> }
> ```
> 

فعلاً Service فقط مسئول ارتباط با API است.

یعنی:

```powershell
Products.jsx
     │
     ▼
productService.js
     │
     ▼
axiosInstance
     │
     ▼
GET /api/products/
     │
     ▼
Django
```

این دقیقاً همان جداسازی مسئولیت‌هایی است که در معماری ACRON می‌خواهیم.

> 116- شروع  ProductCard
> 
> 
> فایل زیر را بساز:
> 
> ```python
> src/features/products/components/ProductCard.jsx
> ```
> 

> 117- محتوای فایلی که قدم قبل ساختی:
> 
> 
> ```python
> function ProductCard({ product }) {
>   return (
>     <article className="product-card">
> 
>       <div className="product-card__image">
>         {product.image ? (
>           <img
>             src={product.image}
>             alt={product.name}
>           />
>         ) : (
>           <span>
>             No image
>           </span>
>         )}
>       </div>
> 
>       <div className="product-card__content">
> 
>         <h3>
>           {product.name}
>         </h3>
> 
>         <p className="product-card__description">
>           {product.description}
>         </p>
> 
>         <div className="product-card__footer">
> 
>           <strong>
>             {product.price}
>           </strong>
> 
>           <button>
>             Add to cart
>           </button>
> 
>         </div>
> 
>       </div>
> 
>     </article>
>   );
> }
> 
> export default ProductCard;
> ```
> 

ولی **هنوز ProductCard را نهایی نمی‌کنیم**.

چرا؟

چون قبل از نهایی کردن آن باید Response واقعی `/api/products/` را ببینیم تا مثلاً بفهمیم Backend دقیقاً چه چیزی برمی‌گرداند:

```powershell
{
  "id": "...",
  "name": "...",
  "price": "...",
  "description": "...",
  "images": [...]
}
```

یا مثلا:

```powershell
{
  "id": "...",
  "name": "...",
  "price": "...",
  "image": "..."
}
```

و بر اساس حدس UI نمی‌سازیم.

در Backend پروژه برای Product ساختار نسبتاً کامل‌تری شامل `Product`، `ProductImage`، `Brand` و `Category` دارد.

بنابراین الان وضعیت پروژه این است

```powershell
                    ACRON FRONTEND
                          │
              ┌───────────┴───────────┐
              │                       │
         Foundation                Routing
              │                       │
        ┌─────┴─────┐          ┌──────┴──────┐
        │           │          │      │      │
      Navbar      Auth       Home Products Cart Orders
                              │
                              ▼
                       PRODUCT DOMAIN
                              │
                       productService
                              │
                              ▼
                       Django API
                              │
                     GET /api/products/
```

<aside>
💡

#### مرحله فعلی: Product Domain

</aside>

ساختار را به این شکل جلو می‌بریم:

```powershell
frontend/
└── src/
    ├── api/
    │   └── axiosInstance.js
    │
    ├── context/
    │   └── AuthContext.jsx
    │
    ├── components/
    │   └── layout/
    │       └── Navbar.jsx
    │
    ├── features/
    │   └── products/
    │       ├── components/
    │       │   ├── ProductCard.jsx
    │       │   ├── ProductGrid.jsx
    │       │   └── ProductSkeleton.jsx
    │       │
    │       └── services/
    │           └── productService.js
    │
    ├── pages/
    │   ├── Home.jsx
    │   ├── Login.jsx
    │   ├── Products.jsx
    │   ├── ProductDetail.jsx
    │   ├── Cart.jsx
    │   └── Orders.jsx
    │
    ├── App.jsx
    └── index.css
```

این با معماری Domain-based که برای ACRON تعریف کرده‌ایم هماهنگ است؛ در مستندات پروژه نیز `features/products` به‌عنوان دامنه محصولات در کنار `carts` و `orders` در نظر گرفته شده است.

> 118- شروع  Product Service
> 
> 
> فایل زیر را بساز:
> 
> ```python
> src/features/products/services/productService.js
> ```
> 

> 119- در فایل قدم قبلی که ساختی این را بنویس:
> 
> 
> ```python
> import axiosInstance from "../../../api/axiosInstance";
> 
> export async function getProducts(page = 1) {
>   const response = await axiosInstance.get("products/", {
>     params: {
>       page,
>     },
>   });
> 
>   return response.data;
> }
> 
> export async function getProductBySlug(slug) {
>   const response = await axiosInstance.get(
>     `products/${slug}/`
>   );
> 
>   return response.data;
> }
> ```
> 

نکته مهم اینجاست که Backend از `ReadOnlyModelViewSet` استفاده می‌کند و `lookup_field = 'slug'` دارد؛ بنابراین جزئیات محصول باید با:

```powershell
GET /api/products/<slug>/
```

گرفته شود، نه ID.

> 120- شروع ProductSkeleton
فایل زیر را بساز:
> 
> 
> ```python
> src/features/products/components/ProductSkeleton.jsx
> ```
> 

> 121- در فایلی که ساختی در قدم قبلی بنویس :
> 
> 
> ```python
> function ProductSkeleton() {
>   return (
>     <article className="product-card product-card--skeleton">
>       <div className="product-card__image skeleton-block" />
> 
>       <div className="product-card__content">
> 
>         <div className="skeleton-line skeleton-line--title" />
> 
>         <div className="skeleton-line" />
> 
>         <div className="skeleton-line skeleton-line--short" />
> 
>         <div className="product-card__footer">
>           <div className="skeleton-line skeleton-line--price" />
>           <div className="skeleton-button" />
>         </div>
> 
>       </div>
>     </article>
>   );
> }
> 
> export default ProductSkeleton;
> ```
> 

> 122- شروع ProductCard
فایل زیر را بساز:
> 
> 
> ```python
> src/features/products/components/ProductCard.jsx
> ```
> 

> 123- داخلش این رو بنویس:
> 
> 
> ```python
> # src/features/products/components/ProductCard.jsx
> import { Link } from "react-router-dom";
> 
> function ProductCard({ product }) {
>   const isAvailable = product.inventory > 0;
> 
>   return (
>     <article className="product-card">
> 
>       <Link
>         to={`/products/${product.slug}`}
>         className="product-card__image-link"
>       >
>         <div className="product-card__image">
> 
>           {product.main_image ? (
>             <img
>               src={product.main_image}
>               alt={product.name}
>               loading="lazy"
>             />
>           ) : (
>             <div className="product-card__no-image">
>               No image
>             </div>
>           )}
> 
>         </div>
>       </Link>
> 
>       <div className="product-card__content">
> 
>         {product.brand?.name && (
>           <span className="product-card__brand">
>             {product.brand.name}
>           </span>
>         )}
> 
>         <Link
>           to={`/products/${product.slug}`}
>           className="product-card__title"
>         >
>           {product.name}
>         </Link>
> 
>         <p className="product-card__description">
>           {product.description}
>         </p>
> 
>         <div className="product-card__footer">
> 
>           <div>
>             <span className="product-card__price">
>               {product.price}
>             </span>
>           </div>
> 
>           <span
>             className={
>               isAvailable
>                 ? "product-card__stock product-card__stock--available"
>                 : "product-card__stock product-card__stock--unavailable"
>             }
>           >
>             {isAvailable
>               ? "In stock"
>               : "Out of stock"}
>           </span>
> 
>         </div>
> 
>       </div>
> 
>     </article>
>   );
> }
> 
> export default ProductCard;
> ```
> 

فعلاً دکمه **Add to Cart** نمی‌گذاریم.

چرا؟

چون Cart هنوز Domain بعدی ماست. نمی‌خواهم ProductCard به Cart API وابسته شود و بعد معماری را دوباره تغییر دهیم.

> 124- ساخت ProductGrid
فایل زیر را بساز:
> 
> 
> ```python
> src/features/products/components/ProductGrid.jsx
> ```
> 

> 125- داخلش این رو بنویس:
> 
> 
> ```python
> import ProductCard from "./ProductCard";
> import ProductSkeleton from "./ProductSkeleton";
> 
> function ProductGrid({
>   products,
>   loading,
> }) {
>   if (loading) {
>     return (
>       <div className="products-grid">
>         {Array.from({ length: 8 }).map((_, index) => (
>           <ProductSkeleton key={index} />
>         ))}
>       </div>
>     );
>   }
> 
>   if (!products.length) {
>     return (
>       <div className="products-empty">
>         <h2>No products found</h2>
> 
>         <p>
>           There are currently no products available.
>         </p>
>       </div>
>     );
>   }
> 
>   return (
>     <div className="products-grid">
>       {products.map((product) => (
>         <ProductCard
>           key={product.id}
>           product={product}
>         />
>       ))}
>     </div>
>   );
> }
> 
> export default ProductGrid;
> ```
> 

> 126- فایل Products.jsx را واقعی می‌کنیم
کل محتوای قبلی را با این جایگزین کن:
> 
> 
> ```python
> # src/pages/Products.jsx
> 
> import { useEffect, useState } from "react";
> 
> import ProductGrid from "../features/products/components/ProductGrid";
> import { getProducts } from "../features/products/services/productService";
> 
> function Products() {
>   const [products, setProducts] = useState([]);
> 
>   const [loading, setLoading] = useState(true);
> 
>   const [error, setError] = useState("");
> 
>   const [page, setPage] = useState(1);
> 
>   const [pagination, setPagination] = useState({
>     count: 0,
>     next: null,
>     previous: null,
>   });
> 
>   useEffect(() => {
>     let isMounted = true;
> 
>     async function loadProducts() {
>       setLoading(true);
>       setError("");
> 
>       try {
>         const data = await getProducts(page);
> 
>         if (!isMounted) {
>           return;
>         }
> 
>         /*
>          * Django REST Framework pagination normally
>          * returns:
>          *
>          * {
>          *   count,
>          *   next,
>          *   previous,
>          *   results
>          * }
>          *
>          * If pagination is ever disabled and the API
>          * returns an array, we support that too.
>          */
> 
>         if (Array.isArray(data)) {
>           setProducts(data);
> 
>           setPagination({
>             count: data.length,
>             next: null,
>             previous: null,
>           });
>         } else {
>           setProducts(data.results ?? []);
> 
>           setPagination({
>             count: data.count ?? 0,
>             next: data.next ?? null,
>             previous: data.previous ?? null,
>           });
>         }
>       } catch (err) {
>         if (!isMounted) {
>           return;
>         }
> 
>         console.error(
>           "Failed to load products:",
>           err
>         );
> 
>         setError(
>           "Unable to load products. Please try again."
>         );
>       } finally {
>         if (isMounted) {
>           setLoading(false);
>         }
>       }
>     }
> 
>     loadProducts();
> 
>     return () => {
>       isMounted = false;
>     };
>   }, [page]);
> 
>   const hasNextPage = Boolean(pagination.next);
>   const hasPreviousPage = Boolean(
>     pagination.previous
>   );
> 
>   return (
>     <main className="page">
> 
>       <div className="page__container">
> 
>         <header className="page__header">
> 
>           <span className="page__eyebrow">
>             ACRON STORE
>           </span>
> 
>           <h1>Products</h1>
> 
>           <p>
>             Explore the ACRON product catalog.
>           </p>
> 
>         </header>
> 
>         {error ? (
>           <div className="products-error">
> 
>             <h2>
>               Something went wrong
>             </h2>
> 
>             <p>
>               {error}
>             </p>
> 
>             <button
>               type="button"
>               onClick={() => setPage(1)}
>             >
>               Try again
>             </button>
> 
>           </div>
>         ) : (
>           <>
>             <ProductGrid
>               products={products}
>               loading={loading}
>             />
> 
>             {!loading &&
>               (hasPreviousPage ||
>                 hasNextPage) && (
>                 <div className="pagination">
> 
>                   <button
>                     type="button"
>                     disabled={!hasPreviousPage}
>                     onClick={() =>
>                       setPage((current) =>
>                         Math.max(
>                           1,
>                           current - 1
>                         )
>                       )
>                     }
>                   >
>                     Previous
>                   </button>
> 
>                   <span>
>                     Page {page}
>                   </span>
> 
>                   <button
>                     type="button"
>                     disabled={!hasNextPage}
>                     onClick={() =>
>                       setPage(
>                         (current) =>
>                           current + 1
>                       )
>                     }
>                   >
>                     Next
>                   </button>
> 
>                 </div>
>               )}
>           </>
>         )}
> 
>       </div>
> 
>     </main>
>   );
> }
> 
> export default Products;
> ```
> 

اینجا عمداً Response را هم به شکل Array و هم Response صفحه‌بندی‌شده پشتیبانی کردم؛ چون Backend پروژه `PageNumberPagination` با `PAGE_SIZE = 10` دارد. 

> 127- ساخت Product Detail
> 
> 
> حالا صفحه جزئیات محصول را می‌سازیم.
> 
> ```python
> src/pages/ProductDetail.jsx
> ```
> 

> 128- داخلش این رو بنویس:
> 
> 
> ```python
> # src/pages/ProductDetail.jsx
> 
> import { Link, useParams } from "react-router-dom";
> import { useEffect, useState } from "react";
> 
> import { getProductBySlug } from "../features/products/services/productService";
> 
> function ProductDetail() {
>   const { slug } = useParams();
> 
>   const [product, setProduct] = useState(null);
> 
>   const [loading, setLoading] = useState(true);
> 
>   const [error, setError] = useState("");
> 
>   useEffect(() => {
>     let isMounted = true;
> 
>     async function loadProduct() {
>       setLoading(true);
>       setError("");
> 
>       try {
>         const data =
>           await getProductBySlug(slug);
> 
>         if (isMounted) {
>           setProduct(data);
>         }
>       } catch (err) {
>         console.error(
>           "Failed to load product:",
>           err
>         );
> 
>         if (isMounted) {
>           setError(
>             "Unable to load this product."
>           );
>         }
>       } finally {
>         if (isMounted) {
>           setLoading(false);
>         }
>       }
>     }
> 
>     if (slug) {
>       loadProduct();
>     }
> 
>     return () => {
>       isMounted = false;
>     };
>   }, [slug]);
> 
>   if (loading) {
>     return (
>       <main className="page">
>         <div className="page__container">
>           <div className="product-detail-loading">
>             Loading product...
>           </div>
>         </div>
>       </main>
>     );
>   }
> 
>   if (error || !product) {
>     return (
>       <main className="page">
>         <div className="page__container">
> 
>           <div className="product-detail-error">
> 
>             <h1>
>               Product not found
>             </h1>
> 
>             <p>
>               {error ||
>                 "This product does not exist."}
>             </p>
> 
>             <Link to="/products">
>               Back to products
>             </Link>
> 
>           </div>
> 
>         </div>
>       </main>
>     );
>   }
> 
>   const isAvailable =
>     product.inventory > 0;
> 
>   return (
>     <main className="page">
> 
>       <div className="page__container">
> 
>         <Link
>           to="/products"
>           className="product-detail__back"
>         >
>           ← Back to products
>         </Link>
> 
>         <section className="product-detail">
> 
>           <div className="product-detail__media">
> 
>             {product.main_image ? (
>               <img
>                 src={product.main_image}
>                 alt={product.name}
>               />
>             ) : (
>               <div className="product-detail__no-image">
>                 No image
>               </div>
>             )}
> 
>           </div>
> 
>           <div className="product-detail__content">
> 
>             {product.brand?.name && (
>               <span className="product-detail__brand">
>                 {product.brand.name}
>               </span>
>             )}
> 
>             <h1>
>               {product.name}
>             </h1>
> 
>             {product.category?.name && (
>               <span className="product-detail__category">
>                 {product.category.name}
>               </span>
>             )}
> 
>             <p className="product-detail__description">
>               {product.description}
>             </p>
> 
>             <div className="product-detail__price">
>               {product.price}
>             </div>
> 
>             <div
>               className={
>                 isAvailable
>                   ? "product-detail__stock product-detail__stock--available"
>                   : "product-detail__stock product-detail__stock--unavailable"
>               }
>             >
>               {isAvailable
>                 ? `${product.inventory} available`
>                 : "Out of stock"}
>             </div>
> 
>             <button
>               type="button"
>               className="product-detail__cart-button"
>               disabled={!isAvailable}
>             >
>               Add to cart
>             </button>
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
> export default ProductDetail;
> ```
> 

دکمه Add to cart فعلاً فقط UI است و هنوز درخواست نمی‌فرستد. در مرحله Cart آن را به Cart Context و API واقعی متصل می‌کنیم.

> 129- حالا Route جدید
> 
> 
> حالا `App.jsx` را تغییر بده.
> 
> ```python
> import {
>   BrowserRouter,
>   Routes,
>   Route,
> } from "react-router-dom";
> 
> import Navbar from "./components/layout/Navbar";
> 
> import Home from "./pages/Home";
> import Login from "./pages/Login";
> import Products from "./pages/Products";
> import ProductDetail from "./pages/ProductDetail";
> import Cart from "./pages/Cart";
> import Orders from "./pages/Orders";
> 
> function App() {
>   return (
>     <BrowserRouter>
> 
>       <Navbar />
> 
>       <Routes>
> 
>         <Route
>           path="/"
>           element={<Home />}
>         />
> 
>         <Route
>           path="/login"
>           element={<Login />}
>         />
> 
>         <Route
>           path="/products"
>           element={<Products />}
>         />
> 
>         <Route
>           path="/products/:slug"
>           element={<ProductDetail />}
>         />
> 
>         <Route
>           path="/cart"
>           element={<Cart />}
>         />
> 
>         <Route
>           path="/orders"
>           element={<Orders />}
>         />
> 
>       </Routes>
> 
>     </BrowserRouter>
>   );
> }
> 
> export default App;
> ```
> 

حالا `/products` لیست محصولات را نشان می‌دهد. و مثلاً جزئیات محصول با slug را می‌گیرد.

```powershell
/products/macbook-pro
```

> 130- حالا CSS محصولات
> 
> 
> به `index.css` اضافه کن:
> 
> [index.css](index%201.css)
> 

<aside>
💡

### الان چه چیزی ساخته‌ایم؟

</aside>

مسیر واقعی داده اکنون این است:

```powershell
                    React
                      │
                      ▼
              Products.jsx
                      │
                      ▼
             productService.js
                      │
                      ▼
              axiosInstance
                      │
                      ▼
          GET /api/products/?page=1
                      │
                      ▼
                  Django
                      │
                      ▼
             ProductViewSet
                      │
                      ▼
              ProductSerializer
                      │
                      ▼
        ┌─────────────┴─────────────┐
        │                           │
      results                    pagination
        │
        ▼
   ProductGrid
        │
        ▼
   ProductCard
        │
        ▼
 /products/<slug>
        │
        ▼
 ProductDetail
```

و Backend واقعاً برای Product همین داده‌های nested را ارائه می‌کند: `category`، `brand` و `media_gallery`.

**پس الان هدف این مرحله این است:**

1. باید `/products/` باز شود.
2. درخواست `GET /api/products/` در Network ثبت شود.
3. کارت‌های واقعی محصولات نمایش داده شوند.
4. کلیک روی محصول → `/products/<slug>/`
5. جزئیات واقعی محصول نمایش داده شود.
6. باید Pagination کار کند.
7. باید Loading و Error State داشته باشیم.
8. هیچ Mock Product در Frontend نداشته باشیم.

<aside>
💡

قدم بعدی ما:

</aside>

```powershell
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
Quantity
   ↓
Remove Item
   ↓
Cart Summary
```

مسیر فعلی Frontend

```powershell
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
Quantity
    ↓
Remove Item
    ↓
Cart Summary
    ↓
Orders
    ↓
Checkout
    ↓
Authentication Hardening
    ↓
Fix Product Images
    ↓
Complete Login
    ↓
جمع‌کردن Open Issues
```

نکته مهم این است که **مشکلات Images و Login حذف نشده‌اند**؛ فقط در Backlog باقی می‌مانند تا معماری اصلی Frontend به ترتیب Domainها کامل شود. از اینجا قدم‌به‌قدم جلو می‌رویم و مثل قبل **کدها را بر اساس ساختار فعلی پروژه ACRON** می‌نویسیم، نه اینکه یک معماری جدید و جداگانه اختراع کنیم.

<aside>
💡

#### قدم اول

</aside>

**Cart Domain → Cart API**

ابتدا Service مربوط به Cart را می‌سازیم و APIهای موردنیاز Backend را به Frontend متصل می‌کنیم. بعد از اینکه این لایه درست شد، سراغ `CartContext` می‌رویم.

<aside>
💡

#### قدم فعلی: Cart API

</aside>

ترتیب اجرایی ما همچنان این است:

```powershell
Cart Domain
   ↓
Cart API        ← الان اینجا هستیم
   ↓
Cart Context
   ↓
Add to Cart
   ↓
Cart Page
   ↓
Quantity
   ↓
Remove Item
   ↓
Cart Summary
```

<aside>
💡

مهم‌ترین نکته این است که الان `CartContext.jsx` مستقیماً با `axiosInstance` به API وصل شده. این دقیقاً جایی است که باید مرحله‌ی **Cart API** را از **Cart Context** جدا کنیم.

پس چیزی را دوباره از صفر نمی‌سازیم؛ کد موجود را **Refactor اصولی** می‌کنیم.

</aside>

وضعیت فعلی

الان این اتفاق افتاده:

```powershell
CartContext
    ↓
axiosInstance
    ↓
Django Cart API
```

اما معماری هدف ما این است: این جداسازی بعداً برای Orders و Checkout هم خیلی مهم خواهد بود.

```powershell
CartContext
    ↓
cartService
    ↓
axiosInstance
    ↓
Django Cart API
```

> 131- تغییر فایل زیر:  frontend/src/services/cartService.js
کامل جایگزین کن
> 
> 
> ```python
> # frontend/src/services/cartService.js
> import axiosInstance from "../api/axiosInstance";
> 
> const cartService = {
>   // دریافت سبد خرید کاربر لاگین‌شده
>   getMyCart: async () => {
>     const response = await axiosInstance.get("carts/mine/");
>     return response.data;
>   },
> 
>   // ایجاد سبد خرید جدید
>   createCart: async () => {
>     const response = await axiosInstance.post("carts/");
>     return response.data;
>   },
> 
>   // دریافت سبد خرید با ID
>   getCart: async (cartId) => {
>     const response = await axiosInstance.get(`carts/${cartId}/`);
>     return response.data;
>   },
> 
>   // افزودن محصول به سبد خرید
>   addItem: async (cartId, productId, quantity = 1) => {
>     const response = await axiosInstance.post("carts/cart-items/", {
>       cart_id: cartId,
>       product_id: productId,
>       quantity,
>     });
> 
>     return response.data;
>   },
> 
>   // تغییر تعداد یک آیتم
>   updateItem: async (itemId, quantity) => {
>     const response = await axiosInstance.patch(
>       `carts/cart-items/${itemId}/`,
>       {
>         quantity,
>       }
>     );
> 
>     return response.data;
>   },
> 
>   // حذف آیتم
>   removeItem: async (itemId) => {
>     await axiosInstance.delete(
>       `carts/cart-items/${itemId}/`
>     );
>   },
> };
> 
> export default cartService;
> ```
> 

حالا تمام ارتباطات Cart با Backend در یک نقطه قرار گرفته‌اند.

> 132- اصلاح `CartContext.jsx`
> 
> 
> حالا `CartContext` نباید مستقیماً Axios را بشناسد: کامل جایگزین کن
> 
> ```python
> # frontend/src/context/CartContext.jsx
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
>   const fetchOrCreateCart = async () => {
>     setLoading(true);
> 
>     try {
>       // کاربر لاگین شده
>       if (isAuthenticated) {
>         const cartData = await cartService.getMyCart();
> 
>         setCart(cartData);
> 
>         if (cartData?.id) {
>           localStorage.setItem("cart_id", cartData.id);
>         }
> 
>         return;
>       }
> 
>       // کاربر مهمان
>       let cartId = localStorage.getItem("cart_id");
> 
>       if (!cartId) {
>         const newCart = await cartService.createCart();
> 
>         cartId = newCart.id;
> 
>         localStorage.setItem("cart_id", cartId);
> 
>         setCart(newCart);
> 
>         return;
>       }
> 
>       try {
>         const cartData = await cartService.getCart(cartId);
> 
>         setCart(cartData);
>       } catch (error) {
>         if (error.response?.status === 404) {
>           localStorage.removeItem("cart_id");
> 
>           const newCart = await cartService.createCart();
> 
>           localStorage.setItem("cart_id", newCart.id);
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
>   useEffect(() => {
>     fetchOrCreateCart();
>   }, [isAuthenticated]);
> 
>   const addToCart = async (productId) => {
>     try {
>       let cartId =
>         cart?.id ||
>         localStorage.getItem("cart_id");
> 
>       if (!cartId) {
>         const newCart = await cartService.createCart();
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
>         const invalidCart =
>           error.response?.status === 400 &&
>           error.response?.data?.cart_id;
> 
>         if (!invalidCart) {
>           throw error;
>         }
> 
>         localStorage.removeItem("cart_id");
> 
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
>         await cartService.addItem(
>           cartId,
>           productId,
>           1
>         );
>       }
> 
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
>   const clearCartState = () => {
>     setCart(null);
>   };
> 
>   const totalItemsCount =
>     cart?.items?.reduce(
>       (total, item) =>
>         total + item.quantity,
>       0
>     ) || 0;
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

#### چرا این تغییر مهم است؟

</aside>

قبلاً:

```powershell
CartContext.jsx
 ├── Axios GET
 ├── Axios POST
 ├── Axios PATCH
 ├── Axios DELETE
 ├── مدیریت token
 ├── مدیریت cart
 └── مدیریت state
```

یعنی Context بیش از حد مسئولیت داشت.

حالا:

```powershell
cartService.js
 └── ارتباط با API

CartContext.jsx
 └── مدیریت State و Business Flow

Cart.jsx
 └── نمایش UI
```

این دقیقاً همان تفکیکی است که در ادامه برای:

```powershell
Orders
Checkout
Payments
```

هم استفاده خواهیم کرد.

<aside>
💡

#### یک نکته مهم در Backend

</aside>

Backend فعلی Cart API این endpointها را در اختیار Frontend گذاشته:

```
GET     /api/carts/mine/
POST    /api/carts/
GET     /api/carts/<cart_id>/

POST    /api/carts/cart-items/
PATCH   /api/carts/cart-items/<item_id>/
DELETE  /api/carts/cart-items/<item_id>/
```

بنابراین `cartService.js` که بالا ساختیم دقیقاً با API فعلی Backend هماهنگ است.

<aside>
💡

#### یک نکته معماری مهم‌تر

</aside>

در Backend این قسمت را داریم:

```
classCartViewSet(...):permission_classes= [AllowAny]
```

و:

```
classCartItemViewSet(ModelViewSet):permission_classes= [AllowAny]
```

این برای **Guest Cart** فعلی قابل درک است، اما یک مسئله امنیتی مهم ایجاد می‌کند:

هر کسی که `cart_id` یک Cart را داشته باشد، می‌تواند بالقوه روی آن Cart عملیات انجام دهد.

مثلاً:

```
POST /cart-items/
PATCH /cart-items/<id>/
DELETE /cart-items/<id>/
```

هیچ بررسی‌ای وجود ندارد که آیا این Cart واقعاً متعلق به همان کاربر است یا نه.

**فعلاً این را دست نمی‌زنیم.**

<aside>
💡

#### مرحله فعلی ما

</aside>

در نتیجه الان:

```powershell
Cart Domain
    ↓
Cart API        ✅
    ↓
Cart Context    ✅ Refactored
    ↓
Add to Cart     ← مرحله بعد
```

اما قبل از اینکه وارد `Cart.jsx` شویم، یک چیز مهم باقی مانده:

#### باید `CartProvider` واقعاً در Root اپلیکیشن قرار گرفته باشد.

چون `CartContext` از `AuthContext` استفاده می‌کند:

```
const { isAuthenticated }=useAuth();
```

بنابراین ترتیب Providerها باید تقریباً این‌طور باشد:

```
AuthProvider
    ↓
CartProvider
    ↓
App
```

مشخص شد که **`CartProvider` هنوز در `main.jsx` قرار نگرفته**. پس قبل از رفتن به `Add to Cart` باید این لایه را درست کنیم.

الان ساختار شما این است:

```
AuthProvider
    ↓
App
```

ولی چون `CartContext` از `useAuth()` استفاده می‌کند، باید:

```
AuthProvider
    ↓
CartProvider
    ↓
App
```

باشد.

> 133- این فایل را اصلاح کن `main.jsx` 
فایل `frontend/src/main.jsx` را به این شکل تغییر بده:
> 
> 
> ```python
> import { StrictMode } from "react";
> import { createRoot } from "react-dom/client";
> 
> import App from "./App.jsx";
> 
> import { AuthProvider } from "./context/AuthContext.jsx";
> import { CartProvider } from "./context/CartContext.jsx";
> 
> import "./index.css";
> 
> createRoot(
>   document.getElementById("root")
> ).render(
>   <StrictMode>
>     <AuthProvider>
>       <CartProvider>
>         <App />
>       </CartProvider>
>     </AuthProvider>
>   </StrictMode>
> );
> ```
> 

<aside>
💡

#### چرا این ترتیب؟

</aside>

چون داخل `CartContext.jsx` داریم:

```
const { isAuthenticated }=useAuth();
```

پس `CartProvider` باید **داخل** `AuthProvider` باشد.

اگر برعکس بنویسیم:

```
CartProvider
    ↓
AuthProvider
```

`CartProvider` به Context احراز هویت دسترسی نخواهد داشت.

<aside>
💡

#### حالا یک نکته مهم درباره `StrictMode`

</aside>

در محیط Development، React با:

```
<StrictMode>
```

ممکن است بعضی lifecycle/effectها را عمداً دوبار اجرا کند تا side effectهای مشکل‌دار را پیدا کند.

ما در `CartContext` این را داریم:

```
useEffect(() => {fetchOrCreateCart();
}, [isAuthenticated]);
```

بنابراین ممکن است هنگام اجرای Development ببینی درخواست Cart بیش از یک بار ارسال شده است.

**فعلاً `StrictMode` را حذف نمی‌کنیم.**

این رفتار در Development است و حذف StrictMode راه‌حل معماری مناسبی نیست. اگر بعداً دیدیم درخواست‌های duplicate واقعاً مشکل ایجاد می‌کنند، همان منطق fetch را اصلاح می‌کنیم.

<aside>
💡

حالا Cart Provider آماده است

</aside>

معماری فعلی ما:

```
main.jsx
│
├── AuthProvider
│     │
│     └── CartProvider
│             │
│             └── App
│
└── index.css
```

و داخل Cart:

```
Cart.jsx
   │
   └── useCart()
          │
          └── CartContext
                  │
                  └── cartService
                          │
                          └── axiosInstance
                                  │
                                  └── Django API
```

این ساختار الان خیلی تمیزتر شده.

<aside>
💡

#### مرحله بعد: Add to Cart

</aside>

حالا می‌رسیم به اولین قابلیت واقعی Cart:

```
ProductCard
     ↓
Add to Cart
     ↓
useCart()
     ↓
addToCart(productId)
     ↓
cartService.addItem()
     ↓
POST /api/carts/cart-items/
     ↓
Django
```

> 134- نسخه کامل `ProductDetail.jsx`
> 
> 
> برای اینکه اشتباه در جابه‌جایی قسمت‌ها پیش نیاید، نسخه‌ی کامل فایل بعد از تغییر این است:
> `acron/frontend/src/pages/ProductDetail.jsx` 
> 
> [ProductDetail.jsx](ProductDetail.jsx)
> 

<aside>
💡

#### حالا `ProductCard`

</aside>

اینجا یک تصمیم معماری کوچک داریم.

در `ProductCard` فعلی، تمام کارت یک محصول است ولی هیچ actionای ندارد. برای فروشگاه، منطقی است که کاربر بتواند **مستقیماً از لیست محصولات هم محصول را به Cart اضافه کند**.

> 135- نسخه کامل `ProductCard.jsx`
> 
> 
> ```python
> import { useState } from "react";
> import { Link } from "react-router-dom";
> 
> import { useCart } from "../../../context/CartContext";
> 
> function ProductCard({ product }) {
>   const isAvailable =
>     product.inventory > 0;
> 
>   const { addToCart } = useCart();
> 
>   const [addingToCart, setAddingToCart] =
>     useState(false);
> 
>   const handleAddToCart = async () => {
>     if (!isAvailable) {
>       return;
>     }
> 
>     setAddingToCart(true);
> 
>     try {
>       await addToCart(product.id);
>     } catch (error) {
>       console.error(
>         "Failed to add product to cart:",
>         error
>       );
>     } finally {
>       setAddingToCart(false);
>     }
>   };
> 
>   return (
>     <article className="product-card">
> 
>       <Link
>         to={`/products/${product.slug}`}
>         className="product-card__image-link"
>       >
>         <div className="product-card__image">
> 
>           {product.main_image ? (
>             <img
>               src={product.main_image}
>               alt={product.name}
>               loading="lazy"
>             />
>           ) : (
>             <div className="product-card__no-image">
>               No image
>             </div>
>           )}
> 
>         </div>
>       </Link>
> 
>       <div className="product-card__content">
> 
>         {product.brand?.name && (
>           <span className="product-card__brand">
>             {product.brand.name}
>           </span>
>         )}
> 
>         <Link
>           to={`/products/${product.slug}`}
>           className="product-card__title"
>         >
>           {product.name}
>         </Link>
> 
>         <p className="product-card__description">
>           {product.description}
>         </p>
> 
>         <div className="product-card__footer">
> 
>           <div>
>             <span className="product-card__price">
>               {product.price}
>             </span>
>           </div>
> 
>           <span
>             className={
>               isAvailable
>                 ? "product-card__stock product-card__stock--available"
>                 : "product-card__stock product-card__stock--unavailable"
>             }
>           >
>             {isAvailable
>               ? "In stock"
>               : "Out of stock"}
>           </span>
> 
>         </div>
> 
>         <button
>           type="button"
>           className="product-card__cart-button"
>           disabled={
>             !isAvailable ||
>             addingToCart
>           }
>           onClick={handleAddToCart}
>         >
>           {addingToCart
>             ? "Adding..."
>             : "Add to cart"}
>         </button>
> 
>       </div>
> 
>     </article>
>   );
> }
> 
> export default ProductCard;
> ```
> 

<aside>
💡

#### یک نکته خیلی مهم درباره مسیر import

</aside>

چون `ProductCard.jsx` اینجاست:

```powershell
src/
└── features/
    └── products/
        └── components/
            └── ProductCard.jsx
```

برای رسیدن به:

```powershell
src/context/CartContext.jsx
```

باید سه مرحله به عقب برویم:

```powershell
components
   ↓ ..
products
   ↓ ..
features
   ↓ ..
src
   ↓
context
```

بنابراین:

```powershell
import { useCart } from "../../../context/CartContext";
```

درست است.

اما `ProductDetail.jsx` مستقیماً داخل `pages` است:

```powershell
src/pages/ProductDetail.jsx
```

پس فقط یک مرحله به `src` برمی‌گردیم:

```powershell
import { useCart } from "../context/CartContext";
```

<aside>
💡

#### حالا چه اتفاقی می‌افتد؟

</aside>

اگر کاربر در Product Detail روی:

```
Add to cart
```

کلیک کند:

```
ProductDetail
      ↓
handleAddToCart()
      ↓
addToCart(product.id)
      ↓
CartContext
      ↓
cartService.addItem()
      ↓
axiosInstance
      ↓
POST /api/carts/cart-items/
      ↓
CartItemSerializer
      ↓
CartItem
```

و بعد:

```
awaitfetchOrCreateCart();
```

اجرا می‌شود.

پس `cart` داخل Context نیز بلافاصله به‌روز می‌شود.

<aside>
💡

#### تست این مرحله

</aside>

حالا این کارها را انجام بده:

#### 1. Backend

```
python manage.py runserver
```

#### 2. Frontend

```
npm run dev
```

#### 3. وارد Products شو

```
/products
```

یک محصولی که `inventory > 0` دارد انتخاب کن.

#### 4. از Product Detail

روی:

```
Add to cart
```

کلیک کن.

باید درخواست زیر را در Network ببینی:

```
POST
/api/carts/cart-items/
```

<aside>
💡

#### وضعیت معماری الان

</aside>

```powershell
Cart Domain
    │
    ├── Cart API              ✅
    │
    ├── cartService           ✅
    │
    ├── CartContext           ✅
    │
    └── Add to Cart           ✅
          │
          ├── ProductCard     ✅
          └── ProductDetail   ✅
```

پس **مرحله بعدی دیگر API نیست**.

مرحله بعد:

```
Cart Page
   ↓
نمایش Cart Items
   ↓
Product
Quantity
Price
Total
```

و بعد از آن:

```
Quantity
   ↓
Remove Item
   ↓
Cart Summary
```

**فعلاً سراغ Orders نمی‌رویم**؛ ابتدا همین Cart را کامل و قابل استفاده می‌کنیم.

> 136- فایل`Cart.jsx` را کامل کنیم
> 
> 
> فایل:   `frontend/src/pages/Cart.jsx` 
> 
> را با این نسخه جایگزین کن:
> 
> ```jsx
> // frontend/src/pages/Cart.jsx
> import {Link }from"react-router-dom";import {useCart }from"../context/CartContext";functionCart() {const {
>     cart,
>     loading,
>     updateQuantity,
>     removeFromCart,
>   }=useCart();if (loading) {return (<mainclassName="page"><divclassName="page__container"><divclassName="page__header"><spanclassName="page__eyebrow">
>               ACRON STORE</span><h1>Your Cart</h1><p>
>               Loading your cart...</p></div></div></main>
>     );
>   }constitems=cart?.items|| [];if (items.length===0) {return (<mainclassName="page"><divclassName="page__container"><divclassName="page__header"><spanclassName="page__eyebrow">
>               ACRON STORE</span><h1>Your Cart</h1><p>
>               Your cart is currently empty.</p></div><Linkto="/products"className="cart__continue-shopping">
>             Continue Shopping</Link></div></main>
>     );
>   }return (<mainclassName="page"><divclassName="page__container"><divclassName="page__header"><spanclassName="page__eyebrow">
>             ACRON STORE</span><h1>Your Cart</h1><p>
>             Review your selected products
>             before continuing.</p></div><sectionclassName="cart"><divclassName="cart__items">
> 
>             {items.map((item) => (<articlekey={item.id}className="cart-item"><divclassName="cart-item__image">
> 
>                   {item.product?.main_image? (<imgsrc={item.product.main_image}alt={item.product.name}/>
>                   ): (<divclassName="cart-item__no-image">
>                       No image</div>
>                   )}</div><divclassName="cart-item__content"><Linkto={`/products/${item.product?.slug||""}`}className="cart-item__name">
>                     {item.product?.name}</Link><pclassName="cart-item__price">
>                     {item.product?.price}</p><divclassName="cart-item__actions"><divclassName="cart-item__quantity"><buttontype="button"onClick={() =>updateQuantity(item.id,item.quantity-1
>                           )
>                         }disabled={item.quantity<=1
>                         }aria-label="Decrease quantity">
>                         −</button><span>
>                         {item.quantity}</span><buttontype="button"onClick={() =>updateQuantity(item.id,item.quantity+1
>                           )
>                         }aria-label="Increase quantity">
>                         +</button></div><buttontype="button"className="cart-item__remove"onClick={() =>removeFromCart(item.id)
>                       }>
>                       Remove</button></div></div><divclassName="cart-item__total">
>                   {item.total_price}</div></article>
>             ))}</div><asideclassName="cart__summary"><h2>
>               Cart Summary</h2><divclassName="cart__summary-row"><span>
>                 Subtotal</span><strong>
>                 {cart.total_price}</strong></div><divclassName="cart__summary-divider"/><divclassName="cart__summary-row cart__summary-row--total"><span>
>                 Total</span><strong>
>                 {cart.total_price}</strong></div><buttontype="button"className="cart__checkout-button">
>               Proceed to Checkout</button><Linkto="/products"className="cart__continue-shopping">
>               Continue Shopping</Link></aside></section></div></main>
>   );
> }exportdefaultCart;
> ```
> 

<aside>
💡

#### چرا از `CartContext` استفاده کردیم؟

</aside>

در بالای صفحه:

```
const {
  cart,
  loading,
  updateQuantity,
  removeFromCart,
}=useCart();
```

یعنی `Cart.jsx` دیگر اصلاً نمی‌داند API کجاست.

ساختار:

```
Cart.jsx
   ↓
useCart()
   ↓
CartContext
   ↓
cartService
   ↓
axios
   ↓
Django
```

این همان separation است که می‌خواستیم.

<aside>
💡

#### اطلاعاتی که Backend به ما می‌دهد

</aside>

Serializer شما:

```
classCartItemSerializer(serializers.ModelSerializer):
```

این فیلدها را برمی‌گرداند:

```
id
product
quantity
total_price
```

و `product` هم:

```
id
name
price
main_image
```

بنابراین در Frontend می‌توانیم بنویسیم:

```
item.product.name
```

و:

```
item.product.price
```

و:

```
item.total_price
```

این کاملاً با Backend فعلی شما هماهنگ است.

<aside>
💡

#### و Quantity را همین الان هم داریم

</aside>

در Cart Page:

```
updateQuantity(item.id,item.quantity+1
)
```

برای افزایش.

و:

```
updateQuantity(item.id,item.quantity-1
)
```

برای کاهش.

و `CartContext` این را به:

```
PATCH /api/carts/cart-items/<item_id>/
```

تبدیل می‌کند.

Body:

```
{
  "quantity":2
}
```

بنابراین مسیر کامل:

```
+ button
   ↓
updateQuantity()
   ↓
cartService.updateItem()
   ↓
PATCH
   ↓
Django
   ↓
fetchOrCreateCart()
   ↓
UI Update
```

<aside>
💡

#### دکمه  Remove Item

</aside>

```
<buttontype="button"className="cart-item__remove"onClick={() =>removeFromCart(item.id)
  }>
  Remove</button>
```

در نهایت می‌رسد به:

```
DELETE /api/carts/cart-items/<item_id>/
```

و بعد Cart دوباره fetch می‌شود.

<aside>
💡

#### تحلیل Cart Summary

</aside>

در Backend این طراحی شده بود:

```python
defget_total_price(self,cart:Cart):returnsum([item.quantity*item.product.priceforitemincart.items.all()
    ])
```

بنابراین:

```
cart.total_price
```

مجموع قیمت Cart است.

و هر `CartItem` نیز:

```
item.total_price
```

دارد.

پس محاسبه قیمت را دوباره در Frontend انجام نمی‌دهیم.

این تصمیم خوبی است، چون **قیمت نهایی باید منبع معتبر Backend داشته باشد**.

<aside>
💡

#### یک مشکل کوچک که باید همین الان اصلاح کنیم

</aside>

در `CartSerializer`، محصول این فیلدها را دارد:

```
fields= ['id','name','price','main_image'
]
```

اما در Cart:

```
<Linkto={`/products/${item.product?.slug||""}`}>
```

ما `slug` نداریم.

در نتیجه لینک محصول در Cart فعلاً تبدیل می‌شود به:

```
/products/
```

این یک bug واقعی است.

### راه درست

چون Product Detail شما با:

```
/products/:slug
```

کار می‌کند، باید `slug` را به `SimpleProductSerializer` اضافه کنیم.

در:

```
backend/apps/carts/serializers.py
```

این:

```
fields= ['id','name','price','main_image']
```

را تبدیل کن به:

```
fields= ['id','name','slug','price','main_image',
]
```

یعنی:

این تغییر کاملاً منطقی است و API Cart همچنان سبک باقی می‌ماند.

> 137- در آدرس backend/apps/carts/serializers.py این را تغییر بده به کد زیر:
> 
> 
> ```python
> class SimpleProductSerializer(serializers.ModelSerializer):
>     class Meta:
>         model = Product
>         fields = [
>             'id',
>             'name',
>             'slug',
>             'price',
>             'main_image',
>         ]
> ```
> 

<aside>
💡

#### وضعیت پروژه

</aside>

الان تقریباً به اینجا رسیده‌ایم:

```python
Cart Domain
│
├── Cart API             ✅
│
├── cartService          ✅
│
├── Cart Context         ✅
│
├── Add to Cart          ✅
│
├── Cart Page            ✅
│
├── Quantity             ✅
│
├── Remove Item          ✅
│
└── Cart Summary         ✅
```

اما هنوز **یک مرحله مهم برای کیفیت این Domain داریم**: باید Cart را با سناریوهای واقعی تست کنیم، مخصوصاً:

```python
Guest
Login
Add product
Add same product again
Increase quantity
Decrease quantity
Remove item
Empty cart
Refresh page
```

بعد از اطمینان از این موارد، می‌رویم سراغ **Orders**.

فعلاً `Proceed to Checkout` را عمداً فعال نمی‌کنیم؛ چون طبق roadmap ما Checkout هنوز نوبتش نرسیده است.

<aside>
💡

و ترتیب توسعه اصلی ما همچنان تغییر نمی‌کند:

</aside>

یک نکته هم مهم است: **Cart را فعلاً تمام‌شده فرض نمی‌کنیم**؛ بلکه Feature اصلی آن پیاده شده و در ادامه، هنگام تست و مرحله‌ی Bug Fixing، مواردی مثل Guest Cart، Login Cart، refresh، موجودی، quantity و رفتارهای مرزی را بررسی می‌کنیم.

```python
Cart Domain
    ↓
Cart API                  ✅
    ↓
Cart Context              ✅
    ↓
Add to Cart               ✅
    ↓
Cart Page                 ✅
    ↓
Quantity                  ✅
    ↓
Remove Item               ✅
    ↓
Cart Summary              ✅
    ↓
Cart Testing / Integration
    ↓
Orders                    ← مرحله بعد
    ↓
Checkout
    ↓
Authentication Hardening
    ↓
Fix Product Images
    ↓
Fix Cart UI
    ↓
Security Hardening
    ↓
Bug / Edge Case Pass
```

<aside>
💡

#### قدم بعدی: Orders

</aside>

حالا از Cart خارج می‌شویم و وارد:  Orders Domain  می شویم.

قبل از اینکه کدی را تغییر دهیم، چون Backend مربوط به Orders از قبل در پروژه وجود دارد، باید قرارداد فعلی آن را با Frontend هماهنگ کنیم.

#### مرحله فعلی: Orders

الف: Backend این APIها را در اختیار ما می‌گذارد:

```python
GET    /api/orders/
GET    /api/orders/<order_id>/
POST   /api/orders/
POST   /api/orders/<order_id>/pay/
```

و چون:

```python
permission_classes = [permissions.IsAuthenticated]
```

است، Orders فقط برای کاربر احراز هویت‌شده قابل استفاده است.

معماری Frontend را هم مثل Cart نگه می‌داریم:

```python
Orders Page
     ↓
ordersService
     ↓
apiClient
     ↓
Django Orders API
     ↓
OrderViewSet
     ↓
OrderService
     ↓
Database
```

> 138- اول Orders Service بسازیم
> 
> 
> در Frontend ساختار شما از قبل Service-based است، پس یک فایل جدید ایجاد کن:
> 
> ```python
> frontend/src/features/orders/services/orderService.js
> ```
> 

> 139- محتوای آن:
> 
> 
> ```python
> import apiClient from "../../../services/apiClient";
> 
> const orderService = {
>   getOrders: async () => {
>     const response = await apiClient.get("/orders/");
>     return response.data;
>   },
> 
>   getOrderById: async (orderId) => {
>     const response = await apiClient.get(
>       `/orders/${orderId}/`
>     );
> 
>     return response.data;
>   },
> 
>   createOrder: async (cartId, shippingAddress) => {
>     const response = await apiClient.post(
>       "/orders/",
>       {
>         cart_id: cartId,
>         shipping_address: shippingAddress,
>       }
>     );
> 
>     return response.data;
>   },
> 
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

چرا Service جدا؟

نمی‌خواهیم `Orders.jsx` مستقیماً بنویسد:

```python
axios.get(...)
```

چون در آن صورت Page تبدیل می‌شود به محل:

- UI
- API
- Authentication
- Error handling
- Business logic

و با بزرگ شدن پروژه مدیریت آن سخت می‌شود.

الگو ، این مدل است:

```python
Page
 ↓
Service
 ↓
apiClient
```

> 140- س
> 
> 
> ```python
> 
> ```
> 

<aside>
📢

# پایان Part-18

</aside>