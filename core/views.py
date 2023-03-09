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


def clients(request ):
    client = Clientadd.objects.all()
    context ={
        "client":client
    }
    return render(request, 'pages/clients.html',context=context)

def show_client(request,client_id):
    show_client = get_object_or_404(Clientadd, pk=client_id)
    context = {
        'show_client':show_client
    }
    return render(request, 'pages/client-show.html', context=context)

def clientservice(request):
    form = CerviseClientForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CerviseClientForm()
    context = {
        'form': form,
    }
    return render(request, 'pages/clientservice.html', context=context)

def endcerviceliend(request):
    form = Cerviceendform(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Cerviceendform()
    context = {
        'form': form,
    }
    return render(request, 'pages/endcerviceliend.html', context=context)

def organizations(request):
    return render(request, 'pages/organizations.html')

def workers(request):
    return render(request, 'pages/worker.hml')

def qarz(request):
    return render(request, 'pages/qarzorliklar.html')

def baza(request):
    return render(request, 'pages/baza.html')