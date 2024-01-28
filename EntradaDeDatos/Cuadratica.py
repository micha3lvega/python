"""
Realizar un programa que haga
el proceso de formula general para la resolución de ecuaciones,
sabiendo que la formula general es la que está en la imagen,
el usuario debe ingresar los valores de “a”, “b” y “c”
"""
import math

a = 2 # float(input("Ingrese el valor de a: "))
b = -9 # float(input("Ingrese el valor de b: "))
c = 4 # float(input("Ingrese el valor de c: "))

# Calcular discriminatnte
discriminante = ((b * b) - (4 * a * c ))

if(discriminante >= 0):

    x = (-b + math.sqrt(discriminante)) / (2 * a) # Solucion positiva
    print("La solucion positiva es:", x)

    x = (-b - math.sqrt(discriminante)) / (2 * a) # Solucion negativa
    print("La solucion negativa es:", x)

else:
    print(f"No hay soluciones reales, el discriminante: {discriminante} es negativo.")
