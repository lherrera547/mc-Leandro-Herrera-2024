from math import factorial, cos

def calcular_coseno_taylor(x, convergencia):
    ta = 1  
    s = ta  # Inicializa la suma de la serie
    n = 0  # Inicializa el contador de términos
    while abs(ta) >= convergencia:
        n += 1
        ta = (-1) ** n * (x ** (2 * n)) / factorial(2 * n)
        s += ta
        vr = cos(x)
        erp = abs((vr - s) / vr) * 100
    return s, erp, n
x = float(input("Por favor ingrese el valor de x en radianes: "))
convergencia = 0.5 * 10 ** -8
valor_estimado, error_relativo, iteraciones = calcular_coseno_taylor(x, convergencia)

print(f"Valor estimado de cos({x}): {valor_estimado}")
print(f"Error relativo porcentual: {error_relativo}%")
print(f"Número de iteraciones: {iteraciones}")
#ta=termino actual
#s=suma
#abs 
#vr= valor real
#erp= error relativo porcentual