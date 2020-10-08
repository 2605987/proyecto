from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Estudiantes,Nomina
from .forms import Estudiantesform, Nominaform

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

def crearPersona(request):
    if request.method == 'GET':
        form = Estudiantesform()
        contexto = {
            'form': form
        }
    else:
        form = Estudiantesform(request.POST)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('crear_persona')
    return render(request, 'crear_persona.html', contexto)

def editarPersona(request,id):
    estudiante = Estudiantes.objects.get(id=id)
    if request.method == 'GET':
        form = Estudiantesform(instance = estudiante)
        contexto = {
            'form': form
        }
    else:
        form = Estudiantesform(instance = estudiante)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('editar_estudiante')
    return render(request, 'editar_estudiante.html', contexto)




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

