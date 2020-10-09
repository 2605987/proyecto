from django.db import models

# Create your models here.
class Eventos (models.Model):
    dia_evento = models.CharField('DIA DEL EVENTO', max_length=100)
    hora_evento = models.CharField('HORA DEL EVENTO', max_length=100)
    tipo_evento = models.CharField('TIPO DE EVENTO', max_length=100)
    numero_invitados= models.CharField('CAPACIDAD', max_length=100)
    #user = models.CharField(max_length=15)
    #usermod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "eventos"
        verbose_name = "evento"
        verbose_name_plural = "eventos"

    def _str_(self):
        return self.dia_evento + ' ' + self.tipo_evento
