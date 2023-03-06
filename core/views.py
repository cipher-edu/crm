from django.shortcuts import render, HttpResponse, get_object_or_404,redirect
from .forms import *
from .models import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

def addclients(request):
    form = ClientsForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('clientservice')
    else:
        form = ClientsForm()
    context = {
        'form': form,
    }
    return render(request, 'pages/addclients.html', context)
def additems(request):
    return render(request, 'pages/additems.html')


def addorganizations(request):
    return render(request, 'pages/addorganizations.html')

def orgsevice(request):
    return render(request, 'pages/organizationsservice.html')

def orgseviceend(request):
    return render(request, 'pages/endserviceorg.html')

def orgseviceend(request):
    return render(request, 'pages/endserviceorg.html')
   
def addworker(request):
    return render(request, 'pages/addworker.html')


def clients(request):
    return render(request, 'pages/clients.html')


def clientservice(request):
    return render(request, 'pages/clientservice.html')

def endcerviceliend(request):
    return render(request, 'pages/endcerviceliend.html')

def organizations(request):
    return render(request, 'pages/organizations.html')

def workers(request):
    return render(request, 'pages/worker.hml')

def qarz(request):
    return render(request, 'pages/qarzorliklar.html')

def baza(request):
    return render(request, 'pages/baza.html')