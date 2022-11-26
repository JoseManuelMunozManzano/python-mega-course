# Escribir en un fichero un string (no list)
file = open("bonus1File.txt", 'w')
file.write('Hey this is just text here and there. You can provide \n characters alike')
file.close()

# Lectura devolviendo lista
file = open('bonus1File.txt', 'r')
print(file.readlines())
file.close()

# Lectura devolviendo string. Si no se ha hecho close() antes, el cursor se ha posicionado tras la última línea
# y ya no hay nada que leer.
file = open('bonus1File.txt', 'r')
print(file.read())
file.close()
