import PySimpleGUI as sg

label1 = sg.Text("Enter feet:")
input1 = sg.Input()

label2 = sg.Text("Enter inches: ")
input2 = sg.Input()

button_convert = sg.Button(button_text="Convert")

window = sg.Window("Convertor", layout=[[label1, input1], [label2, input2], [button_convert]])

window.read()
window.close()
