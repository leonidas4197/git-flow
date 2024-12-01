from operaciones import sumar, restar, multiplicar, dividir, factorial_iterativo, factorial_recursivo

def mostrar_menu():
    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Salir")
    print("6- Calcular el factorial de un número (iterativo)")
    print("7- Calcular el factorial de un número (recursivo)")  # El número se ha cambiado a 7

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            try:
                a = float(input("Introduce el primer número: "))
                b = float(input("Introduce el segundo número: "))
                print("Resultado:", sumar(a, b))
            except ValueError:
                print("Error: Ambos valores deben ser números.")

        elif opcion == '2':
            try:
                a = float(input("Introduce el primer número: "))
                b = float(input("Introduce el segundo número: "))
                print("Resultado:", restar(a, b))
            except ValueError:
                print("Error: Ambos valores deben ser números.")

        elif opcion == '3':
            try:
                a = float(input("Introduce el primer número: "))
                b = float(input("Introduce el segundo número: "))
                print("Resultado:", multiplicar(a, b))
            except ValueError:
                print("Error: Ambos valores deben ser números.")

        elif opcion == '4':
            try:
                a = float(input("Introduce el dividendo: "))
                b = float(input("Introduce el divisor: "))
                print("Resultado:", dividir(a, b))
            except ZeroDivisionError:
                print("Error: No se puede dividir entre 0.")
            except ValueError:
                print("Error: Ambos valores deben ser números.")

        elif opcion == '6':
            try:
                n = int(input("Introduce un número para calcular su factorial (iterativo): "))
                print("Resultado:", factorial_iterativo(n))
            except ValueError:
                print("Error: Debes introducir un número entero.")

        elif opcion == '7':
            try:
                n = int(input("Introduce un número para calcular su factorial (recursivo): "))
                print("Resultado:", factorial_recursivo(n))
            except ValueError:
                print("Error: Debes introducir un número entero.")

        elif opcion == '5':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

if __name__ == "__main__":
    main()
