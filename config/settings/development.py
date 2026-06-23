from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'acron',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '1234',
        'PORT': '3306',
    }
}


