
def producto(num1, num2):
    if num2 == 1:
        return num1
    else:
        return num1 + producto(num1, num2-1)

print()
num1 = int(input("Escribir un primer numero para multiplicar: "))
print()
num2 = int(input("Ahora tiene que escribir un segundo numero: "))
print()
print("El producto resultante es: ", producto(num1, num2))
print()