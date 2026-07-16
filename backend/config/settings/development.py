# development.py is a settings file for the development environment in a Django project. 
# It contains configuration settings that are specific to the development environment, 
# such as enabling debug mode, configuring the database connection, 
# and other settings that are suitable for local development.
# this is the settings file for the development environment, 
# which is used when running the Django project locally on a developer's machine.

# why import * from base.py?
# The import statement from .base import * is used to import all the settings defined in the
from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# we can use SQLite for development, which is a lightweight database that doesn't require a separate server.
# or we can use MySQL for development, which is a more robust database that requires a separate server.
# or we can use PostgreSQL for development, which is a powerful database that requires a separate server.
# PostgreSQL is a good choice for development,
# because it is a powerful database that requires a separate server.
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


