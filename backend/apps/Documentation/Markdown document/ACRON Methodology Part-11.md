# ACRON Methodology Part-11

<aside>
📢

در Part-10 ، **فاز 9:  MCP - Model Context Protocol  تا قدم 14 توسعه یافت**

</aside>

# فاز **9:  MCP - Model Context Protocol**

---

## انتقال فایل‌ها (بدون خراب کردن تاریخچه گیت)

اگر صرفاً فایل‌ها را در VS Code بکشی و رها کنی (Drag & Drop)، گیت ممکن است تاریخچه کامیت‌های قبلی فایل‌ها را گم کند و تصور کند همه را حذف کرده‌ای و دوباره ساخته‌ای.

> 1- بهتر است ابتدا یک برانچ جدید بسازی تا خیالت راحت باشد:
> 
> 
> ```python
> git checkout -b feature/decouple-architecture
> ```
> 

> 2- سپس یک پوشه به نام `backend` در ریشه اصلی بسازی و فایل‌های مربوط به جنگو را با دستور گیت به داخل آن منتقل کنی تا تاریخچه (History) آن‌ها حفظ شود:
> 
> 
> ```python
> mkdir backend
> # انتقال فایل‌ها و پوشه‌های اصلی به پوشه backend
> git mv apps config core manage.py requirements.txt backend/
> git mv products backend/
> git mv categories backend/
> git mv brands backend/
> git mv exporter.py acron_codebase.md backend/
> git mv Pipfile Pipfile.lock backend/
> ```
> 

> 3- *(اگر فایل‌های دیگری مثل `.gitignore` یا `Pipfile` در ریشه داری، آن‌ها را هم به داخل `backend` ببر).*
> 

از آنجایی که فایل تنظیمات تست خودکار تو در مسیر `.github/workflows/django.yml` قرار دارد، گیت‌هاب دیگر نمی‌تواند دستورات تست را مستقیماً در ریشه پروژه اجرا کند، چون فایل `manage.py` به پوشه `backend` منتقل شده است.

> 4- به‌روزرسانی آدرس‌ها در CI/CD (بسیار مهم!) 
باید فایل ورک‌فلو خود را باز کنی و به مراحلی که دستورات پایتون را اجرا می‌کنند، مقدار `working-directory` را اضافه کنی:
> 
> 
> ```python
> defaults:
>   run:
>     working-directory: backend
> ```
> 

برای اینکه گیت‌هاب متوجه شود کدهای بک‌اند شما به پوشه `backend` منتقل شده‌اند و باید تمام دستورات را داخل این پوشه اجرا کند، باید **دو تغییر کوچک اما بسیار مهم** در این فایل اعمال کنی:

1. **تعریف پوشه پیش‌فرض (defaults):** دقیقاً زیر خط `runs-on: ubuntu-latest` باید بلاک `defaults` را اضافه کنی تا گیت‌هاب بداند تمام دستوراتی که در بخش `run` می‌نویسی (مثل نصب پکیج‌ها و اجرای تست‌ها) باید در مسیر `backend/` اجرا شوند.
2. **آدرس‌دهی دقیق کش پایتون (cache-dependency-path):** در بخش `setup-python` باید مشخص کنی که فایل `requirements.txt` حالا درون پوشه `backend` قرار دارد تا سیستم کش گیت‌هاب بدون مشکل کار کند.

> 5- فایل نهایی و اصلاح‌شده تو به شکل زیر خواهد بود. می‌توانی کل این کد را جایگزین فایل فعلی `django.yml` کنی:
> 
> 
> ```python
> name: Django CI
> 
> on:
>   push:
>     branches: [ "main" ]
>   pull_request:
>     branches: [ "main" ]
> 
> jobs:
>   build:
>     runs-on: ubuntu-latest
> 
>     # ۱. مشخص کردن پوشه پیش‌فرض برای اجرای تمام دستورات این جاب (جابجایی به پوشه backend)
>     defaults:
>       run:
>         working-directory: backend
> 
>     # ۲. راه‌اندازی دیتابیس موقت MySQL روی سرور گیت‌هاب
>     services:
>       mysql:
>         image: mysql:8.0
>         env:
>           MYSQL_ROOT_PASSWORD: '1234' # دقیقاً مطابق پسورد شما در development.py
>           MYSQL_DATABASE: 'acron'      # دقیقاً مطابق نام دیتابیس شما
>         ports:
>           - 3306:3306
>         options: --health-cmd="mysqladmin ping" --health-interval=10s --health-timeout=5s --health-retries=3
> 
>     strategy:
>       matrix:
>         # ۳. هماهنگی با requirements: جنگو ۶ حداقل به پایتون ۳.۱۲ نیاز دارد
>         python-version: ["3.12", "3.13"]
> 
>     steps:
>     - uses: actions/checkout@v5
> 
>     - name: Set up Python ${{ matrix.python-version }}
>       uses: actions/setup-python@v5
>       with:
>         python-version: ${{ matrix.python-version }}
>         cache: 'pip'
>         # مشخص کردن مسیر دقیق فایل ریکوایرمنتس برای کش گیت‌هاب
>         cache-dependency-path: backend/requirements.txt 
> 
>     # ۴. نصب ابزارهای لینوکسی مورد نیاز برای کامپایل کتابخانه mysqlclient
>     - name: Install Linux Dependencies for MySQL
>       run: |
>         sudo apt-get update
>         sudo apt-get install -y default-libmysqlclient-dev pkg-config build-essential
> 
>     - name: Install Python Dependencies
>       run: |
>         python -m pip install --upgrade pip
>         pip install -r requirements.txt
> 
>     # ۵. اجرای تست‌ها با معرفی آدرس فایل تنظیمات
>     - name: Run Tests
>       env:
>         DJANGO_SETTINGS_MODULE: config.settings.development
>       run: |
>         python manage.py test
> ```
> 

### تغییرات اعمال شده دقیقاً کجاست؟

- **خطوط ۱۲ تا ۱۵:** بلاک `defaults` اضافه شد که مسیر پیش‌فرضِ اجرای فرآیندها را روی پوشه `backend` تنظیم می‌کند.
- **خط ۳۷:** آرگومان `cache-dependency-path: backend/requirements.txt` اضافه شد تا فرآیند کش کردن پکیج‌های پایتون به دلیل جابجایی فایل `requirements.txt` به داخل پوشه جدید، دچار اختلال و ارور نشود.

مدیریت محیط مجازی (Virtual Environment)

> 6- یادت باشد از این به بعد وقتی ترمینال VS Code را باز می‌کنی، در ریشه اصلی پروژه قرار داری. برای اجرای دستورات جنگو یا استفاده از محیط مجازی (مثلاً با `pipenv`)، باید ابتدا وارد پوشه `backend` شوی:
> 
> 
> ```python
> cd backend
> pipenv shell
> python manage.py runserver
> ```
> 

تنظیم پروتکل CORS (تنها پروتکل نرم‌افزاری مورد نیاز)
وقتی فرانت‌اند را مستقل کنی، احتمالاً روی یک پورت دیگر (مثلاً `localhost:3000` با ری‌اکت یا نکست‌جی‌اس) اجرا می‌شود، در حالی که بک‌اند روی پورت `localhost:8000` بالا می‌آید. مرورگرها به دلیل امنیت، اجازه نمی‌دهند فرانت‌اند به دامنه دیگری درخواست بفرستد، مگر اینکه در بک‌اند مجوز داده باشی.

> 6- برای حل این مسئله، پکیج `django-cors-headers` را روی بک‌اند نصب کن:
> 
> 
> ```python
> pipenv install django-cors-headers
> ```
> 

> 7- سپس در تنظیمات `base.py` موارد زیر را پیکربندی کن:
> 
> 
> ```python
> # settings/base.py
> 
> INSTALLED_APPS = [
>     # ...
>     "corsheaders",
>     # ...
> ]
> 
> MIDDLEWARE = [
>     "corsheaders.middleware.CorsMiddleware", # این خط باید بالاتر از CommonMiddleware باشد
>     "django.middleware.common.CommonMiddleware",
>     # ...
> ]
> 
> # در محیط دولوپمنت می‌توانید این را فعال کنید:
> CORS_ALLOW_ALL_ORIGINS = True 
> 
> # یا برای امنیت بیشتر، دامنه‌های مجاز فرانت‌اند را مشخص کنید:
> # CORS_ALLOWED_ORIGINS = [
> #     "http://localhost:3000",
> # ]
> ```
> 

<aside>
📢

## با پیش‌بردن این چند مرحله، پروژه به زیباترین شکل ممکن به دو بخش مجزا تقسیم می‌شود؛ بک‌اند کاملاً بی‌خبر از فرانت‌اند کارش را می‌کند و فرانت‌اند هم به عنوان مصرف‌کننده APIها به پروژه اضافه خواهد شد.

</aside>

### راهکار استاندارد و حرفه‌ای (بدون خراب کردن main):

به جای مرج کردن کورکورانه، این مراحل را برو:

#### ۱. کدهایت را روی شاخه فعلی کامیت و پوش کن

مطمئن شو آخرین تغییراتت (از جمله پوشه‌بندی جدید و فایل `django.yml` اصلاح‌شده) روی شاخه جدیدت کامیت شده‌اند. سپس آن را به گیت‌هاب بفرست:

```python
git add .
git commit -m "chore: decouple project structure into backend and frontend"
git push origin feature/decouple-architecture
```

*(به جای `feature/decouple-architecture` اسم شاخه خودت را بنویس).*

#### در گیت‌هاب یک Pull Request (PR) باز کن

وارد مخزن (Repository) خود در سایت گیت‌هاب شو. گیت‌هاب خودش یک کادر زرد رنگ به تو نشان می‌دهد که می‌گوید شاخه جدیدی پوش شده است. روی دکمه **Compare & pull request** کلیک کن.

- مسیر ادغام را از شاخه خودت به سمت `main` تنظیم کن.
- روی **Create pull request** کلیک کن.

#### ۳. تماشای اجرای تست‌ها قبل از مرج!

به محض اینکه Pull Request را بسازی، بدون اینکه کدی وارد `main` شده باشد، گیت‌هاب شروع به اجرای تست‌ها روی کدها و ساختار جدید می‌کند.

- در پایین صفحه Pull Request، بخش تست‌ها را می‌بینی که در حال اجرا هستند (یک دایره زرد رنگ در حال چرخش).

#### ۴. اگر تست‌ها با موفقیت پاس شدند (تیک سبز):

با خیال راحت روی دکمه **Merge pull request** کلیک کن تا تغییرات وارد `main` شوند.

#### ۵. اگر تست‌ها شکست خوردند (ضربدر قرمز):

نیازی به بازگرداندن (Revert) کامیت‌ها یا بستن PR نیست!

- در همان محیط VS Code خودت، ارورها را برطرف کن.
- تغییرات جدید را روی همان شاخه کامیت و دوباره `git push` کن.
- گیت‌هاب به صورت خودکار متوجه کدهای جدید روی PR می‌شود و دوباره تست‌ها را اجرا می‌کند تا زمانی که تیک سبز را بگیری.

### دستورالعمل صحیح و گام‌به‌گام برای همگام‌سازی لپ‌تاپ:

وقتی مرج در گیت‌هاب با موفقیت انجام شد، ترمینال خود را باز کن و این مراحل را به ترتیب برو:

> 8- رفتن به شاخه اصلی محلی:
> 
> 
> ```python
> git checkout main
> ```
> 
> *(یا اگر از دستورات جدیدتر استفاده می‌کنی: `git switch main`)*
> 

> 9- دریافت آخرین کدهای مرج‌شده از گیت‌هاب (دستور اصلاح‌شده شما):
> 
> 
> ```python
> git pull origin main
> ```
> 

با این دستور، تمام پوشه‌بندی‌های جدید بک‌اند و فرانت‌اند و فایل تنظیمات اصلاح‌شده CI/CD (`django.yml`) به لپ‌تاپ شما منتقل می‌شوند و سیستم محلی شما دقیقاً شبیه به گیت‌هاب می‌شود.

تمیزکاری و حذف شاخه‌ی قدیمی (اختیاری اما بسیار توصیه شده):

> 10- حالا که کدهای شاخه فرعی شما (مثلاً `feature/decouple-architecture`) وارد `main` شده و روی لپ‌تاپ هم قرار گرفته است، دیگر نیازی به آن شاخه فرعی روی لپ‌تاپ نداری. برای شلوغ نشدن گیت، آن را حذف کن:
> 
> 
> ```python
> git branch -d feature/decouple-architecture
> ```
> 
> ```python
> hint: If you are sure you want to delete it, run 'git branch -D feature/decouple-architecture'
> ```
> 
> *(به جای اسم بالا، نام شاخه‌ای که ساخته بودی را بنویس).*
> 

برای حذف کردن این شاخه روی گیت‌هاب (Remote) دو راه داری:

#### ۱. حذف از طریق سایت گیت‌هاب (ساده‌ترین راه):

وقتی Pull Request تو با موفقیت مرج (Merge) شد، گیت‌هاب در همان صفحه و در کنار پیغام موفقیت‌آمیز بودن مرج، یک دکمه بنفش‌رنگ به نام **Delete branch** به تو نشان می‌دهد. با کلیک روی آن دکمه، شاخه مستقیماً روی سرور گیت‌هاب پاک می‌شود.

#### ۲. حذف از طریق ترمینال لپ‌تاپ:

اگر دوست داری همه کارها را با کد پیش ببری، بعد از حذف شاخه روی لپ‌تاپ، این دستور را در ترمینال بنویس تا دستور حذف به گیت‌هاب فرستاده شود:

```python
git push origin --delete feature/decouple-architecture
```

<aside>
📢

# پایان Part-11

</aside>