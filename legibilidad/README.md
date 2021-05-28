# Legibilidad

## Consigna

Diseñar un algoritmo que calcule el nivel de lectura de un texto ingresado como input. El programa debe:

- Tomar como entrada el texto a analizar.
- Imprimir el indice de legibilidad de la frase.

Para calcular este nivel de complejidad se usará esta formula:
``` python
    indice = 0.0588 * L - 0.296 * S - 15.8 
```
Donde `L` es el número promedio de letras por cada 100 palabras en el texto y `S` es el número promedio de oraciones por cada 100 palabras en el texto. 
### Aclaraciones
- **NO** se considera como ***letra*** a los signos de puntuación, dígitos u otros símbolos.
- Se considera como ***palabra*** a cualquier secuencia de caracteres separados por un espacio.
- Se considera como ***oración*** a cualquier secuencia de caracteres que termina con un punto, signo de exclamación o un signo de interrogación.
- Ignorar casos en que los puntos o signos de exclamación/interrogación no signifiquen el final de una oración. Ejemplo:
    ```
    Que buena película Sr. y Sra. Smith.
    ```
    En este caso, se considera como correcto que el programa encuentre 3 oraciones.
- A la hora de mostrar la resultante, se deberá indicar el grado siempre rendondeando hacia el entero más cercano, ej: `Grado 5`. Cuando el grado sea menor a 1, deberá aparecer `Grado menor a 1` y si es mayor o igual a 16 deberá mostrar `Grado 16+`.
## Ejemplo

```
$ python legibilidad.py
Texto: Harry Potter era un chico muy inusual en muchos sentidos. Por un lado, odiaba las vacaciones de verano más que cualquier otra época del año. Por otro lado, realmente quería hacer su tarea, pero se vio obligado a hacerlo en secreto, en la oscuridad de la noche. Y también resultó ser un mago.

Letras: 231
Palabras: 53
Oraciones: 4

L = 435.8490566037736
S = 7.547169811320755

Grado 8
```
## Test
- `One fish. Two fish. Red fish. Blue fish.` (Grado menor a 1)
- `Would you like them here or there? I would not like them here or there. I would not like them anywhere.` (Grado 2)
- `In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.` (Grado 7)
- `A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.` (Grado 16+)
## Consideraciones

Para que la resolución forme parte del repositorio:   

- El programa debe estar apropiadamente comentado.
- Los comentarios deben ser en linea (`#`).
- Funciones propias deben ser documentadas con un `docstring`.
- Guardar el archivo como `legibilidad_autor.py`
