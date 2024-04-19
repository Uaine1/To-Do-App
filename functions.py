FILEPATH = 'todos.txt'
def get_todos(filepath=FILEPATH):
    ''' Return a text file and return the list of to-do
    items.
    '''
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    ''' Store/write information from the user to text file.
    '''
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


'''def get_help():
    print("For add command - Example: add clean the house")
    print("For show command - it will just show your pending works")
    print("For edit command - Example: edit 1")
    print("For complete command - Example: complete 1")
    print("exit command is exit command dumbass")'''
