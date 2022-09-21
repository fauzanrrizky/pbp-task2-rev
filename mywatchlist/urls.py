# TODO: Implement Routings Here

from django.urls import path
from mywatchlist.views import show_mywatchlist

from mywatchlist.views import request_xml #Import fungsi yang sudah dibuat di mywatchlist\view
from mywatchlist.views import request_json #Import fungsi yang sudah dibuat di mywatchlist\view

app_name = 'mywatchlist'

urlpatterns = [
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', request_xml, name='request_xml'),
    path('json/', request_json, name='show_json'), #sesuaikan dengan nama fungsi yang dibuat
]