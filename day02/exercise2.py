# Create a program that asks the user for their name once.
# Then, the program prints out the name repeatedly with the first letter capitalized.
name = input("Name: ")
capitalized_name = name.capitalize()
while True:
    print(capitalized_name)
