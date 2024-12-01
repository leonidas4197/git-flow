# menu.py
from operaciones import sumar, restar, multiplicar, dividir, factorial_iterativo, factorial_recursivo, fibonacci

def mostrar_menu():
    print("Menú de opciones:")
    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Salir")
    print("6- Calcular el factorial iterativo")
    print("7- Calcular el factorial recursivo")
    print("8- Calcular el Fibonacci de un número")

def manejar_opcion(opcion):
    if opcion == 1:
        try:
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            print(f"Resultado: {sumar(a, b)}")
        except ValueError:
            print("Error: Debes ingresar números válidos.")
    
    elif opcion == 2:
        try:
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            print(f"Resultado: {restar(a, b)}")
        except ValueError:
            print("Error: Debes ingresar números válidos.")
    
    elif opcion == 3:
        try:
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            print(f"Resultado: {multiplicar(a, b)}")
        except ValueError:
            print("Error: Debes ingresar números válidos.")
    
    elif opcion == 4:
        try:
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            print(f"Resultado: {dividir(a, b)}")
        except ValueError:
            print("Error: Debes ingresar números válidos.")
    
    elif opcion == 8:
        try:
            numero = int(input("Introduce un número para calcular el Fibonacci: "))
            print(f"El Fibonacci de {numero} es: {fibonacci(numero)}")
        except ValueError:
            print("Error: Debes ingresar un número válido.")
    
    elif opcion == 5:
        print("Saliendo...")
        exit()

    else:
        print("Opción no válida")
