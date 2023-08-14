from django.db import models

class Dpd(models.Model):
    nama = models.CharField(max_length=30, unique=True)
    alamat = models.TextField()
    contact = models.TextField()
    email = models.TextField()
    gmaps = models.TextField(null=True, blank=True, default='')

    def __str__(self):
        return self.nama

class Dpp(models.Model):
    nama = models.CharField(max_length=30, unique=True)
    jabatan = models.CharField(max_length=30)
    alamat = models.TextField()
    deskripsi = models.TextField()
    foto = models.TextField(null=True, blank=True, default='')

    def __str__(self):
        return self.nama