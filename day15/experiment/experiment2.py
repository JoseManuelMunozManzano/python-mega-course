# Modulos starndard importantes:
# csv - Write and read tabular data to and from delimited files.

import csv

with open("weather.csv", "r") as file:
    data = list(csv.reader(file))

city = input("Enter a city: ").strip().title()

# Quitamos la cabecera con [1:]
for row in data[1:]:
    if row[0] == city:
        print(row[1])
