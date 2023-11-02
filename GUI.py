import functions
import PySimpleGUI as sg
# window is an instance that stored in the var named window
label = sg.Text("Type in To-Do")
input_box = sg.InputText(tooltip="Enter to-do")
add_button = sg.Button("Add")
window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
# read displays the window
window.read()
window.close()
