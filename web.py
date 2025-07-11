import streamlit as st
import functions

todo_list = functions.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todo_list.append(new_todo)
    functions.write_todos(todo_list)

st.title("Todo App")
st.subheader("Enter your todos below...")
st.write("Increase your productivity with this app!")

for i,todo in enumerate(todo_list):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todo_list.pop(i)
        functions.write_todos(todo_list)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo", placeholder="What do you need to do...?",
              on_change=add_todo, key="new_todo")