from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'phone_number', 'address']
        widgets = {
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Ejemplo: +123456789', 
                'class': 'form-input'
            }),
            'address': forms.Textarea(attrs={
                'rows': 3, 
                'placeholder': 'Introduce tu dirección', 
                'class': 'form-textarea'
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo ya está registrado.")
        return email
