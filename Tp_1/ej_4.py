
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente-1)
    
print()
num1 = int(input("Escribir un numero base: "))
print()
num2 = int(input("Ahora ingresar exponente: "))
print()
print("La potencia resultante es: ", potencia(num1, num2))
print()