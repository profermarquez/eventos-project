from django.urls import path
from . import views

app_name = 'notificaciones'

urlpatterns = [
    path('', views.lista_notificaciones, name='lista'),
    path('<int:pk>/detalles/', views.detalle_notificacion, name='detalle'),
    path('<int:pk>/actualizar/', views.actualizar_notificacion, name='actualizar'),
]
