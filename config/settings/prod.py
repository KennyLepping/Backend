from .base import *
from os import getenv

DEBUG = True

ALLOWED_HOSTS = ["kennyleppingapi.com", "www.kennyleppingapi.com", "52.71.160.175"]

SECRET_KEY = getenv('SECRET_KEY')
print(getenv('SECRET_KEY'))

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True # Try redirect if domain is added
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_PRELOAD = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': getenv("DB_NAME"),
        'USER': getenv("DB_USER"),
        'PASSWORD': getenv("DB_PASSWORD"),
        'HOST': getenv("DB_HOST"),
        'PORT': '5432',
    }
}

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'  # Original working S3 bucket: S3_BUCKET_NAME="zappa-a0rwj2q61"
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

MEDIA_ROOT = BASE_DIR / 'media' # Usually where MEDIA_ROOT is

# if you hosted your static files on a custom domain
#AWS_S3_PUBLIC_URL_STATIC = "https://static.yourdomain.com/"
