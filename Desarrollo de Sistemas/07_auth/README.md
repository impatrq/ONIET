# Sistema de Autenticación de Django

Como sabemos, Django provee de un sistema de autenticación ya desarrollado que nos permite crear usuarios, iniciar y cerrar sesión en nuestra aplicación web. Para ello crea un modelo llamado `User`, que es el modelo que Django utiliza para personificar la entidad que se loguea.

Les dejo videos explicativos sobre el sistema de autenticación y referencias en la documentación oficial para que lean.

- https://youtu.be/tUqUdu0Sjyc
- https://www.youtube.com/watch?v=69Mb5yk-q8o
- https://www.youtube.com/watch?v=mOS0L5Lb2u0 & https://www.youtube.com/watch?v=meREllvata8
- https://docs.djangoproject.com/en/3.2/ref/contrib/auth/
- https://docs.djangoproject.com/en/3.2/topics/auth/
- https://docs.djangoproject.com/en/3.2/topics/auth/default/
- https://docs.djangoproject.com/en/3.2/topics/auth/passwords/

# Ejercicio

#### Realizar un sistema que le permita a los usuarios registrarse, iniciar y cerrar sesión además de poder tener un buscador para consultar datos del Covid 19 por país.

##### Aclaraciones

- La página del Login deberá tener una forma de direccionar al usuario a la página del Register y viceversa.
- La página principal que contiene el buscador solo se podrá acceder si el usuario está logueado.
- La página principal además deberá tener siempre un botón para cerrar sesión.
- El buscador se deberá basar en un campo de texto donde el usuario ingresará un país y al apretar un botón se le mostrará una página con los resultados de la búsqueda (Nuevos y Totales: Contagiados, Fallecidos y Recuperados)