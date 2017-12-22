from django.db import models


# Create your models here.


class prueba(models.Model):
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
    codigo = models.CharField(max_length=50, primary_key=True)
    descripcion = models.CharField(max_length=210)

    def __str__(self):
        return self.codigo

    class Meta:
        ordering = ['codigo']


class EstablecimientoSalud(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=210)

    def __str__(self):
        return str(self.descripcion)


class Sexo(models.Model):
    nombre = models.CharField(max_length=210)
    abreviacion = models.CharField(max_length=5, null=True, blank=True)

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


class Edad(models.Model):
    tipo = models.CharField(max_length=2)
    edad = models.IntegerField()
    nomenclaturar = models.CharField(max_length=15)

    def __str__(self):
        return str(self.edad)


class SituacionSalud(models.Model):
    edad = models.ForeignKey(Edad, null=True, blank=True)
    sexo = models.ForeignKey(Sexo, null=True, blank=True)
    # sexoden = models.CharField(max_length=20,  null=True)
    distrito = models.ForeignKey(Distrito, null=True, blank=True)
    # distritoden = models.CharField(max_length=100,  null=True)
    cie = models.ForeignKey(Cie, null=True, blank=True)
    seguro = models.ForeignKey(Seguro, null=True, blank=True)
    niveleconomico = models.ForeignKey(NivelEconomico, null=True, blank=True)
    zona = models.ForeignKey(Zona, null=True, blank=True)
    eess = models.ForeignKey(EstablecimientoSalud, null=True, blank=True)

    def __str__(self):
        return str(self.edad.edad)


class TipoGrupoEnf2(models.Model):
    denominacion = models.CharField(max_length=210, null=True, blank=True)

    def __str__(self):
        return self.denominacion


class Gruponenf2(models.Model):
    denominacion = models.CharField(max_length=210, null=True, blank=True)
    tipogrupoes = models.ForeignKey(TipoGrupoEnf2)
    ciee = models.ManyToManyField(Cie)

    def __str__(self):
        return self.denominacion + " - " + str(self.tipogrupoes.denominacion)


class RangoEdad(models.Model):
    rango = models.CharField(max_length=210, null=True, blank=True)
    cantidad = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.rango


class Poblacion(models.Model):
    anio = models.IntegerField(null=True, blank=True)
    pobtotal = models.IntegerField(null=True, blank=True)
    pobmujer = models.IntegerField(null=True, blank=True)
    pobvaron = models.IntegerField(null=True, blank=True)
    nacimiento = models.IntegerField(null=True, blank=True)
    muerte = models.IntegerField(null=True, blank=True)
    rangoedad = models.ManyToManyField(RangoEdad)

    def __str__(self):
        return " - "
