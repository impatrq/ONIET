text = input()              # Tomo un texto de la consola
f = open("text.txt", "w")   # Si no existe, lo crea. Si existe, lo sobre escribe
f.write(text)               # Escribe el texto en el archivo
f.close()                   # Cierro el archivo
