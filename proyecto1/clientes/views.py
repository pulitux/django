from django.shortcuts import render

def lista(request):
    lista_clientes = [
        'Ana',
        'Maria',
        'Pedro',
        'Jose',
        'Luis',
        'Pedro',
        'Jose',
        'Andrea',
        'Adrian',
        'Lucia',
        'Alex',
        'Benito',
        'Floro']
    contexto = {
        'lista_clientes': lista_clientes
    }
    return render(request, "lista.html",contexto)
# Create your views here.
