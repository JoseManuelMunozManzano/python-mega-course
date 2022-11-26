# Para obtener una lista de las funciones disponibles
import builtins

# Los métodos que nos interesan son los que no tienen los dobles _ (al final)
print(dir(str))

# Para saber que hace el método
print(help(str.capitalize))

a = [1, 2, 3]
print(dir(a))
# append(object, /)
# El / indica el fin de los argumentos que hay que indicar en el método
print(help([].append))

# Lista de funciones disponibles
print(dir(builtins))
