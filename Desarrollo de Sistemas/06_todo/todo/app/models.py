from django.db import models

# Create your models here.

class Persona(models.Model):

    nombre = models.CharField('Nombre de la Persona', max_length=64, blank=False, null=False)
    apellido = models.CharField('Nombre de la Persona', max_length=64, blank=False, null=False)

    def hablar(self):
        print(f"{self.nombre} esta hablando.")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"