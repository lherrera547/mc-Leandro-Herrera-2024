import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, CubicSpline

# Datos de la tabla
x_data = np.array([1, 2, 3, 4, 5, 6, 7])
y_data = np.array([1, 5, 4, 4, -2, 2, 9])

# Puntos a interpolar
x_interp = 3.55

# Interpolación de Lagrange
poly_lagrange = lagrange(x_data, y_data)

# Interpolación de trazadores cúbicos
spline = CubicSpline(x_data, y_data)

# Evaluación de f(x) en x_interp
y_interp_lagrange = poly_lagrange(x_interp)
y_interp_spline = spline(x_interp)

# Gráficas
x_range = np.linspace(min(x_data), max(x_data), 1000)
plt.figure(figsize=(10, 6))

# Datos originales
plt.plot(x_data, y_data, 'ro', label='Datos Originales')

# Polinomio de Lagrange
plt.plot(x_range, poly_lagrange(x_range), label='Polinomio de Lagrange')

# Trazadores cúbicos
plt.plot(x_range, spline(x_range), label='Trazadores Cúbicos')

# Puntos interpolados
plt.plot(x_interp, y_interp_lagrange, 'bo', label=f'Lagrange en {x_interp:.2f}: {y_interp_lagrange:.2f}')
plt.plot(x_interp, y_interp_spline, 'go', label=f'Trazadores Cúbicos en {x_interp:.2f}: {y_interp_spline:.2f}')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolación de Lagrange y Trazadores Cúbicos')
plt.legend()
plt.grid(True)
plt.show()

print(f"Valor estimado de f(3.55) con Lagrange: {y_interp_lagrange:.2f}")
print(f"Valor estimado de f(3.55) con Trazadores Cúbicos: {y_interp_spline:.2f}")
