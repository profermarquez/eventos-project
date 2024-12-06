# eventos/forms.py
from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descripcion', 'tematica', 'fecha', 'horario', 'lugar']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-input'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-textarea'}),
            'tematica': forms.TextInput(attrs={'class': 'form-input'}),
            'fecha': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'horario': forms.TimeInput(attrs={'class': 'form-input', 'type': 'time'}),
            'lugar': forms.TextInput(attrs={'class': 'form-input'}),
        }
