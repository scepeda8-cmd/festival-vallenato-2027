from django.shortcuts import render

from .models import Categoria
from .models import Votacion
from .models import Opcion


def categorias(request):

    categorias = Categoria.objects.all()

    return render(
        request,
        'categorias.html',
        {
            'categorias': categorias
        }
    )


def votaciones(request, categoria_id):

    categoria = Categoria.objects.get(
        id=categoria_id
    )

    votaciones = Votacion.objects.filter(
        categoria=categoria
    )

    return render(
        request,
        'votaciones.html',
        {
            'categoria': categoria,
            'votaciones': votaciones
        }
    )


def opciones(request, votacion_id):

    votacion = Votacion.objects.get(
        id=votacion_id
    )

    opciones = Opcion.objects.filter(
        votacion=votacion
    )

    return render(
        request,
        'opciones.html',
        {
            'votacion': votacion,
            'opciones': opciones
        }
    )