from django.http import HttpResponse
from django.conf import settings

def index(request):
    return HttpResponse(f"Testing {settings.DJANGO_SETTINGS_MODULE}")
