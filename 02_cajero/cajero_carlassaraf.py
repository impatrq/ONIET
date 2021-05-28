#
# GitHub: @carlassaraf
#

monto = int(input("Monto a retirar: "))     
print()                                     

billetes = [50, 20, 10, 5, 1]           # Lista de todos los billetes disponibles

for billete in billetes:                # Itero por cada billete 
    i = 0
    while monto >= billete:             # Reviso si puedo entregar un billete
                                        # de este monto
        i += 1                          # Cuento un billete adicional
        monto -= billete                # Descuento del monto que me queda entregar

    print(f"Cantidad de billetes de {billete}: {i}")   


