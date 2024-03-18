import math

# Define la función para calcular el seno usando la expansión en serie
def expansion_seno(x, tolerancia=1e-8):
    termino = x  # El primer término en la serie es x
    suma = x  # Inicializa la suma con el primer término
    n = 1  # Contador para el número de términos

    while True:
        termino = -1 * x * x / ((2 * n) * (2 * n + 1))  # Calcula cada término de forma iterativa
        suma += termino  # Agrega el nuevo término a la suma
        n += 1  # Incrementa el contador de términos
        
        # Si el valor absoluto del término actual es menor que la tolerancia, rompe el bucle
        if abs(termino) < tolerancia:
            break
    
    # Calcula el seno real para el análisis del error
    seno_real = math.sin(x)
    # Error absoluto aproximado
    error = abs(seno_real - suma)
    # Porcentaje de error relativo
    error_relativo = (error / abs(seno_real)) * 100 if seno_real != 0 else 0

    return suma, error, error_relativo, n

# Dado que no puedo solicitar la entrada al usuario, dejaré un marcador donde se solicitaría la entrada
x_input = float(input("Ingrese el valor en radianes: ")) 
x_input = math.pi / 6  # Este es un marcador de posición para la entrada del usuario (por ejemplo, el valor para 30 grados en radianes)
expansion_seno(x_input)
