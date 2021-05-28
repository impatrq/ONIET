#
# GitHub: @JuanICasareski
#

altura = int(input("\nIngrese la altura: "))            # Registro la altura

assert 1<=altura<=8, "La altura tiene que ser 1<=x<=8"  # Si la altura no está dentro de los parametros, muestro el mensaje despues de la coma y corto la ejecucion.

for i in range(altura+1):
    print(' '*(altura-i), end='')                       # Imprimo los primeros espacios, para que no quede todo pegado a la izquierda
    print('#'*i, end='  ')                              # Imprimo la primera cantidad de '#', con sus dos espacios al final
    print('#'*i)                                        # Imprimo los segundos '#'

