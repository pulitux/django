from django.urls import path
from gestion import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alta', views.alta, name='alta'),
    path('baja', views.baja, name='baja'),
]