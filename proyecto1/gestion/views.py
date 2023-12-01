from django.shortcuts import HttpResponse, render

def index(request):
    return render(request, 'dia1/inicio.html')
def alta(request):
    return render(request, 'dia1/alta.html')
def baja(request):
    return render(request, 'dia1/baja.html')

# Create your views here.
