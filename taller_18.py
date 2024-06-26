# -*- coding: utf-8 -*-
"""Taller_18.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EPojW9ZtwxTv4fA7jNSwMvwh_81O_smm
"""

import numpy as np
import matplotlib.pyplot as plt

def exponential_regression(x, y):
    # Transformar los datos
    x_transformed = x
    y_transformed = np.log(y)

    # Calcular la regresión lineal
    A = np.vstack([x_transformed, np.ones(len(x_transformed))]).T
    m, c = np.linalg.lstsq(A, y_transformed, rcond=None)[0]

    # Coeficientes del modelo exponencial
    a = np.exp(c)
    b = m

    return a, b

# Datos
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([1.6, 2.3, 3.4, 4.5, 6.4, 9])

# Calcular regresión exponencial
a, b = exponential_regression(x, y)

# Imprimir los coeficientes
print("Coeficiente a:", a)
print("Coeficiente b:", b)

# Graficar los datos y la línea de regresión
plt.scatter(x, y, label='Datos')
plt.plot(x, a * np.exp(b * x), color='red', label='Regresión Exponencial')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regresión Exponencial')
plt.legend()
plt.grid(True)
plt.show()