from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def addclients(request):
    return render(request, 'pages/addcliens.html')

def additems(request):
    return render(request, 'pages/aditems.html')


def addorganizations(request):
    return render(request, 'pages/addorganizations.html')

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