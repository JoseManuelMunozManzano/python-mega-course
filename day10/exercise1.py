# Build a percentage calculator that gets from the user the "total value" and the "value" and returns
# the percentage as shown below:
#
# Enter total value: 50
# Enter value: 20
# That is 40.0%
#
# The program should also print a message if the user doesn't enter a number for the "total value or for the "value":
#
# Enter total value: 50
# Enter value: hi
# You need to enter a number. Run the program again
try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))

    percentage = value * 100 / total_value
    print(f"That is {percentage}%")

except ValueError:
    print("You need to enter a number. Run the program again.")
