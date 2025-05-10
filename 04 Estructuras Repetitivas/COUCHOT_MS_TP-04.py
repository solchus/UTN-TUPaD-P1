# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# for i in range (0,101):
#     print (i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

# nro = int(input("Ingrese un numero entero: "))
# i = 0
# while nro > 0:
#     nro = nro // 10
#     i += 1
# print(f"El numero tiene {i} digitos.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

# n1 = int(input("Ingrese el valor minimo: "))
# n2 = int(input("Ingrese el valor maximo: "))
# i = 0
# sumatoria = 0
# for i in range (n1 + 1, n2):
#     sumatoria += i
# print (f"La suma de los numeros comprendidos entre {n1} y {n2} es {sumatoria}.")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

# n = 1
# sumatoria = 0
# while n != 0:
#     n = int(input("Ingrese el numero a sumar, cuando desee el total, ingrese 0: "))
#     sumatoria += n
# print (f"La suma de los numeros ingresados es {sumatoria}.")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# import random
# var_ran = random.randint(0,9)
# num_user = 15
# intentos = 0
# while num_user != var_ran:
#     num_user = int(input("Adivine un numero entre 0 y 9: "))
#     intentos += 1
# print(f"Te tomo {intentos} intentos.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

# for i in range(100,0,-2):
#     print (i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario

# num_user = int(input("Ingrese el numero maximo: "))
# sumatoria = 0
# for i in range(0,num_user):
#     sumatoria += i
# print(f"La suma de los numeros comprendidos entre 0 y {num_user} es {sumatoria}.")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# pares = 0
# impares = 0
# positivos = 0
# negativos = 0
# num_user = 0
# for i in range(1,101):
#     num_user = int(input("Ingrese un numero: "))
#     if num_user % 2 == 0:
#         pares += 1
#     else:
#         impares +=1
#     if num_user > 0:
#         positivos += 1
#     elif num_user < 0:
#         negativos +=1
# print(f"Se ingresaron {positivos} numeros positivos, {negativos} numeros negativos, {pares} numeros pares y {impares} numeros impares.")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

# sumatoria = 0
# for i in range(1,101):
#     num_user = int(input("Ingrese un numero: "))
#     sumatoria += num_user
# media = sumatoria / 100
# print(f"La media de los numeros ingresados es {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# input = int(input("Ingrese el numero a invertir: "))
# num_user = input
# num_inv = 0
# digito = 0
# while num_user > 0:
#     digito = num_user % 10
#     num_inv = num_inv * 10 + digito
#     num_user //= 10
# print(f'El numero {input} invertido es {num_inv}')