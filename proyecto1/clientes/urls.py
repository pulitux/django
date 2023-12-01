from django.urls import path
from clientes import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('lista', views.lista, name='lista')
    ]