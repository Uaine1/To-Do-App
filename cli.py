#from functions import get_todos, write_todos, get_help, title_bar
import functions # A local module/self made module
import time # A standard module

datetoday = time.strftime("%A - %B %d, %Y - %H:%M:%S")

print("Its,", datetoday)
print("Available commands - add, show, edit, complete or exit....... ")

while True:
    user_action = input("Type in a command: ")
    user_action = user_action.strip()

# Checks the typed in commands
    # Add command
    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    # Show command
    elif user_action.startswith('show'):
        print("Pending works", )

        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            show_row = f"{index +1}.{item.capitalize()}"
            print(show_row)

    # Edit command
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new ToDo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Invalid command please try again....")
            continue

    # Complete command
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            prompt = f"Todo {todo_to_remove.capitalize()} was completed... "
            print(prompt)

        except IndexError:
            print("There is no ToDo with that number....")
            continue

    # Exit command
    elif user_action.startswith('exit'):
        break

    else:
        print("Invalid command")

print("Goodbye see you again!!")
