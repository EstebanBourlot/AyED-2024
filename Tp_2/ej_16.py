from pila import Stack

the_empire_strikes_back = Stack()
the_force_awakens = Stack()
aux_stack = Stack()
intersection = Stack()

the_empire_strikes_back_list = ['Darth_Vader', 'Luke_Skywalker', 'Boba_Fett', 'Han_Solo', 'Obi-Wan_Kenobi', 'Leia_Organa', 'Yoda', 'Chewbacca', 'Palpatine', 'C-3PO', 'R2-D2']
the_force_awakens_list = ['Kylo_Ren', 'Rey', 'Luke_Skywalker', 'Han_Solo', 'Leia_Organa', 'Obi-Wan_Kenobi', 'Chewbacca', 'BB-8', 'Yoda', 'R2-D2', 'C-3PO', 'Snoke']

for character in the_empire_strikes_back_list:
    the_empire_strikes_back.push(character)

for character in the_force_awakens_list:
    the_force_awakens.push(character)

while the_empire_strikes_back.size() > 0:
    auxV = the_empire_strikes_back.pop()
    while the_force_awakens.size() > 0:
        auxVII = the_force_awakens.pop()
        aux_stack.push(auxVII)
        if auxV == auxVII:
            intersection.push(auxVII)
    while aux_stack.size() > 0:
        the_force_awakens.push(aux_stack.pop())

print()
print("Los personajes que aparecen en ambos son: ")
print()

while intersection.size() > 0:
    print(intersection.pop())

print()