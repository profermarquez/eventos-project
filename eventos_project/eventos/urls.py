from django.urls import path
from . import views

app_name = 'eventos'

urlpatterns = [
    path('', views.lista_eventos, name='lista'),
    path('crear/', views.crear_evento, name='crear'),
    path('<int:pk>/editar/', views.editar_evento, name='editar'),
    path('<int:pk>/eliminar/', views.eliminar_evento, name='eliminar'),
]
