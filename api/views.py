from django.http import HttpResponse
import os

# Create your views here.
def index(request):
    return HttpResponse(os.getenv("SECRET_KEY"))
