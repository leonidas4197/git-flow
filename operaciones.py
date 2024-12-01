def dividir(a, b):
    # Dividir a entre b usando restas iterativas
    if b == 0:
        return "Error: No se puede dividir entre cero."
    elif not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Error: Los valores deben ser números (int o float)."
    
    resultado = 0
    while a >= b:
        a -= b
        resultado += 1
    return resultado
