# eventos/models.py
from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    tematica = models.CharField(max_length=100)
    fecha = models.DateField()
    horario = models.TimeField()
    lugar = models.CharField(max_length=200)
    
    def __str__(self):
        return self.titulo
