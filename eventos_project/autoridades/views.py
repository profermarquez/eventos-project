# autoridades/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Autoridad
from .forms import AutoridadForm

@login_required
def lista_autoridades(request):
    autoridades = Autoridad.objects.all()
    return render(request, 'autoridades/lista_autoridades.html', {'autoridades': autoridades})

@login_required
def crear_autoridad(request):
    if request.method == 'POST':
        form = AutoridadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autoridades:lista')
    else:
        form = AutoridadForm()
    return render(request, 'autoridades/formulario_autoridad.html', {'form': form, 'titulo': 'Crear Autoridad'})

def editar_autoridad(request, pk):
    autoridad = get_object_or_404(Autoridad, pk=pk)
    if request.method == 'POST':
        form = AutoridadForm(request.POST, instance=autoridad)
        if form.is_valid():
            form.save()
            return redirect('autoridades:lista')
    else:
        form = AutoridadForm(instance=autoridad)
    return render(request, 'autoridades/formulario_autoridad.html', {'form': form, 'titulo': 'Editar Autoridad'})

def eliminar_autoridad(request, pk):
    autoridad = get_object_or_404(Autoridad, pk=pk)
    if request.method == 'POST':
        autoridad.delete()
        return redirect('autoridades:lista')
    return render(request, 'autoridades/confirmar_eliminar.html', {'autoridad': autoridad})
