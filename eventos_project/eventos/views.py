# eventos/views.py
from .models import Evento
from autoridades.models import Autoridad
from django.contrib.auth.decorators import login_required

def matching_autoridades(evento_id):
    evento = Evento.objects.get(id=evento_id)
    autoridades = Autoridad.objects.filter(campo_accion__icontains=evento.tematica)
    return autoridades

from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento
from .forms import EventoForm

@login_required
def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})

@login_required
def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eventos:lista')
    else:
        form = EventoForm()
    return render(request, 'eventos/formulario_evento.html', {'form': form, 'titulo': 'Crear Evento'})

@login_required
def editar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('eventos:lista')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventos/formulario_evento.html', {'form': form, 'titulo': 'Editar Evento'})

@login_required
def eliminar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        evento.delete()
        return redirect('eventos:lista')
    return render(request, 'eventos/confirmar_eliminar.html', {'evento': evento})
