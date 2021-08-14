# Cifrado 2.0

## Consigna

Diseñar un algoritmo que cifre y descifre un texto almacenado en un `.txt`. El programa debe:

- Tomar como argumentos:
  -  Si va a cifrar o descifrar el texto (Usarán los comandos: `-c` para cifrar y `-d` para descifrar).
  -  La key.
  -  Y por último, el nombre del archivo a modificar.
- El archivo `.txt` se encontrá en la carpeta `data/`, y ahí estará el mensaje a modificar.
- Una vez modificado el texto, deberá guardarse en un archivo nuevo nombrado con el nombre del archivo anterior agragando un `-Cifrado` o un `-Descifrado` dependiendo el caso.
- Imprimir un mensaje de confirmación.

Los archivos estarán guardados de la siguente manera:
``` text
    │
    ├── data/
    │   ├── NOMBRE_ARCHIVO.txt
    │   └── NOMBRE_ARCHIVO-Cifrado.txt    # O -Descifrado.txt
    │
    ├── README.md
    └── cifrado 2.0.py
```
. 
### Aclaraciones
- Todos los argumentos se deben validar:
  - Solo existen los comandos `-c` y `-d`.
  - La key (largo/alfabético/repetición, igual que el ejercicio anterior).
  - La existencia del archivo elegido.
- En el caso de que haya un error en el proceso, deberá ser registrado en el mensaje de confirmación. Ejemplos:
  ``` text
    $ python cifrado.py -c tykhñrjofxgswnabzcvudmlpeiq mensaje.txt
    
    ERROR: Archivo no encontrado.
  ```
  ``` text
    $ python cifrado.py -c tykhñr mensaje.txt
    
    ERROR: Key inválida
  ```
  ``` text
    $ python cifrado.py -f tykhñrjofxgswnabzcvudmlpeiq mensaje.txt
    
    ERROR: Comando incorrecto. Use -c o -d.
  ```
- **NO** se contemplará los casos que contengan acentos o diéresis. Directamente se asume que no se ingresarán textos con esos caracteres.
- El resultado debe respetar los signos, los números, los espacios y las mayúsculas. 
- Para que cuando ejecuten el programa use argumentos deben importar `argv`:
  ```python
    from sys import argv

    if len(argv) != 2:      # Recuerden que el primero de los argumentos es el propio nombre del archivo.
        print("Uso: python cifrado.py key")
        exit(1)             # Con este if validan la cantidad de argumentos.

    valor = argv[1]         # argv es una lista, cada posición contiene cada argumento ingresado.
  ```

## Ejemplo

```text
    $ python cifrado.py tykhñrjofxgswnabzcvudmlpeiq -d texto.txt
    
    Mensaje descifrado correctamente.
```
## Test
Para testear usarán el programa siguiente para generar keys válidas y observar que cifre y descifre correctamente (Deberán validar por su cuenta keys inválidas). Lo copian en un archivo llamado `key_generator.py` y lo ejecuntan cada vez que lo necesiten :wink::
```python
    from random import shuffle

    abc = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    abc_list = []

    for c in abc:
        abc_list.append(c)

    shuffle(abc_list)

    print("KEY:","".join(abc_list))
```
## Consideraciones

Para que la resolución forme parte del repositorio:   

- El programa debe estar apropiadamente comentado.
- Los comentarios deben ser en linea (`#`).
- Funciones propias deben ser documentadas con un `docstring`.
- Guardar el archivo como `cifrado_autor.py`
