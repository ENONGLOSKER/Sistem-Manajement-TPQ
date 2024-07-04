# Generated by Django 5.0.3 on 2024-07-02 22:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TPQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('alamat', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Murid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('jenis_kelamin', models.CharField(choices=[('L', 'Laki-laki'), ('P', 'Perempuan')], max_length=50)),
                ('tgl_lahir', models.DateField()),
                ('wali', models.CharField(max_length=100)),
                ('alamat', models.TextField()),
                ('nomor_hp', models.CharField(blank=True, max_length=15, null=True)),
                ('tpq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='TPQ_app.tpq')),
            ],
        ),
        migrations.CreateModel(
            name='Jadwal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kegiatan', models.CharField(max_length=100)),
                ('deskripsi', models.TextField(blank=True, null=True)),
                ('jam_mauli', models.DateTimeField()),
                ('jam_pulang', models.DateTimeField()),
                ('tpq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='TPQ_app.tpq')),
            ],
        ),
        migrations.CreateModel(
            name='Guru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('nomor_hp', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('tpq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='TPQ_app.tpq')),
            ],
        ),
        migrations.CreateModel(
            name='Galeri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gambar', models.ImageField(upload_to='gallery_images/')),
                ('deskripsi', models.TextField(blank=True, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('tpq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='galleries', to='TPQ_app.tpq')),
            ],
        ),
    ]