print("hi" * 10)

print(float("10"))
print(int('10'))
print(str(10))

# Cada uno de estos elementos en un objeto
myList = ['a', 'b', 'c']
print(type(myList))

# Obtener el indice de un elemento usando su valor
print(myList.index('b'))

# Los métodos con doble guion bajo los usa Python internamente. No es necesario que los usemos
myList.__setitem__(1, 'd')          # Igual a myList[1] = 'd'   Este es el que hay que usar
print(myList)

print(myList.__getitem__(2))        # Equivalente a myList[2]   De nuevo, este es el que hay que usar
