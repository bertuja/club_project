from django.db import models

class CategoriaBeneficio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre

class Beneficio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey(CategoriaBeneficio, on_delete=models.CASCADE)
    proveedor = models.CharField(max_length=100)
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_expiracion = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.nombre} ({self.descuento}% descuento)"

class Socio(models.Model):
    dni = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    fecha_registro = models.DateField(auto_now_add=True)
    beneficios_favoritos = models.ManyToManyField(Beneficio, blank=True)
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"