# autoridades/models.py
from django.db import models

class Autoridad(models.Model):
    nombre_completo = models.CharField(max_length=200)
    cargo = models.CharField(max_length=100)
    entidad = models.CharField(max_length=200)
    campo_accion = models.CharField(max_length=200)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_completo

