# Extend the code below so the code prints out the sum of the numbers.
# The output of your code should be as below:
# 49.1
# Hint: Use the sum() function. The function gets a list of numbers as input and produces the sum of all the numbers.
user_entries = ['10', '19.1', '20']

total_user_numbers = sum([float(value) for value in user_entries])

print(total_user_numbers)
