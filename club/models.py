from django.db import models

class CategoriaBeneficio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)  # ← es opcional

    def __str__(self):
        return self.nombre

class Beneficio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey(CategoriaBeneficio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Socio(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    beneficios = models.ManyToManyField(Beneficio, blank=True)

    def __str__(self):
        return self.nombre
