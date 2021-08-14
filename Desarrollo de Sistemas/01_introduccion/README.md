# Desarrollo de Sistemas

### Introducción

La competencia Desarrollo de Sistemas se basa en la realización de un algoritmo de lectura, procesamiento, almacenamiento y representación visual de datos mediante el uso de algunos de los siguientes lenguajes de programación:

- JAVA
- JavaScript
- PHP
- Python
- .NET framework/.NET core (VB,C#,C++) 

La actividad se resuelve en equipos de máximo 3 personas en un tiempo de 3 horas, incluyendo la presentación del problema y su desarrollo. La entrega se realiza por medio de un sistema de control de versiones (git) en cualquier servicio web como GitHub, GitLab, etc.

Información completa [acá](http://oniet.ubp.edu.ar/wp-content/uploads/2020/10/01-01-desarrollo-de-sistemas-reglamento-2020-v3-n.pdf).

### ¿Que vamos a ver?

Si bien hay una gran variedad de lenguajes y tecnologías para elegir, nuestro lenguaje preferido para esta competencia es Python. Esto no significa que estén obligados a cerrarse a este lenguaje, son libres de elegir el que más les guste y con el que más cómodos se sientan.

Aprovechando que durante gran parte del año estuvimos aprendiendo Python, para esta competencia vamos a utilizarlo junto a un Framework llamado Django.

### ¿Qué es un framework?

Según [www.seoestudios.es](https://www.seoestudios.es/blog/que-es-un-framework/#:~:text=Un%20framework%20es%20un%20entorno,un%20producto%20de%20mayor%20calidad.), un framework es un entorno de trabajo que tiene como objetivo facilitar la labor de programación ofreciendo una serie de características y funciones que aceleran el proceso, reducen los errores, favorecen el trabajo colaborativo y consiguen obtener un producto de mayor calidad.

Los framework ofrecen una estructura para el desarrollo y no tienen que estar sujetos a un único lenguaje de programación, aunque es habitual encontrar en el mercado, distintos frameworks específicos para un lenguaje concreto.

Los desarrolladores pueden crear una web o un programa sin la necesidad de utilizar un framework, sobre todo en el caso de pequeños proyectos. Sin embargo, cuando dicho proyecto va creciendo en complejidad se necesitará una organización, seguir unas pautas, desarrollar código fácil de entender por otros desarrolladores, y otros aspectos que harán necesario el uso de un framework.

Ahora, en criollo, es como una caja de herramientas para un lenguaje de programación que nos permite utilizar complementos ya desarrollados para que nuestra aplicación/programa tenga muchas más características sin tener que desarrollarlas nosotros mismos.

Como uno de los requisitos de la competencia es que se resuelva el problema mediante un Sistema Web, el Framework que combina Python y Desarrollo Web es Django.

### ¿Qué es Django?

Django es un framework web escrito en Python que ofrece una gran variedad de componentes y servicios listos para utilizar en nuestro sistema.

Algunos ejemplos de los servicios y características más útiles que ofrece Django son:

- Su fácil manejo de peticiones web mediante url's y funciones
- Su motor de plantillas web y manejo de archivos estáticos
- Su sistema de autenticación de usuarios (el típico Register, Login y Logout que ven en las páginas web)
- Su fácil forma de almacenar datos en Bases de Datos Relacionales (SQL) mediante el modelo de programación ORM.

Con Django vamos a ser capaces de migrar todo este conocimiento sobre resolución de problemas y bases de datos al ámbito web con muchos más componentes para enriquecer nuestro programa (ahora llamado 'sistema web').

### Por último, ¿Que es ORM?

ORM es un modelo de programación que permite mapear las estructuras de una base de datos relacional sobre una estructura lógica de entidades con el objeto de simplificar y acelerar el desarrollo de nuestras aplicaciones.

Las estructuras de la base de datos relacional quedan vinculadas con las entidades lógicas o base de datos virtual definida en el ORM, de tal modo que las acciones CRUD (Create, Read, Update, Delete) a ejecutar sobre la base de datos física se realizan de forma indirecta por medio del ORM.

Ya se, suena bastante complejo, pero quedense tranquilos que los desarrolladores de Django ya se encargaron de facilitarnos el trabajo.

Resumiendo el concepto de ORM, es un modelo de programación que nos permite utilizar clases como si fuesen tablas de nuestra base de datos, logrando crear y modelar una base de datos sin necesidad de escribir ni una linea de SQL.

[Explicación ampliada sobre ORM](https://programarfacil.com/blog/que-es-un-orm/)

---

Sientanse libres de buscar en internet toda la información sobre Django que requieran y si quieren avanzar más rápido les dejo un curso [acá](https://www.youtube.com/watch?v=7XO1AzwkPPE&list=PLU8oAlHdN5BmfvwxFO7HdPciOCmmYneAB) y la documentación oficial de Django [acá](https://docs.djangoproject.com/en/3.2/).