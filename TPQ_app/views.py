from django.shortcuts import render, get_object_or_404, redirect
from .models import TPQ, Guru, Murid, Galeri, Jadwal
from .forms import TPQForm, GuruForm, MuridForm, GaleriForm, JadwalForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
# Create your views here.

# login
def signout_form(request):
    logout(request)
    return redirect('index')

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

# halaman home
def index(request):
    data = TPQ.objects.all().order_by('-id')
    context = {
        'datas':data,
    }
    return render(request, 'index.html', context)

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
@login_required
def tpq_list(request):
    datas = TPQ.objects.all().order_by('-id')

    context = {
        'datas':datas,
    }
    return render(request, 'dashboard_tpq.html', context)

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

@login_required
def tpq_delete(request, pk):
    tpq = get_object_or_404(TPQ, pk=pk)
    tpq.delete()
    return redirect('tpq_list')


# Guru Views
@login_required
def guru_list(request):
    gurus = Guru.objects.all().order_by('-id')
    context = {
        'gurus': gurus,
    }
    return render(request, 'dashboard_guru.html', context)

@login_required
def guru_create(request):
    if request.method == 'POST':
        form = GuruForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guru_list')
    else:
        form = GuruForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard_form.html', context)

@login_required
def guru_update(request, pk):
    guru = get_object_or_404(Guru, pk=pk)
    if request.method == 'POST':
        form = GuruForm(request.POST, instance=guru)
        if form.is_valid():
            form.save()
            return redirect('guru_list')
    else:
        form = GuruForm(instance=guru)
    context = {
        'form': form,
    }
    return render(request, 'dashboard_form.html', context)

@login_required
def guru_delete(request, pk):
    guru = get_object_or_404(Guru, pk=pk)
    guru.delete()
    return redirect('guru_list')
    

# Murid Views

@login_required
def murid_list(request):
    murids = Murid.objects.all().order_by('-id')
    context = {
        'murids': murids,
    }
    return render(request, 'dashboard_murid.html', context)

@login_required
def murid_detail(request, pk):
    murid = get_object_or_404(Murid, pk=pk)
    context = {
        'murid': murid,
    }
    return render(request, 'murid_detail.html', context)

@login_required
def murid_create(request):
    if request.method == 'POST':
        form = MuridForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('murid_list')
    else:
        form = MuridForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard_form.html', context)

@login_required
def murid_update(request, pk):
    murid = get_object_or_404(Murid, pk=pk)
    if request.method == 'POST':
        form = MuridForm(request.POST, instance=murid)
        if form.is_valid():
            form.save()
            return redirect('murid_list')
    else:
        form = MuridForm(instance=murid)
    context = {
        'form': form,
    }
    return render(request, 'dashboard_form.html', context)

@login_required
def murid_delete(request, pk):
    murid = get_object_or_404(Murid, pk=pk)
    murid.delete()
    return redirect('murid_list')

# Galeri Views
@login_required
def galeri_create(request):
    if request.method == 'POST':
        form = GaleriForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tpq_list')
    else:
        form = GaleriForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard_form.html', context)

@login_required
def galeri_update(request, pk):
    galeri = get_object_or_404(Galeri, pk=pk)
    if request.method == 'POST':
        form = GaleriForm(request.POST, request.FILES, instance=galeri)
        if form.is_valid():
            form.save()
            return redirect('tpq_list')
    else:
        form = GaleriForm(instance=galeri)
    context = {
        'form': form,
    }
    return render(request, 'dashboard_form.html', context)

@login_required
def galeri_delete(request, pk):
    galeri = get_object_or_404(Galeri, pk=pk)
    galeri.delete()
    return redirect('tpq_list')

# Jadwal Views
@login_required
def jadwal_list(request):
    jadwals = Jadwal.objects.all().order_by('-id')
    context = {
        'jadwals': jadwals,
    }
    return render(request, 'dashboard_jadwal.html', context)

@login_required
def jadwal_create(request):
    if request.method == 'POST':
        form = JadwalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jadwal_list')
    else:
        form = JadwalForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard_form.html', context)

@login_required
def jadwal_update(request, pk):
    jadwal = get_object_or_404(Jadwal, pk=pk)
    if request.method == 'POST':
        form = JadwalForm(request.POST, instance=jadwal)
        if form.is_valid():
            form.save()
            return redirect('jadwal_list')
    else:
        form = JadwalForm(instance=jadwal)
    context = {
        'form': form,
    }
    return render(request, 'dashboard_form.html', context)

@login_required
def jadwal_delete(request, pk):
    jadwal = get_object_or_404(Jadwal, pk=pk)
    jadwal.delete()
    return redirect('jadwal_list')
  