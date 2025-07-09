def get_todos(filepath="todos.txt"):
    with open(filepath, "r") as file_local:
        todos = file_local.readlines()
    return todos


def write_todos(todos, filepath="todos.txt"):
    with open(filepath, "w") as file_local:
        file_local.writelines(todos)

while True:
    user_action = input("Type 'add', 'show', 'edit', 'complete' or 'exit' -> ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo_list = get_todos()

        todo = user_action[4:] + "\n"
        todo_list.append(todo)
        write_todos(todo_list)

    elif user_action.startswith("show"):
        todo_list = get_todos()

        for i, todo in enumerate(todo_list):
            print(f"{i+1}-{todo.strip('\n')}")

    elif user_action.startswith("edit"):
        try:
            index = int(user_action[5:])
            index -= 1
            todo_list = get_todos()

            todo_list[index] = input("Input new todo:") + "\n"
            write_todos(todo_list)
        except ValueError:
            print("Invalid command...")
            continue
    elif user_action.startswith("complete"):
        try:
            index = int(user_action[9:])
            index -= 1
            todo_list = get_todos()

            removed = todo_list.pop(index).strip("\n")

            write_todos(todo_list)
            message = f"Todo \"{removed}\" has been removed."
            print(message)
        except IndexError:
            print("Index out of range...")
            continue
    elif user_action.startswith("exit"):
        break

    else:
        print("Invalid input")
print("Bye...")
