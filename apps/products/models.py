import cv2

from django.db import models
from django.core.exceptions import ValidationError



# ۱. ساخت ولیدیتور سفارشی برای فایل‌های فرعی (حجم و زمان ویدیو)
def validate_media_file(file):
    # الف) بررسی حجم فایل (400 مگابایت به بایت)
    max_size_mb = 400
    max_size_bytes = max_size_mb * 1024 * 1024
    if file.size > max_size_bytes:
        raise ValidationError(f"حجم فایل نمی‌تواند بیشتر از {max_size_mb} مگابایت باشد.")

    # ب) بررسی مدت زمان ویدیو (اگر فایل ویدیو بود)
    file_name = file.name.lower()
    if file_name.endswith(('.mp4', '.mkv', '.avi', '.mov')):
        # باز کردن موقت فایل ویدیو با OpenCV برای خواندن فریم‌ها
        video = cv2.VideoCapture(file.temporary_file_path())
        
        # به دست آوردن تعداد کل فریم‌ها و نرخ فریم (FPS)
        frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
        fps = video.get(cv2.CAP_PROP_FPS)
        
        # محاسبه زمان به ثانیه (اگر fps صفر نباشد)
        if fps > 0:
            duration_seconds = frames / fps
            if duration_seconds > 120: # 2 دقیقه = 120 ثانیه
                raise ValidationError("مدت زمان ویدیو نمی‌تواند بیشتر از ۲ دقیقه باشد.")
        video.release()



class Category(models.Model):
    # دسته‌بندی والد (برای ساختار درختی)
    parent = models.ForeignKey(
        'self', 
        on_delete=models.PROTECT, 
        null=True, 
        blank=True, 
        related_name='children'
    )
    
    name = models.CharField(max_length=255)
    
    # اسلاگ برای 
    # URL
    # های سئو-محور
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
    
    description = models.TextField(blank=True)
    
    # تصویر دسته‌بندی
    image = models.ImageField(upload_to='categories/%Y/%m/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
    image = models.ImageField(upload_to='brands/%Y/%m/', blank=True, null=True)

    def __str__(self):
        return self.name


      
        
