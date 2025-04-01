# Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

# Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.
nombre = input("Por favor, ingrese su nombre: ")
print(f"Hola, {nombre}!")

# Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.
nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Por favor, ingrese su apellido: ")
edad = input("Por favor, ingrese su edad: ")
lugar = input("Por favor, ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")

# Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.
radio = int(input("Por favor, ingrese el radio de un circulo en cm: "))
area = 3.14 * radio ** 2
perimetro = 2 * 3.14 * radio
print(f"El circulo tiene un area de {area}cm. y un perimetro de {perimetro}cm.")

# Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.
segundos = int(input("Por favor ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(f"Los segundos ingresados equivalen a {horas} horas.")

# Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.
numero = int(input("Por favor, ingrese un numero entero: "))
x1 = numero * 1
x2 = numero * 2
x3 = numero * 3
x4 = numero * 4
x5 = numero * 5
x6 = numero * 6
x7 = numero * 7
x8 = numero * 8
x9 = numero * 9
print(f"""
{numero} x 1 = {x1}
{numero} x 2 = {x2}
{numero} x 3 = {x3}
{numero} x 4 = {x4}
{numero} x 5 = {x5}
{numero} x 6 = {x6}
{numero} x 7 = {x7}
{numero} x 8 = {x8}
{numero} x 9 = {x9}
""")

# Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos
num1 = int(input("Por favor, ingrese un numero distinto a 0: "))
num2 = int(input("Por favor, ingrese otro numero distinto a 0: "))
suma = num1 + num2
div = num1 / num2
mult = num1 * num2
resta = num1 - num2
print(f"""
{num1} + {num2} = {suma}
{num1} / {num2} = {div}
{num1} X {num2} = {mult}
{num1} - {num2} = {resta}
""")

# Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal.
altura = float(input("Por favor, ingrese su altura en m.: "))
peso = float(input("Por favor, ingrese su peso en kg.: "))
imc = peso / altura ** 2
print(f"Su indice de masa corporal es: {imc}")

# Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit.
tempC = float(input("Por favor, ingrese una temperatura en Celsius: "))
tempF = 1.8 * tempC + 32
print(f"La temperatura ingresada equivale a {tempF}°F.")

# Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.
num1 = float(input("Por favor, ingrese el primer numero: "))
num2 = float(input("Por favor, ingrese el segundo numero: "))
num3 = float(input("Por favor, ingrese el tercer numero: "))
prom = (num1 + num2 + num3) / 3
print(f"El promedio de los numeros ingresados es: {prom}")