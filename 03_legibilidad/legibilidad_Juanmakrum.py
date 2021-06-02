frase = input("Ingrese su frase: ")     #ingreso la frase deseada

def simplificar(frase):          
    """ 
    Esta función permite ignorar números y los carácteres que no sean 
    letras más comunes para que no interfieran en el conteo de las letras.
    """       
    frase = frase.replace("?", ".")
    frase = frase.replace("¿", "")
    frase = frase.replace(",", "")
    frase = frase.replace("0", "")
    frase = frase.replace("1", "")
    frase = frase.replace("2", "")
    frase = frase.replace("3", "")
    frase = frase.replace("4", "")
    frase = frase.replace("5", "")
    frase = frase.replace("6", "")
    frase = frase.replace("7", "")
    frase = frase.replace("8", "")
    frase = frase.replace("9", "")     
    frase = frase.replace("-","")
    frase = frase.replace("\n", "")
    return frase


frase = simplificar(frase)              #aplico la función

palabras = frase.replace(".","")        #ignoro los puntos
palabras = palabras.split(" ")          #Separo las palabras por los espacios
cantPalabras = len(palabras)            #averiguo la cantidad de palabras

letras = frase.replace(".", "")         #ignoro los puntos
letras = frase.replace(" ", "")         #ignoro los espacios
cantLetras = len(letras)                #averiguo la cantidad de letras
L = (100*cantLetras)/cantPalabras       #averiguo L con regla de 3

oraciones = frase.split(".")            #divido las oraciones por los puntos
cantOraciones = len(oraciones)          #averiguo la cantidad de oraciones
S = (100*cantOraciones)/cantPalabras    #averiguo S con la regla de 3

indice = 0.0588*L - 0.296*S - 15.8      #Averiguo el índice con la formula
if indice<1: print("Grado menor a 1")
elif indice>=16: print("Grado mayor a 16")
else: print(f"Grado{round(indice)}")    #imprimo el índice redondeado dependiendo el resultado
print(f"letras: {cantLetras}")          #imprimo la cantidad de letras para verificar
print(f"palabras: {cantPalabras}")      #imprimo la cantidad de palabras para verificar
print(f"oraciones: {cantOraciones}")    #imprimo la cantidad de oraciones para verificar
print("Índice:",indice)                 #imprimo el índice sin redondear para verificar