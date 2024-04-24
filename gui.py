import functions
import time
import PySimpleGUI as sg

sg.theme("GreenMono")
clock = sg.Text("", key="clock")
label = sg.Text("Hello type in a todo: ")
input_box = sg.InputText(tooltip="Enter a ToDo", key='todo')

listbox = sg.Listbox(values=functions.get_todos(), key='items',
                     enable_events=True, size=(45, 10))


# Buttons
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
comp_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# Window
# layout = [[label, input_box, add_button], [listbox, edit_button]]
window = sg.Window("My ToDo app",
                   layout=[[clock],
                           [label, input_box, add_button],
                           [listbox, edit_button, comp_button],
                           [exit_button]],
                   font=("Roboto", 12))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%A - %B %d, %Y - %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['items'].update(values=todos)

        case "Edit":
            try:
                todo_edit = values['items'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['items'].update(values=todos)
            except IndexError:
                sg.popup("Select an item first!", font=("Roboto", 12))

        case "Complete":
            try:
                todo_complete = values['items'][0]
                todos = functions.get_todos()
                todos.remove(todo_complete)
                functions.write_todos(todos)
                window['items'].update(values=todos)
                window['todo'].update(value='')
                sg.popup("Task completed!!", font=("Roboto", 12))
            except IndexError:
                sg.popup("Select an item first!", font=("Roboto", 12))

        case "Exit":
            #sg.popup("Exiting program,Bye!", font=("Roboto", 12))
            break

        case 'items':
            window['todo'].update(value=values['items'][0])

        case sg.WINDOW_CLOSED:
            break


window.close()
