import functions
import FreeSimpleGUI as gui
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

gui.theme('DarkTeal2')
clock = gui.Text("", key='clock')
label = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip="Enter todo", key="todo")
add_button = gui.Button("Add")

list_box = gui.Listbox(values=functions.get_todos(), key="todo_list",
                       enable_events=True, size=(45, 10))
edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete")
exit_button = gui.Button("Exit")

window = gui.Window("My To-Do App",
                    layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=("Helvetica", 20))
while True:
    event, values = window.read(timeout=250)
    window['clock'].update(value=time.strftime('%H:%M:%S, %m/%d/%Y'))
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values["todo"] + '\n')

            functions.write_todos(todos)
            window["todo_list"].update(values=todos)
        case "Edit":
            try:
                todo = values["todo_list"][0]
                new_todo = values["todo"]

                todos = functions.get_todos()

                todos[todos.index(todo)] = new_todo

                functions.write_todos(todos)
                window["todo_list"].update(values=todos)
            except IndexError:
                gui.popup("please select an item first", font=("Helvetica", 20))
        case "Complete":
            try:
                todo = values["todo_list"][0]
                todo_list = functions.get_todos()
                todo_list.remove(todo)
                functions.write_todos(todo_list)
                window["todo_list"].update(values=todo_list)
                window['todo'].update(value="")
            except IndexError:
                gui.popup("please select an item first", font=("Helvetica", 20))
        case "todo_list":
            window['todo'].update(value=values["todo_list"][0])
        case "Exit":
            break
        case gui.WIN_CLOSED:
            break
window.close()