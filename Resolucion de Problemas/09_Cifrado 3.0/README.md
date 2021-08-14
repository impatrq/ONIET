# Cifrado 3.0 (POO) :recycle:

## Consigna

Usando de referencia el codigo del ejercicio [Cifrado 2.0](https://github.com/trq20/ONIET/tree/master/05_cifrado%202.0), diseñar una clase mejorando el funcionamiento. La clase debe tener:

- **Atributos necesarios**
  - KEY *(Acceder mediante **Encapsulación**.)*
- **Métodos necesarios**
  - \_\_init__(Key) *(En caso de no pasarle una Key debe generarla.)* 
  - Cifrar(Texto, Veces) -> Texto Cifrado(Str)
  - Descifrar(Texto, Veces) -> Texto Descifrado (Str)
  - RegenerarKey() -> Nueva Key (Str) 

## Aclaraciones

- La clase se debe llamar `Encrypter` y las funciones obligatorias también deben llamarse se de la misma manera que se menciona más arriba.
- Agregar más atributos y métodos en caso de ser necesario. 
- Debe tener coherencia y sentido todos los atributos y métodos.
- El programa tiene que estar perfectamente documentado aplicando el concepto de **Abstracción**.

## Consideraciones

Para que la resolución forme parte del repositorio:   

- El programa debe estar apropiadamente comentado.
- Los comentarios deben ser en linea (`#`).
- Funciones propias deben ser documentadas con un `docstring`.
- Guardar el archivo como `Cifrado 3.0_autor.py`
