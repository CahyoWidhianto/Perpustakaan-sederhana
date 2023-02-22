from django.forms import ModelForm
from django import forms
from perpustakaan.models import Buku

class FormBuku(ModelForm):
    class Meta:
        model = Buku
        #mengambil sebagian filed
        # fields = ['judul', 'penulis', 'kelompok' ]
        #mengambil semua filed
        fields = '__all__'
        #mengambil data kecuali 
        # exclude = ['penerbit', 'jumlah_buku']
        
        widgets = {
            'judul' : forms.TextInput({'class': 'form-control'}),
            'penulis' : forms.TextInput({'class': 'form-control'}),
            'penerbit' : forms.TextInput({'class': 'form-control'}),
            'jumlah' : forms.NumberInput({'class': 'form-control'}),
            'kelompok' : forms.Select({'class': 'form-control'}),
        }