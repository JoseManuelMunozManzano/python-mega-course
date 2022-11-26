# Create a function that gets two arguments, year_of_birth and current_year with current_year being a default argument.
# Please set its default value to whatever the current year is.
# On Day 15, you will learn how to get the current year automatically.
# For now, you can hardcode (i.e., type the actual year) it.
#
# Note: It is enough to define the function for this exercise -no need to call it.
def get_age(year_of_birth, current_year=2022):
    age = current_year - year_of_birth
    return age
