"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.utils import datastructures
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, JsonResponse, FileResponse
from django.shortcuts import render
from django.conf import settings

def home(request):
    return HttpResponse('Hello from home.')

def info(request):
    data = {}
    print('request.META')
    for k,v in request.META.items():
        data[str(k)] = str(v)
        print(k,'=', v)
    return JsonResponse(data)

def shopping(request):
    return render(request, 'shopping.html')

def lucksoot_pdf(request):
    file_path = settings.BASE_DIR / 'lucksoot.pdf'
    return FileResponse(
        open(file_path, 'rb'), 
        content_type='application/pdf', 
        filename='lucksoot.pdf')

urlpatterns = [
    path('', home),
    path('info/', info),
    path('shopping/', shopping),
    path('lucksoot/', lucksoot_pdf),
    path('admin/', admin.site.urls),
]

