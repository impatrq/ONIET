# Django Básico

Estructura de un proyecto de Django: [acá](https://developer.mozilla.org/es/docs/Learn/Server-side/Django/skeleton_website).

Estructura y vinculación de las URL's: [acá](https://tutorial.djangogirls.org/es/django_urls/).

Objeto HttpRequest (el parámetro que recibimos en la función de views.py): [acá](https://docs.djangoproject.com/en/3.2/ref/request-response/).

Crear proyecto de Django:
```django-admin startproject [nombre]```

Crear aplicación:
```python manage.py startapp [nombre]```

Correr servidor:
```python manage.py runserver```

Crear migraciones:
```python manage.py makemigrations```

Aplicar migraciones:
```python manage.py migrate```

Crear superusuario:
```python manage.py createsuperuser```

## Consigna

Crear un sistema web que cuente con 2 URL's:
- http://localhost:8000/hola
- http://localhost:8000/chau

La URL `/hola/` deberá imprimir en consola: `Hola!`.

La URL `/chau/` deberá imprimir en consola: `Chau!`.