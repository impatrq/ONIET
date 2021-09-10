# Modelos

Como ya vimos, Django se basa en el modelo de programación ORM, lo que nos permite interactuar con la base de datos de forma bastante simple utilizando Python como intermediario.

Para crear las tablas de nuestra base de datos, debemos crear clases en el archivo `models.py` de nuestra aplicación.

Ejemplo de tabla (mayormente llamado modelo):

```python
from django.db import models

class Persona(models.Model):

    nombre = models.CharField(max_length=64, null = True, blank = True)
    apellido = models.CharField(max_length=64, null = True, blank = True)
    edad = models.IntegerField()

    def respirar(self):
        print(f"{self.nombre} está respirando.")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
```

Para crear una tabla en nuestra base de datos mediante el ORM de Django, debemos crear una clase y establecer atributos que representarán las columnas.

Para crear atributos simplemente establecemos el nombre y le asignamos un tipo de dato (CharField para texto limitado, IntegerField para números, entre muchos [otros](https://docs.djangoproject.com/es/1.11/ref/models/fields/#field-types)). Además de asignar el tipo de datos, podemos configurar cualidades de ese campo o columna, como su longitud máxima, si puede ser nulo o si puede estar en blanco.

Documentación Oficial sobre Modelos: [acá](https://docs.djangoproject.com/en/3.2/topics/db/models/).

Documentación extra:

- https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Models
- https://www.youtube.com/watch?v=HDz6lqZ91rE
- https://asociacionaepi.es/los-modelos-de-django/
- https://medium.com/@devsar/modelos-en-django-381530c5fc3c