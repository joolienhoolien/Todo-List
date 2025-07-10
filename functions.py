def get_todos(filepath="todos.txt"):
    """Read the supplied file and return a list of the todos"""
    with open(filepath, "r") as file_local:
        todos = file_local.readlines()
    return todos


def write_todos(todos, filepath="todos.txt"):
    """Write the supplied list to the supplied file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos)

