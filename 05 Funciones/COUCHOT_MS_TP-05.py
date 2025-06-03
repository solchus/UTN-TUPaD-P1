# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.
def imprimir_hola_mundo():
    print("Hola, Mundo!")

imprimir_hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.
def saludar_usuario(nombre):
    return f"Hola, {nombre}!"

nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))

# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}."

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")
print(informacion_personal(nombre, apellido, edad, residencia))

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_peri-
# metro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar am-
# bas funciones para mostrar los resultados.
def calcular_area_circulo(radio):
    return 3.14 * (radio * radio)
def calcular_perimetro_circulo(radio):
    return 3.14 * 2 * radio

radio = int(input("Ingrese el radio de un circulo: "))
print(f"El area del circulo es {calcular_area_circulo(radio)} y su perimetro es {calcular_perimetro_circulo(radio)}.")

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
def segundos_a_horas(segundos):
    return int(segundos / 3600)

segundos = int(input("Ingrese la cantidad de segundos a convertir: "))
print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos)} horas.")

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.
def tabla_multiplicar(numero):
    resultado = 0
    for i in range(1,11):
        resultado = i * numero
        print(f"{i} X {numero} = {resultado}")

numero = int(input("Ingrese el numero a multiplicar: "))
tabla_multiplicar(numero)
 
# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resulta-
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
def operaciones_basicas(a, b):
    return (a+b, a-b, a*b, a/b)

a = 5
b = 4
print(operaciones_basicas(a,b))

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
def calcular_imc(peso, altura):
    return round(peso / (altura ** 2),2)

peso = float(input("Ingrese el peso: "))
altura = float(input("Ingrese la altura en metros: "))
print(calcular_imc(peso, altura))

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.
def celsius_a_farenheit(celsius):
    return celsius * 9 / 5 + 32

celsius = float(input("Ingrese la temperatura en Celsius: "))
print(f"El equivalente en Farenheit es {celsius_a_farenheit(celsius)}")

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.
def calcular_promedio(a, b, c):
    return round((a + b + c) / 3,2)
a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))
c = float(input("Ingrese el tercer numero: "))
print(f"El promedio de {a}, {b} y {c} es {calcular_promedio(a, b, c)}")