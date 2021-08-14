# Tarjetas y CSV :credit_card:

## Consigna

Diseñar un algoritmo que interprete códigos de tarjetas de crédito y pueda identificar a que red bancaria pertenecen. El programa debe:

- Tomar los códigos de las tarjetas de un archivo `tarjetas.csv`.
- Verificar la validez de las tarjetas usando el **Algoritmo de Luhn**.
- Identificar a que **red bancaria** pertenecen.
- Reescribir el archivo `tarjetas.csv` agregando la red de cada una de las tarjetas.
- Imprimir un mensaje de confirmación.

Los archivos estarán guardados de la siguente manera:
``` text
    │
    ├── data/
    │   └── tarjetas.csv
    │
    ├── README.md
    └── credit.py
```
### Algoritmo de Luhn

Según el algoritmo de Luhn, se puede determinar si un número de tarjeta de crédito es (sintácticamente) válido de la siguiente manera:
- Multiplica cada dos dígitos por 2, comenzando con el penúltimo dígito del número y luego suma los dígitos de esos productos.
- Suma a ese resultado los dígitos que no se multiplicaron por 2.
- Si el último dígito del total es 0 (o, dicho de manera más formal, si el total es divido por 10 y el resto es igual 0), ¡el número es válido!
<pre>
Como ejemplo se usa una tarjeta VISA: <b>4003600000000014</b>

    Se subraya cada dos dígitos, comenzando con el penúltimo dígito del número:
      <b>4</b> 0</b> <b>0</b> 3 <b>6</b> 0 <b>0</b> 0 <b>0</b> 0 <b>0</b> 0 <b>0</b> 0 <b>1</b> 4
      <b>^   ^   ^   ^   ^   ^   ^   ^</b>   
    Multiplicar cada uno de los dígitos subrayados por 2:
      1 • 2 + 0 • 2 + 0 • 2 + 0 • 2 + 0 • 2 + 6 • 2 + 0 • 2 + 4 • 2

      2 + 0 + 0 + 0 + 0 + 12 + 0 + 8

    Sumar los digitos de esos produtos, <b>NO</b> los prodcutos en sí:

      2 + 0 + 0 + 0 + 0 + 1 + 2 + 0 + 8 = 13
                          ^   ^
    Al resultado obtenido se le suma los digitos que no fueron seleccionados en el primer paso:

      <b>13</b> + 4 + 0 + 0 + 0 + 0 + 0 + 3 + 0 = 20
    
    Si el último dígito de esa suma (20) es un 0, la tarjeta es completamente válida.

</pre>

### ¿Y la red bancaria?
Luego se validar la tajeta con el algoritmo de Luhn, se tendrá que determinar que red utiliza cada tarjeta siguiendo la siguente tabla:
|        Red       |    Comienza con    |  Largo |
|:----------------:|:------------------:|:------:|
|       VISA       |          4         | 13 ,16 |
|    MASTERCARD    | 51, 52, 53, 54, 55 |   16   |
| AMERICAN EXPRESS |       34, 37       |   15   |


### Aclaraciones

- Tanto si el código de la tajeta no pasa el algoritmo de Luhn o no coincide con las condiciones de la tabla de red deberá escribirse `INVÁLIDA` en el `.csv`. Ej:
  ```text
    TARJETA,RED
    XXXXXXXXXXXXXXXXX,INVÁLIDA
  ```
- El archivo `tarjetas.csv`, con las tarjetas que deben utilizar, lo encuentran en la carpeta data de este repositorio.

## Ejemplo

```text
    $ python credit.py
    
    El archivo tarjetas.csv ha sido modificado correctamente.
```
| csv Antes | csv Después |
|:-:|:-:|
| TARJETA,RED | TARJETA,RED |
| XXXXXXXXXXXXXXX, | XXXXXXXXXXXXXXX,VISA |
| XXXXXXXXXXXXX, | XXXXXXXXXXXXX,MASTERCARD |
| XXXXXXXXXXXXXXXX, | XXXXXXXXXXXXXXXX,AMERICAN EXPRESS |
| XXXXXXXXXXXXXXX, | XXXXXXXXXXXXXXX,INVÁLIDA |

## Bonus 	:star:

> A partir de ahora van a aparecer en todos los `README.md` un sección de **Bonus** para los que quieran ponerse a prueba y resolver un ejercio más complejo. 
>
> ***Aclaración**: Los ejercios base, poseen todos los contenidos necesarios para competir. Los bonus son solo para los que quieran praticar más.*

Implementar la el módulo **csv** de Python y usar diccionarios para trabajar. El código tiene que utilizar funciones creadas por ustedes para sea orndenado. Y para terminar, el algoritmo debe crear un nuevo archivo por cada tipo de tarjeta, llenandolo de las tarjetas enontradas correspondientes:
``` text
    │
    ├── data/
    │   ├── tarjetas-VISA.csv
    │   ├── tarjetas-MASTERCARD.csv
    │   ├── tarjetas-AMEX.csv
    │   ├── tarjetas-INVALIDAS.csv
    │   └── tarjetas.csv
    │
    ├── README.md
    └── credit.py
```
## Tips

Para manejar archivos **csv** pueden usar el módulo que tiene integrado Python: https://realpython.com/python-csv/.

Este módulo tiene funciones para trabajar directamente con diccionarios, si quieren saber más sobre qué son diccionarios: https://devcode.la/tutoriales/diccionarios-en-python/

## Consideraciones

Para que la resolución forme parte del repositorio:   

- El programa debe estar apropiadamente comentado.
- Los comentarios deben ser en linea (`#`).
- Funciones propias deben ser documentadas con un `docstring`.
- Guardar el archivo como `credit_autor.py`
