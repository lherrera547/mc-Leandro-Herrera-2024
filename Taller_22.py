import numpy as np
import matplotlib.pyplot as plt

# Datos proporcionados en la tabla
x1 = np.array([1, 1, 2, 3, 1, 2, 3, 3])
x2 = np.array([0, 1, 1, 2, 2, 3, 3, 1])
y = np.array([0.6, 2, 0.1, 0.3, 2.2, 2.3, 0.8, -1])

# Ajuste de la función lineal (y = mx + b)
A = np.vstack([x1, x2, np.ones(len(x1))]).T
m, n, c = np.linalg.lstsq(A, y, rcond=None)[0]

# Coeficientes de correlación (r)
y_pred = m * x1 + n * x2 + c
corr_matrix = np.corrcoef(y, y_pred)
r = corr_matrix[0, 1]

# Graficar los datos y la línea de regresión
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x1, x2, y, c='r', marker='o', label='Datos')
ax.plot(x1, x2, y_pred, c='b', label=f'Ajuste lineal: y = {m:.2f}x1 + {n:.2f}x2 + {c:.2f}\nCoeficiente de correlación (r): {r:.2f}')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')
plt.title('Ajuste lineal en 3D')
plt.legend()
plt.show()
