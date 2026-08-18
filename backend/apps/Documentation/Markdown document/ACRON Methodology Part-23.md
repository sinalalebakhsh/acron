# ACRON Methodology Part-23

<aside>
📢

در Part-22 ، **فاز 12:**    AI - Advisor تا قدم 21  توسعه یافت

</aside>

# فاز 12: AI - Advisor

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

حالا وارد **Backend Advisor** می‌شویم و اولین ارتباط واقعی بین React و Django را می‌سازیم.

هدف این مرحله فقط این است:

```
React
  │
  │ POST /api/advisor/ask/
  ↓
Django
  │
  │ پردازش سؤال
  ↓
JSON Response
  │
  ↓
React
```

**هنوز AI، OpenAI، Celery و Redis را وارد نمی‌کنیم.** اول API پایه را سالم می‌سازیم.

پیشنهاد من این است که App را داخل `apps` بسازی:

```
python manage.py startapp advisor apps/advisor
```

در نتیجه:

```
backend/
└── apps/
    ├── advisor/
    ├── carts/
    ├── customers/
    ├── orders/
    └── products/
```

**اگر `apps` در پروژه‌ات همان ساختار قبلی است، همین روش دوم را استفاده کن.**

<aside>
💡

## در نظر داشته باشید که APP مورد نظر یعنی advisor قبلا ساخته شده بود و داخل آن تنظیماتی انجام شده بود. بنابراین اگر قبلا نساخته بودید از همین مرحله شروع کنید:

</aside>

### وضعیت واقعی Advisor فعلی

بنابراین،  Backend الان تقریباً این ساختار را دارد:

```
backend/
└── apps/
    └── advisor/
        ├── migrations/
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── serializers.py
        ├── services.py
        ├── tests.py
        ├── urls.py
        └── views.py
```

حتی `serializers.py` هم از قبل به شکل مناسبی طراحی شده:

- `MessageSerializer`
- `ConversationSerializer`
- `AskAdvisorInputSerializer`

وجود دارند و `Conversation` نیز پیام‌ها را به‌صورت Nested نمایش می‌دهد.

همچنین Serializer مخصوص سؤال، فیلد `question` را دریافت می‌کند و حداقل ۳ کاراکتر را الزام می‌کند.

پس **هیچ Serializer جدیدی نمی‌سازیم.**

### معماری واقعی فعلی تو

بنابراین، Backend الان این معماری را دارد:

```
                    React
                      │
                      │
                      ▼
              Advisor API
                      │
                      ▼
             AdvisorViewSet
                      │
                      ▼
          AdvisorAIService
                      │
             ┌────────┴────────┐
             ▼                 ▼
       Conversation          Message
             │                 │
             └────────┬────────┘
                      ▼
                  Database
```

و این بخش خیلی خوب طراحی شده است.

خصوصاً این قسمت:

```
ai_response_message = AdvisorAIService.generate_response(
    conversation_id=conversation.id,
    user_message_content=user_question
)
```

یعنی View مسئول منطق AI نیست.

View فقط:

```
Request
 ↓
Validation
 ↓
Service
 ↓
Response
```

را انجام می‌دهد.

<aside>
💡

### پس Endpoint واقعی تو چیست؟

</aside>

این قسمت خیلی مهم است.

در `urls.py` تو داری:

```
router = DefaultRouter()

router.register(
    r'advisor',
    AdvisorViewSet,
    basename='advisor'
)
```

و داخل ViewSet هم داری:

```
@action(
    detail=True,
    methods=['post'],
    url_path='ask'
)
def ask(...)
```

بنابراین Endpoint تولیدشده توسط DRF این است:

```
POST /api/advisor/{conversation_id}/ask/
```

البته یک نکته وجود دارد:

**مسیر نهایی دقیقاً به نحوه Include کردن `apps.advisor.urls` در `config/urls.py` بستگی دارد.**

پس فعلاً **هیچ URL جدیدی نساز.**

<aside>
💡

### حتی Service هم از قبل آماده است

</aside>

این قسمت در `services.py` بسیار مهم است:

```
@classmethod
def generate_response(
    cls,
    conversation_id: str,
    user_message_content: str
) -> Message:
```

Service تو در حال حاضر این جریان را انجام می‌دهد:

```
Question
   │
   ▼
Conversation.objects.get()
   │
   ▼
Analyze Tone
   │
   ▼
Create User Message
   │
   ▼
Load Chat History
   │
   ▼
Mock LLM
   │
   ▼
Create Assistant Message
   │
   ▼
Update Conversation
   │
   ▼
Return Assistant Message
```

<aside>
💡

### پس الان واقعاً کجای پروژه هستیم؟

</aside>

ما در Frontend این ساختار را داریم:

```
frontend/
└── src/
    └── domains/
        └── advisor/
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

و Backend:

```
backend/
└── apps/
    └── advisor/
        ├── models.py
        ├── serializers.py
        ├── services.py
        ├── views.py
        └── urls.py
```

بنابراین اکنون دقیقاً در این نقطه هستیم:

```
React
  │
  │
  ▼
useAdvisor
  │
  │
  ▼
advisorService.js
  │
  │
  X
  │
  ▼
Django Advisor API
```

**فقط اتصال این دو طرف باقی مانده است.**

<aside>
💡

### قدم بعدی ما: اتصال Frontend به Backend

</aside>

حالا برمی‌گردیم به:

```
frontend/src/domains/advisor/services/advisorService.js
```

در حال حاضر احتمالاً چیزی شبیه Mock داریم:

```
const askAdvisor = async (question) => {
  console.log("Advisor service received:", question);

  return {
    role: "assistant",
    content: "I'm processing your question...",
  };
};

export default {
  askAdvisor,
};
```

این قسمت باید در نهایت تبدیل شود به:

```
advisorService
      │
      │ Axios POST
      ▼
/api/advisor/{conversation_id}/ask/
      │
      ▼
AdvisorViewSet.ask()
      │
      ▼
AdvisorAIService.generate_response()
      │
      ▼
Message
      │
      ▼
JSON
      │
      ▼
React
```

اما یک چیز مهم کم داریم:

## `conversation_id`

چون Backend تو به‌صورت کاملاً درست Endpoint را به یک Conversation خاص وابسته کرده:

```
/api/advisor/{conversation_id}/ask/
```

پس React باید ابتدا یک Conversation ایجاد کند.

---

<aside>
💡

### این یعنی Conversation Flow

</aside>

حالا معماری واقعی ACRON این می‌شود:

```
User opens Advisor
        │
        ▼
Create Conversation
        │
        ▼
Django returns UUID
        │
        ▼
React stores conversationId
        │
        ▼
User asks question
        │
        ▼
POST /api/advisor/{conversationId}/ask/
        │
        ▼
Django
        │
        ▼
AdvisorAIService
        │
        ▼
User Message + Assistant Message
        │
        ▼
React
```

پس Backend فعلی تو از ابتدا برای Conversation و History طراحی شده است.

<aside>
💡

### یک مشکل کوچک در `advisor/urls.py`

</aside>

الان داری:

```
router = DefaultRouter()
router.register(r'advisor', AdvisorViewSet, basename='advisor')
```

و بعد قرار است در `config/urls.py` بنویسیم:

```
path(
    "api/advisor/",
    include("apps.advisor.urls"),
),
```

در این حالت مسیرها دو بار `advisor` خواهند داشت:

```
/api/advisor/advisor/
```

مثلاً Endpoint مربوط به `ask` می‌شود:

```
/api/advisor/advisor/{conversation_id}/ask/
```

این چیزی نیست که ما می‌خواهیم.

ما می‌خواهیم معماری URL این باشد:

```
/api/advisor/
```

و:

```
/api/advisor/{conversation_id}/
```

و:

```
/api/advisor/{conversation_id}/ask/
```

<aside>
💡

### اصلاح `advisor/urls.py`

</aside>

> 22- پس فایل:
> 
> 
> ```
> backend/apps/advisor/urls.py
> ```
> 
> را باز کن.
> 
> **کل محتویات فعلی را با این جایگزین کن:**
> 
> ```python
> from django.urls import include, path
> from rest_framework.routers import DefaultRouter
> 
> from .views import AdvisorViewSet
> 
> router = DefaultRouter()
> 
> router.register(
>     r"",
>     AdvisorViewSet,
>     basename="advisor",
> )
> 
> urlpatterns = [
>     path(
>         "",
>         include(router.urls),
>     ),
> ]
> ```
> 

تفاوت اصلی این خط است:

قبلاً:

```
router.register(
    r"advisor",
    AdvisorViewSet,
    basename="advisor",
)
```

حالا:

```
router.register(
    r"",
    AdvisorViewSet,
    basename="advisor",
)
```

چون خود `config/urls.py` قبلاً `/api/advisor/` را اضافه می‌کند.

---

<aside>
💡

### حالا `config/urls.py` را تغییر بده

</aside>

> 23- در فایل:
> 
> 
> ```
> backend/config/urls.py
> ```
> 
> بعد از Orders این قسمت را اضافه کن:
> 
> ```python
> path(
>     "api/advisor/",
>     include("apps.advisor.urls"),
> ),
> ```
> 
> یعنی این بخش:
> 
> ```python
> path(
>     "api/orders/",
>     include("apps.orders.urls"),
> ),
> 
> path(
>     "api/advisor/",
>     include("apps.advisor.urls"),
> ),
> ```
> 

در نتیجه قسمت Domain APIs تو می‌شود:

```
# -------------------------
# Domain APIs
# -------------------------

path(
    "api/carts/",
    include("apps.carts.urls"),
),

path(
    "api/customers/",
    include("apps.customers.urls"),
),

path(
    "api/products/",
    include("apps.products.urls"),
),

path(
    "api/orders/",
    include("apps.orders.urls"),
),

path(
    "api/advisor/",
    include("apps.advisor.urls"),
),
```

<aside>
💡

### حالا URLهای Advisor چه می‌شوند؟

</aside>

با توجه به `AdvisorViewSet` فعلی تو:

```
class AdvisorViewSet(viewsets.ModelViewSet):
```

و:

```
@action(
    detail=True,
    methods=["post"],
    url_path="ask"
)
def ask(...)
```

بعد از اصلاح بالا، DRF این مسیرها را برایمان ایجاد می‌کند:

### ایجاد Conversation

```
POST /api/advisor/
```

### دریافت Conversation

```
GET /api/advisor/{conversation_id}/
```

### حذف Conversation

```
DELETE /api/advisor/{conversation_id}/
```

### ارسال سؤال

```
POST /api/advisor/{conversation_id}/ask/
```

این دقیقاً همان APIای است که برای معماری فعلی Advisor لازم داریم.

<aside>
💡

### حالا یک نکته بسیار مهم درباره جریان کار

</aside>

با این معماری، React نمی‌تواند از همان ابتدا این کار را بکند:

```
POST /api/advisor/{conversation_id}/ask/
```

چون هنوز `conversation_id` نداریم.

بنابراین جریان واقعی باید این باشد:

```
User opens /advisor
          │
          ▼
React
          │
          │ POST /api/advisor/
          ▼
Django
          │
          ▼
Create Conversation
          │
          ▼
UUID
          │
          ▼
React stores conversationId
```

بعد کاربر سؤال می‌پرسد:

```
User
 │
 │ "I need a laptop"
 ▼
React
 │
 │ POST /api/advisor/{conversationId}/ask/
 ▼
Django
 │
 ▼
AdvisorViewSet.ask()
 │
 ▼
AdvisorAIService.generate_response()
 │
 ├── Save User Message
 │
 ├── Load History
 │
 ├── Generate Mock AI Response
 │
 └── Save Assistant Message
 │
 ▼
MessageSerializer
 │
 ▼
React
```

این **کاملاً با Backend فعلی تو هماهنگ است**.

---

<aside>
💡

### یک نکته مثبت درباره `AllowAny`

</aside>

در `AdvisorViewSet` داری:

```
permission_classes = [AllowAny]
```

پس Advisor فعلاً نیاز به Login ندارد.

این با توضیح خودت در View هم هماهنگ است:

> همه کارفرمایان بتوانند به راحتی با مشاور چت کنند.
> 

بنابراین برای Conversation اولیه:

```
Anonymous User
        ↓
POST /api/advisor/
        ↓
Conversation
```

امکان‌پذیر است.

و `perform_create()` هم در صورت Login بودن User را ذخیره می‌کند و در غیر این صورت `visitor_session_key` را نگه می‌دارد.

پس فعلاً **Permission را دست نمی‌زنیم.**

<aside>
💡

### یک نکته مهم درباره `services.py`

</aside>

فعلی تو از قبل این قابلیت را دارد:

```
conversation = Conversation.objects.get(
    id=conversation_id
)
```

بعد:

```
Message.objects.create(
    conversation=conversation,
    role="user",
    ...
)
```

و سپس:

```
chat_history = Message.objects.filter(
    conversation=conversation
).order_by("created_at")
```

یعنی Backend تو از همین الان **Conversation Memory** دارد.

این خیلی مهم است؛ چون وقتی کاربر می‌گوید:

```
What is ACRON?
```

و بعد:

```
Who created it?
```

هر دو پیام در همان Conversation ذخیره می‌شوند و Service می‌تواند History را ببیند.

پس فعلاً نیازی نیست معماری جدیدی برای Chat History بسازیم.

<aside>
💡

### حالا Backend را تست کنیم

</aside>

قبل از اینکه React را به آن وصل کنیم، Backend را تست کن.

اول Django را اجرا کن:

```
python manage.py runserver
```

بعد مرورگر را باز کن:

```
http://127.0.0.1:8000/api/advisor/
```

چون `GET` روی `ModelViewSet` فعال است، باید Endpoint مربوط به List را ببینی؛ بسته به تنظیمات Renderer ممکن است JSON یا صفحه DRF نمایش داده شود.

اما **مهم‌تر از آن** Swagger را هم داری:

```
http://127.0.0.1:8000/api/docs/
```

در Swagger باید دنبال بخش:

```
Advisor
```

بگردی.

احتمالاً Endpointهایی مشابه این خواهی دید:

```
POST   /api/advisor/
GET    /api/advisor/
GET    /api/advisor/{id}/
DELETE /api/advisor/{id}/
POST   /api/advisor/{id}/ask/
```

<aside>
💡

### اولین تست واقعی

</aside>

در Swagger:

### `POST /api/advisor/`

را باز کن.

Request Body مربوط به `ConversationSerializer` را بررسی کن.

نکته: چون `ConversationSerializer` فیلدهای `user` و `created_at` و `updated_at` را Read Only کرده، نباید آنها را دستی بفرستی. Serializer تو این فیلدها را Read Only تعریف کرده است.

احتمالاً می‌توانی Body خالی بفرستی:

```
{}
```

چون `perform_create()` خودش `user` و `visitor_session_key` را تعیین می‌کند.

اگر موفق باشد باید چیزی شبیه این بگیری:

```
{
    "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "user": null,
    "user_username": null,
    "visitor_session_key": "...",
    "messages": [],
    "created_at": "...",
    "updated_at": "..."
}
```

**آن UUID را نگه دار.**

<aside>
💡

### مرحله بعد: اتصال React به Advisor API

</aside>

معماری نهایی این قسمت:

```
                    AdvisorPage
                         │
                         ▼
                    useAdvisor
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
      createConversation()      askAdvisor()
             │                       │
             ▼                       ▼
      POST /api/advisor/    POST /api/advisor/{id}/ask/
             │                       │
             └───────────┬───────────┘
                         ▼
                   Django Advisor
                         │
                         ▼
                 AdvisorAIService
                         │
                         ▼
                      MySQL
```

<aside>
💡

### اول `advisorService.js`

</aside>

الان `advisorService.js` فقط Mock است:

```
const askAdvisor = async (question) => {
  console.log("Advisor service received:", question);

  return {
    role: "assistant",
    content: "I'm processing your question...",
  };
};

export default {
  askAdvisor,
};
```

این را الان به API واقعی Django وصل می‌کنیم.

<aside>
💡

### مرحله ۱ — `advisorService.js`

</aside>

> 24- فایل:
> 
> 
> ```
> frontend/src/domains/advisor/services/advisorService.js
> ```
> 
> را **کامل با این کد جایگزین کن:**
> 
> ```python
> import apiClient from "../../../services/apiClient";
> 
> const createConversation = async () => {
>   const response = await apiClient.post("/advisor/", {});
> 
>   return response.data;
> };
> 
> const askAdvisor = async (conversationId, question) => {
>   const response = await apiClient.post(
>     `/advisor/${conversationId}/ask/`,
>     {
>       question,
>     }
>   );
> 
>   return response.data;
> };
> 
> export default {
>   createConversation,
>   askAdvisor,
> };
> ```
> 

<aside>
💡

### مرحله ۲ — چرا این کد؟

</aside>

مسیر فایل ما:

```
frontend/
└── src/
    ├── services/
    │   └── apiClient.js
    │
    └── domains/
        └── advisor/
            └── services/
                └── advisorService.js
```

از `advisorService.js` برای رسیدن به `src/services/apiClient.js` باید سه مرحله به عقب برویم:

```
services
   ↑
advisor
   ↑
domains
   ↑
src
```

بنابراین:

```
import apiClient from "../../../services/apiClient";
```

درست است.

<aside>
💡

### مرحله ۳ — `createConversation`

</aside>

این تابع:

```
const createConversation = async () => {
  const response = await apiClient.post("/advisor/", {});

  return response.data;
};
```

در واقع این درخواست را می‌فرستد:

```
POST http://127.0.0.1:8000/api/advisor/
```

چرا `/api` را ننوشته‌ایم؟

چون `apiClient` قبلاً `baseURL` را دارد:

```
http://127.0.0.1:8000/api
```

بنابراین:

```
apiClient.post("/advisor/")
```

تبدیل می‌شود به:

```
http://127.0.0.1:8000/api/advisor/
```

دقیقاً همان چیزی که در Swagger تست کردیم.

<aside>
💡

### مرحله ۴ — `askAdvisor`

</aside>

این تابع:

```
const askAdvisor = async (conversationId, question) => {
  const response = await apiClient.post(
    `/advisor/${conversationId}/ask/`,
    {
      question,
    }
  );

  return response.data;
};
```

مثلاً اگر:

```
conversationId =
  "2b594f77-153a-417d-bfb7-f3bb15aecd00";
```

و:

```
question =
  "این پروژه با چه تکنولوژی‌ای ساخته شده؟";
```

باشد، درخواست نهایی می‌شود:

```
POST /api/advisor/2b594f77-153a-417d-bfb7-f3bb15aecd00/ask/
```

با Body:

```
{
  "question": "این پروژه با چه تکنولوژی‌ای ساخته شده؟"
}
```

دقیقاً همان چیزی که **همین الان با Swagger با موفقیت تست کردی**.

<aside>
💡

### مرحله ۵ — حالا Hook

</aside>

اما هنوز یک مشکل داریم.

قبلاً `askAdvisor` فقط این را می‌گرفت:

```
askAdvisor(question)
```

ولی حالا Backend به این نیاز دارد:

```
askAdvisor(conversationId, question)
```

پس باید `useAdvisor.js` را هم تغییر بدهیم.

باید دقیقاً روی Hook فعلی خود ACRON کار کنیم و ساختار `AdvisorInput`، `AdvisorResponse` و `AdvisorPage` را خراب نکنیم.

---

<aside>
💡

### معماری‌ای که الان داریم به آن می‌رسیم

</aside>

```
┌──────────────────────┐
│    AdvisorPage       │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│     useAdvisor       │
│                      │
│ conversationId       │
│ messages             │
│ loading              │
│ submitQuestion()     │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  advisorService.js   │
│                      │
│ createConversation() │
│ askAdvisor()         │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│     apiClient.js     │
└──────────┬───────────┘
           │
           ▼
       Django API
           │
     ┌─────┴─────┐
     ▼           ▼
/advisor/    /advisor/{id}/ask/
     │           │
     ▼           ▼
Conversation AdvisorAIService
                 │
                 ▼
              Message
```

باید **یک تغییر معماری مهم ولی کنترل‌شده** انجام دهیم: Hook باید ابتدا Conversation بسازد، UUID آن را نگه دارد، و بعد سؤال را به همان Conversation ارسال کند.

فعلاً AI واقعی را دست نمی‌زنیم؛ Backend Mock فعلی کاملاً کافی است.

<aside>
💡

### `useAdvisor.js` را کامل جایگزین کن

</aside>

> 25- فایل:
> 
> 
> ```
> frontend/src/domains/advisor/hooks/useAdvisor.js
> ```
> 
> را با این کد جایگزین کن:
> 
> ```python
> import { useEffect, useState } from "react";
> 
> import advisorService from "../services/advisorService";
> 
> const useAdvisor = () => {
>   const [conversationId, setConversationId] = useState(null);
>   const [messages, setMessages] = useState([]);
>   const [isLoading, setIsLoading] = useState(false);
>   const [isInitializing, setIsInitializing] = useState(true);
> 
>   useEffect(() => {
>     const initializeConversation = async () => {
>       try {
>         const conversation =
>           await advisorService.createConversation();
> 
>         setConversationId(conversation.id);
>       } catch (error) {
>         console.error(
>           "Failed to create advisor conversation:",
>           error
>         );
>       } finally {
>         setIsInitializing(false);
>       }
>     };
> 
>     initializeConversation();
>   }, []);
> 
>   const submitQuestion = async (question) => {
>     if (!conversationId) {
>       console.error(
>         "Cannot submit question: conversation is not ready."
>       );
>       return;
>     }
> 
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
>         await advisorService.askAdvisor(
>           conversationId,
>           question
>         );
> 
>       setMessages((currentMessages) => [
>         ...currentMessages,
>         {
>           id: assistantMessage.id,
>           role: assistantMessage.role,
>           content: assistantMessage.content,
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
>     conversationId,
>     messages,
>     isLoading,
>     isInitializing,
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

### چه چیزی تغییر کرد؟

</aside>

قبلاً Hook این بود:

```
submitQuestion
      ↓
advisorService.askAdvisor(question)
```

اما Backend ما به `conversationId` نیاز دارد.

حالا شده:

```
submitQuestion
      ↓
conversationId
      +
question
      ↓
advisorService.askAdvisor(
    conversationId,
    question
)
```

<aside>
💡

### ایجاد Conversation هنگام باز شدن صفحه

</aside>

این قسمت مهم است:

```
useEffect(() => {
  const initializeConversation = async () => {
    try {
      const conversation =
        await advisorService.createConversation();

      setConversationId(conversation.id);
    } catch (error) {
      console.error(
        "Failed to create advisor conversation:",
        error
      );
    } finally {
      setIsInitializing(false);
    }
  };

  initializeConversation();
}, []);
```

وقتی کاربر وارد:

```
/advisor
```

می‌شود، React یک بار این درخواست را ارسال می‌کند:

```
POST /api/advisor/
```

Django مثلاً برمی‌گرداند:

```
{
  "id": "2b594f77-153a-417d-bfb7-f3bb15aecd00",
  "user": null,
  "visitor_session_key": "127.0.0.1",
  "messages": []
}
```

و React فقط این قسمت را نگه می‌دارد:

```
setConversationId(conversation.id);
```

یعنی:

```
conversationId
      ↓
2b594f77-153a-417d-bfb7-f3bb15aecd00
```

<aside>
💡

### چرا `isInitializing` اضافه کردیم؟

</aside>

ما دو حالت Loading داریم که نباید آنها را با هم قاطی کنیم.

### حالت اول

هنوز Conversation ساخته نشده:

```
isInitializing = true
```

یعنی:

```
React
 ↓
POST /api/advisor/
 ↓
Waiting...
```

### حالت دوم

Conversation وجود دارد و سؤال در حال پردازش است:

```
isLoading = true
```

یعنی:

```
Question
 ↓
POST /api/advisor/{id}/ask/
 ↓
Waiting...
```

بنابراین:

```
isInitializing
    ↓
ساخت Conversation

isLoading
    ↓
پردازش سؤال
```

این تفکیک بعداً برای UX خیلی مهم خواهد بود.

<aside>
💡

### یک تغییر مهم دیگر در Response

</aside>

بنابراین Backend ما این را برمی‌گرداند:

```
{
  "id": "...",
  "role": "assistant",
  "role_display": "دستیار هوش مصنوعی",
  "content": "...",
  "detected_tone": "General (عمومی)",
  "created_at": "..."
}
```

ما فقط چیزهایی را که UI فعلاً لازم دارد وارد `messages` می‌کنیم:

```
{
  id: assistantMessage.id,
  role: assistantMessage.role,
  content: assistantMessage.content,
}
```

پس فعلاً:

```
Backend
├── id
├── role
├── role_display
├── content
├── detected_tone
└── created_at
```

ولی Frontend:

```
Message
├── id
├── role
└── content
```

بعداً می‌توانیم `detected_tone` و `created_at` را هم استفاده کنیم.

<aside>
💡

### یک تغییر کوچک در `AdvisorPage.jsx`

</aside>

الان Hook مقدار جدیدی به نام:

```
isInitializing
```

برمی‌گرداند.

پس فایل:

```
frontend/src/domains/advisor/pages/AdvisorPage.jsx
```

احتمالاً الان چیزی شبیه این دارد:

```jsx
const {
  messages,
  isLoading,
  submitQuestion,
  selectSuggestion,
} = useAdvisor();
```

> 26- آن را تبدیل کن به:
> 
> 
> ```jsx
> const {
>   messages,
>   isLoading,
>   isInitializing,
>   submitQuestion,
>   selectSuggestion,
> } = useAdvisor();
> ```
> 

اما یک نکته: **هنوز لازم نیست UI جدیدی برای `isInitializing` بسازیم.**

فعلاً فقط آن را دریافت می‌کنیم.

<aside>
💡

### حالا تست واقعی

</aside>

حالا هر دو سرور باید روشن باشند:

### Django

```
python manage.py runserver
```

### React

```
npm run dev
```

بعد برو به:

```
http://localhost:5173/advisor
```

<aside>
💡

### مهم‌ترین چیزی که باید در Network ببینی

</aside>

حالا DevTools مرورگر را باز کن:

```
F12
```

بعد:

```
Network
```

و صفحه `/advisor` را Refresh کن.

باید اولین Request مربوط به Advisor را ببینی:

```
POST
/api/advisor/
```

و Response باید:

```
201 Created
```

باشد.

در Response باید یک UUID داشته باشی.

مثلاً:

```
{
  "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
}
```

<aside>
💡

### سپس سؤال بپرس

</aside>

مثلاً:

```
ACRON چیست؟
```

در Network باید Request دوم را ببینی:

```
POST
/api/advisor/{UUID}/ask/
```

مثلاً:

```
POST
/api/advisor/2b594f77-153a-417d-bfb7-f3bb15aecd00/ask/
```

و Request Body:

```
{
  "question": "ACRON چیست؟"
}
```

و Response:

```
200 OK
```

<aside>
💡

### نتیجه نهایی که باید روی صفحه ببینی

</aside>

اگر `AdvisorResponse` فعلی درست کار کند، باید چیزی شبیه این داشته باشی:

```
You
ACRON چیست؟

Advisor
پروژه ACRON یک شاهکار معماری Modular Monolith ...
```

یعنی دیگر این پاسخ Mock فرانت‌اند:

```
I'm processing your question...
```

را نباید ببینی.

پاسخ باید از **Django** آمده باشد.

<aside>
💡

### یک تست بسیار مهم دیگر

</aside>

بعد از سؤال اول، سؤال دوم را بپرس:

```
سینا لاله بخش کیست؟
```

باید Request دوم با همان Conversation ID ارسال شود:

```
/api/advisor/{SAME_CONVERSATION_ID}/ask/
```

یعنی نباید برای هر سؤال Conversation جدید ساخته شود.

ساختار باید این باشد:

```
Conversation A
│
├── User: ACRON چیست؟
│
├── Assistant: ...
│
├── User: سینا لاله بخش کیست؟
│
└── Assistant: ...
```

نه این:

```
Conversation A
└── User: ACRON چیست؟

Conversation B
└── User: سینا لاله بخش کیست؟
```

این موضوع برای Memory سیستم Advisor بسیار مهم است.

<aside>
💡

### فعلاً فقط همین را تست کن

</aside>

بعد از Refresh صفحه `/advisor`، در **Network** باید دو چیز را بتوانیم بررسی کنیم:

**هنگام باز شدن صفحه:**

```
POST /api/advisor/
→ 201
```

**هنگام ارسال سؤال:**

```
POST /api/advisor/{conversationId}/ask/
→ 200
```

اگر این دو Request درست باشند، مرحله بعدی دیگر تست API نیست؛ می‌رویم سراغ **بهبود UX خود Advisor**: نمایش وضعیت `Initializing`, `Thinking`, مدیریت خطا، جلوگیری از ارسال سؤال خالی/دوباره‌فرستادن هنگام Loading، و سپس اتصال History واقعی Conversation به UI.

<aside>
📢

# پایان Part-23

</aside>