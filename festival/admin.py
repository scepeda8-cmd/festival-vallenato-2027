from django.contrib import admin

from .models import (
    Edicion,
    Categoria,
    Votacion,
    Opcion,
    Voto
)


@admin.register(Edicion)
class EdicionAdmin(admin.ModelAdmin):

    list_display = (
        'nombre',
        'anio'
    )

    search_fields = (
        'nombre',
    )


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):

    list_display = (
        'nombre',
        'edicion'
    )

    list_filter = (
        'edicion',
    )

    search_fields = (
        'nombre',
    )


@admin.register(Votacion)
class VotacionAdmin(admin.ModelAdmin):

    list_display = (
        'titulo',
        'categoria',
        'habilitada'
    )

    list_filter = (
        'habilitada',
        'categoria'
    )

    search_fields = (
        'titulo',
    )


@admin.register(Opcion)
class OpcionAdmin(admin.ModelAdmin):

    list_display = (
        'nombre',
        'votacion'
    )

    search_fields = (
        'nombre',
    )

    list_filter = (
        'votacion',
    )


@admin.register(Voto)
class VotoAdmin(admin.ModelAdmin):

    list_display = (
        'usuario',
        'categoria',
        'edicion',
        'opcion',
        'fecha_voto'
    )

    list_filter = (
        'edicion',
        'categoria'
    )

    search_fields = (
        'usuario__username',
        'opcion__nombre'
    )

    ordering = (
        '-fecha_voto',
    )