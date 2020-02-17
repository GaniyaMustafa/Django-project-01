from django.db import models

class kategori(models.Model):
    kategori = models.CharField(max_length=50)

    def __str__(self):
        return "{}. {}".format(self.id, self.kategori)

class produk(models.Model):
    produk = models.CharField(max_length=50)
    harga = models.CharField(max_length=50)
    kategori = models.CharField(max_length=50)
    deskripsi = models.TextField(max_length=255)
    
    def __str__(self):
        return "{}. {}".format(self.id, self.produk)
