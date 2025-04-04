import random
from statistics import mode, median, mean

# RESPUESTAS:

# Actividad 1
edad = int(input("Ingrese edad: "))
if edad > 18:
    print("Es mayor de edad")

# Actividad 2
nota = float(input("Ingrese la nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Actividad 3
numero = int(input("Ingrese un número par: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# Actividad 4
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Es niño/a")
elif 12 <= edad < 18:
    print("Es adolescente")
elif 18 <= edad < 30:
    print("Es adulto/a joven")
else:
    print("Es adulto/a")

# Actividad 5
contraseña = input("Ingrese una contraseña: ")
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Actividad 6
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
if media > mediana > moda:
    print("Sesgo positivo(a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo(a la izquierda)")
else:
    print("Sin sesgo")

# Actividad 7
frase = input("Ingrese una frase o palabra: ")
vocales = "aeiouAEIOU"
if frase[-1] in vocales:
    frase += "!"
print(frase)

# Actividad 8
nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 para mayúsculas - 2 para minúsculas - 3 para capitalizar: "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida")

# Actividad 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

# Actividad 10
hemisferio = input("Ingrese el hemisferio en el que se encuentra (N/S):").strip().upper()
dia = int(input("Ingrese el día del mes: "))
mes = int(input("Ingrese el número del mes (1-12): "))
if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
    estacion_norte, estacion_sur = "Invierno", "Verano"
elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
    estacion_norte, estacion_sur = "Primavera", "Otoño"
elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
    estacion_norte, estacion_sur = "Verano", "Invierno"
else:
    estacion_norte, estacion_sur = "Otoño", "Primavera"

if hemisferio == "N" or hemisferio == "n":
    print(f"Está en la estación: {estacion_norte}")
elif hemisferio == "S" or hemisferio == "s":
    print(f"Está en la estación: {estacion_sur}")
else:
    print("Hemisferio inválido")