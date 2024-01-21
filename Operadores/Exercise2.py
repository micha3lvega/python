"""
Una juguetería
tiene mucho éxito en dos de sus productos:
payasos y muñecas.
Suele hacer venta por correo
y la empresa de logística
les cobra por peso de cada paquete,
así que deben calcular
el peso de los payasos y muñecas
que saldrán en cada paquete a demanda.
Cada payaso pesa 112 g y cada muñeca 75 g.
Un cliente frecuente pide la cantidad de
23 payasos y 54 muñecas,
realiza un programa que muestre
el peso total de toda la venta.
"""
clownWeights = 112
dollWeights = 75

clownsOrder = 23
dollOrder = 54

valueOrderClows = clownWeights * clownsOrder
valueOrderDolls = dollWeights * dollOrder

total = valueOrderClows + valueOrderDolls

# (112g/payaso × 23 payasos) + (75g/muneca × 54 munecas) = 8916g
print("El total es:" , total, "g")
print("El total es: " , total, "g", sep="") # Eliminar separacion entre el total y la g
print("El total es: " , (clownWeights * clownsOrder) + (dollWeights * dollOrder),"g", sep="")