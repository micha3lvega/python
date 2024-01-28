"""
Se desea tener un algoritmo que permita determinar y mostrar
el promedio que ha obtenido un alumno en un determinado curso,
conociendo las notas de: tres prácticas, el examen parcial y el examen final.

Considere:

PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6
Donde: P1, P2, P3 : Practicas
PP: promedio de práctica
PROM: promedio
EP: examen parcial
EF: examen final

"""
pratica1 = float(input("Ingrese la nota de la practica uno: "))
pratica2 = float(input("Ingrese la nota de la practica dos: "))
pratica3 = float(input("Ingrese la nota de la practica tres: "))
examenParcial = float(input("Ingrese la nota del examen parcial: "))
examenFinal = float(input("Ingrese la nota del examen final: "))

# Calcular promedio practica
pp = (pratica1 + pratica2 + pratica3) / 3
print("promedio de práctica:", pp)

# Calcular promedio 'PROM'
prom = (pp + (2 * examenParcial) + (3 * examenFinal)) / 6
print("Su promedio es de:", prom)