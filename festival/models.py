from django.db import models
from django.contrib.auth.models import User


class Edicion(models.Model):

    anio = models.IntegerField(unique=True)

    nombre = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.nombre


class Categoria(models.Model):

    edicion = models.ForeignKey(
        Edicion,
        on_delete=models.CASCADE
    )

    nombre = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.nombre


class Votacion(models.Model):

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )

    titulo = models.CharField(
        max_length=200
    )

    habilitada = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.titulo


class Opcion(models.Model):

    votacion = models.ForeignKey(
        Votacion,
        on_delete=models.CASCADE
    )

    nombre = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.nombre


class Voto(models.Model):

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    edicion = models.ForeignKey(
        Edicion,
        on_delete=models.CASCADE
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )

    opcion = models.ForeignKey(
        Opcion,
        on_delete=models.CASCADE
    )

    fecha_voto = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        constraints = [

            models.UniqueConstraint(

                fields=[
                    'usuario',
                    'categoria',
                    'edicion'
                ],

                name='voto_unico_por_categoria'

            )

        ]

    def __str__(self):

        return f"{self.usuario.username} - {self.categoria.nombre}"