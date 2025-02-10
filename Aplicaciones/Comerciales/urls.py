from django.urls import path
from . import views

urlpatterns = [
    # Proyecto
    path('',views.inicio),
    path('nuevoProyecto/', views.nuevoProyecto),
    path('listadoProyecto/', views.listadoProyecto),
    path('guardarProyecto/', views.guardarProyecto),
    path('eliminarProyecto/<id>', views.eliminarProyecto),
    path('editarProyecto/<id>', views.editarProyecto),
    path('procesarEdicionProyecto/', views.procesarEdicionProyecto),

    # Cliente
    path('nuevoCliente/', views.nuevoCliente),
    path('listadoCliente/', views.listadoCliente),
    path('guardarCliente/', views.guardarCliente),
    path('eliminarCliente/<id>', views.eliminarCliente),
    path('editarCliente/<id>', views.editarCliente),
    path('procesarEdicionCliente/', views.procesarEdicionCliente),

    # Contratista
    path('nuevoContratista/', views.nuevoContratista),
    path('listadoContratista/', views.listadoContratista),
    path('guardarContratista/', views.guardarContratista),
    path('eliminarContratista/<id>', views.eliminarContratista),
    path('editarContratista/<id>', views.editarContratista),
    path('procesarEdicionContratista/', views.procesarEdicionContratista),

    # Local
    path('nuevoLocal/', views.nuevoLocal),
    path('listadoLocal/', views.listadoLocal),
    path('guardarLocal/', views.guardarLocal),
    path('eliminarLocal/<id>', views.eliminarLocal),
    path('editarLocal/<id>', views.editarLocal),
    path('procesarEdicionLocal/', views.procesarEdicionLocal),
]
