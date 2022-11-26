# Create a script that asks the user to enter a password.
# Then create a function that checks the strength of the user password.
# The function should return Strong Password if all of the following conditions are true:
# Eight or more characters
# At least one uppercase letter.
# At least one digit.
#
# Here is what happens when the user provides a password that satisfies all three conditions:
# Enter new password: hello123HI
# Strong Password
#
# And if the user enters a password that breaks one of the three conditions, the program returns Weak Password:
# Enter new password: hello
# Weak Password

def is_strength_password(password):
    result = {}

    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    for i in password:
        if i.isdigit():
            digit = True
            break

    result["digits"] = digit

    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True
            break

    result["upper-case"] = uppercase

    return all(result.values())


passwrd = input("Enter new password: ")
is_strength = is_strength_password(passwrd)

if is_strength:
    print("Strong Password")
else:
    print("Weak Password")