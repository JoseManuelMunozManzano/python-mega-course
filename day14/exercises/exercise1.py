# Create a function that finds out the state of water (i.e., gas, liquid, solid) given the temperature.
# In other words, the function has a temperature parameter and returns either "Gas", "Liquid" or "Solid" as a
# string depending on the temperature.
# The function should be written in a separate file from the command line interface file.
# The output should look like in the screenshot below:
#
# Enter water temperature: -12
# Solid
#
# Let's run it one more time. Here is another example:
#
# Enter water temperature: 100
# Gas
#
# Note: To check if a value is between two values, you can use:
# elif 0 < x < 100:
import temperature_functions;

temperature = float(input("Enter water temperature: "))
print(temperature_functions.state_water(temperature))
