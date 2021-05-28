#
# GitHub: @carlassaraf
#

text = input("Text: ")

words = len(text.split(' '))                                        # Separo por espacios y cuento el largo de la lista
sentences = text.count('.') + text.count('!') + text.count('?')     # Cuento las ocurrencias de simbolos que terminan una oracion

letters = 0

for char in text:
    if char.isalpha():                  # Por cada caracter que sea una letra, cuento
        letters += 1

l = 100 * letters / words               # Saco el promedio cada 100 palabras
s = 100 * sentences / words

index = .0588 * l - .296 * s - 15.8

if index >= 16:
    print("Grado 16+")

elif index < 1:
    print("Menor a grado 1")

else:
    print(f"Grado {round(index)}")