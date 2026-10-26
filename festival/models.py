from django.db import models


class Edicion(models.Model):
    anio = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    edicion = models.ForeignKey(
        Edicion,
        on_delete=models.CASCADE
    )
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Votacion(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )
    titulo = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo


class Opcion(models.Model):
    votacion = models.ForeignKey(
        Votacion,
        on_delete=models.CASCADE
    )
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre