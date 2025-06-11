from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registrar/', views.registrar_socio, name='registrar_socio'),
    path('beneficios/', views.lista_beneficios, name='lista_beneficios'),
    path('beneficios/<int:pk>/', views.detalle_beneficio, name='detalle_beneficio'),
    path('agregar-beneficio/', views.agregar_beneficio, name='agregar_beneficio'),
    path('agregar-categoria/', views.agregar_categoria, name='agregar_categoria'),
]