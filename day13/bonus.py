feet_inches = input("Enter feet and inches: ")

# Decoupling functions
# La función convert() hace dos cosas.
# Hace el parseo del string Y luego convierte a metros.
# Sin embargo, el nombre de la función es convertir (no parsear)
# Las funciones SOLO deben hacer UNA cosa.
# La solución es DESACOPLAR.
# Para ello se crea la función parse.
#
# def convert(feet_inches):
#     parts = feet_inches.split(" ")
#     feet = float(parts[0])
#     inches = float(parts[1])
#
#     meters = feet * 0.3048 + inches * 0.0254
#     return meters


def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")
