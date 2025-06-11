from django import forms
from .models import Socio, Beneficio, CategoriaBeneficio

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ['nombre', 'email', 'beneficios']

class BeneficioForm(forms.ModelForm):
    class Meta:
        model = Beneficio
        fields = ['nombre', 'descripcion', 'categoria']

class CategoriaBeneficioForm(forms.ModelForm):
    class Meta:
        model = CategoriaBeneficio
        fields = ['nombre']  

class BusquedaBeneficiosForm(forms.Form):
    termino_busqueda = forms.CharField(
        label='Buscar beneficio por nombre o descripción',
        max_length=100,
        required=False
    )
    categoria = forms.ModelChoiceField(
        label='Filtrar por categoría',
        queryset=CategoriaBeneficio.objects.all(),
        required=False
    )
