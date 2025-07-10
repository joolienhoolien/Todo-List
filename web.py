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

for todo in todo_list:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter a todo",
              on_change=add_todo, key="new_todo")

st.session_state