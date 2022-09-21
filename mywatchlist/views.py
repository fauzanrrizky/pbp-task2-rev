from django.shortcuts import render

from mywatchlist.models import MyWatchList

from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_mywatchlist = MyWatchList.objects.all()
    context = {
        'list_watchlist': data_mywatchlist,
        'nama': 'M Fauzan Rizky',
        'npm' : '2106654315',
        'kode_asdos' : 'ZEF'
    }
    return render(request, "mywatchlist.html", context)

# Membuat sebuah fungsi yang menerima parameter request (XML)
def request_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# Membuat sebuah fungsi yang menerima parameter request (JSON)
def request_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")