from django.db import models

# Create your models here.
class TPQ(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.nama

class Guru(models.Model):
    tpq = models.ForeignKey(TPQ, related_name='teachers', on_delete=models.CASCADE)
    nama = models.CharField(max_length=50)
    nomor_hp = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nama}"

class Murid(models.Model):
    tpq = models.ForeignKey(TPQ, related_name='students', on_delete=models.CASCADE)
    nama = models.CharField(max_length=50)
    jenis_kelamin = models.CharField(max_length=50, choices=[('L', 'Laki-laki'), ('P', 'Perempuan')])
    tgl_lahir = models.DateField()
    wali = models.CharField(max_length=100)
    alamat = models.TextField()
    nomor_hp = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.nama} {self.jenis_kelamin}"

class Galeri(models.Model):
    tpq = models.ForeignKey(TPQ, related_name='galleries', on_delete=models.CASCADE)
    gambar = models.ImageField(upload_to='gallery_images/')
    title = models.TextField(blank=True, null=True, default='-')
    deskripsi = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.deskripsi

class Jadwal(models.Model):
    tpq = models.ForeignKey(TPQ, related_name='schedules', on_delete=models.CASCADE)
    kegiatan = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True, null=True)
    jam_mauli = models.TimeField()
    jam_pulang = models.TimeField()

    def __str__(self):
        return self.kegiatan
