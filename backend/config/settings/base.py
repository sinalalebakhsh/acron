# This file is part of the Django settings for the project. 
# It contains base configurations that are common across different environments 
# (like development, testing, and production).

# why import os and sys?
# The os module is used for interacting with the operating system,
import os

# why import sys?
# The sys module provides access to some variables used or maintained by the interpreter
from pathlib import Path

# why import sys?
# The sys module provides access to some variables used or maintained by the interpreter
import sys


# why import timedelta?
# The timedelta class is used to represent a duration,
from datetime import timedelta


# Build paths inside the project like this: BASE_DIR / 'subdir'.
#  BASE_DIR is defined as the parent directory of the current file's parent directory.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# The SECRET_KEY is a critical setting in Django that is used for cryptographic signing.
# It should be kept secret in production environments to ensure the security of the application.
SECRET_KEY = 'django-insecure-1r%tnk@im4n@uk5zx!q*i@wkr69darorwnglm%sa!_1ou=8#_w'

# Security warning: don't run with debug turned on in production!
# The DEBUG setting controls whether Django will display detailed error pages.
# It should be set to False in production to avoid exposing sensitive information.
ALLOWED_HOSTS = []



# Application definition
# The INSTALLED_APPS setting defines the list of applications that are enabled in this Django project.
# It includes both built-in Django apps and custom apps created for the project.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    # Third party
    # The third-party apps listed here are additional packages 
    # that provide extra functionality to the Django project.
    'rest_framework',
    'drf_spectacular', # مستندسازی API


    # CREATE by me
    # The custom apps listed here are specific to this project 
    # and contain the business logic and models for different parts of the application.
    'apps.accounts',
    'apps.api',
    'apps.carts',
    'apps.customers',
    # 'apps.notifications',
    'apps.orders',
    'apps.payments',
    'apps.products',
    # 'apps.reviews',
    'apps.shipments',
    'apps.ai',
    'apps.advisor', # اضافه کردن اپلیکیشن جدید مشاور هوشمند
]

# The MIDDLEWARE setting defines a list of middleware classes ,
# that are used to process requests and responses in the Django application.
# Middleware is a way to process requests globally, 
# before they reach the view or after the view has processed them.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# The ROOT_URLCONF setting specifies the Python module,
# that contains the URL configuration for the project.
# It tells Django which module to use for resolving URLs to views.
ROOT_URLCONF = 'config.urls'
TESTING = "test" in sys.argv or "PYTEST_VERSION" in os.environ

# The TEMPLATES setting defines the configuration for the template engine used in the project.
# It specifies the backend engine, directories for template files,
# and context processors that provide additional data to templates.
# for contuct between the debug_toolbar and the templates, 
# we can use context processors to pass data from the backend to the frontend templates.
if not TESTING:
    INSTALLED_APPS = [
        *INSTALLED_APPS,
        "debug_toolbar",
    ]
    MIDDLEWARE = [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
        *MIDDLEWARE,
    ]
    INTERNAL_IPS = [
        "127.0.0.1",
    ]


# The WSGI_APPLICATION setting specifies the Python path to the WSGI application callable,
# that Django's built-in servers (and some third-party servers) use to communicate with the application.
# It is used to deploy the Django application on a web server that supports the WSGI interface.
WSGI_APPLICATION = 'config.wsgi.application'

# The TEMPLATES setting defines the configuration for the template engine used in the project.
# It specifies the backend engine, directories for template files,
# and context processors that provide additional data to templates.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]



# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators
# why use password validators?
# Password validators are used to enforce certain rules and requirements for user passwords.
# and they help improve the security of user accounts, 
# by ensuring that passwords are strong and not easily guessable.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# what is i18n? 
# i18n stands for internationalization, 
# which is the process of designing and developing software applications
# that can be adapted to different languages and 
# regions without requiring changes to the source code.
# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# why use static files?
# Static files are files that are served directly to the client,
# without any processing or modification by the
# server. They are typically used for assets like images, 
# CSS files, JavaScript files, and other resources
# that do not change frequently and 
# can be cached by the client's browser for improved performance.
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = 'static/'


# why use media files?
# Media files are user-uploaded files that are stored on the server and,
# can be accessed by users through the application.
# They are typically used for content that is generated or uploaded by users,

AUTH_USER_MODEL = "accounts.CustomUser"

#  why use REST_FRAMEWORK settings?
# The REST_FRAMEWORK setting is used to configure the behavior of the Django REST Framework (DRF),
# which is a powerful and flexible toolkit for building Web APIs in Django.
# And it allows you to customize various aspects of the API,
# such as authentication, permissions, pagination, and more.
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
     # تنظیمات قبلی شما (مثل Authentication و Pagination) اینجا می‌مانند...


    
    # اضافه کردن کلاس تولیدکننده مستندات
    # The 'DEFAULT_SCHEMA_CLASS' setting specifies the class,
    # that will be used to generate the API schema for your project.
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# why use SIMPLE_JWT settings?
# The SIMPLE_JWT setting is used to configure the behavior of the Simple JWT package,
# which is a third-party package for handling,
# JSON Web Tokens (JWT) authentication in Django REST Framework.
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}



# تنظیمات اختصاصی Swagger
# why use SPECTACULAR_SETTINGS?
# The SPECTACULAR_SETTINGS setting is used to configure the behavior of the drf-spectacular package,
# which is a third-party package for generating OpenAPI 3.0 documentation for Django REST Framework APIs.
SPECTACULAR_SETTINGS = {
    'TITLE': 'ACRON Project API with Swagger',
    'DESCRIPTION': 'مستندات جامع APIهای فروشگاه ACRON شامل بخش مشتریان و محصولات',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False, # برای تمیز ماندن خروجی نهایی
    
    # تنظیمات امنیتی برای تست 
    # API
    # ها داخل خود مرورگر
    'SECURITY': [
        {'jwtAuth': []}
    ],
    'SECURITY_DEFINITIONS': {
        'jwtAuth': {
            'type': 'http',
            'scheme': 'bearer',
            'bearerFormat': 'JWT',
        }
    }
}




