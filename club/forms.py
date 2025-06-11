from django import forms
from .models import Socio, Beneficio, CategoriaBeneficio

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ['dni', 'nombre', 'apellido', 'email', 'telefono']
        widgets = {
            'fecha_registro': forms.DateInput(attrs={'type': 'date'}),
        }

class BeneficioForm(forms.ModelForm):
    class Meta:
        model = Beneficio
        fields = ['nombre', 'descripcion', 'categoria', 'proveedor', 'descuento', 'fecha_expiracion']
        widgets = {
            'fecha_expiracion': forms.DateInput(attrs={'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

class CategoriaBeneficioForm(forms.ModelForm):
    class Meta:
        model = CategoriaBeneficio
        fields = ['nombre', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

class BusquedaBeneficiosForm(forms.Form):
    termino_busqueda = forms.CharField(
        label='Buscar beneficios', 
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre o descripción'})
    )
    
    categoria = forms.ModelChoiceField(
        queryset=CategoriaBeneficio.objects.all(),
        required=False,
        label='Filtrar por categoría',
        empty_label='Todas las categorías'
    )