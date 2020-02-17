from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('login.urls')),
    path('', include('kategori.urls')),
    path('admin/', admin.site.urls),
]
