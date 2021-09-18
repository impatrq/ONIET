from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

# * Estudiantes
# id, nombre, apellido y edad

# id, primary key, auto increment, unique, integer

class Estudiantes(models.Model):

    nombre = models.CharField('Nombre', max_length=64, null=False, blank=False)
    apellido = models.CharField('Apellido', max_length=64, null=False, blank=False)
    matricula = models.CharField('Matricula', max_length=4, default="YYYY")
    edad = models.IntegerField('Edad')

    class Meta:
        verbose_name_plural = 'Estudiantes'

    def estudiar(self):
        print(f"{self.nombre} esta estudiando.")

    def __str__(self):
        return f'{self.nombre} tiene {self.edad} años.'

class Notas(models.Model):

    estudiante = models.ManyToManyField(Estudiantes)
    math = models.DecimalField("Math", max_digits=4, decimal_places=2) # 8.50
    geo = models.DecimalField("Math", max_digits=4, decimal_places=2) # 8.50

    def __str__(self):
        return f"{len(self.estudiante.all())}"