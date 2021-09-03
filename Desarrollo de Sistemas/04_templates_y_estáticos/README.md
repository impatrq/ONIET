# Templates en Django

### ¿Que son los templates?

Un template es un archivo de texto, el cual contiene tags y variables. Las variables son reemplazadas por valores que nosotros definimos, y los tags nos ayudan a controlar la lógica del template.

Mediante el uso de templates en Django y su motor de renderizado vamos a poder aplicar lógica en nuestros archivos HTML, CSV y JSON. En nuestro caso nos vamos a centrar en HTML y las distintas etiquetas que el motor de templates de Django nos provee.

### Extender un template base

Cuando tenemos un HTML que queremos extender para usarlo como padre (un HTML que comparte particularidades con otros), podemos hacer uso de la etiqueta `{% extends "" %}`. Haciendo uso de esta etiqueta, definimos que nuestro HTML que contiene la misma es un HTML hijo del archivo base.

Ejemplo: 

base.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML Base</title>
</head>
<body>

    <h1>Este es un titulo de la base</h1>

    
    {% block content %}
        
    {% endblock content %}
        

</body>
</html>
```

hijo.html
```html
{% extends 'base.html' %}


{% block content %}
    <h1>Este es un titulo del hijo</h1>
{% endblock content %} 
```

### Uso de variables

Cuando al renderizar nuestro HTML le pasamos variables por el contexto las podemos utilizar mediante las etiquetas de variable: `{{ nombre_variable }}`.

Ejemplo:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejemplo Variables</title>
</head>
<body>
    
    <h1>{{ titulo }}</h1>

</body>
</html>
```

El String almacenado en `titulo` será el texto mostrado por medio de la etiqueta HTML h1.

### Condicionales

Podemos utilizar condicionales en nuestro template mediante el uso de la etiqueta `{% if condicion %}  {% else %}  {% endif %}`.

Ejemplo:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Condicionales</title>
</head>
<body>
    
    
    {% if numero == 3 %}
        <h1>El numero es 3</h1>    
    {% else %}
        <h1>El numero no es 3</h1>
    {% endif %}
        

</body>
</html>
```

### Bucles

Podemos utilizar los bucles que conocemos al igual que los condicionales utilizando la etiqueta: `{% for elemento in lista_elementos %} {% endfor %}`.

Ejemplo:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bucles</title>
</head>
<body>
    
    
    {% for numero in lista_numeros %}
        <h1>Numero: {{ numero }}</h1>
    {% endfor %}
        

</body>
</html>
```

### Bloques de contenido

Como vimos anteriormente en la extensión de templates base, utilizamos la etiqueta `{% block nombre %} {% endblock nombre %}` para determinar areas variables en nuestra base. El `nombre` puede ser cualquiera que elijamos y el contenido que pongamos ahi dentro es lo que se reflejará en el archivo base.

# Archivos Estáticos

### ¿Que son los archivos estáticos?

Llamamos archivos estáticos a los archivos que utilizamos en nuestra web pero siempre son fijos y no variables. Ejemplos de estos archivos son las imágenes, videos, archivos CSS, JS, entre otros.

Django tiene la particularidad que permite, mediante su motor de templates, manejar las direcciones de nuestros archivos estáticos.

Por ejemplo, si queremos importar nuestro `main.css` y su ubicación es `/assets/css/main.css`, deberíamos hacer lo siguiente:

settings.py
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'assets',
]
```

De esta forma, establecemos que la URL de nuestros archivos estáticos en el servidor será http://localhost:8000/static/ y que la ruta para encontrar esos archivos es la carpeta `assets` en el directorio base de nuestro proyecto.

En el template:

```html
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Archivos estáticos</title>

    <link rel="stylesheet" href="{% static 'css/main.css' %}">

</head>
<body>

</body>
</html>
```

Es importante que no se olviden de cargar los archivos estáticos con la etiqueta `{% load static %}`.