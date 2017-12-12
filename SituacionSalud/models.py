from django.db import models

# Create your models here.


class prueba(models.Model):
    codigo = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=210)

    def __str__(self):
        return self.codigo

class EstablecimientoSalud(models.Model):
    codigo = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=210)

    def __str__(self):
        return self.codigo

class Distrito(models.Model):
    nombre = models.CharField(max_length=210)

    def __str__(self):
        return self.nombre

class Seguro(models.Model):
    nombre = models.CharField(max_length=210)

    def __str__(self):
        return self.nombre

class Cie(models.Model):
    codigo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=210)

    def __str__(self):
        return self.codigo

class Sexo(models.Model):
    nombre = models.CharField(max_length=210)

    def __str__(self):
        return self.nombre

class NivelEconomico(models.Model):
    nombre = models.CharField(max_length=210)

    def __str__(self):
        return self.nombre


class Zona(models.Model):
    nombre = models.CharField(max_length=210)

    def __str__(self):
        return self.nombre

class SituacionSalud(models.Model):
    edad = models.IntegerField(blank=True, null=True)
    sexo = models.ForeignKey(Sexo)
    distrito = models.ForeignKey(Distrito)
    cie = models.ForeignKey(Cie)
    seguro = models.ForeignKey(Seguro)
    niveleconomico = models.ForeignKey(NivelEconomico)
    zona = models.ForeignKey(Zona)
    eess = models.ForeignKey(EstablecimientoSalud)


    def __str__(self):
        return self.edad