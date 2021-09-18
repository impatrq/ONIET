from django.shortcuts import render
from .models import Estudiantes

# Create your views here.

def index(request):
    
    # * Crear y Modificar Objetos

    # estudiante = Estudiantes(nombre = "Lautaro", apellido = "Aubert", edad = 18)
    # estudiante.save()

    # estudiante = Estudiantes.objects.create(nombre = "Agustin", apellido = "Ronda", edad = 18)

    # estudiante.nombre = "Juanma"
    # estudiante.apellido = "Barreto"

    # * Borrar Objetos

    # estudiante.delete()

    # * Leer Objetos

    estudiantes = Estudiantes.objects.all()

    # print(estudiantes)

    # for estudiante in estudiantes[::-1]:
    #     print(estudiante.nombre)

    # lautaro = Estudiantes.objects.get(id=2)

    # print(lautaro.apellido)

    # lautaros = Estudiantes.objects.filter(nombre = "Lautaro")

    # for lautaro in lautaros:
    #     print(lautaro.apellido)

    # lautaro.delete()
    
    # estudiantes = Estudiantes.objects.filter(nombre__icontains = 'n')
    # estudiantes = Estudiantes.objects.filter(edad__gte = 18) # edad >= 18

    print(estudiantes)

    # * Primary Key
    # * Foreign Key

    return render(request, 'index.html', {'students': estudiantes})