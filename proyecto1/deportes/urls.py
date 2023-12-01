from django.urls import path
from deportes import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('equipo', views.equipo, name='equipo'),
    path('madrid', views.jugadores, name='jugadores')
]