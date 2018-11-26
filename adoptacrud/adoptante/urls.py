from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('registro/', views.registro, name="registro"),
    path('registro/crear', views.crear, name="crear"),
    path('buscar/<str:run>', views.buscar, name="buscar"),
    path('eliminar/<str:run>', views.eliminar, name="eliminar"),
    path('editar/<str:run>', views.editar, name="editar"),
    path('registro/edicion/<str:run>', views.edicion, name="edicion"),
    path('registro/test', views.index, name="test")
]