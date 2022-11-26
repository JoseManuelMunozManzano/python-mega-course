# Extend the program you wrote in exercise 2 by printing a message to the user instead of their age
# if their age is greater than 120.
# Feel free to print any message that you like.
def get_age(year_of_birth, current_year=2022):
    age = current_year - year_of_birth
    return age


year = int(input("What is your year of birth? "))
age = get_age(year)
if age > 120:
    print("You are a liar!!!!")
else:
    print(age)
