from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from django.http import JsonResponse

from .models import (
    Categoria,
    Votacion,
    Opcion,
    Voto
)


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

    voto_usuario = None

    if request.user.is_authenticated:

        voto_usuario = Voto.objects.filter(
            usuario=request.user,
            categoria=votacion.categoria,
            edicion=votacion.categoria.edicion
        ).first()

    if request.method == 'POST':

        if not votacion.habilitada:

            messages.error(
                request,
                'Esta votación se encuentra cerrada.'
            )

            return redirect(
                'opciones',
                votacion_id=votacion.id
            )

        if not request.user.is_authenticated:

            messages.error(
                request,
                'Debes iniciar sesión para registrar un voto.'
            )

            return redirect('login')

        opcion_id = request.POST.get(
            'opcion'
        )

        try:

            opcion = Opcion.objects.get(
                id=opcion_id
            )

        except Opcion.DoesNotExist:

            messages.error(
                request,
                'La opción seleccionada no existe.'
            )

            return redirect(
                'opciones',
                votacion_id=votacion.id
            )

        if opcion.votacion.id != votacion.id:

            messages.error(
                request,
                'La opción seleccionada no pertenece a esta votación.'
            )

            return redirect(
                'opciones',
                votacion_id=votacion.id
            )

        try:

            Voto.objects.create(

                usuario=request.user,

                edicion=votacion.categoria.edicion,

                categoria=votacion.categoria,

                opcion=opcion

            )

            messages.success(
                request,
                'Voto registrado correctamente.'
            )

        except IntegrityError:

            messages.error(
                request,
                'Ya participaste en esta categoría.'
            )

        return redirect(
            'opciones',
            votacion_id=votacion.id
        )

    return render(
        request,
        'opciones.html',
        {
            'votacion': votacion,
            'opciones': opciones,
            'voto_usuario': voto_usuario
        }
    )


def mis_votos(request):

    votos = Voto.objects.filter(
        usuario=request.user
    )

    return render(
        request,
        'mis_votos.html',
        {
            'votos': votos
        }
    )


def api_categorias(request):

    datos = []

    categorias = Categoria.objects.all()

    for categoria in categorias:

        opciones_categoria = []

        votaciones_categoria = Votacion.objects.filter(
            categoria=categoria
        )

        for votacion in votaciones_categoria:

            opciones_votacion = Opcion.objects.filter(
                votacion=votacion
            )

            for opcion in opciones_votacion:

                opciones_categoria.append(
                    opcion.nombre
                )

        datos.append({

            "categoria": categoria.nombre,

            "edicion": categoria.edicion.nombre,

            "opciones": opciones_categoria

        })

    return JsonResponse(
        datos,
        safe=False,
        json_dumps_params={
            'ensure_ascii': False
        }
    )