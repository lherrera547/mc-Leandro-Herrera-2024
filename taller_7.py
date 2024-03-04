import math

# Definir una función para calcular el factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Definir la función para calcular e^-x usando la expansión en serie
def calcular_aproximaciones(x, cifras_significativas):
    # Inicializar variables
    suma1, suma2 = 1.0, 1.0
    error_relativo = 100
    n = 1
    
    # Calcular la primera aproximación
    while error_relativo > 10**(-cifras_significativas):
        termino = (-x)**n / factorial(n)
        suma1 += termino
        n += 1
        error_relativo = abs(termino) / suma1 * 100
    
    # Reiniciar variables para la segunda aproximación
    n = 1
    error_relativo = 100
    while error_relativo > 10**(-cifras_significativas):
        termino = x**n / factorial(n)
        suma2 += termino
        n += 1
        error_relativo = abs(termino) / suma2 * 100
    
    # Calcular e^-x como el inverso de e^x para la segunda aproximación
    suma2 = 1 / suma2
    
    # Devolver los resultados
    return suma1, n - 1, suma2, n - 1

# Solicitar entrada del usuario
x = float(input("Introduce el valor de x: "))
cifras_significativas = int(input("Introduce el número de cifras significativas deseadas: "))

# Calcular las aproximaciones
aprox1, iteraciones1, aprox2, iteraciones2 = calcular_aproximaciones(x, cifras_significativas)

# Imprimir los resultados
print(f"Aproximación 1: e^(-{x}) = {aprox1} (Número de iteraciones: {iteraciones1})")
print(f"Aproximación 2: e^(-{x}) = {aprox2} (Número de iteraciones: {iteraciones2})")
