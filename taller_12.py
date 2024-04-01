import math

def funcion_1(x):
    return 1.2 * x**4 - 2.1 * x**3 + 0.8 * x**2 - 3 * x + 5

def funcion_2(x):
    return math.cos(x) * math.log(2 * x)


def calcular_error_resultante(funcion, x, delta_x):
    
    f_x = funcion(x)
    
    f_x_mas_delta = funcion(x + delta_x)
    
    error_resultante = abs((f_x_mas_delta - f_x) / delta_x)
    
    return error_resultante

def main():
    x_1 = 1.3
    delta_x_1 = 0.05
    error_resultante_1 = calcular_error_resultante(funcion_1, x_1, delta_x_1)
    print("Error resultante en la primera función:", error_resultante_1)
    
    x_2 = math.pi * math.e**4
    delta_x_2 = 0.005
    error_resultante_2 = calcular_error_resultante(funcion_2, x_2, delta_x_2)
    print("Error resultante en la segunda función:", error_resultante_2)

if __name__ == "__main__":
    main()
