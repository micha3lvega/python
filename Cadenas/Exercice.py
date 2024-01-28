"""
Crear un programa, que tenga una variable con la cadena:
“Te quiero solo como amigo”, y muestre la siguiente información:
"""
cadena = "Te quiero solo como amigo"

# Imprima los dos primeros caracteres.
print(cadena[:2])

# Imprima los tres últimos caracteres.
print(cadena[-3:])

"""
Imprima dicha cadena cada dos caracteres. Ej.:
Si la cadena fuera “recta” debería imprimir rca
"""
# slicing
print(cadena[::2])

"""
Dicha cadena en sentido inverso. Ej.:
Si la cadena fuera hola mundo!
debe imprimir !odnum aloh
"""
# slicing
print("Hola mundo"[::-1])

"""
La notación de "slicing" en Python es una forma de extraer porciones (o subconjuntos) de una secuencia como cadenas, listas o tuplas. La sintaxis general es [inicio:fin:paso], donde:

'inicio': Es el índice desde el cual comienza el "slice". Si no se especifica, se toma el inicio de la secuencia.
'fin': Es el índice donde termina el "slice". Si no se especifica, se toma el final de la secuencia.
'paso': Es el número de índices que avanza en cada paso. Si no se especifica, se toma un paso de 1.
"""

"""
Imprima la cadena en un sentido y en sentido inverso.
Ej: Si la cadena es “reflejo”
imprime reflejoojelfer.
"""
cadena = "reflejo"
print(cadena + cadena[::-1])

"""
Crear un programa que tenga una variable
con la cadena “Separado”
y un carácter de coma (,);
e inserte el carácter entre cada letra de la cadena.
Ej: separar y , debería devolver s,e,p,a,r,a,r
"""
separado = "Separado"
print(",".join(separado))