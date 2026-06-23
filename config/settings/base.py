from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent.parent.parent

AUTH_USER_MODEL = "accounts.CustomUser"

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


