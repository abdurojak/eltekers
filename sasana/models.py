from django.db import models

class Sasana(models.Model):
    id_sasana = models.AutoField(primary_key=True)
    nama_sasana = models.CharField(max_length=255)
    sejak = models.IntegerField()
    alamat_sasana = models.TextField()
    kelurahan = models.CharField(max_length=100)
    kecamatan = models.CharField(max_length=100)
    kota_kabupaten = models.CharField(max_length=100)
    provinsi = models.CharField(max_length=100)
    # lattitude = models.DecimalField(max_digits=9, decimal_places=6)
    # longitude = models.DecimalField(max_digits=9, decimal_places=6)
    jumlah_instruktur = models.IntegerField()
    jumlah_peserta = models.IntegerField()
    peserta_aktif = models.IntegerField()
    jumlah_latihan_per_minggu = models.IntegerField()
    link_gmap = models.URLField()
    profile = models.ImageField(upload_to='profile_sasana/')

    def __str__(self):
        return self.nama_sasana
