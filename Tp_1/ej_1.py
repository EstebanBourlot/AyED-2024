
def fibonacci(n):
    if (n==0 or n==1):
        return n
    else:
        return fibonacci(n-1)+ fibonacci(n-2)

print()
base = int(input("Ingrese un numero para calcular su fibonacci: "))
print()
print("El numero ingresado corresponde a: (", fibonacci(base), ") en la sucesion fibonacci.")
print()