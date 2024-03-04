
def division_sucesiva_base10_a_base16(numero):
    if numero == 0:
        return '0'

    resultado = ''
    while numero > 0:
        residuo = numero % 16
        if residuo < 10:
            resultado = str(residuo) + resultado
        else:
            resultado = chr(ord('A') + residuo - 10) + resultado
        numero //= 16

    return resultado

numero_base_10 = int(input("Ingrese un número en base 10: "))

print("El número", numero_base_10, "en base 16 es:", division_sucesiva_base10_a_base16(numero_base_10))

def desarollo_de_tarea():
    print("Desarollo de la tarea")
    print("Conversion de base 10 a base 16:")
    print("611 en base 16:", division_sucesiva_base10_a_base16(611))
    print("48 en base 16:", division_sucesiva_base10_a_base16(48))
    print("5000 en base 16:", division_sucesiva_base10_a_base16(5000))
    print("6199 en base 16:", division_sucesiva_base10_a_base16(6199)) 

desarollo_de_tarea()

