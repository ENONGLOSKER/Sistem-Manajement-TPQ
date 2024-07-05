from django.shortcuts import render, get_object_or_404, redirect
from .models import TPQ, Guru, Murid, Galeri, Jadwal
from .forms import TPQForm, GuruForm, MuridForm, GaleriForm, JadwalForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
# Create your views here.

# LOGIN DAN LOGOUT ================================================================
# Fungsi signout_form digunakan untuk melakukan logout pengguna dan mengarahkannya kembali ke halaman indeks.
def signout_form(request):
    logout(request)
    return redirect('index')
# Fungsi signin_form digunakan untuk proses login pengguna. Jika metode permintaan adalah POST, maka akan melakukan otentikasi username dan password. Jika berhasil, pengguna akan diarahkan ke dashboard dengan pesan sukses. Jika gagal, akan diberikan pesan error dan diarahkan kembali ke halaman sign-in. Jika pengguna sudah terotentikasi, akan diarahkan ke dashboard.
def sigin_form(request):
    
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Sign in Berhasil, Selamat datang {user}")
            return redirect('dashboard')
        else:
            messages.error(request, "Sign in Gagal, Silahkan coba kembali!")
            return redirect('signin')
        
    if request.user.is_authenticated:
        return redirect('dashboard')

    return render(request, 'signin.html')


# HALAMAN HOME DAN DASHBOARD ================================================================
# halaman home
# Fungsi index digunakan untuk menampilkan halaman utama dengan data TPQ yang diurutkan berdasarkan ID secara descending.
def index(request):
    data = TPQ.objects.all().order_by('-id')
    context = {
        'datas':data,
    }
    return render(request, 'index.html', context)
# Fungsi dashboard digunakan untuk menampilkan dashboard dengan total TPQ, murid, dan guru yang dihitung dan disertakan dalam konteks untuk dirender ke template dashboard.html.
@login_required
def dashboard(request):
    total_tpq = TPQ.objects.all().count()
    total_murid = Murid.objects.all().count()
    total_guru = Guru.objects.all().count()
    context = {
        'total_tpq':total_tpq,
        'total_murid':total_murid,
        'total_guru':total_guru,
    }
    return render(request, 'dashboard.html', context)



# DASHBOARD TPQ, GURU, GALERI DAN JADWAL ================================================================
# tpq_list(request): Menampilkan daftar TPQ yang ada dengan mengambil semua objek TPQ dan mengurutkannya berdasarkan ID secara descending. Data TPQ tersebut disertakan dalam konteks dan dirender ke template 'dashboard_tpq.html'.
@login_required
def tpq_list(request):
    datas = TPQ.objects.all().order_by('-id')

    context = {
        'datas':datas,
    }
    return render(request, 'dashboard_tpq.html', context)
# tpq_detail(request, pk): Menampilkan detail dari suatu TPQ berdasarkan primary key (pk) yang diberikan. Fungsi ini juga mengambil data guru, murid, jadwal, dan galeri yang terkait dengan TPQ tersebut untuk ditampilkan dalam halaman detail.
@login_required
def tpq_detail(request, pk):
    tpq = get_object_or_404(TPQ, pk=pk)
    
    # Mengambil data guru, murid, jadwal, dan galeri berdasarkan tpq
    guru = Guru.objects.filter(tpq=tpq)
    murid = Murid.objects.filter(tpq=tpq)
    jadwal = Jadwal.objects.filter(tpq=tpq)
    galeri = Galeri.objects.filter(tpq=tpq)

    context = {
        'tpq': tpq,
        'gurus': guru,
        'murid': murid,
        'jadwal': jadwal,
        'galeri': galeri,
    }
    return render(request, 'dashboard_daetail.html', context)
# tpq_create(request): Membuat entri TPQ baru. Jika metode permintaan adalah POST dan formulir valid, entri TPQ baru akan disimpan dan pengguna akan diarahkan kembali ke daftar TPQ.
@login_required
def tpq_create(request):
    if request.method == 'POST':
        form = TPQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tpq_list')
    else:
        form = TPQForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard_form.html', context)
# tpq_update(request, pk): Memperbarui data TPQ berdasarkan primary key (pk) yang diberikan. Jika metode permintaan adalah POST dan formulir valid, data TPQ akan diperbarui dan pengguna akan diarahkan kembali ke daftar TPQ.
@login_required
def tpq_update(request, pk):
    tpq = get_object_or_404(TPQ, pk=pk)
    if request.method == 'POST':
        form = TPQForm(request.POST, instance=tpq)
        if form.is_valid():
            form.save()
            return redirect('tpq_list')
    else:
        form = TPQForm(instance=tpq)
    context = {
        'form': form,
    }
    return render(request, 'dashboard_form.html', context)
# tpq_delete(request, pk): Menghapus data TPQ berdasarkan primary key (pk) yang diberikan. Setelah penghapusan, pengguna akan diarahkan kembali ke daftar TPQ.
@login_required
def tpq_delete(request, pk):
    tpq = get_object_or_404(TPQ, pk=pk)
    tpq.delete()
    return redirect('tpq_list')


# Guru Views
# guru_list(request): Menampilkan daftar guru yang ada dengan mengambil semua objek Guru yang ada dan mengurutkannya berdasarkan ID secara descending. Data guru tersebut disertakan dalam konteks dan dirender ke template 'dashboard_guru.html'.
@login_required
def guru_list(request):
    gurus = Guru.objects.all().order_by('-id')
    context = {
        'gurus': gurus,
    }
    return render(request, 'dashboard_guru.html', context)
# guru_create(request): Membuat entri Guru baru. Jika metode permintaan adalah POST dan formulir valid, entri Guru baru akan disimpan dan pengguna akan diarahkan ke detail TPQ yang terkait dengan Guru tersebut. Jika tidak, formulir kosong akan disertakan dalam konteks untuk dirender ke template 'dashboard_form.html'.
@login_required
def guru_create(request):
    if request.method == 'POST':
        form = GuruForm(request.POST)
        if form.is_valid():
            form.save()
            guru = form.instance  # Mendapatkan instance dari objek yang baru saja disimpan
            return redirect('tpq_detail', pk=guru.tpq.pk)
    else:
        form = GuruForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard_form.html', context)
# guru_update(request, pk): Memperbarui data Guru berdasarkan ID yang diberikan. Jika metode permintaan adalah POST dan formulir valid, data Guru akan diperbarui dan pengguna akan diarahkan kembali ke detail TPQ yang terkait. Jika tidak, formulir dengan data Guru yang ada akan disertakan dalam konteks.
@login_required
def guru_update(request, pk):
    guru = get_object_or_404(Guru, pk=pk)
    if request.method == 'POST':
        form = GuruForm(request.POST, instance=guru)
        if form.is_valid():
            form.save()
            guru = form.instance
            return redirect('tpq_detail', pk=guru.tpq.pk)
    else:
        form = GuruForm(instance=guru)
    context = {
        'form': form,
    }
    return render(request, 'dashboard_form.html', context)
# guru_delete(request, pk): Menghapus data Guru berdasarkan ID yang diberikan. Setelah penghapusan, pengguna akan diarahkan kembali ke detail TPQ yang terkait dengan Guru yang dihapus.
@login_required
def guru_delete(request, pk):
    guru = get_object_or_404(Guru, pk=pk)
    tpq_pk = guru.tpq.pk
    guru.delete()
    return redirect('tpq_detail', pk=tpq_pk)
    

# Murid Views
# jadwal_delete(request, pk): Fungsi ini digunakan untuk menghapus jadwal berdasarkan ID yang diberikan. Setelah penghapusan, pengguna akan diarahkan kembali ke detail TPQ yang terkait dengan jadwal yang dihapus.
@login_required
def murid_list(request):
    murids = Murid.objects.all().order_by('-id')
    context = {
        'murids': murids,
    }
    return render(request, 'dashboard_murid.html', context)

# murid_create(request): Membuat entri Murid baru. Jika metode permintaan adalah POST dan formulir valid, entri Murid baru akan disimpan dan pengguna akan diarahkan ke detail TPQ yang terkait dengan Murid tersebut.
@login_required
def murid_create(request):
    if request.method == 'POST':
        form = MuridForm(request.POST)
        if form.is_valid():
            form.save()
            murid = form.instance
            return redirect('tpq_detail', pk=murid.tpq.pk)
    else:
        form = MuridForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard_form.html', context)
# murid_update(request, pk): Memperbarui data Murid berdasarkan ID yang diberikan. Jika metode permintaan adalah POST dan formulir valid, data Murid akan diperbarui dan pengguna akan diarahkan kembali ke detail TPQ yang terkait.
@login_required
def murid_update(request, pk):
    murid = get_object_or_404(Murid, pk=pk)
    if request.method == 'POST':
        form = MuridForm(request.POST, instance=murid)
        if form.is_valid():
            form.save()
            murid = form.instance
            return redirect('tpq_detail', pk=murid.tpq.pk)
    else:
        form = MuridForm(instance=murid)
    context = {
        'form': form,
    }
    return render(request, 'dashboard_form.html', context)
# murid_delete(request, pk): Menghapus data Murid berdasarkan ID yang diberikan. Setelah penghapusan, pengguna akan diarahkan kembali ke detail TPQ yang terkait dengan Murid yang dihapus.
@login_required
def murid_delete(request, pk):
    murid = get_object_or_404(Murid, pk=pk)
    tpq_pk = murid.tpq.pk
    murid.delete()
    return redirect('tpq_detail', pk=tpq_pk)

# Galeri Views
# Fungsi ini digunakan untuk membuat entri galeri baru. Jika metode permintaan adalah POST dan formulir valid, entri galeri baru akan disimpan dan pengguna akan diarahkan kembali ke detail TPQ yang terkait dengan galeri tersebut. Jika tidak, formulir kosong akan disertakan dalam konteks untuk dirender ke template 'dashboard_form.html'.
@login_required
def galeri_create(request):
    if request.method == 'POST':
        form = GaleriForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            galeri = form.instance
            return redirect('tpq_detail', pk=galeri.tpq.pk)
    else:
        form = GaleriForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard_form.html', context)

# Fungsi ini digunakan untuk memperbarui entri galeri berdasarkan ID yang diberikan. Jika metode permintaan adalah POST dan formulir valid, entri galeri akan diperbarui dan pengguna akan diarahkan kembali ke detail TPQ yang terkait dengan galeri yang diperbarui. Jika tidak, formulir dengan data galeri yang ada akan disertakan dalam konteks.
@login_required
def galeri_update(request, pk):
    galeri = get_object_or_404(Galeri, pk=pk)
    if request.method == 'POST':
        form = GaleriForm(request.POST, request.FILES, instance=galeri)
        if form.is_valid():
            form.save()
            galeri = form.instance
            return redirect('tpq_detail', pk=galeri.tpq.pk)
    else:
        form = GaleriForm(instance=galeri)
    context = {
        'form': form,
    }
    return render(request, 'dashboard_form.html', context)

# Fungsi ini digunakan untuk menghapus entri galeri berdasarkan ID yang diberikan. Setelah penghapusan, pengguna akan diarahkan kembali ke detail TPQ yang terkait dengan galeri yang dihapus.
@login_required
def galeri_delete(request, pk):
    galeri = get_object_or_404(Galeri, pk=pk)
    tpq_pk = galeri.tpq.pk
    galeri.delete()
    return redirect('tpq_detail', pk=tpq_pk)



# Jadwal Views
# jadwal_list(request): Fungsi ini digunakan untuk menampilkan daftar jadwal yang ada, dengan mengambil semua objek Jadwal yang ada dan mengurutkannya berdasarkan ID secara descending. Data jadwal tersebut kemudian disertakan dalam konteks dan dirender ke template 'dashboard_jadwal.html'.
@login_required
def jadwal_list(request):
    jadwals = Jadwal.objects.all().order_by('-id')
    context = {
        'jadwals': jadwals,
    }
    return render(request, 'dashboard_jadwal.html', context)

# jadwal_create(request): Fungsi ini digunakan untuk membuat jadwal baru. Jika metode permintaan adalah POST dan formulir valid, jadwal baru akan disimpan dan pengguna akan diarahkan ke detail TPQ yang terkait dengan jadwal tersebut. Jika tidak, formulir kosong akan disertakan dalam konteks untuk dirender ke template 'dashboard_form.html
@login_required
def jadwal_create(request):
    if request.method == 'POST':
        form = JadwalForm(request.POST)
        if form.is_valid():
            form.save()
            jadwal = form.instance
            return redirect('tpq_detail', pk=jadwal.tpq.pk)
    else:
        form = JadwalForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard_form.html', context)

# jadwal_update(request, pk): Fungsi ini digunakan untuk memperbarui jadwal yang ada berdasarkan ID yang diberikan. Jika metode permintaan adalah POST dan formulir valid, jadwal akan diperbarui dan pengguna akan diarahkan kembali ke detail TPQ yang terkait. Jika tidak, formulir dengan data jadwal yang ada akan disertakan dalam konteks.
@login_required
def jadwal_update(request, pk):
    jadwal = get_object_or_404(Jadwal, pk=pk)
    if request.method == 'POST':
        form = JadwalForm(request.POST, instance=jadwal)
        if form.is_valid():
            form.save()
            jadwal = form.instance
            return redirect('tpq_detail', pk=jadwal.tpq.pk)
    else:
        form = JadwalForm(instance=jadwal)
    context = {
        'form': form,
    }
    return render(request, 'dashboard_form.html', context)

# jadwal_delete(request, pk): Fungsi ini digunakan untuk menghapus jadwal berdasarkan ID yang diberikan. Setelah penghapusan, pengguna akan diarahkan kembali ke detail TPQ yang terkait dengan jadwal yang dihapus.
@login_required
def jadwal_delete(request, pk):
    jadwal = get_object_or_404(Jadwal, pk=pk)
    tpq_pk = jadwal.tpq.pk
    jadwal.delete()
    return redirect('tpq_detail', pk=tpq_pk)
  