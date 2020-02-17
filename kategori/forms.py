from django import forms
from . import models

class KategoriForm(forms.Form):

    def atribute_form():
        style = 'text-align: center; border-radius: 100px'
        return style

    Kategori = forms.CharField(widget=forms.TextInput(
        attrs={
            'style': atribute_form()
        }), max_length=50)
    
class ProdukForm(forms.Form):
    def atribute_form():
        style = 'text-align: center; border-radius: 100px'
        return style
    data = models.kategori.objects.all()
    listdata = []

    for d in data:
        listdata.append((d.kategori, d.kategori))

    produk = forms.CharField(widget=forms.TextInput(attrs={'style': atribute_form()}), max_length=50)
    harga = forms.CharField(widget=forms.NumberInput(attrs={'style': atribute_form()}), max_length=50)
    deskripsi = forms.CharField(widget=forms.Textarea(attrs={'style': 'border-radius: 15px'}), max_length=255)
    

