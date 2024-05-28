from pila import Stack

c = 1

class character_class():

    def __init__(self, name, appearance):
        self.__name = name
        self.__appearance = appearance
    
    def get_name(self):
        return self.__name
    
    def get_appearance(self):
        return self.__appearance
    
    def __str__(self):
        return '{self.__name} - {self.__appearance)'
    
participations = [
    character_class('Rocket Raccoon', 6),
    character_class('Iron Man', 9),
    character_class('Hulk', 6),
    character_class('Groot', 6),
    character_class('Thanos', 3),
    character_class('Wong', 6),
    character_class('Black Widow', 8),
]

character_stack = Stack()
for participation in participations:
    character_stack.push(participation)

while character_stack.size() > 0:
    data = character_stack.pop()
    if data.get_name() == 'Groot':
        print()
        print('Groot esta en la posicion', c) #! a)
    if data.get_name() == 'Rocket Raccoon':
        print()
        print('Rocket esta en la posicion', c) #! a)
    if data.get_appearance() > 5:
        print()
        print(data.get_name(), 'aparece mas de 5 veces (', data.get_appearance(), ')') #! b)
    if data.get_name()[0].upper() == 'C':
        print()
        print(data.get_name(), 'empieza con C') #! d)
    if data.get_name()[0].upper() == 'D':
        print()
        print(data.get_name(), 'empieza con D') #! d)
    if data.get_name()[0].upper() == 'G':
        print()
        print(data.get_name(), 'empieza con G') #! d)
    c += 1

print()
print('La viuda negra tiene', data.get_appearance(), 'apariciones') #! c)
print()