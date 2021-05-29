#
# GitHub: @GianK128
#

import re as regex

def IndiceLegibilidad(texto: str) -> str:
    """
        Calcula el indice de legibilidad de un texto usando una formula.

        Devuelve una str indicando el grado / indice de complejidad del texto.
    """
    # NOTA: regex.sub reemplaza ocurrencias del primer argumento con el contenido del segundo.

    # Cantidad de palabras  --  Sacar la longitud de una lista en la que se encuentran todas las ocurrencias de caracteres 
    #                           que no son simbolos (al buscar en el texto, quitandole algunos caracteres que no quiero que sean separadores).
    word_count = len(regex.findall("\w+", regex.sub("['-]", "", texto)))
    
    # Cantidad de letras    --  Sacar la longitud de una str en la que todos los simbolos fueron cambiados por un espacio vacio.
    letter_count = len(regex.sub("\W+","", texto))

    # Cantidad de oraciones --  Sacar la longitud de una lista donde se encuentran todos las ocurrencias de caracteres que son simbolos
    #                           (buscando en el texto sin caracteres que no son separadores de oración)
    sentence_count = len(regex.findall("\W", regex.sub("[ ',]", "", texto)))

    # Cuenta de promedios
    L = 100 * letter_count / word_count
    S = 100 * sentence_count / word_count

    # Formula de indice
    indice = 0.0588 * L - 0.296 * S - 15.8

    # Condicionales para cambiar lo que se devuelve segun el grado
    return "Grado menor que 1." if indice < 1 else "Grado +16" if indice > 16 else f"Grado {int(indice)}"

# Pruebas - Descomentar para comprobar resultados
# print(
#     IndiceLegibilidad("One fish. Two fish. Red fish. Blue fish."),
#     IndiceLegibilidad("Would you like them here or there? I would not like them here or there. I would not like them anywhere."),
#     IndiceLegibilidad("In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since."),
#     IndiceLegibilidad("A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.")
# )

if __name__ == "__main__":
    texto = input("Meta el texto:\n")       # Tomar texto...
    print(IndiceLegibilidad(texto))         # Llamar a la funcion...