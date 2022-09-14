from django.shortcuts import render

# TODO: Create your views here.
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'list_katalog': data_barang_katalog,
        'nama': 'M Fauzan Rizky',
        'npm' : '2106654315',
    }
    return render(request, "katalog.html", context)
