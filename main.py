#Ask for input from user
todo_list = []

while True:
    user_action = input("Type 'add', 'show', 'edit', or 'exit':")

    match user_action.strip():
        case "add":
            user_action = input("Enter a todo:")
            todo_list.append(user_action)
        case "show":
            for i, todo in enumerate(todo_list):
                print(i + 1, "-", todo)
        case "edit":
            index = int(input("Which todo do you want to edit?"))
            index -= 1
            to_edit = todo_list[index]
            todo_list[index] = input("Input new todo:")
        case "exit":
            break
        case _:
            print("Invalid input")
print("Bye.")
