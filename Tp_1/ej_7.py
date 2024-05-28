
def serie(n):
    if n == 1:
        return 1
    else:
        return 1/n + serie(n-1)

print()
n = int(input("Escribir un numero para calcular la sumatoria de su serie de forma ( 1 + ... + 1/n ): "))
print()
print("La sumatoria da como resultado: ", serie(n))
print()