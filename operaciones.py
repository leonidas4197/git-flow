# operacions.py

def sumar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        return "Error: Ambos valores deben ser int o float."

def restar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b
    else:
        return "Error: Ambos valores deben ser int o float."

def multiplicar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        result = 0
        for _ in range(abs(int(b))):
            result += a
        if b < 0:
            result = -result
        return result
    else:
        return "Error: Ambos valores deben ser int o float."

def dividir(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if b == 0:
            return "Error: No se puede dividir por cero."
        result = 0
        while a >= b:
            a -= b
            result += 1
        return result
    else:
        return "Error: Ambos valores deben ser int o float."

def factorial_iterativo(n):
    if isinstance(n, int):
        if n < 0:
            return "Error: El factorial no está definido para números negativos."
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    else:
        return "Error: El valor debe ser un número entero."

def factorial_recursivo(n):
    if isinstance(n, int):
        if n < 0:
            return "Error: El factorial no está definido para números negativos."
        if n == 0:
            return 1
        else:
            return n * factorial_recursivo(n - 1)
    else:
        return "Error: El valor debe ser un número entero."

def fibonacci(n):
    if not isinstance(n, int):
        return "Error: El valor debe ser un número entero."
    if n < 0:
        return "Error: El valor debe ser un número entero positivo."
    
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
