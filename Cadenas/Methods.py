upper = "MAYUSCULAS"
lower = "minusculas";
name = "michael vega"
swapcase = "aBcDeFgH"
hello = "Hola Mundo"
rfind = "Hola mundo mundo mundo"
number = "100"
alnum = "ABC10034po"
splitLine = "Hello-world"

print(upper.lower()) # Convertir a mayusculas
print(lower.upper()) # Convertir a minusculas
print(name.capitalize()) # Convertir la primera palabra en mayuscula
print(name.title()) # Convertir la primera palabra antes de un espacio en mayusculas
print(name.swapcase()) # Convertir las mayusculas a minusculas y viceversa
print(name.count("vega")) # Imprima dicha cadena cada dos caracteres.
print(name.find("vega")) # Devuelve el índice en el que aparece la subcadena
print(name.find("Carrillo")) # (-1 si no aparece)
print(rfind.rfind("mundo")) # Devuelve el índice en el que aparece la subcadena, empezando por el final
print(number.isdigit()) # Devuelve True si la cadena es todo números
print(alnum.isalnum()) # Devuelve True si la cadena es todo números o carácteres alfabéticos
print(alnum.isalpha()) # Devuelve True si la cadena es todo carácteres alfabéticos
print(lower.islower()) # Devuelve True si la cadena es todo minúsculas
print(upper.isupper()) # Devuelve True si la cadena es todo mayúsculas
print(name.istitle()) # Devuelve True si la primera letra de cada palabra es mayúscula
print(" ".isspace()) # Devuelve True si la cadena es todo espacios
print(hello.startswith("Hola")) # Devuelve True si la cadena empieza con una subcadena
print(hello.endswith("Mundo")) # Devuelve True si la cadena acaba con una subcadena
print(rfind.split()) # Separa la cadena en subcadenas a partir de sus espacios y devuelve una lista
print(splitLine.split("-")) # Podemos indicar el carácter a partir del que se separa
print(",".join("Hola mundo")) # Une todos los caracteres de una cadena utilizando un caracter de unión
print(" ".join("Hola"))
print("   Hola mundo     ".strip()) # Borra todos los espacios por delante y detrás de una cadena y la devuelve
print("-----Hola mundo---".strip('-')) # Podemos indicar el carácter a borrar
print("Hola mundo".replace('o','0')) # Reemplaza una subcadena de una cadena por otra y la devuelve
print("Hola mundo mundo mundo mundo mundo".replace(' mundo','',4)) # Podemos indicar un límite de veces a reemplazar

