# Path absolutos cuando el file está fuera de la carpeta del proyecto

# En Windows se indica la r (raw string) para que no escape, en este caso, el \t
# Ignora los caracteres especiales
# file = open(r"C:\Users\jmmunoz\Downloads\todos.txt", 'r')

# En Mac y Linux
file = open("/Volumes/Coder/Python/Udemy-ThePythonMegaCourse-Ardit/00-Projects/day06/files/todos.txt", "r")
todos = file.readlines()
print(todos)
