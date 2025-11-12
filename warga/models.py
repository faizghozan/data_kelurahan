from django.db import models

class Warga(models.Model):
    nik = models.CharField(max_length=16, unique=True, verbose_name="Nomor Induk Kependudukan")
    nama_lengkap = models.CharField(max_length=100, verbose_name="Nama Lengkap")
    alamat = models.TextField(verbose_name="Alamat Tinggal")
    no_telepon = models.CharField(max_length=15, blank=True, verbose_name="Nomor Telepon")
    tanggal_input = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama_lengkap


class Pengaduan(models.Model):
    STATUS_CHOICES = [
        ('BARU', 'Baru'),
        ('DIPROSES', 'Diproses'),
        ('SELESAI', 'Selesai'),
    ]

    judul = models.CharField(max_length=200, verbose_name="Judul Pengaduan")
    deskripsi = models.TextField(verbose_name="Deskripsi Pengaduan")
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='BARU',
        verbose_name="Status Pengaduan"
    )
    tanggal_lapor = models.DateTimeField(auto_now_add=True, verbose_name="Tanggal Lapor")

    # Relasi ke model Warga
    pelapor = models.ForeignKey(
        Warga,
        on_delete=models.CASCADE,
        related_name='pengaduan_list',
        verbose_name="Pelapor"
    )

    def __str__(self):
        return self.judul
