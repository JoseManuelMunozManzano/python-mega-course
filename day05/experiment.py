myList = ['clean the keyboard', 'throw the monitor', 'Buy grocery']

for index, item in enumerate(myList):
    row = f"{index + 1}-{item}"
    print(row)

# index y item quedan con los últimos valores antes de salir del bucle
print("Hello", index, item)

# index sirve también para calcular la longitud de la lista
print(f"Length is {index + 1}")

# Es más fácil obtener la longitud con este método
print(len(myList))

# enumerate puede usarse en str
for i, j in enumerate("Hello"):
    print(i, j)

# Cual es la salida de la función enumerate()? Un objeto enumerate
a = enumerate(myList)
print(a)

# Representación del objeto enumerate usando list
# [(0, 'clean the keyboard'), (1, 'throw the monitor'), (2, 'Buy grocery')]
# Es la construcción interna del objeto a
# Es una lista hecha de tuplas
print(list(a))
