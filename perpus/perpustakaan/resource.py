from import_export import resources
from perpustakaan.models import Buku

class BukuResource(resources.ModelResource):
    class Meta:
        model = Buku
        fileds = ['judul', 'tanggal', 'kelompok', 'penerbit','jumlah_buku']
        export_order = ['judul', 'kelompok', 'tanggal',  'penerbit','jumlah_buku']
        