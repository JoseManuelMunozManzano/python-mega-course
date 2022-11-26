import functions

# Uso de librerías de terceros
# Una lista completa de librerías de terceros puede encontrarse en:
# https://pypi.org/
# https://pypi.org/project/PySimpleGUI/
# Para instalar paquetes en IntelliJ IDEA, ir a Tools > Manage Python Packages, buscarlo e instalarlo
# Otra forma de instalar paquetes es usando la terminal. En este caso hay que escribir: pip install PySimpleGUI
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()
