import os

import sys

sys.path.append('/opt/bitnami/projects/backend')

os.environ.setdefault("PYTHON_EGG_CACHE", "/opt/bitnami/projects/backend/egg_cache")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
