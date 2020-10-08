from django.db import models


class Estudiantes(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.IntegerField(default=0)
    def __str__(self):
        return self.nombres

class DPsEstudiante(models.Model):
    id = models.AutoField(primary_key=True)
    nombres_representante = models.CharField(max_length=100)
    cedula_representante = models.IntegerField(default=0)
    numero_celular_representante = models.IntegerField(default=0)
    nombre_apellidos_padre = models.CharField(max_length=300)
    cedula_padre = models.IntegerField(default=0)
    numero_celular_padre = models.IntegerField(default=0)
    ocupacion_padre = models.CharField(max_length=100)
    nombre_apellidos_materno = models.CharField(max_length=300)
    cedula_madre = models.IntegerField(default=0)
    numero_celular_madre = models.IntegerField(default=0)
    ocupacion_madre = models.CharField(max_length=100)

class Materia(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad_alumno = models.IntegerField(default=0)
    nombres_materias = models.CharField(max_length=250)

class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    octavo = models.IntegerField(default=0)
    noveno = models.IntegerField(default=0)
    decimo = models.IntegerField(default=0)
    p_bachillerato = models.IntegerField(default=0)
    s_bachillerato = models.IntegerField(default=0)
    t_bachillerato = models.IntegerField(default=0)

class Nomina(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_docente = models.CharField(max_length=100)
    apellidos_docente = models.CharField(max_length=100)
    materia_impartida = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_docente

class Evento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_evento = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    hora = models.DateTimeField(auto_now_add=True)
    lugar = models.CharField(max_length=200)

#class Calificacion
#class MateriaNomina
