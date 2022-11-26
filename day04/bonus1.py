# Data mutability

# Recordar que las listas son mutables
# Si queremos que sean inmutables hay que usar una tupla, que es la versión inmutable de una list
filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename in filenames:
    # Pero esto falla porque los str son inmutables. No pueden cambiar
    # filename[1] = '-'
    # Hay que crear un nuevo string. replace() devuelve un nuevo string
    filenames[filenames.index(filename)] = filename.replace('.', '-', 1)

print(filenames)

# Tupla
# Se crean como las listas, pero usando paréntesis en vez de corchetes
filenames = ("1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt")
print(type(filenames))

print(filenames[1])

# Esto falla porque la tupla es inmutable
# filenames[1] = "Something new"
# filenames.append("new")
