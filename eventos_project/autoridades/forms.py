# autoridades/forms.py
from django import forms
from .models import Autoridad

class AutoridadForm(forms.ModelForm):
    class Meta:
        model = Autoridad
        fields = ['nombre_completo', 'cargo', 'entidad', 'campo_accion', 'email', 'telefono']
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class': 'form-input'}),
            'cargo': forms.TextInput(attrs={'class': 'form-input'}),
            'entidad': forms.TextInput(attrs={'class': 'form-input'}),
            'campo_accion': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'telefono': forms.TextInput(attrs={'class': 'form-input'}),
        }
