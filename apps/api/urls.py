from django.http import HttpResponse
from django.urls import path


def api_home(request):
    return HttpResponse("API Root")


urlpatterns = [
    path('', api_home),
]