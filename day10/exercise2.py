# As you might know, it is not mathematically possible to divide a number by zero.
# Consequently, this is also not possible in Python either -you will get a ZeroDivisionError.
# With that in mind, your task for this exercise is to extend the program you created in Exercise 1
# by displaying a message to the user when they enter 0 for the "total value".
#
# Enter total value: 0
# Enter value: 20
# Your total value cannot be zero
try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))

    percentage = value * 100 / total_value
    print(f"That is {percentage}%")

except ZeroDivisionError:
    print("Your total value cannot be zero.")
except ValueError:
    print("You need to enter a number. Run the program again.")
