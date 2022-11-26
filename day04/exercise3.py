# We have this list:
# ranking = ['John', 'Sen', 'Marry']
# You need to create a program that lets the user enter the person's name,
# and the program returns the rank that person got.

ranking = ['John', 'Sen', 'Marry']

name = input("Enter a name: ")
print(ranking.index(name) + 1)
