# Las triples comillas también pueden usarse, además de para docstring, para ser contenedores de texto multilínea
# que luego se visualizarán en consola (o donde sea) tal y como se escribieron
text = """
Principles of productivity:
    Managing your inflow.
    Systemizing everything that repeats.
"""

print(text)

# Con \ no se generan líneas nuevas. To-do en una línea, pero sirve para indicar que hay más texto que no ha cabido
# en una línea. Haría falta \n para saltar línea.
text = "\n \
Principles of productivity: \n\
    Managing your inflow. \n \
    Systemizing everything that repeats. \n \
"

print(text)