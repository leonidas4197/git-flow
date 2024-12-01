def dividir(a, b):
    """Función para dividir dos números mediante resta iterativa."""
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Ambos parámetros deben ser números (int o float)")
    
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    
    # Hacemos la división mediante restas sucesivas
    signo = 1
    if a < 0:
        a = -a
        signo *= -1
    if b < 0:
        b = -b
        signo *= -1

    cociente = 0
    while a >= b:
        a -= b
        cociente += 1

    return cociente * signo
