from menu import mostrar_menu, pedir_numero

def main():
    opcion = mostrar_menu()
    if opcion == 5:
        print("Saliendo...")
    else:
        numero = pedir_numero()
        print(f"Has seleccionado la opción {opcion} con el número {numero}")

if __name__ == "__main__":
    main()
