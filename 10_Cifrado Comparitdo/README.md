# Cifrado Compartido(POO) :key: :busts_in_silhouette:
 Prometo que es la última vez que reutilizamos este ejercicio. :wink:
## Consigna

Usando la clase del ejercicio [Cifrado 3.0](https://github.com/trq20/ONIET/tree/master/05_cifrado%202.0) creado por su compa, diseñar un algoritmo que pueda cifrar con varias Keys distintas varias veces un determiando `.txt`. 
El programa debe importar esta nueva clase y usar sus funciones.
- El programa debe pedir como argumento:
  - Si va a cifrar o descifrar (Comandos: -c // -d)
  - La dirección del archivo `.txt`.
  - La cantidad de Keys a usar (Solo para -c).
  - La cantidad de veces que va a cifrar por Key (Solo para -c).


## Aclaraciones

- A la hora de cifrar, el programa debe guardar dentro del archivo los parámetros necesarios para poder descifrarlo.
- Cuando el programa descifre debe ir a buscar los parámetros mencionados anteriormente.
- En ambos casos crear un nuevo archivo con el contenido obtenido. El formato del nombre debe ser de la siguiente manera: `$NOMBRE_ANTERIOR-C` (`-D` en el caso de Descifrar)

## Bonus 	:star:
> ***Aclaración**: Los ejercios base, poseen todos los contenidos necesarios para competir. Los bonus son solo para los que quieran praticar más.*

El programa debe tomar, de un archivo llamado `keys.txt`, las keys a utilizar en caso de que exista. Si la cantidad de keys pedida es mayor a las que se encuentran en el archivo, deberá generar las restantes. El programa **NO** debe modificar ese archivo.
## Consideraciones

Para que la resolución forme parte del repositorio:   

- El programa debe estar apropiadamente comentado.
- Los comentarios deben ser en linea (`#`).
- Funciones propias deben ser documentadas con un `docstring`.
- Guardar el archivo como `Cifrado Compartido_autor.py`
