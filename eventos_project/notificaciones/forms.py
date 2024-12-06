# notificaciones/forms.py
from django import forms
from .models import Notificacion

class NotificacionForm(forms.ModelForm):
    class Meta:
        model = Notificacion
        fields = ['evento', 'autoridad', 'estado']
        widgets = {
            'evento': forms.Select(attrs={'class': 'form-select'}),
            'autoridad': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }
