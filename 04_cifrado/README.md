# Cifrado

## Consigna

Diseñar un algoritmo que cifre un texto ingresado como input. El programa debe:

- Tomar como argumento para inicar el programa la key con la cual va a cifrar.
- Imprimir el resultado cifrado.

Para cifrar el texto se hará de la siguente manera:
``` python
           Abecedario Real                      Key
    ABCDEFGHIJKLMNÑOPQRSTUVWXYZ  =>  VWBFJHARZQMOESTCKIPGNDÑXUYL
      ^                                ^
      2                                2
```
Se sustituirá la letra a cifrar del **Abecedario Real** por la correspondiente en la **Key**, y para identificarla se usará la posición. En el caso de arriba, `C` (que corresponde a la posición 2) se cifrará como `B`y así sucesivamente. 
### Aclaraciones
- El argumento (Key) se debe validar:
  - Largo (27 caracteres, ni maś ni menos).
  - Que sea alfabético (No pueden haber numeros ni signos).
  - Que no se repitan los caracteres.
- **NO** se contemplará los casos que contengan acentos o diéresis. Directamente se asume que no se ingresarán textos con esos caracteres.
- El resultado cifrado debe respetar los signos, los números, los espacios y las mayúsculas. Ejemplo:

    ```text
    $ python cifrado.py tykhñrjofxgswnabzcvudmlpeiq

    Texto plano:  Estimados alumnos! me comunico para acercarles la invitacion a la clase que se dictara por zoom el dia viernes 28 de Mayo a partir de las 18:30 hs

    Texto cifrado: Ñudfwthbu tsmwnbu! wñ kbwmnfkb ztvt tkñvktvsñu st fnlfdtkfbn t st kstuñ cmñ uñ hfkdtvt zbv qbbw ñs hft lfñvnñu 28 hñ Wtib t ztvdfv hñ stu 18:30 ou
    ```
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
    $ python cifrado.py tykhñrjofxgswnabzcvudmlpeiq
    Texto: Hola, soy John Doe.
    Cifrado: Obst, ubi Xbon Hbñ.
```
## Test
Para testear usarán el programa siguiente para generar keys válidas y observar que cifre correctamente (Deberán validar por su cuenta keys inválidas). Lo copian en un archivo llamado `key_generator.py` y lo ejecuntan cada vez que lo necesiten :wink::
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
