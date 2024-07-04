from django import forms
from .models import TPQ, Guru, Murid, Galeri, Jadwal

class TPQForm(forms.ModelForm):
    class Meta:
        model = TPQ
        fields = ['nama', 'alamat', 'email']

        widgets = {
            'nama':forms.TextInput(attrs={'class':'form-control'}),
            'alamat':forms.Textarea(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }

class GuruForm(forms.ModelForm):
    class Meta:
        model = Guru
        fields = ['tpq', 'nama', 'nomor_hp', 'email']

        widgets = {
            'tpq':forms.Select(attrs={'class':'form-control'}),
            'nama':forms.TextInput(attrs={'class':'form-control'}),
            'nomor_hp':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }

class MuridForm(forms.ModelForm):
    class Meta:
        model = Murid
        fields = ['tpq', 'nama', 'jenis_kelamin', 'tgl_lahir', 'wali', 'alamat', 'nomor_hp']

        widgets = {
            'tpq':forms.Select(attrs={'class':'form-control'}),
            'nama':forms.TextInput(attrs={'class':'form-control'}),
            'jenis_kelamin':forms.Select(attrs={'class':'form-control'}),
            'tgl_lahir':forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
            'wali':forms.TextInput(attrs={'class':'form-control'}),
            'alamat':forms.Textarea(attrs={'class':'form-control'}),
            'nomor_hp':forms.NumberInput(attrs={'class':'form-control'}),
        }

class GaleriForm(forms.ModelForm):
    class Meta:
        model = Galeri
        fields = ['tpq', 'gambar', 'title','deskripsi']

        widgets = {
            'tpq':forms.Select(attrs={'class':'form-control'}),
            'gambar':forms.FileInput(attrs={'class':'form-control', 'type':'file'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'deskripsi':forms.Textarea(attrs={'class':'form-control'})
        }

class JadwalForm(forms.ModelForm):
    class Meta:
        model = Jadwal
        fields = ['tpq', 'kegiatan', 'deskripsi', 'jam_mauli', 'jam_pulang']

        widgets = {
            'tpq':forms.Select(attrs={'class':'form-control'}),
            'kegiatan':forms.TextInput(attrs={'class':'form-control'}),
            'deskripsi':forms.Textarea(attrs={'class':'form-control'}),
            'jam_mauli':forms.TimeInput(attrs={'class':'form-control', 'type':'time'}),
            'jam_pulang':forms.TimeInput(attrs={'class':'form-control', 'type':'time'})
        }