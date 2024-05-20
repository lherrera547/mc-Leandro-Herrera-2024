# -*- coding: utf-8 -*-
"""taller_24.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vCKJNEbY0VG0RLchuUv7FJ5l5BPX6bxk
"""

def lagrange_interpolation(x_data, y_data):
    n = len(x_data)
    def L(k, x):
        result = 1
        for j in range(n):
            if j != k:
                result *= (x - x_data[j]) / (x_data[k] - x_data[j])
        return result

    # Calcular el polinomio de interpolación de Lagrange
    def lagrange_polynomial(x):
        result = 0
        for k in range(n):
            result += y_data[k] * L(k, x)
        return result

    return lagrange_polynomial

# Datos de ejemplo
x_data = [1, 2, 3, 4, 5]
y_data = [2, 1.8, -2, -4.6, 3.6]

# Obtener el polinomio de interpolación de Lagrange
polynomial = lagrange_interpolation(x_data, y_data)

# Imprimir el polinomio
print("Polinomio de Interpolación de Lagrange:")
print(polynomial)

# Evaluación del polinomio en un punto específico
x = 2.5
print(f"Valor de f({x}) según el polinomio de Lagrange: {polynomial(x)}")