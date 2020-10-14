from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Estudiantes,Nomina
from .forms import Estudiantesform, Nominaform
from django.db.models import Q

def base(request):
    return render(request, 'base.html', {'menu': True})

def inicio(request, plantilla='inicio.html'):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, plantilla)
    # En otro caso redireccionamos al login
    return redirect('login')





def estudiantes(request):
    estudiante = Estudiantes.objects.all()
    contexto = {
        'estudiantes':estudiantes
    }
    return render(request, 'crear_persona.html', contexto)

def crearPersona(request,plantilla="crear_persona.html"):
    if request.method == "POST":
        form = Estudiantesform((request.POST or None))
        if form.is_valid():
            form.save()
            return redirect("consultar-estudiantes")
    else:
        form = Estudiantesform

    return render(request, plantilla, {'form': form})

def editarPersona(request,pk,plantilla="editar_estudiante.html"):
    if request.method == "POST":
        estudiantes = get_object_or_404(Estudiantes, pk=pk)
        form = Estudiantesform(request.POST or None, instance=estudiantes)
        if form.is_valid():
            form.save()
        return redirect('consultar-estudiantes')
    else:
        estudiantes= get_object_or_404(Estudiantes, pk=pk)
        form = Estudiantesform(request.POST or None, instance=estudiantes)

    return render(request, plantilla, {'form': form})

def consultarestudiantes(request):
    buscar = request.GET.get("buscar")
    estudiantes = Estudiantes.objects.all()
    if buscar:
        estudiantes = Estudiantes.objects.filter(
            Q(nombres__icontains=buscar) |
            Q(apellidos__icontains=buscar) |
            Q(cedula__icontains=buscar)
        ).distinct()
    return render(request, 'consultar-estudiantes.html', {'estudiantes': estudiantes})

def eliminarestudiantes(request, pk, plantilla="eliminar-estudiantes.html"):

    if request.method == "POST":
        form = Estudiantesform((request.POST or None))
        estudiantes = get_object_or_404(Estudiantes, pk=pk)
        if form.is_valid():
            estudiantes.delete()
            return redirect('consultar-estudiantes')
    else:
        estudiantes= get_object_or_404(Estudiantes, pk=pk)
        form = Estudiantesform(request.POST or None, instance=estudiantes)

    return render(request, plantilla, {'form': form})




def about(request):
    return render(request, 'acerca_de.html')






def himno(request):
    return render(request, 'himno.html')






def ubicacion(request):
    return render(request, 'ubicacion.html')





#crud
def nomina(request):
    nomina = Nomina.objects.all()
    contexto = {
        'nomina':nomina
    }
    return render(request,'nomina.html', contexto)


def crearDocente(request):
    if request.method == 'GET':
       form = Nominaform()
       contexto = {
           'form': form
       }
    else:
        form = Nominaform(request.POST)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('nomina')
    return render(request,'crear_docente.html',contexto)

def editarDocente(request,id):
    nomina=Nomina.objects.get(id=id)
    if request.method == 'GET': 
        form = Nominaform(instance = nomina)
        contexto = {
            'form':form
        }
    else:
        form = Nominaform( request.POST, instance = nomina)
        conexto = {
            'form':form
        }
        if form.is_valid:
            form.save()
            return redirect('nomina')
    return render(request,'crear_docente.html',contexto)


def eliminarDocente(request, id):
    nomina = Nomina.objects.get(id=id)
    nomina.delete()
    return redirect('nomina')



#crud
def eventos(request):
    return render(request,'eventos.html')






def galeria(request):
    return render(request,'galeria.html')

