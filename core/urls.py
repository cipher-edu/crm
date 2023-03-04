from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('mijoz-yaratish', addclients, name='addclient'),
    path('maxsulot-yaratish', additems, name="additems"),
    path('tashkilot-qo\'shish', addorganizations, name="addorganizations"),
    path('ish-yaratish', addworker, name="addworker"),
    path('mijozlar', clients, name="clients"),
    path('mijozlarga-xizmat-ko\'rsatish',clientservice,name='clientservice'),
    path('mijozga-xizmatni-yakunlash', endcerviceliend, name='endcerviceliend'),
    path('tashkilotlar', organizations, name='organizations'),
    path('workers', workers, name='workers'),
    path('org-service/', orgsevice, name="orgsevice"),
    path('end-service-organizations', orgseviceend, name='orgseviceend')

]
