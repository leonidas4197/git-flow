# menu.py

from operaciones import sumar, restar, multiplicar, dividir, factorial_iterativo, factorial_recursivo, fibonacci

def mostrar_menu():
    print("Menú de opciones:")
    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Salir")
    print("6- Calcular el factorial de un número (iterativo)")
    print("7- Calcular el factorial de un número (recursivo)")
    print("8- Calcular el fibonacci de un número (iterativo)")

def procesar_opcion():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-8): ")

        if opcion == '1':
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                print(f"Resultado de la suma: {sumar(num1, num2)}")
            except ValueError:
                print("Error: Debe ingresar números válidos.")
        
        elif opcion == '2':
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                print(f"Resultado de la resta: {restar(num1, num2)}")
            except ValueError:
                print("Error: Debe ingresar números válidos.")
        
        elif opcion == '3':
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                print(f"Resultado de la multiplicación: {multiplicar(num1, num2)}")
            except ValueError:
                print("Error: Debe ingresar números válidos.")
        
        elif opcion == '4':
            try:
                num1 = float(input("Ingrese el dividendo: "))
                num2 = float(input("Ingrese el divisor: "))
                print(f"Resultado de la división: {dividir(num1, num2)}")
            except ValueError:
                print("Error: Debe ingresar números válidos.")
        
        elif opcion == '6':
            try:
                num = int(input("Ingrese un número entero: "))
                print(f"Resultado del factorial iterativo: {factorial_iterativo(num)}")
            except ValueError:
                print("Error: Debe ingresar un número entero.")
        
        elif opcion == '7':
            try:
                num = int(input("Ingrese un número entero: "))
                print(f"Resultado del factorial recursivo: {factorial_recursivo(num)}")
            except ValueError:
                print("Error: Debe ingresar un número entero.")
        
        elif opcion == '8':
            try:
                num = int(input("Ingrese un número entero: "))
                print(f"Resultado del fibonacci: {fibonacci(num)}")
            except ValueError:
                print("Error: Debe ingresar un número entero.")
        
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Por favor, elija una opción entre 1 y 8.")

if __name__ == "__main__":
    procesar_opcion()
