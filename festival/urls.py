from django.urls import path

from .views import (
    categorias,
    votaciones,
    opciones,
    mis_votos,
    api_categorias
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

    path(
        'mis-votos/',
        mis_votos,
        name='mis_votos'
    ),

    path(
        'api/categorias/',
        api_categorias,
        name='api_categorias'
    ),

]