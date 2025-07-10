import functions
import FreeSimpleGUI as gui

label = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip="Enter todo", key="todo")
add_button = gui.Button("Add")

list_box = gui.Listbox(values=functions.get_todos(), key="todo_list",
                       enable_events=True, size=(45, 10))
edit_button = gui.Button("Edit")

window = gui.Window("My To-Do App",
                    layout=[[label],
                            [input_box, add_button],
                            [list_box, edit_button]],
                    font=("Helvetica", 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values["todo"] + '\n')

            functions.write_todos(todos)
            window["todo_list"].update(todos)
        case "Edit":
            todo = values["todo_list"][0]
            new_todo = values["todo"]

            todos = functions.get_todos()

            todos[todos.index(todo)] = new_todo + "\n"

            functions.write_todos(todos)
            window["todo_list"].update(todos)
        case "todo_list":
            window['todo'].update(value=values["todo_list"][0])
        case gui.WIN_CLOSED:
            break
window.close()