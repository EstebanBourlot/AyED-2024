
def suma(num1):
    if num1 == 0:
        return 0
    else:
        return num1 + suma(num1-1)

print()    
num = int(input("Escriba el numero para calcular su suma: "))
print()
print("La suma resultante es:", suma(num))
print()