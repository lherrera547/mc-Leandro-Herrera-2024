def main():
    # Solicitar al usuario el conjunto universal U
    u_size = int(input("Ingrese la cantidad de elementos del conjunto universal (U): "))
    universal_set = set()
    for i in range(u_size):
        element = float(input(f"Ingrese el elemento {i+1} del conjunto universal (U): "))
        universal_set.add(element)

    # Solicitar al usuario el conjunto A
    a_size = int(input("Ingrese la cantidad de elementos del conjunto A: "))
    set_a = set()
    for i in range(a_size):
        element = float(input(f"Ingrese el elemento {i+1} del conjunto A: "))
        set_a.add(element)

    # Verificar si A es subconjunto de U
    if set_a.issubset(universal_set):
        # Realizar las operaciones si A es subconjunto de U
        result1 = (universal_set.union(set_a)).intersection(set_a)
        result2 = (universal_set.intersection(set_a)).symmetric_difference(set_a)
        result3 = (universal_set.difference(set_a)).symmetric_difference(set_a)

        # Mostrar los resultados
        print(f"(U ⋃ A) ⋂ A = {result1}")
        print(f"U ⋂ A ⨁ A = {result2}")
        print(f"U - A ⨁ A = {result3}")

    else:
        print("El conjunto A no es un subconjunto del conjunto universal U.")


if __name__ == "__main__":
    main()
