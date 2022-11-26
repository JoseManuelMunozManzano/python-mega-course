# Your task for this exercise is to use the function you created in exercise 1.
# Then, below the function definition, get the year of birth from the user using an input function and then call
# and print the defined function to get the user's age as output.
# Here is how the program should behave:
#
# What is your year of birth? 1902
# 121
def get_age(year_of_birth, current_year=2022):
    age = current_year - year_of_birth
    return age


year = int(input("What is your year of birth? "))
age = get_age(year)
print(age)
