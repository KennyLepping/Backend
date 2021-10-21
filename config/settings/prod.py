from .base import *

DEBUG = True

ALLOWED_HOSTS = ["kennyleppingapi.com"]

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True # Try redirect if domain is added
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_PRELOAD = True

# STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'  # Original working S3 bucket: S3_BUCKET_NAME="zappa-a0rwj2q61"

# if you hosted your static files on a custom domain
#AWS_S3_PUBLIC_URL_STATIC = "https://static.yourdomain.com/"

# Do I show up here?
