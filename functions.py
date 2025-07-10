FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read the supplied file and return a list of the todos"""
    with open(filepath, "r") as file_local:
        todos = file_local.readlines()
    return todos


def write_todos(todos, filepath=FILEPATH):
    """Write the supplied list to the supplied file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos)

