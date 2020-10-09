"""APPpractica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

from aplicaciones.principal import views

urlpatterns = [
    path('',views.inicio,name = 'inicio'),
    path('crear_persona/',views.crearPersona,name = 'crear_persona'),
    path('editar_estudiante/<int:id>/',views.editarPersona,name = 'editar_estudiante'),
    path('acerca_de/',views.about,name = 'acerca_de'),
    path('himno/',views.himno,name = 'himno'),
    path('ubicacion/',views.ubicacion,name = 'ubicacion'),
    path('nomina/',views.nomina,name = 'nomina'),
    path('eventos/',views.eventos,name = 'eventos'),
    path('galeria/',views.galeria,name = 'galeria'),
    path('crear_docente/',views.crearDocente,name = 'crear_docente'),
    path('editar_docente/<int:id>/',views.editarDocente, name= 'editar_docente' ),
    path('eliminar_docente/<int:id>/',views.eliminarDocente, name= 'eliminar_docente' ),
    path('eventos/', include('eventos.urls'),name="eventos"),
    path('usuarios/',include('usuarios.urls'),name="usuarios"),
    path('admin/', admin.site.urls),


]