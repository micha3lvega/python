num1 = 100
num2 = 50
num3 = 20
num4 = 5

print(num1 + num2 * num3) # Se ejeucta primero la multiplicacion
print((num1 + num2) * num3) # Se ejeucta primero la suma
print((num1 + num2) * num3 - num4) # Se ejeuctan la suma, la multiplicacion y la resta
print((num1 + num2) * (num3 - num4)) # Se ejecuta la suma, la resta y la multiplicacion

