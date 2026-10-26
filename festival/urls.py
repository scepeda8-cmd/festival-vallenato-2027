from django.urls import path

from .views import (
    categorias,
    votaciones,
    opciones
)

urlpatterns = [

    path(
        'categorias/',
        categorias,
        name='categorias'
    ),

    path(
        'votaciones/<int:categoria_id>/',
        votaciones,
        name='votaciones'
    ),

    path(
        'opciones/<int:votacion_id>/',
        opciones,
        name='opciones'
    ),

]