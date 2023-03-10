from django.shortcuts import redirect, render, HttpResponse
from perpustakaan.models import Buku
from  perpustakaan.forms import FormBuku
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from perpustakaan.resource import BukuResource
# Create your views here.

def export_xls(request):
    buku = BukuResource()
    dataset = buku.export()
    response = HttpResponse(dataset.xls,content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Laporan buku.xls"'
    return response

@login_required(login_url=settings.LOGIN_URL)
def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User berhasil dibuat!")
            return redirect('signup')
        else:
            messages.error(request, "Terjadi kesalahan!")
            return redirect('signup')
    else:
        form = UserCreationForm()
        konteks = {
            'form':form
        }
        return render(request, 'signup.html', konteks)
    

@login_required(login_url=settings.LOGIN_URL)
def buku(request):
    books = Buku.objects.all()
    # menampilkan dengan syarat 
    # books = Buku.objects.filter(jumlah=2)
    # konsep inner join mengambil berdasarkan id dari foreign key
    # books = Buku.objects.filter(kelompok__= 'nama kelompok dalam table')
    # mengambil semua data yang ada
    # limit data (berapa banyak data yang ingin di ambil)
    # books = Buku.objects.all()[:1]
    
    konteks = {
        'books' : books
    }
    return render(request, 'buku.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def penerbit(request):
    return render(request, 'penerbit.html')

@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormBuku()
            pesan = "Data berhasil disimpan"
            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-buku.html', konteks)
    else:
        form = FormBuku()
        
        konteks = {
            'form': form,
        }
    
    return render(request, 'tambah-buku.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah-buku.html'
    if request.POST:
        form = FormBuku(request.POST,  request.FILES, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil diperbaharui")
            return redirect('ubah_buku', id_buku=id_buku)
            
    else:
        form = FormBuku(instance=buku)
        konteks = {
            'form': form,
            'buku': buku,
        }
        return render(request, template, konteks) 
   
@login_required(login_url=settings.LOGIN_URL) 
def hapus_buku(request, id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()
    
    
    return redirect('/buku/')
    