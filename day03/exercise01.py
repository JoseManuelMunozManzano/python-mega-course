# Write a program that asks the user to enter the country they are from.
# If the user enters USA, the program prints out Hello.
# If the user enters the word India, the program prints out Namaste.
# If the user enters the word Germany, the program prints out Hallo.
#
# Note: Strings are case-sensitive in Python, meaning "germany" and "Germany" are treated as two different strings.
# So, please keep that in mind when writing the program.

while True:
    userCountry = input("What's your country? (or exit): ").strip().capitalize()

    match userCountry:
        case "Usa":
            print("Hello")
        case "India":
            print("Namaste")
        case "Germany":
            print("Hallo")
        case "Exit":
            break
