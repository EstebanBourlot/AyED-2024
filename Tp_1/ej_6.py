
def invertir_cadena(cadena):
    if len(cadena) == 0:
        return cadena
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])

print()
cadena = input("Ingresar la cadena que desea invertir: ")
print()
print(invertir_cadena(cadena))
print()