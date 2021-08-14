#
# GitHub: AlejandroMendez7
#

inp = int(input("Ingrese un valor = "))                     # Input como int
total = 0                                                   # Defino una variable 
tup = (50, 20, 10, 5, 1)                                    # Tuple con los billetes

for i in tup:                                               # Loop para el calculo
  if inp % i == 0:                                          # Loop para numeros redondos de un solo tipo de billete Ej: 1200
    total = str(int(inp / i))                               # Calculo y convieto a str el total de billetes
    print("Son "+ total + " billete/s de " + str(i))        # Imprimo la cant del billete 
    break                                                   # Como es multiplo del tipo de billete elegido no es necesario seguir operando y termino el loop
  else:
   while inp > i:                                           # Loop para los num que no son multiplos del tipo de billete en esa instancia del tuple
     total = inp // i                                       # Calculo cuanto necesito de cada uno 
     print("Son "+ str(total) + " billete/s de " + str(i))  # Imprimo la cant de billetes y de que tipo
     inp = inp - total * i                                  # Altero el valor de i para cumplir con el While y poder seguir operando

