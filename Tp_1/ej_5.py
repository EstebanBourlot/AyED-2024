
romano = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def convert_romano_to_dec(numero_romano):
    if len(numero_romano) == 1:
        return romano[numero_romano]
    else:
        if romano[numero_romano[0]] >= romano[numero_romano[1]]:
            return romano[numero_romano[0]] + convert_romano_to_dec(numero_romano[1:])
        else:
            return - romano[numero_romano[0]] + convert_romano_to_dec(numero_romano[1:])

print()
numero = input("Ingresar un numero romano: ").upper()
print()
print("El numero corresponde a: (", convert_romano_to_dec(numero), ") en decimal.")
print()