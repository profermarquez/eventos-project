from django.shortcuts import render
from notificaciones.models import Notificacion
from eventos.models import Evento
from django.contrib.auth.decorators import login_required

def enviar_notificaciones(evento_id):
    evento = Evento.objects.get(id=evento_id)
    autoridades = matching_autoridades(evento_id)
    for autoridad in autoridades:
        Notificacion.objects.create(evento=evento, autoridad=autoridad, estado='pendiente')

# notificaciones/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Notificacion
from .forms import NotificacionForm

@login_required
def lista_notificaciones(request):
    notificaciones = Notificacion.objects.all()
    return render(request, 'notificaciones/lista_notificaciones.html', {'notificaciones': notificaciones})

@login_required
def detalle_notificacion(request, pk):
    notificacion = get_object_or_404(Notificacion, pk=pk)
    return render(request, 'notificaciones/detalle_notificacion.html', {'notificacion': notificacion})

@login_required
def actualizar_notificacion(request, pk):
    notificacion = get_object_or_404(Notificacion, pk=pk)
    if request.method == 'POST':
        form = NotificacionForm(request.POST, instance=notificacion)
        if form.is_valid():
            form.save()
            return redirect('notificaciones:lista')
    else:
        form = NotificacionForm(instance=notificacion)
    return render(request, 'notificaciones/formulario_notificacion.html', {'form': form, 'titulo': 'Actualizar Notificación'})
