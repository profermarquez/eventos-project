from django.urls import path
from .views import LandingPageView, RegistroView, LoginUsuarioView, LogoutUsuarioView

app_name = 'autenticacion'

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('login/', LoginUsuarioView.as_view(), name='login'),
    path('logout/', LogoutUsuarioView.as_view(), name='logout'),
]
