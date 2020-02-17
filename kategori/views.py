from django.shortcuts import render
from django.http import HttpResponseRedirect
from login import views as v
from .forms import KategoriForm, ProdukForm
from . import models

def listcontext():
    data = [
                ['/menu/kategori', 'Kategori'],
                ['/menu/produk', 'Produk'],
                ['/menu/laporan', 'Laporan'],
                ['/', 'Sign Out'],
            ]
    return data

def create_dataKategori(request):
    if request.method == 'POST':
        models.kategori.objects.create(
            kategori = request.POST.get('Kategori'),
        )

def create_dataProduk(request):
    if request.method == 'POST':
        models.produk.objects.create(
            produk = request.POST.get('produk'),
            harga = request.POST.get('harga'),
            kategori = request.POST.get('kategori'),
            deskripsi = request.POST.get('deskripsi'),
        )

def kategori(request):
    if v.log:
        form = KategoriForm(request.POST or None)

        if form.is_valid():
            create_dataKategori(request)

        context = {
            'selected' : 'Kategori',
            'list' : listcontext(),
            'form': form
        }
        return render(request, 'kategori/menu.html', context)
    else:
        return HttpResponseRedirect('/')

def produk(request):
    if v.log:
        data = models.kategori.objects.all()
        form = ProdukForm(request.POST or None)

        if form.is_valid:
            create_dataProduk(request)

        context = {
            'selected' : 'Produk',
            'list' : listcontext(),
            'form' : form,
            'data' : data,
        }
        return render(request, 'kategori/menu.html', context)
    else:
        return HttpResponseRedirect('/')


def laporan(request):
    if v.log:
        data = models.produk.objects.all()

        context = {
            'selected' : 'Laporan',
            'list' : listcontext(),
            'data' : data
        }
        return render(request, 'kategori/laporan.html', context)
    else:
        return HttpResponseRedirect('/')