from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    """
    Modelo de usuario personalizado que extiende de AbstractUser.
    """
    email = models.EmailField(_('Correo Electrónico'), unique=True)
    phone_number = models.CharField(_('Número de Teléfono'), max_length=15, blank=True, null=True)
    address = models.TextField(_('Dirección'), blank=True, null=True)

    # Opcional: campos adicionales personalizados
    is_verified = models.BooleanField(_('¿Correo Verificado?'), default=False)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('Usuario Personalizado')
        verbose_name_plural = _('Usuarios Personalizados')
