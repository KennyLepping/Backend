from .base import *
from decouple import config

DEBUG = True

SECRET_KEY = 'jlkjfd8vjdb833h'

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config("DB_NAME"),
        'USER': config("DB_USER"),
        'PASSWORD': config("DB_PASSWORD"),
        'HOST': config("DB_HOST"),
        'PORT': '5432',
    }
}


# STATIC_URL = '/static/'
