from django.shortcuts import render, redirect
from .models import Socio, Beneficio, CategoriaBeneficio
from .forms import SocioForm, BeneficioForm, CategoriaBeneficioForm, BusquedaBeneficiosForm

def home(request):
    beneficios = Beneficio.objects.all()
    return render(request, 'club/home.html', {'beneficios': beneficios})


def registrar_socio(request):
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_beneficios')
    else:
        form = SocioForm()
    return render(request, 'club/registrar_socio.html', {'form': form})

def agregar_beneficio(request):
    if request.method == 'POST':
        form = BeneficioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_beneficios')
    else:
        form = BeneficioForm()
    return render(request, 'club/agregar_beneficio.html', {'form': form})

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaBeneficioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoriaBeneficioForm()
    return render(request, 'club/agregar_categoria.html', {'form': form})

def lista_beneficios(request):
    beneficios = Beneficio.objects.all()
    form = BusquedaBeneficiosForm(request.GET or None)
    
    if form.is_valid():
        termino = form.cleaned_data.get('termino_busqueda')
        categoria = form.cleaned_data.get('categoria')
        
        if termino:
            beneficios = beneficios.filter(
                models.Q(nombre__icontains=termino) | 
                models.Q(descripcion__icontains=termino)
            )
        if categoria:
            beneficios = beneficios.filter(categoria=categoria)
    
    return render(request, 'club/lista_beneficios.html', {
        'beneficios': beneficios,
        'form': form
    })

def detalle_beneficio(request, pk):
    beneficio = Beneficio.objects.get(pk=pk)
    return render(request, 'club/detalle_beneficio.html', {'beneficio': beneficio})