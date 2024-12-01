from operaciones import sumar, restar, multiplicar, dividir  # Importa la nueva función dividir

def mostrar_menu():
    print("Menú de operaciones:")
    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Salir")

def obtener_valores():
    # Pedir dos valores al usuario
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        return num1, num2
    except ValueError:
        print("Error: Los valores introducidos deben ser números (int o float).")
        return None, None

def ejecutar_operacion(opcion):
    if opcion == 1:
        num1, num2 = obtener_valores()
        if num1 is not None and num2 is not None:
            print(f"Resultado: {sumar(num1, num2)}")
    elif opcion == 2:
        num1, num2 = obtener_valores()
        if num1 is not None and num2 is not None:
            print(f"Resultado: {restar(num1, num2)}")
    elif opcion == 3:
        num1, num2 = obtener_valores()
        if num1 is not None and num2 is not None:
            print(f"Resultado: {multiplicar(num1, num2)}")
    elif opcion == 4:
        num1, num2 = obtener_valores()
        if num1 is not None and num2 is not None:
            # Llamar a la función dividir
            if num2 == 0:
                print("Error: No se puede dividir entre cero.")
            else:
                print(f"Resultado: {dividir(num1, num2)}")
    elif opcion == 5:
        print("Saliendo del programa.")
    else:
        print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = int(input("Selecciona una opción: "))
        if opcion == 5:
            break
        ejecutar_operacion(opcion)
