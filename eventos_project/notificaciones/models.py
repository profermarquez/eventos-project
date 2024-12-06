# notificaciones/models.py
from django.db import models
from eventos.models import Evento
from autoridades.models import Autoridad

class Notificacion(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    autoridad = models.ForeignKey(Autoridad, on_delete=models.CASCADE)
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('enviado', 'Enviado'),
        ('error', 'Error'),
    ]
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')
    fecha_envio = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Notificación para {self.autoridad.nombre_completo} sobre {self.evento.titulo}"
