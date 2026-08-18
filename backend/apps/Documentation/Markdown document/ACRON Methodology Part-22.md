# ACRON Methodology Part-22

<aside>
📢

در Part-21 ، **فاز 11:**    Frontend - Presentation Layer  تمام شد. ( البته در آینده توسعه پیدا میکند.)

</aside>

# فاز 12: AI - Advisor

<aside>
💡

### 🎯 مرحله‌ای که الان شروع می‌کنیم

</aside>

ما هنوز **AI واقعی را به OpenAI یا مدل دیگری وصل نمی‌کنیم.**

اول باید **پوسته و معماری Advisor** را بسازیم.

چرا؟

چون اگر همین الان API هوش مصنوعی را وصل کنیم، احتمالاً خیلی سریع به یک Chat UI معمولی تبدیل می‌شویم.

هدف ما این نیست.

هدف:

```
                    ACRON
                      │
                      ▼
              "Should I buy this?"
                      │
                      ▼
                 AI Advisor
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       Product      User       Question
       Context     Context      Context
          │           │           │
          └───────────┼───────────┘
                      ▼
                 AI Response
                      │
                      ▼
               Buying Decision
```

بنابراین مرحله اول:

<aside>
💡

### مرحله 1 — ساخت Advisor Domain در Frontend

</aside>

ساختار هدف:

```
frontend/src/
│
├── domains/
│   │
│   └── advisor/
│       │
│       ├── components/
│       │   ├── AdvisorHero.jsx
│       │   ├── AdvisorInput.jsx
│       │   ├── AdvisorSuggestions.jsx
│       │   └── AdvisorMessage.jsx
│       │
│       ├── pages/
│       │   └── AdvisorPage.jsx
│       │
│       ├── services/
│       │   └── advisorService.js
│       │
│       └── context/
│           └── AdvisorContext.jsx
│
├── context/
│   ├── AuthContext.jsx
│   └── CartContext.jsx
│
├── services/
│   ├── cartService.js
│   └── ...
```

این نکته معماری مهم است:

**Advisor را داخل `components/` عمومی نمی‌گذاریم.**

چون Advisor یک **Domain** است، درست مثل Cart و Orders.

Backend شما هم همین تفکر را دارد؛ در مستندات پروژه، Advisor به‌عنوان یک Domain مستقل در کنار Customers، Products، Carts و Orders تعریف شده است.

<aside>
💡

### قدم 1 — ساخت پوشه‌ها

</aside>

> 1- در VS Code برو به:
> 
> 
> ```
> frontend/src
> ```
> 
> و این ساختار را ایجاد کن:
> 
> ```
> domains/
> └── advisor/
>     ├── components/
>     ├── pages/
>     ├── services/
>     └── context/
> ```
> 
> فعلاً **هیچ چیز دیگری را تغییر نده.**
> 

<aside>
💡

### قدم 2 — اولین Component

</aside>

> 2- اول این فایل را بساز:
> 
> 
> ```
> frontend/src/domains/advisor/components/AdvisorHero.jsx
> ```
> 
> داخل آن:
> 
> ```
> const AdvisorHero = () => {
>   return (
>     <section>
>       <p>ACRON Advisor</p>
> 
>       <h1>Should I buy this?</h1>
> 
>       <p>
>         Ask ACRON about a product before you buy it.
>       </p>
>     </section>
>   );
> };
> 
> export default AdvisorHero;
> ```
> 

### آموزش این Component

این قسمت:

```
const AdvisorHero = () => {
```

یک React Functional Component می‌سازد.

اسم آن:

```
AdvisorHero
```

است.

چرا `Hero`؟

چون قرار است این بخش در آینده یکی از مهم‌ترین قسمت‌های Homepage باشد.

---

این:

```
<p>ACRON Advisor</p>
```

نام Feature را معرفی می‌کند.

بعد:

```
<h1>Should I buy this?</h1>
```

**مهم‌ترین پیام محصول** است.

این دیگر یک متن تزئینی نیست.

این همان Product Promise ماست.

کاربر باید تقریباً بدون هیچ توضیح دیگری بفهمد:

> این سایت قرار است به من کمک کند بفهمم چیزی را بخرم یا نه.
> 

---

بعد:

```
<p>
  Ask ACRON about a product before you buy it.
</p>
```

فعلاً توضیح کوتاه Feature است.

بعداً می‌توانیم آن را بهتر کنیم.

<aside>
💡

### قدم 3 — Input

</aside>

> 3- حالا:
> 
> 
> ```
> frontend/src/domains/advisor/components/AdvisorInput.jsx
> ```
> 
> بساز.
> فعلاً این نسخه ساده:
> 
> ```python
> import { useState } from "react";
> 
> const AdvisorInput = ({ onSubmit }) => {
>   const [question, setQuestion] = useState("");
> 
>   const handleSubmit = (event) => {
>     event.preventDefault();
> 
>     const trimmedQuestion = question.trim();
> 
>     if (!trimmedQuestion) {
>       return;
>     }
> 
>     onSubmit(trimmedQuestion);
> 
>     setQuestion("");
>   };
> 
>   return (
>     <form onSubmit={handleSubmit}>
>       <input
>         type="text"
>         value={question}
>         onChange={(event) => setQuestion(event.target.value)}
>         placeholder="Ask ACRON about a product..."
>       />
> 
>       <button type="submit">
>         Ask ACRON
>       </button>
>     </form>
>   );
> };
> 
> export default AdvisorInput;
> ```
> 

### چرا این Component جداست؟

اینجا یکی از اصول مهم React را یاد می‌گیری.

ما می‌توانستیم همه این‌ها را داخل `AdvisorHero.jsx` بنویسیم.

مثلاً:

```
AdvisorHero
    ├── title
    ├── description
    ├── input
    ├── button
    └── suggestions
```

ولی این کار بعداً Component را بزرگ و غیرقابل مدیریت می‌کند.

پس:

```
AdvisorHero
     │
     └── AdvisorInput
```

هر Component یک مسئولیت مشخص دارد.

<aside>
💡

### قدم 4 — AdvisorSuggestions

</aside>

> 4- فایل:
> 
> 
> ```
> frontend/src/domains/advisor/components/AdvisorSuggestions.jsx
> ```
> 
> کد:
> 
> ```python
> const AdvisorSuggestions = ({ onSelect }) => {
>   const suggestions = [
>     "Is this good to buy?",
>     "Is this worth the price?",
>     "Is there a better alternative?",
>     "Is this good for programming?",
>   ];
> 
>   return (
>     <div>
>       {suggestions.map((suggestion) => (
>         <button
>           key={suggestion}
>           type="button"
>           onClick={() => onSelect(suggestion)}
>         >
>           {suggestion}
>         </button>
>       ))}
>     </div>
>   );
> };
> 
> export default AdvisorSuggestions;
> ```
> 

این بخش بسیار مهم است.

چرا؟

چون ما نمی‌خواهیم کاربر مجبور باشد بفهمد:

> «خب، حالا دقیقاً باید چه چیزی از AI بپرسم؟»
> 

به او چند سؤال آماده می‌دهیم.

مثلاً:

```python
Is this good to buy?

Is this worth the price?

Is there a better alternative?

Is this good for programming?
```

این دقیقاً به **کاهش سطح تخصص موردنیاز کاربر** کمک می‌کند.

<aside>
💡

### قدم 5 — AdvisorPage

</aside>

> 5- حالا:
> 
> 
> ```
> frontend/src/domains/advisor/pages/AdvisorPage.jsx
> ```
> 
> بساز:
> 
> ```python
> import AdvisorHero from "../components/AdvisorHero";
> import AdvisorInput from "../components/AdvisorInput";
> import AdvisorSuggestions from "../components/AdvisorSuggestions";
> 
> const AdvisorPage = () => {
>   const handleQuestionSubmit = (question) => {
>     console.log("Advisor question:", question);
>   };
> 
>   const handleSuggestionSelect = (question) => {
>     console.log("Advisor suggestion:", question);
>   };
> 
>   return (
>     <main>
>       <AdvisorHero />
> 
>       <AdvisorInput onSubmit={handleQuestionSubmit} />
> 
>       <AdvisorSuggestions
>         onSelect={handleSuggestionSelect}
>       />
>     </main>
>   );
> };
> 
> export default AdvisorPage;
> ```
> 

فعلاً وقتی کاربر سؤال را ارسال کند:

```
console.log(...)
```

داریم.

**این کاملاً عمدی است.**

هنوز Backend AI نداریم.

---

### چرا فعلاً `console.log`؟

این یک اصل مهم در توسعه است:

> **اول UI → بعد State → بعد API → بعد Business Logic → بعد AI**
> 

نه:

> AI API → بعد یک UI سریع دورش بسازیم.
> 

ما می‌خواهیم هر لایه مستقل و قابل تست باشد.

---

### معماری فعلی ما

در این مرحله:

```
AdvisorPage
     │
     ├──────────────► AdvisorHero
     │
     ├──────────────► AdvisorInput
     │                         │
     │                         ▼
     │                    User Question
     │
     └──────────────► AdvisorSuggestions
                               │
                               ▼
                           Question
```

و فعلاً:

```
Question
   │
   ▼
console.log()
```

در مرحله بعد:

```
Question
   │
   ▼
AdvisorContext
   │
   ▼
advisorService
   │
   ▼
Django API
```

و بعد:

```
Django
   │
   ▼
Advisor Service
   │
   ▼
AI Provider
   │
   ▼
AI Response
```

---

### ⚠️ اما هنوز یک کار انجام نده

فعلاً این فایل را **نساز**:

```
AdvisorContext.jsx
```

و همچنین:

```
advisorService.js
```

چون هنوز قرارداد API بین Frontend و Backend Advisor را مشخص نکرده‌ایم.

این خیلی مهم است.

اگر الان این را حدس بزنیم:

```
POST /api/advisor/
```

و مثلاً:

```
{
    "question": "Should I buy this?"
}
```

بعداً ممکن است بفهمیم Backend باید Product Context، User Context، conversation ID و غیره هم داشته باشد.

در نتیجه فعلاً API را حدس نمی‌زنیم.

---

<aside>
💡

### 🎯 نتیجه‌ای که باید الان به آن برسیم

</aside>

بعد از ساخت این چهار فایل:

```
domains/
└── advisor/
    ├── components/
    │   ├── AdvisorHero.jsx
    │   ├── AdvisorInput.jsx
    │   └── AdvisorSuggestions.jsx
    │
    └── pages/
        └── AdvisorPage.jsx
```

هنوز AI نداریم.

اما یک **Vertical Slice بسیار کوچک از Product Experience** داریم:

```
User
 │
 ▼
ACRON
 │
 ▼
Should I buy this?
 │
 ▼
Ask ACRON
 │
 ▼
Question
```

و این دقیقاً چیزی است که می‌خواهیم قبل از ورود به AI بسازیم.

قدم بعدی ما این خواهد بود:

### **اتصال `AdvisorPage` به Router و نمایش آن در مرورگر**

بعد از آن:

1. طراحی واقعی UI
2. انتقال State به `AdvisorContext`
3. طراحی `advisorService`
4. طراحی API Contract
5. ساخت Backend Advisor
6. اتصال AI
7. اتصال Product Context
8. تبدیل Advisor به Feature اصلی Homepage

و مهم‌تر از همه، **AI را از همان ابتدا طوری طراحی می‌کنیم که فقط یک Chatbot نباشد**؛ بلکه بتواند به اطلاعات محصول فعلی ACRON دسترسی داشته باشد. این موضوع با معماری فعلی Product Domain شما هم‌راستا است، چون Product API اطلاعاتی مثل نام، قیمت، موجودی، برند، دسته‌بندی و تصویر را در اختیار Frontend قرار می‌دهد.

<aside>
💡

### اضافه کردن Advisor به Routing

</aside>

> 6- حالا می‌رویم سراغ:
> 
> 
> ```
> frontend/src/App.jsx
> ```
> 
> در ابتدای فایل، بعد از importهای فعلی این را اضافه کن:
> 
> ```jsx
> import AdvisorPage from "./domains/advisor/pages/AdvisorPage";
> ```
> 
> بنابراین بخش importها باید تقریباً این شکلی شود:
> 
> ```jsx
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
> import Checkout from "./pages/Checkout";
> import AdvisorPage from "./pages/AdvisorPage";
> ```
> 

> 7- حالا داخل `<Routes>`، مثلاً بعد از Home، این Route را اضافه کن:
> 
> 
> ```jsx
> <Route
>   path="/advisor"
>   element={<AdvisorPage />}
> />
> ```
> 
> در نتیجه:
> 
> ```jsx
> <Routes>
> 
>   <Route
>     path="/"
>     element={<Home />}
>   />
> 
>   <Route
>     path="/advisor"
>     element={<AdvisorPage />}
>   />
> 
>   <Route
>     path="/login"
>     element={<Login />}
>   />
> 
>   <Route
>     path="/products"
>     element={<Products />}
>   />
> 
>   <Route
>     path="/products/:slug"
>     element={<ProductDetail />}
>   />
> 
>   <Route
>     path="/cart"
>     element={<Cart />}
>   />
> 
>   <Route
>     path="/orders"
>     element={<Orders />}
>   />
> 
>   <Route
>     path="/checkout"
>     element={<Checkout />}
>   />
> 
> </Routes>
> ```
> 

<aside>
💡

### تست

</aside>

حالا Frontend را اجرا کن:

```
npm run dev
```

بعد در مرورگر برو به:

```
http://localhost:5173/advisor
```

یا اگر Vite روی `127.0.0.1` اجرا می‌شود:

```
http://127.0.0.1:5173/advisor
```

### چیزی که فعلاً انتظار داریم

صفحه باید این ساختار را نمایش دهد:

```
                 ACRON Advisor

          AdvisorHero
              │
              ▼
        AdvisorInput
              │
              ▼
      AdvisorSuggestions
```

اما **هنوز AI واقعی نداریم.**

این کاملاً عمدی است.

در حال حاضر:

```
const handleQuestionSubmit = (question) => {
  console.log("Advisor question:", question);
};
```

فقط سؤال را در Console چاپ می‌کند.

یعنی مثلاً کاربر بزند:

> Is this good to buy?
> 

در Console باید چیزی شبیه این ببینی:

```
Advisor question: Is this good to buy?
```

---

<aside>
💡

### چرا فعلاً AI را وصل نمی‌کنیم؟

</aside>

این قسمت خیلی مهم است.

ما نمی‌خواهیم فعلاً این کار را بکنیم:

```
Input
 ↓
OpenAI API
 ↓
Answer
```

چون هنوز **قرارداد Domain Advisor** را مشخص نکرده‌ایم.

هدف نهایی ما چیزی شبیه این است:

```
                 USER
                   │
                   ▼
          "Is this good to buy?"
                   │
                   ▼
            ACRON ADVISOR
                   │
          ┌────────┴────────┐
          │                 │
          ▼                 ▼
       Product           Question
       Context           Context
          │                 │
          └────────┬────────┘
                   ▼
              AI Advisor
                   │
                   ▼
             Recommendation
```

و این Recommendation باید بعداً بتواند مثلاً بگوید:

> **Good choice for your needs.**
> 

یا:

> **I wouldn't recommend this product because...**
> 

یا حتی:

> **It depends on what you're looking for.**
> 

این همان چیزی است که ACRON را از یک فروشگاه معمولی به سمت **AI-assisted commerce** می‌برد.

<aside>
💡

### یک نکته معماری مهم

</aside>

در این مرحله هنوز `AdvisorPage.jsx` را جابه‌جا نمی‌کنیم.

ساختار فعلی:

```
pages/
└── AdvisorPage.jsx
```

برای شروع مشکلی ندارد.

ولی اگر Advisor بزرگ شود، احتمالاً به ساختار قوی‌تری می‌رسیم، مثلاً:

```
src/
└── domains/
    └── advisor/
        ├── components/
        │   ├── AdvisorHero.jsx
        │   ├── AdvisorInput.jsx
        │   ├── AdvisorSuggestions.jsx
        │   └── AdvisorMessage.jsx
        │
        ├── pages/
        │   └── AdvisorPage.jsx
        │
        ├── services/
        │   └── advisorService.js
        │
        └── context/
            └── AdvisorContext.jsx
```

اما **فعلاً این کار را انجام نمی‌دهیم**. مرحله‌به‌مرحله رشد می‌دهیم.

> 8- ساخت فایل `AdvisorHero.jsx`
> 
> 
> ```
> src/domains/advisor/components/AdvisorHero.jsx
> ```
> 
> فعلاً این ساختار را قرار بده:
> 
> ```jsx
> const AdvisorHero = () => {
>   return (
>     <section className="advisor-hero">
>       <h1>ACRON Advisor</h1>
> 
>       <p>
>         Your intelligent shopping assistant.
>       </p>
> 
>       <p>
>         Ask me anything about products, orders, or shopping.
>       </p>
>     </section>
>   );
> };
> 
> export default AdvisorHero;
> ```
> 

> 9- داخل فایل `AdvisorInput.jsx`
> 
> 
> ```
> src/domains/advisor/components/AdvisorInput.jsx
> ```
> 
> قرار بده:
> 
> ```jsx
> import { useState } from "react";
> 
> const AdvisorInput = ({ onSubmit }) => {
>   const [question, setQuestion] = useState("");
> 
>   const handleSubmit = (event) => {
>     event.preventDefault();
> 
>     const trimmedQuestion = question.trim();
> 
>     if (!trimmedQuestion) {
>       return;
>     }
> 
>     onSubmit(trimmedQuestion);
> 
>     setQuestion("");
>   };
> 
>   return (
>     <form onSubmit={handleSubmit} className="advisor-input">
>       <input
>         type="text"
>         value={question}
>         onChange={(event) => setQuestion(event.target.value)}
>         placeholder="Ask ACRON Advisor..."
>       />
> 
>       <button type="submit">
>         Ask
>       </button>
>     </form>
>   );
> };
> 
> export default AdvisorInput;
> ```
> 

اینجا یک نکته معماری مهم داریم:

`AdvisorInput` خودش تصمیم نمی‌گیرد سؤال چه کاری انجام دهد.

فقط سؤال را دریافت می‌کند:

```
User
 ↓
AdvisorInput
 ↓
onSubmit(question)
 ↓
AdvisorPage
```

این دقیقاً همان چیزی است که بعداً اجازه می‌دهد API را بدون خراب کردن UI اضافه کنیم.

<aside>
💡

### ساخت Suggestions

</aside>

> 10- فایل:
> 
> 
> ```
> src/domains/advisor/components/AdvisorSuggestions.jsx
> ```
> 
> را به این شکل قرار بده:
> 
> ```jsx
> const suggestions = [
>   "What products do you recommend?",
>   "Show me my recent orders",
>   "Help me find a product",
>   "What can ACRON Advisor do?",
> ];
> 
> const AdvisorSuggestions = ({ onSelect }) => {
>   return (
>     <section className="advisor-suggestions">
>       <h2>Suggested questions</h2>
> 
>       <div className="advisor-suggestions-list">
>         {suggestions.map((suggestion) => (
>           <button
>             key={suggestion}
>             type="button"
>             onClick={() => onSelect(suggestion)}
>           >
>             {suggestion}
>           </button>
>         ))}
>       </div>
>     </section>
>   );
> };
> 
> export default AdvisorSuggestions;
> ```
> 

الان جریان ما این است:

```
                    AdvisorPage
                         │
            ┌────────────┼────────────┐
            ↓            ↓            ↓
       AdvisorHero  AdvisorInput  AdvisorSuggestions
                         │            │
                         ↓            ↓
                    question      suggestion
                         │            │
                         └─────┬──────┘
                               ↓
                     AdvisorPage handler
```

این معماری برای مرحله بعد خیلی مهم است.

<aside>
💡

### هنوز API نسازیم

</aside>

در این مرحله **نباید** سریع برویم سراغ:

```
OpenAI
ChatGPT API
Django API
Celery
Redis
WebSocket
```

اول باید Frontend flow را کامل کنیم.

مرحله بعدی ما:

```
User enters question
        ↓
AdvisorInput
        ↓
AdvisorPage
        ↓
Question State
        ↓
AdvisorResponse
```

بنابراین Component جدیدی لازم داریم:

```
components/
├── AdvisorHero.jsx
├── AdvisorInput.jsx
├── AdvisorSuggestions.jsx
└── AdvisorResponse.jsx
```

و بعد جریان واقعی Chat را می‌سازیم:

```
User
 │
 │ "I need a laptop"
 ↓
AdvisorInput
 │
 ↓
AdvisorPage
 │
 ↓
messages[]
 │
 ↓
AdvisorResponse
```

بعد از آن تازه می‌رسیم به:

```
React
  ↓
Advisor Service
  ↓
Django REST API
  ↓
Advisor Service
  ↓
AI
```

و اینجا Advisor از یک UI ساده تبدیل می‌شود به یک **Domain واقعی در ACRON**.

### پس فعلاً این کار را انجام بده

1. `AdvisorPage` را به `/advisor` وصل کن.
2. سه Component بالا را با کدهای جدید جایگزین کن.
3. به `/advisor` برو.
4. یک سؤال در Input بنویس.
5. روی **Ask** بزن.
6. روی یکی از Suggested Questions هم کلیک کن.
7. در Console باید مقدار سؤال را ببینی.

وقتی این تست انجام شد، **مرحله بعدی را با ساخت `AdvisorResponse` و state مربوط به conversation ادامه می‌دهیم**؛ یعنی از UI استاتیک وارد ساختار واقعی Chat می‌شویم.

<aside>
💡

### ساخت `AdvisorResponse`

</aside>

ساختار Domain:

```
src/
└── domains/
    └── advisor/
        ├── components/
        │   ├── AdvisorHero.jsx
        │   ├── AdvisorInput.jsx
        │   ├── AdvisorSuggestions.jsx
        │   └── AdvisorResponse.jsx
        │
        └── pages/
            └── AdvisorPage.jsx
```

> 11- فایل جدید:
> 
> 
> ```
> src/domains/advisor/components/AdvisorResponse.jsx
> ```
> 
> کد:
> 
> ```jsx
> const AdvisorResponse = ({ messages }) => {
>   if (!messages.length) {
>     return null;
>   }
> 
>   return (
>     <section className="advisor-response">
>       {messages.map((message) => (
>         <div
>           key={message.id}
>           className={`advisor-message advisor-message-${message.role}`}
>         >
>           <p>{message.content}</p>
>         </div>
>       ))}
>     </section>
>   );
> };
> 
> export default AdvisorResponse;
> ```
> 

اینجا `messages` آرایه‌ای از پیام‌هاست.

مثلاً:

```
[
  {
    id: 1,
    role: "user",
    content: "I need a laptop"
  },
  {
    id: 2,
    role: "assistant",
    content: "Sure! What is your budget?"
  }
]
```

<aside>
💡

### مدیریت Conversation در `AdvisorPage`

</aside>

> 12- حالا `AdvisorPage.jsx` را تغییر بده.
> 
> 
> ```jsx
> import { useState } from "react";
> 
> import AdvisorHero from "../components/AdvisorHero";
> import AdvisorInput from "../components/AdvisorInput";
> import AdvisorSuggestions from "../components/AdvisorSuggestions";
> import AdvisorResponse from "../components/AdvisorResponse";
> 
> const AdvisorPage = () => {
>   const [messages, setMessages] = useState([]);
> 
>   const handleQuestionSubmit = (question) => {
>     const userMessage = {
>       id: Date.now(),
>       role: "user",
>       content: question,
>     };
> 
>     setMessages((currentMessages) => [
>       ...currentMessages,
>       userMessage,
>     ]);
>   };
> 
>   const handleSuggestionSelect = (question) => {
>     handleQuestionSubmit(question);
>   };
> 
>   return (
>     <main>
>       <AdvisorHero />
> 
>       <AdvisorResponse messages={messages} />
> 
>       <AdvisorInput onSubmit={handleQuestionSubmit} />
> 
>       <AdvisorSuggestions onSelect={handleSuggestionSelect} />
>     </main>
>   );
> };
> 
> export default AdvisorPage;
> ```
> 

حالا یک تغییر مهم در معماری اتفاق افتاده است:

```
                    AdvisorPage
                         │
                         │ owns state
                         ↓
                     messages[]
                         │
          ┌──────────────┴──────────────┐
          ↓                             ↓
 AdvisorResponse                  AdvisorInput
          │                             │
          │                             ↓
          │                        question
          │                             │
          └──────────────←──────────────┘
```

یعنی **State مربوط به Conversation در Page نگهداری می‌شود**، نه داخل Input.

این تصمیم برای ادامه پروژه بسیار مهم است.

<aside>
💡

### تست

</aside>

حالا برو:

```
http://localhost:5173/advisor
```

و بنویس:

```
I need a laptop
```

بعد روی `Ask` کلیک کن.

باید پیام در صفحه ظاهر شود.

مثلاً:

```
I need a laptop
```

اگر سؤال دیگری بفرستی:

```
Show me products under $1000
```

باید هر دو پیام نمایش داده شوند:

```
I need a laptop

Show me products under $1000
```

و اگر روی Suggested Question کلیک کنی، آن سؤال هم باید وارد Conversation شود.

<aside>
💡

### الان یک مشکل داریم

</aside>

در حال حاضر Advisor فقط **پیام User** را ذخیره می‌کند.

یعنی:

```
User
 ↓
Question
 ↓
messages[]
```

اما چیزی نداریم که جواب بدهد.

برای همین یک Response موقت ایجاد می‌کنیم.

فعلاً AI نداریم؛ بنابراین یک پاسخ Fake می‌سازیم تا معماری Conversation را تست کنیم.

> 13- در `AdvisorPage.jsx`:
> 
> 
> ```jsx
> const handleQuestionSubmit = (question) => {
>   const userMessage = {
>     id: Date.now(),
>     role: "user",
>     content: question,
>   };
> 
>   const assistantMessage = {
>     id: Date.now() + 1,
>     role: "assistant",
>     content: "I'm processing your question...",
>   };
> 
>   setMessages((currentMessages) => [
>     ...currentMessages,
>     userMessage,
>     assistantMessage,
>   ]);
> };
> ```
> 

حالا جریان:

```
User
 │
 │ Question
 ↓
AdvisorPage
 │
 ├── User Message
 │
 └── Assistant Message
```

و UI:

```
┌─────────────────────────────────────┐
│ I need a laptop                     │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ I'm processing your question...     │
└─────────────────────────────────────┘
```

<aside>
💡

### اما این معماری را فعلاً نگه نمی‌داریم

</aside>

این قسمت خیلی مهم است.

نباید در نهایت `AdvisorPage` تبدیل شود به چیزی مثل:

```
const handleQuestionSubmit = () => {
   // API
   // Axios
   // authentication
   // loading
   // error
   // AI
   // response parsing
   // ...
};
```

این کار Page را به یک Component بزرگ و غیرقابل نگهداری تبدیل می‌کند.

هدف نهایی ما این است:

```
AdvisorPage
     │
     ↓
useAdvisor()
     │
     ↓
advisorService
     │
     ↓
Django API
     │
     ↓
AI
```

بنابراین بعد از اینکه Conversation UI را تثبیت کردیم، منطق را به:

```
hooks/
└── useAdvisor.js
```

و API را به:

```
services/
└── advisorService.js
```

منتقل می‌کنیم.

<aside>
💡

### Loading State

</aside>

قبل از رفتن به Service، بهتر است Loading را هم در معماری داشته باشیم.

> 14- در `AdvisorPage.jsx`:
> 
> 
> ```python
> const [isLoading, setIsLoading] = useState(false);
> ```
> 
> و هنگام ارسال:
> 
> ```jsx
> const handleQuestionSubmit = (question) => {
>   const userMessage = {
>     id: Date.now(),
>     role: "user",
>     content: question,
>   };
> 
>   setMessages((currentMessages) => [
>     ...currentMessages,
>     userMessage,
>   ]);
> 
>   setIsLoading(true);
> 
>   setTimeout(() => {
>     const assistantMessage = {
>       id: Date.now() + 1,
>       role: "assistant",
>       content: "I'm processing your question...",
>     };
> 
>     setMessages((currentMessages) => [
>       ...currentMessages,
>       assistantMessage,
>     ]);
> 
>     setIsLoading(false);
>   }, 1000);
> };
> ```
> 

<aside>
💡

### در نهایت

</aside>

> 15- یعنی فایل `AdvisorPage.jsx` را فعلاً **کامل** به این شکل قرار بده:
> 
> 
> ```python
> import { useState } from "react";
> 
> import AdvisorHero from "../components/AdvisorHero";
> import AdvisorInput from "../components/AdvisorInput";
> import AdvisorSuggestions from "../components/AdvisorSuggestions";
> import AdvisorResponse from "../components/AdvisorResponse";
> 
> const AdvisorPage = () => {
>   const [messages, setMessages] = useState([]);
>   const [isLoading, setIsLoading] = useState(false);
> 
>   const handleQuestionSubmit = (question) => {
>     const userMessage = {
>       id: Date.now(),
>       role: "user",
>       content: question,
>     };
> 
>     setMessages((currentMessages) => [
>       ...currentMessages,
>       userMessage,
>     ]);
> 
>     setIsLoading(true);
> 
>     setTimeout(() => {
>       const assistantMessage = {
>         id: Date.now() + 1,
>         role: "assistant",
>         content: "I'm processing your question...",
>       };
> 
>       setMessages((currentMessages) => [
>         ...currentMessages,
>         assistantMessage,
>       ]);
> 
>       setIsLoading(false);
>     }, 1000);
>   };
> 
>   const handleSuggestionSelect = (question) => {
>     handleQuestionSubmit(question);
>   };
> 
>   return (
>     <main>
>       <AdvisorHero />
> 
>       <AdvisorResponse messages={messages} />
> 
>       <AdvisorInput
>         onSubmit={handleQuestionSubmit}
>         disabled={isLoading}
>       />
> 
>       <AdvisorSuggestions
>         onSelect={handleSuggestionSelect}
>       />
>     </main>
>   );
> };
> 
> export default AdvisorPage;
> ```
> 

### دقیقاً چه چیزی تغییر کرد؟

قبلاً داشتی:

```
<AdvisorInput onSubmit={handleQuestionSubmit} />
```

آن را **حذف کن** و این را جایگزینش کن:

```
<AdvisorInput
  onSubmit={handleQuestionSubmit}
  disabled={isLoading}
/>
```

همچنین بالای فایل این را اضافه کردیم:

```
const [isLoading, setIsLoading] = useState(false);
```

و یادت باشد که فایل `AdvisorInput.jsx` هم باید نسخه‌ای باشد که `disabled` را دریافت می‌کند:

و یادت باشد که فایل `AdvisorInput.jsx` هم باید نسخه‌ای باشد که `disabled` را دریافت می‌کند:

```
const AdvisorInput = ({ onSubmit, disabled = false }) => {
```

و در input و button:

```
disabled={disabled}
```

در نتیجه جریان فعلی این است:

```
User
 ↓
Question
 ↓
AdvisorInput
 ↓
handleQuestionSubmit()
 ↓
isLoading = true
 ↓
"Thinking..."
 ↓
1 second
 ↓
Assistant response
 ↓
isLoading = false
 ↓
Input دوباره فعال
```

**فعلاً همین مرحله را تست کن.** اگر بدون خطا اجرا شد، قدم بعدی را می‌رویم سراغ `useAdvisor.js` تا منطق را از `AdvisorPage.jsx` خارج کنیم؛ این مرحله برای تمیز نگه‌داشتن معماری ACRON مهم است.

### الان دقیقاً چه چیزی را تست کنیم؟

هدف این مرحله این است که مطمئن شویم:

1. صفحه Advisor بدون Error باز می‌شود.
2. سپس Input کار می‌کند.
3. با زدن `Ask` پیام کاربر نمایش داده می‌شود.
4. دکمه برای حدود ۱ ثانیه به `Thinking...` تغییر می‌کند.
5. پاسخ آزمایشی Advisor نمایش داده می‌شود.
6. بعد از پاسخ، Input دوباره فعال می‌شود.
7. سپس Suggested Questions هم کار می‌کنند.

<aside>
💡

### یک تست مهم‌تر

</aside>

حالا صفحه را Refresh کن:

```
Ctrl + R
```

بعد دوباره به:

```
http://localhost:5173/advisor
```

برو.

باید Conversation پاک شده باشد.

این اتفاق **فعلاً طبیعی است**.

چرا؟

چون هنوز Conversation را در Backend یا Local Storage ذخیره نکرده‌ایم.

در حال حاضر:

```
Browser
   ↓
React State
   ↓
messages[]
```

داریم.

با Refresh شدن صفحه:

```
React State
   ↓
Reset
```

می‌شود.

<aside>
💡

### چرا این تست را انجام می‌دهیم؟

</aside>

چون هنوز نمی‌خواهیم وارد Backend شویم.

ما داریم مراحل را جداگانه می‌سازیم:

```
مرحله 1
UI
↓
مرحله 2
React State
↓
مرحله 3
Conversation
↓
مرحله 4
Custom Hook
↓
مرحله 5
Service
↓
مرحله 6
Django API
↓
مرحله 7
AI
```

الان تقریباً در **مرحله 3** هستیم.

اگر همین الان مستقیم برویم سراغ Django API، وقتی مشکلی ایجاد شود نمی‌دانیم مشکل از:

```
React؟
State؟
Component؟
Axios؟
Django؟
URL؟
Authentication؟
API؟
```

است.

ولی اگر هر لایه را جدا تست کنیم، دقیق می‌دانیم مشکل کجاست.

حالا دقیقاً طبق معماری ACRON، منطق Conversation را از `AdvisorPage` خارج می‌کنیم و به یک **Custom Hook** منتقل می‌کنیم.

هدف این مرحله:

```
AdvisorPage
     │
     ↓
useAdvisor()
     │
     ├── messages
     ├── isLoading
     ├── submitQuestion()
     └── selectSuggestion()
```

هنوز **Django و AI را وصل نمی‌کنیم**. اول این لایه را تمیز می‌کنیم.

<aside>
💡

### مرحله 1 — ساخت `useAdvisor.js`

</aside>

> 16- داخل پروژه برو به:
> 
> 
> ```
> frontend/src/domains/advisor/
> ```
> 
> اگر `hooks` وجود ندارد، بساز:
> 
> ```
> advisor/
> ├── components/
> ├── hooks/
> │   └── useAdvisor.js
> └── pages/
>     └── AdvisorPage.jsx
> ```
> 

> 17- فایل جدید:
> 
> 
> ```
> src/domains/advisor/hooks/useAdvisor.js
> ```
> 
> داخل آن قرار بده:
> 
> ```jsx
> import { useState } from "react";
> 
> const useAdvisor = () => {
>   const [messages, setMessages] = useState([]);
>   const [isLoading, setIsLoading] = useState(false);
> 
>   const submitQuestion = (question) => {
>     const userMessage = {
>       id: Date.now(),
>       role: "user",
>       content: question,
>     };
> 
>     setMessages((currentMessages) => [
>       ...currentMessages,
>       userMessage,
>     ]);
> 
>     setIsLoading(true);
> 
>     setTimeout(() => {
>       const assistantMessage = {
>         id: Date.now() + 1,
>         role: "assistant",
>         content: "I'm processing your question...",
>       };
> 
>       setMessages((currentMessages) => [
>         ...currentMessages,
>         assistantMessage,
>       ]);
> 
>       setIsLoading(false);
>     }, 1000);
>   };
> 
>   const selectSuggestion = (question) => {
>     submitQuestion(question);
>   };
> 
>   return {
>     messages,
>     isLoading,
>     submitQuestion,
>     selectSuggestion,
>   };
> };
> 
> export default useAdvisor;
> ```
> 

<aside>
💡

### مرحله 2 — چرا این کار را کردیم؟

</aside>

قبلاً `AdvisorPage.jsx` هم UI داشت و هم منطق:

```
AdvisorPage
├── UI
├── messages
├── isLoading
├── submitQuestion
└── suggestion logic
```

این در پروژه کوچک قابل قبول است، ولی ACRON قرار است بزرگ شود.

حالا:

```
AdvisorPage
      │
      ↓
  useAdvisor
      │
      ├── messages
      ├── loading
      └── actions
```

بنابراین `Page` فقط مسئول ترکیب Componentها است.

<aside>
💡

### مرحله 3 — اصلاح `AdvisorPage.jsx`

</aside>

> 18- حالا کل فایل:
> 
> 
> ```
> src/domains/advisor/pages/AdvisorPage.jsx
> ```
> 
> را به این تبدیل کن:
> 
> ```jsx
> import AdvisorHero from "../components/AdvisorHero";
> import AdvisorInput from "../components/AdvisorInput";
> import AdvisorSuggestions from "../components/AdvisorSuggestions";
> import AdvisorResponse from "../components/AdvisorResponse";
> 
> import useAdvisor from "../hooks/useAdvisor";
> 
> const AdvisorPage = () => {
>   const {
>     messages,
>     isLoading,
>     submitQuestion,
>     selectSuggestion,
>   } = useAdvisor();
> 
>   return (
>     <main>
>       <AdvisorHero />
> 
>       <AdvisorResponse messages={messages} />
> 
>       <AdvisorInput
>         onSubmit={submitQuestion}
>         disabled={isLoading}
>       />
> 
>       <AdvisorSuggestions
>         onSelect={selectSuggestion}
>       />
>     </main>
>   );
> };
> 
> export default AdvisorPage;
> ```
> 

دقت کن که دیگر اینجا نداریم:

```
useState
```

و دیگر این‌ها را هم نداریم:

```
handleQuestionSubmit
handleSuggestionSelect
```

همه این منطق منتقل شده به:

```
hooks/useAdvisor.js
```

<aside>
💡

### مرحله 4 — تست دوباره

</aside>

حالا Browser را باز نگه دار:

```
http://localhost:5173/advisor
```

یک سؤال بپرس:

```
I need a laptop
```

باید همان رفتار قبلی را ببینی:

```
I need a laptop

Thinking...

I'm processing your question...
```

بعد یک Suggested Question را امتحان کن.

اگر همه چیز درست باشد، یعنی:

```
AdvisorPage
      ↓
useAdvisor
      ↓
AdvisorInput
      ↓
AdvisorResponse
```

به درستی کار می‌کند.

<aside>
💡

### مرحله 5 — حالا یک تغییر معماری مهم

</aside>

در حال حاضر `useAdvisor` هنوز این کار را انجام می‌دهد:

```
setTimeout(...)
```

این فقط Mock است.

ما در نهایت چنین چیزی نمی‌خواهیم:

```
useAdvisor
     ↓
setTimeout
```

بلکه می‌خواهیم:

```
useAdvisor
     ↓
advisorService
     ↓
Django API
```

بنابراین قدم بعدی ساخت Service است.

<aside>
💡

### مرحله 6 — ساخت `advisorService.js`

</aside>

> 19- داخل:
> 
> 
> ```
> frontend/src/domains/advisor/
> ```
> 
> یک پوشه بساز:
> 
> ```
> services
> ```
> 
> ساختار:
> 
> ```
> advisor/
> ├── components/
> ├── hooks/
> │   └── useAdvisor.js
> ├── pages/
> │   └── AdvisorPage.jsx
> └── services/
>     └── advisorService.js
> ```
> 

> 20- فایل:
> 
> 
> ```
> src/domains/advisor/services/advisorService.js
> ```
> 
> فعلاً این کد را قرار بده:
> 
> ```jsx
> const askAdvisor = async (question) => {
>   console.log("Advisor service received:", question);
> 
>   return {
>     role: "assistant",
>     content: "I'm processing your question...",
>   };
> };
> 
> export default {
>   askAdvisor,
> };
> ```
> 

این هنوز به Django وصل نیست.

فقط یک abstraction ایجاد کرده‌ایم:

```
UI
 ↓
Hook
 ↓
Service
 ↓
[Backend - later]
```

<aside>
💡

### مرحله 7 — اتصال Hook به Service

</aside>

> 21- حالا `useAdvisor.js` را تغییر بده.
> 
> 
> کد کامل:
> 
> ```python
> import { useState } from "react";
> 
> import advisorService from "../services/advisorService";
> 
> const useAdvisor = () => {
>   const [messages, setMessages] = useState([]);
>   const [isLoading, setIsLoading] = useState(false);
> 
>   const submitQuestion = async (question) => {
>     const userMessage = {
>       id: Date.now(),
>       role: "user",
>       content: question,
>     };
> 
>     setMessages((currentMessages) => [
>       ...currentMessages,
>       userMessage,
>     ]);
> 
>     setIsLoading(true);
> 
>     try {
>       const assistantMessage =
>         await advisorService.askAdvisor(question);
> 
>       setMessages((currentMessages) => [
>         ...currentMessages,
>         {
>           id: Date.now() + 1,
>           ...assistantMessage,
>         },
>       ]);
>     } catch (error) {
>       console.error("Advisor error:", error);
> 
>       setMessages((currentMessages) => [
>         ...currentMessages,
>         {
>           id: Date.now() + 1,
>           role: "assistant",
>           content:
>             "Something went wrong. Please try again.",
>         },
>       ]);
>     } finally {
>       setIsLoading(false);
>     }
>   };
> 
>   const selectSuggestion = (question) => {
>     submitQuestion(question);
>   };
> 
>   return {
>     messages,
>     isLoading,
>     submitQuestion,
>     selectSuggestion,
>   };
> };
> 
> export default useAdvisor;
> ```
> 

حالا معماری ما این شده:

```
                AdvisorPage
                     │
                     ↓
                useAdvisor
                     │
                     ↓
              advisorService
                     │
                     ↓
               ┌──────────┐
               │  Django  │
               │   API    │
               └──────────┘
```

فعلاً Service یک پاسخ Mock برمی‌گرداند.

<aside>
💡

### مرحله 8 — تست مهم

</aside>

دوباره:

```
http://localhost:5173/advisor
```

را باز کن.

سؤال:

```
I need a laptop
```

را بفرست.

این بار باید همان نتیجه قبلی را بگیری.

اما یک تفاوت مهم وجود دارد.

در Console مرورگر باید چیزی شبیه این ببینی:

```
Advisor service received: I need a laptop
```

این نشان می‌دهد که درخواست واقعاً از:

```
AdvisorPage
 ↓
useAdvisor
 ↓
advisorService
```

عبور کرده است.

<aside>
💡

## معماری فعلی ACRON

</aside>

در این نقطه Domain ما به شکل تمیزتری درآمده:

```
advisor/
│
├── components/
│   ├── AdvisorHero.jsx
│   ├── AdvisorInput.jsx
│   ├── AdvisorSuggestions.jsx
│   └── AdvisorResponse.jsx
│
├── hooks/
│   └── useAdvisor.js
│
├── pages/
│   └── AdvisorPage.jsx
│
└── services/
    └── advisorService.js
```

و مسئولیت‌ها:

```
AdvisorPage
    │
    │ composition
    ↓
useAdvisor
    │
    │ state + business flow
    ↓
advisorService
    │
    │ API communication
    ↓
Django
```

این ساختار برای ادامه خیلی بهتر است.

<aside>
💡

### قدم بعدی: ورود به Backend

</aside>

حالا دیگر Frontend پایه‌ی Advisor آماده است.

مرحله بعدی را می‌توانیم ببریم روی Django:

```
frontend
   │
   │ POST
   ↓
/api/advisor/ask/
   │
   ↓
Django Advisor API
   │
   ↓
response
   │
   ↓
React
```

در Backend هم به‌جای اینکه همه‌چیز را داخل یک View بریزیم، Domain مربوط به Advisor را جدا می‌کنیم:

```
backend/
└── apps/
    └── advisor/
        ├── models.py
        ├── serializers.py
        ├── views.py
        ├── urls.py
        └── ...
```

**فعلاً AI را وصل نمی‌کنیم.** اول یک API واقعی Django می‌سازیم که سؤال React را دریافت کند و یک پاسخ آزمایشی برگرداند. بعد از اینکه `React → Django → React` بدون مشکل کار کرد، لایه AI را روی آن سوار می‌کنیم.

<aside>
📢

# پایان Part-22

</aside>