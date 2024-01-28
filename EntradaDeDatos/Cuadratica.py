"""
Realizar un programa que haga
el proceso de formula general para la resolución de ecuaciones,
sabiendo que la formula general es la que está en la imagen,
el usuario debe ingresar los valores de “a”, “b” y “c”
"""
import math

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

# Solucion positiva
x = (-b + math.sqrt(((b * b) - (4 * a * c )))) / (2 * a)

print("La solucion positiva es:", x)

x = (-b - math.sqrt(((b * b) - (4 * a * c )))) / (2 * a)

print("La solucion negativa es:", x)