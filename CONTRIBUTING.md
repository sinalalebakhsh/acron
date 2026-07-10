
# Contributing to the ACRON

Thank you very much for your interest in contributing to the development of ACRON! Your presence will greatly help the growth and improvement of this architecture.
از اینکه قصد دارید در توسعه ACRON مشارکت کنید، بسیار سپاسگزاریم! حضور شما به رشد و بهبود این معماری کمک بزرگی می‌کند. 

To make the participation process transparent and enjoyable for everyone, please read the following guide before you begin.
برای اینکه فرآیند مشارکت برای همه شفاف و لذت‌بخش باشد، لطفاً پیش از شروع، راهنمای زیر را مطالعه کنید.

## 🐛 ثبت باگ (Bug Reports)
اگر در پروژه به خطایی برخورد کردید، لطفاً پیش از ایجاد یک Issue جدید، بخش Issueها را بررسی کنید تا مطمئن شوید قبلاً ثبت نشده باشد. 
برای ثبت باگ جدید، موارد زیر را در توضیحات خود ذکر کنید:
*   نسخه پایتون و جنگویی که استفاده می‌کنید.
    The version of Python and Django you are using.
* مراحل دقیق بازتولید (Reproduce) خطا.
* رفتار مورد انتظار و رفتاری که در حال حاضر رخ می‌دهد.

## 💡 پیشنهاد ویژگی‌های جدید (Feature Requests)
ما همیشه از ایده‌های جدید استقبال می‌کنیم! برای پیشنهاد یک ویژگی:<br>
۱. یک Issue جدید با برچسب `enhancement` ایجاد کنید.<br>
۲. به طور واضح توضیح دهید که این ویژگی چه مشکلی را حل می‌کند یا چه ارزش افزوده‌ای برای ACRON دارد.<br>

## 💻 راه‌اندازی محیط توسعه (Development Setup)

برای اجرای پروژه روی سیستم خود و شروع توسعه، مراحل زیر را طی کنید:<br>

1. **Fork Or Clone:** 

```bash
git clone [https://github.com/sinalalebakhsh/acron.git](https://github.com/sinalalebakhsh/acron.git)

cd acron

pipenv shell

```
📏 استانداردهای کدنویسی

برای حفظ یکپارچگی کدها، لطفاً به موارد زیر دقت کنید:

* کدهای پایتون باید از استانداردهای PEP 8 پیروی کنند.
* نام‌گذاری متغیرها، توابع و کلاس‌ها باید معنادار و خوانا باشد.
* در صورت اضافه کردن یک ویژگی جدید یا تغییر منطق APIها، لطفاً داکیومنت‌ها (Docstrings) را نیز به‌روزرسانی کنید.

