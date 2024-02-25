def main():
    # Solicitar al usuario los dos conjuntos
    conjunto1 = set(map(float, input("Ingrese los números del primer conjunto separados por espacios: ").split()))
    conjunto2 = set(map(float, input("Ingrese los números del segundo conjunto separados por espacios: ").split()))

    # Solicitar la operación al usuario
    operacion = input("Ingrese la operación que desea realizar (unión, intersección, diferencia, diferencia simétrica): ").strip().lower()

    # Realizar la operación seleccionada y mostrar el resultado
    if operacion == "unión":
        resultado = conjunto1.union(conjunto2)
    elif operacion == "intersección":
        resultado = conjunto1.intersection(conjunto2)
    elif operacion == "diferencia":
        resultado = conjunto1.difference(conjunto2)
    elif operacion == "diferencia simétrica":
        resultado = conjunto1.symmetric_difference(conjunto2)
    else:
        print("Operación no válida")
        return

    # Mostrar el conjunto resultante y su cardinalidad
    print(f"El conjunto resultante es: {resultado}")
    print(f"La cardinalidad del conjunto resultante es: {len(resultado)}")


if __name__ == "__main__":
    main()
