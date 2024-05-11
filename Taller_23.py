def interpolacion_lagrange(x, y, x_eval, grado):
    """
    Interpolación de Lagrange para estimar el valor en x_eval.
    
    Parámetros:
        x (list): Lista de las coordenadas x de los puntos de datos.
        y (list): Lista de las coordenadas y de los puntos de datos.
        x_eval (float): El valor en el que estimar la función.
        grado (int): Grado del polinomio de Lagrange.
    
    Retorna:
        float: Valor estimado de f(x_eval).
    """
    n = len(x)
    resultado = 0.0
    for i in range(n):
        termino = y[i]
        for j in range(n):
            if j != i:
                termino *= (x_eval - x[j]) / (x[i] - x[j])
        resultado += termino if grado == -1 or grado == i else 0
    return resultado

# Datos dados
valores_x = [0, 2, 4, 6, 8]
valores_y = [2, 0.1, 3, 4.5, 7]

# Estimación de f(2.75) con polinomios de Lagrange de grados 1 y 2
f_estimada_grado_1 = interpolacion_lagrange(valores_x[:2], valores_y[:2], 2.75, 1)
f_estimada_grado_2 = interpolacion_lagrange(valores_x[:3], valores_y[:3], 2.75, 2)

# Imprimiendo los resultados
print("Valor estimado de f(2.75) con polinomio de Lagrange de grado 1:", f_estimada_grado_1)
print("Valor estimado de f(2.75) con polinomio de Lagrange de grado 2:", f_estimada_grado_2)

# Estimación de f(2.75) con polinomio de Lagrange de grado 3
f_estimada_grado_3 = interpolacion_lagrange(valores_x, valores_y, 2.75, 3)
print("Valor estimado de f(2.75) con polinomio de Lagrange de grado 3:", f_estimada_grado_3)
