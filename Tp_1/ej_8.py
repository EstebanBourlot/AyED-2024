
def convert_to_binary(n):
    if n <= 1:
        return str(n)
    else:
        return convert_to_binary(n // 2) + str(n % 2)
    
print()
n = int(input("Ingresar un numero para calcular su equivalente en binario: "))
print()
print("En binario, su numero se escribe como: ", convert_to_binary(n))
print()
