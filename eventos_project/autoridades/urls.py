from django.urls import path
from . import views

app_name = 'autoridades'

urlpatterns = [
    path('', views.lista_autoridades, name='lista'),
    path('crear/', views.crear_autoridad, name='crear'),
    path('<int:pk>/editar/', views.editar_autoridad, name='editar'),
    path('<int:pk>/eliminar/', views.eliminar_autoridad, name='eliminar'),
]
