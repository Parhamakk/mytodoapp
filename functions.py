FILEPATH = r'C:\Users\98902\Desktop\PYTHON\todos.txt'


def get_todos(file_path=FILEPATH):
    with open(file_path, 'r') as file:
        todos_local = file.readlines()
        return todos_local


def write_todos(todos_arg, file_path=FILEPATH):
    with open(file_path, 'w') as file:
        file.writelines(todos_arg)
