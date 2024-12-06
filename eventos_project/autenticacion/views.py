from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm

# Landing page
class LandingPageView(TemplateView):
    template_name = 'autenticacion/landing.html'

# Vista de registro
class RegistroView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'autenticacion/registro.html'
    success_url = reverse_lazy('autenticacion:login')  # Redirigir al login después del registro

# Vista de inicio de sesión
class LoginUsuarioView(LoginView):
    template_name = 'autenticacion/login.html'

# Vista de cierre de sesión (sin necesidad de redefinir LogoutView)
class LogoutUsuarioView(LogoutView):
    next_page = reverse_lazy('autenticacion:landing_page')  # Redirigir al landing page después del logout
