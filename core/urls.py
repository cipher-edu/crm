from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('mijoz-yaratish', addclients, name='addclient'),
    path('maxsuot-yaratish', additems, name="additems"),
    path('tashkilot-qo\'shish', addorganizations, name="addorganizations"),
    path('ish-yaratish', addworker, name="addworker"),
    path('mijozlar', clients, name="clients")
]
