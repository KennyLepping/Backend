from django.http import HttpResponse
import os


def index(request):
    return HttpResponse(f"Testing {os.getenv('DJANGO_SETTINGS_MODULE')}")
