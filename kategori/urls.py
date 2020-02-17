from django.urls import path
from . import views as v

urlpatterns = [
    path('menu/kategori/', v.kategori),
    path('menu/produk/', v.produk),
    path('menu/laporan/', v.laporan),
]
