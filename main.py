from django.db import models
from django.urls import path
# Create your models here.


class barang(models.Model):

    nama = models.CharField(max_length=255, default='')

    berat = models.CharField(max_length=255, default='')
    harga = models.CharField(max_length=255, default='')
    warna = models.CharField(max_length=255, default='')

Barang.objects.all()
Barang.objects.filter(nama="Baju Koko")

def barang_html(req):
    contoh(nama='barang')
    return render(request=req, template_name='list_barang.html')

urlpatterns = [
    path ('list_barang',barang_html,name='barang')
]

def barang_html(req):
    barangs = barang.objects.all()
    return render (request=request,template_name='barangs/list.html',context={'list':barangs})