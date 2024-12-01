from operaciones import sumar, restar, multiplicar, dividir, factorial_iterativo

def mostrar_menu():
    print("Menú de operaciones:")
    print("1 - Sumar")
    print("2 - Restar")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Salir")
    print("6 - Calcular el factorial de un número (iterativo)")
    
    opcion = int(input("Elija una opción: "))
    
    if opcion == 1:
        valor1 = float(input("Ingrese el primer valor: "))
        valor2 = float(input("Ingrese el segundo valor: "))
        resultado = sumar(valor1, valor2)
        print(f"Resultado de la suma: {resultado}")

    elif opcion == 2:
        valor1 = float(input("Ingrese el primer valor: "))
        valor2 = float(input("Ingrese el segundo valor: "))
        resultado = restar(valor1, valor2)
        print(f"Resultado de la resta: {resultado}")

    elif opcion == 3:
        valor1 = float(input("Ingrese el primer valor: "))
        valor2 = float(input("Ingrese el segundo valor: "))
        resultado = multiplicar(valor1, valor2)
        print(f"Resultado de la multiplicación: {resultado}")

    elif opcion == 4:
        valor1 = float(input("Ingrese el primer valor: "))
        valor2 = float(input("Ingrese el segundo valor: "))
        resultado = dividir(valor1, valor2)
        print(f"Resultado de la división: {resultado}")

    elif opcion == 6:
        valor = int(input("Ingrese un número para calcular el factorial: "))
        resultado = factorial_iterativo(valor)
        print(f"El factorial de {valor} es: {resultado}")

    elif opcion == 5:
        print("Saliendo del programa...")

    else:
        print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    while True:
        mostrar_menu()
