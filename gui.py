import functions
import PySimpleGUI as sg

label = sg.Text("Hello type in a todo: ")
input_box = sg.InputText(tooltip="Enter a ToDo", key='todo')

# Buttons
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
comp_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# Window
window = sg.Window("My ToDo app",
                   layout=[[label, input_box, add_button]],
                   font=("Helvetica", 12))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break


window.close()
