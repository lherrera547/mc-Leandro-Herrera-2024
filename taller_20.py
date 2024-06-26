# -*- coding: utf-8 -*-
"""Taller_20.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hCOB6t5wncNzbb50SWVK5ybJMOWimXQ4
"""

import numpy as np

# Datos de entrada
x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([0.1, 0.3, 0.9, 1.7, 2.8, 4.5, 6.9])

# Regresión lineal
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]

# Predicción
y_pred = m*x + c

# Desviación estándar (sy)
sy = np.std(y, ddof=1)

# Error estándar de la estimación (sxy)
sxy = np.sqrt(np.sum((y - y_pred)**2) / (len(x) - 2))

# Coeficiente de determinación (r2)
r2 = 1 - np.sum((y - y_pred)**2) / np.sum((y - np.mean(y))**2)

# Coeficiente de correlación (r)
r = np.corrcoef(x, y)[0, 1]

# Resultados
print("Desviación estándar (sy):", sy)
print("Error estándar de la estimación (sxy):", sxy)
print("Coeficiente de determinación (r2):", r2)
print("Coeficiente de correlación (r):", r)