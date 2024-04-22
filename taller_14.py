# -*- coding: utf-8 -*-
"""Taller_14.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ooRAZacZmcSmZsXBq4nuCMr-Ar2SbaVw
"""

def producto_escalar(vector1, vector2):
    if len(vector1) != len(vector2):
        return "Los vectores deben tener la misma longitud."

    producto = sum(x * y for x, y in zip(vector1, vector2))
    return producto

def main_producto_escalar():
    longitud = int(input("Ingrese la longitud de los vectores: "))
    vector1 = [float(input(f"Ingrese el elemento {i + 1} del primer vector: ")) for i in range(longitud)]
    vector2 = [float(input(f"Ingrese el elemento {i + 1} del segundo vector: ")) for i in range(longitud)]

    resultado = producto_escalar(vector1, vector2)
    print(f"El producto escalar de los dos vectores es: {resultado}")

if __name__ == "__main__":
    main_producto_escalar()


def operaciones_matrices(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return "Las matrices deben tener las mismas dimensiones."

    tres_A = [[3 * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    cuatro_B = [[4 * B[i][j] for j in range(len(B[0]))] for i in range(len(B))]
    suma_AB = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    try:
        producto_BxA = [[sum(A[i][k] * B[k][j] for k in range(len(A[0]))) for j in range(len(B[0]))] for i in range(len(A))]
    except IndexError:
        return "No se puede calcular el producto B × A, las dimensiones no son compatibles."

    return tres_A, cuatro_B, suma_AB, producto_BxA

def main_matrices():
    filas_A = int(input("Ingrese el número de filas de la matriz A: "))
    columnas_A = int(input("Ingrese el número de columnas de la matriz A: "))
    A = [[float(input(f"Ingrese el elemento ({i + 1},{j + 1}) de la matriz A: ")) for j in range(columnas_A)] for i in range(filas_A)]

    filas_B = int(input("Ingrese el número de filas de la matriz B: "))
    columnas_B = int(input("Ingrese el número de columnas de la matriz B: "))
    B = [[float(input(f"Ingrese el elemento ({i + 1},{j + 1}) de la matriz B: ")) for j in range(columnas_B)] for i in range(filas_B)]

    resultados = operaciones_matrices(A, B)
    if isinstance(resultados, str):
        print(resultados)
    else:
        tres_A, cuatro_B, suma_AB, producto_BxA = resultados
        print("3A:")
        for row in tres_A:
            print(row)
        print("4B:")
        for row in cuatro_B:
            print(row)
        print("A + B:")
        for row in suma_AB:
            print(row)
        print("B × A:")
        for row in producto_BxA:
            print(row)

if __name__ == "__main__":
    main_matrices()