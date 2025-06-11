from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registrar-socio/', views.registrar_socio, name='registrar_socio'),
    path('agregar-beneficio/', views.agregar_beneficio, name='agregar_beneficio'),
    path('agregar-categoria/', views.agregar_categoria, name='agregar_categoria'),
    path('lista-beneficios/', views.lista_beneficios, name='lista_beneficios'),
    path('beneficio/<int:pk>/', views.detalle_beneficio, name='detalle_beneficio'),
]
