# Modulos starndard importantes:
# glob - Unix shell style pathname pattern expansion.

# Obtener una lista de paths de ficheros que satisfacen un patrón
import glob

myfiles = glob.glob("experiment/files/*.txt")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())
