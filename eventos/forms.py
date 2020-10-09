from django import forms
from .models import Eventos








class EventosForm(forms.ModelForm):
    class Meta:
        model= Eventos
        fields=['dia_evento', 'hora_evento', 'tipo_evento', 'numero_invitados']

