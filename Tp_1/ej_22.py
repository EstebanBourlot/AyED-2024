from random import randint
from time import sleep
import sys

mochila = []

for i in range(15):
    mochila.append(randint(1, 50))

def usar_la_fuerza(objetos, sable_de_luz):
    if len(objetos) == 0:
        return -1
    elif objetos[-1] == sable_de_luz:
        return len(objetos)-2
    else:
        return usar_la_fuerza(objetos[0:-1], sable_de_luz)

def delay(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        sleep(0.5)

busqueda = usar_la_fuerza(mochila, 1)
print()
print("Obi-Wan esta en aprietos. Con la ayuda de la fuerza, debera buscar el sable de luz de su mochila")
print()
delay(". . .")
print()
print()
if busqueda == -1:
    print("Obi-Wan NO fue capaz de encontrar el sable de luz, ahora esta en serios problemas")
else:
    print("Obi-Wan fue capaz de encontrar el sable de luz luego de ", busqueda, " intentos fallidos")
print()