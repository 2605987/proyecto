from django import forms
from .models import Estudiantes
from .models import Nomina

class Estudiantesform(forms.ModelForm):
    class Meta:
        model = Estudiantes
        fields = '__all__'

class Nominaform(forms.ModelForm):
    class Meta:
        model = Nomina
        fields = '__all__'
