from django.contrib import admin
from perpustakaan.models import Buku, Kelompok
# Register your models here.

class BukuAdmin(admin.ModelAdmin):
    list_display = ['judul', 'penulis','penerbit','jumlah_buku']
    search_fields = ['judul', 'penulis', 'penerbit']
    list_filter =['kelompok']
    list_per_page = 1
    

admin.site.register(Buku, BukuAdmin)
admin.site.register(Kelompok)
