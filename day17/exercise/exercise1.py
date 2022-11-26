import PySimpleGUI as sg
from converters import to_meters

label1 = sg.Text("Enter feet:")
input1 = sg.Input(key='feet')

label2 = sg.Text("Enter inches: ")
input2 = sg.Input(key='inches')

button_convert = sg.Button(button_text="Convert")
output_label = sg.Text(key='output')

window = sg.Window("Convertor", layout=[[label1, input1], [label2, input2], [button_convert, output_label]])

while True:
    event, values = window.read()
    feet = float(values['feet'])
    inches = float(values['inches'])

    meters = to_meters(feet, inches)
    window['output'].update(value=f"{meters} m")

window.close()
