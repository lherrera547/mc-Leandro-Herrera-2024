import math

def aproximacion(x, n):
    aproximacion = 0
    for i in range(n + 1):
        termino_i = ((-1) ** i * x ** i) / math.factorial(i)
        aproximacion += termino_i
    return aproximacion

def main():
    x_base = 0.5
    x_objetivo = 0.505
    valor_real = math.exp(-x_objetivo)
    
    print("Valor real de e^-0.505:", valor_real)
    
    print("\nOrden\tAproximación\t\tError Relativo (%)")
    
    for i in range(16):
        aproximacion = aproximacion(x_objetivo - x_base, i)
        error_relativo = abs((valor_real - aproximacion) / valor_real) * 100
        print(f"{i}\t{aproximacion}\t{error_relativo:.10f}%")

if __name__ == "__main__":
    main()
