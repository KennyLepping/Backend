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

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'  # Original working S3 bucket: S3_BUCKET_NAME="zappa-a0rwj2q61"
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

MEDIA_ROOT = BASE_DIR / 'media'  # Usually where MEDIA_ROOT is
# STATIC_URL = '/static/'
