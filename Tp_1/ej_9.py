
total = 0
equalizador = 1
i = 0

def logarithm(base, total, equalizador, i):
    if base ** total == n:
        return total
    elif ((base ** total > n) and (base >= 1)) or ((base ** total > n) and (base < 0)):
        i = 1
        return logarithm(base, total-equalizador, equalizador, i)
    else:
        if i == 1:
            equalizador = equalizador/10
            i = 0
        return logarithm(base, total+equalizador, equalizador, i)

print()
base = float(input("Ingresar la base de un logaritmo: "))
print()
n = float(input("Ingresar el logaritmo a calcular: "))
print()
if (n <= 0) or (base <= 0):
    print("El numero ingresado no se encuentra en el dominio de un logaritmo")
else:
    print("El resultado del logaritmo es:", logarithm(base, total, equalizador, i))
print()