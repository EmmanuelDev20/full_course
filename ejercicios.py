# Solicita una frase al usuario
# frase = input("Escribe una frase: ")

# # Muestra la cantidad de caracteres
# print(f"Número de caracteres: {len(frase)}")

# # Imprime la frase en mayúsculas y en minúsculas
# print(f"En mayúsculas: {frase.upper()}")
# print(f"En minúsculas: {frase.lower()}")

# # Muestra solo los primeros 5 caracteres
# print(f"Primeros 5 caracteres: {frase[:5]}")'




# Ejercicios básicos

# 1. Nombre y edad:
# Pide al usuario su nombre y edad.
# Muestra un mensaje que diga: "Hola, [nombre]. Tienes [edad] años."

## Solución:
# nombre = input("¿Cuál es tu nombre? ")
# edad = input("¿Cuántos años tienes? ")
# Asegúrate de que la edad sea un número entero.

# try:
#     edad = int(edad)
# except ValueError:
#     print("Por favor, ingresa un número válido para la edad.")
# else:
#     print(f"Hola, {nombre}. Tienes {edad} años.")

  


# 2. Suma de dos números:
# Solicita dos números al usuario.
# Suma los números e imprime el resultado.
# Asegúrate de convertir los valores ingresados a enteros o flotantes.

## Solución:
# num1 = input("Ingresa el primer número: ")
# num2 = input("Ingresa el segundo número: ")
# try:
#     num1 = float(num1)
#     num2 = float(num2)
# except ValueError:
#     print("Por favor, ingresa números válidos.")
# else:
#     suma = num1 + num2
#     print(f"La suma de {num1} y {num2} es: {suma}")


# 3. Conversión de temperatura:
# Pide una temperatura en grados Celsius.
# Convierte la temperatura a Fahrenheit usando la fórmula:
# 𝐹 = 𝐶 × 9 / 5 +32
# Muestra el resultado con un mensaje claro.

# Solución:
# celsius = input("Ingresa la temperatura en grados Celsius: ")
# try:
#     celsius = float(celsius)
# except ValueError:
#     print("Por favor, ingresa un número válido para la temperatura.")
# else:
#     fahrenheit = celsius * 9 / 5 + 32
#     print(f"La temperatura en Fahrenheit es: {fahrenheit:.2f}°F")


# 4. Cálculo del área de un círculo:
# Solicita el radio de un círculo.
# Calcula el área usando la fórmula:
# 𝐴 = 𝜋𝑟2
# Imprime el área con dos decimales de precisión.

# Solución:
# import math
# radio = input("Ingresa el radio del círculo: ")
# try:
#     radio = float(radio)
# except ValueError:
#     print("Por favor, ingresa un número válido para el radio.")
# else:
#     area = math.pi * radio ** 2
#     print(f"El área del círculo es: {area:.2f} unidades cuadradas.")


# # Ejercicios intermedios
# 5. Tipo de dato detectado:
# Pide un dato al usuario.
# Usa type() para mostrar el tipo de dato ingresado.

# Solución:
# dato = input("Ingresa un dato: ")
# tipo_dato = type(dato)
# print(f"El tipo de dato ingresado es: {tipo_dato}")

# 6. Conversión de tipos:
# Pide al usuario un número entero y conviértelo a flotante.
# Luego, conviértelo a cadena y muestra los valores resultantes con su tipo.
# "El número entero es: [variable] (tipo: [tipo de variable])"

# Solución:
# entero = input("Ingresa un número entero: ")
# try:
#     entero = int(entero)
# except ValueError:
#     print("Por favor, ingresa un número entero válido.")
# else:
#     flotante = float(entero)
#     cadena = str(entero)
#     print(f"El número entero es: {entero} (tipo: {type(entero)})")
#     print(f"El número flotante es: {flotante} (tipo: {type(flotante)})")
#     print(f"El número como cadena es: {cadena} (tipo: {type(cadena)})")

# 7. Operaciones con cadenas:
# Solicita una frase al usuario.
# Muestra la cantidad de caracteres.
# Imprime la frase en mayúsculas y en minúsculas.
# Muestra solo los primeros 5 caracteres.

# Solución:
# frase = input("Escribe una frase: ")
# longitud = len(frase)
# print(f"Número de caracteres: {longitud}")
# print(f"En mayúsculas: {frase.upper()}")
# print(f"En minúsculas: {frase.lower()}")
# print(f"Primeros 5 caracteres: {frase[:5]}")


# 8. Promedio de tres números:
# Solicita tres números.
# Calcula su promedio e imprime el resultado.

# Solución:
# num1 = input("Ingresa el primer número: ")
# num2 = input("Ingresa el segundo número: ")
# num3 = input("Ingresa el tercer número: ")
# try:
#     num1 = float(num1)
#     num2 = float(num2)
#     num3 = float(num3)
# except ValueError:
#     print("Por favor, ingresa números válidos.")
# else:
#     promedio = (num1 + num2 + num3) / 3
#     print(f"El promedio de los tres números es: {promedio:.2f}")



# Ejercicios avanzados
# 8. Calculadora simple:
# Crea una calculadora simple que permita sumar, restar, multiplicar y dividir dos números.
# Solicita dos números y una operación al usuario.
# Realiza la operación y muestra el resultado.
# Solución:
# def calculadora():
#     print("Calculadora simple")
#     print("Operaciones disponibles:")
#     print("1. Sumar")
#     print("2. Restar")  
#     print("3. Multiplicar")
#     print("4. Dividir")
#     operacion = input("Selecciona una operación (1/2/3/4): ")
#     num1 = input("Ingresa el primer número: ")
#     num2 = input("Ingresa el segundo número: ")
#     try:
#         num1 = float(num1)
#         num2 = float(num2)
#     except ValueError:
#         print("Por favor, ingresa números válidos.")
#         return
#     if operacion == '1':
#         resultado = num1 + num2
#         print(f"La suma es: {resultado}")
#     elif operacion == '2':
#         resultado = num1 - num2
#         print(f"La resta es: {resultado}")
#     elif operacion == '3':
#         resultado = num1 * num2
#         print(f"La multiplicación es: {resultado}")
#     elif operacion == '4':
#         if num2 != 0:
#             resultado = num1 / num2
#             print(f"La división es: {resultado}")
#         else:
#             print("Error: No se puede dividir entre cero.")
#     else:
#         print("Operación no válida.")
# calculadora()




# 9. Contador de vocales:
# Solicita una frase al usuario.
# Cuenta la cantidad de vocales (a, e, i, o, u) en la frase.
# Imprime el resultado.
# Solución:
# frase = input("Escribe una frase: ")
# vocales = "aeiouAEIOU"
# contador_vocales = 0
# for letra in frase:
#     if letra in vocales:
#         contador_vocales += 1
# print(f"La cantidad de vocales en la frase es: {contador_vocales}")
# 10. Inversor de cadena:
# Solicita una cadena al usuario.
# Invierte la cadena y muestra el resultado.
# Solución:
# cadena = input("Ingresa una cadena: ")
# cadena_invertida = cadena[::-1]
# print(f"La cadena invertida es: {cadena_invertida}")
# 11. Palíndromo:
# Solicita una palabra al usuario.
# Verifica si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
# Imprime el resultado.
# Solución:
# palabra = input("Ingresa una palabra: ")
# palabra = palabra.lower()
# palabra_invertida = palabra[::-1]
# if palabra == palabra_invertida:
#     print(f"{palabra} es un palíndromo.")
# else:
#     print(f"{palabra} no es un palíndromo.")
# 12. Contador de palabras:
# Solicita una frase al usuario.
# Cuenta la cantidad de palabras en la frase.
# Imprime el resultado.
# Solución:
# frase = input("Escribe una frase: ")
# palabras = frase.split()
# contador_palabras = len(palabras)
# print(f"La cantidad de palabras en la frase es: {contador_palabras}")
# 13. Generador de contraseñas:
# Genera una contraseña aleatoria de 8 caracteres.
# Puedes usar letras mayúsculas, minúsculas y números.
# Imprime la contraseña generada.
# Solución:
# import random
# import string
# def generar_contrasena(longitud=8):
#     caracteres = string.ascii_letters + string.digits
#     contrasena = ''.join(random.choice(caracteres) for _ in range(longitud)) 
#     return contrasena
# contrasena = generar_contrasena()
# print(f"Contraseña generada: {contrasena}")
# 14. Juego de adivinanza:
# Genera un número aleatorio entre 1 y 100.
# Pide al usuario que adivine el número.
# Indica si el número es mayor o menor que el número generado.
# Imprime cuántos intentos le tomó adivinarlo.
# Solución:
# import random
# def juego_adivinanza(): 
#     numero_secreto = random.randint(1, 100)
#     intentos = 0
#     while True:
#         intento = input("Adivina el número entre 1 y 100: ")
#         try:
#             intento = int(intento)
#         except ValueError:
#             print("Por favor, ingresa un número válido.")
#             continue
#         intentos += 1
#         if intento < numero_secreto:
#             print("El número es mayor.")
#         elif intento > numero_secreto:
#             print("El número es menor.")
#         else:
#             print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
#             break
# juego_adivinanza()
# 5. Calculadora de IMC:
# Solicita el peso y la altura del usuario.
# Calcula el Índice de Masa Corporal (IMC) usando la fórmula:
# IMC = peso / (altura ** 2)
# Imprime el resultado y clasifica el IMC según los rangos:
# - Bajo peso: IMC < 18.5
# - Peso normal: 18.5 <= IMC < 24.9
# - Sobrepeso: 25 <= IMC < 29.9
# - Obesidad: IMC >= 30
# Solución:
# peso = input("Ingresa tu peso en kg: ")
# altura = input("Ingresa tu altura en metros: ")
# try:
#     peso = float(peso)
#     altura = float(altura)
# except ValueError:
#     print("Por favor, ingresa números válidos.")
# else: 
#     imc = peso / (altura ** 2)
#     print(f"Tu IMC es: {imc:.2f}")
#     if imc < 18.5:
#         print("Bajo peso")
#     elif 18.5 <= imc < 24.9:
#         print("Peso normal")
#     elif 25 <= imc < 29.9:
#         print("Sobrepeso")
#     else:
#         print("Obesidad")
# 6. Conversor de divisas:
# Solicita una cantidad en dólares y el tipo de cambio a euros. 
# Convierte la cantidad a euros y muestra el resultado.
# Solución:
# dolares = input("Ingresa la cantidad en dólares: ")
# tipo_cambio = input("Ingresa el tipo de cambio a euros: ")
# try:
#     dolares = float(dolares)
#     tipo_cambio = float(tipo_cambio)
# except ValueError:
#     print("Por favor, ingresa números válidos.")
# else:
#     euros = dolares * tipo_cambio
#     print(f"{dolares} dólares son {euros:.2f} euros.")
# 7. Contador de caracteres:
# Solicita una cadena al usuario.
# Cuenta la cantidad de caracteres (sin contar espacios).
# Imprime el resultado.
# Solución:
# cadena = input("Ingresa una cadena: ")
# contador_caracteres = len(cadena.replace(" ", ""))
# print(f"La cantidad de caracteres (sin contar espacios) es: {contador_caracteres}")
# 8. Generador de números aleatorios:
# Genera un número aleatorio entre 1 y 100.
# Imprime el número generado.
# Solución:
# import random
# numero_aleatorio = random.randint(1, 100)
# print(f"Número aleatorio generado: {numero_aleatorio}")
# 9. Juego de piedra, papel o tijera:
# Crea un juego simple de piedra, papel o tijera.
# Solicita al usuario que elija una opción y genera una opción aleatoria para la computadora.
# Compara las opciones y determina el ganador.
# Solución:
# import random
# def juego_piedra_papel_tijera():
#     opciones = ["piedra", "papel", "tijera"]
#     eleccion_usuario = input("Elige piedra, papel o tijera: ").lower()
#     if eleccion_usuario not in opciones:
#         print("Opción no válida.")
#         return
#     eleccion_computadora = random.choice(opciones)
#     print(f"Computadora eligió: {eleccion_computadora}")
#     if eleccion_usuario == eleccion_computadora:
#         print("¡Es un empate!")
#     elif (eleccion_usuario == "piedra" and eleccion_computadora == "tijera") or \
#          (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or \
#          (eleccion_usuario == "tijera" and eleccion_computadora == "papel"):
#         print("¡Ganaste!")
#     else:
#         print("¡Perdiste!")
# juego_piedra_papel_tijera()