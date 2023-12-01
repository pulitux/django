from django.shortcuts import render, HttpResponse
def equipo(request):
    nombre='Real Madrid'
    dato=nombre.upper()
    lista={
           "equipo1":dato
           }
    return render(request, "futbol/equipoPref.html",lista)

def jugadores(request):
    listajugadores=[
        {
            "Nombre":"Sergio Ramos",
            "Demarcacion":"Defensa",
            "Numero":5
        },
        {
            "Nombre": "Eden Hazard",
            "Demarcacion": "Delantero",
            "Numero":7
        },
        {
            "Nombre": "Karim Benzema",
            "Demarcacion": "Delantero",
            "Numero":9
        },
        {
            "Nombre": "Toni Kroos",
            "Demarcacion": "Centrocampista",
            "Numero":8
        },
        {
            "Nombre": "Thibaut Courtois",
            "Demarcacion": "Portero",
            "Numero": 1
        }
    ]
    contexto = {
        'equipo': 'Real Madrid',
        'listado_jugadores': listajugadores
    }
    return render(request, "futbol/jugadores.html",contexto)
