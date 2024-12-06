# eventos_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eventos/', include('eventos.urls')),
    path('autoridades/', include('autoridades.urls')),
    path('notificaciones/', include('notificaciones.urls')),
    path('', include('autenticacion.urls')),  # Incluye las URLs de autenticación y landing
]

