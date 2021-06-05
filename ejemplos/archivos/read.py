f = open("text.txt", "r")   # Si el archivo no se encuentra en el mismo directorio tira un FileNotFoundError
text = f.read()             # Leo el contenido entero del archivo
f.close()                   # Cierro el archivo
print(text)                 # Imprimo el contenido del archivo
