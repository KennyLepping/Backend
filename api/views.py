from django.http import HttpResponse
import os

def index(request):
    return HttpResponse(os.getenv("SECRET_KEY"))
