from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import *
from .models import *

# Create your views here.
def consultareventos(request, plantilla="consultareventos.html"):
    eventos = Eventos.objects.all()
    data = {
        'eventos':eventos
    }
    return render(request, plantilla, data)


#pagina de crear o insertar INSERT
def creareventos(request, plantilla="creareventos.html"):

    if request.method == "POST":
        form = EventosForm((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect('consultareventos')
    else:
        form = EventosForm

    return render(request, plantilla, {'form': form})

#pagina de modificar
def modificareventos(request, pk, plantilla="modificareventos.html"):
    if request.method == "POST":
        eventos = get_object_or_404(Eventos, pk=pk)
        form = EventosForm(request.POST or None, instance=eventos)
        if form.is_valid():
            form.save()
        return redirect('consultareventos')
    else:
        eventos = get_object_or_404(Eventos, pk=pk)
        form = EventosForm(request.POST or None, instance=eventos)



    return render(request, plantilla, {'form': form})


#pagina de eliminar
def eliminareventos(request, pk, plantilla="eliminareventos.html"):

    if request.method == "POST":
        form = EventosForm((request.POST or None))
        eventos = get_object_or_404(Eventos, pk=pk)
        if form.is_valid():
            eventos.delete()
            return redirect('consultareventos')
    else:
        eventos= get_object_or_404(Eventos, pk=pk)
        form = EventosForm(request.POST or None, instance=eventos)

    return render(request, plantilla, {'form': form})