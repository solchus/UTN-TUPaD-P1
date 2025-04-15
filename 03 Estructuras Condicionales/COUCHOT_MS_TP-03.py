# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# edad_mayor = 18
# edad_user = int(input("Ingrese su edad: "))

# if edad_user >= edad_mayor:
#     print("Es mayor de edad.")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

# nota_aprobada = 6
# nota_user = int(input("Ingrese la nota obtenida: "))

# if nota_user >= nota_aprobada:
#     print("Aprobado.")
# else:
#     print("Desaprobado.")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

# num_usuario = int(input("Ingrese un numero par: "))
# calculo_par = num_usuario % 2
# if calculo_par == 0:
#     print("Ha ingresado un numero par")
# else:
#     print("Por favor, ingrese un numero par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

# edad_user = int(input("Ingrese su edad: "))
# if edad_user < 12:
#     print("Pertenece a la categoria niño/a.")
# elif edad_user >= 12 and edad_user < 18:
#     print("Pertenece a la categoria adolescente.")
# elif edad_user >= 18 and edad_user < 30:
#     print("Pertenece a la categoria Adulto/a joven.")
# else:
#     print("Pertenece a la categoria Adulto/a.")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

