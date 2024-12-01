def sumar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    return "Error: Ambos valores deben ser int o float."


def restar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b
    return "Error: Ambos valores deben ser int o float."


def multiplicar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        resultado = 0
        for _ in range(int(abs(b))):
            resultado += a
        return resultado if b >= 0 else -resultado
    return "Error: Ambos valores deben ser int o float."


def dividir(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if b == 0:
            return "Error: No se puede dividir por cero."
        resultado = 0
        while a >= b:
            a -= b
            resultado += 1
        return resultado
    return "Error: Ambos valores deben ser int o float."


def factorial_iterativo(n):
    if not isinstance(n, int):
        return "Error: El valor debe ser un número entero."
    if n < 0:
        return "Error: No se puede calcular el factorial de un número negativo."
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def factorial_recursivo(n):
    if not isinstance(n, int):
        return "Error: El valor debe ser un número entero."
    if n < 0:
        return "Error: No se puede calcular el factorial de un número negativo."
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursivo(n - 1)
